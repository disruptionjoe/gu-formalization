---
title: "K2123: Native potentials on the same positive current"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source selection, physical GU quotient, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2123_same_current_potential_dynamics_probe.py
---

# K2123: Native potentials on the same positive current

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
result: conditional exact construction with explicit domain and inference limits
carrier: K2120 complex32 inside actual K1951 complex128 and K2021 full1920 LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: S=i Jc transpose H D0 Jc compressed to cI with c=9/280 ON=declared_carrier
real_structure: complex Hilbert adjoint; no source-selected physical reality
grading: Clifford labels, current sign and CAR parity are separate
action_owner: repository-construction -- K2028 raw connection class and K1967 mass, restricted by K2120
target: conditional dynamics and operational compatibility MAP-TYPE=intertwiner
```

## Result and distinction from prior work

The thirteen-real-dimensional class of complex raw coefficients of
[K2028](k2028-all-grade-raw-common-form-2026-10-24.md) preserves EVERY constant
positive32 projector constructed in [K2120](k2120-inherited-core-current-2026-10-27.md).
Together with the fixed K1967 mass it gives a common-domain Dirac evolution
conserving the SAME inherited current, with nonflat bounded potentials allowed.
This closes a compatibility seam between two existing actual constructions;
it does not repeat K2028's classification or K2120's maximality theorem.
K2034's supplied positive form is a different object. Full1920 mass-adjoint
failure is unchanged: a restriction does not repair the full operator.

## 1. Pin the actual image, not a similarly sized model

Use K2120's actual rational injection Jc and current F, principal Cj, mass M,
and involutions T,Z,R. Put t=iT, c=9/280, S=iF and

    Ptheta=(I+t)(I+cos(theta)R+sin(theta)iZR)/4.

K2120 proves rank Ptheta=32, [Ptheta,Cj]=[Ptheta,M]=0 and
Ptheta S Ptheta=c Ptheta. It does NOT prove [Ptheta,S]=0, which is false.
Compressing a current and commuting with a current are different operations.

K2028 stores thirteen real induced matrices A_l in the ORIGINAL Jc coordinates,
with imaginary coefficient i A_l. Its indices0,1,11,10 have respectively
(2/3)I,(2/3)C1,(2/3)C2,(2/3)C3; nine others vanish. Consequently the fixed
right inverse with weights3/2 on those four indices lifts arbitrary real
functions a_mu to its exact raw coefficient class. The associated upper and
lower return identities are inherited from K2028's complete raw replay.
This probe replays all thirteen stored induced images and original-coordinate
principal matrices; it does not rerun or newly certify the large raw rank proof.

The equation, on Wtheta=ran Ptheta, is

    E_a phi = (partial_t + Cj partial_j + mu M
                         + i(a0 I + Cj aj))phi = 0,              (1)
    H_a = -i Cj partial_j - i mu M + a0 I + Cj aj.                (2)

Here mu is a fixed real constant, summation is over three spatial indices,
and a_mu are real. The mass is separately supplied K1967 data; K2028's raw
image contains no isotropic mass. Do not attribute this composed mass to it.
Every multiplication and derivative term preserves the constant Wtheta.
On Wtheta, Cj are Hermitian, M is skew-Hermitian, and {Cj,M}=0.
Thus (2) is Hermitian on its declared test domain.

## 2. Same-current conservation and finite speed

For smooth Wtheta-valued solutions define rho=phi* S phi and j_j=phi* S Cj phi.
Because Cj preserves Wtheta,

    rho=c ||phi||²,   j_j=c phi* Cj phi,
    partial_t rho + partial_j j_j=0.                             (3)

This follows directly from (1): derivative terms give the divergence;
the compressed skew mass and imaginary Hermitian potential cancel.
The mass need not conserve S on the whole128 space. One must compress BEFORE
making the conservation inference. For unit n, (C.n)²=I, so |j.n|<=rho.
Integrating (3) over an exterior region whose boundary expands at speed1
shows zero initial exterior density remains zero. Equivalently apply a smooth
Lipschitz cutoff approximating that region, then pass by monotone convergence.
Compact initial support expands by at most |t|. Density of smooth data extends
the support statement to L2 inputs. This is a one-particle finite-speed result;
no interacting source quantum field follows merely by naming a CAR functor.

## 3. Common domain, curvature and gauge

On R3 the free symbol C.k-i mu M squares to (|k|²+mu²)I. Fourier multiplication
therefore defines a selfadjoint operator on H1(R3,Wtheta). Bounded real STATIC
a_mu give a bounded selfadjoint multiplication perturbation. The resolvent
Neumann-series proof of the bounded perturbation theorem gives selfadjointness
on the same H1 domain; its unitary group preserves that domain by spectral
calculus. A norm bound is ||a0||_infinity+|| |a| ||_infinity.

For time dependence a sufficient class is C1 in t with values W1,infinity in x,
bounded on each finite time interval. The interaction-picture Dyson series
converges in L2 operator norm. Commuting each spatial derivative through the
equation bounds H1 growth by Gronwall using bounded spatial derivatives of
the potential; approximation by smooth data gives a common-H1 unitary
propagator and (3). This does not assert domain preservation for arbitrary
measurable time-dependent bounded potentials.

A nonflat bounded example is a2=b sin(x1), with all other a_mu zero:
f12=b cos(x1). Unlike a2=b x1 it falls directly under the bounded theorem.
The scalar gauge transformation phi'=exp(i chi)phi, a'_mu=a_mu-partial_mu chi
preserves (1), current and curvature f_mu,nu. For the H1 assertion require
bounded spatial derivatives of chi and the transformed potential hypotheses.
A local gauge identity does not remove nonzero curvature or global holonomy.

This constructs conservative propagation on an invariant selected sector with
external potential coefficients. Selection of Ptheta, source reality, charge,
quantization, dynamics of a_mu and source-owned interacting positivity remain open.


## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 and SC-META-53 are
UNCERTAIN; SC-META-56 DISAVOWS an odd-action prerequisite. Their polarity and
adherence remain unchanged. LT-SM8/LT-GR6b and ledger0.263 remain unchanged:
these conditional constructions are neither source-selected interacting physical
quotients nor recovered GU physics. Native2+1, total/observed chirality,
full20, K/C, mirror/full-II and normal jets remain distinct debts.

Exact finite probes and genuine input faults test the displayed identities.
Universal domain, causal and global claims rest on the written arguments and
independent internal specialist review, not the finite checks. No external
expert, proof-assistant or novelty certification is claimed.
