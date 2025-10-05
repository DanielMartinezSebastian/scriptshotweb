# 📚 Complete Documentation - Wshot

A comprehensive visual audit and web analysis platform that automates capture, analysis, and documentation of websites at enterprise scale. Designed for development teams, QA, designers, and digital consultants requiring exhaustive cross-platform user experience evaluations.

## 🎯 Main Features

### 🎯 **Automated Visual Auditing**
- 🚀 **Ultra-simple syntax**: `wshot URL -all` for complete audits
- 📱 **Device ecosystem**: 15+ configurations including iPhone (SE, 15, 15 Pro), Samsung Galaxy (S23, S23 Ultra), Google Pixel, iPad (standard, Pro), Galaxy Tab, MacBooks, ThinkPads, professional monitors (FHD, 2K, 4K)
- 🔄 **Smart dual capture**: Fixed viewport + full page with automatic scroll
- 🛡️ **Robust validation**: URL verification system with error detection before processing

### 🏗️ **Enterprise Architecture**
- 📁 **Advanced automatic organization**: Hierarchical structure by domain, device and timestamp with semantic nomenclature
- ⚡ **Zero-configuration engine**: Complete automation without manual intervention
- 📂 **Smart file system**: Saves to `~/Pictures/WSHOT/` with full domain organization
- 🎪 **Native multiplatform**: Full compatibility Windows, macOS, Linux

### 🤖 **Automated Intelligence**
- ⏳ **Advanced rendering control**: Configurable timing system for complex animations (3s default)
- 📜 **Progressive smart scroll**: Activation of lazy loading, parallax and intersection observers
- 🤖 **Obstacle detection and removal**: Auto-close GDPR banners, cookies and pop-ups in multiple languages
- 📊 **Structured metadata extraction**: Complete OpenGraph system with automatic social assets download

### 🚀 **Enterprise Mode**
- 🚀 **Super Mode**: Complete automated audit (all devices + scroll + OpenGraph + optimized timing)
- 📖 **Extensive documentation system**: Contextual help with `--help` and `--info` for technical teams
- 🔧 **Extensible API**: Modular architecture ready for CI/CD pipeline integration

## 🚀 Detailed Installation

### Installation via pip (Recommended) ⭐

Install wshot as a global Python package or in a virtual environment:

**For most systems:**
```bash
pip install wshot

# Or in a virtual environment (recommended)
python3 -m venv wshot-env
source wshot-env/bin/activate  # On Windows: wshot-env\Scripts\activate
pip install wshot
```

**For Arch Linux (recommended - pipx):**
```bash
# Install pipx if you don't have it
sudo pacman -S python-pipx

# Install wshot globally with pipx
pipx install wshot

# Install Chromium
~/.local/share/pipx/venvs/wshot/bin/playwright install chromium
```

**For Arch Linux (alternative - virtual environment):**
```bash
# Create virtual environment
python3 -m venv ~/.wshot-env
source ~/.wshot-env/bin/activate
pip install wshot
playwright install chromium

# Create alias in your .zshrc or .bashrc for global usage
echo 'alias wshot="~/.wshot-env/bin/wshot"' >> ~/.zshrc
source ~/.zshrc
```

**Required additional step:**

After installing with pip, you must install Playwright's Chromium browser:

```bash
# If you installed with normal pip
playwright install chromium

# If you installed with pipx on Arch Linux
~/.local/share/pipx/venvs/wshot/bin/playwright install chromium
```

**Verify installation:**

You can verify everything is installed correctly by running:

```bash
# Basic verification
wshot --help

# Complete verification with test script
python test_installation.py
```

**System dependencies (optional):**

If you encounter errors related to missing system libraries, install them according to your distribution:

```bash
# Ubuntu/Debian
sudo apt install -y libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 \
  libcups2 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 \
  libxrandr2 libgbm1 libpango-1.0-0 libcairo2 libasound2

# Fedora
sudo dnf install -y nss nspr atk at-spi2-atk cups-libs libdrm libxkbcommon \
  libxcomposite libxdamage libXrandr mesa-libgbm pango cairo alsa-lib

# Arch Linux
sudo pacman -S nss nspr atk at-spi2-atk cups libdrm libxkbcommon \
  libxcomposite libxdamage libxrandr mesa pango cairo alsa-lib
```

