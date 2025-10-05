#!/usr/bin/env python3
"""
Simple test to verify wshot installation
Run this after installing with pip to check if everything is working
"""

import sys

def test_import():
    """Test if wshot can be imported"""
    print("Testing import of wshot package...")
    try:
        from wshot import main
        print("✅ wshot package imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Failed to import wshot: {e}")
        return False

def test_playwright():
    """Test if playwright is installed"""
    print("\nTesting playwright installation...")
    try:
        import playwright
        print(f"✅ Playwright installed (version {playwright.__version__})")
        return True
    except ImportError:
        print("❌ Playwright not installed")
        print("   Install with: pip install playwright")
        return False

def test_requests():
    """Test if requests is installed"""
    print("\nTesting requests installation...")
    try:
        import requests
        print(f"✅ Requests installed (version {requests.__version__})")
        return True
    except ImportError:
        print("❌ Requests not installed")
        print("   Install with: pip install requests")
        return False

def test_chromium():
    """Test if chromium is installed"""
    print("\nTesting Chromium browser...")
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            try:
                browser = p.chromium.launch(headless=True)
                browser.close()
                print("✅ Chromium browser is installed and working")
                return True
            except Exception as e:
                print(f"❌ Chromium not installed or not working: {e}")
                print("   Install with: playwright install chromium")
                return False
    except ImportError:
        print("❌ Cannot test Chromium (playwright not installed)")
        return False

def main():
    print("╔════════════════════════════════════════════════════════════╗")
    print("║            Wshot Installation Verification Test           ║")
    print("╚════════════════════════════════════════════════════════════╝\n")
    
    results = []
    results.append(test_import())
    results.append(test_playwright())
    results.append(test_requests())
    results.append(test_chromium())
    
    print("\n" + "="*60)
    if all(results):
        print("✅ ALL TESTS PASSED - Wshot is ready to use!")
        print("\nTry it out:")
        print("  wshot --help")
        print("  wshot --info")
        return 0
    else:
        print("❌ SOME TESTS FAILED - Please fix the issues above")
        return 1

if __name__ == "__main__":
    sys.exit(main())
