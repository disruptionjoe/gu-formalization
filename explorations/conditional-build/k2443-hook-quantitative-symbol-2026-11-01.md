---
title: "K2443 Geometric ordinary inverse and a varying hook symbol"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: "ordinary transverse linear right inverse with fixed analytic radius loss; no mixed nonlinear convergence or native GU solution"
---

# K2443 Geometric ordinary inverse and a varying hook symbol

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
result: K2443
carrier: original161 repeated-polar hooks,105 raw symmetric receivers and seven transverse variables LAYER=toy CHIRALITY=N/A
pairing: ordinary coefficient l1 norm, distinct from the Fischer pairing ON=declared_carrier
real_structure: original real split-metric hook bank over rational coefficients; fixed real embedding of Q(sqrt2), or complex coefficients for norm estimates
grading: homogeneous transverse polynomial degree and105 raw symmetric receiver coordinates
action_owner: repository-construction -- supplied conditional mathematical model
target: degree-sensitive original adjoint splitting, ordinary linear right inverse and actual symbol degeneracy MAP-TYPE=evaluation
```

## Result

The original hook problem has a **polynomial quantitative bound** on its rotation adjoint after its constant-symbol equations hold exactly. If Q is homogeneous of degree k and lies in that exact kernel, then its15 nonuniversal coefficients obey

    sum_(u<v) ||c_uv||_1 <= (7737+3320k) M <=8000(k+1)M,       (1)

where M is the maximum coefficient-l1 norm of the original factor4 rotation residuals. This first controls a restricted actual quotient. The outcome-released construction in section4 then proves a geometric bound for the full ordinary adjoint and an ordinary transverse linear right inverse with a fixed analytic radius loss. It does not estimate the mixed nonlinear recursion. Separately, the repeated symbol drops from generic rank88 to rank at most25 at an actual transverse covector. A constant-rank elliptic shortcut on the punctured cotangent space therefore cannot be assumed.

The [K2435](k2435-fischer-frame-annihilator-2026-11-01.md) all-degree image theorem and [K2437](k2437-augmented-compatibility-adjoint-2026-11-01.md) shared formal solution survive. The quantitative statements close ordinary off-kernel splitting and its normalized-Fischer norm conversion. Mixed elimination, repeated radius losses and the nonlinear majorant remain open. These are conditional hook mathematics, not native stationary GU geometry or evidence about a physical quotient. SC-ACT-01 and SC-GEO-55 remain ASSERTS at their source scopes; SC-META-53 remains UNCERTAIN. Source, ledger0.263 and canon unchanged.

## 1. Exact object and norm

Use the original transverse covectors

    alpha=(e0,9012 e2+8519 e4,e5,e6,e7,e8,e9),
    xi_i=sum_r alpha_r[i]y_r,
    I0={1,3,10,11,12,13}.

The repeated-polar hook Euler symbol is
(A_xi h)_ij=sum_a eta_a xi_a(h_iaj+h_jai), i<=j.
K2435 proves its polynomial adjoint kernel consists exactly of

    Q=tau f+b g+sum_(u<v in I0)c_uv e_uv,                      (2)
    tau_ii=eta_i, b_ij=(2-delta_ij)eta_i eta_j xi_i xi_j.

The coordinates are105 raw symmetric entries. Off-diagonal pairings have the factor2 already carried in b; do not switch to an orthonormal symmetric basis. f,c have degree k, g degree k-2. The norm is sum of absolute ordinary monomial coefficients at unit polydisc radius, **not** factorial-weighted Fischer norm. Since tau and b have no inactive off-diagonal entries, sum||c|| is exactly the coefficient-l1 distance of Q to the polynomial module tau R_k+b R_(k-2). Equation(1) is restricted to (2); it is not a solver for arbitrary prescribed residuals.

## 2. Keep the inhomogeneous original rows

Index inactive partners by r=(0,2,3,4,5,6), u=(1,3,10,11,12,13), active a=(0,5,6,7,8,9). Let delta_u=sum_(v!=u) partial_(r_v)c_uv. The original canonical sorted rotation row, including its factor4, is

    R_(u,s)=A y_s delta_u+B(E_s+lambda)c_(u,u_s),
    E_s=y_s partial_s, lambda=(A+B)/B,                       (3)

for different partners. The anchor is R_(3,2)=-y2 delta_3. The table lists the selected non-anchor rows; its signs are verified against the original tensor bank, not guessed from a permutation convention.

| Rows | A | B | lambda | inverse coefficient bound |
| --- | --- | --- | --- | --- |
| u3,s0 | 1/70 | -27/35 | 53/54 | 70/53 |
| u3,s3 | -1 | 23/70 | -47/23 | 70 |
| u3,s4,5,6 | -71/70 | 3/7 | -41/30 | 70/11 |
| u1,s2,3 | -71/70 | 23/70 | -48/23 | 35 |
| u10,s2 | -1 | 23/70 | -47/23 | 70 |
| u1,s4,5,6 | -36/35 | 3/7 | -7/5 | 35/6 |
| u10,s4,5,6 | -71/70 | 3/7 | -41/30 | 70/11 |
| pairs within11,12,13, smaller u | 0 | 3/7 | 1 | 7/3 |

On a monomial, E_s has eigenvalue n>=0. The inverse bounds are the reciprocals of min_(n>=0)|B(n+lambda)|. Check the nearest nonnegative integer to-lambda and endpoint0; values grow thereafter. Thus no unexamined high-degree small divisor remains in these rows. The smallest shift distance is1/23. This is not an estimate for another operator or for all unselected blocks.

Exact division by y2 preserves coefficient l1 norm **on its image**. From the anchor, ||delta3||<=M. The five components incident to3 are bounded by71M/53,140M,141M/11,141M/11,141M/11; each is<=140M and their sum<=700M.

The u1,s2 and u10,s2 rows then give

    ||delta1|| <= (6790+3220k)M/71,
    ||delta10|| <= (95+46k)M.

Here ||partial2 c||<=k||c||. Divisibility holds because these are residuals of an actual Q in(2); an independently prescribed bank need not satisfy it. Returning to the remaining rows yields

    ||c_1,10|| <= (3430+1610k)M,
    ||c_1,v|| <= (580+273k)M, v=11,12,13,
    ||c_10,v|| <= (620+297k)M, v=11,12,13,
    sum_(11<=u<v<=13)||c_uv|| <=7M.

Adding proves(1). The coefficient inequalities are checked exactly in the probe, together with a nonzero inhomogeneous original polynomial example. All bounds concern the inherited real embedding of Q(sqrt2), or complex coefficients with absolute values. Rescaling the rotation factor4 to d>0 multiplies the residuals by d/4; the conservative constant becomes32000(k+1)/d.

## 3. The actual repeated symbol is not constant rank

At transverse dual-polynomial y=(1,0,...,0), xi=e0. This is a covector evaluation, not an identification of a primal transverse frame vector with an ambient one. For each repeated hook,

    (A_e0 h)_ij=eta0(h_i0j+h_j0i).

All78 off-diagonal rows with i,j!=0 vanish because all three hook indices are distinct. The universal b(e0), as an output annihilator, forces the output's00 entry to vanish; the trace covector supplies another independent restriction. Here Q in(2) is an adjoint covector and is not asserted to have Q00=0. Consequently rank<=105-78-2=25. The probe computes the actual matrix rank at e0 and rechecks the inherited generic rank88. This original rank variation precludes a globally bounded constant-rank pointwise pseudoinverse on the generic88-dimensional image across all nonzero transverse covectors.

Rotations involve derivatives of linear coefficients and repair the **polynomial differential image** in K2435. They do not turn this repeated pointwise symbol into a constant-rank elliptic complex. No claim is made that the full frame system is non-elliptic in every possible reformulation.

## 4. Outcome-released original off-kernel splitting

Let H(Q) be the161-component original constant-symbol adjoint, of degree k+1 for a receiver Q of degree k. Let R(Q) be the original rotation residual bank, degree k. Both use the raw receiver coefficients and coefficient-l1 norm, summed over their components. The proof below concerns residuals of an actual polynomial Q; it is not a surjectivity assertion for arbitrary independent banks H and R.

Remove obvious H-kernel components by

    Qtilde=Q+Q11*tau-sum_(u<v in I0) Q_uv*e_uv.

Here Q11 means entry(1,1), tau11=-1 and b11=0; the inactive off-diagonal entries and entry(1,1) of Qtilde vanish. Put

    b0=b05=beta05*y0*y2, q0=Qtilde05,
    t=b0*Qtilde-b*q0.                                        (4)

The original entries b05,b06,b56 have monomials y0*y2,y0*y3,y2*y3, respectively, with beta coefficients of absolute value2. Thus t has88 possible coordinates, excluding the15 inactive off-diagonal entries,(1,1),(0,5). At y=(1,...,7), H restricted to these88 coordinates is injective: its full kernel is the17-dimensional span of tau,b and the15 dark coordinates, and b05 is nonzero there. Choose88 independent rows, producing a square linear-polynomial matrix M(y) with P=det M nonzero and homogeneous of degree88. The probe selects and records actual original hook rows; no determinant expansion is used. Equation(4) gives

    P*t=adj(M)*b0*(H Q)_selected.                             (5)

Let A>=1 bound each entry's coefficient-l1 norm, and let integer D>=1 clear all coefficients of M. The report records exact A,D from the original bank. Then ||P||1<=88!*A^88 and every nonzero coefficient of P has magnitude at least D^(-88). Define

    W=89^6, B=1+88!*(A*D)^88,
    E_k=2*88!*A^87*D^88 * B^[W*(k+90)+1].                    (6)

Exact polynomial division proves ||t||1<=E_k||HQ||1. Here is the degree-uniform argument, not a numerical extrapolation. Order degree88 monomials lexicographically and weight exponents by(89^6,89^5,...,1). Each replacement of the leading monomial of P by another monomial strictly decreases this positive integer weight, since every exponent is at most88. For a dividend of degree k+90 a reduction path has length at most W(k+90)+1. Division by the leading coefficient costs at most D^88; the sum of branch coefficient magnitudes is bounded by88!*(AD)^88. Summing all path lengths is bounded by B to that depth. This bounds the quotient coefficient-l1 norm by D^88 B^[W(k+90)+1] times the dividend norm. Finally, the matrix coefficient-l1 operator norm of adj(M) is at most88!*A^87 and ||b0||1=2. These give(6). Exact divisibility is essential; a general remainder is not silently discarded.

Recover a representative without dividing by the possibly vanishing determinant. Divide q0=b0*g+r monomial by monomial, leaving r supported on monomials lacking y0 or y2. Define

    rA= -[(t56/y2)|_(y0=0)]/(beta56*y3),
    rB= -[(t06/y0)|_(y2=0)]/(beta06*y3),
    r=rA+rB-rB|_(y0=0),
    Q'=(t+b*r)/b0.                                          (7)

All divisions in(7) are exact monomial divisions on this image. Substituting(4) proves rA=r|_(y0=0), rB=r|_(y2=0); the last expression equals Qtilde-b*g and is polynomial. Its two remainder supports are disjoint. Therefore

    ||r||1 <= (||t56||1+||t06||1)/2 <= ||t||1/2,
    ||Q'||1 <= F*||t||1, F=1/2+||b||1/4,
    H(Q-Q')=0.                                             (8)

The probe checks the original88-coordinate minor, beta coefficients, monomial recovery, residual preservation and(8) on a nonzero original Q containing each remainder sector and a divisible sector. These are concrete implementation checks accompanying the universal algebraic proof.

Apply(1) to Q-Q'. For a fixed original-bank constant G, ||R(Q')||1<=G(k+1)||Q'||1; summing all absolute generator coefficients gives a conservative G recorded by the probe. Since max residual norm is at most summed residual norm,

    dist_1(Q, tau*R_k+b*R_(k-2))
      <= F*E_k ||HQ||1
       +8000(k+1)[||RQ||1+G(k+1)F*E_k||HQ||1].              (9)

The right side is at most C^(k+1)(||HQ||1+||RQ||1) for one fixed finite C>=1, enlarged to absorb polynomial factors. This is the **full ordinary-adjoint quotient estimate**, despite the varying pointwise rank. Its huge constant is an existence bound, not an efficient numerical solver or a claim of a bounded pointwise pseudoinverse.

### Normalized Fischer passage and ordinary analytic scope

On degree k polynomials use squared Hilbert norm sum_alpha |q_alpha|^2 alpha!/k!. In seven variables the weights lie in[7^(-k),1], by the multinomial theorem. With finitely many receiver/generator coordinates, coefficient-l1 and this norm differ by at most an exponential factor times the square root of the degree-k monomial count. The latter is polynomial in k and can also be absorbed in a fixed exponential. Distances to the same kernel inherit these comparisons.

The degree-changing adjoint must be scaled: under these normalized pairings, the adjoint of a derivative from degree k+1 to degree k is **(k+1) times multiplication**, while degree-preserving rotation adjoints remain R. Thus the actual ordinary primal block has adjoint((k+1)H,R), not(H,R). Equation(9) still gives a geometric lower singular-value bound on the orthogonal complement of its kernel, since ||HQ||<=||(k+1)HQ||. Finite-dimensional Hilbert duality and K2435's exact image theorem give a degree-wise ordinary transverse right inverse on the compatible range with norm at most C0^(k+1). We may set unused Koszul input coefficients to zero; repeated hooks and rotations already establish the kernel used here.

Consequently analytic **linear ordinary transverse** forcing satisfying the K2435 compatibility conditions admits an analytic ordinary preimage on a fixed smaller polydisc: exponential coefficient bounds absorb C0^(k+1) by reducing the radius. The one-degree shift of constant-generator inputs changes only a fixed radius factor. This says nothing about uniform estimates as passive ambient parameters vary, solving the augmented mixed equations, or repeated nonlinear inversion on successively smaller domains. A formal nonlinear solution does not become convergent just because one ordinary linear block has a fixed-loss inverse.

## 5. Analytic control: triangular does not mean convergent

The comparison L=1-x partial_y has identity on every homogeneous diagonal block ordered by x-degree, yet

    L_n^(-1)y^n=sum_(j=0)^n n!/(n-j)! x^j y^(n-j).

Thus inverse coefficient norm is at least n!. The analytic forcing1/(1-y) produces a unique divergent formal solution, since its coefficient of x^n is n!. This is a counterexample to a proposed inference from triangular surjectivity, **not** a divergence result for the hook model. A fixed invertible linear coordinate change only gives exponential norm factors and cannot cure this factorial example.

The positive comparison L_lambda=x partial_x+lambda-x partial_y, lambda>0, has coefficients n!/[(n-j)! product_(h=0)^j(h+lambda)]. At lambda=1 they are binomial(n,j)/(j+1), bounded geometrically. The difference is the retained directional-degree denominators, not a finite rank test. The probe verifies both exact recurrences and the original rotation small-divisor bounds.

The scalar augmented inverse of K2437 can already use one fixed adapted shear; that was noted in the prior review and is not counted as new. Equations(4)--(9) now remove the ordinary off-kernel obstruction with a geometric bound. The mixed ordinary/augmented elimination and repeated radius losses can still incur growth. A full nonlinear theorem requires compatible mixed estimates and a majorant or another convergence argument; formal Borel realization alone gives flat residuals, not exact solutions.

[Probe](../../tests/channel-swings/k2443_hook_quantitative_symbol_probe.py), [report](../../lab/process/k2443-hook-quantitative-symbol.json). Original tensor reconstruction, rational row extraction, exact ranks and contrary recurrences supplement the universal proof. No finite degree sample establishes convergence. Independent internal review is not external or proof-assistant certification.
