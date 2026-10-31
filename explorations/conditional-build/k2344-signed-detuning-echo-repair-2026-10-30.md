---
title: "K2344 Phase-sensitive signed-detuning echo repair"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or empirical certification
scripts:
  - tests/channel-swings/k2344_signed_detuning_echo_repair_probe.py
---

# K2344 Phase-sensitive signed-detuning echo repair

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
result: K2344
carrier: complete cavity reference mediator neutral direct sum total excitation K<=M, finite M LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert operator norm and entangled-spectator channel error ON=declared_carrier
real_structure: real coefficients or complex adjoint as explicitly stated
grading: conserved excitation, all sectors including vacuum retained
action_owner: repository-construction -- same matched microscopic contact as K2336 and full K2341 echo after ideal copy
target: uniform two-step elimination and coherent full-carrier finite certificate MAP-TYPE=evaluation
```

## Result and scope

[K2341](k2341-reachable-microscopic-echo-2026-10-30.md) certifies failure at the signed-contact resonance Delta=D. Here holding Delta,g,h fixed while increasing BOTH signed neutral detunings gives a phase-sensitive repair at the actual contact duration t=pi|D|/(2h²). A second unitary elimination removes the leading mediator-neutral exchange omitted by the crude first-step bound. The complete operator error is O(1/|D|), including coherent relative phases and all finite conserved sectors. No truncation to only the flag-one sector is allowed.

This repairs the supplied microscopic echo AFTER IDEAL number copy. It does not implement microscopic number copy, authenticate a hardware rate set, remove loss, or certify the full recorded instrument. Source SC-ACT-01/GEO-55 ASSERTS and META53 UNCERTAIN, ledger0.263 and native verdicts remain unchanged. Effective-unitary elimination is established machinery; see [Bravyi, DiVincenzo and Loss](https://arxiv.org/abs/1105.0675). The new contribution is the explicit second cancellation, signed long-time bound and complete echo consumer on this declared model.

## Complete carrier and first transformation

Assume a finite integer M>=1, real Delta,g,h with h!=0, and signed Ds!=0,Delta. Let K=a†a+aR†aR+Pe+Pf<=M, L=a†a+Pe, Zf=1−2Pf, and

    H0=Delta Pe+g(a e+ +a† e−), C=Pe Zf+Pf,
    Hmic=Ds Pf+H0+h(a f+ +a† f−)−h² C/Ds,
    chi=−h²/Ds, Hd=Ds Pf+H0+chi LZf.

All operators preserve K; finite-dimensional norm bounds therefore include every contact intermediate and all coherent superpositions of the sectors. Define A=a f+, S=(h/Ds)(A−A†), X=h(A+A†). Then [S,DsPf]=−X and [S,X]/2=(h²/Ds)((a†a+1)Pf−a†a(1−Pf)). Adding−h²C/Ds leaves chi LZf EXACTLY. Moreover [S,H0]=K1=(hg/Ds)(f+e−+f−e+). The signs and complete-carrier identities are checked for both Ds signs.

Put s=|h|sqrt(M)/|Ds|, v=|h|sqrt(M), k=|hg/Ds| and c=h²/|Ds|. Then

    e^S Hmic e^-S=Hd+K1+R1,
    ||R1|| <= b=2 v s² exp(2s)+s k+2s c.             (1)

For the fast block DsPf+X, combining [S,DsPf]=−X leaves X-series coefficients j/(j+1)!; its terms j>=2 are bounded by2vs² exp(2s). For H0 the integral remainder after [S,H0] is at most ||[S,K1]||/2<=s k, using unitary conjugation. The compensator change is at most2s c since ||C||=1. These bounds do not assume H0 small in norm or drop the growing duration.

## Second cancellation and contact/echo estimate

For Ds!=Delta define

    T=hg/[Ds(Ds−Delta)] (f+e−−f−e+),
    q=|hg/[Ds(Ds−Delta)]|, a0=|g|sqrt(M)+cM.

Directly [T,DsPf+DeltaPe]=−K1. Conjugate the sum of that diagonal block and K1 together. An integral remainder bounds what remains by ||[T,K1]||/2<=q k. Conjugating g(a e+ +a†e−)+chi LZf changes it by at most2q a0; conjugating R1 leaves its norm unchanged. Thus

    ||e^T e^S Hmic e^-S e^-T−Hd||<=r2=b+q k+2q a0.  (2)

Since S,T are anti-Hermitian, ||e^T e^S−I||<=s+q. Duhamel and the two endpoints give

    E(Ds,t)=2(s+q)+|t|r2,
    ||exp(i Ds t Pf) exp(−itHmic)
          −exp[−it(H0+chi LZf)]||<=E(Ds,t).          (3)

Here [H0+chi LZf,Pf]=0, so the physical neutral phase cancels exactly in the ideal comparison. It is a real control resource, not a discarded global phase. At fixed Delta,g,h,M and t=pi|Ds|/(2h²), (3) is O(1/|Ds|); at Ds=Delta the second transformation is undefined and supplies no rescue.

The two-half echo retains K2341's physical hopping pulses, lower-dressed frequencies, both signs, all upper branches and common absolute clocks. Its difference from the SAME echo with exact ideal contacts is bounded by E(+D,td)+E(−D,td), because the intervening pulses are unitaries. Finite phase-gate drift exp(−iH0 delta) preserves this telescope when used in both circuits and all later clocks advance by delta. This operator estimate preserves arbitrary copied-label spectators and coherent n=0/n=1 phases; flag leakage alone would not prove it.

## Executed finite consumer and resource cost

Take M=2, Delta=10, g=h=1, D=20001/2, J=10^-6 and phase duration delta=1/100. The probe retains the full13-dimensional direct sum K=0,1,2. It computes both complete echo matrices with256-bit Arb complex balls and their Frobenius difference, an upper bound for the operator difference. It also verifies the encoded ideal-prefix n=0/n=1 columns with their common phase. The exact rational certificate uses sqrt2<99/70, pi<22/7, D>=10000 and exp(2s)<1001/1000 (via exp(x)<=1/(1−x) for0<=x<1); it gives summed contact error<1/200. Matrix results are recorded separately; no finite sample proves the universal theorem.

Finite phase durations and signed contacts are included; fast switching remains ideal. The total active duration is2td+2tau+2delta, tau=pi/(4J). If additional dynamics admit a half-diamond generator error rate nu throughout, a telescoped noise allowance is nu times that duration. The probe checks a conservative duration bound with nu=10^-10 and combines it with(3) below1/100. This is a supplied norm-rate budget, not a measured Lindblad rate or a jointly feasible device. For fixed nonzero loss, sending D to infinity increases duration and may worsen total error; the mathematical detuning limit alone is not a physical limit.

Actual Hamiltonian faults remove or reverse the matched compensator, omit the first physical neutral counterphase, or return Delta to resonance. They are compared to the same fixed ideal target rather than changing the acceptance threshold. Noninteger D ensures single-counterphase omission is observable. Omitting both opposite phases can cancel in the ideal echo and is not claimed to fail this whole-echo check. Universal operator control and exact commutators are distinct from the finite interval witness.

## Consequence

The reachable failure is not universal across signed detunings: the same model admits a rigorously priced, phase-sensitive off-resonant repair. This does not transfer to Delta=D, arbitrary unknown cutoffs, a microscopic number-copy implementation or measured hardware. Next compare a jointly attainable control/noise/clock family and implement the copy prefix, keeping these coherent error and duration bounds. Repeating ratio-only or flag-only evidence cannot fill those gaps.
