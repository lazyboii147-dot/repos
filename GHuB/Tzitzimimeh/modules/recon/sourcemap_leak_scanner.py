import requests
import json

def audit_sourcemap(map_url):
    print(f"[*] Auditing source map: {map_url}")
    res = requests.get(map_url)
    if res.status_code == 200:
        data = res.json()
        sources = data.get('sources', [])
        content = data.get('sourcesContent', [])
        print(f"[+] Found {len(sources)} source files embedded in map.")
        for i, src in enumerate(sources[:10]):
            has_content = "Yes" if i < len(content) and content[i] else "No"
            print(f"    - {src} (Content Present: {has_content})")
    else:
        print(f"[!] Failed to fetch source map: {res.status_code}")

if __name__ == "__main__":
    import sys
    url = sys.argv[1] if len(sys.argv) > 1 else "https://www.marriott.com/aries/components/messageResource/messageResource.css.map"
    audit_sourcemap(url)
