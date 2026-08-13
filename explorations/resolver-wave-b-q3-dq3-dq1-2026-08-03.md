---
artifact_type: exploration
label: "Resolver Wave B: Q3 + DQ3 + DQ1"
created: 2026-08-03
status: exploration
posture: adversarial; Layer-0-first; exact algebra; pre-deposit
title: "Hinge-symbol leakage, signature-free RS neutrality, and compact isotypic overlap"
grade: "EXACT ALGEBRAIC DERIVATIONS plus standard compact-spin representation typing; finite kinematic carrier only"
canon_verdict_change: none
route_disposition: REBASE
hostile_review_status: "PASS_AFTER_REPAIRS; three disjoint lenses; 720 direct assertions green"
depends_on:
  - lab/specifications/six-axis/six-axis-template.md
  - lab/process/anchor-council-2026-08-03/seat1-quantum-foundations.md
  - lab/process/anchor-council-2026-08-03/seat3-particle-flavor.md
  - lab/process/anchor-council-2026-08-03/adjudication.md
  - explorations/chirality-grading-and-77-rerun-2026-08-03.md
  - explorations/observable-algebra-commutant-trichotomy-2026-08-03.md
scripts:
  - tests/generation-sector/q3_imposter_symbol_invariance.py
  - tests/observable-algebra/dq3_signature_free_neutrality.py
  - tests/observable-algebra/dq1_compact_isotypic_data.py
  - tests/observable-algebra/dq1_compact_isotypic_sage.py
---

# Resolver Wave B

## Outcome first

Wave B earns three finite, exact results and forces a **REBASE** of two attractive
summaries:

1. The 128-dimensional hinge block is not invariant under the raw projected
   Rarita--Schwinger principal symbol. Every nonzero coordinate direction has
   injective outgoing leakage: rank 128 ungraded and rank 64 on either chiral
   half. The hinge coupling is therefore already first-order. Extrinsic
   curvature cannot be its *sole leading* mediator.
2. The RS Krein form on `ker Gamma` is exactly neutral, with inertia
   `(832,832)`, by a signature-label-free theorem. This requires the
   Krein/metric adjoint `Gamma-sharp`, not the Euclidean SVD dagger.
3. Under the constraint-preserving compact group
   `(Spin(9) x Spin(5))/{(-1,-1)}`, the same `ker Gamma` carrier contains three
   irreducible quaternionic types on both Krein signs. Their overlap sum is
   `3 * dim_R(H) = 12`. Compact uniqueness proved on the 14-frame or fundamental
   spinor carrier does not transfer to this vector-spinor carrier.

None of these results constructs the physical quotient, chooses the actual
dynamical stabilizer, adjudicates imposter Reading A versus B, or uses the
external datum. P1/P2/P3 remain unchanged and unused.

## 0. Layer-0 object table

| name | exact object in this wave | ruling |
|---|---|---|
| `P_hinge` | any order-zero projector with range `H=im X`, `X=10 iota_B-4 iota_F`, inside raw `ker Gamma` | internal kinematic projector; the proof itself is projector-independent quotient leakage |
| external `P3` | integer-valued count/index/relative-KO datum in the external-datum ledger | distinct object; absent from every probe here |
| `sigma_RS` | raw projected principal symbol `q_R(xi)=Pi_R(I tensor c(xi))Pi_R` on the kinematic gamma-trace kernel | not the unbuilt physical symbol/domain |
| “commutator” | with `sigma_R^±:R^± -> R^∓`, the typed defect is `Delta_h^±=sigma_R^±P_h^±-P_h^∓sigma_R^±` | an ordinary commutator only after assembling the ungraded odd operator |
| “neutral” | equality of positive and negative inertia of the restricted Krein form | not physical V-A chirality, anomaly cancellation, or positive energy |
| “compact stabilizer” | compact image of `(Spin(9)xSpin(5))/{(-1,-1)}` in the constraint-preserving diagonal action | not the unbuilt dynamical good-stable group |
| “residual dimension 12” | dimension from `sum dim_R(D_lambda)a_lambda b_lambda` on finite kinematic `ker Gamma` | not 12 parameters in the source action and not a datum count |

This table absorbs the operative part of register row M-M28: “128,”
“chirality,” the graded/ungraded factor, and external P3 are not permitted to
cross types by numerical coincidence. The “13” and link-model fences remain as
recorded in M-M28 because this wave does not touch that topology.

## 1. Specialist pre-assessment and registered outcomes

Three disjoint read-only lenses were used before integration: an RS-symbol
geometer, a Krein/operator theorist, and a compact representation theorist.
They agreed that no 1,664-square brute-force commutant solve was needed.

The official runs were preceded by these terminal rules. A preliminary Q3
smoke test was disclosed to the integrator, so Q3 was not blinded; the exact
derivation and planted failures, rather than surprise, carry its evidence.

### Q3

- `Delta_h=0` for every covector would clear top-order invariance only; the
  next burden would be the zeroth-order `nabla P_hinge`/II identification and
  compressed ellipticity.
- any nonzero `Delta_h` makes the defect first-order and kills the
  independent-block / sole-leading-II reading in that scope;
