---
title: "Selected-K77 RSAP 98D first-wall slice obstruction resolution"
status: active_research
doc_type: exact_local_symplectic_poisson_construction
created: "2026-08-14"
registry: lab/process/selected-k77-rsap-98d-first-wall-slice-obstruction.json
probe: tests/channel-swings/selected_k77_rsap_98d_first_wall_slice_obstruction_probe.py
grade: "EXACT LOCAL CONSTRUCTION AT ONE GENERIC SPLIT-ROOT WALL; GLOBAL RSAP OPEN"
canon_verdict_change: none
---

# Selected-K77 RSAP 98D first-wall slice obstruction resolution

## Result first

The minimal `98`-dimensional RSAP carrier crosses one generic split-root
rank-loss wall. The required nonlinear normal form exists.

At a generic semisimple split-root wall in `so(7,7)*`, the coadjoint orbit has
dimension `82` and the centralizer is

```text
sl(2,R) direct-sum R^6.
```

Poisson splitting reduces the wall problem to an `82`-dimensional symplectic
leaf and the `9`-dimensional transverse Lie--Poisson model

```text
sl(2,R)^* times R^6_zero.
```

Let `A` be the split Cartan subgroup of `SL(2,R)`. The transverse carrier is

```text
X_16 = T*(SL(2,R)/A) times T*R^6,
```

with its product canonical symplectic form and moment map

```text
mu_X([g,xi],q,p) = (Ad_g^* xi,q),   xi in ann(a).
```

The cotangent moment map `T*(SL(2,R)/A) -> sl(2,R)^*` is surjective. It has
differential rank `3` away from its zero section and rank `2` on the zero
section. Projection `T*R^6 -> R^6_zero` is Poisson and has rank `6`.
Therefore the product

```text
M_98 = S_82 times T*(SL(2,R)/A) times T*R^6
```

is one smooth symplectic manifold with a locally surjective Poisson map into
the full `91`-dimensional target neighborhood. Its exact schedule is

| locus | target Poisson rank | map rank | fibre dimension |
| --- | ---: | ---: | ---: |
| regular transverse value | `82+2=84` | `82+3+6=91` | `7` |
| split-root wall | `82+0=82` | `82+2+6=90` | `8` |

Both rows saturate `2 rank(dJ) <= 98+rank(pi)`. The prior tangent schedule was
not merely sharp in abstract linear algebra; it is attained by a smooth
nonlinear cotangent construction.

This admits one first wall. It does not construct a global all-charge RSAP.

## Layer-0 correction: which codimension is one?

The phrase “codimension-one discriminant wall” refers to the root hyperplane
in the real Cartan or invariant base. At a generic point, the corresponding
subregular locus has codimension three in the full Lie--Poisson target: two
orbit dimensions and one transverse invariant direction disappear together.

The distinction is load-bearing. The construction covers a full local target
neighborhood through a `3`-dimensional `sl(2,R)^*` transverse factor; it does
not pretend that a hypersurface chart in the `91`-dimensional target is the
whole Poisson normal form.

## Exact transverse certificate

Use the basis `(H,E,F)` of `sl(2,R)` with

```text
[H,E]=2E,   [H,F]=-2F,   [E,F]=H.
```

For dual coordinates `(h,e,f)`, the Lie--Poisson matrix is

```text
      [  0    2e   -2f ]
P  =  [ -2e    0     h ] .
      [  2f   -h     0 ]
```

It has rank `2` at every nonzero point and rank `0` at the origin.

In the associated-bundle presentation

```text
T*(SL(2,R)/A) = SL(2,R) times_A ann(a),
```

take `xi=(0,e,f)` and tangent coordinates `(E,F,E*,F*)`. The exact moment
differential is

```text
       [ 2e  -2f  0  0 ]
dmu =  [  0    0  1  0 ] .
       [  0    0  0  1 ]
```

The canonical source Poisson matrix in these coordinates is the standard
rank-four symplectic matrix. Direct multiplication gives

```text
dmu Pi_X dmu^T = P(0,e,f).
```

