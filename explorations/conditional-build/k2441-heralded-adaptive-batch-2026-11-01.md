---
title: "K2441 Heralded programming of an adaptive batch"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: "fixed controller within each complete batch; predictable averaged success subchannel only, no across-batch adaptive or final-transcript guarantee"
---

# K2441 Heralded programming of an adaptive batch

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
result: K2441
carrier: normalized r-slot process Choi program on retained input references and flagged outputs LAYER=toy CHIRALITY=N/A
pairing: completed-operation trace distance ON=declared_carrier
real_structure: complex positive Hermitian states and completely positive causal maps
grading: declared temporal slots and classical flags
action_owner: repository-construction -- supplied conditional mathematical model
target: hidden whole-batch routing and sequential Bell programming MAP-TYPE=evaluation
```

## Result

The single-input programming interface of [K2440](k2440-hidden-route-instrument-use-2026-11-01.md) extends to a **whole finite causal process**, with feedback and quantum memory inside the programmed batch. A fixed causal controller may choose later inputs using earlier quantum outputs and classical instrument flags. Accepting one Bell outcome at every slot implements that controller applied to the target comb, with success probability

    q = (product_i d_Ai)^(-2).                                  (1)

For r qubit slots q=4^(-r). The controller, its fresh private input/reference state, and its internal operations must be the same across the averaged batches and independent of each current emitted program. Its internal decisions may adapt within the batch. This distinction removes K2440's one-input restriction without claiming arbitrary adaptation between batches.

Whole mixed-process tomography and the generic tester constant already belong to [K2438](k2438-mixed-instrument-certification-2026-11-01.md); they are reused, not new results. The contribution here is the complete-batch **physical heralded consumer**, its hidden-route experiment, and the original-instrument feedback replay. Quantum comb/link products are standard [Chiribella, D'Ariano and Perinotti](https://arxiv.org/abs/0904.4483). No novelty, measured device or native GU identification is claimed. SC-META-53 remains UNCERTAIN; ledger0.263 and source polarities remain unchanged.

## 1. Sequential physical construction

A program is a density operator on R1 B1 ... Rr Br, with dim Ri=d_Ai; Bi includes every visible original flag. All these registers are prepared before use and held in trusted isolation. For a target deterministic comb C, its normalized Choi program is sigma=C/D, D=product_i d_Ai. This program can be obtained by the chronological Bell experiment of K2438, but the theorem applies to any actual emitted state, even one with a defective causal marginal.

Initialize a fixed causal controller with fresh private input and reference memory independent of the entire current program and returning device memory. At slot i it prepares Ai from its retained memory and earlier Bj, then projects Ai Ri onto the normalized Bell vector. Keep only the named successful Bell outcome, pass Bi and its original flag to the controller, and continue. Stop on a failed Bell outcome and retain a failure flag. No Pauli correction for other outcomes is presumed; the original instrument is not covariant under an arbitrary correction alphabet. Failed unknown data cannot generally be retried.

Let P_T denote the resulting success CP trace-nonincreasing map on the entire program, including the fixed controller initialization. Direct contraction of each normalized Bell bra contributes d_Ai^(-1/2), while normalized Choi encoding contributes the other d_Ai^(-1/2). Thus

    P_T(sigma) = q O_T(C),                                    (2)

where O_T(C) is the normalized final controller/reference output under the original comb. Equivalently, the usual normalized-Choi tester map Xi_T is physically realized as P_T=Xi_T/D². Deterministic causal normalization gives Tr O_T(C)=1 for every such controller, so q is independent of input, feedback and target flags **after summing all complete flag histories**. It need not be constant conditional on an individual original flag or a partial success record.

A direct inductive proof replaces the first successful Bell contraction by the corresponding first-slot Choi link, retaining all remaining program and controller memory indices; repeat through r. This proof does not factor a memory-bearing comb into independent slots. Complete the failure outcomes to make one CPTP operation on arbitrary program states. The map is physical even if the actual program is not a causal Choi state; only the target identity(2) uses causality.

### Released consequence: a flag-independent tester norm

The physical construction also improves K2438's conservative tester constant. For fixed fresh controller initialization, the first Bell-success operation has effect (rho_A1^T/d_A1) tensor I on the first program reference and all remaining registers. This is bounded by I/d_A1 even when the controller input is entangled with retained private memory. Every later successful operation is trace-nonincreasing. Therefore

    P_T*(I)<=I/d_A1, Xi_T*(I)<=D²/d_A1.                       (2a)

Thus the generic normalized-Choi-to-strategy trace-distance factor can be chosen as C=min(K²,D²/d_A1). For r qubit slots C=2^(2r-1), regardless of the number of visible classical flags. Keeping flags changes the strategy space but does not change this physical upper bound. The unflagged two-slot pure-input forwarding tester has effect norm8 for Xi. This is also sharp on causal differences: take H=|0><0|_(R1) tensor Phi_(B1,R2) tensor Z_(B2), sigma0=I16/16 and sigma0±epsilon H, 0<epsilon<=1/16. These are positive causal combs because Tr_B2 H=0, while Xi(H)=8Z and ||H||1=2. Their output-to-program trace-distance ratio is8. The probe verifies the witness exactly. This proves the two-slot constant8 is exact for the unrestricted tester class; it does not say every target needs that worst factor. For four flagged qubit slots the inherited3456 bound reduces to128. No preparation, tomography or independence premise is removed. The sharper constant is reusable by K2442's process consumer.

## 2. Hidden whole-batch test/use experiment

Condition before each batch t on the declared prior classical history. Emit a full program state rho_t, with device memory traced out. Only after emission and isolation choose a fresh private test coin of probability pi. A test measures a full-program Pauli setting and all flags; a use applies the same P_T. The choice and measurement setting cannot leak to the source before emission. Future emission may depend on prior records.

Use K2440's direct martingale, generalized to the entire program: for each coefficient j, a random setting on each of the2r qubits independently chooses X,Y,Z. The same outcome supplies all compatible marginals. If j has k nonidentity factors, its importance weight is w_j=3^k; retain the full flag-string indicator. Then

    E(W_tj|past,test)=c_tj, |W_tj|<=w_j, E(W_tj²|past,test)<=w_j.
    hat c_U,j = [(1-pi)/(pi N_U)] sum_t T_t W_tj,
    rho_U = (1/N_U) sum_t U_t rho_t,
    b_j=max((1-pi)w_j/pi,1),
    v_j=(1-pi)²w_j/pi+(1-pi),
    r_j=[sqrt(2n v_j L_n)+2b_j L_n/3]/N_U,
    L_n=log(2 M n(n+1)/alpha), M=48^r.                         (3)

For N_U>0 these simultaneously bound every coefficient of rho_U at every n, with confidence1-alpha. This is the same time-union Freedman proof as K2440, applied to the full emitted batch. It uses3^(2r)=9^r settings, not16^r campaigns. No resetting or post-hoc target selection. A bounded readout bias eta_j contributes n(1-pi)eta_j/N_U; increase b_j by(1-pi)eta_j when centering. The sparse estimator's stated second-moment bound remains required.

For coefficient error vectors e_z of all16^r Paulis at each of3^r flag strings, K2438 gives

    D(rho_U,sigma)<=epsilon=(1/2)sum_z||e_z||_2.                (4)

All dimensions and exponential observation costs remain explicit. rho_U averages each state conditioned on its own earlier history. It is not the reservoir state conditioned on all later measurements or the joint state of all used batches.

## 3. Success normalization and useful error threshold

Because P_T is fixed and linear, the average predictable success output is A=P_T(rho_U). Its trace s is an average conditional success probability. Completed-operation contractivity and(2) give

    ||A-q O_T(C)||_1+|s-q| <= 2 epsilon,
    |s-q|<=epsilon,
    D(A/s,O_T(C))<=epsilon/s<=epsilon/(q-epsilon), epsilon<q.   (5)

A uniform or selected-use-average trusted completed-operation half-diamond error kappa adds to epsilon. It includes storage, Bell operations, private initialization and the controller when bounded in that operational norm. This is a theorem about the actual program; it does not need an extra counterfactual ideal-Bell input correction. Identifying the original producing device's comb remains a different task requiring K2438 preparation transfer.

A desired normalized output error tau is ensured by

    epsilon+kappa <= tau q/(1+tau).                           (6)

For two qubit slots q=1/16. At pi=1/2, ideal successful batches per emission are1/32, with two source slots per batch. Full two-slot settings number81 and coefficients2304. The report evaluates a prospective4e15-emission example with realized N_U=2e15, empirical and readout residuals1e-8 and kappa1e-6 using Arb256. These are conditional costs and allowances, not measured counts or optimal sample complexity.

No hybrid product-process guarantee across batches follows from(5). Nor is A/s the mean of individually normalized outputs or the final-transcript conditional harvested state. Changing the controller based on pre-batch history can select errors that cancel in rho_U; the noncancelling hypothesis in K2442 is a distinct repair. A controller can be fixed before the experiment while adapting arbitrarily to earlier outcomes **inside** each batch.

## 4. Original and contrary controls

The probe reconstructs both original flagged instruments, retains all nine two-slot flag histories, uses a genuinely complex input entangled with a private reference, and applies distinct feedback unitaries selected by the first flag. Exact sequential Bell contractions match direct two-slot channel composition divided by16 on every history. Total success is1/16; individual histories differ. A classical-memory shared-X comb also passes the whole-program contraction, and differs from the independent-X process under feedback. A separate genuinely quantum-memory control stores the first input for the second output while emitting a fixed first output and discarding the second input. Its whole-program contraction preserves the private input entanglement; dephasing that memory leaves the same one-slot marginals but changes the final output distance by12/25. Thus the proof is tested beyond factorized and classical-memory programs.

The probe checks the physical success-map effect is bounded by identity, complex conjugation conventions, causal normalization, moment first/second moments and prospective costs. Revealed routing and averaging history-selected controllers are retained contrary cases. Accepting all Bell outcomes without a separately proved covariance is rejected by K2440's pinned noncovariant control.

[Probe](../../tests/channel-swings/k2441_heralded_adaptive_batch_probe.py), [report](../../lab/process/k2441-heralded-adaptive-batch.json). Universal equations(2)–(6) are written proofs; finite exact fixtures and interval arithmetic do not substitute for them. Internal specialist review is not external or proof-assistant certification.

Actual use needs trusted whole-program isolation, causal controller/Bell instruments, fresh private initialization, a complete record and enough successful outputs. Future or cross-batch entangled use remains unproved.
