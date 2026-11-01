---
title: "K2422 Joint recovery optimality and balanced uncertainty"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional positive-Hilbert channel mathematics; no native GU or device verdict
scripts:
  - tests/channel-swings/k2422_joint_recovery_optimality_probe.py
---

# K2422 Joint recovery optimality and balanced uncertainty

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
result: K2422
carrier: physical planar flagged qubit instruments with shared good and bad decoders LAYER=toy CHIRALITY=N/A
pairing: half-diamond channel error and output-first unnormalized Choi trace ON=declared_instrument
real_structure: real planar Bloch data with complex Hermitian positive Choi matrices
grading: good/bad records; planar and perpendicular channel blocks
action_owner: repository-construction -- inherited recorded-instrument model
target: joint minimax recovery certificates and balanced uncertainty MAP-TYPE=evaluation
```

## Results

The finite variable-loss recovery problem has an attained exact joint dual and a four-term nonnegative optimality-gap identity. It covers both the good decoder and the physically coupled bad decoder. This extends [K2407](k2407-finite-minimax-certificates-2026-10-31.md)'s fixed-loss bad-channel dual using [K2419](k2419-positive-visibility-dual-2026-10-31.md)'s good-disk reduction.

The full identity-optimality question is also settled by a singular-safe3-by-3 matrix criterion on active-law mixtures (section5). A useful explicit consequence is an exact minimax theorem. Define

    E0 = max_i w_i (3−tr Q_i)/4.

If zero belongs to the convex hull of **loss-weighted means w_i m_i of laws attaining E0**, identity good and positive-sign decoding, with the inherited Y correction on the negative sign, is globally optimal over all shared CPTP decoders. At most three active laws suffice for this certificate. Mean-antipodal uncertainty at each fixed w,Q is a corollary; varying losses and moment traces are allowed. A three-law, non-antipodal exact fixture attains1/2.

The asymmetric K2419 pair does not meet this sufficient condition, and its exact optimum remains open within the existing bracket. No new numerical optimum is claimed for it. These are imported positive-Hilbert channel constructions: SC-META-53 remains UNCERTAIN, and no GU quotient, measured apparatus, calibrated clock or ledger verdict is supplied.

## 1. Objects and convex primal

Each law is a probability distribution of unit planar axes n and physical visibility0≤v≤1, with mean m=E[n], Q=E[v nnᵀ], and loss0≤w≤1. The original bad-sign map is

    J_z(rho)=E[(Tr rho+z n·r)/2 · (I+v n·sigma)/2], z=±1.

The good record carries the identity input. Means and moments are from the SAME law; arbitrary independently supplied vectors/matrices are not automatically physical. Q is positive semidefinite with trace≤1.

K2419's common sign/conjugation averaging and good-channel theorem reduce arbitrary shared recovery to a real bad CPTP Choi matrix J, Tr_out J=I2, and good planar block

    G(g)=[[a,b],[-b,a]], g=(a,b), ||g||≤1,

with perpendicular multiplier1. The optimum over this convex disk equals the original optimum; at least one optimal good controller is a unitary. Keep the disk for minimax, not a nonconvex circle substitution.

For B_i=t m_iᵀ+A Q_i, C_i=I−(1−w_i)G−w_iB_i, define

    ell_i=(tr C_i, C_i12−C_i21), L_i=||ell_i||.

Physical pointer outputs give ||B_i||_*≤1. Hence the complete channel norm reduces to E_i=(w_i+L_i)/4 for these disk-good controllers, including nonsymmetric B_i. The primal is min_(g,J) max_i E_i. It is compact and convex. Real J includes the hidden perpendicular multiplier required for complete positivity; never optimize t and A as independent contractions.

## 2. Complete attained joint dual

Choose p_i≥0, sum p_i=1 and q_i=(q_ci,q_si), ||q_i||≤p_i. Let F(q)=[[q_c,q_s],[-q_s,q_c]] and

    s=sum (1−w_i)q_i,
    v=sum w_i F(q_i)m_i,
    M=sum w_i F(q_i)Q_i,
    H=(sum v_a sigma_a tensor I + sum M_ab sigma_a tensor sigma_b^T)/2,

where sigma=(X,Z). Then

    4E* = max [sum p_i w_i + 2sum q_ci −2||s||−Tr Z]
          subject to I tensor Z−H >=0.                 (1)

Norm support and the simplex encode the maximum of the endpoint costs. The resulting objective is bilinear between compact convex primal and (p,q) sets, so minimax exchanges their extrema. The good support is2||s||. For the bad support, Tr(HJ)=v·t+<M,A>, and J=I4/2 is strictly feasible with Tr_out J=I2. Semidefinite strong duality supplies an attained Z and support Tr Z. The support is continuous in compact(p,q), so the outer maximum and a corresponding Z are attained. Complex Hermitian duals can be averaged with conjugation because H is real.

These are applications of standard [Sion minimax](https://msp.org/pjm/1958/8-1/pjm-v8-n1-p14-p.pdf) and [semidefinite duality](https://web.stanford.edu/~boyd/papers/pdf/semidef_prog.pdf), not novelty claims. Compactness, physical symmetry and strict feasibility are checked hypotheses here.

## 3. Exact gap, matching and stable certificates

For a feasible primal with E≥max E_i and dual slack D=I tensor Z−H≥0, subtract(1) from4E:

    4E−dual = sum p_i(4E−w_i−L_i)
              + sum(p_i L_i−q_i·ell_i)
              + 2(||s||−g·s) + Tr(DJ).                (2)

Every term is nonnegative. Thus their sum divided by4 bounds this controller's excess over the true optimum. Zero sum is an exact global certificate. It requires active endpoint support; q_i=p_i ell_i/L_i when p_i>0 and L_i>0; g=s/||s|| when s≠0; and DJ=0. At zero radius retain the norm-subgradient disk rather than divide by zero. For K2419's strictly positive losses, L_i≥w_i>0.

Conversely saddle-point optimality produces matching witnesses. These equations are algebraic after adjoining nonnegative square-root variables, so an isolated algebraic solution with original PSD/TP checks could settle K2419 exactly. Its current dual is positive definite and cannot match a nonzero TP J; a matching certificate needs singular slack. The probe verifies this using the actual old matrices and all four gap terms. A minimax bad decoder need not be extreme or rank2.

Two quantitative consequences follow without uniqueness:

- If a candidate certificate gives E−dual/4≤epsilon and D≥gamma P_perp for an orthogonal projection, then Tr(P_perp J)≤4epsilon/gamma. This bounds Choi weight outside the exposed optimal face.
- For s≠0, ||g−s/||s||||≤2 sqrt(epsilon/||s||). This bounds good-disk misalignment, not distance to a unique entire controller.

A numerically suggested dual is not a certificate until its PSD error is bounded. If exact/interval evidence proves D≥−eta I4, replace Z by Z+eta I2. This restores feasibility, lowers the dual by2eta and adds eta/2 to the error-gap bound. Mere floating-point eigenvalues are insufficient evidence.

For a compact variable-loss family, a finite active certificate with at most nine laws exists. The convex controller image has eight coordinates(g2,t2,A4). At an optimum, the max-function subgradient is a convex combination of active support gradients whose negative lies in the feasible normal cone. Caratheodory in R8 reduces this combination to nine. Multiple directions at one zero-radius law can be merged within its support disk. This is an existence bound, not a method for identifying the active laws, and does not claim nine are necessary.

## 4. Exact balanced-active-law theorem

For identity decoding, B_i=Q_i and G=I. Write lambda1,lambda2 for the nonnegative eigenvalues of Q_i. Then

    L_i=w_i(2−tr Q_i), H_i=w_i|lambda1−lambda2|≤w_i,
    E_i=w_i(3−tr Q_i)/4.

Suppose p is supported on maximizers of this cost and sum p_i w_i m_i=0. Set q_i=(p_i,0). Then s=(1−barw,0), v=0, M=sum p_i w_i Q_i≥0, and choose Z=(tr M/2)I. If M=sum lambda_j e_j e_jᵀ,

    D=(1/2)sum lambda_j [I4−sigma(e_j) tensor sigma(e_j)^T] >=0.

Each term is PSD and annihilates the unnormalized Bell vector |Omega>. Therefore DJ_identity=0. Equation(1) equals sum p_i w_i(3−tr Q_i)=4E0, matching identity. This proves unrestricted global optimality. At most three active laws suffice by Caratheodory in the two-dimensional weighted-mean plane.

A direct independent lower bound also avoids minimax (write d_i=1−(1−w_i)g_y): for any common symmetry-averaged controller, E_i≥(d_i+tr C_i)/4. Balanced averaging cancels translation. Using g_y≤1, tr G≤2, ||A||op≤1 and M≥0 gives4 max E_i≥3barw−tr M=4E0. The identities and contraction bounds refer to the original physical channels.

The condition is sufficient, not necessary. It extends K2404's fixed-loss/fixed-trace identity criterion without contradicting its unpaired variable-trace counterexample. Global antipodal symmetry is stronger than needed: one E0-maximizing law and its partner at the **same w,Q** suffice. If every law has that partner, the theorem applies immediately even with variable w and trace Q.

The probe constructs a non-antipodal three-law family with losses(4/5,1,5/6), moment traces(1/2,1,3/5), axes((1,0),(0,1),−(3/5,4/5)) and mean lengths(3/8,2/5,3/5). Its weighted means sum to zero and every identity error is1/2. Original instruments, full channels and the matching singular dual are checked exactly. Separate paired examples include nonscalar Q and changing trace/loss. A single deterministic-axis law violates the balance condition and constant decoding beats identity, testing the theorem's boundary.

## 5. Complete identity-optimality criterion

The balanced condition has a necessary-and-sufficient extension. Let A be the active law set attaining E0. For a compact physical family with E0>0, identity is globally optimal **if and only if** there are probabilities p supported on A such that

    M=sum p_i w_i Q_i, v=sum p_i w_i m_i,
    v vᵀ <= (tr M) M.                                 (3)

This is a small semidefinite feasibility problem in the active probabilities, not an optimization over decoder channels. Equivalently require the3-by-3 linear matrix inequality

    [[M, v], [vᵀ, tr M]] >=0.                          (4)

The equivalence includes singular cases: if tr M=0, M=0 and both conditions require v=0; otherwise take the scalar Schur complement. For positive definite M it is vᵀ M^(-1)v≤tr M. For rank1, also retain the range condition on v. No inverse is used in(3) or(4).

**Necessity.** An attained joint dual at identity must saturate each nonnegative term in(2). Active laws have w>0 and hence L>0, so q_i=(p_i,0). Complementarity D J_identity=0 forces

    Z=(tr M I+v_x X+v_z Z_Pauli)/2.

To see uniqueness, (I tensor Z)|Omega>=(Zᵀ tensor I)|Omega>, and vectorization is injective; symmetry of M cancels the antisymmetric Pauli products. In the normalized Bell complement (Phi-minus, minus-Psi-plus, Psi-minus), D restricts exactly to

    [[M_xx, M_xz, v_x],
     [M_xz, M_zz, v_z],
     [v_x,  v_z,  tr M]].

The remaining Bell direction is zero. PSD is therefore exactly(4). For compact families the finite active-support argument in section3 supplies the same conclusion.

**Sufficiency.** Given active p satisfying(4), the displayed Z is a feasible dual and annihilates J_identity. Its trace is tr M, so the dual matches4E0. Identity attains it. If E0=0, every w=0 because tr Q≤1; identity is trivially optimal.

Only the five real coordinates(M_xx,M_xz,M_zz,v_x,v_z) matter. Caratheodory therefore allows at most six active laws for this identity certificate; the balanced special case needs at most three. This extends, with variable loss and trace, K2404's earlier fixed-loss/fixed-trace criterion. It is not a new general channel-duality method.

The probe derives the original Bell restriction symbolically, checks its determinant, and tests positive-definite, rank1 and zero-moment boundaries. It also verifies that K2419's identity controller has only its first law active and fails(3) exactly. A nonzero-mean rank1 fixture passes(3), demonstrating that balance is not necessary: axes±e_x with probabilities5/8,3/8 and visibility1/2 realize m=(1/4,0), Q=diag(1/2,0). Thus the criterion classifies identity optimality, while leaving the asymmetric nonidentity optimum unresolved.

## 6. Approximate symmetry and experimental meaning

Use complete flagged instruments, not independent moment errors. For compact families with Hausdorff distance≤delta in half-diamond norm, every fixed CPTP recovery's worst error changes by at most delta, by contractivity and the triangle inequality. Thus their optimal values differ by at most delta, and transporting an optimal controller gives regret≤2delta.

For the special antipodal closure S_sym=S union reflected(S), the bound improves. If every reflected instrument is within delta of S, the symmetric optimum is C=max_S w(3−trQ)/4. Identity has that same exact cost C on S, and E*_S≥C−delta. Hence identity regret is at most delta. This prices approximate symmetry directly. It supplies no measured delta, apparatus budget or experimental verification.

## Verification and remaining work

[Probe](../../tests/channel-swings/k2422_joint_recovery_optimality_probe.py) and [report](../../lab/process/k2422-joint-recovery-optimality.json) use original sign maps, full CP/TP Choi matrices, Bell-block norms, exact support normalization, matching duals and the four-term gap on K2419's actual inputs. Universal minimax/balance/stability claims rest on the written arguments, independently reviewed internally; finite examples are not universal proofs. No external-expert or proof-assistant acceptance is asserted.

For the asymmetric pair, solve the singular matching conditions or obtain a physically justified uncertainty set that supports a different consuming decision. Another rounded matrix alone is a narrower bound, not exact optimality. Keep K2419's numerical bracket and full apparatus/calibration requirements.
