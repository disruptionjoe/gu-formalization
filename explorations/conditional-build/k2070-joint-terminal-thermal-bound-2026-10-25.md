---
title: "K2070: Joint terminal blocks and a tighter global thermal bound"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional finite/countable four-state bath model; no exact optimum, dimension minimum or GU verdict
scripts:
  - tests/channel-swings/k2070_joint_terminal_thermal_bound.py
  - tests/channel-swings/k2070_joint_terminal_thermal_bound_probe.py
---

# K2070: Joint terminal blocks and a tighter global thermal bound

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: exact two/three-terminal price envelopes consumed into a global thermal lower certificate
carrier: four-state thermal channel with nondegenerate positive-spacing catalyst supports LAYER=toy CHIRALITY=N/A
pairing: classical diagonal marginal return ON=declared_thermal_population_model
real_structure: nonnegative real populations with rational certificate data
grading: occupied energy and gap labels, not field parity
action_owner: repository-construction -- unchanged K2059/K2066 fixed-bath model
target: finite and countable energy-constrained return MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] For the unchanged bath(8,4,2,1)/15,
spacing1/2<delta<=1 and energy budget E=5/2,

    199433405349365662917307150317/716395853109380299634702964040
      <= F_delta(5/2) <= 335946011010129/1206372108151072,
    0.27838436596717137 <= F_delta(5/2) <= 0.27847627505663369.

The remaining width is0.000091909089. Compared with K2066's
lower and K2068's current upper, the width shrinks by
66.351676 percent.
Eight assignments improve; all671 assignments are compared. The upper is the unchanged
K2068 physical41-level witness, not new verification or an asserted optimum. Source
claims, physics ledger and canon do not change. This is independent mathematical
progress on a conditional thermal model, not GU evidence.

## 1. Why joint blocks change the certificate

K2054 already gives the exact one-terminal response; K2066 retains incoming flow in
its first-terminal envelope. Its bottleneck164 has retained support[1,3,5,7,9] and an
active deeper cap(14,2). Raising that cap independently is invalid: K2054's sharp
single-terminal fixture still exists. Joint deletion retains the shared intermediate
population, so simultaneous extremizers must be feasible in the SAME block.

We first built the complete two-terminal envelope and consumed it into eight improved
assignments, reaching lower0.27833056288103875. Its bottleneck moved to the third
terminal. The same exact construction was then extended to three terminals, retaining
every shorter prefix and checking the remaining deep-tail caps. Derivation, finite
geometry, Bellman maximization and all-component transfer are distinct evidence steps.

## 2. Exact raw response and worst incoming flow

Write the edge coefficients at theta=1/2 as

    (L1,H1)=(14/15,7/15), (L2,H2)=(4/5,1/5),
    (L3,H3)=(8/15,1/15), k_d=H_d/(1+L_d).

For retained parent p and added populations u,v at gaps d,e, put A=(p-c0)_+, where
c0 is the actual incoming flow from the retained previous population. The exact
unnormalized return increment is

    2Delta = (A-(L_d u-H_d p)_+)_+ - A
       + (u-(H_d p-L_d u)_+-(L_e v-H_e u)_+)_+
       + (v-(H_e u-L_e v)_+)_+.                       (1)

Only adjacent populations share bath shells because consecutive gaps sum to at least4.
The initial parent deficit is subtracted once. The middle population receives its
actual incoming flow and loses its actual outgoing flow; optimizing these separately
would lose precisely the information needed here.

The A-dependent term is -min(A,(L_d u-H_d p)_+), decreasing in A. Therefore
Delta(p,A,u,v)>=Delta(p,p,u,v) for0<=A<=p. This is a worst-incoming bound, not a claim
that actual c0 vanishes. The same statement holds for a longer block.

For gaps d1,...,dk and populations p0,...,pk define

    D_i=(p_i - (H_di p_(i-1)-L_di p_i)_+
                  - (L_d(i+1) p_(i+1)-H_d(i+1) p_i)_+)_+,

omitting absent incoming/outgoing terms. At worst incoming A=p0,

    Delta_k=(sum_(i=0)^k D_i-p0)/2.                  (2)

For actual A replace D0-p0 by -min(A,outgoing0). Equation(2) is independently
replayed from the raw fixed-bath maximum over each shell, including zero populations
while keeping the cell's gap labels. It is not an assumed sum of independent losses.

