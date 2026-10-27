---
title: "K2130: Stable empty-vacuum transport obstruction and noisy local field response"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: application of standard spectral analyticity to a fixed model class; supplied free-field counterconstruction, no nonlinear parity apparatus or GU recovery
scripts:
  - tests/channel-swings/k2130_stable_empty_vacuum_locality_probe.py
---

# K2130: Stable empty-vacuum transport and a causal noisy alternative

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: conditional model-class obstruction and constructive countercontrol
carrier: positive Hilbert local net; empty CAR Fock for obstruction and massive scalar Fock for countercontrol LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product ON=declared_carrier
real_structure: operator adjoint and real scalar test functions
grading: CAR even detector; bosonic scalar alternative
action_owner: repository-construction -- autonomous semibounded group or supplied free massive scalar field
target: delayed local detection versus exact vacuum darkness MAP-TYPE=intertwiner
```

## 1. Decision and prior scope

No autonomous semibounded modification of K2125 can retain all of its stationary
empty vacuum, exact local-net cone, bounded local vacuum-dark particle detector,
and nonzero transport to a region initially disjoint from the preparation.
This is an application of the standard Hegerfeldt positive-operator theorem,
not a new theorem or an obstruction to stable relativistic QFT. It closes the
interacting model class, rather than only K2060's free one-particle projection.
K2127 smoothing fails exact locality and still has unbounded energy; K2128's
regulator convergence does not repair this conjunction.

A supplied massive scalar field below demonstrates the surviving alternative:
positive energy, finite-energy local preparation, a strictly causal change in
local detector probability, and nonzero vacuum baseline. It is a free field
with a supplied local instrument, not a nonlinear parity-measuring apparatus.

## 2. Spectral argument on the actual net assumptions

Let H be selfadjoint and bounded below, U(t)=exp(-itH), and let the normalized
vacuum obey H Omega=E0 Omega. Let A be bounded and localized in I, and let
0<=B<=I be an even local effect in J with B Omega=0. Assume dist(I,J)>0 and
alpha_t(B)=U(t)* B U(t) commutes with A whenever |t|<dist(I,J)/c. This follows
from the exact cone of the given local net; trajectories alone do not suffice.
No Gaussian, quadratic, number-conservation, or differentiability assumption
on A Omega is needed. Normalize psi=A Omega when nonzero.

For those early times, alpha_t(B) Omega=0 and hence

    <psi,alpha_t(B)psi>=0.

Writing H'=H-inf spectrum(H)>=0, the vector-valued function
B^(1/2) exp(-izH') psi is bounded and analytic for Im z<0 and continuous at
real z. Pair it with any fixed vector. Its boundary value vanishes on a real
open interval. Schwarz reflection across the zero interval and the identity
theorem imply it vanishes everywhere. Taking boundary limits gives

    <U(t)psi,B U(t)psi>=0 for EVERY real t.                  (1)

For the empty CAR Fock net choose B=n(g)=a*(g)a(g) for a normalized compact
mode g in J. It is a bounded even projection and B Omega=0. Every compact
local excitation A Omega is therefore undetectable by this mode at all times.
K2125 explicitly transports such excitations to J, so no proposed stabilization
can preserve all the stated premises. A common energy offset changes nothing.
Nonlinear interactions do not bypass the proof when the same premises hold.

This does not prove locality from spectral positivity. K2125 evades (1) by
spectrum R. A semibounded hopping Hamiltonian gives sin^2(gt) arrival probability
at arbitrarily small t and evades the exact cone. A stationary polarized vacuum
can have no nonzero bounded local dark effect and evades B Omega=0. Arbitrary
externally time-dependent H(t) lacks the single analytic group used here; an
autonomous clock/controller would need the assumptions proved anew.

Primary source: [Hegerfeldt, sections 2--4](https://arxiv.org/html/quant-ph/9806036v1).
The proof here is the local-net application, not a new analytic uniqueness claim.

## 3. Stable causal counterconstruction with an explicit baseline

In one spatial dimension fix m>0, omega=sqrt(-d_x^2+m^2), H=dGamma(omega),
and scalar vacuum Omega. Use real f,g in C_c^infinity with separated supports
I,J, and the standard field normalization

    phi(f)=(a(omega^(-1/2)f)+a*(omega^(-1/2)f))/sqrt(2),
    W(f)=exp(i phi(f)).

The local preparation W(f) Omega is normalized and has finite energy
||f||_2^2/2. Define the supplied bounded local Kraus operators

    K_plus=(I+W(g))/2,  K_minus=(I-W(g))/2.

Their squared norms sum to I; E_minus=(I-Re W(g))/2 is a valid local effect.
Write

    sigma(t)=<f, sin(omega t) omega^(-1) g>,
    r=exp(-||omega^(-1/2)g||^2/4),
    p0=(1-r)/2,
    pf(t)=(1-r cos(sigma(t)))/2,
    pf(t)-p0=r(1-cos(sigma(t)))/2.                         (2)

These follow from the Weyl commutator and vacuum characteristic functional.
For nonzero g, 0<r<1, so the absolute detector probability has no dark interval.
Finite propagation of the Klein--Gordon Cauchy problem makes sigma(t)=0 for
|t|<dist(I,J), giving an EXACT causal response difference.

This difference is provably nonzero later. The one-dimensional sine kernel is
(1/2) J0(m sqrt(t^2-(x-y)^2)) inside |x-y|<t and zero outside. Choose nonnegative
smooth f,g with integral1 supported in intervals of radius a=1/(32m), centered
at0 and L=1/(4m). For |t|<3/(16m), sigma=0. At t*=1/(2m), all pairs lie strictly
inside the cone and the Bessel argument is at most1/2. The alternating series
for J0 gives 15/16<=J0(z)<=1 on[0,1/2], so

    15/32 <= sigma(t*) <= 1/2, hence pf(t*)-p0>0.            (2a)

The kernel is the Klein--Gordon fundamental solution, fixed by its Cauchy data
and Bessel equation, not a positive-frequency compact particle wavefunction.
Standard field conventions: [Fewster--Rejzner](https://arxiv.org/abs/1904.04051).

The unread local channel is (rho+W(g)rho W(g)*)/2. On vacuum its injected mean
energy is ||g||_2^2/4. Smooth smearing makes preparation and these branches
finite-energy; this is not the total work of a recording device. The Kraus
instrument remains supplied. The scalar carrier changes the empty-CAR local
factorization; it is an explicit conditional alternative, not a repair with
unchanged premises or a source-selected GU model.

## 4. Correct detector target and finite-code consequence

For local normal trace-preserving preparations with bounded local Kraus operators
in I and an even local
effect in J, locality keeps their two outcome probabilities identical outside
the cone. Local Kraus operators commute with the spacelike effect and their
adjoint products sum to I. This holds with correlated initial states. A
response difference is not a positive probability function and is not subject
to the zero-interval theorem (1). Equation (2) supplies the concrete example.

K2108 already owns separating-vacuum darkness and the scalar commutant bound.
Its useful finite-code corollary is as follows. For an isometry V:C^d->H choose
B'_j in M' approximating psi_j=Ve_j with sum_j||psi_j-B'_j Omega||^2<=delta^2;
put C^2=sum_j||B'_j||^2. For any E in M, 0<=E<=I, columnwise Cauchy--Schwarz gives

    ||E^(1/2)V|| <= C sqrt(<Omega,E Omega>)+delta.             (3)

Thus ||V* E V|| is bounded by the square of the right side (and by1), uniformly
over code states and arbitrary references. This is a corollary, not a separate
research arc or physical energy bound. It does not claim fixed C as the code,
region, approximation accuracy or target changes. K2110's growing-region
escape remains intact. The new construction must specify signal RELATIVE to
vacuum/background and its full recorded channel, not promise a universally
vacuum-dark local counter under the old empty-Fock premises.

## Acceptance and continuation

The probe checks exact finite matrix/Weyl identities and explicit countercontrols;
it cannot certify spectral analyticity, continuum causality or a full local net.
Those rest on the written proof and independent internal review. No novelty,
external-expert or proof-assistant certification is claimed. Next construct an
actual interacting polarized-vacuum controller with a full recorded instrument,
or derive a quantitative detector budget on its fixed code and local region.
A nonzero scalar response is not complete parity readout.

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 and SC-META-53 remain
UNCERTAIN; SC-META-56 DISAVOWS an odd-action prerequisite. LT-SM8/LT-GR6b,
ledger0.263, source register and canon are unchanged. All state, dynamics,
probability and instrument inputs above are supplied conditional mathematics.
