---
artifact_type: exact_source_object_family_index_obstruction
created: 2026-08-14
status: SOURCE_METRIC_FIBRE_IS_TEN_DIMENSIONAL_BUT_NONCOMPACT_NONPROPER_AND_SPLIT__ORDINARY_ELLIPTIC_FAMILY_INDEX_ROUTE_DOES_NOT_INSTANTIATE
ledger_rows: [RA-G2, LT-SM3, AC-F1, AC-G1a]
canon_verdict_change: none
---

# Selected K77 source metric-fibre family-index obstruction

## Result first

The source-native observerse projection has the right dimension but the wrong
analytic type for the conditional family-index theorem:

```text
pi: Y^14 = Met_(1,3)(X^4) -> X^4.
```

At each `x in X`, the fibre is the ten-dimensional space of nondegenerate
Lorentzian forms on `T_xX`,

```text
F_x = GL(4,R)/O(1,3).
```

It is noncompact: for any `g in F_x`, the ray `g_t=e^(2t)g` remains in the
same fixed-signature fibre and leaves every compact subset. Therefore `pi` is
not proper, since the preimage of the compact set `{x}` is the noncompact
fibre `F_x`.

The settled K77 trace-reversed vertical form is also indefinite. At
`g=diag(-1,1,1,1)` its bilinear form on `Sym^2(T_x^*X)` is

```text
G_g(h,k)=tr(g^-1 h g^-1 k)-1/2 tr(g^-1 h) tr(g^-1 k),
signature(G_g)=(6,4).
```

It has nonzero null covectors. For the vertical Dirac/Clifford symbol,
`c_v(xi)^2=-G_v^*(xi,xi)`, so a nonzero null `xi` makes `c_v(xi)` nilpotent
and noninvertible. The source-owned vertical operator is therefore not an
ordinary elliptic chiral Dirac family on compact Riemannian fibres.

Hence the exact integral identity

```text
Ind(D_v tensor L^-1) = -conjugate(Ind(D_v tensor L))
```

remains true for its stated **conditional proper compact Riemannian spin
family**, but that antecedent does not instantiate on the actual source metric
bundle. The ordinary family-index route is closed on the current GU object
before line selection, flux, observation or BV/BFV descent.

This is not a theorem against every noncompact, transversally elliptic,
Callias, APS, relative or Wick-rotated construction. Each such replacement
requires a separately source/action-owned operator, coercive potential,
compact quotient, boundary condition or real-form change. None is presently
supplied. The physical successor therefore switches to the independently
action-owned asymmetric boundary/domain route already exposed by the exact
W/mirror real-action class theorem.

## Proof

### 1. The actual ten-dimensional fibre

The source construction makes `Y^14` the bundle of Lorentzian metrics on the
four-dimensional base. A symmetric bilinear form has

```text
dim Sym^2(R^4)^* = 4(4+1)/2 = 10
```

coordinates. Fixing nondegenerate signature `(1,3)` selects an open orbit of
`GL(4,R)`, with stabilizer `O(1,3)`, hence `F_x=GL(4,R)/O(1,3)`.

The scaling curve `t -> e^(2t)g` never changes signature. Its matrix norm is
unbounded as `t -> +infinity`, while as `t -> -infinity` it approaches the
degenerate boundary outside the fibre. Thus the fibre is noncompact. A proper
map has compact inverse image of every compact set; `{x}` is compact and its
inverse image is `F_x`, so the metric-bundle projection is not proper.

### 2. The vertical trace-reversed form

Use the symmetric basis

```text
(00),(01),(02),(03),(11),(12),(13),(22),(23),(33).
```

The exact Gram matrix of `G_g` has eigenvalue multiplicities

```text
-2 x3, -1 x1, +1 x3, +2 x3,
```

so its determinant is `64` and inertia is `(6,4,0)`. In particular the
orthogonal basis elements `(01)` and `(12)` have squared norms `-2` and `+2`.
Their sum is a nonzero null direction.

For a Dirac-type vertical symbol, the Clifford relation makes the square of
the symbol scalar multiplication by the negative vertical norm. On that
nonzero null direction the square vanishes. An invertible linear map cannot
have zero square, so the symbol is singular and ordinary ellipticity fails.

