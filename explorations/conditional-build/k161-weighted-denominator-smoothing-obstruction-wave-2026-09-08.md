---
title: "K161 weighted-denominator smoothing obstruction wave"
status: active_research
doc_type: conditional_complete_weighted_weyl_tail_and_inverse_smoothing_obstruction_result
created: 2026-09-08
date: 2026-09-08
claim_ceiling: exact repository-owned result for the supplied two-edge positive-polarization point-Fock control that all five normal-ordered K139/K141 Weyl-denominator components converge after one spectator-energy weight with an explicit O(Lambda^-1/2) complete-rectangle bound, while the active-vacuum high-spectator sequence has only logarithmic denominator growth and makes the required full-energy inverse-smoothing norm infinite whenever the denominator inverse exists; this kills the weighted Neumann transfer, not the singular extension, and selects the regular K152 interface, whose five tails are now serialized but whose regular-core bound, total form-dual residual, coercivity, next-spectrum gap, left floor and charge transport remain absent; no native count, K152 interval, physical/source selection, Born derivation, prediction or confirmation follows
manifest: lab/process/k161-weighted-denominator-smoothing-obstruction-wave.json
solver: tests/channel-swings/k161_weighted_denominator_smoothing_obstruction.py
probe: tests/channel-swings/k161_weighted_denominator_smoothing_obstruction_probe.py
target_claim: INTERNAL_TARGET:K160_WEIGHTED_BOUNDARY_INVERSE_SMOOTHING
target_claim_verdict: COMPLETE_WEIGHTED_ERROR_CLOSES__INVERSE_SMOOTHING_ROUTE_KILLED__REGULAR_K152_ROUTE_SELECTED
canon_verdict_change: none
---

# K161 weighted-denominator smoothing obstruction wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact remains on
> a repository-supplied positive particle/hole control. It does not identify
> the source-native GU object or select a physical polarization, extension,
> coupling, state, or observable. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this result binds K139--K160's equal-coupling two-edge point control.
It completes the one-energy weighted cutoff estimate on K148's actual
spectator-Fock boundary space and tests the independent inverse-smoothing
premise required by K160. It does not test Weinstein's source action, build a
physical Hilbert space, or settle the truth of GU.

```gu-typed-objects
result: complete one-spectator-energy weighted Pauli/exchange Weyl-denominator cutoff convergence together with a high-spectator no-go for the full-energy inverse-smoothing premise and a fail-closed switch to the regular K152 interface
carrier: K139's hard-core C3 impurity tensor antisymmetric Fock carrier over L2(R;C4), with K148's operator-valued boundary space over the unbounded spectator-energy operator S and K141's normalized momentum-cell cofinal family LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive Fock Hilbert pairing and finite boundary-space Hermitian pairing; graph-dual annihilation estimates are used only after the explicit right weight (1+S)^-1 ON=repository_signed_point_control
real_structure: CAR adjoint and complete signed flavor permutation; no q=(0,1) count transfers until the regular residual, coercivity, floor and every charge-block object intertwine
grading: conserved incidence charge, four particle/hole polarity blocks, finite cutoff versus cofinal limit, active-edge vacuum versus spectator excitation, weighted error topology versus inverse-smoothing topology
action_owner: repository-construction -- operator, extension coordinate, time orientation, polarization, couplings, domain and state are not selected by Weinstein's source or a GU action
target: close all weighted second-order denominator tails, kill or validate the inverse-smoothing bridge, and route the surviving certificate topology MAP-TYPE=intertwiner
```

## Inline preflight bookend

K160 closed only the matched diagonal spectator tail. K139 and K141 already
prove that the diagonal occupation and four normal-ordered exchange blocks
converge on the free operator graph, but had not converted those statements
to one common energy-weighted denominator error. That conversion is the first
packet. The second packet asks the logically independent question K160 exposed:
whether the limiting denominator inverse gains one complete spectator-energy
power.

Mechanism retrieval found the exact K133 spectator logarithm, K134's Pauli and
exchange census, K135's graph-dual estimates, K139's four signed polarity
blocks, K141's common continuum carrier, K148's operator-valued boundary, and
K160's diagonal weighted estimate. It found no complete weighted component
sum or full-energy inverse-smoothing theorem. No correction-registry entry
supersedes those inputs.

