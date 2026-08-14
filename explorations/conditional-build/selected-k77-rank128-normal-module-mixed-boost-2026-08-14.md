---
artifact_type: exact_anti_redo_composition_and_convention_result
created: 2026-08-14
status: HELD_V0228_FULL_NORMAL_MODULE_RECONFIRMED__VECTOR_COVECTOR_SIGN_FORK_EXACT__SELECTED_GRAPH_ONLY_COMPACT_NATURAL
target_claim: NONE-NOT-A-KILL
source_return: lab/sources/selected-k77-rank128-normal-module-mixed-boost-source-return-2026-08-14.md
registry: lab/process/selected-k77-rank128-normal-module-mixed-boost.json
probe: tests/channel-swings/selected_k77_rank128_normal_module_mixed_boost_probe.py
hostile_review: lab/process/hostile-reviews/2026-08-14-selected-k77-rank128-normal-module-mixed-boost-review.md
canon_verdict_change: none
ledger_row_changes: none
---

# Selected K77 rank-128 normal module and mixed boosts

## Result first

The proposed mixed-boost carrier gate was already closed by the held v0.228
result. The ten transverse rank-128 defects are pairwise disjoint and their
direct sum is exactly

```text
ker(R_obs) = N*X tensor S,            dimension 10 x 128 = 1280.
```

The canonical coordinate inclusion of this normal-covector--spinor module
intertwines all 45 generators of `so(6,4)`. The predecessor's `21/45` result
does not obstruct the full carrier. It detects the particular selected H640
graph lift, its complementary projector and the zero-form-seed defect
trivialization, each of which is natural only for `so(6)+so(4)`.

The apparent `24/24` sign pattern has an exact characteristic-zero
explanation. If `A` is the normal vector generator, the normal covector action
is

```text
A_(N*) = -A^T = eta_(6,4) A eta_(6,4)^(-1).
```

Using `A` itself on a covector label accidentally agrees with `-A^T` for the
21 same-sign rotations and disagrees for all 24 mixed-sign boosts. Correcting
that vector/covector convention makes the canonical `N* tensor S` inclusion
equivariant `45/45`. It does **not** repair the selected graph: all 24 mixed
boosts still expose that splitting.

Thus the exact disposition is:

```text
full N* tensor S configuration carrier:   exact so(6,4) module
selected H640 graph/trivialization:        compact-natural only
ten independent carrier repairs:           superseded
one moving graph/BV naturality problem:     open
physical carrier/cohomology/domain:          open
```

No new ledger migration is warranted because v0.228 already booked this exact
scoped theorem.

## Anti-redo and object typing

The preflight compared the portfolio-correction probe, the v0.228 successor,
its ledger migration and the current rank-128 steering text. The held result
already states `FULL_SO6_4_MODULE_EXACT`; re-solving ten normalizations or
presenting the carrier theorem as new would duplicate settled work.

Five objects remain separate:

1. one rank-128 defect image `D_i`;
2. the direct sum of ten such images;
3. the canonical configuration module `N* tensor S = ker(R_obs)`;
4. the selected H640 graph and its zero-form-seed trivialization; and
5. a future action/BV-owned physical carrier or cohomology.

Equal dimension alone did not identify the module. The held certificate also
proves that every `D_i` lies in `ker(R_obs)`, their total rank is 1280, and the
observation kernel has dimension 1280. The new convention calculation explains
why the earliest attempted intertwiner showed precisely a compact/mixed split.

## Exact convention calculation

Work over `QQ` with the filed real `Cl(7,7)` gamma representation. The normal
axes have signature `(6,4)`. For each normal bivector `(i,j)`, let

```text
S_ij = (1/2) gamma_i gamma_j
```

and let `A_ij` be its vector representation. Exact sparse arithmetic verifies
all `45 x 14` Clifford covariance identities

```text
[S_ij, gamma(v)] = gamma(A_ij v).
```

On `N* tensor S`, the infinitesimal action is

```text
(-A_ij^T) tensor 1 + 1 tensor S_ij.
```

Because `A_ij^T eta + eta A_ij=0`, the metric identification between normal
vectors and covectors gives `-A_ij^T=eta A_ij eta^(-1)` for all 45 generators.
If that dualization is omitted, `A_ij=-A_ij^T` holds exactly for the 21
same-sign rotations and fails exactly for the 24 mixed boosts. This reproduces
the observed count without fitting any physics.

The held GF(1009) fixture then independently replays:

```text
rank D_i = 128                         for all ten i;
rank(D_i + D_j) = 256                  for all 45 pairs;
rank(sum_i D_i) = 1280;
sum_i D_i = ker(R_obs);
canonical N* tensor S inclusion:       45/45 intertwiners;
selected graph/zero-seed splitting:    21/45 intertwiners.
```

The earlier ambient-H640 carrier theorem also supplies a second-prime
`GF(1013)` control for the ten individual rank-128 transverse leaks. The
current convention theorem itself is in characteristic zero, so no finite
field is being used to decide the sign fork.

## What closes and what remains

Closed:

- the ten defects form one canonical full normal module;
- the 24 mixed failures are not a failure of that carrier;
- the vector/covector sign and metric-normalization convention is exact; and
- ten independent normalizations or ten carrier repairs are the wrong work
  unit.

Open:

- derive an action- or BV-owned moving graph correction intertwining the
  physical normal symmetry;
- or prove that the physical action/observation reduces normal symmetry to
  `U(3,2)` or the compact stabilizer already respected by the selected graph;
- build the actual physical carrier, BV/KT quotient, analytic domain, positive
  pairing and physical cohomology.

An arbitrary moving graph correction was not classified here. The result
therefore does not prove that no full-normal-natural graph can exist; it proves
that the filed selected graph is not one and that the carrier itself is not
the obstruction.

## Claim ceiling

`ker(R_obs)` is a configuration-level representation. It is not
`Pi_RS^phys`, a phase space, a chiral quotient, a positive Hilbert space, an
index, a generation count, a particle spectrum or a source-owned physical
law. No ledger row, verdict, residue coordinate, quotient, P1/P2/P3 datum,
canon claim or public posture changes.

## Reproduction

```sh
sage -python \
  tests/channel-swings/selected_k77_rank128_normal_module_mixed_boost_probe.py
```

The probe performs the characteristic-zero convention calculation, replays
the held exact defect/module certificate, and fires controls against both
carrier-to-physics and carrier-to-graph overclaims.
