---
title: "Selected-K96 RSAP connected-orbit normalizer refinement"
status: active_research
doc_type: exact_connected_orbit_refinement_and_classical_rsap_construction
created: "2026-08-15"
registry: lab/process/selected-k96-rsap-connected-orbit-refinement.json
probe: tests/channel-swings/selected_k96_rsap_connected_orbit_refinement_probe.py
grade: "CONNECTED REFINEMENT CLOSED; CLASSICAL 98D RSAP CONSTRUCTED AT THE EXACT MINIMUM"
canon_verdict_change: none
---

# Selected-K96 RSAP connected-orbit normalizer refinement

## Result first

The K95 connected-orbit seam closes uniformly, without a 3,691-row component-
group census. Let

```text
G = SO_0(7,7),
Q = diag(I_7,-I_7),
p_0 = {X in so(Q): R_0 X + X R_0 = 0},
```

where the `+1` and `-1` eigenspaces of `R_0` have signatures `(3,4)` and
`(4,3)`. The normalizer of `p_0` contains a reflection in one positive
coordinate and an independent reflection in one negative coordinate. They
commute with `R_0`, preserve `p_0`, and generate all four components

```text
O(7,7)/SO_0(7,7) = Z/2 x Z/2.
```

Consequently every connected `SO_0(7,7)` adjoint orbit inside every K88--K95
structurally covered `O(7,7)` class still meets the same fixed complement
`p_0`. Hence

```text
Ad(SO_0(7,7)) p_0 = so(7,7).
```

The canonical cotangent moment map on
`T*(Spin_0(7,7)/H_bal)` is therefore surjective. It has dimension `98`, rank
`91` over the complete regular locus, rank `49` over zero, and the K95 sharp
singular schedule `(189-c)/2`. This is a classical RSAP at the exact minimum
dimension `98`. The stronger everywhere-submersive all-charge problem remains
minimum `182`; the two results are not conflated.

## The component argument

The four components of `O(7,7)` are labelled by the two orientation signs in
the maximal compact deformation retract `O(7) x O(7)`. With the K88 coordinate
order, choose

```text
k_+ = diag(-1,1,...,1)       on one Q-positive coordinate,
k_- = diag(1,...,1,-1,1,...) on one Q-negative coordinate.
```

Both are `Q`-orthogonal. Because they are diagonal in the `R_0` decomposition,
they commute with `R_0`; conjugation by either therefore preserves `p_0`.
Their component labels are `(-,+)` and `(+,-)`, while `1` and `k_+k_-` give
`(+,+)` and `(-,-)`. Thus the component map from the normalizer is onto.

Now fix `Y in p_0`. Any point in its full orthogonal orbit is
`Z=oYo^-1` for some `o in O(7,7)`. Choose a normalizer representative `k` in
the same ambient component as `o`. Then

```text
g = o k^-1 in SO_0(7,7),
k Y k^-1 in p_0,
Z = g (k Y k^-1) g^-1.
```

So the connected `G`-orbit of `Z` meets `p_0`. If the real centralizer merges
some component labels, it only merges already-covered orbits; no centralizer
connectedness assumption is used.

## Composition with K88--K95

- K88 constructs the smooth balanced symmetric horn, identifies
  `h_bal^perp=p_0`, reaches zero with map rank `49`, and covers every regular
  semisimple Cartan type.
- K89 covers all `99` connected pure nilpotent classes, including both
  principal regular classes.
- K90 covers the complete regular nonsemisimple locus.
- K91--K95 close every singular mixed structural layer; K95 totals `4,348`
  structural rows with zero balanced-signature failures.
- The normalizer lemma upgrades structural `O(7,7)` coverage to every
  connected `SO_0(7,7)` refinement at once.

For regular points of `p_0`, the symmetric-space rank is seven, equal to the
ambient Lie rank. Their seven-dimensional centralizer lies in `p_0`, so the
`h_bal` centralizer is zero and the cotangent moment differential has full
rank `91`. This agrees with the independent K88--K90 exact certificates.

## RSAP consequence

An RSAP is one smooth surjective Poisson map that is submersive on the regular
coadjoint locus and may lose rank on singular strata. The independent lower
bound is `91+7=98`. The balanced horn is smooth and symplectic, its canonical
moment map is Poisson, K96 proves it surjective, and its regular differential
rank is `91`. Therefore the RSAP minimum is exactly `98`.

This does not alter the separate pointwise lower bound `182` for a map that is
a submersion at zero and hence everywhere across all charges. K96 constructs
the weaker rank-singular target exactly as defined.

## Claim ceiling

This is an independent classical Hamiltonian construction. The source does not
select `H_bal`, this cotangent carrier, or its global attachment to the actual
GU action. No BFV reduction, positivity, quantum state space, particle content,
phenomenology, Higgs, family-index, chirality, datum, ledger or public-posture
claim follows.

The next gate is source/action ownership: derive or obstruct selection and
global attachment of `H_bal` from the actual source-owned action before giving
this exact mathematical RSAP any physical interpretation.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k96_rsap_connected_orbit_refinement_probe.py
```
