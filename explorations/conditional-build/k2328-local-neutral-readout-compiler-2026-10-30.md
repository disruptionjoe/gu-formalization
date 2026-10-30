---
title: "K2328 Structured local compiler for neutral phase readout"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: finite supplied-control compilation with error bounds; no hardware or GU feasibility
scripts:
  - tests/channel-swings/k2328_local_neutral_readout_compiler_probe.py
---

# K2328 Structured local compiler for neutral phase readout

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
result: K2328
carrier: two boson modes with hard total charge Q<=N and finite neutral qubit line LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert norm and ancilla-stable full-instrument trace distance ON=declared_carrier
real_structure: complex adjoint and programmed real Hamiltonian controls
grading: optical total charge and neutral binary record
action_owner: repository-construction -- retained Kerr plus supplied hopping, local dispersive coupling and nearest-neighbor neutral gates
target: coherent phase-to-neutral parking compiler with finite rates, loss and clock budget MAP-TYPE=evaluation
```

## Result and changed control assumption

[K2326](k2326-finite-neutral-readout-2026-10-30.md) constructed a neutral phase instrument using supplied multi-photon rank blocks. We replace those blocks by a structured finite compiler: coherently copy pilot number, then perform N descending threshold-controlled selective edge swaps. A parity echo makes the conditional hopping from ordinary hopping and a dispersive qubit coupling. Every neutral/dispersive pause is aligned to a full Kerr revival, so retained drift is accounted for. We give uniform operator errors, finite time and loss conditions; no arbitrary many-body logarithm implements the parking map.

The control alphabet is still supplied. Two addressed cavity modes occupy one optical node, connected by a controllable beam splitter. A movable neutral qubit adjacent to that node couples dispersively to either number operator. Neutral qubits lie on a line and have bounded-rate one-qubit and adjacent two-qubit gates. This is locality on the stated device interaction graph, not point-local continuum QED or a derivation of effective Kerr/dispersive controls. The node's two modes are colocated or directly linked; moving a cavity mode across a large device is not free. Reference loss, neutral noise, leakage and non-Markov effects are absent from the ideal model and require explicit error allowances if present.

Source SC-META-53 remains UNCERTAIN; source ACT01/GEO55/COS50/51/54 ASSERTS, ledger0.263 and native GU claims remain unchanged. Positive Hilbert controls are imported conventional apparatus, not GU quantization. No efficiency at enormous N, experiment, novelty or hardware feasibility is established.

## Supplied alphabet, reused components and drift

Set hbar=1, N>=1. The retained optical drift is H0=chi n_P(n_P-1)/2, chi!=0, on every Q<=N shell. Its norm is D0=|chi|N(N-1)/2 and its exact period divides Tchi=2pi/|chi| because n(n-1)/2 is integer. Available controls are

- complex beam-splitter coupling g(t)a_R^dagger a_P+conjugate, |g|<=g_BS;
- dispersive h(t)n_X tensor |1><1|_f, X=P or R, |h|<=g_d;
- arbitrary one-qubit and adjacent two-qubit gates generated at a supplied norm rate g_q>0, with neutral SWAP routing.

A desired neutral gate has a Hermitian logarithm of norm<=pi, so it takes at most pi/g_q before optional waiting. Only constant-size gates use this fact; no large many-body logarithm is smuggled in. To make every such gate exactly optical-identity, choose duration

    t_q=Tchi ceil[pi/(g_q Tchi)]

and lower its amplitude as needed. Neutral generators commute with H0. A dispersive controlled phase angle |alpha|<=pi is similarly implemented over t_d=Tchi ceil[pi/(g_d Tchi)]. The dispersive coefficient cap is g_d; its hard-shell Hamiltonian norm can be N g_d. These are finite integer-revival pauses, not free inverse Kerr evolution. End-point timing and phase precision remain costs.

Coherent phase estimation from [K2276](k2276-structured-detector-implementation-2026-10-29.md) copies n_P into a q-bit record B, initially0, where q=ceil(log2(N+2)) and d=2^q. It uses q dispersive controlled phases and a neutral inverse QFT; no optical-number measurement occurs. Kerr commutes with these pulses and each optical pause is a full revival. [K2287](k2287-finite-register-compensator-2026-10-30.md)'s arithmetic machinery is prior evidence, not a new result here. The original phase is retained coherently in sum_n c_n e^(-2in phi)|n,N-n>|n>_B. Correct known query/storage phases before this stage as in K2326; unknown extra phases are errors.

## Why passive conditional parking fails, and the N-stage repair

An n-conditioned passive beam splitter cannot in general rotate the interior Dicke state |n,N-n> into |0,N>: for0<n<N their one-particle reduced density eigenvalues differ, and passive SU(2) conjugation preserves those eigenvalues. For N=2,n=1 the initial eigenvalues are(1,1), whereas the desired state has(0,2). Merely recording n does not fix this optical orbit obstruction. Adding a third protected optical mode can swap phase elsewhere, but does not transfer it to neutral memory or return the original two-mode stock.

For k=N,N-1,...,1 compute f_k=[B>=k] coherently, use it to control the selected edge swap k->k-1, and uncompute the flag. The ideal edge Hamiltonian in the H0 interaction frame has downward coefficient +iJ and upward coefficient -iJ; time tau=pi/(2J) maps |k,N-k> to +|k-1,N-k+1>. It also maps the reverse state to its negative, which is why the threshold flag is essential.

Induction proves the complete map. Before stage k, every original branch n>=k has pilot occupation k and flag1; every n<k remains at pilot n with flag0. Thus the first group descends, the second stays. At the end all pilot occupations vanish and the unchanged orthogonal record keeps every amplitude:

    sum c_n e^(-2in phi)|n,N-n>|0>_B
       -> |0,N> sum c_n e^(-2in phi)|n>_B.            (1)

There are N stages, not sum_n n. The map is an isometry on the initial N-shell; on each lower Q=L<N shell define selected edge k<=L with amplitude J sqrt[k(L-k+1)]/sqrt[k(N-k+1)], zero for k>L, and retain the same threshold control. This is the actual resonant part of the supplied hopping, with norm<=J and unwanted-edge bounds inherited from the N-shell coefficients. No exact lower-shell parking is required. In the interaction frame every downward coefficient is chosen with positive transfer sign. Final parked states have H0=0, so the laboratory frame adds no terminal optical phase. Program the drive against the total coherent clock; integer-revival gaps leave its integer-multiple-chi carrier phase unchanged.

## Controlled hopping from a parity echo, with the real drift retained

For one bit f define C=exp[-i pi n_P |1><1|_f]. It is exactly identity on f0 and optical parity on f1, C²=I, CH0C=H0. If B is a fixed-phase beam-splitter Hamiltonian, CBC=-B on f1. Let b=||B||. The physical echo pair (rightmost acts first) is

    E_delta= exp[-i(H0+B)delta/2] C
             exp[-i(H0-B)delta/2] C.                 (2)

Each C is implemented over t_d and has no residual Kerr unitary. On f1, (2) equals exp[-i(H0+B)delta] exactly. On f0, the two opposite hops approximate exp[-iH0 delta]. The unitary Lie-product remainder is bounded by delta²||[H0+B,H0-B]||/8<=delta² D0 b/2. Thus (2) approximates exp[-i(H0+|1><1|B)delta] uniformly, including coherent flags and spectators. Omitting one C is not a valid echo.

For selected edge k let b_k=sqrt(k(N-k+1)), use coupling amplitude J/b_k and frequency omega_k=chi(k-1). With the alphabet's DOWNWARD coefficient g multiplying a_R^dagger a_P, program g(t)=+i(J/b_k)exp(+i omega_k t), frozen at each microstep start; its conjugate is the raising coefficient. The full hopping norm is at most b=NJ/b_k. Freezing the drive phase at a microstep's left endpoint adds at most |omega_k|b delta²/2. Contractive telescoping gives the conservative error per tau pulse

    epsilon_echo,k <= tau delta_k b (D0+|omega_k|).    (3)

All durations here are active hopping durations; the parity overhead is counted in physical time below. Revival gaps preserve the ideal interaction phase; phase noise and clock drift do not receive that exemption.

## Spectral selectivity, finite step count and physical time

[K2324](k2324-kerr-selective-lossy-control-2026-10-30.md)'s direct averaging theorem, specialized to zero loss, compares this driven Kerr hopping with the ideal selected edge on the WHOLE hard shell. Its error per edge is

    e_sel,k <= (4sqrt(2)J/|chi|)[1+tau(2J+NJ/b_k)].   (4)

Threshold control is a direct sum of this active block and identity in the interaction frame. Let Csel=4sqrt(2)(1+pi+pi²/2). Since sum_{k=1}^N1/sqrt(k(N-k+1))<=pi, summing (4) gives

    epsilon_sel <= Csel JN/|chi|.                    (5)

For the sum inequality pair k with N+1-k and compare each interior sample of1/sqrt(x(L-x)), L=N+1, with the centered unit interval integral: convexity makes that integral at least the sample. The union of centered intervals lies in(0,L), whose full integral is pi. N=1 is exactly selective, with no off-resonant edge, so (5) is an optional loose bound there.

For any requested epsilon_echo>0 take

    r_k=max(1,ceil[N tau² (NJ/b_k)(D0+|omega_k|)/epsilon_echo]),
    delta_k=tau/r_k.

Then the sum of (3) is <=epsilon_echo. A useful explicit bound is

    R=sum r_k <= N + pi³ |chi| N²(N-1)(N+2)/(8J epsilon_echo),
    T_park = Npi/(2J) + 2t_d R.                       (6)

For N=1, D0=omega1=0, r1=1 and echo error vanishes exactly. The amplitude requirement is J<=g_BS sqrt(N). Selection demands a sufficiently SMALL J/|chi|; fine echo accuracy increases revival overhead. These requirements compete with loss; a large gap alone is not evidence of feasibility.

The q-bit threshold comparator can be synthesized explicitly without a multi-controlled primitive. For each integer n in[k,N], XOR the equality [B=n] into a clean flag, using X gates for zero controls, a chain of Toffoli ANDs into q-1 clean work bits, a final toggle and uncomputation. The equalities are disjoint, so their XOR equals the threshold. Repeat the circuit after the optical pulse to clean the flag. Each Toffoli has an exact decomposition into at most15 one-/two-qubit gates. An equality uses at most2q zero-control X gates, 2(q-1) Toffolis and one final CNOT, hence at most32q primitive gates. Allocate at most6q+6 neutral sites including B, total-Q scratch, work/flags, copy environment and reset blanks. Routing one operand and restoring it costs at most12q+13 adjacent primitives per distant two-qubit gate, and at most12q+12 SWAPs per dispersive contact. The active flag is restored to the qubit adjacent to the optical node before every echo, so its repeated parity pulses require no additional routing. Thus all threshold computations and uncomputations cost at most

    G_cmp <= 32q(12q+13) N(N+1).

Here N(N+1) counts all equality operations including uncomputation. Four QFT/inverse-QFT circuits, three sets of q Hadamards, one final equality, q+1 copy gates (record plus acceptance flag) and q+1 reset SWAPs require at most4q²+41q+2 unrouted neutral gates. Initial pilot copy uses q dispersive phases, final Q=n_P+n_R copy uses2q and its uncomputation uses2q: the total is5q, not3q. A conservative upper bound absorbing these auxiliary gates and contact routing is

    G_neutral <= 1000 q²(q+2)(N+2)²,
    T_total <= T_query + T_park + 5q t_d + G_neutral t_q. (7)

Only retained B and acceptance flag are reset; scratch is uncomputed and copied environments are exported. Fresh blank supply and environment storage are external resources. Constants are intentionally loose, and no optimal gate count is claimed. Finite two-qubit decompositions are standard prior art, not a new universality claim; see [Barenco et al., Elementary gates for quantum computation](https://arxiv.org/abs/quant-ph/9503016).

Preparation is separate and adds its actual duration/error. All idle waits are included. Finite two-qubit decompositions are standard prior art, not a new universality claim; see [Barenco et al., Elementary gates for quantum computation](https://arxiv.org/abs/quant-ph/9503016).

## Full instrument, loss, clocks and reset

After ideal parking, copy total Q into a fresh binary scratch register by dispersive phases on P and R, compute flag[Q=N], then uncompute scratch. Apply F_d to B, copy its computational label and acceptance flag to a fresh environment and retain the classical record. Because d>=N+2, the Fourier circular-loss calculation of K2326 has no alias and gives exactly2[1-cos(pi/(N+2))] for its sine coefficients, for every phi. A record dimension N+1 would not suffice in general. Here the symbol d is record dimension; optical Q remains charge.

Unlike K2326's exact lossy rank blocks, this compiler is compared to an ideal LOSSLESS instrument. Approximate parking can leave pilot population, so it does not claim a perfect loss herald or exact no-jump pretilt. All failures/false acceptances stay inside the full-channel comparison. With hard Q<=N, Markov pilot loss gamma and Hamiltonian errors Delta H, ancilla-stable trace distance obeys

    epsilon_inst <= epsilon_input + epsilon_sel + epsilon_echo
                    + gamma N T_total + integral ||Delta H|| dt. (8)

This follows from unitary telescoping and Duhamel: half the induced trace norm of the dissipator is <=gamma N. Neutral recording and tracing contract distance. Reference loss gamma_R would add gamma_R N T_total; neutral dissipators, leakage and rate mismatch need their own bounds. The initial error is a full input error, not a conditional preparation angle from a different experiment. Query/sensing intervals and all revival waits contribute to T_total. For ideal N-shell input acceptance is1; actual acceptance is at least1-epsilon_inst. Event probabilities shift by at most epsilon_inst, and an observable bounded in[0,4] changes expected risk by at most4epsilon_inst. Conditioning on acceptance requires normalization and must not reuse this unconditional bound unchanged.

A sufficient formal resource window chooses positive epsilon_sel,epsilon_echo,epsilon_loss with total below the desired budget, imposes (5), J<=g_BS sqrt(N), constructs (6)-(7), then requires gamma<=epsilon_loss/(N T_total). The constants are supplied effective parameters. This demonstrates a nonempty mathematical region if loss can be arbitrarily small; it neither proves physical parameters independently tunable nor optimal survival. K2326's exact lossy pretilt gains have NOT been retained by this approximation theorem.

Clock errors are part of Delta H: a revival endpoint error costs at most D0|delta t|; carrier phase error costs at most b|delta phase| times its active duration. If phases derive from one clock, delta phase includes accumulated omega_k delta t, not only each local switch error. Dispersive number-phase errors scale with N. Reference protection and the fresh neutral zeros are supplied resources. Reset is nearest-neighbor SWAP to fresh zero qubits, transferring entropy to consumed memory; it is not autonomous cyclic erasure or free entropy disposal.

## Verification, hostile controls and next endpoint

The companion probe applies the actual finite joint optical/record threshold swaps to coherent columns, checks the passive orbit invariant, parity echo generators and exact phases, Fourier aliasing and uniform resource algebra. Genuine altered gates, threshold predicates and revival durations must fail the same evaluators; finite numeric echo controls are distinguished from exact algebra. Written averaging/product-formula/Duhamel arguments supply the all-N guarantee, not small-N simulation alone.

The next physical question is whether a particular microscopic cavity/qubit implementation provides the assumed chi,g_BS,g_d,g_q,loss and clock accuracy on this hard shell, especially after the large revival/routing overhead. A reduced-noise or faster selective primitive could improve (7); a compiled circuit alone is not viability at N near10^27. The native GU physical state/domain remains a separate missing construction.
