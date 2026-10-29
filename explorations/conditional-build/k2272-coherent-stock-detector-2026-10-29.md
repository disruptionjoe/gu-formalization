---
title: "K2272 Preparing coherent stock for the full detector"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied model only; no source or canonical verdict
scripts:
  - tests/channel-swings/k2272_coherent_stock_detector_probe.py
---

# K2272 Preparing coherent stock for the full detector

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2272 Preparing coherent stock for the full detector
carrier: ordinary bosonic Fock space with finite neutral memory and an external phase drive LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product and spectral measure ON=declared_carrier
real_structure: real coefficients and complex Hilbert adjoint where applicable
grading: no native chirality or Clifford grading transported
action_owner: repository-construction -- supplied conditional model
target: complete recorded detector approximation with explicit preparation and charge cost MAP-TYPE=intertwiner
```

## Result and scope

An ordinary Glauber coherent state, prepared from vacuum by a specified resonant drive, can replace the supplied sine reference in [K2253](k2253-full-instrument-reference-reuse-2026-10-29.md). The same field-plus-record-plus-history comparison survives, including approximate return of the original coherent stock. A fully priced example gives ten-call error below0.008221, but requires mean stock occupation10^28 and a huge finite comparison compiler. It is an existence construction, not an affordable detector.

The external phase-stable drive is an explicit asymmetric resource. No conserving device creates that resource from invariant vacuum. This is ordinary positive-Hilbert-space apparatus mathematics; SC-META-53 remains UNCERTAIN, LT-SM8/LT-GR6b and ledger0.263 unchanged. No native GU action, quotient, prediction or thermodynamic regeneration follows. [K2270](k2270-untruncated-detector-control-2026-10-29.md) supplies full-Fock sector compilation; [K2273](k2273-positive-control-energy-2026-10-29.md) supplies its positive-pulse and moment conditions.

## 1. Actual preparation and its explicitly imported source

For one oscillator of frequency omega>0 use

    H(t)=hbar omega N+i hbar u(t)(exp(-i omega t)a†-exp(i omega t)a),
    u(t)=2sqrt(mu)/T sin²(pi t/T), 0<=t<=T.              (1)

The interaction picture has a fixed displacement generator. Vacuum evolves, up to scalar phase, to alpha(t)=exp(-i omega t) integral_0^t u(s)ds. At T its magnitude is sqrt(mu). Reference and detector phases must be calibrated to that known rotation, not silently ignored. Exact pulse accounts are

    integral u=sqrt(mu), peak u=2sqrt(mu)/T,
    peak |u'|=2pi sqrt(mu)/T², integral u²=3mu/(2T).     (2)

The displayed slew is for the envelope; the laboratory carrier adds omega-dependent terms. Completing the square gives H(t)>=-hbar u(t)²/omega. Adding the scalar hbar u²/omega makes the instantaneous Hamiltonian positive with identical state dynamics. At zero-envelope endpoints, deposited free energy and net work on this oscillator are hbar omega mu. This is not the total pump, phase-reference, clock, cooling or switching cost. The drive explicitly breaks number symmetry. There is no circular claim of coherence from conserving invariant resources.

## 2. Translation quality with the vacuum boundary included

In the calibrated frame, c_n=exp(-mu/2)mu^(n/2)/sqrt(n!), n>=0, extended by zero to l2(Z). Let S|n>=|n+1>. Then (Sc)_n=sqrt(n/mu)c_n, INCLUDING n=0, and

    ||Sc-c||²=E[(sqrt(N/mu)-1)²]
        <=E[(N/mu-1)²]=1/mu.                          (3)

The inequality follows from |sqrt(z)-1|<=|z-1| for z>=0 and the Poisson mean/variance. The bilateral shift is a comparison instrument, not a physical negative-charge battery. Telescoping gives ||S^k c-c||<=|k|/sqrt(mu), for either sign of integer k.

Let beta be the normalized restriction of c to integer charges [R,U], and p the discarded probability. Then

    D(c,beta)=sqrt(p), ||c-beta||<=sqrt(2p),
    ||S^k beta-beta||<=|k|/sqrt(mu)+2sqrt(2p).           (4)

Here D is half trace distance between pure-state density matrices. In K2253 there are TWO controlled translations, on input n<=Q and output m<=R. Their combined error is therefore

    (Q+R)/sqrt(mu)+4sqrt(2p),                          (5)

not one copy of the truncation allowance.

## 3. Rebuild the physical compiler on the new charge sector

For the supplied full recorded instrument V with V*(N+1)V<=C(N+1), retain K2253's finite failure-completed isometry W and its finite neutral environment. Its low-input/high-output error terms remain

    e_tail=2sqrt(B/(Q+1))+sqrt(2C(B+1)/(R+2)).          (6)

For each total charge t from R through U+Q, copy W's amplitudes into physical reference charges t-m. They are nonnegative, and all needed input levels exist because n<=Q<=R. Complete the partial isometry separately within each finite total-charge shell. The resulting low-input, beta-initialized comparison has support within

    K=U+Q, m charged modes plus one reference,
    dim H_<=K = a_neutral binomial(K+m+1,m+1).          (7)

Use K2270's genuine number-conserving full-Fock alphabet to REBUILD this finite-sector compiler. The prior numerical threshold cannot be transplanted. Shell blocks above K have globally defined dynamics but no accuracy assertion. The actual initial coherent state is untruncated; high-sector behavior is priced by its initial trace-distance comparison, not described as nonexistent. The huge finite neutral environment is retained, not inferred small from a binary record.

For J adaptive calls with the original K2253 averaged ideal-input bound B, controller isolation from the reference and arbitrary external history,

    D(full_actual, full_ideal tensor original_c)
       <= J[e_tail+(Q+R)/sqrt(mu)+4sqrt(2p)]
          +2sqrt(p)+sum zeta_j+sum eta_j+epsilon_prep. (8)

One sqrt(p) replaces the actual initial c by beta; the other replaces the FINAL ideal beta by original c. Neither is charged at every call. zeta is low-sector compiler error, eta is K2270's domain-qualified outgoing projected perturbation error, and epsilon_prep is additional actual preparation error charged once. The ideal-prefix hybrid keeps the low-supported comparison at each insertion; subsequent actual maps contract trace distance even when the real reference has drifted or become correlated. Actual controllers need not preserve a real-state moment budget for (8), but K2273 energy statements require their own stronger hypotheses. Rare postselection is not covered uniformly.

## 4. A conservative explicit ten-call budget

Take the K2253 two-mode detector C=81, B=1, J=10 and

    Q=15999999, R=5183999998,
    mu=10^28, U=2mu, K=20000000000000000000015999999.

For Poisson N with mean mu, R<=mu/2 and Chebyshev give

    Pr(N<R)<=4/mu, Pr(N>2mu)<=1/mu,
    p<=5/mu, sqrt(p)<3*10^-14, sqrt(2p)<4*10^-14.

These deliberately loose inequalities need no evaluation of an enormous Poisson sum. Equation (6) is exactly1/2000+1/4000. Also (Q+R)/sqrt(mu)<0.000052. With exact preparation, total compilation error0.0001 and total projected perturbation error0.0001, (8) is strictly below0.008221. The margin can absorb only an explicitly allocated additional preparation error; none is implicitly supplied.

The deposited reference energy is hbar omega*10^28. This is MUCH larger stock than the earlier sine construction, not an energetic optimization. Preparation duration can trade envelope magnitude and slew; it does not reduce deposited energy. The finite compiler's gate count and precision remain enormous, and the actual charged Hilbert space is infinite. Full-system moment/energy convergence does not follow from this trace-distance budget.

## 5. Resource moments and limits of restoration

For the prepared reference, exact Poisson identities give

    E N=mu, E N²=mu²+mu,
    E N³=mu³+3mu²+mu,
    E N⁴=mu⁴+6mu³+7mu²+mu.                            (9)

Hence E(N+1)²=mu²+3mu+1 and E(N+1)⁴=mu⁴+10mu³+25mu²+15mu+1. Every finite mu has finite moments, but they grow rapidly with improved accuracy. A product input plus reference obeys (N_sys+N_ref+1)^p <=2^(p-1)[(N_sys+1)^p+N_ref^p] for p>=1 because these commuting charges reduce it to a scalar inequality. Initial input moments must be supplied; a mean-input budget alone does not imply them.

These moments enable K2273's qualified mean/RMS control estimates. They do not prove uniform energetic convergence as mu increases, perpetual reuse, exact independent stock restoration, or renewed phase supply. The finite-battery bound with a physical maximum charge H is not inherited by this coherent state. Conservation and full-state comparison remain operative at their actual hypotheses.

## Verification and continuation

The companion probe checks Poisson recurrence and factorial-moment algebra, finite positive/boundary controls, both translation allowances, exact budget arithmetic, new comparison threshold, drive integrals and asymmetric-source countercontrols. These finite checks supplement the written infinite-state and adaptive-channel proofs. Independent internal review is not external-expert, Lean, hardware, novelty or remote-CI certification. General phase-reference constructions are established background, including [Åberg](https://arxiv.org/abs/1304.1060); no catalytic-coherence novelty or exact catalysis is claimed here.

The next economical question is a specified finite source/clock implementation or a restricted controller with substantially smaller proved resource costs. An assumed classical phase source with priced oscillator energy is progress in input specification, not a complete physical supply chain.
