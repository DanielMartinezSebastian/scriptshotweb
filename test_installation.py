#!/usr/bin/env python3
"""
Wshot Installation Verification
Run this after installing with pip to verify everything works correctly.
Especially useful to check that Playwright's Chromium browser was installed.
"""

import sys

def test_wshot():
    """Test if wshot is properly installed and importable"""
    print("🔍 Testing wshot installation...")
    try:
        from wshot import main
        print("✅ Wshot package installed correctly")
        return True
    except ImportError as e:
        print(f"❌ Wshot not installed: {e}")
        print("   Install with: pip install git+https://github.com/DanielMartinezSebastian/wshot.git")
        return False

def test_chromium():
    """Test if Chromium browser is installed for Playwright"""
    print("\n🔍 Testing Chromium browser...")
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            browser.close()
            print("✅ Chromium browser is working")
            return True
    except Exception as e:
        print(f"❌ Chromium not working: {e}")
        print("   Install with: playwright install chromium")
        return False

def main():
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                Wshot Installation Test                    ║")
    print("╚════════════════════════════════════════════════════════════╝\n")
    
    # Test core installation
    wshot_ok = test_wshot()
    
    # Test browser (most common issue)
    chromium_ok = test_chromium() if wshot_ok else False
    
    print("\n" + "="*60)
    if wshot_ok and chromium_ok:
        print("🎉 SUCCESS! Wshot is ready to use!")
        print("\n💡 Try it out:")
        print("   wshot --help")
        print("   wshot https://example.com --device desktop")
        return 0
    else:
        print("❌ Installation incomplete - see errors above")
        return 1

if __name__ == "__main__":
    sys.exit(main())

if __name__ == "__main__":
    sys.exit(main())
