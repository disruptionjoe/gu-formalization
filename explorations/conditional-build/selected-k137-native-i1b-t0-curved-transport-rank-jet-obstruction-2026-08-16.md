---
title: "Selected-K137 native I1B T=0 curved transport rank/jet obstruction"
status: active_research
doc_type: exact_cross_stratum_characteristic_rank_background_jet_and_boundary_owner_gate
created: "2026-08-16"
registry: lab/process/selected-k137-native-i1b-t0-curved-transport-rank-jet-obstruction.json
probe: tests/channel-swings/selected_k137_native_i1b_t0_curved_transport_rank_jet_obstruction_probe.py
grade: "K137 PROVES THAT K136'S FIVE GAUGE-REDUCED NULL CLASSES DO NOT FORM ONE SMOOTH CONSTANT-RANK BUNDLE THROUGH THE GENERIC NONNULL, NULL, AND SPACELIKE-SHELL STRATA. THE GAUGE-REDUCED COUPLED KERNEL HAS DIMENSION ZERO AT GENERIC NONSHELL NONNULL COVECTORS, FIVE ON THE NULL METRIC SCHUR STRATUM, 46481 AT THE A=4 SHELL, ZERO AT A=121, AND POSITIVE DISTORTION MULTIPLICITY ON THE OTHER SHELLS. NULL BICHARACTERISTIC BASE CURVES ARE THE METRIC NULL-GEODESIC HAMILTON FLOW, BUT AMPLITUDE TRANSPORT REQUIRES A CONSTANT-RANK STRATUM, THE FULL SUBPRINCIPAL SYMBOL ALONG THE CURVE, AND GLUING DATA AT RANK CHANGES. K127 OWNS ONLY AN UNSELECTED POINTWISE RICCI-FLAT TWO-JET FAMILY; EQUAL TWO-JETS WITH DIFFERENT THREE-JETS HAVE THE SAME K127/K136 POINT SYMBOL DATA BUT DIFFERENT NEIGHBORHOOD TRANSPORT. THE DISPLAYED I1B ACTION OWNS NO BOUNDARY FUNCTIONAL, GAUGE FIXING, PSEUDODIFFERENTIAL PROJECTOR, OR CROSS-STRATUM GLUING LAW. FIXED-BOUNDARY VARIATION IS NOT SUCH AN ADDITION. STRATUMWISE TRANSPORT AFTER THOSE DATA ARE SUPPLIED REMAINS OPEN."
target_claim: K136_NEXT_GATE__COMPLETE_CURVED_SUBPRINCIPAL_TRANSPORT_ON_FIVE_CLASS_QUOTIENT_OR_ACTION_OWNED_BOUNDARY_ADDITION
target_verdict: ONE_CROSS_STRATUM_FIVE_BUNDLE_OBSTRUCTED_BY_EXACT_RANK_JUMPS__NULL_BASE_FLOW_GEODESIC__AMPLITUDE_CONNECTION_UNSELECTED_BY_POINT_TWOJET__NO_CURRENT_I1B_BOUNDARY_ADDITION__K138_GENERIC_RICCI_FLAT_THREEJET_STRATUMWISE_TRANSPORT
canon_verdict_change: none
---

# Selected-K137 native I1B T=0 curved transport rank/jet obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> first-transgression, real `Cl(7,7)`, mixed-order characteristic-rank,
> Hamilton-transport, metric-jet and boundary-owner calculation. Ordinary
> Einstein, Higgs/VEV, family-index, chirality, anomaly, symmetry-breaking and
> familiar particle-spectrum constructions do not adjudicate it without an
> explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: K137 binds the selected displayed `comm/symi/symi` `I1B` Hessian at
K127's local Ricci-flat `T=0` fixed-boundary germ family, K135's coupled
nonnull/shell symbol, and K136's five-class null quotient. It obstructs one
smooth five-dimensional quotient through rank-changing strata. It does not
obstruct transport confined to a smooth constant-rank stratum after a
background neighborhood, complete subprincipal coefficient, and domain or
gluing law are supplied.

## Result in plain English

