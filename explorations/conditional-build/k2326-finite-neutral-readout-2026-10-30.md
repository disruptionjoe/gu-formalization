---
title: "K2326 Finite neutral readout and loss-dark flag"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics only; no native physical acceptance
scripts:
  - tests/channel-swings/k2326_finite_neutral_readout_probe.py
---

# K2326 Finite neutral readout and loss-dark flag

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
result: K2326
carrier: two-mode bosons with total occupation at most N plus finite neutral memory and Markov pilot loss LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert norm, no-jump contraction and full-instrument trace distance ON=declared_carrier
real_structure: complex adjoint with programmed controls
grading: total photon shell, sensing occupation and neutral record labels
action_owner: repository-construction -- supplied occupation-selective block Hamiltonian and protected reference, not a microscopic Kerr readout
target: finite coherent transfer, late loss flag, discrete phase measurement and priced neutral reset MAP-TYPE=evaluation
```

## What is now constructed

[K2324](k2324-kerr-selective-lossy-control-2026-10-30.md) granted a finite-duration neutral readout W. Here an explicit block Hamiltonian transfers the phase-bearing state to a neutral register while moving every surviving photon into the protected reference. A diagonal pretilt exactly removes known no-jump attenuation. A finite-time loss flag can then be read safely: the accepted branch is already loss-dark. Finite Fourier, classical-record and reset operations complete the declared instrument. The construction prices their norm, duration, memory and failed attempts.

The added readout controls are occupation-selective, multi-photon rank-block operations. They are NOT synthesized by the Kerr/beam-splitter alphabet. Consequently this is a conditional finite control-model construction and a precise compilation target, not experimental feasibility, locality, efficiency at huge N, or a complete microscopic apparatus. SC-META-53 remains UNCERTAIN and ledger0.263 unchanged. No native GU quantization or physical quotient is inferred.

## Explicit coherent transfer with pilot loss

Use pilot P and protected reference R, total number Q<=N, N>=1; the jump is sqrt(gamma)a_P, gamma>=0. Neutral register B has M=N+2 states, initially |0>. For n=1,...,N define orthogonal pairs

    A_n=|n,N-n> |0>_B,  B_n=|0,N> |n>_B,
    H_n=i hbar G (|B_n><A_n|-|A_n><B_n|).             (1)

Equation(1) is the transfer interaction-frame Hamiltonian. Persistent K2324 Kerr drift need not be discarded: let H0 A_n=hbar E_n A_n, H0 B_n=0, E_n=chi n(n-1)/2, and program the laboratory coupling as i hbar G sum_active[exp(+i E_n t)|B_n><A_n|-exp(-i E_n t)|A_n><B_n|], with H_lab=H0+that coupling. Its exact H0 interaction frame gives (1); the no-jump attenuation gamma n/2 commutes with H0; transformed jumps still lower Q and annihilate parked states. The full amplitude-damping dissipator is not asserted to be invariant under the nonlinear Kerr frame. The completed B_n has zero Kerr energy, so no free terminal correction is needed. Time is measured from readout start with the matching initial drive phase. The coupling norm is hbar G, while total lab norm is bounded by hbar[|chi|N(N-1)/2+G]. Programmed frequencies, phases and residual drift are priced control assumptions, and errors enter Delta H below. A_0=|0,N>|0> is untouched. Extend the transfer COUPLINGS as zero on lower total-number shells and the unused orthogonal complement. A retained Kerr drift may persist there; it preserves shell number and cannot create an accepting branch. All active blocks start together, each stops at its prescribed time; their sum has operator norm hbar G, not N hbar G, since blocks are orthogonal. This norm statement does not make implementation complexity constant.

Assume G>gamma N/4. Set d_n=gamma n/4, nu_n=sqrt(G²-d_n²), and

    tau_n=atan2(nu_n,d_n)/nu_n,
    r_n=exp(-d_n tau_n), r_0=1.                        (2)

In the ordered A_n,B_n pair the no-jump generator is [[-2d_n,-G],[G,0]]. Starting at A_n its exact coefficients are

    a_n(t)=e^(-d_n t)[cos(nu_n t)-(d_n/nu_n)sin(nu_n t)],
    b_n(t)=e^(-d_n t)(G/nu_n)sin(nu_n t).              (3)

At tau_n, cos=d_n/G, sin=nu_n/G, so a_n=0 and b_n=r_n. Switch that block off; B_n is pilot vacuum and loss-dark. With x=d_n/G, arccos(x)/sqrt(1-x²)<=pi/2 on [0,1), so

    T_read=max tau_n <= pi/(2G),
    r_n²>=exp[-gamma n pi/(4G)].                      (4)

For a direct inequality proof put x=cos(theta), 0<theta<=pi/2: concavity of sin gives sin(theta)>=2theta/pi. Equality at gamma=0 is harmless. The strict G bound is sufficient for the chosen oscillatory construction; no all-control necessity claim is made.

A jump from any active A_n goes to Q=N-1 and B=0; subsequent transfer couplings vanish there; a diagonal Kerr drift preserves that lower shell. Further losses may occur but Q never returns to N. On every no-jump N-shell input, including an arbitrary preparation-error vector, the map is exactly

    sum x_n A_n -> |0,N> sum r_n x_n |n>_B.             (5)

Thus preparation approximation does not leave pilot residual after exact transfer.

## Pretilt, finite sensing, and complete acceptance costs

Let c_n=sqrt[2/(N+2)]sin[pi(n+1)/(N+2)] be the sine target from [K2312](k2312-relational-finite-calibration-2026-10-30.md). The query phase is exp(-2in phi). A known pilot-loss interval T_q>=0 before readout, including sensing/storage, is allowed; its Hamiltonian is diagonal and commutes with n. No unknown phase continues through the transfer unless separately budgeted.

Prepare the normalized positive target

    b_n=c_n exp(gamma n T_q/2)/(r_n Z),
    Z²=sum c_n² exp(gamma n T_q)/r_n².                 (6)

The query/storage no-jump attenuation and (5) then give exactly

    |0,N> sum c_n e^(-2in phi)|n>_B / Z.               (7)

Known diagonal query/storage phases must also be precompensated: if they accumulate theta_n (including E_n T_q for persistent Kerr), prepare z_n=b_n exp(+i theta_n) using K2324's programmed target phases. Equation(6) specifies the positive magnitudes; equation(7) assumes this compensation or zero known phase. Unknown extra diagonal phases are not canceled by commutation alone. Both the unknown query phase and pretilt are diagonal, so (6) is independent of phi. K2322's backward compiler prepares any positive b, not just c, with the same duration/exposure upper bound. With J>gamma/4 and q(a)=(pi/2+arcsin a)/sqrt(1-a²), a=gamma/(4J), ideal preparation survival p_p obeys

    p_p>=exp[-gamma N² q(a)/(2J)],
    p_0=p_p/Z² >= exp[-gamma(N²q(a)/(2J)+N T_q+Npi/(4G))]. (8)

[K2324](k2324-kerr-selective-lossy-control-2026-10-30.md)'s Kerr approximation for that pretilted preparation has raw no-jump error eta bounded by its same norm estimate (target phases are programmed as there). Contractions through the query and transfer give raw error<=eta. Write A=sqrt(p_p). If d=eta Z/A<1, actual accepted probability and conditional trace distance satisfy

    p_actual >= (A/Z-eta)²=p_0(1-d)²,
    D(conditional neutral state, ideal phase state)<=d. (9)

This is the elementary distance from a vector to a target ray: its orthogonal component is at most eta, with the sharper normalized angle bound eta/(A/Z). The exact transfer still parks all surviving charge even for this preparation error. Lost branches stay below N and will be rejected.

An explicit sufficient total-survival design chooses positive allocations L_p,L_q,L_r with L_p+L_q+L_r=L, and enforces gamma N² q(a)/(2J)<=L_p, gamma N T_q<=L_q, gamma Npi/(4G)<=L_r, together with a<1 and G>gamma N/4. Then p_0>=e^-L. To obtain d<=epsilon<1 it suffices that K2324's C(a)JN/|chi|<=epsilon e^(-L/2). These simultaneous inequalities expose the preparation quadratic and readout linear occupation costs. They do not assert that physical chi,gamma,J,G can be chosen independently or that the readout blocks can be manufactured.

## Finite flag and finite phase instrument

After (5), couple a neutral flag f initially |0> with

    H_f=hbar g_f Pi_Q=N tensor X_f,
    T_f=pi/(2g_f), g_f>0.                             (10)

The N-shell branch is now loss-dark, so (10) flips its flag exactly. A lower-shell branch never enters N, so its flag remains0 even if further photons are lost during this pulse. There is no ideal instantaneous shell test. A flag BEFORE transfer would miss losses; a flag begun while the accepted branch still has pilot population can also produce false accepts after a late jump. Exact parking is essential to this construction.

Conditional on f=1 apply F_M with entries (F_M)jn=M^-1/2 exp(2pi i jn/M) to B. It is a finite neutral unitary. Since F_M^4=I, its eigenprojectors are P_lambda=(1/4)sum_l=0^3 lambda^-l F_M^l for lambda in {1,-1,i,-i}. For any prescribed T_F>0,

    H_F=-(hbar/T_F)sum_lambda Arg(lambda)P_lambda,
    exp(-i H_F T_F/hbar)=F_M, ||H_F||<=pi hbar/T_F.    (11)

Zero eigenspaces may be omitted. This is a spectral-log Hamiltonian construction, not a local gate synthesis. Neither it nor subsequent neutral operations adds pilot loss on successful branches. Copy B's label j coherently to a fresh M-state neutral environment by controlled modular addition and trace that environment. A Hermitian logarithm of this finite unitary gives a finite pulse with norm<=pi hbar/T_copy. The resulting classical record realizes

    p_j=|sum c_n exp[-2in(phi-pi j/M)]|²/M.             (12)

The successful charged state remains |0,N>, independent of j. Since M=N+2>N+1, sums with |n-m|<=N and |n-m+-1|<=N+1 have no nonzero alias. Hence for EVERY phi the circular loss is

    E[4 sin²(phi-pi Jrecord/M)]
       =2[1-cos(pi/(N+2))].                           (13)

M=N+1 normalizes probabilities but can alias this loss: N=1,M=2 yields 1-cos(4phi). No continuous random offset or infinite-precision fresh randomness has been introduced to repair that error.

Bounded classical risk and the retained-pump bounds of K2312 now compose with (9). For its N=3e27 example, ideal conditional good probability is at least43/45. With conditional distance d, joint acceptance-and-good probability is at least p_0(1-d)² max(0,43/45-d). Unconditional charged renewal cost per accepted run is at most N/[p_0(1-d)²] when each attempt is restocked with at most N fresh photons; The corresponding long-run frequency of accepted-and-good outcomes has the further factor, but true-good depends on unknown phi and is not an observable stopping rule or heralded retry guarantee. This is a supplied retry/restock model with independent identical attempts and known parameters, not free recycling of failures. Counts are photons; physical energy requires frequency. The working output versus actual record marginal uses K2312's conservative2d allowance when quantum/classical correlations are retained.

## Neutral reset, clocks and genuine failure branches

A reset of a d_R-dimensional neutral record R uses a fresh blank C of that dimension and the actual SWAP S_RC:

    H_swap=pi hbar(I-S_RC)/(2T_s),
    exp(-i H_swap T_s/hbar)=S_RC, ||H_swap||=pi hbar/T_s. (14)

It sends rho_R tensor |0><0|_C to |0><0|_R tensor rho_C, preserving correlations with all other systems. Reset transfers entropy and consumes fresh memory; it is not a cyclic erasure. Flag plus M record admits d_R=2M. One may encode a canonical failure and M success outcomes using M+1 states, but compression needs its own unitary and no saving is assumed. Universal reversible storage for Ruses arbitrary records of dimension d_R requires d_R^Ruses reservoir dimension by injectivity. Under a uniform phase prior, ideal successful j is uniform; classical record entropy is h2(p_0)+p_0 log M if failure is canonical. These are information/stock costs, not a Landauer heat bound without a specified thermal reservoir and Hamiltonian spectrum. Charged replacement after failure is separate.

For a claim about corrected working output, explicitly inherit K2312's supplied record-controlled inverse actuator. At actuator rate Omega its T_c=pi/Omega and state-specific angle-error allowance are additional resources; no microscopic implementation is supplied here. All durations T_q,T_read,T_f,T_F,T_copy,T_s,T_c are explicit and serially summed with preparation when pricing latency (T_c only when that correction is used). The N independently programmed switch times are a control burden. If block n switches at tau_n+delta instead, (3) gives

    a_n=-e^[-d_n(tau_n+delta)] (G/nu_n)sin(nu_n delta),
    b_n=e^[-d_n(tau_n+delta)][cos(nu_n delta)+(d_n/nu_n)sin(nu_n delta)]. (15)

Thus pilot residual generically returns; perfect heralding is no longer justified. Compare instead the FULL trace-preserving instruments, including failed/false-accepted records. With hard Q<=N, integrated generator perturbations give the ancilla-stable trace-distance bound

    epsilon_inst <= D_input + integral (||Delta H||/hbar+N|Delta gamma|)dt. (16)

D_input is full-input trace distance, not automatically eta or the conditional d in (9). The hard Q<=N bound covers the calibration apparatus, not an unbounded-charge retained working pump. Exact controlled working correction may be appended by contraction; a noisy working actuator needs K2312's state-specific 2sqrt(mu)|u| bound or a separately supplied hard cutoff, because its operator-norm mismatch can be infinite. The Hamiltonian commutator has induced trace norm<=2||Delta H||/hbar and the dissipator of a_P has norm<=2N; the factor1/2 in trace distance gives (16), using contractivity and Duhamel. Switch-time error contributes at most G sum_n |delta tau_n|. Fourier/flag/copy/reset errors and any continuing unknown phase enter their own integrated terms. A constant mismatch in rates must be integrated over the actual finite cycle, not omitted after declaring a dark ideal branch. Equation(16) controls event probabilities and bounded loss on ALL outcomes, so joint good success is at least p_0*43/45-epsilon_inst for comparison with the exact ideal full instrument. It does not promise a loss-free flag after timing error; a generic quantum-output/actual-record comparison again permits2epsilon_inst.

## Evidence and remaining physical step

Exact controls derive the block generator solution, endpoint, attenuation pretilt, Fourier identities, flag/late-jump behavior, reset unitary and timing residual. Finite high-precision controls check multi-block transfer on actual matrices; they are not universal proof certificates. Uniform bounds and all-N statements use the written arguments. The endpoint supplies a concrete neutral readout and cost model in a stronger control alphabet than Kerr preparation, avoiding an arbitrary W while openly pricing that additional assumption.

Next compile (1), (10), and the neutral Fourier/copy/reset gates from a declared microscopic spatial alphabet with actual rate/clock/noise relations, or prove an obstruction for that alphabet. The operator norm G does not price spatial complexity, many-body selectivity, reservoir purity or reference protection. Those remaining physical objects, not another abstract unitary-extension theorem, decide feasibility. Source, ledger, canon and public physics posture remain unchanged.
