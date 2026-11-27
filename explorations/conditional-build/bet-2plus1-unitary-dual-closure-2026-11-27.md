---
title: The complete unitary weighted survivor retains the opposite shape block
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: BET-2PLUS1
tier: T1
expected_delta: Decide two-sided local closure for the complete unitary b=H survivor, beyond the previously tested metric connection extensions.
actual_delta: Every homogeneous allowed F/U connection correction factors through normal Clifford insertion on the entire observed complement. The opposite block remains Wsharp P_K A_II, so exact two-sided closure is impossible at nonzero II in the declared orthogonal dual realization.
class_covered: The existing nonzero independent chiral wedge/SE family with fixed LC-normal jets, fixed form/exterior grammar and compatible nondegenerate Hermitian Clifford pairing; all unitary spinor connections in the owned weighted b=H solution family. Barred fields use the same already-declared local orthogonal density-dual splitting, not an assumed full source functional transpose.
premises:
- explorations/conditional-build/bet-2plus1-chiral-weight-transport-2026-11-25.md
- explorations/conditional-build/local-dual-closure-second-fundamental-form-2026-11-24.md
- explorations/conditional-build/determinant-repair-variation-2026-11-24.md
- explorations/conditional-build/observation-functional-dual-2026-11-24.md
- lab/sources/source-claim-register.yaml#SC-OP-04
- lab/sources/source-claim-register.yaml#SC-OP-05
- lab/sources/source-claim-register.yaml#SC-CHI-04
source_bridge:
  status: conditional
  reason: The source supplies candidate four-independent-field grammar and effective chirality claims, but does not require exact off-shell autonomy of this q or select the orthogonal barred readout, density and global domain used here.
kill_condition: At nonzero II the full unitary weighted one-way survivor cannot make both local cross blocks vanish in the named orthogonal paired realization. A failure of the insertion factorization, ordered symbol or reference-jet identification invalidates that extension.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: CW-SE-FIXED-Q-PAIRED-ADJOINT
target_claim_verdict: Exact two-sided local realization excluded at nonzero II in the declared weighted unitary class; not a source-effective-chirality verdict.
canon_verdict_change: none
matrix_or_ledger_effect: none
---

# Weighted one-way closure does not remove the opposite shape block

```yaml
program_target: BET-2PLUS1
tier: T1
expected_delta: Extend the opposite-block test to every already-admitted unitary weighted connection and independent chiral weight.
actual_delta: Full observed-complement insertion factorization preserves the geometric opposite block; nonzero II obstructs this exact two-sided realization.
```

## Result and scope

The existing weighted-adjoint repair cancels the hidden-to-observed leakage exactly when its normal logarithmic density gradient equals the mean curvature H. **It cannot also cancel the opposite block by changing any connection in the complete compatible unitary family.** Every remaining connection correction has hidden-normal projection zero on the entire observed complement. The surviving opposite block is the old shape map multiplied by an invertible chiral weight.

This extends the November24 metric-normal-extension result to the larger unitary spinor-connection family classified on November25. It does not enumerate neighboring weights, choose a new action or infer a physical family count. The source's effective low-gravity separation is not identified with the exact off-shell autonomy tested here.

| State | Scope |
|---|---|
| **ESTABLISHED by the written proof** | Insertion factorization for all allowed homogeneous connection corrections; full opposite-block formula and II obstruction. Acceptance/controls are recorded separately. |
| **RULED OUT** | Exact two-sided local closure at II nonzero with the held q, LC-normal jets and the declared orthogonal barred density-dual realization, throughout the complete unitary weighted survivor. |
| **NOT MODELED / UNDETERMINED** | A different barred map or physical domain, nonlocal/section-supported duality, other principal or lower-order grammars, effective decoupling, source selection and GU or class-C falsification. |

