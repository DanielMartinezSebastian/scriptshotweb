# 📸 Wshot

Herramienta de captura de pantallas web automatizada para múltiples dispositivos. Ideal para auditorías visuales, testing responsive y documentación de proyectos web.

## 🚀 Instalación Rápida

```bash
pip install git+https://github.com/DanielMartinezSebastian/wshot.git
playwright install chromium
```

> ¿Problemas de instalación? Ver [DOCS.md](DOCS.md#-instalación-detallada) o [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

## ⚡ Uso Básico

```bash
# Capturar en todos los dispositivos
wshot https://example.com -all

# Dispositivo específico
wshot https://example.com --device mobile
wshot https://example.com --device desktop

# Modo super (recomendado)
wshot https://example.com --super
```

> Ver todos los comandos y opciones en [DOCS.md](DOCS.md#️-lista-completa-de-parámetros)

## 📱 Dispositivos Principales

| Dispositivo | Dimensiones | Uso |
|-------------|-------------|-----|
| `mobile` | 393×852 | iPhone 15 (móvil estándar) |
| `tablet` | 768×1024 | iPad (tablet estándar) |
| `laptop` | 1280×800 | Portátil 13" (estándar) |
| `desktop` | 1920×1080 | Monitor Full HD (estándar) |
| `desktop-4k` | 3840×2160 | Monitor 4K profesional |

> Ver lista completa en [DEVICES.md](DEVICES.md)

## 📂 Estructura de Salida

```
~/Pictures/WSHOT/
└── example.com/
    ├── mobile/
    │   ├── example.com_mobile-20241005_142958.png
    │   └── example.com_mobile-completa-20241005_142958.png
    └── desktop/
        ├── example.com_desktop-20241005_142958.png
        └── example.com_desktop-completa-20241005_142958.png
```

## ⚙️ Opciones Principales

```bash
# Todos los dispositivos
wshot https://example.com -all

# Dispositivo específico
wshot https://example.com --device mobile

# Modo super (recomendado para sitios complejos)
wshot https://example.com --super

# Con tiempo de espera personalizado
wshot https://example.com --device desktop --wait-time 5

# Cerrar automáticamente banners de cookies
wshot https://example.com --device desktop --auto-dismiss

# Extraer metadatos OpenGraph
wshot https://example.com --device desktop --og

# Abrir explorador al finalizar
wshot https://example.com --super --open
```

## 📖 Ayuda

```bash
wshot --help      # Ayuda rápida
wshot --info      # Guía completa
```

## 📚 Documentación

- **[DOCS.md](DOCS.md)** - Documentación completa y características avanzadas
- **[DEVICES.md](DEVICES.md)** - Lista completa de dispositivos disponibles
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Solución de problemas comunes
- **[ROADMAP.md](ROADMAP.md)** - Evolución y planes futuros del proyecto

## 📄 Licencia

MIT License - ver [LICENSE](LICENSE) para detalles.