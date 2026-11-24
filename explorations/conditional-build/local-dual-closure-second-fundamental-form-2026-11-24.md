---
title: The repaired observation kernel is invariant but the native second fundamental form still couples
  the opposite block
status: exploration
doc_type: structural-result
created: '2026-11-24'
program_target: X-P1-P2
tier: T2
expected_delta: Compute the opposite hidden-observed block of the existing density-repaired tangential
  reconstruction under an explicit metric-spin duality
actual_delta: In the existing metric-spin/coherent-jet exterior reconstruction, the opposite block is
  a P_K A_II; it vanishes for all horizontal fields iff II=0. The actual metric-bundle shape gives exact
  rank512, despite the scalar density repair. Nonzero II also obstructs vanishing for every metric normal
  extension in this coherent-jet/exterior category; the rank remains specific to B_n=0.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# The second fundamental form and two-sided observation

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.
>
> Classification: `INTERNAL_STRUCTURAL_ONLY`. This tests a supplied
> reconstruction and metric-spin splitting. The source's complete density-dual
> operator and physical barred readout remain unselected.

program_target: X-P1-P2
tier: T2
expected_delta: Determine the actual opposite cross block rather than repeating the abstract triangular counterexample
actual_delta: A geometric formula and total-geodesicity criterion; actual native opposite block has exact rank512

```gu-typed-objects
result: Exact second-fundamental-form criterion for the opposite observation block of the existing weighted exterior reconstruction
carrier: full one-form/scalar Dirac carrier, H4 plus symmetric-metric N10, existing q=(P_H,Gamma_Y,nu) LAYER=ambient+observed BRIDGE=literal-contraction CHIRALITY=S-FULL-DIRAC
pairing: declared nondegenerate metric form times compatible spin pairing, scalar block nondegenerate, and a supplied positive section density; not a source-owned physical pairing ON=declared_carrier
real_structure: full complex Cl14 Dirac representation; native Lorentz H and trace-reversed N; no K77/K95 identification
grading: same geometric normal gamma-kernel and its metric-orthogonal complement; no physical family or weak-current grading selected
action_owner: repository-construction -- existing exterior and weighted-codifferential expression, no new action or coefficient chosen
target: reducing versus invariant observation splitting and conditional independent-barred variation MAP-TYPE=intertwiner
```

## 1. What is new, and the precise conditional object

The [earlier variation result](determinant-repair-variation-2026-11-24.md)
already proves that a general independent-barred bilinear needs two cross
blocks, and that the added scalar arrow alone has a rank128 hidden response.
Neither determines the **net opposite block** of the existing reconstructed
operator. We compute it here, including the old coherent operator.

Retain the [November13 exterior comparison](source-exterior-connection-2026-11-13.md):

- the full `E=(H*⊕N*)⊗S ⊕ S` with complex Dirac S;
- `q(zeta,nu)=(b=P_H zeta,Gamma_Y zeta,nu)` and
  `K=ker q=ker Gamma_N ⊂ N*⊗S`;
- the full split-preserving connection `nabla'=nabla^LC+B`, with
  `B_XY=-II(X,Y)`, `B_Xn=S_n X`, and `B_n=0` at the section;
- coherent normal covariant jets zero at the section, and the existing
  natural two-channel NW map
  `Phi(F)=a C(F)+(c0/2)J Gamma C(F)`, with `a≠0`;
- the existing weighted-codifferential change with `grad f=H_mean`, which
  cancels the mean-curvature scalar leakage. It does not change the NW arrow.

The stable zero-SE family has `c0=-a/12`, `a e g≠0`; the opposite-block formula
below does not need that particular value of c0. No new coefficient is chosen.
SC-OP-04/05 keep the printed matrix candidate-strength and rivals open.
SC-CHI-01/04/52 describe effective separation, not exact autonomous sectors.
The `2+1`/imposter construction and four independent source fields are retained.

We first compute an operator block on this **tangential normal-jet
reconstruction**. Its metric-dual implication is conditional on using the
corresponding orthogonal barred readout and a bilinear on the SAME restricted
operator. It is not a computation of the full source's global density-dual.
Formal dualization after tangential restriction need not equal restriction of
the ambient formal dual: normal derivatives, the observation functional and
domain/end terms must be carried in the latter procedure.