The route census covered boundary triples, Feshbach/Weyl denominators, CAR
graph duals, energy weights, Combes--Thomas and elliptic smoothing, compactness,
high-spectator Weyl sequences, the regular pullback, generalized Ritz and
Lehmann--Goerisch enclosure, source ownership and hostile topology review.
Elliptic intuition would demand order-one denominator growth, while the held
spectator asymptotic is only logarithmic. The high-spectator sequence decides
that fork before any large matrix search. Exact computation is limited to
outward rational tail bounds and fail-closed interface checks.

The source and physics ledgers supply scope, not selection. `SC-META-53`
remains `UNCERTAIN` about the physical unbounded-spectrum problem, and
`LT-SM8` remains `NEEDS` because no GU action-derived quotient, positive
physical pairing or state is constructed here. No ledger row moves.

## 1. All five normal-ordered denominator tails close after one energy weight

Write

```text
omega(p)=sqrt(1+p^2),
h(p)=(2 pi)^(-1/2)(omega(p)+mu)^(-1),
A=1+S,  mu=256.                                        (1)
```

For `Lambda>=1`, the continuum point graph-dual tail and the dressed creation
tail satisfy

```text
||1_(|p|>Lambda)/omega||_2^2
 <= integral_(|p|>Lambda) dp/(2 pi p^2)
 < 1/(3 Lambda),

||1_(|p|>Lambda) h||_2^2 < 1/(3 Lambda).              (2)
```

The corresponding full squared norms are at most `1/2`. CAR pull-through gives

```text
||a(f) A^-1|| <= ||f/omega||_2,
||a*(h)|| <= ||h||_2.                                  (3)
```

For one ordered edge pair in one polarity block, split the cutoff difference
according to whether the omitted momentum occurs on the annihilation or the
resolvent-dressed creation leg. Equations (2)--(3) give

```text
||(X_Lambda^(sigma,tau)-X^(sigma,tau)) A^-1||
 <= 2/sqrt(6 Lambda)=sqrt(2/(3 Lambda)).               (4)
```

The two-edge control has four ordered edge pairs and the four K139 polarity
blocks `++,+-,-+,--`. Matrix-unit contractions have norm at most one and the
declared equal couplings are one, so all exchange tails together are bounded
by

```text
16 sqrt(2/(3 Lambda)).                                 (5)
```

The diagonal component has two matched active-edge tails. K160 contributes
`1049/(6 Lambda)` after summing them. The four particle/hole endpoint
occupation corrections contribute at most `4/(3 Lambda)`. Hence

```text
||(D_(W,Lambda)(z)-D_W(z)) A^-1||
 <= 1057/(6 Lambda)+16 sqrt(2/(3 Lambda))              (6)
```

uniformly on the complete K157 rectangle. This is a deliberately conservative
triangle bound; its role is convergence, not sharp spectral optimization.

For exact outward rational certificates,

```text
Lambda=4096:  sqrt(2/(3 Lambda)) < 1/78,
              complete error < 79277/319488;

Lambda=65536: sqrt(2/(3 Lambda)) < 1/313,
              complete error < 6622297/123076608.      (7)
```

Thus the component gap left by K160 genuinely closes: the weighted error is
complete and tends to zero as `O(Lambda^(-1/2))`. This conclusion does not
say that the product with the limiting inverse is small.

## 2. The limiting denominator cannot supply one full energy of smoothing

Fix any point `z` on the K157 contour. Take normalized boundary vectors
`psi_s` with the active edge species empty and spectator energy `S psi_s=s
psi_s`, along an unbounded sequence. Every normal-ordered exchange block
annihilates this active-vacuum sequence. Endpoint occupation corrections are
zero or bounded, `W` is finite dimensional and bounded, and the matched K133
spectator functional grows only logarithmically. Therefore constants
`C0,C1<infinity`, independent of `s`, obey

```text
||D_W(z) psi_s|| <= C0+C1 log(1+s).                    (8)
```

There are now only two cases.

If `D_W(z)` is not invertible, the required contour separation already fails.
If it is invertible, put

```text
phi_s=D_W(z)psi_s / ||D_W(z)psi_s||.                   (9)
```

Then `||phi_s||=1`, while

