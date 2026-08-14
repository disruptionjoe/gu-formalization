---
artifact_type: exact_regular_semisimple_global_symplectic_realization
created: 2026-08-14
status: COMPLETE_REGULAR_SEMISIMPLE_LOCUS_GLOBAL_MINIMUM_98_CONSTRUCTED__DISCONNECTED_CARTAN_ATLAS__SINGULAR_STRATA_OPEN
registry: lab/process/selected-k77-regular-semisimple-cartan-atlas-realization.json
canon_verdict_change: none
---

# Selected-K77 regular-semisimple Cartan-atlas realization

## Result first

The sharp `98`-dimensional Cartan-slice construction is not special to the
selected real Cartan type `(5,2)`. It globalizes over the **complete regular-
semisimple locus** as a finite, generally disconnected Cartan atlas.

For each representative real Cartan subalgebra `h` of
`g=so(7,7)` and each connected regular chamber `C subset h*`, set

```text
M_C = Spin_0(7,7) x C subset T*Spin_0(7,7),
theta_C = <lambda,g^-1 dg>,
omega_C = d theta_C,
J_C(g,lambda) = Ad*_g(lambda).
```

Every component is exact symplectic of dimension `91+7=98`; `dJ_C` has rank
`91` and seven-dimensional right-Cartan fibres. Taking the disjoint union of
these components over the finitely many real-Cartan conjugacy and chamber
types gives a global equivariant symplectic realization of every regular
semisimple covector. Since the regular Poisson lower bound is `98`, this is
the global minimum on the complete regular-semisimple locus.

The construction does not cover singular charges. The all-strata minimum
remains open in `[98,182]`, with `T*Spin_0(7,7)` the canonical all-charge
fallback.

## Type-independent proof

At a regular `lambda`, the trace form gives

```text
g = h direct-sum [g,lambda].
```

The Kirillov block is nondegenerate on the `84` orbit directions and has
kernel `h` of dimension seven. The seven chamber-momentum directions pair
nondegenerately with that kernel. In a Cartan-adapted basis the two-form is

```text
        [ -K_lambda  -E ]
Omega = [                ],
        [    E^T      0 ]
```

where `rank K_lambda=84` and `rank E=7`, hence `rank Omega=98` independent
of the split/compact signature of the real Cartan. Likewise

```text
dJ = [K_lambda E]
```

has rank `91`. The exact probe verifies the block theorem under three
different Cartan-pairing signatures.

Every regular semisimple element has a real Cartan centralizer, and real
reductive groups have finitely many Cartan conjugacy classes; deleting the
root walls leaves finitely many connected chambers. Their `Ad*` saturations
cover the regular-semisimple locus. Disconnectedness is allowed for a
symplectic realization and is stated explicitly.

## Relation to the product obstruction

This does not revive the rejected orbit-product family. At fixed `lambda`,
`G x {lambda}` is presymplectic of rank `84`, with the right-Cartan fibre
retained upstairs. Its quotient is the KKS orbit. The compact-period variation
therefore remains compatible with an exact form upstairs and still obstructs
the different untwisted product-of-orbits construction.

## Singular and physical ceiling

At the zero singular wall the same seven slice directions give rank `14`, not
`98`; regularity is load-bearing. Gluing across singular orbit-type walls,
constructing another all-strata carrier below dimension `182`, and proving a
connected carrier are all open.

The source and selected action do not own this Cartan atlas, an edge kinetic
term, a boundary admission law, an analytic domain, prequantization, positive
pairing or physical quotient. No W/mirror choice, chirality, generation count,
ledger, canon, residue, quotient, datum or public-posture change follows.

## Reproduction

```bash
uv run --with-requirements requirements.txt python \
  tests/channel-swings/selected_k77_regular_semisimple_cartan_atlas_realization_probe.py
```

The exact structural certificate passes `27/27`.
