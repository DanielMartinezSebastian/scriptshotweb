# 📸 Wshot

Una plataforma integral de auditoría visual y análisis web que automatiza la captura, análisis y documentación de sitios web a escala empresarial. Diseñada para equipos de desarrollo, QA, diseñadores y consultores digitales que requieren evaluaciones exhaustivas de experiencia de usuario multiplataforma.

## ✨ Características Principales

### 🎯 **Auditoría Visual Automatizada**
- 🚀 **Sintaxis ultra-simple**: `wshot URL -all` para auditorías completas
- 📱 **Ecosistema de dispositivos**: 15+ configuraciones incluyendo iPhone (SE, 15, 15 Pro), Samsung Galaxy (S23, S23 Ultra), Google Pixel, iPad (estándar, Pro), Galaxy Tab, MacBooks, ThinkPads, monitores profesionales (FHD, 2K, 4K)
- 🔄 **Captura dual inteligente**: Viewport fijo + página completa con scroll automático
- 🛡️ **Validación robusta**: Sistema de verificación de URLs con detección de errores antes del procesamiento

### 🏗️ **Arquitectura Empresarial**
- 📁 **Organización automática avanzada**: Estructura jerárquica por dominio, dispositivo y timestamp con nomenclatura semántica
- ⚡ **Motor de configuración cero**: Automatización completa sin intervención manual
- 📂 **Sistema de archivos inteligente**: Guarda en `~/Pictures/WSHOT/` con organización por dominio completo
- 🎪 **Multiplataforma nativo**: Compatibilidad total Windows, macOS, Linux

### 🤖 **Inteligencia Automatizada**
- ⏳ **Control avanzado de renderizado**: Sistema de timing configurable para animaciones complejas (3s por defecto)
- 📜 **Scroll inteligente progresivo**: Activación de lazy loading, parallax y intersection observers
- 🤖 **Detección y eliminación de obstáculos**: Auto-cierre de banners GDPR, cookies y pop-ups en múltiples idiomas
- 📊 **Extracción de metadatos estructurados**: Sistema completo OpenGraph con descarga automática de assets sociales

### 🚀 **Modo Empresarial**
- 🚀 **Modo Super**: Auditoría completa automatizada (todos los dispositivos + scroll + OpenGraph + timing optimizado)
- 📖 **Sistema de documentación extensivo**: Ayuda contextual con `--help` e `--info` para equipos técnicos
- 🔧 **API extensible**: Arquitectura modular preparada para integración en pipelines CI/CD

## 🎯 Roadmap de Evolución Tecnológica

### ✅ **Fundamentos Completados**
- [x] ~~Sistema de renderizado avanzado con scroll progresivo~~ ✅ **COMPLETADO**
- [x] ~~Motor de timing inteligente para animaciones complejas~~ ✅ **COMPLETADO**
- [x] ~~Modo auditoría empresarial unificado~~ ✅ **COMPLETADO**
- [x] ~~Arquitectura de almacenamiento profesional en Pictures/WSHOT/~~ ✅ **COMPLETADO**
- [x] ~~Refactorización para distribución mediante pip~~ ✅ **COMPLETADO**

### 🔮 **Expansión de Capacidades**
- [ ] **Motor multiidioma**: Unificación completa español/inglés en toda la interfaz
- [ ] **Analizador SEO avanzado**: Extracción y análisis de JSON-LD, microdata y schema.org
- [ ] **Optimización WebP**: Compresión inteligente y formatos optimizados para web
- [ ] **Sistema de headers personalizados**: Bypass de bloqueos y detección anti-bot
- [ ] **Motor de cookies inteligente**: Inyección automática para sitios conocidos
- [ ] **Spider de sitio completo**: Crawling y captura automática de toda la arquitectura web
- [ ] **Extractor de media avanzado**: Recopilación automática de todos los assets multimedia
- [ ] **Generador de reportes Markdown**: Documentación automática con análisis visual
- [ ] **Sistema de autenticación**: Soporte para login automático y sesiones persistentes

