---
title: "K2256 Causal reset with finite fresh resources"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied model theorem only; no source physicalization or canonical verdict
scripts:
  - tests/channel-swings/k2256_causal_fresh_resource_reset_probe.py
---

# K2256 Causal reset with finite fresh resources

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2256 Causal reset with finite fresh resources
carrier: K disjoint adjacent two-spin ports and arbitrary causal tester memory LAYER=toy CHIRALITY=N/A
pairing: positive tensor-product Hilbert inner product ON=declared_carrier
real_structure: complex conjugation and Hilbert adjoint
grading: occupation number; no fermionic intervention convention imposed
action_owner: repository-construction -- finite positive local FSWAP pulses with isolated outputs and inaccessible spent donors
target: complete adaptive reset process and joint freshness cost MAP-TYPE=intertwiner
```

## Question and supplied interface

[K2252](k2252-adaptive-reset-interface-2026-10-29.md) realizes prepared-input routing, but its old outputs interact with later inputs. Here every output is delivered BEFORE the next input and never interacts with the device again. Use K disjoint adjacent pairs (S_k,B_k), not an unimplemented single-port conveyor. At round k the tester supplies S_k, possibly entangled with all its memory, and B_k is a fresh donor in tau_p=diag(1-p,p). After the pulse S_k is output O_k and B_k becomes permanently inaccessible spent waste. Future controls act on other pairs. Input placement, output isolation, donor preparation, switches and K ports are explicit resources.

Fresh-ancilla repeated interactions are established background; see [Attal and Pautrat](https://arxiv.org/abs/math-ph/0311002). The contribution here is the exact ordinary-output dilation, adaptive error accounting and freshness counterexample for the retained FSWAP control. No novelty or bath-renewal theorem is claimed.

## 1. Exact replacement from the existing positive local control

Use K2252's F=FSWAP, F|s,b>=(-1)^(sb)|b,s>, and

    G=I-F=n_S+n_B-(sigma_S^+sigma_B^-+h.c.), G>=0,
    exp(-i pi G/2)=F, ||G||=2.                         (1)

There is no parity restriction on input/reference states. For any rho_SR,

    (F tensor I_R)(rho_SR tensor tau_B)(F* tensor I_R)
      =sum_b p_b |b><b|_O tensor
         (Z^b tensor I_R)rho_DR(Z^b tensor I_R).        (2)

The formula uses named tensor factors: canonically reorder the input to S,B,R before applying F_SB tensor I_R; the output ordering is O,D,R. Tracing D yields exactly tau_O tensor rho_R. Thus the ordinary tensor-output channel is replacement even for an entangled input. The phase is retained in the waste; FSWAP is not ordinary SWAP and need not transfer the undisturbed input to the donor.

Output isolation removes K2252's future-input counterexample: no later device operation touches O_k. By induction, every causal tester has exactly the same accessible history under these slots as under ideal replacement slots. This includes arbitrary coherent/adaptive input preparation and quantum memory. The tester may itself process old outputs; the same tester is used in the comparison. Access to spent donors or device reinteraction with old outputs changes the interface and is not covered.

A positive uniform onsite drift omega(n_S+n_B), omega>=0, commutes with G. It factors into number phases and does not change tau or the replacement conclusion. A C1 nonnegative pulse g(t)=sin²(t),0<=t<=pi, realizes (1), with peak added norm2 and peak derivative norm2. Each pair is used once, sequential duration Kpi,2K physical spins. The external clock and disconnection are supplied, not autonomous.

## 2. Complete adaptive error and correlated stock

Let T include the tester, all initially present inputs and its reference. If the actual initial preparation obeys

    D(sigma_(T B1...BK), sigma_T tensor tau_p^tensor K)<=delta,

where D is half trace norm, this deviation is charged ONCE by contractivity of the entire circuit. Merely correct individual donor marginals is insufficient.

Suppose slot k has pulse area pi/2+Delta_k and an additional perturbation with integrated full operator norm eta_k (in the appropriate interaction picture). The ideal F error obeys

    ||U_k-F||<=2|sin Delta_k|+eta_k
                 <=2|Delta_k|+eta_k.                 (3)

Common known onsite phases may be included in both dilations. Duhamel and a telescoping hybrid interleaving the SAME causal tester give

    D(actual accessible history, ideal history)
      <=min(1,delta+sum_k(2|Delta_k|+eta_k)).           (4)

Unitary operator error bounds purified state distance, partial trace contracts it, and every remaining tester/device CPTP map contracts it. This proves a complete adaptive process bound, not only a collection of marginals. Joint stock closeness is not multiplied by K. Conditioned rare histories do not inherit an unscaled normalized error.

For K=1000,p=1/5,delta<=1/10000, |Delta_k|<=1/1000000, sum eta_k<=1/10000, equation(4) is at most11/5000=0.0022. This needs2000 spins,1000pi time in the pulse units, nominal ideal-stock mean onsite energy200omega, and ideal-stock entropy1000 h(1/5). With joint preparation error delta, actual stock energy can differ by at most1000omega delta; exact actual entropy is not asserted. It consumes1000 independent prepared donors; it is not renewable service.

### Reduced-channel improvement and exact stock dimension

Because each donor is discarded permanently, the hybrid can compare reduced slot channels instead of entire dilations. For U_alpha=exp(-i alpha G), direct matrix-unit calculation gives q_out=cos²(alpha)q+sin²(alpha)p and rho01,out=exp(i alpha)cos(alpha)rho01. This is the generalized amplitude-damping channel in [K2249](k2249-finite-density-chain-reset-2026-10-29.md), up to a known number phase. Its complete distance from replacement is at most r/2+max(p,1-p)r², r=|cos alpha|. The proof decomposes a positive input/reference block matrix: the offdiagonal block trace norm is at most1/2, and the diagonal population contribution is at most max(p,1-p). The phase does not affect this bound. Thus replace2|Delta_k| in(4) by |sin Delta_k|/2+max(p,1-p)sin²(Delta_k). For the1000-call consumer above the total is below0.000701, including the same delta and perturbation budgets. This strengthening is licensed by irreversible donor isolation, not by assuming restored donor independence.

There is also an exact resource lower bound in a deliberately restricted class. For a CLOSED unitary dilation of K input/output qubits with a donor Hilbert space of dimension d and donor-state rank r<=d, and no other discarded ancilla or hidden controller memory, the induced channel has Kraus rank at most dr<=d². For0<p<1 the exact K-fold replacement channel has Choi matrix I_(2^K) tensor tau_p^tensor K of rank4^K. Hence d>=2^K. The K-donor construction attains this donor dimension. This is exact dimension optimality within that dilation class, not an approximate, energy, time or unrestricted apparatus optimum; a tester injecting an extra discarded memory changes the count.

## 3. Why donor marginals and a returned marginal are not freshness

Prepare two donors jointly as (1-p)|00><00|+p|11><11|. Each donor marginal is exactly tau_p. Give both slots vacuum inputs and apply exact F. The two outputs have the same correlated mixture, whereas two ideal reset slots produce tau_p tensor tau_p. Their distance is

    2p(1-p)=8/25 for p=1/5.                            (5)

An adaptive tester need not even be used to witness failure. Correlations with an initial tester likewise violate the independent-stock premise.

Even one spent donor is unsuitable as a blindly reused fresh resource. Its marginal is D_p(rho)=(1-p)rho+pZrho Z, with mean occupation equal to the previous input's. For |+> at p=1/5 it retains offdiagonal3/10 and mean1/2, unlike tau_p. Feeding a new vacuum input to that donor exposes wrong output populations. In the one-use dilation, S(D_p rho)>=S(rho), and I(O:D)=S(D_p rho)-S(rho). Total entropy is conserved by the pulse; erasure moves information into waste and correlations. No universal Landauer work cost is inferred without a bath/return protocol.

This closes a finite causal reset interface with explicitly stocked resources. Replenishing correlated donors, operating one fixed port with local transport, or deriving autonomous timing are new physical constructions; complete finite stock is not evidence for any of them.

## Reproduction and scope

Run `python tests/channel-swings/k2256_causal_fresh_resource_reset_probe.py`; `--write` refreshes its exact report. Finite exact controls and changed-input faults supplement the written universal proofs, not certify them by sampling. The concrete proof and controls received independent internal specialist review; no Lean, external-expert, novelty or remote-CI certification is claimed.

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 remains UNCERTAIN on the southeast rival; SC-META-53 remains UNCERTAIN on physical positivity. These results concern supplied constructions, not every source-admitted completion. LT-SM8/LT-GR6b/AC-F1 and ledger0.263 remain unchanged. Preserve full16cells/full20/K-C, native2+1/nonchiral, physical quotient and global source-domain debts.
