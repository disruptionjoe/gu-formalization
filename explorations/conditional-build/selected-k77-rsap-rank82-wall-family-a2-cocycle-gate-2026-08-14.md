---
title: "Selected-K77 RSAP rank-82 wall family and A2 cocycle gate"
status: active_research
doc_type: exact_local_construction_and_candidate_obstruction
created: "2026-08-14"
registry: lab/process/selected-k77-rsap-rank82-wall-family-a2-cocycle-gate.json
probe: tests/channel-swings/selected_k77_rsap_rank82_wall_family_a2_cocycle_gate_probe.py
grade: "ALL ISOLATED REAL RANK-82 WALLS AND ORTHOGONAL COCYCLES CONSTRUCTED; NATURAL SPLIT-A2 CANDIDATE KILLED; GENERAL A2 AND GLOBAL RSAP OPEN"
canon_verdict_change: none
---

# Selected-K77 RSAP rank-82 wall family and A2 cocycle gate

## Result first

The `98`-dimensional RSAP program now crosses every isolated real rank-`82`
wall type and every orthogonal rank-two overlap. Its first orthogonal triple
cocycle also closes exactly. The first noncommuting overlap does not.

There are two real rank-one transverse factors at a rank-`82` first wall:

| derived centralizer | homogeneous cotangent factor | map rank | target rank |
| --- | --- | ---: | ---: |
| `sl(2,R)` | `T*(SL(2,R)/A)` | `3 -> 2` | `2 -> 0` |
| `su(2)` | `T*(SU(2)/U(1)) = T*S^2` | `3 -> 2` | `2 -> 0` |

Multiplying either factor by an `82`-dimensional symplectic leaf and
`T*R^6` gives the same exact `98`-dimensional first-wall schedule already
constructed for the split case. Thus the isolated real wall-family census is
complete at this local grade.

Because `D7` is simply laced, every nonparallel pair of its roots spans either
`A1 x A1` or `A2`. The orthogonal case factorizes and passes. For adjacent
roots, the natural minimal split candidate

```text
T*(SL(3,R)/SL(2,R))
```

has the right dimension, the right generic semisimple rank and the right rank
at the `A2` origin, but its moment differential has rank `7`, not `8`, over a
regular nilpotent value. In the complete `98`-dimensional product this is map
rank `90`, not the required regular-locus rank `91`. The candidate is rejected.

This is a candidate obstruction, not a universal `A2` no-go theorem. Global
RSAP existence remains open.

## Complete isolated-wall census

The regular centralizer in `so(7,7)` has dimension seven. A rank-`82` wall has
centralizer dimension nine, so its derived transverse part adds exactly two
real dimensions. The only real rank-one forms at that size are `sl(2,R)` and
`su(2)`, each accompanied by a six-dimensional centre. A genuinely complex
root pair adds at least four real centralizer dimensions and lands at target
Poisson rank at most `80`; it is not a first rank-`82` wall.

For the compact form, use the basis `(H,X,Y)` with

```text
[H,X]=Y,   [H,Y]=-X,   [X,Y]=H.
```

At `xi=(0,x,y)` in the annihilator of `u(1)=R H`, the cotangent differential
on `T*(SU(2)/U(1))` is

```text
       [  y  -x  0  0 ]
dmu =  [  0   0  1  0 ] .
       [  0   0  0  1 ]
```

Direct multiplication by the canonical source Poisson matrix gives the
`su(2)^*` Lie--Poisson matrix at `(0,x,y)`. Its rank is three off the zero
section and two on it, while the target Poisson rank is respectively two and
zero. Coadjoint saturation of the equatorial annihilator plane is all of
`su(2)^*`. The compact and split constructions therefore have identical
dimension and rank schedules.

## Orthogonal pairs construct

For two orthogonal roots, the intersection centralizer is

```text
s_1 direct-sum s_2 direct-sum R^5,
```

where each `s_i` is either `sl(2,R)` or `su(2)`. The wall leaf has dimension
`80`. Set

```text
M_98 = S_80 x X_4(s_1) x X_4(s_2) x T*R^5.
```

The exact schedules are

| locus | target Poisson rank | map rank | fibre dimension |
| --- | ---: | ---: | ---: |
| both factors regular | `84` | `91` | `7` |
| one factor at its wall | `82` | `90` | `8` |
| both factors at the intersection | `80` | `89` | `9` |

The probe checks all four real-form pairings. In each, the complete block
identity `dJ Pi_M dJ^T=Pi_target` holds exactly.

There is no hidden pairwise potential defect: each homogeneous factor carries
its tautological cotangent potential and the product potential is their sum.
Swapping commuting factors preserves that sum and intertwines the moment maps.

## The first orthogonal triple cocycle closes

Three mutually orthogonal roots give

```text
M_98 = S_78 x X_4(s_1) x X_4(s_2) x X_4(s_3) x T*R^4.
```

