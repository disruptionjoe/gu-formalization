---
title: "K2359 Loss during neutral gates and transparent repair"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or hardware certification
scripts:
  - tests/channel-swings/k2359_loss_during_neutral_control_probe.py
---

# K2359 Loss during neutral gates and transparent repair

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
result: K2359
carrier: positive-Hilbert eight neutral qubits in four dual rails LAYER=toy CHIRALITY=N/A
pairing: Hilbert trace and reference-aware trace distance ON=declared_carrier
real_structure: complex Hilbert amplitudes and real Hermitian-control coefficients
grading: physical rail occupations, outer-code bits and logical qubit remain distinct
action_owner: repository-construction -- supplied exchange, local Z and cross-rail ZZ; distinct sector-conditioned repair
target: unknown-time error correction and explicit repair MAP-TYPE=evaluation
```

## Result and scope

The supplied neutral dual-rail apparatus admits encoded single-qubit rotations and entangling phases through exchange, local Z and two-body ZZ controls. However, excitation preservation does not make loss during a gate equivalent to idle erasure. An explicit gate on K2356's code has a continuum of unknown-loss-time errors that no fixed recovery exactly corrects. A sector-conditioned Hamiltonian extension repairs this logical Z gate algebraically, with a separate control-availability requirement. These are conditional apparatus results, not a source-native GU state, measured hardware performance or a complete fault-tolerant universal computer.

[K2356](k2356-protected-erasure-record-2026-10-31.md) already priced noisy control separately from its idle-memory erasure theorem. The present counterexample constrains an attempted stronger composition; it does not retract K2356. SC-META-53 remains UNCERTAIN and LT-SM8's physical-state/domain requirements remain unchanged. Neutral couplings are supplied additions, not derived from the earlier JC alphabet.

## Real encoded primitives and preparation boundary

For one pair encode |b> as |b,1-b>. Xbar=(XqXr+YqYr)/2 restricts to X; Zq restricts to Z; Zq_i Zq_j restricts to encoded ZiZj. Each preserves the pair excitation count. Xbar and Zq give arbitrary encoded rotations, and their composition with ZZ supplies the usual encoded controlled phase and CNOT (with local phases and Hadamard). Hbar=(Xbar+Zq)/sqrt2 has full operator norm1 and restricts to Hadamard; it is not an involution on vacuum sectors. No claim about vacuum-sector phases is inferred from its encoded restriction.

This conservation begins AFTER preparation. The four-pair code has exactly four excitations. Number-preserving controls cannot create it from an unknown single physical input and seven vacuum qubits. Excitation injection, input-to-dual-rail mapping and initialization retain separate energy, noise and timing costs. The theorem below assumes a supplied encoded codeword and tests a logical operation on it.

## Exact gate-loss counterexample

Use the four-qubit outer code

    V|b>=(|00bb>+|11,(1 xor b),(1 xor b)>)/sqrt2,

with each outer qubit represented by its dual rail. Physical H(t)=g(t)Zq1 Zq3 restricts to g(t)Z_L on the code. Let theta=integral_0^T g and phi=integral_0^tau g. Condition on exactly one loss, in pair1, at time tau. Write A_s=<s|_1 V for its two possible lost-rail components; A_s†A_s=I/2 and their surviving syndrome images are orthogonal.

After loss q1 is vacuum, so its physical Z is+1. Zq3 on A_s acts as(-1)^s Z_L. Apart from nonzero scalar damping weights the actual jump-history operators are

    E_s(phi)=A_s U_[phi+(-1)^s(theta-phi)], U_a=exp(-iaZ_L).

This follows by multiplying the pre-jump and post-jump propagators, not by inserting a phase error after the ideal gate. Equal rail damping makes no-jump attenuation scalar on each fixed excitation sector. Its time dependence can weight histories but cannot remove the following nonscalar cross-time operator:

    E_1(phi)†E_1(psi)=1/2 exp[2i(phi-psi)Z_L].

The Knill-Laflamme condition for exact correction of the history family requires every such operator to be scalar on the logical code. It fails at generic distinct times. Constant positive damping has positive density over a whole time interval, so this is not a zero-probability endpoint objection. Retaining the surviving syndrome does not restore the missing jump phase. The conclusion is exact-correction failure for this alphabet/history family; approximate correction and changed controls remain possible.

K2356's ordinary end-only recovery yields, for a fixed loss time,

    1/2 U_theta rho U_theta† +1/2 U_(2phi-theta) rho U_(2phi-theta)†.

At theta=pi/4,phi=pi/8 and logical |+>, its trace distance from the ideal output is sqrt2/4. Thus even a SINGLE flagged pair loss can cause logical error during this gate. The idle probability of at least two erasures cannot alone bound the full gate channel. Damping/no-jump weights, earlier preparation and readout debts remain part of a complete instrument bound.

## Constructive follow-through: transparent logical Z

A sufficient condition for correction through a gate is H_surv(t)A_s=A_s H_L(t)+c_s(t)A_s, or a syndrome-only mixing generalization. Then propagation commutes through each correctable loss up to factors that carry no logical information.

Construct an explicit full-sector extension. Label each dual pair by0,1 orE(vacuum). Let P_empty project onto four occupied pairs, and P_j onto exactly pairj erased with all others occupied. In each zero/one-erased sector choose i to be a surviving member of{1,2}, k a surviving member of{3,4}. Define

    H_ET(t)=g(t) sum_{j in {empty,1,2,3,4}} P_j Zq_i(j) Zq_k(j),

and let it vanish on other sectors, including doubly occupied invalid pairs. The projectors commute and have orthogonal ranges; hence ||H_ET||=|g|. Every code or one-loss code image has Zi Zk=(-1)^b, independent of the random r. Therefore H_ET V=gVZ_L and H_ET A_js=gA_js Z_L for all four possible loss positions and both rails. All zero/one-loss histories implement the same logical rotation and ordinary erasure recovery removes their syndrome. This extends to a reference by linearity on logical matrix units.

This is a real algebraic repair, but its occupation-projector-conditioned many-body controls are an added primitive. Merely decomposing its ideal endpoint into two-body gates does not establish transparent DURING-gate evolution. No claim that the old ZZ alphabet realizes this continuous extension is made. The repair is for logical Z; a complete transparent universal gate set, preparation and syndrome readout remain separate constructions.

For a pulse starting and ending at zero, with cap|g|<=G and slew|g'|<=V, a nonnegative area theta>=G²/V has a trapezoid of duration theta/G+G/V; otherwise a triangle has duration2sqrt(theta/V). Orthogonal-sector norm1 permits the same elementary norm/slew accounting for the new primitive if it actually exists. It does not price synthesizing its projectors. For ideal transparent controls and independent matched pair damping, the storage-style zero/one-erasure argument again applies during this particular gate; arbitrary correlated loss, phase noise and imperfect control still require separate bounds.

An alternative repair resolves the jump phase and surviving syndrome. Feedforward U_[theta-a_s(phi)] restores the target. If the phase estimate has error at most epsilon, the s=1 branch differs by a Z angle at most2epsilon, giving reference-aware half-diamond distance at most2epsilon (capped at1); known-time recovery is a changed-information premise. End-only parity flags, or correction merely between gates, do not supply it.

## Verification

The companion probe reconstructs physical exchange and ZZ restrictions, the code maps, actual jump propagators, nonscalar cross-time products, midpoint output error, timestamp repair and all zero/one-loss images of the ternary-sector extension. Changed controls remove sector conditioning, ignore gate propagation, or assume number injection without preparation. Universal history and channel implications follow the written arguments, not numerical sampling. The known erasure-code background is [Grassl, Beth and Pellizzari](https://arxiv.org/abs/quant-ph/9610042). No novelty, external-expert or hardware certificate is asserted.
