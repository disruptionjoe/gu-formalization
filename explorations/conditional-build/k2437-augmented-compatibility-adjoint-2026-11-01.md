---
title: "K2437 A shared formal Gram, sigma and Euler solution"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: formal solution in the conditional original hook model; no convergence, smooth stationary solution, physical quotient or source-native GU identification
---

# K2437 A shared formal Gram, sigma and Euler solution

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
result: K2437
carrier: original fourteen-dimensional hook model and its seven transverse plus seven boundary variables LAYER=toy CHIRALITY=N/A
pairing: original split Gram, four-form sigma and algebraic monomial Fischer pairing ON=declared_carrier
real_structure: characteristic-zero Q(sqrt2), inherited real split metric
grading: homogeneous derivative order; symmetric derivative jets versus polynomial coefficients
action_owner: repository-construction -- conditional curved hook Euler model
target: one coherent formal series satisfying original algebraic and Euler equations MAP-TYPE=evaluation
```

## Result

There is **one coherent formal series** in the original conditional hook model satisfying every Gram, sigma and Euler coefficient, with the fixed repaired cubic and K2423 boundary quartic. This strengthens [K2433](k2433-lower-quartic-compatibility-2026-11-01.md)'s formal algebraic series with Euler through eight. It is a formal existence theorem over Q(sqrt2), not a convergent or smooth solution.

The missing augmented scalar compatibility map has an exceptionally small exact certificate: one original repeated-polar hook h is invisible to all seven transverse Euler symbols, while its scalar compatibility operator is the nonzero constant directional derivative

    Jstar(h f) = (2253/2) partial_1 f + (2253/17038) partial_2 f.       (1)

This supplies arbitrary scalar compatibility while preserving transverse Euler. Together with [K2435](k2435-fischer-frame-annihilator-2026-11-01.md)'s all-degree ordinary image theorem, it removes every further augmented rank-bank obligation. The released successor is the same-coefficient induction in section5; scalar image completeness alone would not prove it.

This is GU-independent conditional mathematics. SC-ACT-01 ASSERTS its distinct first bosonic action and SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita; neither identifies this hook model with that action. SC-META-53 remains UNCERTAIN, SC-META-56 DISAVOWS an odd-action prerequisite. Source polarities, ledger0.263 and canon are unchanged. No novelty, external-expert or proof-assistant certification is claimed.

## 1. Original augmented operator and exact adjoint

Keep H(0)=0, the original first jet K, background metric and connection fixed. For a homogeneous top-jet variation V of degree d>=4 with lower jets fixed, differentiation of the **full** curved scalar compatibility identity gives

    J_d(V) = -(1/d) sum eta_p eta_i eta_j eta_k R_pijk partial_i V_pkj
      -(4/d) sum eta_i eta_j F(partial_i V,K_j)_ij
      -(2/d) sum eta_i eta_j F(K(x),partial_i partial_j V)_ij
           = (4/d) Jstar(V).                                     (2)

F is the original symmetric polarization of the quadratic Euler term. The earlier d=4,5,6 checks are retained by dependency, but the uniform identity follows from Leibniz extraction: curvature times the top first derivative contributes factor1/d; the two differentiated quadratic-gradient factors contribute4/d; the external K positions in H times its second derivative contribute2/d after the d(d-1) polynomial differentiation factor. Since H(0)=0, no higher jet survives. Derivatives of curvature or connection and all other Leibniz partitions involve only jets through d-1. Covariant commutators lower differential order and therefore change only affine forcing. Changed frame jets do not change this fixed K coefficient bank.

Write the transverse version on a constant hook as

    Jstar(h f)=sum_r a_r(h) partial_r f
       +sum_rst b_rst(h)y_t partial_r partial_s f.

The algebraic Fischer pairing has monomial weights alpha!, with no integration-by-parts sign. For symmetric receiver Q and scalar receiver p the augmented adjoint on a constant hook is

    U_h(Q,p)=sum_r y_r <A_r h,Q> +sum_r a_r(h)y_r p
             +sum_rst b_rst(h)y_r y_s partial_t p.                (3)

For an original linear generator sum_t y_t h_t, the equation is sum_t partial_t U_(h_t)=0. The order in (3) matters: the adjoint of y_t partial_r partial_s is y_r y_s partial_t, not partial_t(y_r y_s p). The probe checks original coefficient pairings and rejects both that reversal and omission of the outer derivative.

## 2. The exact small witness

Use the original ordered repeated-polar basis rep of K2425. Set

    h=rep[32]+(9012/8519)rep[55].                                  (4)

The report serializes every nonzero original hook coordinate, so the witness is not specified only by list positions. Direct original contractions establish:

- h is a nonzero repeated hook and G(K_i,h)=0 for all original i;
- A_r h=0 for all seven transverse symbols;
- a(h)=(0,2253/2,2253/17038,0,0,0,0);
- every one of the343 original b_rst(h) coefficients is zero.

No reduced fitted operator, modular affine lift or finite-degree rank inference occurs. The exploratory common-symbol kernel had dimension22; only the explicit witness and its identities are needed for the theorem.

Put a=2253/2, b=2253/17038. For a homogeneous scalar polynomial p define I_1 as integration in y1 with zero constant term. The finite operator

    S p = sum_(j>=0) [(-b)^j/a^(j+1)] I_1^(j+1) partial_2^j p       (5)

terminates at the y2 degree of p and satisfies (a partial_1+b partial_2)S p=p by telescoping. It increases homogeneous degree by one and is divisible by y1. Equivalently use u=y1, v=y2-y1/8519 and integrate in u at fixed v. Only nonzero rational constants and positive integers are divided; there is no coordinate localization or resonance.

Therefore h S p is repeated, K-polar, zero on W, and belongs to ker D_E, with Jstar(h S p)=p. This proves scalar surjectivity **inside** the ordinary transverse Euler kernel at every degree. For any ordinary admissible receiver first solve T_k by K2435, then apply (5) to the remaining scalar error. Consequently

    rank(T_k,Jstar_k)=105 binom(k+6,6)-binom(k+4,6),                (6)

with the final term zero when k<2. Equivalently (3) forces p=0, and K2435 leaves Q=tau f+b_quadratic g. The explicit primitive is stronger than merely counting the annihilator.

## 3. Ambient transfer retains mixed derivatives

Equation (1) is a **transverse** Euler-kernel statement. Multiplying by W monomials generally creates D_W terms; a direct ambient-kernel claim would be false. The probe includes a mixed fixture where these terms are nonzero.

For a degree-d correction, multiply each transverse block k by W monomials of degree d-1-k. D_E reaches leading E-degree k. D_W raises that degree. In Jstar, K(x) has one E degree, so EE terms reach k, EW terms reach k+1, WW terms reach k+2. The full finite system is block triangular with the complete diagonal images (6). Solve successive E degrees while retaining the mixed terms. This gives

    sum_(k=0)^(d-1) binom(d+5-k,6) rank(T_k,Jstar_k)
      =105 binom(d+12,13)-binom(d+10,13).                          (7)

The right side is the entire ordinary trace/double-divergence compatible Euler image plus **all** degree-(d-1) scalar receivers. The original mixed fixture independently checks its leading scalar coefficient and the strictly higher E degree of the remaining terms. Replacing the rotation factor4 by d and the scalar row by4/d rescales nonzero columns/rows without changing this image. No mixed block is set to zero in the theorem.

## 4. Preserve the actual algebraic family

The allowed first change at order d is R+d rho(C_(d-1))K, with R repeated, G(K,R)=0 and R|W=0. It is realized by changing the repeated inner coefficient and inserting an orthogonal frame factor whose first field effect is at order d. Earlier jets are untouched. The polar condition preserves full Gram through order d+1, and the zero inner W value preserves the next W boundary. All inner coefficients remain repeated, so sigma stays identically zero in the orthogonal frame.

K2433's common totally null section D, with independent actual K/q contractions and all fourteen t/r pairings in the original quadratic ideal, is crucial here. Its ambient normal-ideal division can reconstruct the next coefficient from the **actual corrected lower jets**, preserving previously selected inner boundaries. It is not permissible to restore the old lower forcing after an Euler correction or to combine separately chosen algebraic and differential jets.

## 5. Executed successor: one nested formal solution

Start from the actual shared quartic furnished by K2425 and used in K2433: Euler through fourth order, fifth compatibility from the cubic, sixth compatibility selected on the quartic, full Gram through fifth and the sixth W boundary. Keep its repaired cubic and inner W4 unchanged.

For d>=5 maintain these invariants at the start of stage d:

1. One set of lower coefficients through d-1 and one orthogonal frame.
2. Gram through order d and F_(d+1)|W=0.
3. Euler through d-1, and compatibility for Euler d and d+1 already imposed.

K2433 constructs repeated R_d from the actual lower coefficients: derive its K targets, use the common section and homogeneous ideal lift to select its W boundary, then divide the residual normal ideal. This supplies full Gram through d+1 and F_(d+2)|W=0.

The trace of the remaining Euler forcing obeys the established Gram constraint; Ric_tf and the linear hook Euler term have the required trace identities. Its double-divergence compatibility was imposed at stage d-2 (the listed base handles d=5,6). Thus the forcing lies in K2435's ordinary image. Apply the full **augmented** ambient image (7) to solve Euler d and simultaneously set compatibility for Euler d+2 to zero. By section4 this preserves all prior coefficients, the full Gram order and the chosen inner W_d boundary. Compatibility for d+1 depends on the fixed jet d-1 and is unchanged.

This restores exactly the induction invariants for d+1. Recompute future K targets after each correction. The resulting jets are nested: every finite coefficient is eventually fixed and never revised. Their inverse-limit formal series satisfies every original Euler, Gram and sigma coefficient. This is not a conclusion from an infinite sequence of unrelated existential jets. The frame, boundary and all lower choices are shared throughout.

## 6. Analytical frontier and verification

The newly available scalar inverse also has a quantitative analytic bound. Put c=b/a=1/8519. Its integral form is

    S p(y)=(y1/a) integral_0^1 p(s y1,y2+c(s-1)y1,y_other) ds.     (8)

For a holomorphic p on the larger polydisc, supremum norms obey

    ||S p||_(r1,r2,...) <= (r1/a)||p||_(r1,r2+c r1,...).           (9)

The path stays inside that larger polydisc; differentiating at fixed v=y2-c y1 proves the same right-inverse identity. For homogeneous degree k at unit coefficient l1 norm, the finite sum in(5) gives

    ||S p||_coeff,1 <= (1+c)^k ||p||_coeff,1/a.                   (10)

For a monomial y1^u y2^v this follows by integrating s^u[1+c(1-s)]^v over[0,1]; the triangle inequality covers arbitrary coefficients. The pure y2^k column has exact coefficient norm[(1+c)^(k+1)-1]/[a c(k+1)], checked independently through k=64. That exact expression tends to infinity as k grows because c>0; this formula, rather than the finite checks, proves that a same-radius degree-independent coefficient bound is false, but the scalar inverse has at most geometric growth and a controlled domain loss. The factor d/4 needed for J_d adds only polynomial growth. This is a quantitative result for the scalar subproblem, not for the combined recursion.

The primitive (5) is polynomial and finite at every degree. It alone does **not** bound the growth of the full ordinary image solver, E/W elimination, nonlinear forcing, common-section lifts and successive frame products. No convergence radius, analytic solution, globally smooth solution, ellipticity, physical domain, positive quotient or native GU bridge follows. A formal Taylor series can be realized by a smooth germ with a residual flat at the base point; flatness is not vanishing on a neighborhood, so that shortcut does not close the PDE.

The substantive next mathematical problem is a quantitative compatible right inverse and majorant estimate on the entire recursion, or a precise analytic obstruction. Another finite Gram/Euler order is now dominated. The independent native matter/light challenge still needs the actual source/readout/domain packet; this conditional result does not provide it.

[Probe](../../tests/channel-swings/k2437_augmented_compatibility_adjoint_probe.py) and [report](../../lab/process/k2437-augmented-compatibility-adjoint.json) reconstruct original tensors, the small witness, all original derivative coefficients, exact primitives and mixed-coordinate controls. Written equations(2)--(7) and the nested induction supply the universal proof; finite fixtures are not substitutes for it. Dependencies pin the inherited K2433 and K2435 premises. Independent internal review specifically challenged the normalization, transverse-to-ambient transfer, fixed lower-jet quantifiers and formal-versus-convergent ceiling.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 sage -python tests/channel-swings/k2437_augmented_compatibility_adjoint_probe.py --check
```
