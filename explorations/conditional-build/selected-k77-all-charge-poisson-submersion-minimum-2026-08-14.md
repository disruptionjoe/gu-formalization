---
artifact_type: exact_all_charge_poisson_submersion_minimum
created: 2026-08-14
status: ALL_CHARGE_POISSON_SUBMERSION_MINIMUM_EXACTLY_182__WEAKER_SINGULAR_MAP_CLASS_OPEN
probe: tests/channel-swings/selected_k77_all_charge_poisson_submersion_minimum_probe.py
registry: lab/process/selected-k77-all-charge-poisson-submersion-minimum.json
canon_verdict_change: none
---

# Selected-K77 all-charge Poisson-submersion minimum

## Result first

The all-charge symplectic-realization interval closes exactly in the standard
Poisson-submersion class:

```text
complete regular-semisimple locus: minimum 98,
all of so(7,7)*:                  minimum 182.
```

Let `J:M->P` be a Poisson submersion from a symplectic manifold to the
91-dimensional Lie--Poisson target. At `x` over `p`, the Hamiltonian lifts of
the 91 independent target covectors span a 91-dimensional subspace `W`. The
restriction of the symplectic form to `W` has rank `rank(pi_p)`. Its radical
therefore has dimension `91-rank(pi_p)` and lies in
`W^omega=ker(dJ)`, whose dimension is `dim(M)-91`. Hence

```text
dim(M) >= 91 + corank(pi_p) = 182-rank(pi_p).
```

On the regular locus `rank(pi)=84`, reproducing the sharp lower bound 98. At
the zero coadjoint orbit `rank(pi_0)=0`, any Poisson submersion covering zero
has dimension at least 182. The canonical cotangent moment map
`T*Spin_0(7,7)->so(7,7)*` has dimension 182 and covers every charge, so the
bound is attained.

## Scope correction

This theorem is pointwise and does not require the carrier to be connected.
It also explains why gluing the 98-dimensional regular Cartan atlas cannot
produce an all-charge Poisson submersion without increasing dimension.

It does not obstruct a weaker Poisson map whose differential ceases to be
surjective at singular charges. Such a map is not a symplectic realization in
the standard submersion sense and must be typed as a different target class
before a below-182 search begins.

The construction is mathematical, not source- or action-owned. No boundary
action, analytic domain, prequantization, positive pairing, physical quotient,
ledger, canon, residue, datum or public-posture move follows.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k77_all_charge_poisson_submersion_minimum_probe.py
```
