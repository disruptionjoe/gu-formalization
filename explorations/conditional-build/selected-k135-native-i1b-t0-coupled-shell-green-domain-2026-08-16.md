---
title: "Selected-K135 native I1B T=0 coupled shell, Green, and domain classification"
status: active_research
doc_type: exact_coupled_metric_distortion_shell_null_chain_green_and_domain_gate
created: "2026-08-16"
registry: lab/process/selected-k135-native-i1b-t0-coupled-shell-green-domain.json
probe: tests/channel-swings/selected_k135_native_i1b_t0_coupled_shell_green_domain_probe.py
grade: "K135 COMPOSES THE ACTION-OWNED METRIC CURVATURE MAP AND OPERATIVE FINITE-SYMBOL ADJOINT WITH K134'S COMPLETE HERMITIAN DISTORTION PENCIL. THE METRIC IMAGE CLOSES IN AN EXACT 112D INVARIANT PACKET. IT MEETS SHELL KERNELS ONLY AT SQUARED RADII 4 AND 121: SIX METRIC DIRECTIONS PAIR AT 4 AND ONE AT 121. THE FULL COUPLED NULLITIES AT ALL 27 POSITIVE SHELLS REMAIN NONZERO; AT 4 THE NULLITY IS 46485, AT 121 IT IS THE FOUR METRIC DIFFEOMORPHISM DIRECTIONS, AND ELSEWHERE IT IS THE DISTORTION MULTIPLICITY PLUS FOUR. ON THE NULL PACKET, LOCAL K C_1 POWER RANKS ARE 90,48,6,3,0, BUT -A* C^-1 A HAS ONLY A FREQUENCY-INDEPENDENT RANK-ONE COEFFICIENT: A ANNIHILATES EVERY POSITIVE JORDAN-DEGREE CONTRIBUTION. THE COUPLED NULL METRIC SYMBOL THEREFORE HAS RADICAL NINE. METRIC COUPLING DOES NOT REMOVE THE SPACELIKE SHELL OBSTRUCTION OR SELECT A CLOSED DOMAIN, BOUNDARY POLARIZATION, KT/BFV QUOTIENT, INVERSE OR PHYSICAL COHOMOLOGY."
target_claim: K134_NEXT_GATE__COMPOSE_METRIC_CURVATURE_BLOCK_ON_SPACELIKE_SHELLS_AND_NULL_JORDAN_CHAINS
target_verdict: COUPLED_ALL_27_SPACELIKE_SHELLS_REMAIN_SINGULAR__METRIC_PAIRS_ONLY_RADII4_AND121__NULL_SCHUR_FREQUENCY_INDEPENDENT_RANK1__NULL_METRIC_RADICAL9__DOMAIN_STILL_UNSELECTED
canon_verdict_change: none
---

# Selected-K135 native I1B T=0 coupled shell, Green, and domain classification

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> first-transgression, real `Cl(7,7)`, mixed-order Hermitian Fourier-symbol,
> Green-form and ultrahyperbolic-domain calculation. Ordinary Einstein,
> Higgs/VEV, family-index, chirality, anomaly, symmetry-breaking and familiar
> particle-spectrum constructions do not adjudicate it without an explicit
> typed bridge. Read `lab/methods/source-native-comparator-routing.md` before
> reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: K135 binds the selected displayed `comm/symi/symi` `I1B` Hessian at
K127's local Ricci-flat `T=0` fixed-boundary germ, on the settled real
`Cl(7,7)` carrier. The adjoint used below is the operative finite-symbol action
adjoint. It does not select a global operator domain or boundary adjoint.

## Result in plain English

K134 found 27 exact spacelike singular radii in the complete distortion block.
K135 now places the actual ten metric variables back into the same invariant
basis. The metric curvature image occupies an exact 112-dimensional distortion
packet and has spacelike rank six.

Only two shell sectors meet that image:

```text
a=4:   local distortion nullity 45, pairing rank 6,
       local coupled nullity 43, full coupled nullity 46485;
a=121: local distortion nullity 1, pairing rank 1,
       local coupled nullity 4, full coupled nullity 4.            (1)
```

At `a=81`, the local three-dimensional shell kernel is orthogonal to the
metric image. At every other radius the metric packet is invertible while the
shell lies in the other invariant blocks. Thus the full coupled shell nullity
is the distortion multiplicity plus the four metric diffeomorphism directions,
except for the two adjustments in (1). Every one of the 27 shells remains
singular. In particular, coupling lifts the unique `a=121` distortion mode but
cannot lift the action-owned diffeomorphism radical.

On the null metric-support packet, with `L=K C_1(n)`, the exact power ranks are

```text
rank(L,L^2,L^3,L^4,L^5)=(90,48,6,3,0).              (2)
```

For nonzero `kappa_1`, the distortion inverse is the finite Neumann polynomial
through degree four. But composing with the metric block gives

```text
-A* C_null(rho)^(-1) A = S_0,
rank(S_0)=1,
[rho^j](-A* C_null(rho)^(-1) A)=0 for j=1,2,3,4.    (3)
```

