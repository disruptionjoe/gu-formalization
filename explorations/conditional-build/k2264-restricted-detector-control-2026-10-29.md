---
title: "K2264 Pairwise conserving control for the full detector"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied conditional model only; no source physicalization or canonical verdict
scripts:
  - tests/channel-swings/k2264_restricted_detector_control_probe.py
---

# K2264 Pairwise conserving control for the full detector

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2264 Pairwise conserving control for the full detector
carrier: finite hard-cutoff charged oscillator registers, neutral record workspace, and K2253 full field instrument LAYER=toy CHIRALITY=N/A
pairing: positive tensor Hilbert space, operator norm and half trace distance ON=declared_carrier
real_structure: complex conjugation and Hilbert adjoint
grading: copy, occupation and record labels; not physical chirality
action_owner: repository-construction -- supplied mathematical model
target: explicit two-subsystem control alphabet and complete instrument synthesis MAP-TYPE=intertwiner
```

## 1. Replace arbitrary shell control by a stated alphabet

[K2253](k2253-full-instrument-reference-reuse-2026-10-29.md) supplies a finite number-conserving shell unitary for the full recorded detector; [K2262](k2262-coherent-reference-supply-2026-10-29.md) supplies fresh coherent reference replacement. Neither proves a restricted control synthesis. Here we prove approximate synthesis from an explicit finite alphabet. The locality is **at most two tensor subsystems per Hamiltonian term**, with all-pair diagonal couplings. It is not spatial finite-range locality or a continuum apparatus.

Take s=m+1 charged registers: m field-mode registers capped at R and a battery capped at H. Write caps c_i>=1, occupation n_i=0,...,c_i, and one neutral workspace of dimension a>=2. The physical field Fock space is compared through these finite low-level sectors. Hard local walls are an explicit supplied engineering assumption; truncated ladders cannot be silently identified with ordinary infinite bosonic controls. Extra neutral dimensions may be added finitely before synthesis. On each full field-mode Fock space define its bounded ladder and occupation functions as the stated finite block on levels0,...,R and zero on the orthogonal complement. Keep tensor identities on spectators. Every resulting generator remains at most two-subsystem and commutes with physical number. The finite tensor box is reducing, so there is no cutoff leakage. Outside that box the resulting conserving unitary need not be identity. This is a local block extension, not a global cube projector masquerading as a local interaction.

Allowed independently signed controls, each a Hermitian fixed matrix times a real pulse, are:

- diagonal N_i, N_i² and N_iN_j for EVERY i<j;
- neutral projectors P_l=|l><l| and N_i P_l for EVERY i,l;
- nearest-neighbor ladder hopping X_i=a_i* a_(i+1)+a_(i+1)* a_i on a connected charged chain, with hard-cutoff ladder matrices;
- neutral neighbor flips Y_l=|l+1><l|+|l><l+1|.

Tensor identities on spectators are understood. Every term commutes with total NUMBER. Self/cross-Kerr and number-dependent neutral energies are substantive supplied nonlinear controls. Relative control phases and classical timing are supplied; they do not by themselves supply total-number asymmetry. Nonuniform physical energy conservation is not claimed.

## 2. Actual configuration graph and integer separation

Vertices are z=(n_1,...,n_s,l). An edge changes one quantum between adjacent charged registers, or moves l by one. In every total-charge shell the graph is connected. To see charged connectivity, compare any occupation vector with the left-packed vector: move available quanta left along the chain into vacancies, relaying vacancies when an intermediate site is full. This reduces the sum of position-weighted occupations until the unique left-packed vector is reached. Neutral flips then connect the label factor. All moves respect the caps.

List the diagonal features

    f=(N_i,N_i²,N_iN_j (i<j),P_l,N_iP_l),
    F=2s+s(s-1)/2+a+sa.

For every DIRECTED primitive edge the difference vector Delta f is nonzero and unique across the full finite carrier, even across different total shells. For a hopping edge, Delta N identifies direction and pair; Delta N_i² identifies the two endpoint occupations, cross terms Delta(N_iN_j) recover each spectator occupation, and Delta(N_iP_l) identifies the neutral label. For a neutral flip, Delta P identifies the two labels and Delta(N_iP_l) recovers every occupation. These claims concern primitive edges, not all ordered pairs of arbitrary configurations.

Let C=max(1,max c_i²), b=4C+1 and

    D0=sum_(k=0)^(F-1) b^k f_k, Lambda=max_z D0(z), M=2Lambda+1.

All feature values are integers between0 and C. If two edge gaps were equal, subtract their difference vectors: digits lie in [-2C,2C]. The largest nonzero base-b digit dominates the sum of all smaller ones, a contradiction. Thus the directed gaps Delta_e are distinct nonzero integers in [-Lambda,Lambda], and distinct modulo M. This explicit coding is exceptionally expensive but finite. Dropping spectator cross terms would invalidate the proof: frequency selection then addresses several configurations at once.

## 3. Fourier isolation without supplying shell projectors

For a primitive Hermitian X, an edge v<-u has positive coefficient c_e (a square root of occupation products for hopping, or1 for label flips). Put Delta_e=D0(v)-D0(u), t_j=2pi j/M. Its desired Hermitian edge generator is

    H_e(phi)=e^(i phi)|v><u|+e^(-i phi)|u><v|.

Discrete Fourier orthogonality proves the EXACT matrix identity

    H_e(phi)=(1/M) sum_(j=0)^(M-1)
       [2cos(phi-Delta_e t_j)/c_e] e^(i t_j D0)X e^(-i t_j D0). (1)

Only e and its reverse survive; all other directed edge gaps differ modulo M. Each summand's exponential can be realized by conjugating one primitive pulse with diagonal evolution. D0 is a sum of F commuting one-/two-subsystem features, so its conjugation is a sequence of at most F such pulses on each side. Equation(1) does not assume independent edge control; it constructs it from the allowed alphabet.

Let S=2||X||/c_e. The sum of the norms of the M weighted summands is at most S. First-order product formula with r repeats approximates exp(-i theta H_e) with operator error at most

    theta² S²/r.                                    (2)

For skew-Hermitian generators, integrate the commutator defect for one step, use ||[A,B]||<=2||A||||B|| and unitary norms1, then telescope r steps. This gives the stated conservative bound without an exponential amplification factor. Choosing r>=theta²S²/eta produces error<=eta with at most r M(2F+1) primitive pulses. This is a constructive finite bound, not a practical compile-time guarantee. A modular implementation can reduce conjugation times using integral spectra, but no such optimization is needed.

## 4. From edges to the actual shell isometry

Connected-graph edge X/Y rotations generate SU(d_t) independently in each charge shell of dimension d_t>=2. One explicit route is QR by Givens rotations between arbitrary vertex pairs, realized by path swaps, a local edge rotation and the inverse path swaps. Each path has length<=d_t-1. Two transverse edge axes give its SU(2), including needed diagonal phases. Counting at most d_t(d_t-1)/2 elimination rotations and d_t-1 diagonal phase corrections, each with a fixed SU(2) Euler decomposition and route/unroute, a deliberately loose bound of100 d_t^3 elementary edge X/Y rotations suffices. The proof needs no independent shell-wide U(1) phase.

The K2253 prescribed action occupies only the low-input subspace with a fixed initialized neutral state. Choose a>=2 large enough for its finite isometry and at least one unprescribed direction in every relevant nonzero shell. Complete its isometry to any unitary and adjust the determinant by a phase on that complement; this produces SU(d_t) while leaving the prescribed action EXACT. In irrelevant shells choose identity. A one-dimensional shell with fully prescribed nontrivial phase would defeat this step; neutral enlargement prevents that case. Arbitrary independent U(d_t) synthesis is not claimed.

Let J<=100 sum_t d_t³ be the total number of edge rotations for the chosen completion. Allocate each error eta= zeta/J (omit identities). Formula(2) gives a finite full-carrier compilation with operator error<=zeta. For m=2 the charged caps are(R,R,H), so the full workspace has dimension (R+1)²(H+1)a; this is finite for the actual K2253 cutoffs, but vastly too large to imply practical implementation. No full matrix of that size is built or numerically certified here. The universal constructive argument, not finite controls, supplies the dimensional generalization.

## 5. Bounded C1 pulses, drift and full-instrument composition

For a primitive Hermitian A and signed integrated angle theta, use

    h(t)=2theta/T sin²(pi t/T), 0<=t<=T,

zero outside. The pulse and its first derivative vanish at its endpoints, its area is theta, peak Hamiltonian norm is <=2|theta|||A||/T, and slew is <=2pi|theta|||A||/T². Any finite positive peak/slew limits J0,S0 are met by

    T>=max(2|theta|||A||/J0, sqrt(2pi|theta|||A||/S0)). (3)

All diagonal coefficients, frequencies, number of switches and durations are finite and may be enormous. A common drift omega N_total commutes with every term and yields known exp(-i omega N_total T_total). State the comparison in that rotating frame or supply the corresponding local number-phase correction; discarding this rotation would change the phase-sensitive detector. Unequal or uncontrollable drift is outside this theorem.

Operator error zeta on the invariant finite box adds at most zeta to half trace distance for box-supported input entangled with arbitrary external history, by applying the two unitaries to a purification and contractivity. For general full-Fock inputs apply this comparison to K2253's low-input component: Q<=R puts that component in the box, and its existing input-tail term2sqrt(B0/(Q+1)) already covers the remainder. No uniform full-Fock operator-norm comparison to an identity extension is asserted, and no second input-tail penalty is needed. Thus K2253's actual complete FIELD+RECORD+external-reference+retained-battery comparison becomes

    error_K <= K e(B0;Q,R,L) + sum_j zeta_j + sum_j integral||Delta H_j||dt,
    e=2sqrt(B0/(Q+1))+sqrt(2C_det(B0+1)/(R+2))+(Q+R)pi/(L+1). (4)

Use the same ideal-prefix/actual-suffix hybrid; ideal unconditional energy bounds per call and controllers not accessing the battery remain substantive. The construction includes neutral environment and record dephasing, not merely binary effect probabilities. With K2253's K=10,B0=1,C_det=81,Q=15999999,R=5183999998,L=99999999999999, base error is below.00914. Total compilation budget.0001 and Hamiltonian-error budget.0001 give full error below.00934. Initial joint preparation error, if present, adds once. This shared-reference version needs one supplied sine packet; it does not require fresh coherent SWAP between calls. Fresh-stock K2262 can instead be composed with all its own replacement costs.

## 6. Explicit finite resource followthrough for the actual detector

For this two-outcome Lüders target the coherent isometry has no additional environment before record dephasing. Its K2253 failure completion needs a neutral input copy of dimension d_Q=(Q+1)(Q+2)/2. A neutral record2 tensor environment(d_Q+1), hence a=2(d_Q+1), contains both success record states with environment0 and failure record0 with an orthogonal d_Q-dimensional environment. The same space provides spare completion directions in every relevant shell. Thus one concrete choice at the stated cutoffs is

    d_Q=128000008000000, a=256000016000002,
    D_box=(R+1)^2(H+1)a, F=9+4a,
    H=100005199999995, C=H^2, b=4C+1,
    Lambda<=C(b^F-1)/(b-1), M=2Lambda+1.            (5)

Use the actual maximum Lambda when constructing the filter. Its bound proves finiteness without writing an integer with an astronomical number of digits. Since sum d_t=D_box, take J<=100D_box^3. Each nonzero hopping coefficient is at least1 and each primitive hopping norm at most2H; neutral flips have norm1. Choose edge Euler angles with |theta|<=2pi and a common repeat count

    r=ceil(64(22/7)^2 H^2 J/zeta).

Then every edge error is at most zeta/J, and at most J r M(2F+1) primitive pulses suffice. J may be replaced by the conservative integer100D_box^3 when allocating precision. Smoothness is only C1 with bounded slew as in(3). If total allowed Hamiltonian error is eta_total, an equal per-pulse allocation is eta_total/[J r M(2F+1)] in integrated operator norm. This prices timing and precision as well as dimension; it is an existence compiler with extreme resource demands. No large matrix, integer frequency table or pulse list was materialized by the finite controls.

The full detector channel can therefore be approximated to the stated error under this explicit alphabet, but arbitrary shell freedom has been replaced by enormous nonlinear control, coherence, time and precision resources. Determining affordable synthesis or a finite-range physical implementation remains a different research endpoint.

## 7. Necessary controls and resource boundary

An independent negative control shows why ordinary untruncated passive bilinear optics alone is insufficient for shell universality. Starting in |2,0>, passive mixing produces (u a1*+v a2*)²|0>/sqrt2, with |u|²+|v|²=1. Its |1,1> probability is2|u v|²<=1/2. A full shell unitary can send |2,0> to |1,1>; passive mixing cannot. This test uses caps>=2 where the entire N=2 shell is unaffected by truncation. Hard-wall effects on higher shells can themselves be nonlinear, and the argument is not a general no-go for all ancilla-assisted passive instruments.

The alphabet cannot manufacture the required phase stock from invariant input. If rho commutes with N_total, each permitted unitary preserves that property; tracing other registers leaves a battery marginal commuting with N_B. The sine packet beta has nonzero adjacent-charge coherences for L>=2. Fresh invariant heat/charge therefore cannot prepare it through these controls. Imported coherent preparation, all-pair nonlinear interactions, hard walls, neutral work memory, timing and discarded waste remain explicit resources.

This closes an unrestricted-shell-control assumption in one specified finite tensor-local model. It does not close geometrically local finite-range synthesis, efficient large-resource scaling, autonomous timing, phase-stock production/recycling, continuum leakage or a source-owned detector. Nonlinear oscillator control is established background; see [Yuan et al., weak-Kerr universal control](https://arxiv.org/abs/2312.15783). The alphabet and finite proof here must stand on their own, rather than borrowing that paper's differently controlled system as a guarantee.

## Scientific ceiling and reproduction

SC-OP-04 ASSERTS the candidate four-field grammar; SC-OP-05 remains UNCERTAIN on the southeast rival; SC-META-53 remains UNCERTAIN on physical positivity. Ledger0.263 (88 active targets/91 stored rows), LT-SM8/LT-GR6b/AC-F1, source/canon verdicts, full16cells/full20/K-C, native2+1/nonchiral, mirrors/fullII/normaljets, scalar/thermal and cosmology ceilings are unchanged. These results do not supply a source action, physical quotient, physical chiral carrier or held-out prediction.

The universal assertions are written mathematical proofs. The accompanying finite exact controls and deliberately changed-input tests check algebra, constants and counterexamples; they do not certify continuum completeness, arbitrary-dimensional controllability or a physical realization. Internal independent review is distinct from Lean, external-expert, novelty and remote-CI certification. Run the listed script; `--write` regenerates the hash-bound report.
