---
title: "K1816--K1820 full-Fisher slab-three leafwise calibration wave"
status: active_research
doc_type: exploration
updated_at: "2026-10-20"
---

# K1816--K1820: fixed-q two-radius global minimizer certified

## Fixed-q global composition (2026-10-20)

The four complete local packets resolve every necessary root box. Their exact
closed partitions contain **79 gradient-excluded terminals, one positive-Hessian
terminal and zero unresolved terminals**. The new data exclude all 37 candidate
leaves other than leaf50. With the original 14 exclusions, 51 of 52 stationary
candidate leaves are now excluded. Leaf38's original unsupported flag remains
preserved; its new exclusion comes from this distinct correlated certificate.

The entire necessary-root bounding rectangle in leaf50 has transformed Hessian
`A > 3.1587695861e-9` and `det(H) > 1.1883377946e-16`. These are conservative
rounded lower bounds of the exact rational endpoints in K1820. Strict positive
definiteness on a convex rectangle makes the gradient strictly monotone:
for different x,y, integrate `(x-y)^T H(y+s(x-y))(x-y)>0` over s in [0,1].
Thus there is at most one stationary point there. K1787's whole-line Krawczyk
box lies inside original leaf50, and its root must lie in the necessary-root
rectangle by the exact derivative transport. Existence plus injectivity proves
one stationary point in the entire 52-leaf candidate union. The connected-graph
argument below is an additional structural result; the final proof does not
need it because only one convex root rectangle survives.

Let R be K1816's compact union of 78 closed retained boxes. Its boundary has
value strictly above `T=7958932265249/50000000000000000000` by K1819; 26 of its
boxes have the same strict value exclusion. K1787 encloses the surviving
stationary value in
`[1.5917864530497670077445861802075968567e-7 +/- 3.19e-24]`, strictly below T.
A continuous objective attains its minimum on R. That minimizer cannot lie on
the exposed boundary or a value-excluded box, and hence is an interior
stationary point in the 52-leaf candidate union. It must be the unique point
just certified. This proves a unique minimum on R, without asserting that
value-excluded regions have no higher stationary points.

The global-domain bridge is the already accepted chain: K1760 excludes the
zero-noise/rare-atom collars; K1763's compact candidate lower bound is above
the K1787 value upper bound, so those incumbent-relative exclusions still
apply. K1769 covers every possible remaining Hermite sublevel competitor;
K1777 closes its lower boundary strip; K1792 and K1809 exclude slabs one and
two. K1791/K1796 prune the slab-three complement of R at
`T0=31835729061/200000000000000000 > T`. Thus every admissible point outside R
has value above the certified local point. No boundary escape or missing
stationary component remains in this **fixed q=1/1024 symmetric unit-variance
two-radius scalar chart**. Its unique global minimizer is the K1787 point.

This is a computed, repository-derived active-research theorem. It is not an
optimizer over arbitrary channel laws, a GU action or physical state, a
prediction or confirmation, or a canon promotion. The earlier method failures,
component-box singular witnesses and partial counts remain valid historical
evidence. Native status propagation and any later canon review are separate.

## Correlated local jets and a connected candidate graph (2026-10-20)

This continuation uses the same fixed-q, symmetric, unit-variance two-radius
scalar Fisher objective, its positive chart, whole-line measure and exact
candidate cover. It is repository-derived variational mathematics. It supplies
no GU action, physical carrier, state/observable map, prediction or confirmation.
The component-box obstruction below remains true; the new instrument preserves
correlations before interval ranging.

### Correlated Taylor transfer

Four local expansion points are the exact midpoints of the retained root-box
unions in the four existing t-columns. They are ordinary expansion points;
**their gradients are not assumed zero**. For each column, save the normalized
compact objective jet through total degree eight at the point and on the entire
point-to-root-box hull. K1811's observation quadrature uses order fourteen,
the existing `cell_half_width=1/4` configuration and window [-11,11].
In that implementation each observation cell has width 1/4 and local radius
1/8; the configuration name is retained for reproduction. K1786 supplies whole-line absolute gradient
and Hessian tail bounds on each original root box. All saved endpoints are
outward rational enclosures, with canonical payload digests.

