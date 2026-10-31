---
title: "K2353 Stagewise damping and a late-record speed limit"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or empirical certification
scripts:
  - tests/channel-swings/k2353_late_record_relaxation_probe.py
---

# K2353 Stagewise damping and a late-record speed limit

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
result: K2353
carrier: K2347 two-input copy echo on full stagewise reachable finite support LAYER=toy CHIRALITY=N/A
pairing: trace distance and restricted half-diamond channel norm ON=declared_carrier
real_structure: real parameters; complex Hilbert structure only for quantum channels
grading: excitation Q and neutral occupancy Pf
action_owner: repository-construction -- K2350 finite ramps with supplied Markov amplitude-damping jumps
target: joint sufficient error budget and necessary fixed-readout T1 bound MAP-TYPE=evaluation
```

## Result and scope

[K2350](k2350-joint-switching-resource-certificate-2026-10-30.md) gives a finite-ramp certificate with an abstract noise rate and a distinct early common-erasure obstruction. Here four specified amplitude-damping channels justify the noise rate on the actual reachable support. Late neutral-record relaxation factors exactly through the last hopping pulse and yields a necessary speed limit for its declared readout, even with arbitrary earlier preparation. This is neither the earlier common-vacuum theorem nor a claim about every recovery architecture. No hardware measurement, GU dynamics or physical-state quotient is supplied; SC-META-53's uncertainty and ledger0.263 remain unchanged.

## Four jumps and invariant support

Reuse the11-pulse schedule, t=pi D/2, tau=pi/(4J), neutral durationdelta, ramp durationr and c fromK2350. Define the time-local Lindblad model

    L_a=sqrt(gamma)a, L_R=sqrt(gamma)a_R,
    L_e=sqrt(gamma)e_-, L_f=sqrt(kappa)f_-, gamma,kappa>=0.

These rates are supplied constant parameters, not inferred bath data. The total rate operator is R=sum L†L=gamma Q+kappa Pf. Jumps only lower K=Q+Pf; R is diagonal in number sectors. The no-jump Hamiltonian and the scheduled controls preserve the same stagewise support as the nominal dynamics. Therefore trajectories, including jump histories and arbitrary ancillas, stay in the finite carrier. Bosonic heating would destroy this argument and is not covered.

For a restricted support with R<=A I, the completely positive jump map has diamond norm||R||<=A; the anticommutator map has diamond norm<=A. Thus half-diamond generator norm<=A. Duhamel and contractivity of CPTP propagators bound channel difference from the nominal unitary by the integrated A. This uses restricted operators on an invariant carrier, not unbounded oscillator diamond norms on the full Fock space.

The stage bounds are

    A1=gamma+kappa,
    A2=max(2gamma,gamma+kappa),
    AH=2gamma+kappa,
    A3=max(3gamma,2gamma+kappa).

During the first Hadamard Q<=1,Pf<=1; after it K<=2. Copy contact and its counterphase preserve K<=2. The second Hadamard has Q<=2,Pf<=1 and may raise K to3. The remaining seven pulses preserve K<=3. Total noise debt is therefore

    Bnoise=A1(delta+2r)+A2(t+delta+4r)+AH(delta+2r)
           +A3(2t+3delta+2tau+14r).                       (1)

Durations sum to T=3t+6delta+2tau+22r. For gamma=kappa=lambda this simplifies to

    Bnoise=lambda(8t+16delta+6tau+60r),                    (2)

saving lambda(t+2delta+6r) over the global3lambda T estimate. This is an upper bound, not exact accumulated error.

Combine the unchanged K2350 contactC(D), selectivebeta J, ramp rL and preparation error:

    Ebound=C(D)+beta J+rL+Bnoise+epsilon_input.             (3)

At fixed remaining parameters, this still has form bJ+k/J+F, with b=beta+6r/c, k=A3 pi/2 and F containing all other terms. The prior quadratic interval criterion applies with these new coefficients. Its failure remains failure of a sufficient certificate, not impossibility. For the prior supplied D=20001/2,J=10^-6,delta=.01,r=10^-10, take gamma=kappa=10^-10/4. Every stage rate is<=3*10^-10/4, below the oldnu=10^-10. Thus the old<.01 witness remains certified with a strictly smaller noise bound. The exact probe evaluates the improved same-device rational bound; unchanged amplitude and slew cap checks are reused from K2350. No rates were measured.

## Exact final-record relaxation

The final hopping pulse, its ramps and H0 act only on cavity/reference/mediator, trivially on f. The three gamma jumps also act only on that subsystem. Hence the final generator is a tensor sum and its evolution factors into a trace-preserving subsystem channel and neutral amplitude damping with

    eta=exp[-kappa(tau+2r)].

This factorization holds even for a correlated incoming state. Taking a partial trace, the neutral marginal is AD_eta(rho_f); trace preservation on the other factor suffices. With immediate measurement of f in its declared energy basis and no subsequent recovery, its flag1 probability is

    p1_out=eta p1_in<=eta.

For the encoded input whose target flag is1, trace-distance error of the measured distribution is therefore at least

    1-exp[-kappa(tau+2r)].                                 (4)

There is no subtraction of nominal circuit error and no need to assume a good preceding circuit. At eta=1/4 this floor is3/4, distinct fromK2350's early common-erasure3/8. At kappa=J=10^-6 andr>=0, kappa tau=pi/4>3/4 and exp(x)>1+x gives floor>3/7. Earlier controls cannot evade(4), but a different final record, subsequent error correction, replenishment or active final-f control changes its assumptions. Pure dephasing leaves the computational flags unchanged and supplies no such floor.

To achieve error<=epsilon in(0,1), necessarily

    kappa[pi/(4J)+2r]<=ell=-log(1-epsilon).

For kappa>0 this requires ell>2kappa r and

    J>=pi kappa/[4(ell-2kappa r)].                         (5)

Intersect this necessary interval with the sufficient interval from(3) and the amplitude/slew constraints. Existence in the intersection certifies the supplied model only if every sufficient condition holds; emptiness caused solely by the sufficient interval is not a universal no-go.

## Genuine cap-conditioned speed limit

On the declared complete K<=3 carrier, the hopping perturbation has EXACT norm3J/c. If the actual cap G and envelope-slew cap V apply to this full carrier, linear ramps imply3J/c<=min(G,Vr). Combining with(4), every realization of this specific final hopping/readout architecture obeys

    kappa[3pi/(4c min(G,Vr))+2r]<=ell                      (6)

as a necessary condition for epsilon accuracy. This uses the exact hopping norm, not a conservative upper norm estimate relabeled as necessary. Lab-carrier derivatives are still separate from envelope slew. Other pulse caps only tighten feasibility.

Let a=3pi/(4c). Minimizing f(r)=a/min(G,Vr)+2r over r>0 gives

    r_opt=min(G/V,sqrt(a/(2V))),
    f_min=a/G+2G/V,       if G<=sqrt(aV/2),
    f_min=2sqrt(2a/V),    otherwise.                       (7)

Proof: in the ramp-limited region f=a/(Vr)+2r is strictly convex and minimized at its derivative zero; in the amplitude-limited region f=a/G+2r increases. Compare at the shared boundary. If kappa f_min>ell, the stated architecture cannot meet epsilon under these whole-carrier caps, regardless of earlier controls. It does not exclude another detector or correction scheme. This removes the misleading limit of taking arbitrarily slow selective hopping while holding nonzero record T1 fixed.

## Evidence and next condition

The probe checks support maxima by exact finite number sectors, duration and rate identities, Kraus completeness and correlated-state marginal damping, exact hopping norms, calculus of the two cap regimes, and the rational sufficient witness. Modified channels test zero relaxation, pure dephasing and record recovery. Heating and an underpriced Q<=1 noise restriction are analytic excluded-support counterexamples, not evolved noisy-circuit reruns. Universal channel and speed bounds rely on the proof above. Next requires simultaneous measured rates/caps/timing on one device, or a rigorously specified error-correcting final record and its costs; no empirical/hardware or full q,N instrument claim is made.
