---
title: "X-D1-P3: three-local transfer forgets topological torsion, not all holonomy"
status: active_research
doc_type: exploration
created: "2026-11-11"
program_target: X-D1-P3
tier: T1
expected_delta: "open to decided_for_C only if the full additive datum-floor claim survives; otherwise constrained"
actual_delta: "constrained: ordinary transfer retained; explicit additive local-system counterexample prevents the universal floor inference"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: "No action-class exclusion, physical index, independent-data lower bound or source verdict"
scripts:
  - tests/program-focus/x_d1_p3_transfer_scope_probe.py
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`. This tests the mathematical inference
in Part B of the [two-datum packet](../../lab/process/work-packets/two-datum-theorem-2026-11-10.md).
It does not decide whether an action in class C realizes P3.

```gu-typed-objects
result: X-D1-P3-three-local-scope
carrier: Lorentzian metric fibre F, its double cover, ordinary complex K groups and finite projective local systems LAYER=UNTYPED (mathematical category, not a physical carrier identification) CHIRALITY=N/A
pairing: additive invariants with explicit forgetful functor ON=declared_carrier
real_structure: real metric fibre; complex topological K; R=Z_(3) and F_3 local coefficients
grading: integer realized index, mod-three arithmetic, additive torsion and tensor order are distinct
action_owner: N/A -- structural test of a proposed inference
target: transfer and local-system factorization MAP-TYPE=pullback
```

## Result and preflight

Native bookend fields (matching the frontmatter):

- program_target: X-D1-P3
- tier: T1 attempted; final matrix result constrained
- expected_delta: decided_for_C only if the full floor survives; otherwise constrained
- actual_delta: constrained; blanket additive forgetting fails, ordinary transfer survives

Target X-D1-P3; attempted Tier 1. The expected full floor is **not established**.
The exact test is whether every additive invariant retaining the time-line local
system factors through its pullback to the time-oriented cover. The counterexample
below settles that formulation negatively. It does not distinguish two choices of
future/past trivialization of a fixed system and is not a class-C kill.

Let R=Z_(3), the rationals with denominator prime to 3. Then 2 is invertible.
Let F=GL(4,R_real)/O(3,1), with one negative direction, and let D1 denote the
orthochronous sign local system associated to its time-oriented double cover.
This D1 is not the manifold-orientation system of orientable RP^3.

The following narrower statements survive:

1. Pullback on **constant-coefficient** cohomology with values in an R-module is
   an isomorphism.
2. Pullback on ordinary complex K-theory becomes an isomorphism after tensoring
   with R. The reduced complex sign-line class vanishes there.
3. The corresponding compact-support statement holds with a compatible Thom
   class for the rank-seven bundle describing F.

These statements alone give neither independence nor necessity of two external
data. The existing P1/P2 weld remains at its separate reconstructed-symbol grade;
P3 remains the realized integer-valued index, not a multiplicity or a mod-three class.

## 1. Concrete additive counterexample

The simply connected cover retracts to S^3; F retracts to RP^3. Finite projective
R-local systems on F are representations of C2 on finite projective R-modules.
Writing g for the nonidentity element, the central idempotents

    e_plus=(1+g)/2, e_minus=(1-g)/2

split R[C2] as R x R. Each module splits into its plus and minus eigenspaces.
Ranks (m_plus,m_minus) identify its additive Grothendieck group with Z x Z.
Every short exact sequence of these finite projective modules splits; alternatively
the two idempotent projections are exact and ranks add. Thus both

    I(V)=rank_R H^0(F;V)=m_plus in R,
    T(V)=trace(g|V)=m_plus-m_minus in R

are exact-sequence additive invariants. Pullback to the simply connected cover
forgets monodromy and remembers only m_plus+m_minus. The trivial and sign rank-one
systems have the same pullback, yet I takes values 1 and 0, and T values 1 and -1.
Neither invariant factors through this forgetful pullback. Reduction modulo 3
is a second, finite witness. This is the elementary idempotent version of the
averaging/character mechanism in [Etingof et al., §§4.1–4.2](https://math.mit.edu/~etingof/reprbook.pdf).

There is no conflict with Hom(Z/2,Z/3)=0. The sign representation has order two
under **tensor product**, whereas [sign]-[trivial] has infinite additive order in
Z x Z. The packet silently changed operations if it used the former to establish
the latter. In the representation ring eta=[sign]-1 satisfies eta²=-2eta;
there is no additional eta²=0 relation there.

The existing cellular control already exhibits the distinction. Untwisted
homology differentials in dimensions 1,2,3 are 0,2,0. D1-twisted ones are 2,0,2.
Over F3 the respective Betti numbers are (1,0,0,1) and (0,0,0,0), and H^0 has
ranks 1 and 0. Both Euler characteristics are zero. Therefore this example is
**not an index/count difference**, a physical realization, or a comparison of
opposite trivializations of one fixed local system.

## 2. The geometric and compact-support seam

Choose an auxiliary positive Euclidean metric on R_real^4, solely to describe
the fibre. A Lorentzian form has a unique negative eigenline L. Its orthogonal
complement Q carries its positive-definite block. The logarithm of the negative
eigenvalue's magnitude and the matrix logarithm of that block identify F with

    Tot(E), E = R_real ⊕ Sym²(Q) over RP³, rank(E)=7.

This description also supplies an explicit deformation retraction. It introduces
no selected Lorentzian action. The sign cover is obtained by orienting L.

There is a direct noncanonical trivialization of E. Identify R_real^4 with the
quaternions. The map L tensor Im(H) -> Q, q tensor u |-> qu, is a fibrewise
isomorphism: for imaginary u, qu is orthogonal to q, and both sides have rank 3.
It is well defined under changing q to -q. Thus Q is isomorphic to three copies
of L. Consequently Sym²(Q) is L tensor L tensor Sym²(R_real^3), which is trivial
because the Euclidean metric trivializes L tensor L. Hence E is trivial of rank 7.
In particular it has a Spin^c Thom class; mere real orientability would not have
been an adequate general complex-K hypothesis.

Bott suspension now gives K_c^j(F)=K^{j-7}(RP³). This is also a special case of
[Carey–Wang, Theorems 1.2 and 3.5](https://arxiv.org/html/math/0507414v4), whose
W3 twist records the general obstruction. Use the pulled-back Thom class on
the cover; do not independently choose incompatible orientations.

## 3. What ordinary transfer actually proves

For constant R-module coefficients, the cellular complex and the degree +1
antipodal action on S³ show that pullback is an isomorphism: in degrees 0 and 3
it is respectively identity and multiplication by 2, both invertible over R;
the other cohomology vanishes. This agrees with the constant-coefficient transfer
of [Hatcher, §3.G](https://pi.math.cornell.edu/~hatcher/AT/ATch3.4.pdf).
Keeping D1 as a coefficient system changes the statement, as section 1 shows.

For complex K, the dimension-three Atiyah–Hirzebruch filtration has reduced
K^0=H²(RP³;Z)=Z/2 and K^1=H³(RP³;Z)=Z. The unit survives; there is no possible
nonzero differential in this dimension, and the rank map splits K^0. Thus

    K^0(RP³)=Z ⊕ Z/2, K^1(RP³)=Z.

Pullback preserves rank and multiplies the degree-three generator by 2. Hence
it becomes an isomorphism in both parities after tensoring with R, as does the
compact-support map under the compatible Thom identification above.

For the complexified sign line L_C, eta=[L_C]-1 lies in filtration 2, so eta²=0
by dimension. The tensor identity L_C²=1 then gives 2eta=0. Thus eta disappears
after three-localization. Unlike the representation ring, **ordinary topological
K has forgotten the flat connection and imposed the extra filtration relation**.
The integral covering-transfer formula is

    p_! p^*(x) = (1+[L_C])x,

not literally 2x before localization. Afterwards it is 2x. Any fixed additive
homomorphism from this ordinary localized K-group to an R-module is insensitive
to the vanished twist. This assertion does not cover arbitrary holonomy-sensitive
invariants or a pushforward whose defining data change along with the twist.

## 4. The missing physical-index bridge and consequence

A general families index starts with a symbol on the vertical cotangent bundle,
not automatically with a class in K_c(F). Passing to this particular group requires
an explicit symbol identification, K-orientation, support/Fredholm conditions,
and compatible pushforward. APS problems additionally retain boundary/domain
information; see [Melrose–Rochon](https://arxiv.org/abs/math/0507590).
Class C presently does not require every count to factor through this one fixed
ordinary K-group, with D1-dependence exclusively given by tensoring L_C.

Even such a factorization would establish invariance of that index under the
specified twist. It would not establish independent necessity of an orientation
input and a count input, existence of a realized count, or the exact integer count.
A proof that changing one datum does not change one invariant is not a lower
bound on the number of external data in every theory.

Therefore X-D1-P3 moves **open -> constrained**, with two precise retained facts:
the ordinary transfer/Thom theorem and the obstruction to blanket additive
forgetting. No ledger row moves and no action class is ruled out. Part B's broad
floor proof is finished with this narrowed outcome. Part A (the separate weld
lift) remains meaningful but cannot use a proved two-datum floor as an input.
The unresolved floor requires a specified invariant category and an actual
class-C index/independence bridge; it is not repaired by more finite arithmetic.

## 5. Evidence, review and limits

The exact probe reconstructs the group-ring idempotents, both cellular complexes,
quaternion orthogonality/norm identity, the sign transition on Sym²(Q), additive
character counterexample and operation distinction. Characteristic-two and
Euler-characteristic controls deliberately remove the distinguishing information.
These checks support the written argument; they do not certify all topology.
The original input probe is reused as a predecessor, including its numerical
metric samples; those samples are not a proof of the universal retraction.

[ThreeLocalFloor.lean](../../Lean/GUFormalization/ThreeLocalFloor.lean) proves
Hom(ZMod 2,ZMod 3)=0, that 2 is a unit modulo 3, and that the additive character
on Z x Z cannot factor through rank modulo 3. The geometric identification,
K-theory and physical-index discussion are written/cited mathematics, not
Lean-certified. Topology, index and adversarial reviews agree on the constrained
scope, including the holonomy/trivialization and tensor/additive distinctions.

[Exact probe](../../tests/program-focus/x_d1_p3_transfer_scope_probe.py) ·
[replay report](../../lab/process/x-d1-p3-three-local-scope.json) ·
[constraint matrix](../../lab/process/action-constraint-matrix.json).
