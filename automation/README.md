# Hourly Frontier Automation

This folder contains the local hourly automation for repeated GU formalization frontier passes.

## Files

- `hourly-frontier-prompt.md` is the unattended agent prompt template.
- `gui-automation-pointer-prompt.md` is the thin prompt to paste into a Codex app GUI hourly automation if that UI is available.
- `run-hourly-frontier.ps1` creates a run id, writes logs under `automation/runs/`, and invokes a local non-interactive CLI runner.
- `.gitignore` keeps hourly run logs out of git.

## Scheduled Task

Windows Scheduled Task name:

```powershell
GU Formalization Hourly Frontier Dispatch
```

Inspect it:

```powershell
Get-ScheduledTask -TaskName 'GU Formalization Hourly Frontier Dispatch'
Get-ScheduledTaskInfo -TaskName 'GU Formalization Hourly Frontier Dispatch'
```

Disable it:

```powershell
Disable-ScheduledTask -TaskName 'GU Formalization Hourly Frontier Dispatch'
```

Re-enable it:

```powershell
Enable-ScheduledTask -TaskName 'GU Formalization Hourly Frontier Dispatch'
```

## Runner Selection

By default, the script tries to resolve a local CLI runner automatically. To force a runner:

```powershell
$env:GU_FRONTIER_RUNNER = 'claude'
```

or:

```powershell
$env:GU_FRONTIER_RUNNER = 'codex'
```

Current caveat from the 2026-06-23 setup pass: `codex` was present in WindowsApps but failed from PowerShell with `Access is denied`, while `claude` was installed but rate-limited. The script logs those failures cleanly until a usable non-interactive runner is available.
