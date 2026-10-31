---
title: "K2383 Optimal complete recovery during a transparent drive"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or measured physical verdict
scripts:
  - tests/channel-swings/k2383_driven_erasure_recovery_probe.py
---

# K2383 Optimal complete recovery during a transparent drive

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
result: K2383
carrier: four dual-rail pairs encoding one qubit and arbitrary untouched reference LAYER=toy CHIRALITY=N/A
pairing: positive finite Hilbert pairing and reference-aware diamond norm ON=declared_carrier
real_structure: complex amplitudes and real matched rail loss rates
grading: occupied and erased pair flags; unobserved loss time
action_owner: repository-construction -- independent Markov amplitude damping and K2362 physical transparent X/Z controls
target: complete driven channel and optimal final CPTP recovery MAP-TYPE=evaluation
```

## Complete result

[K2380](k2380-complete-erasure-recovery-2026-10-31.md) proves the complete idle recovery optimum. Here the same physical code and error-transparent controls are driven during loss. The final erasure flags are available; the loss times and emitted environment are not. We allow any final CPTP decoder with fresh input-independent ancillas, without pre-shared reference entanglement. This is an abstract optimal channel theorem, not a priced implementation of the new decoder.

Use outer bits |b> represented by the two rails |b,1-b> and

    V|b>=(|00bb>+|11,(1-b),(1-b)>)/sqrt2.
    H(t)=h(t) X_ET + g(t) Z_ET,
    X_ET=(5-N)(x0x1+x2x3)/2,
    Z_ET=(5-N)(z0+z1)(z2+z3)/4.

The rail operators x_i,z_i vanish on vacuum/double occupation and restrict to Pauli X,Z on each occupied pair. h,g and within-pair matched nonnegative loss rates k_i are bounded piecewise continuous. Their values are supplied, not measured. U'=-i(hX+gZ)U with U(0)=I is the intended logical evolution. K2362's identities on the code and all single-loss images imply exact zero/one-loss transparency.

Set eta_i(t)=exp(-integral_0^t k_i), w_S=product_(i in S)(1-eta_i(T)) product_(i notin S)eta_i(T), and P_j=sum_|S|=j w_S. For S={i,j} define

    omega_S(t)=product_(l notin S)eta_l(T)
       *[k_i(t)eta_i(t)(1-eta_j(t))
         +k_j(t)eta_j(t)(1-eta_i(t))].                (1)

This is the density of the second loss time conditional only on the final flag, BEFORE normalization. Its integral is w_S by differentiating (1-eta_i)(1-eta_j). Define P_S=X for same-group erasures {0,1} or{2,3}, and P_S=Z for the four split-group erasures. For w_S>0,

    U(t)^dagger P_S U(t)=n_S(t).sigma,
    v_S=(1/w_S) integral omega_S(t)n_S(t)dt,
    lambda_S=||v_S||<=1.                            (2)

Zero-weight flags contribute0 without defining lambda. The exact optimum reference-aware half-diamond error relative to U(T) is

    e_opt=sum_|S|=2 w_S(3-lambda_S)/4
                    +3(P3+P4)/4.                  (3)

## Why later physical controls do not hide another history term

Before the second loss, transparency keeps the same logical U(t) on all surviving histories, with scalar no-jump attenuation because rates match within each pair. Sum the erased-bit labels at that second loss. The physical partial-trace map is K2380's two-erasure channel applied to U(t)rho U(t)^dagger.

With a same-group loss, the two survivors carry W D_X(rho) W^dagger, W|b>=|bb>; the actual remaining Hamiltonian is(3h/2)XX and its Z term vanishes. XX commutes with that entire branch density. With split losses the survivor density is[I+r_z ZZ]/4; X_ET vanishes and H=(3g/4)ZZ also commutes. These statements hold linearly for every matrix unit, not only basis populations. Thus postsecond control changes neither branch, even for time-dependent noncommuting h/g schedules.

K2380's extraction CX gives exactly

    Phi_S(rho)=1/2[I+(v_S.r)P_S].                   (4)

The remaining spectator is input-independent after extraction. Each unextracted surviving single-pair marginal is I/2, so a third loss makes the whole retained channel constant. N<=1 controls vanish. In particular no additional time register survives beyond the binary channel(4); its statistics can still depend on time. The probe reconstructs the physical N2 restrictions from the supplied full formulas and checks all six masks on all four logical matrix units, including every third-loss marginal.

## Sharp optimum over all final decoders

Work in the frame undoing U(T). For lambda>0 set n=v/lambda. Map the two P eigenstates in(4) to pure output states with Bloch vectors ±n. This gives

    Psi_S=lambda D_n+(1-lambda)Depol,
    D_n(rho)=(rho+(n.sigma)rho(n.sigma))/2.           (5)

For lambda=0 choose the completely mixed output. Any decoder restricted to the classical binary input(4) prepares two states with Bloch vectors a_+,a_-, each norm<=1. Its Bell overlap is

    1/4+(a_+-a_-).v/8 <= (1+lambda)/4.

The decoder(5) attains this. Three/four-loss flags have Bell overlap1/4, zero/one-loss flags at most1. The Bell-versus-complement measurement therefore lower-bounds complete half-diamond error by(3).

Conversely(5) is a convex mixture of identity, traceless-unitary conjugation, and depolarization. Express depolarization as the four-Pauli average. Every nonidentity unitary here is traceless, hence maps a Bell state to the orthogonal Bell complement, even when different axes yield nonorthogonal states within that complement. Triangle inequality bounds complete half-diamond error by the nonidentity weight; the Bell input attains it. This proves(3), with arbitrary reference. The standard channel/diamond framework is in [Watrous's text](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf); the supplied-code calculation is given here without a novelty claim.

## Strict drive penalty and the information in a time record

Subtract the idle value:

    e_opt-e_idle=(1/4)sum_|S|=2 w_S(1-lambda_S).      (6)

If every k_i(t)>0 almost everywhere on the full experiment interval(0,T), omega_S(t)>0 almost everywhere for t>0. Equality in the norm bound for an average of unit vectors holds iff its vector is constant almost everywhere. The derivative norm of U^dagger XU is2|g|; that of U^dagger ZU is2|h|. Consequently the complete idle optimum survives exactly when h=g=0 almost everywhere under these rate assumptions. Genuine drive gives a strictly positive penalty, not necessarily a large one. Zero-rate windows, endpoint impulses and time-resolved recovery change these premises.

A useful physical counterconstruction follows: if only an exact second-loss time (alongside the original final flag, with no rail/bit label or coherent environment) is additionally recorded, its axis n(t) is known and has norm1. A time-conditioned decoder restores the idle branch bound for every time, so its complete optimum is e_idle. This does not restore quantum information lost in two erasures; it removes the extra uncertainty from the averaging in(2). Such a time record is additional apparatus/environment access, absent in(3), with independent measurement and timing costs. For bins B, put w_SB=integral_B omega_S and v_SB=integral_B omega_S n_S/w_SB, omitting empty bins. A coarse time-bin record replaces w_S lambda_S by sum_B w_SB ||v_SB|| in(3). Refining bins cannot worsen the optimum by the triangle inequality; this directly quantifies the value of timing information without claiming a free detector.

## Explicit noncommuting schedule with identity endpoint

Take T=2, k_i=log2, h=pi,g=0 on[0,1], then h=0,g=pi on[1,2]. The generators do not commute, yet each pulse is -I and U(2)=I. This bounded piecewise-constant fixture has supplied instantaneous switching and makes no finite-slew claim.

Let k=log2, Omega=2pi, D=(k-iOmega)(2k-iOmega), and

    C1=8k(k+iOmega)/(9D),
    C2=2k(5k-iOmega)/(9D).
    lambda_X=|4/9+C2|, lambda_Z=|5/9+C1|.           (7)

The normalized second-loss density is(32k/9)(exp(-kt)-exp(-2kt)). Its masses on the two intervals are4/9 and5/9; integrating its complex oscillating factors gives C1,C2 exactly. The probe derives these endpoint integrals independently from the exponential antiderivative. Every two-loss flag has w=9/256 and P3+P4=189/256, so

    e_opt=(729-18lambda_X-36lambda_Z)/1024
           >675/1024=e_idle.                       (8)

Strictness follows analytically from nonconstant axes; emitted decimals illustrate it and are not its proof. Im C2=2kOmega(13k²+Omega²)/[9(k²+Omega²)(4k²+Omega²)]>0. The unchanged idle decoder reads the final X axis, whereas v_X has a nonzero transverse component. It is therefore strictly suboptimal despite U(2)=I. Endpoint-only equivalence cannot determine complete recovery.

## Costs, robustness and next physical condition

Do NOT inherit K2380's21-gate recovery budget: the optimal axes in(5) require new flag-dependent rotations, and U(T) must be restored in the decoded output. One must price those controls, their errors, preparation and readout. Formula(3) is the loss-channel contribution before those debts.

For mismatched actual rails, fix a matched reference, the same H(t), and one decoder before applying [K2377](k2377-time-ordered-rate-robustness-2026-10-31.md). Contractivity gives e_actual<=min(1,e_reference+min(sqrt(Qrate),D1)), then add nonoverlapping complete instrument costs. This is a sufficient same-decoder bound, not the unequal-rail optimum. If axis synthesis is approximate, its independently bounded channel error adds by triangle inequality; it cannot be silently absorbed into e_opt.

SC-META-53 remains UNCERTAIN and LT-GR6b remains open. The result does not build GU's source-owned physical quotient or demonstrate measured hardware. Internal specialist review and exact finite probes are not external-expert, proof-assistant or apparatus certification. Next construct and price the optimal-axis decoder or supply actual matched/mismatched rate and time-record capabilities for the same device.
