export type ChapterSpec = {
  id: string;
  title: string;
  intro: string;
  keys: string[];
};

export const CHAPTERS: ChapterSpec[] = [
  {
    id: 'basic_info',
    title: '基本信息',
    intro: '名称、版本、许可证和对外入口。数据集版本与论文版本分开记录。',
    keys: [
      'name',
      'full_name',
      'version',
      'paper_version',
      'release_date',
      'section',
      'subfields',
      'license',
      'paper_url',
      'code_url',
      'dataset_url',
      'official_homepage',
      'paper_title',
    ],
  },
  {
    id: 'organization',
    title: '发起与维护',
    intro: '作者单位不等于发起机构，也不等于当前维护方。资助方只写已经公开的信息。',
    keys: ['initiators', 'partners', 'authors', 'maintainer', 'funders'],
  },
  {
    id: 'design_goals',
    title: '设计目标',
    intro: '要测什么能力，以及为什么已有的评测不够。',
    keys: ['capabilities', 'gap_in_prior_benchmarks'],
  },
  {
    id: 'construction',
    title: '构建方式',
    intro: '题目从哪来、谁出的、怎样审核，以及有没有去污染。',
    keys: ['question_sources', 'author_background', 'review_process', 'quality_control', 'decontamination'],
  },
  {
    id: 'data_format',
    title: '数据形式',
    intro: '题量、题型、模态、语言、难度，以及公开集和隐藏集怎样划分。',
    keys: ['size', 'question_types', 'modalities', 'languages', 'difficulty', 'public_hidden_split'],
  },
  {
    id: 'evaluation',
    title: '评测方法',
    intro: '指标、评分和提示设置不同，分数就不能直接比较。',
    keys: ['metrics', 'scoring', 'prompt_settings', 'official_scripts', 'comparability_warning'],
  },
  {
    id: 'latest_status',
    title: '最新情况',
    intro: '版本、饱和、污染和衍生工作。没查清的保持待核实。',
    keys: [
      'checked_at',
      'latest_dataset_version',
      'paper_revision_history',
      'saturation',
      'contamination_and_issues',
      'derivatives',
    ],
  },
  {
    id: 'leaderboard',
    title: '榜单快照',
    intro: '只收录来源页上读得到的结果。快照代表采集日，不是实时排名。',
    keys: ['snapshot_date', 'official_url', 'third_party_url', 'results', 'coverage_note'],
  },
  {
    id: 'contact',
    title: '联系方式',
    intro: '只收录论文、官网或仓库里的公开渠道，不收集私人联系方式。',
    keys: ['public_emails', 'github_issues', 'official_social', 'privacy_policy'],
  },
  {
    id: 'original_files',
    title: '原始文件',
    intro: 'Drive 中的 PDF 是下载下来的原件，不改内容。哈希对应那一次下载。',
    keys: ['paper_pdf_url', 'drive_pdf', 'sha256', 'pdf_bytes', 'drive_folder', 'other_documents'],
  },
  {
    id: 'changelog',
    title: '变更记录',
    intro: '这条档案每次修改的日期和内容。旧记录保留。',
    keys: [],
  },
];

export const PRIMARY_SECTIONS: { id: string; blurb: string }[] = [
  { id: '物理', blurb: '物理知识、推理与科学计算' },
  { id: '化学', blurb: '化学知识、分子与实验相关任务' },
  { id: '生物与医学', blurb: '生物医学问题、实验流程与文献' },
  { id: '地球与天文', blurb: '天文、地球观测、气候与天气' },
  { id: '材料', blurb: '材料属性、稳定性与发现' },
];

export const SECONDARY_SECTIONS = ['语言', '推理', '数学', '代码', '多模态', 'Agent', '安全'];