<details>
<summary><strong>🏗️ Refactorización Arquitectónica Futura</strong> (haz clic para expandir)</summary>

<br>

Para mejorar la mantenibilidad y escalabilidad del proyecto, se propone la siguiente **reestructuración modular**:

### 📋 Roadmap de Arquitectura

**Objetivo:** Migrar de una arquitectura monolítica (`cli.py`) a una estructura modular y profesional que facilite:
- ✅ **Mantenimiento** - Código organizado por responsabilidades
- ✅ **Escalabilidad** - Fácil adición de nuevas características
- ✅ **Testing** - Unidades testeable independientes
- ✅ **Reutilización** - Módulos importables por otras aplicaciones

### 🎯 Estructura Propuesta

```
wshot/
├── __init__.py
├── cli.py                 # CLI interface (ligero, solo argumentos)
├── core/                  # 📁 Lógica principal
│   ├── __init__.py
│   ├── capture.py         # Funciones de captura de screenshots
│   ├── devices.py         # Configuraciones de dispositivos
│   ├── utils.py           # Utilidades (validación URLs, manejo archivos)
│   └── opengraph.py       # Extracción metadatos OpenGraph
├── formats/               # 📁 Diferentes formatos de salida
│   ├── __init__.py
│   ├── png.py             # Formato PNG (actual)
│   ├── webp.py            # Formato WebP optimizado
│   └── markdown.py        # Generación de reportes en Markdown
└── scrapers/              # 📁 Scrapers especializados
    ├── __init__.py
    ├── full_site.py       # Captura completa navegando por todos los links
    └── media_extractor.py # Extracción de contenido multimedia
```

### 🔄 Migración por Fases

**Fase 1: Separación de Responsabilidades** 🟡
- [ ] Extraer lógica de dispositivos a `core/devices.py`
- [ ] Mover funciones de captura a `core/capture.py`
- [ ] Separar validación de URLs y utilidades a `core/utils.py`
- [ ] Mantener `cli.py` solo para interfaz de comandos

**Fase 2: Formatos Modulares** 🟠
- [ ] Crear módulo `formats/png.py` (migrar código actual)
- [ ] Implementar `formats/webp.py` para optimización
- [ ] Desarrollar `formats/markdown.py` para reportes

**Fase 3: Scrapers Avanzados** 🔴
- [ ] Implementar `scrapers/full_site.py` para captura completa de sitios
- [ ] Crear `scrapers/media_extractor.py` para extracción de multimedia
- [ ] Integrar scrapers con formatos de salida

**Fase 4: Consolidación** 🟢
- [ ] Tests unitarios para todos los módulos
- [ ] Documentación API interna
- [ ] Optimización de rendimiento
- [ ] Refactorización de imports y dependencias

### 💡 Beneficios Esperados

**Para Desarrolladores:**
- 🧩 **Modularidad** - Cada función tiene su lugar específico
- 🧪 **Testabilidad** - Tests unitarios por módulo
- 📖 **Legibilidad** - Código más fácil de entender y mantener
- 🔧 **Extensibilidad** - Nuevas features sin tocar código existente

**Para Usuarios:**
- 🚀 **Nuevas Características** - WebP, sitios completos, reportes MD
- ⚡ **Mejor Rendimiento** - Código optimizado y eficiente
- 🎯 **Más Formatos** - Múltiples opciones de salida
- 📊 **Reportes Avanzados** - Informes detallados de auditorías

### 🎪 Compatibilidad

- ✅ **API CLI** - Interfaz de comandos se mantendrá idéntica
- ✅ **Retrocompatibilidad** - Todos los comandos actuales seguirán funcionando
- ✅ **Funcionalidades** - Características actuales se preservan 100%
- ✅ **Configuración** - Mismos parámetros y estructura de salida

> **Nota:** Esta refactorización es una mejora interna que no afectará la experiencia del usuario final. El comando `wshot` funcionará exactamente igual pero con una base de código más robusta y mantenible.