For a constant-coefficient derivative combination of order d=1 or 2, combine
normalized jet coefficients *before* bounding them. The point polynomial has
total degree 7-d. Its integral Taylor remainder has degree 8-d and a common
segment/kernel for all terms of that derivative order. A coefficient from
normalized objective jet (i+a,j+b) receives factor
`(i+a)!/i! * (j+b)!/j!` for derivative (a,b). Bound the combined highest-degree
coefficient on the entire hull, then sum absolute coefficient bounds times
maximum coordinate offsets. Range the point polynomial with tensor Bernstein
coefficients on the target rectangle. Add absolute whole-line tail errors with
the triangle inequality, including the absolute directional weights. No
cancellation of unknown tail errors is assumed.

The transformed Hessian uses basis (1,-8),(0,1):
`A=Jtt-16 Jtz+64 Jzz`, `B=Jtz-8 Jzz`, `C=Jzz`.
Its determinant `A*C-B^2` equals the original determinant. Positive lower
bounds for A and this determinant certify a positive Hessian. A negative or
zero-containing bound is not a failure of the objective or a second root.
Indeed, column zero's leaf26 has a negative transformed determinant, while its
new gradient bounds exclude stationarity. Requiring convexity everywhere would
be stronger than the needed root-local condition.

Rational replay bisects a closed rectangle only when neither a signed gradient
component/directional combination nor positive Hessian has been certified.
Children share the splitting boundary and cover their parent exactly. Every
child retains its parent's tail bound and the full column remainder hull.
Depth-eight unresolved terminals remain explicit; they cannot support a
uniqueness claim. The partition is a certificate on necessary root boxes,
not an assertion that any retained box contains a root.

### Connected vertical zero graph

The original 52 candidate leaves form four contiguous vertical stacks over
adjacent closed t-intervals. Existing exact whole-leaf bounds prove Jzz>0 and
Jtz>0 everywhere in those stacks. Each bottom has Jz<0; the last three tops
have Jz>0. At every shared t endpoint the overlapping vertical interval has
negative bottom and positive top signs. Thus both adjacent stacks contain the
same unique Jz-zero at a join.

In the first stack, the top's Jz is strictly increasing with t because
Jtz>0. Its value at the right endpoint is positive: the second stack's top
is lower and already has positive Jz there. Consequently the first stack's
root-existence set is an interval ending at its right endpoint, even though
its whole-top interval is not sign-definite. The union of all Jz-zero points
is therefore one connected graph z(t), differentiable through the joins by
the implicit-function theorem. This conclusion uses the exact join signs,
not merely local monotonicity or a picture of neighboring boxes.

On that graph, `g(t)=Jt(t,z(t))` has derivative
`g'=Jtt-Jtz^2/Jzz=det(H)/Jzz` at every point. If a complete root-box cover proves
positive Hessian at every possible full-gradient zero, every zero of g is a
strict upward crossing. Two such zeros would force an intervening zero with
nonpositive derivative (take the first return from positive to nonpositive),
a contradiction. This is the remaining conditional bridge to at-most-one
stationary point in the candidate union. Graph geometry alone does not prove
it. The 26 value-excluded leaves may contain higher stationary points; this
argument must never be described as uniqueness on the entire slab.

The same-jet gradient/curvature partition, exact packet results and remaining
obligations are recorded in K1820. Canon and protected physical grades remain
unchanged. Earlier counts and method limitations below are historical evidence.

## Complete Bernstein bank and component-bound limit (2026-10-19)

All **52 Bernstein replacements** are complete, with no power-range fallback.
Exact saved gradients exclude **14 leaves**; exact derivative transport retains
**38 root-feasible polygons**, occupying **12.782892%** of the original candidate
area (previous mixed bank: 13.036706%). Leaf 63 is now directly excluded as well
as excluded by transport; no new composed leaf exclusion follows. Leaf 38 stays
retained with its original contradictory advisory flag and unchanged digest.
The complete bank is frozen in K1818 and every input is embedded in K1820.