## 2. The orthogonal splitting is explicit

Write `J_N psi(n)=c(n)psi` and
`Gamma_N z=sum_r eta_r c(n_r)z(n_r)` in an orthonormal normal frame. Then

    Gamma_N J_N=m I,       P_K=I-J_N Gamma_N/m,       m=dim N.

For a compatible nondegenerate spin pairing with uniform Clifford adjoint
sign, `P_K` is metric-selfadjoint and its image is nondegenerate. This follows
from `Gamma_N^dagger=±J_N`: the insertion image is nondegenerate since its
induced pairing is `±m` times the spin pairing. Thus

    E = K ⊥ O_tilde,
    O_tilde = (H*⊗S) ⊕ J_N S ⊕ S.

For observed coordinates `(b,tau,nu)`, its actual orthogonal lift is

    r(b,tau,nu)=( b + J_N(tau-Gamma_H b)/m, nu ).        (1)

This is a right inverse to the source-shaped q, not replacement of contraction
by an arbitrary projection. A scalar density multiplier does not change this
pointwise orthogonal splitting. Its analytic dual interpretation is separate.

## 3. Include the coherent operator before taking the difference

The tangential principal coefficients preserve BOTH K and O_tilde.
For hidden z, their NW output is `a c_H(xi)z`, still normal gamma-traceless;
the other output rows vanish. On the complement, the normal one-form output
of horizontal b is of the form `J_N spinor`; normal gamma-insertion input
likewise returns normal insertion, and the scalar NE arrow is horizontal.
These identities hold for the entire two-channel tangent symbol, not only its
semisimple locus.

The full split-preserving metric connection preserves horizontal/normal
bundles, their Clifford maps and this orthogonal decomposition along the
section. Consequently the coherent **tangential** differential operator has
zero blocks in both directions. This includes the derivatives of the moving
geometric projector: they vanish covariantly for that connection, not because
an arbitrary moving q was frozen numerically. Normal derivatives have been
handled only by the declared coherent-jet prescription.

For the exterior completion the already-proved difference is

    V_B(zeta,nu)=(Phi[zeta composed T_B],
                  g zeta(w_B+grad f)).

Here `T_B(X,Y)=0`, `T_B(X,n)=S_n X`, `T_B(n,m)=0`, and `w_B=-H_mean`.
The weighted correction makes the scalar component zero on **all** zeta,
not just the hidden kernel. The top component depends only on horizontal b.
Thus all net cross coupling is now located in the NW torsion insertion.

## 4. Exact opposite block and its complete vanishing criterion

Define the normal spinor-valued one-form

    A_II(b)(n)=sum_mu eta_mu c(e_mu) b(S_n e_mu).        (2)

Normal projection of `C(b composed T_B)` is exactly (2).
The normal part of the `c0 J Gamma C/2` term lies in `im J_N`, hence is
annihilated by P_K. Therefore the complete opposite block is

    B_shape := P_K D_repaired r = a P_K A_II(b).        (3)

It is independent of the observed trace/scalar coordinates and of c0.
In block form the restricted operator is

    D_repaired = [[D_K, B_shape], [0, D_O]].            (4)

Unlike the abstract triangular control in the earlier result, (3) evaluates
its off-diagonal entry on the actual source-guided geometry.

**Theorem.** In the full faithful complex Clifford representation, with
nondegenerate H,N, `dim N≥2` and `a≠0`,

    B_shape=0 for every horizontal b    iff    II=0.    (5)

**Proof.** If II=0, every shape operator vanishes. Conversely, fix one
horizontal covector input index and allow its spinor coefficient to vary.
The corresponding coefficients of A_II are matrices `A_r=c_H(v_r)`, each
pure horizontal Clifford degree1. If P_K A=0 then

    A_r = (1/m)c(n_r) F,
    F = sum_s eta_s c(n_s)c_H(v_s).