## 3. Complete finite geometry and recession checks

At p0=1, Delta_k is continuous piecewise affine on the nonnegative orthant. All
breaks lie on the following finite hyperplanes:

- p_i=0 for each variable population;
- H_di p_(i-1)-L_di p_i=0 for each edge flow;
- for each i and each subset of its existing incoming/outgoing flows, the affine
  expression p_i minus those chosen incoming/outgoing losses equals0.

The last bullet includes extensions of boundaries beyond the cells where their
positive-part branches are active. Extra boundaries add test points; they cannot
remove an actual extremum. For k=2 this gives16 nonnegative intersection points and
six recession directions for each of the six legal gap pairs. For k=3 the producer
intersects every independent triple of hyperplanes; every independent pair of their
normals supplies a possible ray, retained only when an orientation is nonnegative.
The separate checker reconstructs the intersections by rational row reduction.

Why this is complete: the arrangement partitions the orthant into finitely many
pointed polyhedra, and the objective is affine on each cell. Every cell vertex is an
intersection of k boundary hyperplanes. Every extreme recession ray is an intersection
of k-1 independent homogeneous boundaries, including orthant boundaries. If objective
slope is nonpositive on every enumerated ray, its supremum on each cell occurs at a
vertex (or is constant along a ray from one). Conversely a positive recession slope
makes the supremum infinite. Extra enumerated rays are valid directions at infinity;
Delta_k's recession function is its p0=0 homogeneous expression. Evaluating it at all
rays also covers all intermediate directions by piecewise linearity.

Thus, for rewards q1,...,qk, define

    B_k(q)=max_vertices [sum_i q_i p_i-Delta_k(1,p)],
    require sum_i q_i r_i<=Delta_k(0,r) on every ray. (3)

This is the EXACT worst-incoming block price when finite. Homogeneity gives B_k*p0
for any p0>0; the recession conditions themselves cover p0=0. No finite grid or
floating optimizer establishes this completeness claim.

## 4. Paying the remaining tail without losing a path

Reuse K2059's homogeneous energy price a-t*n, t>0, cutoff64 with a<=65t, and

    G(n,d)=max(0,max_(e:d+e>=4)[a-t*n+k_e G(n+e,e)]).

G is exactly zero beyond64. For an actual tail after the retained endpoint z,
check separately the cases of zero, one and two added populations. For three or more,
price the first two rewards by q1=a-t*n1,q2=a-t*n2 and use q3=G(n3,d3) in(3).
The recursion pays deletion of every later population by its one-terminal loss.
Require G(n,d)<=c_d only on states reachable at depth FOUR OR GREATER, where

    c1=29/135, c2=9/50, c3=23/90.

Reachability includes a state if ANY path reaches it at such depth, even if another
path reaches it earlier. Removing all first-three states by a naive set difference
would be unsound. The producer uses a depth-capped reachability graph; the separate
checker explicitly seeds every fourth state and propagates it. For a two-terminal
prefix use its actual q2, not G2: there is no third population in that case.

Reverse erasure of a finite tail, then its exact initial block, proves

    sum_tail(a-t*n_i)p_i - Delta_total <= B_s*p_z,    (4)

where B_s is the maximum of0 and all legal shorter/joint-block prices. The final
block's last reward is allowed to be enlarged to G>=0; this preserves an upper bound
without ever multiplying a signed reward by a population inequality.

## 5. Incoming-aware convex majorant and its consumed improvement

For the initial outgoing flow O=(L_d p1-H_d p0)_+, the exact response at actual A
is Delta(A)=rest/2-min(A,O)/2. Consequently

    Delta(A)>=Delta(p0),
    Delta(A)>=rest/2-A/2.

Let Bw be the worst-incoming block price in(3), and let B0 be the same vertex maximum
with the loss replaced by rest/2 (equivalently add min(p0,O)/2 to the old loss).
The recession costs are unchanged because p0=0 there. For any FIXED0<=theta<=1,
convexly combining the two valid upper prices gives

    tail reward-Delta(A)
       <=p0[(1-theta)Bw+theta B0]+theta A/2.           (5a)

