import json
import re
import urllib.parse
import html
import base64

class TzitzimimehUniversalRegexScanner:
    def __init__(self):
        self.framework = "Tzitzimimeh Monolith"
        self.tier = "RED-COMPLIANCE"
        self.regex_patterns = {
            "telemetry_endpoints": re.compile(r"https?://([a-zA-Z0-9-]+\.)*(analytics|metrics|telemetry|stats|collector|siteintercept|digital-cloud)\.[a-zA-Z]{2,}/.*", re.IGNORECASE),
            "source_map_references": re.compile(r".*\.js\.map$", re.IGNORECASE),
            "restricted_path_access": re.compile(r"/etc\.clientlibs/.*", re.IGNORECASE),
            "sensitive_session_tokens": re.compile(r"(md_ex_AuthorizationToken|fs_uid|_abck|bm_[sz]|QSI_.*_intercept)", re.IGNORECASE),
            "arbitrary_execution_sinks": re.compile(r"(eval|setTimeout|setInterval|Function)\s*\(", re.IGNORECASE),
            "dom_manipulation_sinks": re.compile(r"(innerHTML|outerHTML|document\.write)\s*=", re.IGNORECASE)
        }

    def decode_payload(self, encoded_string):
        decoded_variants = {
            "raw": encoded_string,
            "url_decoded": urllib.parse.unquote(encoded_string),
            "html_decoded": html.unescape(encoded_string)
        }
        try:
            padded = encoded_string + '=' * (-len(encoded_string) % 4)
            decoded_bytes = base64.b64decode(padded, validate=True)
            decoded_variants["base64_decoded"] = decoded_bytes.decode('utf-8', errors='ignore')
        except Exception:
            decoded_variants["base64_decoded"] = None

        try:
            clean_hex = re.sub(r'\\x|0x|\s', '', encoded_string)
            if len(clean_hex) % 2 == 0 and all(c in '0123456789abcdefABCDEF' for c in clean_hex):
                decoded_variants["hex_decoded"] = bytes.fromhex(clean_hex).decode('utf-8', errors='ignore')
            else:
                decoded_variants["hex_decoded"] = None
        except Exception:
            decoded_variants["hex_decoded"] = None

        return decoded_variants

    def scan_content(self, content_stream):
        findings = []
        for line_num, line in enumerate(content_stream.splitlines(), start=1):
            decoded_dict = self.decode_payload(line)
            for variant_name, text_val in decoded_dict.items():
                if not text_val:
                    continue
                for category, pattern in self.regex_patterns.items():
                    matches = pattern.findall(text_val)
                    if matches:
                        findings.append({
                            "line": line_num,
                            "category": category,
                            "encoding_variant": variant_name,
                            "matched_data": matches
                        })
        return findings

if __name__ == "__main__":
    scanner = TzitzimimehUniversalRegexScanner()
    print("[+] Tzitzimimeh Universal Regex Scanner fully operational.")