So the metric effective symbol does not inherit the distortion block's
fourth-order growth: `A` annihilates all positive Jordan-degree contributions.
The price is not a regular metric block. Its rank is only one on the ten
metric variables, leaving a nine-dimensional null metric-symbol radical. Four
directions are action-owned diffeomorphisms; K135 does not classify the other
five as gauge or physical modes.

## 0. Pre-wave answers

1. **Fork.** The calculation stands on settled `REAL-CLIFFORD-FORM=Cl(7,7)`
   and does not settle `SIGNATURE-AMBIENT` or port to `Cl(9,5)`.
2. **Search dimension.** K134's `56/56/49` exhaustive block census is reused.
   Only the exact invariant packet meeting the metric image is recomputed;
   no dense `229386` matrix is formed.
3. **New unowned object.** None. `A`, `A*`, `C_1`, and `K` are all inherited
   from the selected action germ. A global boundary adjoint or domain is not
   supplied.
4. **What dies or is re-scoped.** The possibility that metric coupling removes
   every K134 shell dies. The stronger claim that the metric Schur block must
   inherit fourth-order null growth also dies. Neither result creates a closed
   realization, positivity, gauge tower, or cohomology.

## 1. Exact spacelike shell census

For positive `x=kappa_1/rho`, the full coupled nullities are:

```text
a : nullity
1:316, 2:82, 3:290, 4:46485, 5:1291, 6:1720,
7:1720, 8:1291, 9:2006, 10:290, 11:82, 12:17,
13:5, 16:1720, 25:1720, 36:1291, 48:17, 49:719,
64:290, 81:82, 88:82, 100:17, 120:290, 121:4,
144:719, 160:1291, 168:1720.                        (4)
```

The negative shells have the same nullities by the pencil symmetry. Shell
multiplicity is not gauge dimension. Equation (4) is the kernel dimension of
the complete finite coupled Hessian at that shell, including the four metric
diffeomorphism directions.

The exceptional interaction is structural. At `a=4`, six metric combinations
pair with six of 45 local distortion-kernel directions. Adding ten metric
variables therefore changes local nullity from 45 to 43 and full nullity by
minus two. At `a=121`, one metric combination pairs with the unique local
distortion mode; after that pair becomes nondegenerate, only the four
diffeomorphism directions remain.

## 2. Green and domain disposition

The action owns the finite-symbol Hermitian pairing in this calculation, but
not a boundary polarization or one closed realization across the
ultrahyperbolic characteristic geometry. Three facts are now simultaneous:

1. every fixed nonzero `kappa_1` still meets coupled spacelike singular shells
   after frequency rescaling;
2. the null distortion inverse still has fourth-order frequency growth, even
   though its metric Schur projection cancels all positive powers; and
3. the null metric effective symbol has rank one and radical nine.

Thus neither the full coupled inverse nor a regular reduced metric inverse is
selected. A restricted microlocal or boundary-value domain might control or
exclude some shells, but it must be supplied by action-compatible analytic
data and tested against the Green form. Deleting the shell frequencies is not
a domain construction.

Only the four metric diffeomorphism columns are action-owned Noether data at
this germ. The remaining shell kernels and five additional null metric-symbol
radical directions are not promoted to distortion gauge, Koszul--Tate
generators, BFV edge modes, or physical states.

## 3. Reverse scaffold and next gate

```text
R0 positive physical cohomology, if derived, requires a closed domain.
R1 K127--K132: local T0 coupled Hessian and all-grade symbol.
R2 K133--K134: no distortion complex; exact Hermitian shell/Jordan census.
R3 K135: metric coupling leaves all 27 spacelike shells singular.
R4 K135: null Schur is frequency-independent rank one with radical nine.
R5 K136: classify action-compatible microlocal/boundary realizations across
   the shell divisor and null radical, or prove the available local covariant
   boundary classes cannot give a closed Fredholm/Green realization.
R6 only after a domain: construct the actual KT/BFV reduction and positivity.
```

K136 must distinguish an honest restricted domain from deletion of bad
frequencies. It must type which of the five non-diffeomorphism null metric
directions are propagated constraints, boundary data, or genuine
characteristics using tangential and lower-order coefficients. No ledger,
canon, public posture, particle, phenomenology, or GU truth-status claim
changes. Joe input is not required.

## K136 successor classification

K136 exactly resolves the frozen null quotient: four action-owned
diffeomorphisms sit inside a six-dimensional `ker A`, whose other two classes
are TT plus/cross; three further `A`-visible compensated classes complete the
nine-dimensional Schur radical. The five quotient classes are finite-symbol
characteristics only. The non-gauge `a=4` shell kernel also produces
approximate-shell sequences, obstructing the frozen translation-invariant
whole-space Fredholm route and unbounded finite-order local-boundary repairs.
Compact, nonlocal, anisotropic, different-background, and new action-boundary
routes remain outside that theorem. K137 now owns full curved subprincipal
transport on the five-class quotient or an explicit action-owned boundary
addition.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k135_native_i1b_t0_coupled_shell_green_domain_probe.py
```
