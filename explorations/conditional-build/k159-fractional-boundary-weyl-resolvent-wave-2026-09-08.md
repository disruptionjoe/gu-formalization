---
title: "K159 fractional boundary and Weyl-resolvent wave"
status: active_research
doc_type: conditional_fractional_domain_common_form_obstruction_and_boundary_weyl_resolvent_interface_result
created: 2026-09-08
date: 2026-09-08
claim_ceiling: exact repository-owned fractional-domain and certificate-interface result for the supplied two-edge positive-Fock point control; the dressed point boundary lies in the free Hilbert scale exactly below exponent one half, so neither the common free form domain nor free operator graph survives, while an operator-valued boundary/Weyl resolvent comparison remains available but its native spectator-Fock denominator lacks cofinal separation, rank and left-tail data; no native count, K152 interval, physical/source selection, Born derivation, prediction or confirmation follows
manifest: lab/process/k159-fractional-boundary-weyl-resolvent-wave.json
solver: tests/channel-swings/k159_fractional_boundary_weyl_resolvent.py
probe: tests/channel-swings/k159_fractional_boundary_weyl_resolvent_probe.py
target_claim: INTERNAL_TARGET:K158_COMMON_FREE_FORM_OR_BOUNDARY_RESOLVENT_REPAIR
target_claim_verdict: COMMON_FREE_FORM_ROUTE_KILLED_BOUNDARY_WEYL_ROUTE_NOT_YET_FALSIFIED
canon_verdict_change: none
---

# K159 fractional boundary and Weyl-resolvent wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact remains on
> a repository-supplied positive particle/hole control. It does not identify
> the source-native GU object or select a physical polarization, extension,
> coupling, state, or observable. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this result binds K139--K158's equal-coupling two-edge point control.
It tests K158's direct-form alternative, locates the exact domain threshold,
and types the boundary-resolvent replacement, including K148's operator-valued
many-body boundary space. It is not a result about
Weinstein's source action, a physical Hamiltonian, or the truth of GU.

```gu-typed-objects
result: sharp fractional Hilbert-scale classification of the dressed point boundary, a common-free-form route obstruction, and a fail-closed boundary-gamma/Weyl resolvent and count-transfer interface
carrier: K139's hard-core C3 impurity tensor antisymmetric Fock carrier over L2(R;C4), with free Hilbert scale Dom((H0+1)^s) and an operator-valued spectator-Fock boundary space that is not reduced to the finite impurity matrix LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive Fock Hilbert pairing, fractional free-scale duality, and the boundary-space Hermitian pairing in the Krein resolvent formula ON=repository_signed_point_control
real_structure: CAR adjoint and complete signed flavor permutation; q=(1,0) transports to q=(0,1) only when gamma fields, Weyl denominators, contour and lower-floor data intertwine
grading: conserved incidence charge, fractional exponent s, finite approximant versus cofinal limit, local contour island versus complete below-threshold count
action_owner: repository-construction -- operator, extension coordinate, time orientation, polarization, couplings, domain and state are not selected by Weinstein's source or a GU action
target: well-typed boundary-resolvent replacement for the killed common free-graph and common free-form routes MAP-TYPE=intertwiner
```

## Inline preflight bookend

K158 correctly killed the free-operator-graph estimate and offered either a
boundary/rigged-domain route or a direct form-resolvent route. Re-deriving the
domain question before choosing between them changes the work list: the same
point vector also misses the free quadratic-form domain. A common-free-form
Kato comparison is therefore not a weaker repair; it repeats the topology
error at the endpoint exponent `1/2`.

The route census covered the free operator graph, the free quadratic-form
domain, fractional Hilbert scales, singular-form pullbacks, boundary triples,
Krein resolvent formulas, operator-valued Weyl functions, Riesz transfer
and equal-rank form enclosures. The ultraviolet exponent is the cheapest
route-changing discriminator. Once it excludes the common form domain, the
boundary/Weyl route is the only tested continuation that never applies the
point chart in a topology it does not preserve.