```gu-typed-objects
result: complete-unitary opposite-block invariance in the weighted observation survivor
carrier: full Dirac S128; one-form plus scalar; H4/N10 split; observed6S and hidden normal gamma kernel LAYER=ambient+observed BRIDGE=literal-section-plus-gamma-trace CHIRALITY=S-FULL-DIRAC
pairing: fixed nondegenerate compatible Hermitian Clifford pairing and metric form pairing; smooth positive scalar density; named orthogonal barred dual ON=declared_local_reconstruction
real_structure: compatible Clifford real form separately supplied; complex proof and inherited native rank do not identify K77 with K95
grading: ambient chirality weights only; no physical generation or index grading
action_owner: repository-construction -- existing wedge/SE reconstruction and local paired realization; no source action or physical quotient constructed
target: observed-to-hidden cross block of the same tangential reconstruction MAP-TYPE=intertwiner
```

> **GU-COMPARATOR-ROUTING — scope before inference.** The source total theory is nonchiral and its generation target is2+1, not three ordinary repeated families. This conditional local-operator result does not adjudicate physical chirality or a family index. [Routing](../../lab/methods/source-native-comparator-routing.md).

## 1. Held coordinates, operator and complete survivor

Use an orthonormal frame e_i with eta_i=+1 or -1, gamma_i=c(e_i), gamma_i^2=eta_i and gamma^i=eta_i gamma_i. All formulas below use ordinary covector components z_i and xi_i:

    Gamma z=sum_i gamma^i z_i,    (J psi)_i=gamma_i psi,
    c(xi)=sum_i gamma^i xi_i,     i_xi z=sum_i eta_i xi_i z_i,
    A_w(xi)=c(xi)I-xi Gamma+J(c(xi)Gamma-i_xi).

These are the simultaneous covector transports of the raw conventions in [chiral-weight transport](bet-2plus1-chiral-weight-transport-2026-11-25.md) §1: F=diag(eta_i), z_cov=F z_raw and xi_cov=F xi_raw. Input, output and covector are all transported. In particular J_cov has gamma_i, while Gamma_cov has gamma^i; dropping either raised-normal sign changes the computation.

The owned symbol is

    D_xi(z,nu)=(A_w(xi) W z+xi nu, -i_xi z+c(xi) E nu),
    W=w_plus P_plus+w_minus P_minus,   w_plus w_minus nonzero.

The weights are the inherited constant real nonzero weights (parallel at the reference); variable weight fields are outside this theorem. The reciprocal southeast family E remains the existing one; its value does not enter a hidden normal one-form output. No new E is selected. Define Wsharp by exchanging w_plus,w_minus. It satisfies gamma_i W=Wsharp gamma_i. Sharp here is a coefficient exchange, **not an adjoint**.

Retain q(z,nu)=(z_H,Gamma z,nu), K=ker Gamma_N, and

    Gamma_N J_N=m I,    P_K=I-J_N Gamma_N/m,    m=10.

The compatible metric-spin pairing makes K nondegenerate and gives the existing orthogonal complement

    Otilde=(H* tensor S) plus J_N S plus S,
    r(b,tau,nu)=(b+J_N(tau-Gamma_H b)/m,nu).             (1)

A scalar density does not change this pointwise splitting.

The complete **one-way** weighted solution family is already proved in the November25 report. Write b_density for the normal gradient of log density, distinct from the horizontal field b. At b_density=H every compatible unitary spinor connection differs from the particular split connection by

    Delta K_h=U_h,       U_h†=-U_h,   U_h in Comm(Cl^0(N)),
    Delta K_r=F gamma_r, F gamma_r+kappa gamma_r F†=0 for every r. (2)

Here gamma_i†=kappa gamma_i with a uniform kappa=+1 or -1. The particular connection has K_r^0=0 and

    K_h^0=(1/2)sum_mu gamma^mu c(II_(h mu)).             (3)

Normal covariant jets are fixed using LC **before** varying the spinor connection. The full exterior/form grammar is unchanged. Consequently the connection variation is the zeroth-order operator

    Delta D=sum_i D_(e^i) diag(Delta K_i).              (4)

In its NW block W acts **after** Delta K_i. The proof never commutes W through a general connection or changes T composed with d_A into d_A composed with T.

## 2. A normal Clifford identity

Let C_N=Comm(Cl^0(N)). Equation(2) implies

    gamma_r^-1 F gamma_r=-kappa F†

