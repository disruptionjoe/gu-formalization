---
title: "K2237 Computable continuum causal detector error witnesses"
status: active_research
doc_type: exploration
created: "2026-10-29"
scripts:
  - tests/channel-swings/k2237_computable_causal_witness_probe.py
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional scalar continuum error bounds; no local apparatus or GU realization
---

# K2237 Computable continuum detector signalling witnesses


> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

```gu-typed-objects
result: explicit continuum finite-energy bounded witnesses for supplied number-and-squeeze detectors
carrier: positive massive scalar Fock space, compact canonical mode and representation complement LAYER=toy CHIRALITY=N/A
pairing: Hilbert form and physical free-energy form ON=declared_carrier
real_structure: real Cauchy smearing and complex adjoint
grading: canonical oscillator occupation and parity; not spinor chirality
action_owner: repository-construction -- supplied number effects and outcome squeezes
target: complete recorded-channel energy-constrained causal separation MAP-TYPE=intertwiner
```

Conditional independent scalar mathematics,
not GU source selection or physical recovery. This constructs explicit
finite-energy witnesses for K2234's separation. It does not construct an
apparatus, prove sufficiency after communication, or inherit K2219's optimum.
The concrete effects/squeezes are K2225's supplied consumer.

## Object and hypotheses

Use the positive massive scalar Fock representation on R^d,
omega=sqrt(-Delta+m^2), m>0, H=dGamma(omega), physical vacuum Omega.
Take real normalized f in C_c^infinity, m_j=<f,omega^j f>,
nu=sqrt(m_1/m_-1), q=sqrt(nu)phi(f), p=pi(f)/sqrt(nu),
b=(q+ip)/sqrt(2), n=b* b. Let

    N=(sqrt(m_1 m_-1)-1)/2.

The reduced physical vacuum on this oscillator is the centered thermal state
of mean N: its q,p variances are both N+1/2 and its mixed covariance is zero.
This follows from the KG Gaussian covariance and the stated nu, not an
identification of oscillator vacuum with physical vacuum. Its complement can
be entangled with it. No spatial tensor factorization is asserted.

The complete target instrument has Kraus K_r=S_r sqrt(e_r(n)), finite r,
e_r(n)>=0, sum_r e_r(n)=1, finite s_r>0, S_r* q S_r=s_r q and
S_r* p S_r=p/s_r. All controls, positivity and this target are supplied.
Let Phi be its unread channel. Real structure is Cauchy conjugation and
Hilbert adjoint; grading is oscillator occupation, not spinor chirality.

Choose real compact smooth u,g in disjoint A,B with a=<f,u> and c=<f,g>
nonzero. For positive alpha choose lambda=sqrt(2)alpha/(sqrt(nu)a).
Alice's inputs are physical vacuum and U_A Omega,
U_A=exp(-i lambda pi(u)). Their energies are 0 and

    E_A=lambda^2 ||omega u||^2/2.

The reduced oscillator of U_A Omega is displaced thermal with real mean
alpha. The symplectic complement is also displaced: this displacement MUST
be retained, and exactly cancels Bob's raw input shift. Bob's local observable
is X=phi(g). Put k=1/sqrt(nu), Y=phi(g-cf), so

    X=c k q+Y,    [Y,b]=[Y,b*]=0,
    <Y>_0=0,     <Y>_1=-sqrt(2)c k alpha,
    V_Y=Var(Y)=<g-cf,omega^-1(g-cf)>/2.

## Positive adjacent weights: exact finite-sum implementation

Write x=alpha^2 and rho_alpha for the displaced thermal oscillator state.
Define P_n=sqrt(n+1) <n+1|rho_alpha|n>/alpha. For N>=0,

    P_n=exp[-x/(N+1)] sum_(j=0)^n
      binom(n+1,j+1) N^(n-j) x^j/[j! (N+1)^(n+j+2)].       (1)

Every P_n is nonnegative; for alpha>0 every P_n is positive. Their generating
function is

    G(t)=sum_n P_n t^n
        =[1+N(1-t)]^-2 exp[-x(1-t)/(1+N(1-t))].             (2)

In particular sum P_n=1, sum n P_n=2N+x, and
P_0=exp[-x/(N+1)]/(N+1)^2. At N=0 these are Poisson weights
exp(-x)x^n/n!, not a false assertion that the physical vacuum is pure in f.