### Installation from repository (Development)

If you want to develop or contribute to the project:

```bash
git clone https://github.com/DanielMartinezSebastian/wshot.git
cd wshot

# Install in development mode
pip install -e .
playwright install chromium
```

## 📂 Detailed Output Structure

**Default location:**
- 📁 `~/Pictures/WSHOT/` (folder in user's Pictures)
- 📁 Or custom path with `--output-dir ~/Projects/Screenshots`

```
~/Pictures/WSHOT/
├── example.com/                    # Complete domain extracted from URL
│   ├── mobile/                     # Only requested folders
│   │   ├── example.com_main-page-mobile-20241005_142958.png           # Viewport
│   │   └── example.com_main-page-mobile-full-20241005_142958.png       # Full page
│   ├── tablet/
│   │   ├── example.com_contact-tablet-20241005_142958.png
│   │   └── example.com_contact-tablet-full-20241005_142958.png
│   ├── laptop/
│   │   ├── example.com_services-laptop-20241005_142958.png
│   │   └── example.com_services-laptop-full-20241005_142958.png
│   ├── desktop/
│   │   ├── example.com_main-page-desktop-20241005_142958.png
│   │   └── example.com_main-page-desktop-full-20241005_142958.png
│   └── opengraph/                  # OpenGraph metadata (if using --og or --all)
│       ├── opengraph-20241005_142958.json     # All metadata
│       └── og-image-20241005_142958.jpg       # Downloaded social image
```

**With `--all` or `--super` all folders are created automatically:**
```
~/Pictures/WSHOT/example.com/
├── mobile/           # iPhone 15 (default mobile)
├── iphone-se/
├── iphone-15-pro/
├── iphone-17/
├── galaxy-s23/
├── galaxy-s23-ultra/
├── pixel-7/
├── tablet/           # iPad (default tablet)
├── ipad-pro/
├── galaxy-tab-s9/
├── laptop/           # 13" Laptop (default)
├── laptop-15/
├── laptop-16/
├── desktop/          # Full HD Monitor (default)
├── desktop-2k/
├── desktop-4k/
└── opengraph/    ← Includes JSON + og:image
```

## 🛡️ URL Validation

Wshot automatically verifies that URLs are valid before proceeding:

```bash
# ✅ Valid URL
wshot https://google.com -all
# 🔍 Validating URL...
# ✅ Valid URL (Status: 200)
# 📁 Creating screenshots...

# ❌ Non-existent URL
wshot https://site-that-does-not-exist.com -all
# 🔍 Validating URL...
# ❌ Error: URL does not respond
# ❌ No folders created
```

## ✨ Características Avanzadas

### 🤖 **Automatic Pop-up Dismissal**
```bash
# Automatically close cookie banners, GDPR notices and other pop-ups
wshot https://site.com --device desktop --auto-dismiss

# Combine with other options for perfect screenshots
wshot https://site.com --super --auto-dismiss
```

**What does it do?**
- 🍪 Detecta y cierra automáticamente banners de cookies
- 📋 Cierra avisos de privacidad y consentimiento GDPR
- 🚫 Elimina pop-ups que bloquean la vista de la página
- 🌍 Soporte multiidioma (español, inglés, francés, alemán, italiano, portugués)
- 🎯 Compatible con frameworks populares: OneTrust, Cookiebot, Quantcast, TrustArc, Osano

### 📊 **OpenGraph Metadata Extraction**
```bash
# Extract OpenGraph metadata from any page
wshot https://site.com --device desktop --open-graph
# Or use the short alias:
wshot https://site.com --device desktop --og

# Automatically activated with --all and --super
wshot https://site.com --all  # ← OpenGraph included
wshot https://site.com --super  # ← OpenGraph included
```

**What does it extract?**
- 🏷️ **og:title** - Título para redes sociales
- 📝 **og:description** - Descripción optimizada
- 🖼️ **og:image** - Imagen social (descargada automáticamente)
- 🌐 **og:url** - URL canónica
- 🎯 **og:type** - Tipo de contenido (website, article, etc.)
- 📱 **og:site_name** - Nombre del sitio
- 🐦 **Twitter Card** - Metadatos de Twitter
- 📄 Y muchos más...

### ⏳ **Animation Control**
```bash
# Custom wait time for animations to load (default: 3s)
wshot https://site.com --wait-time 5
```
Perfect for sites with CSS animations, JavaScript or content that loads with delay.

### 📜 **Smart Smooth Scroll**
```bash
# Gradual scroll to trigger scroll-based animations
wshot https://site.com --smooth-scroll
```
Ideal for:
- Sites with **lazy loading**
- **Parallax** effects
- Animations triggered by **intersection observer**
- Content that appears when scrolling

### 🚀 **Super Mode (All-in-One)**
```bash
# Single command for optimized complete capture
wshot https://site.com --super
```
**Automatically activates:**
- ✅ **All devices** (`-all`) - Capture on mobile, tablet, laptop, desktop and all variants
- ✅ Smooth scroll (`--smooth-scroll`)
- ✅ OpenGraph extraction (`--open-graph`)
- ✅ Optimized timing (`--wait-time 2`)

### 📂 **Automatically Open File Explorer**
```bash
# Open explorer when finished (multiplatform)
wshot https://site.com --super --open

# On Windows opens Explorer
# On macOS opens Finder  
# On Linux detects your manager: Dolphin (KDE), Nautilus (GNOME), Thunar (XFCE), etc.
```

## 🎛️ Complete Parameters List

| Parameter | Description | Example |
|-----------|-------------|---------|
| `URL` | URL of the website to capture | `https://example.com` |
| `-all, --all-devices` | Capture on all devices | `-all` |
| `--device DEVICE` | Specific device | `--device mobile` |
| `--cliente NOMBRE` | Custom client name | `--cliente "MyCompany"` |
| `--output-dir PATH` | Custom output directory | `--output-dir ~/Projects` |
| `--wait-time SECONDS` | Wait time for animations | `--wait-time 5` |
| `--smooth-scroll` | Smooth scroll before full page capture | `--smooth-scroll` |
| `--auto-dismiss` | 🤖 Automatically close cookie banners and pop-ups | `--auto-dismiss` |
| `--open-graph, --og` | 📊 Extract OpenGraph metadata and download social image | `--og` |
| `--super` | 🚀 Complete optimized mode (ALL devices + OpenGraph + smooth scroll) | `--super` |
| `--open` | 📂 Open file explorer when finished | `--open` |
| `--help, -h` | Standard help | `--help` |
| `--info` | Complete extended guide | `--info` |

## 🎨 Capture Types

### 📏 **Viewport (Normal)**
Captures the visible browser area according to device size.

### 📜 **Complete (Full Page)**
Captures the entire page including scrollable content (`full_page=True`).

## 🔧 Requirements

- Python 3.8+  
- Playwright (automatically installed with pip)
- Requests (automatically installed with pip)
- Internet connection

## 📄 Advanced Practical Examples

```bash
# Capture contact page on all devices (basic)
wshot https://mycompany.com/contact -all

# Capture on most popular mobile (iPhone 15)
wshot https://mystore.com/products --device mobile

# Compare Android vs iPhone
wshot https://myapp.com --device galaxy-s23
wshot https://myapp.com --device mobile

# Capture on professional tablet with extra wait time
wshot https://myblog.com --device ipad-pro --wait-time 6

# Verify on most common laptop (13 inches)
wshot https://my-dashboard.com --device laptop

# Audit on professional 4K monitor
wshot https://my-portfolio.com --device desktop-4k

# Site with cookie banner - close automatically
wshot https://google.com --device desktop --auto-dismiss

# Extract only OpenGraph metadata without screenshots
wshot https://mycompany.com --device mobile --og

# Site with many animations - use super mode and open explorer
wshot https://animated-site.com --super --open

# Site with lazy loading, cookies and OpenGraph - complete combination
wshot https://parallax-site.com -all --smooth-scroll --auto-dismiss

# Complete SEO audit: screenshots + OpenGraph metadata
wshot https://important-client.com --super --cliente "VIPClient"

# Compact vs premium mobile comparison
wshot https://responsive.com --device iphone-se
wshot https://responsive.com --device galaxy-s23-ultra

# Verification on most common work devices
wshot https://intranet.com --device laptop --auto-dismiss

# Save to custom location and open automatically
wshot https://project.com --super --output-dir ~/Projects/WebAudits --open
```

### 🎯 Business Use Cases

| Site type | Recommended command | Reason |
|-----------|---------------------|--------|
| **Simple static site** | `--device desktop` | Fast and efficient |
| **Responsive site** | `-all` | View on all devices + OpenGraph |
| **Mobile app/PWA** | `--device mobile --device galaxy-s23` | Test on most popular mobiles |
| **Dashboard/Admin** | `--device laptop` | Typical work resolution |
| **E-commerce** | `--device mobile --device tablet --device desktop` | Cover mobile and desktop shopping |
| **Portfolio/Landing** | `--device desktop-4k` | Show maximum visual quality |
| **Site with animations** | `--super` | Optimized timing + scroll + OpenGraph |
| **Site with lazy loading** | `--smooth-scroll` | Activates deferred content |
| **Site with cookies/GDPR** | `--auto-dismiss` | Closes banners automatically |
| **SEO audit** | `--super` | Complete screenshots + OpenGraph metadata |
| **Google, Facebook, etc.** | `--super --auto-dismiss` | Clean screenshots without pop-ups + metadata |
| **Complete audit** | `--super --auto-dismiss` | Exhaustive capture without obstructions + SEO |
| **Slow site** | `--wait-time 7` | More time to load |
| **Brand comparison** | `--device mobile --device galaxy-s23` | iPhone vs Android |

## 🛠️ Development

### Project structure:
```
wshot/
├── wshot/                   # Main Python package
│   ├── __init__.py         # Package module
│   └── cli.py              # Main CLI code
├── pyproject.toml          # Project configuration (PEP 621)
├── MANIFEST.in             # Files included in distribution
├── test_installation.py    # Verification script
├── .gitignore              # Files to ignore in Git
├── LICENSE                 # MIT License
└── README.md               # This file
```

### Run in development mode:
```bash
# Install in editable mode
pip install -e .
playwright install chromium

# Run
wshot https://example.com --device mobile-17

# Or using super mode for complete testing:
wshot https://example.com --super
```

## 🤝 Contributing
1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🎉 Project Evolution

### v1.0.0 - Enterprise Visual Audit Platform 🏢
- ✅ **Enterprise architecture**: Complete refactoring as distributable Python platform
- ✅ **Unified global command**: `wshot` available system-wide after pip installation
- ✅ **Advanced organizational structure**: Elimination of redundancies and clean architecture
- ✅ **Modern PEP 621 configuration**: `pyproject.toml` with industry standards
- ✅ **Simplified installation**: `pip install git+https://...` for immediate deployment
- ✅ **Verification suite**: `test_installation.py` for environment validation
- ✅ **Development mode**: `pip install -e .` for contributors

### 🏗️ **Implemented Technical Capabilities**
- 📱 **Multi-device engine**: 15+ configurations from compact mobiles to professional 4K monitors
- 🛡️ **Robust validation system**: Preventive URL verification with error handling
- 📁 **Semantic organization**: Automatic structure by complete domain with descriptive nomenclature
- ⏳ **Advanced rendering engine**: Granular timing control for sites with complex animations
- 📜 **Smart progressive scroll**: Automatic activation of lazy loading and parallax effects
- 🤖 **AI for obstacle removal**: Detection and automatic closure of multilingual GDPR/cookie banners
- 📊 **Structured metadata extractor**: Complete OpenGraph system with automatic asset download
- 🚀 **Unified audit mode**: Super-mode for complete enterprise evaluations
- 📂 **System integration**: Automatic opening of multiplatform file explorers
- 📖 **Extensive technical documentation**: Contextual help system for development teams