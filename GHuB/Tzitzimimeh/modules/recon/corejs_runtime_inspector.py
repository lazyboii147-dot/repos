import requests
import re

def inspect_corejs_runtime(script_path_or_url):
    print(f"[*] Inspecting component container for runtime polyfill injection...")
    # Supporting local or remote analysis
    if script_path_or_url.startswith("http"):
        res = requests.get(script_path_or_url)
        content = res.text if res.status_code == 200 else ""
    else:
        try:
            with open(script_path_or_url, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception:
            content = ""

    if content:
        versions = re.findall(r'version\s*:\s*[\"\']3\.\d+\.\d+[\"\']', content)
        symbols = re.findall(r'Symbol', content)
        json_overrides = re.findall(r'JSON\.stringify', content)
        
        print(f"[+] Core-JS Version Signatures Found: {len(versions)}")
        print(f"[+] Symbol/Built-in References Found: {len(symbols)}")
        print(f"[+] JSON Serialization Signatures Found: {len(json_overrides)}")
        
        if len(versions) > 0:
            print("    [!] CRITICAL: Full polyfill runtime injection detected in component bundle.")
    else:
        print("[!] Failed to retrieve or read script content.")

if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "https://assets.adobedtm.com/launch_container_mock.js"
    inspect_corejs_runtime(target)
