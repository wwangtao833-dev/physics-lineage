# 物理学谱系

[在线数据库](https://wwangtao833-dev.github.io/physics-lineage/) · [检查与覆盖对照](AUDIT.md)

180 个核心条目、17 个领域。支持关键词、领域、主题、时代与来源状态筛选，详情包含公式、边界条件、来源及关联条目。纯静态页面，不依赖外部脚本或在线公式渲染服务。

## 维护

- `data.js`、`data-extended.js`：原有 120 条。
- `data-reviewed.js`：20 条旧记录的局部修正；保留明确的复核状态。
- `scripts/build-modern.py`：60 条补充内容及来源的编辑入口；运行 `python3 scripts/build-modern.py` 生成 `data-modern.js`。
- `node scripts/validate.mjs`：检查编号、必填字段、分类、年代、来源协议及关联完整性。
- 本地预览：`python3 -m http.server 8000`，打开 `http://localhost:8000`。

推送 main 后，GitHub Actions 先执行校验，再将网页所需文件部署至 Pages。新增条目必须说明公式约定、适用范围、代表年代和来源。年份为历史索引节点，并不主张唯一首创权。
