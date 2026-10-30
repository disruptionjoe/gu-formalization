---
title: "K2336 Microscopic matched contact with a finite-time instrument bound"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no survey, hardware or native GU acceptance
scripts:
  - tests/channel-swings/k2336_dispersive_contact_realization_probe.py
---

# K2336 Microscopic matched contact with a finite-time instrument bound

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
result: K2336
carrier: full pilot/reference Fock spaces, mediator qubit and neutral qubit; local input Q<=N and invariant contact K=Q+Pf<=N+1 LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert norm and restricted-input half-diamond distance ON=declared_carrier
real_structure: complex adjoint with real detuning and coupling
grading: total contact excitation K; ideal optical-mediator excitation Q
action_owner: repository-construction -- rotating-wave two-qubit cavity Hamiltonian plus supplied longitudinal contact and phase controls
target: realize K2334 matched contact with explicit switching, drift, leakage and noise costs MAP-TYPE=evaluation
```

## Result and microscopic model

[K2334](k2334-microscopic-neutral-transfer-2026-10-30.md) compiles unknown lower-dressed-state readout assuming an exactly matched bare contact chi(n+Pe)Z_f. Here a specified microscopic cavity-neutral exchange and a tunable mediator-neutral longitudinal interaction approximate that contact. An explicit finite-shell bound includes the cross-commutator with the original JC mediator, sudden switching, contact duration, phase compensation and noise. This is a mathematical device model, not evidence that one experimental device supplies these couplings/rates.

Use K2334 H0=Delta Pe+g(a e_+ +a† e_-), Q=n+n_R+Pe, L=n+Pe and Z_f=1-2Pf. During one contact, hopping and other neutral gates are off. Supply signed D!=0, real h, and

    chi=-h²/D,
    Hmic=D Pf+H0+h(a f_+ +a† f_-)+C,
    C=chi(Pe Z_f+Pf).                                (1)

Thus the mediator-neutral coefficient is chi, including its SIGN, and the local neutral frequency counterterm is chi Pf. This alphabet replaces an assumed photon-number contact by microscopic transverse exchange; it STILL supplies tunable mediator-neutral ZZ and neutral frequency control. It does not derive those from GU or from cavity hopping. Negative detuning gives positive chi in this Z convention. No independent-neutral-entangling capability follows from this interaction alone.

The microscopic unitary is defined on the full Fock direct sum. Each total K=Q+Pf sector is finite and invariant. On ideal input Q<=N with arbitrary neutral state, the contact occupies K<=M=N+1. The extra photon is essential: |N,g,f=1> couples to |N+1,g,f=0>. Artificial Q<=N projection changes the model. The reference is inert during the contact; loss/reference protection and neutral gates remain explicit resources.

SC-ACT-01/GEO-55/COS-50/51/54 ASSERTS and SC-META-53 UNCERTAIN, ledger0.263 and native verdicts are unchanged. Positive Hilbert dynamics, rotating-wave Hamiltonians and supplied Markov noise are imported conventional assumptions. No hardware, empirical, external-expert or native GU acceptance follows.

## Finite-shell derivation with a controlled remainder

Set X=a f_+ +a† f_-, Y=a f_+ -a† f_-, S=(h/D)Y. On K<=M, S is anti-Hermitian, ||S||<=s=|h/D|sqrt M and ||hX||<=v=|h|sqrt M. Direct commutators give

    [S,D Pf]=-hX,
    [S,hX]/2=(h²/D)(Pf-n Z_f),
    [S,H0]=(hg/D)(f_+ e_-+f_- e_+),
    ||C||=|chi|.                                     (2)

The Delta Pe term commutes with S. Combining the second-order shift with C leaves precisely chi LZ_f, so

    e^S Hmic e^-S = D Pf+H0+chi LZ_f+R,
    ||R|| <= r = exp(2s) [|hg/D|
                    + 2|h|³ sqrt M (M+1)/D²].         (3)

Here is an explicit bound, not a gap slogan. Let ad_S(A)=[S,A]. After cancellation of hX, the fast-sector tail is sum_(k>=2) k/(k+1)! ad_S^k(hX), bounded by2v s² exp(2s). The remaining H0 tail is integral_0^1 e^(tS)[S,H0]e^(-tS)dt, at most exp(2s)|hg/D| (unitarity even permits a tighter bound). C changes by at most2s||C||exp(2s). Their sum is(3). No spectral-gap condition D>Delta or free dressed input gate has been silently assumed.

Duhamel and ||e^S-I||<=s give the undressed unitary bound

    ||e^(-itHmic)-e^[-it(DPf+H0+chi LZ_f)]||
       <=2s+|t|r.                                    (4)

This also bounds half-diamond distance on ideal Q<=N inputs, including arbitrary entangled spectators. It charges both sudden-switch endpoint dressings. Do not apply the small instantaneous remainder without multiplying by the actual contact time.

## Lab phase, switching and composition

Correct e^(-iDt Pf) with a real neutral Z phase after each contact. With h and C and D switched off during correction, H0 commutes with that phase; its unavoidable extra H0 drift is retained in K2334's absolute-time carrier convention. A phase modulo global phase fits in time <=pi/g1 under an available neutral generator cap g1. This is an additional local gate and its noise/time is charged. A consistently tracked rotating frame could substitute only after all later controls are transformed; it is not an unexplained free correction. Known finite ramps/control deviations instead contribute integral||Delta H||dt on the relevant finite carrier. No adiabatic-ramp theorem is asserted.

K2334 uses q=ceil(log2(N+2)) copy contacts and two contacts for each of N selective echoes. Thus Cnum=q+2N and total contact time

    Td=pi(N+1-1/d)/|chi|, d=2^q.                     (5)

Use D signs required by the signed contact. Add Cnum real phase gates and phase time <=Cnum*pi/g1. With identical |D|,|h|, total microscopic-contact error is

    e_contact <=2 Cnum s+Td r.                       (6)

Although actual leakage can persist between contacts, (6) does NOT assume the full actual circuit stays in Q<=N+1. For channels E_j actual and F_j ideal, telescope

    E_m...E_1-F_m...F_1
      =sum_j E_m...E_(j+1)(E_j-F_j)F_(j-1)...F_1.

Every local difference sees an ideal prefix with Q<=N; later physical CPTP maps contract its error. The global direct-sum microscopic channels therefore admit the local bound without deleting accumulated leakage. Arbitrary external entanglement is retained by the same restricted-input diamond estimate.

Let lambda0=kappa N+Gamma+kappa_R N+lambda_neutral for noncontact ideal segments and lambdac=kappa(N+1)+Gamma+kappa_R(N+1)+lambda_neutral for contacts. Amplitude damping only decreases K, and neutral dephasing preserves it; these local noise bounds need no actual-circuit hard truncation. Other excitation-raising noise requires its own invariant/dominating bound and is not covered. With K2334 constants A'_N,B_N,G and the explicit neutral elementary time t_el derived below, the complete sufficient instrument bound is

    e_inst <= e_in + A'_N J + lambda0 B_N/J
              + 2 Cnum s + Td r + lambdac Td
              + lambda0*(G*t_el+Cnum*pi/g1) + e_control.    (7)

Here e_control includes actual timing/ramp/parameter errors and any nonideal neutral gates, and e_in includes preparation error. Hopping caps J/b_k<=g_BS still apply. Fresh pure outcome/reset registers and their costs remain K2334 assumptions. There is no exact loss heralding. The output/reset channel is CPTP, so event error is <=e_inst and the [0,4]-valued phase risk error <=4e_inst.

Set e_fixed to all terms in(7) except A'_N J+lambda0 B_N/J. For tolerance epsilon the same sufficient amplitude window exists when epsilon-e_fixed>0 and

    (epsilon-e_fixed)²>=4 A'_N lambda0 B_N,            (8)

with J between the two quadratic roots and within the hopping cap. This evaluates the microscopic model in the actual consumer rather than just restating dispersive smallness. Failure of this conservative certificate is not a hardware impossibility theorem.

## Executed successor: explicit nearest-neighbor neutral gates

Supply individually switchable adjacent Ising interactions Jzz Z_j Z_(j+1), plus arbitrary one-qubit rotations with Hamiltonian norm cap g1; all spectator Ising terms can be switched off. These are additional concrete device-model assumptions. During neutral gates the cavity contact/detuning controls are off. H0 commutes with the neutral gates, so its full elapsed drift remains in the absolute-time protocol; no Kerr revival is substituted.

An Ising pulse of duration pi/(4|Jzz|), with its sign compensated by local rotations if needed, yields exp(-i pi ZZ/4). Two local Z rotations give CZ up to one harmless global phase:

    CZ=e^(-i pi/4) exp(i pi ZI/4) exp(i pi IZ/4) exp(-i pi ZZ/4).

Conjugate by target Hadamards for CNOT. Serial local rotations give the conservative bound

    t_CNOT <= pi/(4|Jzz|)+3pi/g1.

SWAP is three CNOTs. A controlled phase diag(1,1,1,e^(i theta)) is (P(theta/2) tensor P(theta/2)) CNOT (I tensor P(-theta/2)) CNOT, with P(alpha)=diag(1,e^(i alpha)); this uses two CNOTs and three local phase gates. K2334's actual compiler uses these, one-qubit gates, and the held fifteen-elementary-gate Toffoli decomposition into local/CNOT gates. It does not require arbitrary SU(4) gates after this expansion. Thus every elementary operation counted by its conservative G has duration at most

    t_el=3pi/(4|Jzz|)+12pi/g1.                        (11)

Routing SWAPs are already counted in G. The extra Cnum neutral phase corrections cost at most Cnum*pi/g1 separately. Equation(7) now prices a fully specified nearest-neighbor neutral alphabet. Nonideal rotations, residual spectator interactions and imperfect switching contribute to e_control; a finite control norm or a declared Ising coupling alone does not show they vanish. This construction closes the abstract neutral-gate synthesis step in the conditional model, not its same-device experimental availability.

## Constructive feasibility and actual limitations

At fixed desired |chi|>0 choose |D|->infinity, |h|=sqrt(|chi D|), and matching signed longitudinal/frequency controls. Then s->0, r->0, while Td is fixed. Thus the contact error can be made arbitrarily small in THIS supplied family. This spends unbounded detuning and exchange amplitude; it is not free hardware feasibility. At fixed h, increasing D makes Td proportional to D/h², and the cross-commutator contribution behaves like g/h. The present bound then does not certify arbitrary accuracy from detuning alone.

The probe evaluates one simultaneous mathematical rate fixture N=2,Delta=2,g=7/10,|chi|=1,|D|=10^16,|h|=10^8,g1=|Jzz|=10^12,kappa=Gamma=kappa_R=10^-24,lambda_neutral=10^-24,J=10^-8, with zero stipulated input/control errors. All rates are in one fixed unit convention. It is deliberately extreme, not measured; the full inequality(7), not an isolated ratio, is checked. Its significance is that the conditional inequalities are jointly nonempty; actual physically plausible rates remain open.

A separate finite propagator control uses modest h and large D, retains every state K<=N+1 (including reference/mediator/neutral branches), and compares the actual corrected unitary with the ideal interaction for the actual contact angle. Its finite high-precision result is not an interval certificate; (2)-(4) carry the universal claim.

## Counterexample: small h/D is not time-uniform accuracy

Even set g=0 and mediator ground. In total cavity-neutral excitation m=2, (1) reduces to

    [[0,h sqrt2],[h sqrt2,D-h²/D]].                   (9)

For D>0 its lower energy lambda_- differs from the ideal ground-neutral value -2h²/D by delta=lambda_-+2h²/D>0, asymptotically2h^4/D^3. At t=pi/delta, the superposition of vacuum and the lower dressed m=2 eigenvector develops an order-one relative phase error compared with the second-order target, while its bare/dressed distance and leakage vanish as h/D->0. Equivalently the bare superposition has the same limiting separation, by the vanishing dressing bound. This is a real changed-time counterexample; it does not contradict the fixed-angle construction above. The compensated one-excitation block is unusually exact, so testing only m=1 would miss the defect.

Ignoring [S,H0] is also unjustified: the exchange term in(2) transfers excitation between mediator and neutral qubits. For Delta near D it is near resonant. Neither the matched diagonal term nor a local phase correction removes that operator. The exact commutator control detects omission before any long-time approximation is used.

## Evidence and next physical construction

The companion probe checks full finite-shell commutator identities, actual corrected propagators, the norm remainder, rate budget and the genuine long-time counterexample; changed Hamiltonian sign, omitted mediator/contact compensation and truncated boundary inputs must fail scientific checks. Universal claims use the written bounds and channel telescope, not numerical sampling. [Bravyi, DiVincenzo and Loss](https://arxiv.org/abs/1105.0675) supply established context for rigorous Schrieffer-Wolff methods; the elementary finite-shell bound here is derived explicitly and claims no novelty for that technique.

Next constrain ONE device's accessible h,D, longitudinal matching, neutral entangling operations, noise, clock/ramp control and pure-register/reset supply, then test(7)-(8). The explicit adjacent-Ising compiler above removes abstract two-qubit synthesis as an open mathematical step; its simultaneous rates and crosstalk with this cavity model still require device evidence. Native action/quantization, observed physical state/domain, source-owned readout and empirical performance remain separate obligations.
