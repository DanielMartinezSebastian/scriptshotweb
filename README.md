# 📸 Wshot

Automated web screenshot tool for multiple devices. Perfect for visual audits, responsive testing, and web project documentation.

## 🚀 Quick Installation

```bash
pip install wshot
playwright install chromium
```

<details>
<summary>Install from source</summary>

```bash
pip install git+https://github.com/DanielMartinezSebastian/wshot.git
playwright install chromium
```
</details>

> Installation issues? See [DOCS.md](DOCS.md#-detailed-installation) or [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

## ⚡ Basic Usage

```bash
# Capture on all devices
wshot https://example.com -all

# Specific device
wshot https://example.com --device mobile
wshot https://example.com --device desktop

# Super mode (recommended)
wshot https://example.com --super
```

> See all commands and options in [DOCS.md](DOCS.md#️-complete-parameters-list)

## 📱 Main Devices

| Device | Dimensions | Usage |
|--------|------------|-------|
| `mobile` | 393×852 | iPhone 15 (mobile standard) |
| `tablet` | 768×1024 | iPad (tablet standard) |
| `laptop` | 1280×800 | 13" Laptop (standard) |
| `desktop` | 1920×1080 | Full HD Monitor (standard) |
| `desktop-4k` | 3840×2160 | 4K Professional Monitor |

> See complete list in [DEVICES.md](DEVICES.md)

## 📂 Output Structure

```
~/Pictures/WSHOT/
└── example.com/
    ├── mobile/
    │   ├── example.com_mobile-20241005_142958.png
    │   └── example.com_mobile-complete-20241005_142958.png
    └── desktop/
        ├── example.com_desktop-20241005_142958.png
        └── example.com_desktop-complete-20241005_142958.png
```

## ⚙️ Main Options

```bash
# All devices
wshot https://example.com -all

# Specific device
wshot https://example.com --device mobile

# Super mode (recommended for complex sites)
wshot https://example.com --super

# Custom wait time
wshot https://example.com --device desktop --wait-time 5

# Auto-dismiss cookie banners
wshot https://example.com --device desktop --auto-dismiss

# Extract OpenGraph metadata
wshot https://example.com --device desktop --og

# Open file explorer when finished
wshot https://example.com --super --open
```

## 📖 Help

```bash
wshot --help      # Quick help
wshot --info      # Complete guide
```

## 📚 Documentation

- **[DOCS.md](DOCS.md)** - Complete documentation and advanced features
- **[DEVICES.md](DEVICES.md)** - Complete list of available devices
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Common problem solutions
- **[ROADMAP.md](ROADMAP.md)** - Project evolution and future plans

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.