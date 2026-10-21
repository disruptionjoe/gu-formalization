---
title: "K1914: Exact bounded scalar reachability as a transport-cut problem"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied conditional models only; no native GU identification, novelty or formal proof
scripts:
  - tests/channel-swings/k1914_scalar_control_transport_cuts.py
  - tests/channel-swings/k1914_scalar_control_transport_cuts_probe.py
---

# K1914: Exact bounded scalar reachability as a transport-cut problem

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
result: necessary and sufficient measurable pulse cuts and exact smooth endpoints with strict amplitude slack
carrier: two characteristic directions in the supplied massless one-dimensional target LAYER=toy CHIRALITY=N/A
pairing: real Lebesgue duality and supplied positive CAR interpretation ON=finite_characteristic_strip
real_structure: real scalar potential and real phase lifts
grading: two propagation directions; no source chirality identification
action_owner: repository-construction -- common scalar bounded spacetime pulse
target: prescribed final right phase with identically zero left phase MAP-TYPE=intertwiner
```

## 1. Freeze the geometry and regularity class

[K1902](k1902-fixed-support-scalar-noise-2026-10-21.md) gives a smooth-pulse
sufficient amplitude bound and a weaker necessary one. Here is an exact
characterization for bounded MEASURABLE pulses on the same moving tube.
For a fixed smooth compactly supported phase, section 6 proves the same
threshold is the smooth-control infimum, with exact endpoints at every
strictly larger amplitude. No joint phase-energy optimizer is asserted.

Let c,T,L>0, d=2cT, I=[-L,L], J=[-L,L+d]. In characteristic coordinates
u=x-ct, z=x+ct the allowed region is

    E={(u,z): u in I, u<=z<=u+d}.

Define w(u,z)=V((z-u)/(2c),(z+u)/2)/(2c), zero off E.
A pulse |V|<=M corresponds to |w|<=m=M/(2c).
Use characteristic LABELS at time zero for final phases. Their two marginals are

    phi(u)=integral w(u,z) dz,  psi(z)=integral w(u,z) du. (1)

Changing to final spatial positions merely translates the appropriate label.
The required endpoint is (phi,psi)=(phi,0), with real phi in L-infinity(I).
In particular integral_I phi=0. Fix the real phase lift; minimizing over all
2pi lifts or probability laws is a separate problem.

## 2. Exact cut theorem

For measurable A subset I and B subset J define

    C(A,B)=area(E intersect [(A x B^c) union (A^c x B)]).

There exists such a bounded measurable pulse if and only if

    integral_I phi=0,
    |integral_A phi| <= m C(A,B) for every A,B.           (2)

Necessity: integrate (1) against 1_A(u)-1_B(z); the zero column marginal
removes B, leaving only the crossing region, where the integrand is bounded
by m in absolute value. This tests genuinely nonlocal transport constraints,
not just |phi(u)|<=MT.

For sufficiency take K={w in L-infinity(E): |w|<=m}. Banach-Alaoglu makes K
weak-star compact. Its marginal map into L-infinity(I) x L-infinity(J) is
weak-star continuous: a test pair f in L1(I), g in L1(J) pulls back to
f(u)+g(z), integrable on finite E with bounded section lengths. Thus the
image is convex and weak-star compact. Separation says (phi,0) lies in it
exactly when, for every real L1 pair,

    integral f phi <= m integral_E |f(u)+g(z)| du dz.    (3)

For bounded f,g, set A_t={f>t}, B_t={-g>t}. Integrating threshold differences
gives f(u)+g(z)=integral(1_A_t(u)-1_B_t(z))dt and
|f(u)+g(z)|=integral|1_A_t(u)-1_B_t(z)|dt. Since integral phi=0,
integral f phi=integral dt integral_A_t phi. Apply the upper half of (2)
for each t and Fubini to get (3). Common bounded truncations of f and -g
converge in L1; bounded section lengths and bounded phi allow passage to
arbitrary L1 tests. This proves sufficiency, not merely a dual lower bound.
No finite mesh or sampled set collection replaces the universal quantifier.

The capacity can be minimized over B explicitly. Define

    a_A(z)=length(A intersect I intersect [z-d,z]),
    ell(z)=length(I intersect [z-d,z]),
    C(A)=integral_J min(a_A(z),ell(z)-a_A(z)) dz.

At each z, choose membership in B to pay the smaller crossing length.
Consequently the exact amplitude threshold is

    M_star=2c sup_A |integral_A phi|/C(A).                (4)

Zero/zero contributes zero; positive numerator over zero is infinite.
If M_star is finite, its bounded measurable endpoint is attained by the
compactness argument. Formula (4) is a characterization, not a closed-form evaluation
for K1902's smooth plateau profiles. It includes the rowwise
amplitude bound through small sets A, and is monotone under larger duration
or support because the feasible pulse class enlarges.

## 3. A sharp continuous family, including the actual pulse

For d>=2L and m>0 define on E

    w(u,z)=-m sign(u) 1_{|u|<=z<=d-|u|}.

At each z its nonzero u section is symmetric, so the column marginal is zero.
The row phase is

    phi(u)=-m sign(u)(d-2|u|), u in [-L,L].              (5)

For A=[-L,0], direct integration gives C(A)=L(d-L) and
integral_A phi=m L(d-L). Thus (2) saturates and this pulse is an actual
GLOBAL amplitude minimizer for its fixed phase lift, M_star=2cm.
The primitive and the cut are continuous integrals, not grid evidence.
The phase jumps at zero. It has no finite H1 energy; it is deliberately
not an energy optimizer or a smooth K1902 admissible phase. Smoothing the
pulse gives approximated endpoints, not exact preservation of (5).

## 4. A stronger short-duration obstruction and its consumer

For d<=L and A=[-L,0], the crossing overlap is only z in[0,d]. There
a_A=d-z and ell-a_A=z, so

    C(A)=integral_0^d min(z,d-z) dz=d^2/4.

Every admissible pulse therefore satisfies

    M >= 2 |integral_(-L)^0 phi|/(c*T^2).                (6)

This recovers a necessary T^-2 steering cost that the pointwise MT bound
misses. For K1902's odd, piecewise-linear energy minimizer with contrast
magnitude theta and plateaux [-b,-a],[a,b], its half-area is
|integral_(-L)^0 phi|=theta(L+b-a)/4. Thus at 2cT<=L any exact realization
of that fixed profile needs

    M >= theta(L+b-a)/(2c*T^2).                          (7)

The bound persists as a limiting necessity for its smooth H1-approximating
profiles because their half-area converges. This is not a universal statement
for every profile with the same two plateau values: overshoot, changed
common phase and altered transitions can change the half-area. The full
cut problem, not (7) alone, governs those alternatives. K1902's amplitude
sufficient construction remains valid; this adds a rigorous lower bound.

## 5. Reproducible finite analogue and regularity boundary

For a finite bipartite edge set with capacities c_ij, signed values
|w_ij|<=m c_ij, row sums phi_i and zero column sums satisfy the exact same
cut theorem, with sums replacing area. A finite max-flow formulation follows
by adding m c_ij to each signed edge, turning the interval into [0,2m c_ij].
This is a tool for exact finite discretizations, not proof that one mesh
certifies all continuum cuts. The probes enumerate every finite cut with
rational arithmetic and construct an attaining primal flow. A connected
three-row example has local row bounds and zero total but fails a global
cut; removing the column constraint would miss it.

For an interior-supported bounded pulse, product mollification in (u,z)
preserves zero column marginal, never raises amplitude, and smooths the row
phase. The following correction closes the exact-endpoint issue for smooth
compact phase profiles; it does not smooth the discontinuous example (5)
while keeping its exact endpoint.

## 6. Released exact smooth-endpoint theorem

Suppose phi is real, C-infinity compactly supported in (-L,L), with zero
integral. Then

    inf_smooth ||V||_infinity = M_star,
    every M>M_star admits an exact smooth compact pulse. (8)

The infimum ranges over pulses compactly supported in the OPEN moving tube,
with exact final marginals (phi,0). A minimizer at equality is not asserted.
The old scalar construction already proves finiteness of M_star.

Proof: start from a measurable minimizer w at M_star. For 0<alpha<1 map

    u'=alpha*u, z'=alpha*z+(1-alpha)*d/2,
    w_alpha(u',z')=w(u,z), zero elsewhere.

Its support lies strictly inside E: |u'|<=alpha L and
(1-alpha)d/2<=z'-u'<=(1+alpha)d/2. The amplitude is unchanged. Its row
marginal is phi_alpha(u')=alpha phi(u'/alpha), and its column marginal is
zero. Total zero area is preserved; phi_alpha approaches phi in every C^k
norm because the original phi is smooth and compactly supported in I.
Product convolution with nonnegative smooth probability mollifiers of radius
smaller than the support margin yields a smooth interior pulse w_alpha,e.
The row marginal is phi_alpha*eta_e, the column remains identically zero,
and the sup norm still does not increase. Choose e->0 with alpha->1.
Then r=phi-phi_alpha*eta_e is smooth compact, has zero area, and tends to
zero in sup norm (in fact every C^k norm).

Fix once and for all a smooth g compact in (0,T) with integral1. Define

    f(y)=-(1/(2c)) integral_(-L)^y r(v)dv,
    V_r(t,x)=g'(t)f(x-ct)+g(t)r(x-ct).

Its right phase is r, its left phase is zero by integrating
(partial_t-c partial_x)[g(t)f(x-ct)] on the opposite characteristics, and it
is smooth compact in the open tube. The compactness of f follows from zero
area. Its amplitude is bounded by

    ||V_r||_infinity <= [ (L/c)||g'||_infinity
                         +||g||_infinity ] ||r||_infinity.

This tends to zero. Adding it to the shrunken, mollified physical pulse
2c*w_alpha,e therefore gives EXACT (phi,0) and amplitude below any chosen
M>M_star. Necessity of M>=M_star follows from (2). This proves (8).
The correction is permitted because the model has no bounds on derivatives
of V; it would not prove a control-bandwidth or slew-rate version.

This releases a concrete acceptance test: for a specified smooth phase,
all cuts below a strict budget imply a smooth exact realization. It closes
the measurable-to-smooth infimum gap without evaluating the supremum over A.
Optimizing the phase itself, its lifts, noise law or gradient energy remains
a different variational problem. At the piecewise-linear K1902 energy
infimum, joint limiting amplitude/energy attainment still needs its own proof.

## 7. Hostile review and prior art

Strongest overclaim: attainment at the exact smooth amplitude threshold,
optimal noise energy, or a bandwidth-constrained smoothing theorem. None is
claimed. Strict-slack smooth exact reachability is proved separately above. Strongest contrary
construction: (5) attains the cut threshold but has infinite phase-gradient
energy; local row bounds also fail the finite global-cut control. Weakest
seams: the 2c Jacobian, final phase labels, weak-star image closedness and
threshold signs. They are explicit and independently checked in finite
controls. The proof carries the continuum quantifiers.

[Korman and McCann](https://arxiv.org/abs/1201.6404) and
[Korman, McCann and Seis](https://arxiv.org/abs/1307.7774) study bounded-density
transport and its duality. Our signed marginals can be shifted to that positive
capacity framework. The specialized proof above is self-contained; this is
no assertion of a new transport theorem. Its use here is to replace the pulse
ansatz bracket by an exact measurable characteristic-control criterion.


## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field operator grammar; SC-MAS-01 and
SC-CHI-02 ASSERT a stylized curvature-mass toy; SC-META-53 remains UNCERTAIN
about indefinite spectra. None selects the positive Hilbert pairing, bath,
scalar drive, observable algebra or physical units here. LT-SM8, LT-GR6b
and AC-F1 remain unchanged. Full20 injection, separate K/C, physical domain
and accessible-algebra identification remain independent construction debts.
No source-register, physics-ledger or canon verdict changes. No GU prediction,
novelty, external expert acceptance or formal proof is claimed. Analytic
arguments carry general scope; exact finite probes test the actual algebra
and countercontrols. Report and dependency-pin checks establish only
consistency and provenance, separately from mathematical-input faults.
