# 📸 ScriptShotWeb

Una herramienta profesional para capturar pantallas de sitios web en múltiples dispositivos y resoluciones, optimizada para sitios modernos con animaciones y contenido dinámico.

## ✨ Características

- 🚀 **Sintaxis ultra-simple**: `scriptshotweb URL -all`
- 📱 **Múltiples dispositivos**: iPhone SE, iPhone 17, iPad, Desktop
- 🔄 **Doble captura**: Viewport + página completa scrolleable
- 🛡️ **Validación inteligente**: Verifica URLs antes de crear carpetas
- 📁 **Organización automática**: Carpetas por cliente y dispositivo
- ⚡ **Sin configuración manual**: Todo automatizado
- 📂 **Capturas organizadas**: Guarda en ./capturas/ del proyecto por defecto
- ⏳ **Control de animaciones**: Tiempo de espera configurable para animaciones (3s por defecto)
- 📜 **Scroll inteligente**: Scroll suave para disparar animaciones basadas en scroll
- 🚀 **Modo Super**: Captura optimizada completa con un solo comando
- 📖 **Ayuda completa**: Sistema de ayuda extensivo con `--help` e `--info`

## 🚩 Próximas Features

- [x] ~~Realizar captura completa de la url navegando primero hasta abajo para disparar animaciones basadas en scroll~~ ✅ **COMPLETADO**
- [x] ~~Control de tiempo de espera para animaciones~~ ✅ **COMPLETADO**
- [x] ~~Modo super para captura completa optimizada~~ ✅ **COMPLETADO**
- [x] ~~Alojar las capturas dentro de una carpeta general como downloads o similar en lugar de simplemente en la carpeta del script~~ ✅ **COMPLETADO**
- [ ] Refactorizar para homogeneizar uso de idioma castellano vs ingles
- [ ] Obtener capturas en webp optimizado
- [ ] Capturar webs completas navegando por todos los links bajo ese dominio para obtener toda la web
- [ ] Scrapear contenido en formato .md
- [ ] Obtener todo el contenido media que exista en la url objetivo
## 🚀 Instalación

### Opción 1: Instalación Automática (Recomendada)
```bash
git clone https://github.com/DanielMartinezSebastian/scriptshotweb.git
cd scriptshotweb
./install.sh
```

### Opción 2: Instalación Manual
1. **Clonar repositorio**:
```bash
git clone https://github.com/DanielMartinezSebastian/scriptshotweb.git
cd scriptshotweb
```

2. **Configurar entorno virtual**:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

3. **Hacer ejecutable**:
```bash
chmod +x scriptshotweb.sh
```

## 🎯 Uso Básico

### Capturar todos los dispositivos:
```bash
./scriptshotweb.sh https://example.com -all
```

### Capturar dispositivo específico:
```bash
./scriptshotweb.sh https://example.com --device mobile-17
./scriptshotweb.sh https://example.com --device tablet
./scriptshotweb.sh https://example.com --device desktop
```

### 🚀 Modo Super (Recomendado para sitios complejos):
```bash
./scriptshotweb.sh https://example.com --super
# Activa automáticamente: todos los dispositivos + scroll suave + tiempo optimizado (2s)
```

### ⚙️ Opciones avanzadas:
```bash
# Con tiempo de espera personalizado para animaciones
./scriptshotweb.sh https://example.com --device desktop --wait-time 7

# Con scroll suave para disparar animaciones basadas en scroll  
./scriptshotweb.sh https://example.com -all --smooth-scroll

# Combinando opciones
./scriptshotweb.sh https://example.com --device tablet --wait-time 4 --smooth-scroll
```

### 📖 Ver ayuda:
```bash
./scriptshotweb.sh --help      # Ayuda estándar
./scriptshotweb.sh --info      # Guía completa con ejemplos
```

## 📱 Dispositivos Disponibles

| Dispositivo | Dimensiones | Descripción |
|-------------|-------------|-------------|
| `mobile-se` | 375×667 | iPhone SE |
| `mobile-17` | 393×852 | iPhone 17 |
| `tablet` | 768×1024 | iPad |
| `desktop` | 1920×1080 | Desktop |

## 📂 Estructura de Salida

