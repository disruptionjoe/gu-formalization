---
title: "Structurally Forced, Internally Undecidable (DRAFT)"
status: draft
doc_type: draft_marker
created: 2026-07-14
promotion: "Joe-gated. This is NOT a candidate. Do not promote to papers/candidates/ or submit anywhere without explicit approval."
---

# Structurally Forced, Internally Undecidable -- DRAFT

**This is a FIRST-PASS DRAFT, not a finished paper and NOT a candidate.**

Working title (Joe-approved): *Structurally Forced, Internally Undecidable: the C-operator grading sign in
self-consistent indefinite-metric (Krein) gauge theories.*

The paper LEADS with the general, GU-independent mechanism (a Schur / invariant-theory statement about an
indefinite metric and its C-commutant). Geometric Unity is the worked example, not the subject.

## What is in this folder

- [`draft-skeleton.md`](draft-skeleton.md) -- the draft: abstract (general first), the general theorem
  (proven, with one checkable side-hypothesis), the five-method independence backbone (W206-W211), the
  forced-coefficient source-action context (W203), honest positioning vs the prior art, an "Honest limits"
  section, and a light nod to the "Located, Not Forced" line.
- [`tests/general_krein_grading_sign.py`](tests/general_krein_grading_sign.py) -- machine check of the
  general theorem over a sweep of signatures `(p,q)` (81/81, exit 0). DRAFT-tier: it lives in this folder,
  runs standalone, and is deliberately NOT wired into the repo greens gate.

## Status and governance

- **Grade:** exploration / DRAFT-tier. All verification is internal (reproduced and adversarially reviewed
  within one AI-directed process; not yet independently replicated or peer-reviewed).
- **General theorem:** came out **PROVEN** at the general level, with one explicit and checkable
  side-hypothesis (non-coincidence of the two C-eigenspaces as representations of the good-stable
  stabilizer), which holds automatically in the canonical maximal-compact case `O(p) x O(q)`. It is NOT left
  as a bare conjecture; the hardening register below lists the referee-grade tightening still owed.
- **No canon movement.** bar (b) and H59 stay OPEN. The generation count stays `{1,3}`. No forbidden target
  is assumed or inserted. No scientific verdict is flipped into canon.
- **No external action.** No publication, no submission, no deployment. Promotion to candidate is Joe-gated.
- **Machine checks:**
  - `python -u papers/drafts/structurally-forced-internally-undecidable/tests/general_krein_grading_sign.py`
    (81/81, exit 0)
  - `python -u tests/W211_five_method_convergence.py` (exit 0; the five-method convergence certificate)

## Source material (all on origin/main, cited as used)

- W203 -- source action built with Schur-forced relative coefficients (only overall scale free).
- W202 -- signature crux: the `(6,4)` Krein sign is decoupled from the `(9,5)`/`(7,7)` signature choice.
- W206 (R16 counterfactual-invariance), W207 (R9 Dirac-BRST), W208 (R7 Lawvere fixed point),
  W209 (R12 topos internal logic), W210 (R1 Helmholtz inverse-variational) -- the five decisive-bit methods.
- W211 -- five-method convergence synthesis (LOCATED-NOT-FORCED; bar (b) does not self-clear).

---

## Remaining-hardening register

What still needs doing in the GU repository before this draft could be considered candidate / arXiv grade.
GU-repo hardening remains; this list is explicit so it can be carried into the drafting-factory seed note.

1. **Prove the general Krein theorem in full generality (TOP priority).** The theorem is proven for the
   canonical maximal-compact case `G* = O(p) x O(q)` and machine-checked over a signature sweep. Still owed:
   a written proof that does not specialize to the maximal compact; the precise characterization of when the
   non-coincidence hypothesis (the two C-eigenspaces sharing no common irreducible `G*`-constituent) can
   FAIL for a proper subgroup `G < O(eta)`, and what happens to the residual dimension when it does; and a
   statement of the minimal hypotheses on `G` under which the forced-form/free-sign dichotomy holds.
2. **Full literature review.** The Section 6 positioning is a first-pass sweep. A referee-grade version needs
   exact citations (Mostafazadeh's metric-operator papers; Bender-Boettcher and Bender-Brody-Jones for
   PT/CPT and the C operator; Mannheim on PT-symmetric QFT, Pais-Uhlenbeck, and conformal gravity;
   Lee-Wick, CLOP, and Anselmi-Piva fakeon), plus a check that the specific forced-form/free-sign and
   multi-formalism-independence claims are not anticipated in literature not yet swept (Krein-space QFT,
   Gupta-Bleuler/BRST cohomology of the physical metric, indefinite-metric representation theory).
3. **Referee-grade written proofs of each of the five methods.** The five methods are each machine-checked
   on their decisive linear-algebra core, but the paper currently cites them; a candidate version needs a
   written, human-readable proof of each (invariance dim-2, BRST `H^0(Q)` non-selection, Lawvere two-fixed-
   points, topos classifier intuitionistic-on-sign, Helmholtz sign-blindness) that a referee can check
   without running code.
4. **Independent-reader pass.** No result here has been read by anyone outside the AI-directed process that
   produced it. A domain expert (Krein / PT-symmetric QFT, and separately invariant theory / representation
   theory) should confirm (a) the general theorem and its side-hypothesis, (b) the honesty of the prior-art
   positioning, and (c) that the five methods are genuinely independent rather than the same computation in
   five costumes.
5. **Tighten the structural identifications.** The claim that all five methods localize the SAME external
   owner (the interacting C-operator = the unbuilt C2-closing spectral section = the temporal-issuance /
   time-as-finality datum) is structural, not fully built. The cross-program object stays gated; the paper
   asserts no cross-repository identity. A candidate version needs the GU-side identification made precise
   and the one-way gating restated.
6. **Venue positioning.** Decide the honest venue and framing (hep-th / math-ph general Krein result with GU
   as an application, versus a GU-specific note). The general theorem is the publishable core; the GU
   instance is the motivating example. Section 8's relationship to "Located, Not Forced" should be settled
   (companion, not sequel).
7. **Source-action completion context.** W203 builds the source action's forced coefficients but the
   completion to the full nonlocal term is not built; a candidate version should state precisely how much of
   "the form is forced" rests on the built part versus the schema match.

*DRAFT marker. Promotion is Joe-gated. Zero em dashes.*
