import requests
from bs4 import BeautifulSoup
import json

def scan_components(url):
    print(f"[*] Scanning Aries components on target: {url}")
    headers = {'User-Agent': 'Tzitzimimeh-Recon-Agent/1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"[!] Error fetching target: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    components = []
    
    for div in soup.find_all(True, {'data-component-endpoint': True}):
        comp_info = {
            "id": div.get('data-component-id'),
            "name": div.get('data-component-name'),
            "endpoint": div.get('data-component-endpoint')
        }
        components.append(comp_info)

    print(f"[+] Discovered {len(components)} component endpoints.")
    print(json.dumps(components, indent=2))

if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "https://www.marriott.com"
    scan_components(target)
