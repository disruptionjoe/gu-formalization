---
title: "K1371--K1375 nonlinear Gauss charge-graph closure"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-07"
updated_at: "2026-10-07"
---

# K1371--K1375 nonlinear Gauss charge-graph closure

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE` only because this packet tests the
maximal-compact analytic route left uncertain by SC-META-53. The compact
circle, charge operator, scalar-electrodynamics action and every graph topology
below are repository constructions. They do not identify a source-selected
reduction, observed charge assignment or source observation map.

Scope: an exact obstruction to defining the nonlinear Gauss source on K1366's
energy space, a covariant mixed charge-Sobolev repair, the resulting closed
neutral Gauss surface and positive Coulomb reduction, and smooth conditional
constraint propagation. No global coupled evolution, nonlinear KT resolution,
proper BV-BFV quotient, quantization or GU physical cohomology is constructed.

```gu-typed-objects
result: nonlinear Gauss-source Hminus1 obstruction, covariant first charge-Sobolev repair, closed neutral constraint surface, bounded Coulomb solve, and smooth constraint propagation
carrier: scalar-electrodynamics phase data on T3 with unbounded self-adjoint integer Q and the K1372 covariant mixed graph topology LAYER=toy BRIDGE=maximal-compact-charge-reduction CHIRALITY=N/A
pairing: positive Maxwell electric energy, charge-regularized matter energy and Hminus1-H1 Gauss duality ON=repository_owned_control
real_structure: complex Hilbert charge representation with self-adjoint Q and real Abelian gauge field
grading: spatial Fourier momentum, integer compact charge and BRST ghost degree
action_owner: repository-construction -- the mixed topology is an analytic requirement, not a source action term
target: SC-META-53 conditional nonlinear constraint boundary MAP-TYPE=restriction
```

## Preflight bookend

K1366--K1370 close the free graph form and vacuum-linearized quotient but leave
the nonlinear Gauss map untyped. The first question is therefore earlier and
cheaper than global well-posedness: does the admitted energy make

```text
rho(phi,pi)=e Im <Q phi,pi>
```

a bounded element of `H^-1(T3)` when `Qphi` and `pi` are only in `L2`? If not,
the exact repair must be identified before any global evolution or nonlinear
cohomology claim is even formulable.

The source/action-owned selector remains the strongest independent challenger,
but the released source supplies no generator normalization or observed-carrier
kernel. The Gauss functional question is fully decidable on the repository
control and directly conditions every later KT/BV-BFV step.

## K1371 — bounded energy, divergent Gauss functional

Use normalized Haar measure on `T3` and set

```text
u_N(x)=N^(-3/2) sum_{k in {0,...,N-1}^3} exp(i k.x).
```

Then `||u_N||_2=1` and

```text
||grad u_N||_2^2=3(N-1)(2N-1)/6.
```

Use K1358's actual charge ladder and choose orthonormal vectors
`Qe_{4N}=4Ne_{4N}`, `Qe_4=4e_4`, with phase data

```text
phi_N=(4N)^(-1)u_N e_{4N}+(1/4)e_4,
pi_N=i u_N e_{4N}-i e_4,
A_N=0.
```

All K1366 energy terms stay bounded:

```text
||pi_N||^2=2,
||grad phi_N||^2<3/16,
||Qphi_N||^2=2,
||phi_N||^2=1/16+(16N^2)^-1.
```

The quartic term is bounded too, because

```text
integral |u_N|^4=((2N^2+1)/(3N))^3
```

and hence `integral ||phi_N||^4<1`. But the Gauss density is exactly

```text
rho_N=Im<Qphi_N,pi_N>=|u_N|^2-1,
integral rho_N=0.
```

For nonzero Fourier mode `m` with `|m_j|<N`,

```text
rho_hat_N(m)=product_j (N-|m_j|)/N.
```

Put `r=floor(N/4)`. On the cube `0<max |m_j|<=r`, every coefficient is at
least `27/64`, so

```text
||rho_N||_H^-1^2
 >= ((2r+1)^3-1)(27/64)^2/(1+3r^2),
```

which grows linearly in `N`. Thus the norm grows like at least `sqrt(N)`.
K1366's positive energy does not continuously define the nonlinear Gauss map.
The countersequence is already neutral, so removing the zero mode does not
repair it.

## K1372 — the first sufficient covariant charge-Sobolev repair

Require one covariant spatial derivative of the charged graph variable:

```text
X_Q,A^1={phi: phi,Qphi,D_A phi,D_A(Qphi) in L2}.
```

This is an analytic phase-space topology, not a new action term. Under the
local circle transformation `phi'=exp(i alpha Q)phi`, `A'=A+d alpha`,

```text
D_A'(Qphi')=exp(i alpha Q)D_A(Qphi),
```

so the mixed norm is gauge covariant. The covariant Kato inequality gives

```text
|grad ||Qphi|| | <= ||D_A(Qphi)||.
```

Scalar Sobolev embedding on `T3` therefore yields `Qphi in L6`. For `f in H1`,

```text
|<rho,f>|
 <= |e| ||Qphi||_L6 ||pi||_L2 ||f||_L3
 <= C |e| ||Qphi||_covH1 ||pi||_L2 ||f||_H1.
