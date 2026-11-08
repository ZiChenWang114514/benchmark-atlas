# Benchmark Constitution Page更新

源码为更新成功后ReadCanvas导出的完整快照。原24项保留结构化阅读；新增76项为索引阅读视图，所有条目均链接完整11章节Google Doc。100项均显示2026H2引用/使用证据；26条动态可展开。

数据内嵌、本地gzip解压、无网络请求。Page不是实时榜单。新增条目完整字段不全部复制进Canvas，避免失去逐字段归档来源；权威JSON与Markdown仍在data/benchmarks和content/benchmarks。


- `benchmark-constitution.canvas.tsx`：已发布 Page 的完整源码快照，使用应用内 `grok/canvas` 组件库；不是独立部署的网站工程。
- `validation.json`：100 个基准、来源索引、跨字段引用、内嵌 gzip 完整性和 /中文档案入口的校验记录。Canvas 发布工具已通过严格类型检查。
- 中文新闻区、五板块目录、搜索、板块筛选、名称/发布日期排序、档案阅读与返回导航。
- 档案覆盖宪法第四章的十一个章节；作者列表在阅读视图节选，全部作者、论文修订历史和补充材料链接到完整中文归档。未知项显示“待核实”，不推断为官方未公开。
- 数据在写入时内嵌，gzip 仅在浏览器本地解压，无远程请求；需要支持 DecompressionStream 的现代浏览器。外部证据与 链接由读者主动打开。
- 本次资料访问日为 2026-11-07；观察日期与事件日期分开显示。此 Page 不会自动刷新，不修改数据库；控件只改变当前视图。
- 原始逐字段 JSON 位于 `../data/benchmarks/`，新闻位于 `../data/news.json`。此 Canvas 不会自动刷新；更新数据后若还要更新 Canvas，须重新发布并把源代码同步到此目录。
- 面向公众的静态网站在 `../site/`，发布到 GitHub Pages。它在构建时直接读取 `data/`，不依赖这份 Canvas 快照；数据推送到 `main` 后由 Actions 重新构建。