Thus `rank(dmu)=3` for `(e,f) != (0,0)` and `rank(dmu)=2` at the wall. This
is an exact Poisson identity, not a finite-difference rank observation.

## Why the transverse moment map is surjective

The annihilator `ann(a)` is the off-diagonal plane `h=0`. Its coadjoint
saturation is all of `sl(2,R)^*`.

For a traceless real matrix, trace and determinant classify the nonzero
semisimple type, with an orientation distinction on the elliptic side. The
off-diagonal plane contains:

- both split Weyl sides `(0,1,1)` and `(0,-1,-1)`;
- both elliptic orientations `(0,1,-1)` and `(0,-1,1)`;
- representatives of every nonzero nilpotent component; and
- the origin.

Equivariance then gives

```text
Ad^*(SL(2,R)) ann(a) = sl(2,R)^*.
```

The wall construction is consequently locally onto the complete transverse
Poisson neighborhood, not just onto the two semisimple chamber rays.

## Matching the existing regular Cartan charts

The old regular carrier is the cotangent-slice restriction

```text
G times C subset T*G,
theta_C = <lambda,g^-1 dg>.
```

On the hyperbolic regular cone of `ann(a)`, the `A` action gauges every
transverse covector locally to `lambda(E+F)`. A fixed Weyl conjugation carries
`E+F` to the split Cartan generator `H`. Under this gauge and conjugation, the
tautological potential on

```text
SL(2,R) times_A ann(a)
```

becomes the old `lambda H` cotangent potential. The two signs of `lambda` are
the two adjacent regular Cartan chambers. Hence the new chart agrees with the
existing symplectic form and moment components on both regular overlaps.

At `lambda=0`, that regular gauge degenerates, but the cotangent bundle
`T*(SL(2,R)/A)` does not. Its zero section supplies the smooth wall preimage,
where the moment fibre grows from dimension `7` to `8`. The domain is one
smooth manifold, not a union of symplectic strata.

## Product Poisson check

The executable probe constructs the complete block matrices:

```text
source:  Pi_82 direct-sum Pi_T*(SL2/A) direct-sum Pi_T*R6,
map:     I_82 direct-sum dmu direct-sum dpr_q,
target:  Pi_82 direct-sum Pi_sl2* direct-sum 0_6.
```

At both a regular point and the wall it verifies exactly

```text
dJ Pi_source dJ^T = Pi_target,
rank(Pi_source)   = 98,
rank(Pi_target)   = 84 then 82,
rank(dJ)          = 91 then 90.
```

The `sl2` Jacobi identity and split, elliptic, nilpotent and zero controls are
also exact integer checks.

## Claim ceiling and next scaffold

This packet constructs one generic split-root wall only.

- It does not classify compact-root or other real first-wall types.
- It does not prove compatibility where two or more wall charts meet.
- It does not cross deeper singular orbit types.
- It does not approach the zero-charge requirement `rank(dJ)<=49`.
- It does not construct one globally surjective RSAP map.
- It supplies no source-owned boundary action, stationary GU background,
  physical cohomology, quantization, spectrum or empirical prediction.

The next RSAP swing is therefore a **wall-family and cocycle census**:

1. classify every real rank-`82` wall type meeting the regular Cartan atlas;
2. construct the corresponding homogeneous cotangent factor for each type;
3. verify pairwise symplectic-potential and moment-map agreement; and
4. test the first triple-wall cocycle before entering deeper strata.

The global search interval remains `[98,182]`, with `182` still the canonical
all-charge cotangent fallback. No ledger, canon, residue, quotient datum or
public posture changes.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k77_rsap_98d_first_wall_slice_obstruction_probe.py
```

The exact probe passes `46/46`.

Mathematical anchors: A. Weinstein, “The local structure of Poisson
manifolds,” *Journal of Differential Geometry* 18 (1983), 523–557,
doi:[10.4310/jdg/1214437787](https://doi.org/10.4310/jdg/1214437787), and the
standard equivariant cotangent moment map for a homogeneous space. The finite
certificate above specializes both constructions to the required split-root
normal form.
