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

## Internal ops gitignore gate

`internal_ops_gitignore_audit.py` checks that `steward/runs/` remains ignored and contains no
tracked files. This protects local CapacityOS run records from being published with the public
research repo while leaving those records available for collision checks.

## Public path hygiene gate

`public_path_hygiene_audit.py` checks the root public entry file, neutral contributor/config
files, `process_gates/` sources, and `lab/active-research/` owner surfaces for absolute
home-path leaks before those surfaces are committed in this public repo. Including
active research keeps frontstage public packets from carrying local machine paths; the gate
still treats the content as prose/governance hygiene, not as mathematical validation.
It intentionally does not scan canon, derivation, proof, result-grade, paper, Lean proof,
exploration, or research-status surfaces, so it can run while those areas are dirty or under
governance review.

## Lean certificate surface gate

`lean_certificate_surface_audit.py` checks the Lean scaffold, current certificate files,
standalone Lean certificate pointers, owner-surface references, CI workflow, and local
Lean check script. It strips Lean comments before scanning for proof placeholders, so
honest explanatory headers can mention `sorry` or `axiom` while proof bodies remain
placeholder-free. This is a process gate; `lake build` and targeted `lake env lean ...`
commands remain the compile checks.

## Tests manifest count gate

`tests_manifest_count_audit.py` checks the live organized-subdirectory counts in
`tests/README.md` against the current direct non-README files in each listed test
directory. Rows marked `archived off-tree` are allowed only when the named directory is
not present. This protects the public reproduction map from drifting as validators are
added or archived without treating manifest counts as mathematical evidence.

## Reproduction harness scope gate

`reproduce_harness_scope_audit.py` imports `scripts/reproduce_all.py` without running
the certificate suite, then checks that quick mode discovers exactly the live `tests/`
Python certificates, full mode adds only the declared paper certificate roots, skip
directories remain excluded, `process_gates/` remains outside the computational
certificate sweep, and list mode prints repository-relative slash paths.

## Relocated surface path hygiene

Repository process, automation, and active-research owner surfaces now live under `lab/`.
Process gates should point at current `lab/process/`, `lab/automation/`, and
`lab/active-research/` paths when checking live owner surfaces. Historical exploration
artifacts may still quote older path strings as provenance. Do not rewrite those mechanically
unless the selected gate depends on them as current executable inputs.

Remaining content failures are governance debt to fix or retire separately; they are not
introduced by the path repair.
