---
title: "K1376--K1380 charge-lift propagation boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-07"
updated_at: "2026-10-07"
---

# K1376--K1380 charge-lift propagation boundary

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
circle, charge operator, scalar-electrodynamics action and every lifted graph
topology below are repository constructions. They do not identify a
source-selected reduction, observed charge assignment or source observation
map.

Scope: an exact free-flow obstruction to K1372's one-sided topology, the
conserved full first charge lift that repairs it, a conditional coupled
Gronwall estimate, and a concentration obstruction to closing that estimate
from the original conserved energy. No global coupled evolution, nonlinear KT
resolution, proper BV-BFV quotient, quantization or GU physical cohomology is
constructed.

```gu-typed-objects
result: free noninvariance of the one-sided mixed topology, exact conserved first charge lift, conditional coupled Gronwall estimate, and base-energy coefficient obstruction
carrier: scalar-electrodynamics phase data on T3 with unbounded self-adjoint integer Q and the full first charge-lift graph domain LAYER=toy BRIDGE=maximal-compact-charge-reduction CHIRALITY=N/A
pairing: positive charge-lift graph energy plus Maxwell L2 energy ON=repository_owned_control
real_structure: complex Hilbert charge representation with self-adjoint Q and real Abelian gauge field
grading: spatial Fourier momentum, integer compact charge and BRST ghost degree
action_owner: repository-construction -- the lifted graph energy is an analytic hierarchy, not a source action term
target: SC-META-53 conditional nonlinear propagation boundary MAP-TYPE=restriction
```

## Preflight bookend

K1372 proves that `D_A(Qphi)` is sufficient to define the Gauss source at one
time, but it imposes no corresponding charge condition on the canonical
momentum. A functional topology is not yet a dynamical phase space. The
cheapest route-changing test is therefore the free propagator of K1367, before
any nonlinear Maxwell estimate.

The source/action-owned selector remains the strongest independent challenger,
but no released source datum fixes the compact generator, normalization or
observed carrier. The free invariance question is exact, reusable and directly
conditions every later global KT/BV-BFV claim.

## K1376 — the one-sided topology fails even for the free flow

At `A=0`, write

```text
Omega^2=-Delta+m^2+mu Q^2,       mu>0.
```

Choose the K1358 charge eigenvector `Qe_(4N)=4N e_(4N)`, spatial momentum
`k_N=(4N,0,0)`, and initial data

```text
phi_N(0)=0,      pi_N(0)=exp(i k_N.x)e_(4N).
```

The K1372 fixed-time norm is uniformly bounded at zero: `Qphi_N=0` and
`||pi_N||_2=1`. With

```text
omega_N=sqrt((4N)^2+m^2+mu(4N)^2),
t_N=pi/(2omega_N),
```

the free solution gives

```text
||grad Qphi_N(t_N)||_2=(4N)^2/omega_N
  ~ 4N/sqrt(1+mu).
```

Since `t_N -> 0`, no strongly continuous free evolution acts on the one-sided
K1372 phase topology. The obstruction is not the Gauss functional theorem;
it is the missing charged momentum and the next charge graph level.

## K1377 — the exact free first charge lift

Set `psi=Qphi`. Because `Q` commutes with the free operator, `psi` satisfies
the same charge-regularized wave equation. Spectral calculus conserves

```text
E_Q = ||Qpi||_2^2 + ||grad Qphi||_2^2
      + m^2||Qphi||_2^2 + mu||Q^2phi||_2^2
    = ||Qpi||_2^2 + ||Omega Qphi||_2^2.
```

Thus the invariant free phase domain is

```text
Qphi in H1 intersect L2(D(Q)),       Qpi in L2.
```

This controls K1372's spatial mixed norm and supplies the missing charged
momentum. It is a full first charge lift, requiring `Q^2phi` as well as
`Qpi`; K1366's base energy does not imply it.

## K1378 — conditional coupled propagation

For a smooth common-core solution set `psi=Qphi`. The radial multiplier and
covariant derivative commute with `Q`, so

```text
D_mu D^mu psi+(m^2+mu Q^2+f(||phi||^2))psi=0.
```

The lifted current is `j_Q^a=e Im<Qpsi,D^a psi>`. The covariant energy
identity is

```text
dE_Q,f/dt = integral E.j_Q
             +(1/2) integral partial_t f ||psi||^2.
```

The ordinary Maxwell energy cancels the original matter current, not this
lifted one. For `mu,m>0` and `f>=0`, Cauchy--Schwarz gives

```text
dE_Q,f/dt
 <= C_(mu,m)(|e| ||E||_infinity+||partial_t f||_infinity) E_Q,f.
```

Hence the lift propagates by Gronwall whenever the displayed coefficient is
in `L1_t`. This is an exact conditional a priori estimate, not a derivation of
that spacetime integrability from the conserved base energy.

## K1379 — the base energy does not close the estimate

For the real normalized Dirichlet square and cube

```text
u_N=(2N+1)^(-1) sum_(k2,k3=-N)^N exp(i(k2 x2+k3 x3)),
v_N=(2N+1)^(-3/2) sum_(k in {-N,...,N}^3) exp(i k.x),
```

one has `||u_N||_2=||v_N||_2=1`,
`||u_N||_infinity=2N+1` and
`||v_N||_infinity=(2N+1)^(3/2)`. Thus
`E_N=u_N(x2,x3)e_1` is divergence-free, has fixed Maxwell energy and
unbounded `L-infinity` norm.
Independently take real aligned charge-four data

```text
phi_N=e_4,       pi_N=v_N e_4.
```

Their base momentum, mass and charge-regularizer energies are bounded and
their Gauss density vanishes. For the cubic radial coefficient
`f(s)=lambda s`, however,

```text
partial_t f(||phi||^2)|_(t=0)=2lambda v_N,
```

whose `L-infinity` norm diverges. Therefore neither coefficient in K1378 is
controlled by the original energy plus Gauss. This does not exclude a weaker
Strichartz, Morawetz, null-form or higher-regularity spacetime closure.

## K1380 — admission replay

The bridge census now has 53 rows: 34 satisfied, five conditional, ten
excluded and four missing. The exact free first charge lift is satisfied; the
coupled Gronwall estimate is conditional; and two implications are excluded:
the one-sided K1372 topology is not a free invariant phase space, and the base
energy does not control K1378's `L-infinity` coefficient norm.

The same four source/physical rows remain missing: source-owned selection and
normalization; identification with one source action; a closed fully coupled
global nonlinear BV-BFV quotient with positive physical Hilbert cohomology;
and a source-owned observed-state/export map. K1145/K1150 remain `0/7`.

## Postflight hostile review

The strongest overclaim is that the exact free lift proves a global coupled
theorem. It does not: the lifted Maxwell exchange has no cancellation in the
base energy, and the required endpoint coefficient norms are not controlled.
The strongest contrary construction is K1379's neutral concentration family.
The weakest seam is whether a weaker dispersive spacetime norm can replace the
displayed `L1_t L-infinity_x` condition; this packet neither constructs nor
excludes that route.

The graph hierarchy is not attributed to the source and selects neither `Q`,
its sign, primitive normalization nor observed semantics. No source, ledger,
canon, paper, prediction, confirmation or public posture moves.

## Exact next input

Either prove a global higher-regularity or dispersive estimate that propagates
the first charge lift in the coupled Maxwell system, or find a weaker
gauge-covariant topology that still controls the Gauss source and closes under
the flow. Only then attempt a closed nonlinear KT resolution and proper
positive BV-BFV quotient. Independently, a source/action-owned observed-
carrier selector must fix the generator and normalization and preserve the
same domain.