```text
||(1+S)D_W(z)^(-1) phi_s||
 = ||(1+S)psi_s|| / ||D_W(z)psi_s||
 >= (1+s)/(C0+C1 log(1+s)) -> infinity.               (10)
```

Consequently

```text
||(1+S)D_W(z)^(-1)||=infinity                         (11)
```

whenever the inverse exists. K160's weighted Neumann parameter is therefore
not merely unproved: its required inverse-smoothing factor is infinite. The
alternative failure of invertibility is no rescue because it violates the
same route's denominator-separation premise.

Equation (11) kills the **weighted inverse-transfer topology**. It does not kill the singular boundary operator, fixed-energy resolvents, weaker
logarithmic weights, or the regular-representative route. In particular,
complete weighted cutoff convergence in (6) and failure of the inverse product
in (11) are compatible facts.

## 3. The regular-representative/K152 branch is now selected

The route switch preserves the component work rather than discarding it. The
regular branch now has explicit references for exactly five normal-ordered
tails:

```text
q_Lambda, T_Lambda^(++), T_Lambda^(+-),
T_Lambda^(-+), T_Lambda^(--).                          (12)
```

K152 does not require the killed free-`H0` graph chart from K158 and does not
require the killed boundary inverse-smoothing estimate from (11). It instead
requires, on one same-cofinal conforming family,

- a complete regular-core relative bound `B`;
- the total shifted form-dual residual, after all five tails compose;
- a proved coercive shift;
- a lower bound on the next distinct spectral value;
- a native floor excluding spectrum left of the chosen contour; and
- the complete signed-flavor unitary intertwiner.

The companion compiler accepts only when all six data classes and all five
tail references are present. K161 supplies the five tails and none of the six
remaining native classes, so it correctly emits no interval or count.

## 4. Rank and count remain fail-closed

The weighted boundary route cannot be revived by a finite reference rank,
because its inverse topology has failed on the actual spectator space. The
regular route still cannot turn K157's two-mode inertia into a native count:
that finite block is not yet the same cofinal family, the complete residual
and next-spectrum gap are absent, and no native left floor excludes spectrum
below `-5`.

Signed flavor covariance remains an algebraic requirement, not a verbal
symmetry shortcut. No `q=(0,0)`, `q=(1,0)` or transported `q=(0,1)` native
ground count follows.

## Inline postflight bookend

- **Strongest exact advance:** every diagonal Pauli/spectator and polarity-
  exchange component has one common complete-rectangle weighted error bound,
  equation (6).
- **Route verdict:** the weighted cutoff error closes, but its required
  full-energy inverse smoothing is impossible. The weighted Neumann transfer
  is killed and the regular K152 branch is selected.
- **Strongest contrary construction:** fixed-spectator fibers and weaker
  logarithmic weights may still converge. They do not supply the factor
  `1+S` used by K160's inverse compiler.
- **Strongest overclaim:** “failure of inverse smoothing kills the singular
  extension.” Refused: the no-go binds one transfer topology only.
- **Weakest reproducibility seam:** the next regular packet must compose the
  five now-serialized tails into one form-dual residual; separately quoting
  their convergence does not manufacture `B`, coercivity or a next-spectrum
  gap.

No native ground count, K152 energy interval, threshold/Gram closure,
full-Fock scattering/NESS, physical or source selection, Born rule, held-out
score, prediction, confirmation, canon, paper, release, or public-posture move
follows.

## Next condition

On one explicit K141 cofinal conforming family, assemble the regular
representative from `q, T^(++), T^(+-), T^(-+), T^(--)`; compute the complete
regular-core bound `B`, total shifted form-dual residual and coercivity, and
prove a next-distinct-spectrum lower bound plus a native floor left of `-5`.
Then verify the full signed-charge intertwiner and feed only that complete
packet to K152. Do not reopen the weighted inverse-smoothing route without a
different weight topology or a changed high-spectator premise.

## Reproduction

```bash
python3 tests/channel-swings/k161_weighted_denominator_smoothing_obstruction.py --demo
python3 tests/channel-swings/k161_weighted_denominator_smoothing_obstruction_probe.py
python3 tests/channel-swings/k161_weighted_denominator_smoothing_obstruction_probe.py --selftest
```