</details>

## 🚀 Instalación

### Instalación mediante pip (Recomendada) ⭐

Instala wshot como un paquete Python global o en un entorno virtual:

**Para la mayoría de sistemas:**
```bash
# Instalación desde el repositorio con pip
pip install git+https://github.com/DanielMartinezSebastian/wshot.git

# O en un entorno virtual (recomendado)
python3 -m venv wshot-env
source wshot-env/bin/activate  # En Windows: wshot-env\Scripts\activate
pip install git+https://github.com/DanielMartinezSebastian/wshot.git
```

**Para Arch Linux (recomendado - pipx):**
```bash
# Instalar pipx si no lo tienes
sudo pacman -S python-pipx

# Instalar wshot globalmente con pipx
pipx install git+https://github.com/DanielMartinezSebastian/wshot.git

# Instalar Chromium
~/.local/share/pipx/venvs/wshot/bin/playwright install chromium
```

**Para Arch Linux (alternativa - entorno virtual):**
```bash
# Crear entorno virtual
python3 -m venv ~/.wshot-env
source ~/.wshot-env/bin/activate
pip install git+https://github.com/DanielMartinezSebastian/wshot.git
playwright install chromium

# Crear alias en tu .zshrc o .bashrc para uso global
echo 'alias wshot="~/.wshot-env/bin/wshot"' >> ~/.zshrc
source ~/.zshrc
```

**Paso adicional necesario:**

Después de instalar con pip, debes instalar el navegador Chromium de Playwright:

```bash
# Si instalaste con pip normal
playwright install chromium

# Si instalaste con pipx en Arch Linux
~/.local/share/pipx/venvs/wshot/bin/playwright install chromium
```

**Verificar instalación:**

Puedes verificar que todo está instalado correctamente ejecutando:

```bash
# Verificación básica
wshot --help

# Verificación completa con script de test
python test_installation.py
```

**Dependencias del sistema (opcional):**

Si encuentras errores relacionados con librerías del sistema faltantes, instálalas según tu distribución:

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

### Instalación desde el repositorio (Desarrollo)

Si quieres desarrollar o contribuir al proyecto:

```bash
git clone https://github.com/DanielMartinezSebastian/wshot.git
cd wshot

# Instalar en modo desarrollo
pip install -e .
playwright install chromium
```

## 🎯 Uso Básico

### Capturar todos los dispositivos:
```bash
wshot https://example.com -all
```

### Capturar dispositivo específico:
```bash
# Dispositivos más comunes (nombres cortos)
wshot https://example.com --device mobile     # iPhone 15 (predeterminado móvil)
wshot https://example.com --device tablet     # iPad (predeterminado tablet)
wshot https://example.com --device laptop     # Portátil 13" (predeterminado)
wshot https://example.com --device desktop    # Monitor Full HD (predeterminado)

# Móviles específicos
wshot https://example.com --device iphone-se
wshot https://example.com --device iphone-17
wshot https://example.com --device galaxy-s23
wshot https://example.com --device pixel-7

# Tablets específicos
wshot https://example.com --device ipad-pro
wshot https://example.com --device galaxy-tab-s9

# Portátiles específicos
wshot https://example.com --device laptop-15
wshot https://example.com --device laptop-16

# Desktop/Monitores específicos
wshot https://example.com --device desktop-2k
wshot https://example.com --device desktop-4k
```

### 🚀 Modo Super (Recomendado para sitios complejos):
```bash
wshot https://example.com --super
# Activa automáticamente: TODOS los dispositivos + scroll suave + tiempo optimizado (2s) + OpenGraph
# Equivale a: -all + --smooth-scroll + --open-graph + --wait-time 2
```

