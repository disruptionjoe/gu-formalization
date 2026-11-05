---
title: "K2568 Sharp bandwidth and noise cost of annular Cauchy preparation"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: selected homogeneous mode-family Cauchy instability and sharp analytic-prior noise rate; no physical evolution or global boundary theorem
scripts:
  - tests/channel-swings/k2568_cauchy_preparation_bandwidth_probe.py
---

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
result: K2568
carrier: original K2564 homogeneous response on a fixed A7 times B7 annulus with normalized omega harmonics LAYER=toy CHIRALITY=N/A
pairing: auxiliary positive harmonic coefficient norms and compact conserved metric-test duality ON=declared_carrier
real_structure: real separated solutions and real Cauchy coefficients
grading: exact data, noisy data, analytic preparation and metric gauge remain distinct
action_owner: repository-construction -- selected comm/symi/symi completion
target: preparation stability and optimal worst-case endpoint reconstruction MAP-TYPE=evaluation
```

# Complete data can select a response without selecting it stably

## Result, object and scope

K2566 shows why finitely many calibrations do not select the local response to K2564's actual localized source. A natural repair is to supply complete Cauchy data. On an explicit homogeneous subfamily of that SAME curved system, complete mode data uniquely select each separated solution, but arbitrarily small smooth data can give arbitrarily large gauge-invariant responses. This is an exact calculation on the actual operator, not a transfer from the signature of a generic ultrahyperbolic equation.

The executed repair supplies an analytic preparation radius rho. Propagating between two annuli costs exactly d=log(tanh(t1/2)/tanh(t0/2)) of that radius. A further executed consumer proves the sharp noisy-data reconstruction rate R^(d/rho) delta^(1-d/rho) when rho>d. At rho=d the forward map is bounded but uniform noisy recovery fails. A fixed smooth conserved detector also witnesses discontinuity from smooth Cauchy data. A different supplied far-boundary condition then constructs stable continuation, with an explicit order-one angular normal-trace requirement.

Sections1--5 concern the named omega-harmonic, zero-normal-derivative homogeneous family in the supplied completion. Section6 concerns a different far-Dirichlet boundary-prepared family of the same omega modes. They do not establish an instability in physical time, exclude a complete global boundary prescription, or identify the selected product with Met(X). The auxiliary positive norms are not physical energy. SC-ACT-01, SC-GEO-03 and SC-GEO-55 remain ASSERTS at their existing source scope; SC-META-52 and SC-META-53 remain UNCERTAIN. Ledger0.263 LT-GR6b/10/11 and LT-SM8 keep their native action, observation and physical-domain debts. No GU verdict or novelty claim follows.

## 1. Actual homogeneous fields and a growing angular sector

Reuse K2564/K2566's complete homogeneous response, including its auxiliary row:

    (Y+mu-21K)u=0, Qfield=u R(1), z=0,
    h=-rE u R(1), e2=-A2^-1 B Qfield,
    E h=-(rE/2)(mu-5K)u R(1).                     (1)

Here B is the first-order auxiliary coupling, not the B manifold or a new scalar operator; A2^-1 is the unchanged parallel algebraic inverse. E is the original formally self-adjoint Einstein linearization with its Bianchi identity. E annihilates metric gauge, so E h is gauge-invariant. The chosen representative h alone is not. The exact constants satisfy

    K=35 kappa^2/3624192,
    mu=611557655 kappa^2/39953092608,
    c=mu/K-21=120691003/77168>0,
    mu-5K=67736495 kappa^2/4439232512>0.

Fix 0<t0<t1 inside one nonsingular B annulus. Set the theta dependence constant and choose one real L2-normalized omega harmonic H_m of degree m, with Lomega H_m=m(m+2)H_m. For u=v_m(t)H_m(omega), the actual B Laplacian gives

    v_m''+p(t)v_m'=[m(m+2)csch^2(t)+c]v_m,
    p(t)=3(tanh t+coth t),
    v_m(t0)=1, v_m'(t0)=0.                        (2)

The positive RHS and integrating-factor formula imply v_m>0 and v_m'>=0. Each mode is smooth on the same closed annulus; no infinite-series existence has yet been assumed.

## 2. Exact exponential rate, with uniform two-sided constants

Put n=m+1 and

    x=log tanh(t/2), dx/dt=1/sinh t,
    J(t)=sinh t cosh^(3/2)t, y(x)=J(t)v_m(t).

Direct substitution of (2), including the first derivative, yields

    y_xx=[n^2+V(t)]y,
    V(t)=(c+35/4)sinh^2t-(3/4)tanh^2t,
    y(x0)=J0, y_x(x0)=A0 J0/2,
    A0=5cosh t0-3sech t0>0.                       (3)

V is positive and increasing: write it as sinh^2t times (c+35/4-(3/4)sech^2t); both factors are positive increasing. Let D=V(t1), d=x1-x0>0, and k_n=sqrt(n^2+D). Positive Volterra kernels compare (3) to the constant-coefficient equations y_xx=n^2 y and y_xx=(n^2+D)y, with the same positive initial data. Therefore

    J0 cosh(nd) <= y(x1)
       <= J0[cosh(k_n d)+(A0/(2k_n))sinh(k_n d)].

Use n>=1, k_n<=n+D/(2n), cosh z>=e^z/2 and sinh z<=e^z to obtain

    c_- e^(nd) <= b_n:=v_(n-1)(t1) <= c_+ e^(nd),
    c_-=J0/(2J1),
    c_+=(J0/J1)(1+A0/2)exp(Dd/2).                 (4)

These constants can be loose; their independence of n proves the EXACT exponential rate d. The probe derives the Liouville potential independently and checks its sign factorization. No numerical ODE integration supplies the universal estimate.

## 3. Smooth-data instability, also visible to a fixed conserved detector

On the selected sequence of normalized harmonics, define the auxiliary Sobolev norm by sum n^(2s)|a_n|^2. This is equivalent to the ordinary angular Sobolev norm because 1+m(m+2)=n^2. Tensor norms use a fixed positive majorant on a compact A patch; they are not contractions with an indefinite form.

Take a single initial coefficient a_n=exp(-eta n) with 0<eta<d. Every finite angular Sobolev norm tends to zero. Differentiating (2) repeatedly at t0 expresses any fixed normal jet as a polynomial in m(m+2) times these initial data. The algebraic/first-order reconstruction (1) therefore makes every fixed finite initial jet of the full fields tend to zero too. Equation(4) makes the endpoint E h norm diverge. No fixed finite loss of Sobolev derivatives repairs this map. Initial data are complete and smooth in this statement; the instability is not caused by leaving finitely many calibration numbers unspecified.

For a stronger output topology choose a compact t slab [ta,tb] inside (t0,t1), disjoint from the B source, and 0<eta<d_a=x(ta)-x0. Choose a nonnegative smooth bump chi(t) supported in the slab and nonzero on an interior subinterval. The angular function

    g(omega)=sum_(n>=1) exp(-sqrt(n)) H_(n-1)(omega)

is smooth: harmonic derivatives grow only polynomially with n, and its coefficients decay faster than every inverse power. Choose a compact A tensor W_A whose metric pairing with R(1) has a fixed nonzero sign; such a test exists because R(1) is nonzero and the pairing nondegenerate. Let W=chi(t)g(omega)W_A, constant in theta, with the sign adjusted for the coefficient in (1), and F=E W. Then F is ONE fixed smooth compact conserved detector. Orthogonality, positive volume density and the uniform lower bound on the slab give

    <F,h_n>=<W,E h_n>
         >=C exp[(d_a-eta)n-sqrt(n)] -> infinity.   (5)

The detector is constructed mathematically, not identified with an empirical instrument. Full angular spheres are compact; the A and t cutoffs make W compact. Thus the chosen preparation-to-response map is discontinuous even into distributions on this tube. Adding h_n to the same base response preserves the actual source. No claim compares responses satisfying the same complete global boundary conditions.

## 4. Executed repair: exactly how much analytic preparation suffices

In the known zero-normal-derivative omega family supply the independent preparation norm

    ||a||_(rho,s)^2=sum n^(2s)exp(2rho n)|a_n|^2.

For finite sums, endpoint continuation is the diagonal map T:a_n -> b_n a_n. By (4), it extends boundedly from this analytic space to endpoint H^s iff rho>=d. Sufficiency is termwise comparison; necessity uses single modes. At the endpoint rho=d the map is bounded with no spare exponential margin. For rho<d there are also members of the prior space whose formal endpoint series is not in H^s, so an unrestricted endpoint solution cannot be silently assigned.

This is a supplied mathematical repair, not a derivation of a physical preparation. It leaves all global boundary and source-selection choices intact. Norms for the reconstructed auxiliary field may require additional polynomial factors; the sharp statement here is for the scalar amplitude and the proportional invariant E h, or the fixed h representative, on the named family.

## 5. Executed noisy-data consumer: optimal exponent and its failure at equality

Use s=0. Assume ||a||_(rho,0)<=R, rho>d, and observe z=a+e with ||e||_2<=delta. Define (T_N z)_n=b_n z_n for n<=N and zero otherwise, so truncation includes the actual continuation multiplier. From (4),

    ||T_N z-Ta||_2
      <=c_+[e^(dN)delta+e^(-(rho-d)(N+1))R].       (6)

For delta small enough that N=floor(log(R/delta)/rho)>=1, (6) is at most

    2c_+ R^(d/rho)delta^(1-d/rho).                 (7)

Indeed N<=log(R/delta)/rho<N+1 bounds each term by that same scale. No noise probability distribution or Gaussian assumption is used.

The exponent cannot be improved uniformly, even by nonlinear estimators. Put n=ceil(log(R/delta)/rho), and present the identical observed datum z=0 for the two permissible truths

    a^+=R e^(-rho n)e_n, a^-=-a^+,
    e^+=-a^+, e^-=-a^-.

Their noise norms are at most delta. At least one reconstruction error is at least half their output separation, hence by (4) at least

    c_- e^(-(rho-d)) R^(d/rho)delta^(1-d/rho).     (8)

This is a sharp minimax RATE up to constants, not the exact minimax constant. At rho=d the same alternatives give a lower bound c_-R for arbitrarily small delta: bounded exact forward continuation does not imply uniformly stable noisy recovery on this critical analytic ball. At rho<d the forward map itself is unbounded. A named smoother detector could require less bandwidth; neither (8) nor the chosen detector (5) says that every detector is unstable.

## 6. Execute a different repair: correlated far-boundary preparation

The growing family above fixes the near normal derivative to zero. A different supplied boundary relation can exclude its growing component. On x in[0,d], prescribe y(0)=a and y(d)=0 for (3). The positive quadratic functional

    integral_0^d [y'^2+(n^2+V)y^2] dx

has a unique minimizer with these endpoints, solving the same equation. Define beta_n=-y'(0)/a (independent of nonzero a). Integration by parts identifies beta_n a^2 with the minimum energy. Comparing with constant potentials n^2 and n^2+D gives

    n coth(nd)<=beta_n<=k_n coth(k_n d).            (9)

The scalar maximum principle gives, for a>0,

    0<=y(x)/a<=sinh(n(d-x))/sinh(nd)<=1.           (10)

Indeed the upper comparison has the same endpoint values and its positive-operator residual is V times that comparison, which is nonnegative. Linearity handles negative coefficients. In original variables the necessary near trace is

    v'(t0)=-[beta_n+A0/2]v(t0)/sinh(t0),
    |v(t)/v(t0)|<=J0/J(t)<=1.                    (11)

Thus this DIFFERENT boundary-prepared family has bounded coefficient-l2 continuation and bounded amplification of l2 input noise, with no analytic radius assumption. It answers the instability's admissible-repair test at the same differential equation, while changing the specified preparation. This scalar far-boundary zero does not require e2 or the normal derivative to vanish there. The exact far-boundary zero and the nonlocal angular correlation (11) are supplied conditions; neither is selected by the source or identified with physical causal data. It does not contradict sections3--5, whose near normal derivative was zero.

There is a genuine regularity price: (9) implies beta_n is comparable to n. The prepared normal trace maps angular H^s to H^(s-1). An l2 amplitude need not have an l2 normal derivative, and no l2 estimate for every auxiliary field is asserted. For any fixed interior x>0, (10) gives exponential angular smoothing. This confines the result to a clear boundary preparation alternative instead of treating failure of one Cauchy class as failure of every admissible domain.

## Verification, contrary cases and next condition

Universal comparison and minimax proofs above are distinct from exact symbolic identities and finite supporting fixtures. The producer checks the actual constants, signs, transformed potential, zero-derivative conversion, polynomial jets and a rational exponential-coordinate bandwidth/noise example. Controls change the angular sign, omit the conjugating weight, erase the critical bandwidth, and replace a noisy inverse by exact-data continuity. Independent internal geometry/PDE and hostile review are required; no external-expert, proof-assistant or physical certification is claimed.

The new nonlocal stable boundary relation excludes the growing modes mathematically. The next useful preparation question is whether an independently justified source or observation condition selects it or another stable relation. Its imposed far-boundary zero remains an external choice, not a source-selected answer. The exact selected-family noise exponent supplies a concrete criterion for any proposed detector/preparation consumer. K2564's non-Cauchy distributional existence and K2566's finite-calibration result remain valid.

[K2564](k2564-localized-spectral-response-2026-11-05.md), [K2566](k2566-finite-observation-preparation-2026-11-05.md), [probe](../../tests/channel-swings/k2568_cauchy_preparation_bandwidth_probe.py), [report](../../lab/process/k2568-cauchy-preparation-bandwidth.json).
