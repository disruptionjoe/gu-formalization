---
title: "K2449 Full mixed adjoint with the repeated-polar boundary ideal"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: "full original adjoint and equivalent geometric-bound question; no proved geometric bound or nonlinear convergence"
---

# K2449 Full mixed adjoint with the repeated-polar boundary ideal

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
result: K2449
carrier: original repeated-polar hook generators and raw105 symmetric receivers over fourteen coordinates LAYER=toy CHIRALITY=N/A
pairing: positive coefficient Fischer inner product ON=declared_carrier
real_structure: real exact coefficients or complex coefficients with positive Hermitian coefficient norm
grading: seven transverse E coordinates and seven passive W coordinates; homogeneous field degree d
action_owner: repository-construction -- supplied conditional mathematical model
target: exact joint annihilator and quantitative inverse criterion MAP-TYPE=evaluation
```

## Result and custody

The complete mixed adjoint can be tested without discarding the repeated-polar boundary ideal, passive derivatives, or the outer derivatives of linear generators. This supplies one fixed generator bank and an exact quotient for the unresolved analytic estimate. It is a new explicit joint formulation and independent dual argument for the inherited image, not a new all-degree rank claim. K2437 already proves the compatible formal image; K2446 only gives a quadratic-exponential inverse ceiling. Neither is promoted to convergence here.

SC-ACT-01 and SC-GEO-55 remain ASSERTS at their native source scopes. This hook construction is conditional; SC-META-53 remains UNCERTAIN. Source, ledger0.263 and canon are unchanged.

## 1. Original operator and allowed fields

Write X=(y0,...,y6,z0,...,z6). The original constant repeated-polar generators are h in the161-element bank. Their scalar coefficients f of field degree d must vanish on y=0, so f lies in I_E=(y0,...,y6). The112 original linear generators G(X)=sum_t y_t h_t multiply arbitrary homogeneous degree d-1 polynomials. These two families generate the admissible field space; retain their redundancy.

Let A_r(h) be the original raw symmetric105 ordinary Euler symbol on ambient covector r. Write the original scalar operator

    Jstar(h f)=sum_r a_r(h) partial_r f
                 +sum_(r,s,t) b_rst(h) y_t partial_r partial_s f,
    J_d=(4/d)Jstar,       r,s=0,...,13, t=0,...,6.

All A,a,b come from the original tensor contractions, with the original split metric and fixed Q(sqrt2) embedding. No transverse-only or constant-symbol replacement is made. The positive coefficient inner product used for the estimate is a mathematical norm; it is not a physical state pairing.

For a receiver (Q,p) of degree d-1, use the unnormalized Fischer inner product <X^alpha,X^beta>=delta_alpha,beta alpha!. Then the scalar adjoint polynomial of degree d is

    U_h(Q,p)=sum_r X_r <A_r(h),Q>
       +(4/d)[sum_r a_r(h)X_r p
                    +sum_(r,s,t) b_rst(h)X_r X_s partial_(y_t) p].       (1)

The order X_r X_s partial_t is essential. Multiplication by y_t occurs before taking the adjoint, hence partial_t acts first on p. Reversing that order introduces false lower terms.

## 2. Boundary and linear-generator adjoint

The repeated field pairing vanishes for every f in I_E iff

    Pi_(I_E) U_h=0,

not iff U_h=0. Equivalently partial_(y_i)U_h=0 for every i<7. For G=sum_t y_t h_t, its coefficient adjoint is

    sum_t partial_(y_t) U_(h_t).                          (2)

Thus parameterizing every repeated field as sum_i y_i h f_ih gives a degree-preserving joint adjoint bank with1127+112=1239 polynomial rows: partial_i U_h and(2). Input and receiver parameter degree are both d-1. Dividing both Fischer norms by(d-1)! therefore changes no adjoint coefficient in this bank. In particular no extra d may be inserted into(1), and the actual4/d remains.

The proof is coefficientwise Fischer duality: derivative and coordinate multiplication are Fischer adjoints. The monomials supported entirely in W are orthogonal to I_E. Taking the adjoint of multiplication by a linear generator introduces the outer derivative in(2). The finite probe checks these identities on the original mixed tensors, including fixtures chosen from nonzero outputs to avoid vacuous pairings.

## 3. Exact kernel of the joint bank

Reuse K2437's diagonal image theorem and the original universal trace and double-divergence identities. In the raw105 receiver convention let tau be the universal trace vector and b_full(X) the corresponding full ambient quadratic double-divergence symbol. The full adjoint kernel is precisely

    (Q,p)=(tau f+b_full g,0),                            (3)

Here tau_ii=eta_i with zero off-diagonal entries and b_full,ij=(2-delta_ij)eta_i eta_j xi_i xi_j, where xi_i=sum_r covs[r][i]X_r. The raw105 dot product does not insert an orthonormal symmetric-tensor rescaling.

Here deg f=d-1 and deg g=d-3 (negative degrees mean zero). This is also the ordinary ambient compatibility kernel inherited from K2437, now recovered dually.

To see the reverse inclusion, take a receiver in the joint kernel and its largest remaining E degree k. Test admissible fields with E degree k+1, keeping arbitrary passive monomials. All mixed W contributions have output E degree k+1 or k+2, and therefore pair to zero against this receiver. The top block is in the augmented transverse adjoint kernel: p_k=0 and Q_k=tau f_k+b_E g_(k-2), by the inherited all-degree theorem, coefficientwise in W. Subtract the full universal kernel element tau f_k+b_full g_(k-2). Its top E block agrees; b_full-b_E has only E degrees1 and0, so subtraction creates lower E-degree blocks only. Descending induction terminates. The forward inclusion is the exact full trace/double-divergence identity. This argument does not estimate the size of the elimination coefficients.

## 4. Quantitative question without a false convergence claim

Use normalized Fischer norm ||f||_d^2=sum_alpha |f_alpha|^2 alpha!/d!. For homogeneous degree d U,

    sum_i<7 ||partial_i U||_(d-1)^2
       =d sum_alpha alpha_E |U_alpha|^2 alpha!/d!,

so the sum lies between d||Pi_I U||_d^2 and d^2||Pi_I U||_d^2. The boundary projection and derivative bank differ by polynomial factors only.

There is likewise a controlled right inverse of boundary synthesis. For f in I_E define f_i=partial_i(E_E^(-1)f), with E_E^(-1) dividing each original f monomial by alpha_E before differentiation. Then sum_i y_i f_i=f and

    ||f||_d^2 <= sum_i ||f_i||_(d-1)^2 <= d||f||_d^2.       (4)

Consequently representing the boundary ideal adds at most sqrt(d) in this norm. Fixed generator synthesis costs at most a degree polynomial and fixed constants, since the bank is finite and multiplication by a coordinate is bounded between normalized homogeneous norms. These are norms on the fixed parameter bank; kernel redundancies remain quotiented.

Let T_d be the1239-row adjoint acting on the orthogonal complement of(3). A bound

    ||(Q,p)|| <= C^d ||T_d(Q,p)||                         (5)

would, by finite-dimensional singular-value duality, give a geometric right inverse of the full primal coefficient map on its compatible image. Synthesis and coefficient/Fischer norm conversions cost at most polynomial times fixed-exponential factors, so(5) really would imply a positive analytic radius for the linear forcing problem. It would avoid multiplying separate diagonal inverse losses. No such C is established here. A finite singular-value plot cannot prove(5), and a linear bound alone would not close the nonlinear majorant, shared section, or exact neighborhood realization.

## 5. Discriminators and next step

The exact probe retains full ambient A,a,b. It tests mixed primal/dual pairings, original linear generators, boundary-only W pieces, and polynomial norm/synthesis identities. Deliberately omitting W coefficients, reversing the second-order adjoint, omitting an outer derivative, and dropping4/d must each produce a nonzero defect. The inherited h is still only a transverse ordinary kernel, not an ambient one.

The next mathematical target is(5) in this exact quotient, or an original invariant subfamily disproving a proposed bound. Constant-symbol division, the scalar primitive alone, and additional finite rank banks do not settle it. The geometric problem stays open at a more explicit and independently checkable operator.

[Exact probe](../../tests/channel-swings/k2449_full_mixed_boundary_adjoint_probe.py), [report](../../lab/process/k2449-full-mixed-boundary-adjoint.json). Universal proofs, finite original-object checks and prospective budgets are separate evidence. Internal independent review is not external-expert or proof-assistant certification.
