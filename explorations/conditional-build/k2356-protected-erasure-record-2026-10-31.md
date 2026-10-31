---
title: "K2356 A finite coherent erasure-protected final record"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional coherent-record construction; no hardware or GU certification
scripts:
  - tests/channel-swings/k2356_protected_erasure_record_probe.py
---

# K2356 A finite coherent erasure-protected final record

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
result: K2356
carrier: one logical qubit encoded in eight neutral qubits with flagged amplitude damping LAYER=toy CHIRALITY=N/A
pairing: trace norm and half-diamond channel distance ON=declared_carrier
real_structure: real parameters and explicitly named complex quantum Hilbert space
grading: logical qubit versus rail excitation and erasure flag
action_owner: repository-construction -- supplied neutral Pauli drives and two-neutral controlled couplings
target: coherent recovery, finite resource budget and remaining loss floor MAP-TYPE=evaluation
```

## Result and backward demand

[K2353](k2353-late-record-relaxation-2026-10-31.md) proves a floor p=1-exp(-kappa T) for its immediate physical-f readout. This construction changes that named architecture: encode f into eight neutral qubits, leave them untouched during the final hop, detect rail erasures and coherently recover. It protects a logical qubit entangled with the rest of the apparatus, not just a classical flag. Under equal independent amplitude damping on all rails, the recovered late-memory channel has half-diamond error at most

    B(p)=6p²-8p³+3p⁴.

The proof includes the actual encoder, recovery, finite cap/slew durations, noisy-gate debt and a residual common-erasure lower bound. This is a supplied positive-Hilbert apparatus construction, not GU physical-state recovery; SC-META-53 remains UNCERTAIN and LT-SM8/GR6b remain unchanged. It does not evade early pre-copy information destruction. The primitive alphabet is ENLARGED: it supplies two-neutral controlled coupling absent from the previous JC compiler, and does not claim that old controls already implement it.

## Exact inner channel and outer code

Encode each abstract bit q as |q,1-q> in two physical neutral rails. For equal independent amplitude damping with survival eta=1-p on each rail, restriction to this one-excitation subspace gives the erasure channel

    E(rho)=eta DR(rho)+p |00><00| Tr(rho).

The no-jump operator is sqrt(eta) times the identity on the code; the two jump operators replace the state by vacuum with the correct traced-out environment. This identity holds when tensoring an arbitrary reference. It does not say an erased qubit's entanglement survives locally.

Use the four-qubit code

    V|b> = (1/sqrt2) sum_(r=0,1) |r,r,r xor b,r xor b>.

For every erased abstract position j, tracing the other three positions in V|b><c|V† gives delta_bc I_j/2. Equivalently the two erasure Kraus maps A_js=<s|_j V obey A_js† A_jt=delta_st I_logical/2. This is the complete single-known-erasure correction condition, including off-diagonal logical matrix units. It follows directly from the displayed two codewords; no external code theorem is needed as a black box.

The four independent rail pairs produce orthogonal flags for erased subsets S, with probabilities p^|S| eta^(4-|S|), independent of the logical state. Recover |S|=0 or1 exactly. For |S|>=2 use any trace-preserving fallback, such as retaining output physical f and discarding other records. The resulting channel is (1-B)Id+B F for a channel F, hence half-diamond error<=B. This is an upper bound, not an equality or proof that every two-erasure pattern is uncorrectable.

## Explicit finite encoder and recovery

Number abstract qubits q1..q4, with original f=q3 and all other seven physical qubits initially0. Apply H1, CX1,2, CX1,3, CX3,4. Then for each i apply X to its partner rail r_i and CX(q_i,r_i). This is12 elementary gates and yields the displayed code followed by dual rails.

At recovery, prepare four syndrome ancillas0. Two CNOTs from each rail pair into its ancilla record parity; one-excitation code gives1, erased vacuum gives0. Measure those four ancillas. This measurement distinguishes orthogonal erasure sectors and does not measure the surviving logical information. Decode each surviving rail with CX(q_i,r_i) then X(r_i), at most8 gates. When one abstract position j is erased, its original pair partner is a singleton s and the opposite pair has two copies s xor b. Apply CX(singleton,first opposite), then CX(first opposite,second opposite). The first opposite becomes b and the remaining two bits are s,s; discard them. If output is q1, SWAP(q1,q3) costs3 CNOTs to return to f. When none is erased, CX1,3 and CX3,4 factor b in q3 from the GHZ syndrome on1,2,4. Each branch is coherent on b and reference-independent. With two or more erasures the explicitly chosen fallback needs no additional gates.

Thus recovery needs at most8 parity CNOTs+8 rail-decoding gates+2 outer-decoding gates+3 routing gates=21 gates, and4 syndrome measurements. Missing/erased rails are skipped based on the observed flag. Pad shorter good branches with idle time if a fixed duration is required; price the entire worst-case duration below. Ancilla preparation, readout duration/error and feedback latency are additional resources, not free consequences of code distance.

## Control alphabet and finite rates

Supply H_U(t)=h(t) U for Hermitian involutions U=X, H=(X+Z)/sqrt2, or CX=[I+Z_c+X_t-Z_c X_t]/2. Then integral h dt=pi/2 implements -iU, an irrelevant global phase. The two-body Z_c X_t term is explicit. Neutral free evolution is zero in this declared rotating frame or compensated with a proven tracked phase. With |h|<=G and |h'|<=V, a nonnegative symmetric triangle/trapezoid has shortest duration within this fixed-involution scalar-envelope class

    t_g=2sqrt[pi/(2V)]                   if G>=sqrt(pi V/2),
    t_g=pi/(2G)+G/V                     otherwise.

Minimality follows from h(t)<=min(G,Vt,V(T-t)) for a pulse that starts and ends at zero; integrate this pointwise bound. This is not a universal gate speed limit. The first formula equates triangle area to pi/2; the second uses ramps of duration G/V and plateau area remaining. No unpriced discontinuous pulse is used. Let T_enc=12t_g and T_rec=21t_g+4t_m+t_feedback, with additional prep/reset duration added if nonzero. Four simultaneous measurements may be faster, but the conservative budget serializes them.

The old subsystem excitation Q<=3 is retained; old K<=3 is NOT retained. Use full neutral Hilbert space of8 qubits during encoding/idle and12 including syndrome ancillas during recovery. If each physical neutral qubit has Markov damping rate bounded by kappa_g throughout the added encoding/recovery intervals, including measurement, feedback and padding, its rate operator is bounded by8kappa_g or12kappa_g. The Duhamel half-diamond debt is therefore at most

    E_total <= epsilon_pre + B(p)
               +(3gamma+8kappa_g)T_enc
               +(3gamma+12kappa_g)T_rec
               +epsilon_prep+epsilon_measure+epsilon_control.

Here epsilon_prep is the trace-distance error of the joint prepared ancilla state; epsilon_measure and epsilon_control are ancilla-stable half-diamond errors of the complete implemented instruments/channels, including feedforward, rather than per-bit misclassification probabilities. Here epsilon_pre includes all unchanged earlier errors and the final subsystem hop's own imperfection/loss, while the two3gamma terms price only the added encoding/recovery time. The late neutral idle AD is handled exactly by B and must not also be counted as a bare kappa T error. The code/recovery identities tensor with that subsystem. Insert encoding before the final hop and shift its absolute tone clock by T_enc; any free subsystem evolution during added time must be included in the ideal clock/frame or compensated, not silently dropped.

An explicit incremental witness: p=1/10, G=V=1 gives t_g=pi/2+1, t_m=1, feedback0, gamma0, kappa_g=10^-6. With ideal initial ancillas and stipulated exact measurement/control, B=523/10000. Gate/recovery damping debt is (348t_g+48)/10^6, so total incremental debt<0.053243 using pi<22/7, below the bare late floor0.1. This does not constrain epsilon_pre and does not certify a complete hardware instrument. The same idle kappa=10^-6 can give p=.1 at T=10^6 log(10/9), so the witness need not turn damping off during gates. Real correlations, primitive availability, measurement/reset and same-device rates remain unmeasured. The code improves the bound B<p only for 0<p<(5-sqrt13)/6; large loss is not repaired by this finite code.

## Follow-through: unequal pairs and bounded mismatch

Different pairs may have different survival eta_i as long as the two rails within each pair match. Exact flagged erasure and the same recovery then give

    B=1-product_i eta_i-sum_i[(1-eta_i) product_(j!=i) eta_j].

Thus global equality of all eight rates is unnecessary. If actual rail rates differ from matched reference pair rates by delta_kappa_(i,a), the finite-carrier Duhamel bound adds at most T_idle sum_(i,a)|delta_kappa_(i,a)| to the half-diamond budget. This is a conservative robustness certificate; it follows by summing differences of the single-qubit damping generators, each with half-diamond norm at most the absolute rate difference, then using CPTP contraction. It prices small within-pair mismatches rather than calling exact matching experimentally free. Large mismatch may defeat the bound without proving hardware impossibility.

The record stores exactly four rail excitations before loss. If each rail has laboratory gap hbar omega, that stored excitation energy is4hbar omega; drive work, readout and reset costs are not derived from the rotating-frame norm cap. No energy-efficiency claim follows.

## Necessary limits and genuine countercontrols

All four rail pairs erase with probability p^4, leaving identical vacuum for both logical inputs. For a recovery acting only on the record with fresh input-independent ancillas, trace-distance contraction implies distinguishability<=1-p^4; approximating both orthogonal logical outputs therefore requires worst input error>=p^4/2. A correlated common reset with probability q similarly gives floor q/2 regardless of this redundancy. Side information in the subsystem/environment would change the theorem's premises.

Unequal survival rates within a rail pair yield a diagonal, nonscalar no-jump map, and state-dependent erasure probabilities: the state-independent binomial proof no longer applies. A physical Z on the q3 rail induces logical Z under the no-erasure decoder, changing |+> to |-> while leaving computational flags unchanged. Thus success on basis flags alone cannot certify coherent protection. Heating can create11 and breaks the vacuum/one-excitation flag model. Repetition with OR decoding gives classical error p^m but attenuates the logical off-diagonal by eta^(m/2); it is not the original coherent target.

## Evidence and next condition

The probe verifies encoder columns, all single-erasure matrix units, actual conditional recovery maps, parity extraction on the good sectors, exact dual-rail Kraus identity, failure probability and finite-rate arithmetic. These finite exact computations accompany universal channel proofs above. No external-expert, hardware, empirical or native GU certification is implied. Next is a priced implementation of the new neutral two-body primitive and measured correlated/unequal-rail noise, or a full instrument composition including nonzero preparation/measurement error. Another claim that abstract repetition fixes the original coherent problem is ruled out by the retained countercontrol.
