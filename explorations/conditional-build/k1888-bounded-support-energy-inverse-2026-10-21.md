---
title: "K1888: Bounded-support observation energy and the exact error-budget law"
status: active_research
doc_type: exploration
scripts:
  - tests/channel-swings/k1888_bounded_support_energy_inverse.py
  - tests/channel-swings/k1888_bounded_support_energy_inverse_probe.py
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: bounded-domain minimum preparation energy and compact-source approximation for the fixed conditional observation; no native GU or physical boundary condition
---

# K1888: Bounded-support observation energy and the exact error-budget law

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: bounded support and source energy jointly control observation approximation
carrier: K1840 real16 source and real4 target on an open rectangular box in R3 LAYER=toy CHIRALITY=N/A
pairing: positive source H-L2 and Euclidean target L2 ON=minimal_observation_graph_domain
real_structure: real constant matrices and real exponential charge duals
grading: four charge modes, compatible targets and unobserved source kernel
action_owner: repository-construction -- fixed conditional conservative observation
target: preparation right inverse and source-energy versus target-error tradeoff MAP-TYPE=quotient
```

## 1. The missing boundary condition matters

[K1883](k1883-compact-support-observation-range-2026-10-21.md) gives the
compact smooth range, while
[K1886](k1886-support-bounded-observation-approximation-2026-10-21.md) gives
its fixed-box target-error floor without bounding source energy. This result
supplies the simultaneous energy problem. In particular, **approaching that
floor does not require source energy to diverge**. The compact smooth infimum
can remain unattained while the source norms stay bounded.

Use one of the four actual coordinate types, its positive matrix H, and

```
O = sum_i T_i partial_i + R S1,
Z = stack(T1,T2,T3), S1=24 K T1,
K=diag(1,-1,-1,1), kappa=24R, W(x)=exp(kappa K x1).
```

The signed kappa is retained. On Omega=product_i(-L_i,L_i), L_i>0, let A
be the closure of O initially defined on Cc-infinity(Omega,R16), in the graph
norm ||psi||_H+||O psi||_2. It is a preparation/support domain, not a claimed
physical wall or evolution boundary condition. Its graph core is Cc-infinity
by definition. For smooth sources its zero-normal-flux boundary condition is
`sum_i n_i T_i psi=0`; it does not require every source component to vanish.

The actual flux Gram is

```
G = Z H^-1 Z^T,
gamma=1584/625, Gamma=7182/625, alpha=138/25,
spec(G)={gamma (multiplicity8), Gamma (multiplicity4)}.       (1)
```

All four types give the same G. Its diagonal 4x4 blocks are alpha I, but its
cross blocks are nonzero. For example

```
G12=(1866/625) [[0,0,-1,0],[0,0,0,-1],[1,0,0,0],[0,1,0,0]]. (2)
```

Consequently the whole-space identity O O-dagger=alpha(-Delta+kappa^2)I
from [K1881](k1881-dynamical-minimum-energy-observation-lift-2026-10-21.md)
does **not** license a componentwise scalar Robin realization on this box.

This remains internal conditional mathematics. SC-OP-04 ASSERTS candidate
four-field grammar; SC-MAS-01 and SC-CHI-02 ASSERTS a stylized mass/decoupling
toy. SC-OP-05 and SC-META-53 remain UNCERTAIN. No actual native full20
placement, injection, physical pairing or observed domain has been supplied.
RA-F1, AC-F1, LT-SM8 and source, physics-ledger and canon verdicts are unchanged.

## 2. Exact operator domain and a quantitative inverse

Write

```
D* u = stack((-partial1+kappa K)u, -partial2 u, -partial3 u).
```

The adjoint of A has domain H1(Omega,R4) and is
`A* u=H^-1 Z^T D* u`. To justify the domain rather than assume it, the
distributional adjoint condition gives H^-1 Z^T D* u in L2. The constant
map H^-1 Z^T is injective with a left inverse because Z has full row rank;
therefore all three components of D* u are L2. Since u is L2 and kappa
constant, every first weak derivative is L2. The converse is immediate.

Its closed quadratic form is

```
a(u,v)=<A*u,A*v>_H = integral (D*u)^T G(D*v), domain H1.
N=ker A*={W c:c in R4}, Y0=N-perp in target L2.             (3)
```

The kernel follows from G>0 and D*u=0. The self-adjoint operator associated
with (3), denoted K_Omega=A A*, has interior expression
alpha(-Delta+kappa^2)I. For smooth u its actual natural boundary condition is

```
sum_i n_i [G D*u]_i=0.                                   (4)
```

This follows by integrating (3), or by imposing the source zero-normal-flux
condition on A*u. Cross blocks in G couple target components and tangential
derivatives in (4). At kappa=0, u=cos(pi(x2+L2)/(2L2)) e1 satisfies scalar
Neumann conditions on every face but has a nonzero (4) flux on x1 faces by
(2). This is an explicit counterexample to the scalar-boundary substitution.

The auxiliary form b(u)=||D*u||^2 has exactly the same kernel. In one
dimension, for K-eigenvalue s=+1 or -1, its operator is
`-d^2/dx1^2+kappa^2` with `u'=s kappa u` at BOTH endpoints. Its ground
mode is exp(s kappa x1), with eigenvalue0. Its positive eigenvalues are
`kappa^2+(n pi/(2L1))^2`, n>=1: solve the elementary sine/cosine ODE and
both endpoint equations. Below kappa^2 the hyperbolic endpoint determinant
vanishes only at eigenvalue0; at kappa^2 the linear solution is trivial
unless it is the massless ground mode. Thus no omitted positive low mode
undermines the gap. The other two coordinates have ordinary Neumann
spectra. Tensor products therefore prove, on Y0,

