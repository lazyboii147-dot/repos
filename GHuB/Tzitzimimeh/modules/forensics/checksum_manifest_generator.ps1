param(
    [string]\ = "evidence_manifest.sha256"
)
Write-Host "[*] Generating SHA-256 manifest for artifacts..." -ForegroundColor Yellow
Get-ChildItem -Recurse -File -Include *.map, *.json, *.css, *.js | Get-FileHash -Algorithm SHA256 | Select-Object Hash, Path | Out-File -FilePath \ -Encoding utf8
Write-Host "[+] Manifest generated successfully: \" -ForegroundColor Green
