#!/usr/bin/env python3
"""
Wshot - Simplified tool for web screenshots
Usage: wshot URL [-all] [--device DEVICE] [--wait-time SECONDS] [--smooth-scroll] [--super]

Examples:
  wshot http://mariadelasmercedes.com/contacto -all
  wshot https://mecalito.com --device mobile-17
  wshot https://example.com --device tablet --wait-time 5 --smooth-scroll
  wshot https://site.com --super  # Complete optimized mode
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
# Playwright and requests imports will be done later to allow --help to work

def display_extended_help():
    """Show additional information about script usage"""
    extended_help_text = r"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                                  _           _                               ║
║                                 | |         | |                              ║
║                    __      __ __| |__   ___ | |_                             ║
║                    \ \ /\ / / __| '_ \ / _ \| __|                            ║
║                     \ V  V /\__ \ | | | (_) | |_                             ║
║                      \_/\_/ |___/_| |_|\___/ \__|                            ║
║                                                                              ║
║                    🚀 Enterprise Visual Audit Platform                      ║
╚══════════════════════════════════════════════════════════════════════════════╝

📖 DESCRIPTION:
   Wshot is a professional tool for taking website screenshots
   across multiple devices, optimized for modern sites with
   animations, scroll effects and dynamic content.

🎯 MAIN FEATURES:
   • Screenshots on 15+ predefined devices and resolutions
   • Support for animations and delayed loading content
   • Smooth scroll to trigger scroll-based animations
   • Automatic closure of cookie banners and pop-ups 🤖
   • OpenGraph metadata extraction for SEO and social media 📊
   • Automatic file organization by client and device
   • Super mode for optimized complete capture

📱 AVAILABLE DEVICES:

   🔥 SHORT NAMES (recommended):
   mobile      │ iPhone 15       │ 393 × 852   │ Default mobile
   tablet      │ iPad            │ 768 × 1024  │ Default tablet
   laptop      │ Laptop 13"      │ 1280 × 800  │ Default laptop
   desktop     │ Full HD Monitor │ 1920 × 1080 │ Default desktop

   📱 SPECIFIC MOBILES:
   iphone-se        │ iPhone SE (2022)      │ 375 × 667   │ Compact mobile
   iphone-15-pro    │ iPhone 15 Pro         │ 393 × 852   │ Premium mobile
   iphone-17        │ iPhone 17 (2025)      │ 402 × 874   │ Future mobile
   galaxy-s23       │ Samsung Galaxy S23    │ 360 × 780   │ Standard Android
   galaxy-s23-ultra │ Samsung Galaxy S23 U. │ 412 × 915   │ Premium Android
   pixel-7          │ Google Pixel 7        │ 412 × 892   │ Pure Android

   📱 SPECIFIC TABLETS:
   ipad-pro         │ iPad Pro (12.9")      │ 1024 × 1366 │ Professional tablet
   galaxy-tab-s9    │ Samsung Galaxy Tab S9 │ 800 × 1280  │ Android tablet

   💻 SPECIFIC LAPTOPS:
   laptop-15        │ MacBook Pro 15"       │ 1440 × 900  │ Standard laptop
   laptop-16        │ MacBook Pro 16"       │ 1728 × 1117 │ Premium laptop

   🖥️ SPECIFIC DESKTOPS:
   desktop-2k       │ 2K/QHD Monitor        │ 2560 × 1440 │ Premium desktop
   desktop-4k       │ 4K/UHD Monitor        │ 3840 × 2160 │ Professional desktop

🚀 USAGE MODES:

   Basic (one device):
   $ wshot https://example.com --device desktop

   Complete (all devices):  
   $ wshot https://example.com --all-devices

   Super optimized (recommended for complex sites):
   $ wshot https://example.com --super

⚙️  ADVANCED OPTIONS:
   --wait-time SECONDS     │ Wait time for animations (default: 3s)
   --smooth-scroll         │ Smooth scroll before full page capture
   --auto-dismiss          │ Automatically close cookie banners and pop-ups 🤖
   --open-graph, --og      │ Extract OpenGraph metadata (og:*, Twitter Card) 📊
   --client NAME           │ Custom name to organize files
   --output-dir PATH       │ Custom output directory
   --open                  │ Open file explorer when finished

📂 FILE STRUCTURE:
   Screenshots are saved by default in:
   ~/Pictures/WSHOT/ (folder in user Pictures)
   └── [client]/
       ├── mobile-se/
       ├── mobile-17/ 
       ├── tablet/
       └── desktop/
           ├── page-viewport-20241004_143025.png
           └── page-fullpage-20241004_143025.png
   
   Use --output-dir to save in another location like:
   ~/Pictures/Wshot or ~/Downloads/Wshot

💡 TIPS:
   • Use --super for sites with many animations
   • Use higher --wait-time for slow sites
   • Smooth scroll is ideal for lazy loading and parallax
   • Use --auto-dismiss for sites with annoying cookie banners
   • Combine --auto-dismiss with --super for perfect captures without pop-ups
   • Use --og or --open-graph to extract SEO and social media metadata
   • --all and --super modes automatically include OpenGraph extraction
   • URLs must include http:// or https://

"""
    print(extended_help_text)

