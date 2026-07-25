import json
import re

class ComponentEngine:
    def __init__(self, html_content):
        self.html = html_content

    def extract_hdvars(self):
        match = re.search(r'var hd_vars\s*=\s*(\{.*?\});', self.html, re.DOTALL)
        if match:
            return json.loads(match.group(1))
        return None

    def parse_session_cleanup_endpoint(self):
        match = re.search(r'data-sessioncleanupurl=["\']([^"\']+)["\']', self.html)
        return match.group(1) if match else None

if __name__ == "__main__":
    print("[*] Initializing Tzitzimimeh Component Engine Core...")
