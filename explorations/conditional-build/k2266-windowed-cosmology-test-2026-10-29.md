---
title: "K2266 Weak windows and the finite-data boundary"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied model only; no source or canonical verdict
scripts:
  - tests/channel-swings/k2266_windowed_cosmology_test_probe.py
---

# K2266 Weak windows and the finite-data boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2266 Weak windows and the finite-data boundary
carrier: real positive expansion histories on one compact interval with a shared action LAYER=toy CHIRALITY=N/A
pairing: real scalar integration and metric contraction ON=declared_carrier
real_structure: real scalar histories and real metric coefficients
grading: no native chirality or Clifford grading transported
action_owner: repository-construction -- supplied conditional model
target: window residuals, joint profiling and finite-node nonidentifiability MAP-TYPE=evaluation
```

## Result and scope

[K2265](k2265-shared-cosmology-consistency-2026-10-29.md) gives a full-equation global consistency test. Here it is carried into weak windows, an explicit shared-domain forward interface and a finite-data counterconstruction. The weak form removes y'' but retains (y')². Thus it reduces derivative demands without turning published distance nodes into sufficient inputs. A finite collection of mathematical windows supplies necessary conditions; all compactly supported windows recover the continuum equation.

The same fixed flat vacuum metric f(R) family and standard redshift/optics assumptions apply. SC-COS-50/51/54 ASSERTS their source demands; no bridge identifying this conditional metric action with the native connection-distortion theory is claimed. LT-GR2e/ledger0.263, source polarities and existing cosmology ceilings remain unchanged. Survey redshift windows are not automatically the test functions below.

## 1. Exact weak identity and endpoints

Write x=1+z, y=H², a=alpha/b,r=rho/b and Q as in K2265. On I=[u,v] with 0<u<v, take a C2 window w with w=w'=0 at both endpoints. Twice integrating by parts gives

    q_w[y]=integral_I [(45/4) w x²(y')²
             -(9/2)(x²w''+6xw'+4w)y²] dx,
    A_w=3 integral_I wy dx, B_w=-(1/2) integral_I w dx,
    q_w+A_w a+B_w r=0.                            (1)

For unrestricted endpoints add

    [-9wx²yy'+(9/2)(x²w'+4xw)y²]_u^v

to q_w. Dropping this boundary term for a top-hat window is invalid. With only w=0 at the endpoints, the once-integrated version is

    integral_I [9x²w'yy'+36xwyy'+(45/4)wx²(y')²
                +3awy-rw/2] dx=0.

These identities hold for smooth histories; validity for every compactly supported smooth w is equivalent to the strong constraint by the fundamental lemma. For a fixed finite window bank, they are only necessary conditions. The nonlinear derivative square cannot in general be reconstructed from means of y or from finitely many y samples.

## 2. One joint coefficient fit, exact residual and deterministic error

For windows w_j put X_j=(A_j,B_j) and q_j=q_wj. Exact compatibility requires rank[X|-q]=rank X. If X has full column rank, any fixed positive-definite weight W gives

    theta_hat=-(X^T W X)^(-1)X^T W q,
    residual=q+X theta_hat,
    minimum= residual^T W residual.               (2)

Use a weighted pseudoinverse for rank deficiency; a zero minimum does not by itself give the positive-F condition. W is an explicitly supplied numerical weighting. It is NOT automatically an inverse survey covariance: both X and q depend nonlinearly on the same uncertain reconstructed history. Treating X as exact and claiming chi-square degrees of freedom would be unjustified without an observation/noise model.

An exact finite-bank countercontrol uses y=x on [1,2], w=(x-1)²(2-x)². For the fixed pure-R² member b=-1,a=r=0, F=9x>0 but q=54/35>0, so this history fails. In contrast b=1,a=30,r=2538/7 yields one-window residual zero and F=30-9x>0 throughout, although its pointwise residual is not zero. Thus even positivity plus one weak pass is not a solution. Multiple windows can expose this failure with the same constants. For the shape y=1+x³, three windows w,xw,x²w give an exact augmented-rank obstruction, without per-window refitting.

For reproducible reconstruction errors let y,yt be C1 with sup norms <=M, derivatives <=V, ||y-yt||∞<=epsilon0 and ||y'-yt'||∞<=epsilon1. Set L_w=x²w''+6xw'+4w. Then

    |q_w[y]-q_w[yt]| <= (45/2)V epsilon1 integral |w|x²
                          +9M epsilon0 integral |L_w|,
    |A_w[y]-A_w[yt]| <=3 epsilon0 integral |w|.   (3)

These follow from |p²-q²|<=2 bound·|p-q|. B_w is exact when the window is. A fixed-(a,r) residual uncertainty adds |a| times the second bound; free unbounded a prevents replacing this by one uniform numerical tolerance. On a declared compact coefficient set, interval propagation gives rigorous rejection if every allowed pair misses the error boxes. No derivative-free tolerance or measured error covariance is invented.

### A finite robust exclusion, beyond a formal identity

In the declared dimensionless normalization take y0=1+x³ on [1,2], the three windows w,xw,x²w above, and restrict |a|<=100 while leaving r unrestricted. The unit-l1 left-null vector of X[y0] is

    u=(649/1806,-145/301,41/258),
    |u dot q[y0]|=205767/24104080.

For any C3 positive y with ||y-y0||∞<=epsilon and ||y'-y0'||∞<=epsilon, epsilon<=1, use M=10,V=13 in (3). Bounding each integral |L_w| by the absolute polynomial coefficient sum integrated on [1,2] gives

    |u dot (q[y]+a A[y]) - u dot q[y0]|
       <= (2589985595/7224) epsilon.

The r term cancels exactly for all r because the B column depends only on the windows. At epsilon=10^-8 the bound is strictly smaller than the nonzero margin. Therefore NO history in that C1 ball can satisfy the full vacuum equation with |a|<=100, regardless of r, b!=0 or additional positive-F selection. This is a rigorous bounded-parameter neighborhood exclusion, not merely an exact polynomial mismatch. The threshold margin/bound coefficient is about2.381e-8; the chosen smaller rational radius is verified without floating point.

The normalization, parameter bound and C1 error radius are declared hypotheses. They are not inferred observational errors or a universal exclusion for unbounded a. Converting this useful mathematical discriminator into data requires the actual history reconstruction and justified norm bounds.

## 3. A shared-domain forward model, not independent node fits

The strong constraint is the second-order ODE

    y'=v,
    v'=2v/x+v²/(4y)+a/(3x²)-r/(18x²y),
    chi'=1/sqrt(y).                              (4)

Choose ONE (a,r), ONE initial (y0,v0), one integration origin/chi0 and one constant ruler across the interval. In units c=1, D_H/r_d=1/(r_d sqrt y), and flat D_M/r_d=chi/r_d with chi(1)=0 when integrating from today. If only a subinterval is solved, its chi offset is a shared boundary nuisance, not a separately adjustable value at every point. Feed the resulting history into the actual observation operator and correlated likelihood, including their tracer/template/perturbation assumptions; (4) does not supply that operator.

The RHS is locally smooth only for x>0,y>0. Enforce y>0 and F=b(a-12y+3xv)>0 on the ENTIRE chosen interval. Numerical integration success is not certification. A rigorous implementation can propagate interval enclosures with a positive margin and stop at the first loss of those margins; no global extension theorem for arbitrary parameters is asserted.

There is an exact common-domain witness: K2265's fixed b=-1,a=r=0, y=C0(x³+D0)^(4/3), C0,D0>0 works on any declared compact x>0 interval, with explicit positive minima for y and F. Thus this interface is not dependent on an unproved existence claim. Its radial integral need not be elementary; fixed interval quadrature with a justified error or direct integration of chi is a named next implementation. No physical fit follows from that witness.

The family-scale transformation is y→s²y,a→s²a,r→s⁴r,r_d→r_d/s. When a,r are free, nondimensionalize with one H_* and profile the dimensionful coefficient/ruler combinations a/H_*²,r/H_*⁴ and H_*r_d, together with dimensionless initial shape data y0/H_*²,v0/H_*² and any shared distance offset. Independently fixed dimensional coefficients can break this nuisance symmetry; no universal unidentifiability is claimed.

## 4. Exact distance-and-expansion-node counterconstruction

Start with a smooth exact solution with H,F strictly positive on a compact interval, and any finite set of nodes. Put h=1/H. Choose psi smooth with compact support strictly between adjacent nodes and set

    h_epsilon=h+epsilon psi'.                    (5)

All h/H node jets are unchanged. Every node integral from one shared origin in the solved interval (or with the same shared boundary offset) is unchanged because the integral of psi' across its support is zero. Thus all flat transverse-distance nodes and radial-distance nodes coincide exactly for a fixed ruler. For sufficiently small epsilon in C1, h_epsilon>0 and F_epsilon>0 throughout by compactness and the original margins.

Choose psi locally equal to (x-c)^3/6 near an interior c, multiplied by a smooth cutoff equal to one there. At c its first two derivatives vanish, while the third derivative of psi is1. Consequently y and y' are unchanged, y'' shifts by -2epsilon/h(c)^3, and the constraint residual for the original coefficients changes by

    18 c² y(c) epsilon/h(c)^3 !=0.

The two histories therefore have identical finite H+distance nodes, including all nodal jets, but only the original satisfies the fixed equation. They also cannot both be members of the free-coefficient family if the starting exact solution is nonconstant on an unperturbed open interval: two distinct unperturbed y values fix the same a,r by K2265, and the interior residual then fails. The pure-R² positive witness supplies such a baseline.

This proves that finite point-compressed observations cannot CERTIFY family membership. It does not prove arbitrary finite nodes can be fit BY this finite-dimensional family, does not prevent finite observations from rejecting it through forward modeling, and does not prove the perturbed history fits an actual survey likelihood. The missing continuous information must be supplied by a declared reconstruction with quantified error or a full common-history forward model.

## Verification and successor

The exact probe independently checks weak/strong integrals and boundary terms, negative and false-acceptance controls, joint rank/profiling, deterministic-error arithmetic, ODE reconstruction and the local bump residual; the positive exact solution and scale covariance are checked in K2265. Universal smooth-bump and full-interval statements rely on the written proof and independent internal review, not finite samples. No external-expert, Lean, novel cosmology, empirical or remote-CI certification is claimed.

The next useful cosmology calculation is a finite-interval solver/validated domain plus an explicitly chosen observation operator with covariance and nuisance treatment, or a bounded theory-space residual exclusion. A derivative identity alone and a new finite-node pass are no longer useful endpoints. Run the listed probe; --write regenerates the hash-bound report.