# Device/size configuration
DEVICE_SIZES = {
    # 📱 Mobile devices - default short names
    "mobile": {"width": 393, "height": 852, "nombre": "iPhone 15 (default mobile)"},
    "iphone-se": {"width": 375, "height": 667, "nombre": "iPhone SE (2022)"},
    "iphone-15-pro": {"width": 393, "height": 852, "nombre": "iPhone 15 Pro"},
    "iphone-17": {"width": 402, "height": 874, "nombre": "iPhone 17 (2025)"},
    "galaxy-s23": {"width": 360, "height": 780, "nombre": "Samsung Galaxy S23"},
    "galaxy-s23-ultra": {"width": 412, "height": 915, "nombre": "Samsung Galaxy S23 Ultra"},
    "pixel-7": {"width": 412, "height": 892, "nombre": "Google Pixel 7"},
    
    # 📱 Tablets - default short names
    "tablet": {"width": 768, "height": 1024, "nombre": "iPad (default tablet)"},
    "ipad-pro": {"width": 1024, "height": 1366, "nombre": "iPad Pro (12.9\")"},
    "galaxy-tab-s9": {"width": 800, "height": 1280, "nombre": "Samsung Galaxy Tab S9"},
    
    # 💻 Laptops - default short names
    "laptop": {"width": 1280, "height": 800, "nombre": "Laptop 13\" (default laptop)"},
    "laptop-15": {"width": 1440, "height": 900, "nombre": "MacBook Pro 15\" / ThinkPad X1"},
    "laptop-16": {"width": 1728, "height": 1117, "nombre": "MacBook Pro 16\""},
    
    # 🖥️ Desktop - default short names
    "desktop": {"width": 1920, "height": 1080, "nombre": "Full HD Monitor (default)"},
    "desktop-2k": {"width": 2560, "height": 1440, "nombre": "Monitor 2K/QHD"},
    "desktop-4k": {"width": 3840, "height": 2160, "nombre": "Monitor 4K/UHD"},
    
    # 🏷️ Aliases for long names (compatibility)
    "iphone-15": {"width": 393, "height": 852, "nombre": "iPhone 15 (alias for mobile)"},
    "ipad": {"width": 768, "height": 1024, "nombre": "iPad (alias for tablet)"},
    "laptop-13": {"width": 1280, "height": 800, "nombre": "Laptop 13\" (alias for laptop)"},
    "desktop-fhd": {"width": 1920, "height": 1080, "nombre": "Monitor Full HD (alias for desktop)"},
    
    # 🏷️ Legacy aliases (full compatibility)
    "mobile-se": {"width": 375, "height": 667, "nombre": "iPhone SE (alias for iphone-se)"},
    "mobile-17": {"width": 393, "height": 852, "nombre": "iPhone 15 (legacy alias)"}
}

def validar_url(url):
    """Validates that the URL responds before proceeding with captures"""
    # Import requests only when needed
    try:
        import requests
        from requests.exceptions import RequestException, Timeout, ConnectionError
    except ImportError:
        print("❌ Error: The 'requests' library is not installed")
        print("💡 Install with: pip install requests")
        return False
    
    print(f"🔍 Validating URL: {url}")
    
    try:
        # Try a HEAD request first (faster)
        response = requests.head(url, timeout=10, allow_redirects=True)
        
        # If HEAD is not supported, try GET
        if response.status_code == 405:  # Method Not Allowed
            response = requests.get(url, timeout=10, allow_redirects=True)
        
        if response.status_code == 200:
            print(f"✅ Valid URL (Status: {response.status_code})")
            return True
        else:
            print(f"⚠️ URL responds but with status: {response.status_code}")
            # Allow some codes that might work with Playwright
            if response.status_code in [301, 302, 303, 307, 308]:
                print(f"📝 Redirection detected, continuing...")
                return True
            return False
            
    except (ConnectionError, Timeout) as e:
        print(f"❌ Connection error: {e}")
        return False
    except RequestException as e:
        print(f"❌ Request error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error validating URL: {e}")
        return False

