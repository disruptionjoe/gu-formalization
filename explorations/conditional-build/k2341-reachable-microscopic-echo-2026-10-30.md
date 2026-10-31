---
title: "K2341 Reachable microscopic two-half echo resonance"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU, empirical or whole-instrument acceptance
scripts:
  - tests/channel-swings/k2341_reachable_microscopic_echo_probe.py
---

# K2341 Reachable microscopic two-half echo resonance

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
result: K2341
carrier: full fixed total excitation2 cavity/reference/mediator/neutral Hilbert sector LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert norm and trace-distance event lower bound ON=declared_carrier
real_structure: complex adjoint and real parameters
grading: total excitation p+r+e+f=2, all eight states retained
action_owner: repository-construction -- K2334 two-half echo with K2336 microscopic matched contacts and ideal copied input
target: rigorous finite reachable-input echo failure MAP-TYPE=evaluation
```

## Scope and concrete question

[K2338](k2338-resonant-contact-resource-boundary-2026-10-30.md) excludes ratio-only contact certification on a contact-domain input, without claiming that input reaches the correlated echo. Here a valid N=1 lower-dressed state AFTER IDEAL coherent number copy and threshold computation enters the complete two-half echo of [K2334](k2334-microscopic-neutral-transfer-2026-10-30.md). Both microscopic contacts, both physical hopping halves, all upper branches, physical neutral counterphases and absolute tone clocks are retained. A rigorous finite interval calculation bounds the final wrong-flag probability above0.98.

This is a failure of this specified echo implementation on its ideal-prefix reachable input. It is not an all-microscopic copy-plus-readout calculation, an asymptotic full-echo theorem, a hardware impossibility or a contradiction of the conservative K2336 sufficient error bound. That bound does not approve these rates. SC-ACT-01/GEO-55 ASSERTS and META53 UNCERTAIN, ledger0.263 and native GU verdicts are unchanged.

## Complete finite carrier and pulses

Basis states are (p,r,e,f) with p,r nonnegative, e,f in{0,1} and p+r+e+f=2, giving eight states. Define Pf=f, L=p+e, Zf=1-2f, and

    H0=Delta Pe+g(aP e+ +aP†e-),
    B=aR†aP, X=h(aP f+ +aP†f-),
    Hmic(Ds)=H0+Ds Pf+X-(Pe Zf+Pf)/Ds.             (1)

We set g=h=1, so chi=-1/Ds. Reference hopping and both exchanges preserve the full total excitation. A smaller Q=p+r+e<=1 truncation would discard actual contact intermediates and is invalid.

For D>0, contact time td=pi D/2 and corrected contact

    V(Ds)=exp(i Ds td Pf) exp(-i td Hmic(Ds)).       (2)

The first chronological contact has Ds=+D and chi<0, implementing nominal A†; the second has Ds=-D and chi>0, nominal A. Counterphases in(2) are actual gates as assumed in the K2336 contact model. The main witness takes their duration zero in the same ideal-gate limit; a finite drift-duration control is specified below. This does not authenticate a physical phase rate.

Put R=sqrt(Delta²+4), c=sqrt[(1+Delta/R)/2], s=sqrt[(1-Delta/R)/2], omega=(Delta-R)/2, J=10^-6, u=J/c, tau=pi/(4J). A physical absolute-clock half pulse of phase phi starting at t is

    P_phi(t)=exp[-i omega L(t+tau)]
      exp[-i(H0-omega L+u exp(i phi)B+u exp(-i phi)B†)tau]
      exp[i omega L t].                            (3)

This follows by an exact rotating-frame change, with [L,B]=-B; no rotating-wave removal of upper branches is made inside (3). Chronology is precisely

    W=P_(pi/2)(2td+tau) V(-D) P_pi(td) V(+D).        (4)

The input c|1,0,0,1>-s|0,0,1,1> is a lower JC eigenstate with copied label1 and threshold flag1. The spectator label register is fixed and omitted, not erased. It belongs to the output image of K2334's ideal copy. The ideal selective echo preserves f=1 and parks the excitation in the reference; in particular its probability for f=0 is exactly zero.

## Interval witness and independently explained mechanism

At Delta=D=10 the probe constructs(1)-(4) using Arb complex balls at256 bits. It bounds the sum of squared output amplitudes on f=0 and verifies

    0.98710 < Pr_W(f=0) <0.98711.                   (5)

Every matrix exponential and phase is enclosed; no floating-point eigensystem is used for acceptance. Measuring f=0 proves trace distance at least(5), hence the restricted-input half-diamond error exceeds0.98. Interval output and precision are stored in the report. This is a finite exact-input certificate, not extrapolation from several detunings.

The first local K=2 contact illustrates the mechanism. In basis |2gg>,|1eg>,|1ge>,|0ee> its diagonal is (0,D-1/D,D-1/D,2D); couplings from |2gg> to either middle state are sqrt2, and from either middle state to |0ee> are1. The antisymmetric middle state is dark at E=D-1/D. The symmetric bright sector is

    [[0,2,0],[2,E,sqrt2],[0,sqrt2,2D]].             (6)

Its middle eigenvalue is E+2/D+O(D^-3), giving a relative phase approaching pi over td=pi D/2 and transferring the neutral excitation into the mediator. This asymptotic explanation is independent of the finite certificate, but does not establish a long-time full-echo limit: the long hopping durations and changing spectral separations require a separate uniform estimate. The second signed contact has other resonances, so a global neutral-gap assumption would be false. The actual complete finite propagator already accounts for them.

## Executed controls and admissible repairs

The positive control replaces each microscopic contact with its EXACT ideal matched contact exp[-i(H0+chi LZf)td], keeping all hopping matrices, pulse times and clocks. It gives f=0 probability zero and near-complete parking. Removing h exchange also prevents flag leakage, but loses the desired microscopic phase synthesis and is only a mechanism control. Projecting away the full K=2 intermediates falsely erases the failure and is explicitly detected. Additional noninteger-D and finite phase-gate-duration tests retain nontrivial counterphases and drift; they are finite interval controls, not a universal hardware claim.

A finite phase implementation of duration delta after each contact is represented by exp(-iH0 delta) V(Ds), with subsequent pulse start times advanced by delta. Since H0 commutes with Pf, this is the assumed simultaneous drift plus phase gate model; during that gate neutral exchange is off. The control delta=1/100 is checked without resetting the absolute tone clock.

A direct detuning-based repair would separate BOTH signed contact detunings from the relevant populated dressed transitions, and then check accumulated phases and both physical halves on the same carrier. K2338's isolated-level leakage estimate alone does not certify those phases. K2336's valid sufficient compiler bound remains another route when a jointly attainable rate/noise set satisfies it. Raising detuning while keeping Delta=D is not a repair. Full microscopic number-copy, finite switches, loss, clock, reset and a measured joint feasible set remain distinct next inputs.

No source or ledger verdict changes. The universal objects used here are the written excitation conservation, rotating-frame identity and event-distance inequality; the new failure is the finite Arb witness. Established effective-Hamiltonian background is [Bravyi, DiVincenzo and Loss](https://arxiv.org/abs/1105.0675); it does not certify these device rates.