Proof: for N>0 integrate coherent projectors against
exp(-|beta-alpha|^2/N)/(pi N). A coherent projector contributes
sqrt(n+1)rho_(n+1,n)=beta exp(-|beta|^2)|beta|^(2n)/n!.
Summation and a two-dimensional Gaussian integral give alpha G(t).
Taylor expansion gives (1), continuously including N=0. This integral is
only a representation of the reduced state; no field complement is discarded
when evaluating Y or X below.

For finite certification use either

    sum_(n>K)P_n <= (2N+x)/(K+1),

or, for t=1+delta>1 and N delta<1,

    sum_(n>K)P_n <= t^(-K-1)(1-N delta)^-2
                         exp[x delta/(1-N delta)].         (3)

These are rigorous tail bounds, not asymptotic fits. All finite terms use
nonnegative polynomials and elementary exponential interval bounds.

## First-moment signal, allowing unequal outcome squeezes

Set

    sigma_n=sum_r s_r sqrt(e_r(n)e_r(n+1)),
    D_q=sum_n P_n sigma_n-1.

Direct number-basis matrix elements give

    <q>_Phi(rho_alpha)=sqrt(2)alpha sum_n P_n sigma_n,
    <X>_Phi(input1)-<X>_Phi(input0)=sqrt(2)c k alpha D_q.    (4)

The second equality includes the complement mean -sqrt(2)c k alpha.
The undeformed vacuum target mean is zero by parity. Omitting this complement
would spuriously label identity as signalling.

A momentum intervention exp(i lambda phi(u)) gives the analogous statement
with k=sqrt(nu), X=pi(g), Y=pi(g-cf),
alpha=lambda a/sqrt(2nu), V_Y=<g-cf,omega(g-cf)>/2,
E_A=lambda^2||u||^2/2, and sigma_n=sum_r s_r^-1 sqrt(e_r(n)e_r(n+1)).
Thus both quadratures can be tested. A truncated sum with (3) supplies a
computable certified interval for D_q or D_p.

For no feedback (all s_r=1), Cauchy-Schwarz gives 0<=sigma_n<=1.
Any nonconstant effect sequence has an adjacent strict inequality. Since
P_n>0 for every n, D_q<0, with explicit lower signal
sqrt(2)|c|k alpha(1-sigma_j)P_j for any such link j.
This is a constructive all-nonconstant no-feedback result, stronger than an
existential finite-energy density argument.

It is NOT a complete witness family for arbitrary feedback. Exact hostile
counterconstruction: e_1(n)=1/5 at even n,4/5 at odd n, e_0=1-e_1,
s_1=2,s_0=1/2. Every adjacent overlap for each outcome is 2/5.
Both sigma_q and sigma_p are identically1, despite a nonconstant instrument.
Thus an interval containing zero requires another observable, not a causal
verdict. The second-moment construction below supplies that observable for
this precise counterexample; completeness for arbitrary feedback remains open.

## Bounded local witness and exact error coefficient

Let S=max_r s_r for the q construction (max_r 1/s_r for p). Positivity of
q^2<=2n+1 and completeness of the effects give

    <q^2>_out <= S^2[2(N+x)+1].

This does not assume conditional thermal states. In detail, apply the form
inequality to sqrt(e_r(n))psi and sum, using that e_r commutes with n.
The complement second moment is unchanged and equals V_Y+2c^2k^2 x for
input1, V_Y for input0. The form inequality
(c k q+Y)^2<=2c^2k^2 q^2+2Y^2 therefore gives an upper bound on the SUM of
the target Bob second moments:

    M=4c^2k^2[S^2(2N+x+1)+x]+4V_Y.                       (5)

If a certified positive d satisfies d<=|sqrt(2)c k alpha D_q|, choose
R=2M/d and the bounded local observable F_R=clip(X,-R,R)/R.
Its norm is at most1 and it belongs to Bob's local von Neumann algebra by
spectral calculus. The scalar inequality
|x-clip(x,-R,R)|<=x^2/R proves that its target expectation separation is at
least d/(2R)=d^2/(4M).

An actual apparatus channel obeying operational finite propagation for
T<dist(A,B) has equal Bob expectations on the two inputs. Each output's
half trace distance epsilon permits norm-one expectation error at most
2epsilon, so

    epsilon_(E_A) >= d^2/(16M).                            (6)

