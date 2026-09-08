---
title: "K160 spectator-Weyl weighted-denominator wave"
status: active_research
doc_type: conditional_spectator_weyl_unweighted_norm_obstruction_and_weighted_denominator_interface_result
created: 2026-09-08
date: 2026-09-08
claim_ceiling: exact repository-owned spectator-topology and weighted-certificate-interface result for the supplied two-edge positive-Fock point control; at every finite sharp cutoff the matched diagonal Weyl tail converges on each fixed spectator-energy fiber but has infinite ordinary operator norm across unbounded spectator Fock space, while one spectator-energy weight gives an exact outward O(Lambda^-1) bound on the complete K157 rectangle; a native weighted resolvent transfer still lacks the complete Pauli/exchange denominator error, inverse smoothing, low-energy separation, same-family rank and left-tail floor; no native count, K152 interval, physical/source selection, Born derivation, prediction or confirmation follows
manifest: lab/process/k160-spectator-weyl-weighted-denominator-wave.json
solver: tests/channel-swings/k160_spectator_weyl_weighted_denominator.py
probe: tests/channel-swings/k160_spectator_weyl_weighted_denominator_probe.py
target_claim: INTERNAL_TARGET:K159_UNWEIGHTED_SPECTATOR_WEYL_CONVERGENCE
target_claim_verdict: ORDINARY_OPERATOR_NORM_ROUTE_KILLED_WEIGHTED_ROUTE_NOT_YET_FALSIFIED
canon_verdict_change: none
---

# K160 spectator-Weyl weighted-denominator wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact remains on
> a repository-supplied positive particle/hole control. It does not identify
> the source-native GU object or select a physical polarization, extension,
> coupling, state, or observable. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this result binds K133--K159's equal-coupling two-edge point control. It
tests whether K159's operator-valued Weyl denominator can converge in ordinary
operator norm on the full spectator-Fock boundary space, and then types the
weakest energy-weighted replacement that survives. It is not a result about
Weinstein's source action, a physical Hamiltonian, or the truth of GU.

```gu-typed-objects
result: exact logarithmic obstruction to ordinary operator-norm convergence of the matched cutoff Weyl tail, plus a one-spectator-energy weighted tail estimate and fail-closed weighted Krein compiler
carrier: K139's hard-core C3 impurity tensor antisymmetric Fock carrier over L2(R;C4), with K148's operator-valued boundary space over an unbounded spectator-energy operator S LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive Fock Hilbert pairing and boundary-space Hermitian pairing in the Krein resolvent formula ON=repository_signed_point_control
real_structure: CAR adjoint and complete signed flavor permutation; q=(1,0) transports to q=(0,1) only when the weighted denominator, inverse smoothing, contour, rank and floor data intertwine
grading: conserved incidence charge, finite cutoff versus cofinal limit, fixed spectator fiber versus uniform spectator operator norm, local contour island versus complete below-threshold count
action_owner: repository-construction -- operator, extension coordinate, time orientation, polarization, couplings, domain and state are not selected by Weinstein's source or a GU action
target: a well-typed energy-weighted boundary-denominator route after the ordinary operator-norm route fails MAP-TYPE=intertwiner
```

## Inline preflight bookend

K159 correctly replaced the killed common free graph and form routes with an
operator-valued boundary/Weyl comparison, but its abstract compiler still
asked for an ordinary operator-norm Weyl error `dm`. K133 had already exposed
the decisive spectator logarithm. Applying that exact asymptotic to the
*cutoff-to-limit denominator difference*, rather than merely to the limiting
diagonal, changes the route: pointwise convergence on every fixed spectator
fiber does not become uniform convergence over unbounded spectator energy.

The route census covered ordinary norm convergence, strong/fiberwise
convergence, spectator-energy weights, weighted Neumann inversion, the K152
regular-representative branch, and direct low-energy denominator estimates.
The cheapest discriminator is the diagonal vacuum expectation. It already
kills the ordinary topology, so no complete Pauli/exchange calculation can
rescue that premise.

## 1. The matched Weyl tail is unbounded in spectator operator norm

Let `S>=0` be the spectator bath energy and keep K133's subtraction coordinate
`mu=256`. At the interior spectral point `z=-1`, the matched sharp-cutoff
diagonal tail on a spectator-energy fiber `s` is

```text
T_Lambda(s)=integral_(|p|>Lambda)
  [1/(omega(p)+s+1)-1/(omega(p)+mu)] dp/(2 pi).       (1)
```

This is the active-edge vacuum diagonal matrix element of the full
operator-valued denominator error. On that reducing input, active-edge Pauli
terms vanish and flavor-changing exchange terms have zero diagonal
expectation, so they cannot cancel (1) in the norm lower bound.

Put `P=max(Lambda,mu+1,1)`. For `P<=p<=s/4`, `omega(p)<=p+1`, hence

```text
1/(omega+mu) >= 1/(2p),
1/(omega+s+1) <= 1/s <= 1/(4p).                       (2)
```

Using both momentum half-lines gives, whenever `s>=4P`,

```text
|T_Lambda(s)| >= [4 pi]^-1 log(s/(4P)).               (3)
```

The spectator-Fock spectrum is unbounded. Therefore the multiplication
operator represented by (1) has infinite norm for every finite `Lambda`.
For each *fixed* `s`, its tail still converges to zero as `Lambda` tends to
infinity. The failed implication is precisely

```text
fiberwise cutoff convergence  !=  ordinary operator-norm convergence. (4)
```

