---
title: "K2244 Positive bounded local gates with retained onsite drift"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied mathematics; no source selection or physical recovery
scripts:
  - tests/channel-swings/k2244_onsite_drift_local_control_probe.py
---

# K2244 Positive bounded local gates with retained onsite drift

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2244 Positive bounded local gates with retained onsite drift
carrier: finite oscillator graph with finite record and arbitrary reference LAYER=toy CHIRALITY=N/A
pairing: positive complex Fock/Hilbert trace ON=declared_carrier
real_structure: explicitly stated real matrices or complex Hilbert adjoint below
grading: local occupation number
action_owner: repository-construction -- supplied onsite H0 plus positive finite-spectral local controls
target: complete recorded detector in laboratory picture under energy-constrained error MAP-TYPE=intertwiner
```

## Result and scope

The complete finite-network detector of [K2241](k2241-local-mode-detector-network-2026-10-29.md) can be approximated at any fixed positive operator-norm cap by positive local controls while retaining onsite oscillator drift. Polar compression gives genuinely bounded finite-rank local generators; explicit final phase corrections restore the laboratory-picture target. Every energy-constrained error, cutoff, gate time and modulation cost is stated below.

The drift here is H0=sum omega_j n_j with positive omega_j. It differs from [K2225](k2225-positive-drift-detector-control-2026-10-28.md)'s coupled W-squared drift. Arbitrary local spectral control matrices are supplied, not synthesized from a fixed small laboratory gate alphabet. No continuum, causal-field, hardware, source-selection, optimum-work or GU recovery credit follows. The finite network is a declared independent quantum model.

## 1. Finite-rank replacement without a projected-generator assumption

For a unitary U on a site/edge support S (including the finite record when needed), assume the quadratic-form inequality U*G_S U<=gamma G_S, G_S=N_S+1, gamma>=1. Write P_L=1_(N_S<=L), P_R=1_(N_S<=R), with R>=L and

    delta^2=gamma(L+1)/(R+1)<1.

On P_L, energy transport and the output tail inequality give ||(1-P_R)UP_L||<=delta. Thus A=P_RUP_L obeys A*A>= (1-delta^2)P_L. Its polar normalization V=A(A*A)^(-1/2) is an isometry from P_L into P_R. The singular values of A lie in[sqrt(1-delta^2),1], hence

    ||V-UP_L|| <= delta+1-sqrt(1-delta^2)
                <= delta+delta^2 = eta_bound.       (1)

Extend V's orthonormal columns to a unitary on the finite-dimensional P_R space, and use identity on its complement. Call this W_R. The extension, not P_RUP_R alone, is the actual unitary. With a finite record, both cutoffs include its full finite carrier. W_R-I has finite rank on this LOCAL factor; spectator identities mean it is not globally finite rank.

For a pure input with arbitrary reference, split by P_L. The vector error is at most eta_bound+2sqrt(p_tail); p_tail<=B/(L+1) if the global mean G=N+1 is at most B. Purification and partial trace yield

    half trace error <= eta_bound+2sqrt(B/(L+1)).    (2)

This establishes energy-constrained reference-uniform approximation. It does not assert operator-norm approximation on the full infinite-dimensional space or convergence of output energy moments. No convergence of exp(-i P_R K P_R) is assumed.

Choose the spectral phases of W_R in[0,2pi], so exp(-iK_R)=W_R with 0<=K_R<=2pi and K_R=0 on the complement. This positive bounded generator exists even for an ideal Gaussian gate whose usual quadratic generator is unbounded or indefinite.

## 2. Exact retained-drift implementation and timing

Fix a control-norm cap g>0, tau=2pi/g. For a gate interval, use the absolute-time modulation

    Hc(t)=exp(-itH0)(K_R/tau)exp(itH0).              (3)

H0 is never removed. Hc(t)>=0 and ||Hc(t)||<=g. Onsite drift factors across sites and preserves local number cutoffs; therefore(3) has the same site/edge support as K_R. In the interaction picture it is the constant K_R/tau, giving exactly W_R over that interval. H0+Hc is selfadjoint on D(H0) as a bounded perturbation. Finite-dimensional modulation on its support is norm-continuous within each interval; finitely many switches are allowed.

At any fixed g, longer total circuits take proportionally longer time. This is no fast-control limit. Positive generator shifts produce physical phase relative to the untouched high-energy sector; the chosen unitary completion already includes that phase correctly.

## 3. Complete recorded instrument in the laboratory picture

K2241's collector, number-effect rotation on a record, controlled squeeze and inverse collector are q local coherent gates. Defer record pinching until after feedback: the feedback is diagonal in the record basis, so pinching commutes with it. This gives the SAME complete recorded instrument, not just the unrecorded channel.

Use the ideal-prefix energy bound

    B=Gamma^2 R_s^2 (E/omega_min+1),                (4)

from K2241 (Gamma bounds both collector and inverse; R_s bounds the selected squeezes). Passive prefixes preserve G; active partial collector products obey the same product bound. Measurement rotation preserves oscillator N. Every local gate has its own finite gamma; use those bounds in(1).

With M oscillator sites fix total duration T=(q+M)tau in advance. Append M onsite ideal rotations F_j=exp(+i omega_j T n_j), approximated by finite-rank unitaries using section1. Their gamma is1; because they preserve cutoffs, one may instead make them exact on P_R and identity outside with the simpler tail estimate. Their ideal product F=exp(+iH0T) cancels the common final free evolution. There is no implicit clock equation: T is fixed by gate count and tau before choosing the phases.

Hybrid telescoping replaces gates one at a time, with each error evaluated on the IDEAL prefix state, which obeys(4). Subsequent implemented unitaries, final drift, pinching and discarded factors contract trace distance. Therefore the complete laboratory-picture instrument obeys

    epsilon <= min(1,sum_(j=1)^(q+M)
       [delta_j+delta_j^2+2sqrt(B/(L_j+1))]).         (5)

No assumption that actual prefixes retain the ideal bound B is needed for(5). The same construction realizes any finite local unitary circuit whose ideal prefix energy transport is bounded as stated.

## 4. Actual energy, bandwidth and an explicit active example

Every W_R and its within-gate interaction-picture control evolution preserves P_R and is identity on its complement, after onsite phase conjugation. Full laboratory evolution on that complement is the free onsite drift, which preserves H0. Its maximum possible increase in local occupation expectation is at most R. Thus at any time

    actual mean H0 <= E+omega_max sum_j R_j.         (6)

This crude finite bound is not energy convergence as cutoffs grow. Also ||dot Hc||<=2g omega_max R on each support. Fixed operator norm does not fix bandwidth, spectral rank or programming precision. All are supplied and can be enormous.

For K2241's two-site complex fixture, use E<=1 and omega_min=omega_max=1. Gamma=36, R_s=3/2 give B=5832. A two-mode passive collector can be decomposed into an adjacent Givens gate and up to two onsite phases, then a two-mode squeeze and an onsite squeeze: at most5 gates. Both collectors plus number-effect and conditional squeeze give q<=12, and M=2 final corrections give Q<=14. Local gamma<=9 suffices (two-mode squeeze exp(2t)=9, single squeeze exp(2r)=4, conditional squeeze<=9/4).

Choose common L+1=10^9, R+1=9*10^15. Then delta<=1/1000 and2sqrt(5832/10^9)<1/200. Hence

    epsilon <14(1/1000+1/10^6+1/200)=0.084014<0.1,
    T<=28pi/g.                                    (7)

The finite ranks are exceptionally large. Equation(7) is a rigorous existence consumer, not a useful hardware specification, minimum-time law or efficient synthesis claim. It keeps the same complex canonical-mode target and complete record.

### Smooth positive pulses also impose a finite slew limit

A finite derivative bound can be supplied constructively, beyond the piecewise-constant schedule. For any requested g>0 and b>0 use one common R_max and choose

    tau >= max(4pi/g, sqrt(8pi^2/b), 16pi omega_max R_max/b).

In each interval use f(s)=2sin^2(pi s/tau)/tau on0<=s<=tau, zero outside, and replace K_R/tau in(3) by K_R f(s). Its integral is1, so the interaction-picture gate is still exactly W_R. The control is positive, and

    ||Hc||<=4pi/tau<=g,
    ||dot Hc||<=4pi^2/tau^2+8pi omega_max R_max/tau<=b.

Both f and f' vanish at endpoints, so adjoining different gates gives a global C1 control. The same approximation and actual-energy bounds hold. Fix T=(q+M)tau before choosing final phase corrections; their cutoff and energy bounds are phase-independent, so this introduces no circularity. For the14-gate consumer the new duration is at most14tau, replacing the norm-only bound28pi/g when slew is imposed.

For example g=b=omega_max=1 and R_max>=1 admit tau=64R_max, by pi<22/7 and the displayed inequalities. The resulting time is enormous at(7)'s cutoff. A C1 compact pulse has no strict frequency bandlimit; a bounded derivative is a slew constraint, not a compact Fourier-spectrum claim. Exact pulse shape, spectral matrices and timing remain supplied. This follow-through removes an arbitrary instantaneous-switch assumption while preserving the stated locality and energy ceilings.

## 5. Coupled-drift countercontrol and remaining input

On a three-site chain, hopping drift J(a1* a2+a2* a1+a2* a3+a3* a2) spreads an onsite control under conjugation. Already its commutator with the bounded site1 vacuum projector is nonzero on edge1--2; nested commutators reach site3. Thus(3) is not a same-support prescription for general coupled physical drift. K2225's coupled model and continuum field remain distinct unresolved targets.

Preflight rejected unsupported projected-generator limits and bounded-coefficient language as substitutes for an operator-norm bound. Postflight checks polar normalization, extension, energy tails, arbitrary reference, coherent feedback and the absolute final-time phases. Exact finite controls use an actual leaky unitary compression, coupled-drift support and integer/rational resource inequalities. They cannot certify the universal Fock theorem by counting passing fixtures.

Next substantive inputs are a restricted experimentally specified control algebra with synthesis bounds, coupled-drift control preserving support, bandwidth/precision constraints or a same-mode continuum approximation. The present result removes the finite onsite-drift operator-norm existence gap; it does not provide these additional models.

## Reproduction and evidence kind

Run `python tests/channel-swings/k2244_onsite_drift_local_control_probe.py`. The default checks a clean baseline, actual input faults under unchanged predicates, and note/code/dependency hashes. `--write` refreshes the report. Exact finite arithmetic and matrix controls support the written proofs; they do not certify universal arguments by sampling. These are internally reviewed conditional results, with no external-expert, proof-assistant, novelty, hardware or GU prediction claim.