**Ubicación por defecto:**
- 📁 `./capturas/` (carpeta en el directorio del proyecto)
- 📁 O ruta personalizada con `--output-dir ~/Pictures/ScriptShotWeb`

```
scriptshotweb/
├── capturas/
│   └── example/                    # Nombre extraído de la URL
│       ├── mobile-17/             # Solo carpetas solicitadas
│       │   ├── pagina-mobile-17-20231004_142958.png           # Viewport
│       │   └── pagina-mobile-17-completa-20231004_142958.png  # Página completa
│       └── tablet/
│           ├── pagina-tablet-20231004_142958.png
│           └── pagina-tablet-completa-20231004_142958.png
└── scriptshotweb
```

## 🛡️ Validación de URLs

ScriptShotWeb verifica automáticamente que las URLs sean válidas antes de proceder:

```bash
# ✅ URL válida
./scriptshotweb.sh https://google.com -all
# 🔍 Validando URL...
# ✅ URL válida (Status: 200)
# 📁 Creando capturas...

# ❌ URL inexistente
./scriptshotweb.sh https://sitio-que-no-existe.com -all
# 🔍 Validando URL...
# ❌ Error: La URL no responde
# ❌ No se crean carpetas
```

## ⚙️ Opciones Avanzadas

### Todas las opciones disponibles:
```bash
# Especificar cliente manualmente:
./scriptshotweb.sh https://example.com -all --cliente "MiCliente"

# Control de tiempo de espera para animaciones (default: 3 segundos):
./scriptshotweb.sh https://example.com --device desktop --wait-time 5

# Scroll suave para disparar animaciones basadas en scroll:
./scriptshotweb.sh https://example.com -all --smooth-scroll

# Modo super (combina lo mejor de todo):
./scriptshotweb.sh https://example.com --super
# Equivale a: -all + --smooth-scroll + --wait-time 2
```

### 📖 Sistema de ayuda:
```bash
./scriptshotweb.sh --help      # Ayuda rápida con todas las opciones
./scriptshotweb.sh --info      # Guía completa con ejemplos detallados
```

### 🎛️ Lista completa de parámetros:
| Parámetro | Descripción | Ejemplo |
|-----------|-------------|---------|
| `URL` | URL del sitio web a capturar | `https://example.com` |
| `-all, --all-devices` | Capturar en todos los dispositivos | `-all` |
| `--device DEVICE` | Dispositivo específico | `--device mobile-17` |
| `--cliente NOMBRE` | Nombre personalizado del cliente | `--cliente "MiEmpresa"` |
| `--output-dir PATH` | Directorio personalizado de salida | `--output-dir ~/Proyectos` |
| `--wait-time SEGUNDOS` | Tiempo de espera para animaciones | `--wait-time 5` |
| `--smooth-scroll` | Scroll suave antes de captura completa | `--smooth-scroll` |
| `--super` | 🚀 Modo completo optimizado | `--super` |
| `--help, -h` | Ayuda estándar | `--help` |
| `--info` | Guía completa extendida | `--info` |

## 🎨 Tipos de Captura

### 📏 **Viewport (Normal)**
Captura el área visible del navegador según el tamaño del dispositivo.

### 📜 **Completa (Full Page)**
Captura toda la página incluyendo contenido scrolleable (`full_page=True`).

## ✨ Nuevas Características (v2.0)

### ⏳ **Control de Animaciones**
```bash
# Tiempo de espera personalizado para que carguen animaciones (default: 3s)
./scriptshotweb.sh https://site.com --wait-time 5
```
Perfecto para sitios con animaciones CSS, JavaScript o contenido que se carga con delay.

### 📜 **Scroll Suave Inteligente**
```bash
# Scroll gradual para disparar animaciones basadas en scroll
./scriptshotweb.sh https://site.com --smooth-scroll
```
Ideal para:
- Sitios con **lazy loading**
- Efectos **parallax**
- Animaciones activadas por **intersection observer**
- Contenido que aparece al hacer scroll

### 🚀 **Modo Super (Todo-en-Uno)**
```bash
# Un solo comando para captura completa optimizada
./scriptshotweb.sh https://site.com --super
```
**Activa automáticamente:**
- ✅ Todos los dispositivos (`-all`)
- ✅ Scroll suave (`--smooth-scroll`)
- ✅ Tiempo optimizado (`--wait-time 2`)