With zero, one, two or three factors on their walls, the target ranks are
`84,82,80,78` and the map ranks are `91,90,89,88`. Exact permutation matrices
preserve the product symplectic form, strictly intertwine the three moment
factors and compose to the identity on the first triple overlap. Equivalently,
the additive tautological potential has zero Cech defect. This settles the
first triple cocycle only for a commuting `A1^3` subsystem.

## Why the adjacent `A2` overlap is different

At two adjacent split-root walls, the derived centralizer is `sl(3,R)` and the
centre is `R^5`; the symplectic leaf has dimension `78`. A minimal `98D`
attachment therefore needs a `10D` symplectic transverse factor mapping to
`sl(3,R)^*` with

```text
map rank 8 on every regular value,
map rank 5 at the A2 origin.
```

The most direct homogeneous cotangent candidate takes the upper-left block
`H=SL(2,R)` in `SL(3,R)`. Its annihilator is the five-plane of arrowhead
matrices

```text
xi(a,u,v,r,s) = [ a  0   u ]
                  [ 0  a   v ] .
                  [ r  s  -2a]
```

At `[e,xi]`, the stabilizer of the cotangent moment map is
`h intersection g_xi`, so

```text
rank(dmu) = 8 - dim(h intersection g_xi).
```

Generic arrowhead points have zero intersection and give rank eight. At the
origin the entire three-dimensional `h` stabilizes, giving the desired rank
five. Those two controls make the candidate look unusually strong.

## The regular-nilpotent rank defect

Take

```text
N = [ 0  0  1 ]
    [ 0  0  0 ] .
    [ 0  1  0 ]
```

This lies in the arrowhead annihilator, satisfies `N^3=0`, `N^2 != 0`, and
has ranks `rank(N)=2`, `rank(N^2)=1`. It is the regular nilpotent Jordan type
in `sl(3,R)`. Its centralizer has dimension two, so its coadjoint orbit and
target Poisson rank have dimension six: it is a regular target value, not an
`A2` singular point.

Writing an element of the block `sl(2,R)` as `(A,B,C)`, its infinitesimal
action on the chosen `N` has coefficient rank two. Hence

```text
dim(h intersection g_N)=1,
rank(dmu_N)=7.
```

After adjoining `S_78` and `T*R^5`, the full map rank is

```text
78 + 7 + 5 = 90 < 91.
```

The natural candidate is therefore not submersive on the regular locus and
cannot be an RSAP chart. Passing only semisimple samples would have missed the
failure.

## Claim ceiling

This packet establishes:

- local `98D` models for both isolated real rank-`82` wall types;
- all split/compact combinations at orthogonal `A1 x A1` intersections;
- exact pairwise potential and moment-map compatibility there;
- one strict commuting `A1^3` triple cocycle; and
- rejection of `T*(SL(3,R)/SL(2,R))` as the split-`A2` factor.

It does not establish:

- a universal obstruction to every `10D` Hamiltonian `A2` realization;
- the compact or mixed real forms of the `A2` problem;
- adjacent-root pair or triple cocycles;
- deeper strata, the zero-charge rank-`49` requirement, or global surjectivity;
- any physical action, background, cohomology, quantum or empirical claim.

The all-charge cotangent fallback remains dimension `182`. No ledger, canon,
residue, quotient, datum or public posture changes.

## Next reverse scaffold

Keep Variancer's reverse conditional construction. Start from the superposition
hypothesis:

```text
H_RSAP98: one smooth 98D symplectic carrier maps surjectively to so(7,7)^*,
          is Poisson everywhere, and is submersive over every regular value.
```

Build backward from its necessary adjacent-`A2` behavior rather than forward
from another attractive homogeneous space:

1. derive the complete local rank, isotropy, fibre and potential-cocycle
   conditions forced by `H_RSAP98` over semisimple, nilpotent and zero `A2`
   values;
2. classify all three-dimensional isotropy subalgebras in each relevant real
   `A2` form and test whether any annihilator avoids every regular stabilizer;
3. if cotangent models exhaust, turn the nilpotent defect into a scoped no-go;
   if not, construct the smallest noncotangent or multicomponent alternative;
4. demand one chart pass semisimple, regular-nilpotent and origin ranks before
   attempting adjacent-root potential gluing; and
5. only after that pass, compute the first noncommuting triple Cech cocycle.

The strongest immediate hypothesis is now: **orthogonal wall assembly is not
the bottleneck; regular nilpotent isotropy in adjacent `A2` sectors is.** The
next swing must try to kill that statement by finding a `10D` realization with
rank eight at every regular nilpotent point and rank five over the origin.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k77_rsap_rank82_wall_family_a2_cocycle_gate_probe.py
```

The exact probe passes `92/92`.

Mathematical anchor: A. Weinstein, “The local structure of Poisson
manifolds,” *Journal of Differential Geometry* 18 (1983), 523–557,
doi:[10.4310/jdg/1214437787](https://doi.org/10.4310/jdg/1214437787), together
with the standard equivariant cotangent moment map for homogeneous spaces.