### 3. Family-index consequence

The previous theorem needs a continuous family of elliptic chiral Fredholm
operators on compact Riemannian spin fibres. The source object simultaneously
fails the compact/proper and definite/elliptic inputs. Consequently there is
no analytic index class of the predecessor's stated kind to which the exact
conjugate-odd identity can presently be applied.

No choice of line bundle repairs those earlier failures. A line twist changes
the coefficient bundle, not fibre compactness or the null cone of the
principal symbol.

## Layer 0

| Object | Decided here | Not decided |
| --- | --- | --- |
| `Met_(1,3)(X)` | source metric bundle with 10D fibres | a compact internal space |
| fibre `GL(4,R)/O(1,3)` | noncompact | a chosen compact quotient |
| projection `pi` | not proper | a different proper fibration |
| K77 vertical form | exact `(6,4)` inertia | a Wick-rotated Riemannian form |
| vertical Clifford symbol | singular on nonzero null covectors | modified/transversal ellipticity |
| integral family theorem | retained on its conditional antecedent | instantiated GU index class |
| line twist | cannot repair properness or ellipticity | source-selected nontrivial line |
| physical successor | asymmetric action-owned boundary/domain | constructed BFV cohomology |

The total-space rolled operator, the vertical symbol, an imposed Euclidean
fibre operator and a boundary-relative Fredholm operator are distinct objects.

## Broad route-changing lens census

- **Differential geometry — selected:** the homogeneous metric fibre decides
  compactness before any operator construction.
- **Proper-map topology — selected:** one point in the base supplies the exact
  compact-set counterexample to properness.
- **PDE/symbol analysis — selected:** split vertical signature supplies a
  nonzero characteristic covector and kills ordinary ellipticity.
- **Index theory — strict:** the integral theorem survives unchanged, but its
  analytic-index antecedent is absent on the source object.
- **Spin geometry — bounded:** no spin-structure classification is needed,
  because properness and ellipticity already fail.
- **Noncompact index theory — open:** Callias/coercive, APS/relative and
  transversally elliptic variants would require new owned data and a new
  theorem, not a silent reuse of the compact-family result.
- **Topology/gauge — restrained:** possible fibre topology does not select a
  physical line, flux or sector.
- **BV/BFV — successor:** an action-derived asymmetric closed domain can alter
  the physical state problem without pretending the bulk metric fibre is a
  compact Riemannian family.
- **Source criticism — high:** the source owns the metric bundle and explicitly
  acknowledges the multiple-time analytic debt; it does not supply the needed
  compactification or elliptic family.
- **Philosophy of science — strict ceiling:** an exact conditional theorem is
  not evidence for a route whose antecedent is false of the selected object.

## Controls and hostile boundary

The strongest overclaim is “family index is impossible in GU.” The result is
narrower: the **ordinary proper compact Riemannian elliptic family-index route**
does not instantiate on the current source metric bundle and vertical K77
symbol. A future source-owned modified operator/domain could define a different
index problem.

The strongest contrary control is a compact ten-dimensional Riemannian spin
manifold used as every fibre. Then the projection is proper and the Dirac
symbol is invertible for every nonzero covector, so the predecessor integral
theorem fires exactly. The obstruction is object-sensitive, not dimensional.

The weakest seam is operator ownership: the settled split form fixes the
current vertical principal type, but an independently justified coercive
potential, compact quotient, boundary condition or real-form change could
create a different Fredholm problem. Until one is action/source-owned, none
may be imported to rescue the route.

## Progress and next gate

```text
Ledger v0.249 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
```

The family-index successor is now decided on the actual source object: its
ten-dimensional fibre is noncompact, its projection is nonproper and its
vertical K77 symbol is nonelliptic. Preserve the conditional integral theorem
as reusable mathematics, but move physical decoupling work to the independently
action-owned asymmetric boundary/domain route. The next exact gate is to
construct the smallest source-action-derived boundary relation or closed
domain that is not invariant under W/mirror exchange, and test its Green/BFV
compatibility without fitting a projector or flux.

No verdict, residue, datum, quotient, generation count, canon claim or public
posture changes.