## 1. The dressed point vector has a sharp half-power threshold

With `omega(p)=sqrt(1+p^2)` and auxiliary coordinate `lambda=256`, the one-
channel dressed point vector is

```text
h(p)=(2 pi)^(-1/2)(omega(p)+lambda)^(-1).              (1)
```

Membership in the free Hilbert scale of exponent `s` requires

```text
integral omega(p)^(2s)/(omega(p)+lambda)^2 dp < infinity. (2)
```

The integrand is asymptotic to `|p|^(2s-2)`. Hence

```text
h in Dom(omega^s)  iff  s<1/2.                         (3)
```

At `s=1/2`, whenever `omega>=lambda`, the integrand is bounded below by a
constant multiple of `1/omega`, so the divergence is logarithmic. At `s=1`,
K158's nonzero constant lower density is recovered. Thus `h` is Hilbert-
bounded and belongs to every strict sub-form fractional scale, but it is in
neither the free quadratic-form domain nor the free operator domain.

For `0<=s<1/2` and a cutoff `Lambda>=1`, `1/pi<1/3` gives the outward bound

```text
||1_(|p|>Lambda) omega^s h||^2
 <= [3(1-2s)]^-1 Lambda^(2s-1).                        (4)
```

At `s=1/4`, `Lambda=4096`, this is `1/96` per channel. For the K141 cell
approximation with `delta=1/4096`, Lipschitz dispersion gives the complete
coarse cell bound `2 delta^2=1/8388608` per channel. Combining four signed
edge/polarity coefficients by the triangle inequality gives

```text
d_(1/4),n <= 4 sqrt(1/96+1/8388608).                  (5)
```

This converges as `O(n^-1/4)` along square indices. It is a valid rigged-scale
tail, not a free-form or free-graph bound.

## 2. The direct common-free-form route is killed

The free form domain is the `s=1/2` endpoint. Equation (3) excludes the
boundary correction already on the impurity vacuum. Removing any finite
momentum window leaves the logarithmic tail, so no cofinal cutoff makes the
missing form-domain error finite.

This does not kill K139's singular operator. K139 defines the extension on a
chart-transformed domain. It kills only the tempting argument that the same
chart can be compared on one common free quadratic-form domain. Nor can a
strict `s<1/2` estimate be silently promoted to the endpoint; its constant in
(4) diverges as `s` approaches `1/2`.

## 3. Operator-valued boundary gamma/Weyl data give the well-typed route

For one fixed self-adjoint extension coordinate `W`, write the boundary
resolvent in Krein form

```text
R_W(z)=R_0(z)+gamma(z) D_W(z)^(-1) gamma(conj z)^*,    (6)
```

where `D_W=W-M(z)` is the Weyl denominator. K148's native shared-corner
Feshbach analysis proves that the many-body self energy is operator-valued on
spectator bath Fock space; it does not reduce to the finite impurity matrix.
Thus `gamma`, `D_W` and every norm below are operator-valued on the complete
boundary space. The formula uses Hilbert-bounded gamma fields at nonreal `z`; it
does not require `gamma` or the K139 chart to preserve the free form or
operator domain.

Suppose uniformly on one complete contour that

```text
||R_(0,n)-R_0||<=r0,  ||gamma_n||,||gamma||<=g,
||gamma_n-gamma||<=dg, ||D^-1||<=d0, ||D_n-D||<=dm.   (7)
```

If `theta=d0 dm<1`, then

```text
||D_n^-1|| <= dn=d0/(1-theta),
||D_n^-1-D^-1|| <= d0 dn dm,                           (8)
```

and direct expansion of (6) gives

```text
eta <= r0 + dg dn g + g(d0 dn dm)g + g d0 dg.         (9)
```

