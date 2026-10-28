---
title: "K2198 Finite detector certificates locate the optimizer and enclose its tail"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied positive Fock instrument at fixed positive rational squeezes and nonzero interior contrast; output field energy only
scripts:
  - tests/channel-swings/k2198_detector_profile_certificates_probe.py
---

# K2198 Finite detector profile certificates

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2198 finite optimizer-coordinate and whole-tail geometric certificates
carrier: fixed positive scalar Fock vacuum and photon-added signal with binary diagonal local occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and free vacuum output energy ON=declared_carrier
real_structure: positive square-root diagonal Kraus followed by one real squeeze per reported outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction: supplied free Hamiltonian and instrument class
target: finite-budget lower energy envelope and inverse contrast bound MAP-TYPE=intertwiner
```

## Result and scope

Finite feasible upper and rational dual lower energy certificates enclose the
unique fixed-squeeze optimizer coordinate by coordinate. They then give
explicit two-sided bounds on EVERY complementary tail ratio, including a
computable entry index and prefactor. Refinement eventually certifies these
bounds. This does not certify an arbitrary shooting trajectory or supply
practical optimization complexity or joint-squeeze uniqueness.

A concrete certificate at s1=105488613/10^8, s0=86390048/10^8, d=1/2 proves

    (1/200) 9^-m <= 1-e_(2+m) <= (1/8) 4^-m,  m>=0,

for the true unique optimizer at those FIXED squeezes. The finite input is
K2174's already-feasible witness, converted to K2196's rational dual. This is
a new optimizer-profile enclosure, not a new energy bracket or a certificate
that those squeezes jointly minimize. All infinite competitors, including cap
faces, remain in the fixed-squeeze minimization.

The supplied positive Fock binary diagonal Kraus instrument has one squeeze
per outcome and output FIELD energy as cost. Apparatus/preparation/clock/reset
and total work remain separate. SC-META-53 remains UNCERTAIN; source,
ledger0.263, LT-SM8/LT-GR6b, canon and physical quotient are unchanged.
No novelty or external-expert/proof-assistant claim.

## 1. Finite dual gap gives optimizer coordinate boxes

Use K2194/K2196 p_n=(3/4)4^-n, C=40/3, A(s)=41s²/6+3/(2s²), q_n=3n-1.
Fix positive rational s1,s0 and rational 0<d<3/4. Let D be ANY valid K2196
finite rational dual, U a certified feasible upper energy, epsilon=U-D.
For any feasible effect of energy at most U, the nonnegative AM-GM/cap gap
decomposition bounds each individual branch edge by epsilon:

    Cs_j(n+1)p_n/(8u_j) [2u_j sqrt(e_(j,n))-sqrt(e_(j,n+1))]^2 <= epsilon,

where e_(1,n)=e_n and e_(0,n)=1-e_n. This follows by expanding the original
edge AM-GM gap, with x_(n+1)=p_n e_(n+1)/4; every remaining cap term is
nonnegative. Free slopes u_j must be positive, but need not come from a
feasible profile. In particular this inequality holds at the true optimizer.

Put delta_j=sqrt(8u_j epsilon/[Cs_j(n+1)p_n]),
L_j=(1+2u_j)delta_j, a=4u1² and b=4u0². The caps imply

    |e_(n+1)-a e_n|<=L_1,
    |(1-e_(n+1))-b(1-e_n)|<=L_0,
    |(a-b)e_n-(1-b)|<=L_1+L_0.                         (1)

If a!=b, intersect the interval with center(1-b)/(a-b) and radius
(L_1+L_0)/|a-b| with[0,1]. This is a rigorous e_n box. Use the first
inequality to enclose e_(n+1), or another edge certificate. Square roots
are computed with outward rational bounds. A degenerate a=b does not give
a coordinate box; refine the certificate rather than divide by zero.

## 2. Why refining certificates actually locates coordinates

For any sequence U_m-D_m->0, a fixed true optimizer edge has positive
alpha=sqrt(e_(j,n)) and beta=sqrt(e_(j,n+1)). Its gap forces

    f(u_m)=(2u_m alpha-beta)^2/u_m ->0.

The function f(u)=4alpha²u-4alpha beta+beta²/u is coercive on(0,infinity)
and vanishes only at u*=beta/(2alpha). Thus even freely selected dual
slopes converge to the true tangent slopes. K2194's strict monotonicity gives

    a*-b*=(e_(n+1)-e_n)/[e_n(1-e_n)]>0.

Consequently the centers and radii in(1) converge to e_n and0. Interior
boxes for e0,e1 then enclose the TRUE multiplier, independently of the
chosen dual multiplier, through the n=0 stationary equation:

    eta=C/4 [s1 sqrt(e1/e0)-s0 sqrt((1-e1)/(1-e0))]-DeltaA/2. (2)

This uses the fixed-squeeze uniqueness/interiority and monotonicity theorems;
none of those is inferred from the finite witness.

## 3. Two-sided geometric bounds for every tail ratio

Let a_n=sqrt(e_n), b_n=sqrt(1-e_n), r_n=b_(n+1)/b_n in(0,1).
K2194's exact stationary recurrence gives, for n>=1,

    1/r_(n-1)+(1+1/n)r_n/4=k_n,
    k_n=k+(s1/s0)[a_(n-1)/a_n-1+(1+1/n)(a_(n+1)/a_n-1)/4]+c/n,
    k=[5s1/4-(DeltaA-3eta)/C]/s0,
    c=s1/(4s0)-(DeltaA/2+eta)/(Cs0).                     (3)

Suppose finite certificates give e_N>=L>0 and intervals for k,c. Monotonicity
and the caps imply, for n>=N+1,

    Kminus=k_lo-(s1/s0)(1-sqrt(L))-max(-c_lo,0)/(N+1),
    Kplus=k_hi+s1/(4s0)(1+1/(N+1))(1/sqrt(L)-1)+max(c_hi,0)/(N+1),
    Kminus<=k_n<=Kplus.                                 (4)

Use outward rounding throughout. Set q=(1+1/(N+1))/4. If Kminus>1+q,
choose rational 0<sigma<=rho<1 satisfying

    1/sigma+sigma/4>=Kplus,  1/rho+q rho<=Kminus.        (5)

Then sigma<=r_n<=rho for ALL n>=N. To prove it, the backward recurrence
sandwiches r_(n-1) between phi_minus(r_n) and phi_plus(r_n), where

    phi_minus(t)=1/(Kplus-t/4), phi_plus(t)=1/(Kminus-q t).

Both are increasing contractions of[0,1] into itself: denominators exceed1,
and derivatives are at most1/4 and q<1. Start at any arbitrarily remote
actual ratio in(0,1), iterate backward, and pass to the fixed-point bounds.
On[0,1], 1/t+q t decreases strictly. Thus(5) puts sigma below the lower
fixed point and rho above the upper one. Multiplying ratios proves

    (1-e_N)sigma^(2m)<=1-e_(N+m)<=(1-e_N)rho^(2m).       (6)

No asymptotic prefactor is guessed, and no finite shooting prefix is treated
as an infinite feasible trajectory.

## 4. Termination and useful tail consumers

K2194 proves k>5/4 and e_N->1, with finite c. Some finite N therefore meets
the strict condition Kminus>1+q for exact inputs. Section2 proves sufficiently
refined finite certificates resolve it. Dovetail N with K2196's complete
finite-dual search and the inherited feasible-upper approximation; ensure the
dual cutoff exceeds tested N. A finite rational sigma,rho exists whenever the
strict condition holds. This proves termination, not an efficient search rate.

Let f_N=1-e_N and t=rho²/4. For the complement y_n=p_n(1-e_n), (6) gives

    sum_(n>=N) y_n <= p_N f_N/(1-t),
    sum_(n>=N)(n+1/2)y_n <= p_N f_N[(N+1/2)/(1-t)+t/(1-t)^2],
    sum_(n>=N)(n+1)sqrt(y_n y_(n+1))
       <= p_N f_N rho/2 [(N+1)/(1-t)+t/(1-t)^2].        (7)

Lower counterparts use sigma and a certified lower bound on f_N. These
convergent geometric sums supply explicit moment/coherence error budgets.

## 5. Concrete finite certificate and verification

The probe reuses K2174's rational feasible witness and exact contrast repair,
with its actual full-tail interval energy. Its free slopes are outward rational
approximations to witness ratios. Equation(1), not closeness of the witness
in a plot, proves the optimizer boxes. The n=0 dual multiplier is merely a
chosen rational; the true multiplier interval comes separately from(2).
Exact rational checks establish e2 in[7/8,199/200], Kminus>13/6 and
Kplus<37/12. Thus N=2, sigma=1/3,rho=1/2 satisfy(5), yielding the displayed
whole-tail theorem. The energy values are reused inputs; their difference
is a fixed-squeeze certificate gap, not a sharper global energy bracket.

Controls check the original AM-GM square coefficient, exact coordinate
identity, recurrence-to-k_n algebra, barrier rejection, tail sums and the
actual finite certificate. Baseline-first faults change the gap factor,
effect ratio, recurrence coefficient, barrier direction or multiplier sign;
crashes are not detections. Universal proofs, rational finite certificate,
and inherited inputs remain distinct. Next work can exploit profile boxes
and tail envelopes in a practical certified optimizer or investigate joint
squeeze uniqueness. An efficient solver and physical apparatus remain open.
