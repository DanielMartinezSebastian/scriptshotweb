# 📱 Devices - Wshot

Complete reference of all available devices for screenshot capture.

## 📱 Mobile Devices

### iPhone
| Device | Dimensions | Description | Alias |
|--------|------------|-------------|-------|
| `mobile` | 393×852 | iPhone 15 (default mobile) | `iphone-15` |
| `iphone-se` | 375×667 | iPhone SE (2022) | `mobile-se` |
| `iphone-15-pro` | 393×852 | iPhone 15 Pro | - |
| `iphone-17` | 402×874 | iPhone 17 (2025) | `mobile-17` |

### Android
| Device | Dimensions | Description | Alias |
|--------|------------|-------------|-------|
| `galaxy-s23` | 360×780 | Samsung Galaxy S23 | - |
| `galaxy-s23-ultra` | 412×915 | Samsung Galaxy S23 Ultra | - |
| `pixel-7` | 412×892 | Google Pixel 7 | - |

## 📟 Tablets

### iPad
| Device | Dimensions | Description | Alias |
|--------|------------|-------------|-------|
| `tablet` | 768×1024 | iPad (10.9") - default tablet | `ipad` |
| `ipad-pro` | 1024×1366 | iPad Pro (12.9") | - |

### Android Tablets
| Device | Dimensions | Description | Alias |
|--------|------------|-------------|-------|
| `galaxy-tab-s9` | 800×1280 | Samsung Galaxy Tab S9 | - |

## 💻 Laptops

| Device | Dimensions | Description | Alias |
|--------|------------|-------------|-------|
| `laptop` | 1280×800 | 13" Laptop (default laptop) | `laptop-13` |
| `laptop-15` | 1440×900 | MacBook Pro 15" / ThinkPad X1 | - |
| `laptop-16` | 1728×1117 | MacBook Pro 16" | - |

## 🖥️ Desktop/Monitors

| Device | Dimensions | Description | Alias |
|--------|------------|-------------|-------|
| `desktop` | 1920×1080 | Full HD Monitor (default) | `desktop-fhd` |
| `desktop-2k` | 2560×1440 | 2K/QHD Monitor | - |
| `desktop-4k` | 3840×2160 | 4K/UHD Monitor | - |

## 🎯 Dispositivos Recomendados por Categoría

### Móviles Más Populares
1. **`mobile`** (iPhone 15) - 393×852
2. **`galaxy-s23`** (Samsung) - 360×780
3. **`iphone-se`** (Compacto) - 375×667

### Tablets Más Comunes
1. **`tablet`** (iPad estándar) - 768×1024
2. **`ipad-pro`** (Profesional) - 1024×1366

### Portátiles Estándar
1. **`laptop`** (13" estándar) - 1280×800
2. **`laptop-15`** (15" profesional) - 1440×900

### Desktop Profesional
1. **`desktop`** (Full HD estándar) - 1920×1080
2. **`desktop-4k`** (4K profesional) - 3840×2160

## 📊 Comparativa de Resoluciones

### Por Categoría de Pantalla

#### 📱 Móviles (Portrait)
```
iphone-se      ████████████████                375×667
galaxy-s23     ██████████████████              360×780  
mobile         ████████████████████            393×852
iphone-15-pro  ████████████████████            393×852
galaxy-s23-ultra ███████████████████████       412×915
pixel-7        ███████████████████████         412×892
iphone-17      ████████████████████████        402×874
```

#### 📟 Tablets (Portrait)
```
tablet         ████████████████████████████████     768×1024
galaxy-tab-s9  ████████████████████████████████     800×1280
ipad-pro       ████████████████████████████████████ 1024×1366
```

#### 💻 Portátiles (Landscape)
```
laptop         ████████████████████████████████████████████████████ 1280×800
laptop-15      ████████████████████████████████████████████████████████████ 1440×900
laptop-16      ████████████████████████████████████████████████████████████████████ 1728×1117
```

#### 🖥️ Desktop (Landscape)
```
desktop        ████████████████████████████████████████████████████████████████████████████████ 1920×1080
desktop-2k     ████████████████████████████████████████████████████████████████████████████████████████████████ 2560×1440
desktop-4k     ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████ 3840×2160
```

## 🎮 Uso por Comandos

### Dispositivos Individuales
```bash
# Móviles
wshot https://example.com --device mobile
wshot https://example.com --device iphone-se
wshot https://example.com --device galaxy-s23

# Tablets
wshot https://example.com --device tablet
wshot https://example.com --device ipad-pro

# Portátiles
wshot https://example.com --device laptop
wshot https://example.com --device laptop-15

# Desktop
wshot https://example.com --device desktop
wshot https://example.com --device desktop-4k
```

### Combinaciones Populares
```bash
# Trio básico (móvil, tablet, desktop)
wshot https://example.com --device mobile
wshot https://example.com --device tablet  
wshot https://example.com --device desktop

# Comparación iPhone vs Android
wshot https://example.com --device mobile
wshot https://example.com --device galaxy-s23

# Gama completa móvil
wshot https://example.com --device iphone-se
wshot https://example.com --device mobile
wshot https://example.com --device galaxy-s23-ultra

# Professional Setup
wshot https://example.com --device laptop-15
wshot https://example.com --device desktop-4k
```

### Todos los Dispositivos
```bash
# Captura en TODOS los dispositivos automáticamente
wshot https://example.com -all

# Con modo super (incluye optimizaciones)
wshot https://example.com --super
```

## 🏷️ Aliases y Compatibilidad

### Nombres Alternativos
| Dispositivo Principal | Aliases Disponibles |
|----------------------|---------------------|
| `mobile` | `iphone-15` |
| `tablet` | `ipad` |
| `laptop` | `laptop-13` |
| `desktop` | `desktop-fhd` |
| `iphone-se` | `mobile-se` |
| `iphone-17` | `mobile-17` |

### Retrocompatibilidad
Todos los nombres de dispositivos de versiones anteriores siguen siendo compatibles para mantener scripts existentes funcionando.

## 🎯 Recomendaciones de Uso

### Para Testing Responsive
```bash
# Combo básico responsive
wshot site.com --device mobile --device tablet --device desktop

# Combo extendido
wshot site.com --device iphone-se --device mobile --device tablet --device laptop --device desktop-4k
```

### Para E-commerce
```bash
# Enfoque en dispositivos de compra
wshot tienda.com --device mobile --device tablet --device desktop
```

### Para Portfolios/Creativos
```bash
# Máxima calidad visual
wshot portfolio.com --device desktop-4k --device laptop-16
```

### Para Apps Móviles
```bash
# Comparación móvil completa
wshot app.com --device iphone-se --device mobile --device galaxy-s23 --device pixel-7
```

### Para Dashboards/Admin
```bash
# Resoluciones de trabajo típicas
wshot admin.com --device laptop --device desktop
```

## 🔄 Actualizaciones de Dispositivos

Los dispositivos se actualizan regularmente para reflejar:
- Nuevos lanzamientos de dispositivos populares
- Cambios en resoluciones estándar del mercado
- Feedback de la comunidad sobre dispositivos necesarios

Para sugerir nuevos dispositivos o modificaciones:
1. Abre un issue en GitHub
2. Incluye la resolución exacta y justificación
3. Proporciona fuentes sobre popularidad/uso del dispositivo

---

> **Nota**: Las resoluciones están basadas en viewport real de navegadores, no en resolución nativa de pantalla. Esto asegura capturas precisas de cómo los usuarios realmente ven los sitios web.