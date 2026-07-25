import re
import json

def audit_medallia_embed(script_content):
    print("[*] Auditing Medallia Kampyle embed configuration script...")
    
    analytics_urls = re.findall(r'https?://[^\s\"\'\(\)]+medallia\.com[^\s\"\'\(\)]*', script_content)
    site_codes = re.findall(r'JS_SITE_CODE:\s*[\"\']([^"\']+)[\"\']', script_content)
    integration_ids = re.findall(r'DEFAULT_MEC_INTEGRATION_ID:\s*[\"\']([^"\']+)[\"\']', script_content)

    results = {
        "medallia_endpoints": list(set(analytics_urls)),
        "js_site_code_references": list(set(site_codes)),
        "integration_identifiers": list(set(integration_ids))
    }

    print(json.dumps(results, indent=2))
    if len(analytics_urls) > 0:
        print("    [!] WARNING: Third-party customer feedback and analytics telemetry embed detected.")

if __name__ == "__main__":
    sample = 'var n={DEFAULT_ANALYTICS_SUBMIT_EVENTS_URL:"https://analytics-fe.digital-cloud.medallia.com/api/web/events",JS_SITE_CODE:"resources.digital-cloud.medallia.com/wdcus/1745/onsite/generic.js"};'
    audit_medallia_embed(sample)