### ⚙️ Opciones avanzadas:
```bash
# Con tiempo de espera personalizado para animaciones
wshot https://example.com --device desktop --wait-time 7

# Con scroll suave para disparar animaciones basadas en scroll  
wshot https://example.com -all --smooth-scroll

# Cerrar automáticamente banners de cookies y pop-ups
wshot https://example.com --device desktop --auto-dismiss

# Extraer metadatos OpenGraph (og:title, og:description, og:image, etc.)
wshot https://example.com --device desktop --open-graph
# O usar el alias corto:
wshot https://example.com --device desktop --og

# Abrir explorador de archivos automáticamente al finalizar
wshot https://example.com --super --open

# Combinando opciones (recomendado para sitios con cookies)
wshot https://example.com --device tablet --wait-time 4 --smooth-scroll --auto-dismiss --og --open
```

### 📖 Ver ayuda:
```bash
wshot --help      # Ayuda estándar
wshot --info      # Guía completa con ejemplos
```

## 📱 Dispositivos Disponibles

| Dispositivo | Dimensiones | Descripción | Categoría |
|-------------|-------------|-------------|-----------|
| **📱 Móviles** ||||
| `mobile` | 393×852 | iPhone 15 (predeterminado móvil) | Móvil estándar |
| `iphone-se` | 375×667 | iPhone SE (2022) | Móvil compacto |
| `iphone-15-pro` | 393×852 | iPhone 15 Pro | Móvil premium |
| `iphone-17` | 402×874 | iPhone 17 (2025) | Móvil futuro |
| `galaxy-s23` | 360×780 | Samsung Galaxy S23 | Android estándar |
| `galaxy-s23-ultra` | 412×915 | Samsung Galaxy S23 Ultra | Android premium |
| `pixel-7` | 412×892 | Google Pixel 7 | Android puro |
| **📱 Tablets** ||||
| `tablet` | 768×1024 | iPad (10.9") - predeterminado tablet | Tablet estándar |
| `ipad-pro` | 1024×1366 | iPad Pro (12.9") | Tablet profesional |
| `galaxy-tab-s9` | 800×1280 | Samsung Galaxy Tab S9 | Android tablet |
| **💻 Portátiles** ||||
| `laptop` | 1280×800 | Portátil 13" (predeterminado laptop) | Portátil compacto |
| `laptop-15` | 1440×900 | MacBook Pro 15" / ThinkPad X1 | Portátil estándar |
| `laptop-16` | 1728×1117 | MacBook Pro 16" | Portátil premium |
| **🖥️ Desktop** ||||
| `desktop` | 1920×1080 | Monitor Full HD (predeterminado) | Desktop estándar |
| `desktop-2k` | 2560×1440 | Monitor 2K/QHD | Desktop premium |
| `desktop-4k` | 3840×2160 | Monitor 4K/UHD | Desktop profesional |

### 🏷️ Dispositivos Específicos (nombres largos)
| Dispositivo | Dimensiones | Descripción |
|-------------|-------------|-------------|
| `iphone-15` | 393×852 | Alias para `mobile` |
| `ipad` | 768×1024 | Alias para `tablet` |
| `laptop-13` | 1280×800 | Alias para `laptop` |
| `desktop-fhd` | 1920×1080 | Alias para `desktop` |

### 🏷️ Dispositivos Legacy (compatibilidad)
| Dispositivo | Dimensiones | Descripción |
|-------------|-------------|-------------|
| `mobile-se` | 375×667 | Alias para `iphone-se` |
| `mobile-17` | 393×852 | Alias para `iphone-15` (legacy) |

## 📂 Estructura de Salida

**Ubicación por defecto:**
- 📁 `~/Pictures/WSHOT/` (carpeta en Pictures del usuario)
- 📁 O ruta personalizada con `--output-dir ~/Proyectos/Capturas`

```
~/Pictures/WSHOT/
├── example.com/                    # Dominio completo extraído de la URL
│   ├── mobile/                     # Solo carpetas solicitadas
│   │   ├── example.com_pagina-principal-mobile-20241005_142958.png           # Viewport
│   │   └── example.com_pagina-principal-mobile-completa-20241005_142958.png  # Página completa
│   ├── tablet/
│   │   ├── example.com_contacto-tablet-20241005_142958.png
│   │   └── example.com_contacto-tablet-completa-20241005_142958.png
│   ├── laptop/
│   │   ├── example.com_servicios-laptop-20241005_142958.png
│   │   └── example.com_servicios-laptop-completa-20241005_142958.png
│   ├── desktop/
│   │   ├── example.com_pagina-principal-desktop-20241005_142958.png
│   │   └── example.com_pagina-principal-desktop-completa-20241005_142958.png
│   └── opengraph/                  # Metadatos OpenGraph (si se usa --og o --all)
│       ├── opengraph-20241005_142958.json     # Todos los metadatos
│       └── og-image-20241005_142958.jpg       # Imagen social descargada
```

**Con `--all` o `--super` se crean todas las carpetas automáticamente:**
```
~/Pictures/WSHOT/example.com/
├── mobile/           # iPhone 15 (predeterminado móvil)
├── iphone-se/
├── iphone-15-pro/
├── iphone-17/
├── galaxy-s23/
├── galaxy-s23-ultra/
├── pixel-7/
├── tablet/           # iPad (predeterminado tablet)
├── ipad-pro/
├── galaxy-tab-s9/
├── laptop/           # Portátil 13" (predeterminado)
├── laptop-15/
├── laptop-16/
├── desktop/          # Monitor Full HD (predeterminado)
├── desktop-2k/
├── desktop-4k/
└── opengraph/    ← Incluye JSON + imagen og:image
```

## 🛡️ Validación de URLs

Wshot verifica automáticamente que las URLs sean válidas antes de proceder:

```bash
# ✅ URL válida
wshot https://google.com -all
# 🔍 Validando URL...
# ✅ URL válida (Status: 200)
# 📁 Creando capturas...

# ❌ URL inexistente
wshot https://sitio-que-no-existe.com -all
# 🔍 Validando URL...
# ❌ Error: La URL no responde
# ❌ No se crean carpetas
```

## ⚙️ Opciones Avanzadas

### Todas las opciones disponibles:
```bash
# Especificar cliente manualmente:
wshot https://example.com -all --cliente "MiCliente"

# Control de tiempo de espera para animaciones (default: 3 segundos):
wshot https://example.com --device desktop --wait-time 5

# Scroll suave para disparar animaciones basadas en scroll:
wshot https://example.com -all --smooth-scroll

# Modo super (combina lo mejor de todo):
wshot https://example.com --super
# Equivale a: -all + --smooth-scroll + --open-graph + --wait-time 2
# ↑ Captura TODOS los dispositivos disponibles automáticamente
```

### 📖 Sistema de ayuda:
```bash
wshot --help      # Ayuda rápida con todas las opciones
wshot --info      # Guía completa con ejemplos detallados
```

### 🎛️ Lista completa de parámetros:
| Parámetro | Descripción | Ejemplo |
|-----------|-------------|---------|
| `URL` | URL del sitio web a capturar | `https://example.com` |
| `-all, --all-devices` | Capturar en todos los dispositivos | `-all` |
| `--device DEVICE` | Dispositivo específico | `--device mobile` |
| `--cliente NOMBRE` | Nombre personalizado del cliente | `--cliente "MiEmpresa"` |
| `--output-dir PATH` | Directorio personalizado de salida | `--output-dir ~/Proyectos` |
| `--wait-time SEGUNDOS` | Tiempo de espera para animaciones | `--wait-time 5` |
| `--smooth-scroll` | Scroll suave antes de captura completa | `--smooth-scroll` |
| `--auto-dismiss` | 🤖 Cerrar automáticamente banners de cookies y pop-ups | `--auto-dismiss` |
| `--open-graph, --og` | 📊 Extraer metadatos OpenGraph y descargar imagen social | `--og` |
| `--super` | 🚀 Modo completo optimizado (TODOS los dispositivos + OpenGraph + scroll suave) | `--super` |
| `--open` | 📂 Abrir explorador de archivos al finalizar | `--open` |
| `--help, -h` | Ayuda estándar | `--help` |
| `--info` | Guía completa extendida | `--info` |

## 🎨 Tipos de Captura

### 📏 **Viewport (Normal)**
Captura el área visible del navegador según el tamaño del dispositivo.

### 📜 **Completa (Full Page)**
Captura toda la página incluyendo contenido scrolleable (`full_page=True`).

## ✨ Características Destacadas

### 🤖 **Cierre Automático de Pop-ups**
```bash
# Cerrar automáticamente banners de cookies, avisos GDPR y otros pop-ups
wshot https://site.com --device desktop --auto-dismiss

# Combinar con otras opciones para capturas perfectas
wshot https://site.com --super --auto-dismiss
```

**¿Qué hace?**
- 🍪 Detecta y cierra automáticamente banners de cookies
- 📋 Cierra avisos de privacidad y consentimiento GDPR
- 🚫 Elimina pop-ups que bloquean la vista de la página
- 🌍 Soporte multiidioma (español, inglés, francés, alemán, italiano, portugués)
- 🎯 Compatible con frameworks populares: OneTrust, Cookiebot, Quantcast, TrustArc, Osano

### 📊 **Extracción de Metadatos OpenGraph**
```bash
# Extraer metadatos OpenGraph de cualquier página
wshot https://site.com --device desktop --open-graph
# O usar el alias corto:
wshot https://site.com --device desktop --og

# Se activa automáticamente con --all y --super
wshot https://site.com --all  # ← OpenGraph incluido
wshot https://site.com --super  # ← OpenGraph incluido
```

**¿Qué extrae?**
- 🏷️ **og:title** - Título para redes sociales
- 📝 **og:description** - Descripción optimizada
- 🖼️ **og:image** - Imagen social (descargada automáticamente)
- 🌐 **og:url** - URL canónica
- 🎯 **og:type** - Tipo de contenido (website, article, etc.)
- 📱 **og:site_name** - Nombre del sitio
- 🐦 **Twitter Card** - Metadatos de Twitter
- 📄 Y muchos más...

### ⏳ **Control de Animaciones**
```bash
# Tiempo de espera personalizado para que carguen animaciones (default: 3s)
wshot https://site.com --wait-time 5
```
Perfecto para sitios con animaciones CSS, JavaScript o contenido que se carga con delay.

### 📜 **Scroll Suave Inteligente**
```bash
# Scroll gradual para disparar animaciones basadas en scroll
wshot https://site.com --smooth-scroll
```
Ideal para:
- Sitios con **lazy loading**
- Efectos **parallax**
- Animaciones activadas por **intersection observer**
- Contenido que aparece al hacer scroll

### 🚀 **Modo Super (Todo-en-Uno)**
```bash
# Un solo comando para captura completa optimizada
wshot https://site.com --super
```
**Activa automáticamente:**
- ✅ **Todos los dispositivos** (`-all`) - Captura en mobile, tablet, laptop, desktop y todas las variantes
- ✅ Scroll suave (`--smooth-scroll`)
- ✅ Extracción OpenGraph (`--open-graph`)
- ✅ Tiempo optimizado (`--wait-time 2`)

### 📂 **Abrir Explorador de Archivos Automáticamente**
```bash
# Abrir explorador al finalizar (multiplataforma)
wshot https://site.com --super --open

# En Windows abre Explorer
# En macOS abre Finder  
# En Linux detecta tu gestor: Dolphin (KDE), Nautilus (GNOME), Thunar (XFCE), etc.
```

## 🔧 Requisitos

- Python 3.8+
- Playwright (instalado automáticamente con pip)
- Requests (instalado automáticamente con pip)
- Conexión a internet

## 📄 Ejemplos Prácticos

```bash
# Capturar página de contacto en todos los dispositivos (básico)
wshot https://miempresa.com/contacto -all

# Capturar en el móvil más popular (iPhone 15)
wshot https://mitienda.com/productos --device mobile

# Comparar en Android vs iPhone
wshot https://miapp.com --device galaxy-s23
wshot https://miapp.com --device mobile

# Capturar en tablet profesional con tiempo de espera extra
wshot https://miblog.com --device ipad-pro --wait-time 6

# Verificar en portátil más común (13 pulgadas)
wshot https://mi-dashboard.com --device laptop

# Auditoría en monitor 4K profesional
wshot https://mi-portfolio.com --device desktop-4k

# Sitio con banner de cookies - cerrar automáticamente
wshot https://google.com --device desktop --auto-dismiss

# Extraer solo metadatos OpenGraph sin capturas
wshot https://miempresa.com --device mobile --og

# Sitio con muchas animaciones - usar modo super y abrir explorador
wshot https://sitio-animado.com --super --open

# Sitio con lazy loading, cookies y OpenGraph - combinación completa
wshot https://sitio-parallax.com -all --smooth-scroll --auto-dismiss

# Auditoría SEO completa: capturas + metadatos OpenGraph
wshot https://cliente-importante.com --super --cliente "ClienteVIP"

# Comparación móvil compacto vs premium
wshot https://responsive.com --device iphone-se
wshot https://responsive.com --device galaxy-s23-ultra

# Verificación en dispositivos de trabajo más comunes
wshot https://intranet.com --device laptop --auto-dismiss

# Guardar en ubicación personalizada y abrir automáticamente
wshot https://proyecto.com --super --output-dir ~/Proyectos/AuditoriasWeb --open
```

### 🎯 Casos de uso recomendados:

| Tipo de sitio | Comando recomendado | Razón |
|---------------|---------------------|-------|
| **Sitio estático simple** | `--device desktop` | Rápido y eficiente |
| **Sitio responsive** | `-all` | Ver en todos los dispositivos + OpenGraph |
| **App móvil/PWA** | `--device mobile --device galaxy-s23` | Probar en móviles más populares |
| **Dashboard/Admin** | `--device laptop` | Resolución típica de trabajo |
| **E-commerce** | `--device mobile --device tablet --device desktop` | Cubrir compras móviles y desktop |
| **Portfolio/Landing** | `--device desktop-4k` | Mostrar máxima calidad visual |
| **Sitio con animaciones** | `--super` | Tiempo optimizado + scroll + OpenGraph |
| **Sitio con lazy loading** | `--smooth-scroll` | Activa el contenido diferido |
| **Sitio con cookies/GDPR** | `--auto-dismiss` | Cierra banners automáticamente |
| **Auditoría SEO** | `--super` | Capturas completas + metadatos OpenGraph |
| **Google, Facebook, etc.** | `--super --auto-dismiss` | Capturas limpias sin pop-ups + metadatos |
| **Auditoría completa** | `--super --auto-dismiss` | Captura exhaustiva sin obstrucciones + SEO |
| **Sitio lento** | `--wait-time 7` | Más tiempo para cargar |
| **Comparación de marcas** | `--device mobile --device galaxy-s23` | iPhone vs Android |

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📜 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 🛠️ Desarrollo

### Estructura del proyecto:
```
wshot/
├── wshot/                   # Paquete Python principal
│   ├── __init__.py         # Módulo del paquete
│   └── cli.py              # Código principal CLI
├── pyproject.toml          # Configuración del proyecto (PEP 621)
├── MANIFEST.in             # Archivos incluidos en distribución
├── test_installation.py    # Script de verificación
├── .gitignore              # Archivos a ignorar en Git
├── LICENSE                 # Licencia MIT
└── README.md               # Este archivo
```

### Ejecutar en modo desarrollo:
```bash
# Instalar en modo editable
pip install -e .
playwright install chromium

# Ejecutar
wshot https://example.com --device mobile-17

# O usando el modo super para pruebas completas:
wshot https://example.com --super
```

## 🔧 Troubleshooting (Solución de Problemas)

### Problema: "libicudata.so.66 not found" u otras librerías faltantes

**Síntoma:** Error al ejecutar capturas mencionando librerías `.so` faltantes.

**Solución:**
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install -y libnss3 libnspr4 libatk1.0-0 \
  libatk-bridge2.0-0 libcups2 libdrm2 libxkbcommon0 libxcomposite1 \
  libxdamage1 libxfixes3 libxrandr2 libgbm1 libpango-1.0-0 libcairo2 libasound2

# Fedora
sudo dnf install -y nss nspr atk at-spi2-atk cups-libs libdrm \
  libxkbcomposite libxdamage libXrandr libgbm pango cairo alsa-lib

# Arch Linux
sudo pacman -S nss nspr atk at-spi2-atk cups libdrm libxkbcommon \
  libxcomposite libxdamage libxrandr mesa pango cairo alsa-lib
```

### Problema: "playwright: command not found"

**Síntoma:** No se encuentra el comando playwright.

**Solución:**
```bash
# Reinstalar playwright
pip install playwright
playwright install chromium
```

### Problema: Las capturas salen en negro o vacías

**Síntoma:** Las imágenes capturadas están en negro o no muestran contenido.

**Solución:**
```bash
# 1. Verificar instalación
python test_installation.py

# 2. Aumentar tiempo de espera
wshot https://sitio.com --device desktop --wait-time 10

# 3. Usar modo super con scroll suave
wshot https://sitio.com --super
```

### Verificación completa del sistema

Si tienes múltiples problemas:

```bash
# 1. Verificar estado actual
python test_installation.py

# 2. Reinstalar desde cero
pip uninstall wshot
pip install git+https://github.com/DanielMartinezSebastian/wshot.git
playwright install chromium

# 3. Prueba funcional
wshot https://example.com --device desktop
```

### Obtener ayuda adicional

Si ninguna solución funciona:

1. **Revisa los logs detallados**:
   ```bash
   wshot https://sitio.com --device desktop 2>&1 | tee error.log
   ```

2. **Información del sistema**:
   ```bash
   python3 --version
   lsb_release -a  # o cat /etc/os-release
   ```

3. **Abre un issue en GitHub** con:
   - Salida de `python test_installation.py`
   - Contenido de `error.log`
   - Información del sistema
   - Comando que estabas ejecutando

---

## 🎉 Evolución del Proyecto

### v1.0.0 - Plataforma de Auditoría Visual Empresarial 🏢
- ✅ **Arquitectura empresarial**: Refactorización completa como plataforma Python distribuible
- ✅ **Comando global unificado**: `wshot` disponible sistema-wide tras instalación pip
- ✅ **Estructura organizacional avanzada**: Eliminación de redundancias y arquitectura limpia
- ✅ **Configuración moderna PEP 621**: `pyproject.toml` con estándares de industria
- ✅ **Instalación simplificada**: `pip install git+https://...` para deploy inmediato
- ✅ **Suite de verificación**: `test_installation.py` para validación de entornos
- ✅ **Modo desarrollo**: `pip install -e .` para contribuidores

### 🏗️ **Capacidades Técnicas Implementadas**
- 📱 **Motor multi-dispositivo**: 15+ configuraciones desde móviles compactos hasta monitores 4K profesionales
- 🛡️ **Sistema de validación robusto**: Verificación preventiva de URLs con manejo de errores
- 📁 **Organización semántica**: Estructura automática por dominio completo con nomenclatura descriptiva
- ⏳ **Motor de renderizado avanzado**: Control granular de timing para sitios con animaciones complejas
- 📜 **Scroll progresivo inteligente**: Activación automática de lazy loading y efectos parallax
- 🤖 **IA para eliminación de obstáculos**: Detección y cierre automático de banners GDPR/cookies multiidioma
- 📊 **Extractor de metadatos estructurados**: Sistema completo OpenGraph con descarga automática de assets
- 🚀 **Modo auditoría unificado**: Super-mode para evaluaciones empresariales completas
- 📂 **Integración del sistema**: Apertura automática de exploradores de archivos multiplataforma
- 📖 **Documentación técnica extensiva**: Sistema de ayuda contextual para equipos de desarrollo