---
artifact_type: exact_regular_real_cartan_and_product_globalization_obstruction_result
created: 2026-08-14
status: REGULAR_CARTAN_SPLIT5_COMPACT2__UNTWISTED_PRODUCT_98_OBSTRUCTED__TWISTED_MINIMAL_REALIZATION_OPEN
source_return: SOURCE_CONFIRMS_ENDPOINT_TRACE_DUAL_AND_ACTION_SCALING__SOURCE_SILENT_EDGE_CARRIER_BOUNDARY_FUNCTIONAL_GLOBALIZATION_AND_DOMAIN
ledger_rows: [RA-G2, LT-SM3, AC-F1, AC-G1a]
registry: lab/process/selected-k77-regular-cartan-global-realization-obstruction.json
canon_verdict_change: none
---

# Selected K77 regular-Cartan globalization obstruction

## Result first

The actual nonzero regular endpoint is not split-regular.  For its exact
trace-dual `L in so(7,7)`, the characteristic polynomial is even.  Writing

```text
det(x-L)=q(x^2)
```

gives a squarefree degree-seven rational polynomial.  Exact real-root
isolation—not floating eigenvalue classification—finds five positive and two
negative roots of `q`.  Thus `L` has five real eigenvalue pairs and two purely
imaginary pairs.  Its seven-dimensional real Cartan centralizer has type

```text
(split rank, compact rank) = (5,2).
```

This decides the first global route.  The tempting sharp construction

```text
(one regular orbit family) x T*R^7,       dimension 84+14=98,
```

cannot globalize as an **untwisted product family** carrying the KKS form on
every orbit in a chamber containing the action-owned scaling line.  The two
compact-circle directions of the stabilizer give a rank-two real KKS period
space.  Under `L -> lambda L`, those nonzero periods scale with `lambda`.
But the restrictions of one closed two-form on a product fibration have a
locally constant fibrewise de Rham class.  The varying KKS classes contradict
that requirement.

The sharp local lower bound remains 98.  This result does **not exclude** a
twisted or monodromic 98-dimensional equivariant realization whose total
space is not the rejected product, nor does it prove a larger minimum.  The
smallest global equivariant carrier therefore remains open in `[98,182]`,
with `T*Spin(7,7)` still the canonical 182-dimensional fallback.

## Exact Cartan certificate

The predecessor constructs `L` over the rationals from all 91 endpoint charge
components through the nondegenerate vector trace form.  Its characteristic
polynomial contains only even powers.  Passing to `q(y)` avoids numerical
classification of fourteen roots.  Exact rational isolating intervals give

```text
negative roots of q: 2
positive roots of q: 5
zero roots of q:     0
all multiplicities: 1.
```

Positive `y` yields a real hyperbolic pair `+/-sqrt(y)`; negative `y` yields
an elliptic pair `+/-i sqrt(-y)`.  Squarefreeness and the already-certified
seven-dimensional abelian centralizer make this a regular real Cartan with
five split and two compact directions, rather than the maximally split
Cartan silently assumed by the easiest chamber model.

## Why the product obstruction is topological

Let `H^0` be the identity component of the endpoint stabilizer.  At the
classified fixture it has the real type

```text
H^0 ~ (R_{>0})^5 x (S^1)^2.
```

The compact torus lattice has rank two.  In the fibration
`H -> Spin(7,7) -> Spin(7,7)/H`, its lattice supplies two real two-cycle
directions on the orbit (finite fundamental-group effects do not change the
rank).  The KKS class pairs with these cycles by the compact components of
the orbit covector.  Those components are nonzero here and scale along the
exact action-owned line `(B,T)->lambda(B,T)`.

For a closed form `Omega` on an untwisted product `O x C x R^7`, the class of
`Omega|_{O x {c,p}}` is constant under the canonical identification of fibre
cohomology.  It therefore cannot equal a family of KKS classes with changing
rank-two periods.  Adding the canonical `dc_i wedge dp_i` term fixes local
Poisson nondegeneracy but not this global cohomology mismatch.

## Route comparison and hostile boundary

- **Exact invariant/Lie theory** beats numerical eigenvalue inspection and
  proves the actual Cartan type.
- **Orbit topology** kills the simplest 98-dimensional global product without
  claiming that topology kills every minimal realization.
- **Twisted coupling or monodromy** remains the live minimal horn.  It must
  construct a genuine Hamiltonian `Spin(7,7)` space and equivariant moment
  map, not merely rename local coordinates.
- **Cotangent-group geometry** remains the guaranteed global fallback at 182.
- **Variational/source ownership** remains unchanged: neither mathematical
  carrier is printed by the selected action or source.

The strongest overclaim would be a universal no-go for dimension 98.  The
argument proves no such statement: it rejects one globally trivial orbit
family.  Conversely, the strongest contrary shortcut would ignore the two
compact directions and reuse the split-Cartan product; the exact spectrum
forbids that at this fixture.

No boundary kinetic term, global edge bundle, polarization, Green domain,
positive pairing, reduced phase space or physical cohomology is constructed.
No ledger verdict, residue, quotient, datum, canon claim, W/mirror choice,
chirality, generation count or public posture changes.  Weinstein's total
target remains non-chiral.

## Next gate

Construct or obstruct a twisted/monodromic 98-dimensional equivariant
realization for real Cartan type `(5,2)`, or construct the best global carrier
strictly below the 182-dimensional cotangent-group fallback.  Only a surviving
carrier should then be compared with charged boundary symmetry and tested for
source/action ownership before analytic BFV work.

## Reproduction

```sh
sage -python \
  tests/channel-swings/selected_k77_regular_cartan_global_realization_obstruction_probe.py
```

The probe replays the exact 37-check predecessor and certifies the even
characteristic polynomial, squarefree squared-spectrum polynomial, exact
five-positive/two-negative root split, Cartan type, product-obstruction scope,
source ceiling and hostile controls.
