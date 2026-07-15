# lab/automation/

Machinery and provenance for the repository's automated research cadence (the hourly run loop), plus a Lean
check helper. This is **operational record, not load-bearing research** -- an outsider can safely skip it.

- `check-lean.ps1` - required GU Lean/Lake wrapper. It acquires an exclusive CapacityOS temp lock and
  runs `lake build -j1`, preventing direct-chat and scheduled GU builds from overlapping.
- `runs/` — per-run prompts and logs from automated cycles.
- `evidence/` — captured outputs / receipts from runs.
- `logs/` — run logs.
- `tmp/` — scratch.

The research outputs the cadence produced live under `explorations/hourly-cycles/` (notes) and
`tests/hourly-cycles/` (scripts), both archived; the durable, reviewed results live in `canon/` and the
papers under `papers/published/`.
