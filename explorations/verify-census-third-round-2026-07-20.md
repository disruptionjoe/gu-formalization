---
title: "Targeted third dry round on the corrected crossed-fiber census sentence: verified DRY by a third route independent of both prior passes -- structure constants of the commutant algebra computed by least squares, regular representation diagonalized, four rank-32 primitive idempotents extracted (algebra proven C^4), all 2^4 = 16 involutions exhaustively enumerated with completeness forced by the idempotent-basis argument, each classified independently by K_S-parity and half-splitting dimension: skew set exactly +-d~ and +-J_c, extras neither skew nor half-splittings (+1-eigenspace dims 96/32, never 64); census repeated at a second fresh crossed point; correction banner text matches the proven repair with no drift -- the paper cluster is CLEAR for factory drafting"
status: active_research
doc_type: adversarial_verification
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (targeted third round: census)"
axiom: lab/process/boundary-adapter-standing-axiom.md
targets:
  - explorations/sector-relative-section-theory-2026-07-20.md
  - explorations/verify-section-theory-2026-07-20.md
runnable:
  - tests/channel-swings/verify_census_third_round_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Third dry round, targeted: the corrected census sentence

Scope, per the stopping rule: ONE SENTENCE. The second dry round
(`explorations/verify-section-theory-2026-07-20.md`, commit 5afb44b)
returned NOT-DRY on exactly one claim -- the crossed-fiber census
("exactly eight involutions" was false; the algebra is C^4 with
sixteen) -- and proved the repair symbolically: the K_S-skew
involutions are exactly +-d~ and +-J_c, and the extra eight are
neither K_S-skew nor half-splittings. A correction banner carrying
that repair was applied (commit 73b66dd). This pass verifies the
CORRECTED statement independently and checks banner-vs-theorem
fidelity. Nothing else in the cluster is re-litigated.

**Verdict up front: DRY. The corrected sentence stands, verified by a
third route at two crossed points; the banner states exactly the
proven repair, nothing stronger; the paper cluster is CLEAR for
factory drafting.**

## 1. Independence of the route

Three routes, no overlap in method:

- **Original probe** (`sector_relative_section_probe.py`): checked
  rank-4 independence and the d~ properties; the involution count was
  ASSERTED, never enumerated -- that is how the error survived.
- **Second dry round** (`verify_section_theory_probe.py`): exhibited a
  ninth involution numerically and proved the repair in sympy by
  solving the coefficient equations (K_S-skewness kills the I and Ku
  coefficients; x^2 = I then forces bd = 0, b^2 + d^2 = 1).
- **This pass** (`verify_census_third_round_probe.py`, numpy only, no
  sympy, no RNG): (1) computes the STRUCTURE CONSTANTS of
  span{I, d~, Ku, J_c} by least squares back into the span (closure
  residual 2.3e-15; commutativity machine-exact); (2) builds the
  regular representation from those constants alone, diagonalizes a
  generic left-multiplication operator, and normalizes the four joint
  eigenvectors to PRIMITIVE IDEMPOTENTS -- mutually orthogonal,
  summing to I, each of trace exactly 32 (defect 1.3e-15): the algebra
  is C^4, machine-proven; (3) ENUMERATES ALL involutions exhaustively:
  the four idempotents are a basis (change-of-basis condition number
  1.0), so x = sum c_a e_a, x^2 = sum c_a^2 e_a, and x^2 = I forces
  c_a = +-1 -- the involution set is EXACTLY the 2^4 = 16 sign
  combinations, complete by linear algebra, not by search; (4)
  classifies each of the 16 INDEPENDENTLY by K_S-parity defect norms
  and +1-eigenspace dimension (exact, from the trace of a manifestly
  diagonalizable element).

The structural argument requested in the mission -- the C^4 block
structure forces exactly 2^4 involutions; the K_S-skew condition
selects which -- is step (3) with its premises machine-checked, not
assumed.

## 2. What the enumeration found (crossed point q = -47.747)