def extraer_nombre_cliente(url):
    """Extracts the client name from the complete domain URL"""
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        # Remove www. if it exists
        if domain.startswith('www.'):
            domain = domain[4:]
        # Use the complete domain (ex: example.com instead of just example)
        client_domain = domain
        # Clean special characters but keep dots
        client_domain = re.sub(r'[^a-zA-Z0-9\.]', '', client_domain)
        return client_domain
    except:
        return "website"

def generate_capture_filename(url, device, timestamp, es_completa=False):
    """Creates descriptive filename including domain and path"""
    try:
        parsed = urlparse(url)
        
        # Extract domain (without www.)
        domain = parsed.netloc.lower()
        if domain.startswith('www.'):
            domain = domain[4:]
        
        # Extract path and clean
        path = parsed.path.strip('/')
        if not path:
            path_description = "main-page"
        else:
            path_description = path.replace('/', '-').replace('#', '-section-')
        
        # Clean special characters from path
        path_description = re.sub(r'[^a-zA-Z0-9\-]', '', path_description)
        if not path_description:
            path_description = "main-page"
        
        # Clean special characters from domain but keep dots
        domain_clean = re.sub(r'[^a-zA-Z0-9\.]', '', domain)
        
        # Create name with format: domain.com_path-device-timestamp
        nombre_base = f"{domain_clean}_{path_description}"
            
        # Add suffix if it's a full capture
        suffix = "-fullpage" if es_completa else ""
        
        return f"{nombre_base}-{device}{suffix}-{timestamp}.png"
    except:
        suffix = "-fullpage" if es_completa else ""
        return f"capture-{device}{suffix}-{timestamp}.png"

def wait_for_animations(page, wait_time):
    """Waits the specified time for animations to load"""
    if wait_time > 0:
        print(f"⏳ Waiting {wait_time} seconds for animations to load...")
        time.sleep(wait_time)

def auto_dismiss_popups(page):
    """
    Automatically detects and closes cookie banners, privacy notices 
    and other pop-ups that block the screen.
    
    Searches for common accept/close buttons in multiple languages and popular frameworks.
    """
    print("🔍 Detecting and closing pop-ups automatically...")
    
    # Complete list of CSS selectors for accept/close cookie buttons
    # Includes common framework selectors, multilingual texts, and typical classes
    close_button_selectors = [
        # Selectors by text in Spanish
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
        
        # Selectors by text in English
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
        
        # Selectors by text in French
        'button:has-text("Accepter")',
        'button:has-text("Tout accepter")',
        'button:has-text("J\'accepte")',
        'button:has-text("Fermer")',
        'button:has-text("D\'accord")',
        
        # Selectors by text in German
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
        
        # Selectors by text in Portuguese
        'button:has-text("Aceitar")',
        'button:has-text("Aceitar tudo")',
        'button:has-text("Eu aceito")',
        'button:has-text("Fechar")',
        'button:has-text("Entendi")',
        
        # Selectors by common classes (case insensitive)
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
        
        # Selectors by specific common classes
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
        
        # Generic selectors for modals/overlays
        '.modal-footer button:first-child',
        '.modal-actions button:first-child',
        'div[role="dialog"] button:first-child',
        'div[role="alertdialog"] button:first-child',
    ]
    
    closed_popups_count = 0
    attempts = 0
    max_attempts = len(close_button_selectors)
    
    # Try to close pop-ups with each selector
    for selector in close_button_selectors:
        if attempts >= max_attempts:
            break
            
        try:
            # Search for elements matching the selector (very short timeout)
            popup_elements = page.locator(selector)
            count = popup_elements.count()
            
            if count > 0:
                # Try to click the first visible element
                for i in range(count):
                    try:
                        popup_element = popup_elements.nth(i)
                        # Check if visible before clicking
                        if popup_element.is_visible(timeout=500):
                            popup_element.click(timeout=1000)
                            closed_popups_count += 1
                            print(f"✅ Pop-up cerrado: {selector}")
                            # Wait a moment for the animation to close
                            time.sleep(0.5)
                            break
                    except:
                        # If it fails with this element, try the next one
                        continue
                        
        except Exception as e:
            # Ignore errors and continue with the next selector
            pass
        
        attempts += 1
    
    if closed_popups_count > 0:
        print(f"✅ {closed_popups_count} pop-up(s) closed automatically")
        # Wait an additional moment for any closing animation to finish
        time.sleep(1.0)
    else:
        print("ℹ️  No pop-ups detected to close (or already closed)")
    
    return closed_popups_count

