// Targeted corrections to legacy entries. Unchanged records remain explicitly unreviewed.
(() => {
  const em = {title:'Feynman Lectures II · Maxwell equations',url:'https://www.feynmanlectures.caltech.edu/II_18.html'};
  const qm = {title:'Feynman Lectures III · Quantum amplitudes',url:'https://www.feynmanlectures.caltech.edu/III_16.html'};
  const stat = {title:'Feynman Lectures I · Statistical mechanics',url:'https://www.feynmanlectures.caltech.edu/I_40.html'};
  const qft = {title:'Coleman · Quantum Field Theory',url:'https://arxiv.org/abs/1110.5013'};
  const patches = {
    'fermi-dirac': {formula:'f(E)=1/{exp[(E−μ)/(k_B T)]+1}',conditions:'平衡态的独立费米子或有效准粒子；T>0，零温时取阶跃函数极限。',sources:[stat]},
    yukawa: {formula:'V(r)=−g² exp(−mr)/(4πr)（ℏ=c=1）',conditions:'单个有质量玻色子交换的静态势模型；本式使用自然单位。恢复普通单位后的作用距离为 ℏ/(mc)，势能系数须采用一致的耦合约定。',sources:[qft]},
    tunneling: {formula:'T ∝ exp(−2κL)，κ=√[2m(V₀−E)]/ℏ',conditions:'一维矩形高宽势垒，E<V₀ 且 κL≫1；只显示主导指数衰减，透射率还有依赖能量的前因子。',variables:'T 透射概率，L 势垒宽度，V₀ 势垒高度，E 粒子能量，m 质量。',sources:[qm]},
    maxwell: {formula:'∇·E=ρ/ε₀；∇·B=0；∇×E=−∂B/∂t；∇×B=μ₀J+μ₀ε₀∂E/∂t',conditions:'SI 单位下微观电磁场方程；ρ、J 包含全部电荷与电流。介质宏观表述可改用 D、H 并补充本构关系。',sources:[em]},
    'em-wave': {conditions:'所示 c=1/√(μ₀ε₀) 为真空波速。无源真空可导出波动方程；介质须指定本构关系，色散介质的相速度与群速度一般不同。',sources:[em]},
    'gauss-magnetism': {context:'磁场散度为零是经典麦克斯韦体系的一部分。磁力线在有限区域中没有源或汇，可以闭合，也可以延伸至无穷远；不能把所有磁力线都说成闭合曲线。',sources:[em]},
    noether: {formula:'作用量的连续全局对称性 ⇒ 满足运动方程时的守恒流',conditions:'作用量具有可微连续全局对称性（允许差一个边界项）；结论在满足运动方程时成立。局域规范对称性涉及诺特第二定理与约束。',sources:[qft]},
    'navier-stokes': {conditions:'所示 μ∇²v 形式用于不可压缩、动力黏度为常数的牛顿流体，另需连续性方程、初始及边界条件。可压缩或变黏度情形应使用完整黏性应力散度。'},
    'born-rule': {formula:'ρ(x)=|ψ(x)|²，P(A)=∫_A |ψ(x)|² dx',conditions:'归一化的位置波函数；ρ(x) 是概率密度而不是单点概率。离散测量概率使用相应投影算符。',variables:'ψ 位置波函数，ρ 概率密度（此处不是密度算符），A 空间区域。',sources:[qm]},
    'fermi-golden': {people:'狄拉克等发展含时微扰理论；费米推广该表述',conditions:'弱微扰、近连续终态谱及中间时间尺度下的跃迁速率近似；不适用于短时二次行为或孤立两能级的完整相干振荡。',sources:[qft]},
    'newton-laws': {summary:'以惯性、力与动量变化、作用与反作用建立经典动力学框架。'},
    radioactivity: {formula:'N(t)=N₀ exp(−λt)，t₁/₂=ln2/λ',context:'1896年贝克勒尔发现放射性；卢瑟福、索迪在1902—1903年前后发展放射性转化与衰变规律。发现年份与指数衰变理论形成并非同一节点。',conditions:'独立衰变且衰变常数 λ 不随时间变化；复杂衰变链须联立母体与子体方程。'},
    'rc-transient': {formula:'V_C(t)=V₀[1−exp(−t/RC)]（由零电压充电）',conditions:'理想恒压源、恒定电阻电容、初始电容电压为零；其他初始条件需加入相应齐次解。'},
    bohr: {conditions:'所示 E_n=−13.6 eV/n² 用于氢原子的非相对论近似，忽略有限核质量、精细结构等修正；类氢离子须加入 Z² 与约化质量修正。'},
    bcs: {conditions:'所示零温能隙与临界温度关系适用于弱耦合、各向同性 s 波 BCS 超导；不是所有超导体的普适比例。',sources:[{title:'Feynman Lectures III · Superconductivity',url:'https://www.feynmanlectures.caltech.edu/III_21.html'}]},
    'standard-model': {conditions:'标准模型描述电磁、弱、强相互作用，不含引力。最小版本中的中微子无质量；解释已观测的振荡需要扩展质量项。',sources:[{title:'PDG 2025 · Electroweak model',url:'https://pdg.lbl.gov/2025/reviews/rpp2025-rev-standard-model.pdf'},{title:'PDG 2025 · Neutrino mixing',url:'https://pdg.lbl.gov/2025/reviews/rpp2025-rev-neutrino-mixing.pdf'}]},
    'grav-redshift': {formula:'(ν接收−ν发射)/ν发射 ≈ (Φ发射−Φ接收)/c²',conditions:'静态弱引力场，发射者和接收者相对静止；光向较高引力势传播时接收频率降低。',variables:'Φ 牛顿引力势，ν 本地测量的光频率；忽略相对运动的多普勒效应。',sources:[{title:'Carroll · General Relativity',url:'https://arxiv.org/abs/gr-qc/9712019'}]},
    'first-law': {formula:'ΔU=Q−W（W 为系统对外做功）',conditions:'封闭系统，Q 为吸收热量，W 为系统对外做功；开放系统还需计入物质携带的能量。'},
    'second-law': {formula:'ΔS孤立系统≥0；dS≥δQ/T边界',conditions:'Clausius 不等式中温度为换热处的边界／热库温度；可逆过程取等号。局部子系统的熵可以因向外输运而减少。'},
    boltzmann: {conditions:'S=k_B lnΩ 的直接形式用于微正则系综中等概率可及微观态；一般概率分布使用 Gibbs 熵。',sources:[stat]}
  };
  for (const item of PHYSICS_DATA) {
    item.sources=[]; item.related=[]; item.kind='旧版条目';
    item.editorial='旧版条目 · 待逐项复核';
    if (patches[item.id]) {
      Object.assign(item, patches[item.id]);
      item.editorial='旧版条目 · 本次局部修正';
    }
  }
  TIMELINE_MILESTONES.push(
    {year:'1954',title:'规范场论',subtitle:'非阿贝尔相互作用',color:'#da97ed'},
    {year:'1980',title:'量子霍尔',subtitle:'拓扑与量子物质',color:'#e5a2ff'},
    {year:'1994',title:'量子算法',subtitle:'计算与信息',color:'#a7bedb'},
    {year:'2015',title:'引力波探测',subtitle:'时空的新窗口',color:'#ff9fc7'}
  );
})();
