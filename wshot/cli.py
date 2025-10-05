#!/usr/bin/env python3
"""
Wshot - Herramienta simplificada para capturas de pantalla web
Uso: wshot URL [-all] [--device DEVICE] [--wait-time SECONDS] [--smooth-scroll] [--super]

Ejemplos:
  wshot http://mariadelasmercedes.com/contacto -all
  wshot https://mecalito.com --device mobile-17
  wshot https://example.com --device tablet --wait-time 5 --smooth-scroll
  wshot https://site.com --super  # Modo completo optimizado
"""

import argparse
import sys
import platform
import subprocess
from pathlib import Path
from urllib.parse import urlparse
from datetime import datetime
import re
import time
# Importaciones de playwright y requests se harán más tarde para permitir que --help funcione

def mostrar_ayuda_extendida():
    """Muestra información adicional sobre el uso del script"""
    ayuda = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                               WSHOT - GUÍA COMPLETA                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

📖 DESCRIPCIÓN:
   Wshot es una herramienta profesional para realizar capturas de pantalla
   de sitios web en múltiples dispositivos, optimizada para sitios modernos con
   animaciones, efectos de scroll y contenido dinámico.

🎯 CARACTERÍSTICAS PRINCIPALES:
   • Capturas en 4 tamaños de dispositivo predefinidos
   • Soporte para animaciones y contenido que se carga con delay
   • Scroll suave para disparar animaciones basadas en scroll
   • Cierre automático de banners de cookies y pop-ups 🤖
   • Extracción de metadatos OpenGraph para SEO y redes sociales 📊
   • Organización automática de archivos por cliente y dispositivo
   • Modo super para captura completa optimizada

📱 DISPOSITIVOS DISPONIBLES:
   mobile-se  │ iPhone SE      │ 375 × 667   │ Móvil pequeño
   mobile-17  │ iPhone 17      │ 393 × 852   │ Móvil moderno  
   tablet     │ iPad           │ 768 × 1024  │ Tablet estándar
   desktop    │ Desktop        │ 1920 × 1080 │ Escritorio HD

🚀 MODOS DE USO:

   Básico (un dispositivo):
   $ wshot https://example.com --device desktop

   Completo (todos los dispositivos):  
   $ wshot https://example.com --all-devices

   Super optimizado (recomendado para sitios complejos):
   $ wshot https://example.com --super

⚙️  OPCIONES AVANZADAS:
   --wait-time SEGUNDOS    │ Tiempo de espera para animaciones (default: 3s)
   --smooth-scroll         │ Scroll suave antes de captura completa
   --auto-dismiss          │ Cerrar automáticamente banners de cookies y pop-ups 🤖
   --open-graph, --og      │ Extraer metadatos OpenGraph (og:*, Twitter Card) 📊
   --cliente NOMBRE        │ Nombre personalizado para organizar archivos
   --output-dir PATH       │ Directorio personalizado de salida
   --open                  │ Abrir explorador de archivos al finalizar

📂 ESTRUCTURA DE ARCHIVOS:
   Las capturas se guardan por defecto en:
   ./capturas/ (carpeta en el proyecto)
   └── [cliente]/
       ├── mobile-se/
       ├── mobile-17/ 
       ├── tablet/
       └── desktop/
           ├── pagina-viewport-20241004_143025.png
           └── pagina-completa-20241004_143025.png
   
   Usa --output-dir para guardar en otra ubicación como:
   ~/Pictures/Wshot o ~/Downloads/Wshot

💡 CONSEJOS:
   • Usa --super para sitios con muchas animaciones
   • Usa --wait-time mayor para sitios lentos
   • El scroll suave es ideal para lazy loading y parallax
   • Usa --auto-dismiss para sitios con banners de cookies molestos
   • Combina --auto-dismiss con --super para capturas perfectas sin pop-ups
   • Usa --og o --open-graph para extraer metadatos SEO y redes sociales
   • El modo --all y --super incluyen automáticamente extracción OpenGraph
   • Las URLs deben incluir http:// o https://

