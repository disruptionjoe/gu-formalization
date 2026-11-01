---
title: "K2452 Analytic mixed inverses on two original hook families"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: "linear analytic inversion for bounded passive degree and an eleven-variable scalar family; no full mixed or nonlinear convergence"
---

# K2452 Analytic mixed inverses on two original hook families

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
result: K2452
carrier: original repeated-polar hooks and raw105 symmetric receivers in seven transverse E and seven passive W coordinates LAYER=toy CHIRALITY=N/A
pairing: ordinary coefficient l1 norm in one fixed adapted coordinate system ON=declared_carrier
real_structure: real original split-metric hooks over the fixed real embedding of Q(sqrt2), or complex coefficients for analytic estimates
grading: homogeneous field degree d, receiver degree d-1, and passive polynomial degree
action_owner: repository-construction -- supplied conditional hook model
target: analytic linear inverses on two exact invariant subfamilies MAP-TYPE=evaluation
```

## Result and preflight

The original full mixed operator has analytic linear inverses on two infinite
families: all compatible forcing with a fixed finite passive-degree bound,
and arbitrary scalar forcing in eleven explicitly identified coordinates.
The latter allows unbounded degree in four passive coordinates and is solved
inside the full ambient ordinary Euler kernel. These are original-operator
statements, not a conclusion from finite ranks or a transverse replacement.

The object is K2449's conditional repeated-polar/boundary-ideal construction,
not Weinstein's unconstructed physical quotient or native action. Source
SC-ACT-01 and SC-GEO-55 remain ASSERTS and SC-META-53 remains UNCERTAIN; no source,
ledger or canon change is implied. Retrieval used K2437's original witness
and scalar normalization, K2443's actual ordinary quantitative estimate,
K2446's augmented diagonal and mixed filtration, and K2449's full boundary
adjoint. The competing unrestricted quotient estimate remains open. A large
inverse on a chosen primal subspace would not refute the full estimate:
alternative generators must also be excluded by a full dual certificate.

## 1. Fixed finite passive degree

Let L_d=(D,J_d), J_d=(4/d)Jstar, on actual degree-d fields, d>=4.
Use precisely the original generator bank and boundary restriction from
K2449. Write L_d=L0+N, with L0 the transverse diagonal. K2446 provides a
coefficientwise-in-W compatible diagonal inverse D_d with

    ||D_d|| <= d C^d,       ||N|| <= B d^2,

for fixed C>=1 and B>=0 after fixed norm and generator constants are
absorbed. D_d preserves every passive monomial. If an off-range extension is used for
bookkeeping, choose the transverse compatible-range projection separately
for each fixed W monomial; a global projection that mixes W degrees is not
used. Each term of N contains at
least one W derivative: ordinary D_W and scalar EW terms lower passive
degree by one; scalar WW terms lower it by two. Thus N strictly lowers
passive degree, whereas D_d preserves it. This is an invariant filtration of
the actual mixed operator, not only of an auxiliary triangular matrix.

For compatible forcing F of passive degree at most m, the same sequential
compatibility argument as K2437/K2446 gives the exact inverse

    R_d,m F = sum_(j=0)^q (-D_d N)^j D_d F,
    q=min(m,d-1).

Every successive leading ordinary residual satisfies the original transverse
trace/double-divergence conditions; the scalar residual is unrestricted.
Thus diagonal inverses are used on their actual compatible ranges. No
claim is made that independently prescribed off-range banks are solvable.
The result is still of passive degree at most m and belongs to the original
allowed field space, including vanishing of repeated coefficients at E=0.

The inherited quantitative estimates now give

    ||R_d,m F|| <= d C^d sum_(j=0)^m (B d^3 C^d)^j ||F||
      <= (m+1) max(1,B)^m d^(3m+1) C^((m+1)d) ||F||.       (1)

For every fixed m this is geometric in d. For example d^a<=2^(ad) gives a
valid single constant

    C_m=2^(3m+1) (m+1) max(1,B)^m C^(m+1),
    ||R_d,m|| <= C_m^d.                                  (2)

Consequently compatible analytic forcing that is polynomial in W with a
fixed finite degree m has an analytic full mixed linear preimage on a
smaller neighborhood. The finitely many lower homogeneous degrees are
outside the d>=4 top-jet assertion and must be supplied separately if part
of the application. No uniform bound in m is asserted. Letting m grow with
d recovers the unresolved loss rather than proving unrestricted analytic
inversion. Nonlinear products can increase passive degree, so this family
does not close the nonlinear recursion.

## 2. An eleven-variable ordinary-null scalar family

Use the original serialized K2437 hook h, with c=9012/8519:

    h_11,2,11=1,       h_11,4,11=c,
    h_11,11,2=-1,      h_11,11,4=-c,
    h_13,2,13=-1,      h_13,4,13=-c,
    h_13,13,2=1,       h_13,13,4=c.

All other entries vanish. It is repeated and polar to every original K_i.
For an original covector xi, its ordinary Euler symbol has exactly the
possibly nonzero entries

    (A_xi h)_11,11=2(-xi_2+c xi_4),
    (A_xi h)_13,13=-2(-xi_2+c xi_4),
    (A_xi h)_2,11=xi_11,    (A_xi h)_4,11=c xi_11,
    (A_xi h)_2,13=-xi_13,   (A_xi h)_4,13=-c xi_13.

Here eta_2=eta_11=eta_13=-1 and eta_4=1, with the raw symmetric
receiver convention. Therefore its exact covector kernel is

    S={xi: xi_11=xi_13=0, -xi_2+c xi_4=0}, dim S=11.       (3)

The original adapted E covectors all lie in S. Four further original
covectors are e1,e3,e10,e12, which correspond, up to nonzero fixed signs,
to passive coordinates z0,z2,z3,z5. Thus scalar polynomials in

    (y0,...,y6,z0,z2,z3,z5)                               (4)

have all differential covectors in S. This is a restriction of dependence,
not a restriction obtained by evaluating an arbitrary field at z=0.

For xi in S, contraction of h in each of its three slots with eta*xi
vanishes, not merely the symmetric sum defining A_xi h. In the original
polarization formula

    F(A,B)_ij=(2/3) sum_(a,c) eta_a eta_c
                  [A_aic B_ajc+B_aic A_ajc]
             -(2/3) sum_(b,c) eta_b eta_c
                  [A_ibc B_jbc+B_ibc A_jbc],

every metric-weighted contraction against eta_i xi_i eta_j zeta_j, with xi,zeta in S, consequently
contains a vanishing contraction of h. It follows that all original scalar
second-order coefficients b_rst(h) with r,s in (4) vanish, for every t.
This applies to the full original K(x), with no mixed terms discarded by
assumption. Also D(h f)=0 for every f depending only on (4).

On this eleven-variable ring Jstar(h f)=a dot grad f is a constant
first-order derivative, where a is the restriction of the original ambient
first-order coefficient bank. The known transverse coefficient is

    a_y1=2253/2 != 0,       a_y2=2253/17038.

The full original first-order bank has no other nonzero coefficient, as
checked independently on all fourteen adapted covectors. Thus no passive
first derivative was omitted. Put t=y1, a0=a_y1, and let u denote the other
ten coordinates in (4). Writing b for their coefficient vector, define

    (S_h g)(t,u)=(t/a0) integral_0^1
                     g(s t,u+(b/a0)(s-1)t) ds.            (5)

This is integration along a fixed constant vector field, with zero initial
value at t=0. Hence a dot grad S_h g=g and S_h g is divisible by y1.
Thus h S_h g is an allowed repeated-polar field and vanishes on E=0.
The construction preserves precisely the eleven-variable ring.

For g of homogeneous degree d-1 the actual inverse is

    V_d=(d/4) h S_h g,   D(V_d)=0,   J_d(V_d)=g.           (6)

For an analytic series the multiplier is degree-dependent: apply d/4 to
each degree-(d-1) forcing coefficient (equivalently apply (Euler+1)/4 to
the scalar forcing before S_h). Replacing this by one constant factor
would invert the wrong scalar operator.

With Gamma=1+sum_j |b_j/a0|>=1, coefficient-l1 norms satisfy

    ||S_h g||_1 <= Gamma^(d-1) ||g||_1/|a0|,
    ||V_d||_1 <= d ||h||_1 Gamma^(d-1) ||g||_1/(4|a0|).    (7)

Expand the integral substitution monomial by monomial: each shifted u_j
factor costs at most (1+|b_j/a0|), all bounded by Gamma; integration on
[0,1] cannot enlarge this absolute coefficient bound. Here Gamma=8520/8519 and ||h||_1=4(1+9012/8519), so this scalar
family has an explicit small fixed radius loss, rather than the generic
existence constant of (2). This proves a fixed
analytic radius loss and covers arbitrary analytic dependence in all four
selected passive coordinates, not just finite passive polynomials.

## 3. Controls, postflight and limits

The exact probe reconstructs original K and h, checks (3) on every original
ambient covector, checks all three slot contractions on the eleven actual
adapted covectors, and checks every original b_rst there. Nonzero fixtures
use passive dependence and the primitive, ordinary Euler, scalar equation,
4/d normalization and boundary ideal. A forbidden passive direction has a
nonzero original ordinary Euler symbol, preventing extension to all W by
silently reusing the transverse witness. The finite polynomial fixtures
verify implementation; (1)--(7) are the all-degree proofs.

No full K2449 quotient bound follows: (1) has m-dependent constants and
(6) solves only zero ordinary forcing with the displayed scalar dependence.
Neither family proves a nonlinear majorant, convergent Gram/sigma/Euler
construction, smooth stationary GU field, physical quotient or source-native
identification. The strongest next discriminator remains an estimate on the
full original joint quotient, or a full-bank dual obstruction; more finite
ranks are not evidence for either. Internal independent review is not
external-expert or proof-assistant certification.

[Exact probe](../../tests/channel-swings/k2452_partial_analytic_hook_inverse_probe.py),
[report](../../lab/process/k2452-partial-analytic-hook-inverse.json).
