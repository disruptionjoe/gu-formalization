---
artifact_type: exact_finite_central_holonomy_classification
created: 2026-08-14
status: UNIVERSAL_FIBRE_CHARACTER_CLASSIFIED__ONLY_COMMON_MU2_SIGN__OBSERVATION_TRIVIAL_ON_VERTICAL_CLASS__BASE_DOMAIN_AND_BOUNDARY_DATA_OPEN
ledger_rows: [RA-G2, LT-SM3, AC-F1, AC-G1a]
canon_verdict_change: none
---

# Selected K77 `mu_128` holonomy classification gate

## Result first

The Lorentz-metric fibre does **not** supply 128 physical central-holonomy
sectors. Its deformation-retract spine is `RP^3`, so its fundamental group is
`Z/2`. The exact character group is

```text
Hom(Z/2, mu_128) = mu_128[2] = {+1,-1}.
```

Thus the universal fibre contribution is at most one nontrivial sign. Even
that sign need not survive in the total observerse: in the homotopy sequence
for

```text
RP^3 -> Y=Met(X) -> X,
```

the image of the fibre `Z/2` is its quotient by the image of the connecting
map `pi_2(X) -> Z/2`. It is therefore either `Z/2` or zero. Fibre topology
alone cannot choose which.

An observation section `s:X->Y` satisfies `p o s=id`. On fundamental groups it
selects the base subgroup, not the vertical fibre generator. Consequently the
pure vertical sign character, extended trivially over base loops, pulls back
trivially along the observation section. Any nontrivial observed character
must instead come from the actual base or chosen physical-domain topology,
which the checked source does not specify.

The one surviving fibre sign also cannot distinguish luminous matter from its
mirror. On the actual real-K77 full-spin carrier it is the scalar `-I_128`; on
both `64`-dimensional Weyl halves it restricts to the same `-I_64`. Its
determinant is one on the full carrier and on each half. It is therefore a
common spin sign, not a W/mirror-odd selector.

This closes the **universal fibre-supplied finite-centre decoupling route**.
It does not classify characters of an unspecified spacetime or analytic
domain, choose a flat connection, kill a boundary-relative charge, or build
the source-claimed low-curvature luminous/dark decoupling.

## Plain English

The determinant calculation left a 128th-root loophole. The loophole is real
as abstract group theory, but the geometry does not automatically fill all
128 slots. The only universal loop already present in the Lorentz-metric fibre
has order two, so it can see only a plus or minus sign.

That minus sign is the ordinary common spin sign: it multiplies both chiral
halves in exactly the same way. Looking at spacetime through an observation
section also removes the vertical loop rather than turning it into an observed
charge. A nontrivial physical holonomy could still be supplied by spacetime,
a selected domain, an independent root line, or a boundary theory, but each is
new global data and none is currently owned by the source construction.

## Exact topology and character theorem

For a connected fibration `F->Y->X` with a section, the relevant homotopy
sequence is

```text
pi_2(X) -> pi_1(F) -> pi_1(Y) -> pi_1(X) -> 1.
```

Here `F` has the homotopy type `RP^3` and `pi_1(F)=Z/2`. Let

```text
K = image(pi_1(F) -> pi_1(Y)).
```

Exactness gives

```text
K = (Z/2) / image(pi_2(X) -> Z/2),
```

so `K` is either zero or `Z/2`. The section splits the projection on
fundamental groups, hence `pi_1(Y)` is a semidirect product of `K` with the
base group. Since `Aut(Z/2)` is trivial, the nontrivial vertical character—if
`K` survives—extends as the sign on `K` and the identity on the section's base
subgroup.

Writing `mu_128` additively as `Z/128`, a homomorphism from `Z/2` is fixed by
an element `k` satisfying

```text
2k = 0 mod 128.
```

The only solutions are `k=0` and `k=64`, corresponding to `+1` and `-1`.
This is the exact sense in which the fibre offers `mu_2`, not 128 independent
choices.

## Observation and physical domain

The observation section obeys `p_* s_*=id`. A loop in the observed copy of
`X` is therefore a base loop. The vertical-only sign is identity on that
subgroup, so

```text
s^*(chi_vertical) = 1.
```

This does **not** prove that every observed or physical-domain character is
trivial. A character of `pi_1(X)` or of a separately defined analytic domain
can survive. The source does not choose the needed topology or domain, and the
ambient first-order problem is ultrahyperbolic, so a physical closed domain is
not generic background structure that may be assumed silently.

