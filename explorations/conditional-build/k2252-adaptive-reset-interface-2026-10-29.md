---
title: "K2252 Local parity-aware extraction and its adaptive-output boundary"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite spin circuit and exact causal-interface counterexample; no GU mapping
scripts:
  - tests/channel-swings/k2252_adaptive_reset_interface_probe.py
---

# K2252 Local parity-aware extraction and its adaptive-output boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2252 Local parity-aware extraction and its adaptive-output boundary
carrier: finite spin chain with ordered fermionic encoding, prepared input registers and retained outputs LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product ON=declared_carrier
real_structure: complex conjugation and Hilbert adjoint
grading: physical occupation and fixed Jordan-Wigner ordering; not physical families
action_owner: repository-construction -- externally controlled onsite and nearest-neighbor XY couplings
target: local implementation of prepared-input reset and temporal-output causality MAP-TYPE=intertwiner
```

## Question and retained evidence

[K2250](k2250-quantum-stream-interface-2026-10-29.md) gives a complete joint-output reset estimate for a specified fermionic extraction circuit with jointly prepared inputs. It explicitly leaves local implementation and adaptive interventions open. We implement its routing using a one-dimensional nearest-neighbor spin chain with finite positive controls, and prove why the final tensor-output channel cannot generally be promoted to an ordinary temporal reset process.

The full scattering-block bound and its finite bath estimate are reused from K2250; fermionic nearest-neighbor encoding is standard background ([Bravyi and Kitaev](https://arxiv.org/abs/quant-ph/0003137)). The new result is the explicit physical ordering, complete routing schedule, smooth finite control and error price, together with an exact temporal-interface counterexample. It is not a new fermionic-swap theorem.

Layer0 keeps tensor SWAP, fermionic SWAP, end-of-batch outputs and outputs delivered during a process distinct. This supplied positive-Hilbert model does not provide GU action/quotient data. SC-META-53 is UNCERTAIN and LT-SM8/LT-GR6b/ledger0.263 retain their scope. Native2+1 and nonchiral source claims are unaffected.

## 1. An exact positive local generator

In the ordered two-spin basis00,01,10,11 let

    F = [[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,-1]],
    G=n_left+n_right-(sigma_left^+ sigma_right^-+h.c.).

Directly G=I-F, G²=2G, spectrum(G)={0,0,2,2}, and

    exp(-i pi G/2)=F.                                  (1)

Thus FSWAP needs only onsite number terms and sign-reversed XY hopping, not an extra ZZ interaction. G is positive with norm2. In a fixed Jordan-Wigner order an adjacent pair has no intervening parity string; the -1 on11 remains essential. Ordinary SWAP is a different gate.

For a nonnegative scalar pulse g(t) with integral pi/2, the Hamiltonian g(t)G gives (1). For example g(t)=sin²(t) on0<=t<=pi, zero elsewhere, has peak Hamiltonian norm2, peak derivative norm2 and zero endpoint derivative. Joining these pulses with zero intervals is C1, not asserted C-infinity or Fourier-bandlimited. For general norm cap a>0 and slew cap b>0, choose duration T satisfying T>=2pi/a and T²>=2pi²/b, and g(t)=(pi/T)sin²(pi t/T). These caps apply to the added control; a retained background is counted separately.

## 2. Complete local layout and chronological output order

Put the spins on one line in order

    I_K,...,I_2,I_1,B_1,...,B_(M-1),

with I1 at site0. All K inputs are prepared jointly, possibly entangled with an arbitrary external reference; the M-1 bath spins independently have tau_p=diag(1-p,p). There are M+K-1 physical spins.

At round k evolve only the M-site block0,...,M-1 by its XY path hopping for effective duration tau. After this dwell and when k<K, pause bath hopping and bubble I_(k+1) from position-k to0 using k adjacent FSWAPs. Earlier outputs shift one site left. Induction gives after round k the left-to-right output block O1,...,Ok, with remaining prepared inputs to its left. After K rounds the entire output block O1,...,OK is contiguous and already in chronological order. The routing gate count is

    L_gate=sum_(k=1)^(K-1) k=K(K-1)/2.                 (2)

Each local gate is exactly the second quantization of its adjacent one-particle permutation. Therefore the full circuit equals K2250's declared fermionic network with a fixed initial input-order reversal. That reversal is itself a unitary on the jointly prepared input space; the arbitrary-input/reference bound is invariant under it. No final nonlocal output permutation is silently omitted.

A uniform onsite omega N may remain on every spin throughout. It commutes with every number-preserving hopping and FSWAP pulse and factors into a final product of number phases, preserving the thermal replacement target. If omega>=2J, every active path drift omega N+J lambda(t) adjacency is positive for0<=lambda<=1, and added routing generators are positive. Coupled-path hopping must actually be switched off during routing; this is an explicit apparatus resource.

## 3. Smooth dwell and complete resource consumer

Use a path envelope lambda(t)=sin²(pi t/(2tau)) over duration2tau for each dwell. Its integral is tau; the path adjacency commutes with itself at different times, so its effective hopping propagator is exactly the constant-coupling duration-tau propagator. Its maximum per-edge hopping is J and its maximum slew is Jpi/(2tau). Uniform onsite phases do not alter the reset bound.

Take K=10, M-1=2000000, J=1, omega=3, p=1/5, tau=10000. K2250's finite-chain bound then gives full joint-output/reference reset error below0.004501. This construction uses

    2000010 physical spins, 45 routing gates,
    elapsed duration 200000+45pi,
    initial bath mean onsite energy 1200000.

The finite-tail comparison uses active hopping time Ktau=100000, not total wall time; routing leaves the bath frozen apart from commuting onsite phases. Inputs, external switching, initial bath preparation and control precision remain supplied. This is finite-resource existence, not an efficient device, autonomous injection or renewable bath.

For imperfect routing gates, a telescoping unitary bound adds sum delta_l, where delta_l bounds the full gate operator norm error. An area defect Delta alpha has

    delta_l=2|sin Delta alpha|<=2|Delta alpha|.          (3)

If residual bath hopping during routing is at most J rho per edge, Duhamel's bound adds

    eta_off <= (M-1)J rho L_gate pi.                    (4)

These are state/reference-uniform bounds even for coherent inputs. With |Delta alpha|<=5*10^-6 per gate and rho<=10^-13, the added errors are at most0.00045 and less than0.000028286. Total error is less than0.004979286<0.005. Exact dwell calibration is assumed here; other imperfections require their own additional bound. The small off-control tolerance is exposed rather than treated as free.

## 4. Why this is not yet a temporal adaptive reset service

Take K=2 and one bath spin with p=1/5. At the first dwell use the ordinary XY unitary U whose single-excitation block is [[c,-is],[-is,c]], c=3/5,s=4/5, and whose00,11 phases are1. Put I1 in |+>. Compare I2=|0> with I2=|1>. In spatial order I2,I1,B apply

    (I tensor U), then (F tensor I), then (I tensor U).

After the first dwell the retained O1 has coherence c/2. FSWAP moves it to the left but changes that coherence's sign when I2 is occupied. The second dwell acts only on the other two spins and cannot change O1's tensor marginal. Exact reduction gives

    rho_O1^(I2=0)=[[173/250, 3/10],[3/10,77/250]],
    rho_O1^(I2=1)=[[173/250,-3/10],[-3/10,77/250]].    (5)

Their half trace distance is3/5. Any ordinary causal two-round channel must have the same first-delivered output marginal for these two choices of future input. By the triangle inequality, the final tensor-output channel in (5) is at least3/10 from every such causal channel in worst-input complete distance. More generally the lower bound is c/2 for this fixture.

This is no physical backwards signalling: the old output was stored and then interacted with I2 during routing, so it was not delivered before the future input. Nor does it contradict K2250's long-dwell reset bound; the c=3/5 small-bath fixture is a different parameter choice. It proves that a final joint-output estimate alone is not an ordinary adaptive-process estimate. Interventions on stored outputs change the algebra, and a noncausal cosine-sine decomposition cannot be inserted as a causal history-by-history proof.

A causal service must physically isolate and deliver prior outputs, or type a parity-aware operational interface and prove an appropriate strategy norm. Replacing FSWAP with ordinary SWAP restores a different tensor routing but loses the exact fermionic scattering formula, as K2250's coherent counterexample shows. Both branches remain explicit; neither grants an arbitrary adaptive reset theorem.

## Reproduction and consequence

Run `python tests/channel-swings/k2252_adaptive_reset_interface_probe.py`; `--write` refreshes the report. The probe checks exact two-site generator identities, all occupation-basis signs of local routing, the actual three-spin partial traces and numerical resource inequalities as rational arithmetic. Faults alter physical gate/input data rather than expected predicates. These finite controls supplement the written general schedule, unitary and error proofs; they do not certify them by sampling.

The next genuine missing input is output-isolating causal extraction with a full adaptive bound, or a priced parity-aware intervention contract. Repeating finite prepared-input reset or adding routing gates without specifying delivery time does not fill it. No external-expert, proof-assistant, novelty or remote-CI certification is claimed.