independently of r. Comparing two normal indices gives F in C_N. For every X in C_N the conjugation

    sigma(X)=gamma_r^-1 X gamma_r

is independent of r, has sigma^2=I, and obeys X gamma_r=gamma_r sigma(X). Only the individually non-null orthonormal generators are inverted. There is no division by the square of an arbitrary, possibly null, vector.

W and all horizontal gamma_h lie in C_N. For X in C_N the signature-correct contractions are

    sum_r gamma^r X gamma_r=m sigma(X),
    sum_r gamma^r gamma_a gamma_r=(2-m)gamma_a.         (5)

Both follow by the Clifford anticommutation relations, with gamma^r=eta_r gamma_r. Here a is a normal index. The internal commutant need not be enumerated.

## 3. Every homogeneous correction factors through insertion on Otilde

We prove P_K Delta D r=0 by the three summands in (1). Only the normal one-form output matters; scalar outputs cannot contribute to it.

### Horizontal input (b,0)

In the normal output of the NW part of (4), every term is already prefactored by J_N except

    -sum_h gamma^h W Delta K_a b_h

at a normal output index a. Tangent U_h terms have no such contribution because their exterior index is horizontal. Using the normal adjoint condition directly,

    -sum_h gamma^h W F gamma_a b_h
      =-kappa gamma_a sum_h gamma^h Wsharp F† b_h.       (6)

The spinor after gamma_a is independent of a. Hence this is also an insertion and P_K kills it. This keeps Wsharp in its actual order and uses no commutation of W with F†.

### Normal-insertion input (J_N s,0)

For tangent U_h, its even-normal commutant condition makes diag(U_h) J_N s an insertion. W preserves the insertion image, and the horizontal wedge symbol preserves it as well. Its normal output is therefore killed by P_K.

For the normal F terms put X=WF in C_N. Apart from terms already prefactored by J_N, the normal output at a is

    sum_r gamma^r X gamma_r gamma_a s
      -sum_n gamma^n X gamma_a gamma_n s
      =m gamma_a Xs-(2-m)gamma_a Xs
      =(2m-2)gamma_a Xs.                               (7)

The first equality uses (5), sigma(X)gamma_a=gamma_a X, and the fact that X commutes with gamma_a gamma_n. Thus these columns are insertion-valued too.

### Scalar input (0,nu)

The normal NE response is simply

    Delta K_a nu=F gamma_a nu=-kappa gamma_a F†nu,       (8)

again in im J_N. Tangent NE output is horizontal and SE output scalar. Combining(6)–(8) gives the **full observed-complement identity**

    P_K Delta D r=0.                                  (9)

The density correction acts in the scalar return and cannot change(9). Higher density jets do not enter this first-order local reconstruction. No full matrix rank computation is needed for the homogeneous family.

## 4. The particular reference and the full surviving block

The reference identification is essential. Equation(3) is the spin lift of the split-preserving metric connection with

    B_XY=-II(X,Y),    B_X n=S_n X,    B_n=0.

Its normal values vanish, so its coherent normal covariant jets equal the held LC-normal jets at the section. Its tangent form connection differs from LC, but rewriting the **same exterior operator** retains the torsion insertion. Dropping that insertion would compare different operators.

Define C on two-forms by C(xi wedge z)=c(xi)z-xi Gamma z. Then

    Gamma C(xi wedge z)=2(i_xi-c(xi)Gamma)z,
    Phi0=C-(1/2)J Gamma C,
    Phi0(xi wedge z)=A_w(xi)z.

Thus the unweighted reference is precisely a member of the two-channel family in [the opposite-block theorem](local-dual-closure-second-fundamental-form-2026-11-24.md) §§3–4. That theorem did not require its special stable coefficient relation. The scalar SE term contributes no hidden-normal output.

At this metric-spin reference the held chiral weights are parallel. The weighted NW operator on z is therefore the unweighted one on Wz; this step is made only at the reference, not at arbitrary F/U. W preserves Otilde, and its horizontal component is Wb. The inherited exterior/coherent identity cancels the scalar torsion trace at b_density=H, while its full hidden-normal output is

    B0 r(b,tau,nu)=P_K A_II(Wb),
    A_II(b)(n)=sum_mu eta_mu c(e_mu)b(S_n e_mu).        (10)

