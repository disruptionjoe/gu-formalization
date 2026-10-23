---
title: "K1988: Full diagonal pairing obstruction and necessary mixing"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1988_diagonal_pairing_structural_test.py
  - tests/channel-swings/k1988_diagonal_pairing_structural_test_probe.py
---

# K1988: Full diagonal pairing obstruction and necessary mixing

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: complete128-component diagonal-field constraint and quantitative off-diagonal necessity
carrier: fixed raw1920 section and real128 core in14 flat coordinates LAYER=toy CHIRALITY=N/A
pairing: coordinate-diagonal or general real symmetric matrix field Q ON=raw_spinor_and_vector_spinor
real_structure: fixed real coefficients, not an identified source bar
grading: declared coordinate matrix entries, not physical chirality
action_owner: repository-construction -- unchanged raw lower-return equation
target: structural constraint on genuine local fields MAP-TYPE=intertwiner
```

## Result: arbitrary diagonal functions cannot solve this equation

Keep the unchanged raw equation and coefficients of
[K1985](k1985-symmetric-second-jet-compatibility-2026-10-23.md):

    L(Q) := sum_k eta_k (partial_k Q) J_k = R_s(Q),
    R_s(Q) = sum_k eta_k Omega_k^T Q J_k - s Q T,
    eta_k = +1 (k<7), -1 otherwise; s in {-1,+1}.

For every C1 field Q on any open subset of R14, if Q is diagonal in the
DECLARED raw128 coordinate basis and satisfies this equation, then Q=0.
Its128 diagonal functions may depend on all14 coordinates independently.
This is larger than K1973's two chiral scalar weights and distinct from
K1979's small three-dimensional symmetric algebra. It is not a theorem about
diagonalizability in a moving basis: differentiating that basis adds connection
terms. General symmetric local existence remains open.

## Exact support separation settles all derivative orders at once

Let S be the union of the entry supports of J_0,...,J_13. For a diagonal
matrix D, multiplying D J_k changes row weights without changing support.
Consequently the projection Pi onto entries outside S annihilates L(D),
for EVERY choice of its first derivatives. The equation forces

    Pi R_s(D) = A_s d = 0,    d_i=D_ii.                 (1)

The actual unsupported entries number128. Their exact incidence graph splits
into32 disjoint4-by4 blocks. Each block is invertible for both signs. The JSON
contains every actual entry location, coefficient block and rational inverse.
Multiplying each stored inverse by its block gives I4 exactly; the blocks
cover all128 variables. This proves rank128 and hence d=0 pointwise.
No differentiation, Taylor-order extrapolation, numerical rank tolerance,
Clifford-square assumption or restriction of the14-coordinate dependence is
used. It eliminates the entire coordinate-diagonal field search in this core.

## Released quantitative consumer: a solution must mix coordinates

Write a general field Q=D+W, where D is its coordinate diagonal and W its
zero-diagonal remainder. Use the matrix maximum absolute row-sum norm and
sup norm for vectors. Put

    C_A = ||A_s^{-1}||_infinity = 5026645120/120016881,
    b_k = ||J_k||_infinity,
    B_R = sum_k ||Omega_k^T||_infinity ||J_k||_infinity
          + ||T||_infinity.

Both signs have the same C_A; all b_k and B_R are exact in the JSON.
Since Pi merely selects entries, its entry-sup norm is bounded by the matrix
row-sum norm. Rearranging the FULL equation gives the pointwise necessity

    ||d||_infinity <= C_A [sum_k b_k ||partial_k W||_infinity
                                      + B_R ||W||_infinity].       (2)

Thus a positive field Q>=mI needs the bracket in(2) to be at least m/C_A.
A small off-diagonal value alone does not imply failure: its derivatives can
supply the required mixing. This is an explicit diagnostic for approximations,
not a positivity exclusion for the full matrix field.

At an identity-valued point W=0 and Pi R_s(I) is explicitly nonzero. The
sharper directly evaluated constraint implies

    max_k ||partial_k W||_infinity >= 42759/220096  (s=-1),
    max_k ||partial_k W||_infinity >= 94887/880384  (s=+1).  (3)

These constants come from ||Pi R_s(I)||_max / sum_k b_k. The previously
constructed positive first jets pass the full equation and serve as a contrary
control: their off-diagonal derivatives avoid the diagonal obstruction.
Neither(2) nor(3) turns those finite jets into a local solution.

## Verification, source scope and next test

The separate probe reconstructs R_s(E_ii) directly from raw coefficients,
checks1282 raw/inverse/first-jet obligations and rejects four genuine
coefficient, inverse, support and bound faults after a green baseline.
The pointwise argument supplies universal C1 scope; the checks certify its
finite coefficient identities. Both implementations are internal, by one
author; no external expert or proof assistant is claimed.

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 and SC-META-53 remain
UNCERTAIN. None selects this basis, pairing or raw core. Source, physics-ledger
and canon verdicts do not change. The next meaningful pairing construction
must allow off-diagonal values or derivatives with the necessary size above,
and address full local integrability or an actual obstruction. A basis change
must transform every coefficient and derivative term, not merely diagonalize Q.
