import re
import json

def audit_dynatrace_bootstrap(script_path_or_content):
    print("[*] Auditing Dynatrace RUM bootstrap script for sensitive field ingestion...")
    
    # Check for dataLayer mappings
    mappings = re.findall(r'mdcc\d+\s*=\s*bdataLayer\.([a-zA-Z0-9_]+)', script_path_or_content)
    cookies = re.findall(r'__dTCookie', script_path_or_content)
    interceptors = re.findall(r'addEventListener', script_path_or_content)

    results = {
        "mapped_datalayer_fields": list(set(mappings)),
        "cookie_manipulation_detected": len(cookies) > 0,
        "event_interception_detected": len(interceptors) > 0
    }

    print(json.dumps(results, indent=2))
    if len(mappings) > 0:
        print("    [!] WARNING: Sensitive data layer properties mapped into monitoring metadata.")

if __name__ == "__main__":
    sample = "mdcc38=bdataLayer.sessionId; mdcc44=bdataLayer.search_criteria; document.cookie='__dTCookie=1;SameSite=Lax';"
    audit_dynatrace_bootstrap(sample)
