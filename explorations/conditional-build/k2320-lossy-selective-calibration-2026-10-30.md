---
title: "K2320 Lossy selective calibration"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics only; no native physical acceptance
scripts:
  - tests/channel-swings/k2320_lossy_selective_calibration_probe.py
---

# K2320 Lossy selective calibration

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
result: K2320
carrier: fixed total-N pilot/reference shell, lower-number loss sectors, neutral record and independent retained working pump LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product, trace distance and occupation-control operator norm ON=declared_carrier
real_structure: complex amplitudes and physical adjoint
grading: total photon number, calibration charge twice photon number, loss-event count
action_owner: repository-construction -- K2315 selective controls with specified Markov loss and charged replacement
target: preparation exposure, flagged accuracy, protected-reference bound and renewal cost MAP-TYPE=evaluation
```

## Fixed architecture and loss model

Use [K2312](k2312-relational-finite-calibration-2026-10-30.md)'s sine state on |n,N-n>, independent retained working pump mu=10^28, and single sensing query exp(-2i phi n). Its ideal full-output good-event probability p0>=43/45 has conditional error<9.986e-12; its actual-record average error d0<9.491e-12. Here impose [K2315](k2315-calibration-control-cost-2026-10-30.md)'s number-selective occupation-neighbor Hamiltonian with ||H_off||<=hbar J and arbitrary diagonal part. Its exact sine preparation from |0,N> requires T_p>=N/(2J); the specified Givens schedule attains T_p<=pi N/(2J). Occupation adjacency is not spatial locality, fixed J is not fixed microscopic beam-splitter coupling, and exact pulse areas are still supplied.

Add independent equal Markov amplitude damping on BOTH pilot and reference, with jump operators sqrt(gamma)a_P and sqrt(gamma)a_R. The environment is inaccessible. Extend the controls to lower shells while conserving total photon number; no gain, replacement or working-pump consumption occurs before the final flag. All sensing, storage and readout operations in the vulnerable interval must have a number-conserving dilation using neutral auxiliaries. The final total-number test and subsequent replacement are idealized separately. Let the entire vulnerable duration T=T_p+T_o be deterministic and record-independent. T_o>=0 includes the supplied sensing/readout/storage durations; an instantaneous ideal query is allowed only if explicitly granted. Controls and phases may be time dependent.

This supplies a concrete open-system control model, not a measured device, microscopic implementation or GU prediction. SC-META-53 remains UNCERTAIN, source/ledger0.263 unchanged. [K2318](k2318-loss-limited-calibration-2026-10-30.md)'s single sensing-arm channel remains a different noise placement; its necessary sensitivity bound is not a preparation-survival theorem.

## Exact no-loss law and preparation exposure

On total-number shell N the no-jump generator is

    H_eff(t)=H(t)-i hbar gamma N I/2.

Thus the unnormalized no-jump propagator is exp(-gamma Nt/2)U(t), regardless of noncommuting number-preserving controls. The normalized state, phase estimate and conditional working output are exactly ideal. Every jump lowers total number, and no subsequent permitted control restores it. The final N-shell flag therefore selects exactly the no-jump event, with

    p_surv=exp(-gamma N T).                                      (1)

This does not assume photon-count monitoring of the environment. The flag uses the retained total number. If durations depend on outcomes, the survival factor reweights those records and(1)'s common probability/average formula cannot be used; use a uniform T_max bound or a separately weighted analysis.

Combining(1) with the actual preparation bound gives

    p_surv <= exp[-gamma N²/(2J)]      for any exact preparation,
    p_surv >= exp[-gamma N (pi N/(2J)+T_o)] for the stated schedule. (2)

The first is necessary within this exact-state, equal-loss, no-replenishment protocol. It is NOT an impossibility bound on using all lossy states for phase estimation. A general lossy sensor might use lower-number branches; this protocol marks them failed and counts them in the all-launch statistics.

## Complete confidence and averaged-output budgets

For the supplied flagged architecture, all-launch success is at least p0 p_surv. Hence

    p_loss=1-p_surv <=1/172                                      (3)

is sufficient for success>=.95, since (43/45)(171/172)=19/20. The actual ideal success can exceed43/45, so(3) is not a necessary confidence threshold. Assign every failure its actual error cost, bounded by1; successful record distributions remain ideal conditional on no loss. The actual-record averaged output error obeys

    d_actual <= p_surv d0+(1-p_surv) <= d0+p_loss.                 (4)

For the distinct average-error goal1e-11, p_loss<=5e-13 suffices, giving<9.991e-12. The confidence and average budgets must not be interchanged. Preparation, inverse actuation, reference drift and pulse errors were ideal in(1)--(4); actual nonzero errors consume additional slack by the existing trace-distance triangle bounds.

For any specified allowed failure epsilon in(0,1), put L=-log(1-epsilon). Necessary and constructive sufficient PREPARATION-ONLY conditions are respectively

    gamma/J <=2L/N²,                 gamma/J <=2L/(pi N²).        (5)

With nonzero T_o, the constructive condition is instead gamma N[pi N/(2J)+T_o]<=L. At N=3e27, use rigorous epsilon<=L<=epsilon/(1-epsilon). For confidence epsilon=1/172, the necessary preparation rate cannot exceed2/(171*9e54); a simple conservative sufficient rate is1/(86*pi*9e54). For average epsilon=5e-13 the simple sufficient rate is1/(9*pi*10^66); the necessary rate from(5) is at most1/[9*10^66(1-5e-13)]. These compare rates, not seconds or hardware feasibility. They expose an N²/J vulnerable photon-time cost that a post-preparation loss budget alone did not count.

## Protected reference: finite-rate necessity, and a false shortcut

Now change the architecture: only the pilot loses, with rate gamma, reference protected. For the normalized no-jump state let m(t)=<n> and v(t)=Var(n). Direct differentiation of the normalized non-Hermitian equation gives

    m'=(i/hbar)<[H,n]>-gamma v <= J.                              (6)

The commutator norm bound is K2315's occupation-neighbor bound; no bound on diagonal energies is needed. If the NORMALIZED NO-JUMP ENDPOINT itself must equal the sine state, m(T_p)=M=N/2. Starting at m(0)=0 and using m>=0,(6) gives T_p>=M/J and

    m(t)>=max(0,M-J(T_p-t)),
    integral_0^Tp m(t)dt >=M²/(2J),
    p_surv=exp[-gamma integral m(t)dt] <=exp[-gamma N²/(8J)].      (7)

This finite-rate necessary bound is valid even when the controls have been redesigned to compensate conditional filtering, provided the control norm and exact conditional endpoint premises hold. It is not a sufficient selective compiler and it does not force a confidence bound if the protocol exploits loss outcomes or uses a different calibration state. A final trace distance eta to the sine state gives M>=N(1/2-eta) and the corresponding squared bound when eta<1/2.

One may NOT exponentiate the occupation of the LOSS-FREE ideal path and assert an exact survival formula for its lossy implementation. For N=1, start in (|0,1>+|1,0>)/sqrt2 and store with H=0. Then p_surv=(1+exp(-gamma t))/2, whereas exponentiating the ideal mean1/2 gives exp(-gamma t/2). The surviving state is tilted toward |0,1>. Its mean is exp(-gamma t)/(1+exp(-gamma t)); integrating that conditional mean recovers the true survival. Equal loss on both modes made the first theorem scalar; protected reference removes that special simplification. This exact countercontrol prevents calling(7) an achieved protected-reference construction.

## Exact protected-reference compiler for the one-photon shell

The necessary bound(7) alone does not construct a compiler. On N=1 this can be settled exactly, including the strongest admissible diagonal/phase controls. Write the normalized no-jump state with population angle theta in[0,pi/2], so pilot population is sin²theta. Any offdiagonal control norm<=hbar J gives

    theta' <= J-(gamma/4)sin(2theta).                            (8)

The loss contribution follows by differentiating tan(theta)=|psi_1/psi_0|; arbitrary diagonal phases cannot increase the radial population velocity. Equality is attained by the constant Hamiltonian H/hbar=[[0,-iJ],[iJ,0]] with positive real initial amplitude (1,0). The sine target is theta=pi/4. Hence an exact conditional sine endpoint is finite-time reachable iff gamma<4J. At equality the speed vanishes quadratically at the endpoint, giving infinite arrival time; above it the first root theta_bar=asin(4J/gamma)/2<pi/4 is an uncrossable population barrier. This is for the two-state shell, the stated control norm, pilot-only loss and no gain, not a general quantum-sensing impossibility.

For a=gamma/(4J)<1 and nu=J sqrt(1-a²), the saturating pulse has

    T_* = atan[nu/(J-gamma/4)]/nu,
    p_* = exp(-gamma T_*/2)/(1-a).                               (9)

These are the minimum preparation time AND maximum no-jump survival for this exact endpoint. To check the construction, the unnormalized amplitudes are

    psi_0=e^(-gamma t/4)[cos(nu t)+(gamma/(4nu))sin(nu t)],
    psi_1=e^(-gamma t/4)(J/nu)sin(nu t).

At T_* they are equal, and their squared norm gives(9). Equivalently T_* is integral_0^(pi/4) dtheta/[J-(gamma/4)sin2theta]. For optimal survival, define V(theta)=integral_0^theta sin²u/[J-(gamma/4)sin2u]du. When gamma<4J the denominator is positive throughout[0,pi/2], and(8) implies dV/dt<=sin²theta. Every path to pi/4 therefore has conditional occupation exposure at least V(pi/4), attained by the same pulse. This proves optimal survival even against phase control, slower paths and population backtracking. At gamma=0 the formulas give T_*=pi/(4J),p_*=1; above threshold no exact finite-time target exists. Approximate targets and other final states remain different problems.

This provides an achieved finite-rate protected-reference example and a sharp compiler threshold. It does not establish the large-N sine-state compiler required at stock3e27: there, multiple occupation amplitudes filter at different rates, and previous Givens amplitudes do not remain fixed during later lossy pulses. The large-N exposure bound(7) survives, but its attainability is still an actual control problem.

## Charged renewal and finite-memory reset

For equal loss and any number-conserving control, the full master equation gives d<E N_total>/dt=-gamma<E N_total>, hence the expected lost photon stock per full-duration attempt is

    ell=N(1-exp(-gamma T)).                                      (10)

The inherited calibration charge is Q_cal=2 N_total, so required mean replacement charge is2ell. Restoring every failed branch to stock N while returning all charged auxiliaries unchanged is impossible under total-charge-conserving operations whenever ell>0. A retained working pump or depleting charged ancilla is a reservoir if used; renaming it does not erase the consumption. This is charge accounting, not a thermodynamic energy/heat theorem.

For a separately supplied iid renewal model, run every attempt for the same duration T, measure the flag at the end, restore its exact missing photons from a charged reservoir, and repeat until no loss. Expected attempts is1/p_surv. The expected aggregate photon replacement before the first no-loss completion is

    ell/p_surv=N(1-exp(-gamma T)) exp(gamma N T),                  (11)

and charge cost is twice this. First-step conditioning proves(11): expected total cost equals ell+(1-p_surv) times itself. The successful attempt loses zero photons. An always-abort-at-first-jump policy is a different duration/cost model. Repeating the phase query also changes the single-query all-launch task;(11) is renewal resource accounting, not a loophole in its95% requirement.

K2312's M=N+2 records require at least ceil(log2 M) neutral bits for orthogonal outcomes (92 at N=3e27). Retaining R complete records reversibly requires dimension M^R in the worst case, plus failure information. A finite apparatus restored to its initial state must export these distinctions to a memory/environment or erase them; a unitary cannot send multiple orthogonal records to one state while restoring everything else. This does not price Landauer heat without an explicit thermal reservoir or energy spectrum. Charged replenishment and neutral information reset are separate debts, now represented in the same protocol.

## Verification, context and remaining discriminator

The probe independently constructs finite loss Kraus maps and checks the scalar no-jump operator, completeness, loss-sector orthogonality, number expectation and conditional filtering. Exact symbolic controls check occupation-speed/drift and exposure, while rational controls check budgets and changed-input faults. Written arguments establish arbitrary-N/time-dependent claims; no finite control is promoted to all-N certification. The underlying quantum-trajectory formalism is standard; see [Dalibard, Castin and Molmer (1992)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.68.580), with an [author manuscript](https://arxiv.org/abs/0805.4002). No novelty adjudication is made.

The strongest next apparatus construction is an explicit protected-reference selective compiler with its NO-JUMP endpoint and full-channel error proved, plus a priced reservoir and neutral reset. The equal-loss model gives a sufficient architecture with explicit N² exposure; the protected-reference bound is necessary only. A microscopic rate/control relation gamma(J), real pulse errors and reservoir spectra would make a feasibility statement possible; none is inferred. Recomputing loss-free Givens universality or sine minimax would not answer that question.
