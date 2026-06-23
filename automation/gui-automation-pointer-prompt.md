# Codex GUI Automation Pointer Prompt

Use this as the thin prompt for a Codex app GUI hourly automation.

```text
Run the GU formalization hourly frontier workflow for this repository:

C:\Users\joe\JB\Github Repos\gu-formalization

Use `automation/hourly-frontier-prompt.md` as the authoritative instruction template.
Create a fresh run id in `yyyyMMdd-HHmmss` format, replace the template placeholders,
execute one bounded frontier pass, and write the run summary to:

automation/runs/<run-id>/summary.md

If the GUI automation can call a local command instead of interpreting the prompt directly,
run:

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\Users\joe\JB\Github Repos\gu-formalization\automation\run-hourly-frontier.ps1"

Keep all outputs scoped, do not run destructive git commands, and keep all new claims at
exploration grade unless the repo's promotion rule is explicitly satisfied.
```

