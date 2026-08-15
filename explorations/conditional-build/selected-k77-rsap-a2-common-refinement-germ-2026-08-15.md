---
title: "Selected-K77 RSAP adjacent-A2 common-refinement germ"
status: active_research
doc_type: exact_regular_symplectic_transition_construction
created: "2026-08-15"
registry: lab/process/selected-k77-rsap-a2-common-refinement-germ.json
probe: tests/channel-swings/selected_k77_rsap_a2_common_refinement_germ_probe.py
grade: "ADJACENT A1/A2 REGULAR GERMS AND FIRST NONCOMMUTING TRIPLE GERM CONSTRUCTED; GLOBAL AND SINGULAR GLUING OPEN"
canon_verdict_change: none
---

# Selected-K77 RSAP adjacent-A2 common-refinement germ

## Result first

The previously type-missing 20-dimensional adjacent transition constructs on
every sufficiently small contractible piece of the common regular overlap.
The four transferred dimensions are exactly two Darboux pairs in the regular
`A2` coadjoint leaf. After extracting the common `78D` leaf, the two sides are

```text
rank-one refinement: O4 x X4(A1) x T*R1 x T*R5,
A2 refinement:       X10(A2) x T*R5.
```

Both are local minimal symplectic realizations of the same 13-dimensional
regular Poisson target `sl(3)^* x R5_zero`, whose rank is six and corank is
seven. Relative Darboux normalization identifies both with one universal
model. In frozen normal-form coordinates the transition is an explicit
`20 x 20` permutation that only regroups canonical pairs. It preserves the
symplectic form, strictly intertwines the complete moment map, and preserves
the primitive. A different local section changes the primitive only by the
exact differential of a quadratic Casimir function.

Using the same universal normalization for three adjacent root charts also
closes the first noncommuting triple at germ grade: the pair maps themselves
need not commute, but their ordered triple product telescopes to the identity,
and both moment and primitive Cech defects vanish.

This is not a global algebraic transition. Monodromy, section gluing, singular
extension, deeper strata, zero charge and global RSAP remain open.

## The common regular target

On the regular locus of `sl(3)^*`, the Lie--Poisson tensor has rank six and
two independent local Casimirs. Adjoining the five centre coordinates gives
local coordinates

```text
(q1,q2,q3,p1,p2,p3,c1,...,c7)
```

with

```text
pi = sum_i partial_qi wedge partial_pi,
```

and all seven `c_a` central. Therefore every minimal symplectic realization
has dimension at least

```text
13 + 7 = 20.
```

Both existing refinements attain this bound. The universal local realization
is

```text
U20 = (q_i,p_i,c_a,t_a),
omega = sum_i dqi wedge dpi + sum_a dca wedge dta,
J(q,p,c,t) = (q,p,c),
theta = sum_i pi dqi + sum_a ta dca.
```

Its moment differential has rank 13 and satisfies the full Poisson identity
`dJ Pi_U dJ^T=pi`.

## Identifying the four-dimensional transfer block

The rank-one description resolves one `A1` slice and one of the two `A2`
invariants while leaving two leaf pairs in the old `82D` leaf. Relative to
the common `78D` leaf, its transverse coordinates are

```text
O4       = (q1,p1,q2,p2),
X4(A1)   = (q3,p3,c1,t1),
T*R1     = (c2,t2),
T*R5     = (c3,t3,...,c7,t7).
```

The principal-`A2` description instead groups

```text
X10(A2)  = (q1,q2,q3,p1,p2,p3,c1,c2,t1,t2),
T*R5     = (c3,t3,...,c7,t7).
```

Thus the missing `O4` is not a new factor or imported degree of freedom. It
is the pair of regular-orbit canonical pairs that the rank-one chart had left
inside its larger leaf. The extra `T*R1` is the second local `A2` Casimir and
its conjugate; the other five cotangent pairs are the unchanged centre.

## The pair map and primitive

Let `kappa_A1` and `kappa_A2` be relative-Darboux normalizations of the two
minimal realizations to `U20`, chosen over one contractible regular target
patch. Then

```text
Phi = kappa_A2^-1 composed with kappa_A1
```

is the required common-refinement symplectomorphism and

```text
J_A2 composed with Phi = J_A1.
```

In the displayed coordinates `Phi` is exactly the permutation that regroups
the same ten canonical pairs from the rank-one block order into the `A2`
block order. The executable certificate checks the full `20 x 20`
symplectic identity and the full 13-row moment square, not dimensions alone.
The frozen primitives agree strictly.

A section change may shift the conjugate variables by

```text
t -> t + A c,   A=A^T.
```

This preserves `omega` and `J`, while

```text
theta_new - theta = d(1/2 c^T A c).
```

So the requested exact gauge term is also typed and controlled.

## First noncommuting triple germ

Choose three root-adapted normalizations `kappa_1,kappa_2,kappa_3` through the
same universal model and define

```text
Phi_ij = kappa_j^-1 composed with kappa_i.
```

The exact probe chooses symplectic root-coordinate permutations for which two
successive pair maps do not commute. Nevertheless

```text
Phi_31 Phi_23 Phi_12 = identity
```

by direct multiplication. Each square with the full moment map commutes and
the additive primitive defect is zero. Noncommutativity of the root subsystem
therefore creates no local Cech obstruction on a contractible regular patch.

## Hostile scope and claim ceiling

The strongest overclaim would replace “regular germ” with “global adjacent
chart.” Relative Darboux coordinates require local Casimir coordinates,
sections and a contractible patch; they do not supply a single algebraic
formula over the full regular overlap. The strongest contrary route is
monodromy or incompatible section changes around the discriminant. Nothing in
this packet kills that possibility. The weakest reproducibility seam is the
theorem-to-model bridge: the finite probe certifies the frozen normal form,
while existence of the normalizations uses the regular Poisson splitting and
relative Darboux theorem.

No singular wall, deeper stratum or zero-charge point is covered. No global
`98D` carrier, physical action, stationary background, cohomology, spectrum or
Standard Model result follows. The `182D` cotangent parent remains the
all-charge fallback. No ledger, canon, residue, quotient, datum or public
posture changes.

## Next exact gate

Globalize one adjacent pair map across its complete connected regular overlap.
Choose explicit group/cotangent sections for one real form, compute their
transition functions around the discriminant, and decide whether the exact
primitive gauges have zero monodromy. Only then attempt singular extension or
use the local triple result in a global atlas.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k77_rsap_a2_common_refinement_germ_probe.py
```

The probe uses exact integer and rational linear algebra only.
