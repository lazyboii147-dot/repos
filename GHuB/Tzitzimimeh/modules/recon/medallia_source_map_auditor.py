import json
import re

def audit_medallia_source_map(map_file_content):
    print("[*] Auditing Medallia / Kampyle source map for internal module exposure...")
    try:
        data = json.loads(map_file_content)
        sources = data.get('sources', [])
        sources_content = data.get('sourcesContent', [])
        
        print(f"[+] Total Exposed Internal Modules: {len(sources)}")
        print(f"[+] Total SourcesContent Blocks: {len([c for c in sources_content if c])}")
        
        # Check for critical internal modules
        critical_modules = [
            "KAMPYLE_CONSTANT.js",
            "MDIGITAL_CONFIGURATION.js",
            "KAMPYLE_TARGETING.js",
            "KAMPYLE_SCREEN_CAPTURE.js",
            "MDIGITAL_ANALYTICS.js"
        ]
        
        exposed_critical = [m for m in critical_modules if any(m in s for s in sources)]
        print(f"[+] Critical Modules Identified: {exposed_critical}")
        
        if len(exposed_critical) > 0:
            print("    [!] P0 CRITICAL EXPOSURE: Full proprietary SDK source tree and configuration exposed via public source map.")
            
    except Exception as e:
        print(f"[!] Failed to parse source map: {e}")

if __name__ == "__main__":
    # Mock analysis execution
    sample_map = '{"sources": ["KAMPYLE_CONSTANT.js", "MDIGITAL_CONFIGURATION.js", "KAMPYLE_TARGETING.js"], "sourcesContent": ["const A=1;", "const B=2;", "const C=3;"]}'
    audit_medallia_source_map(sample_map)
