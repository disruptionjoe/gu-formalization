---
title: "K1891: Massive slab observation with compatible conservative domains"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional four-type system, selected slab boundaries and static normal mass profiles; no native GU or physical boundary selection
scripts:
  - tests/channel-swings/k1891_massive_boundary_observation.py
  - tests/channel-swings/k1891_massive_boundary_observation_probe.py
---

# K1891: Massive slab observation with compatible conservative domains

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
result: conservative massive observation domains with exact spectrum and recovery limits
carrier: real16 source complexified by tangential Fourier transform to complex4 target LAYER=toy CHIRALITY=N/A
pairing: source H-positive energy and target Euclidean pairing ON=specified_closed_slab_domains
real_structure: real coefficients, conjugate Fourier fibers
grading: normal mass involution K and boundary eigenspaces, not physical chirality
action_owner: repository-construction -- fixed K1840 conservative repair
target: differential observation O on a slab with matched source and target domains MAP-TYPE=restriction
```

## Result and scope

The boundary-domain obligation left by [K1890](k1890-preparation-evolution-boundary-incompatibility-2026-10-21.md)
is solvable, including transverse motion and a smooth static mass profile R(x1).
An explicit rational eight-dimensional source boundary and a two-dimensional
target boundary transport the observation and its adjoint. Their closed
observation Gram is **576 alpha times the square of the target Hamiltonian**.
Here alpha=138/25. The missing normal modes do not disappear at nonzero mass:
they become two exponentially weighted surface modes. Nonzero transverse
momentum makes these modes observable and gives them a mass-independent
surface Dirac dispersion.

These are conditional equations, not the source's full20 placement. SC-OP-04
ASSERTS candidate four-field grammar; SC-MAS-01/SC-CHI-02 ASSERT a stylized
curvature coupling. SC-OP-05 and SC-META-53 remain UNCERTAIN. WGS05 still lacks
the full20 injection and separate K/C reality/pairing maps. RA-F1, AC-F1,
LT-SM8, source and physics-ledger verdicts remain unchanged. CAR quantization,
physical wall selection, interacting positivity and native GU are not supplied.

## 1. Actual matrices and the boundary construction

Use precisely K1832 H,A_i, K1836 T_i,D_i and the **first** K1840 repair C,B,S
in each of the four coordinate types. Set d_i=D_i/24 and

```
K=D1 B, P+=(I+K)/2, P-=(I-K)/2, E=H^-1 T1^T/alpha,
F=H A1, N_a=T_a-24 D1 T1 A_a (a=2,3).
```

K is symmetric, K²=I, its eigenspaces W± have dimension2 and are D1-isotropic.
D2,D3 commute with K. The exact identities include

```
T1 E=I, A1 E=E d1, C E=-E B, T1 C=-B T1,
S=-24 K T1, T1 A1^-1=24 D1 T1.
```

Thus the normal slow sector and its H-orthogonal fast complement are reducing
for A1 and C. Transverse A_a need not preserve that split.

Here is a reproducible rational construction, not just a dimension argument.
Let Z be the nullspace basis returned by exact row reduction of
`stack(T1, P+N2, P+N3)`, using column order in the pinned matrices.
It has dimension8. The form q=Z^T F Z has rank4 and radical dimension4.
Its columns numbered0,1 are isotropic and independent modulo the radical.
Define

```
L_fast = span(Z ker q, Z[:,0], Z[:,1]),
L = L_fast direct_sum E W+.
```

The certificate serializes the resulting16x8 rational matrix in every type.
Direct verification gives

```
dim L=8, L^T F L=0, T1 L=W+,
P+ N2 L=P+ N3 L=0.                                      (1)
```

Since F has inertia(8,8), L is self-orthogonal. Impose this SAME trace
subspace at both normal endpoints x=0,ell, and impose W- on the target.
This is one explicit boundary, not a classification or physical selection.
It attains K1890's minimal observed rank2 per face.

## 2. Evolution domains and the actual transport calculation

Fix a tangential Fourier momentum p=(p2,p3). Write

```
P_s=A1 partial_x+i sum p_a A_a+R(x)C,
P_t=d1 partial_x+i sum p_a d_a+R(x)B,
O=T1 partial_x+i sum p_a T_a+R(x)S.
```

Assume real smooth R on the closed interval. H is fixed positive; H A_i are
symmetric and HC is skew. The H1 source domain with traces in L makes P_s
skew-adjoint, by the Green identity and L=L^(perp_F). The target H1 domain
with traces in W- similarly makes P_t skew-adjoint. Bounded matrix potentials
preserve these fiber results. The torus direct sum, or transverse-plane direct
integral, uses the natural square-integrable graph domains. Real Fourier
conjugation is preserved.

K1840's identities give `O P_s=P_t O`, including the R' term. Formal algebra
alone is insufficient. If psi and P_s psi have boundary values in L, then

```
O psi = 24 D1 T1 P_s psi + i sum p_a N_a psi              (at a boundary).
```

The mass terms cancel because T1 C=d1 S. Both terms lie in W- by (1).
Consequently O sends the smooth invariant source core into the target domain.
Differentiating the solution there and using uniqueness gives
`O exp(-tP_s)=exp(-tP_t)O`. It extends by the observation graph closure.
The smooth-vector core is a core for P_s; O is bounded from its graph norm
into L2, so no assumed boundary preservation replaces this calculation.

For fixed p, the closure of O initially on that source domain has a simple
description: its slow component f=T1 psi lies in H1 with traces in W+;
its fast component is arbitrary L2. Fast derivatives are invisible to T1.
Approximation by smooth fast functions with chosen endpoint values proves
the extra fast trace constraints disappear in this weaker graph closure.
This does NOT remove them from the evolution generator's domain.
The observation domain is invariant under the source unitary group by the
core identity and unitarity. Taking adjoints gives the corresponding strong
adjoint intertwiner.

## 3. Closed Gram and target Hamiltonian

The observation adjoint is

```
Odagger=H^-1[-T1^T partial_x-i sum p_a T_a^T+R S^T],
Dom Odagger={y in H1: y(0),y(ell) in W-}.
```

The boundary condition follows from `[y* T1 psi]`, since T1 L=W+.
With kappa=24R and V(x)=integral_0^x kappa(s)ds, direct multiplication yields

```
O Odagger = alpha[-partial_x²+|p|²+kappa²-kappa' K].       (2)
```

Its domain is H2 with

```
P+ y=0,    P-(y'-kappa y)=0                              (both endpoints).
```

The second condition is exactly the slow trace condition on Odagger y.
Moreover the fast part of Odagger y has trace in L_fast: the exact independent
adjoint-boundary calculation checks this, rather than assuming it from a
bulk identity. These conditions also equal Dom(P_t²), and

```
O Odagger = -576 alpha P_t².                             (3)
```

This holds as an equality of self-adjoint nonnegative realizations.
It supplies global spectral/range information, not only equality of symbols.
The minimum-energy inverse on the positive spectral subspace is
`Odagger (O Odagger)^-1`; whenever bounded, it intertwines the two groups.
The normalized polar observation is a unitary identification of the visible
source complement with the target complement of ker(Odagger).

## 4. Spectrum, hidden surface modes and energy consumers

For constant R, let k_n=n*pi/ell, n>=1. The target K+ components are
Dirichlet sine modes. K- components have Robin modes
`cos(k_n x)+(kappa/k_n)sin(k_n x)`, plus `exp(kappa x)`.
The scalar separated Sturm--Liouville problems are self-adjoint with compact
resolvent. Solving the endpoint determinant gives exactly these modes;
the exponential mode is the separate negative radial eigenvalue of
`-partial_x²`, not an omitted n=0 sine. Their tensor products with W± are complete.
Thus the **observation Gram** eigenvalues are

```
surface: alpha |p|²                    (multiplicity2),
bulk: alpha (|p|²+kappa²+k_n²)          (multiplicity4).
```

The target evolution frequencies are `+/-|p|/24` on the surface and
`+/-sqrt(|p|²+kappa²+k_n²)/24` in the bulk (two per sign). At p=0 the two
surface modes are stationary and unreachable. At p!=0 they propagate and
have exact unit-target preparation energy `1/(alpha |p|²)`.
A unit bulk target has energy `1/[alpha(|p|²+kappa²+k_n²)]`.
These are the repaired evolution domains; K1889's old preparation coefficient
c=1403424/359375 is NOT the coefficient alpha here.

On a transverse torus, remove only the two p=0 surface modes. If p_min is
the shortest nonzero transverse momentum, the sharp inverse norm is

```
1/sqrt(alpha min(p_min²,kappa²+(pi/ell)²)).               (4)
```

For the normal subsystem alone omit p_min: it is
`1/sqrt(alpha(kappa²+(pi/ell)²))`. Best error for a general target includes
its orthogonal projection onto the two missing modes, at every source budget.
For finite mode data, the remaining budget/error tradeoff is exactly the
existing K1869 spectral law applied to THESE eigenvalues; no new variational
calculus is claimed.

On the infinite transverse plane the p=0 set has measure zero, so the kernel
in L2 is zero and the observation range is dense. It is not all of L2.
Writing a(p) for the coefficient of the normalized radial surface frame, the
precise extra finite-energy condition is
`integral_R2 |a(p)|²/|p|² dp < infinity`; the bulk inverse is bounded.
A smooth surface target with a(0)!=0 fails logarithmically. Mass localizes
its radial profile but does not cure this infrared obstruction.

## 5. Follow-through: arbitrary smooth static normal profiles

No constant-mass approximation is needed for (1)--(3). The surface frame is
`exp(V(x)) W-`, normalized in L2(0,ell). It still has Gram eigenvalue
alpha|p|², and the same two-dimensional transverse Dirac dynamics.
The scalar K+ Dirichlet operator is `D*D`, D=partial_x+kappa; the K- Robin
partner is `DD*`. Their nonzero spectra agree, while the latter has the
single scalar ground state exp(V). This follows from the closed first-order
Dirichlet operator and its unrestricted adjoint, not a sampled potential.
Each scalar level carries the target spin multiplicities above.

For any Dirichlet u put h=exp(V)u. The Rayleigh quotient is
`integral exp(-2V)|h'|² / integral exp(-2V)|h|²`.
The ordinary interval Dirichlet Poincare inequality therefore proves

```
nu_1 >= exp(-2 osc(V)) (pi/ell)² > 0.                    (5)
```

Equations (4) and the plane range criterion extend with nu_1 replacing
kappa²+(pi/ell)², and (5) gives an explicit conservative bound.
A sign-changing wall or variable curvature profile does not remove the
surface deficit in this selected domain. This is a conditional domain result,
not a no-go for the source's effective-chirality mechanism or other boundaries.

## Verification, hostile review and remaining work

Producer:72 exact matrix groups and3 input pins. Separate trace-jet/ODE probe:
45 mathematical checks plus3 pins and1 reported-multiplicity check. It rejects
3 mathematical faults (boundary isotropy, Robin sign, bulk mass term) and1
serialized alpha fault through explicit failing checks after a clean baseline.
An initial positivity check attempted symbolic cubic eigenvalue comparisons;
it was replaced by exact Sylvester leading minors. That crash was not counted
as a detected mutant. Continuum completeness, domain closure and profile gap
are proved above, not certified by finite sampling.

Hostile review checked (i) Dom G versus the weaker observation graph domain,
(ii) p=0 exponential modes, (iii) old preparation versus repaired spectra,
(iv) profile derivative signs and (v) real fibers versus arbitrary boundary
mixing. The adjoint trace test closes the main reproducibility seam. No
blocking mathematical finding remains in this scope; independent-agent,
external-expert, proof-assistant acceptance and novelty are not claimed.
This uses standard one-dimensional factorization and boundary-space methods.
The new contribution here is their composition with the actual four-type
matrices, boundary construction, and full observation/evolution domains.

Native full20 identification, nonlinear rotating mass classes, physical
quantization/selection and a three-wall box remain separate questions.
The source boundary here is selected to make this observation work; it is not
forced by GU geometry. The causal algebra question is separately addressed
by K1892 on whole space, without importing this boundary's spectrum.
