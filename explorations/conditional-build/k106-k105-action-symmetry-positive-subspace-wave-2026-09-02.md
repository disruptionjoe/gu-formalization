---
title: "K106 K105 action symmetry and positive-subspace obstruction"
status: active_research
doc_type: exact_blind_sector_orthogonal_symmetry_and_cross_term_positive_subspace_nonselection_result
created: 2026-09-02
date: 2026-09-02
claim_ceiling: exact O(256) times O(183) blind-sector symmetry of the frozen K105 action, domain, Green pair and boundary form, plus an exact rank-at-most-ten cross-term-only lower bound of 250 on the positive blind dimension and typed tests for additional action, boundary, state and observable symmetry breakers; no source ownership, no theorem against full distortion or boundary operators, no physical polarization, state, Born law, curved locality, prediction, confirmation or GU verdict
manifest: lab/process/k106-k105-action-symmetry-positive-subspace-wave.json
probe: tests/channel-swings/k106_k105_action_symmetry_positive_subspace_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K106 K105 action symmetry and positive-subspace obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

Scope: this packet strengthens K105's exact `e_0/e_1` witness to the complete
orthogonal symmetry of the coefficient-blind positive and negative sectors. It
then proves the strongest obstruction available to a continuation that changes
only the metric-to-distortion cross coefficient. Finally it freezes exact
tests that an independently owned distortion action, boundary condition, state
or observable would have to pass to break the symmetry. It does not choose one
of those additions and does not turn a planted discriminator into physics.

```gu-typed-objects
result: the frozen K105 packet has O(256) times O(183) blind-sector symmetry, and every cross-term-only replacement from metric-10 to distortion-448 leaves a positive blind subspace of dimension at least 250
carrier: rapid l2 histories of the K105 quotient metric-6 plus K155 distortion-448 fiber, with compactly supported smooth time tests LAYER=ambient CHIRALITY=N/A
pairing: Euclidean on the quotient metric sector and the exact K155 distortion lowerer of inertia (260,188,0) ON=repository_owned_action_control
real_structure: coefficientwise real Cl(7,7) packet; no complexification, Cl(9,5) transport or positive-Hilbert replacement
grading: K105 metric fields, distortion fields, four diffeomorphism ghosts and minimal antifields; selector candidates add no grading unless separately owned
action_owner: repository-construction -- K105 owns the frozen free action while no source action, full distortion discriminator, physical boundary operator, state or observable selector is supplied
target: natural positive-retract selection from the exact action-domain-Green packet and cross-term-only continuations MAP-TYPE=evaluation
```

## Inline preflight bookend

The gate starts from K105 rather than selecting a positive line by convention.
K105 fixes a diagonal involutive distortion lowerer `K` of inertia
`(260,188,0)`, a rank-one cross coefficient `C_*:M^10 -> D^448` with exactly
nine supported output rows, a fibre-scalar modal kinetic/potential block, and
an action/domain/Green retract along `e_0`. Its probe also fixes `256` positive
and `183` negative coordinate lines on which `C_*^T K` vanishes. K103 remains
the source boundary: the absorbed `Cl(9,5)` construction tree owns neither an
authenticated action nor a boundary-Dirac/domain packet, while K155 is one
repository-selected conditional `Cl(7,7)` coefficient fixture rather than the
unrecovered historical Shiab.

The problem-matched lens census covered Krein orthogonal groups, stabilizers
of finite-rank action coefficients, Grassmann dimension bounds, naturality
under automorphisms, reducing subspaces of closed multipliers, Green-form
symmetries, self-adjoint boundary extensions, quasifree covariance, detector
interfaces and spontaneous versus action-owned symmetry breaking. The
cheapest decisive test is not another coordinate retract: it is the full
stabilizer of the 439 coefficient-blind axes.