- tangential zero with vertical nonzero would preserve a four-dimensional
  observation-only version while killing ambient `Y14` invariance.

### DQ3

- anticommutation plus constraint invariance gives off-diagonal Gram form and
  equal positive/negative indices;
- `(832,832)` additionally requires nondegeneracy of the restriction;
- substituting a Euclidean adjoint for `Gamma-sharp` is a terminal type error.

### DQ1

- shared types on both signs give a positive residual dimension;
- disjoint types reproduce compact uniqueness;
- any unexpected fourth type, singular cross-pairing, or non-equivariant
  gamma trace stops the inference.

## 2. Q3 exact derivation

Let the split sizes be `m=4`, `n=10`, `d=m+n=14`, and define the metric-dual
partial embeddings by

```text
(iota_B psi)_a = eta_a e_a psi  for a in B,
(iota_F psi)_a = eta_a e_a psi  for a in F.
```

Then `Gamma iota_B=mI`, `Gamma iota_F=nI`, and

```text
X = n iota_B - m iota_F
```

lands in `ker Gamma`. For `c(xi)=sum xi_b e_b`, the metric/Krein projection is

```text
Pi_R = I - (1/d) iota_all Gamma.
```

Write `S^±` for source-spinor volume chirality and `R^±` for the corresponding
RS halves. Because `X` reverses chirality, `H^-=X(S^+)` and `H^+=X(S^-)`.
The typed symbol maps are `sigma_R^±:R^± -> R^∓`. Rather than choosing a
particular projector, the proof computes the quotient leakage

```text
ell_xi^± : H^± -> R^∓ / H^∓.
```

Nonzero quotient leakage is equivalent to failure of any projector with range
`H` to intertwine the principal symbol.

Clifford anticommutation gives

```text
Gamma (I tensor c(xi)) X = 2(n c(xi_B) - m c(xi_F)) =: z.
```

If `q_R(xi)X psi` lay again in `im X`, every vector slot would infer the same
source endomorphism `A`. For `xi=e_b`, compare slot `b` with any other slot
`a` in the same block. The two inferred actions obey the exact identity

```text
A_b - A_a = 2 e_b.
```

Every Clifford generator is invertible because `e_b^2=eta_b I`. Hence the
only spinor with zero leakage is `psi=0`. The leakage map is injective on the
128-dimensional source; because `e_b` bijects the two chiral halves, its
restriction has rank 64 on either half. These ranks are theorem-inferred from
the exact witness, not matrix-rank calls in the coefficient probe. This proof uses
only nondegenerate Clifford relations and block sizes greater than one, so it
holds for both `(9,5)` and `(7,7)`, all five allocations, and every coordinate
direction. Linearity then shows the principal defect is not identically zero.

The executable certificate checks the coefficient identity over exact
`Fraction` arithmetic for all 140 form/allocation/direction combinations. It
passes explicit `(9,5)` and `(7,7)` sign vectors and verifies the invertibility
and even-dimensional chirality premises rather than merely relabelling the
same loop. **584 assertions passed**, including live zero/identity
and false-invariance controls. An independent explicit Cl(9,5) hostile replay
also returned rank 128 for all 14 coordinate directions and rank 64 on both
chiral restrictions; that replay is a review receipt, not silently counted as
the exact probe.

**Earned Q3 disposition:** `FIRST_ORDER_LEAKAGE_CONFIRMED_KINEMATIC`.
This kills the statement that II is the sole leading hinge mediator and kills
an invariant direct-summand reading of the raw RS symbol. It does **not** kill
all coupled systems, all compressed operators `P_hDP_h`, or a future physical
quotient; each needs its own ellipticity/Fredholm/domain construction.

## 3. DQ3 exact theorem and native corollary

Let `B=B^dagger` represent a Hermitian form, let
`Omega=Omega^dagger`, `Omega^2=I`, and assume `{Omega,B}=0`. If
`V=ker Gamma` is `Omega`-invariant, then in `V=V_+ direct-sum V_-`,

```text
B|V = [ 0  C ; C^dagger  0 ].
```

Therefore its inertia is `(r,r,dim V-2r)`, `r=rank C`. If `B|V` is
nondegenerate, `C` is square and invertible and the inertia is exactly `(n,n)`.

For the RS carrier, take `B=eta tensor beta_p`,
`beta_p=i^(p(p-1)/2)e_0...e_(p-1)`, and `Omega=I tensor omega`. Thus
`beta_9` is the raw nine-word while `beta_7=i e_0...e_6`; both are Hermitian
involutions. The volume word anticommutes with the odd beta word,
and Clifford oddness makes `ker Gamma` invariant. Nondegeneracy is not inferred
from ambient invertibility. The load-bearing metric-adjoint identity is

```text
e_a^dagger beta_p = beta_p e_a,
<Gamma Psi,s>_beta = <Psi,Gamma-sharp s>_(eta tensor beta).
```

Together with the correctly typed adjoint formula

```text
(Gamma-sharp s)_a = eta_a e_a s,
Gamma Gamma-sharp = sum_a eta_a e_a^2 = 14 I.
```

