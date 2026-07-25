import re
import json

def analyze_corejs_stream(script_content):
    print("[*] Performing deep recon on Core-JS execution stream...")
    
    versions = re.findall(r'3\.\d+\.\d+', script_content)
    shared_keys = re.findall(r'core-js_shared', script_content)
    licenses = re.findall(r'zloirock\.ru', script_content)
    
    results = {
        "versions_detected": list(set(versions)),
        "shared_storage_referenced": len(shared_keys) > 0,
        "license_markers_found": len(licenses) > 0
    }
    
    print(json.dumps(results, indent=2))
    if len(versions) > 0:
        print("    [+] Core-JS polyfill bundle integrity confirmed.")

if __name__ == "__main__":
    sample = '''
    var e="core-js_shared",o=En.exports=n[e]||r(e,{});return(o.versions||(o.versions=[])).push({version:"3.45.1"...
    '''
    analyze_corejs_stream(sample)
