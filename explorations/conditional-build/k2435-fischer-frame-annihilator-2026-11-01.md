---
title: "K2435 All-degree original frame Euler image"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: ordinary all-degree image only; no augmented compatibility, all-order stationary solution, convergence or native GU identification
---

# K2435 All-degree original frame Euler image

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
result: K2435
carrier: original fourteen-dimensional hook model and seven transverse polynomial variables LAYER=toy CHIRALITY=N/A
pairing: algebraic monomial Fischer pairing and raw symmetric receiver coordinates ON=declared_carrier
real_structure: rational original symbol, characteristic zero; inherited real split metric
grading: homogeneous transverse polynomial degree; coefficient transpose distinct from differential formal adjoint
action_owner: repository-construction -- conditional hook Euler model
target: ordinary frame-preserving Euler image in every degree MAP-TYPE=evaluation
```

## Result

The ordinary original transverse maps T_k from [K2425](k2425-frame-euler-module-2026-11-01.md) attain their trace/double-divergence upper bound **for every k>=0**:

    rank T_k = 104 binom(k+6,6) - binom(k+4,6),

with the last term zero for k<2. This is a structural proof on the original coefficients, not extrapolation from the certificates through T7. It removes the need for further ordinary frame-image rank banks. It does **not** prove the augmented Euler/curved-compatibility image, so [K2433](k2433-lower-quartic-compatibility-2026-11-01.md)'s same formal Gram/sigma family still has only its proved Euler-through-eight companion.

The argument first derives the exact Fischer annihilator, then uses one rank88 rational matrix plus primitive polynomial saturation to reduce it to fifteen scalar polynomials. Exact first-order rotation equations eliminate those polynomials at every degree. The differentiation of linear generators is essential. An independently proposed simplified rotation formula omitted a zeroth-order term; the original bank rejected it, and the corrected coefficients below are the accepted proof.

The result concerns a conditional repository hook model, not the native action named by SC-ACT-01 ASSERTS or the gauge-rotated Levi-Civita displacement in SC-GEO-55 ASSERTS. SC-META-53 remains UNCERTAIN and SC-META-56 DISAVOWS requiring an odd action for the graded claim. Ledger0.263, source polarities and canon are unchanged. No novelty, external-expert or proof-assistant certification is claimed.

## 1. Exact adjoint, including the linear coefficients

Work over R=Q[y0,...,y6]. On monomials use <y^a,y^b>=a! delta_ab, and use the ordinary dot pairing on the105 raw symmetric receiver coordinates i<=j. This is an algebraic Fischer pairing; it is not integration by parts and includes no minus sign. Define

    A_r h = symbol(h,alpha_r),
    (symbol(h,alpha))_ij = sum_a eta_a alpha_a (h_iaj+h_jai),
    H_Q(h) = sum_r y_r <A_r h,Q>.

For homogeneous receiver Q of degree k, annihilation of the image is equivalent to:

    H_Q(h)=0                 for all161 constant repeated-polar h;
    partial_b H_Q(J_a)-partial_a H_Q(J_b)=0   for all21 Koszul pairs;
    sum_t partial_t H_Q(4 rho_ab KE_t)=0     for all91 rotations.      (1)

Here the original linear generators are y_b J_a-y_a J_b and sum_t y_t 4rho_ab KE_t. Multiplication and differentiation are Fischer adjoints. Applying that rule twice proves (1) and explains the derivative on the y factor inside H_Q. The probe verifies every original constant and linear generator against independent primal differentiation with mixed repeated monomials and factorial weights.

For a general bank the Koszul equations say q_a=H_Q(J_a) is closed. Homogeneity gives the explicit potential Phi=sum_a y_a q_a/(k+2), with q_a=partial_a Phi. On this particular original bank, the stronger reduction below proves q=0; no unsolved potential freedom remains.

## 2. The entire polynomial constant-symbol kernel

Let xi_i=sum_r alpha_r[i] y_r. In the original bank

    alpha = [e0, 9012 e2+8519 e4, e5,e6,e7,e8,e9],
    I0 = {1,3,10,11,12,13}.

All xi on I0 vanish. Define universal covectors

    tau_ii=eta_i, tau_ij=0 for i<j,
    b_ij=(2-delta_ij) eta_i eta_j xi_i xi_j.

The factor2 off diagonal is required by the raw symmetric dot pairing. Trace and double divergence annihilate the hook Euler operator. Direct original coefficient identities verify H_tau=H_b=0, and verify their products by arbitrary polynomials for every linear generator.

For a repeated hook, each off-diagonal output is supported on xi_i or xi_j. Hence the fifteen e_uv with u<v in I0 also annihilate every repeated symbol, including the Gram duals J_a. The seventeen covectors tau,b,e_uv are independent over Q(y). An exact rational evaluation at y=(1,2,3,4,5,6,7) gives rank88 for the105-by161 constant symbol matrix. Therefore its rank over Q(y) is exactly88 and these seventeen covectors exhaust its rational kernel.

There are no hidden polynomial denominators. Write a polynomial solution as

    Q=tau f+b g+sum_(u<v in I0) c_uv e_uv                 (2)

over Q(y). The active off-diagonal b entries05,06,56 are nonzero constant multiples of y0*y2, y0*y3, y2*y3; their gcd is1. Since the corresponding Q entries are polynomials, a reduced denominator of g divides all three and is a unit. Thus g is polynomial. The inactive diagonal Q11=-f makes f polynomial, and the remaining c_uv are then polynomial. This proves a free polynomial kernel, not merely a generic pointwise statement. Homogeneous Q has f,c of degree k and g of degree k-2; g=0 for k<2.

Every term in (2) annihilates the entire repeated symbol, so all Koszul equations vanish automatically. The rotations alone must remove the fifteen c_uv.

## 3. Exact degree-uniform elimination of the fifteen components

Index the inactive/active partners as

    r = [0,2,3,4,5,6],
    u_r = [1,3,10,11,12,13],
    a_r = [0,5,6,7,8,9],
    delta_u = sum_(v != u) partial_(r_v) c_uv.

The report contains the complete original rotation coefficient bank and all36 equations from rotations(a_s,u). With the canonical ordered rotation sign, they have the exact form

    A y_s delta_u + (A+B)c_(u,u_s) + B y_s partial_s c_(u,u_s)=0, (3)

when s!=r_u, and A y_s delta_u=0 otherwise. Equivalently they are
A sum_(v!=u) partial_(r_v)(y_s c_uv)+B partial_s(y_s c_(u,u_s)).
The extra A*c term in (3) must not be dropped.

First take u=3,s=2. Its A=-1, so y2 delta_3=0 and delta_3=0 in the polynomial ring. For u=3 and the other s, B is nonzero and (3) reduces to

    B(E_s+lambda)c_(3,u_s)=0, E_s=y_s partial_s,
    lambda=(A+B)/B.

The exact shifts are53/54 for s=0, -47/23 for s=3, and -41/30 for s=4,5,6. None is a nonpositive integer. On each monomial E_s has a nonnegative integer eigenvalue, so all five entries incident to3 vanish.

Next use s=2 for every u!=3. The c_(u,3) term is zero. The respective A values are -71/70 for u=1, -1 for u=10, and1/70 for u=11,12,13. Each is nonzero, so every delta_u=0.

Finally (3) eliminates the remaining pairs. One may choose:

| Pairs | Row choice | Shift lambda |
| --- | --- | --- |
| (1,10) | u=1,s=3 | -48/23 |
| (1,v), v=11,12,13 | u=1,s=r_v | -7/5 |
| (10,v), v=11,12,13 | u=10,s=r_v | -41/30 |
| pairs within11,12,13 | smaller u, s=r_larger | 1 |

Again no shift is a nonpositive integer. Thus every c_uv is zero at **every degree**. This uses integral-domain cancellation of y_s delta_u=0 and division by nonzero rational constants only; it does not invert coordinates in the constructed field or assume positivity of the split Gram form.

An independent reviewer also found a different elimination using special y1 rotations and positive diagonal sums. The accepted probe checks the full original coefficients of (3); it does not rely on the earlier erroneous simplified formula or on the alternative route.

## 4. Image theorem and ambient consequence

Equations (1) now have exactly

    annihilator(T_k)=tau R_k direct_sum b R_(k-2).

Counting dimensions proves the stated rank. This proves ordinary surjectivity onto the trace/double-divergence-compatible image; it is not ordinary surjectivity onto every symmetric tensor.

For an ambient homogeneous correction of order m>=1, the E/W filtration from K2425 multiplies T_k by W monomials of degree m-1-k. The diagonal blocks have the proven images; W derivatives enter higher E-degree blocks. The finite triangular minor in each degree gives

    sum_(k=0)^(m-1) binom(m+5-k,6) rank T_k
      =104 binom(m+12,13)-binom(m+10,13),               (4)

with the last term zero when m<3. The right side is the full ambient Euler upper bound. Hence repeated-polar/W-zero plus frame corrections span the entire ordinary Euler image in every order. Replacing the nonzero rotation factor4 by the actual order m rescales generator columns and leaves the span unchanged.

**What this does not do:** a curved affine Euler forcing must first lie in that image. Its double-divergence compatibility depends on earlier jets. The augmented scalar compatibility operators in K2425/K2427/K2429 are not in (1), and their all-degree surjectivity is not proved by (4). No new ninth-Euler shared jet, all-order stationary field or convergence follows. The next substantive geometry problem is the augmented compatibility operator on the same coherent K2433 algebraic family, rather than another ordinary rank computation.

## 5. A delayed-resonance contrary construction

Finite rank saturation alone remains invalid in this architecture. For any positive integer N, take D=div in two variables and the linear generator L=(x,-(N+1)y). Then

    D(Lf)=(x partial_x-(N+1)y partial_y-N)f.

On a monomial x^(k-b)y^b its eigenvalue is k-N-(N+2)b. Every degree k<N is invertible, yet x^N enters the kernel/cokernel at degree N. The probe uses N=11. This is a counterexample to extrapolation, not a counterexample to the original hook map, whose exact shifts have now been checked.

## Verification

[Probe](../../tests/channel-swings/k2435_fischer_frame_annihilator_probe.py) and [report](../../lab/process/k2435-fischer-frame-annihilator.json) reconstruct original tensors and generators, verify Fischer pairing and universal operators, certify exact rank88, test all36 rotation identities and all30 nonresonant shifts, and exercise incorrect off-diagonal weights, omitted derivatives and a delayed resonance. The universal theorem is the written algebraic argument above; finite degree convolution checks are reporting controls, not its proof. Dependency pins protect reused predecessor evidence. No expensive T0--T7 rank banks are replayed.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 sage -python tests/channel-swings/k2435_fischer_frame_annihilator_probe.py --check
```