```

Thus `rho` is a continuous `H^-1` functional on the repaired topology. K1371
shows why the prior `L2` charge graph term does not suffice. This proves a
first sufficient derivative repair, not uniqueness among every fractional or
nonlocal alternative, and it does not prove that the coupled flow propagates
the repaired norm.

## K1373 — closed Gauss surface and positive Coulomb reduction

On phase data with `E,pi in L2` and `phi in X_Q,A^1`, define

```text
G(E,phi,pi)=div E-e Im<Qphi,pi> in H^-1(T3).
```

The divergence is bounded `L2 -> H^-1` and K1372 controls the nonlinear term.
Hence `G` is continuous in the natural covariant graph topology and `G^-1(0)`
is closed. Integrating the constraint restricts to the neutral sector.

On the mean-zero spaces,

```text
div L2(T3;R3)=H^-1_0(T3)
```

with bounded right inverse

```text
R rho=-grad(-Delta)^-1 rho.
```

Fourier mode by Fourier mode, `||Rrho||_2<=||rho||_H^-1`. Every constrained
electric field splits orthogonally as

```text
E=E_T+Rrho,      div E_T=0,
||E||^2=||E_T||^2+||Rrho||^2.
```

This is a closed positive kinematic Gauss reduction. It is not yet a closed
Koszul--Tate resolution or a proper nonlinear BV-BFV quotient.

## K1374 — smooth conditional propagation and BRST compatibility

For a smooth common-core solution of the repository scalar-electrodynamics
equation

```text
D_mu D^mu phi+(m^2+mu Q^2+f(||phi||^2))phi=0,
```

the current `j^mu=e Im<Qphi,D^mu phi>` obeys

```text
partial_mu j^mu=0.
```

The cancellation uses self-adjointness of `Q`, commutation of `Q` with the
covariant derivative and the real `Q^2`/radial potential. Combining continuity
with `partial_mu F^(mu nu)=j^nu` gives

```text
partial_t(div E-j^0)=0.
```

Thus a smooth solution that starts on the Gauss surface stays on it. The
nonlinear Abelian BRST rules `sA=dc`, `sphi=i e c Qphi`, `sc=0` remain nilpotent
on the common core, and the Gauss functional is BRST closed there. These are
conditional identities for an existing smooth solution. They supply neither
global existence nor propagation of the K1372 mixed norm.

## K1375 — admission replay

The bridge census now has 49 rows: 33 satisfied, four conditional, eight
excluded and four missing. Three rows become satisfied: the `H^-1` current
bound on the repaired covariant topology, the closed neutral Gauss surface with
bounded positive Coulomb reduction, and smooth Noether/Gauss propagation on
the common core. One implication is excluded: K1366's energy alone does not
control the nonlinear Gauss functional.

The same four source/physical rows remain missing:

- source-owned selection and normalization on the observed carrier;
- identification with one source-action-derived interacting constraint complex;
- a global nonlinear graph estimate, closed KT resolution, proper BV-BFV
  quotient and positive GU physical Hilbert cohomology; and
- a source-owned observed-state/export map.

K1145/K1150 remain `0/7`. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53
remains `UNCERTAIN`, and LT-SM8/LT-GR6b/RA-F1/AC-F1 remain `NEEDS`.

## Postflight hostile review

The strongest overclaim is that closedness of the Gauss zero set closes the
nonlinear physical quotient. It does not: the repaired topology has not been
propagated globally, the KT differential has not been proved closed/proper on
a solution space, and no source observation map exists. The strongest contrary
construction is K1371 itself: positivity plus `L2` charge coercivity can miss
the dual norm required by the constraint. The weakest seam is the conditional
smooth propagation step; it assumes a solution stays on the common core and
therefore cannot serve as an existence theorem.

The repair is not attributed to the source and does not select `Q`, its sign,
primitive normalization or observed semantics. No source, ledger, canon,
paper, prediction, confirmation or public posture moves.

## Exact next input

The compact route now needs a global a priori estimate that propagates
`D_A(Qphi)` (or a proved weaker sufficient substitute) together with the
Maxwell energy and Gauss constraint. Only after that may one attempt a closed
nonlinear KT resolution, proper BV-BFV quotient and positive physical Hilbert
cohomology. Independently, a source/action-owned observed-carrier selector must
fix the generator and normalization and preserve the same functional domain.
Do not promote kinematic closedness or smooth conditional propagation to a
global nonlinear or GU physical result.
