(() => {
  const state = { query: "", field: "全部", era: "all", topic: "全部", sort: "year-asc", source: "all" };
  const el = id => document.getElementById(id);
  const cards = el("cards");
  const dialog = el("detail-dialog");

  function escapeHtml(value) {
    return String(value).replace(/[&<>"]/g, char => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[char]));
  }

  function fieldStyle(field) {
    return `--field-color:${FIELD_META[field].color}`;
  }

  function renderFilters() {
    const counts = PHYSICS_DATA.reduce((acc, item) => ((acc[item.field] = (acc[item.field] || 0) + 1), acc), {});
    const options = ["全部", ...Object.keys(FIELD_META)];
    el("field-filters").innerHTML = options.map(field => {
      const color = field === "全部" ? "#eef5ff" : FIELD_META[field].color;
      const count = field === "全部" ? PHYSICS_DATA.length : counts[field];
      return `<button class="field-chip ${field === state.field ? "active" : ""}" data-field="${escapeHtml(field)}" style="--field-color:${color}" type="button"><span><i></i>${escapeHtml(field)}</span><b>${count}</b></button>`;
    }).join("");

    el("era-filters").innerHTML = `<button class="era-btn active" data-era="all" type="button">全部</button>` + ERAS.map(era => `<button class="era-btn" data-era="${era.id}" type="button">${era.label}</button>`).join("");
    renderTopicOptions();
  }

  function renderTopicOptions() {
    const available = PHYSICS_DATA.filter(item => state.field === "全部" || item.field === state.field);
    const topics = [...new Set(available.map(item => item.topic))].sort((a, b) => a.localeCompare(b, "zh-CN"));
    if (state.topic !== "全部" && !topics.includes(state.topic)) state.topic = "全部";
    el("topic-filter").innerHTML = `<option value="全部">全部主题</option>` + topics.map(topic => `<option value="${escapeHtml(topic)}">${escapeHtml(topic)}</option>`).join("");
    el("topic-filter").value = state.topic;
  }

  function renderTimeline() {
    el("timeline").innerHTML = TIMELINE_MILESTONES.map(item => `<div class="time-segment" style="--seg-color:${item.color}"><time>${item.year}</time><strong>${item.title}</strong><span>${item.subtitle}</span></div>`).join("");
  }

  function renderEpochBars() {
    const buckets = ["古代", "16C", "17C", "18C", "19C", "1900s", "1910s", "1920s", "1930s", "1940s", "1950–69", "1970+"].map(label => ({ label, count: 0 }));
    PHYSICS_DATA.forEach(item => {
      let i = item.year < 1500 ? 0 : item.year < 1600 ? 1 : item.year < 1700 ? 2 : item.year < 1800 ? 3 : item.year < 1900 ? 4 : item.year < 1910 ? 5 : item.year < 1920 ? 6 : item.year < 1930 ? 7 : item.year < 1940 ? 8 : item.year < 1950 ? 9 : item.year < 1970 ? 10 : 11;
      buckets[i].count += 1;
    });
    const max = Math.max(...buckets.map(b => b.count));
    el("epoch-bars").innerHTML = buckets.map(b => `<i class="epoch-bar" style="--h:${Math.max(8, b.count / max * 100)}" data-label="${b.label} · ${b.count}项" aria-label="${b.label} ${b.count}项"></i>`).join("");
  }

  function normalized(text) {
    return String(text).toLowerCase().replace(/[\s·—–-]/g, "");
  }

  function getResults() {
    const q = normalized(state.query);
    const era = ERAS.find(item => item.id === state.era);
    const result = PHYSICS_DATA.filter(item => {
      const searchable = normalized([item.id, item.kind, item.title, item.people, item.field, item.topic, item.formula, item.summary, item.application, item.significance, item.context, item.conditions, item.variables, item.date].join(" "));
      return (state.source === "all" || (state.source === "sourced" ? item.sources.length > 0 : item.sources.length === 0)) && (!q || searchable.includes(q)) && (state.field === "全部" || item.field === state.field) && (state.topic === "全部" || item.topic === state.topic) && (!era || era.test(item.year));
    });
    return result.sort((a, b) => state.sort === "year-desc" ? b.year - a.year : state.sort === "field" ? a.field.localeCompare(b.field, "zh-CN") || a.year - b.year : a.year - b.year);
  }

  function cardTemplate(item) {
    return `<article class="theory-card" style="${fieldStyle(item.field)}">
      <div class="card-top"><span class="card-meta"><i></i>${escapeHtml(item.field)} · ${escapeHtml(item.topic)}</span><time class="card-year">${escapeHtml(item.date)}</time></div>
      <h3>${escapeHtml(item.title)}</h3>
      <p class="record-status">${escapeHtml(item.kind)} · ${escapeHtml(item.editorial)}</p><p class="people">${escapeHtml(item.people)}</p>
      <div class="formula">${escapeHtml(item.formula)}</div>
      <p class="summary">${escapeHtml(item.summary)}</p>
      <div class="card-bottom"><span class="application">应用 · ${escapeHtml(item.application)}</span><button class="detail-btn" type="button" data-id="${item.id}" aria-label="查看${escapeHtml(item.title)}详情">展开档案 →</button></div>
    </article>`;
  }

  function render() {
    const result = getResults();
    cards.innerHTML = result.map(cardTemplate).join("");
    el("empty").hidden = result.length > 0;
    el("result-count").textContent = result.length;
    el("live-count").textContent = PHYSICS_DATA.length;
    el("field-count").textContent = new Set(result.map(item => item.field)).size;
    el("result-label").textContent = result.length === PHYSICS_DATA.length ? "全部条目" : `${result.length} 个匹配结果`;
    const active = [state.source === "sourced" ? "附参考来源" : state.source === "legacy" ? "待补来源" : "",state.field !== "全部" ? state.field : "", state.topic !== "全部" ? state.topic : "", state.era !== "all" ? ERAS.find(e => e.id === state.era)?.label : "", state.query ? `“${state.query}”` : ""].filter(Boolean);
    el("filter-status").textContent = active.length ? active.join(" · ") : "显示全部条目";
  }

  function openDetail(item) {
    el("detail-content").innerHTML = `<article style="${fieldStyle(item.field)}">
      <header class="detail-hero">
        <div class="detail-kicker">${escapeHtml(item.field)} · ${escapeHtml(item.topic)} · ${escapeHtml(item.date)}</div>
        <h2 id="detail-title">${escapeHtml(item.title)}</h2><p class="record-status">${escapeHtml(item.kind)} · ${escapeHtml(item.editorial)}</p>
        <p class="detail-people">关键人物：${escapeHtml(item.people)}</p>
        <div class="detail-formula">${escapeHtml(item.formula)}</div>
      </header>
      <div class="detail-body">
        <section class="detail-block full"><h3>理论内核</h3><p>${escapeHtml(item.summary)}</p></section>
        <section class="detail-block full"><h3>形成与创作者</h3><p>${escapeHtml(item.context)}</p></section>
        <section class="detail-block"><h3>适用条件与边界</h3><p>${escapeHtml(item.conditions)}</p></section>
        <section class="detail-block"><h3>关键变量</h3><p>${escapeHtml(item.variables)}</p></section>
        <section class="detail-block"><h3>主要应用</h3><p>${escapeHtml(item.application)}</p></section>
        <section class="detail-block"><h3>历史意义</h3><p>${escapeHtml(item.significance)}</p></section>
        <section class="detail-block full"><h3>参考来源</h3>${item.sources.length ? '<ul>'+item.sources.map(source => `<li><a href="${escapeHtml(source.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(source.title)} ↗</a></li>`).join('')+'</ul>' : '<p>旧版条目尚未补入逐项来源。局部修正不代表全部历史与细节已完成复核。</p>'}</section>
        <section class="detail-block full"><h3>关联条目</h3>${item.related.length ? item.related.map(id => `<button type="button" class="related-btn" data-id="${escapeHtml(id)}">${escapeHtml(PHYSICS_DATA.find(row => row.id === id).title)}</button>`).join('') : '<p>后续继续补充知识关联。</p>'}</section>
      </div>
    </article>`;
    if (!dialog.open) dialog.showModal();
  }

  function reset() {
    state.query = ""; state.field = "全部"; state.era = "all"; state.topic = "全部"; state.sort = "year-asc"; state.source = "all"; el("source-filter").value = "all";
    el("search").value = ""; el("sort").value = "year-asc";
    document.querySelectorAll("[data-field]").forEach(btn => btn.classList.toggle("active", btn.dataset.field === "全部"));
    document.querySelectorAll("[data-era]").forEach(btn => btn.classList.toggle("active", btn.dataset.era === "all"));
    renderTopicOptions(); render();
  }

  document.addEventListener("click", event => {
    const fieldButton = event.target.closest("[data-field]");
    if (fieldButton) {
      state.field = fieldButton.dataset.field;
      document.querySelectorAll("[data-field]").forEach(btn => btn.classList.toggle("active", btn === fieldButton));
      renderTopicOptions();
      render(); return;
    }
    const eraButton = event.target.closest("[data-era]");
    if (eraButton) {
      state.era = eraButton.dataset.era;
      document.querySelectorAll("[data-era]").forEach(btn => btn.classList.toggle("active", btn === eraButton));
      render(); return;
    }
    const detailButton = event.target.closest("[data-id]");
    if (detailButton) openDetail(PHYSICS_DATA.find(item => item.id === detailButton.dataset.id));
  });

  el("search").addEventListener("input", event => { state.query = event.target.value.trim(); render(); });
  el("source-filter").addEventListener("change", event => { state.source = event.target.value; render(); });
  el("sort").addEventListener("change", event => { state.sort = event.target.value; render(); });
  el("topic-filter").addEventListener("change", event => { state.topic = event.target.value; render(); });
  el("reset-filters").addEventListener("click", reset);
  el("empty-reset").addEventListener("click", reset);
  el("detail-dialog").querySelector(".close-dialog").addEventListener("click", () => dialog.close());
  el("about-btn").addEventListener("click", () => el("about-dialog").showModal());
  el("about-dialog").querySelector(".close-about").addEventListener("click", () => el("about-dialog").close());
  [dialog, el("about-dialog")].forEach(modal => modal.addEventListener("click", event => { if (event.target === modal) modal.close(); }));
  document.addEventListener("keydown", event => {
    if (event.key === "/" && !/input|textarea|select/i.test(document.activeElement.tagName)) { event.preventDefault(); el("search").focus(); }
  });

  renderFilters(); renderTimeline(); renderEpochBars(); render();

  if (document.modelContext?.registerTool) {
    const validFields = ["全部", ...Object.keys(FIELD_META)];
    const validEras = ["all", ...ERAS.map(e => e.id)];
    const validTopics = ["全部", ...new Set(PHYSICS_DATA.map(item => item.topic))];
    document.modelContext.registerTool({
      name: "search_physics_archive",
      title: "检索物理学谱系",
      description: "检索物理学理论档案，可按关键词、领域、二级主题和时代筛选。",
      inputSchema: { type: "object", properties: { query: { type: "string", maxLength: 100 }, field: { type: "string", enum: validFields }, topic: { type: "string", enum: validTopics }, era: { type: "string", enum: validEras } }, additionalProperties: false },
      annotations: { readOnlyHint: true, untrustedContentHint: false },
      execute: (input = {}) => {
        const { query = "", field = "全部", topic = "全部", era = "all" } = input;
        if (typeof query !== "string" || query.length > 100 || !validFields.includes(field) || !validTopics.includes(topic) || !validEras.includes(era)) throw new TypeError("无效的检索条件");
        state.source = "all"; el("source-filter").value = "all"; state.query = query; state.field = field; state.topic = topic; state.era = era;
        el("search").value = query;
        document.querySelectorAll("[data-field]").forEach(btn => btn.classList.toggle("active", btn.dataset.field === field));
        document.querySelectorAll("[data-era]").forEach(btn => btn.classList.toggle("active", btn.dataset.era === era));
        renderTopicOptions();
        render();
        return { count: getResults().length, titles: getResults().slice(0, 20).map(item => item.title) };
      }
    });
  }
})();