"""
    print(ayuda)

# Configuración de dispositivos/tamaños
TAMAÑOS = {
    "mobile-se": {"width": 375, "height": 667, "nombre": "iPhone SE"},
    "mobile-17": {"width": 393, "height": 852, "nombre": "iPhone 17"},
    "tablet": {"width": 768, "height": 1024, "nombre": "iPad"},
    "desktop": {"width": 1920, "height": 1080, "nombre": "Desktop"}
}

def validar_url(url):
    """Valida que la URL responda antes de proceder con las capturas"""
    # Importar requests solo cuando se necesite
    try:
        import requests
        from requests.exceptions import RequestException, Timeout, ConnectionError
    except ImportError:
        print("❌ Error: La librería 'requests' no está instalada")
        print("💡 Instala con: pip install requests")
        return False
    
    print(f"🔍 Validando URL: {url}")
    
    try:
        # Intentar una petición HEAD primero (más rápida)
        response = requests.head(url, timeout=10, allow_redirects=True)
        
        # Si HEAD no es soportado, intentar GET
        if response.status_code == 405:  # Method Not Allowed
            response = requests.get(url, timeout=10, allow_redirects=True)
        
        if response.status_code == 200:
            print(f"✅ URL válida (Status: {response.status_code})")
            return True
        else:
            print(f"⚠️ URL responde pero con status: {response.status_code}")
            # Permitir algunos códigos que pueden funcionar con Playwright
            if response.status_code in [301, 302, 303, 307, 308]:
                print(f"📝 Redireccionamiento detectado, continuando...")
                return True
            return False
            
    except (ConnectionError, Timeout) as e:
        print(f"❌ Error de conexión: {e}")
        return False
    except RequestException as e:
        print(f"❌ Error en la petición: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado validando URL: {e}")
        return False

def extraer_nombre_cliente(url):
    """Extrae el nombre del cliente desde la URL del dominio"""
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        # Remover www. si existe
        if domain.startswith('www.'):
            domain = domain[4:]
        # Remover extensión del dominio
        nombre = domain.split('.')[0]
        # Limpiar caracteres especiales
        nombre = re.sub(r'[^a-zA-Z0-9]', '', nombre)
        return nombre
    except:
        return "sitio_web"

def crear_nombre_archivo(url, device, timestamp, es_completa=False):
    """Crea nombre descriptivo para el archivo"""
    try:
        parsed = urlparse(url)
        # Extraer path y limpiar
        path = parsed.path.strip('/')
        if not path:
            descripcion = "pagina-principal"
        else:
            descripcion = path.replace('/', '-').replace('#', '-seccion-')
        
        # Limpiar caracteres especiales
        descripcion = re.sub(r'[^a-zA-Z0-9\-]', '', descripcion)
        if not descripcion:
            descripcion = "captura"
            
        # Añadir sufijo si es captura completa
        sufijo = "-completa" if es_completa else ""
        
        return f"{descripcion}-{device}{sufijo}-{timestamp}.png"
    except:
        sufijo = "-completa" if es_completa else ""
        return f"captura-{device}{sufijo}-{timestamp}.png"

def wait_for_animations(page, wait_time):
    """Espera el tiempo especificado para que carguen las animaciones"""
    if wait_time > 0:
        print(f"⏳ Esperando {wait_time} segundos para que carguen las animaciones...")
        time.sleep(wait_time)

def auto_dismiss_popups(page):
    """
    Detecta y cierra automáticamente banners de cookies, avisos de privacidad 
    y otros pop-ups que bloqueen la pantalla.
    
    Busca botones comunes de aceptar/cerrar en múltiples idiomas y frameworks populares.
    """
    print("🔍 Detectando y cerrando pop-ups automáticamente...")
    
    # Lista completa de selectores CSS para botones de aceptar/cerrar cookies
    # Incluye selectores comunes de frameworks, textos en múltiples idiomas, y clases típicas
    selectores = [
        # Selectores por texto en español
        'button:has-text("Aceptar")',
        'button:has-text("Aceptar todo")',
        'button:has-text("Aceptar todas")',
        'button:has-text("Aceptar cookies")',
        'button:has-text("Acepto")',
        'button:has-text("Entendido")',
        'button:has-text("De acuerdo")',
        'button:has-text("Cerrar")',
        'a:has-text("Aceptar")',
        'a:has-text("Aceptar todo")',
        'a:has-text("Cerrar")',
        
        # Selectores por texto en inglés
        'button:has-text("Accept")',
        'button:has-text("Accept all")',
        'button:has-text("Accept All")',
        'button:has-text("Accept cookies")',
        'button:has-text("Accept Cookies")',
        'button:has-text("I accept")',
        'button:has-text("I Accept")',
        'button:has-text("Got it")',
        'button:has-text("OK")',
        'button:has-text("Close")',
        'button:has-text("Agree")',
        'button:has-text("I agree")',
        'button:has-text("Continue")',
        'button:has-text("Consent")',
        'a:has-text("Accept")',
        'a:has-text("Accept all")',
        'a:has-text("Close")',
        
        # Selectores por texto en francés
        'button:has-text("Accepter")',
        'button:has-text("Tout accepter")',
        'button:has-text("J\'accepte")',
        'button:has-text("Fermer")',
        'button:has-text("D\'accord")',
        
        # Selectores por texto en alemán
        'button:has-text("Akzeptieren")',
        'button:has-text("Alle akzeptieren")',
        'button:has-text("Ich akzeptiere")',
        'button:has-text("Schließen")',
        'button:has-text("Einverstanden")',
        
        # Selectores por texto en italiano
        'button:has-text("Accetta")',
        'button:has-text("Accetta tutto")',
        'button:has-text("Accetto")',
        'button:has-text("Chiudi")',
        'button:has-text("Ho capito")',
        
        # Selectores por texto en portugués
        'button:has-text("Aceitar")',
        'button:has-text("Aceitar tudo")',
        'button:has-text("Eu aceito")',
        'button:has-text("Fechar")',
        'button:has-text("Entendi")',
        
        # Selectores por clases comunes (insensitive a mayúsculas)
        '[class*="cookie" i][class*="accept" i]',
        '[class*="cookie" i][class*="consent" i]',
        '[class*="cookie" i][class*="agree" i]',
        '[class*="cookie" i][class*="allow" i]',
        '[class*="consent" i][class*="accept" i]',
        '[class*="consent" i][class*="agree" i]',
        '[class*="gdpr" i][class*="accept" i]',
        '[class*="privacy" i][class*="accept" i]',
        '[class*="banner" i][class*="accept" i]',
        '[class*="modal" i][class*="accept" i]',
        '[class*="popup" i][class*="accept" i]',
        '[class*="notice" i][class*="accept" i]',
        
        # Selectores por clases específicas comunes
        '.cookie-consent-accept',
        '.cookie-accept',
        '.cookie-accept-all',
        '.accept-cookies',
        '.accept-all-cookies',
        '.consent-accept',
        '.gdpr-accept',
        '.privacy-accept',
        '#cookie-accept',
        '#accept-cookies',
        '#cookieConsent button',
        '#cookieNotice button',
        '.cc-accept',
        '.cc-allow',
        '.cc-dismiss',
        
        # Selectores por IDs comunes
        '[id*="cookie" i][id*="accept" i]',
        '[id*="cookie" i][id*="consent" i]',
        '[id*="gdpr" i][id*="accept" i]',
        '[id*="consent" i][id*="accept" i]',
        
        # Selectores para frameworks populares de cookies
        # OneTrust
        '#onetrust-accept-btn-handler',
        '.onetrust-close-btn-handler',
        '.optanon-allow-all-button',
        
        # Cookiebot
        '#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll',
        '#CybotCookiebotDialogBodyButtonAccept',
        '.CybotCookiebotDialogBodyButton',
        
        # Cookie Consent
        '.cc-btn.cc-allow',
        '.cc-compliance button',
        
        # Quantcast
        '.qc-cmp2-summary-buttons button[mode="primary"]',
        'button[aria-label*="Accept" i]',
        'button[aria-label*="Consent" i]',
        
        # TrustArc
        '#truste-consent-button',
        '.truste-button1',
        
        # Osano
        '.osano-cm-accept',
        '.osano-cm-accept-all',
        
        # Google Consent Mode
        'button[data-google-interstitial-action="accept"]',
        
        # Selectores por atributos ARIA
        'button[aria-label*="accept" i]',
        'button[aria-label*="consent" i]',
        'button[aria-label*="agree" i]',
        'button[aria-label*="close" i]',
        'button[aria-label*="dismiss" i]',
        
        # Botones de cerrar (X, close icons)
        'button[class*="close" i]',
        'button[aria-label="Close"]',
        'button[aria-label="Cerrar"]',
        '[class*="close-button" i]',
        '[class*="dismiss" i]',
        
        # Selectores genéricos para modales/overlays
        '.modal-footer button:first-child',
        '.modal-actions button:first-child',
        'div[role="dialog"] button:first-child',
        'div[role="alertdialog"] button:first-child',
    ]
    
    cerrados = 0
    intentos = 0
    max_intentos = len(selectores)
    
    # Intentar cerrar pop-ups con cada selector
    for selector in selectores:
        if intentos >= max_intentos:
            break
            
        try:
            # Buscar elementos que coincidan con el selector (timeout muy corto)
            elementos = page.locator(selector)
            count = elementos.count()
            
            if count > 0:
                # Intentar hacer clic en el primer elemento visible
                for i in range(count):
                    try:
                        elemento = elementos.nth(i)
                        # Verificar si es visible antes de hacer clic
                        if elemento.is_visible(timeout=500):
                            elemento.click(timeout=1000)
                            cerrados += 1
                            print(f"✅ Pop-up cerrado: {selector}")
                            # Esperar un momento para que se cierre la animación
                            time.sleep(0.5)
                            break
                    except:
                        # Si falla con este elemento, probar con el siguiente
                        continue
                        
        except Exception as e:
            # Ignorar errores y continuar con el siguiente selector
            pass
        
        intentos += 1
    
    if cerrados > 0:
        print(f"✅ Se cerraron {cerrados} pop-up(s) automáticamente")
        # Esperar un momento adicional para que termine cualquier animación de cierre
        time.sleep(1.0)
    else:
        print("ℹ️  No se detectaron pop-ups que cerrar (o ya estaban cerrados)")
    
    return cerrados

def extraer_opengraph(page, url, base_path, timestamp):
    """
    Extrae todos los metadatos OpenGraph de la página y los guarda en JSON.
    También descarga las imágenes og:image si están disponibles.
    
    Args:
        page: Objeto page de Playwright
        url: URL de la página
        base_path: Ruta base donde guardar los archivos
        timestamp: Timestamp para nombrar archivos
    
    Returns:
        dict: Diccionario con los metadatos extraídos
    """
    import json
    
    print("🔍 Extrayendo metadatos OpenGraph...")
    
    # Extraer todos los metadatos og:* de la página
    og_data = page.evaluate("""
        () => {
            const metaTags = document.querySelectorAll('meta[property^="og:"], meta[name^="og:"]');
            const data = {};
            
            metaTags.forEach(tag => {
                const property = tag.getAttribute('property') || tag.getAttribute('name');
                const content = tag.getAttribute('content');
                if (property && content) {
                    // Remover el prefijo 'og:' para simplificar
                    const key = property.replace('og:', '');
                    data[key] = content;
                }
            });
            
            // También extraer metadatos estándar relevantes
            const title = document.querySelector('title');
            const description = document.querySelector('meta[name="description"]');
            const keywords = document.querySelector('meta[name="keywords"]');
            const canonical = document.querySelector('link[rel="canonical"]');
            
            // Añadir metadatos adicionales si no están en og:
            if (title && !data.title) {
                data.title = title.textContent;
            }
            if (description && !data.description) {
                data.description = description.getAttribute('content');
            }
            if (keywords) {
                data.keywords = keywords.getAttribute('content');
            }
            if (canonical) {
                data.canonical_url = canonical.getAttribute('href');
            }
            
            // Twitter Card metadata (complementario)
            const twitterCard = document.querySelector('meta[name="twitter:card"]');
            const twitterSite = document.querySelector('meta[name="twitter:site"]');
            const twitterCreator = document.querySelector('meta[name="twitter:creator"]');
            
            if (twitterCard) data.twitter_card = twitterCard.getAttribute('content');
            if (twitterSite) data.twitter_site = twitterSite.getAttribute('content');
            if (twitterCreator) data.twitter_creator = twitterCreator.getAttribute('content');
            
            return data;
        }
    """)
    
    # Añadir información adicional
    og_data['extracted_at'] = datetime.now().isoformat()
    og_data['source_url'] = url
    og_data['timestamp'] = timestamp
    
    # Crear carpeta opengraph
    og_path = base_path / 'opengraph'
    og_path.mkdir(parents=True, exist_ok=True)
    
    # Guardar JSON con los metadatos
    json_filename = f"opengraph-{timestamp}.json"
    json_path = og_path / json_filename
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(og_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Metadatos OpenGraph guardados: {json_path}")
    
    # Descargar imagen og:image si existe
    if 'image' in og_data and og_data['image']:
        try:
            import requests
            from urllib.parse import urljoin
            
            image_url = og_data['image']
            # Convertir URL relativa a absoluta si es necesario
            if not image_url.startswith('http'):
                image_url = urljoin(url, image_url)
            
            print(f"📥 Descargando imagen OpenGraph: {image_url}")
            
            response = requests.get(image_url, timeout=10, stream=True)
            if response.status_code == 200:
                # Obtener extensión de la imagen
                ext = image_url.split('.')[-1].split('?')[0]
                if ext not in ['jpg', 'jpeg', 'png', 'gif', 'webp']:
                    ext = 'jpg'  # Default
                
                image_filename = f"og-image-{timestamp}.{ext}"
                image_path = og_path / image_filename
                
                with open(image_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                
                print(f"✅ Imagen OpenGraph descargada: {image_path}")
                og_data['image_local_path'] = str(image_path)
            else:
                print(f"⚠️  No se pudo descargar la imagen (Status: {response.status_code})")
        except Exception as e:
            print(f"⚠️  Error descargando imagen OpenGraph: {e}")
    
    # Mostrar resumen de los metadatos encontrados
    print(f"\n📊 Metadatos OpenGraph encontrados:")
    if 'title' in og_data:
        print(f"   📌 Título: {og_data['title'][:80]}{'...' if len(og_data['title']) > 80 else ''}")
    if 'description' in og_data:
        print(f"   📝 Descripción: {og_data['description'][:80]}{'...' if len(og_data['description']) > 80 else ''}")
    if 'type' in og_data:
        print(f"   🏷️  Tipo: {og_data['type']}")
    if 'image' in og_data:
        print(f"   🖼️  Imagen: ✅")
    if 'site_name' in og_data:
        print(f"   🌐 Sitio: {og_data['site_name']}")
    
    print(f"   ℹ️  Total: {len(og_data)} campos extraídos\n")
    
    return og_data

def smooth_scroll_page(page):
    """Realiza scroll suave hacia abajo para disparar animaciones basadas en scroll"""
    print("📜 Realizando scroll suave para disparar animaciones...")
    
    # Obtener la altura total de la página
    total_height = page.evaluate("document.body.scrollHeight")
    viewport_height = page.evaluate("window.innerHeight")
    
    print(f"📏 Altura total de la página: {total_height}px, Viewport: {viewport_height}px")
    
    # Scroll optimizado - pasos de 80px (balance entre velocidad y efectividad)
    step_size = 80
    steps = int(total_height / step_size)
    
    print(f"🔄 Realizando scroll suave en {steps} pasos de {step_size}px...")
    
    for i in range(steps):
        # Usar scrollBy para scroll incremental natural
        page.evaluate(f"""
            window.scrollBy(0, {step_size});
            window.dispatchEvent(new Event('scroll'));
        """)
        
        # Pausa corta optimizada (0.08s - rápido pero efectivo)
        time.sleep(0.08)
        
        # Mostrar progreso cada 20% del recorrido
        progress = (i / steps) * 100
        if progress % 20 < (100 / steps):
            print(f"📍 Progreso: {int(progress)}% ({i * step_size}px de {total_height}px)")
    
    # Asegurar que llegamos al final
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    print("📍 Llegado al final de la página")
    
    # Forzar estado final de animaciones comunes
    print("✨ Forzando estado final de animaciones...")
    page.evaluate("""
        // AOS (Animate On Scroll)
        document.querySelectorAll('[data-aos]').forEach(el => {
            el.classList.add('aos-animate');
            el.style.opacity = '1';
            el.style.transform = 'none';
        });
        
        // GSAP ScrollTrigger refresh
        if (typeof ScrollTrigger !== 'undefined') {
            ScrollTrigger.getAll().forEach(st => st.refresh());
        }
        
        // Intersection Observer - forzar visibilidad
        document.querySelectorAll('[class*="fade"], [class*="slide"], [class*="animate"]').forEach(el => {
            if (el.style.opacity === '0' || el.style.opacity === '') {
                el.style.opacity = '1';
            }
            if (el.style.visibility === 'hidden') {
                el.style.visibility = 'visible';
            }
        });
        
        // Disparar scroll event final
        window.dispatchEvent(new Event('scroll'));
        window.dispatchEvent(new Event('resize'));
    """)
    
    # Pausa final para que se completen las animaciones
    time.sleep(1.0)
    print("✅ Scroll completado - página lista para captura desde el final")

def capturar_url(url, device_key, device_config, base_path, timestamp, wait_time=3.0, smooth_scroll=False, auto_dismiss=False):
    """Captura screenshots de una URL en un dispositivo específico"""
    # Importar playwright solo cuando se necesite
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("❌ Error: La librería 'playwright' no está instalada")
        print("💡 Instala con: pip install playwright")
        print("💡 Luego ejecuta: playwright install")
        return
    
    print(f"📱 Configurando: {device_config['nombre']} ({device_config['width']}x{device_config['height']})")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport=device_config)
        
        try:
            print(f"📸 Navegando a: {url}")
            page.goto(url, wait_until="networkidle")
            
            # Esperar tiempo especificado para animaciones
            wait_for_animations(page, wait_time)
            
            # Cerrar pop-ups automáticamente si está activado
            if auto_dismiss:
                auto_dismiss_popups(page)
            
            # Captura normal (viewport)
            archivo_normal = crear_nombre_archivo(url, device_key, timestamp, False)
            ruta_normal = base_path / archivo_normal
            page.screenshot(path=str(ruta_normal))
            print(f"✅ Captura viewport: {ruta_normal}")
            
            # Captura completa (página scrolleable)
            if smooth_scroll:
                smooth_scroll_page(page)
                # Esperar tiempo mínimo después del scroll suave
                wait_for_animations(page, 1.0)  # Tiempo mínimo optimizado
            
            archivo_completa = crear_nombre_archivo(url, device_key, timestamp, True)
            ruta_completa = base_path / archivo_completa
            page.screenshot(path=str(ruta_completa), full_page=True)
            print(f"✅ Captura completa: {ruta_completa}")
            
        except Exception as e:
            print(f"❌ Error capturando {url} en {device_key}: {e}")
        finally:
            browser.close()

def crear_estructura_carpetas(cliente, devices_a_usar, output_dir=None):
    """Crea la estructura de carpetas solo para los dispositivos que se van a usar"""
    # Determinar el directorio base de salida
    if output_dir:
        # Si se especifica un directorio personalizado
        base_output = Path(output_dir).expanduser()
    else:
        # Por defecto: carpeta 'capturas' en el directorio del proyecto
        base_output = Path.cwd() / "capturas"
    
    # Crear la ruta completa con el nombre del cliente
    base_path = base_output / cliente
    
    for device_key in devices_a_usar:
        device_path = base_path / device_key
        device_path.mkdir(parents=True, exist_ok=True)
        print(f"📁 Carpeta verificada: {device_path}")
    
    return base_path

def abrir_explorador_archivos(ruta):
    """
    Abre el explorador de archivos del sistema en la ruta especificada.
    Funciona en Windows, macOS y Linux (detecta automáticamente el gestor de archivos).
    """
    ruta = Path(ruta).resolve()
    
    if not ruta.exists():
        print(f"⚠️  La ruta {ruta} no existe, no se puede abrir el explorador")
        return False
    
    sistema = platform.system()
    
    try:
        if sistema == "Windows":
            # Windows: usar explorer
            subprocess.run(["explorer", str(ruta)], check=False)
            print(f"📂 Abriendo Explorer en: {ruta}")
            
        elif sistema == "Darwin":  # macOS
            # macOS: usar open
            subprocess.run(["open", str(ruta)], check=False)
            print(f"📂 Abriendo Finder en: {ruta}")
            
        elif sistema == "Linux":
            # Linux: intentar xdg-open (funciona con cualquier gestor de archivos predeterminado)
            # xdg-open detecta automáticamente el gestor de archivos del entorno de escritorio
            # (Dolphin en KDE, Nautilus en GNOME, Thunar en XFCE, etc.)
            try:
                subprocess.run(["xdg-open", str(ruta)], check=False, 
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"📂 Abriendo explorador de archivos en: {ruta}")
            except FileNotFoundError:
                # Si xdg-open no está disponible, intentar gestores comunes
                gestores = ["dolphin", "nautilus", "thunar", "nemo", "caja", "pcmanfm"]
                for gestor in gestores:
                    try:
                        subprocess.run([gestor, str(ruta)], check=False,
                                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        print(f"📂 Abriendo {gestor} en: {ruta}")
                        break
                    except FileNotFoundError:
                        continue
                else:
                    print(f"⚠️  No se pudo detectar un explorador de archivos. Ruta: {ruta}")
                    return False
        else:
            print(f"⚠️  Sistema operativo no soportado: {sistema}")
            return False
        
        return True
        
    except Exception as e:
        print(f"⚠️  Error al abrir explorador de archivos: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="""