Boundary-relative charge is a third object. It requires the actual
preboundary/BFV complex, symplectic potential, allowed gauge group and charge
map. Absolute fibre holonomy neither supplies nor kills it.

## Action on W and its mirror

On the real-K77 complexified full-spin carrier let `Gamma` be the volume
grading and `P_+`, `P_-` its two rank-64 projectors. The nontrivial central
character acts by

```text
z = -I_128,
P_+ z P_+ = -P_+,
P_- z P_- = -P_-.
```

Both restrictions have trace `-64`; their difference is zero. The action
commutes with the grading and is unchanged under the anti-linear half
exchange. By contrast, the planted asymmetric control `Gamma` has opposite
eigenvalues on the two halves. The exact probe therefore distinguishes a real
half selector from the common central sign and finds that the source-adjacent
fibre class is the latter.

The result is compatible with Weinstein's non-chiral total theory. It simply
does not construct the separate low-curvature luminous/dark effective
behavior. That burden remains with a nonstandard action-owned family operator,
an asymmetric physical domain, or a separately constructed boundary
reduction.

## Layer 0

| Object | Decided here | Not decided |
| --- | --- | --- |
| fibre spine `RP^3` | `pi_1=Z/2` | total-space fibre image |
| fibre image in `pi_1(Y)` | zero or `Z/2` | which without base/connecting map |
| characters into `mu_128` | only `+1,-1` on fibre | base/domain characters |
| nontrivial fibre sign | common `-I` on both halves | chosen physical holonomy |
| observation section | vertical-only character pulls back trivially | arbitrary observed base character |
| determinant | forgets the sign | independent scalar root line |
| flat holonomy | zero curvature, global character | large-gauge/BV survival |
| boundary-relative charge | remains separate | actual BFV construction |
| total matter | source-claimed non-chiral | luminous/dark decoupling mechanism |

## Broad route-changing lens census

- **Algebraic topology — exact:** homotopy exactness prevents the fibre
  fundamental group from being promoted to the total space without the
  connecting map.
- **Character theory — exact:** `Hom(Z/2,mu_128)=mu_2`; group order is not the
  number of fibre-supplied sectors.
- **Spin representation theory — exact:** the surviving sign is the same
  scalar on both half-spin carriers.
- **Category/commuting-square — exact:** observation selects the section/base
  subgroup, so a vertical-only character pulls back trivially.
- **Gauge theory — structural:** availability of a character does not choose a
  flat connection or make it gauge-physical.
- **Symplectic/BFV — open by ownership:** large-gauge and boundary survival
  require an owned preboundary complex and charge map.
- **Analytic/PDE — open by ownership:** no physical closed domain is supplied,
  especially in ultrahyperbolic ambient signature.
- **Source criticism — high:** the checked source supplies no base topology,
  finite character, root line, boundary phase space or analytic domain.
- **Philosophy of science — falsifiable ceiling:** the result removes a free
  mechanism rather than turning missing global input into evidence.
- **Wild-frontier control:** a nontrivial base/domain character remains a
  legitimate future route only after its topology and physical selection are
  built, not chosen to match the desired sector split.

## Hostile close

The strongest overclaim would be “all `mu_128` holonomy is impossible.” That
is false. The theorem classifies only the universal fibre contribution. A
nontrivial base, selected analytic domain, independent root line, disconnected
extension or boundary theory can carry additional characters.

The strongest counterexample is a domain with `pi_1=Z/4`, for which
`Hom(Z/4,mu_128)` has four elements. The probe includes it as a firing control.
It shows both that the character calculation is sensitive to the actual
domain and that the source's unspecified domain cannot be silently replaced
by the fibre.

The weakest reproducibility seam is the global homotopy input: a concrete
spacetime can make the connecting map kill or preserve the vertical `Z/2`.
The result states both cases and does not choose between them.

## Progress and next gate

```text
Ledger v0.246 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
Frontier closed: universal RP3-fibre finite-centre selector
Frontier remaining: base/domain character or boundary-relative BV/BFV charge; nonstandard family operator/domain
```

The adjacent global routes now have explicit ownership tests. To pursue a
base/domain character, construct the actual physical domain and compute its
fundamental group and allowed gauge quotient. To pursue boundary charge, build
the preboundary/BFV complex. Neither may be fitted by hand. The more direct
physics route remains the action-owned nonstandard family operator or domain
that can yield luminous/dark effective decoupling while total matter remains
non-chiral.

No field, root line, character, holonomy, boundary charge, physical domain,
datum, residue coordinate, quotient count, P1/P2/P3 use, canon verdict or
public posture changes. The exact probe is the reproducibility endpoint.
