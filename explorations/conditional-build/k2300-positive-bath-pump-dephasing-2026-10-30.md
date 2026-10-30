---
title: "K2300 Positive finite bath and retained-pump dephasing"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite collective bath; no spatial-control or laboratory certification
scripts:
  - tests/channel-swings/k2300_positive_bath_pump_dephasing_probe.py
---

# K2300 Positive finite bath and retained-pump dephasing

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2300 Positive finite bath and retained-pump dephasing
carrier: complex field and retained pump Hilbert space with finite oscillator environment LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert pairing and half trace distance ON=declared_carrier
real_structure: Hilbert adjoint and real charge eigenvalues
grading: conserved Q=N_all+2K; no Clifford transfer
action_owner: repository-construction -- enlarged collective oscillator bath Hamiltonian
target: reduced complete recorded instrument retaining original pump MAP-TYPE=evaluation
```

## Result and assumptions

[K2296](k2296-stochastic-pump-drift-2026-10-30.md) supplied a Gaussian residual phase. A finite thermal oscillator environment derives that phase and its correlations, but also produces a coherent Q² phase. Semiboundedness requires accounting for a counterterm; ignoring its coherent effect can make a zero-noise prediction badly wrong. An explicit weak-coupling model meets the inherited full-instrument budget. Centering the coupling about the initial mean charge improves the sufficient bound but requires an additional calibrated force.

This is an ENLARGED apparatus model: the collective coupling QB and global Q² counterterm are not K2293's spatially local positive alphabet. It does not prove that the earlier local primitives synthesize this environment. It retains the same ideal field/record/pump target and its proven drift-free error delta<9.272e-12. Every actual circuit gate conserves Q and is independent of the bath. Fields start in vacuum; pump is coherent with mu=10^28, or displaced thermal with pump occupation n_P=1 and mu=4*10^28. The new bath is traced out; keeping it or its noise flag in the target changes the error problem. SC-META-53 remains UNCERTAIN; this supplied positive Hilbert model does not settle native GU positivity or ledger0.263.

## 1. Positive Hamiltonian and exact channel

For finitely many oscillators, omega_j>0, initial independent FREE Gibbs states with occupation n_Ej, take real g_j (a mode phase absorbs a complex phase), and

    H_E= sum_j omega_j b_j†b_j + Q sum_j g_j(b_j+b_j†)+c Q²,
    C=sum_j g_j²/omega_j, c>=C.

Completion gives H_E=sum omega_j(b_j†+g_j Q/omega_j)(b_j+g_j Q/omega_j)+(c-C)Q²>=0. Without cQ² and with C>0, shifted oscillator ground states have energy -Cq² on charge q, unbounded below. An arbitrary fixed linear charge term cannot repair that quadratic descent. A bounded-charge restriction is a different model.

On each finite total-charge sector the actual field/pump circuit is finite dimensional and commutes with H_E. The shifted oscillators are self-adjoint; their direct sum defines the positive Hamiltonian. Finite-charge truncation and the stated fourth moments justify the following unbounded-charge channel bounds. A free Gibbs initial state is not equilibrium of the coupled Hamiltonian.

At total duration T, tracing the bath multiplies charge matrix element q,q' by

    exp[-v(T)(q-q')²/2+i theta(T)(q²-q'²)],
    v=sum_j (2n_Ej+1) 4g_j² sin²(omega_j T/2)/omega_j²,
    theta=(C-c)T-sum_j g_j² sin(omega_j T)/omega_j².        (1)

For one sector, complete the square and use Weyl displacement composition. The bath displacement is q times g_j(e^(-i omega_j T)-1)/omega_j; its thermal characteristic function supplies v. The Weyl phase gives g_j²(omega_j T-sin omega_j T)/omega_j², and the explicit counterterm subtracts cT. Thus the reduced channel is Gaussian phase averaging followed by exp(i theta Q²). For c=C the linear-in-T term cancels but the sine term survives. The two maps commute and may be moved through the entire fixed Q-conserving circuit to its input.

## 2. Full retained-pump error and a concrete consumer

Let kappa_j be pump-number cumulants. The Gaussian part has K2296's upper bound 2v[kappa2+sqrt(kappa4+3kappa2²)]. Purifying the input, the deterministic phase obeys D<=|theta|sqrt(Var Q²)=4|theta|sqrt(Var K²). Hence

    D_full<=delta+2v[kappa2+sqrt(kappa4+3kappa2²)]
                    +4|theta|sqrt(Var K²).                 (2)

This is a state-specific full field/record/retained-pump bound, not an arbitrary-input diamond norm. For coherent pump, kappa2=kappa4=mu and Var K²=4mu³+6mu²+mu. For n_P=1, kappa2=3mu+2, kappa3=13mu+6, kappa4=75mu+26 and

    Var K²=12mu³+102mu²+203mu+66.

The raw Kerr sensitivity scales as mu^(3/2). Choosing a variance alone does not control it.

Concrete example: one mode, n_E=1 (beta omega=log2), lambda=|g|/omega=10^-29 and exactly c=C=omega lambda². Uniformly for all T,

    v<=12*10^-58, |theta|<=10^-58.

Exact rational square-root enclosures give both consumers D_full<9.284e-12<10^-11. The initial positive bath expectation is omega n_E+c E Q²: the excess is less than0.041omega coherent and0.641omega thermal. Bath occupation and pump occupation are separate inputs. The field number moments, field error<.008 and depletion12.8±.004 survive because both maps conserve number. These are consequences of specified coupling parameters, not evidence that such isolation or counterterm calibration is feasible. Arbitrarily long T is covered only for the EXACT c=C common finite bath; a mismatch contributes |c-C|T.

## 3. Covariance, revival and a failed variance-only criterion

For a bounded piecewise-continuous real envelope y(t) and integrable c(t), define F_j=integral_0^T y(t)exp(i omega_j t)dt. With c(t)>=C y(t)², the same displacement proof gives

    v=sum_j(2n_Ej+1)g_j²|F_j|²,
    theta=sum_j g_j² integral_{t>s} y(t)y(s)sin[omega_j(t-s)] ds dt
          -integral c(t)dt.

For segment filters F_ja, their phase covariance is Sigma_ab=sum(2n_Ej+1)g_j² Re(F_ja conjugate(F_jb)); total v=1^T Sigma1. It is not an iid approximation. Two consecutive half-periods of one mode have F2=-F1, so total v=0 while each separate segment has positive variance. System-only Q-conserving controls cannot change Q in a toggling frame. Externally changing y to +1 then -1 at a full period would instead give |F|=4/omega and destroy this revival; that actuator is not already supplied by those controls.

For c=C, a full one-mode period gives v=theta=0. Near it, T=2pi k/omega+tau, v<=(2n_E+1)g²tau² and |theta|<=g²|tau|/omega. Timing error and coupling/counterterm mismatch must both be priced.

Positivity alone does not fix c. Choose c=C+omega/16 and T=2pi/omega: v=0 but theta=-pi/8. For the identity-circuit coherent-pump control Q=2K, the gate is exp(-i pi K²/2). Even K get phase1 and odd K phase-i. Its exact overlap squared is (1+exp(-4mu))/2, so half trace distance is sqrt((1-exp(-4mu))/2), approaching1/sqrt2. This countercontrol refutes a universal variance-only guarantee; its pure-state equality is not asserted for the ten-call mixed recorded output.

## 4. Centered coupling is a priced repair

Replace Q in the entire bath Hamiltonian by R0=Q-q0, with q0=EQ of the initial field/pump state. Positivity and commutation remain. Gaussian dephasing is unchanged; the coherent gate is exp(i theta R0²), whose sufficient error is

    4|theta|sqrt(kappa4+2kappa2²).                           (3)

Indeed Var[(Q-EQ)²]=16(kappa4+2kappa2²). This reduces the mean-charge sensitivity. The initial excess bath expectation becomes4c kappa2. If the supplied center is q0+e, a further sufficient error is4|theta e|sqrt(kappa2). A center chosen from a measurement on the actual unknown input would need its own disturbance analysis; here it is fixed from the specified preparation.

With n_E=1, lambda=10^-22, c=C and exact centering, v<=1.2*10^-43, |theta|<=10^-44. Both full consumers obey D_full<9.358e-12. In the thermal case initial excess expectation is below4.801*10^-15omega. This small expectation conceals a strong balancing force: |g|q0≈8*10^6omega and c q0²≈6.4*10^13omega. Their generation, switching work, calibration and stability are unpriced. The expanded negative linear-Q term cannot silently be counted as one of K2293's positive local controls.

The bath gains free-oscillator energy ER0² sum omega_j |g_j(e^(-i omega_j T)-1)/omega_j|²; this is nonnegative and bounded by4omega lambda² ER0² for one mode. It is not the total switching work or an energetic-catalysis result.

## 5. A positive number bath avoids the quadratic counterterm

The counterterm requirement above belongs to LINEAR oscillator-displacement coupling. It is not a universal dephasing requirement. An independent repair is

    H_E=omega N_E+g Q N_E, omega>0, g>=0.

This positive diagonal cross-Kerr interaction needs no Q² term. A free thermal bath with geometric probability (1-r)r^n gives the exact charge channel

    chi(d)=(1-r)/(1-r exp(-i d gT)), d=q-q'.

This noise is non-Gaussian; K2296's Gaussian-specific lower bounds cannot be transplanted. For bath occupation n_E=1, r=1/2, phase mean m=gT and variance v=2(gT)². The same bath persists across waits, giving fully correlated increments. Its reduced number distribution is unchanged, although it becomes correlated with the circuit output.

For ANY centered phase with finite variance v, Taylor's integral remainder and unitary invariance imply

    D(E[exp(-i Phi Q)rho exp(i Phi Q)],rho)
      <=v/4 ||[Q,[Q,rho]]||_1.

The first derivative averages to zero. Finite fourth moment of Q justifies the trace-class remainder; it is the same upper bound used in K2296, without a Gaussian lower-bound claim. Separate the mean rotation. For the actual pump inputs,

    D_full<=delta+2sqrt(kappa2)|m|
              +2v[kappa2+sqrt(kappa4+3kappa2²)].             (6)

No mean-compensation gate or uncounted wait is assumed. At gT<=10^-28, both consumers obey D_full<9.342e-12. The initial interaction expectation is g EQ n_E, not g² EQ²/omega. This avoids the displaced bath's balancing force and counterterm, while demanding an extremely weak collective coupling for the full elapsed duration. It supplies neither spatial locality nor hardware isolation. Unbounded T at fixed nonzero g is not covered by this budget. A bath occupation eigenstate is a deterministic phase control, while a thermal mixture is not.

## Verification and next condition

Exact symbolic cumulants, displacement phases, covariance and rational consumer budgets are checked separately from finite truncated oscillator propagator controls. The universal direct-sum/channel argument is written above. Faults alter actual counterterm, charge multiplier, covariance, moment or centering formula. The positive bath is a concrete environment model, but spatial locality, physical calibration, switching and isolation remain independent construction requirements. No hardware, novelty, Lean or external-expert certification. Standard exactly solvable independent-boson background: [quantum heat statistics](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.2.020338); the finite model and bounds used here are explicitly derived.
