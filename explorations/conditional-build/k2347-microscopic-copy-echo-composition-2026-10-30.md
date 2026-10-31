---
title: "K2347 Microscopic coherent copy and echo on reachable support"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or empirical certification
scripts:
  - tests/channel-swings/k2347_microscopic_copy_echo_composition_probe.py
---

# K2347 Microscopic coherent copy and echo on reachable support

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
result: K2347
carrier: cavity reference mediator and neutral bit, ideal Q1 input and exact reachable32-state carrier LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product and restricted-input channel distance ON=declared_carrier
real_structure: real coefficients; complex Hilbert adjoint where stated
grading: excitation sectors; neutral rotations change total excitation
action_owner: repository-construction -- K2336 microscopic compiler with K2344 improved signed contacts
target: coherent three-contact transfer, support and error budget MAP-TYPE=evaluation
```

## Result, reuse and scope

[K2336](k2336-dispersive-contact-realization-2026-10-30.md) already supplies a microscopic copy/readout compiler. [K2344](k2344-signed-detuning-echo-repair-2026-10-30.md) strengthens the contact estimate by a second unitary elimination but tests an echo after ideal copy. Here that bound is composed through the actual copy and a complete coherent three-contact echo. Neutral rotations enlarge reachable support; ignoring this creates an unjustified cutoff. This is an improved conditional compiler and an executed finite isometry, not a first compiler, physical device or GU measurement derivation. SC-ACT-01/GEO-55 ASSERTS and META53 UNCERTAIN, ledger0.263 and native verdicts are unchanged.

## General contact composition

Use K2344's exact Hmic(Ds), matching compensator C, H0, L and Zf. For finite N, an ideal prefix has Q=a†a+aR†aR+Pe=N; each neutral contact input lies in K=Q+Pf<=M=N+1. Put

    rho=|h|sqrt(M)/D, q_sigma=|hg/[sigma D(sigma D−Delta)]|,
    r_sigma=b+q_sigma |hg/D|+2q_sigma(|g|sqrt(M)+h²M/D),
    E_sigma(t)=2(rho+q_sigma)+|t|r_sigma,
    b=2|h|sqrt(M)rho² exp(2rho)+rho|hg/D|+2rho h²/D.

Here sigma is +1 or−1. Require D>0,h!=0 and sigma D!=Delta. Contact error is K2344's operator bound on K<=M, including the physical neutral counterphase. A finite counterphase gate also evolves under H0, which commutes with Pf.

For q binary-copy bits, d=2^q>N and alpha_j=2pi2^j/d, the negative-detuning copy duration is t_j=alpha_j D/(2h²). There are q copy contacts and2N parking contacts, each parking duration t_e=pi D/(2h²). T_copy=pi D(1−1/d)/h². The improved total contact debt is

    sum_j E_-(t_j)+N[E_+(t_e)+E_-(t_e)].          (1)

At fixed finite N,Delta,g,h it is O(1/D), while total contact duration is proportional to D. Add the same selective-pulse, neutral-gate, preparation, switching, noise and clock debts as K2336. Do not send D to infinity at fixed nonzero noise and declare convergence of the full instrument.

This is a RESTRICTED-input telescope. For products U_j(actual), V_j(ideal), expand U_m...U_1−V_m...V_1 with actual unitary suffixes and ideal prefixes. Each local difference acts on the known ideal-prefix sector; actual leakage need not remain there. Tensoring spectator identities preserves the bound. Later readout/partial trace contracts trace distance, so an isometry operator bound also bounds half-diamond distance on that input subspace. Neutral gates do not preserve K. A proof using one globally invariant K<=N+1 across the entire actual sequence would be wrong.

## Executed N=1 coherent copy and echo

Freeze Delta=10,g=h=1,D=20001/2,J=10^-6,delta=1/100,N=1,q=1. R=sqrt(Delta²+4), c=sqrt[(1+Delta/R)/2], s1=sqrt[(1−Delta/R)/2], omega=(Delta−R)/2. Inputs are the coherent span

    u0=|p0,r1,e0,f0>,
    u1=c|p1,r0,e0,f0>−s1|p0,r0,e1,f0>.

Supply finite neutral primitives H_f (Hadamard) and S_f=diag(1,i). Their actual gates are G_H=exp(−iH0 delta)H_f and G_S=exp(−iH0 delta)S_f. Define t=pi D/2, tau=pi/(4J), and

    V_sigma=exp(−iH0 delta) exp(i sigma D t Pf)
            exp(−it Hmic(sigma D)).

The physical neutral counterphase is part of V, with duration delta. The hopping pulse at absolute start a and phase z is

    P_z(a)=exp[−i omega(a+tau)L]
           exp[−i tau(H0−omega L+(J/c)(z B+conj(z)B†))]
           exp[i omega a L], B=aR†a.

Chronological sequence:

    G_H, V_-, G_H, G_S, V_+, P_(-1)(2t+5delta),
    V_-, P_i(3t+6delta+tau).                         (2)

Total time T=3t+6delta+2tau. The ideal copy contact is exp(−i alpha LZf/2), alpha=pi; its copied n1 amplitude is−i and S_f removes it. The ideal selected echo then parks the n1 excitation with amplitude+1. With common absolute clocks both ideal outputs are |p0,r1,e0> tensor |f0> or |f1>, with common phase1. This is a coherent transfer target: a wrong relative phase fails even if flags are correct. The q=1 witness is not the q>=2 finite Fourier phase-risk formula of the larger compiler.

For exact reachable evolution use basis Q=p+r+e<=3 tensor f, dimension32. Inputs have Q=1. First H gives K<=2; copy preserves K. Second H raises support by at most one, to K<=3; all subsequent S, contacts and hopping preserve K. The artificial boundary K=4 of this finite matrix is unreachable. Thus full32 matrices represent the exact physical evolution of these columns. The probe checks the full two-column error, unitarity enclosures and vanishing impossible support, rather than an unrelated full32 operator target.

## Error and resource consumer

The contact telescope uses M=2 on ideal prefixes even though exact actual simulation uses32 states. For N=1, the only unwanted upper-dressed transition in the ideal-prefix Q<=1 carrier is separated by R, not the much smaller generic all-N lower-branch frequency spacing. The same integration-by-parts selective estimate gives

    e_sel <=16J/(R c)[1+(pi/4)(3+1/c)].            (3)

The upper matrix element is bounded by1 and the selected matrix element is c. This is a restricted-prefix proof, not a gap certificate for every leaked higher sector. K2332 supplies the general averaging argument; the probe checks the exact two transition frequencies. A sufficient whole-transfer budget is

    2E_-(t)+E_+(t)+e_sel+nu T+epsilon_input+epsilon_controls. (4)

The probe evaluates conservative rational bounds with sqrt2<99/70, R>10,c>99/100,pi<22/7 and nu=10^-10, epsilon_input=epsilon_controls=0. The resulting certificate is below1/100. The finite256-bit Arb matrix comparison is separately recorded; it does not prove the uniform theorem.

Finite neutral Hamiltonians can implement these primitives: H_H=pi(I−H_f)/(2delta), H_S=−pi Pf/(2delta), and H_phase=−wrap(sigma D t)Pf/delta. All have norm at most pi/delta (identity scalar kept for phase bookkeeping). They commute with H0. This consumes a supplied neutral-control bound at least pi/delta, not zero-time gates. Microscopic fast switching and a common norm-rate noise bound remain supplied. Any actual cavity/reference loss must be bounded on the complete reachable carrier: for this witness cavity+reference excitation is at most3, so a declared loss generator bound must price that support, not only ideal N=1. The explicit nu is not a measured loss rate or proof that all controls coexist on one device.

Omitting the copy phase, resetting a tone clock, omitting the copy contact or removing the compensator are tested against the unchanged coherent target. Four faulty circuits are explicitly evolved. The additional changed-carrier control is an analytic contradiction from the certified leaked weight, not a rerun of a projected circuit. Insufficient cutoff is demonstrated by a genuinely populated leaked state outside Q<=1, not by claiming every low-dimensional truncation must visibly fail a loose error threshold. Full-rate feasibility, switch dynamics and empirical control/noise inputs remain the next independent objects. No novelty, Lean, external-expert, hardware or native GU certification.
