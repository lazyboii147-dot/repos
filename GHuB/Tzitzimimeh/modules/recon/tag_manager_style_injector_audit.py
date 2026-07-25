import requests
import re

def audit_tag_manager_script(script_url):
    print(f"[*] Auditing tag manager script for dynamic styling/DOM injection: {script_url}")
    res = requests.get(script_url)
    if res.status_code == 200:
        content = res.text
        # Check for style element creation patterns
        style_matches = re.findall(r'document\.createElement\s*\(\s*["\']style["\']\s*\)', content)
        print(f"[+] Found {len(style_matches)} dynamic style element creation signatures.")
        
        if len(style_matches) > 0:
            print("    [!] WARNING: Script dynamically injects styles at runtime (UI modification vector).")
    else:
        print(f"[!] Failed to fetch script: {res.status_code}")

if __name__ == "__main__":
    import sys
    url = sys.argv[1] if len(sys.argv) > 1 else "https://assets.adobedtm.com/rc/RC52bfb068605b4863962807a92d4a1a6d-source.min.js"
    audit_tag_manager_script(url)
