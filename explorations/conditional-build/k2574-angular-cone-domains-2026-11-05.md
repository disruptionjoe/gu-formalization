---
title: "K2574 Stable domains on two disjoint angular cones"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: actual annular cone bounds and all-angular analytic impedance preparation; no general Sobolev inverse or physical domain selection
scripts:
  - tests/channel-swings/k2574_angular_cone_domains_probe.py
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
result: K2574
carrier: actual K2564 product completion with all theta and omega harmonic multiplicities LAYER=toy CHIRALITY=N/A
pairing: coefficient Sobolev norms and compact conserved Einstein tests ON=declared_carrier
real_structure: real coefficients and positive auxiliary norms; complexification only where explicit
grading: positive and oscillatory cones versus uncovered turning modes
action_owner: repository-construction -- stated conditional model
target: uniform response on a fixed declared spectral subspace MAP-TYPE=evaluation
```

# Two different data choices control two angular regimes

## Result and scope

K2572's actual theta200 resonance shows that scalar Dirichlet uniqueness fails on some annuli. It does not exclude stable full-frequency subspaces. On one FIXED annulus, the actual separated equation has an omega-dominated positive cone with stable two-boundary data and a theta-dominated oscillatory cone with stable real Cauchy data. Both cones contain infinitely many modes with unbounded theta and omega degrees. Their direct sum has a single bounded response operator and a bounded compact conserved readout. This expands theta-zero control without claiming all-angular inversion.

The intermediate turning band is genuinely present; sections1--6 do not bound it in the same Sobolev control norm. Section7 supplies a separate all-angular analytic-data preparation with a conservative bound. These are supplied mathematical preparations on the existing conditional product completion, not physically selected boundary conditions, causal time evolution, a self-adjoint coupled operator domain, or native GU recovery. SC-ACT-01, SC-GEO-03 and SC-GEO-55 remain ASSERTS; SC-META-53 remains UNCERTAIN. Ledger0.263 LT-GR6b/10/11 and LT-SM8, Met(X), observation and physical-quotient debts do not change. No novelty, canon or empirical claim follows.

## 1. Fixed carrier and exact coefficients

Keep K2568/K2572's actual transformation and fields:

    x=log[tanh(t/2)/tanh(t0/2)], 0<=x<=d,
    y=J(t)v, J=sinh(t)cosh(t)^(3/2),
    y''=P_(ell,n)(x)y,
    P=n²+V(t)−L a(t), L=ell(ell+2), n=m+1>=1,
    a(t)=tanh²(t), V=A sinh²(t)−(3/4)tanh²(t),
    c=120691003/77168, A=c+35/4.

Use every multiplicity in the S3 theta and omega harmonic spaces, with a fixed orthonormal REAL harmonic basis. The positive angular coefficient norm uses frequency nu=sqrt(1+n²+L). It is auxiliary Sobolev size, not physical energy. On a fixed nonsingular annulus J and J^-1 are smooth bounded. The unchanged homogeneous reconstruction gives h=−rE v R(1) and nonzero Einstein response proportional to v; the auxiliary e2 uses one differential coupling. Adding these fields to the same localized base source preserves the source.

Since dx/dt=1/sinh(t)>0, a increases. With z=sinh²t, V=A z−3z/[4(1+z)], whose derivative in z is A−3/[4(1+z)²]>0. Put a_j=a(t_j), V_j=V(t_j), D=V_1. Fix eta in(0,1).

## 2. Positive cone: two-boundary contraction and smoothing

Define E_eta by

    L a1 <= (1−eta)n².

Then eta n²<=P<=n²+D. The real basis solutions B(0)=1,B(d)=0 and T(0)=0,T(d)=1 are nonnegative and B+T<=1 by the one-dimensional maximum principle. For prescribed amplitudes u,r,

    y(x)=B(x)u+T(x)r,
    |y(x)|²<=B(x)|u|²+T(x)|r|².

Comparison with constant eta n² gives the unambiguous bounds

    B(x) <= (exp(−sqrt(eta)n x)−exp(−sqrt(eta)n(2d−x)))
            /(1−exp(−2sqrt(eta)nd)),
    T(x) <= (exp(−sqrt(eta)n(d−x))−exp(−sqrt(eta)n(d+x)))
            /(1−exp(−2sqrt(eta)nd)).

Thus every strictly interior subannulus smooths all angular frequencies exponentially: on E_eta, nu is comparable to n. Summing all multiplicities with nu^(2s) gives sup_x ||y(x)||_Hs²<=||u||_Hs²+||r||_Hs². Standard ODE comparison also bounds |B'|,|T'| by k coth(kd), k=sqrt(n²+D), hence by n sqrt(1+D)coth(d). Therefore the first x derivative lies in H^(s−1), uniformly through the closed tube. Higher derivatives follow from the ODE and smooth coefficients, losing at most their order. These are actual-potential proofs, not consequences of one flat fixture.

## 3. Oscillatory cone: stable real Cauchy data

Define O_eta by

    n²+D <= (1−eta)L a0.

Here L>0 and q=−P=L a−n²−V satisfies eta L a0<=q<=L a1. The equation is y''+qy=0. For the real or complex scalar energy E=|y'|²+q|y|²,

    E'=q'|y|²,  |E'|<=|q'|E/q,
    integral_0^d |q'|/q <= Tvar
       :=[L(a1−a0)+(D−V0)]/(eta L a0).

The last estimate uses separate monotonicity of a,V; it does NOT assume q monotone. Since the cone bounds D/L, Tvar is uniformly bounded over its modes. Integrating both signs yields exp(−Tvar)E(0)<=E(x)<=exp(Tvar)E(0).

Prescribe REAL data y(0)=u and y'(0)=sqrt(L)g. The energy is equivalent, uniformly on the cone, to L(|y|²+|y'/sqrt(L)|²). Consequently this full normalized Cauchy jet has a bounded invertible propagation map between any two sections. Unlike the positive cone's unrestricted Cauchy problem, it has no exponential frequency amplification. Unlike positive-cone Dirichlet control, it does NOT generally smooth the full Cauchy jet. This is an equation-specific estimate, not a sign-of-signature argument or a physical causality claim.

## 4. Execute exact nonempty cones and a real uncovered band

Take t0=asinh(1), t1=asinh(2), eta=1/2. Then

    a0=1/2, a1=4/5,
    V0=121337285/77168, D=606773239/96460.

The E cone is L<=5n²/8 and contains ell=j,n=2j for every integer j>=2. The O cone is n²+D<=L/4 and contains ell=4n for every integer n>=46, as well as ell=200,n=1. In the O cone q lies between L/4 and 4L/5. Also Tvar<=11/5: 4(a1−a0)=6/5 and 4(D−V0)/L<=1. Hence

    |y(x)|²+|y'(x)|²/L
       <=5 exp(11/5)(|u|²+|g|²).

The same argument bounds inverse normalized-jet propagation. For the actual ell200,n1 example the variation bound is 6496787331/3896984000<2. K2572's Dirichlet resonance is compatible with this Cauchy estimate: a nonzero solution with both values zero generally has nonzero near derivative.

The omitted band is not merely a gap in notation. For ell=5j,n=4j,j>=40,

    P(0)=(7/2)j²−5j+V0>0,
    P(d)=−4j²−8j+D<0.

Each such mode has at least one turning point. Neither cone theorem covers it. Nonzero individual Dirichlet denominators at a chosen endpoint do not supply a uniform estimate here. No assertion of unavoidable small divisors at every fixed endpoint is made.

## 5. Execute one common restricted domain and detector consumer

Use the orthogonal projectors onto the fixed disjoint E and O cones, including all multiplicities. The control space is the direct sum of an Hs Dirichlet pair on E and an Hs normalized Cauchy pair on O. Solve each mode by the corresponding data rule and sum. The estimates above give a unique C([0,d];Hs) scalar field and C([0,d];H^(s−1)) normal derivative, supported in E union O. Strong continuity follows first for finite harmonic sums, then by uniform bounds and density. The ODE holds distributionally; higher derivative estimates justify classical solutions for smooth data. No infinite series is inferred merely from modewise nonresonance.

Reconstruction multiplies by J^-1 and fixed smooth tensors; h has the scalar Sobolev bound, while e2 can cost one derivative. These estimates do not bound every complete field in the scalar norm. A compact smooth conserved detector F pairs with h through the unchanged conserved test construction. On H0 control data, compact support, Cauchy-Schwarz and the uniform scalar bound give |<F,h>|<=C_F ||control||. It extends continuously from finite sums, with Lipschitz error C_F times control-noise norm. No F or physical preparation is selected by that boundedness statement. This is a common SOLUTION OPERATOR for the declared subspace, not a full coupled Green inverse or all-angular self-adjoint realization.

## 6. Released alternative: impedance control on the oscillatory cone

This section explicitly COMPLEXIFIES the real equation; it represents two real quadratures with coupled boundary control, not an ordinary real Robin condition. Let k_j=sqrt(q(j)), j=0,d, and prescribe

    f0=y'(0)+i k0 y(0), fd=y'(d)−i kd y(d).

The conserved flux Im(y' conjugate(y)) and direct expansion give the exact identity

    |f0|²/k0+|fd|²/kd=E(0)/k0+E(d)/kd.

In particular zero f0,fd forces zero Cauchy data, hence zero solution. A nonsingular two-by-two boundary map therefore gives existence and uniqueness for each mode. Since k_j is comparable to sqrt(L), the flux identity and energy propagation bound control the normalized jet by |f0/sqrt(L)|²+|fd/sqrt(L)|² uniformly. Thus infinite-mode synthesis works on the O cone in these scaled boundary norms too. This genuinely removes its scalar Dirichlet resonances by changing the prescribed data. Same-sign impedances would not give the sum identity; the exact probe includes a resonant same-sign counterexample. This cone-specific impedance estimate does not cover the turning band; section7 uses a different impedance and a stronger data norm.

The original t jets are obtained from y=Jv and y_x=sinh(t)(J_t v+J v_t). On this fixed annulus these are bounded invertible shears/rescalings after dividing the normal coordinate by n on E or sqrt(L) on O. The estimates therefore survive coordinate conversion; this does not turn the auxiliary norms into physical energy.

## 7. Released full-angular consumer: analytic impedance preparation

There is a useful full-angular successor without pretending the turning band has a polynomial bound. Keep the SAME fixed annulus, actual equation and all harmonic multiplicities, but prescribe analytic boundary data for an explicitly complexified homogeneous preparation. Set

    nu=sqrt(1+n²+L), k=sqrt(nu²+D).

Then |P|<=max(n²+D,L)<=nu²+D=k². Unlike section6, this k is positive even when P changes sign and is identical at both ends for each mode. Prescribe f0=y'(0)+iky(0), fd=y'(d)−iky(d), and let g0=f0/k, gd=fd/k. Conservation of Im(y' conjugate(y)) gives the EXACT identity

    ||Z(0)||²+||Z(d)||²=|g0|²+|gd|²,
    Z=(y,y'/k).

This uses the positive auxiliary norm |y|²+|y'/k|², not the possibly indefinite expression with q. Homogeneous boundary data force zero y,y' at an endpoint. The finite two-boundary linear map is injective, hence surjective, for EVERY mode. It removes zero denominators by changing boundary data, without moving the annulus or asserting a lower bound for the old Dirichlet problem.

The exact first-order equation is

    Z'=k [[0,1],[P/k²,0]] Z.

The Euclidean operator norm of its displayed matrix is max(1,|P|/k²)<=1. Gronwall from EACH endpoint therefore yields

    ||Z(x)||<=exp(k min(x,d−x)) sqrt(|g0|²+|gd|²)
             <=exp(k d/2) sqrt(|g0|²+|gd|²).                  (A)

This is an upper bound, not a claim that the exponential rate is sharp or needed for this actual potential. Define the analytic data norm by summing nu^(2s)exp(2rho nu)(|g0|²+|gd|²) across all modes and multiplicities. Since k<=nu+sqrt(D), the gain in(A) is at most exp(sqrt(D)d/2)exp(nu d/2). Thus if rho>=d/2, (A) gives a bounded homogeneous solution map into C([0,d];Hs), with normal derivative in C([0,d];H^(s−1)). The density argument from section5 proves convergence on the entire closed tube, including the critical equality case; higher derivatives lose their order. If rho>d/2, the remaining exponential margin gives smooth angular fields through the closed tube. Multiplication by J^-1 and reconstruction preserve the earlier derivative bookkeeping. Every smooth compact conserved detector is continuous on this analytic control space.

This is a full-angular homogeneous preparation for supplied two-real-quadrature data. It is NOT an arbitrary-Sobolev boundary inverse, an inhomogeneous Green operator, a source-selected physical or causal law, or a sharp analytic threshold. Treating D as a fixed lower-order coefficient, rather than multiplying the leading frequency by sqrt(1+D), improves the sufficient radius to d/2; the fixed prefactor exp(sqrt(D)d/2) remains conservative. On the concrete annulus d=log[((sqrt5−1)/2)/(sqrt2−1)]. No uniform polynomial estimate has been proved for the turning band, and no claim that one is impossible follows. The finite supporting probe verifies the auxiliary flux cancellation, the first-order matrix singular values and a true turning-mode inclusion; the inequality and infinite-series argument carry the universal result.

A contrary comparison explains why the analytic weight cannot simply be dropped from this proof. On a centered interval of length d, choose k*d>pi/2 and a=pi/(4k). Let P=−k² for |x|<=a and P=+k² outside. The exact C1 solution is cos(kx) inside and exp(−k(|x|−a))/sqrt(2) outside. Its center normalized jet has norm1, whereas its two normalized impedance data have combined norm sqrt(2)exp(−k(d/2−a)). Amplification therefore equals exp(k*d/2−pi/4)/sqrt(2). This piecewise real barrier/well is a comparison/control, NOT the actual smooth angular potential; it refutes a general inference from endpoint flux to unweighted interior control, but proves neither sharpness nor analytic necessity for the actual family.

## Evidence and next condition

The comparison, energy, density and flux proofs above carry the universal claims. The probe checks exact potential derivatives/constants, infinite-family polynomial inequalities, flux identities and independent contrary constructions; finite fixtures support but do not certify the continuum theorem. Next requires a sharper or polynomial turning-band estimate for a prescribed boundary rule, or independently justified physical control/observation; the conservative all-angular analytic preparation is now constructed. Preserve K2572's preparation-error criterion and resonance, and the difference between scalar stability, auxiliary derivative costs and physical selection.

[K2572 actual equation and resonance](k2572-boundary-preparation-robustness-2026-11-05.md), [probe](../../tests/channel-swings/k2574_angular_cone_domains_probe.py), [report](../../lab/process/k2574-angular-cone-domains.json).
