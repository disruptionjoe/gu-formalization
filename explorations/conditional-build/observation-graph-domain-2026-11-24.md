---
title: Thin observation and the two continuity requirements of index additivity
status: exploration
doc_type: structural-result
created: '2026-11-24'
program_target: X-P1-P2-P3
tier: T2
expected_delta: Constrain the analytic realization of the conditional observed-hidden index bridge using the actual contraction and existing normal-jet prescriptions
actual_delta: Graph-trace continuity and closed hidden-domain requirements characterized in the cutoff-stable structural subclass
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

program_target: X-P1-P2-P3
tier: T2
expected_delta: Constrain the analytic realization of the conditional observed-hidden index bridge using the actual contraction and existing normal-jet prescriptions
actual_delta: Graph-trace continuity and closed hidden-domain requirements characterized in the cutoff-stable structural subclass


# Thin observation and the two continuity requirements of index additivity

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`. Base revision:
`d7bd31e050fd92a127c2e5fd55ce49f07fb3858c`. Internally reviewed T2 structural result. Primary target X-P1-P2-P3; secondary P3xglobal_index
and P1xdomain_boundary. No packet, matrix status, source claim or ledger row is
closed by this result.

```gu-typed-objects
result: Necessary domain conditions for continuous literal observation in an index complex
carrier: smooth finite-rank bundles near a fixed codimension10 observation section in Y=Met(X); source one-form/scalar and geometric RS subbundles are separately admissible examples LAYER=ambient+observed BRIDGE=literal-section-contraction CHIRALITY=S-FULL-DIRAC
pairing: auxiliary smooth positive density and component Hermitian norms used only to define local L2 graph topology; not physical Krein positivity ON=declared_carrier
real_structure: real scalar cutoffs preserve any separately supplied smooth pointwise reality law; no K77/K95 identification
grading: any separately supplied smooth zero-order grading preserved by scalar multiplication; not a selected physical weak grading
action_owner: N/A -- universal differential-operator/domain test, no action or missing native domain constructed
target: both degree maps qE and qF in the conditional Fredholm observation complex MAP-TYPE=restriction
```

## 1. What is being tested

The [November11 index statement](p1-p2-domain-index-2026-11-11.md) §3 and
[November20 audit](observed-hidden-split-sc-chi-01-2026-11-20.md) §2 require
continuous surjections qE:E→Eo and qF:F→Fo, with E the actual graph-norm domain
of a closed chiral operator D. They additionally require intertwining and
Fredholmness of total, hidden and observed complexes. Their conclusion is
conditional index additivity, with total0 separately required for
observed=−hidden. This paper tests the continuity premise when q is literal
section contraction. It does not replace that premise with pointwise rank.

SC-CHI-01/04 assert a non-chiral total with effective observed separation;
SC-GEN-01 disavows simple triplication and SC-GEN-02/03 name the 2+1 and
imposter summands. None chooses the graph topology, an ordinary integer index,
or a global closed physical domain. SC-OP-04 is the candidate-strength
four-independent-field operator; SC-OP-05 leaves rival operators open. The
source's smooth field spaces are not a claim of continuous L2 observation.
RA-F1, AC-F1 and LT-SM8 remain NEEDS in ledger0.263.

Previously owned facts are not rediscovered here. K2242 proves the raw
unrestricted-normal-jet equation does not admit a nonzero value-only equation
receiver, and supplies a constrained normal-independent control. K2531 proves
Sobolev regularity thresholds for thin and partially thick sources; K2543
separates finite smearing from a divergent shrinking-detector limit. The new
composition tests the actual index packet's TWO continuity requirements,
including the at-section jet prescriptions used by the November13 and
November24 local survivor.

## 2. Local graph-trace theorem

Fix an embedded section S in a smooth manifold M, codimension c, and local
coordinates (x,y) with S={y=0}. Let E,F be smooth finite-rank bundles, let D be
a linear differential operator of order at most m with smooth coefficients near a
compact coordinate tube, and choose smooth positive densities and positive
component norms. These are auxiliary analytic norms; D may have indefinite,
nonelliptic or non-Clifford principal symbol. Put

    ||u||_D = (||u||_L2² + ||Du||_L2²)^(1/2).

Let Q:E|S→O be a smooth zeroth-order contraction and q u=Q(u|S). Let V be a
linear space of smooth fields. Assume there is u∈V, compactly supported in the
tube, with q u≠0, and that V contains

    u_epsilon(x,y)=chi(y/epsilon) u(x,y),

for all sufficiently small epsilon, where chi is smooth, compactly supported,
and identically1 near0. This is the exact **cutoff-stability hypothesis**; no
invariance of a solution space under multiplication is assumed. The observed
topology is any fixed normed Hausdorff space containing q u.

**Theorem.** If c>2m, q on V is not closable from the D-graph topology. In
particular it cannot extend to a continuous observation map on a graph-domain
completion containing these fields.

**Proof.** On the fixed compact tube all coefficients and needed derivatives
of u are bounded. Its support after multiplication has normal volume
O(epsilon^c), so ||u_epsilon||_L2=O(epsilon^(c/2)). Leibniz's rule gives
terms with k≤m normal derivatives on the cutoff. Each has size at most
O(epsilon^(−k)) on that support, hence L2 norm
O(epsilon^(c/2−k)). Thus

    ||D u_epsilon||_L2 = O(epsilon^(c/2−m)),
    ||u_epsilon||_D → 0             when c>2m.

But u_epsilon=u on a neighborhood of S for each epsilon; consequently
q u_epsilon=q u≠0. The graph of q has (0,q u) in its closure, so that closure
is not the graph of an operator. This proves nonclosability, stronger than
unboundedness. ∎

For the existing first-order fermion/RS expressions and c=10 the exponents
are exactly

    ||u_epsilon||_L2=O(epsilon^5),
    ||D u_epsilon||_L2=O(epsilon^4),  q u_epsilon=q u.

This needs no principal-symbol inversion, ellipticity or positive physical
pairing. Smooth lower terms, spin/form connections, locally nonzero smooth
density weights and zeroth-order field transports cannot remove it: on the
fixed compact tube their coefficients are bounded and their positive norms
are equivalent. In particular the determinant weight and its smooth profile
rivals from November24 are positive and regular at the section. Their global
end behavior cannot fix this local failure. Scalar cutoffs also preserve
pointwise gamma-tracelessness, reality and grading subbundles.

The statement concerns a fixed observation section and fixed background data.
It does not assume that a constraint imposed simultaneously at every possible
section is preserved by a cutoff adapted to one section.

### The hidden kernel is not closed

With u as above, v_epsilon=u−u_epsilon has q v_epsilon=0 but converges to u in
graph norm. Thus ker(q|V) is not graph-closed. This is precisely the closed
hidden-domain premise used by the Banach exact-sequence argument, not just an
unbounded estimate for an unrelated readout.

More generally, suppose a proposed homogeneous local jet prescription at S
contains every compact smooth field vanishing on a neighborhood of S. For any
compact smooth w, (1−chi(y/epsilon))w satisfies that prescription and converges
to w in graph norm when c>2m. Its graph closure therefore contains the entire
compact smooth local core. Such an at-section prescription cannot, by itself,
define a proper closed restriction of that core in this graph topology.
Outer boundary conditions are unaffected by choosing the tube in the interior;
additional nonlocal/tube-wide constraints require a separate test.

## 3. Audit of the actual recorded prescriptions

| Existing object | Exact analytic disposition |
|---|---|
| November13 `source-lower-term-compatibility` fixes LC normal covariant jets to zero **at the section**, before changing the spin connection. | A cutoff identically1 near S preserves those jets exactly. If the proposed off-shell domain is specified by these local conditions alone, it meets the theorem's cutoff premise and cannot provide continuous graph observation. |
| November13 `source-exterior-connection` §7 uses coherent normal covariant jets zero **at the point**, and expressly leaves an ambient global domain unbuilt. | Same conclusion. All jets, not merely the first jet, agree because the cutoff preserves the germ. Changing the connection while keeping a different jet convention is still a different prescription; neither at-section convention controls tube concentration. |
| November24 determinant repair uses those prescriptions and proves local cancellation, section-density equality and smooth weighted alternatives. | The algebraic cancellation survives. It is not a bounded-quotient or closed-domain theorem. No correction to its stated local result is needed. |
| K2242 §4 imposes normal independence throughout a product neighborhood, not merely at S. | Multiplication by chi(y/epsilon) violates that tube-wide equation. This genuine surviving category is outside the theorem. K2242 already records its L2 and source-selection limitations. |
| A physical solution subspace, nonlocal spectral restriction, or source-derived extension operator. | Cutoff stability is not automatic. One must test its actual norm and domain; the theorem alone supplies no exclusion. |

A finite jet condition only at one point is weaker still. The literal
source-shaped q=(P_H,Gamma_Y,nu) is a smooth zeroth-order map after restriction;
the theorem applies to any nonzero output slot. It does not replace contraction
by a freely chosen projection. Nor does the value-level identity qD=dq prove
a continuous quotient of graph completions.

## 4. The equation-space map is a separate burden

If F is the usual ambient L2 equation receiver and qF is a nonzero literal
section contraction, the same construction with m=0 gives

    ||f_epsilon||_L2=O(epsilon^(c/2)),
    qF f_epsilon=qF f≠0.

Thus qF is nonclosable on an unrestricted smooth L2 core for **every c>0**.
Increasing the source-domain regularity without specifying the equation-space
topology does not repair this second failure. A trace defined on Ran(D) alone
is not automatically the stipulated continuous surjection on all F; replacing
F by a range/closure changes the complex and its cokernel and index.

Weakening the norm on the observed space alone does not help: the same fixed
nonzero observed vector remains constant along the sequence in every fixed
Hausdorff normed target that retains it. A nonliteral smeared observation,
changed domain or stronger ambient topology is a genuine change of premises.
No subtraction of ghosts or finite grading choice supplies that change.

## 5. Surviving analytical categories and their exact costs

**Already-owned normal-independent control.** On a supplied finite-volume
product normal factor Z with product positive norms/density and fields
u(x,y)=v(x), assume the product operator obeys D(u)=(d v)∘pr and
observation is identity restriction under that product trivialization. Then

    ||u||_L2(M)=Vol(Z)^(1/2)||v||_L2(S),
    ||u||_D=Vol(Z)^(1/2)||v||_d.

Restriction is bounded on these subspaces, and so is the analogous
normal-independent equation-space map. For a general bounded coefficient
contraction Q only the corresponding trace estimate follows; operator
intertwining is an additional hypothesis. The displayed identity is not
automatically the many-slot source quotient. K2242's optional compact flat torus
realizes this norm control. On an infinite-volume normal factor, nonzero
constant extensions are not ambient L2. Neither the compactification nor a
finite normal profile is source-selected; this is a countercontrol, not a
new native domain or an observed-hidden index realization.

**Stronger trace topology.** In a local Euclidean chart, isotropic H^s trace
onto a codimension10 plane is bounded into H^(s−5) when s>5. To see the
threshold, Fourier-transform in (x,y); Cauchy–Schwarz on the normal Fourier
integral uses

    integral_R10 (1+|eta|²+|zeta|²)^(-s) d zeta
       = C_s (1+|eta|²)^(5−s),            s>5.

The integral diverges at s=5. This calculation gives the sufficient local
trace estimate; it does not claim that divergence alone rules out every
critical Besov, anisotropic or constrained trace space. For a simple
first-order Sobolev complex D:H^s→H^(s−1), BOTH literal traces are covered
by this estimate only when s>6, with receivers H^(s−5) and H^(s−6).
This is an explicitly changed analytic realization. For a nonelliptic D,
its ordinary L2 graph norm does not become H^s merely by renaming it.
Continuity still supplies neither intertwining, closed range, Fredholmness,
physical positivity nor the required integer observable.

For global Riemannian bounded-geometry/vector-bundle trace results see
[Schneider and Große, arXiv:1301.2539v2](https://arxiv.org/abs/1301.2539v2).
Those hypotheses do not automatically hold for indefinite, noncompact
Met(X); the local positive chart norms above are auxiliary. An anisotropic
domain must explicitly control normal regularity; tangential regularity
alone does not prevent the cutoff sequence.

**Finite smearing.** A fixed L2 normal test profile gives a bounded averaged
readout by Cauchy–Schwarz. It is a changed observation map, with its own
intertwining and source-ownership obligations; K2543 already distinguishes
fixed-width probes from their singular zero-width limits. It is not silently
substituted for source contraction here.

## 6. Consequence for the matrix and packet

The admissible index-bridge subclass now has a sharper necessary condition:
it cannot use both literal thin observation and the ordinary first-order
L2 graph/L2 equation topology on the cutoff-stable off-shell cores described
above. At-section normal-jet and smooth determinant-density prescriptions do
not evade this condition. Both qE and qF and the closed hidden complex must
be justified on the SAME analytic realization.

This constrains X-P1-P2-P3/P3xglobal_index analytically; it does not establish
that all action-C realizations lie in the tested topology. The November21
packet remains blocked on `NATIVE-GRADED-FREDHOLM-OBSERVATION`. Its missing
domain datum is more specific: the actual off-shell/solution space, norms and
closed domains must provide a continuous nonzero section contraction in both
degrees, or explicitly justify a different observation complex. No source
action, stabilized RS action, boundary operator or K3 family is built to
satisfy it. The existing conditional index theorem remains true.

There is no GU falsification, physical count, paper/canon promotion, or source
claim change. Effective weak chirality need not be an integer Fredholm index.
The ordinary self-adjoint total index0 is still non-evidential for a chiral
block; no continuity result settles that separate grading problem.

## Reproduction and acceptance

`tests/program-focus/observation_graph_domain_probe.py` checks a plateau cutoff with a finite-regularity
polynomial transition, its norm/derivative scaling, preservation of at-section
jets, the codimension/order range, failure of tube-wide normal independence,
and the finite-volume positive control. Its polynomial fixture is C2, enough
for its first-order example; the theorem uses a smooth flat bump. Exact finite
controls support the proof but do not prove an unbuilt native domain.
Independent T2 review accepted the theorem and clarified the product/identity-map hypotheses of the finite-volume control. Exact probe: 46 checks. See the [review](../../lab/process/hostile-reviews/2026-11-24-structural-compatibility-review.md).
