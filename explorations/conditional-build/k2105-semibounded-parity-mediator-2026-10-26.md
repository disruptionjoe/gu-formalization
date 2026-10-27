---
title: "K2105: Nonnegative covariant-kinetic parity mediator"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source selection, relativistic apparatus or physical recovery
scripts:
  - tests/channel-swings/k2105_semibounded_parity_mediator_probe.py
---

# K2105: Nonnegative covariant-kinetic parity mediator

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
result: conditional mathematical construction with explicit domain and approximation limits
carrier: L2 real line tensor two memory modes tensor two-state pointer LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product ON=declared_positive_Hilbert_space
real_structure: complex adjoint; no source-selected real form
grading: even memory occupations; bosonic pointer
action_owner: repository-construction -- supplied covariant kinetic Hamiltonian and fixed laboratory readout
target: stable spectrum and coherent scattering instrument MAP-TYPE=intertwiner
```

[Conditional mathematics accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Source and object boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 and SC-META-53 are
UNCERTAIN; SC-META-56 DISAVOWS a mandatory odd-action prerequisite. These
supplied positive Hilbert apparatus/algebra models are not equation9.16.
K2021 supplies local R0/R1; a source-selected positive observed algebra,
state and dynamics still need construction. LT-SM8/LT-GR6b, source-register,
ledger0.263 and canon remain unchanged. Native2+1, total/observed chirality,
full20 and K/C accessibility are distinct debts. This is reverse-scaffold
conditional mathematics, with no GU recovery, novelty or external certification.

## 1. Repair the spectrum by changing the kinetic model

[K2104](k2104-point-contact-parity-transport-2026-10-26.md) constructs
self-adjoint chiral contacts but their spectrum is the whole real line.
Positive-momentum compression changes locality. Here use a different model,
with hbar=1, m>0 and H0=p²/(2m), p=-i partial_x, with Dom p=H¹(R,C^D) and Dom H0=H²(R,C^D).
Let G be a smooth unitary matrix multiplier, with bounded first two derivatives,
G=I left of a and G=W right of b. Define

    A(x)=i G'(x)G(x)*,   D=G p G*=p+A,
    H=G H0 G*=D²/(2m),  Dom H=G H²=H².              (1)

A is Hermitian. Unitary conjugation proves self-adjointness, spectrum[0,infinity)
and nonnegativity; its form is ||D psi||²/(2m). On test functions,

    2m H = p² + A p + p A + A²
         = p² + 2A p - i A' + A².                   (2)

The derivative interaction and A² are part of the supplied apparatus.
This is a local differential expression with compact coefficient support,
not H0 plus a bounded scalar or matrix multiplication potential. Its energy
is nonnegative even when internal G mixes pointer states. A constant rest
energy could be added; that does not turn Schrödinger propagation relativistic.

## 2. Exact transmission and parity instrument

For k>0, G(x)e^{ikx}c is a generalized eigenfunction at k²/(2m). On the left
it is the incoming e^{ikx}c, and on the right it is e^{ikx}Wc, with no
reflected term. Incidence from the right has transmitted W*; multiplying by
W* first gives the incoming right amplitude c. Thus

    T_left(k)=W, T_right(k)=W*, R_left=R_right=0.     (3)

These are exact stationary scattering data at every positive energy, not
an approximation by fast particles. For disjoint ordered zones choose

    G(x)=exp[-i theta2(x)n2(I-X)] exp[-i theta1(x)n1(I-X)],
    theta_j(-infinity)=0, theta_j(+infinity)=pi/2.    (4)

n1,n2 are occupations of already localized memory modes and X is the pointer
Pauli matrix. The completed rotations commute and equal controlled X gates.
W sends psi tensor |0> to

    P_even psi tensor |0> + P_odd psi tensor |1>.    (5)

Read the pointer in its fixed laboratory Z basis. The recorded channel is
sum_b |b><b| tensor P_b rho P_b, preserving coherence within each parity
block. This holds with arbitrary references. It is not a refined measurement
of n1 and n2 followed by classical coarse graining. Diagonal memory drift
commuting with (4) can be factored and calibrated. Unspecified noncommuting
drift is not included.

Laboratory preparation and measurement axes are essential: if states,
Hamiltonian AND all readout observables are conjugated together by G, the
model is just the free model in a new frame. The relative W in fixed external
frames is what implements(5). This construction does not derive those
frames or controls from GU. Gauge-removable spin couplings have established
precedent, e.g. [Tokatly and Sherman, Ann.Phys.325(2010)1104](https://arxiv.org/abs/0910.0951).
This citation is an adjacent precedent, not a claim that their disordered
2D model is this instrument or that this construction is novel.

## 3. Point contacts are nonnegative self-adjoint extensions

Take G piecewise constant with jumps Uj at xj and ordered product W.
Then H=G H0 G* is self-adjoint and nonnegative on G H². Equivalently it
acts as -partial_x²/(2m) between contacts and requires BOTH traces

    psi(xj+)=Uj psi(xj-),  psi'(xj+)=Uj psi'(xj-).    (6)

Piecewise H² with these traces is exactly G H²; the quadratic-form domain
is G H¹. Current is conserved since both traces have the same unitary.
Continuity of psi with only a derivative delta jump is a different extension.
Equations(3) persist, by checking these actual traces on each plane wave.
A piecewise constant G is not differentiated as an ordinary bounded
multiplier in(2): distribution products would not define this domain.

Let smooth G_e agree with G off a set E_e of total length tending to zero.
For z outside[0,infinity), choose k=sqrt(2mz) with Im k>0. The free resolvent
kernel is (im/k)exp(ik|x-y|), whose row L² norm squared is
m²/(|k|² Im k). Vector-valued Cauchy--Schwarz and ||G_e-G||<=2 give

    ||(H_e-z)^(-1)-(H-z)^(-1)||
       <=4m sqrt(|E_e|)/(|k| sqrt(Im k)).            (7)

Expand G_e R0 G_e* - G R0 G* into two terms; each differing multiplier
is supported in E_e. Apply the row estimate and its adjoint. This proves
dimension-independent norm-resolvent convergence, also after tensoring any
reference. Strong convergence of the propagators follows directly from
G_e->G strongly and the conjugation formula. Neither statement establishes
uniform operator-norm dynamics or an energy-independent finite-time gate.
[K2107](k2107-parity-arrival-resources-2026-10-26.md) supplies the operational
arrival and coefficient resource distinctions.

## 4. Contrary controls and exact boundary of the repair

If H0+V=G H0G* on all C_c-infinity test fields, comparison of first derivative
coefficients in(2) forces A=0. Then G is constant and W=I. A nontrivial
covariant gate cannot be implemented simply by retaining its zero-order term.
A broader scattering boundary is also known: for a self-adjoint matrix
multiplier with integral(1+|x|)||V(x)|| dx finite, T_left/right(k)->I at high
energy. Thus that multiplier-only class cannot have a fixed nonidentity W
at every energy. This uses [Aktosun and Weder, Theorem4.1, equations4.2--4.3](https://arxiv.org/html/2212.07573v2), with potential rescaled by2m.
It excludes neither energy-window approximations nor derivative couplings.

Dropping A² also loses the positivity proof. For the commuting flip profile,

    H_bad=(p²+Ap+pA)/(2m)
         =G[H0-A²/(2m)]G*.                          (8)

On the occupied, X=-1 channel, A=2theta' and the transformed potential is
-2(theta')²/m. If theta' is nonzero and compactly supported, a normalized
trial f_R=R^(-1/2)exp(-|x|/R) has kinetic1/(2mR²) but negative potential
expectation of order -1/R. For sufficiently large R its energy is negative.
For a fixed profile rescaled to width e, unitary dilation gives
inf spectrum H_bad,e=e^(-2)inf spectrum H_bad,1<0. These are attractive
bound states deepening with the contact limit, not a small omitted correction.
The full-square H_e remains nonnegative.

The model repairs bounded-below energy for a nonrelativistic mediator. It
does not provide finite propagation speed, a relativistic local field theory,
a massive-field-to-memory capture interface, preparation/work accounting,
or a source-owned physical state. A finite zone coupled to a localized
register is finite-range coupling; the point model is a separate singular
limit with diverging coefficients. No all-apparatus exclusion or recovery
claim follows from either construction.

## 5. Verification

Universal statements follow from unitary conjugation, trace domains,
plane-wave matching, the kernel estimate and the written variational argument.
Exact controls check a nonconstant covariant derivative, its full square,
all16 memory matrix units, two-sided transmission with nontrivial complex
rotation, resolvent row integral, and an actual negative quadratic form when
A² is omitted. Mutations change coefficients, gates or contact traces.
Finite probes are not a continuum proof or proof-assistant certification.

The polynomial gauge control uses unbounded noncompact A=2x only to check
differential algebra. The square pulse is nonsmooth and is not the pi-flip
profile; it tests negative quadratic-form energy. Neither replaces the
written compact-smooth operator and variational proofs.
