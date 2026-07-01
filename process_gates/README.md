# process_gates

Governance / consistency / prose-discipline audits, relocated here from `tests/` in the
2026-06-30 de-theater pass so that `tests/` is reserved for files that build a mathematical
object and compute a number/rank/dim/index.

These files assert **documentation and status discipline** (posture wording, claim-DAG
consistency, allowed/forbidden provenance inputs, "no overclaim" checks, Lean-surface presence,
etc.) — they do **not** perform mathematics. A green run here means the prose/governance
contracts hold; it says nothing about whether a GU claim is mathematically checked. For that,
see `tests/` (real computations) and `tests/chase/` (verified verdict scripts).

## Why top-level (same depth as `tests/`)

Each gate computes the repo root as `Path(__file__).resolve().parents[1]`, which assumes the
file sits one level under the repo root. `process_gates/` is at the same depth as `tests/`, so
that path logic is preserved unchanged and no gate needed editing to move here.

## Note on pre-existing staleness

Some gates carry stale references from before the CapacityOS/repo reorganizations (e.g.
`ROOT / "process" / "runbooks"` and `ROOT / "active-research"`, which now live under `lab/`),
or assert document content that has since changed. Those failures predate this relocation and
were part of the reason to move these out of the real test suite. They are governance debt to
fix or retire, tracked separately — not introduced by the move.
