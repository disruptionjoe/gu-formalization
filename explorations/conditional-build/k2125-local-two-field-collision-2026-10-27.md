---
title: "K2125: Causal two-field contact readout and its energy cost"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source selection, physical GU quotient, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2125_local_two_field_collision_probe.py
---

# K2125: Causal two-field contact readout and its energy cost

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
carrier: empty Fock over three L2 line species R,L0,L1; finite-mode code only for readout LAYER=toy CHIRALITY=N/A
pairing: ordinary positive Fock metric and local graded Fock von Neumann algebras ON=declared_carrier
real_structure: complex Hilbert adjoint; no source-selected physical reality
grading: CAR parity; probe starts with fixed one-particle parity; transport direction is not source or four-dimensional chirality
action_owner: repository-construction -- unitary-conjugated chiral transport with contact transmission domain
target: conditional dynamics and operational compatibility MAP-TYPE=intertwiner
```

## Result and prior boundary

There is an exact selfadjoint continuum contact apparatus whose COMPLETE
field-and-probe local observable algebra propagates causally, and which performs
coherence-preserving parity readout after compact packets cross. It is not a
stable massive apparatus: its energy spectrum is unbounded below, and generic
midcollision states have infinite absolute free energy. This sharp distinction
replaces the acausal regional-smearing construction of
[K2122](k2122-regional-quartic-readout-2026-10-27.md) with an actual local-net
model at an explicit ultraviolet price.

[K2104](k2104-point-contact-parity-transport-2026-10-26.md) already constructs
point-contact transport with static finite registers and leaves arbitrary
apparatus-intervention locality open. Here BOTH system and interacting probe
are second-quantized travelling fields; the inactive probe rail is included
in the local algebra as well. This is not the finite static-register model.
[K2121](k2121-adaptive-gaussian-parity-2026-10-27.md)'s Gaussian floor is respected:
the contact phase is a nonGaussian controlled number interaction.

The abstract role of local dynamical probe couplings is established in
[Fewster and Verch, Quantum fields and local measurements](https://arxiv.org/abs/1810.06512).
That framework does not certify this empty-Fock contact model, its energy
condition or this particular instrument. Known fermionic controlled phases
also occur in [Bravyi and Kitaev, Fermionic quantum computation](https://arxiv.org/abs/quant-ph/0003137).
No novelty claim is made; the construction and limitations below are explicit.

## 1. Define the operator by its domain

Let h=L2(R)_R direct-sum L2(R)_L0 direct-sum L2(R)_L1 and F=Gamma_-(h).
Right movers have velocity v>0, both left rails velocity -v. On each finite
particle sector set

    H0=-iv sum_i partial_xi + iv sum_j partial_yj
                              +iv sum_k partial_zk,
    Gtheta=exp[-i theta sum_(i,j) 1{x_i>y_j}],
    Htheta=Gtheta H0 Gtheta*,  D(Htheta)=Gtheta D(H0).             (1)

Here x labels R, y labels L1, z labels L0. The free operator is the
selfadjoint Fourier multiplier v(sum p_x-sum p_y-sum p_z); its sector domain
is the corresponding directional Sobolev domain, NOT full H1 in all particle
coordinates. The Fock operator is the direct sum with the usual square-sum
graph-domain condition. Gtheta is unitary on this direct sum, separately
symmetric in each species' coordinates, and thus respects CAR antisymmetry.
Equation(1) defines a selfadjoint operator without multiplying distributions.
On functions with sufficient transverse regularity its trace condition across
one crossing face is psi(r=0+)=exp(-i theta)psi(r=0-), r=x_i-y_j.
Commuting phase factors resolve simultaneous crossings consistently. The
formal density2v theta n_R(x)n_L1(x) is only a mnemonic; no unrenormalized
quartic operator distribution is asserted to exist.

Write T(t)=exp(-itH0). Exactly,

    Utheta(t)=Gtheta T(t) Gtheta*,
    (T(t)psi)(x,y,z)=psi(x-vt,y+vt,z+vt).                         (2)

At final coordinates and t>=0, the phase in(2) is
exp[-i theta sum 1{0<x_i-y_j<2vt}]. At endpoints of the intervals any
convention agrees almost everywhere. For general signed t the exponent is
the difference of step functions at r and r-2vt. This difference, including
the INITIAL Gtheta*, proves the exact cocycle and U(-t)=U(t)*.
Gtheta is a mathematical conjugacy, not an instantaneous physical gate
applied across the line at preparation.

## 2. Full local algebra, not only packet velocity

Let A(I) be the von Neumann algebra generated by the smeared CAR fields of
ALL three species supported in bounded interval I, in this empty-Fock
representation. Use the spatial graded Fock factorization. For t>=0 the
Heisenberg fields have the following shorthand:

    alpha_t(psi_R(x))
       =exp[-i theta N_L1((x-vt,x+vt))] psi_R(x-vt),
    alpha_t(psi_L1(x))
       =exp[-i theta N_R((x-vt,x+vt))] psi_L1(x+vt),              (3)
    alpha_t(psi_L0(x))=psi_L0(x+vt).

These are identities of smeared BOUNDED annihilation operators, justified
as follows. On finite-particle wavefunctions insert(2), remove the indicated
coordinate, and cancel phases from every unchanged pair. An R removal
at initial a=x-vt leaves precisely the phase from L1 coordinates in
(a,a+2vt); an L1 removal leaves the corresponding R interval. Other species
and noncrossed pairs cancel. Smear with f(x). The resulting bounded operator
has norm||f|| by unitary conjugation; the finite-sector equality extends to
the whole Fock space. Number-string unitaries are spectral functions of the
local number operator and belong to the local Fock von Neumann algebra.
No norm-quasilocal CAR C*-algebra assertion is inferred from this fact.
For the two interacting species, the membership conditions
 y+vt in (x-vt,x+vt) and x-vt in (y-vt,y+vt) are equivalent.
Thus the two equal negative string phases preserve mixed CAR; reversing
only one species phase would fail. The finite probe checks the complex
quarter-turn strings and the outgoing probe rail coherence.

All participating coordinates in(3) lie in I expanded by vt. Spatial graded
factorization proves these smeared operators act only in that expanded
factor. Normality of conjugation extends from the generators to

    alpha_t(A(I)) subset A(I expanded by v|t|).                  (4)

The signed-time version follows the same phase cancellation with reversed
interval orientation. Even observables of disjoint local factors commute.
Thus for even B whose backward cone misses intervention region J, and a
local normal trace-preserving instrument with Kraus Knu in A(J),

    sum_nu Knu* alpha_t(B) Knu=alpha_t(B).                       (5)

For infinite Kraus sums use strong convergence of sum Knu*Knu=I. Initial
correlations are arbitrary; the identity holds at the observable level.
Parity-compatible local instruments can have odd individual Kraus operators:
the disjoint EVEN alpha_t(B) still commutes with them. Equations(4),(5)
include probe rail coherence and arbitrary local apparatus interventions,
not merely the propagation of one prepared packet. Composition gives causal
ordered interventions. No negative-energy assumption has been removed.

## 3. Complete recorded parity after full crossing

Choose d orthonormal smooth compact R modes f_j with joint support in a bounded
interval left of the smooth compact probe mode g. Prepare arbitrary code state
on Gamma_-(span{f_j}), possibly correlated with an external reference, with all
other field modes empty. Prepare one probe particle in (L0(g)+L1(g))/sqrt2.
Choose t so every system/probe support pair has fully crossed. In the freely
translated output modes the exact interaction is

    exp[-i theta N_R N_L1].                                    (6)

At theta=pi, outgoing local rail measurement in the +/- basis has Kraus
operators P_even=(I+(-1)^N_R)/2 and P_odd=(I-(-1)^N_R)/2, up to an irrelevant
branch phase. Therefore the complete recorded channel is

    rho -> sum_(b=even,odd) |b><b| tensor P_b rho P_b.             (7)

This is valid on every code matrix unit and arbitrary external references.
It preserves coherence within each parity sector. Readout is local in the
outgoing probe region after the full crossing time, and is a separately
supplied local instrument allowed by the net; no separate dynamical model
of the final classical recording device is claimed.

A spectator particle crossed by L1 also contributes to N_R. Unknown spectator
states therefore cannot be silently left unchanged while reading only the
chosen modes. Vacuum spectators and complete crossing are real hypotheses.
For incomplete crossing, spatially distinct components can acquire different
phases and entangle with packet position, preventing exact(7).

For a phase error theta=pi+delta on a code with at most d particles, the two
Stinespring isometries differ in norm by at most

    min(sqrt2, d |delta|/sqrt2).

Indeed only the L1 rail changes and |exp(-i n delta)-1|<=n|delta|.
Applying the same local readout and tracing the probe cannot increase channel
distance, giving the safe recorded half-diamond bound
min(1,d|delta|/sqrt2). This is a finite-code bound, not uniform on all Fock space.
Incomplete-support tails require their own preparation estimate; the contact
phase bound alone does not control them.

## 4. Selfadjoint and causal does not mean finite energy

Htheta is unitarily equivalent to H0. Already the one-R sector has spectrum R,
so Htheta is not semibounded and its empty Fock vacuum is not a ground state.
No massive polarized Dirac sea or positive-energy capture theorem is imported.

There is a sharper obstruction than this spectral observation. In the one-R,
one-L1 sector put r=x-y and s=(x+y)/2. H0=-2iv partial_r, so
|H0|=2v|p_r|. Take smooth compact incoming data supported in r<0, nonzero on
a later crossing slice r=-2vt. Initial Gtheta*=I there. During collision,
(2) has a jump of size(exp(-i theta)-1) times a nonzero smooth transverse
amplitude across r=0 whenever theta is not in2pi Z. On a transverse set of
positive measure the fractional H1/2 seminorm includes a positive multiple of

    integral_0^epsilon integral_0^epsilon (a+b)^(-2) da db = infinity.

One can restrict to b comparable with a to obtain integral da/a. Hence the
state is outside the form domain of |H0| and has infinite absolute free energy.
This is an analytic discontinuity result, not a finite Fourier truncation.
The positive free proxy dGamma(v|p|) dominates |H0| by the triangle inequality
of the commuting momenta and also diverges. Yet the state remains in D(Htheta)
when the initial incoming data are in that domain, because its jump satisfies
the interacting transmission condition. Conservation of interacting Htheta
cannot be substituted for a finite free-energy preparation/controller budget.

Fully separated initial and final compact smooth packets can both have finite
free energy, and(7) remains exact. This does NOT make the intermediate energy
finite. A smooth finite-range replacement may remove the jump but changes the
strict point-contact model and must reprove locality and finite-code error.
A stable massive nonlinear field coupling with a controlled ultraviolet limit
remains the strongest missing interface. K2115's massive smooth capture and
K2122's bounded regional energy cannot compose with this result by relabeling
fields or domains.


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
