---
title: "K130 K129 compact cylindrical Gauss pairing Fock measure boundary wave"
status: active_research
doc_type: reverse_scaffold_compact_gauge_reduction_result
created: 2026-09-07
date: 2026-09-07
target_claim: INTERNAL_TARGET:K129_COMPACT_OR_RIGGED_NONZERO_PHYSICAL_REDUCTION_SUCCESSOR
claim_ceiling: exact repository-owned projective compact-circle U(1)^8 charge-network construction with normalized finite-graph Haar Gauss projectors, a nonzero positive refinement-consistent physical inductive limit, eight integer global electric-flux sectors shifted by circle holonomy, graphwise Wilson/Klein defect covariance and exact fixed-graph equivalence to axial reduction; the natural point-supported matter completion does not admit an isometric local-gauge/position intertwiner from K128's continuum Lebesgue L2 CAR carrier, so the fixed-width continuum defect and regulator-independent interacting Hamiltonian do not follow, and no smooth-gauge Haar projector, full K128 equivalence, rigging map, point-Fock extension, finite-coupling NESS/current, source/GU ownership, Born derivation, prediction, confirmation or holdout credit follows
manifest: lab/process/k130-k129-compact-cylindrical-gauss-pairing-fock-measure-boundary-wave.json
probe: tests/channel-swings/k130_k129_compact_cylindrical_gauss_pairing_fock_measure_boundary_probe.py
---

