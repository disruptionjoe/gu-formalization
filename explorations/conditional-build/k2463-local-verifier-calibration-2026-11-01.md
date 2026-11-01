---
title: "K2463 When a larger verifier gap improves an operational certificate"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional whole-instrument calibration and prospective schedule costs; no measured device advantage"
---

# K2463 When a larger verifier gap improves an operational certificate

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
result: K2463
carrier: original 108-dimensional positive Hilbert programs with classical randomized local tests LAYER=toy CHIRALITY=N/A
pairing: conditional expectation and positive-Hilbert trusted-effect pairing ON=declared_carrier
real_structure: real probabilities and exact real algebra; complex positive states only in the supplied quantum model
grading: original tensor slots or classical histories and test/use branches; no imported physical grading
action_owner: repository-construction -- supplied conditional mathematical models
target: When a larger verifier gap improves an operational certificate MAP-TYPE=evaluation
```

## Result

The gap9/20 verifier of K2460 does not automatically outperform K2457's
gap2/5 verifier. Its extra calibration allowance must be below an explicit
threshold, and its branch costs matter. This note composes full-instrument
error, setting randomness and a stopping-compatible cost tail with the
existing actual-use certificate. It uses the original gaps as authenticated
predecessor evidence; the inherited full-carrier blocks also resolve the cost-aware cheap family
below. No full-local optimum or measured advantage is claimed.

SC-META-53 remains UNCERTAIN. The positive Hilbert programs are supplied
conditional models, not native GU physical states; LT-SM8, ledger0.263 and
canon remain unchanged. All numeric costs below are hypothetical charges.

## 1. Complete-effect calibration, including setting choice

On the complete original carrier let P=|Psi><Psi| and

    Omega=sum p_j E_j <= P+(1-nu)(I-P).

Each label j includes branch and finite phase selection. Suppose implemented
effects satisfy 0<=Etilde_j<=I and Etilde_j<=E_j+beta_j I.
Fresh labels, independent of the current resource conditional on the past,
have probabilities q_j with TV(p,q)<=eta. Then

    sum q_j Etilde_j <= Omega+beta_eff I,
    beta_eff=sum p_j beta_j+eta.                         (1)

Indeed the label term sum(q-p)Etilde is bounded above by the sum of
positive coefficients, namely TV. The remaining p-weighted error is
bounded by sum p beta. The TV coefficient is one, not two. Consequently
implemented rejection on a normalized use-branch state satisfies

    b >= nu(1-<Psi,rho Psi>)-beta_eff.                   (2)

Test/use state leakage remains separately accounted for by K2459 or K2462.
Known label marginals alone cannot supply conditional independence.

A sufficient implementation hypothesis bounds each complete local instrument,
including outcome register and postmeasurement state, in **half-diamond norm**
(error uniform over inputs and auxiliary systems). A sequential circuit
hybrid and trace-norm contractivity give

    beta_j <= min(1, sum_depth max_history epsilon_depth,history). (3)

Controlled alternatives at one depth form a block-diagonal classical control:
the norm error is at most the largest branch error. One does not add errors
across54 mutually exclusive conditional outcomes or135 randomly chosen phase
labels. Sequential gates do add; include phase gates, trusted native-axis
rotations, preparation/custody and the final accept predicate when applicable.
Uniform whole-instrument error is stronger than matching outcome probabilities:
postmeasurement disturbance can change the next feedforward step.

The proof telescopes actual versus ideal channels one depth at a time,
uses contractivity before and after each difference, and bounds the final
accept probability by half trace distance. Equation (3) is a sufficient
mathematical budget; it supplies no empirical calibration procedure.

## 2. Original-output calibration crossover

Under K2459's fixed-parameter pathwise original-budget premise put

    e=(tau-kappa/qherald)/C_out,
    D=nu e^2-beta_eff,
    A=[gamma B+log(1/alpha)]/[-log(1-pi)].

Require e>0,D>0 and the separately checked positive actual mean success.
Zero failures and N_U>=ceil(A/D) suffice for the original success-weighted
output bound. Under K2462's expected-budget premise replace the numerator
by gamma K/alpha+log(1/alpha); no other algebraic change is needed.

For the two inherited gaps,

    D_new-D_old=e^2/20-(beta_new-beta_old).               (4)

Thus the new verifier improves the continuous sample allowance iff its
extra additive calibration is less than e^2/20. Integer ceilings can tie
and must be compared separately. At tau=.01,kappa=10^-6,qherald=1/4,
C_out=2, the threshold is exactly

    e=.004998, e^2/20=.0000012490002.

The gap improvement cannot compensate arbitrarily poor implementation.
Nonpositive D gives no finite count from this certificate, not proof that
no better experiment can work. For unchanged beta=10^-8, pi=eta=1/2,
alpha=.05,B=10^-6 the original pathwise counts are432973 and384822.
With expected K=10^-6 they are432985 and384833, inherited from K2462.
These are design calculations; no hardware meets these premises by assertion.

## 3. Prospective cost at an actual stopping rule

Stop at the first test rejection or the N-th actual use. Assume fixed fresh
routing probability pi and fixed fresh test-label law p_j, independent of
the current resource and previous outcomes. Let c_U>=0 bound each use
charge, c_j>=0 bound each test-label charge, and S>=0 bound setup charge.
These may include deterministic worst-case gate/time costs. Extend the
random schedule prospectively past abort, using fresh unused random labels.
Actual operating cost, excluding setup, is bounded by this hypothetical
complete schedule cost W_N; total spent cost is bounded by S+W_N.

For s>0 with pi sum p_j exp(s c_j)<1, geometric waiting before each use gives

    E exp(s W_N) <=
      [exp(s c_U)(1-pi)/(1-pi sum p_j exp(s c_j))]^N.    (5)

Equality holds for exact charges. The N waiting blocks are independent
under these fresh fixed scheduling assumptions. Markov's inequality gives

    P(all-pass completion and S+W_N>K_cost)
      <= exp(-s(K_cost-S))
         [exp(s c_U)(1-pi)/(1-pi sum p_j exp(s c_j))]^N. (6)

Selecting the right side <=delta_cost and combining with the output event
by a union bound controls the joint event of all-pass completion with
invalid output or excessive cost by alpha+delta_cost, plus independently
spent calibration/budget failure probabilities. This is not a guarantee
conditioned on passing, and does not cover arbitrarily delayed stopping.
If actual fresh label law is q rather than p, (5)-(6) must use q, or a
proved upper bound on its moment; calibration TV alone is not a license to
reuse a cheaper nominal schedule distribution.

The expected prospective cost ceiling is

    S+N[c_U+pi/(1-pi) sum p_j c_j].                      (7)

It is not a deterministic cost. With pi=1/2,c_U=1,S=0, old test charges
all1, and new Q/E charges1,B/R charges4, the latter mean test charge is17/8.
The original sufficient counts then give expected prospective costs865946
and1202568.75. The larger gap costs more under these supplied charges.
This does not compare measured runtimes or conditional-on-success averages.
For constant costs the continuous cost crossover is
D_new/D_old > cost_per_use_new/cost_per_use_old; ceilings and setup costs
require the full finite expression. The probe also composes an explicit
Chernoff cost budget with the original384822-use design: z=1001/1000
gives cost budget1209325 and tail probability below.01. This cost
probability is added to, not substituted for, the output failure allowance.

## 4. Released exact cheap optimum and costly-effect exclusion

Cost-aware design is a different objective from maximizing the gap. Let
T be the original phase-averaged E test and consider pQ+(1-p)T. For each
original program a is27/100 or15/52. K2457's authenticated complete-carrier
blocks give the full target-orthogonal maximum as

    lambda(p)=max(g(p),(1-p)ell),
    M(p)=[[p+(1-p)a/(1+a), (1-p)sqrt(a/2)/(1+a)],
          [(1-p)sqrt(a/2)/(1+a), (1-p)/(2(1+a))]],
    g(p)=lambda_max M(p),
    ell=max_chi [t_chi+sqrt(t_chi^2-4d_chi)]/2.          (8)

The maximum runs over all30 nonzero character blocks; other zero-block
nontarget eigenvalues are at most p<=g(p). No companion coordinate is
removed. Put h=1/[2(1+a)], q=1-p. The trace and determinant of M are
1-hq and hq(1-q). Differentiating its larger root gives its unique minimum

    q0=[3+sqrt(a/(1+a))]/(4+h), p0=1-q0,
    g0=2q0-1, nu_c=1-g0.                              (9)

The discriminant is1-6hq+h(h+4)q^2. Its square-root second derivative
is positive because4h(h+4)-36h^2=16h(1-2h)>0 for these a>0.
Thus g is strictly convex in q; its stationary point is the unique minimum.

The probe checks all30 original blocks with rigorous intervals and finds
q0*ell<g0 for BOTH actual programs. Thus p0 is their exact optimum in this
entire cheap two-effect family, not just a candidate from a grid. Equation
(9) is asserted as the full-family optimum here only for these checked
programs; a different program can have a dominating nonzero block.

There is an explicit global cost witness. Let v be the normalized top
zero-block eigenvector at p0, viewed in the original target-orthogonal
carrier, and X=vv*. Stationarity gives

    Tr X Q = Tr X T = g0,
    Tr X(I-Q)=Tr X(I-T)=nu_c.                          (10)

This is a spectral upper-bound witness for EVERY mixture that includes
these cheap effects and additional target-complete physical effects
0<=E<=I, E Psi=Psi. (The rejection upper bound itself does not require
target completeness; interpreting the mixture as a verifier does.) For fixed
pi=1/2,cU=1, cheap test charge1 gives prospective cost2 per actual use.
If an added effect has test charge c_E, write K_E=1+c_E. Since
Tr X(I-E)<=1, every such effect with K_E>=2/nu_c obeys the same rejection
per cost bound as Q,T. Taking mixtures and testing on X proves

    gap(Omega)/cost_per_use <= nu_c/2.                 (11)

The cheap optimum attains equality. This excludes arbitrary expensive
effects assigned that charge, including B/R, without claiming their best
unpriced gap or assuming a five-effect convex hull. In particular the
actual nu_c>.41 in both programs, so test charge4 (K_E=5) is excluded.
The claim allows only these two cheap effects plus the cost-qualified
extras; a new cheap effect could beat it.

With COMMON additive calibration beta and original output parameter e,
replace the numerator by e^2 gap-beta. The corresponding exclusion is

    K_E >= 2(e^2-beta)/(e^2 nu_c-beta).                 (12)

The published e=.004998,beta=10^-8 satisfies a positive denominator and
keeps K_E=5 excluded for both programs. Different implementation errors
need their actual branch-weighted calibration, not this common-beta claim.

At zero calibration the test-charge threshold ccrit=2/nu_c-1 is sharp
over unrestricted physical effects: E=P_Psi has gap1 and mixing it with
the cheap optimum increases efficiency below the threshold, ties at it,
and decreases efficiency above it. This projector is NOT asserted local
or available hardware. The probe verifies the three comparisons and the
explicit dual expectation identities. Finite ceilings, setup charges,
confidence cost tails and calibration acquisition costs remain outside
this continuous objective; use the earlier complete finite cost formulas
for those decisions.

## 5. Released routing optimum under a routing-stable zero-leakage premise

If the leakage budget is zero and calibration/mean test charge mu>0 remain
valid under changing the fresh test probability, the continuous expected
prospective cost has routing factor

    f_mu(t)=[mu exp(t)+1-mu]/t, t=-log(1-pi)>0.         (13)

This follows by multiplying the sufficient use count proportional to1/t
by1+mu*pi/(1-pi). Its unique stationary minimum solves

    mu exp(t)(t-1)=1-mu.                              (14)

The derivative numerator is negative at t=0 and strictly increasing
because its derivative is mu*t*exp(t)>0. For the cheap effects mu=1,
t=1, pi=1-exp(-1), and the routing factor improves from2/log2 to exp(1).
This exact specialization supplies no nonzero-budget routing optimum:
the compensator coefficient and independently justified leakage premise
may change with pi. Applying (13) to a fixed nonzero numerator without
re-establishing that premise is invalid. Setup/rounding still require the
finite cost formulas.

## 6. Contrary controls and evidence boundaries

On a qutrit take Psi=|0>, E1=P0+P1,E2=P0+P2. Uniform independent labels
give gap1/2. Correlated pairs(label1,|1>),(label2,|2>) pass certainly with
zero fidelity and exactly correct label marginals. This falsifies dropping
resource-independence from (1).

The TV coefficient is attained with E1=I,E2=P0 on |1>: moving eta label
mass to E1 increases acceptance exactly eta. An instrument that reports the
same outcome but resets the state to an orthogonal state defeats calibration
based solely on outcome probabilities. Sequential reset errors accumulate
while mutually exclusive label counts alone do not measure error.

For one use, pi=1/2,cU=cT=1, W=1+Geom has PGF z/(2-z) and
P(W>m)=2^-m. Replacing it by deterministic W<=2 fails with probability1/4.
The probe checks exact geometric remainder identities and wrong-normalizer
controls; the written proof supplies arbitrary N and the tail inequality.

Predecessor gap proofs, universal instrument/probability arguments, exact
finite counterexamples and Arb256 prospective calculations are distinct
kinds of evidence. Independent internal review is not external-expert,
proof-assistant, novelty or experimental certification.

[Probe](../../tests/channel-swings/k2463_local_verifier_calibration_probe.py) and [report](../../lab/process/k2463-local-verifier-calibration.json).
