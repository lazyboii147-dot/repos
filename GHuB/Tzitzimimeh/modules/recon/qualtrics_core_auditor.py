import json
import re

def audit_qualtrics_core_module(module_content):
    print("[*] Auditing Qualtrics SiteIntercept CoreModule and logic tree evaluator...")
    try:
        # Extract AST logic nodes and evaluators
        logic_evaluators = re.findall(r'evaluate(?:LogicTree|ComparatorNode|ConjunctionNode|LogicNode)', module_content)
        frustration_signals = re.findall(r'(?:RAGE_CLICK|MOUSE_THRASH|ERROR_CLICK|DEAD_CLICK)', module_content)
        integration_hooks = re.findall(r'(?:SiteCatalystValue|google_tag_manager|DataLayerHelper)', module_content)
        
        print(f"[+] Logic Tree Evaluators Discovered: {len(logic_evaluators)}")
        print(f"[+] Frustration Signal Patterns Found: {set(frustration_signals)}")
        print(f"[+] Third-Party Integration Hooks: {set(integration_hooks)}")
        
        if len(logic_evaluators) > 0 and len(frustration_signals) > 0:
            print("    [!] P0 CRITICAL EXPOSURE: Client-side targeting AST evaluator and behavioral frustration monitoring active.")

    except Exception as e:
        print(f"[!] Qualtrics module audit failed: {e}")

if __name__ == "__main__":
    sample_code = "evaluateLogicTree = function() { return RAGE_CLICK + SiteCatalystValue; };"
    audit_qualtrics_core_module(sample_code)
