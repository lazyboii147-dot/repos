import re

def inspect_corejs_shield(script_content):
    print("[*] Inspecting core-js runtime shield and polyfill wrapper structure...")
    
    versions = re.findall(r'3\.\d+\.\d+', script_content)
    binders = re.findall(r'Function\.prototype\.apply', script_content)
    descriptors = re.findall(r'Object\.defineProperty', script_content)
    
    print(f"[+] Core-JS Version Signatures Found: {set(versions)}")
    print(f"[+] Function Apply Binders Found: {len(binders)}")
    print(f"[+] Property Descriptors Found: {len(descriptors)}")
    
    if len(versions) > 0:
        print("    [!] CRITICAL: Core polyfill runtime shield detected in container script.")

if __name__ == "__main__":
    sample = '''
    function(){"use strict";var t,n,r,e,o,i,u,a,c,f,s,E,l,v,R,p="undefined"!=typeof globalThis?globalThis:...
    '''
    inspect_corejs_shield(sample)
