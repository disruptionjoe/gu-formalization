---
title: "K2556 Finite radial polynomial point-source responses and Cauchy limits"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: local distributional existence for finite radial polynomial pressure sources; no compact radial source, physical boundary or uniform synthesis
scripts:
  - tests/channel-swings/k2556_distributional_source_response_probe.py
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2556
carrier: finite radial-polynomial conserved pressure sources times arbitrary local seven-dimensional B distributions LAYER=toy CHIRALITY=N/A
pairing: original indefinite tensor/test duality; auxiliary local Sobolev norms only ON=declared_carrier
real_structure: real nonzero kappa, analytic curved product; complex scalar factorization recombined to real solutions
grading: scalar and TT source pieces, six potentials, shifted metric and original metric remain distinct
action_owner: repository-construction -- selected comm/symi/symi completion of K2537
target: point-source response existence in a finite radial class and rejection of naive Cauchy extension MAP-TYPE=evaluation
```

# K2556 Admit the B point source through a finite radial invariant space

## Result and exact scope

The actual conserved radial-pressure source FORM of K2552 has local
B-distributional solutions for every finite polynomial pressure P(C²),
including rho=delta_B, with all seven B variables and every original selected
linear field equation retained. This supplies a nonzero source family beyond
analytic B germs. It is not a solution for K2531's compact radial profile:
nonzero finite polynomials cannot have that support. Nor is it a uniform
polynomial approximation theorem, a causal or physical boundary prescription,
a common closed self-adjoint realization, or uniqueness modulo gauge.

The source remains j_A rho with eigenvalues A/2 on the four observer
directions and P/2 on the three normal directions, no B/mixed source. We
choose a different auxiliary polynomial splitter, not K2552's Dirichlet
splitter. This changes the decomposition but not the specified polynomial
source. No arbitrary-splitter response independence is claimed here.

SC-ACT-01 ASSERTS its first-order action; SC-GEO-55 ASSERTS displacement from
gauge-rotated Levi-Civita; SC-GEO-03 ASSERTS Met(X); SC-META-53 is UNCERTAIN
about indefinite spectra. The independent curved product and selected action
completion remain repository constructions. Ledger0.263, native physics,
source polarities and canon remain unchanged.

## 1. Exact finite-dimensional radial closure

Retain K2552's K>0, C'=−KS, S'=C, C²+KS²=1, alpha=C'/C and beta=C/S.
For C near1 (regular radial center), the scalar operators become

    X=K[(1-C²)∂C²+(4/C-7C)∂C],
    D5=K[(1-C²)∂C²+(6/C-11C)∂C].                    (1)

For every even m>=0, with the lowering term absent at m=0,

    X C^m=m(m+3)K C^(m-2)-m(m+6)K C^m,
    D5 C^m=m(m+5)K C^(m-2)-m(m+10)K C^m.            (2)

Thus V_N=span{1,C²,...,C^(2N)} is invariant for both. Their triangular
diagonals x_j=−2j(2j+6)K and y_j=−2j(2j+10)K are distinct within each
operator, so each has an eigenbasis on V_N. They need not share that basis.
These are smooth even radial functions in r; the apparent C^-1 causes no
problem and the tensor reconstruction has no center flux.

For ANY real P∈V_N set

    A=P+(C/4)∂C P, t=(4A+3P)/2,
    chi=−(X+7K)^−1 t/6.                             (3)

The pressure conservation law P'+4alpha(P−A)=0 holds identically. The
inverse in(3) exists on V_N because 7−2j(2j+6) is never zero for an integer
j>=0. The TT radial amplitude

    b=P/2+(4alpha+2beta)chi'+6Kchi

also belongs to V_N, since

    (4alpha+2beta)(C^m)'=4mK C^(m-2)−6mK C^m.        (4)

Moreover b belongs to V_(N-1) for N>=1, and b=0 for N=0. For a leading
pressure monomial C^m, the leading chi coefficient is1/[12K(m-1)], because
7-m(m+6)=-(m+7)(m-1). Its b coefficient is
1/2+6K(1-m)/[12K(m-1)]=0. The original half factor is essential.

K2552's source identity j_A=L_A*chi+R(b) therefore holds with the ORIGINAL
half normalization and full pressure tensor. There is no imposed TT forcing
and no B-frequency projection.

## 2. Local scalar B inverses that accept distributions

Choose a sufficiently small compact smooth coordinate ball M in an analytic
B chart. For each complex z, Y−z has real nondegenerate quadratic principal
symbol p; d_xi p=2g_B^-1 xi is nonzero for xi!=0. Remark2.1 of Oksanen,
Salo, Stefanov and Uhlmann gives real-principal-type after shrinking the chart.
Their Proposition2.2(d) supplies a bounded H^s(M)→H^(s+1)(M) right inverse
when the compactly supported adjoint kernel is zero. These are unrestricted
local solutions, with no imposed Cauchy data.

Here that kernel is zero. Fix an analytic coordinate t with non-null dt on
a slightly larger chart. A nonzero compactly supported distributional solution
of the analytic adjoint (Y−conj(z)) would have a point of maximal t in its
support. Holmgren uniqueness across the noncharacteristic plane t=constant
excludes support there, a contradiction. This concerns the support of the
adjoint kernel, not compact support of the resulting inverse.

The finite family of factors below can use one common small chart, since
their principal symbols agree. For arbitrary local rho, first restrict to a smaller ball and use a cutoff
in a larger chart; the compactly supported distribution has some finite
negative Sobolev order. For a degree-m nonzero polynomial F(Y), factor
it over C, divide the forcing by its leading coefficient, and solve its m
second-order factors successively. If
L1 v1=f, L2 v2=v1,...,Lm vm=v_(m-1), then
L1...Lm vm=f. No commutation of the CHOSEN right inverses is assumed.
The differential factors themselves commute. The Sobolev index increases by
one per factor; coefficients and norm constants can depend on every root and
N. A point delta in seven dimensions lies in H^s for s<−7/2, in particular
H^-4. Real parts give real solutions whenever F and f are real.

[Local solvability reference, Remark2.1 and Proposition2.2](https://users.jyu.fi/~salomi/pub/real_principal_type_v32.pdf).
The theorem application and its kernel hypothesis are mathematical inputs,
not consequences of the finite algebraic probe count.

## 3. All four response equations, with the actual mixed determinant

Diagonalize chi in the X eigenbasis and b in the D5 eigenbasis. Their finite
coefficients multiply the SAME rho(B). The two TT equations reduce, mode by
mode, to

    (Y+y_j−16K)v_j=rE b_j rho,
    c(Y+y_j+mu−21K)u_j=−rE b_j rho.                  (5)

The scalar Einstein equation reduces to Y+x_j+12K. The scalar displacement
equation reduces to d(x_j,Y), always of degree5 with the nonzero leading
coefficient from K2554. In particular one retains

    d_1(X,Y)=P0(X+Y)+XY Q0(X+Y),                     (6)

not just P0. Section2 solves each of these finitely many scalar equations
with B distributions. Assemble w,U,v,u; K2552 equations(8)–(10) and the
cofactor identity then give

    z=z_TT+z_scalar, Q=Q_TT+Q_scalar,
    h=z−rE sym(Q), e2=−A2^-1 BQ.                    (7)

Every displayed differentiation acts on smooth radial coefficients or on
B distributions, so is defined. Radial smoothness and evenness preserve
regularity at r=0, including the full R(b) tensor; no puncture-source is
introduced. The same source equality holds distributionally. This establishes
existence for the full selected linear equations in this finite radial class.
It does not assert positive energy or a selected physical readout.

### A nontrivial exact source with both scalar and TT pieces

Take P=C² and A=(3/2)C². Then

    t=(9/2)C²,
    chi=C²/(12K)−5/(42K)
        =(C²−5/8)/(12K)−15/(224K),
    b=−1/21.                                       (8)

The two scalar eigenvalues are−16K and0; the TT D5 eigenvalue is0.
Thus the exact response uses d(−16K,Y),d(0,Y), Einstein factors Y−4K and
Y+12K, and TT factors Y−16K and c(Y+mu−21K). This is not a constant-only
or TT-only example. Multiplying by delta_B is allowed by section2.

For any fixed finite N, choose the bounded right inverses once. If smooth
rho_epsilon→delta_B in H^-4(M), the resulting potentials converge in their
stated Sobolev spaces and all reconstructed fields converge distributionally.
Thus this finite-radial construction has a justified B-smoothing limit,
unlike an uncontrolled CK approximation. It supplies no uniform N→infinity
limit, nor convergence to a compact radial source.

The example can also be the local core of a genuine compact radial source.
Choose a smooth nonincreasing cutoff eta, equal1 near r=0 and zero before R;
set P_global=C² eta and A_global=P_global+P_global'/(4alpha) away from0.
Near0 use A_global=(3/2)C², which agrees smoothly. Since alpha<0 and
P_global'<=0, A_global>=P_global>=0, and conservation holds. The local
core source is exactly(8). This does not solve the cutoff region, the
Dirichlet-split tail problem, or K2531's independently specified profile.

## 4. Why a naive Cauchy replacement remains invalid

The unrestricted B signature(3,4) leaves a same-sign tangential covector
orthogonal to any non-null prospective time covector. The scalar principal
polynomial then has nonreal normal roots; analytic noncharacteristic CK
existence is not a smooth Cauchy estimate. This repeats the applicable
ultrahyperbolic fence, not a new all-domain no-go.

There is a NEW obstruction to a seemingly favorable repair in the FROZEN
one-time scalar determinant model. This is the auxiliary constant-coefficient
pencil obtained by replacing X,Y with constant quadratic operators; it is
not a claim about all lower coefficients of a fully composed curved operator. At kappa=1, let L be the leading
coefficient of P0 and q2 the quadratic coefficient of Q0. Exact algebra gives

    gcd(P0,Q0)=1,
    L=−2605746313310516251459584/22521658027326625,
    q2=−4248943925994768/160894724947221409,
    q2/L=6125/26834819055616 >0.

Set X=−n^6,Y=n^6+n^4 z in the frozen constant-coefficient dispersion
polynomial. After division by n^20 its coefficientwise limit is

    z²(L z³−q2).                                   (9)

The cubic roots are simple, including a nonreal conjugate pair
z±=a(−1±i sqrt(3))/2, a=(q2/L)^(1/3)>0. Root continuity (or the implicit
function theorem with epsilon=1/n) gives nearby roots z_n. For the one-time
Fourier convention Y=omega², X=−k², k=n³, the growing branch satisfies

    omega_n=n³+(z_n/2)n+o(n),
    |Im omega_n|/n→sqrt(3)a/4>0.                     (10)

Hence homogeneous modes grow as exp(c t k^(1/3)); no uniform finite-loss
Sobolev Cauchy estimate holds for that frozen scalar equation. Its Cauchy
jets grow only polynomially with k, while any t>0 gives exponential growth.
Real solutions follow by conjugate pairing. Fourier amplitudes
exp(−epsilon k^(1/sigma)) also show this branch obstructs all-data Gevrey
sigma>3 evolution; sigma=3 requires radius/time control, and sigma<3
sufficiency is NOT established. This is a frozen scalar diagnostic, not a
variable-coefficient instability theorem or a physical gauge-mode claim.

Dropping XYQ0 would miss it: roots of P0(X+Y)=0 have fixed Z=X+Y,
so Im sqrt(n^6+Z)=O(n^-3). The genuine mixed correction changes the
high-frequency conclusion. Full B ultrahyperbolicity has its own stronger
Cauchy obstruction; the restricted-slice exponent is not a full-system bound.
Neither obstruction contradicts the non-Cauchy distributional solutions above.

## Verification, retained debt and next test

The probe recomputes the actual six-row matrix determinant, finite radial
operator identities and spectra, source conservation/splitter/example, mixed
polynomial gcd, dispersion scaling, and contrary controls. Universal local
solvability and smoothing convergence use section2, not numerical root samples.
Independent specialist review checks the theorem hypotheses and reconstruction.

The exact compact radial source still requires uniform spectral/polynomial
synthesis or a different direct domain construction; the current inverses
have no such uniform estimates. A polynomial cannot vanish on an open radial
annulus without being zero. Arbitrary-splitter matching, boundary choice,
source-disjoint metric observations and physical acceptance remain independent
obligations. The next decisive step is a norm-controlled radial synthesis with
the actual mixed determinant, or an explicit finite-mode gauge-invariant
observation with its boundary dependence retained. Do not replace the source
by the example or promote existence to a unique physical response.

[Four-scalar reduction](k2552-localized-source-domain-2026-11-04.md),
[analytic-germ result](k2554-analytic-source-response-2026-11-05.md),
[probe](../../tests/channel-swings/k2556_distributional_source_response_probe.py).
