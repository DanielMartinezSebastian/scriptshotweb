# 📚 Documentación Completa - Wshot

Una plataforma integral de auditoría visual y análisis web que automatiza la captura, análisis y documentación de sitios web a escala empresarial. Diseñada para equipos de desarrollo, QA, diseñadores y consultores digitales que requieren evaluaciones exhaustivas de experiencia de usuario multiplataforma.

## 🎯 Características Principales

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

## 🚀 Instalación Detallada

### Instalación mediante pip (Recomendada) ⭐

Instala wshot como un paquete Python global o en un entorno virtual:

**Para la mayoría de sistemas:**
```bash
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

## 📂 Estructura de Salida Detallada

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

## ✨ Características Avanzadas

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

## 🎛️ Lista Completa de Parámetros

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

## 🔧 Requisitos

- Python 3.8+
- Playwright (instalado automáticamente con pip)
- Requests (instalado automáticamente con pip)
- Conexión a internet

## 📄 Ejemplos Prácticos Avanzados

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

### 🎯 Casos de Uso Empresariales

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

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

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