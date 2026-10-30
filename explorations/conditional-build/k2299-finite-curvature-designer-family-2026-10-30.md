---
title: "K2299 Finite high-curvature limit designer family"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied metric background family and algebraic sign conditions only
scripts:
  - tests/channel-swings/k2299_finite_curvature_designer_family_probe.py
---

# K2299 Finite high-curvature limit designer family

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2299 Finite high-curvature limit designer family
carrier: real flat FLRW histories and real scalar metric actions LAYER=toy CHIRALITY=N/A
pairing: real metric contraction and action integral ON=declared_carrier
real_structure: real functions on the closed half-line x>=1
grading: no Clifford identification
action_owner: repository-construction -- supplied metric f(R)
target: complete homogeneous designer equation MAP-TYPE=evaluation
```

## Result and scope

The growing branch in [K2295](k2295-quadratic-expansion-reconstruction-2026-10-30.md) failed a finite high-curvature F limit. Its decaying companion supplies an entire one-parameter family with F>0, f_RR>0 and F tending to alpha. A smaller nonempty interval also has positive algebraic trace mass everywhere. This corrects no prior result: K2295 explicitly excluded only its chosen initial data. It removes a false universal extrapolation and gives a background-consistent candidate for the independent coupled-perturbation test.

The fixed history is E=H²/H_*²=Mx³+Nx⁴+L, x>=1, M>0, N,L>=0, alpha>0. Ordinary conserved sources remain q=3alpha(Mx³+Nx⁴), P=alpha N x⁴. Curvature is R=3Mx³+12L, hence R'=9Mx²>0. All quantities use K2295's dimensionless convention. SC-COS-50/51/54 ASSERTS their connection-distortion demands; these supplied metric functions are a different object. LT-GR2e and ledger0.263 stay unchanged. No empirical, local-gravity, full perturbation or native GU claim follows.

## 1. Reduction of order gives the missing branch

The designer equation for u=F-alpha is

    x²E u''+x(2E+xE'/2)u'-xE'u=0.                         (1)

Let g be K2295's solution g(1)=g'(1)=1. Its proved properties are g,g'>0 at every finite x>=1 and g→infinity. Write p=x²sqrt(E), q0=xE'/sqrt(E)>0. Equation(1) is (pu')'=q0 u, so pg' is strictly increasing. Define

    I(x)=integral_x^infinity dt/[p(t)g(t)²], h(x)=g(x)I(x).

Since p>=sqrt(M)x^(7/2) and g increases,

    0<h(x)<=2/[5sqrt(M)g(x)x^(5/2)]→0.                    (2)

The integral converges, and local differentiation gives W(g,h)=g h'-g'h=-1/p. Differentiating once more verifies (1). It is an independent solution. Furthermore

    I(x)<[1/(p(x)g'(x))] integral_x^infinity g'/g²
        =1/[p(x)g'(x)g(x)],

where the strict inequality follows from strict increase of pg'. Thus h'=g'I-1/(pg)<0. Normalize v=h/h(1): v(1)=1, v>0, v'<0 and v→0. This is a continuum proof, not a numerical endpoint guess.

## 2. Complete finite-limit classification

Every real solution is F=alpha+B g+C h. A finite limit forces B=0, and that limit is necessarily alpha. Therefore write

    F=alpha-A v,
    f_RR=-A v'/(9Mx²).

Strict positivity of f_RR forces A>0. F then increases from alpha-A, giving the necessary and sufficient interval

    0<A<alpha                                             (3)

on the CLOSED domain x>=1. A=alpha has F(1)=0; it is not in this class. A=0 is the Einstein control with f_RR=0. A<0 has the wrong derivative sign. Any B!=0 violates the finite-limit condition.

Use exactly K2295's action reconstruction

    f_rec=RF-6EF+2q+6ExF'.                                 (4)

Its identity f_rec'-FR'=6L_F/x+2[q'-3(q+P)/x], with L_F the full designer equation, proves genuine f_R=F. The 00, spatial and trace equations then all hold. No new independent cosmological constant is freely added to(4). The M=0 radiation case has constant R and cannot use this inversion.

Since -h'<1/(pg), also R f_RR tends to zero as x→infinity: R grows as x³ while p grows at least as x^(7/2), and Rf_RR is bounded by a constant times x/(pg). These asymptotes do not themselves establish local screening or physical recovery.

## 3. An independent uniform algebraic mass condition

Let s=log x, n=xE'/E>0 and w=-v_s=-xv'>0. Equation(1) gives

    w_s=-(1+n/2)w-nv<0.

Consequently w<=w1=-v'(1). Put C0=1/3+4L/(3M). Then

    R f_RR=A[1/3+4L/(3Mx³)]w <= A C0 w1,
    F-R f_RR >= alpha-A(1+C0 w1).

The nonempty interval 0<A<alpha/(1+C0 w1) is necessary and sufficient for strictly positive

    m_alg²=(F/f_RR-R)/3                                   (5)

throughout x>=1: the bound is attained at x=1, so equality has zero mass there and larger A has negative mass there. Equation(5) is an algebraic trace-mass expression, NOT the constrained physical scalar perturbation mass on a rolling background. [K2291](k2291-rolling-scalar-applicability-2026-10-30.md) already demonstrates why those must remain distinct. No matter growth, sound-speed, initial-data or observational acceptance is inferred.

## 4. Exact dust control and contrary branches

For N=L=0, r±=(-5±sqrt(73))/4 and v=x^r−. An explicit reconstructed action is

    F=alpha-A x^r−,
    f=alpha R+AM(3-6r−)x^(r−+3), R=3Mx³.

The identity (3-6r)(r+3)=-9 follows from 2r²+5r-6=0 and proves f_R=F. Here w1=-r− and the mass-positive interval is exactly 0<A<alpha/(1-r−/3): F-Rf_RR=alpha-A(1-r−/3)x^r− reaches its minimum at x=1. Choosing alpha/(1-r−/3)<A<alpha preserves F,f_RR>0 but makes m_alg² negative at the endpoint, a real independent countercontrol.

## Verification and next condition

The probe checks exact ODE/self-adjoint/reduction-of-order identities, reconstruction and dust signs, rational parameter countercontrols and dependence hashes. Analytic integral estimates establish the half-line classification; finite samples are not its proof. The decaying branch now needs the actual coupled matter/metric perturbation and source matching on the same action, with justified initial data. This is standard designer-f(R) methodology; no novelty or external-expert certification is claimed. Background reference: [De Felice and Tsujikawa](https://arxiv.org/abs/1002.4928).
