import os
import hashlib
import json

def audit_source_map_artifact(file_path):
    print(f"[*] Auditing local source map artifact: {file_path}")
    if not os.path.exists(file_path):
        print(f"[!] Artifact not found: {file_path}")
        return

    # Compute SHA-256 for chain of custody
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    
    file_hash = sha256_hash.hexdigest()
    print(f"[+] Artifact SHA-256 Checksum: {file_hash}")

    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            sources = data.get('sources', [])
            content = data.get('sourcesContent', [])
            print(f"[+] Total Mapped Components/Modules: {len(sources)}")
            print(f"[+] SourcesContent Available: {len([c for c in content if c])}")
        except Exception as e:
            print(f"[!] Failed to parse source map JSON: {e}")

if __name__ == "__main__":
    import sys
    target_file = sys.argv[1] if len(sys.argv) > 1 else "RC9082a0018d6a47d9afe33d420c53c08c-source.map"
    audit_source_map_artifact(target_file)