A useful method limit is now exact: every retained leaf's *independent component
Hessian box* contains a rational singular rank-one matrix. Write its entries as
`(tt,tz,zz)=(r*r*c,r*c,c)` with `c>0`; `(1,-r)` is a nonzero kernel vector.
The producer chooses a rational `r` and verifies the nonempty intersection
`[zz] intersect [tz]/r intersect [tt]/r^2` before selecting `c`. The probe checks
each recorded entry against its saved interval and multiplies the matrix by
its kernel independently. This proves that these component boxes alone cannot
certify uniform Hessian invertibility or strict positive definiteness, even
with a fixed nonsingular preconditioner. It does **not** prove that the actual
Hessian is singular, that another root exists, or that no other uniqueness
argument can work. Correlations, tighter bounds on the contracted tube, or an
independent global argument can remove this obstruction.

K1787 local existence and all 114 exposed faces/vertices remain certified.
Global optimizer admission stays withheld: none of the 38 profile Schur
intervals is positive. Further repetition of this completed bank is not the
next proof step. Compare a correlated directional/interval-Newton certificate
with the same-carrier action/observation construction before more quadrature.
No source claim, physics ledger, canon, prediction or public posture changes.

Validation distinguishes exact proof from controls: 38 rational matrix witnesses
and three rank-one/positive-definite/indefinite fixtures check the new limit;
the existing polynomial interpolation, endpoint and transport controls remain.
The quadrature, whole-line tails, full anchor-hull remainder and boundary proofs
are reused. The earlier mixed-method counts below are historical. The native
status rollup remains pending the already identified successor footprint.

## October 19 complete mixed-method bank and composition

All 52 candidate rectangles are covered by a complete derivative bank: **46
completed Bernstein rows (13--58)** and **six accepted corrected power-range
fallbacks (59--64)**. This is not a declaration that the Bernstein replay has
finished. Each row keeps its original method, interval bounds, payload and
digest. Both methods enclose derivatives of the same scalar objective on the
same exact box with the same full anchor-to-leaf remainder hull and whole-line
tails; selecting either valid row for each box therefore preserves coverage.
The artifact records both method-specific leaf lists and embeds every row.

Exact saved gradients exclude **13 leaves**: 13, 14, 27, 28, 29, 39--42,
52--54 and 64. Leaf 38 remains retained; its conflicting advisory flag and
original digest remain visible. K1820's exact transport additionally excludes
**leaf 63**, for **14 exclusions and 38 retained polygons**. Leaves 54 and 63
are new relative to the previous 12-leaf composed exclusion. The feasible area
is **13.036706%** of the original candidate area, versus **17.105628%** before.
This is a necessary location enclosure, not a root count or probability.

The follow-through recomputes every local profile Schur interval. None of the
38 retained leaves has certified positive profile curvature. Thus the new
bounds improve localization but still do not establish global convexity,
stationary uniqueness or optimality. K1787 local existence and K1819's complete
114-face/114-vertex boundary cover survive unchanged. Physics, source, ledger,
canon and public-posture conclusions do not move. This remains a provisional
scientific checkpoint with the previously identified native status rollup
pending a separately admitted footprint.

### Reproduction and proof review

`--assemble-available-bank` reads validated completed Bernstein checkpoints and uses
an accepted corrected checkpoint wherever a replacement is absent. It refuses
missing coverage and conflicts with numerical replay flags; it never computes
a new leaf. Its full output can replace the K1818 artifact only after review.
Recompute K1819 and K1820 from that exact frozen bank, not a changing scratch
folder. Later arriving checkpoints do not change the tracked result implicitly.

The Taylor/Bernstein transfer was checked on the actual formulas: affine
substitution maps each exact rectangle to the unit square; tensor Bernstein
basis functions are nonnegative and sum to one. Their coefficient extrema
bound the polynomial. The differentiated degree-eight remainder uses the full
anchor-to-leaf hull, factorial derivative factors and maximum absolute offsets;
analytic K1786 tails complete the whole-line enclosure. The compact quadrature
proof is reused, not presented as a fresh independent integration.

