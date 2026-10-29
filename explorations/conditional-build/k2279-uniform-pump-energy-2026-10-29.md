---
title: "K2279 Pump-uniform field energy and real depletion"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied model only; no native GU or canonical verdict
scripts:
  - tests/channel-swings/k2279_uniform_pump_energy_probe.py
---

# K2279 Pump-uniform field energy and real depletion

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2279 Pump-uniform field energy and real depletion
carrier: ten fresh two-mode fields, one coherent weighted-charge pump and neutral records LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product ON=declared_carrier
real_structure: complex Hilbert conjugation and adjoint
grading: declared oscillator charge where used; no native Clifford or chirality transfer
action_owner: repository-construction -- supplied conditional model
target: uniform field moment and energetic convergence with retained-pump trace comparison MAP-TYPE=intertwiner
```

## Result and exact consumer

The loose K2276 bound grows as mu² and cannot establish energy convergence when pump occupation mu grows to improve trace error. Here a shellwise commutator estimate supplies a FIELD second-moment bound independent of mu>=mu0 for a specified fresh-register consumer. It composes with [K2278](k2278-calibrated-pump-detector-2026-10-29.md) to give simultaneous field-energy accuracy and joint trace accuracy retaining the original pump. Actual pump energy still depletes. No total-energy catalytic renewal, affordable device or native GU quotient follows. SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b and ledger0.263 remain unchanged.

Supply J distinct two-mode fields, each supported initially on Nj<=1, jointly entangled with arbitrary external memory if desired. The single independent pump is EXACTLY coherent with mean mu. Apply the K2278 calibrated detector once to each field, using fixed addressed modes; earlier outputs remain isolated. Exact tracked register SWAPs are an equivalent routing convention. General mixers or adaptive energy-injecting controllers are NOT licensed by their mere preservation of global charge. Neutral and dispersive operations commute with each logical Nj. Define

    Q=N_all+2n_c,   Lj=Nj+2,
    Aj=integral |z(t)|dt over both pump pulses on field j,
    a=4 max_j Aj.                                    (1)

No physical input or pump truncation is imposed. Initially Nj<=1 is a restriction on this consumer, not a claim for all inputs to K2278.

## 1. Exact finite-shell moment propagation

On a Q=t shell, pump occupation k<=t/2. A pump pulse changes Nj by ±2. For an upward entry out of n=Nj,

    2 sqrt((n1+1)(n2+1)k)/(sqrt(mu)(n+2))
       <=sqrt(t/(2mu)),

and the analogous downward entry obeys the same bound, using k+1<=t/2 when the transition is possible. These are entries of [Lj,H_z]Lj^-1, multiplied by |z|. Each row and each column has at most two entries, so the row/column norm estimate proves

    ||[Lj,H_z]Lj^-1|| <=2|z|sqrt(t/(2mu)).             (2)

For finite-shell Schroedinger evolution, differentiating ||Lj psi||² cancels the Hermitian H_z term and gives an absolute derivative bounded by4|z|sqrt(t/(2mu))||Lj psi||². Gronwall yields

    E_t Lj²(final)<=exp[4Aj sqrt(t/(2mu))] E_t Lj²(initial). (3)

Other registers' pump pulses commute with Lj; all actual neutral/dispersive gates commute with it too, including the allowed calibration errors. Thus only the two pulses on the logical register contribute Aj. The estimate covers arbitrary neutral/past-history correlations. Piecewise-continuous time dependence is handled inside each finite shell, without asserting an unproved global differentiability theorem.

Q commutes with Lj² and the complete actual propagator, so coherences between Q shells do not enter this expectation. Initially N_all<=J, Lj²<=9, and independent coherent pump number K has the Poisson(mu) law. Sum the nonnegative finite-shell estimates (Tonelli) to obtain

    E Lj²(final) <=9 E exp[a sqrt((J+2K)/(2mu))].       (4)

The field and pump need not be independent at the end. Equation(4) uses their independence only at preparation.

## 2. A bound uniform in pump size

Use sqrt(x)<=(1+x)/2 and the Poisson moment-generating function:

    F(mu)=exp[a/2+aJ/(4mu)+mu(exp(a/(2mu))-1)].        (5)

Then(4)<=9F(mu). The exponent decreases with mu: for u>=0, exp(u)(1-u)-1<=0 proves the derivative of mu(exp(c/mu)-1) is nonpositive. Thus for every mu>=mu0,

    E(N_all+1)² <= E(sum_j Lj)²
                 <=J sum_j E Lj² <=9J² F(mu0).       (6)

This is uniform FIELD control. The pump/total-Q moments still grow with mu and do not inherit(6).

For J=10, Aj<=2.2, mu0=10^10, a<=44/5. An exact certificate gives F(mu0)<7000. Set u=a/(2mu0)<1 and use exp(u)-1<=u/(1-u); the exponent in(5) is <881/100. Finally

    exp(881/100) <=(100000/99119)^1000<7000,

where the final inequality is an exact integer-power comparison. Consequently actual E(N_all+1)²<6,300,000. The ideal original K2276 instrument has E(N_all+1)²<5,856,400 on this consumer. No dependence on growing mu remains.

## 3. Compose trace and energetic errors

K2273's sharp energy-continuity inequality, applied to A=N_all and BOTH moment bounds, gives

    |E N_all(actual)-E N_all(ideal)|
       <=sqrt(6,300,000 delta),                      (7)

where delta is the full joint half trace distance. For a common free-field frequency multiply by hbar omega; this is not total engineering work or a noncommuting interaction-energy theorem. With positive unequal frequencies a bound using omega_max follows. At delta around0.01 this conservative bound is large. Its purpose is a genuine uniform energetic limit and an explicit stronger-precision consumer, not a claim of useful energy accuracy from the earlier0.01 example.

For a finite simultaneous accuracy example, take J=10, exact coherent mu=10^28, q=50, each pump amplitude/phase error<=10^-17, every one of1000 dispersive areas within10^-17, and all at most260100 neutral gates within10^-17 in operator norm. Then K2278's exact bound is

    delta <600(1+10^-17)/10^14 +440/(2^50+1)
             +1200sqrt2*(2*10^-17)+22*1000*10^-17
             +260100*10^-17 <10^-11.                 (8)

All Aj<2.2 (r=log3<1.1), so the same uniform moment bound applies. Equation(7) is then <.008 field quanta. This requires20 pump pulses,1000 dispersive pulses, at most260100 neutral gates and102 neutral qubits per core, plus20 addressed field modes. It is finite but extremely demanding in stock and precision. No hardware feasibility or optimality follows.

The true asymptotic statement is obtained by mu,q tending upward and total calibration budgets tending to zero while Aj stays bounded; then delta tends to zero and(7) tends to zero. Improving mu alone while keeping calibration errors fixed leaves an error floor.

## 4. Follow-through: nearly restored state, nonzero energy consumption

For ten fresh vacuum inputs, the exact target nonselective instrument adds64/25 mean field quanta per call (K2253), hence total128/5=25.6. Exact weighted-Q conservation with initial field vacuum implies

    E N_all(actual)=2[mu-E n_c(actual)].

Combining this identity with(7)-(8) yields

    |mu-E n_c(actual)-64/5|<.004.                    (9)

Thus the pump loses approximately12.8 of its weighted-frequency quanta even though its reduced state is within10^-11 trace distance of the original coherent state. This is consistent: pump moments are not uniformly bounded as mu increases. Exact state restoration and exact target energy gain remain incompatible; the result is not free phase replenishment. With resonance omega_c=2omega, energy transferred to fields equals pump loss energy, before accounting for controls and source preparation.

A trace-only preparation promise cannot replace the coherent-moment premise. For example a mixture (1-epsilon)|alpha><alpha|+epsilon|M><M| is within epsilon trace distance of the coherent state while its second pump moment grows without bound as M increases. The Q-based exponential estimate likewise has no uniform bound on that class. This counterexample shows failure of the energetic inference from trace preparation alone; it does not prove that every such high-charge mixture necessarily creates large final field energy. A different preparation is allowed only with an independently bounded actual charge exponential moment sufficient for(4).

## 5. Positive-control completion is not a free extension

The signed-pulse alphabet is essential to the stated budget. K2276's optional semibounded replacement adds a weighted quadratic compensator. A residual phase exp[-i epsilon(Q+2)²] is outside K2278's dispersive/neutral model. For vacuum fields Q=2K, K Poisson(mu); after removing an irrelevant global phase, spectral calculus gives

    vector error <= |epsilon| sqrt(Var((Q+2)²))
                  =4|epsilon|sqrt(4mu³+14mu²+9mu).     (10)

The variance is preserved by any preceding Q-conserving core. This residual commutes with all Nj, so it does not spoil the uniform field moment argument, but its full retained-pump channel error needs the additional severe precision budget(10). Known deterministic phase tracking or different compensators require an explicit construction. This closes an inference seam without claiming that the positive-pulse implementation has been completed.

## Verification and open physical interface

The probe checks actual low-Q weighted-shell commutator entries including pump-vacuum boundaries, their squared row/column bounds, Poisson polynomial moments and exponential majorants, exact integer certificates, the complete channel/energy budget and depletion arithmetic. It plants wrong commutator normalization, missing pump weight, inflated calibration, and omitted neutral-gate costs. The universal direct-sum/Gronwall/Tonelli proof and sharp measure-theoretic continuity are written proofs, not inferred from sampled shells. Independent internal review is distinct from Lean, external-expert, hardware, novelty or remote-CI certification.

Remaining substantive work is physical: calibrated resonance/trilinear implementation and finite clock/phase preparation, economical precision/resource tradeoffs, or broader consumers with controlled actual energy injection. The uniform field result does not bound total pump energy uniformly, synthesize the primitive from a different alphabet, or establish native positive GU dynamics.

## Dependency evidence

- [K2253](k2253-full-instrument-reference-reuse-2026-10-29.md): full instrument and exact vacuum energy.
- [K2273](k2273-positive-control-energy-2026-10-29.md): sharp energy continuity and moment warning.
- [K2276](k2276-structured-detector-implementation-2026-10-29.md): actual instrument, domains and ideal moments.
