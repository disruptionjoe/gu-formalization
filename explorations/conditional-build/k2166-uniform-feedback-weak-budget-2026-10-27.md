---
title: "K2166 Sharp uniform weak-budget feedback detector frontier"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed positive free-field model and binary diagonal effects with reported-outcome real squeezes; vacuum field energy only
scripts:
  - tests/channel-swings/k2166_uniform_feedback_weak_budget_probe.py
---

# K2166 Sharp uniform weak-budget feedback frontier

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
result: K2166 sharp global weak-budget limit, rare-branch exclusion and balanced optimal branch probabilities
carrier: fixed positive scalar Fock vacuum and photon-added signal with binary diagonal local occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and free vacuum output energy ON=declared_carrier
real_structure: positive square-root diagonal Kraus followed by one real squeeze per reported outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction: supplied free Hamiltonian and instrument class
target: globally optimized small-energy detection contrast MAP-TYPE=intertwiner
```

## Result and scope

For precisely [K2162](k2162-feedback-detector-frontier-2026-10-27.md)'s operation class,

    lim_(B downarrow 0) V_fb(B)/sqrt(B) = 1/sqrt(kappa),
    kappa = z E_sum - 2 D²/H0,
    D = N E_sum/(2N+1),  H0=(3m1+m_-1 m2)/2.

K2162 proved the achievable lower limit only. The new upper bound is uniform over all
binary effect sequences, including arbitrarily high occupations and vanishing outcome
probabilities. It does not assume that all effect values are close to one half.
Asymptotically optimal detectors have vacuum click probability tending to one half and use
asymptotically all the allowed field-energy budget. No whole effect-profile convergence follows.

Keep the fixed smear, photon-added signal, positive free Hamiltonian, N>0 and finite moments
of [K2160](k2160-outcome-conditioned-squeezing-2026-10-27.md). Countable hidden diagonal Kraus
are allowed with one common real squeeze per reported outcome; K2160's positive-root
minimization applies. Hidden-label feedback, general Gaussian channels, arbitrary local
instruments, signal-averaged energy, and autonomous preparation/switching/reset cost are
outside the result. SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b, source, ledger and canon
are unchanged. This is useful independent mathematics, not a GU-derived positive state.

## 1. Relax each branch by its two occupation moments

Use K2160's unnormalized w,M,T and set

    A(x)=m2 x²/(2nu)+nu/(2x²), C=2s E_sum,
    D_M=N E_h+(N+1)E_j,
    D_w=((N-1)E_h+N E_j)/2.

For a nonzero branch let mu=M/w. Cauchy gives T<=sqrt(M(M+w)). Because its coefficient
in F is -Cx<0, for every x>0,

    F(w,M,T;x) >= w G(mu,x),
    G(mu,x)=(mu+1/2)A(x)-Cx sqrt(mu(mu+1))+D_M mu+D_w.
    f(mu)=min_(x>0) G(mu,x).

The x-dependent part has strictly positive second derivative and diverges at both ends;
the minimum is unique. Thus with click moments (w,M), completeness gives

    E >= w f(M/w)+(1-w)f((N-M)/(1-w)),                    (1)
    Delta=(M-Nw)/N.

Zero branches are omitted. Formula(1) is a relaxation, not a claim that arbitrary pairs
of geometric conditional states are jointly realizable by bounded binary effects.

## 2. Coercivity controls both rare branches and occupation tails

The normalized Schmidt state

    psi_mu = (1+mu)^(-1/2) sum_n (mu/(1+mu))^(n/2)|n,n>

where |n,n> uses the b,c occupation basis, has moments M=mu, w=1, T=sqrt(mu(mu+1)). It realizes G as a free-field energy after
squeezing. At mu=0 use |0,0>. All finite mu states are in the required energy form domain:
the finite physical two-mode span has finite one-particle energy matrix

    K = [[E_h,F_hj],[F_hj,E_j]], tr K=E_sum,
    det K=(m2-m1²)/(4N(N+1))>0.

N>0 implies the spectral measure is not concentrated at one frequency, so m2>m1².
Take the explicit lambda=det K/tr K>0, which is no larger than the smallest eigenvalue.
The quadratic form of H on states occupying these modes dominates lambda times their total
physical number. Invariance of the span under omega is unnecessary: the expectation uses
its compression. No uniform gap for the whole one-particle operator is assumed.

Put u=(x+x^-1)/2>=1. Direct substitution into physical h,j number moments gives

    n_h+n_j = (2N+1)(2mu+1)u²-4s sqrt(mu(mu+1))u-1.

This is increasing for u>=1: its derivative at 1 is strictly positive by
2N+1>2sqrt(N(N+1)) and 2mu+1>2sqrt(mu(mu+1)). Therefore

    G(mu,x) >= 2lambda [sqrt(N+1)sqrt(mu)-sqrt(N)sqrt(mu+1)]²
             >= lambda (mu-N)²/[(2N+1)mu+N].              (2)

For the second inequality rationalize the square and bound the resulting denominator by
2[(2N+1)mu+N]. It follows that f>=0, vanishes only at mu=N, and has a uniform positive
linear lower tail. This is a proof over all mu, not a finite occupation check.
For the actual branch, (2) gives the homogeneous bound

    E_r >= lambda (M_r-Nw_r)²/[(2N+1)M_r+Nw_r].          (3)

Summing two branches, their denominators add to 2N(N+1), so the harmonic-mean inequality
provides the useful all-budget estimate

    E >= 2lambda z Delta²,  V_fb(B)<=sqrt(B/(2lambda z)). (4)

The usual maximal contrast bound may further cap this expression. This explicit finite-budget
bound is not the sharp small-budget coefficient.

## 3. Local moment Hessian, with no expansion in the effects

Near mu=N>0 the unique minimizer x(mu) is smooth by strict convexity. At (N,1),
G=G_mu=G_x=0 and

    G_mumu=E_sum/[2N(N+1)],
    G_mux=-E_sum/(2N+1),  G_xx=H0.

Consequently

    f''(N)=E_sum/[2N(N+1)]-E_sum²/[(2N+1)² H0],
    2N² f''(N)=kappa>0.                                (5)

K2162's moment identities prove 0<kappa<z E_sum. This Hessian is that of the relaxed
geometric-state energy. It agrees with the already achieved coefficient without assuming
that each actual branch is thermal.

## 4. Uniform upper asymptote

Consider any sequence of allowed detectors with E->0 and nonzero contrast. Pass to a
subsequence with w->t in [0,1]. Such subsequences suffice to bound the overall limsup.

If t=0, 0<=M<=N and (3) force M->0: a subsequence with M bounded away from zero would
have a strictly positive lower energy. From the same branch bound,

    Delta²/E <= [(2N+1)M+Nw]/(lambda N²) -> 0.

If t=1 apply the identical argument to the complement. Thus rare reported outcomes cannot
produce the leading square-root gain, even if their conditional occupation diverges.

For 0<t<1, (1),(2) force both conditional means to N. Taylor expansion is now only of the
single smooth scalar function f near N. Writing d=M-Nw=N Delta, it gives uniformly along
this subsequence

    E >= (f''(N)/2-o(1)) d² [1/w+1/(1-w)],
    limsup Delta²/E <= 2t(1-t)/(N² f''(N)) <= 1/kappa.   (6)

No occupation cutoff, tail limit exchange or uniform Taylor series for e_n appears.
Arbitrary hidden diagonal Kraus cannot improve this because their energy is at least the
positive-root value used in (1). The attained budget optimizers from K2162, E<=B, satisfy
limsup V_fb(B)/sqrt(B)<=1/sqrt(kappa). Its bounded constant-tail constructions already give
the opposite liminf, establishing the claimed limit.

## 5. Useful consumers and exact fixture

If Delta/sqrt(B)->1/sqrt(kappa) and E<=B->0, (6) and rare-branch exclusion force w->1/2.
They also force E/B->1, since otherwise the bound on Delta²/E would be violated along a
subsequence. This constrains optimal branch probabilities and budget use, not the pointwise
shape of every effect or a unique detector.

For m1=5, m_-1=5/9, m2=41, nu=3, N=1/3:

    K=[[5,-4],[-4,5]], det K=9, lambda=9/10,
    G_mumu=45/4, G_mux=-6, G_xx=170/9,
    f''(N)=3177/340, kappa=353/170.

Hence V_fb(B)~sqrt(170B/353). The common-squeeze asymptotic is sqrt(2B/5), so reported-
outcome feedback yields a strict leading-order advantage in this declared resource model.
Equation(4) supplies the global coarser bound E>=9Delta²/20; the exact eigenvalue1 improves
it to E>=Delta²/2. Neither replaces the sharp local coefficient353/170.

The next independent physical question is a stable autonomous implementation with accounted
preparation and reset. Within the present class, finite-budget global optimization or
higher-order corrections are distinct questions; rare branches and tails are no longer
missing hypotheses for this leading asymptote. K2164's integer saturation tie result remains
separate. No arbitrary-channel optimum, external acceptance or novelty is asserted.

## Evidence

The companion probe independently differentiates the branch energy, expands physical number,
checks the compressed energy determinant, metric-free scalar inequalities and finite fixture.
Changed coefficient, cross term, branch weight and complement inputs must fail real checks
after a green baseline. Universal Cauchy, coercivity, sequence and attainability arguments
are written proofs requiring independent internal specialist acceptance. Finite samples and
symbolic identities do not alone certify the full theorem. No proof-assistant certification.