Four independent exact degree-six tensor interpolation controls recover
Bernstein coefficients by rational matrix inversion on shifted nonsymmetric
rectangles and check containment in the producer's range. They exercise mixed
terms and both coordinate shifts without reusing its binomial conversion.
Endpoint/discrepancy controls, the replacement-coverage mutation and existing
transport quadratic, clipping, domain-gap and consistency controls remain
required. Their finite test coverage does not replace the continuum proof.

**Historical sections below:** the earlier nine-direct/twelve-composed counts
and 40-polygon area are superseded by this complete mixed-method checkpoint.
The original serialization finding and proof history remain preserved.

## October 19 replacement-checkpoint serialization finding

The unfinished Bernstein replacement has a **non-bankable exclusion flag**
on leaf 38. Its checkpoint digest is
`deb7b6552262fdc0d750098f7cd727bffaf10b8fe13dcdd876df487ba8aa73a3`.
The saved whole-line `z` gradient is
`[8.5288594933649714996656707604440415459e-11 +/- 8.53e-11]`.
Its exact decimal lower endpoint is negative and its upper endpoint positive,
although `decision.rejected_by` says `z`. Outward display rounding can erase
a strict sign available to the in-memory Arb value. The saved enclosure is
still usable as an enclosure; its flag is not a reproducible exclusion.

K1818's `gradient exclusions semantic` validation rejects treating this
flag as a proved exclusion. Recheck every replacement decision against its
serialized bounds at assembly. Retain leaf 38 as method-indeterminate unless a replay supplies
a sufficiently precise outward enclosure that independently excludes zero.
Do not change its recorded digest, infer a tighter radius from the flag, or
discard its otherwise valid derivative bounds. The complete published
52-checkpoint bank has no such gradient/decision discrepancy; K1820's twelve
accepted exclusions and forty retained polygons are unchanged. This finding
does not claim the in-memory calculation was wrong or that another root exists.

### Conservative assembly without numerical replay

K1818 now derives the rejected axes from the exact rational endpoints of each
saved decimal enclosure. An endpoint equal to zero is retained. The assembler
never edits a checkpoint or manufactures a tighter bound. It embeds all saved
gradient evidence in new artifacts and separately records every disagreement
with the original in-memory decision, including the unchanged original payload
and digest. The validator authenticates these rows against the digest map and
K1816 provenance, recomputes the complete classification and discrepancy list,
and rejects missing evidence or an unsupported exclusion. Older accepted
artifacts retain their existing evidence format and semantic checks.

Thus leaf 38 needs no replay merely to participate conservatively in a complete
bank: its saved gradient enclosure retains the leaf. Establishing a strict
sign still requires a tighter certified enclosure. This removes a recovery
cost without increasing scientific coverage. The numerical functions,
remainder hulls, quadrature parameters and checkpoint files are unchanged;
full replacement-bank review remains necessary before acceptance.

A read-only audit of existing atomic checkpoints, which computes no missing
leaf, is available with the pinned Python dependencies:

```bash
uv run --with python-flint==0.9.0 --with sympy==1.14.0 python tests/channel-swings/k1818_full_fisher_slab_three_stationary_cover.py --resume-bernstein-bank --max-new 0 --summary
```

The hostile probe plants both directions of a flag disagreement. Seven exact
endpoint cases include positive, negative, zero-contact and the actual leaf-38
rounding values; four malformed intervals are rejected. Eleven hostile
mutations test false exclusions, altered digests, missing discrepancy/leaf
evidence, and unsupported global claims. These are exact serialization and
reporting controls, not an independent quadrature replay or a global theorem.

## October 19 exact interior derivative transport

K1820 now composes the **already-complete corrected K1818 bank**, without
consuming the unfinished Bernstein replacement or performing new quadrature.
The resulting exact transport excludes 12 of the 52 value-indeterminate
leaves, adding **13, 14 and 29** to K1818's nine direct gradient exclusions.
The other 40 leaves have nonempty root-feasible polygons. Their total area is
approximately **17.105628%** of the original 52-leaf candidate area; this is
location uncertainty, not a probability or a count of stationary points.
The artifact stores the exact rational polygons and area fraction.

The scalar objective, positive density, unrenormalized measure, real carrier
and claim ceiling in the typed-object block below are unchanged. The target
here is the zero set of `(J_t,J_z)` on the same closed rectangles. Source and
physics ledger rows do not move. This is independent mathematical composition
of accepted derivative bounds, not source-owned physics or a new GU test.

