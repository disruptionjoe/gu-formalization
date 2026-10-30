---
title: "K2324 Kerr-selective lossy control"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics only; no native physical acceptance
scripts:
  - tests/channel-swings/k2324_kerr_selective_lossy_control_probe.py
---

# K2324 Kerr-selective lossy control

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
result: K2324
carrier: fixed total-N two-mode bosonic shell, pilot loss and protected reference LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert norm, no-jump contraction and trace distance ON=declared_carrier
real_structure: complex adjoint and programmed classical drive phase
grading: sensing occupation n and total photon shell
action_owner: repository-construction -- supplied Kerr drift and beam-splitter drive with Markov pilot loss
target: finite-time selective-control approximation, phase correction and sufficient resource window MAP-TYPE=evaluation
```

## Replace a granted selector by a specified Hamiltonian

[K2322](k2322-protected-reference-compiler-2026-10-30.md) exactly prepares a conditional sine state using ideal individual occupation-neighbor controls. Here replace that granted selector with a concrete finite-shell Kerr drift and a driven two-mode beam splitter. A rigorous propagator estimate, valid with noncommuting pilot loss, gives a whole-compiler error of order NJ/|chi| at fixed gamma/J<4. Combined with quadratic photon exposure, it yields an explicit sufficient Kerr-to-loss resource condition. It is an approximation theorem for a supplied model, not an implementation or an optimum.

All Hamiltonians below are divided by hbar. In shell N>=1 let n=0,...,N, E_n=chi n(n-1)/2, chi!=0, and

    H_lab(t)=diag(E_n)+u_k exp(-i omega_k t) a_P^dagger a_R
                         +conjugate transpose,
    b_j=sqrt[j(N-j+1)], omega_k=chi(k-1), |u_k|=J/b_k.    (1)

During pulse k, the drive couples ALL adjacent edges with amplitudes u_k b_j, not just the selected edge. Pilot loss is sqrt(gamma)a_P, protected-reference loss zero, gamma>=0. Losses never return to shell N. A perfect final total-number flag is supplied. Classical phase/timing, exact chi/gamma, this Hamiltonian and positive quantum mechanics are additional assumptions; no microscopic relation among rates or physical energy/timing bound has been established. Occupation locality is not spatial finite range. SC-META-53 remains UNCERTAIN and ledger0.263 unchanged.

Use the exact H0 interaction frame. Since H0 commutes with n, the no-jump generator is

    A_actual(t)=-i[H_k+V_k(t)]-gamma n/2,
    A_ideal=-i H_k-gamma n/2,                            (2)

where H_k has only edge k with norm J, and unwanted raising edge j carries phase exp[i chi(j-k)t]. These formulas are exact for (1); there is no prior rotating-wave approximation in the supplied Hamiltonian. Its physical derivation from a real electromagnetic device is separate.

## Direct contractive averaging, including the loss

On a pulse interval [t_k,t_k+tau_k], define Hermitian F_k(t)=integral_tk^t V_k(v)dv and f_k=sup||F_k(t)||. Both propagators in (2) are contractions. Integration by parts in Duhamel, differentiating U_actual(t_end,t) F_k(t) U_ideal(t,t_k), gives

    ||K_actual-K_ideal|| <= f_k [1+tau_k(2J+v_k+gamma/2)],
    v_k=sup||V_k|| <= N |u_k|.                         (3)

The dissipative term is a COMMUTATOR [gamma n/2,F], not an anticommutator norm N gamma||F||/2. For a Hermitian nearest-neighbor matrix F with zero diagonal, i[n,F] is unitarily similar to F via diagonal entries i^n, so ||[n,F]||=||F||. The Hamiltonian commutator costs2Jf and the extra product V F costs v_k f. Boundary F(t_k)=0 leaves only one endpoint f. This proves (3) for arbitrary pulse start and duration with the exact loss drift. It does not silently compare a lossy pulse to a unitary one.

To prove v_k<=N|u_k|, the complete beam-splitter matrix is unitarily equivalent to2|u_k|J_x in spin N/2 and has norm N|u_k|. Removing the selected edge splits the chain into two principal blocks, a pinching that cannot increase its norm. Time phases are removed by a diagonal unitary.

An unwanted primitive entry obeys

    |F_j(t)|<=2|u_k| b_j/[|chi| |j-k|].                 (4)

For j>k, b_j²/b_k² <=j/k<=1+(j-k); for j<k, the analogous second factor gives b_j²/b_k²<=(N-j+1)/(N-k+1)<=1+(k-j). Thus for |j-k|>=1,

    b_j/(b_k |j-k|)<=sqrt2,
    f_k<=4sqrt2 J/|chi|.                               (5)

The last step is the tridiagonal row-sum bound (at most two unwanted entries per row). For N=1 there are no unwanted edges, so f_1=0 exactly; the loose uniform (5) is not needed. Exact individual f_k or tighter row bounds can replace (5).

## Whole lossy compiler and its lab-frame phases

Let a=gamma/(4J)<1 and

    q(a)=(pi/2+arcsin a)/sqrt(1-a²).

Reuse K2322's backward-elimination durations tau_k<=q/J, total T<=Nq/J, and ideal survival

    p>=exp[-gamma N² q/(2J)].                          (6)

Telescoping the ACTUAL contractions gives total raw error eta<=sum_k e_k. Since

    sum_{k=1}^N 1/sqrt[k(N-k+1)] <= pi,

(3)--(5) yield

    eta <= C(a) JN/|chi|,
    C(a)=4sqrt2 [1+q(a)(2+2a+pi)].                      (7)

For the sum bound, f(x)=[x(N+1-x)]^-1/2 is convex on (0,N+1): log f has positive second derivative, hence so does f. Jensen on each interval [k-1/2,k+1/2] bounds f(k) by its cell integral; the full integral over (0,N+1) is pi. The factor2a in (7) is gamma/(2J). All estimates are finite-N uniform inequalities, not numerical asymptotics or optimal constants.

Known Kerr drift must be removed in the LAB output without granting a free diagonal gate. First compute the ideal positive-target durations and T. They depend only on target magnitudes. For normalized target amplitudes z_n with nonzero magnitudes, choose

    D_nn=exp{i[arg z_n+E_n T]},
    u_k=(iJ/b_k) exp{i[arg z_k-arg z_(k-1)+chi(k-1)T]}.  (8)

For the positive sine vector all arg z_n=0. K2322's forward Hermitian selected edge has raising coefficient +iJ. Equation(8) implements D H_k D^dagger on that resonant edge using a drive referenced to GLOBAL time in (1). Since D commutes with n, the ideal interaction-frame product has the same durations and survival and sends |0> to D|z|/C0 up to a global phase. Multiplication by exp(-iH0T) gives z/C0 in the lab. There is no circular timing solve: T was computed from magnitudes first. Each actual off-resonant edge need not share the same D conjugation; the bound only uses its phase-independent magnitude.

If a waveform uses local time t-t_k, multiply u_k by exp[-i omega_k t_k] to recover (1). Omitting this starting-phase factor shifts the selected rotation. Omitting (8) leaves a generally incorrect Kerr phase on the target. Unknown drift or clock errors need a separate budget. No instantaneous final physical correction is assumed.

## Released consumer: sufficient rate/gap window and robustness

For eta<sqrt(p), the same geometric argument as K2322 gives

    p_actual >= (sqrt(p)-eta)²,
    D(normalized actual,z) <= eta/sqrt(p).              (9)

For a desired ideal failure epsilon in (0,1), L=-log(1-epsilon), and normalized state-error allowance 0<zeta<1, fix 0<a0<1 and require a<=a0. q and C are increasing, so a fully explicit sufficient construction is

    J >= max{gamma/(4a0), gamma N² q(a0)/(2L)},
    J <= |chi| zeta sqrt(1-epsilon)/[C(a0)N].            (10)

When this interval is nonempty, p>=1-epsilon and (9)'s state error is at most zeta; the actual success probability still has the reduced lower bound in (9). At gamma=0 omit the first lower bound if a0=0 and use q(0),C(0) directly. For positive gamma and fixed a0,epsilon,zeta, the exposure term in (10) implies a sufficient gap/loss scale proportional to N³. This is a conservative CERTIFICATE requirement, not a necessary scaling for every control, a hardware impossibility or an optimal resource bound. The microscopic beam splitter has norm N J/b_k and is not in K2322's fixed offdiagonal-norm-J class; its whole exact reachability iff theorem cannot be transferred. However the chosen amplitude envelope has head-tail coupling |u_k|sqrt(N)<=J, since b_k>=sqrt(N). The same head-tail comparison independently retains the necessary gamma<4J condition for an exact sine endpoint under that envelope, including the Kerr diagonal drift. Exact finite-chi sufficiency is unproved: below threshold this note proves arbitrarily accurate approximation as |chi| increases, not exact finite-gap reachability.

A simple explicit conservative numerical-free choice is a0=1/2. Then q(a0)=4pi/(3sqrt3), and (10) gives exact symbolic constants. Rate errors, Hamiltonian errors and timing-induced waveform errors may be added through contractive Duhamel: on a common duration, an additional error is at most integral(||Delta H||+N|Delta gamma|/2)dt. For chi uncertainty the diagonal perturbation norm is |Delta chi|N(N-1)/2; carrier and programmed phase errors must also be included in Delta H, not hidden in that one diagonal term. Large known Kerr splitting does not itself grant sufficiently accurate phase control.

There is a genuine zero-gap failure in the lossless restricted alphabet: for chi=gamma=0, beam-splitter drives with arbitrary time-dependent phase generate passive two-mode SU(2). From |0,N> the probabilities remain binomial. For N=3 the symmetric sine target has endpoint ratio1 and interior-to-endpoint amplitude ratio golden-ratio phi, whereas a symmetric binomial orbit has ratio sqrt3. Therefore it is unreachable within that alphabet. This does not exclude nonlinear controls outside (1), gamma>0 conditioned dynamics, or the distinct N=1 case. It supplies a nontrivial countercontrol to a selector assertion without spectral separation.

## Full-record meaning and remaining instrument

K2312's ideal query/readout/retained-pump benchmark may still be composed CONDITIONALLY after this preparation. With ideal instantaneous subsequent instrument, its previous good-event probability43/45 changes by at most eta/sqrt(p); multiplying by (9)'s survival gives

    success >= (sqrt(p)-eta)² [43/45-eta/sqrt(p)]

when the bracket is positive. Its bounded actual-record average cost similarly is at most 9.491e-12 +1-(sqrt(p)-eta)²+eta/sqrt(p), charging failed preparations at worst cost1. This is a classical-risk transfer for that supplied retained-pump task, not a generic claim about quantum output closeness.

A specified noninstantaneous readout has a separate rigorous interface. Supply a number-conserving neutral dilation W generated by a declared Hamiltonian in time T_r, with no-jump R under the same pilot loss. Contractive Duhamel gives ||R-W||<=xi=gamma N T_r/2 (plus integrated Hamiltonian mismatch). If A=sqrt(p), then ||R actual_prep-A Wz||<=eta+A xi. With d=eta/A+xi<1, the final no-loss probability is at least p(1-d)² and normalized postread trace distance is at most d. Put the shell flag AFTER readout. For a classical-outcome-only bounded risk replace eta/A by d and survival by p(1-d)² in the preceding inequalities; a generic comparison including the retained quantum output and actual record marginal requires K2312's conservative2d allowance. This is conditional on W and T_r, not a construction of their hardware. A preparation-only flag would miss readout loss.

The new Hamiltonian prices selective PREPARATION only. It does not implement K2312's phase POVM, noninstantaneous inverse actuation, physical loss flag, charged replenishment or neutral reset. Number conservation still ensures loss branches cannot reenter shell N; a full error-controlled instrument would need explicit lower-shell extensions and a declared outcome/reset apparatus. In particular no uncharged retries or ideal-readout assumption has disappeared. [Burgarth et al., Taming the Rotating Wave Approximation](https://arxiv.org/abs/2301.02269) provides context for rigorous finite-error analysis; its Rabi-model result is not the theorem for this different dissipative finite shell. Equations(3)--(10) are proved here; no novelty is claimed.

The probe checks exact detunings, commutator similarity, coupling ratios, sum identities, low-shell controls and genuine changed-input failures. Finite matrix exponentials compare actual lab-driven lossy pulses and the ideal schedule, including the phase repair, but are numerical controls rather than interval certificates. Universal error/resource claims rest on the written proof. No native GU quantization, hardware feasibility, empirical test or external certification follows.
