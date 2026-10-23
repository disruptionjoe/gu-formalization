---
title: "K1980: A constructive minimum-norm optimal measurable pulse"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1980_constructive_minimum_norm_pulse.py
  - tests/channel-swings/k1980_constructive_minimum_norm_pulse_probe.py
---

# K1980: A constructive minimum-norm optimal measurable pulse

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
result: strongly convergent clipped integral construction, explicit marginal residual bounds and canonical pulse symmetry
carrier: fixed scalar width9 characteristic strip and K1969 optimal phase LAYER=toy CHIRALITY=N/A
pairing: real L2 strip norm and normalized Lebesgue marginal projections ON=characteristic_strip
real_structure: bounded real measurable pulses; no smoothness assumption
grading: characteristic directions, not source chirality
action_owner: repository-construction -- fixed conditional scalar model
target: amplitude-preserving recovery of a canonical optimal pulse MAP-TYPE=intertwiner
```

## 1. Exact object and construction

Use the optimal phase phi_star of
[K1974](k1974-scalar-excursion-separation-2026-10-23.md), with M=23/100.
Its exact algebraic definition, full-cut feasibility, optimal Dirichlet energy
and bounded-measurable existence are reused dependencies. The new result is a
specific STRONGLY CONVERGENT integral algorithm selecting one optimal pulse,
not another phase or cut certificate. It does not output a closed-form pulse
array, a quadrature certificate, or an exactly feasible finite iterate.

Let D={(u,z):-3<=u<=3, u<=z<=u+9}, with area 54, and H=L2(D;R).
For ell(z)=|[-3,3] intersect[z-9,z]| define the orthogonal projections

    (P v)(u,z)=(1/9) int_u^(u+9) v(u,w) dw,
    (Q v)(u,z)=(1/ell(z)) int_(max(-3,z-9))^(min(3,z)) v(w,z) dw,
    g(u,z)=2 phi_star(u)/9.                                  (1)

Ignore the measure-zero endpoints where ell=0. Fubini and Jensen prove
P,Q bounded orthogonal projections on H, even where ell approaches zero.
The exact feasible set is C={|v|<=M, Pv=g, Qv=0}; it is nonempty by K1974,
closed and convex. It has a unique minimum-H-norm element v_dagger. This
secondary choice does not change the scalar Dirichlet optimum: every v in C
has the same optimal phase and zero opposite phase.

For epsilon>0 start v_(epsilon,0)=0 and iterate

    v_(epsilon,k+1)=clip_[-M,M](((2I-P-Q)v_(epsilon,k)+g)/(2+epsilon)). (2)

Every iterate satisfies the amplitude bound EXACTLY. Both marginal equations
are limits, not constraints satisfied at each finite step.

## 2. Direct proof of contraction and strong convergence

Consider on the amplitude box

    F_epsilon(v)=||v||^2/2 + (||Pv-g||^2+||Qv||^2)/(2epsilon). (3)

Its Hessian is I+(P+Q)/epsilon. Because 0<=P,Q<=I, its spectrum lies
in[1,1+2/epsilon]. Equation(2) is projected gradient with step
 tau=epsilon/(2+epsilon). Before clipping its linear part is
(2I-P-Q)/(2+epsilon), positive semidefinite with norm at most

    q_epsilon=2/(2+epsilon)<1.                              (4)

Clipping is the orthogonal projection onto the box and is nonexpansive in H.
Therefore(2) is a contraction, has a unique fixed point v_epsilon, and
that fixed point is exactly the minimizer of(3), by the convex variational
inequality. Set B=M sqrt(54). Comparing with v_dagger gives

    ||v_epsilon||<=||v_dagger||<=B,
    r_epsilon:=sqrt(||Pv_epsilon-g||^2+||Qv_epsilon||^2)
                 <=sqrt(epsilon)||v_dagger||<=B sqrt(epsilon),
    ||v_(epsilon,k)-v_epsilon||<=B q_epsilon^k.              (5)

As epsilon decreases to0, the bounded family has weakly convergent
subsequences. Every weak limit is in C because the residual vanishes and
closed convex sets are weakly closed. Lower semicontinuity and(5) force the
limit to be the UNIQUE v_dagger. Moreover limsup||v_epsilon||<=||v_dagger||,
so weak convergence upgrades to strong convergence in the Hilbert space.
Every sequence epsilon->0 therefore converges strongly to v_dagger.

For an explicit single sequence take epsilon_n=1/n^2 and the least integer
k_n>=0 satisfying (2/(2+epsilon_n))^k_n<=epsilon_n. Then
v_(epsilon_n,k_n) -> v_dagger STRONGLY. This is a constructive definition
by known integrals, clipping and a prescribed rational stopping bound. No
unproved weak-to-strong inference or smooth representative is used.

This is an application of standard regularization/projection principles,
not a novelty claim. Related primary literature:
[regularized gradient-projection methods in Hilbert space](https://pmc.ncbi.nlm.nih.gov/articles/PMC5222927/).
The proof here supplies the actual strip operators and does not import a
convergence theorem without verifying its hypotheses.

## 3. Executed consumers: residuals, integration error and symmetry

Since ||(P,Q)||<=sqrt(2), finite iterates have the rigorous residual bound

    r_(epsilon,k)<=B(sqrt(epsilon)+sqrt(2)q_epsilon^k).       (6)

The realized phase phi_v(u)=(1/2)int v(u,z)dz and opposite phase
psi_v(z)=(1/2)int v(u,z)du obey

    ||phi_v-phi_star||_(L2[-3,3]) <=(3/2)r_(epsilon,k),
    ||psi_v||_(L2[-3,12]) <=sqrt(3/2)r_(epsilon,k).          (7)

Indeed ||Pv-g||_H^2=(4/9)||phi_v-phi_star||^2 and
||Qv||_H^2=int 4psi_v(z)^2/ell(z) dz, with ell<=6.
These are quantitative MARGINAL errors, not an H1 phase/Dirichlet energy
estimate, exact plateaux, or a certified physical protocol at finite k.

If each evaluated update has H-error at most eta AFTER clipping, contraction
gives error at step k at most B q^k+eta/(1-q). Approximating the pre-clipped
update to eta suffices because clipping is nonexpansive and preserves the
amplitude bound. For epsilon_n and k_n above, eta_n<=epsilon_n^2/(2+epsilon_n)
makes eta_n/(1-q)<=epsilon_n. Thus certified quadrature with these tolerances
would preserve strong convergence. Such quadrature is a remaining implementation
obligation; the finite fixtures below are not its certificate.

The isometric involution Sv(u,z)=-v(-u,9-z) preserves D, the box and both
constraints because phi_star is odd. It commutes with the iteration and its
forcing. Starting at 0, EVERY exact iterate and v_dagger satisfy Sv=v.
Uniqueness provides the same symmetry conclusion independently.
K1974's forced saturation also applies to v_dagger: on 3<z<6 it equals+M
for-3<u<-t and-M for t<u<3. Consequently

    M^2(18-6t) <= ||v_dagger||_H^2 <=54M^2.                (8)

Its minimum-norm selection is not a smoothness theorem. K1977 still proves
that no C1 pulse attains this phase. The unrestricted smooth exact-endpoint
infimum remains open.

## 4. Checks, contrary cases and next boundary

The producer constructs13 exact polygon-cut strip cells, a feasible rational
TEST marginal, and 192 exact two-start contraction checks. The separate probe
computes cell areas by polygon clipping, independently assembles the weighted
orthogonal projections, solves four exact finite quadratic programs and checks
the iterate error against their true optima. Its20 obligations pass; four
changed area/column sign/step/amplitude inputs are rejected after baseline.
The fixture marginal is NOT phi_star. Finite fixture results are algorithm
controls; sections1-3 establish the continuum construction analytically.

Strongest overclaim: finite residual control mistaken for exact plateau or
Dirichlet energy certification. Equations(6)-(7) expressly do not imply that.
Strongest contrary case: vanishing column length; conditional expectation
stays bounded in the correct area-weighted Hilbert norm. Weakest remaining
implementation seam: certified continuum integrations and an effective
strong-norm error to v_dagger; no such convergence modulus is claimed.
A closed analytic pulse formula or certified adaptive transport could still
be useful, but existence of a canonical strongly convergent construction is
no longer missing. This is independent scalar mathematics; SC-META-53 remains
UNCERTAIN and source/physics-ledger/canon verdicts do not change.
