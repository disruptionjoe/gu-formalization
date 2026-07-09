<!--
Pull request template for the GU / Observerse research program.
Operationalizes the "How to submit a pull request" norms in CONTRIBUTING.md.
Delete any section that does not apply; this is a checklist, not a gate.
-->

## Summary

<!-- A clear thesis-statement summary (the first ~200 words is what most readers see). -->

## What this contribution does

<!-- Which specific mathematical piece it constructs, tests, or kills. Name the GU
     reconstruction claim or hypothesis it advances, blocks, or refutes. -->

## Contribution type

<!-- e.g. GU reconstruction work / substrate-level invariant work / persona-pass
     correction / accessibility edit / specification proposal / reference pointer.
     See CONTRIBUTING.md "What kinds of contribution are welcome". -->

## Claim-status / grading discipline

If this change involves a math claim, confirm the three-tier tagging discipline
(`RESEARCH-POSTURE.md`, `CONTRIBUTING.md`):

- [ ] Claims are tagged `[verified]` / `[reconstruction]` / `[speculation]` with sources named.
- [ ] Explicit assumptions, and falsification / rollback conditions, are stated.
- [ ] If this promotes, downgrades, or re-scopes a claim, I ran
      `lab/process/runbooks/claim-status-consistency-quality-workflow.md`.
- [ ] No verdict inflation, compatibility-as-derivation, or imported target data hidden
      as a reconstruction (the forbidden moves in `RESEARCH-POSTURE.md`).

## Validation / reproduction

If this change touches certificates, process gates, reproduction docs, or claim-supporting
prose, report the relevant checks:

- [ ] Ran targeted certificate checks or `python scripts/reproduce_all.py --quick --tracked-only`.
- [ ] Ran relevant process gates, such as
      `python process_gates/reproduction_docs_consistency_audit.py` for reproduction-doc changes or
      `python process_gates/process_gate_readme_inventory_audit.py` for process-gate inventory changes.
- [ ] Reported any skipped heavy, full-suite, or Lean checks and why.

## Checklist

- [ ] Branch named descriptively (e.g. `pr/freed-hopkins-pairing-counterexample`).
- [ ] Followed the relevant structural template (persona pass / deep-research brief /
      hextuple substrate specification) where applicable.
- [ ] Citations use inline `[Author Year]` with full references at the end (arXiv links preferred).

## Attribution preference

<!-- Default is attributed. If you'd prefer pseudonymous or anonymous contribution,
     say so here. -->
