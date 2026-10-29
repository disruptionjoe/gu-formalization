---
title: "K2268 Finite observations with an explicit regularity price"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied model only; no source or canonical verdict
scripts:
  - tests/channel-swings/k2268_observation_regularity_cosmology_probe.py
---

# K2268 Finite observations with an explicit regularity price

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2268 Finite observations with an explicit regularity price
carrier: positive C3 histories y=H² on a compact redshift interval LAYER=toy CHIRALITY=N/A
pairing: real history integration and positive finite ellipsoid form ON=declared_carrier
real_structure: real histories and real measurement vectors
grading: no native chirality or Clifford grading transported
action_owner: repository-construction -- supplied conditional model
target: conditional finite-data rejection of one fixed vacuum metric family MAP-TYPE=evaluation
```

## Result and scope

A specified finite point observation map, a joint deterministic error ellipsoid, and an independently supplied curvature bound suffice for a rigorous rejection test of the fixed flat vacuum metric family in [K2265](k2265-shared-cosmology-consistency-2026-10-29.md). A direct C1 reconstruction would be extremely expensive. Integrating the weak residual before bounding errors instead makes the derivative error quadratic, giving an explicit nonempty 2001-node example.

This is a conditional mathematical observation experiment, not a survey analysis. The observation is directly y=H² in declared dimensionless units; BAO distances, measured H, and transformed errors are different operators. SC-COS-50/51/54 ASSERTS their source demands; this supplied f(R)=alpha R-bR²/2-rho vacuum model is not the native connection-distortion action. LT-GR2e, ledger0.263 and source polarities remain unchanged. The regularity/error assumptions below are not derived from positive F, from finite data, or from GU.

## 1. Exact observation and reconstruction bounds

On I=[u,v], x=1+z>0, let nodes u=x0<...<xn=v, widths h_i, and data

    d_i=y(x_i)+e_i, e^T Sigma^(-1)e<=q,

with supplied symmetric positive-definite Sigma and q>=0. This is a simultaneous deterministic uncertainty set. Statistical coverage would require an independently justified noise law and choice of q; Sigma need not be called a covariance. Assume separately ||y''||infinity<=L. Let p be the continuous piecewise linear interpolant of d. With c_i the vector selecting node i and Delta_i=c_(i+1)-c_i, set

    eta=max_i sqrt(q Sigma_ii),
    nu_i=sqrt(q Delta_i^T Sigma Delta_i)/h_i.

The ellipsoid support function proves these bounds without independence. In each cell,

    |y-p| <= Lh_i²/8+eta,
    |y'-p'| <= L[(x-x_i)²+(x_(i+1)-x)²]/(2h_i)+nu_i
              <= Lh_i/2+nu_i.                         (1)

The first term is the linear interpolation remainder. For the second, subtract the mean of y' over the cell and integrate |y'(x)-y'(s)|<=L|x-s|. The data-error secant contributes nu_i. p is generally NOT C1; its derivative is used almost everywhere, with one-sided slopes at knots. Both constants are saturated by quadratics at a midpoint or endpoint. Noise is amplified by 1/h in the derivative; oversampling at fixed point error is not always helpful.

A smooth reference y0 with ||y0''||<=L0 and exactly d_i=y0(x_i) gives

    eps0=(L+L0) h_max²/8+eta,
    eps1=(L+L0) h_max/2+max nu_i,
    ||y-y0||infinity<=eps0, ||y'-y0'||infinity<=eps1. (2)

This applies (1) to y and y0; it does not assume their curvatures cancel. A supplied bound on (y-y0)'' could improve it but would be a different assumption. Continuity extends the derivative bound across knots.

The generic weak functional of K2266 can be evaluated on p,p' as integrals, then compared with y using its stated deterministic C0/derivative bound. Do not identify this evaluation with a smooth strong residual of p: p'' contains knot masses. The following direct smooth-reference estimate is stronger for the specified example.

## 2. Weak cancellation improves the actual consuming inequality

For smooth y0,y and g=y-y0, window w with w=w'=0 at u,v, put

    c=x²w, ell=x²w''+6xw'+4w,
    W=integral |w|, C=integral |c|,
    D=integral |(c y0')'|, J=integral |ell|.

Because c vanishes at the endpoints, integration by parts gives EXACTLY

    integral c[(y')²-(y0')²]
      = -2 integral (c y0')' g + integral c(g')². (3)

If both histories have sup norm<=M, the K2266 residual difference satisfies, for |a|<=A,

    |q_w[y]+a A_w[y] - q_w[y0]-a A_w[y0]|
      <= eps0[(45/2)D+9MJ+3AW]+(45/4)C eps1².   (4)

The shared r term cancels in a window combination v with v·B=0. Unlike a generic Lipschitz bound, the derivative uncertainty enters quadratically. This is the useful successor to the naive C1 reconstruction, not merely a different norm label.

On [1,2], y0=1+x³, w_j=x^j(x-1)²(2-x)², j=0,1,2, and

    v=(649,-870,287)/1806,
    v·B=0, v·A[y0]=0, v·q[y0]=205767/24104080>0,
    ||v||1=1.

Use L=L0=12, |a|<=100, M=10. Elementary bounds on t=x-1 in [0,1] are |w0|<=1/16, |w0'|<=1/2, |w0''|<=2. Therefore, for all three windows, W<=1/4, C<=1, J<=153/2, D<=132. For example |w_j'|<=9/4 and |w_j''|<=97/8 imply J; y0'=3x² gives D<=12*8/4+3*16*9/4=132. Equation (4), summed with |v_j|, is bounded by

    9930 eps0+(45/4)eps1².                       (5)

For exactly 2000 uniform cells, d_i=1+x_i³, q=1 and Sigma=10^-16 I, use eta=10^-8 and nu_i<=2eta/h (the exact sqrt2 bound is smaller). Then

    eps0=19/25000000, eps1=151/25000,
    bound=3978609/500000000
         <205767/24104080.                       (6)

All candidate histories satisfy |y|<10 and y>0 because y0 ranges from2 to9 and eps0<1. Thus no positive C3 history obeying these data/error/curvature assumptions can solve the fixed vacuum equation for any |alpha/b|<=100 and any rho/b. Selecting positive F only narrows this already excluded class. The observation set is nonempty: y=y0,e=0 meets it. The arrays of 2001 points are specified by formula; the probe verifies the exact bound, not a synthetic survey or 2001 sampled ODE solves.

This example prices the missing input: 2001 specified y observations, tiny simultaneous error and a global curvature bound. It is not evidence that a current survey supplies any of them. The direct requirement eps1<10^-8 at the same L would need over1.2 billion cells even without noise, whereas the weak-residual consumer does not require that C1 radius.

## 3. Positive domains and what finite data cannot do

For a general data vector, define E0=L h_max²/8+eta and E1=L h_max/2+max nu_i as the bounds on y-p and y'-p' from (1). Then min d_i>E0 certifies y>0, since a linear interpolant lies between its endpoint values. For a fixed b,a, define in each cell

    Fbar(x)=b(a-12p(x)+3x p'(x)).

This is affine; compute its one-sided endpoint minima. A minimum over all cells strictly exceeding |b|(12E0+3x_max E1), with x_max the right endpoint certifies F=b(a-12y+3xy')>0 throughout. For a coefficient box, also minimize the affine dependence on a,b with care about signs; no finite-node positivity shortcut is licensed. Such F positivity is not perturbative stability.

Finite points with a finite curvature bound still cannot certify exact family membership in general: a sufficiently small smooth hidden bump can preserve all nodes and stay within any available regularity slack. K2266's distance-and-node counterconstruction remains intact. Rejection and certification are different tasks. A shared-history forward solution with an actual observation likelihood remains the alternative when regularity cannot be independently justified. No universal bound L follows from the earlier positive-F argument.

## Verification and next question

The companion exact probe checks interpolation saturation, covariance cross terms, noise amplification, derivative-energy identity, window bounds, the nonempty rational rejection and positive-domain controls. Universal interpolation and integral implications are written mathematics with independent internal review; finite controls are not Lean, external-expert, empirical or novelty certification. The next scientific input is a justified observation operator and error/regularity class, or a validated forward ODE comparison; tightening arbitrary toy error digits would not supply it. [K2269](k2269-correlated-cosmology-certificate-2026-10-29.md) independently retains correlations in a finite reconstruction and explicitly prices its remaining nonpolynomial bias.
