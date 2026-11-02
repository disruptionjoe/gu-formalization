---
title: "K2486 Exact noisy-flag filtering, correlations and renewal costs"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional mathematical result on the stated original or supplied carrier; no native GU or measured implementation claim"
---

# K2486 Exact noisy-flag filtering, correlations and renewal costs

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
result: K2486
carrier: original 108-dimensional positive-Hilbert programs and explicitly supplied canonical instruments LAYER=toy CHIRALITY=N/A
pairing: positive trace or actual-law expectation as explicitly distinguished below ON=declared_carrier
real_structure: complex adjoint for quantum matrices; real probabilities for classical laws
grading: target and complement or absorbing classical trial histories
action_owner: repository-construction -- supplied conditional mathematical models
target: Fresh noisy-flag filtering, sharp fidelity and complete stopped costs MAP-TYPE=evaluation
```

## Result and Layer 0

Fresh independent diagonal flags admit an exact all-pass filtering law on the original coherent Q/T verifier. Conditional output error tends to zero below one-half flag noise, while output yield vanishes. A full-carrier worst-sector crossover, sharp finite-cap guarantee and stopped/renewal costs follow. Correlated flags with identical marginals exhibit a permanent error floor, making freshness a load-bearing assumption.

The operative carrier is the original positive-Hilbert108 program, with imported trace probabilities and ideal coherent controls. SC-META-53 remains UNCERTAIN; ledger0.263 LT-SM8/LT-GR6b still owe native interacting quotient and domain bridges. No source, ledger, canon or physical credit changes; eta is a prospective assumption, not measured calibration. This result certifies a conditional filtering calculation, not an unknown producer or hardware implementation.

## Prior-object search and scope

Loaded GU AGENTS, semantic routing, Layer0, research posture, verification and
contribution requirements. Inspected K2447, K2454, K2484 and K2484's actual
probe. Searched conditional-build records for noisy/mixed flags, purity,
controlled Householders, elementary gates and entanglement cost. K2484 is
the located original noisy-flag result: it identifies per-use outcome-label
swap error and uses general complete-instrument error accumulation. It does
not derive the same-copy fresh-noise dynamics below. K2090's apparatus
purity bound and K2484's coherent circuit remain inherited, not new.

The new contribution is an exact noisy instrument calculation on the
original Q/T carrier, sharp finite-n filtering, a genuine worst-sector
crossover, reset/correlation countercontrols and exact stopped cost. It
does not compile elementary gates, certify noise, or show arbitrary noise
is harmless. The generic complete-instrument error bound remains necessary
for unmodelled gate, storage, leakage, coherent-control or reset defects.

## 1. Exact model, instrument, Jordan decomposition

At each test use an independently refreshed flag
tau=diag(p,e), e in[0,1/2), p=1-e. Require its state to be independent of the
system, retained reference, previous flags and history. All other Q/T
coherent controls, uncomputation and binary readout are exact. Apply
U_R=R tensor X+(I-R) tensor I and record accept iff flag=1. The accepted
CP map is

    A_R(rho)=p R rho R+e (I-R)rho(I-R).

The rejected map interchanges p,e. This is exactly the ideal projective
instrument followed by an independent classical outcome swap. Merely
knowing its acceptance effect pR+e(I-R) would not fix this instrument.
Its per-test complete half-diamond error from the ideal instrument is e,
as K2484 already proves. We model that particular error exactly instead of
spending it anew in a generic additive remainder.

Use R_1=Q,R_2=T,R_3=Q,..., stop at the first recorded rejection. On the
original full carrier, K2454's rank and angle data imply the orthogonal
reducing decomposition

    P: dimension1, Q=T=1;
    H_theta=span(z,y): dimension2,
      Q=diag(1,0), T=[[r,sqrt(r(1-r))],[sqrt(r(1-r)),1-r]];
    A=ranQ intersect kerT: dimension8, Q=1,T=0;
    B=kerQ intersect ranT: dimension10, Q=0,T=1;
    N=kerQ intersect kerT: dimension87, Q=T=0.

Here r=27/127 or15/67, both in(0,1/2); Z=|z><z|,
Y=|y><y|. The dimensions sum to108 and are derived from rankQ10,
rankT12, one common vector and one nontrivial angle block. These are the
two-effect Q/T sectors; do not import K2482's different53-dimensional
dark space from its other setting family.

## 2. Exact finite-n all-pass effect and sharp fidelity

Let E_n=(A_Q^* A_T^* ... A_Rn^*)(I), so Tr(E_n rho) is all-pass
probability; composition order is the adjoint of chronological maps. Set

    M=[[p*r, p*(1-r)], [e*(1-r), e*r]],
    d_n=(d_z(n),d_y(n))^T=M^(n-1)(p,e)^T, n>=1.

Then exactly

    E_n=p^n P+d_z(n)Z+d_y(n)Y
        +p^ceil(n/2)e^floor(n/2) A
        +e^ceil(n/2)p^floor(n/2) B+e^n N.                 (1)

To prove it, the first accepted Q map dephases z/y and leaves populations
diag(p,e)(rho_zz,rho_yy). Each subsequent measurement, expressed in its
own eigenbasis, applies M to those populations because the successive
bases have squared overlap matrix [[r,1-r],[1-r,r]]. The trace coefficient
on initial populations is (1,1)M^(n-1)diag(p,e); detailed balance
M diag(p,e)=diag(p,e)M^T turns its transpose into d_n. Remaining sectors
are common eigenvectors and give the displayed scalar products. For e=0,
use continuity or direct multiplication. This recovers K2484 for n>=2:
E_n=P+r^(n-1)Z.

The unnormalized target mass is precisely p^n F, F=Tr(P rho), since
A_R^*(P)=pP. The accepted bad mass is Tr((E_n-p^nP)rho). Define

    w_n=max{d_z(n),d_y(n),p^ceil(n/2)e^floor(n/2),
            e^ceil(n/2)p^floor(n/2),e^n}.

For F>=F0>0 the sharp worst conditional output infidelity is

    eps_n=(1-F0)w_n/[F0*p^n+(1-F0)w_n].                  (2)

It is attained by rho=F0 P+(1-F0)|v><v| for a unit vector in a maximizing
sector, and the formula decreases with F, proving the lower-bound-F case.
No purity or absence of arbitrary external reference entanglement is needed
for the marginal fidelity statement. This is filtering of the actual
output, not certification that the unknown producer already prepared P.

For the original r<1/2, d_z>=d_y: differences obey the positive recurrence
D_n=rD_(n-1)+p e(1-2r)D_(n-2), with D_1=p-e and D_2=r(p-e).
Other scalar sectors are at most Q-only for p>=e. Thus max of d_z and the
Q-only coefficient suffices, though using all five is a useful probe check.
The Q-only term is genuinely necessary:

    d_z(3)-p^2 e=p*r*(p-e)*(r-e).

For e>r it wins at n=3, contrary to carrying over the noiseless worst
state z. At n=2 d_z(2)-p e=p*r*(p-e)>0. Thus the worst state actually
changes as the cap and noise change. e=1/3 is an exact prospective example
above both original r values. Include this as a mutation/countercontrol.

## 3. No floor in this exact model, throughput cost and critical noise

The characteristic polynomial of M is

    f(lambda)=lambda^2-r*lambda+p*e*(2r-1).

For 0<e<1/2 its Perron eigenvalue is

    lambda_+=(r+sqrt(r^2+4*p*e*(1-2r)))/2.

The second root is negative. The exact inequalities are

    e<sqrt(p*e)<lambda_+<p<1.

Proof: f(sqrt(pe))=r sqrt(pe)(2sqrt(pe)-1)<0,
and f(p)=p(p-e)(1-r)>0. The quadratic has just one positive root.
Therefore every bad coefficient divided by p^n tends to zero, with
asymptotic principal rate lambda_+/p. Equation(2) tends to zero: there is
no nonzero conditional infidelity floor caused by fresh diagonal flags
alone. Meanwhile q_n=Tr(E_n rho)~F p^n for F>0, so accepted output yield
tends to zero. This is a fidelity/throughput tradeoff, not free mitigation.
At e=0 use the original r^(n-1) law.

At e=1/2, E_n=2^-n I and target mass=2^-n F, so conditional fidelity is
exactly F: all-pass records contain no filtering information. At e>1/2,
the common-null state survives as e^n while P survives as p^n; mixtures
with nonzero null component lose target fidelity asymptotically. A known
stationary symmetric error above1/2 can be relabelled to1-e, but this is
a different supplied protocol and does not cure unknown/correlated error.

Fidelity is monotone with cap n for 0<=e<=1/2: for any positive accepted
state sigma, Tr(A_R sigma)<=p Tr(sigma), while target mass is multiplied
by p. Hence q_(n+1)<=p q_n and conditional target fraction cannot fall.
This also proves w_(n+1)/p^(n+1)<=w_n/p^n and monotonicity of(2).

## 3a. Sharp robust guarantee for bounded independent flag drift

Identical noise is unnecessary for a uniform guarantee. Suppose each fresh flag is independent of system, retained reference and past, with a prescribed possibly different e_j<=e_star<1/2. Put p_j=1-e_j and t_j=e_j/p_j. Factor the accepted map as p_j B_R^{t_j}, where B_R^t(X)=RXR+t Rperp X Rperp. For t' >= t, B_R^{t'}-B_R^t is completely positive. Compositions preserve this order on positive inputs, so the normalized all-pass output for any sequence t_j<=t_star is bounded in positive-operator order by the homogeneous t_star output. Both normalized target masses are exactly F. Taking the bad-sector trace and applying x/(F+x) proves that equation(2) at e_star is the sharp uniform infidelity bound over all these sequences. Equality is available when every e_j=e_star and the maximizing initial sector is chosen. Target output mass is at least F0(1-e_star)^n. Thus the first feasible homogeneous cap gives a robust guarantee without assuming that every flag has identical error. This is a prospective conditional calibration interface; unconditional flag marginals or a hidden common error bit do not satisfy the freshness premise. It grants no control over additional coherent/state-dependent errors.

## 4. Exact stopped costs and cap optimization

For nonnegative deterministic test prices c_j, the exact expected cost
through first rejection or cap n is

    C_n(rho)=sum_(j=1)^n c_j q_(j-1), q_0=1, q_k=Tr(E_k rho).   (3)

The maximum prospective spend is sum c_j. Set h_P(k)=p^k and h_l(k)
equal to the five bad coefficients of(1), all h_l(0)=1. At exact F the
worst expected cost is the finite-dimensional formula

    F sum_j c_j p^(j-1)+(1-F) max_l sum_j c_j h_l(j-1).     (4)

Maximize the entire accumulated coefficient for a fixed sector. Do not
silently sum per-time maxima, since the same input must realize all terms.
For F>=F0 the cost may be maximized also at F=1, so check both endpoints
F0 and1 (linear dependence before the finite max). In fact h_l(k)<=p^k for every sector, so pure P maximizes expected per-attempt cost over F>=F0. This differs from infidelity, whose worst F is F0.

If fresh input attempts really are independent and identically prepared,
with the same rho and independent reset flags, restart after failure to
obtain one accepted output. The renewal expected spend is C_n(rho)/q_n.
This ratio need not apply to arbitrary correlated new input attempts.
For exact F>=F0>0, so every denominator is positive, its worst value over rho is

    max_l [F sum_j c_j p^(j-1)+(1-F)sum_j c_j h_l(j-1)]
          /[F p^n+(1-F)h_l(n)].                         (5)

This follows because a ratio of positive affine forms over a simplex is
a denominator-weighted average of its vertex ratios. For F>=F0, test F0
and1 as well: each sector ratio is linear fractional in F and has no
strict interior extremum.

For every fixed input, C_n is nondecreasing and q_n nonincreasing in n;
with strictly positive next-step cost and q_n>0, C_n/q_n strictly grows.
The worst ratios also grow. Therefore among deterministic alternating caps
meeting a chosen uniform fidelity tolerance, the first feasible n minimizes
both expected per-attempt cost and expected renewal cost; feasibility is
monotone by Section3. This is only optimization over these fixed caps,
not over different instruments, accepted histories or adaptive strategies.
For every strictly positive infidelity tolerance there is a finite feasible n when F0>0 and e<1/2; zero tolerance generally requires a limit. Fixed positive
per-test prices and e>0 give divergent renewal cost as n->infinity.
For a pure target and unit prices, C_n=(1-p^n)/e and renewal cost
(p^-n-1)/e, which is an immediate transparent cost control.

## 5. Essential contrary controls

1. Correlated flags: draw one B~Bernoulli(e) and use flag |B> for every
   test, independent of initial system. Each unconditional flag marginal
   is the declared diag(p,e). For rho=F P+(1-F)|d><d|, d in N, all-pass
   target mass=pF and bad mass=e(1-F), independent of n. Infidelity has
   the permanent floor e(1-F)/[pF+e(1-F)]. Conditional freshness, not only
   marginal purity calibration, is indispensable. This common-bit model
   is an exact physical classical correlation, not an adversarial slogan.
2. No reset: start a pure zero flag and retain its accepted value1 for
   the next controlled-X circuit. The target passes first, then produces
   record0 on the second test. All-pass target yield is zero for n>=2.
3. Effect-only replacement: same pR+eRperp effect may measure then prepare
   a state in N on acceptance, destroying target fidelity immediately.
   Thus matching acceptance probabilities cannot validate this conclusion.
4. Coherent flag preparation: offdiagonal tau_01 adds tau_01 R rho Rperp
   and its adjoint to the accepted map. The classical transfer recursion
   is not licensed by diagonal probabilities alone.
5. At e=0 recover original theorem; at e=1/2 no gain; for e>1/2 choose N
   to show wrong filtering. At e=1/3,n=3 the Q-only sector disproves
   the tempting assumption that z always maximizes the error.

## Independent verification

The written all-n proof is separate from finite regression counts. A read-only quantum specialist and independent adversarial reviewer check transfer orientation, the full carrier, freshness, output versus input claims and iid renewal. The lead independently derives the representative CP-map products and compares the actual output target mass and stopped costs. Original rank/angle data are authenticated from K2454/K2484 evidence; unchanged full-carrier reconstruction is reused, not counted as newly executed. Contrary controls alter actual instruments/noise laws or use exact original sector witnesses. No proof-assistant or external-expert certification.

## 7. Closest literature checked

Liu, Shang, Han and Zhang, Universally Optimal Verification of Entangled
States with Nondemolition Measurements, PRL126,090504(2021),
https://arxiv.org/abs/2005.01106 and full HTML
https://arxiv.org/html/2005.01106v3 . Sequential nondemolition verification
and reuse of target states are prior work; do not claim them as new.

Zhang, Li, Liu and Shang, Verification of entangled states under noisy
measurements, Advanced Quantum Technologies8,2400575(2025),
https://arxiv.org/abs/2406.01470 and full HTML
https://arxiv.org/html/2406.01470v2 . Section2 gives target-eigenvector and
positive noisy spectral-gap distinguishability conditions; Section4 eqs15--16
explicitly distinguishes classical readout transition errors from residual
quantum measurement errors. Their framework in Sections2--3 uses many-copy
acceptance statistics and hypothesis testing. The candidate above instead
computes one retained state's output under the supplied alternating CP maps.
This comparison supports scope only: no priority/novelty certification.

Next substantive step: add actual declared calibrated instrument/storage
error to this exact noisy baseline, or construct an elementary/spatial
implementation. A numeric eta without measurement is only a prospective
example. Native GU positivity and observable export remain separately open.

[Probe](../../tests/channel-swings/k2486_noisy_flag_alternating_verifier_probe.py) and [report](../../lab/process/k2486-noisy-flag-alternating-verifier.json).

## Unmodelled complete-instrument errors

The existing K2481/K2484 conditioning and ideal-prefix hybrid bounds compose with this exact noisy baseline. If the remaining complete-instrument errors, including retained references and history, have half-diamond bounds delta_j, terminal state error is at most epsilon=sum_j delta_j q_(j-1) on the chosen baseline input. Actual conditional infidelity is at most min(1,(x_n+epsilon)/q_n); epsilon<q_n suffices for nonzero actual output. These are reused inequalities, not new calibration evidence. The explicitly modeled eta need not be charged again; correlated reset, coherent gate, storage and other defects require their own justified bounds.
