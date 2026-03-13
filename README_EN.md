# WebNovel Writer for OpenClaw

Generate popular web novels with AI assistance.

[中文版本](README.md)

---

## ✨ Features

- 📖 Genre support - Fantasy, urban, romance, sci-fi
- 📝 Outline generation - Auto-generate story outlines
- 👥 Character design - Create character profiles
- 🌍 World building - Build story worlds

---

## 🚀 Installation

```bash
cd ~/.openclaw/workspace/skills
# Skill installed at: ~/.openclaw/workspace/skills/webnovel-writer
chmod +x webnovel-writer/scripts/*.py
```

**That's it! All scripts included, no external cloning needed.**

---

## 📖 Usage

```bash
# Basic usage
python3 webnovel-writer/scripts/*.py

# Check help
python3 webnovel-writer/scripts/*.py --help
```

**Purpose:** Write web novels with AI assistance

---

## 🛠️ Scripts

| Script | Function |
|--------|----------|
| `*.py` | Main scripts (check scripts/ directory) |

---

## 🔒 Security Notes

### Code Source ✅
**All scripts included in the package:**
- ❌ No external cloning
- ❌ No downloading external code

### Network Access
- **Scripts run locally** - No network calls (unless specified)

### File Access
- **Read:** Configuration files in skill directory
- **Write:** Only when explicitly specified

### Data Security
- **Local processing** - All operations run locally
- **No upload** - No data sent to external servers

### Usage Tips
1. Check scripts/ directory for available scripts
2. Test with simple commands first
3. Don't provide sensitive information

---

**Author:** @williamwg2025  
**Version:** Check SKILL.md  
**License:** MIT-0

---

## 📁 Directory Structure

```
webnovel-writer/
├── SKILL.md          # Skill metadata and documentation
├── README.md         # Chinese documentation
├── README_EN.md      # English documentation
├── config/           # Configuration files (optional)
│   └── *.json
└── scripts/          # Script files
    ├── *.py
    └── *.sh
```

---

**Last updated:** 2026-03-13