- Sixteen involutions, all squaring to I at 3.2e-15, pairwise
  separation >= 1.370. Exactly 8 are the named +-{I, d~, Ku, J_c};
  exactly 8 are mixed-sign extras.
- **K_S-SKEW set = {+d~, -d~, +J_c, -J_c} exactly** -- four, no
  others. K_S-self-adjoint set = {+-I, +-Ku} exactly.
- The eight extras are NEITHER: minimum parity defect 1.69 (O(1), not
  borderline), and their +1-eigenspaces have dimensions
  {96, 96, 96, 96, 32, 32, 32, 32} -- never 64, so none is a
  half-splitting. The half-splittings among all sixteen are exactly
  +-d~, +-Ku, +-J_c (dimension 64 each).
- The second round's ninth involution (I + d~ + Ku - J_c)/2 appears in
  MY enumeration at 1.3e-15 as one of the unnamed extras (sign pattern
  weight-1 on the blocks, +1-eigenspace dimension 96 -- matching the
  second round's reported figure).
- The whole census REPEATS at a second crossed point on the same ray
  (s* + 0.8, q = -257.947), a point used by neither earlier probe:
  same blocks, same sixteen, same skew set, same extra dims.
- Refutation control: the ORIGINAL sentence ("exactly eight") fails
  against this route too -- three independent routes now agree it was
  false and agree on the repair.
- Sensitivity control: the classifiers have teeth -- Ku fails the
  skew test at defect 1.38, d~ fails the self-adjoint test at 3.24,
  and any repair that listed +-Ku as skew or any extra as a
  half-splitting would FAIL the probe.

## 3. Banner-vs-theorem fidelity (no drift)

The banner (commit 73b66dd, checked mechanically by the probe and by
reading) asserts, above the body, exactly four things: (a) the
algebra is C^4 with SIXTEEN involutions (a ninth exhibited); (b) the
K_S-SKEW involutions are exactly +-d~ and +-J_c; (c) the remaining
eight are neither K_S-skew nor half-splittings; (d) the Z/2
classification, existence, wall-matching, and downstream consequences
are UNAFFECTED. All four are what this pass proved -- (a)-(c)
directly; (d) because the classification consumes only the skew set
(the crossed-side adjoint type) minus the d~ exclusion, both intact.
The banner claims nothing beyond the second round's proven repair (it
even drops the round's stronger "nor K_S-self-adjoint" clause and the
dimension figures -- an under-claim, the safe direction), and the
original false sentence is retained unedited below the banner per
record discipline. No drift between banner and theorem.

## 4. Verdict

**DRY.** The corrected census sentence is true as banner-stated,
verified by a third independent route (structure constants -> regular
representation -> primitive idempotents -> exhaustive 2^4 enumeration
-> member-by-member classification), at two crossed points, with
refutation and sensitivity controls passing and banner-theorem
fidelity confirmed. Under the stopping rule the targeted re-check of
the one material item from the second round finds no material
revision required: **the section-theory paper cluster is CLEAR for
factory drafting.**

## 5. Receipts

- Probe: `tests/channel-swings/verify_census_third_round_probe.py` --
  deterministic (no RNG; two runs byte-identical), numpy only, exit 0
  -- HEADLINE `6 [E] + 2 [F] = 8 (setup [T] = 2 excluded) ALL PASS`.
- Independent anchors reproduced from scratch: conf-down wall
  s* = 0.0585, t* = 0.575 (matches both earlier probes); q at the
  census point -47.747; second crossed point q = -257.947.
- Hard constraints honored: no commits, no pushes, no lake/Lean, no
  edits to any existing file; deliverables are these two new files
  only.

## 6. Boundary

Adversarial-verification tier under the standing axiom; matrix/symbol
grade, same as the targets. Scope was one sentence: nothing here
re-verifies the other 20 claims of the second round's table, and
nothing touches the operator-grade N2 gap, the +-i0 scheme bit, the
P = 0 stratum, or any K-group. No claim-status, canon-verdict,
scorecard, or public-posture movement. No cross-owner writes; no
external actions.