```
b(u)>=nu ||u||^2,
nu=min{kappa^2+pi^2/(2L1)^2, pi^2/(2L2)^2, pi^2/(2L3)^2},
a(u,u)>=gamma nu ||u||^2.                                (5)
```

This is the exact gap of b, and a lower bound for K_Omega; it does not
identify the spectrum of the coupled boundary problem. Formula(5), together
with ||grad u||<=||D*u||+|kappa| ||u||, makes a coercive H1 form on Y0.
For every y in Y0 there is a unique u in H1 intersect Y0 with
`a(u,v)=<y,v>` for all v in H1. Put psi=A*u. The same identity is precisely
the adjoint-domain criterion for psi in Dom A and A psi=y. Thus

```
R_Omega y = A* K_Omega^-1 y,
min_{psi in Dom A, Apsi=y} ||psi||_H^2
       = E_Omega(y):=<y,K_Omega^-1 y>,
||R_Omega y||_H <= ||y||/sqrt(gamma nu).                   (6)
```

The minimizer is unique: it lies perpendicular to ker A, and any other
preimage differs by a kernel vector. The finite-dimensional kernel N accounts
for exactly the four exponential charges, agreeing with K1883. Compact
embedding of H1 into L2 gives a discrete positive spectrum of K_Omega on Y0.
No unproved smooth boundary regularity at box corners is needed for (6).
Translating the box and data together leaves the constant-coefficient operator
and energy unchanged; the same constants use the translated box half-widths.

## 3. Exact compact lifts approach the same minimum energy

For smooth compact y in Y0, the infimum in (6) is unchanged if sources must
be smooth compact and solve O psi=y EXACTLY. This needs more than graph-core
density because an approximating source need not solve the exact equation.

Choose fixed smooth compact scalar bumps rho_i inside the coordinate
intervals, each with integral1. Let ell_i=2L_i and beta_i=||rho_i||_2. The
K1883 tensor primitive applied to h=W y defines F with div F=h. Its three
components satisfy the uniform bound

```
||F||_2 <= C_prim ||h||_2,
C_prim^2 = [ell1(1+beta1 sqrt(ell1))/pi]^2
 + [beta1 ell2 sqrt(ell1)(1+beta2 sqrt(ell2))/pi]^2
 + [beta1 beta2 ell3 sqrt(ell1 ell2)/pi]^2.                 (7)
```

