# WebNovel Writer - 网文小说生成助手

专业的网文小说创作助手，帮助你快速生成爆款网文。

[English Version](README_EN.md)

---

## ✨ 功能特性

- 📖 **题材支持** - 玄幻、都市、言情、科幻、悬疑、历史等
- 📝 **大纲生成** - 自动生成完整故事大纲、世界观设定
- 👥 **人物设定** - 主角、配角、反派详细人设
- 📚 **章节生成** - 自动生成章节内容框架
- 🔥 **爆款元素** - 退婚、系统、重生、穿越、金手指等
- 📊 **爆款分析** - 分析热门作品套路

---

## 🚀 安装

```bash
cd /root/.openclaw/workspace/skills
git clone https://github.com/williamwg2025/openclaw-webnovel-writer.git webnovel-writer
chmod +x webnovel-writer/scripts/*.py
```

---

## 📖 使用

### 生成小说大纲

```bash
# 玄幻重生文
python3 webnovel-writer/scripts/generate-outline.py --genre 玄幻 --theme 重生

# 都市神豪文
python3 webnovel-writer/scripts/generate-outline.py --genre 都市 --theme 神豪
```

### 生成人物设定

```bash
# 主角设定
python3 webnovel-writer/scripts/character-gen.py --role 主角 --genre 玄幻

# 反派设定
python3 webnovel-writer/scripts/character-gen.py --role 反派 --genre 都市

# 女主设定
python3 webnovel-writer/scripts/character-gen.py --role 女主 --genre 言情
```

### 生成章节框架

```bash
python3 webnovel-writer/scripts/chapter-gen.py --chapter 1 --outline "退婚现场"
```

---

## 🎯 支持题材

| 题材 | 说明 | 热门元素 |
|------|------|----------|
| 玄幻 | 修炼、异能、异界 | 系统、金手指、越级挑战 |
| 都市 | 现代都市生活 | 神豪、兵王、医仙 |
| 言情 | 爱情故事 | 总裁、重生、甜宠 |
| 科幻 | 未来科技 | 末世、机甲、星际 |
| 仙侠 | 修仙问道 | 宗门、渡劫、长生 |

---

## 🔥 爆款套路

### 开篇套路
- **退婚流**：被退婚→获得金手指→打脸
- **重生流**：重生回到过去→弥补遗憾→崛起
- **穿越流**：穿越到异界→利用现代知识→称霸
- **系统流**：获得系统→完成任务→变强

### 爽点设计
- **打脸**：被看不起→展现实力→震惊众人
- **装逼**：低调→被迫出手→全场震惊
- **收获**：修炼/探索→获得宝物/功法→实力大增

---

## 🛠️ 脚本说明

| 脚本 | 功能 |
|------|------|
| `generate-outline.py` | 生成小说大纲 |
| `character-gen.py` | 生成人物设定 |
| `chapter-gen.py` | 生成章节框架 |

---

## 📄 许可证

MIT-0

---

**作者：** @williamwg2025  
**版本：** 1.0.0  
**灵感来源：** 起点中文网、纵横中文网、番茄小说等热门作品分析