the scalar right-inverse gives the B-orthogonal splitting
`E=ker Gamma direct-sum im Gamma-sharp`. Thus `ker Gamma` is a nondegenerate
orthogonal summand. Since its dimension is
`14*128-128=1664`, its exact inertia is `(832,832)`.

The SymPy/Clifford-word certificate passes **103 exact assertions**,
including phased-beta Hermiticity, every metric-adjoint generator identity,
both signatures, and four planted failures: non-invariant constraint,
degenerate restriction, commuting form, and Euclidean-adjoint substitution.

**Earned DQ3 disposition:** `SIGNATURE_FREE_NEUTRALITY_CONFIRMED_KINEMATIC`.
This assembles existing abstract and signature-specific pieces; it is a
constraint-restricted corollary, not an independent new theorem family.

## 4. DQ1 exact compact branching

Use the compact covering group `Spin(9)xSpin(5)`; the three tensor products
below descend through the central quotient. Let

```text
U = Delta_9 tensor Delta_5,
R_9 = ker(C^9 tensor Delta_9 -> Delta_9),
R_5 = ker(C^5 tensor Delta_5 -> Delta_5).
```

The Weyl dimension formula gives

| compact type | highest-weight construction | complex dimension |
|---|---|---:|
| `U` | `Delta_9 tensor Delta_5` | 64 |
| `X` | `R_9 tensor Delta_5` | 512 |
| `Y` | `Delta_9 tensor R_5` | 256 |

On either 14D Weyl half,

```text
ker Gamma = U + X + Y,       64+512+256=832.
```

The opposite half restricts identically, so the full complex carrier is
`2U+2X+2Y`, dimension 1664. These Weyl halves are isotropic, not themselves
the positive/negative Krein spaces.

The remaining chain is analytic standard representation theory, stated rather
than hidden in the script: `(-1,-1)` acts trivially on all three tensor
products; `Delta_9,R_9` are real type and `Delta_5,R_5` quaternionic type, so
`U,X,Y` are quaternionic. The Krein form is K-invariant. DQ3 gives a
nondegenerate K-equivariant pairing between the two isotropic Weyl copies.
Because `U,X,Y` are distinct and occur with multiplicity one on each side,
Schur's lemma makes each cross block nonzero and nondegenerate. Passing from
the two null copies to their sum/difference graphs gives one positive and one
negative real copy per type. Consequently

```text
D_lambda=H,  (a_lambda,b_lambda)=(1,1)  for U,X,Y,
sum dim_R(D_lambda) a_lambda b_lambda = 3*4=12.
```

The base exact Weyl-dimension/arithmetic certificate passes **21 assertions**
with Python `Fraction`. A separate Sage 10.9 Weyl-character certificate passes
**12 assertions** and verifies the actual character identities
`B4: 9x16=16+128` and `B2: 5x4=4+16`. Sage is kept separate so the ordinary
Python harness has no optional dependency. The reality types are the standard
compact Clifford-classification input, made explicit rather than numerically guessed.
Controls reject a missing chirality copy, a complex-for-quaternionic
misclassification, a dimension-only type merge, and transfer from the
frame-only `9+5` carrier.

**Earned DQ1 split disposition:** the dimensions/branching arithmetic are
executable-exact; `SHARED_COMPACT_TYPES_RESIDUAL_DIMENSION_12` is exact
conditional on the explicitly named standard compact-Clifford classification
and K-invariant-pairing inputs above. This directly corrects any summary claiming
compact uniqueness on this carrier. It does not contradict uniqueness on a
different carrier, and it does not establish that this compact group is the
physical stabilizer.

## 5. What changes in the construction

The efficient next route is narrower:

1. Keep the hinge as a coupled first-order channel or test `P_hDP_h` as a new
   compressed operator. Do not spend a wave trying to derive the *leading*
   coupling solely from `nabla P_hinge`/II.
2. Carry neutral Krein pairing as a theorem-level kinematic constraint, not a
   signature-specific numerical observation.
3. If a future action/quotient selects this `ker Gamma` carrier and compact
   stabilizer, its selector faces a 12-dimensional continuous family, not one
   free bit. An external datum could select among already-admissible points,
   but P1/P2/P3 currently have no typed arrow into this family.
4. Rebase Wave C: retain the `16 tensor 144` and `Lambda^5/126` branching
   dictionary as representation information, but remove the claim that Q3
   licenses an II-only mediator between them. Occurrence of a 126 will mean
   representation-channel availability only—not a coupling, mediator, mass,
   or A/B adjudication. The physical bilinear/Krein/reality/VEV/induced-4D-mass
   checklist remains mandatory.

## 6. Boundaries

- No physical `Pi_RS^phys`, interacting BV quotient, closed domain, or
  observation pushdown is constructed.
- No 4D chirality, anomaly, generation count, Yukawa, mass, cosmological, or
  Standard Model equation is claimed.
- The imposter A/B referent remains unadjudicated.
- External P1/P2/P3 are unchanged and unused.
- No claim, canon, bar(b), H59, count, public-posture, or third-lane status moves.