Wshot - Herramienta profesional para capturas de pantalla web

Esta herramienta permite realizar capturas de pantalla optimizadas de sitios web
en múltiples dispositivos y tamaños, con soporte para animaciones y efectos de scroll.
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
EJEMPLOS DE USO:
  
  Captura básica en un dispositivo:
    wshot https://example.com --device desktop
    wshot https://site.com --device mobile-17
  
  Captura en todos los dispositivos:
    wshot https://example.com --all-devices
  
  Captura con tiempo de espera personalizado:
    wshot https://site.com --device tablet --wait-time 7
  
  Captura con scroll suave para animaciones:
    wshot https://animated-site.com --all-devices --smooth-scroll
  
  Cerrar automáticamente banners de cookies:
    wshot https://google.com --device desktop --auto-dismiss
  
  Extraer metadatos OpenGraph:
    wshot https://miempresa.com --device desktop --og
  
  Modo super (completo y optimizado):
    wshot https://complex-site.com --super
  
  Combinando opciones:
    wshot https://site.com --device desktop --wait-time 4 --smooth-scroll --auto-dismiss --og
  
  Guardar en directorio personalizado:
    wshot https://site.com --super --output-dir ~/Proyectos/Capturas

  Abrir explorador de archivos automáticamente:
    wshot https://site.com --super --open --auto-dismiss
    wshot https://site.com --device desktop --open

