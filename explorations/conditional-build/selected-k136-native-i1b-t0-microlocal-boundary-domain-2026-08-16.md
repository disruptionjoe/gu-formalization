---
title: "Selected-K136 native I1B T=0 microlocal characteristic and local-domain obstruction"
status: active_research
doc_type: exact_null_characteristic_quotient_shell_weyl_sequence_green_boundary_domain_gate
created: "2026-08-16"
registry: lab/process/selected-k136-native-i1b-t0-microlocal-boundary-domain.json
probe: tests/channel-swings/selected_k136_native_i1b_t0_microlocal_boundary_domain_probe.py
grade: "K136 EXACTLY QUOTIENTS K135'S NINE-DIMENSIONAL NULL METRIC RADICAL. FOUR DIRECTIONS ARE THE ACTION-OWNED DIFFEOMORPHISM IMAGE. THE FIVE GAUGE-REDUCED CLASSES SPLIT INTO TWO A-NULL TRANSVERSE-TRACELESS CLASSES AND THREE A-VISIBLE COMPENSATED MIXED CLASSES WHOSE DISTORTION RESPONSE IS ISOTROPIC FOR THE EFFECTIVE SCHUR FORM. ALL FIVE ARE FINITE-SYMBOL CHARACTERISTICS, NOT YET PROPAGATED CURVED-BACKGROUND SOLUTIONS. K135'S NON-GAUGE SPACELIKE SHELL KERNELS PRODUCE NORMALIZED APPROXIMATE-SHELL SEQUENCES, SO THE FROZEN TRANSLATION-INVARIANT WHOLE-SPACE REALIZATION IS NOT BOUNDED BELOW MODULO A FINITE KERNEL AND IS NOT FREDHOLM ON THE DECLARED SOBOLEV SCALE. THE SAME INTERIOR SEQUENCES DEFEAT LOCAL BOUNDARY TRACE CONDITIONS ON UNBOUNDED DOMAINS. EVERY CONORMAL IS PRINCIPAL-CHARACTERISTIC AND THE ACTION GREEN FORM IS DEGENERATE, SO THE ORDINARY ELLIPTIC CALDERON AND NONCHARACTERISTIC CAUCHY ROUTES ARE UNAVAILABLE. NO UNIVERSAL CLAIM IS MADE AGAINST EXTERNALLY SUPPLIED NONLOCAL, ANISOTROPIC, COMPACT-DOMAIN, OR DIFFERENT-BACKGROUND REALIZATIONS."
target_claim: K135_NEXT_GATE__CLASSIFY_FIVE_NULL_METRIC_CLASSES_AND_ACTION_COMPATIBLE_LOCAL_GREEN_REALIZATIONS
target_verdict: NULL_QUOTIENT_4_GAUGE_PLUS_2_A_NULL_TT_PLUS_3_A_VISIBLE_COMPENSATED__FROZEN_WHOLE_SPACE_AND_UNBOUNDED_LOCAL_BOUNDARY_FREDHOLM_ROUTES_OBSTRUCTED__CURVED_SUBPRINCIPAL_PROPAGATION_STILL_OPEN
canon_verdict_change: none
---

# Selected-K136 native I1B T=0 microlocal characteristic and local-domain obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> first-transgression, real `Cl(7,7)`, mixed-order Hermitian Fourier-symbol,
> Green-form and ultrahyperbolic-domain calculation. Ordinary Einstein,
> Higgs/VEV, family-index, chirality, anomaly, symmetry-breaking and familiar
> particle-spectrum constructions do not adjudicate it without an explicit
> typed bridge. Read `lab/methods/source-native-comparator-routing.md` before
> reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: K136 binds the selected displayed `comm/symi/symi` `I1B` Hessian at
K127's local Ricci-flat `T=0` fixed-boundary germ, on the settled real
`Cl(7,7)` carrier. Its Fredholm obstruction applies to the frozen
translation-invariant whole-space realization and to unbounded-domain
realizations whose boundary condition is a local trace condition and whose
interior agrees with that frozen operator. It does not classify every compact,
nonlocal, anisotropic, or externally supplied realization.

## Result in plain English

K135 left nine null metric directions after eliminating the invertible
distortion block at nonzero `kappa_1`. K136 identifies them exactly. In the
ordered metric basis

```text
(00,01,02,03,11,12,13,22,23,33),
```

the four null-covector diffeomorphisms span `G`. The kernel of the original
metric-to-distortion map `A` is exactly

```text
ker A = G plus span(h_11-h_22, h_12),                 (1)
```

so the two extra `A`-null classes are the transverse-traceless plus and cross
directions. The Schur radical is three dimensions larger:

```text
ker S_null = ker A plus span(
  h_11+h_22,
  h_01-h_13,
  h_02-h_23).                                        (2)
```

The last three directions have independent nonzero `A` images, but those
images are isotropic after composition with the exact distortion inverse.
They are therefore compensated mixed metric-distortion characteristics, not
new gauge transformations. After quotienting only the action-owned `G`, the
null symbol has exactly five characteristic classes: two `A`-null TT and three
`A`-visible compensated classes.

This is a symbol classification, not a propagation theorem. K132 already
exhibits a normal-null row made live by a tangential coefficient. The complete
curved-background subprincipal transport on these five quotient classes has
not been constructed, so K136 does not call them five physical waves, five
constraints, five boundary modes, or five cohomology generators.

## 0. Pre-wave answers

1. **Fork.** The result stays on real `Cl(7,7)`, nonzero `kappa_1`, and the
   selected frozen K127 germ. It does not settle the ambient-signature fork.
2. **Boundary object.** The action supplies a formal degenerate Green class,
   not a selected maximal isotropic trace subspace, Krein majorant, graph
   closure, or pseudodifferential projector.
