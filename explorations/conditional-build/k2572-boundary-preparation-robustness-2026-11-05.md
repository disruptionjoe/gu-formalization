---
title: "K2572 Stability of a prepared boundary relation is exponentially sensitive"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact annular preparation-error and two-boundary stability criteria; no physical boundary selection
scripts:
  - tests/channel-swings/k2572_boundary_preparation_robustness_probe.py
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
result: K2572
carrier: actual K2568 omega two-Cauchy-data family and the K2564 theta200 resonance on the same product completion LAYER=toy CHIRALITY=N/A
pairing: coefficient Sobolev norms and conserved Einstein readout ON=declared_carrier
real_structure: real coefficients and positive auxiliary norms
grading: source-selected physics and supplied mathematical preparations remain distinct
action_owner: repository-construction -- stated conditional model
target: robustness of the supplied stable preparation MAP-TYPE=evaluation
```

# The stable preparation needs correlated errors

## Result and backward demand

K2568 constructs a stable far-Dirichlet family of the actual curved homogeneous response, but does not test errors in the near normal-derivative relation that realizes it. Here that omitted robustness question has an exact answer. Relative to the natural order-one normal trace, a diagonal preparation error must decay exponentially in angular frequency to keep full-field continuation bounded on a fixed annulus. Arbitrarily small polynomially decaying calibration errors fail this criterion. The failure concerns independently perturbed near Cauchy preparation; directly prescribing noisy data at both boundaries remains stable in the theta-zero family.

This enlarges the analyzed family from one fixed near derivative to both separated Cauchy coordinates of every selected omega mode. Sections1--5 do not cover arbitrary B harmonics, the entire coupled solution space, or a physical time evolution. Section6 executes a specific additional theta-sector counterexample to a universal boundary extension. The scalar amplitude is proportional to the gauge-invariant Einstein response E h; auxiliary reconstruction can cost further polynomial derivatives. Positive sequence norms are not physical energy. A finite detector can be much more stable than the full field, as K2570 proves.

Source scope remains SC-ACT-01, SC-GEO-03 and SC-GEO-55 ASSERTS, SC-META-53 UNCERTAIN. Ledger0.263 LT-GR6b/10/11 and LT-SM8, the source-selected domain, Met(X) identification, physical observation and quotient remain open. No new source assertion, physical exclusion, novelty claim or canon change follows.

## 1. Fundamental solutions of the actual transformed equation

On K2568's fixed closed annulus, shift x so x=0 at t0 and x=d at t1. Keep

    x=log[tanh(t/2)/tanh(t0/2)], y=J(t)v,
    J=sinh(t)cosh(t)^(3/2),
    y''=(n²+V(x))y, n=m+1>=1,
    V=(c+35/4)sinh²(t)-(3/4)tanh²(t),
    c=120691003/77168, 0<V<=D=V(t1).

The prime here means x derivative. Complete fields are the unchanged

    Qfield=u R(1), h=-rE u R(1),
    e2=-A2^-1 B Qfield, E h=-(rE/2)(mu-5K)u R(1).

Every scalar solution of this equation gives these homogeneous fields by K2564/K2568; adding it to the same base response preserves the localized source. The auxiliary B is the existing first-order coupling, not a new manifold operator. J and its inverse are bounded on this fixed annulus, so scalar y estimates transfer to v and the stated invariant response without changing exponential criteria.

Let S_n solve S_n(0)=0, S_n'(0)=1, and let B_n solve B_n(0)=1, B_n(d)=0. The positive-potential Dirichlet problem is uniquely solvable. Put beta_n=-B_n'(0). Positivity and Volterra comparison give, with k_n=sqrt(n²+D),

    sinh(nx)/n <= S_n(x) <= sinh(k_n x)/k_n,
    0<=B_n(x)<=sinh(n(d-x))/sinh(nd)<=1,
    n coth(nd)<=beta_n<=k_n coth(k_n d).             (1)

The first inequality compares the same positive initial derivative, not two differently normalized solutions. S_n is positive and increasing on (0,d]. Since k_n<=n+D/(2n),

    A_d e^(nd)/n <= S_n(d) <= B_d e^(nd)/n,
    A_d=(1-e^(-2d))/2>0, B_d=exp(Dd/2)/2.           (2)

All constants are independent of n. A single-mode or flat-potential fixture does not prove (1); its proof is the actual positive Volterra/Dirichlet comparison above, using K2568's verified potential.

## 2. Exact stability criterion for imperfect diagonal preparation

Suppose an amplitude a_n is prepared with the perturbed x-normal trace

    y_n(0)=a_n, y_n'(0)=(-beta_n+epsilon_n)a_n.

The error sequence epsilon is fixed by the preparation rule before the amplitude is chosen. Uniqueness gives the exact identity

    y_n(x)=[B_n(x)+epsilon_n S_n(x)]a_n,
    y_n(d)=epsilon_n S_n(d)a_n.                    (3)

No approximation, asymptotic cancellation or fitted field is used. For H^s coefficient input and output with the SAME s, endpoint continuation is bounded iff

    sup_n |epsilon_n| S_n(d)<infinity,
    equivalently sup_n |epsilon_n| e^(nd)/n<infinity. (4)

Necessity uses normalized single modes at the endpoint. Sufficiency for the ENTIRE closed tube follows from |B_n|<=1 and S_n(x)<=S_n(d), giving operator norm at most 1+sup|epsilon S_n(d)| uniformly in x. The endpoint norm itself is exactly sup|epsilon S_n(d)|; do not identify it with the larger sufficient tube bound. Negative errors or cancellations at interior points cannot hide the endpoint because B_n(d)=0.

For input analytic norm sum n^(2s)e^(2rho n)|a_n|² with rho>=0 and output H^s, the exact criterion becomes

    sup_n |epsilon_n|e^((d-rho)n)/n<infinity.        (5)

The stable B part is bounded for every rho>=0. If epsilon_n=n e^(-alpha n), alpha>=0, the sharp radius is rho+alpha>=d, including equality. At equality the endpoint multiplier between the normalized spaces stays bounded away from zero. Exact continuation is bounded, but recovery from unweighted noisy amplitude data on that critical prior is not uniformly consistent when rho>0: K2568's indistinguishable single-mode proof applies with effective exponent d-alpha=rho. When rho=0 the forward map is bounded on the noise norm and ordinary Lipschitz recovery holds; the critical-noise assertion must not be extended to that case.

Every nonzero constant error and every power error epsilon_n=c0 n^(-q), c0!=0 and finite real q, fails (4). Thus no uniform finite-order error guarantee ensures stability on the unrestricted Sobolev ball. This does NOT say every finite-order approximation to beta fails: an approximation might have an exponentially small remainder or even be exact. The error sequence, not the name of an approximation method, decides (4).

## 3. Execute the full two-jet and finite-band consumers

The natural scaled Cauchy coordinates are (a_n,g_n), with g_n=y_n'(0)/n. Define the departure from the stable graph by

    zeta_n=g_n+(beta_n/n)a_n.

Then ALL selected two-jet solutions satisfy

    y_n(x)=B_n(x)a_n+n S_n(x)zeta_n,
    y_n(d)=n S_n(d)zeta_n.                        (6)

Beta_n/n is uniformly bounded by (1), so this change of Cauchy coordinates is a bounded invertible shear on H^s x H^s. The stable graph is exactly zeta=0. Consequently the endpoint requires an analytic radius d on the independent defect coordinate, not on an exactly correlated stable amplitude. Arbitrarily small independent uncertainty in the ACTUAL prepared g has unbounded endpoint amplification on an unrestricted l2 ball. This is not a claim that derivative measurement noise defeats an exact known stable prior: if the true preparation is known to satisfy zeta=0, ignore noisy g and reconstruct B_n a from the amplitude data. Noise correlated as delta g=-(beta/n)delta a stays on the stable graph and does not have this failure. The statement distinguishes absolute derivative error epsilon from normalized error epsilon/n.

For the band 1<=n<=N, suppose |epsilon_n|/n<=eta. Equation (2) gives the explicit sufficient endpoint error gain

    sup_(n<=N)|epsilon_n|S_n(d)<=eta B_d e^(dN).   (7)

An adversary using the maximal error eta n at mode N realizes gain at least eta A_d e^(dN). Thus to guarantee a chosen gain G for every such error, eta<=G e^(-dN)/B_d suffices; necessarily eta<=G e^(-dN)/A_d. These differ by fixed constants, and give the exact exponential dependence. This is a calibration requirement for the stipulated family, not an observed instrument tolerance.

The probe executes an exact transparent comparison fixture: V=0, d=log2, N=10. It gives nS_n(d)=(2^n-2^-n)/2, so the largest-mode gain for eta=1/1000 is 1048575/2048000, over one half. The exact uniform band tolerance for gain at most1/100 is 512/26214375. V=0 is a constant-potential comparison/control, NOT the actual curved potential. For the actual potential the lower comparison already makes that eta=1/1000 fail the gain1/100 test, independently of the unknown loose D upper constant. This is a valid one-sided transfer because V>0 increases S.

## 4. Execute the alternative: direct two-boundary control

Instead prescribe y_n(0)=a_n and y_n(d)=r_n. The exact solution is

    y_n(x)=B_n(x)a_n+T_n(x)r_n,
    T_n(x)=S_n(x)/S_n(d), 0<=T_n(x)<=1.           (8)

The maximum principle also gives B_n+T_n<=1: the constant1 has positive residual under -d²/dx²+n²+V, with the same boundary values as B+T. Therefore pointwise

    |y_n(x)|² <= B_n(x)|a_n|²+T_n(x)|r_n|²,
    ||y(x)||_(H^s)² <= ||a||_(H^s)²+||r||_(H^s)². (9)

The same estimate applies to differences, so independently noisy boundary amplitudes have bounded full-tube amplification. This is not inference of a distant boundary value from noisy near jets: it supplies that boundary as separate data/control. The required near normal relation is

    y_n'(0)=-beta_n a_n+r_n/S_n(d).               (10)

The extra term is exponentially small relative to n r_n. Equation (10) explains the apparent contrast with (6): bounded far errors correspond to highly correlated near jets, whereas independent near-slope errors can represent huge far amplitudes. No physical causal mechanism or source-selection principle enforces these correlations here.

There is also an interior existence gain. Comparison with the constant potential gives T_n(x)<=sinh(nx)/sinh(nd), while (1) bounds B_n. On every strictly interior subannulus x in[eta,d-eta], both are at most e^(-n eta)/(1-e^(-2d)). Thus any Sobolev boundary data define a convergent, angularly smooth interior solution. The ODE and its derivatives add only polynomial frequency factors on compact subannuli; the first-order auxiliary reconstruction is smooth there too. This proves interior fields, without claiming smooth boundary traces from rough data.

For an actual compact conserved detector F, let q^B_n=<F,h[(B_n/J) H_(n-1)]> and q^T_n=<F,h[(T_n/J) H_(n-1)]>. On finite boundary sums its reading is sum(q^B_n a_n+q^T_n r_n). Smooth compact F and its Einstein adjoint test, bounded B/T amplitudes and harmonic Parseval imply both coefficient sequences are square summable. One direct proof bounds the pairing by C ||(a,r)||_2 using (9), compact support and Cauchy-Schwarz, then applies Hilbert duality. Hence that readout extends to all l2 two-boundary data and has Lipschitz noise error bounded by sqrt(||q^B||²+||q^T||²) times the combined boundary-noise norm. This consumes the actual conserved observation construction, rather than relabeling arbitrary sequences as a detector. It does not establish an l2 bound for every derivative of h or e2, or select a physical F.

## 5. Released follow-through: characterize angularly mixed preparation errors

The diagonal criterion is not sufficient for an apparatus that mixes harmonics. Work on the selected harmonic coefficient H^s space, with all operator norms conjugated by the same n^s weight. Let a preparation supply

    g=-diag(beta_n/n)a+E a,
    D=diag(n S_n(d)).

Initially take E on finite-support amplitudes, with its output interpreted coordinatewise; do not assume it produces a valid endpoint field. The product is admissible on that dense domain only when E a belongs to Dom(D)={z: sum n^(2s)|D_n z_n|²<infinity}. A finite bound on DE then forces E itself to extend boundedly through E=D^-1 K. For an initially bounded E, closedness of D implies E(H^s) lies in Dom(D) and DE=K on all H^s. An error failing this domain condition has no bounded endpoint map; finite truncations below still define valid counterexamples. Equation(6) says the endpoint is exactly D E a. Bounded endpoint continuation exists iff this densely defined product extends to a bounded operator K on H^s. Equivalently, on the initial domain,

    E=D^-1 K.                                    (11)

Here D^-1 is a bounded exponentially smoothing diagonal operator by(2); its range lies in the domain of D. Thus every bounded K constructs an admissible E, and the equivalence has no hidden unbounded-operator inversion. The same input yields

    y(x)=diag(B_n(x))a+diag(T_n(x))K a.            (12)

It is an actual two-boundary solution with r=K a, bounded through the tube and smooth in its interior. Necessity is from the endpoint, sufficiency from (8)--(9). This completely characterizes linear angular mixing errors relative to this selected family, rather than checking only diagonal entries or a matrix norm before exponential amplification.

There is no open stability neighborhood in the natural normalized-error operator norm. Even rank-one errors can fail: take E a=c u <e_1,a>, c!=0, with u_n=e^(-sqrt(n)). The sequence u is rapidly decaying and belongs to every H^s; E can have arbitrarily small norm by scaling c. But D u has exponential growth and is not in H^s. Finite-mode truncations of u give genuine smooth solutions with uniformly small near error and unbounded endpoint norm as the cutoff grows. This proves failure of a uniform bounded-continuation estimate; no nonexistent infinite endpoint field is assigned. Conversely E=D^-1 K can mix arbitrarily many modes safely for every bounded K. Rank, small unweighted norm and smoothness alone do not decide robustness.

The probe executes a two-mode angularly mixed K and E=D^-1 K in the exact V=0 comparison fixture, checks DE=K, and rejects the substituted E=K that omits the exponential filter. It also checks growing finite truncations of a rank-one smooth-error sequence on square mode indices, where e^(-sqrt(n)) can be chosen exactly as 2^(-sqrt(n)) without changing the argument. These are supporting finite realizations of the written operator theorem, not a physical control prescription or an arbitrary-B-domain result.

## 6. Execute the strongest scope test: additional theta modes can resonate

The stable two-boundary result above fixes theta degree zero. Its generalization to the complete angular carrier is NOT automatic. K2564 gives the actual operator

    Y/K=-partial_t²-p(t)partial_t-sech²(t)Ltheta+csch²(t)Lomega.

For a theta harmonic of degree ell, Ltheta=ell(ell+2), and omega degree n-1, the same Liouville transform gives

    y''=[n²+V(t)-ell(ell+2)tanh²(t)]y.            (13)

The new negative term removes the positivity needed for the maximum principle. This is not just a missing proof: there are actual resonant annuli. Take n=1, ell=200 and t between asinh(1) and asinh(2). In the corresponding x interval [0,d0], define

    q(x)=ell(ell+2)tanh²(t)-1-V(t).

Since tanh²(t)>=1/2, sinh²(t)<=4 and V(t)<=4(c+35/4),

    q(x)>=20164-4c>10000, c=120691003/77168.      (14)

The interval length is

    d0=log[((sqrt(5)-1)/2)/(sqrt(2)-1)]>log(4/3)>1/4.

These inequalities have exact rational/radical checks in the probe. Solve the ACTUAL variable-coefficient equation y''+q(x)y=0 with y(0)=0,y'(0)=1. Its first positive zero x* occurs before pi/100<1/25<d0. A direct comparison proves this without a numerical zero search: if y stayed positive up to L=pi/100, put z=sin(100x)>0 there. The Wronskian W=y'z-yz' has W'=(10000-q)yz<0 and W(0)=0, while W(L)=100y(L)>=0, a contradiction. A zero at L is excluded by the same strict inequality. Initial positivity and continuity give the first zero in(0,L).

Choose the far annulus boundary at t* corresponding to x*. The nonzero smooth scalar solution then vanishes at BOTH scalar boundaries. Reconstruct the unchanged complete homogeneous fields and use a nonzero theta harmonic of degree200 with constant omega harmonic. The invariant E h is proportional to this nonzero scalar, so this kernel is not merely metric gauge. It can be added with arbitrary amplitude to the same base sourced response without changing either supplied scalar boundary amplitude. Its normal derivative and auxiliary e2 boundary data need not vanish; the counterexample concerns precisely the two scalar amplitude conditions. Thus the extended two-boundary problem on this resonant annulus has no uniqueness or bounded inverse from scalar boundary values to fields.

The far boundary is CHOSEN at a proved zero. This does not say an arbitrary previously fixed annulus is resonant, or that every full-angular boundary prescription fails. Extra field/normal boundary conditions, different endpoints or a restricted spectral domain change the question. Nor does it affect the theta-zero maximum-principle theorem, whose positive potential remains intact. It is a concrete adverse test on the actual larger harmonic carrier, not a conclusion inferred from indefinite signature. No physical-time instability or native GU exclusion follows.

### Execute the admissible endpoint repair and its precision limit

The resonant zero is simple: y(x*)=y'(x*)=0 would force the entire ODE solution to vanish, contrary to y'(0)=1. For a nearby far endpoint d with S_(ell,n)(d)!=0, the solution with near value0 and far value1 is S_(ell,n)(x)/S_(ell,n)(d). Choose a fixed interior point where the numerator is nonzero. Taylor expansion at the simple zero shows its magnitude grows as a nonzero constant divided by |d-x*|. Moving the boundary off resonance repairs this one mode's uniqueness but does not give a uniform bound over nearby annuli.

For each fixed integer pair (ell,n), every positive zero of S_(ell,n) is simple, hence isolated in the nonsingular interval. Its forbidden endpoint set is countable. The union over all harmonic pairs is still countable. Thus outside this exceptional endpoint set, EVERY separated mode and every finite harmonic sum has a unique scalar two-boundary solution. This is a concrete admissible mathematical repair under the same differential equation. It is not a common full-angular Sobolev inverse: nonvanishing alone gives no uniform lower bound on the denominators, and no uniform spectral bound or infinite-mode solution synthesis follows. The correct remaining full-domain question is quantitative spectral control at the actually prescribed endpoint, not the assertion that all choices resonate.

## Evidence and next condition

The decisive statements are the actual-potential comparison, exact fundamental-solution decomposition and endpoint single-mode converse. Exact symbolic and rational probe fixtures test conditional unit-determinant transfer algebra/decomposition, normalization, finite-band tolerance, boundary contraction and actual-sector resonance bounds; those fixtures are not independent continuum proofs. Contrary controls use a nonzero polynomial normal mismatch, erase the factor n in the scaled jet, and break the boundary correlation. A stable direct-boundary repair is explicitly preserved.

Next test a source- or instrument-justified mechanism against (4), (7), or the alternative two-boundary data requirement. For angularly mixed linear preparation, (11) is now the full criterion on the selected harmonic family; a physical model must justify its K and data access. Section6 now disproves unrestricted two-boundary uniqueness on some annuli after theta modes are admitted. A specified fixed full-angular domain and its boundary conditions remain to be tested. A numerical refinement of beta without a proved error sequence cannot certify robustness. K2570 scalar detection, K2564 source existence and K2566 finite-calibration ambiguity retain their exact scopes.

[K2568 actual equation and preparation](k2568-cauchy-preparation-bandwidth-2026-11-05.md), [K2570 conserved detector](k2570-detector-recovery-2026-11-05.md), [probe](../../tests/channel-swings/k2572_boundary_preparation_robustness_probe.py), [report](../../lab/process/k2572-boundary-preparation-robustness.json).
