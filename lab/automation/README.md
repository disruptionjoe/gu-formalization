# lab/automation/

Machinery and provenance for the repository's automated research cadence (the hourly run loop), plus a Lean
check helper. This is **operational record, not load-bearing research** -- an outsider can safely skip it.

- `check-lean.ps1` - required Windows-host GU Lean/Lake wrapper. It acquires an exclusive host-local
  private orchestration overlay temp lock and runs `lake build`, preventing compliant direct-chat and scheduled builds on
  that host from overlapping. Lake 5 no longer accepts the historical `lake build -j1` form. The wrapper
  does not serialize another computer or cloud runner and cannot technically prevent a direct command from
  bypassing policy.
- `check-lean.sh` - required macOS/POSIX-host counterpart. It uses `shlock` on the same host-local
  private orchestration overlay temp-lock identity, supports the optional update/cache preparation steps, and runs the default
  target without the Lake-5-incompatible `-j1` argument.
- `evidence/` — captured outputs / receipts from runs.
- `logs/` — run logs.
- `tmp/` — scratch.

The research outputs the cadence produced live under `explorations/research-cycles/` (notes) and
`tests/research-cycles/` (scripts), both archived; the durable, reviewed results live in `canon/` and the
papers under `papers/published/`.
