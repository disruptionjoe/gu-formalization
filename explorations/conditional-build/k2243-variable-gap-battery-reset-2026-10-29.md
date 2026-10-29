---
title: "K2243 Finite variable-gap reset with exact conserved energy"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied mathematics; no source selection or physical recovery
scripts:
  - tests/channel-swings/k2243_variable_gap_battery_reset_probe.py
---

# K2243 Finite variable-gap reset with exact conserved energy

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2243 Finite variable-gap reset with exact conserved energy
carrier: finite control register, qubit record and fresh cells, finite one-axis or multi-axis battery LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert trace ON=declared_carrier
real_structure: explicitly stated real matrices or complex Hilbert adjoint below
grading: energy occupation and register labels, no fermionic grading
action_owner: repository-construction -- supplied fixed nonnegative data Hamiltonian and clock
target: variable-gap reset, retained reference and battery accounting MAP-TYPE=intertwiner
```

## Result and construction scope

An explicit finite control register converts variable-gap reset into gates commuting with one fixed enlarged Hamiltonian. Uniform ladders implement integer-multiple gaps; a finite multi-axis battery implements arbitrary positive real gaps, including the earlier logarithmic schedule. The reduced record/reference reset is exact and does not require battery coherence. A coherent sine packet additionally bounds disturbance and correlations when the battery is retained. These are supplied finite apparatus models, not GU dynamics, local hardware, preparation optima or renewable heat baths.

Reuse [K2229](k2229-finite-step-thermal-reset-work-2026-10-28.md)'s thermal sequence, [K2240](k2240-finite-battery-gate-2026-10-29.md)'s sine translation and [K2238](k2238-finite-clock-thermal-circuit-2026-10-29.md)'s commuting-gate clock. The new object is the gap register and its full shell-preserving unitary, including endpoints. No source/ledger/canon result moves.

## 1. Uniform ladder and full unitary

Let q0=0, positive integer qj, and E_j=Delta qj. Put

    H_CR=Delta sum_a q_a |a><a| tensor n_R,
    H_B=Delta sum_(k=0)^N k |k><k|,
    H_cells=sum_(j=1)^K E_j n_j.                    (1)

A ramp between labels a,b swaps |a,0,k> with |b,0,k> for every k. It also swaps |a,1,k> with |b,1,k+q_a-q_b> whenever both levels exist. All unmatched boundary states and other labels are fixed. Disjoint transpositions define a unitary involution on the ENTIRE finite space, commuting with(1). A one-way shift plus fixed endpoint is not a unitary; cyclic battery wrap violates energy conservation.

At label j apply the SWAP of R and cell j, conditioned on |j><j|, with identity on other labels. On the active label their gaps agree. This gate commutes with the full Hamiltonian on every sector. An unconditional SWAP generally fails this test.

Initialize register0 and independent Gibbs cells tau_j with p_j=(1+exp(beta E_j))^-1. Alternate ramps0->1->...->K and the corresponding controlled SWAPs, then lower K->0. There are2K+1 gates, K fresh cells and K+1 control states. Every reachable control label is deterministic. The reverse branches of full transpositions ensure unitarity but are not visited on this initialized computation.

## 2. Margins and exact reset without coherence

For monotone integer q1<=...<=qK=Q, battery shifts before lowering lie in[-Q,0], because every upward increment multiplies occupation0 or1. The last lowering adds Q times its last occupation, so final shifts lie in[-Q,Q]. Support k=Q,...,Q+L-1 in a battery0,...,L+2Q-1 is safe at every step; its dimension is L+2Q.

For any initial battery density operator on this safe support, independent of the record/reference and fresh stock, each ramp preserves the record's occupation; each fresh SWAP replaces its state by tau_j. The final ramp leaves the record diagonal with probability p_K. Tracing battery and cells gives EXACTLY

    rho_RF -> tau_K tensor rho_F.                  (2)

The final ramp may correlate battery and record, but each conditional battery unitary preserves the reference marginal. Thus(2) remains true for arbitrary entanglement of initial R with F. Its half-diamond distance to pure reset is exactly p_K: tensoring rho_F leaves the trace norm of tau_K-|0><0| unchanged. A dephased battery or a single safe energy eigenstate is enough. Coherence is not a reset prerequisite.

For initial record excitation w, the mean battery decrease is exactly

    W=w E1+sum_(j=2)^K p_(j-1)(E_j-E_(j-1))-p_K E_K. (3)

The control returns to zero record gap; total energy conservation equates(3) to increased cell energy. These are actual mean energy transfers, independent of battery coherence; they do not price Gibbs preparation or clock engineering. Entropy and correlations reside in spent cells/battery, so no finite cyclic entropy sink is supplied.

## 3. Stronger joint restoration bound

Take K2240's normalized sine packet on L consecutive battery levels. Its one-step translation defect is d=2sin(pi/(2(L+1)))<=pi/(L+1). A shift h has defect at most |h|d by telescoping translations. On the active control label, occupation sectors are orthogonal, so ramp-versus-ideal norm error is at most |q_a-q_b|d, also after tensoring a reference. Purification bounds joint half trace distance by this norm.

Hybrid telescoping compares actual and ideal prefixes with the SAME initial packet, retaining all cells and reference. For the monotone circuit the absolute ramp differences sum2Q; SWAPs contribute zero. Therefore

    epsilon_joint <= min(1,2Q pi/(L+1)).             (4)

Initial packet independence is needed for this statement. It compares against the ideal gap operations with an unchanged battery; it does not mean the exact battery has zero work transfer. A small trace error permits finite energy differences when the battery energy range is large. For initial correlated batteries the bound needs a whole-joint preparation error, not just a marginal estimate.

## 4. Irrational gaps: exact multi-axis completion

A single uniform ladder cannot exactly transfer a gap not in Delta Z. The K2229 displayed gaps contain log(7/3) and log(101/100), which are rationally independent: an integer relation would contradict prime valuations at7,3 and101. This excludes exact use of ONE uniform ladder with those gaps, not finite batteries generally.

Supply instead K coordinates k_j in{0,...,L+1} with

    H_B=sum_j E_j k_j,
    d_B=(L+2)^K.                                   (5)

Let e0=0 and e_j the jth coordinate vector. Ramp a->b translates the excited battery by e_a-e_b. Define full transpositions exactly as before, using only pairs inside the box; other states are fixed. Energy is conserved for arbitrary positive real E_j, including rational dependencies or irrational ratios.

Along the initialized path, coordinate j receives -n_before_j at entry and +n_after_j at departure, each at most once. At all times it lies in{-1,0,1}; there is no hidden shift by2. Product packet support1,...,L on each coordinate is safe. This proves exact(2),(3) for the original logarithmic schedule as well, at an enormous explicit finite dimension. The joint product-sine bound is

    epsilon_joint <= min(1,2K pi/(L+1)),
    initial mean H_B=(L+1)/2 sum_j E_j.              (6)

Each coordinate translation is charged twice at most. The exponent in(5), high initial energy and supplied exact gaps are real costs; this is not efficient apparatus or a reusable stock theorem. Safe diagonal product batteries still suffice for reduced reset. This follow-through removes a commensurability limitation without hiding it in a freely adjustable single-ladder spacing.

## 5. Clock composition and explicit consumer

All gates now commute with one fixed finite nonnegative data Hamiltonian. Apply K2238 with programmed length2K+1, R_pad identity gates, M=2K+1+R_pad, clock dimension M+1, bandwidth2gM and endpoint T=pi/(2g). After tracing clock, the padded timing error is

    epsilon_clock <= min(1,binom(M,R_pad+1)|g delta|^(2R_pad+2)). (7)

The retained record/reference reset error is p_K+epsilon_clock, without(4) or(6). The complete comparison retaining battery adds its joint error. Ideal comparison must include same-time free data evolution; energies and Gibbs populations are unaffected. The initial clock must be independent or whole-joint close to its required preparation.

For beta Delta=log2, qj=j and K=20: p_K=1/1048577<10^-6,41 gates,21 register states,20 fresh cells. With R_pad=8, M=49, d_clock=50, |g delta|<=10^-3 gives binom(49,9)/10^54<10^-44. For joint battery error below.01 choose L=12572; d_B=12612 and40pi/12573<.01 using pi<22/7. The clock bandwidth is98g. For w=1/2, (3)/Delta is exactly 1/2+sum_(j=1)^19 1/(1+2^j)-20/(1+2^20), lying strictly between1.26 and1.27 by rational arithmetic. No Landauer-optimality claim is made for this coarse schedule.

At the endpoint the register returns0 but the continuing clock Hamiltonian still acts. Extraction/readout, clock reset, replenishing Gibbs stock and permanent isolation are not supplied. K2238's recurrence and finite-plateau obstruction remain. Extending the existing microscopic reservoir/entropy-export model requires new dynamics, not a claim that the present finite box renews itself.

## 6. Hostile checks

Preflight rejected one-way shifts and inherited incommensurate single-ladder consumers. Postflight checks full-space conservation (not just the active path), pathwise margins, reference decoupling versus battery correlation, coherent restoration versus reduced reset, and actual mean energy. The finite probe enumerates complete small shell permutations, histories, matrix-unit reference traces and multi-axis irrational-energy coefficient vectors. Wrong shifts, wraparound, unconditional SWAP, inadequate margins and omitted lowering are actual input faults. Universal resource and reference proofs are written above.

## Reproduction and evidence kind

Run `python tests/channel-swings/k2243_variable_gap_battery_reset_probe.py`. The default checks a clean baseline, actual input faults under unchanged predicates, and note/code/dependency hashes. `--write` refreshes the report. Exact finite arithmetic and matrix controls support the written proofs; they do not certify universal arguments by sampling. These are internally reviewed conditional results, with no external-expert, proof-assistant, novelty, hardware or GU prediction claim.
