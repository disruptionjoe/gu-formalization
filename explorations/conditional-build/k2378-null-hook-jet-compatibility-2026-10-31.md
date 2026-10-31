---
title: "K2378 A rational null hook jet meets finite second-jet compatibility"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional selected-action mathematics; no native GU verdict
scripts:
  - tests/channel-swings/k2378_null_hook_jet_compatibility_probe.py
---

# K2378 A rational null hook jet meets finite second-jet compatibility

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
result: K2378
carrier: zero-value hook tensor with first and second covariant jets on K2345 geometry LAYER=toy CHIRALITY=N/A
pairing: nondegenerate real Clifford trace and Levi-Civita metric ON=declared_carrier
real_structure: real Cl(7,7); real hook tensors and signed covariant jet pairing
grading: hook algebraic constraints through order two and Euler equation through order one
action_owner: repository-construction -- selected comm/symi/symi I1 with independent fixed metric and epsilon
target: finite jet compatibility, with no local solution claim MAP-TYPE=evaluation
```

# Null-image hook jet and finite second-jet compatibility

Scope: conditional K2375 selected action on its actual K2345 metric, at a single point with H=0 and kappa²=280/31. This neither constructs a local stationary field nor proves formal integrability. No source-native GU identification or verdict follows.

## Full necessary algebraic second derivatives

Write K_l=∇_lH at the point. Metric compatibility and H=0 imply

    ∇_l∇_m h² = 2<K_l,K_m>,
    ∇_l∇_m sigma_H = 2 sum_i eta_i (K_l)_i wedge (K_m)_i.

Thus every pair must vanish, not just the contracted Laplacian. The four-form polar expression is symmetric because its factors have degree two. Unknown second derivatives cannot affect these tests at a zero of H.

## Explicit rational zero-value one-jet that passes every pair

Use eta=(+,-,-,-,+,+,+,+,+,+,-,-,-,-). Number the seven ordered positive/negative pairs r=0,...,6, in the displayed order:

    (p_r,q_r)=(0,1),(4,2),(5,3),(6,10),(7,11),(8,12),(9,13).

Let lambda_i=27/28 on {0,1,2,3,10} and -15/28 otherwise; this is the actual Ric_tf endomorphism eigenvalue, not an assumed positive metric. Define t_r=lambda_p+lambda_q, and s(i) the pair containing i. Put

    d^r_i=0                                           if s(i)=r,
    d^r_i=lambda_i/6+t_r/70+t_s(i)/420                otherwise.

Since sum_i lambda_i=sum_r t_r=0,

    sum_i d^r_i=(-1/6+12/70-2/420)t_r=0,
    sum_r d^r_i=lambda_i+(-1/70+6/420)t_s(i)=lambda_i.

Let u_r=e^p_r+e^q_r. Define the only nonzero derivative slices by

    (K_p_r)_i=eta_i d^r_i e^i wedge u_r,
    K_q_r=0.

Each slice is a hook: its components contain a repeated index, so total alternation vanishes; contraction is u_r sum_i d^r_i=0. Support excludes the paired indices. Direct contraction gives B_ii=-eta_i sum_r d^r_i=-Ric_tf,ij and offdiagonal B=0. Thus B+B^T=-2Ric_tf.

For every fixed form index i every slice contains the common internal factor e^i. Hence all sigma polar wedges vanish. Also

    <e^i wedge u_r,e^i wedge u_s>
       =eta_i <u_r,u_s>-u_r(i)u_s(i).

The first term vanishes because the u_r are mutually orthogonal null covectors. The second vanishes after multiplication by the coefficients: if u_r(i) is nonzero, d^r_i=0. Consequently all 196 Gram pairs vanish. This is stronger than cancellation of the signed total derivative norm and preserves the full Hessian constraints.

## Symmetric second jet matching the differentiated PDE

Do not assume ∇Ric=0. Put C_lij=-2∇_l Ric_tf,ij at the point. Constant scalar curvature and contracted Bianchi give both

    g^ij C_lij=0,      g^li C_lij=0.

C is symmetric in i,j. Split

    C3_lij=(C_lij+C_ilj+C_jli)/3,
    C21=C-C3.

Both pieces have both traces zero. Define

    S=(13/180)C3+(26/363)C21.

For any tracefree symmetric two-tensor T, define the K2375 hook injection

    J_l(T)_ijk=g_lj T_ik-g_lk T_ij
                -(g_ij T_lk-g_ik T_lj)/13.

Then set

    L_lm;ijk=1/2 [J_m(S_l)_ijk+J_l(S_m)_ijk].

Each L slice is a hook and L_lm=L_ml. Let D_i=g^mk S_mik. Direct contraction yields, in general dimension n with c=n(n-2)/(n-1),

    g^mk(L_lm;i k j+L_lm;j k i)
      =(c+1)S_lij-(g_lj D_i+g_li D_j)/2
        -(S_ilj+S_jli)/(2(n-1))+g_ij D_l/(n-1).

Here D=0. At n=14 the map has eigenvalue 180/13 on C3 and 363/26 on C21, establishing the right inverse exactly. The quadratic U,W terms have zero first derivative at H=0, so this is precisely the first covariant derivative of the grade-one PDE. The curvature identity [∇_l,∇_m]H=R_lm·H has zero right side here. Thus symmetric L is consistent with the actual curvature commutator and is realizable as a covariant second jet at this zero.

The result establishes a complete finite second jet: field equation at the point, first derivative of its first-order PDE, algebraic constraints and their first/second derivatives, and second derivative commutation. It does NOT establish the twice-differentiated PDE, algebraic third derivatives (which involve K and L), third-jet curvature commutation (which involves R·K), a formal infinite jet, local existence, or global existence.

## Executed successor: double-divergence rejects the first candidate

Use the actual curvature convention R(X,Y)=[nabla_X,nabla_Y] on vectors.
Since H is skew in its last two indices,

    nabla^j B_ij = (1/2)[nabla^j,nabla^k] H_ikj
                = -(1/2) R^a_i{}^{jk} H_akj.

The two internal-index curvature terms contract symmetric Ricci against a skew pair and vanish. The double divergence of a tensor and its transpose agree (the double codifferential of their alternating difference is zero). At H=0 this therefore gives

    div div(B+B^T) = -R^a_i{}^{jk} K^i_akj.                 (8)

No unknown third jet can change this contracted identity. Define P_ab=nabla^i H_iab, X=(1/2)nabla^i H_jab nabla^j H_i{}^ab, and Y=nabla^j H_aib nabla^i H^a_j{}^b. For the displayed jet P=0. Product differentiation at H=0 gives div div U=X and div div W=|B|²+Y. The Ricci source has zero divergence because R=-10 is constant. Thus a necessary compatibility is

    -R^a_i{}^{jk} K^i_akj = (4/3)(|B|²+Y-2X).             (9)

The actual K2345 metric backend, transformed to the stated orthonormal frame, verifies every curvature entry used. Exact contractions give X=-1167/7840, Y=4797/3920, |B|²=405/56. The left side is33/35; the right is817/70; their defect is **-751/70**. The constructed finite second jet therefore cannot extend to a smooth local solution with that first jet. This is a stronger test than the previously failed norm Laplacian, with actual curvature dependence. The finite-order compatibility proved above remains true.

## Repair search preserves the earlier constraints

There is a seven-parameter family preserving all the preceding first-jet and quadratic algebraic constraints. Let H^r_i=eta_i d^r_i e^i wedge u_r and replace

    K_p_r=(1+b_r)H^r,     K_q_r=b_r H^r.

B depends on (1+b_r)-b_r=1, so is unchanged; all pairwise Gram and sigma products remain zero; P remains zero. The universal second-jet right inverse also remains applicable because the derivative of the quadratic field terms still vanishes at H=0.

With a common b across all seven pairs, the defect (9) is

    -(280 b²+421 b+3004)/280.

Its discriminant is negative and its leading coefficient is negative: this entire one-parameter repair family is excluded by (9), not merely the original b=0 point.

Independent parameters behave differently. The exact defect is

    -(1120 b1 b2+1120 b1 b3+1972 b1+1120 b2 b3
       +1972 b2+1114 b3-3 b4-3 b6+36048)/3360.

It is indefinite and has unconstrained affine directions. For example **b1=-9012/493 with every other b_r=0**, acting on the second pair (4,2), gives zero defect. Alternatively b1=-b2=±sqrt(2253/70) and all others zero works. Both are real exact scalar repairs, not approximate cancellation. In particular the common-parameter exclusion cannot be promoted to this larger family. Neither root alone certifies the full third-order norm/sigma constraints or twice-differentiated tensor PDE. Those constraints, not another scalar fit, decide the next prolongation.

## Actual third-order test: all seven parameters fail with this second jet

The rational scalar repair was followed through against actual differentiated geometry. In coordinate vertical directions E,F put A=g^-1 E, B=g^-1 F. The actual Ricci tensor has blocks

    Ric_horizontal=g/4,
    Ric_vertical(E,F)=-(5/4)tr(AB)+(1/4)tr(A)tr(B),
    Ric_mixed=0.

These follow from the actual Ricci eigenspaces and the metric's translation/GL congruence transport, rather than assuming Ricci parallel. Differentiating these coordinate expressions and subtracting both Levi-Civita connection actions produces C=-2 nabla Ric_tf. Since nabla g=0 and R is constant, this equals -2 nabla Ric. The probe uses K2345's actual metric derivatives and connection, transforms to the stated frame, obtains48 nonzero C components, checks both trace conditions, and checks every component of the differentiated PDE with the displayed universal L. Vertical covariant derivatives of Ric vanish; horizontal mixed ones do not.

At H=0, the third derivatives of the algebraic constraints are independent of any third H jet:

    nabla_abc h²=2(<L_ab,K_c>+<L_ac,K_b>+<L_bc,K_a>),
    nabla_abc sigma=2[polar(L_ab,K_c)+polar(L_ac,K_b)
                     +polar(L_bc,K_a)].                 (10)

Here polar(U,V)=sum_i eta_i U_i wedge V_i. Two four-form components alone give a complete contradiction for the **whole seven-parameter first-jet family with this fixed L**. Let c=-167063 sqrt(2)/2032800, which is nonzero. The exact actual-geometry values are

    (nabla_000 sigma)_(0,1,2,12)=c(1+b0),
    (nabla_111 sigma)_(0,1,3,8) =c b0.

Both must vanish. Dividing by c and subtracting gives 1=0. The other six parameters cannot alter either row. Thus neither the original jet nor the scalar-repaired jet nor another member of this family extends with this displayed second derivative. This argument checks actual full constraint components, not only a scalar contraction or a finite search.

The conclusion is deliberately narrower than excluding the first-jet family with arbitrary L: one may add a symmetric hook-valued kernel to L while preserving its differentiated divergence. That changes (10). The next repair must solve that joint linear constraint before claiming a third jet; mere scalar cancellation is insufficient.

## A second-derivative repair attempt is excluded by support

A natural repair would put every L_lm in the common-null space of the repeated-index hooks, so all mixed third-order norm/sigma products with K vanish automatically. Allow all coefficients, not just the seven fixed H^r: for each pair r use H_i=eta_i d_i e^i wedge u_r with d_p_r=d_q_r=0 and sum_i d_i=0. There are12 available coefficients minus one trace, hence11 per pair and77 independent dimensions in all.

This complete proposed repair space fails the actual differentiated PDE. For every member, every m and each paired (p_r,q_r), H_p_r,m,q_r=H_q_r,m,p_r=0: an internal u_s component is supported at p_r or q_r only when s=r, whose corresponding d vanishes. Therefore any second jet with values in this space forces D_l,p_r,q_r=0, independent of its coefficient functions and derivative-index symmetry.

But the actual geometry gives **C_2,4,2=3/4** for pair r=1=(4,2). This is checked both by the full coordinate Ricci derivative and the independent mixed-connection formula C(X,H,U)=(3/2)g(H,S_U X) for traceless vertical U; take X=H=e2 and S4=diag(1,1,-1,-1)/2. The required equality would be0=3/4. The probe checks all77 basis tensors against every paired receiver.

Thus this whole natural common-null repair is ruled out. General L outside this subspace may still satisfy only the required *mixed* third constraints; there is no justification for forcing it to lie in the common-null space. Constructing that larger coupled kernel, then the full third-jet equations, is the exact remaining task. No general hook-field exclusion or local existence follows.

## Controls and strongest overclaim

- K2375's J_l(S) one-jet remains rejected by its nonzero contracted norm; this new construction changes the jet, not that conclusion.
- A lone negative-norm kernel correction can cancel a contracted scalar while leaving a nonzero full Gram matrix.
- Replacing one null u_r by e^p_r makes at least one diagonal Gram pair nonzero.
- Deleting the row-sum correction destroys hook traces; dropping the column constraint destroys B matching.
- A nonzero sigma control such as H045+H067 confirms wedge checks are capable of failure.
- Treating L=0 as a second-jet solution would require actual ∇Ric=0 and is not asserted.
- The second-jet right inverse is proved symbolically for every C with its stated two trace conditions. Exact fixtures check symmetric, hook, signed and mixed components; they are normalization controls, not the universal proof.

Independent algebra review checked the middle-slot divergence, both eigenvalues and the exact derivative orders. Exact replay is documented in the companion report. Internal review is not proof-assistant or external-expert certification. The twice-diverged equation has now been tested and repaired in the broader family; solve the joint second-jet kernel and mixed third-order constraint problem next. No local solution is established.

## Source, retained result and evidence boundary

This is conditional selected-action mathematics. SC-ACT-01/02/06 and SC-GEO-55 ASSERTS retain their source meaning; SC-META-56 DISAVOWS requiring a separate odd action. Source polarities and the physics ledger remain unchanged. [K2375](k2375-axial-hook-stationarity-2026-10-31.md) owns the complete hook equation and rejected old jet; K2345 is not assumed as a new convention: actual geometry is inherited by the exact predecessor dependency in the companion report. No general hook exclusion, nonlinear local existence or physical GU conclusion follows.