K136 left a tempting but ill-typed instruction: transport five null classes
through null and spacelike-shell crossings. K137 applies the necessary
constant-rank test before inventing a connection. After quotienting only the
four action-owned metric diffeomorphisms, the coupled kernel dimensions are

```text
generic nonnull, away from shells: 0;
null metric Schur stratum:          5;
spacelike shell a=4:                46481;
spacelike shell a=121:              0;
other spacelike shells:             positive, shell-dependent.
```

A vector bundle has locally constant fibre dimension. These fibres therefore
cannot be one smooth rank-five bundle through the stated crossings. The rank
jump is not a coordinate defect and cannot be repaired by choosing a basis.

The scalar null factor still supplies a base Hamilton flow: for
`q(x,xi)=g^{-1}(xi,xi)`, `H_q` is the null-geodesic bicharacteristic flow.
That does not transport amplitudes. A system amplitude connection additionally
needs smooth left/right characteristic projectors of constant rank and the
complete subprincipal symbol along the curve. At shell or null rank changes,
the projector is singular or changes dimension and a separate transmission,
mode-conversion, boundary, or gluing law is required.

K127 does not select those missing data. It owns an arbitrary Ricci-flat
metric two-jet at one point. Two metric germs can have the same two-jet there
and different third jets. They agree on the pointwise curvature, K127
stationarity, K135 symbol and K136 quotient, but differ in the first
neighborhood variation of the connection/curvature coefficients and hence in
amplitude transport away from the point. A point two-jet is enough for the
frozen symbol calculation, not for a transport law along a bicharacteristic.

Finally, the displayed `I1B` functional supplies no boundary functional,
gauge-fixing term, pseudodifferential projector, or rank-change gluing law.
K127's compact-support or fixed-boundary variation makes the local bulk
variation legal; it does not turn the fixed value into an action-owned
boundary equation. K137 therefore returns an exact missing-owner result, not
a guessed boundary repair.

## 0. Pre-wave answers

1. **Fork.** Real `Cl(7,7)`, nonzero `kappa_1`, K127's Ricci-flat `T=0`
   local family, and the selected source-native Shiab remain fixed.
2. **Cheapest decisive condition.** Constant fibre rank precedes any attempt
   to construct a smooth system connection. K135/K136 already decide it.
3. **Positive route.** Null base curves survive as geodesic Hamilton flow;
   stratumwise amplitude transport remains constructible on a selected
   background if a smooth constant-rank characteristic module closes.
4. **Claim ceiling.** One cross-stratum five-bundle and a current action-owned
   boundary repair are absent. No universal propagation or domain no-go follows.

## 1. Exact characteristic-rank stratification

Off the spacelike shell divisor, the distortion block is invertible. The exact
`a=17` nonshell control gives full coupled nullity four, exhausted by the
diffeomorphism columns, so its gauge-reduced coupled kernel is zero.

For a null covector, K136 gives the exact nesting

```text
G_diff(4) subset ker A(6) subset ker S_null(9),
```

and hence `dim(ker S_null/G_diff)=5`. At `a=4`, K135's full coupled nullity is
`46485`, so the gauge-reduced dimension is `46481`. At `a=121`, the only
remaining coupled kernel is the four-dimensional diffeomorphism image and the
quotient is zero. The remaining 25 shell rows retain shell-dependent
distortion kernel beyond gauge. Thus even the shell fibres do not share one
rank, much less the null rank five.

This proves

```text
no smooth constant-rank five-class quotient extends through the generic,
null, and complete spacelike-shell stratification.                 (1)
```

Equation (1) does not say that microlocal solutions cannot approach or leave a
rank-change set. It says such passage is a singular transmission problem and
requires additional matching data; ordinary vector-bundle parallel transport
is not defined across it by the frozen symbol alone.

## 2. Hamilton base flow versus amplitude transport

The null characteristic hypersurface is generated by

```text
q(x,xi)=g^{mu nu}(x) xi_mu xi_nu=0.
```

Its Hamilton field

```text
H_q=(partial_xi q) partial_x-(partial_x q) partial_xi
```