Positive controls retain K105's exact coefficient and inertia, exercise a
nontrivial rational rotation inside the blind positive plane, saturate the
general dimension bound with a planted rank-ten cross coefficient, and supply
one explicitly planted full distortion boundary operator with a simple
positive eigenspace. Negative controls distinguish breaking the displayed
swap from selecting a unique line, reject scalar boundary data and
action-functional state covariances as breakers, and refuse coordinate,
source, state, Born or locality promotion.

## 1. The complete blind-sector symmetry

Let `I_+` be the indices whose `K` diagonal entry is `+1` and whose row of
`C_*` is zero; define `I_-` analogously for diagonal entry `-1`. Put

```text
E_+ = span{e_i : i in I_+},       E_- = span{e_i : i in I_-}.
```

The exact K105 census gives

```text
dim E_+ = 256,        dim E_- = 183.                         (1)
```

Because `K` is diagonal, its restrictions are `+I_256` and `-I_183`.
Because every corresponding coefficient row vanishes, `im C_*` lies in the
`K`-orthogonal complement of `E_+ direct-sum E_-`. Therefore every

```text
R_+ in O(E_+),       R_- in O(E_-)                           (2)
```

extends by the identity on the remaining nine coordinate axes to a map `R`
satisfying

```text
R^T K R = K,        R C_* = C_*.                            (3)
```

The modal operator `Omega` is scalar on the finite distortion fibre, so `R`
also commutes with the free distortion block. It acts trivially on the metric
and ghost sectors. Consequently it commutes with the full Euler operator,
preserves the maximal multiplier domain and rapid core, intertwines both exact
retarded/advanced kernels, and preserves the Green boundary form. Hence

```text
O(256) x O(183)  is a subgroup of Aut(action, domain, core, G_ret, G_adv, beta).
                                                                    (4)
```

K105's `e_0/e_1` swap is one element of the first factor. The rational rotation

```text
e_0 -> (3 e_0 + 4 e_1)/5,
e_1 -> (-4 e_0 + 3 e_1)/5                           (5)
```

is another exact witness and shows that the ambiguity is continuous rather
than a two-point accident.

Any line selector natural with respect to the frozen packet must return a line
fixed by every automorphism in (4). The standard real representation of
`O(256)` has no nonzero invariant line. Thus the action, domain and Green data
do not naturally select any K91-positive line in `E_+`. This is stronger than
coordinate nonselection but remains a theorem only about the frozen packet.

## 2. Cross-term-only persistence theorem

The same obstruction survives every continuation whose only new
distortion-sensitive coefficient is a cross map

```text
A : M^10 -> D^448                                      (6)
```

while the distortion kinetic and potential block remains fibre-scalar. Let
`P_+` denote the 260-dimensional positive eigenspace of `K` and define

```text
W_A = P_+ intersect ker(A^T K).                         (7)
```

Since `rank(A^T K)<=10`, the Grassmann dimension inequality gives

```text
dim W_A >= 260-rank(A) >= 250.                          (8)
```

The restriction of `K` to `W_A` is positive definite and `im A` is
`K`-orthogonal to `W_A`. Any orthogonal rotation of `W_A`, extended by the
identity on its `K`-orthogonal complement, preserves `K`, fixes `A`, and
commutes with the unchanged fibre-scalar distortion block. The augmented
action therefore retains at least an `O(dim W_A)` positive blind symmetry.

The bound is sharp: a rank-ten coefficient with independent image along ten
positive axes leaves exactly `250` of the original positive axes in (7).
Accordingly, a gauge-completed `A_2+A_0` may break the literal `e_0/e_1` swap,
but if it enters only through a `10 -> 448` cross term it cannot uniquely
select a positive line. This does not obstruct a new distortion-to-distortion
action coefficient, a boundary operator, a state, or an observable interface.

## 3. Typed symmetry-breaker tests

Let `U` exchange `e_0` and `e_1` and act identically elsewhere. An additional
datum must first have a nonzero symmetry defect:

