# Benchmark Atlas · Page 前端

页面：https://cursor.com/canvas/store-b55ff34d-87f8-49b6-b918-2b49a450dddf/9113c060-061a-4a5e-8de9-1873740d500a

- `benchmark-atlas.canvas.tsx`：已发布 Page 的完整源码快照，使用应用内 `grok/canvas` 组件库；不是独立部署的网站工程。
- `validation.json`：24 个基准、来源索引、跨字段引用、内嵌 gzip 完整性和 Drive/中文档案入口的校验记录。Canvas 发布工具已通过严格类型检查。
- 中文新闻区、五板块目录、搜索、板块筛选、名称/发布日期排序、档案阅读与返回导航。
- 档案覆盖宪法第四章的十一个章节；作者列表在阅读视图节选，全部作者、论文修订历史和补充材料链接到完整中文归档。未知项显示“待核实”，不推断为官方未公开。
- 数据在写入时内嵌，gzip 仅在浏览器本地解压，无远程请求；需要支持 DecompressionStream 的现代浏览器。外部证据与 Drive 链接由读者主动打开。
- 本次资料访问日为 2026-11-07 KST；观察日期与事件日期分开显示。此 Page 不会自动刷新，不修改数据库；控件只改变当前视图。
- 原始逐字段 JSON 位于 `../data/benchmarks/`，新闻位于 `../data/news.json`。后续更新数据后还须重新发布 Page，并将发布成功的源代码同步到此目录。
- 此次未创建 GitHub 仓库，未 push。