Indeed the successive marginals have norms at most sqrt(ell1)||h|| and
sqrt(ell1 ell2)||h|| by Cauchy-Schwarz. Each zero-integral primitive vanishes
at both ends of its interval, so Dirichlet Poincare bounds its norm by
ell_i/pi times the integrand norm. The triangle inequality bounds the first
two marginal subtractions; the last marginal has integral zero by Q_R(y)=0.
These are norm bounds, not derivative bounds. Smoothness and compactness
follow directly from the primitive construction. Its support can enlarge
inside Omega; no uniform margin from the boundary is asserted.

Use the pointwise minimum-energy flux right inverse
`N_H=H^-1 Z^T G^-1`, so `Z N_H=I` and `N_H^T H N_H=G^-1`.
Then B y=N_H stack(W^-1 F_i) is a compact exact lift with

```
||B y||_H <= exp(2|kappa|L1) C_prim ||y||/sqrt(gamma).     (8)
```

Compact-support divergence inverses are standard; nearby context is
[Costabel and McIntosh, Bogovskii and regularized Poincare integral operators](https://arxiv.org/abs/0808.2614).
The explicit rectangular proof above supplies the present weighted constants;
no theorem about a different domain is imported and no novelty is claimed.

The constant depends on the fixed box and bumps, but NOT on the support
margin or on y. This deliberately loose bound is sufficient for the density
argument; it is not advertised as the best massive inverse bound.

Let psi*=R_Omega y. By the definition of A choose compact smooth psi_n
converging to psi* in graph norm. The residuals e_n=y-O psi_n are compact
smooth, charge-zero, and tend to0 in L2. Thus
`psi_n+B e_n` are exact compact lifts and converge to psi* in source energy
by (8). This proves equality of the two infima. The minimum need not be
attained by a compact smooth source. For nonsmooth L2 y only the graph-domain
exact lift and compact APPROXIMATION are asserted.

## 4. The full support-energy-error law

[K1869](k1869-wall-observation-finite-energy-range-2026-10-20.md), sections2
and6, already supplies closed-operator minimal lifting and penalized spectral
approximation. That calculus is reused here. The new obligation is the actual
coupled bounded-support realization, its gap, and transfer of its energy
infima to compact smooth sources; K1869's massless planar-wall Gaussian has a
different infrared obstruction and diverging preparation energy.

For arbitrary y in target L2, let r=P_N y and z=y-r. K1886 computes r from
the four charges; on a centered cube `||r||^2=||q||^2/g`. Let positive
orthonormal eigenpairs of K_Omega on Y0 be (lambda_j,e_j), z_j=<z,e_j>,
and let B>=0 be a budget on the SOURCE NORM (energy is B^2). Define

```
E*=sum_j |z_j|^2/lambda_j <= ||z||^2/(gamma nu).           (9)
```

If B^2>=E*, the infimum of ||O psi-y|| over compact smooth sources with
||psi||_H<=B is exactly ||r||. For B^2<E* and B>0 there is a unique t>0
such that

```
sum_j lambda_j |z_j|^2/(lambda_j+t)^2 = B^2.             (10)
```

The exact squared error infimum is

```
||r||^2 + sum_j t^2 |z_j|^2/(lambda_j+t)^2,               (11)
```

with graph-domain minimizer `psi_t=A*(K_Omega+t)^-1 z`.
At B=0 the only source is0 and the error is ||y||; if z=0 the charge
floor already equals ||y|| for every budget. Equation(10) is strictly
decreasing in t for nonzero z, tending from E* to0, so no root choice is
ambiguous.

For proof, minimize `||Apsi-z||^2+t||psi||_H^2` in the orthogonal source
modes. Completion of squares gives both psi_t and the lower bound

```
||Apsi-y||^2 >= ||r||^2
 + sum_j t |z_j|^2/(lambda_j+t) - t B^2.                  (12)
```

At (10) this equals (11). For t=0 use (6). Compact graph-core approximants
converge to each minimizer in both source norm and observed target. Scaling
an approximant by min(1,B/||psi_n||_H) enforces the budget exactly and tends
to the identity for every nonzero minimizing norm. Thus the same infimum
holds for the compact smooth class. It need not be attained in that class.
If a budget below sqrt(E*) could reach the charge floor as an infimum,
weak compactness of its source ball and weak closedness of the graph would
produce a lift of z with smaller energy than (6), a contradiction.

In particular B>=||z||/sqrt(gamma nu) is an explicit sufficient budget for
approaching K1886's floor. For nonzero-charge smooth compact y the best
compact target error remains unattained, exactly as K1886 proves, but it can
be approached with this finite budget. Nonattainment and energy blow-up are
different statements. Equations(10)--(12) are an exact variational law;
explicit numerical evaluation for a chosen y still requires its coupled
boundary spectral data, not the auxiliary scalar eigenvalues from (5).

## 5. A massive whole-space bound does not survive fixed support uniformly

Take a cube L1=L2=L3=L. Formula(5) gives gap at least
`gamma pi^2/(2L)^2` for EVERY R. Conversely use

```
u(x)=W(x)c cos(pi(x2+L)/(2L)).
```

It lies in Y0, D1*u=D3*u=0, and only its second derivative component
contributes to the form. Since G22=alpha I, its Rayleigh quotient is
`alpha pi^2/(2L)^2`. A form test need not satisfy the operator's boundary
condition. Therefore the best bounded-support inverse norm obeys

```
2L/(pi sqrt(alpha)) <= ||R_Omega|| <= 2L/(pi sqrt(gamma)). (13)
```

Both inequalities hold also for R=0. This worst-case norm grows linearly
with box size even at nonzero mass. The whole-space minimum inverse bound
`1/(24|R| sqrt(alpha))` cannot be transplanted to all support-constrained
compatible targets. The offending target modes depend on the box and can
concentrate near a face as mass grows; this does not contradict whole-space
surjectivity or assert that each fixed compact target has diverging cost.
Nor does (13) give the exact coupled-domain spectral gap.

## 6. Repaired frames, controls and remaining boundary

At a fixed time K1879's repaired O_theta=U O V^-1 has orthogonal target
frame U and H-unitary source frame V. Smooth frame multiplication preserves
compact support and is isometric in the two L2 norms; conjugating the graph
core transports its closure. Hence A_theta=U A V^-1,
K_theta=U K_Omega U^-1, the charges use W U^-1y, and (6)--(13) hold
with the transported domain. This is an instantaneous preparation statement.
No fixed-box evolution invariance, pure-mass rotating repair or physical
boundary condition is asserted.

Exact algebra checks reconstruct all four flux Grams, their positive spectral
projectors, weighted right inverses, cross-boundary countercontrols, and the
coefficient identities behind the interior operator. An independent probe
checks rows and rational quadratic forms, elementary scalar eigenfunctions,
compact tensor primitives, and finite-dimensional energy/error duality.
Planted coefficient/adjoint/normalization/boundary and arithmetic faults are
separate from report/pin faults; the clean baseline runs first. Analytic
arguments in sections2--5 carry the continuum/domain and density claims.
Finite controls do not certify infinite-dimensional spectral completeness.

The producer passes 55 exact algebra groups with 5 input pins. The independent
probe passes 294 mathematical controls and 9 report/pin checks, then rejects
6 actual mathematical faults, 2 serialized-coefficient faults and 5 report/pin
faults with explicit assertion failures after its clean baseline. Neither
the producer nor probe had a failed verification attempt in this packet.

The preflight favored the coupled form over an imported scalar Robin spectrum,
and the postflight checked the graph-core correction, unattained-versus-
unbounded distinction, and budget endpoint scaling. No source/physics/canon
verdict changes, physical causality result, novelty claim, external specialist
acceptance or proof-assistant certification is supplied. Further quantitative
work can solve the actual coupled boundary spectrum for a specified target;
repeating whole-space Fourier recovery or fixed-support charge projection
would not answer that next question.
