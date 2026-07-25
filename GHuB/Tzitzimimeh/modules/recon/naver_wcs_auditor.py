import requests
import re

def audit_naver_injection(container_url):
    print(f"[*] Auditing target container for Naver WCS telemetry injection...")
    res = requests.get(container_url)
    if res.status_code == 200:
        content = res.text
        matches = re.findall(r'wcs\.naver\.net', content)
        print(f"[+] Found {len(matches)} references to wcs.naver.net.")
        if len(matches) > 0:
            print("    [!] WARNING: Uncontrolled third-party analytics injection detected via Tag Manager.")
    else:
        print(f"[!] Failed to fetch container: {res.status_code}")

if __name__ == "__main__":
    audit_naver_injection("https://assets.adobedtm.com/launch_container_mock.js")
