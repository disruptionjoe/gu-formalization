---
title: "K2436 Direct certification of a process with memory"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: tested conditional fixed-slot processes only; no optimal dimension factor, future transfer, physical calibration or native GU identification
---

# K2436 Direct certification of a process with memory

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
result: K2436
carrier: fixed finite r-slot causal quantum comb with arbitrary internal memory and retained references LAYER=toy CHIRALITY=N/A
pairing: normalized process Choi fidelity and half strategy discrimination distance ON=declared_carrier
real_structure: complex positive Hilbert states and completely positive causal maps
grading: input/output slots, within-batch order and pre-batch history
action_owner: repository-construction -- imported quantum process framework
target: tested conditional process averages against a fixed memoryless unitary sequence MAP-TYPE=evaluation
```

## Result

A complete r-slot Bell experiment can bound the adaptive distinguishability of the **whole tested process**, even when its internal memory persists across slots. For input dimensions d_Ai, output dimensions d_Bi, D=product_i d_Ai, and a fixed memoryless unitary target (equal input/output dimension within each slot), define

    K^2=D product_(i<r) d_Bi.

If p is the failure probability of the target product-Choi projector on the normalized process Choi state, then

    delta_strategy(process,target) <= min(1,K sqrt(p)).              (1)

For r qubit slots K^2=2^(2r-1). Trusted imperfect preparation, readout and stopping-safe batch statistics compose into

    mean delta_strategy <= min(1,K sqrt(B(a,e))),                     (2)

using [K2434](k2434-direct-preparation-leakage-2026-11-01.md)'s sharp preparation-transfer function. The same bound holds for the distance of the mean tested conditional process. These conclusions require an entire temporal experiment; isolated reset-channel tests do not supply it.

The process/strategy representation and discrimination metric are standard [Gutoski--Watrous](https://cs.uwaterloo.ca/~watrous/Papers/GeneralTheoryQuantumGames.pdf) and [Gutoski](https://arxiv.org/abs/1008.4636) frameworks. The purpose here is to provide a proved consumer for the repository's preparation and adaptive-statistics interfaces. No novelty or optimal dimension/sample constant is claimed. This is imported conditional quantum mathematics; SC-META-53 remains UNCERTAIN, ledger0.263 is unchanged, and no physical device or native GU probability construction is supplied.

## 1. The exact process being tested

Fix the slots and the unitary target sequence before observing outcomes. Let C be the unnormalized Choi operator of a deterministic causal comb, with trace D, and rho=C/D. In chronological Bell probing, prepare a Bell pair for every input before slot one, keep all references inaccessible to the device, feed each signal at its slot, and retain all outputs. The final output/reference state is rho. Arbitrary internal device memory and correlations across slots are allowed. The target state is the rank-one projector P=|Phi_U><Phi_U|, the tensor product of the target unitary Choi vectors.

Define delta_strategy as the supremum, over all causal adaptive testers with arbitrary reference memory, of half the trace distance between their final accessible output states for C and the target. It prices interventions that depend coherently or classically on earlier outputs. The calibration experiment itself is the fixed Bell experiment; the bound quantifies other testers on **that same initialized comb**.

A process can change with pre-batch recorded history. That gives a family C_t, each initialized with the actual memory marginal at its own batch start. Neither (1) nor testing identifies a future initialization or future comb.

## 2. Pure-target proof with the correct tester norm

Purify a causal tester and retain its internal environments. Connecting it to a normalized Choi operator is a CP linear map Xi, normalized on deterministic combs. Its effect satisfies

    Xi*(I)=D T, T=I_Br tensor S,
    S>=0, Tr S=product_(i<r) d_Bi.

These equalities follow from the co-strategy causal trace constraints. In particular ||Xi*(I)||<=K^2. It is generally **not** bounded by D: feedback testers need not have ||T||<=1.

For the memoryless unitary target, the purified tester's ideal output is pure, say psi. Set F=Xi*(I-psi). Then F>=0, F<=K^2 I and Tr(FP)=0. Positivity implies FP=PF=0, and therefore

    F <= K^2(I-P).

The actual tester output has infidelity to psi at most K^2 p. Its half trace distance is at most the square root of that infidelity. Discarding retained tester environments cannot increase distance; taking the supremum proves (1). The proof exploits the target's purity. It cannot be transferred silently to a mixed noisy target or a mixed recorded instrument.

The exact two-qubit feedback tester prepares |0> at slot1 and feeds its output directly into slot2. In tensor order B2,A2,B1,A1,

    T=I_B2 tensor |Omega><Omega|_(A2 B1) tensor |0><0|_A1,
    ||T||=2, ||Xi*(I)||=8, D=4.

The probe builds its original contraction matrix L, checks L*L=4T, verifies L Phi_U=|0>, and directly checks F<=8(I-P). A generic trace-distance conversion with tester norm assumed one would have an invalid premise. A potentially sharper sqrt(Dp) constant is not established here.

## 3. Whole-batch preparation and adaptive statistics

For batch t condition on recorded history before that batch. Let A contain **all** signal/reference resources prepared jointly before slot1, and M every initial returning device-memory degree of freedom. Let q_t be the true infidelity of the A marginal to the complete target input Bell product. The physical device acts on signals and M, never on references. Regard the chronological sequence as one CPTP map; define the counterfactual ideal comb using exactly the actual initial marginal rho_M,t. This is the object to which (1) applies.

Let p_t be the actual true product-test failure. K2434's dimension-independent pure-resource argument gives

    p0_t <= B(p_t,q_t),
    B(p,q)=q+(1-q)(sqrt((1-q)p)+sqrt(q(1-p)))^2 if p+q<=1,
           1 otherwise.                                             (3)

Measure all outcomes without postselection. A lost readout is retained as failure under the declared measurement contract. The process theorem assumes the fixed square-slot carrier; a physical erasure output outside that carrier needs an explicitly enlarged output space, target and recomputed constants before applying (1). Use one retained Bernoulli failure outcome for the whole batch. [K2430](k2430-adaptive-decoder-certification-2026-11-01.md)'s declared stopping-safe protocol gives u_n bounding the average observed conditional failure. With effect-error allowances eta_t and a simultaneous calibrated mean-infidelity bound e in[0,1], put

    a=min(1,u_n+mean eta_t), e>=mean q_t.

Concavity and monotonicity of B imply mean p0_t<=B(a,e). Concavity of square root and convexity of strategy distance prove (2), for both mean distance and distance of the mean comb. Coverage is at least1-alpha-beta when the statistical failure allowance is alpha and the simultaneous calibration event fails with probability at most beta; independence of these events is not needed.

Controls can adapt **between batches**. The pre-batch joint-resource premise does not automatically cover adaptive resource preparation within a batch, reference leakage, changing slot dimensions, unpriced heralding, resetting counts or changing the target after observing outcomes. Those require a separately specified experiment. No device-memory reset is required inside a tested batch; transfer to a future batch still needs its own evidence.

## 4. Executed successor: individual Bell measurements in the same batch

A collective entangling measurement across all slots is unnecessary for this product-unitary target. The commuting per-slot projectors P_i obey

    I-product_i P_i <= sum_i (I-P_i).                                (4)

Measure each output/reference pair after the process (or earlier only if the retained subsystem will never interact again). Record the full outcomes and define batch failure as any failed slot. This realizes the product test exactly. If only separately bounded marginal failure probabilities from **this same joint batch ensemble** are available, their sum upper-bounds the corresponding joint failure: p for the actual experiment, p0 for counterfactual ideal marginals. Measured imperfect-preparation bounds still require the section3 B transfer before using (1). Apply the marginal bounds' own simultaneous error allocation.

The same pure-projector union inequality bounds whole-resource infidelity by the sum of calibrated Bell-resource marginal infidelities from that same pre-batch preparation. It requires no independence between the resource pairs. Separate ensembles or measurements after different resets cannot be combined as though they were the same joint preparation.

In particular, exact pure target Bell marginals in one complete process-Choi experiment force the joint state to equal P and the entire process to equal the target. There is no hidden-memory counterexample under those exact premises. Near-perfect marginals give the explicit sum bound, rather than a qualitative assumption of independence.

## 5. Memory controls and quantitative consumer

A shared fair X label applied in two slots and independent fair X labels have identical complete one-use channels, but different processes. Input |00> yields equal output bits with certainty in the shared case and probability1/2 in the independent case; the output-state distance is1/2. Their normalized Choi operators satisfy the causal trace constraints exactly. **Their one-use marginals are noisy, not pure unitary targets.** This example does not contradict section4.

For a sufficient prospective1% strategy-distance target, alpha=.05, perfect preparation/readout and zero retained batch failures, choose

    n > K^2 log(20)/0.01^2.

The [report](../../lab/process/k2436-multiround-process-certificate.json) gives rigorous rounded-up budgets for1,2,4,8 qubit slots and counts both batches and slot uses. The four-slot requirement is about3.835 million complete batches; the eight-slot requirement is about981.64 million. These are conservative sufficient requirements, not observed data or optimal complexity. The exponential dimension factor is exposed rather than hidden in a one-use constant.

With four times the ideal zero-count budget, the report also uses K2434's exact inverse of B to certify a positive whole-batch preparation budget. A simple tested choice is e=v/100, v=0.01^2/K^2. More samples do not remove fixed preparation/readout floors. At infinite samples and zero readout the bound still requires e<=1-sqrt(1-v).

Further consequences use the same event: the fraction of tested batches at distance>=epsilon is at most min(1,K^2 B(a,e)/epsilon^2); weights bounded by rho/n give distance<=min(1,K sqrt(rho B(a,e))). These are claims about the tested family. A process that behaves ideally during every test and changes afterwards remains an exact countercontrol to unsupported future transfer.

## Verification and remaining frontier

[Probe](../../tests/channel-swings/k2436_multiround_process_certificate_probe.py) checks exact real and genuinely complex phase-unitary state constructions, causal partial traces, feedback normalization, pure-target operator inequality, shared-memory discrimination and projector union bounds. Arb256 certifies prospective budgets. The universal result rests on sections2--4, with independent internal review; it is not inferred from the finite fixtures.

```sh
python tests/channel-swings/k2436_multiround_process_certificate_probe.py --check
```

Dependencies are SymPy and python-flint. The next physical step is a declared complete batch experiment with actual trusted joint resource/readout evidence, slots and operational costs. A sharper dimension constant or mixed/instrument target needs a new theorem. The existing nonunitary recovery target is not silently replaced by an ideal unitary: (1) is a separate process-level interface whose applicability must be established for a chosen consumer. Native GU identification and future deployment remain open.
