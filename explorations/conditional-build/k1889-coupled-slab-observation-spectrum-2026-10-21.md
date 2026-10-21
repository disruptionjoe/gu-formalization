---
title: "K1889: Exact coupled slab spectrum and the return of an infrared obstruction"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional compressed-system mathematics on the stated slab and domains; no native GU identification or physical boundary selection
scripts:
  - tests/channel-swings/k1889_coupled_slab_observation_spectrum.py
  - tests/channel-swings/k1889_coupled_slab_observation_spectrum_probe.py
---

# K1889: Exact coupled slab spectrum and the return of an infrared obstruction

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
result: exact coupled slab preparation bands and finite-energy range/budget laws
carrier: conditional real16 source and real4 target, complexified for transverse Fourier analysis LAYER=toy CHIRALITY=N/A
pairing: positive H source L2 and Euclidean target L2 ON=minimal_observation_graph_slab
real_structure: conjugate Fourier momenta recover real fields
grading: surface/bulk spectral decomposition, not a physical chiral grading
action_owner: repository-construction -- fixed conditional observation operator
target: preparation inverse spectrum and source-energy/error tradeoff MAP-TYPE=quotient
```

## 1. Question, domain and reused result

[K1888](k1888-bounded-support-energy-inverse-2026-10-21.md) constructs a
minimum-energy preparation inverse on a rectangular box, but does not solve
its coupled spectrum. Here the domain is deliberately changed to
`Omega=(-L,L) x T(l2) x T(l3)`, where T(ell) has period ell. Keep exactly the
same observation coefficients, source energy and zero-normal-observation-flux
support boundary at x1=+/-L. Transverse directions are periodic, not compactly
supported in a box. This result solves the slab, not the three-wall box.

Let A be the closure of O on sources smooth periodic transversely and compact
inside the open normal interval, with graph norm ||psi||H+||O psi||2. As in
K1888, Dom A*=H1 and its form is integral (D*u)^*G(D*u), where

```
D*u=((-partial1+kappa K)u,-partial2 u,-partial3 u),
kappa=24R, K=diag(1,-1,-1,1),
alpha=138/25, beta=1866/625, rho=beta/alpha=311/575,
c=alpha*(1-rho^2)=1403424/359375 > 0.
```

The argument establishing Dom A* in K1888 applies unchanged: the constant
flux map has full row rank, so its adjoint has a left inverse and the
adjoint condition controls all first distributional derivatives. Fourier
series and the form definition specify the global operator without assuming
corner regularity. In this note complexification is only a Fourier tool;
real fields obey conjugate symmetry at opposite momenta.

The actual data are K1832's real16 source with positive H, K1836's
real4 observation, and K1888's flux Gram. SC-OP-04 ASSERTS candidate
four-field grammar; SC-MAS-01 and SC-CHI-02 ASSERTS a stylized curvature-mass
toy. SC-OP-05 and SC-META-53 remain UNCERTAIN. These matrices are a
repository conditional construction, not the source's unconstructed full20
placement/injection/reality/pairing/domain adapter. RA-F1, AC-F1, LT-SM8,
source, physics-ledger and canon verdicts do not change.

## 2. Actual Robin matrix and complete spectrum

For tangential momentum `p=(2pi n2/l2,2pi n3/l3)`, write

```
J2=G12/beta, J3=G13/beta,
M_p=kappa K-i rho(p2 J2+p3 J3),
m_p^2=kappa^2+rho^2 |p|^2.
```

All four coordinate types have the same G. Direct exact reconstruction gives
`J2^2=J3^2=-I`, `{J2,J3}=0`, `{K,J2}={K,J3}=0`.
Consequently M_p is Hermitian, has trace0, and `M_p^2=m_p^2 I`.
When m_p>0 it has eigenvalues +m_p and -m_p, each twice.
The ACTUAL normal flux condition is

```
alpha(-u'+kappa K u)-i beta(p2 J2+p3 J3)u=0,
therefore u'=M_p u at BOTH endpoints.                         (1)
```

The two outward normals do not reverse the Robin coefficient: each multiplies
the whole zero-flux expression by its sign. The interior operator is
`alpha(-d^2/dx1^2+kappa^2+|p|^2)I`.

Diagonalize M_p by a constant unitary matrix. For scalar Robin coefficient
b=+m_p or -m_p, the mode `exp(b x1)` is an eigenfunction of -d^2 with
eigenvalue -b^2. Every positive oscillatory normal eigenvalue is
`w_n^2=(n pi/(2L))^2`, n>=1, with eigenfunction
`cos(w_n(x1+L))+(b/w_n)sin(w_n(x1+L))`.
Indeed the right endpoint residual is
`-(w^2+b^2)sin(2Lw)/w`. For negative eigenvalues put w=i s:
the determinant vanishes only at s=|b|; the linear w=0 case gives no
additional mode unless b=0, in which case the constant is already the ground
mode. This elementary regular scalar Sturm-Liouville problem is self-adjoint
with compact resolvent; the displayed eigenfunctions exhaust it (alternatively
its characteristic determinant covers every eigenvalue and the spectral theorem
supplies completeness). Thus, per complex Fourier momentum, the complete bands are

```
surface: lambda_s(p)=c |p|^2, multiplicity4,
bulk:    lambda_n(p)=alpha(kappa^2+|p|^2+(n pi/(2L))^2),
         multiplicity4 for each n>=1.                         (2)
```

Coinciding eigenvalues from different p or n add multiplicities. Opposite
complex Fourier momenta are paired when constructing real fields. The word
surface names the exponentially weighted preparation eigenfunctions; it does
not assert a dynamical edge particle. At kappa=p=0 all four ground profiles
are constant and (2) remains valid.

A convenient normalized frame for the whole surface band is

```
E_p(x1)=sqrt(m_p/sinh(2Lm_p))*exp(M_p x1),
E_0 limit at m_p=0 = I/sqrt(2L).                              (3)
```

Since M_p is Hermitian and its square is scalar,
`integral E_p^*E_p dx1=I`: the odd sinh term integrates to zero.
Individual +/-m_p eigendirections concentrate near opposite faces with
normal density proportional to exp(+/-2m_p x1). Thus mass increases
normal localization without opening a gap in lambda_s(p).

## 3. Sharp finite-period preparation budgets

The kernel has exactly four p=0 profiles exp(kappa K x1)v, as in K1888.
On its orthogonal complement, let
`p_min=2pi/max(l2,l3)`. Equation (2) gives the EXACT gap

```
g=min(c p_min^2, alpha(kappa^2+pi^2/(4L^2))),
||minimum_energy_right_inverse||=1/sqrt(g).                    (4)
```

This is not K1888's auxiliary scalar lower bound. For periods2pi, L=1,
kappa=1, the gap is c and the norm is sqrt(359375/1403424).
Every positive mode y of target norm a has minimum source energy a^2/lambda.
For source NORM budget B its exact best target error is
`max(0,a-B sqrt(lambda))`. Graph-core density and rescaling enforce the same
infimum with smooth sources supported away from the normal faces; attainment
in that smaller core is not asserted.

The general energy-budget formula is reused from K1869/K1888, now with
explicit coupled spectral data. For two orthonormal surface modes with
|p|=1 and2, target amplitude1 in each, choose penalty t=c. Then

```
B^2=41/(100c),       best error^2=29/100.                      (5)
```

The minimum source amplitudes are sqrt(lambda)/(lambda+c).
Completing squares for sum[(sqrt(lambda)a-1)^2+c a^2]
proves optimality, not merely feasibility. Taking real cosine/sine pairs
produces the same normalized real example. No fitting of coefficients is used.

## 4. Infinite transverse plane: mass no longer supplies an L2 inverse

Replace the transverse torus by R2, keeping the finite normal interval and its
support boundary. Partial Fourier transform gives exactly the same fibers.
The surface spectrum c|p|^2 reaches0 for every mass, while the bulk has the
strict gap alpha(kappa^2+pi^2/(4L^2)). There is no L2 kernel because the
p=0 set has measure zero, but range is dense and not all of target L2.
For surface coefficients z_s(p)=integral E_p(x1)^* yhat(x1,p) dx1,
the exact finite-energy range criterion is

```
integral_R2 |z_s(p)|^2/(c|p|^2) dp < infinity.                (6)
```

Bulk contributions have a bounded inverse and add finite energy for every
L2 target. Formula (6) follows by applying the elementary minimum-source
formula in each positive spectral fiber and integrating; the polar
factorization yields a source precisely when this weighted norm is finite.
It also proves that the inverse is unbounded. This differs from K1881's
massive whole-R3 surjectivity: normal support changes the operator domain.

For a smooth target compact inside the slab, z_s is differentiable near0.
Thus (6) holds iff z_s(0)=0: a nonzero limit gives logarithmic divergence;
a zero limit gives O(|p|), which is integrable in two tangential dimensions.
By (3), z_s(0)=0 is exactly the four exponential-charge condition
`integral exp(kappa K x1)y(x) dx=0` (normalization is a nonzero scalar).
Sufficiency also agrees with K1883's compact primitive inside a finite
containing rectangle. What is new here is necessity even for general
finite-energy sources confined only in the normal direction. A nonzero-charge
compact target still has a finite-energy whole-R3 lift at nonzero mass, but
cannot have one with this fixed normal support.

## 5. Exact accuracy versus energy for an infrared-singular target

Use unitary tangential Fourier normalization with Lebesgue dp and choose
`yhat(x1,p)=pi^(-1/2) exp(-|p|^2/2) E_p(x1)v`, ||v||=1 real.
It has target norm1, is real after inverse transform, and fails (6).
For penalty t>0 put a=t/c. The best penalized source and its target error obey

```
B(t)^2=((1+a) exp(a) E1(a)-1)/c,
e(t)^2=a-a^2 exp(a) E1(a),
E1(a)=integral_a^infinity exp(-u)/u du.                       (7)
```

To derive this, substitute u=|p|^2 in the radial integrals:
`c B^2=integral_0^infinity u exp(-u)/(u+a)^2 du` and
`e^2=integral_0^infinity a^2 exp(-u)/(u+a)^2 du`.
Writing F(a)=exp(a)E1(a) gives `F'=F-1/a`; splitting
u=(u+a)-a yields (7). As t decreases0, B increases without bound
and e decreases0. Every finite B has positive optimal error, although the
unconstrained error infimum is zero. The penalty is uniquely selected by B;
strict monotonicity follows directly from the positive spectral integrand.

The standard expansion `E1(a)=-gamma_E-log(a)+O(a)` gives

```
B^2=(log(1/a)-gamma_E-1+o(1))/c,
e^2=a(1+o(1)),
e(B)=exp(-(c B^2+gamma_E+1)/2)*(1+o(1)).                    (8)
```

The expansion is [NIST DLMF 6.6.2](https://dlmf.nist.gov/6.6.E2);
the application and integral reduction above are explicit. K1869 already
uses spectral regularization for another infrared-obstructed observation;
no novelty is claimed for the calculus. Here it is driven by the actual
coupled boundary surface band even at nonzero mass. As on the torus,
compact graph-core approximants and scaling preserve each positive budget
infimum, without asserting a compact minimizer.

## 6. Verification, hostile checks and exact remaining limit

The producer reconstructs all four Grams and checks40 exact groups plus3
input pins. The separate probe checks123 exact controls,6 high-precision
radial integrals and8 reporting/pin checks. Its clean baseline precedes
5 mathematical faults and2 serialized coefficient faults, each caught by
explicit FAIL assertions. Finite probes do not prove spectral completeness,
global domains or the range theorem; sections1--5 carry those arguments.
The first producer attempt failed to simplify equivalent exp/sinh normalizers;
rewriting sinh in exponentials resolved equality without changing mathematics.

Inline hostile review checked both Robin endpoint signs, the omitted
hyperbolic/zero-frequency roots, real multiplicities, normalizing the full
surface frame, transverse volume change, zero versus absent L2 charge modes,
and nonattainment versus energy blow-up. No blocking finding remained after
the scope was fixed. There was no independent agent, external specialist or
proof-assistant review. The slab does not solve a rectangular box spectrum,
and its preparation domain is not automatically an evolution domain.
[K1890](k1890-preparation-evolution-boundary-incompatibility-2026-10-21.md)
tests the latter independently. An actual native adapter, interacting quotient,
noncanonical rotating construction and the three-wall box spectral problem
remain distinct open tasks; none follows from the solvable slab.