### Proof of transport and contraction

Let `g=(J_t,J_z)` and `H=Dg`. The 52 corrected, digest-authenticated
checkpoints enclose `g` and `H` on their whole closed leaves, including the
analytic whole-line tails. All 52 full payloads are embedded in K1820 and
checked against the published K1818 digest map and K1816 partition/provenance.
Their original quadrature is reused; this calculation does not independently
re-integrate it.

Form the grid from the leaf endpoints and the exact K1787 center coordinates.
Retain only covered vertices. An edge exists only if a single closed leaf
contains both endpoints, hence the entire segment by convexity. There are
110 vertices and 177 undirected edges. For an edge parallel to coordinate `j`
of length `h>0`, the fundamental theorem of calculus gives

```text
g_i(v)-g_i(u) in h * H_ij(edge).
```

Intersect all valid incident-leaf enclosures. Each vertex begins with its
incident gradient intervals; the anchor also carries K1787's certified
**nonzero gradient at its rational center**. It is not replaced by zero or
identified with the stationary point. Forward and reverse difference bounds
then propagate by exact rational interval intersections. At most `N-1`
Bellman-Ford sweeps cover all simple paths; a further tightening or an empty
intersection is rejected as inconsistent input rather than banked as a proof.

For a corner `q` of a leaf, travel first horizontally and then vertically to
`p` in that leaf. Both legs stay in the certified rectangle. Their lengths
have fixed signs, so the corresponding Hessian endpoints give affine lower
and upper bounds for each `g_i(p)`. Every stationary point must satisfy
`lower_i(p)<=0<=upper_i(p)`. Intersect the rectangle with these halfplanes
from all four corners using exact rational clipping. An **empty** polygon
excludes a stationary point; a line or singleton is retained. Combining the
three new exclusions with the original nine leaves exactly 40 candidates.
This proves neither that the retained polygons contain roots nor that every
point outside them has objective value above the comparison threshold.

### Outcome-contingent structural follow-through

Every corrected leaf also has `J_zz>0` and `J_tz>0`. On any covered contiguous
vertical fiber, `J_z` has at most one zero. Where such a zero is interior, the
implicit-function theorem gives a locally smooth curve with
`z'(t)=-J_tz/J_zz<0`. This does not prove a globally existing or connected
zero graph across the stepped cover.

On that curve, the derivative of `J_t` is
`J_tt-J_tz^2/J_zz`. K1820 now computes its exact enclosure from the saved
Hessian intervals on every leaf. **None of the 40 retained leaves has a
certified positive lower bound.** Thus the existing independent component
bounds cannot establish the required profile curvature. The next meaningful
numerical target is the contracted zero tube and its Schur complement,
with interval-Newton/profile continuation as an alternative; another full
uncontracted value bank is not justified by these results. Existing K1787
local existence and all 114 K1819 boundary certificates survive unchanged.

### Controls and acceptance boundary

The consumer replays in standard Python with rational arithmetic. Four exact
quadratic controls exercise a nonzero anchor gradient, a saddle, a root on
shared boundaries and an outside-domain root. Additional controls preserve
zero-area lines/points, forbid edges across uncovered gaps and reject an
inconsistent derivative. A clean baseline is checked before nine hostile
mutations of input certificates or reported conclusions. These controls test
the actual transport and clipping machinery; the global/physics mutations
separately test reporting discipline. The proof above supplies the continuum
transfer. Independent code review and the independently derived transport
calculation are recorded with this provisional checkpoint. An independent
nonlinear quartic control with variable Hessian bounds also excluded 15 of 16
boxes while preserving its known root; this is a finite algorithm control,
not independent quadrature of the Fisher objective.

Complete stationary uniqueness and global admission remain unproved. The
native status-rollup obligation described below remains pending for a safe
successor admission; this is not final wave acceptance or canon promotion.

## October 19 structural completion