3. **Cheapest decisive condition.** A non-gauge shell kernel plus a continuous
   symbol is enough to construct normalized approximate-shell sequences; no
   large matrix inverse or guessed boundary ansatz is needed.
4. **Claim ceiling.** The ordinary frozen whole-space Fredholm route and the
   corresponding unbounded local-boundary route close. Exotic or externally
   supplied realizations remain open at their exact additional assumptions.

## 1. Exact five-class quotient

For the null covector `n=(1,0,0,1)`, K135's Schur matrix is rank one and its
radical is the hyperplane

```text
h_00 - 2 h_03 + h_33 = 0.                            (3)
```

The four vectors `n_(mu xi_nu)` have rank four and lie in both `ker A` and
`ker S_null`. Adding the two TT representatives gives rank six and exhausts
`ker A`. Adding the three representatives in (2) gives rank nine and exhausts
`ker S_null`; their `A` images have rank three. Thus the exact nested dimensions
are

```text
dim G = 4,
dim ker A = 6,
dim ker S_null = 9,
dim(ker A/G) = 2,
dim(ker S_null/ker A) = 3,
dim(ker S_null/G) = 5.                               (4)
```

The split in (4) is frame-representative language for this null direction.
The invariant content is the nested quotient dimension and whether `A`
annihilates the class. No positive norm or physical polarization has been
selected.

## 2. Shell-neighborhood obstruction

Fix nonzero `kappa_1` and one of K135's spacelike shell covectors with a
non-gauge kernel; `a=4` is sufficient. Let `P(xi)` be the frozen coupled
Hermitian symbol and choose normalized Fourier packets `u_epsilon` supported
in shrinking disjoint patches around that shell, polarized along corresponding
least-singular vectors. Continuity of `P` gives

```text
norm(P(D) u_epsilon) <= C epsilon norm(u_epsilon),    (5)
```

while the packets can be chosen weakly null and mutually orthogonal. The
kernel polarization at `a=4` contains distortion shell directions beyond the
four metric diffeomorphisms, so gauge quotienting does not remove (5).

Equation (5) rules out a positive lower bound modulo a finite-dimensional
kernel. Hence the frozen translation-invariant whole-space realization has
non-closed range at zero and is not Fredholm on the declared mixed Sobolev/
Douglis--Nirenberg scale. Merely requiring the Fourier transform to vanish on
the exact measure-zero shell does nothing: the shrinking neighborhoods still
give (5). Excluding a full neighborhood is a nonlocal spectral restriction,
not a boundary condition derived from the local action.

On an unbounded domain, translate compactly localized versions of the same
packets arbitrarily far from the boundary. Any finite-order local trace
condition is then invisible to the interior sequence. Such a condition cannot
repair this essential obstruction. This argument does not cover a compact
domain or an externally chosen nonlocal/anisotropic projector, and K136 makes
no claim about those cases.

## 3. Green and boundary classification

Three independent facts prevent the current packet from selecting an ordinary
local covariant realization:

1. K130 proves every nonzero conormal is characteristic on the tracked
   distortion carrier, so no ordinary noncharacteristic Cauchy hypersurface
   is available.
2. The action Green form has radicals `196/196/198` on the tracked causal
   strata and rank jump at the null stratum, so it does not itself select a
   symplectic trace space or Lagrangian polarization.
3. K135's full coupled shell divisor produces the approximate sequences (5),
   so an ordinary elliptic Calderon/local-boundary Fredholm repair is not
   available on the frozen unbounded model.

The honest escape routes all require new data: a fully evaluated curved
subprincipal transport, an action-owned gauge fixing and boundary term, a
specified compact geometry with its trace domain, or an explicitly nonlocal
anisotropic projector with compatibility and adjoint tests. None is licensed
by the finite-symbol packet alone.

## 4. Reverse scaffold and next gate

```text
R0 positive physical cohomology, if derived, requires a closed reduced domain.
R1 K130-K132: every conormal characteristic; Green radical stratified.
R2 K133-K135: exact Hodge pencil, 27 coupled shells, null Schur radical nine.
R3 K136: radical/G = five = two A-null TT plus three compensated mixed classes.
R4 K136: approximate-shell sequences obstruct frozen unbounded local Fredholm routes.
R5 K137: evaluate the complete curved-background subprincipal/Hamilton transport
   on the five-class quotient and test smooth propagation through null/shell
   crossings, or supply and verify an explicit action-owned boundary addition.
R6 only after R5: construct the actual KT/BFV reduction, positivity, and states.
```

K137 must not infer propagation from normal nullity. It must calculate the
subprincipal connection and tangential compatibility on the five quotient
classes, including shell crossings and the null rank jump. If the needed
action-owned coefficients or boundary term are absent, that absence is the
result. Joe input is not required.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k136_native_i1b_t0_microlocal_boundary_domain_probe.py
```

## K137 successor classification

K137 applies the constant-rank test before constructing a transport
connection. Modulo the four action-owned diffeomorphisms, the coupled kernel
has dimension zero generically off shell, five on the null Schur stratum,
`46481` at `a=4`, zero at `a=121`, and shell-dependent positive dimension on
the remaining shells. These fibres cannot be one smooth rank-five bundle
through the crossings. The null scalar factor still owns geodesic Hamilton
base flow, but K127's point Ricci-flat two-jet does not select the complete
amplitude connection along a neighborhood, and the displayed bulk `I1B` owns
no boundary functional or transmission law. K138 must build the generic
Ricci-flat three-jet subprincipal evaluator and test the five-class quotient
on one fixed smooth null stratum before any crossing or domain claim.
