param(
    [string]$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path,
    [string]$Runner = $env:GU_FRONTIER_RUNNER,
    [int]$TimeoutMinutes = 55
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Runner)) {
    $Runner = "auto"
}

$automationRoot = Join-Path $RepoRoot "automation"
$runsRoot = Join-Path $automationRoot "runs"
$logsRoot = Join-Path $automationRoot "logs"
$lockPath = Join-Path $automationRoot "hourly-frontier.lock"
$promptTemplatePath = Join-Path $automationRoot "hourly-frontier-prompt.md"

New-Item -ItemType Directory -Force -Path $runsRoot, $logsRoot | Out-Null

function Test-ProcessAlive {
    param([int]$ProcessId)
    try {
        $null = Get-Process -Id $ProcessId -ErrorAction Stop
        return $true
    } catch {
        return $false
    }
}

if (Test-Path -LiteralPath $lockPath) {
    $lock = Get-Content -LiteralPath $lockPath -Raw | ConvertFrom-Json
    $ageMinutes = ((Get-Date) - [datetime]$lock.started_at).TotalMinutes
    if ((Test-ProcessAlive -ProcessId ([int]$lock.pid)) -and $ageMinutes -lt ($TimeoutMinutes + 10)) {
        Add-Content -LiteralPath (Join-Path $logsRoot "scheduler.log") -Value "$(Get-Date -Format o) skipped: previous run still active (pid $($lock.pid))"
        exit 0
    }
    Remove-Item -LiteralPath $lockPath -Force
}

$runId = Get-Date -Format "yyyyMMdd-HHmmss"
$startedAt = Get-Date -Format o
$runDir = Join-Path $runsRoot $runId
New-Item -ItemType Directory -Force -Path $runDir | Out-Null

@{
    pid = $PID
    run_id = $runId
    started_at = $startedAt
} | ConvertTo-Json | Set-Content -LiteralPath $lockPath -Encoding UTF8

$prompt = Get-Content -LiteralPath $promptTemplatePath -Raw
$prompt = $prompt.Replace("{{RUN_ID}}", $runId)
$prompt = $prompt.Replace("{{RUN_STARTED_AT}}", $startedAt)
$prompt = $prompt.Replace("{{REPO_ROOT}}", $RepoRoot)

$promptPath = Join-Path $runDir "prompt.md"
$stdoutPath = Join-Path $runDir "stdout.log"
$stderrPath = Join-Path $runDir "stderr.log"
$exitPath = Join-Path $runDir "exit.json"
$prompt | Set-Content -LiteralPath $promptPath -Encoding UTF8

function Resolve-FrontierRunner {
    param([string]$RequestedRunner)

    if ($RequestedRunner -eq "auto") {
        $claude = Get-Command "claude" -ErrorAction SilentlyContinue
        if ($null -ne $claude) {
            return @{ Name = "claude"; Path = $claude.Source }
        }

        $codex = Get-Command "codex" -ErrorAction SilentlyContinue
        if ($null -ne $codex) {
            return @{ Name = "codex"; Path = $codex.Source }
        }

        throw "No supported CLI runner found. Set GU_FRONTIER_RUNNER to a working command."
    }

    $cmd = Get-Command $RequestedRunner -ErrorAction SilentlyContinue
    if ($null -eq $cmd) {
        throw "Requested runner '$RequestedRunner' was not found on PATH."
    }
    return @{ Name = $RequestedRunner; Path = $cmd.Source }
}

function ConvertTo-ProcessArgument {
    param([string]$Argument)

    if ($Argument -match '^[A-Za-z0-9_./:=\\-]+$') {
        return $Argument
    }

    return '"' + $Argument.Replace('"', '\"') + '"'
}

function New-RunnerInvocation {
    param(
        [string]$RunnerName,
        [string]$PromptPath,
        [string]$PromptText
    )

    switch -Regex ($RunnerName) {
        "claude" {
            $instruction = "Read and execute the unattended instructions in '$PromptPath'."
            $args = @("-p", $instruction, "--permission-mode", "bypassPermissions", "--effort", "high")
            if (-not [string]::IsNullOrWhiteSpace($env:GU_FRONTIER_MAX_BUDGET_USD)) {
                $args += @("--max-budget-usd", $env:GU_FRONTIER_MAX_BUDGET_USD)
            }
            return @{ Arguments = $args; StandardInput = "" }
        }
        "codex" {
            return @{ Arguments = @("exec", "--full-auto", "--skip-git-repo-check", "-"); StandardInput = $PromptText }
        }
        default {
            return @{ Arguments = @(); StandardInput = $PromptText }
        }
    }
}

try {
    $resolvedRunner = Resolve-FrontierRunner -RequestedRunner $Runner
    $invocation = New-RunnerInvocation -RunnerName $resolvedRunner.Name -PromptPath $promptPath -PromptText $prompt

    Push-Location $RepoRoot
    try {
        $psi = [System.Diagnostics.ProcessStartInfo]::new()
        $psi.FileName = $resolvedRunner.Path
        $psi.Arguments = (($invocation.Arguments | ForEach-Object { ConvertTo-ProcessArgument -Argument $_ }) -join " ")
        $psi.WorkingDirectory = $RepoRoot
        $psi.RedirectStandardInput = $true
        $psi.RedirectStandardOutput = $true
        $psi.RedirectStandardError = $true
        $psi.UseShellExecute = $false

        $process = [System.Diagnostics.Process]::new()
        $process.StartInfo = $psi
        $null = $process.Start()

        if (-not [string]::IsNullOrEmpty($invocation.StandardInput)) {
            $process.StandardInput.Write($invocation.StandardInput)
        }
        $process.StandardInput.Close()

        $stdoutTask = $process.StandardOutput.ReadToEndAsync()
        $stderrTask = $process.StandardError.ReadToEndAsync()

        if (-not $process.WaitForExit($TimeoutMinutes * 60 * 1000)) {
            $process.Kill()
            throw "Runner timed out after $TimeoutMinutes minutes."
        }

        $stdoutTask.Result | Set-Content -LiteralPath $stdoutPath -Encoding UTF8
        $stderrTask.Result | Set-Content -LiteralPath $stderrPath -Encoding UTF8

        @{
            run_id = $runId
            runner = $resolvedRunner.Name
            runner_path = $resolvedRunner.Path
            exit_code = $process.ExitCode
            started_at = $startedAt
            finished_at = Get-Date -Format o
        } | ConvertTo-Json | Set-Content -LiteralPath $exitPath -Encoding UTF8

        Add-Content -LiteralPath (Join-Path $logsRoot "scheduler.log") -Value "$(Get-Date -Format o) completed run $runId with exit code $($process.ExitCode) via $($resolvedRunner.Name)"
        exit $process.ExitCode
    } finally {
        Pop-Location
    }
} catch {
    $_ | Out-String | Set-Content -LiteralPath $stderrPath -Encoding UTF8
    @{
        run_id = $runId
        runner = $Runner
        exit_code = 1
        started_at = $startedAt
        finished_at = Get-Date -Format o
        error = $_.Exception.Message
    } | ConvertTo-Json | Set-Content -LiteralPath $exitPath -Encoding UTF8
    Add-Content -LiteralPath (Join-Path $logsRoot "scheduler.log") -Value "$(Get-Date -Format o) failed run ${runId}: $($_.Exception.Message)"
    exit 1
} finally {
    if (Test-Path -LiteralPath $lockPath) {
        Remove-Item -LiteralPath $lockPath -Force
    }
}
