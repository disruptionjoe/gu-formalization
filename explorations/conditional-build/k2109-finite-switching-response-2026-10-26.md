---
title: "K2109: Finite switching, vacuum noise and one-particle response"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional imported positive-Hilbert detector mathematics; no GU recovery or apparatus certification
scripts:
  - tests/channel-swings/k2109_finite_switching_response_probe.py
---

# K2109: Finite switching, vacuum noise and one-particle response

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: conditional detector bounds and constructions with explicit locality and approximation assumptions
carrier: free real massive scalar Fock space in 3+1 Minkowski and a two-level probe LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product ON=declared_positive_Hilbert_space
real_structure: complex adjoint; no source-selected real form
grading: ordinary observable algebra; no source grading identified
action_owner: repository-construction -- declared pointlike inertial scalar coupling at leading perturbative order
target: vacuum excitation and one-particle absorption budget MAP-TYPE=evaluation
```

[Conditional mathematics accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Source and inference boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 and SC-META-53 are
UNCERTAIN; SC-META-56 DISAVOWS a mandatory odd-action prerequisite. The
positive Hilbert spaces, local algebras, vacuum and dynamics here are imported,
not selected by equation9.16. K2021 local R0/R1 already exists; source-selected
observation and physical domain remain open. LT-SM8/LT-GR6b, source register,
ledger0.263 and canon are unchanged. Native2+1, total/observed chirality,
full20 and K/C accessibility are separate obligations. No GU derivation,
novelty, external-expert or proof-assistant certification is claimed.

## 1. A pointlike switching model with a limited claim

Use hbar=c=1, real scalar mass m>0, gap Delta>0, inertial worldline x=0,
initial detector ground state and field vacuum. The formal interaction is
lambda chi(t)[sigma_+ exp(i Delta t)+sigma_- exp(-i Delta t)] phi(t,0),
with real nonzero chi in C_c^infinity(R). Normalize

    phi(t,0)=integral d³k [a(k)e^(-i omega_k t)+a*(k)e^(i omega_k t)]
                         /sqrt(2(2pi)³ omega_k),
    omega_k=sqrt(|k|²+m²), [a(k),a*(q)]=delta³(k-q),
    chihat(s)=integral dt chi(t)e^(ist).

The squared first-order excitation amplitude is lambda² F_m(Delta), where

    F_m(Delta)=1/(4pi²) integral_m^infinity
              sqrt(omega²-m²)|chihat(Delta+omega)|² d omega.       (1)

The factor follows from4pi k²dk/[2(2pi)³omega], k dk=omega d omega.
This is a rigorous finite leading response coefficient. We do not construct
an exact pointlike interaction Hamiltonian or prove a uniform perturbation
remainder, full recorded instrument or all-coupling positivity. Standard
smooth-switching response context: [Louko–Satz](https://arxiv.org/abs/0710.5671)
and [Fewster–Juárez-Aubry–Louko](https://arxiv.org/abs/1605.01316).
No scalar-to-fermionic/GU transfer is implicit.

## 2. Compact switching cannot make this coefficient vanish

F is finite because chihat is Schwartz on R. It is strictly positive:
if F=0, the nonnegative continuous integrand makes chihat(Delta+omega)=0
for all omega>m. Compact support of chi makes chihat entire; the identity
theorem and injectivity of Fourier transformation then give chi=0, contrary
to assumption. A real massless scalar also has this statement with m=0
and Delta>0. This is an exact exclusion of zero leading vacuum response
for this model, not a universal nonzero numeric floor.

Zeros at finitely many frequencies are allowed. Existing [K90](k90-observed-detector-response-kms-wave-2026-09-01.md) discrete
one-mode cancellation controls are therefore unaffected: a continuum of
mass-shell frequencies is the essential new premise. Rotating-wave deletion
of the creation term sets this coefficient to zero by changing the model;
it is not a derivation that compact switching cancels the original term.

## 3. Explicit adiabatic suppression, with its signal limitation

For chi_T(t)=chi(t/T), T>0, let D_N=||chi^(N)||_1, integer N>=2.
Integration by parts gives |chihat(s)|<=D_N/|s|^N. Thus

    F_T <= D_N² T^(2-2N)/(4pi²) * J_N,
    J_N=(Delta+m)^(2-2N)/(2N-2)
             -Delta (Delta+m)^(1-2N)/(2N-1).                     (2)

Here sqrt(omega²-m²)<=omega bounds the remaining integral; integrating
omega/(Delta+omega)^(2N) gives J_N. Every N is available for fixed smooth
chi, so this coefficient decays faster than any inverse power of T. The
constants depend on N and chi. This is not an exponential bound, a finite-T
zero, a uniform family bound, or control of higher perturbative orders over
arbitrarily long interaction times. Increasing T increases localization time.

A noncompact exact normalization control is chi(t)=exp(-t²/(2T²)), m=0.
For z=T Delta,

    F_0=[exp(-z²)-sqrt(pi) z erfc(z)]/(4pi).                       (3)

It follows by inserting chihat(s)=sqrt(2pi)T exp(-T²s²/2) into(1).
The probe independently integrates the Gaussian and checks(3). This is not
the compact-support theorem's witness. A compact triangular switch is a
second elementary transform control: chi(t)=max(0,1-|t|/T), with
chihat(s)=2(1-cos(sT))/(T s²), continued to T at s=0. It has only finite
smoothness, so it does not inherit arbitrary-N decay.

## 4. Actual one-particle input and a uniform absolute error

Take |1_f>=a*(f)|0>, ||f||_L2(d³k)=1. Define

    u_f(t)=integral d³k f(k)e^(-i omega_k t)/sqrt(2(2pi)³omega_k),
    A_f=integral dt chi(t)e^(i Delta t) u_f(t),
    B_f=integral dt chi(t)e^(i Delta t) conjugate(u_f(t)).

The distributions are evaluated after time smearing; the resulting kernels
are L2 because chi is smooth. The annihilation part of the first-order field
operator produces A_f|0>. The creation part produces a two-particle vector,
whose squared norm is F_vac+|B_f|² by CCR. These orthogonal sectors give

    F_1=F_vac+|A_f|²+|B_f|²,
    |B_f|²<=F_vac,
    |A_f|²+F_vac <= F_1 <= |A_f|²+2F_vac.                        (4)

Cauchy–Schwarz proves the middle bound and it is uniform over normalized f,
even if f depends on T. Thus replacing the full leading coefficient by its
absorption contribution has absolute error at most2F_vac. This is neither
relative signal-to-noise control nor evidence that absorption stays nonzero.

For example an angular wavepacket with spherical harmonic l>0 is orthogonal
to both radial kernels at the origin, so A_f=B_f=0 and F_1=F_vac. If
Delta<m, no mass-shell absorption resonance omega=Delta exists. For the scaled switching chi_T write A_(f,T) and B_(f,T). For any
normalized f in the subthreshold case, integration by parts bounds

    |A_(f,T)|² <= D_N² T^(2-2N)/(4pi²)
          integral_m^infinity sqrt(omega²-m²)/(omega-Delta)^(2N) d omega. (5)

The integral is bounded above, with h=m-Delta>0, by
h^(2-2N)/(2N-2)+Delta h^(1-2N)/(2N-1). It is finite for N>=2 and Delta<m. Hence all leading signal and
noise vanish in this subthreshold adiabatic limit. A finite gap margin is
essential; equation(5) is not uniform as Delta approaches m. Above threshold,
a resonant wavepacket and a controlled perturbation remainder still need
construction before claiming an efficient capture interface.

## 5. Reproducibility and scope

The exact probe checks radial Jacobian, Gaussian and triangular transforms,
adaptive-time power, integrated tail constant, and the actual truncated-Fock
CCR one-particle formula. Mutants change normalization, sign, kernels and
bosonic creation amplitudes. Finite controls do not prove the continuum
identity theorem or all-time apparatus existence. A common spatially smeared
qubit would add a separate causality issue; it has not been substituted here.
