---
title: "K1832: common positive energy for the corrected K77 principal fixture"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact symmetrization and constant-coefficient energy for the compressed conditional fixture; no physical pairing or source action
---

# One positive form works in every spatial direction

The three corrected spatial matrices from K1824 admit one rational positive
symmetrizer. Thus their **compressed constant-coefficient system** is symmetric
hyperbolic, with propagation speed at most1 in the stated coordinate units.
Its positive energy is mathematical; it is not a derived GU physical pairing.
All common positive forms, after fixed module identifications, are parametrized
by positive Hermitian32-by32 matrices. There is no unique selected energy.

The result also settles a useful compatibility test: a nonzero square-zero
zero-order coefficient, including K1830's rank128 completions, cannot generate
a dissipative real evolution in any positive norm. Its finite paired action
and auxiliary complex remain valid; they do not become a stable time generator.

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
result: common positive symmetrizer, energy estimate and zero-order compatibility boundary
carrier: corrected E512 compressed principal fixture with32 real16 modules LAYER=toy CHIRALITY=N/A
pairing: constructed rational positive symmetric energy ON=compressed_constant_coefficient_system
real_structure: rational matrices extended to real vector fields; commuting complex structure on each module
grading: time and three spatial derivatives; auxiliary square-zero degree remains separate
action_owner: repository-construction -- normalized compressed principal fixture, not a source-owned action
target: simultaneous symmetrization and real evolution energy MAP-TYPE=evaluation
```

## 1. Exact object and structural reduction

Use precisely K1824's A_j=P O D0^-1 D_j L P on im(P), j=7,8,9.
K1822 certifies the rational inverse, graph lift and projector; K1824 certifies
the joint algebra M8(C), represented on32 equivalent real16 modules, and

```
576 A(xi)^4 - 577 |xi|² A(xi)² + |xi|^4 I = 0.
```

This does not identify the compression with an invariant restriction of the
uncompressed operator or a physical quotient. No new source cells, derivative
adjoint, reality identification or stationary background have been supplied.
SC-OP-04 ASSERTS, SC-OP-05 UNCERTAIN, SC-ACT-01/02/06 ASSERTS and
SC-META-53 UNCERTAIN remain; RA-F1, AC-F1 and LT-SM8 keep their existing grades.

The32 support blocks have20 ambient coordinates and rank16 projector images.
Select exact projector-column bases and left inverses, retaining the actual
matrices rather than replacing their representation. Four coordinate types
occur eight times each. Solve simultaneously

```
H A_j = A_j^T H,  H=H^T.
```

The full intertwiner space has dimension2; the symmetric subspace has
dimension1 in every irreducible type. Normalize H00=1. Exact LDL elimination
has16 positive pivots for each type. On the first type the eigenvalues are
11/27,26/27,22/9,11/3, each fourfold. Its energy condition number is9 in
that basis. Other coordinate types need not share its rational spectrum;
positivity is proved separately by their rational LDL pivots. The certificate
contains every16-by16 matrix, H, complex structure and pivot.

The direct sum of these forms is positive on E512 and symmetrizes all three
matrices. K1824's exact module intertwiners transport it to identical modules.
On one module a commuting complex structure J satisfies J^T H=-HJ. For any
other symmetric common form G, H^-1 G commutes with all A_j. Conversely this
commutation plus H-self-adjointness gives a symmetric common form. The full
commutant is M32(C), and its H-adjoint is complex conjugate transpose in an
H-orthonormal multiplicity basis. Therefore all positive G correspond exactly
to positive Hermitian32-by32 multiplicity matrices, of real dimension1024.
This is a cone of available energy forms, not1024 physical free parameters.

## 2. Follow-through: an actual Cauchy estimate

On R³ (or a periodic three-torus) take the constructed constant matrices and

```
partial_t u + sum_j A_j partial_j u =0,
E(t)=integral u^T H u.
```

For smooth rapidly decaying data integration by parts gives E'(t)=0.
In Fourier variables H^(1/2) A(xi) H^(-1/2) is real symmetric, so its
complex exponential is unitary. Plancherel extends the solution operator
uniquely to an isometric group on every H^s, with the same H norm on derivatives.
The equivalent ordinary Euclidean norm has a uniform bound independent of
frequency and time. This proves constant-coefficient well-posedness, not a
nonlinear, variable-background or noncompact-GU domain theorem.

The quartic bounds all eigenvalues by |xi|. Consequently
|u^T H A(n)u|<=u^T H u for unit n. Integrating the local energy identity over
an exterior cone proves support propagates at speed at most1. Coordinate
units are inherited from the fixture; no physical speed calibration follows.
These are the standard symmetric-hyperbolic energy arguments (see
[Tadmor's energy-method notes](https://www.math.umd.edu/~tadmor/lecture-notes/hyperbolic/node4.html)); the new computation here supplies H for this fixture.

For a fixed unit normal, the flux form H A(n) has inertia(256,256), using the
real spectral projectors and the connected unit sphere (no zero eigenvalue
can occur). A maximal nonnegative-flux boundary subspace is exactly a graph
from its positive to its negative spectral sector with contraction norm in
the |A(n)|-weighted H energies. Indeed positive projection is injective on a
nonnegative subspace, and maximal dimension forces it onto the positive
sector; the flux inequality is precisely the contraction inequality. Equality
means an isometry. This classifies the finite boundary-energy choices; it
selects none and does not assert a variable-domain boundary-value theorem.

## 3. Follow-through: why the nilpotent completion is not damping

For a real constant zero-order C in u_t+sum A_j u_xj+C u=0,

```
E'(t)=-integral u^T(HC+C^T H)u.
```

Dissipativity in this norm requires HC+C^T H>=0. If C is nilpotent, its
trace is zero. After conjugation by H^(1/2), the symmetric part has zero
trace and is positive semidefinite, hence vanishes. The conjugated C is then
real skew-symmetric, normal, and nilpotent, so C=0. The conclusion holds for
ANY positive norm, independently of the principal matrices. In particular,
none of K1830's nonzero square-zero rank128 maps is dissipative as this real
time-evolution coefficient. On the periodic zero spatial mode,

```
u(t)=(I-t C)u(0)
```

has quadratic energy growth for any u(0) with Cu(0)!=0. Choosing the opposite
sign of C cannot remove this obstruction. A nonpositive energy, an auxiliary
homological differential, an imaginary quantum generator or a changed carrier
is a different question. No source completion is ruled out by this supplied
real-evolution requirement.

A general bounded C still has the usual finite-time exponential energy bound
from the largest norm of its H-symmetric part. Failure of dissipation is not
failure of constant-coefficient well-posedness, and growth is not a physical
instability verdict without the action/observable bridge.

## 4. Validation and hostile review

```
sage -python tests/channel-swings/k1832_k77_common_energy_form.py
sage -python tests/channel-swings/k1832_k77_common_energy_form_probe.py
```

The producer reuses K1824's rational primitive reconstruction, checks all32
image bases and four exact symmetrizer types, and tests spectral projectors
and a corrupted energy. The separate probe solves directly in136 symmetric
coordinates (a different equation assembly), verifies all leading principal
minors, and tests Fourier-energy algebra, complex cross-copy forms, boundary
contractions and polynomial growth for small nilpotents. It does not claim a
second independent reconstruction of the full source fixture. Reporting
comparisons are separate from mathematical controls.

The initial check incorrectly expected rational energy eigenvalues in every
coordinate type; rational LDL positivity passed and supplies the correct
basis-independent criterion. That unnecessary assertion was replaced, not
used to infer positivity. The strongest overclaim is physical energy or
uncompressed descent; both are expressly excluded. Contrary controls reject
the Euclidean-transpose shortcut and nonzero nilpotent damping. The written
PDE proof checks constant coefficients, domain, Fourier convention and flux
orientation. No unresolved finding in this scope, no separate-agent review,
no novelty claim and no canon promotion.

Next: construct an action-owned stationary-background coefficient and its
actual Riesz/real-structure relation, then test its H-symmetric part and
constraint preservation. The available H cone alone does not select that
input; more arbitrary nilpotent seeds cannot answer it.