This is also a lower bound on reference-uniform complete-record error:
discarding record and reference cannot increase trace distance, and these
unreferenced states are admitted tests. For any E>0, mix the SAME physical
vacuum into BOTH inputs with p=min(1,E/E_*), using E_*>=E_A. Causal equality
persists by linearity, and the same fixed F_R gives

    epsilon_E >= [d^2/(16M)] min(1,E/E_*).                 (7)

The target uses the fixed Cauchy identification of K2234. Composing free
evolution into the target changes the observable/regions and requires a new
statement. Operational causality is assumed of the candidate apparatus, not
inferred from algebra-local notation.

## Concrete rational continuum consumer

Take normalized real compact smooth u,g with disjoint supports and identical
gradient norms <=m^2/16, and f=(u+g)/sqrt(2). Such functions are obtained by
scaling one smooth normalized bump and translating a disjoint copy; this
does not invoke a lattice limit. Then a=c=1/sqrt(2),

    m_2<=17m^2/16,
    m<=nu<=sqrt(m_2)<=sqrt(17)m/4<2m,
    N<1/100,
    V_Y<=||g-cf||^2/(2m)=1/(4m)<=c^2/nu.

Here m_1<=sqrt(m_2), m_-1<=1/m and
m_-1>=1/m_1 (Cauchy-Schwarz) prove the bounds on nu. Moreover
sqrt(m_1 m_-1)<=(17/16)^(1/4)<51/50 proves the bound on N.

Freeze exactly e_1(n)=n/(n+1), e_0(n)=1/(n+1), s_0=2/3,s_1=7/5.
Set alpha=1/10, lambda=1/(5sqrt(nu)). Then

    E_A=lambda^2 ||omega u||^2/2<=17m/800=:E_*,
    sigma_0=2/(3sqrt(2))<1/2,
    sigma_n<=7/5 for every n.

The latter is Cauchy-Schwarz on outcome probability vectors; it is not
inferred from finitely many occupation tests. Using exp(-y)>=1-y,

    P_0 >= (99/100)/(101/100)^2=9900/10201,
    1-sum_n P_n sigma_n
       >= (9/10)P_0-2/5 >=24148/51005 >47/100.             (8)

Thus no cancellation can hide this supplied unequal-squeeze detector. We may
take d^2=2209 c^2/(500000nu). Equation(5) gives

    M <= (7572/625)c^2/nu.

Consequently this genuine continuum, physical-vacuum construction has

    epsilon_E >= (2209/96921600) min(1,800E/(17m))          (9)

whenever T<dist(supp u,supp g). The coefficient is approximately
0.0000227916171421. All constants are rational bounds; no continuum
quadrature or occupation truncation is being offered as proof.

K2228's same direct-control target has error at most
u_Lambda=min(1,sqrt(2L(E+1)T0/Lambda)), T0=1+2pi. Define c_E by (9).
For Lambda>T0/dist(A,B), any causal substitute C_Lambda satisfies

    dist_E(C_Lambda,A_Lambda)>=max(0,c_E-u_Lambda).

For Lambda>8L(E+1)T0/c_E^2 this is at least c_E/2. This consumer uses the
same input-energy norm and target. It does not bound accuracy after the
communication time, output-energy convergence, reset, or apparatus resources.

## The exact first-moment blindspot has a second-moment witness

Return to e_1=1/5 on even n and4/5 on odd n, e_0=1-e_1,
s_1=2,s_0=1/2. With V=(-1)^n and P_odd=(1-V)/2,

    Phi*(q)=q, Phi*(p)=p,
    Phi*(q^2)-q^2=(9/4)q^2 P_odd,
    Phi*(p^2)-p^2=(9/4)p^2 P_even.                         (10)

Effects commute with q^2,p^2 because these preserve parity. The even/odd
q^2 coefficients are1 and13/4; for p^2 they are13/4 and1. This verifies
the parity placement independently of first-moment cancellation.

Write v=1/(2N+1), x=alpha^2 for the real displacement. Gaussian integration
of coherent projectors gives

    <V>=v exp(-2vx),
    <q^2 V>=(v^2/2)exp(-2vx),
    <q^2 P_odd>=(N+1/2+2x)/2-(v^2/4)exp(-2vx).            (11)

