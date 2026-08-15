---
title: "Selected-K77 RSAP split A2/A3 common refinement"
status: active_research
doc_type: exact_regular_symplectic_transition_construction
created: "2026-08-15"
registry: lab/process/selected-k77-rsap-a2-a3-common-refinement.json
probe: tests/channel-swings/selected_k77_rsap_a2_a3_common_refinement_probe.py
grade: "ONE COMPLETE CONNECTED SPLIT A2/A3 BIG-CELL TRANSITION AND FIRST A2/A3/A2 TRIPLE CONSTRUCTED; OTHER COMPONENTS AND SINGULAR GLUING OPEN"
canon_verdict_change: none
---

# Selected-K77 RSAP split `A2/A3` common refinement

## Result first

The first higher-root transition constructs on one complete connected split
regular Gauss big-cell component. The common target is

```text
sl(4,R)^*_regular x R4_zero,
```

of dimension `19`, Poisson rank `12` and corank `7`. Its minimal symplectic
realization therefore has dimension `19+7=26`. Relative to the common `72D`
leaf, the two existing descriptions are exactly

```text
A2 side: O6 x X10(A2) x T*R5,
A3 side:      X18(A3) x T*R4.
```

The transferred `O6` is three regular-leaf Darboux pairs. It is not a new
factor. Together with the three leaf pairs and two invariant pairs in
`X10(A2)`, it supplies the same six leaf pairs and seven invariant pairs as
the `A3` refinement. Both sides identify with one universal `26D` model.
The frozen transition is an explicit complete-pair permutation. It preserves
the symplectic tensor, all `19` moment components and the tautological
primitive strictly.

The earlier `A1/A2` result was local because no global section had been typed.
For the present split higher-root gate, fix one sign choice and the ordered
regular chamber inside the `SL(4,R)` Gauss big cell. Its six unipotent root
coordinates, three logarithms of positive principal minors, and invariant
coordinates form a single Euclidean cell. The relative normalizations are
therefore global on that complete connected overlap component. Their
cotangent lifts preserve the tautological one-form by definition, and the
component has no loop on which a primitive monodromy class could survive.

The first root-adapted `A2/A3/A2` triple also closes on this component. Its
successive pair maps do not commute, but all three arise from normalizations
through the same universal realization. Their ordered product telescopes to
the identity, so the full moment and primitive Cech defects vanish exactly.

This is not every split regular component. Other sign choices, lower Bruhat
cells that are still regular, compact and mixed `A3` forms, singular
centralizer jumps, zero charge and a global all-strata RSAP remain open.

## The common regular target

On the regular locus of `sl(4,R)^*`, the stabilizer has rank three, so the
Lie--Poisson tensor has rank `15-3=12`. Adjoining four central coordinates
gives local target coordinates

```text
(q1,...,q6,p1,...,p6,c1,...,c7),
```

with six leaf Darboux pairs and seven Casimirs. The universal minimal
realization is

```text
U26 = (q_i,p_i,c_a,t_a),
omega = sum_i dqi wedge dpi + sum_a dca wedge dta,
J(q,p,c,t) = (q,p,c),
theta = sum_i pi dqi + sum_a ta dca.
```

The executable certificate verifies `rank(dJ)=19`,
`dJ Pi_U dJ^T=pi_19`, and nondegeneracy of `Pi_U`.

## Exact factor accounting

Relative to the common `72D` leaf, the `A2` side groups the coordinates as

```text
O6       = (q1,p1,q2,p2,q3,p3),
X10(A2)  = (q4,q5,q6,p4,p5,p6,c1,c2,t1,t2),
T*R5     = (c3,t3,...,c7,t7).
```

The split principal-`A3` side groups the same coordinates as

```text
X18(A3) = (q1,...,q6,p1,...,p6,c1,c2,c3,t1,t2,t3),
T*R4    = (c4,t4,...,c7,t7).
```

Thus `O6` supplies exactly the three orbit pairs gained when the rank-six
`A2` leaf is replaced by the rank-twelve `A3` leaf. The third `sl4` invariant
is promoted from the old centre block into `X18(A3)`; total invariant-pair
count remains seven.

Let `kappa_A2` and `kappa_A3` be the displayed normalizations to `U26`. Then

```text
Phi = kappa_A3^-1 composed with kappa_A2
```

is a `26 x 26` permutation of complete canonical pairs. The exact probe checks
the full symplectic and moment squares. A different invariant section may
shift `t -> t+A c` with `A=A^T`; this changes the primitive only by
`d(half c^T A c)`.

## Globality on one connected split big-cell overlap

Fix the identity Bruhat cell, one sign component of its nonzero principal
minors, and one ordering of the four distinct real eigenvalues. Gauss
factorization is unique there. After absorbing the fixed signs, the diagonal
coordinates are three positive ratios `a1,a2,a3`; writing `ui=log(ai)` gives
`R3`. The six strict-triangular entries give `R6`. The ordered invariant
chamber is also an open convex cell. Hence the complete selected overlap
component is contractible.

The `A2` and `A3` base coordinate systems are related by ordinary root shears
and regrouping inside this one Gauss factorization. These are global
diffeomorphisms on the selected component. For any base transition
`x'=f(x)`, the cotangent lift is

```text
x'=f(x),        xi'=(Df(x))^(-T) xi,
```

and therefore `xi'^T dx'=xi^T dx` identically. No logarithm branch changes
inside the fixed positive-minor component. This is enough for strict global
primitive and moment compatibility there; it does not glue another sign or
Bruhat component.

## First noncommuting `A2/A3/A2` triple

Choose two `A2` root embeddings on the sides of the `A3` chart and normalize
all three through `U26`. The probe uses two distinct complete-pair
permutations. The successive maps fail to commute, while

```text
Phi_31 Phi_23 Phi_12 = identity.
```

Every full moment square commutes and every primitive pullback is strict, so
both Cech defects are zero on the selected component. Noncommutativity alone
does not create a gluing obstruction.

## Claim ceiling and next gate

- One complete connected split regular Gauss big-cell component constructs.
- The full carrier remains `72+26=98D` with regular map rank `91`.
- Other split sign and Bruhat components remain unclassified.
- Compact and mixed `A3` forms, singular centralizer jumps, zero charge and
  global RSAP remain open.
- No canon, ledger, residue, quotient datum, physical claim or public posture
  changes.

Next classify the remaining split regular components and their transition
cocycles. Only after those glue should the construction cross the first
singular centralizer jump.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k77_rsap_a2_a3_common_refinement_probe.py
```

The probe uses exact integer and rational linear algebra only.
