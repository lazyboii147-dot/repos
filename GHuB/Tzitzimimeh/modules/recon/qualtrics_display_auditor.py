import json
import re

def audit_qualtrics_display_engine(module_content):
    print("[*] Auditing Qualtrics Target Display Engine and Utility Layer...")
    try:
        # Scan for display suppression, telemetry, and action engines
        suppression_keys = re.findall(r'(?:shouldPreventRepeatedDisplay|QSI_.*_intercept)', module_content)
        action_engines = re.findall(r'(?:runJavaScriptAction|evalJS|AddCookie|RemoveCookie)', module_content)
        dom_measurements = re.findall(r'(?:getDimensions|convertPercentToPixel|cumulativeOffset|getWindowSize)', module_content)
        
        print(f"[+] Suppression & Cookie Patterns: {set(suppression_keys)}")
        print(f"[+] Action Engine Hooks Found: {set(action_engines)}")
        print(f"[+] DOM Measurement Functions: {len(dom_measurements)}")
        
        if len(suppression_keys) > 0 and len(action_engines) > 0:
            print("    [!] P0 CRITICAL EXPOSURE: Client-side display suppression, impression telemetry, and arbitrary JS execution engines active.")

    except Exception as e:
        print(f"[!] Qualtrics display audit failed: {e}")

if __name__ == "__main__":
    sample_code = "shouldPreventRepeatedDisplay = function() { return runJavaScriptAction(); };"
    audit_qualtrics_display_engine(sample_code)
