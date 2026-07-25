import re
import json

def audit_kakao_pixel_script(script_content):
    print("[*] Auditing Kakao Pixel tracking script structure...")
    
    account_keys = re.findall(r'KAKAO_PIXEL_[A-Z_]+', script_content)
    weakmap_shims = re.findall(r'Weakmap-shim', script_content)
    events = re.findall(r'key:\s*["\']([a-zA-Z]+)["\'],value:\s*function', script_content)

    results = {
        "kakao_pixel_keys": list(set(account_keys)),
        "weakmap_shim_detected": len(weakmap_shims) > 0,
        "tracked_events_sample": list(set(events))[:10]
    }

    print(json.dumps(results, indent=2))
    if len(account_keys) > 0:
        print("    [!] WARNING: Third-party analytics pixel container with identifier persistence detected.")

if __name__ == "__main__":
    sample = "var k={kakaoAccountId:'KAKAO_PIXEL_ACCID',idfv:'KAKAO_PIXEL_IDFV'};"
    audit_kakao_pixel_script(sample)
