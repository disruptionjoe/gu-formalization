---
title: "K2127: Smooth two-field readout and the locality collar"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional empty-Fock model; no source selection, stable massive QFT, GU recovery, novelty or external certification
scripts:
  - tests/channel-swings/k2127_smooth_collision_locality_probe.py
---

# K2127: Smooth two-field readout and the locality collar

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
result: conditional exact dynamics and quantitative limits
carrier: empty Fock over counterpropagating L2 line species R,L0,L1 LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert Fock metric and spatial graded local von Neumann factors ON=declared_carrier
real_structure: complex adjoint; no GU-selected reality
grading: CAR parity; propagation direction is not physical chirality
action_owner: repository-construction -- smooth pairwise unitary conjugacy of free transport
target: full recorded instrument, locality and free-energy compatibility MAP-TYPE=intertwiner
```

## Result and prior boundary

Smoothing [K2125](k2125-local-two-field-collision-2026-10-27.md)'s actual two-field
contact interaction preserves exact completed parity readout and gives finite free
energy for compact smooth data in each finite-particle sector at fixed smoothing.
It loses strict speed-v locality, retains an unbounded-below spectrum, and is not
a stable massive apparatus. The exact signalling witness below prevents a finite
interaction range from being mistaken for a causal light cone.
K2104's static-register smoothing and K2122's regional quartic are different
objects. The new comparison keeps both travelling fields, domain and readout fixed.

## 1. Operator and exact propagator

Fix v>0, epsilon>0, theta real and a smooth monotone profile F with F=0 on
(-infinity,-1] and F=1 on [1,infinity). On a sector with R coordinates x,
active L1 coordinates y and inactive L0 coordinates z define

    G_e = exp[-i theta sum_ij F((x_i-y_j)/epsilon)],
    H_e = G_e H0 G_e*,       D(H_e)=G_e D(H0),
    H0 = -iv sum_i d_xi + iv sum_j d_yj + iv sum_k d_zk.          (1)

The free domain is the directional Fourier-multiplier domain, not full H1
in all coordinates. G_e is separately symmetric in each species and unitary.
Sectorwise the product rule gives

    H_e = H0 + (2v theta/epsilon) sum_ij F'((x_i-y_j)/epsilon).   (2)

This multiplier is bounded for each fixed particle sector, so (1) has the
same sector domain as H0. Full Fock selfadjointness follows by unitary conjugacy
and direct sum; the bound grows like n_R n_L1 and is not a bounded full-Fock
perturbation. The exact propagator is G_e T(t) G_e*, where at final coordinates
its phase is

    exp[-i theta sum_ij {F(r_ij/epsilon)-F((r_ij-2vt)/epsilon)}]. (3)

Equivalently at initial coordinates use F((r+2vt)/epsilon)-F(r/epsilon).
The initial conjugacy is essential for U(0)=I, signed cocycles and inverse time.
For each fixed sector, compact smooth initial data stay compact smooth and have
finite dGamma(v|p|) at each finite time. Already a one-R sector has spectrum R,
so no spectral lower bound is repaired.

## 2. Full local algebra and the sharp distinction

Removing an R coordinate from (3) leaves an exponential of the L1 number
operator weighted by the phase difference; removing L1 gives the matching R
string. All other pair factors cancel. For t>=0, the weight is supported in
(-epsilon,2vt+epsilon) in relative position. In the Heisenberg field centered
at x, both translated field and every string coordinate lie within
[x-vt-epsilon,x+vt+epsilon]. For t<0 reverse the oriented difference.

As in K2125, finite-sector identities extend to bounded smeared annihilators
by unitary conjugacy. Weighted number exponentials are bounded unitaries in
the relevant spatial Fock von Neumann factor. Spatial graded factorization
and normality then give

    alpha_t^e(A(I)) subset A(I expanded by v|t|+epsilon).         (4)

This is a support upper bound, not a strict finite-speed cone. It does imply
no signalling for interventions outside that expanded region, with arbitrary
initial correlations and parity-compatible local instruments. It does not imply
no signalling outside I expanded by v|t|.

### Explicit even-operation signalling witness

A C-infinity profile can have F'=2/3 on [-1/2,1/2]. To construct one, set a
symmetric smooth nonnegative bump h=1 there, h=0 outside [-1,1], and on the
right transition use h(u)+h(1-u)=1 after linear rescaling. For instance the
usual flat smoothstep b(1-u)/(b(u)+b(1-u)), b(u)=exp(-1/u) for u>0, has this
property. Then integral h=3/2, and F(z)=(2/3)integral_{-infinity}^z h.
In the middle F(z)=1/2+2z/3 exactly.

Take epsilon=v=1, A centered at0 and B centered at1/4, with packet radii
1/128, and t=1/32. Every initial relative coordinate lies in
[-17/64,-15/64], and every final one in [-13/64,-11/64], all inside the
linear plateau. The phase difference in (3) is exactly1/24. In A prepare
either one R particle or one inactive L0 particle with the same compact spatial
wavefunction; the two preparations are related by a local even species swap.
In B prepare one probe particle (L0(g)+L1(g))/sqrt2. The two L0 modes in the
second preparation remain orthogonal and disjoint, so antisymmetry creates
no extra observable phase. Total particle number and parity match.

For the R preparation the outgoing probe is
(|0>+exp(-i theta/24)|1>)/sqrt2; for the inactive preparation it remains |+>.
The local even probe-rail observable distinguishes them with trace distance

    D = |sin(theta/48)|.                                      (5)

For theta=pi this is strictly positive while 2vt=1/16<dist(A,B)=15/64.
The probe readout region translated left at time t remains outside A's
speed-v cone. This is an actual intervention-level failure. The argument
works at arbitrarily short times within a plateau, so increasing the velocity
to any fixed finite constant does not turn the immediate collar into a cone.

## 3. Complete recorded parity survives a completed encounter

Prepare arbitrary states on the R Fock code of d orthonormal compact modes,
with external references allowed and other field modes empty, and one |+>
dual-rail probe. Require every initial system/probe relative coordinate to
be below -epsilon and every final one above epsilon. Equation(3) becomes
exactly exp(-i theta N_R N_L1), with no position-dependent phase.
At theta=pi, the outgoing +/- rail measurement yields the two Kraus maps
P_even and P_odd on the system. Thus the entire recorded instrument is

    rho -> sum_b |b><b| tensor P_b rho P_b.                      (6)

This holds on all matrix units and hence with arbitrary references; it is
not just a matching parity probability. Within-parity coherence survives.
Spectators or incomplete crossings invalidate that exact reduction, as in
K2125. The final recording instrument is supplied separately, not dynamically
built here. Finite epsilon can therefore give EXACT final records while
violating strict intermediate locality. Its ultraviolet limit and energy
cost are quantified in [K2128](k2128-contact-limit-energy-cost-2026-10-27.md).

## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 and SC-META-53 remain
UNCERTAIN; SC-META-56 DISAVOWS an odd-action prerequisite. This supplied model
changes none of those source polarities, ledger0.263, LT-SM8/LT-GR6b or canon.
Finite exact controls check equations and witnesses. Infinite-dimensional domains,
local-algebra statements and analytic bounds rest on the written arguments and
independent internal review, not finite certificates or external certification.
