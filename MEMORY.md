# 项目记忆 · 筑见 Neil 个人网站

## 文件映射（已验证正确，勿随意覆盖）

| 文件名 | 内容 | 最后确认 |
|--------|------|---------|
| `index.html` | 首页 | ✓ |
| `invest.html` | 投资工具集子页 | ✓ |
| `social-gongzhonghao.jpg` | 公众号引流图 | ✓ |
| `social-video.jpg` | 视频号引流图 | ✓ |
| `social-xiaohongshu.jpg` | 小红书引流图 | ✓ |
| `invest-clawbot.jpg` | 微信ClawBot估值查询截图 | ✓ |
| `invest-email.jpg` | PE-TTM分析图（注意：文件名是email但内容是PE） | ✓ |
| `invest-pe.jpg` | 邮件执行反馈截图（注意：文件名是pe但内容是邮件） | ✓ |
| `invest-fcf.jpg` | FCF买入信号截图 | ✓ |
| `invest-lightgbm.jpg` | LightGBM回测截图 | ✓ |

## invest.html 图片顺序

1. `invest-clawbot.jpg` → ClawBot 微信截图
2. `invest-email.jpg` → PE-TTM 分析图
3. `invest-pe.jpg` → 邮件执行反馈

## 关键规则

1. **换图前必须确认**：先识别图片内容，再确认替换哪个位置，和用户二次确认后再操作
2. **一次只换一张**：用户说换多张时，逐张确认逐张替换
3. **上传后验证**：每次上传后下载回来确认内容是否正确
4. **不做多余操作**：用户说换图就只换图，不要同时改HTML结构或互换文件

## 网站信息

- 首页：https://zhujianneil.github.io
- 投资页：https://zhujianneil.github.io/invest.html
- GitHub：https://github.com/zhujianneil/github.io（仓库实际为 zhujianneil.github.io）
- 服务器：甲骨文云 VPS，目录 /home/ubuntu
- GitHub Actions 自动部署已配置

## 首页结构

- Hero：标题 + CTA（"如果你也在用框架对抗噪音"）+ 三个锚点卡片
- Works：投资（链 invest.html）/ AI / 认知
- Contact：召唤语 + GitHub + 邮箱 + 三张引流图 + 咨询描述（投资判断 · AI 工作流设计 · AI × 财务）
- Footer：不蒜子访问统计