F has pure mixed Clifford degree2. For each r, multiplication by c(n_r)
has degree3 normal-pair/horizontal terms arising from each `s≠r`.
The left side has no degree3 part. Those distinct blades force every
`v_s=0`: for any s choose r≠s, possible because m≥2. The remaining degree1
part then vanishes as well. Faithfulness of the full Clifford representation
justifies the degree separation. Doing this for every horizontal input index
shows all coefficients of S_n vanish, hence II=0. ∎

In particular **zero mean curvature is insufficient**. A nonzero tracefree
II still yields this opposite coupling, even though the earlier mean-curvature
scalar leakage is zero. Conversely a totally geodesic observation is a genuine
positive control. No ambient field equation was used to declare II zero.

A smooth change of density whose only operator change is the already-tested
SW weighted-codifferential repair cannot affect (3), since that change has
no normal one-form output. This also holds for all determinant-profile rivals
with the same prescribed first jet. A different NW completion, different
barred map or changed observation is a different structural category and is
not excluded by (5).

### All metric normal extensions: a stronger necessary condition

Now keep the same tangent split correction B_X but allow arbitrary metric
normal connection values B_n, with the corresponding coherent normal-jet
prescription. This is the same structural extension category as November13
§5; it does not hold a different LC-normal-jet convention silently fixed.
For pure horizontal input `(zeta,nu)=(b,0)=r(b,Gamma_H b,0)`,
which is an allowed observed-complement input under (1), define

    A_n^H = P_H B_n|H,       (A_n^H)^dagger_g = -A_n^H.

The normal component C(b composed T_B)(n) has a horizontal-Clifford part

    C_H(n) = sum_mu eta_mu c(e_mu) b((S_n-A_n^H)e_mu),

and a normal-Clifford part coming from
`T_B(n',n)=B_(n')n-B_n n'`. The latter has no horizontal Clifford generator.
As before, the c0 J Gamma term is killed by P_K.

For a fixed horizontal input component, write the coefficient matrix as
`A_r=c_H(v_r)+c_N(w_r)`. The pure horizontal Clifford degree-one, normal-degree-zero part of
`c(n_r) sum_s eta_s c(n_s) A_s` is exactly `c_H(v_r)`:
only s=r can contract the two normal Clifford factors, while the
normal-only terms cannot create a horizontal generator. Terms with two
normal generators and one horizontal generator are a distinct degree-three
component. Therefore the pure horizontal degree-one part of P_K A_r is

    (1-1/m)c_H(v_r).

If the opposite NW block vanishes on every horizontal b, m>1 and Clifford
faithfulness force all v_r=0. Hence `S_n=A_n^H` for every n. The shape
operator is g-selfadjoint while A_n^H is g-skew, so both are zero. Thus

    zero opposite block for a metric normal extension  =>  II=0.  (5a)

This necessary condition is independent of whether the extension has also
achieved the unbarred quotient condition. Purely normal torsion terms cannot
cancel the decisive horizontal Clifford component, and a scalar-row density
repair cannot change it. It covers every metric B_n in this declared
coherent-jet/exterior completion, not just the B_n=0 representative.

The converse remains the earlier **B_n=0** positive control. An arbitrary
nonzero normal extension may retain other coupling even when II=0. Likewise,
the rank512 statement below is only for B_n=0; no uniform rank512 bound is
asserted over all extensions. Non-metric source-parent displacements,
changed NW contractions, changed readouts or different domain prescriptions
remain separate constructions.

## 5. The actual metric-bundle shape, and a native rank certificate

The [source-adapted geometry](source-chimeric-trace-compatibility-2026-11-13.md)
already supplies

    K(II(X,Y),v)=-v(X,Y)/2,
    S_v X=-(1/2)g^-1 v X,
    II(X,Y)=-(1/2)[X^flat odot Y^flat-g(X,Y)g/2].       (6)

It has mean `t/2`, norm-square `-1`, and nonzero traceless shape. These are
prior results, not re-derived progress. In an actual K-orthogonal symmetric
matrix basis n_i and Lorentz orthonormal frame e_mu,

    A_i,j=-(1/2)sum_mu eta_mu eta_j (n_i)_(j,mu) c(e_mu).