This is an upper bound, not a claim that the exact incoming envelope is convex.
Use the maximum of0 and these prices for all admitted prefix lengths/paths. On each
fixed orientation subcell the incoming flow c0 is affine; A=(p0-c0)_+ is convex.
The coefficient theta/2 is nonnegative. Thus the resulting boundary price is convex
in retained populations, which is precisely what the vertex transfer needs.

The final cell164 uses theta=7/10. Other replacement cells use theta=0. Exact
candidate discovery compared fixed rational weights; theta=1's stronger local
incoming bound was weaker globally (approximately0.2781755596), while theta=7/10
raises the cell164 certificate to the reported global lower. This is not an optimal
weight classification. The fixed-weight certificate itself is exact.

For fixed theta the sum of two finite maxima is a maximum over pairs of affine
pieces. Instead of materializing every pair, policy separation retains the actual
maximizer of each at the current rational(a,t), adds that affine inequality, and
reoptimizes. Every cut is globally valid; the final recomputation checks both actual
maxima, all Bellman policies and every other inequality. Nonnegative mixture weights
are essential. The separate verifier computes both maxima directly, independently
of the producer's selected cuts.

## 6. Low cells, high components and countable transfer

For each retained cell s and each of its bank vertices verify

    R >= a-t*energy+boundary_s(p_z,A).                (5)

For theta=0 the boundary is B_s*p_z. For theta>0 use(5a), which is convex on each
fixed orientation subcell. R is affine on the inherited deficit subcells, so its
difference from the right side is concave. Checking every vertex therefore proves
the inequality throughout. No convexity of the exact response is assumed.

Every high-component inequality is retained with the SAME a,t, safe offset
ell=max(1,s_penultimate+1), or1 for singleton s, recomputed high Bellman table, all
one-terminal caps, all wholly erased-root bounds, and every old high-bank vertex.
The low-cell inequality is always checked even when no outgoing gap exists. These
conditions yield R>=a*mass-t*energy on the whole physical arrangement, using the
unchanged K2059 packing/placement proof. Lowering one low contact without satisfying
the high-component inequalities would not be a global result.

For countable finite-mean populations apply the finite inequality to unnormalized
finite prefixes. Positive spacing makes the cutoff11 retained set finite; mass,
energy and return converge by the existing l1-continuity argument. There is no highest
terminal in an infinite support and no uncontrolled optimization/limit interchange.
All original671 complete cells and20975 vertices, physical support placement and the
K2068 upper witness are hash-pinned reuse. No new completeness enumeration of that
large bank is claimed.

## 7. Exact reproduction, consequence and limits

The producer uses rational affine-envelope optimization in the explicit price box
0<=t<=1. Each chosen Bellman policy supplies valid affine cuts; actual-policy
recalculation adds any violated cut until every inequality passes. Termination alone
certifies nothing. The candidate and all constraints are rational, and failed
iterations are recorded. The price box is a search choice, not a physical assumption
or a claim of dual optimality. `--write` regenerates the declared certificate;
without it the producer compares the exact result with the saved JSON.

The lower line and its exact common dominance interval are serialized in the
certificate. All671 assignments dominate that line at both interval endpoints,
which proves the affine comparison throughout. The K2068 affine upper remains
available on its own overlapping interval. The remaining gap is positive; unrestricted
optimality and minimum physical dimension remain open.

Same-author hostile checks distinguish written proofs, exact finite geometry,
actual raw bath controls and hash-pinned reuse. The separate checker passes2996 raw
and geometry controls,168276 new low/high inequalities and all671 interval comparisons.
Six actual faults are caught after a passing baseline: an omitted vertex, corrupted
recession loss, inflated price, lost response half-factor, omitted triple vertex and
a mixture weight outside[0,1]. The three-terminal
geometry is checked by a separately implemented row-reduction algorithm, not producer
assertions. There is no independent specialist, proof-assistant, external or novelty
certification.

The completed two-terminal bound was limited by a third-terminal cost cap; the
three-terminal bound was then limited by a worst-incoming low contact. Equation(5a)
consumes that information and moves the active restriction to a HIGH-component
inequality (bank174,vertex46,outgoing gap2). The low cell164 remains the global
bottleneck, with its high component shifted by ell=8. Another tail-length increase
alone does not remove that active coupling. Next compare a joint low/high-component
certificate under the actual shared physical placement with a genuinely new feasible
population. Scalar weight tuning above is candidate discovery, not proof of search
exhaustion or of an optimum. The remaining positive gap is explicit.