In particular the trace and scalar columns vanish at the reference. Each coefficient of A_II is horizontal Clifford degree1, so A_II(Wb)=Wsharp A_II(b). P_K commutes with Wsharp. Equations(9)–(10) give the full formula for every connection in(2):

    B_unitary r(b,tau,nu)=Wsharp P_K A_II(b).           (11)

The old full-Clifford shape theorem proves P_K A_II=0 for all b iff II=0, for m at least2. Wsharp is invertible. Hence no member of the complete weighted unitary survivor is a reducing two-sided local splitting when II is nonzero. The criterion is stronger than H=0: tracefree nonzero II also obstructs it. If II=0, the zero homogeneous connection and zero required density jet provide the old positive control.

### Native rank, with its actual geometry binding

For the **same actual metric-bundle shape and native full128-spinor port** used in the inherited report §5, the matrix P_K A_II from4S to the normal gamma kernel has certified complex rank512. The source is the recorded nonzero512-square minor modulo97, determinant91, with denominators invertible there. It is reused, not rerun here.

The full reference equality(10), including its zero trace/scalar columns, is why the full6S block has rank512 rather than merely a lower bound. Equation(9) preserves that whole block, and invertible Wsharp preserves rank. Thus **the full block has exact complex rank512 in that authenticated native port**. If only the pure-horizontal reference is transferred to another port, the inherited minor gives only a rank lower bound after that transfer is justified. The II criterion itself is the signature-compatible algebraic theorem; no K77/K95 geometric identification or new rank calculation is inferred by relabeling. These coefficient dimensions are not particle or family counts.

## 5. Independent barred fields and the inference ceiling

For the already-declared local section bilinear with the same nondegenerate metric-spin pairing, positive scalar density and orthogonal barred splitting, the nonzero opposite block contributes its density-dual to the equation obtained by varying observed unbarred fields. It is zeroth-order, so no integration-by-parts derivative can erase it. Independent observed bars/unbars require both cross blocks to vanish for exact autonomy with arbitrary independent hidden fields. The one-way q closure remains true; the opposite block fails.

This is not an identification of the source's completed barred observation. The functional transpose of literal unrestricted section observation is a section-supported current, as proved in [observation functional duality](observation-functional-dual-2026-11-24.md). Restricting an ambient formal dual and dualizing a tangential reconstruction need not agree. A supplied annihilator restriction on bars, stronger/nonlocal Riesz map, section-supported action or different physical domain changes the tested category; none is selected or certified here.

SC-OP-04 **ASSERTS** candidate-strength four-independent-field grammar. SC-OP-05 is **UNCERTAIN** about unselected southeast rivals. SC-CHI-04 **ASSERTS** emergent effective chirality in low gravitational regimes, not the exact off-shell q-autonomy used here. SC-GEN-01 **DISAVOWS** simple triplication; source2+1, imposter and RS labels remain separate. A nonzero local cross block alone supplies neither a low-energy coupling magnitude nor a physical chirality/count verdict.

**Consumed:** further changes of W, reciprocal E or F/U within this exact paired realization as attempts to erase the opposite block. **Still open:** the actual source density/bar/current/global-domain bridge and genuinely different operator or observation categories. Existing bounded-profile, infinite-volume and graph-trace results are not rerun or promoted to physical necessities. No new action, choice family, source prediction, matrix/ledger/canon verdict or guessed action variant is added.

## 6. Verification scope

The new proof is the full-complement insertion calculation(6)–(9) and its correctly matched composition with the old reference block. Existing complete one-way classification, geometric shape and native rank are inherited with their premises.

`Lean/GUFormalization/UnitaryDualClosure.lean` proves only projection of an insertion-factored block vanishes, and that invertible postcomposition preserves whether a linear map is zero. It supplies no Clifford, adjoint, source, jet, domain or rank512 premise. Small Clifford controls calibrate the ordered identities, not the full native dimension. Exact controls, dependency hashes, targeted compilation and independent T1 reviews are recorded by the root verification packet; this draft attributes no execution to its author.
