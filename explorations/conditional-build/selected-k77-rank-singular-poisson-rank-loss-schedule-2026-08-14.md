---
title: "Selected-K77 rank-singular Poisson rank-loss schedule"
status: conditional_result
doc_type: exact_structural_gate
created: "2026-08-14"
claim_grade: "EXACT POINTWISE NECESSARY RANK SCHEDULE; NO GLOBAL RSAP EXISTENCE"
canon_verdict_change: none
---

# Selected-K77 rank-singular Poisson rank-loss schedule

## Target

Let

```text
J : (M^m, omega) -> (so(7,7)*, pi)
```

be the typed RSAP candidate: one smooth surjective Poisson map, submersive on
the regular locus, with differential rank allowed to fall on singular strata.
At `x in M`, write

```text
p = J(x),  s = rank(dJ_x),  r = rank(pi_p).
```

The question is what rank loss is forced before attempting a global wall
attachment.

## Pointwise theorem

Define the Hamiltonian span

```text
W = omega^sharp(im(dJ_x)^*) subset T_x M.
```

Then `dim W=s`, and Poisson compatibility identifies the restriction of
`omega` to `W` with the pullback of `pi_p`. Its rank is at most `r`, so

```text
dim rad(omega|W) >= s-r.
```

Also `W^omega=ker(dJ_x)`. Hence the radical lies in a space of dimension
`m-s`, giving

```text
s-r <= m-s,
2s <= m+r,
s <= floor((m+r)/2).
```

For the 91-dimensional target the differential-rank deficit therefore obeys

```text
delta = 91-s >= max(0, 91-floor((m+r)/2)).
```

Because both `m` and Lie--Poisson rank `r` are even here, the positive branch
is `(182-m-r)/2` exactly.

## Exact schedule

| target stratum | `r` | `m=98` ceiling for `s` | forced deficit `91-s` |
|---|---:|---:|---:|
| regular | 84 | 91 | 0 |
| first rank-drop wall | 82 | 90 | at least 1 |
| zero charge | 0 | 49 | at least 42 |

Thus a minimal 98-dimensional RSAP cannot cross the first rank-82 wall while
remaining a submersion: at least one differential direction must die there.
At zero charge its differential rank is at most 49.

For a general even `m` in `[98,182)`, the first rank-82 wall forces loss only
when `m=98`; `m>=100` is not decided there by this inequality. Every
below-182 candidate is nevertheless forced to lose rank by zero charge:

```text
rank(dJ_x) <= m/2 < 91  when J(x)=0.
```

This corrects two tempting overextensions: rank loss at the first wall is not
forced for every dimension below 182, and the pointwise schedule does not
construct a smooth surjective map.

## Sharpness at tangent-space grade

The inequality is exact as symplectic linear algebra. In a symplectic vector
space with `m=2n`, choose `r/2` complete symplectic pairs and `s-r` additional
unpaired isotropic basis vectors. Their span has dimension `s`, restricted
form rank `r`, and fits precisely when

```text
r/2 + (s-r) <= n  <=>  2s <= m+r.
```

The triples `(98,91,84)`, `(98,90,82)` and `(98,49,0)` all saturate the
inequality. This proves there is no stronger obstruction from pointwise
symplectic linear algebra alone. It does not provide the nonlinear Poisson,
smoothness, surjectivity, equivariance or gluing data.

## Construction consequence

The first minimal-carrier wall packet is now typed:

1. start from the exact 98-dimensional regular Cartan component;
2. supply a local smooth Poisson normal form whose map rank changes `91->90`
   as target Poisson rank changes `84->82`;
3. match the regular symplectic form and moment map on the overlap;
4. prove smoothness and Poisson compatibility across the wall;
5. retain enough later degeneration to reach rank at most 49 over zero.

Failure of this local normal form obstructs the 98-dimensional attachment,
not all RSAP dimensions. Success is only a local wall admission.

## Verdict ceiling

This is an exact necessary and tangent-space-sharp rank schedule. RSAP
existence, a global all-charge carrier, stationary GU background, physical
reduction, ledger row, canon verdict and public posture remain unchanged.
