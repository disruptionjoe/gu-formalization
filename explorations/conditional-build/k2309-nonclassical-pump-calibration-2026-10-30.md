---
title: "K2309 Nonclassical pump calibration"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics only; no native physical acceptance
scripts:
  - tests/channel-swings/k2309_nonclassical_pump_calibration_probe.py
---

# K2309 Nonclassical pump calibration

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
result: K2309
carrier: same twenty-mode vacuum-field circuit, retained coherent pump and single-pass pilot number carrier LAYER=toy CHIRALITY=N/A
pairing: positive complex Fock Hilbert form and half trace distance ON=declared_carrier
real_structure: ordinary complex conjugation and operator adjoint on positive Fock space
grading: pilot number K and total circuit charge Q=N_field+2K_pump; no Clifford identification
action_owner: repository-construction -- K2306 common-phase circuit plus specified sine pilot, phase measurement and correction
target: complete retained-pump calibration and explicit preparation-resource bounds MAP-TYPE=evaluation
```

## New task and inherited resources

Keep [K2306](k2306-retained-pump-phase-calibration-2026-10-30.md): mu=10^28 retained coherent pump, baseline delta<9.386e-12, unknown fixed common phase phi Q, supplied inverse correction, and independent pilots. The original vacuum-field circuit has even total charge; phase modulo pi suffices. Arbitrary odd-charge coherent field inputs do not share that alias. The pump itself is not measured for estimation. Source SC-META-53 remains UNCERTAIN and ledger0.263 unchanged; the positive Hilbert pilot is not a native physical quotient.

Sine-reference/path-spectrum facts already occur in K2240/K2251 and coherent preparation in K2275. This result reuses them to price the retained-pump calibration task, adds general single-pass mean-resource necessity, and composes confidence/average/control errors. It claims no new universal sine theorem or hardware feasibility.

## Fixed-cutoff minimax circular loss

For number cutoff N, prepare

    |s_N>=sqrt(2/(N+2)) sum_n=0^N sin(pi(n+1)/(N+2)) |n>.

Its mean number is N/2. One equal-duration encoding exp(-2i phi K), canonical phase POVM on R/pi Z and ideal correction give error density

    p(e)=1/pi |sum_n a_n exp(2in e)|²,
    L=E[4sin²e]=2[1-cos(pi/(N+2))].                   (1)

Fourier orthogonality fixes the normalization and nearest-coherence moment. The sine vector is the top eigenvector of the path adjacency with offdiagonal1/2.

More precisely (1) is the minimax circular quadratic loss among states supported0..N and all measurements. Uniform-prior averaging lower-bounds worst-case risk; phase symmetrization makes the averaged risk constant. A covariant POVM seed has unit diagonal and nearest offdiagonals of modulus<=1. The nearest-coherence sum is at most the top path eigenvalue, after diagonal phases align each edge; positivity or purification gives the same bound for mixed states with phase-free ancillas. The sine vector and canonical seed attain it. This proves neither optimal actual pump trace error nor mean-only optimality.

The retained-pump sandwich from K2306 and1-exp(-x)<=x give

    D_average<=delta+sqrt(mu L)
             <=delta+pi sqrt(mu)/(N+2).              (2)

The first inequality is convexity followed by Cauchy-Schwarz, not a pure-state formula applied to the whole mixed output. A retained calibration record is allowed if compared to the desired output tensor its ACTUAL record marginal; conditional errors are integrated. Pilot remnants are consumed, not returned unchanged.

## A single concrete stock meets two different specifications

Take N=3*10^27 and r=3*10^-27. Mean pilot occupation is1.5*10^27 and Hilbert dimension N+1. Since pi²<10, L<10/(9*10^54). On residual |e|_pi>=r,4sin²e>=4sin²r>=25*10^-54, using sin r>=5r/6 for r<=1. Markov gives failure<2/45<1/20. On success D<delta+2sqrt(mu)r<9.986e-12. Separately (2) gives unconditional averaged error<9.491e-12. These are different meanings; no95%-success guarantee is mistaken for a tiny average error.

A concrete imperfections budget also fits: allow pilot preparation trace error eta<=10^-14 and a uniform correction-channel error zeta<=10^-14 on the stated reachable input class. Require the actual imperfect pilot to be independent of circuit, pump and history, coupled only by classical feedforward, and supported on the same finite0..N carrier. Its actual mean differs from N/2 by at most N eta=3*10^13; trace closeness without this no-leakage condition would not bound energy. For the bounded conditional error function f(hatphi) in[0,1], changing the pilot changes its expectation by at most the outcome total variation eta. This direct bounded-risk argument also applies with the actual calibration-record marginal retained, and avoids paying eta twice in a comparison through a different marginal. The uniform correction bound then adds zeta, so eta+zeta add to(2), giving average<9.511e-12. For the high-confidence statement, preparation changes event probabilities by at most eta; on every actual outcome in the fixed good set G_phi={hatphi:|hatphi-phi|_pi<r}, the SAME conditional circuit bound holds and correction adds zeta, giving probability>=1-2/45-eta>.95 and successful error<9.996e-12. The correction hypothesis is a channel-error budget, not a supplied microscopic actuator. Unknown drift between calibration and use needs its own allowance.

## Necessity beyond coherent probes

Let arbitrary mixed/entangled pilots plus phase-independent ancillas have nonnegative total number K and mean m, with one encoding exp(-2i phi K). For hypotheses separated by Delta,

    |Tr rho exp(-2i Delta K)|>=max(0,1-2|Delta|m).

This follows from |1-exp(-ix)|<=|x|; purification and contraction give discrimination distance at most sqrt(1-max(0,1-2|Delta|m)^2). K2306's success neighborhoods for phases separated by2*10^-25 are disjoint. Uniform95% calibration therefore requires distance>=.9 and

    m>10^24,
    m>=(1-sqrt(19/100))/(4*10^-25).                   (3)

At m<=10^24 distance is at most.8. The prior must contain these two phases. This is a per-run success lower bound, not automatically a lower bound for average corrected-output trace error. Unequal positive durations replace m by E sum(Tj/T)Kj, LINEAR weights; the coherent squared-duration formula is a different bound. Repeated adaptive phase queries, unpriced phase references or readout of the working pump require a revised resource model. If the working pump is measured, its encoding and return/backaction must be counted too.

## Actual followthrough: the preparation bill remains large

For N>=2, |s_N> and its number rotation through theta*=4pi/(N+2) are orthogonal. Expanding sin² into three Fourier terms and summing the finite geometric series proves this exactly. K2275's covariant trace-distance contraction then gives a necessary coherent-stock mean M for deterministic preparation within0<eta<1/2:

    M >= log(1/[4eta(1-eta)])/[2(1-cos theta*)]
      >= (N+2)² log(1/[4eta(1-eta)])/(16pi²).          (4)

For the fixture eta=10^-14, log>28 and pi²<10 imply M>1.575*10^54. A supplied low-occupation nonclassical pilot therefore does not prove cheap coherent-source synthesis. At eta=0 no finite coherent source can prepare this exact orthogonal-orbit stock. An asymmetric ancillary resource changes(4) and must be counted; heralded success is outside deterministic preparation. This is an explicit alternative cost, not a contradiction of(2).

With number-diagonal stock, encoding changes nothing. With only invariant ancillas and a total-charge-invariant measurement, outcome probabilities also cannot depend on phi; the canonical phase readout needs a reference. Energy is sum hbar omega_j times occupation, and no arbitrary low frequency is priced as free. State manufacture, phase reference, detector and corrective actuation remain supplied except for the explicit budgets above. No energy catalysis or autonomous calibration follows.

## Verification and next condition

Exact small-cutoff Fourier/eigenvector controls, general symbolic identities and rational bounds test factors and budgets. Faults alter charge, sine normalization/index, circular-loss factor and resource expressions, and are detected by the actual evaluators. Uniform minimax, contraction and continuum probability claims use the written proofs; this is internal review, not external-expert or novelty certification.

The next useful question is an explicit reference/preparation/correction architecture satisfying these budgets, or a different resource class with preparation included. Replacing an unexplained tiny phase variance by another one would not settle it.