projects to null geodesics. This invariant base-flow statement uses the metric
principal factor and survives a null-frame change.

For a matrix or mixed-order system, however, the transported polarization is
not fixed by `H_q`. It uses a smooth characteristic projector and a
subprincipal/Poisson-bracket connection on its image. K136 supplies a fibre
at one frozen null covector. K132 supplies exact tangential counterevidence:
only 11 of 24 normal-null rows in an actual block remain null for a tangential
covector. Those facts prevent promotion of a point kernel to a propagated
constraint or physical-wave bundle.

K127's normal-coordinate two-jet fixes `g`, its first derivative and curvature
at one point. A freely chosen compatible metric third jet changes `nabla R`
and the neighboring connection/curvature coefficients without changing any
K127 pointwise two-jet certificate. Therefore the following data remain
necessary before amplitude transport is evaluable:

- a background on a neighborhood of the bicharacteristic, not one point jet;
- the complete mixed-order subprincipal symbol in one covariant convention;
- a smooth constant-rank characteristic projector on the selected stratum;
- a transmission or gluing law at every rank-changing intersection.

## 3. Boundary-owner audit

The source action is the bulk transgression

```text
I1B=<T,S(F_B+1/2 D_B T+1/3 T^2)>+(kappa_1/2)<T,*T>.
```

Its present serialized form contains no boundary functional and selects no
maximal isotropic trace space. The repository's local calculations use compact
support or fixed boundary values to discard the boundary variation. That is a
variation class, not an added Euler equation, boundary kinetic law, gauge
fixing, spectral projector, or transmission map. The action-owned local Green
concomitant remains degenerate and does not choose any of them.

Consequently K137 finds no current action-owned boundary addition to test.
The honest open alternatives are an explicitly supplied action boundary term,
a selected compact geometry and closed trace domain, a nonlocal anisotropic
projector with adjoint/covariance proofs, or a stratumwise transport and
mode-conversion law derived from a source-global background.

## 4. Reverse scaffold and next gate

```text
R0 a physical reduced state space requires a closed propagated domain.
R1 K135/K136: generic, null and shell kernels have exact unequal ranks.
R2 K137: unequal gauge-reduced ranks obstruct one smooth five-bundle through crossings.
R3 K137: q=0 still owns null-geodesic base flow, not amplitude transport.
R4 K137: K127's point two-jet and bulk I1B own neither neighborhood transport
   coefficients nor a boundary/transmission addition.
R5 K138: build the generic Ricci-flat three-jet subprincipal evaluator and test
   Dencker invariance on one fixed smooth null stratum, with explicit switch
   conditions before any shell or rank-change encounter.
R6 only after R5: supply a gluing/domain owner, then construct KT/BFV and positivity.
```

K138 must remain stratumwise. It should derive the complete covariant
subprincipal coefficient on a generic Ricci-flat three-jet, test whether the
five-dimensional null quotient is invariant under that connection, and state
the first rank-change switch condition. It must not smuggle in a global
background or boundary term. Joe input is not required.

## K138 successor classification

K138 separates the geometric null carrier from the still-untyped
action-specific amplitude law. At the reference null covector and a second
exact rationally rotated null covector, the complete action-derived packet
gives `S_null=-48 ell_n ell_n^T`; the nine-dimensional radical modulo the
four action-owned diffeomorphisms is therefore a Lorentz-covariant rank-five
bundle on a smooth null patch. Moreover `H_q q={q,q}=0`, so a null Hamilton
ray does not drift onto K135's distinct spacelike shells. An exact Ricci-flat
Brinkmann family varies two independent curvature-gradient three-jet
parameters without changing that principal projector. This re-scopes the
present artifact's implication that a three-jet is required before geometric
projector/frame transport can be evaluated. The cross-stratum rank
obstruction remains unchanged. Full Dencker invariance is still open because
the mixed-order Hessian has no declared covariant first-order or
Douglis--Nirenberg reduction and hence no typed invariant subprincipal
five-by-five endomorphism. K139 owns that exact reduction and leakage test.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k137_native_i1b_t0_curved_transport_rank_jet_obstruction_probe.py
```
