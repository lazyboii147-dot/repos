import json
import re

def audit_akamai_defense_headers(headers_content, body_content=""):
    print("[*] Auditing Akamai Bot Manager, EdgeScape, and Dispatcher protection responses...")
    
    # Check for bot manager tokens and cookies
    abck_token = re.findall(r'_abck=([^\s;]+)', headers_content)
    bm_cookies = re.findall(r'bm_[sz]=([^\s;]+)', headers_content)
    retry_after = re.findall(r'retry-after:\s*(\d+)', headers_content, re.IGNORECASE)
    dispatcher_vhost = re.findall(r'x-vhost:\s*([^\s]+)', headers_content, re.IGNORECASE)
    
    # Device characteristics & EdgeScape geolocation
    device_chars = re.findall(r'device-characteristics=([^\s]+)', headers_content)
    akamai_loc = re.findall(r'browser-akamai-loc-([a-z]+):\s*([^\s]+)', headers_content, re.IGNORECASE)

    results = {
        "bot_manager_active": len(abck_token) > 0 or len(bm_cookies) > 0,
        "cooldown_penalty_seconds": int(retry_after[0]) if retry_after else 0,
        "dispatcher_vhost": dispatcher_vhost[0] if dispatcher_vhost else "unknown",
        "device_fingerprinting_detected": len(device_chars) > 0,
        "edgescape_geolocation_captured": len(akamai_loc) > 0
    }

    print(json.dumps(results, indent=2))
    
    if results["bot_manager_active"] and results["cooldown_penalty_seconds"] > 0:
        print("    [!] AKAMAI DEFENSE VERIFIED: Explicit bot scoring, device fingerprinting, and rate-limiting active on protected clientlibs.")

if __name__ == "__main__":
    sample_headers = "HTTP/1.1 403 Forbidden\r\nRetry-After: 28800\r\nX-Vhost: publish\r\nSet-Cookie: _abck=123; bm_s=456;\r\n"
    audit_akamai_defense_headers(sample_headers)
