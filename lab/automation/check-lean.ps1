param(
    [switch]$Update,
    [switch]$Cache
)

$ErrorActionPreference = "Stop"

if (-not (Get-Command lake -ErrorAction SilentlyContinue)) {
    Write-Error "Lake is not installed or not on PATH. Install Lean/elan, then rerun this script."
    exit 127
}

if ($Update) {
    lake update
}

if ($Cache) {
    lake exe cache get
}

lake build
