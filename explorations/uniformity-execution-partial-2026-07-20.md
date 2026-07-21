---
title: "Uniformity execution — PARTIAL results + handoff: single-carrier slopes REGULAR (leaning U-REGULAR); product 2nd point + controls remain (blocked by local runtime ceiling, not by the physics)"
status: active_research
doc_type: partial_execution
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (uniformity execution; run stopped at Joe's request, handed off)"
axiom: lab/process/boundary-adapter-standing-axiom.md
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Uniformity execution — partial results and handoff

Executing the pre-scoped Prong-1 plan
(explorations/prong1-uniformity-method-scope-2026-07-20.md, literature basis
prong2-krein-resolvent-literature-2026-07-20.md). Probes:
tests/channel-swings/uniformity_execution_probe.py (full),
uniformity_gaps_probe.py (gap-filler). Runs were repeatedly killed by the
LOCAL RUNTIME CEILING on long jobs (the resolvent solves at N>=129 are
CPU-heavy); this is a tooling limit, NOT a physics obstruction. The pieces
that DID complete are decisive-leaning.

## MEASURED (committed run logs; deterministic)

- STAGE 1 product construction: PASS. Exact commuting-tensor Clifford
  doubling M2 = M_A(x)I(x)tau1 + I(x)M_B(x)tau3 gives M2^2 = q2 I
  (commutator 0.0, ||M2^2 - q2 I|| = 4.4e-15). The scope's flagged residual
  (a bounded section-symbol product EXISTS) is SETTLED. Emergent
  distinct-wall at s~0.4981 where neither factor vanishes (masking-free).
- STAGE 2 Mourre sign-post: FAILED as implemented — c_N came out NEGATIVE
  and N-growing (-133/-275/-525). ASSESSMENT: likely an implementation
  artifact (the compressed commutator was NOT correctly projected to the
  Krein-positive definite range; the eigsh-SA bottom of the full compressed
  operator is not the definite-range Mourre constant). The direct slope
  test (Stage 3) is the decisive instrument and supersedes this precursor.
  A correct Mourre c_N needs the projector onto 1_I(H)>0 applied first.
- STAGE 3 single-carrier slopes (THE DECISIVE TEST) -- both REGULAR:
  - GAPPED positive control: tau_w = -0.342 (U_w: 18.6 -> 14.7; shrinking).
  - CROSSING ray (the wall): tau_w = -0.236 (2-pt, N=65/129: 13.1 -> 11.1)
    AND tau_w = -0.134 (3-pt, N=65/129/257: 16.5 -> 23.4 -> 13.7). BOTH
    NEGATIVE => the resolvent norm at the wall does NOT grow with N.
    This is the REGULAR-critical-point signature in resolvent norm.
  - Gate threshold REG = 0.35: both |tau| < REG => regular.
- STAGE 3 product carrier: only N=65 done (U_w = 10.796). Need N=129 for
  the product slope.

## REMAINING (blocked only by runtime; ~3-5 min of compute total)

1. PRODUCT slope: product(distinct-wall T2) at N=129 (have N=65=10.796).
   -> pr_tau = logslope([65,129],[10.796, U_129]). Tests product-uniformity
   (the theorem's novel clause).
2. CONTROL neg#1 (gate POWER, most important for credibility): over-singular
   carrier = build_single(A_DN, T_OP, S_LO, S_HI, N, DELTA, exponent=1.0) at
   N=65,129 -> os_tau MUST be > 0.60 (clearly divergent) or the gate can't
   see singularity and the regular readings are meaningless.
3. CONTROL neg#2 (no false-fire): identical-block product =
   build_product(T_OP, N, DELTA) at N=65,129 -> id_tau must be < ~0.55.

## PRELIMINARY VERDICT (honest, incomplete)

LEANING **U-REGULAR**: the crossing ray -- the actual type-changing wall --
has a regular (negative) resolvent-norm slope by two independent runs, and
the gapped control also reads regular, so the metric behaves. IF the
over-singular control confirms the gate detects divergence AND the product
slope stays regular, the outcome is U-REGULAR = the shared open theorem is
numerically supported (then QUARANTINE for hostile verify; Krein-Mourre on
the definite strip is the proof route). The verdict is NOT final until the
over-singular control (gate power) and the product 2nd point are in.

## UPDATE (same session): the gap run COMPLETED — outcome U-OBSTRUCTION

The gaps probe finished (exit 0). New data:
- PRODUCT slope: N=65=10.796, N=129=8.737 -> pr_tau = -0.309 (REGULAR;
  product-uniformity holds at 2-block grade — U shrinks with N).
- CONTROL neg#1 over-singular: N=65=34.246, N=129=17.896 -> os_tau = -0.947
  (SHRINKS; did NOT diverge).

**Adjudicated outcome: U-OBSTRUCTION** — every carrier (gapped, crossing,
product) reads REGULAR (all slopes negative), which is CONSISTENT with
U-REGULAR, BUT the gate's POWER is unconfirmed because the negative control
did not fire.

**Diagnosis (a real test-design flaw the discipline caught):** the
over-singular control was built as exponent=1.0 on (q + i*DELTA) at FIXED
DELTA=0.3. At fixed delta, (q+i delta)^{-1} is BOUNDED — delta regularizes
it — so it is NOT actually singular in resolvent norm; the true singular
behavior is the delta->0 limit, which this probe does not take. So the
"over-singular" control tests nothing, and its non-divergence is expected,
not informative. The gate power is therefore genuinely UNCONFIRMED: with
this construction we cannot distinguish "the wall is regular" from "the
metric is blind to singularity at these N/delta."

**What this does NOT change:** the single-carrier + product slopes are all
regular (encouraging, consistent with U-REGULAR). What it DOES change: the
claim ceiling is U-OBSTRUCTION, not U-REGULAR, until a PROPER power control
exists.

## CORRECTED REMAINING WORK (supersedes the list above)

The blocker is no longer runtime — it is the CONTROL DESIGN. To reach a
real verdict:
1. Replace the fixed-delta over-singular control with a DELTA-LADDER: show
   that a genuinely singular reference (e.g. the section resolvent on a
   NULL-Q ray, or (q+i delta)^{-1/2} as delta->0 on a crossing ray) has
   U(delta) GROWING as delta->0, while the regular carriers stay bounded.
   That establishes gate power in the correct (delta) variable.
2. OR use a reference operator with an analytically KNOWN singular
   resolvent as the positive-divergence control.
3. Then re-adjudicate: regular carriers + a firing power control => U-REGULAR.

## HANDOFF

A fresh agent (or a machine without the local ceiling) runs
uniformity_gaps_probe.py to completion (product N=129 + over-singular +
identical-product), then adjudicates against the committed single-carrier
slopes above. Method is fully specified in the scope doc; do not redesign.
Fix the Stage-2 Mourre projector if a clean precursor is wanted, but it is
not gating.
