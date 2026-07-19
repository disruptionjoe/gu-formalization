param(
    [switch]$Update,
    [switch]$Cache
)

$ErrorActionPreference = "Stop"

if (-not (Get-Command lake -ErrorAction SilentlyContinue)) {
    [Console]::Error.WriteLine("Lake is not installed or not on PATH. Install Lean/elan, then rerun this script.")
    exit 127
}

# All Windows-host GU Lean invocations use this wrapper. The host-local exclusive file handle
# prevents compliant direct-chat and scheduled GU runs on this host from starting
# overlapping local builds. It does not coordinate another host or cloud runner.
# The workspace contract still forbids overlapping Lean work in other repos.
$lockRoot = Join-Path ([System.IO.Path]::GetTempPath()) "CapacityOS-locks"
New-Item -ItemType Directory -Force -Path $lockRoot | Out-Null
$lockPath = Join-Path $lockRoot "lean-build.lock"
$lockStream = $null

try {
    try {
        $lockStream = [System.IO.File]::Open(
            $lockPath,
            [System.IO.FileMode]::OpenOrCreate,
            [System.IO.FileAccess]::ReadWrite,
            [System.IO.FileShare]::None
        )
    }
    catch [System.IO.IOException] {
        [Console]::Error.WriteLine("Another Lean/Lake build holds the CapacityOS lock: $lockPath")
        exit 75
    }

    $receipt = [System.Text.Encoding]::UTF8.GetBytes(
        "pid=$PID`nstarted_utc=$([DateTime]::UtcNow.ToString('o'))`nrepo=$((Get-Location).Path)`n"
    )
    $lockStream.SetLength(0)
    $lockStream.Write($receipt, 0, $receipt.Length)
    $lockStream.Flush()

    if ($Update) {
        lake update
        if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
    }

    if ($Cache) {
        lake exe cache get
        if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
    }

    # Lake 5 no longer accepts the historical `lake build -j1` form. The
    # wrapper's host-local lock still serializes GU Lean builds on this machine.
    lake build
    exit $LASTEXITCODE
}
finally {
    if ($null -ne $lockStream) {
        $lockStream.Dispose()
    }
}