Formula (3) applies immediately and cannot vanish because (6) is not zero.
A supporting full native calculation uses S128, all ten actual normal
directions, and the trace-reversed normal Gram matrix. It is not a reduced-
dimension toy.

**Exact native rank: 512.** The probe constructs
the `1280 × 512` matrix P_K A in the coefficient field
`Q(i,sqrt(2),sqrt(3))`, reduces an integral denominator-localization at97
using `i→22`, `sqrt2→14`, `sqrt3→10`, and records maximal-minor pivot rows and
determinant. All denominators are products of2,3,5, invertible at97.
The recorded512-square minor has determinant91 modulo97. Thus the
original minor is nonzero. Since the input has dimension512, this
certificate proves complex rank512 exactly. It does not infer a
characteristic-zero kernel from a merely vanishing modular determinant.

The full observed receiver has dimension6S, but (3) depends only on b∈4S.
Its observed kernel is exactly the two
spinor trace/scalar directions. The rank is a local linear-map statement,
not a particle/family count or positivity assertion.

The tangential time coefficient respects the same decomposition and is
invertible on the stable family. Normalizing time therefore multiplies this
block by an invertible hidden coefficient and preserves its rank. This does
not identify untransported variational pairings before and after row operations.

## 6. What follows for independent barred fields

On a supplied section bilinear whose density-dual is the declared metric-spin
identification of (4), and whose barred readout uses the same orthogonal
splitting, variation with respect to observed unbarred fields includes
`B_shape^! bar-h`. Since this is a zeroth-order block, its formal dual is its
pointwise density-dual with no integration-by-parts derivative term.
Nondegenerate pairings and nonzero scalar densities preserve its rank.

Thus this specific orthogonal two-sided splitting is not reducing on the
native shape (6), even though the unbarred quotient remains invariant.
Calling every printed star a global adjoint would not supply these premises;
the source matrix's four independent fields and epsilon wrappers require
actual identification. Nor may one infer the complete source barred equation
by dualizing only the new SW arrow or only the tangential restriction.

The annihilator subspace `q^*(O*)⊂E*` is a different object from a quotient
barred observation `E*→O*`. For a true quotient-intertwining operator the
annihilator is invariant under its algebraic dual, including when B_shape is
nonzero. Restricting the barred hidden coordinate to zero can therefore be
consistent in that supplied algebraic category, but is an additional field
restriction, not a consequence of source independence or observed chirality.
For the actual thin-section functional map, its transpose also includes the
section distribution; finite-fibre duality alone cannot produce a smooth
ambient barred source. The companion source audit addresses that distinction.

Effective separation remains distinct from exact autonomy. A nonzero local
cross block alone gives no low-energy observable size without solution,
current and scale information. The source has not demanded that all dark and
luminous fields be exactly independent off shell.

## 7. Result for the joint target

This wave replaces an unspecified opposite block with the explicit geometric
map (3), its necessary-and-sufficient total-geodesicity criterion, and a
native rank check. The existing weighted scalar repair remains a valid
one-sided local closure; it does not make the canonical metric-orthogonal
splitting two-sided.

No source action, physical barred readout, full density-dual, closed analytic
domain or class-C inhabitant is constructed. No row or source verdict moves.
X-P1-P2 and secondary X-P1-P2-P3 retain the exact scope: any intended exact
independent-barred observation realization must explain its actual duality,
observation and NW cross-block treatment. Choosing a new map merely to remove
(3) would incur a different construction and its ownership burden.

## Reproducibility

`tests/program-focus/local_dual_closure_second_fundamental_form_probe.py` uses the existing SA-1
native rational metric basis, exact full Cl14 matrices modulo97, a recorded
nonzero minor certificate, and mean-zero/nonzero-shape and totally-geodesic
controls. The general criterion (5) is proved by Clifford grades, not by the
finite rank run. The serialized exact probe passed25 checks, including the native minor
certificate. Independent T2 review accepted the conditional theorem and certificate. Root replay passed25 exact checks, including the rank512 minor with residue91. See the [review](../../lab/process/hostile-reviews/2026-11-24-source-dual-grading-review.md).
