---
title: "K1356--K1360 maximal-compact nonuniform-charge bridge control"
status: active_research
doc_type: conditional_research_result
created: "2026-10-07"
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
claim_effect: none
---

# K1356--K1360 maximal-compact nonuniform-charge bridge control

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE` only for testing the maximal-compact
escape explicitly left open by K1351--K1355. The selected circle, charge
normalization and interacting control are repository constructions. They do
not identify source hypercharge, observed particle charges or a physical GU
quotient.

Scope: exact compact-subgroup, K-type, unbounded-generator and classical
gauge/BRST/BV-BFV core statements for `G=Spin_0(7,7)` and K1335's spherical
principal-series Hilbert carrier `H_ps=L2(K/M)`. No source-selected reduction,
completed nonlinear domain, global causal theorem, positive physical Hilbert
cohomology or observed-state map is constructed.

```gu-typed-objects
result: an explicit maximal-compact circle has a positive kinetic control, nonuniform integer weights in an actual spherical K-type, an unbounded self-adjoint generator, and a repository-owned interacting gauge/BRST/BV-BFV realization on the dense K-finite core
carrier: G=Spin_0(7,7), K=(Spin(7)xSpin(7))/diagonal center, H_ps=L2(K/M), selected circle C and H_Kfin LAYER=ambient BRIDGE=maximal-compact-charge-reduction CHIRALITY=N/A
pairing: principal-series Hilbert pairing plus the positive restriction of minus the split Killing form to the selected compact circle ON=selected_compact_subgroup
real_structure: unitary complex Hilbert representation with real compact Lie-algebra generator and self-adjoint charge operator Q
grading: integer C-charge grading on H_ps; formal ghost/antifield grading on the classical common core; no completed physical BV cohomology
action_owner: repository-construction
target: strongest surviving compact-reduction route after K1355 MAP-TYPE=restriction
```

## Preflight bookend

K1351--K1355 exclude the direct full-group character, uniform internal phase,
full-`G` fixed-charge sector, pointwise finite-fibre linear bridge and positive
full-split quadratic kinetic routes. They leave one precise constructive horn:
select a compact subgroup, accept reduced symmetry, compute its nonuniform
charges on the actual principal-series carrier and test compatibility with an
interacting constraint complex.

The positive route would show that the compact escape is mathematically real
rather than a verbal loophole. The negative route would find that no spherical
K-type carries the needed nonuniform weights or that the charge operator cannot
share even a dense invariant core with the gauge/BV algebra. Either answer
changes whether a source-selected compact reduction is worth seeking. A typed
nonlinear/nonlocal source observation map is the strongest independent
challenger, but no released kernel is available to test.

## K1356: explicit compact circle and positive kinetic control

For the connected spin group, take

```text
K = (Spin(7) x Spin(7))/diagonal{plus_or_minus 1}.
```

Inside the first factor select

```text
C = {[exp(alpha e1e2),1] : alpha in R/(2 pi Z)}.
```

In the vector representation `exp(alpha e1e2)` rotates the first coordinate
plane by angle `2 alpha`. At `alpha=pi` its spin lift is the nontrivial class
`[-1,1]`; at `alpha=2 pi` it is the identity. Thus this is a genuine primitive
circle in `K`, not the full-group character excluded by K1351.

The projected vector generator is `J12=E12-E21`, so

```text
Tr(J12^2) = -2,            -Tr(J12^2)/2 = 1.
```

The negative Killing form is positive on the compact algebra and hence on
this circle. A circle-valued curvature therefore has an exact positive
quadratic kinetic form. The price is explicit: the choice preserves the
circle centralizer, not full split `G`, and neither the coordinate plane nor
its normalization is source selected.

## K1357: an actual spherical K-type has nonuniform charges

The compact picture is `H_ps=L2(K/M)`. Consider

```text
V = Sym^2_0(R^7_C) tensor 1,
```

the 27-dimensional trace-free quadratic representation of the first compact
factor. The split spherical subgroup `M` acts by simultaneous even sign
changes. Its diagonal quadratics give a six-dimensional trace-free fixed
space, so Peter--Weyl and Frobenius reciprocity place `V` in `L2(K/M)` with
multiplicity `dim V^M=6`.

Under `C`, the vector weights are `(+2,-2,0,0,0,0,0)`. The symmetric square
has multiplicities

```text
q       -4   -2    0   +2   +4
Sym^2    1    5   16    5    1
Sym^2_0  1    5   15    5    1.
```

Thus one irreducible spherical K-type already contains neutral and four
nonzero charge sectors. This is the nonuniform structure K1352 left open. A
fixed nonzero sector is not full-`G` invariant, and no row is identified with
a released source field or observed particle.

## K1358: the full charge generator is self-adjoint and unbounded

Restriction of the unitary principal series gives a strongly continuous
circle representation

```text
U(alpha) = exp(i alpha Q).
```

Stone's theorem makes `Q` self-adjoint. Because `C` has period `2 pi`,
`H_ps` decomposes into integer charge spaces `H_q`, and

```text
D(Q) = {v=sum_q v_q : sum_q q^2 ||v_q||^2 < infinity}.
```

The algebraic K-finite vectors form a dense invariant core and every such
vector is a finite charge sum. The operator is nevertheless unbounded. For
every `n>=1`, the M-spherical harmonic K-type
`Sym^(2n)_0(R^7_C) tensor 1` occurs: the harmonic projection of `x1^(2n)` is
nonzero and M-fixed. Its extreme circle charges are `plus_or_minus 4n`.
Consequently the spectrum is unbounded in both signs. Normalized vectors at
charges `q_n=4n` with coefficients `1/n` define a Hilbert vector but not a
`D(Q)` vector.

This is a new functional debt, not a defect in the finite K-type control.
K1346's scalar charge was bounded everywhere; the compact reduction replaces
it with a genuine unbounded internal generator whose graph domain must be
preserved by the completed dynamics.

## K1359: interacting gauge and BV-BFV algebra on one common core

On `M=R x T3`, use the common algebraic core

```text
C_c^infinity(R;C^infinity(T3)) algebraic_tensor H_Kfin
```

and define

```text
D_mu phi = partial_mu phi + i A_mu Q phi,
phi' = exp(i alpha Q) phi,
A' = A - d alpha.
```

Because the K-finite core is circle invariant and `Q` is bounded on each
finite K-type summand,

```text
D'_mu phi' = exp(i alpha Q) D_mu phi
```

holds exactly on the core. The K1346 scalar-electrodynamics action therefore
has an operator-charge analogue with nonzero current
`Im<phi,Q D_mu phi>` and seagull term `A_mu A^mu ||Q phi||^2`. For nonnegative
mass squared and quartic coupling its classical core energy is the sum of
nonnegative electric, magnetic, covariant-gradient, mass and quartic terms.

The formal BRST rules are

```text
sA = dc,       s phi = i c Q phi,       sc = 0.
```

They are nilpotent because the odd ghost squares to zero and `Q` commutes with
itself. The minimal BV antifield couplings close the classical master equation
formally, and the boundary BFV charge is the ghost paired with the Q-weighted
Gauss constraint. This proves algebraic compatibility on one dense invariant
core. It does not prove that the nonlinear flow preserves a completed graph
domain, that the KT image is closed, or that the global physical quotient is
a positive Hilbert space.

## K1360: updated admission boundary

The bridge census now has 37 rows: 24 satisfied, four conditional, five
excluded and four missing. Six mathematical control rows are new: the explicit
compact circle, its positive kinetic form, an M-spherical nonuniform charge
decomposition, the unbounded self-adjoint integer generator, the dense
K-finite core and the repository-owned operator-charge gauge/BRST/BV-BFV
algebra on that core.

The same four source/physical rows remain missing:

- source-owned selection and normalization of the compact reduction on the
  actual observed carrier;
- identification with one source-action-derived interacting constraint
  complex;
- a closed global nonlinear BV-BFV quotient with positive physical Hilbert
  cohomology; and
- a source-owned observed-state/export map.

K1145/K1150 remain `0/7` for native candidates. SC-ACT-01/02/06 remain
`ASSERTS`, SC-META-53 remains `UNCERTAIN`, and LT-SM8/LT-GR6b/RA-F1/AC-F1
remain `NEEDS`.

## Postflight hostile review

The strongest overclaim is that a maximal-compact reduction has now been
derived from GU. It has not: one coordinate circle was deliberately selected
to test mathematical feasibility. The strongest charge objection is that
the displayed even charges are a normalization artifact of the spin cover.
That is true as a warning, not a failure: the normalization is stated, and the
durable result is nonuniform integral spectrum after a genuine circle is
fixed. Hypercharge normalization remains unowned.

The strongest functional objection is that `Q` is unbounded. K1358 makes that
the central conclusion. K1359 works on the dense invariant K-finite core and
does not promote formal closure to a completed nonlinear theory. The strongest
symmetry objection also survives: each nonzero charge sector retains only the
circle centralizer, not the full irreducible split-group action.

The useful result is therefore exact but conditional. The compact route is no
longer merely possible in words; it has a positive kinetic control, actual
spherical charge sectors and an interacting algebraic realization. Its next
obligation is source ownership plus completed unbounded-domain dynamics.

## Exact next input

The next decisive input is a source/action-derived reduction datum on the
actual observed carrier that selects a compact generator or Cartan majorant,
fixes its normalization and proves that the source constraint/observation maps
preserve `D(Q)` and its charge decomposition. Given that datum, close the
operator-valued covariant derivative and nonlinear flow on one common graph
domain, prove global causal evolution and a closed KT/BV-BFV quotient, and
test positivity/nontriviality of the resulting physical Hilbert cohomology.

The independent alternative remains a typed nonlinear, differential,
integral or distributional map from released source section spaces to the
principal-series carrier; it must specify its domain, equivariance reduction,
action owner and observed semantics rather than evade K1353 by name alone.