Thus K159's native unweighted `dm` cannot exist on the complete boundary
space. Replacing that space by a finite impurity matrix would erase the K148
spectator variable and is not an admissible repair.

## 2. One spectator-energy weight restores a quantitative tail

On the complete K157 rectangle, `Re z<=-1` and `|z|<21/4`. Resolvent
denominators then give the absolute bound

```text
|T_Lambda(s;z)|
 <= pi^-1 [log(1+s/Lambda)+(mu+|z|)/Lambda].          (5)
```

For `0<alpha<=1`, `log(1+t)<=t^alpha/alpha`. Multiplying on the right by
`(1+S)^(-alpha)` and using `1/pi<1/3` yields

```text
||T_Lambda(S;z)(1+S)^(-alpha)||
 <= 1/(3 alpha Lambda^alpha)+(mu+21/4)/(3 Lambda).    (6)
```

At the smallest integral one-energy weight, `alpha=1`, this is

```text
Lambda=4096:   1049/49152,
Lambda=65536:  1049/786432.                           (7)
```

This proves an `O(Lambda^-1)` outward estimate uniformly on the whole
rectangle for the matched diagonal spectator term. It does not yet include
the remaining Pauli and exchange components of the native Weyl denominator.

## 3. Weighted denominator errors have a valid Neumann compiler

Write `A=1+S`, `D=D_W(z)` and `D_n=D_(W,n)(z)`. Suppose uniformly on one
complete contour that

```text
epsilon=||(D_n-D)A^-1||,
c1=||A D^-1||,
d0=||D^-1||,
theta=epsilon c1 < 1.                                 (8)
```

Then `K=(D_n-D)D^-1` has norm at most `theta`, so

```text
D_n^-1 = D^-1(I+K)^-1,
||D_n^-1|| <= d0/(1-theta),
||D_n^-1-D^-1|| <= d0 theta/(1-theta).                (9)
```

Substitution into K159's Krein expansion gives an ordinary resolvent error.
The exact-rational companion accepts an abstract fixture with
`theta=1/500`, approximant inverse bound `1000/499`, inverse-difference bound
`2/499`, and total resolvent error `4497/499000`; on a perimeter-ten contour,
the rank-transfer gap closes.

That positive control proves the interface, not the native premises. In
particular, the inverse-smoothing estimate `||A D^-1||<infinity` is independent
of (6). It must be established for the actual operator-valued denominator and
on the same contour.

## 4. The native denominator packet remains incomplete

The weighted route now requires all of the following on the same K141 cofinal
family:

- the complete weighted denominator error, including diagonal Pauli and all
  exchange pieces rather than only (6);
- a uniform one-energy inverse-smoothing bound and low-energy denominator
  separation;
- exact reference rank for those same cofinal matrices;
- a native spectral floor excluding spectrum left of `-5`;
- the signed-charge intertwiner carrying every ingredient to q=(0,1).

The fail-closed compiler rejects any missing reference, a weighted Neumann
parameter at least one, a contour error at least `3/5`, or a floor below `-5`.
No native packet is supplied here.

## 5. Route disposition

The ordinary operator-norm boundary/Weyl route is **killed**. The
energy-weighted route is **not yet falsified** because its diagonal ultraviolet
piece closes exactly, but its inverse-smoothing and complete denominator
premises have not been tested. An immediate switch to K152 would discard that
newly viable topology before its decisive denominator question is answered.
The next discriminator is therefore the native inverse-smoothing/low-energy
separation estimate; failure there routes to K152 with K158's five
normal-ordered tails, regular-core bound, residual, coercivity and next-spectrum
data.

## Inline postflight bookend

- **Strongest exact advance:** every finite-cutoff matched Weyl tail has
  infinite ordinary spectator operator norm, while one spectator-energy weight
  yields the uniform complete-rectangle bound (6).
- **Route verdict:** K159's unweighted `dm` route is killed. The weighted
  denominator route is `NOT-YET-FALSIFIED` and has a fail-closed inverse and
  resolvent interface.
- **Strongest contrary construction:** fixed-energy fibers converge. That is
  genuine strong/fiberwise evidence, but equation (3) proves it is not uniform
  over spectator Fock space.
- **Strongest overclaim:** “the diagonal weighted bound is the complete native
  Weyl error.” Refused: Pauli/exchange terms and inverse smoothing remain
  separately missing.
- **Weakest reproducibility seam:** the native K139/K141 denominator is not yet
  serialized into complete weighted components or a cofinal low-energy inverse
  certificate.

No native ground count, K152 energy interval, threshold/Gram closure,
full-Fock scattering/NESS, physical or source selection, Born rule, held-out
score, prediction, confirmation, canon, paper, release, or public-posture move
follows.

## Next condition

Derive the complete K139/K141 operator-valued Weyl denominator error after one
spectator-energy weight, including every Pauli/exchange component, and prove
`||(1+S)D_W(z)^(-1)||` plus low-energy denominator separation uniformly on the
complete K157 contour. If either estimate fails, switch to the regular-
representative/K152 branch. If both close, combine them with same-family rank,
the native left floor and the signed-charge intertwiner before any count claim.

## Reproduction

```bash
python3 tests/channel-swings/k160_spectator_weyl_weighted_denominator.py --demo
python3 tests/channel-swings/k160_spectator_weyl_weighted_denominator_probe.py
python3 tests/channel-swings/k160_spectator_weyl_weighted_denominator_probe.py --selftest
```
