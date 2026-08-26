$root = Split-Path $PSScriptRoot -Parent
$roundcube = Join-Path $root "docker\roundcube"

Write-Host "Starting DLP Application..."

Set-Location $roundcube

docker compose up -d

if ($LASTEXITCODE -ne 0) {
    Write-Host "Failed to start Docker."
    exit 1
}

Write-Host ""
Write-Host "DLP Application started successfully."
Write-Host "Roundcube: http://localhost:8000"