import requests
import re

def audit_corejs_injection(container_url):
    print(f"[*] Auditing target container for Core-JS polyfill injection...")
    res = requests.get(container_url)
    if res.status_code == 200:
        content = res.text
        matches = re.findall(r'version\s*:\s*[\"\']3\.\d+\.\d+[\"\']', content)
        print(f"[+] Found {len(matches)} Core-JS version matching signatures.")
        if len(matches) > 0:
            print("    [!] WARNING: Large polyfill runtime injected via Tag Manager (Prototype pollution / Supply-chain risk).")
    else:
        print(f"[!] Failed to fetch container: {res.status_code}")

if __name__ == "__main__":
    audit_corejs_injection("https://assets.adobedtm.com/launch_container_mock.js")
