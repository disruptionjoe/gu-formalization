# process_gates

Governance / consistency / prose-discipline audits, relocated here from `tests/` in the
2026-06-30 de-theater pass so that `tests/` is reserved for files that build a mathematical
object and compute a number/rank/dim/index.

These files assert **documentation and status discipline** (posture wording, claim-DAG
consistency, allowed/forbidden provenance inputs, "no overclaim" checks, Lean-surface presence,
etc.) - they do **not** perform mathematics. A green run here means the prose/governance
contracts hold; it says nothing about whether a GU claim is mathematically checked. For that,
see `tests/` (real computations) and `tests/chase/` (verified verdict scripts).

## Why top-level (same depth as `tests/`)

Each gate computes the repo root as `Path(__file__).resolve().parents[1]`, which assumes the
file sits one level under the repo root. `process_gates/` is at the same depth as `tests/`, so
that path logic is preserved unchanged and no gate needed editing to move here.

## Current routing link gate

`roadmap_current_routing_links_audit.py` checks that local Markdown links in
`lab/roadmap/README.md` are repository-relative and resolve from that file's actual location.
Failures report the roadmap line number and target path. This protects the current routing
table without treating roadmap prose as a research claim.

## Relocated surface path hygiene

Repository process, automation, and active-research owner surfaces now live under `lab/`.
Process gates should point at current `lab/process/`, `lab/automation/`, and
`lab/active-research/` paths when checking live owner surfaces. Historical exploration
artifacts may still quote older path strings as provenance. Do not rewrite those mechanically
unless the selected gate depends on them as current executable inputs.

Remaining content failures are governance debt to fix or retire separately; they are not
introduced by the path repair.