K1819 now closes **all 114 exposed atomic faces and all 114 vertices of
the slab-three retained union**. K1804's earlier 122/122 census describes
the union across both slabs two and three; it was incorrectly carried as a
slab-three-only obligation. The original atlas remains valid in its own scope.
The complete corrected K1818 bank has nine direct gradient exclusions and
43 method-indeterminate leaves before the K1820 transport composition above.
Its incomplete Bernstein replacement is not used here. Complete stationary uniqueness and global optimality remain open.

Classification: `INTERNAL_STRUCTURAL_ONLY`. This result is independent scalar
variational mathematics and conveys no source-owned physical state, observable,
prediction, confirmation or unrestricted-infimum claim.

```gu-typed-objects
result: K1819 boundary theorem and K1820 exact derivative transport of stationary candidates
carrier: real scalar functions of observation y and rational parameter rectangles (t,z); LAYER=toy; CHIRALITY=N/A
pairing: integral rho_theta(y) f(y) g(y) dy ON=real scalar functions in L2(rho_theta)
real_structure: ordinary real conjugation
grading: N/A
action_owner: repository-construction
target: full Fisher objective J(theta), its gradient zero set and boundary of retained slab-three union; MAP-TYPE=not-a-map
```

### Compact support removes the tail obligation for this lower witness

Use the same positive density and score as the existing producers:
`rho=G D/(sqrt(v) sqrt(2 pi))`, `s=sqrt(t) R/(v D)`, and
`J=integral_R rho s^2`. Here `G,D,R,v` are exactly the K1807/K1816
mixture quantities, with no change of measure or compact renormalization.
On every certified parameter box, `0<t<1`, `0<z<1` and
`2t^2>1/1024` keep the mixture chart positive and nonsingular.

Let `C=[-11,11]` and `H=1_C h0`, where `h0` is the fixed K1787 score.
Then the already-certified compact quantities are exactly
`A_C=<s,H>_rho` and `B_C=<H,H>_rho`. Cauchy gives
`J B_C >= A_C^2`. The certified `A_C>0` implies `B_C>0`, so the
26 strict compact cross margins `A_C^2-T B_C>0` imply `J>T` on
the entire closed parameter boxes, including their faces and vertices.
The threshold is `T=7958932265249/50000000000000000000`.

No derivative or integration by parts of `H` occurs, so its jumps at the
window endpoints cause no distributional boundary term. This does **not**
certify the different untruncated `h0` witness's whole-line cross margin.
K1808's untruncated tail result remains valid; it is unnecessary for this
support-truncated lower witness. No new quadrature is used.

### Finite closed pruning removes the remaining boundary calculations

Let `D` be K1771's original closed slab-three rectangle:

```text
t in [887855469/17179869184, 4059652289/68719476736]
z in [17/32, 37/64].
```

K1791 and K1796 use finite bisections into closed rectangles. Let `P` be
the union of their strictly pruned boxes and `R` the final retained union.
Their accepted complete partition certificates give `D=P union R`; every
point of `P` satisfies `J>T0`, where
`T0=31835729061/200000000000000000` and
`T0-T=1/50000000000000000000>0`.

For `p` on the boundary of `R` and in the interior of `D`, choose points
of `D` outside `R` approaching `p`. They lie in `P`. A finite union of
closed boxes is closed, so `p` lies in `P` and inherits its strict lower
bound. This uses the finite closed partition, not a continuity inference
that a positive value off a boundary must remain strictly positive there.

Exact Fraction geometry reconstructs 114 exposed faces and 114 vertices
from K1816's 78 boxes. Direct positive-box inheritance covers 45 faces
and 47 vertices. The other 69 faces (including endpoints) and 67 vertices
are strictly inside `D`, hence covered by the lemma. All 13 faces and
14 vertices on the original domain boundary have direct witnesses from
leaves 0--12. No stationary exclusion is used to claim boundary values.

The K1819 artifact records every face/vertex, direct witness identity or
closed-cover proof, exact threshold slack and the linked partition digests.
This composes accepted K1791/K1796 certificates; their costly numerical
predicates and K1816 quadrature were not independently recomputed.

### Verification and scope review