# K130 K129 compact-cylindrical Gauss pairing/Fock-measure boundary wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: projective compact-circle U(1)^8 charge-network Gauss reduction with a positive nonzero physical pairing and an exact continuum-L2 matter measure-class obstruction
carrier: inductive limit of L2(U(1)^(8E),Haar) graph carriers with integral point-charge matter labels; K128 comparison carrier is C9 impurity tensor C512 Klein tensor antisymmetric Fock over eighteen full Dirac Lebesgue-L2 species LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: normalized graph Haar pairing and Kronecker charge-network pairing ON=repository_owned_compact_cylindrical_gauge_control
real_structure: complex conjugation of U(1)^8 characters, integer electric charge lattice, CAR adjoint and Hermitian Clifford-Klein generators
grading: total fermion parity and total integral U(1)^8 charge; graph gauge redundancy is projected and global electric flux remains
action_owner: repository-construction
target: refinement-compatible physical charge-network inductive limit and intertwining comparison with K128 continuum axial/Coulomb reduction MAP-TYPE=intertwiner
```

Scope: this packet constructs the compact cylindrical representation of one
repository-owned `U(1)^8` gauge control on the spatial circle. It proves a
nonzero positive physical pairing and exact graphwise reduction statements.
It then tests the natural bridge to K128's continuum Lebesgue-`L2` CAR matter
and proves that the point-supported charge-network map does not extend
isometrically while preserving position and local gauge action. It does not
exclude a different rigged, Fock-compatible, renormalized or continuum
construction.

## Inline preflight bookend

The rebuilt frontier contained seven substantial arcs. Compact projective
connection measure, the circle global mode and the continuum-matter bridge are
independently decidable. Normalized Gauss projection, refinement consistency
and graphwise axial equivalence depend on the compact character construction.
The regulator-independent Hamiltonian and point interaction depend on a
successful continuum matter bridge; scattering/NESS and source ownership
remain further downstream.

Mechanism retrieval separates this result from K124's single finite lattice,
K128's already-reduced continuum CAR theory and K129's regular bosonic Fock
representation with zero normalizable Gauss kernel. Standard projective-
connection and generalized-Haar ancestry was checked against Ashtekar--
Lewandowski, Baez's generalized-measure construction and Baez's spin-network
construction. The exact Abelian charge solution, refinement diagram and K128
measure comparison below are repository-owned.

The route-changing lens census covered compact harmonic analysis, projective
limits, charge networks, lattice Gauss law, local gauge representation,
inductive Hilbert limits, CAR functoriality, Lebesgue versus counting measure,
strong measurability, Wilson dressing, electric forms, rigged reduction,
singular point interactions, scattering/NESS, source fidelity and hostile
philosophy of science. Compact characters are primary because they supply the
positive physical pairing K129 lacked; the fixed-wavefunction refinement test
is the cheapest decisive check of K128 equivalence. A rigging map is the
fallback if the compact point-matter bridge fails.

## 1. Every finite circle graph has a normalized nonzero Gauss projector

Let `Gamma` be a connected oriented cycle with vertex set `V` and edge set
`E`, and put `G=U(1)^8`. The compact gauge carrier is

```text
H_Gamma=L2(G^E, product Haar).
```

Its orthonormal Fourier basis is labelled by integral edge fluxes
`n_e in Z^8`. For integral vertex charges `Q_v in Z^8`, a vertex gauge
transformation `g=(g_v)` multiplies the charge-network basis vector by

```text
product_v g_v^(div n(v)+Q_v).                             (1)
```

Normalized Haar averaging over the compact group `G^V` therefore gives the
orthogonal projector

```text
P_Gamma |n,Q> = 1_[div n+Q=0] |n,Q>.                     (2)
```

This is a genuine bounded projector with a positive range pairing. It is not
a Haar integral over the smooth infinite-dimensional gauge group used in
K129. For a connected circle, (2) has a solution exactly when
`sum_v Q_v=0`. Fixing one edge flux `m in Z^8`, every other edge flux is the
integer cumulative-charge solution. The root impurity/vacuum with `Q=0` and
`m=0` is a normalized physical vector, so the physical range is nonzero.

## 2. Subdivision preserves the projector and physical pairing

Subdivide an edge `e` into `e_1 e_2` and add one neutral bivalent vertex. The
cylindrical embedding is

```text
iota: f(...,U_e,...) -> f(...,U_(e_1) U_(e_2),...),
iota |...,n_e,...> = |...,n_e,n_e,...>.                   (3)
```

Haar invariance makes `iota` isometric. The new neutral Gauss equation is
`n_(e_2)-n_(e_1)=0`, already satisfied by (3), while every old vertex equation
is unchanged. Hence

```text
P_(Gamma') iota = iota P_Gamma.                           (4)
```

The physical ranges and their positive pairings form an inductive system.
Its completion `H_phys^cyl` is nonzero. This escapes K129's zero-kernel
theorem because the representation is nonregular: holonomy characters exist,
but no self-adjoint point or smeared connection generator is obtained by
differentiating weakly continuous translations.

The electric energy of a fixed charge network is also subdivision-consistent
when an edge contribution is weighted by its geometric length:
`ell_e |n_e|^2` becomes
`ell_(e_1)|n_e|^2+ell_(e_2)|n_e|^2`. This supplies a compatible graphwise
electric quadratic form on the algebraic cylindrical domain, not yet a closed
regulator-independent interacting Hamiltonian with continuum CAR matter.

## 3. Circle holonomy and the eight global flux integers survive reduction

The Gauss equations determine flux only up to the same integer
`m in Z^8` on every edge. Multiplication by a circle character

```text
Hol_k(U)=product_e U_e^k,       k in Z^8,                  (5)
```

sends every `n_e` to `n_e+k`, preserves (2), and shifts `m` to `m+k`.
Thus the compact physical space retains all eight integer global electric-flux
directions and the conjugate circle-holonomy shift. These sectors are absent
from K128's selected trivial-open-holonomy interval sector and must be fixed or
summed over before any equivalence claim.

Large smooth gauge transformations change link representatives but do not
change the gauge-invariant total circle holonomy. The exact content here is
the compact character action and its global sector shift, not K129's regular
connection operator or a source-selected theta vacuum.

## 4. Graphwise Wilson/Klein reduction is exactly axial

Place the impurity and finitely many charged matter modes at graph vertices.
For a neutral transition creating charge `-b` at `y` and changing the impurity
by `+b` at `x_0`, multiplication by the Wilson character on an oriented path
from `x_0` to `y` shifts `n_e` by `b` on precisely that path. Its divergence
cancels the two charge changes, so it maps `Ran P_Gamma` to itself. The odd
CAR factor and K126's odd Clifford--Klein factor make the transition even.

For fixed `Gamma`, choose a spanning tree/cut and solve (2). The map

```text
J_(Gamma,m): |Q,matter> -> |n(Q,m),Q,matter>              (6)
```

is an isometry from the neutral lattice-matter sector onto the physical
charge-network sector at global flux `m`. Under (6), the Wilson character
becomes the cumulative electric-string update used by K128. Thus compact
Dirac reduction and axial reduction agree exactly **at a fixed graph and
global sector**. This strengthens K124 and locates the precise finite-
resolution content of K128; it is not yet an equivalence with K128's continuum
Lebesgue-`L2` CAR Fock space.

## 5. The natural continuum CAR bridge fails by measure class

The projective compact construction represents localized charged matter by
orthogonal point labels. Its one-particle position carrier is therefore
`ell2(Sigma_counting)`: every vector has at most countable support. K128 uses
`L2(Sigma,dx)`, in which point evaluation is null and nonzero vectors are
Lebesgue wave packets. These representations are not related by the natural
position-labelled map.

The obstruction is visible without cardinality arguments. Take the same
normalized continuum wavefunction `f(x)=1` on `[0,1]`. At dyadic level `r`,
represent it by the normalized sum over the `2^r` cell midpoints,

```text
psi_r=2^(-r/2) sum_j |(j+1/2)2^(-r)>.                    (7)
```

Midpoint sets at different dyadic levels are disjoint, so
`<psi_r,psi_s>=0` for `r!=s` and
`||psi_r-psi_s||=sqrt(2)`. The sequence is not Cauchy although every member
represents the same continuum step function under the intended Riemann
interpretation. Consequently no refinement-compatible isometry can send
Lebesgue wave packets to these point charge networks while preserving their
position labels.

The invariant version is stronger. The representation of the position/
local-multiplication algebra on `ell2(Sigma_counting)` is atomic: every
singleton label has a nonzero minimal spectral projection. Its representation
on `L2(Sigma,dx)` is diffuse: singleton projections vanish and there are no
nonzero minimal position projections. A unitary intertwiner of the local
multiplication representations would preserve their projection lattices and
minimality, which is impossible. Thus the obstruction is not an artifact of
the chosen dyadic sequence.

An abstract Hilbert-space isomorphism is irrelevant: it would not intertwine
the continuum multiplication algebra, local gauge phases, position support or
Dirac dynamics. The graphwise Wilson/Klein defect is a sum over point matter
modes. Its fixed-width continuum integral therefore has no strong limit in
this natural compact point-matter completion. The exact fixed-graph map (6)
does not extend to a unitary equivalence with K128.

This is a route obstruction, not a universal no-go. A Fock-compatible rigging
map, a direct-integral construction, a different continuum matter measure or a
renormalized operator-algebraic coupling may still work, but it must state its
pairing and intertwining maps explicitly.

## 6. Hamiltonian, point and NESS consequences

The compatible pure charge-network electric form does not repair the failed
continuum matter embedding. There is therefore no common regulator-independent
Hamiltonian whose continuum matter term is K128's positive Dirac/Fock form and
whose interaction is K127's fixed-width Wilson/Klein defect. K125's
`epsilon^(-1/2)` CAR point norm remains unchanged, so no singular IBC,
counterterm, closed form or resolvent limit follows.

Without a continuum interacting dynamics and infinite leads, no Moller/Ruelle
map, return-to-NESS theorem or microscopic field current is constructed.
K115's reduced cycle ratio `6561/256` remains a reduced-model affinity. The
gauge group, compact representation, global sector, charges, couplings,
boundary convention and state remain repository imports rather than outputs
of a source/GU action.

## Inline postflight bookend

The compact connection, normalized graph-Haar, refinement, global-sector and
graphwise reduction arcs complete. They provide a nonzero positive cylindrical
physical space and exact fixed-graph axial equivalence. The continuum-matter
arc is negative: natural point charge networks have counting measure, while
K128 matter has Lebesgue measure; the fixed-wavefunction midpoint sequence is
orthogonal rather than Cauchy. The Hamiltonian/point arc therefore stops at an
exact representation-interface predicate.

- **Strongest construction:** a projectively consistent nonzero compact
  physical Hilbert space with normalized graphwise Gauss projectors and eight
  global electric-flux/holonomy directions.
- **Strongest overclaim caught:** fixed-graph charge-network/axial equivalence
  does not extend automatically to K128's continuum CAR Fock carrier.
- **Strongest contrary route:** a rigged or direct-integral reduction that
  retains Lebesgue wave packets may evade the counting/Lebesgue mismatch, but
  must construct a positive pairing and the local-gauge/Dirac intertwiners.
- **Weakest reproducibility seam:** abstract separable Hilbert spaces may be
  unitarily isomorphic. The actual obstruction is to an intertwiner of the
  position/local-multiplication representations: the point carrier is atomic
  and the Lebesgue carrier diffuse. The result has been narrowed to that exact
  geometric scope rather than a bare Hilbert-dimension claim.

No source action, physical preparation, detector effect, Born rule, held-out
score, prediction, confirmation, canon, paper, release or public-posture
status changes.

## Next condition

Construct a Fock-compatible rigging map or direct-integral continuum reduction
whose positive physical pairing preserves K128's Lebesgue `L2` matter,
intertwines local gauge multiplication and the Dirac form, and carries the
fixed-width Wilson/Klein defect. Alternatively prove that no such intertwiner
exists under explicit regularity and locality assumptions. Only then attempt a
regulator-independent gauge-covariant Hamiltonian and singular number-changing
Fock interaction; infinite-lead finite-coupling scattering/NESS and an actual
source/GU action remain separate requirements.

## Standard-construction ancestry

- A. Ashtekar and J. Lewandowski, [*Differential Geometry on the Space of
  Connections via Graphs and Projective Limits*](https://arxiv.org/abs/hep-th/9412073).
- J. C. Baez, [*Generalized Measures in Gauge Theory*](https://arxiv.org/abs/hep-th/9310201).
- J. C. Baez, [*Spin Network States in Gauge Theory*](https://arxiv.org/abs/gr-qc/9411007).

## Reproduction

```bash
python3 tests/channel-swings/k130_k129_compact_cylindrical_gauss_pairing_fock_measure_boundary_probe.py
python3 tests/channel-swings/k130_k129_compact_cylindrical_gauss_pairing_fock_measure_boundary_probe.py --selftest
```