For completeness, at complex coherent amplitude beta,
<q^2 V>=[1/2-2(Im beta)^2]exp(-2|beta|^2). Integrating against the
positive thermal Gaussian centered at real alpha yields (11), also at N=0
by continuity. Thus the displaced-minus-undisplaced odd moment is

    x+(v^2/4)[1-exp(-2vx)] >= x.

Bob's raw input X^2 expectations coincide because U_A is supported in A.
The first-moment identities in (10) preserve the mixed qY term, while Y^2
is unchanged. Therefore the two target Bob second moments differ by at least

    d_2=(9/4)c^2 k^2 x.                                   (12)

This step retains all mode/complement correlations and does not identify
their joint state as a product.

To convert this unbounded observable to a bounded local effect, let
v_q=N+1/2 and S=2. Since q^4 preserves parity and all the effects are
functions of parity, Phi*(q^4)<=S^4 q^4 as positive forms. The input q
and Y marginal distributions are Gaussian, even though their joint state
need not factor. Their respective fourth moments are
3v_q^2+12v_q x+4x^2 and
3V_Y^2+12V_Y c^2k^2x+4c^4k^4x^2. Since q and Y commute, scalar functional
calculus gives X^4<=(8)[c^4k^4 q^4+Y^4]. Hence the sum of the two target
fourth moments is bounded by

    M_4=8{c^4k^4 S^4[6v_q^2+12v_q x+4x^2]
             +6V_Y^2+12V_Y c^2k^2x+4c^4k^4x^2}.          (13)

Set R=2M_4/d_2 and F=min(X^2,R)/R. This is a local effect,0<=F<=1.
The bound X^2-min(X^2,R)<=X^4/R shows target expectation separation at
least d_2^2/(4M_4). Each effect expectation error is at most epsilon,
so the two causal comparison errors yield

    epsilon_E >= [d_2^2/(8M_4)] min(1,E/E_*).              (14)

The factor8 here differs from factor16 in (6) because F is an effect,
whereas the clipped signed quadrature had only norm at most1.

For the same scaled continuum bumps and x=1/100,
v_q<=51/100, V_Y<=c^2k^2, and

    M_4<=(160378/625)c^4k^4,
    epsilon_E >= (81/328454144) min(1,800E/(17m)).          (15)

Thus the strongest explicit first-moment counterconstruction is itself
quantitatively separated using a finite-energy second-moment witness. This
does not assert that first and second moments detect every feedback channel.

## Duplication search, controls and ceiling

Local searches found K2145's special parity Weyl witness, K2234's general
existence proof and finite two-site consumer, but no displaced-thermal
adjacent-link/finite-tail method or explicit unequal-squeeze continuum bound.
External searches located the existing general measurement-causality and
unsharp-Luders literature; no novelty claim is made. Relevant primary anchors
include [Fewster--Verch](https://arxiv.org/abs/1810.06512) and
[Bostelmann--Fewster--Ruep](https://doi.org/10.1103/PhysRevD.103.025017).
These support the causal measurement distinction, not formulas(9)/(15),
which are derived here. No claim of exhaustive literature novelty clearance.

Independent finite controls should check: exact low-order coefficients of
(2) versus (1); coherent N=0 limit; first moment 2N+x; actual effect/squeeze
zero-link; universal Cauchy-Schwarz bound; cancellation counterconstruction;
identity plus complement cancellation; moment coefficients; clipped-witness
factor16; N,nu and physical-energy inequalities; low-energy common-vacuum
mixing; reference/record contractivity; and direct-channel triangle factor8.
Finite controls are not certification of continuum CCR/domain statements.
The first-moment construction uses positive forms and finite second moments;
the second-moment blindspot witness uses finite fourth moments of the chosen
Gaussian input marginals. No finite-difference null, spatial Fock
factorization or physical-energy-variance assumption is used.


## Reproduction and independent review

Independent internal specialist review rederived the displaced-thermal weights, complement cancellation, clipped witness, physical energy, both rational bounds and the same-target retained-drift consumer. The second-moment repair uses the stated Gaussian fourth moments. No mathematical blocker remained. Run `python tests/channel-swings/k2237_computable_causal_witness_probe.py`; default execution repeats finite exact algebra/arithmetic controls and eight mathematical-input faults and rejects stale note/probe/dependency hashes. `--write` refreshes the certificate. The finite tests illustrate the formulas and contrary cases; the continuum and all-reference claims rely on the written arguments.