An independent read-only review checked the density/score scaling, the
unrenormalized measure, the Cauchy hypotheses, all 78 checkpoint hashes,
positive chart, exact threshold difference and boundary geometry. Exact
finite-measure controls check signed scores and compact support; a cancellation
control distinguishes the untruncated witness. Hostile mutations reject wrong
thresholds, windows, anchors, partition links, missing terminal cells and
unsupported outer-domain closure. K1819's producer passes 15 controls, its
probe passes 18 controls, and K1820's producer/probe pass 11/3 controls.
These are composition, geometry and mutation checks, not fresh quadrature.

Publication status: coherent provisional checkpoint of the ongoing wave.
The boundary composition and its checks are complete; final wave acceptance
also requires the native `RESEARCH-STATUS.md` promotion rollup. That file is
outside this wave's frozen write scope, so the rollup remains an explicit
next-admission obligation. The current status, roadmap and verification
surfaces are reconciled here; no canon or global-optimizer promotion occurs.

| Claim | Prior result | Current result | Load-bearing evidence |
| --- | --- | --- | --- |
| K1819 exposed slab-three boundary | unclosed, with two-slab census carried forward | all 114 faces and 114 vertices excluded at T | K1771, K1791, K1796, K1816 and the two arguments above |
| K1820 global optimizer | unproved | unproved; interior stationary uniqueness remains | K1787 local certificate and incomplete interior cover |

The older account below is retained as **historical through October 16**.
Its open-boundary wording is superseded by this section. This is an
active-research result, not canon promotion.

## Historical result through October 16

K1816 now contains the complete atomic, digest-checked fixed K1787-score bank
on all 78 exact K1796 slab-three leaves. The selected uniform configuration is
parameter order eight, observation order fourteen and 88 rational observation
cells of half-width `1/4`. It proves strict compact margins on exactly 26
leaves: `0--12` and `65--77`. The contiguous block `13--64` is
method-indeterminate, with zero counterexample flags. The worst uniform lower
endpoint occurs on leaf 53 at `-9.2561445289e-25`.

The completed bank changes the route. Raising leaf 53 to observation order
sixteen improves its lower endpoint to `-4.1152250086e-25` but does not close
it. Exact t-only, z-only, depth-two, depth-three and targeted t-by-z scouts
drive the enclosure toward zero while remaining indeterminate. At the exact
rational lower-t/mid-z point, however, the same fixed witness has a strictly
positive margin `8.2260790157e-29`. Thus the negative box endpoints are still
certificate-method limits, not counterexamples, but the vanishingly small
point margin makes deeper value subdivision computationally dominated.

K1818's first full-objective gradient bank exposed a remainder-domain defect
during hostile review. The Taylor polynomial is centered at K1787, but the
degree-eight derivative enclosure was evaluated only on each target leaf. For
every leaf outside the anchor, Taylor's intermediate point can lie on the
segment between the anchor and leaf, so the derivative enclosure must cover
the complete anchor-to-leaf hull. The ten apparent stationary exclusions are
therefore withdrawn before downstream use. They do not change K1816's value
bank or K1787's local stationary certificate.

The corrected producer uses configuration-distinct checkpoints and the exact
axis-aligned hull of K1787's anchor with each target leaf. The complete replay
rigorously excludes leaves `27`, `28`, `39--42`, `52`, `53`, and `64` by at
least one whole-line gradient component. The other 43 candidates remain
method-indeterminate, including leaf 50 containing K1787's named stationary
box; retention is not evidence of another stationary point. K1804's 122
exposed atomic faces and 122 exposed vertices remain open. Stationary
uniqueness, global optimality, unrestricted scope and source-owned physics
remain withheld.

## Exact gradient replay and current continuation

```bash
UV_CACHE_DIR=/private/tmp/uv-cache-gu-science uv run --offline --with python-flint==0.9.0 --with sympy==1.14.0 python tests/channel-swings/k1818_full_fisher_slab_three_stationary_cover.py --resume-bank --summary
```

The command reuses only corrected anchor-hull checkpoints; the invalidated
leaf-only files have distinct names and are ineligible. Leaf-centered
reexpansion or a complete interval-Newton/Krawczyk cover is now required on the
43 retained leaves. Exposed-boundary closure is now supplied above. Complete
interior stationary uniqueness and protected global admission remain downstream.