The exact-rational companion compiler checks the scalar norm inequalities
(8)--(9), rejects a denominator
collision, and accepts a nonvacuous abstract perimeter-ten fixture with
`10 eta<6`. Those inequalities remain valid for bounded operators, but the
finite scalar fixture is not the native boundary object. The current chain does not serialize
uniform cofinal `dg`, `dm`, `d0` or `r0` for K139's same extension coordinate.

## 4. The repaired route changes the role of the five normal-ordered tails

K158 still correctly identifies missing diagonal Pauli/spectator and four
exchange tails plus a regular-core bound. Those quantities are required to
construct the regular representative quantitatively and to feed the K152
form/residual route. They are not additional inputs to (6) when the Weyl
operator is derived directly from the boundary extension; its renormalized
operator-valued denominator already owns that information. Requiring both
would double count one interaction correction under two representations.

The two routes therefore branch honestly:

- boundary/Weyl route: serialize `r0,dg,dm,d0` uniformly on the complete
  contour for the actual cofinal K141 approximation;
- regular-representative/K152 route: serialize the five normal-ordered tails,
  `B`, total residual, coercivity and next-spectrum data on conforming cores.

Neither branch inherits the other's missing data merely by renaming it.

## 5. Local rank still is not the complete ground count

Even if (9) closes, the reference rank must be proved on the same cofinal
family whose gamma/Weyl data enter the comparison. K157's arbitrary two-mode
matrix remains insufficient. And the rectangle encloses only `[-5,-1]`; a
native lower bound at least `-5`, or a contour closing the full lower half-
line, is still required to exclude spectrum left of `-5`.

The fail-closed count compiler therefore requires all of: same-cofinal-family
provenance, its exact rank, complete-contour error below `3/5`, and a native
left-tail floor. It accepts an abstract complete packet and rejects each
missing premise. No native packet is currently supplied.

## Inline postflight bookend

- **Strongest exact advance:** the dressed boundary has the sharp regularity
  `h in Dom(omega^s)` exactly for `s<1/2`, with an outward `s=1/4` cofinal
  tail and cell ledger.
- **Route verdict:** both the common free-operator-graph route and the common
  free quadratic-form route are killed. The boundary/Weyl Krein route is
  `NOT-YET-FALSIFIED` and now has an exact fail-closed error interface.
- **Strongest contrary construction:** K148 already proves that the native
  denominator is operator-valued on spectator Fock space. It may fail uniform
  contour separation even when every finite impurity matrix looks regular;
  the abstract compiler does not assume otherwise.
- **Strongest overclaim:** “fractional convergence below one half implies form
  convergence at one half.” Refused: the constant and the integral both
  diverge at the endpoint.
- **Weakest reproducibility seam:** K139--K141 do not serialize the cofinal
  operator-valued gamma/Weyl data or a native lower spectral floor.

The q=(0,1) sector remains only the signed-flavor image of q=(1,0), including
the boundary denominator and domain. No native count, K152 energy interval,
threshold/Gram closure, full-Fock scattering/NESS, physical or source
selection, Born rule, held-out score, prediction, confirmation, canon, paper,
release or public-posture move follows.

## Next condition

Derive the K139 extension's explicit operator-valued gamma field and Weyl
denominator on the spectator-Fock boundary space for the normalized K141
cofinal cells, including the matched
counterterm coordinate. Prove uniform denominator separation and the bound
`r0,dg,dm,d0` on a complete contour, compute exact rank on those same cofinal
matrices, and add a native floor excluding spectrum below the contour. If the
boundary denominator cannot be separated, switch to the regular-
representative/K152 branch and then supply the five normal-ordered tails,
`B`, residual, coercivity and next-spectrum data rather than mixing the two
interfaces.

## Reproduction

```bash
python3 tests/channel-swings/k159_fractional_boundary_weyl_resolvent.py --demo
python3 tests/channel-swings/k159_fractional_boundary_weyl_resolvent_probe.py
python3 tests/channel-swings/k159_fractional_boundary_weyl_resolvent_probe.py --selftest
```
