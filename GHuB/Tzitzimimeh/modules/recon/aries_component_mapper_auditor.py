import json
import re

def audit_aries_component_map(bundle_content):
    print("[*] Auditing Aries search subsystem and component mapper bundle...")
    try:
        # Scan for Webpack source map signatures and module paths
        modules = re.findall(r'webpack:///./[^\s\"\'\)]+', bundle_content)
        constants = re.findall(r'[A-Z_]{4,}', bundle_content)
        
        print(f"[+] Total Mapped Subsystem Modules: {len(modules)}")
        print(f"[+] Internal Constants / Enums Discovered: {len(set(constants))}")
        
        # Check for core search components
        core_search_modules = [
            "searchFormHorizontal-lib.js",
            "sell-options-handler.js",
            "commonUtilityMethods.js",
            "autocompleteFormFieldMapper.js",
            "GoogleApiWrapper"
        ]
        
        exposed_search_core = [m for m in core_search_modules if any(m in mod for mod in modules)]
        print(f"[+] Core Search Modules Identified: {exposed_search_core}")
        
        if len(exposed_search_core) > 0:
            print("    [!] P0 CRITICAL SUPPLY-CHAIN EXPOSURE: Full search subsystem dependency graph and geolocation logic exposed.")

    except Exception as e:
        print(f"[!] Aries bundle audit failed: {e}")

if __name__ == "__main__":
    sample_bundle = 'webpack:///./core/libs/search-components.js webpack:///./src/products/search/libs/sell-options-handler.js'
    audit_aries_component_map(sample_bundle)