DISPOSITIVOS DISPONIBLES:
  mobile-se    iPhone SE (375x667)
  mobile-17    iPhone 17 (393x852)  
  tablet       iPad (768x1024)
  desktop      Desktop (1920x1080)

NOTAS:
  • Las capturas se guardan en carpetas organizadas por cliente y dispositivo
  • El nombre del cliente se extrae automáticamente de la URL
  • Se generan dos tipos de captura: viewport y página completa
  • El modo --super activa automáticamente: all-devices + smooth-scroll + open-graph + wait-time 2s
  • El modo --all incluye automáticamente extracción de OpenGraph
  • Usa --auto-dismiss para cerrar automáticamente banners de cookies y pop-ups (ideal para Google, Facebook, etc.)
  • Los metadatos OpenGraph se guardan en carpeta opengraph/ con JSON e imagen descargada
        """
    )
    
    parser.add_argument('url', 
                       nargs='?',  # Hacer que URL sea opcional
                       help='URL completa del sitio web a capturar (ej: https://example.com)')
    
    parser.add_argument('-all', '--all-devices', 
                       action='store_true',
                       help='Capturar en todos los dispositivos disponibles (mobile-se, mobile-17, tablet, desktop)')
    
    parser.add_argument('--device', 
                       choices=list(TAMAÑOS.keys()),
                       help='Dispositivo específico para capturar. Opciones: mobile-se, mobile-17, tablet, desktop')
    
    parser.add_argument('--cliente',
                       help='Nombre personalizado del cliente para organizar capturas (se detecta automáticamente desde URL si no se especifica)')
    
    parser.add_argument('--output-dir',
                       help='Directorio personalizado para guardar las capturas (default: ./capturas/ en el directorio actual)')
    
    parser.add_argument('--wait-time',
                       type=float,
                       default=3.0,
                       help='Tiempo de espera en segundos para que carguen animaciones y contenido dinámico (default: 3.0)')
    
    parser.add_argument('--smooth-scroll',
                       action='store_true',
                       help='Realizar scroll suave hacia abajo antes de captura completa para disparar animaciones basadas en scroll')
    
    parser.add_argument('--auto-dismiss',
                       action='store_true',
                       help='🤖 Cerrar automáticamente banners de cookies, avisos de privacidad y otros pop-ups que bloqueen la pantalla. Detecta y cierra botones comunes en múltiples idiomas (Aceptar, Accept, Accepter, etc.)')
    
    parser.add_argument('--open-graph', '--og',
                       dest='open_graph',
                       action='store_true',
                       help='📊 Extraer metadatos OpenGraph (og:title, og:description, og:image, etc.) y guardarlos en JSON. También descarga la imagen og:image. Se activa automáticamente con --all y --super')
    
    parser.add_argument('--super',
                       action='store_true',
                       help='🚀 Modo super: activa automáticamente --all-devices + --smooth-scroll + --open-graph + wait-time optimizado (2s) para capturas completas y rápidas')
    
    parser.add_argument('--info',
                       action='store_true',
                       help='📖 Mostrar guía completa y ejemplos detallados de uso')
    
    parser.add_argument('--open',
                       action='store_true',
                       help='📂 Abrir el explorador de archivos al finalizar las capturas (detecta automáticamente: Explorer en Windows, Finder en macOS, o tu gestor de archivos en Linux como Dolphin, Nautilus, etc.)')
    
    args = parser.parse_args()
    
    # Si se solicita información extendida, mostrarla y salir
    if args.info:
        mostrar_ayuda_extendida()
        sys.exit(0)
    
    # Si no es --info, entonces URL es requerida
    if not args.url:
        print("❌ Error: URL es requerida")
        print("💡 Usa --help para ver opciones básicas o --info para guía completa")
        parser.print_help()
        sys.exit(1)
    
    # Si se usa --super, activar automáticamente las opciones optimizadas
    if args.super:
        args.all_devices = True
        args.smooth_scroll = True
        args.open_graph = True  # Activar OpenGraph automáticamente en modo super
        # Si no se especificó wait_time personalizado, usar 2 segundos para modo super (optimizado)
        if args.wait_time == 3.0:  # valor default
            args.wait_time = 2.0
    
    # Si se usa --all, activar automáticamente OpenGraph
    if args.all_devices and not args.open_graph:
        args.open_graph = True
    
    # Validar argumentos
    if not args.all_devices and not args.device and not args.super:
        print("❌ Error: Debes especificar -all, --device o --super")
        print("💡 Usa --help para ver opciones básicas o --info para guía completa")
        parser.print_help()
        sys.exit(1)
    
    # VALIDAR URL ANTES DE CREAR CARPETAS
    if not validar_url(args.url):
        print(f"❌ Error: La URL {args.url} no responde o no es accesible")
        print("💡 Verifica que la URL sea correcta y esté disponible")
        sys.exit(1)
    
    # Detectar cliente automáticamente o usar el proporcionado
    cliente = args.cliente or extraer_nombre_cliente(args.url)
    
    # Generar timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Determinar dispositivos a usar
    if args.all_devices:
        devices_a_usar = list(TAMAÑOS.keys())
        if args.super:
            print(f"🚀 MODO SUPER ACTIVADO 🚀")
            print(f"📱 Capturando URL: {args.url}")
            print(f"👤 Cliente: {cliente}")
            print(f"📱 Dispositivos: {', '.join(devices_a_usar)}")
            print(f"⏳ Tiempo de espera: {args.wait_time}s")
            print(f"📜 Scroll suave: ✅ Activado")
            print(f"📊 Extracción OpenGraph: ✅ Activado")
            if args.auto_dismiss:
                print(f"🤖 Cierre automático de pop-ups: ✅ Activado")
        else:
            print(f"🚀 Capturando URL: {args.url}")
            print(f"👤 Cliente: {cliente}")
            print(f"📱 Dispositivos: {', '.join(devices_a_usar)}")
            if args.open_graph:
                print(f"📊 Extracción OpenGraph: ✅ Activado")
            if args.auto_dismiss:
                print(f"🤖 Cierre automático de pop-ups: ✅ Activado")
    else:
        devices_a_usar = [args.device]
        print(f"🚀 Capturando URL: {args.url}")
        print(f"👤 Cliente: {cliente}")
        print(f"📱 Dispositivo: {args.device}")
        if args.smooth_scroll:
            print(f"📜 Scroll suave: ✅ Activado")
        if args.wait_time != 3.0:
            print(f"⏳ Tiempo de espera: {args.wait_time}s")
        if args.open_graph:
            print(f"📊 Extracción OpenGraph: ✅ Activado")
        if args.auto_dismiss:
            print(f"🤖 Cierre automático de pop-ups: ✅ Activado")
    
    # Crear estructura de carpetas SOLO para dispositivos solicitados
    base_path = crear_estructura_carpetas(cliente, devices_a_usar, args.output_dir)
    
    print(f"📁 Carpeta base: {base_path}")
    print("="*60)
    
    # Extraer OpenGraph si está activado (antes de las capturas)
    og_data = None
    if args.open_graph:
        # Importar playwright para extraer OpenGraph
        try:
            from playwright.sync_api import sync_playwright
            
            print(f"\n📊 Extrayendo metadatos OpenGraph...")
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                # Usar desktop viewport para OpenGraph
                page = browser.new_page(viewport=TAMAÑOS['desktop'])
                
                try:
                    page.goto(args.url, wait_until="networkidle")
                    # Esperar un poco para que cargue todo
                    time.sleep(2)
                    
                    # Cerrar pop-ups si auto-dismiss está activado
                    if args.auto_dismiss:
                        auto_dismiss_popups(page)
                    
                    # Extraer OpenGraph
                    og_data = extraer_opengraph(page, args.url, base_path, timestamp)
                    
                except Exception as e:
                    print(f"❌ Error extrayendo OpenGraph: {e}")
                finally:
                    browser.close()
                    
        except ImportError:
            print("❌ Error: La librería 'playwright' no está instalada")
            print("💡 Instala con: pip install playwright")
    
    # Realizar capturas
    for i, device_key in enumerate(devices_a_usar, 1):
        print(f"\n[{i}/{len(devices_a_usar)}] Procesando {device_key}...")
        device_config = TAMAÑOS[device_key]
        device_path = base_path / device_key
        
        capturar_url(args.url, device_key, device_config, device_path, timestamp, args.wait_time, args.smooth_scroll, args.auto_dismiss)
    
    print(f"\n🎉 ¡Capturas completadas!")
    print(f"📂 Revisa las imágenes en: {base_path}")
    
    # Abrir explorador de archivos si se solicitó
    if args.open:
        print("")
        abrir_explorador_archivos(base_path)

if __name__ == "__main__":
    main()