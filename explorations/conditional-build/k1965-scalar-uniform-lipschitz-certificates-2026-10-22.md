---
title: "K1965: Uniform scalar regularity and linear mesh certificates"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional independent mathematics; no GU identification, novelty or external certification
scripts:
  - tests/channel-swings/k1965_scalar_uniform_lipschitz_certificates.py
  - tests/channel-swings/k1965_scalar_uniform_lipschitz_certificates_probe.py
---

# K1965: Uniform scalar regularity and linear mesh certificates

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
result: uniform finite and continuum phase regularity, linear energy convergence and sharper feasible bound
carrier: fixed scalar two-characteristic tube with plateaux and zero area LAYER=toy CHIRALITY=N/A
pairing: Dirichlet gradient energy and Lebesgue marginals ON=three_free_intervals
real_structure: real signed controls and real phase lifts
grading: characteristic directions only; no physical chirality
action_owner: repository-construction -- fixed scalar control
target: unique optimal phase regularity and certified approximation MAP-TYPE=intertwiner
```

## 1. Question, scope and answer

Keep [K1942](k1942-complete-scalar-energy-duality-2026-10-22.md)'s complete
scalar problem and [K1963](k1963-effective-scalar-cut-certificates-2026-10-22.md)'s
aligned grids. The interval is I=[-3,3], the characteristic tube has width9,
physical c=1, phase +1 on[-2,-1], phase -1 on[1,2], boundary trace0 and total
area0. The free intervals have lengths1,2,1. At M=23/100 the strict witness
from K1944 has

    M0=22451259/97656250, U0=78227902689379/19531250000000,
    Delta=M-M0=19357/195312500.

Every finite-cut energy minimizer, including the all-grid minimizers, has a
UNIFORM Lipschitz bound independent of the number and size of its cuts:

    ||phi_h'||_infinity <= Lstar
      =1+4(U0-4)/(15 Delta)=110161564379/7258875000.       (1)

The unique full optimum is also Lipschitz. The effective energy enclosure
improves from K1963's O(sqrt(h)) to O(h). No smooth exact optimal pulse,
continuum optimum value or source-owned drive is asserted.

## 2. Normalize the small cuts before bounding their multipliers

Write phi=phi0+v in the zero-area Dirichlet space H of K1942. The baseline
phi0 is piecewise affine, has energy4 and is gradient-orthogonal to H.
Replace a cut by its complement and reverse its sign if necessary so its
measure s is at most3. Null cuts are vacuous. Its capacity satisfies C(A)>=3s.
Use the normalized constraint

    ell_A(phi)=sign integral_A phi/C(A) <= M/2.

The strict witness satisfies every such constraint at most M0/2. Finite
projection/KKT supplies nonnegative multipliers lambda_A and

    v_h=-sum_A lambda_A g_A,

where g_A is the H representer of ell_A. This remains true when normals are
linearly dependent, using a conic basis. Let v0 be the strict witness's phase
minus phi0; ||v0||²=U0-4. Pair stationarity with v0-v_h and use active contact:

    (Delta/2) sum lambda_A
      <= <v_h,v0>-||v_h||²
      <= ||v_h|| sqrt(U0-4)-||v_h||² <=(U0-4)/4.

Consequently sum lambda_A <= S=(U0-4)/(2 Delta). This is a uniform bound on
NORMALIZED multipliers. Unnormalized small-cut multipliers need not obey it.
The last inequality is completion of a square, not a Slater assertion without
a numerical margin. A boundary-only constraint with zero representer cannot
be active against this strict witness.

## 3. Green-kernel bound and continuum regularity

Let G be the unprojected Dirichlet inverse of -d²/du² on the three intervals,
h=G1, and H0=integral h=5/6. Then ||h||_infinity=1/2 and
||h'||_infinity=1. For f=sign 1_A/C(A), restricted to free intervals,
||f||_1<=1/3. The one-dimensional Green kernel has |partial_u G(u,y)|<=1.
The projected representer is

    g_A=Gf-mu h, mu=integral(h f)/H0,
    |mu|<=1/5, ||g_A'||_infinity<=1/3+1/5=8/15.

Thus ||v_h'||_infinity<=8S/15 and (1) follows from ||phi0'||_infinity=1.
Extend each v_h by zero over the plateaux; it is continuous at their endpoints,
so the same global Lipschitz constant applies across every interface.
K1942's nested-grid convergence to the unique full phase, together with this
uniform bound, proves phi_star is Lipschitz with the same constant.

A further regularity consumer does not require a new numerical bank. On the
OPEN free intervals, g_A''=-f+mu, so its total L1 norm is at most
1/3+4/5=17/15. Therefore the sum of variations of v_h' over those intervals
is at most17S/15. Weak compactness of finite measures and strong H1 convergence
pass this bound to the distributional second derivative of phi_star on each
free interval. This is piecewise BV regularity of its derivative; endpoint
jumps are excluded from that bound, and no C1 or H2 regularity is claimed.

## 4. Linear amplitude and energy certificates

K1963's same-cell coupling gives, for an arbitrary measurable cut of smaller
mass s, a phase averaging error at most s L h for an L-Lipschitz phase.
Its unchanged window-capacity error is at most2hs. Layer cake, capacity
concavity and C(A)>=3s give the explicit amplitude allowance

    epsilon_h=(2/3)h(L+M).                               (2)

This replaces sqrt(h J) by h L; it does NOT drop the capacity error.
For a finite-grid minimizer use L=Lstar, and mix with the strict pulse using

    theta_h=epsilon_h/(Delta+epsilon_h),
    J_h <= J_star <= U_h=(1-theta_h)J_h+theta_h U0.

The repaired amplitude is exactly M. In particular

    U_h-J_h <= [(2/3)(Lstar+M)/Delta](U0-4)h.             (3)

This is a computable mesh choice for any requested energy tolerance. With
K1963's exact graph separation it avoids exponential cut enumeration, but
no polynomial-time optimization or bit-complexity bound is inferred. Phase
squared H1 error is at most U_h-J_h and squared uniform error at most half
that quantity, by K1942. The phase errors themselves are O(sqrt(h)).
A known feasible finite phase can use its sharper actual L in (2), even if
it is not a finite minimizer; its own energy then supplies a valid repaired
upper, while only an actual dual certificate supplies a lower.

## 5. Exact consumer on the existing 96-cell graph

The two active halfcuts +/-7/16 have nonnegative multipliers and exact KKT
contact. K1963's integer flow/cut construction verifies all2^96 grid unions
at h=1/16, so this phase is indeed the finite all-grid minimizer. Independent
piecewise ODE integration gives

    J_h=1850592923/462545000,
    L_h=2383957/2312725,
    epsilon_h=777569/14801440.

The resulting original-budget existence bound is

    J_star <=4687863248719336527/1170426590666000000,
    U0-U_h=11772695745864735479/1428743396809082031250000.

The improvement over U0 is about8.24e-6 and exceeds K1963's coarse repaired
improvement. The new upper is existence through the complete cut theorem;
new pulse coefficients are not serialized. K1942's stronger lower bound
remains valid; the gap remains open. Smoothing with arbitrarily small slack
uses K1944's existing strict-feasibility argument, not exact smooth attainment.

## 6. Verification and boundaries

The producer verifies16 exact obligations, including two exact integer
flow/cut certificates, actual slopes, normalized multiplier masses and rational
repair bounds. The separate ODE probe verifies14 controls and detects four
mathematical faults: missing mean projection, altered multiplier, understated
actual slope and insufficient repair mixing. Hash checks are separate.
The symbolic square check initially compared expanded and unexpanded forms;
normalizing their difference fixed the harness before the green baseline.
Uniform regularity, convergence and BV claims are the analytic proofs above,
not conclusions from these finite cases. No external expert or proof-assistant
certification is claimed.

[Korman, McCann and Seis](https://arxiv.org/abs/1307.7774) are established
capacity-transport duality context; the abstract was rechecked. No novelty
claim. SC-OP-04 ASSERTS candidate grammar and SC-MAS-01 ASSERTS a stylized
local mass toy; neither supplies this control. SC-META-53 remains UNCERTAIN.
LT-SM8/LT-GR6b/AC-F1, source, physics and canon verdicts stay unchanged.
The remaining scalar question is a matching continuum certificate or an
implemented exact active-set search, not the existence of an effective rate.
