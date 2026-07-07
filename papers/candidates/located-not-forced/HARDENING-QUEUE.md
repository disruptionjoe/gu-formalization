---
title: "Located, Not Forced — hardening queue (convergent lane)"
status: active
doc_type: hardening-queue
scope: paper-local
created: 2026-07-07
source: "adversarial review 2026-07-07 (external-style, maintainer-supplied)"
run_type: convergent-progress (hourly-pickable; see lab/process/runbooks/lean-verification-run.md)
---

# Located, Not Forced — hardening queue

Convergent hardening tasks derived from the 2026-07-07 adversarial review. These are **hourly-pickable**
(bounded, well-specified, monotone success condition) and belong to the convergent-progress lane, not
discovery. **None blocks the title claim** — the paper is READY (staged, both deferral work-cards closed,
spine Lean-verified, GU-independent core). These items lower the barrier to the EXTERNAL review the paper's
biggest weakness (W1) demands, and make the delimitations auditable. Work top-down; flip status per item.

Honest scope: W1 (circular internal verification) cannot be *closed* by hourly work — only external humans
break the single-process ceiling. What the lane CAN do is make external replication one command away. That
is H1/H8/H9.

## Queue

- **H1 — one-command reproducibility harness** (attacks W1; highest value). A single script that recomputes
  EVERY load-bearing symbolic/numeric check in the paper from a clean checkout, exit 0, printing each cited
  number next to its paper reference (net chiral index ~ -2.4e-15 across (9,5)/(7,7)/(14,0); the (+96,-96)
  signature; e_R = 1/12; the 12k indices; the 2-primary identities). Type: reproducibility. Success: `python
  papers/candidates/located-not-forced/reproduce_all.py` exits 0 and every number matches the paper.
- **H2 — Lean-formalize the finite theorems** (attacks W1, W3, W6). Extend the Lean lane: T2 Krein index
  conservation + antilinear bound are already verified (LocatedNotForcedLegs.lean); ADD the class-C
  enumeration completeness (finite generator set + closure) and the 2-primary arithmetic identities as
  machine-checked (not engine-swept). Maps to Lean lane queue items; see `../../../lab/process/lean-verification-lane-LEDGER.md`.
  Success: the enumeration-completeness core typechecks, no sorry/axiom.
- **H3 — explicit class-C boundary table** (attacks W3). An exhaustive "IN class C / OUT of class C" table
  with the exact closure conditions (covariant, sector-interior, linear-or-antilinear, so(4)+so(10)-equivariant,
  built from sector data), so the delimitation is auditable, not prose. State what OUT means (external
  backgrounds, non-sector gauge twists, full function-space). Type: scholarship/consistency.
- **H4 — premise-flag consistency audit** (attacks W2). Verify EVERY place the "located" narrative appears
  (title, abstract, intro item, §7, §9, §12, status table) carries the `Hom(Z/3,Z)=0` category-error flag
  adjacent and consistently; produce a flag-location map. The premise must be unmissable everywhere, not just
  in §9. Type: consistency-audit. Success: a map showing each narrative locus + its adjacent caveat.
- **H5 — per-claim GU-dependency audit** (attacks W5). For each theorem/lemma, a one-line tag: "depends only
  on Cl(p,q) RS sector structure" (GU-independent) vs "depends on GU-specific choice X" (GU-motivated arena).
  Produces an auditable GU-independence table backing the paper's GU-independent-core claim. Type: audit.
- **H6 — prior-art delta table** (attacks W4). A table stating the exact differentiator vs each reference
  (Wang 2023 framed bordism 24/8=3; Wan-Wang-Yau 2026 Pontryagin-mod-3 + color triality; Garcia-Etxebarria-
  Montero Z_9; Dobrescu-Poppitz; Kaplan-Sun): what layer each targets (SM boundary data / full spacetime /
  sector-interior) and precisely what the inverse 2-primary-blindness reading adds. Type: scholarship.
- **H7 — antilinear residual scoping** (attacks W6). Explicitly close-or-scope the two residuals: the
  K-definite non-chirality re-gradings, and the function-space extension (WC-FUNCTION-SPACE-EXT). Either a
  bounded computation closing them or a crisp one-paragraph scope statement in the paper. Type: Lean/computation.
- **H8 — external-reviewer packet** (attacks W1). Assemble a one-command "clone -> reproduce_all -> lake build
  -> read the claim map" packet + a short REVIEWER.md so an external mathematician can replicate in one pass.
  Type: packaging. Success: the packet runs green from a fresh clone.
- **H9 — load-bearing-number manifest with independent re-derivation** (attacks W1). A manifest listing each
  load-bearing number, its script, and a SECOND independent derivation (different method) confirming it, so
  no single number rests on one code path. Type: reproducibility.
- **H10 — (optional, maintainer-gated) fold this week's corroboration.** A scoped one-line remark folding
  V7 (CP^2 kill: every selected twist m^2=1 mod 3, certified double import) into §8/§9 as fresh evidence for
  the category-error reading. The paper's §9 already makes the equivalent point; this only adds the citation.
  Do NOT edit the frozen ready paper without maintainer go.

## Progress metric

A run makes progress iff it advances one item to a checkable done-state (harness green, a Lean file
typechecked, an audit table produced). If an item is genuinely blocked, note it here and move to the next.
No item is a claim-status change; canon/paper edits that touch the frozen submission pause for the maintainer.