def extract_opengraph_metadata(page, url, base_path, timestamp):
    """
    Extracts all OpenGraph metadata from the page and saves it to JSON.
    Also downloads og:image images if available.
    
    Args:
        page: Playwright page object
        url: Page URL
        base_path: Base path where to save files
        timestamp: Timestamp for naming files
    
    Returns:
        dict: Dictionary with extracted metadata
    """
    import json
    
    print("🔍 Extracting OpenGraph metadata...")
    
    # Extract all og:* metadata from the page
    og_data = page.evaluate("""
        () => {
            const metaTags = document.querySelectorAll('meta[property^="og:"], meta[name^="og:"]');
            const data = {};
            
            metaTags.forEach(tag => {
                const property = tag.getAttribute('property') || tag.getAttribute('name'); 
                const content = tag.getAttribute('content');
                if (property && content) {
                    // Remove 'og:' prefix to simplify
                    const key = property.replace('og:', '');
                    data[key] = content;
                }
            });
            
            // Also extract relevant standard metadata 
            const title = document.querySelector('title');
            const description = document.querySelector('meta[name="description"]');
            const keywords = document.querySelector('meta[name="keywords"]');
            const canonical = document.querySelector('link[rel="canonical"]');
            
            // Add additional metadata if not present in og:
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
            
            // Twitter Card metadata (complementary)
            const twitterCard = document.querySelector('meta[name="twitter:card"]');
            const twitterSite = document.querySelector('meta[name="twitter:site"]');
            const twitterCreator = document.querySelector('meta[name="twitter:creator"]');
            
            if (twitterCard) data.twitter_card = twitterCard.getAttribute('content');
            if (twitterSite) data.twitter_site = twitterSite.getAttribute('content');
            if (twitterCreator) data.twitter_creator = twitterCreator.getAttribute('content');
            
            return data;
        }
    """)
    
    # Add additional information
    og_data['extracted_at'] = datetime.now().isoformat()
    og_data['source_url'] = url
    og_data['timestamp'] = timestamp
    
    # Create opengraph folder
    og_path = base_path / 'opengraph'
    og_path.mkdir(parents=True, exist_ok=True)
    
    # Save JSON with metadata
    json_filename = f"opengraph-{timestamp}.json"
    json_path = og_path / json_filename
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(og_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ OpenGraph metadata saved: {json_path}")
    
    # Download og:image if it exists
    if 'image' in og_data and og_data['image']:
        try:
            import requests
            from urllib.parse import urljoin
            
            image_url = og_data['image']
            # Convert relative URL to absolute if necessary
            if not image_url.startswith('http'):
                image_url = urljoin(url, image_url)
            
            print(f"📥 Downloading OpenGraph image: {image_url}")
            
            response = requests.get(image_url, timeout=10, stream=True)
            if response.status_code == 200:
                # Get image extension
                ext = image_url.split('.')[-1].split('?')[0]
                if ext not in ['jpg', 'jpeg', 'png', 'gif', 'webp']:
                    ext = 'jpg'  # Default
                
                image_filename = f"og-image-{timestamp}.{ext}"
                image_path = og_path / image_filename
                
                with open(image_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                
                print(f"✅ OpenGraph image downloaded: {image_path}")
                og_data['image_local_path'] = str(image_path)
            else:
                print(f"⚠️  Could not download image (Status: {response.status_code})")
        except Exception as e:
            print(f"⚠️  Error downloading OpenGraph image: {e}")
    
    # Show summary of found metadata
    print(f"\n📊 OpenGraph metadata found:")
    if 'title' in og_data:
        print(f"   📌 Title: {og_data['title'][:80]}{'...' if len(og_data['title']) > 80 else ''}")
    if 'description' in og_data:
        print(f"   📝 Description: {og_data['description'][:80]}{'...' if len(og_data['description']) > 80 else ''}")
    if 'type' in og_data:
        print(f"   🏷️  Type: {og_data['type']}")
    if 'image' in og_data:
        print(f"   🖼️  Image: ✅")
    if 'site_name' in og_data:
        print(f"   🌐 Site: {og_data['site_name']}")
    
    print(f"   ℹ️  Total: {len(og_data)} fields extracted\n")
    
    return og_data

def smooth_scroll_page(page):
    """Performs smooth scroll down to trigger scroll-based animations"""
    print("📜 Performing smooth scroll to trigger animations...")
    
    # Get total page height
    total_height = page.evaluate("document.body.scrollHeight")
    viewport_height = page.evaluate("window.innerHeight")
    
    print(f"📏 Total page height: {total_height}px, Viewport: {viewport_height}px")
    
    # Optimized scroll - 80px steps (balance between speed and effectiveness)
    step_size = 80
    steps = int(total_height / step_size)
    
    print(f"🔄 Performing smooth scroll in {steps} steps of {step_size}px...")
    
    for i in range(steps):
        # Use scrollBy for natural incremental scroll
        page.evaluate(f"""
            window.scrollBy(0, {step_size});
            window.dispatchEvent(new Event('scroll'));
        """)
        
        # Optimized short pause (0.08s - fast but effective)
        time.sleep(0.08)
        
        # Show progress every 20% of the journey
        progress = (i / steps) * 100
        if progress % 20 < (100 / steps):
            print(f"📍 Progress: {int(progress)}% ({i * step_size}px of {total_height}px)")
    
    # Ensure we reach the end
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    print("📍 Reached end of page")
    
    # Force final state of common animations
    print("✨ Forcing final state of animations...")
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
        
        // Intersection Observer - force visibility
        document.querySelectorAll('[class*="fade"], [class*="slide"], [class*="animate"]').forEach(el => {
            if (el.style.opacity === '0' || el.style.opacity === '') {
                el.style.opacity = '1';
            }
            if (el.style.visibility === 'hidden') {
                el.style.visibility = 'visible';
            }
        });
        
        // Trigger final scroll event
        window.dispatchEvent(new Event('scroll'));
        window.dispatchEvent(new Event('resize'));
    """)
    
    # Final pause for animations to complete
    time.sleep(1.0)
    print("✅ Scroll completed - page ready for capture from the bottom")

def capture_screenshot(url, device_key, device_config, base_path, timestamp, wait_time=3.0, smooth_scroll=False, auto_dismiss=False):
    """Captures screenshots of a URL for a specific device"""
    # Only import playwright when needed
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("❌ Error: The 'playwright' library is not installed")
        print("💡 Install with: pip install playwright")
        print("💡 Then run: playwright install")
        return
    
    print(f"📱 Configuring: {device_config['nombre']} ({device_config['width']}x{device_config['height']})")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport=device_config)
        
        try:
            print(f"📸 Navigating to: {url}")
            page.goto(url, wait_until="networkidle")
            
            # Wait specified time for animations
            wait_for_animations(page, wait_time)
            
            # Close pop-ups automatically if activated
            if auto_dismiss:
                auto_dismiss_popups(page)
            
            # Captura normal (viewport)
            normal_capture_filename = generate_capture_filename(url, device_key, timestamp, False)
            normal_capture_path = base_path / normal_capture_filename
            page.screenshot(path=str(normal_capture_path))
            print(f"✅ Viewport capture: {normal_capture_path}")
            
            # Full capture (scrollable page)
            if smooth_scroll:
                smooth_scroll_page(page)
                # Wait minimum time after smooth scroll
                wait_for_animations(page, 1.0)  # Optimized minimum time
            
            full_capture_filename = generate_capture_filename(url, device_key, timestamp, True)
            full_capture_path = base_path / full_capture_filename
            page.screenshot(path=str(full_capture_path), full_page=True)
            print(f"✅ Full page capture: {full_capture_path}")
            
        except Exception as e:
            print(f"❌ Error capturing {url} on {device_key}: {e}")
        finally:
            browser.close()

def create_device_folder_structure(client_name, devices_to_use, output_dir=None):
    """Creates folder structure only for devices that will be used"""
    # Determine the base output directory
    if output_dir:
        # If a custom directory is specified
        base_output = Path(output_dir).expanduser()
    else:
        # Default: 'WSHOT' folder in user's Pictures folder (cross-platform)
        home_dir = Path.home()
        pictures_dir = home_dir / "Pictures"
        base_output = pictures_dir / "WSHOT"
    
    # Create the complete path with the client name
    base_path = base_output / client_name
    
    for device_key in devices_to_use:
        device_path = base_path / device_key
        device_path.mkdir(parents=True, exist_ok=True)
        print(f"📁 Folder verified: {device_path}")
    
    return base_path

def open_file_explorer(file_path):
    """
    Opens the system file explorer at the specified path.
    Works on Windows, macOS and Linux (automatically detects file manager).
    """
    file_path = Path(file_path).resolve()
    
    if not file_path.exists():
        print(f"⚠️  Path {file_path} does not exist, cannot open explorer")
        return False
    
    operating_system = platform.system()
    
    try:
        if operating_system == "Windows":
            # Windows: use explorer
            subprocess.run(["explorer", str(file_path)], check=False)
            print(f"📂 Opening Explorer at: {file_path}")
            
        elif operating_system == "Darwin":  # macOS
            # macOS: use open
            subprocess.run(["open", str(file_path)], check=False)
            print(f"📂 Opening Finder at: {file_path}")
            
        elif operating_system == "Linux":
            # Linux: try xdg-open (works with any default file manager)
            # xdg-open automatically detects the desktop environment file manager
            # (Dolphin en KDE, Nautilus en GNOME, Thunar en XFCE, etc.)
            try:
                subprocess.run(["xdg-open", str(file_path)], check=False, 
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"📂 Opening file explorer at: {file_path}")
            except FileNotFoundError:
                # If xdg-open is not available, try common managers
                managers = ["dolphin", "nautilus", "thunar", "nemo", "caja", "pcmanfm"]
                for manager in managers:
                    try:
                        subprocess.run([manager, str(file_path)], check=False,
                                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        print(f"📂 Opening {manager} at: {file_path}")
                        break
                    except FileNotFoundError:
                        continue
                else:
                    print(f"⚠️  Could not detect a file explorer. Path: {file_path}")
                    return False
        else:
            print(f"⚠️  Unsupported operating system: {operating_system}")
            return False
        
        return True
        
    except Exception as e:
        print(f"⚠️  Error opening file explorer: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description=r"""
                   _           _   
                  | |         | |  
     __      __ __| |__   ___ | |_ 
     \ \ /\ / / __| '_ \ / _ \| __|
      \ V  V /\__ \ | | | (_) | |_ 
       \_/\_/ |___/_| |_|\___/ \__|
                                     

🚀 Enterprise Visual Audit Platform

This tool allows you to take optimized screenshots of websites
across multiple devices and sizes, with support for animations and scroll effects.
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
USAGE EXAMPLES:
  
  Basic capture on one device:
    wshot https://example.com --device desktop
    wshot https://site.com --device mobile-17
  
  Capture on all devices:
    wshot https://example.com --all-devices
  
  Capture with custom wait time:
    wshot https://site.com --device tablet --wait-time 7
  
  Capture with smooth scroll for animations:
    wshot https://animated-site.com --all-devices --smooth-scroll
  
  Automatically close cookie banners:
    wshot https://google.com --device desktop --auto-dismiss
  
  Extract OpenGraph metadata:
    wshot https://mycompany.com --device desktop --og
  
  Super mode (complete and optimized):
    wshot https://complex-site.com --super
  
  Combining options:
    wshot https://site.com --device desktop --wait-time 4 --smooth-scroll --auto-dismiss --og
  
  Save to custom directory:
    wshot https://site.com --super --output-dir ~/Projects/Screenshots

  Open file explorer automatically:
    wshot https://site.com --super --open --auto-dismiss
    wshot https://site.com --device desktop --open

AVAILABLE DEVICES:
  mobile-se    iPhone SE (375x667)
  mobile-17    iPhone 17 (393x852)  
  tablet       iPad (768x1024)
  desktop      Desktop (1920x1080)

NOTES:
  • Screenshots are saved in folders organized by client and device
  • Client name is automatically extracted from URL
  • Two types of capture are generated: viewport and full page
  • --super mode automatically activates: all-devices + smooth-scroll + open-graph + wait-time 2s
  • --all mode automatically includes OpenGraph extraction
  • Use --auto-dismiss to automatically close cookie banners and pop-ups (ideal for Google, Facebook, etc.)
  • OpenGraph metadata is saved in opengraph/ folder with JSON and downloaded image
        """
    )
    
    parser.add_argument('url', 
                       nargs='?',  # Hacer que URL sea opcional
                       help='Complete URL of the website to capture (ex: https://example.com)')
    
    parser.add_argument('-all', '--all-devices', 
                       action='store_true',
                       help='Capture on all available devices (mobile-se, mobile-17, tablet, desktop)')
    
    parser.add_argument('--device', 
                       choices=list(DEVICE_SIZES.keys()),
                       help='Specific device to capture. Options: mobile-se, mobile-17, tablet, desktop')
    
    parser.add_argument('--client',
                       help='Custom client name to organize captures (automatically detected from URL if not specified)')
    
    parser.add_argument('--output-dir',
                       help='Custom directory to save captures (default: ~/Pictures/WSHOT/ in user Pictures folder)')
    
    parser.add_argument('--wait-time',
                       type=float,
                       default=3.0,
                       help='Wait time in seconds for animations and dynamic content to load (default: 3.0)')
    
    parser.add_argument('--smooth-scroll',
                       action='store_true',
                       help='Perform smooth scroll down before full page capture to trigger scroll-based animations')
    
    parser.add_argument('--auto-dismiss',
                       action='store_true',
                       help='🤖 Automatically close cookie banners, privacy notices and other pop-ups that block the screen. Detects and closes common buttons in multiple languages (Accept, Aceptar, Accepter, etc.)')
    
    parser.add_argument('--open-graph', '--og',
                       dest='open_graph',
                       action='store_true',
                       help='📊 Extract OpenGraph metadata (og:title, og:description, og:image, etc.) and save to JSON. Also downloads og:image. Automatically activated with --all and --super')
    
    parser.add_argument('--super',
                       action='store_true',
                       help='🚀 Super mode: automatically activates --all-devices + --smooth-scroll + --open-graph + optimized wait-time (2s) for complete and fast captures')
    
    parser.add_argument('--info',
                       action='store_true',
                       help='📖 Show complete guide and detailed usage examples')
    
    parser.add_argument('--open',
                       action='store_true',
                       help='📂 Open file explorer when captures are finished (automatically detects: Explorer on Windows, Finder on macOS, or your file manager on Linux like Dolphin, Nautilus, etc.)')
    
    args = parser.parse_args()
    
    # If extended information is requested, show it and exit
    if args.info:
        display_extended_help()
        sys.exit(0)
    
    # If not --info, then URL is required
    if not args.url:
        print(r"""
                   _           _   
                  | |         | |  
     __      __ __| |__   ___ | |_ 
     \ \ /\ / / __| '_ \ / _ \| __|
      \ V  V /\__ \ | | | (_) | |_ 
       \_/\_/ |___/_| |_|\___/ \__|
                                     
        """)
        print("❌ Error: URL is required")
        print("💡 Use --help for basic options or --info for complete guide")
        parser.print_help()
        sys.exit(1)
    
    # If --super is used, automatically activate optimized options
    if args.super:
        args.all_devices = True
        args.smooth_scroll = True
        args.open_graph = True  # Activar OpenGraph automáticamente en modo super
        # If no custom wait_time was specified, use 2 seconds for super mode (optimized)
        if args.wait_time == 3.0:  # default value
            args.wait_time = 2.0
    
    # If --all is used, automatically activate OpenGraph
    if args.all_devices and not args.open_graph:
        args.open_graph = True
    
    # Validate arguments
    if not args.all_devices and not args.device and not args.super:
        print("❌ Error: You must specify -all, --device or --super")
        print("💡 Use --help for basic options or --info for complete guide")
        parser.print_help()
        sys.exit(1)
    
    # VALIDATE URL BEFORE CREATING FOLDERS
    if not validar_url(args.url):
        print(f"❌ Error: URL {args.url} does not respond or is not accessible")
        print("💡 Verify that the URL is correct and available")
        sys.exit(1)
    
    # Auto-detect client or use provided one
    client_name = args.client or extraer_nombre_cliente(args.url)
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Determine devices to use
    if args.all_devices:
        selected_devices = list(DEVICE_SIZES.keys())
        if args.super:
            print(f"🚀 SUPER MODE ACTIVATED 🚀")
            print(f"📱 Capturing URL: {args.url}")
            print(f"👤 Client: {client_name}")
            print(f"📱 Devices: {', '.join(selected_devices)}")
            print(f"⏳ Wait time: {args.wait_time}s")
            print(f"📜 Smooth scroll: ✅ Activated")
            print(f"📊 OpenGraph extraction: ✅ Activated")
            if args.auto_dismiss:
                print(f"🤖 Auto-dismiss pop-ups: ✅ Activated")
        else:
            print(f"🚀 Capturing URL: {args.url}")
            print(f"👤 Client: {client_name}")
            print(f"📱 Devices: {', '.join(selected_devices)}")
            if args.open_graph:
                print(f"📊 OpenGraph extraction: ✅ Activated")
            if args.auto_dismiss:
                print(f"🤖 Auto-dismiss pop-ups: ✅ Activated")
    else:
        selected_devices = [args.device]
        print(f"🚀 Capturing URL: {args.url}")
        print(f"👤 Client: {client_name}")
        print(f"📱 Device: {args.device}")
        if args.smooth_scroll:
            print(f"📜 Smooth scroll: ✅ Activated")
        if args.wait_time != 3.0:
            print(f"⏳ Wait time: {args.wait_time}s")
        if args.open_graph:
            print(f"📊 OpenGraph extraction: ✅ Activated")
        if args.auto_dismiss:
            print(f"🤖 Auto-dismiss pop-ups: ✅ Activated")
    
    # Create folder structure ONLY for requested devices
    base_path = create_device_folder_structure(client_name, selected_devices, args.output_dir)
    
    print(f"📁 Base folder: {base_path}")
    print("="*60)
    
    # Extract OpenGraph if activated (before captures)
    og_data = None
    if args.open_graph:
        # Import playwright for OpenGraph extraction
        try:
            from playwright.sync_api import sync_playwright
            
            print(f"\n📊 Extracting OpenGraph metadata...")
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                # Use desktop viewport for OpenGraph
                page = browser.new_page(viewport=DEVICE_SIZES['desktop'])
                
                try:
                    page.goto(args.url, wait_until="networkidle")
                    # Wait a bit for everything to load
                    time.sleep(2)
                    
                    # Close pop-ups if auto-dismiss is activated
                    if args.auto_dismiss:
                        auto_dismiss_popups(page)
                    
                    # Extract OpenGraph
                    og_data = extract_opengraph_metadata(page, args.url, base_path, timestamp)
                    
                except Exception as e:
                    print(f"❌ Error extracting OpenGraph: {e}")
                finally:
                    browser.close()
                    
        except ImportError:
            print("❌ Error: The 'playwright' library is not installed")
            print("💡 Install with: pip install playwright")
    
    # Perform captures
    for i, device_key in enumerate(selected_devices, 1):
        print(f"\n[{i}/{len(selected_devices)}] Processing {device_key}...")
        device_config = DEVICE_SIZES[device_key]
        device_path = base_path / device_key
        
        capture_screenshot(args.url, device_key, device_config, device_path, timestamp, args.wait_time, args.smooth_scroll, args.auto_dismiss)
    
    print(r"""
    ╔══════════════════════════════════════════════════════════════════╗
    ║                                                                  ║
    ║                             _           _                        ║
    ║                            | |         | |                       ║
    ║               __      __ __| |__   ___ | |_                      ║
    ║               \ \ /\ / / __| '_ \ / _ \| __|                     ║
    ║                \ V  V /\__ \ | | | (_) | |_                      ║
    ║                 \_/\_/ |___/_| |_|\___/ \__|                     ║
    ║                                                                  ║
    ║                   🎉 Screenshots completed!                      ║
    ╚══════════════════════════════════════════════════════════════════╝""")
    print(f"📂 Check images at: {base_path}")
    
    # Open file explorer if requested
    if args.open:
        print("")
        open_file_explorer(base_path)

if __name__ == "__main__":
    main()