**Recomendado para:**
- Sitios complejos con animaciones
- Auditorías completas
- Sitios modernos con efectos avanzados

### 📖 **Sistema de Ayuda Extendido**
```bash
./scriptshotweb.sh --help      # Ayuda rápida
./scriptshotweb.sh --info      # Guía completa con ejemplos
```

### 📂 **Ubicación de Archivos**
```bash
# Por defecto guarda en ./capturas/ dentro del proyecto
./scriptshotweb.sh https://site.com --super

# Especificar ubicación personalizada (ej: Pictures o Downloads)
./scriptshotweb.sh https://site.com --super --output-dir ~/Pictures/ScriptShotWeb
./scriptshotweb.sh https://site.com --super --output-dir ~/Downloads/Capturas
```
**Beneficios:**
- ✅ Mantiene las capturas organizadas en el proyecto
- ✅ Fácil de encontrar y gestionar
- ✅ Opción de mover a Pictures/Downloads si lo prefieres
- ✅ Compatible con .gitignore para no subir capturas al repo

## 🔧 Requisitos

- Python 3.7+
- Playwright
- Requests
- Conexión a internet

## 📄 Ejemplos Prácticos

```bash
# Capturar página de contacto en todos los dispositivos (básico)
./scriptshotweb.sh https://miempresa.com/contacto -all

# Capturar solo en móvil iPhone 17
./scriptshotweb.sh https://mitienda.com/productos --device mobile-17

# Capturar página principal en tablet con tiempo de espera extra
./scriptshotweb.sh https://miblog.com --device tablet --wait-time 6

# Sitio con muchas animaciones - usar modo super
./scriptshotweb.sh https://sitio-animado.com --super

# Sitio con lazy loading - usar scroll suave
./scriptshotweb.sh https://sitio-parallax.com -all --smooth-scroll

# Captura completa optimizada para auditoría
./scriptshotweb.sh https://cliente-importante.com --super --cliente "ClienteVIP"

# Guardar en ubicación personalizada
./scriptshotweb.sh https://proyecto.com --super --output-dir ~/Proyectos/AuditoriasWeb
```

### 🎯 Casos de uso recomendados:

| Tipo de sitio | Comando recomendado | Razón |
|---------------|---------------------|-------|
| **Sitio estático simple** | `--device desktop` | Rápido y eficiente |
| **Sitio responsive** | `-all` | Ver en todos los dispositivos |
| **Sitio con animaciones** | `--super` | Tiempo optimizado + scroll |
| **Sitio con lazy loading** | `--smooth-scroll` | Activa el contenido diferido |
| **Auditoría completa** | `--super` | Captura exhaustiva |
| **Sitio lento** | `--wait-time 7` | Más tiempo para cargar |

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
scriptshotweb/
├── scriptshotweb.sh      # Script principal (wrapper)
├── scriptshotweb         # Script Python core
├── install.sh           # Script de instalación automática
├── requirements.txt     # Dependencias Python
├── .venv/              # Entorno virtual
├── .gitignore          # Archivos a ignorar en Git
├── LICENSE             # Licencia MIT
└── README.md           # Este archivo
```

### Ejecutar en modo desarrollo:
```bash
source .venv/bin/activate
python scriptshotweb https://example.com --device mobile-17

# O usando el modo super para pruebas completas:
python scriptshotweb https://example.com --super
```

---

## 🎉 Changelog

### v2.1 - Mejoras de Organización
- ✅ Organización en carpeta ./capturas/ por defecto
- ✅ Soporte para directorios personalizados (`--output-dir`)
- ✅ Optimización del modo super (2s en lugar de 5s)
- ✅ Mejoras en velocidad de scroll (0.08s por paso)

### v2.0 - Nuevas Características
- ✅ Control de tiempo de espera para animaciones (`--wait-time`)
- ✅ Scroll suave para disparar animaciones (`--smooth-scroll`) 
- ✅ Modo super optimizado (`--super`)
- ✅ Sistema de ayuda extendido (`--help`, `--info`)
- ✅ Mejor manejo de sitios modernos con animaciones

### v1.0 - Funcionalidades Base
- ✅ Capturas multi-dispositivo
- ✅ Validación inteligente de URLs
- ✅ Organización automática de archivos
- ✅ Capturas viewport y página completa
