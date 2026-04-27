# 项目记忆 · 筑见 Neil 个人网站

## 行动准则（Karpathy Guidelines）

### 1. Think Before Coding（先思考）
- 显式声明假设，不确定就问
- 有歧义就呈现多种解释
- 该反对时就反对
- 困惑就停下来问

### 2. Simplicity First（简单优先）
- 只写解决问题所需的最少代码
- 不做未请求的功能/抽象/配置
- 如果200行能变成50行，重写

### 3. Surgical Changes（精准修改）
- 只触碰必须改的
- 不"改进"相邻代码
- 匹配现有风格
- 每一行修改都能追溯到用户请求

### 4. Goal-Driven Execution（目标驱动）
- 定义成功标准，循环验证
- "加验证" → "写测试用例，然后让它通过"
- "修bug" → "写复现测试，然后让它通过"

## 文件映射（已验证正确，勿随意覆盖）

| 文件名 | 内容 | 最后确认 |
|--------|------|---------| 
| `index.html` | 首页 | ✓ |
| `invest.html` | 投资工具集子页 | ✓ |
| `social-gongzhonghao.jpg` | 公众号引流图 | ✓ |
| `social-video.jpg` | 视频号引流图 | ✓ |
| `social-xiaohongshu.jpg` | 小红书引流图 | ✓ |
| `invest-clawbot-800.jpg` | 微信ClawBot估值查询截图 | ✓ 2026-04-27 |
| `email-correct-600.jpg` | 邮件执行反馈截图 | ✓ 2026-04-27 |
| `pe-final-600.jpg` | PE-TTM分位分析截图 | ✓ 2026-04-27 |
| `invest-lightgbm.jpg` | LightGBM回测截图 | ✓ |

## invest.html 图片顺序

1. `invest-clawbot-800.jpg` → ClawBot 微信截图
2. `email-correct-600.jpg` → 邮件执行反馈
3. `pe-final-600.jpg` → PE-TTM 分位分析

## 关键规则

1. **换图前必须确认**：先识别图片内容，再确认替换哪个位置，和用户二次确认后再操作
2. **一次只换一张**：用户说换多张时，逐张确认逐张替换
3. **上传后验证**：每次上传后下载回来确认内容是否正确
4. **不做多余操作**：用户说换图就只换图，不要同时改HTML结构或互换文件

## 网站信息

- 首页：https://zhujianneil.github.io
- 投资页：https://zhujianneil.github.io/invest.html
- AI页：https://zhujianneil.github.io/ai.html
- GitHub：https://github.com/zhujianneil/github.io（仓库实际为 zhujianneil.github.io）
- 服务器：甲骨文云 VPS，目录 /home/ubuntu
- GitHub Actions 自动部署已配置

## 首页结构

- Hero：标题 + CTA（"如果你也在用框架对抗噪音"）+ 三个锚点卡片
- Works：投资（链 invest.html）/ AI（链 ai.html）/ 认知
- Contact：召唤语 + GitHub + 邮箱 + 三张引流图 + 咨询描述（交流 / 合作 / 咨询）
- Footer：不蒜子访问统计（初始值8427）

## 用户持仓（投资分析参考）

**持仓（12只）**:
- 美股：BRK.B、PDD、V
- 港股：腾讯(00700)、小米(01810)
- A股：移动(600941)、福耀(600660)、招行(600036)、海尔(600690)、宝钢(600019)、上港(600018)、中国通号(688009)

**观察仓（4只）**:
- 茅台(600519)、神华(601088)、长江电力(600900)、泡泡玛特(09992)

## 重要原则

1. **发现错误要直接指出**，不要美化
2. **不许把任务丢给用户**，遇到问题自己解决
3. **外部操作谨慎**（发邮件、发帖等）
4. **对内操作大胆**（阅读、整理、学习）
5. **换图必须确认**：先识别内容→确认位置→用户确认→一次只换一张→上传后验证
