---
title: "K2372 The vectorial grade-two extension also fails on the actual metric"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics or numerical evidence; no native GU or hardware certification
scripts:
  - tests/channel-swings/k2372_vectorial_mixed_grade_obstruction_probe.py
---

# K2372 The vectorial grade-two extension also fails on the actual metric

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2372
carrier: all smooth radial odd plus vectorial grade-two translation fields on K2345 geometry LAYER=toy CHIRALITY=N/A
pairing: nondegenerate Clifford trace and Levi-Civita metric ON=declared_carrier
real_structure: real Cl(7,7) with arbitrary smooth scalar and one-form coefficients
grading: Clifford grades one and two, all transverse receiver grades retained
action_owner: repository-construction -- selected comm/symi/symi first action with independent fixed metric and epsilon
target: full mixed-field translation equations and actual-metric obstruction MAP-TYPE=evaluation
```

## Scope

Selected comm/symi/symi I1, real Cl(7,7), Levi-Civita reference and fixed metric/epsilon with unrestricted compactly supported translation variations. SC-ACT-01/02/06 and SC-GEO-55 ASSERTS preserve their source meanings; SC-META-56 DISAVOWS requiring a separate odd or supersymmetry-like action as a prerequisite to GU; the selected I1 here is bosonic. Ledger0.263 is unchanged. This tests a conditional reconstruction on K2345 geometry; no physical GU or full mixed-field verdict.

## Concrete next field, not an abstract future search

Let Phi_i=gamma_i and let v be a real covector. Clifford-raise v and set

    V(v)_i = gamma_i wedge_Cl v = [gamma_i,v]/2,
    T = a Phi + V(v),

where a and v are arbitrary smooth functions/one-forms on all fourteen
coordinates. This genuinely mixes Clifford grades one and two. Derivatives
include the full LC connection and formal adjoint. Do not identify V(v) with
source-owned contorsion merely because the standard term is familiar.

The exact full receiver equations reduce to

    mu(a) v = 11 da,                     mu(a)=kappa+568a/3,
    0 = -2 Einstein
        +[kappa a+312a^2-88 |v|^2]g
        +12 nabla_i v_j-nabla_j v_i-11g_ij div(v)
        +(4/3)v_i v_j.                                      (A)

The second equation includes its antisymmetric part. Thus dv=0 (the unnormalized difference of its transpose is 13 dv), without dividing by mu, v, kappa or a.
On mu!=0 the even auxiliary field is concretely v=11 da/mu. Equivalently,
locally v=df with f=(33/568)log|mu|+constant, and
u=exp(4f/33) is proportional to |mu|^(1/142).
At mu=0 the original even equation requires da=0 there; v is not discarded.
The no-go below uses neither this inverse nor a choice of branch.

## Universal coefficient and full-support justification

For the radial odd field, the known odd cubic is 312a^2 Phi. The even cubic
term is linear in a and v. Under O(g), V(v) is the unique standard-vector
trace summand of V* tensor Lambda^2 V. The grade rules and invariant index count below exclude the scalar
and higher even copies, so the coefficient is a scalar times a V(v).
The native receiver e4 gamma04 with v=e0 gives 568a/3, while the mass row
is 1 and the radial derivative row is -11 da_0. This yields the first(A).

The odd quadratic V(v) term must be c |v|^2 g + d v tensor v: these exhaust
the invariant rank-two outputs quadratic in a vector. Exact native rows
give c=-88 and d=4/3. The odd derivative has precisely the three contractions
c1 nabla_i v_j+c2 nabla_j v_i+c3 g_ij div(v). Native independent diagonal
and mixed jets give (12,-1,-11). Signed fixtures use Clifford-raised v and
retain the receiver pairing factors. There is no epsilon contraction with
enough indices to add another invariant in dimension fourteen.

All receiver grades have been accounted for. The selected Shiab grade graph
begins 0->3, 1->2, 2->1/5, 3->0/4, 4->3/7, 5->2/6, 6->5/9.
For r>=7 its smallest output is at least r-3>=4. Commuting a grade-two
coefficient with a grade-r receiver preserves r; commuting a vector with an
even/odd grade-r receiver gives r-1/r+1, respectively (grade zero commutes).
Thus first terms and formal adjoints for a general grade-one plus grade-two
field can reach receiver grades one, two, five and six; grades zero, three,
four and seven or higher are absent. Do NOT claim that the general
grade-five adjoint vanishes: S5 really can return to grade two.

For THIS vectorial family the grade-five derivative and quadratic-v
adjoints vanish by invariant index count. Their output V* tensor Lambda^5 V*
has six indices whereas nabla v and v tensor v have only two. Metrics can
pair the one form index to one internal index; a second metric insertion
must pair two antisymmetrized internal indices, giving zero. The a^2 grade-five
term has even fewer input indices. Similarly, a potentially nonzero
grade-six mixed cubic covector has only the vector input a v but output
V* tensor Lambda^6 V*, so the same metric-contraction argument kills it.
Dimension fourteen precludes an epsilon contraction for either map. Thus
these high-grade vanishings hold for arbitrary v and nabla v, not just the
selected fixtures. Scalar/grade-three/four vanish already by the grade graph.

The first-term grade-five covector is the total four-index alternation of
the grade-two curvature argument, followed by metric insertion. LC curvature
has Bianchi symmetry. Phi wedge Phi does too. For D V(v), each term is
gamma_j wedge nabla_i v-gamma_i wedge nabla_j v, whose four-index alternation
vanishes because its metric insertion repeats an index, regardless of dv.
The commutator V(v) wedge V(v) is built from g and the symmetric v tensor v,
so has the same Bianchi property. Cross Phi/V terms have Clifford grade one.
Consequently grades five and six vanish identically, and(A) is a full translation
equation, not a restricted scalar/vector Euler equation.

An independent normalization cross-check: m(V(v),V(v))=-13|v|^2; the mixed
cubic scalar is -(3692/3) a |v|^2. Its v variation divided by -13 gives
568a/3, while its a variation equals the trace of the odd V^2 tensor,
(4/3-14*88)|v|^2=-(3692/3)|v|^2.

## Exact actual-metric obstruction, including singular mu

Because dv=0, take v=df on an arbitrary contractible local patch and put
u=exp(4f/33)>0. The tracefree part of(A) says

    Hess(u) = alpha u Ric + beta g,       alpha=8/363,        (B)

for some scalar beta. Indeed
11 Hess(f)+(4/3)df tensor df=(363/4)Hess(u)/u.
Nothing about the even equation is needed for this necessary condition.

K2345 has n=14, scalar curvature R=-10, Ricci eigenvalue lambda_t=1/4
on the vertical trace line and lambda_s=-5/4 on vertical traceless space.
The fibre is totally geodesic: Gamma^horizontal_vertical,vertical=0 follows
directly from the block metric and its base-coordinate independence.
Vertical covariant differentiation preserves the trace/traceless/horizontal
projectors (K2363), so nabla_vertical Ric=0. K2366 proves R(t,U)=0 for
vertical trace t and every vertical traceless U, on the entire tangent space.

Take the trace and divergence of(B), using constant R and contracted Bianchi:

    d beta = [(alpha-1)Ric#-alpha R I] du/(n-1).              (C)

The standard commutation identity used here is
div Hess(u)=d Delta(u)+Ric(grad u, .).
Let b(lambda)=((alpha-1)lambda-alpha R)/13.
Differentiate(B) antisymmetrically on t,U. Its left side is
R(t,U)grad u=0 and the derivative-Ricci terms vanish. Hence

    [b(lambda_t)+alpha lambda_s] t(u)=0,
    [b(lambda_s)+alpha lambda_t] U(u)=0.

The two exact coefficients are

    -(24alpha+1)/52,       (48alpha+5)/52,

both nonzero at alpha=8/363. All vertical derivatives of u therefore vanish.
Total geodesy of the fibre then gives zero vertical-vertical Hessian. Apply(B)
to a nonnull trace direction and a nonnull traceless direction:

    beta=-alpha u/4,       beta=5alpha u/4.

Since alpha!=0, these imply u=0, contradicting u>0. Thus no smooth field in
the entire mixed family a Phi+V(v) is translation-stationary on this actual
metric. The argument covers null v, arbitrary coordinate dependence, mu=0,
kappa=0 and every real a. It does not exclude other grade-two contorsion
components, nonradial odd fields, other Clifford grades or other geometry.

## Controls and exact successor

Do not drop the derivative formal adjoint: it changes -11 and destroys(A).
Do not drop the skew odd row: dv=0 is a full independent receiver condition.
Do not generalize vectorial grade-five vanishing to arbitrary grade-two
fields: the actual changed-family jet D1 E0=gamma45 gives full derivative
Euler value 2 at Z=e6 gamma01456.
Do not divide by mu and erase its singular stratum; e.g. kappa=568,a=-3 gives
mu=0, da=0 and permits arbitrary v in the even equation alone.
The existing flat a=0,v=0 solution and K2360 changed-geometry solution remain
valid scope escapes; a positive scalar u on a flat chart can satisfy(B), so
the actual fibre-curvature identities are essential. In particular alpha=0
admits constant u on this metric and is an altered-coefficient countercontrol.

The next unresolved construction must introduce a nonvectorial grade-two
component (the 3-form or tracefree hook part of T* tensor Lambda^2 T*) and/or
a nonradial odd field. Its first equations are the full even algebraic
equation (kappa M+C_O)E+b(O)=0 and the odd Euler equation, retaining all
transverse grades. The scalar-gradient auxiliary branch is no longer an
unresolved placeholder after the stated proof and native coefficient checks.

## Auxiliary resonance follow-through

The action, geometry and variations are exactly those of K2372. Let O=aPhi
remain radial, but now let E be an arbitrary real grade-two one-form.
As an O(7,7) module,

    T* tensor Lambda2 T* = V14 + Lambda3 T*364 + hook896.

The last summand has zero contraction and zero total antisymmetrization.
Write E=V(v)+E3+Eh accordingly. All three are inequivalent real irreducible
modules (the same algebraic Young decomposition after complexification).

### Full even operator

The even equation is algebraic in E. With radial O it is O(g)-equivariant because it contracts only the metric, soldering field and invariant Clifford pairing,
and its grade-two block is therefore scalar on each of these three pieces.
This does not use positive definiteness or an indefinite diagonalization.
The derivative source from O is exclusively the vector piece -11V(da).

The only other potentially even receiver grade is six: [gamma1,Z6] is
grade five and S5 can return to grade two. Nevertheless its coefficient is
linear in aE, a rank-three tensor, with output V* tensor Lambda6 V*, of rank
seven. Two metric insertions would be required. At most one can pair the
single form index with an internal index; the second pairs antisymmetrized
internal indices and vanishes. An epsilon14 contraction is impossible with
ten total input/output indices. Thus the grade-six map is identically zero
for arbitrary E2 when O is radial. Grade zero/four and higher even grades
are excluded by the selected Clifford grade graph. No even receiver is lost.

Native exact coefficients (using the nondegenerate mass pairing) are

    muV = kappa+(568/3)a,
    mu3 = kappa+(112/3)a,
    muh = kappa-(56/3)a.

An all-positive axial representative is
e0 gamma45-e4 gamma05+e5 gamma04, with mass norm -3. Native cubic rows are
(-112/3,+112/3,-112/3), giving coefficient112/3. A hook representative is
e0 gamma45+e4 gamma05, norm -2; rows(56/3,56/3,0) give coefficient -56/3.
These are rational, nonnull normalization controls, not physical norms.
The executable independently repeats negative-signature representatives,
mixed-block inputs and selected off-support/grade-six receivers.

The FULL even equation is therefore precisely

    muV v=11da,       mu3 E3=0,       muh Eh=0.              (1)

### Nonresonant reduction and exact surviving strata

Where mu3 and muh are nonzero, E3=Eh=0 and K2372 excludes the resulting
vectorial family, even when muV=0. In a smooth stationary configuration,
such a regular point would have an open regular neighborhood. Consequently
there can be no such point on this actual metric.

For kappa!=0 the only remaining values are a=-3kappa/112 or a=3kappa/56.
Continuity makes a constant on each connected component, because these are
two distinct isolated real values. Hence da=0 and (1) gives v=0. More
precisely the remaining *candidate* branches are (their field may vanish at individual points)

    axial: a=-3kappa/112, E=E3,
           muh=3kappa/2, muV=-57kappa/14;
    hook:  a=3kappa/56, E=Eh,
           mu3=3kappa, muV=78kappa/7.

The separate vector resonance a=-3kappa/568 has mu3=57kappa/71 and
muh=78kappa/71, so it is already excluded by K2372, not an omitted branch.

For kappa=0 all three roots coalesce at a=0. A point with a!=0 has an open
regular neighborhood and is excluded. Thus a=0 everywhere; the even
equation leaves arbitrary E2 and the odd equations must still be solved.
This agrees with the open pure-even kappa=0 case rather than disposing of it.

### Exact unresolved mathematical work

These algebraic conditions DO NOT establish stationary axial/hook fields.
The remaining full odd grade-one/five PDE is

    projection_(1,5) [ -2Einstein+(kappa a+312a^2)Phi
                      +D_adjoint_complete(E)+Q(E,E) ]=0,

where the source/scalar terms occupy grade one only. For any odd receiver Z,

    D(E)[Z]=1/2{P(Z,S(D_B E))
                  -sum_k P(nabla_k E,S(e^k wedge Z))},
    Q(E,E)[Z]=1/3{P(Z,S(E wedge E))
                  +P(E,S(Z wedge E+E wedge Z))}.

These formulas are the exact resumable operator, with actual LC derivatives,
not a proposed surrogate action. General axial/hook E has rank-three
coefficients: nabla E has four indices and E squared has six, so invariant
rank counting no longer kills the grade-five equation. Nor does its odd
skew part reduce to dv=0 for a single one-form. K2372's positive-exponential
Ricci-Hessian proof therefore cannot be reused without a new derivation.
No solution, physical positivity, full source action or canon verdict is
claimed for either surviving singular stratum.