```text
cross coefficient A:      Delta_A     = U A - A,
distortion term V:         Delta_V     = U^-1 V U - V,
boundary operator Theta:  Delta_Theta = U^-1 Theta U - Theta,
state covariance Lambda:  Delta_Lambda= U^* Lambda U - Lambda,
observable O:              Delta_O     = O U - O.             (9)
```

For a quadratic distortion or Robin boundary term, formal compatibility also
requires

```text
V^T K = K V,             Theta^T K = K Theta.             (10)
```

A nonzero defect proves only that the added datum breaks the swap. Selection
requires more: the datum must be independently owned, its relevant spectral
projector must be rank one and `K`-positive with a nonzero separating gap, and
the chosen line must reduce the completed Euler operator and preserve its
closed domain, Green identities and boundary form.

For a state candidate, positivity must hold on an independently constructed
physical quotient, the antisymmetric part must match the causal propagator,
and bisolution, gauge-basic and—if curved-spacetime credit is sought—Hadamard
conditions remain mandatory. A symmetry-breaking covariance may be an initial
or boundary preparation rather than an action-selected vacuum. For an
observable, `O U != O` must be accompanied by a fixed source/interaction,
gauge basicness, causal localization and a no-refit record rule.

Temporal positive-frequency splitting does not distinguish `e_0` from `e_1`
because their modal frequencies coincide. The existing scalar boundary family
`Omega+rI` and every state covariance obtained by functional calculus of the
frozen Euler operator likewise commute with (4).

## 4. Exact contrary control and switch condition

To prove that the tests do not reject every selector, plant the full
distortion-space Robin operator

```text
Theta_* e_i = (i+1)e_i,       i=0,...,447.                 (11)
```

It is invertible, satisfies `Theta_*^T K=K Theta_*`, retains the ambient
inertia `(260,188,0)`, has `Delta_Theta_* != 0`, and has the simple isolated
lowest eigenspace `span(e_0)`, which is `K`-positive with unit gap. Thus a full
distortion/boundary datum can break the blind-sector symmetry without deleting
the negative carrier. But (11) is deliberately a planted coordinate control:
it has no source, boundary-normal, locality or physical-state ownership and
selects nothing in K105.

The credible reopener is a source/action-derived distortion or boundary
operator—such as a typed boundary Dirac, Calderon or Dirichlet-to-Neumann
operator—constructed from the actual carrier, action and boundary normal. The
program switches to forward physical-state and observable-export burdens only
if that owner satisfies (9)-(10), has a simple isolated `K`-positive spectral
line, preserves the analytic and Green packet, and keeps all 188 negative
ambient directions explicit. Otherwise the exact nonselection result persists.

## Inline postflight bookend

- **Strongest overclaim:** interpreting (4) or (8) as a theorem against every
  positive subspace or every possible GU action. Refused: a full distortion,
  boundary, state or observable datum is outside the cross-term-only class.
- **Strongest contrary construction:** a source-owned boundary or distortion
  operator with a simple positive eigenspace may select a line. Preserved;
  (11) proves the mathematical test can recognize that shape without granting
  it source or physical status.
- **Weakest reproducibility seam:** the continuous-group theorem uses the exact
  zero-row decomposition, not the counts alone. The probe reconstructs the row
  support, inertia and rational rotation before applying the abstract block
  argument; the general rank bound is proved by dimension, with a sharp
  rank-ten finite control.

The narrow exact probe and its baseline-first hostile selftest certify the
finite packet, theorem premises, planted breaker and claim fences. K105's
ambient pairing and rank-one leakage remain unchanged. No authenticated source
action, historical Shiab, physical quotient, state, Born pairing, curved local
net, prediction, confirmation, canon or public-posture state moves.

## Reproduction

```bash
uv run --offline --with sympy python \
  tests/channel-swings/k106_k105_action_symmetry_positive_subspace_probe.py
uv run --offline --with sympy python \
  tests/channel-swings/k106_k105_action_symmetry_positive_subspace_probe.py --selftest
```
