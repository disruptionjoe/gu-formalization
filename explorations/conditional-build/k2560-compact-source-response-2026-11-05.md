---
title: "K2560 Actual compact radial forcing and controlled bounded-mode response"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: actual compact radial response for supplied bounded B eigenfamilies; no B point-source synthesis or physical boundary selection
scripts:
  - tests/channel-swings/k2560_compact_source_response_probe.py
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
result: K2560
carrier: actual compact smooth radial pressure times prescribed bounded B eigenfamilies on the selected curved A7 times B7 product LAYER=toy CHIRALITY=N/A
pairing: distribution duality with compact smooth conserved symmetric metric tests ON=declared_carrier
real_structure: real nonzero kappa; real distributional B data and real parts of complex factor solutions
grading: scalar and TT source splits, original metric h, shifted metric z and displacement Q remain distinct
action_owner: repository-construction -- selected comm/symi/symi completion of K2537
target: regular-center full-source response, bounded spectral synthesis and supplied-readout continuity MAP-TYPE=evaluation
```

# K2560 Actual compact radial forcing through regular-center inverses

## Result and retained scope

For every smooth-even compact radial pressure profile in K2552's conserved source class, and every prescribed B-eigendistribution rho satisfying Y rho=nu rho, the full selected linear system has a regular-center response on the entire small radial tube. The result uses the actual Dirichlet scalar/TT split, including its cancelling tails. It does not approximate the compact profile by polynomials. It supplies quantitative potential bounds uniform on bounded nu sets, continuous dependence on radial data, and bounded spectral superposition under explicitly supplied integrability hypotheses.

This is new relative to K2550's supplied one-coordinate TT source and K2556/58's finite radial polynomials with arbitrary B distributions: the radial cutoff region is now solved in the full conserved-pressure source. The two advances are complementary. A B point source is not an eigendistribution; this construction does not yet solve the original compact-profile times delta_B source or provide unrestricted spectral synthesis.

The regular-center inverse data are a supplied mathematical preparation, not source-selected physics, a causal Green operator or uniqueness of the full system. SC-ACT-01, SC-GEO-03 and SC-GEO-55 keep their ASSERTS polarities and SC-META-53 its UNCERTAIN polarity. The independent product, metric, action completion and source remain conditional repository objects. GR6b/10/11 and ledger0.263 do not move.

## 1. Explicit entire inverses, including the center

Use K2552's K=35 kappa^2/3624192, R=1/abs(kappa), X=partial_r^2+(4alpha+2beta)partial_r and D5=partial_r^2+(6alpha+4beta)partial_r. Their weights are w2=C^4 S^2 and w4=C^6 S^4. On [0,R],

    (1/2)r^m <= w_m(r) <= r^m, m=2,4.

The m=2 estimate is K2552. For m=4, sin(x)/x>=1-x^2/6 and cos^2(x)>=1-x^2 imply
w4/r4 >=(1-x^2)^3(1-x^2/6)^4 >=1-(11/3)x^2>1/2,
where x=sqrt(K)r. These estimates also identify a smooth positive even quotient w_m/r^m at the center.

For continuous F define

    (T_m F)(r)=integral_0^r [1/w_m(s)] integral_0^s w_m(v)F(v) dv ds.

Then T_m F(0)=0, (T_m F)'(0)=0 and L_m T_m F=F, where L2=X and L4=D5. The derivative is O(r); there is no center flux or delta source. On smooth even input this is a smooth even solution. This follows directly from w_m=r^m a(r^2) with positive smooth a: the inner integral is r^(m+1) times a smooth even function, and each subsequent integration preserves evenness. The same argument iterates for the resolvent equation below.

For n>=0, positivity of the kernel and weight comparison give

    |T_m^n F(r)| <= ||F||_infinity 2^n r^(2n)/(2n+1)!.

Indeed applying T_m to r^(2n) bounds it by
2 r^(2n+2)/[(2n+m+1)(2n+2)], no larger than the m=2 expression; induction gives the displayed factorial. In particular T_m is bounded on C[0,R]. For every complex z the operator series

    R_m(z)=sum_(n>=0) z^n T_m^(n+1)

converges absolutely in operator norm and solves (L_m-z)R_m(z)F=F with zero regular center value. Its norm obeys

    ||R_m(z)|| <= H_R(|z|),
    H_R(q)=sum_(n>=0) 2^(n+1)R^(2n+2)q^n/(2n+3)!
            <= (R^2/3) exp(sqrt(2q)R).

For q>0 the series also equals
2R^2 [sinh(t)-t]/t^3, t=sqrt(2q)R, and H_R(0)=R^2/3. The exponential bound follows termwise from (2n+3)! >=6(2n)!.

Uniqueness among regular solutions with value zero at0 follows without a small-z restriction: f=zT_m f implies f=z^n T_m^n f, whose sup bound tends to zero. The solution of f=T_m(F+zf), together with the weighted integral identity, gives smooth-even regularity for smooth-even F. No smooth Cauchy theorem for the indefinite B geometry is used: this is a one-dimensional radial Volterra problem.

## 2. Solve the actual full-source equations

Fix real nu and a real local distribution rho on B satisfying (Y-nu)rho=0. Nonzero smooth analytic eigen-germs are available by the already established noncharacteristic analytic construction; a general eigendistribution is accepted only when actually supplied. All products below are smooth radial functions tensor rho, hence defined.

Take the actual smooth-even compact A,P satisfying P'+4alpha(P-A)=0, with original source eigenvalues A/2,P/2,P/2. In particular K2531's given A and its repaired pressure are admitted. Use K2552's exact Dirichlet splitter

    (X+7K)chi_D=-t/6, t=(4A+3P)/2, chi_D(R)=0,
    b_D=P/2+(4alpha+2beta)chi_D'+6Kchi_D.

Do not truncate chi_D or b_D outside the source support. Define

    v=rE R_4(16K-nu)b_D,
    u=-(rE/c) R_4(21K-mu-nu)b_D,
    w=R_2(-nu-12K)chi_D.

They satisfy exactly the two TT and scalar Einstein equations of K2552:

    (D5+nu-16K)v=rE b_D,
    c(D5+nu+mu-21K)u=-rE b_D,
    (X+nu+12K)w=chi_D.

For the scalar displacement let d(X,nu)=L product_(j=1)^5(X-z_j). The full determinant from K2554 is degree five in X with constant leading coefficient L!=0; keep its mixed XY Q0(X+Y) term. Solve sequentially

    f0=chi_D/L,
    fj=R_2(z_j) f_(j-1), j=1,...,5; U=f5.

Then d(X,nu)U=chi_D. Differential factors commute; no commutation of the chosen inverse operators is used. This solution has (X^j U)(0)=0 for j=0,...,4. Conversely those regular central jets make it unique for the scalar polynomial equation, by recursive factorization or the Volterra uniqueness argument. Thus the result is independent of root order; taking real parts is sufficient for real source data, and uniqueness also proves the result is real. Repeated roots cause no problem.

Now use the original K2552 full reconstruction with Y replaced by nu on rho:

    z_TT=R(v)rho, Q_TT=R(u)rho,
    z_scalar=-(rE/2) S0(w rho),
    Q_scalar=-rE T[adj(M) vsrc (U rho)],
    z=z_TT+z_scalar, Q=Q_TT+Q_scalar,
    h=z-rE sym(Q), e2=-A2^-1 BQ.

Every selected row, including skew, mixed, auxiliary grade2 and original metric, follows from the already proved full intertwinings and the four now solved scalar equations. The source is the same compact radial pressure times rho, with its half normalization. The tensors extend smoothly through the normal center with distributional B coefficients; no punctured-tube solution has been substituted.

The central data select these potentials in this sufficient invariant construction. They do not classify all solutions, fix physical boundary values, or imply gauge uniqueness of the full coupled system.

## 3. Bounds, continuity and the bounded-family consumer

For |nu|<=V, write d(X,nu)/L=X^5+sum_(j=0)^4 a_j(nu)X^j and choose

    Z(V)=1+max_(j=0,...,4) sup_(|nu|<=V)|a_j(nu)|.

This is finite and executable from the exact polynomial; the elementary Cauchy root bound gives |z_j|<=Z(V). Consequently

    ||U||_infinity <= |L|^-1 H_R(Z(V))^5 ||chi_D||_infinity,
    ||w||_infinity <= H_R(V+12K)||chi_D||_infinity,
    ||v||_infinity <= |rE|H_R(V+16K)||b_D||_infinity,
    ||u||_infinity <= |rE/c|H_R(V+abs(21K-mu))||b_D||_infinity.

The existing Dirichlet radial inverse also supplies a sup bound. Its positive kernel and the same weight comparison give ||A_r^-1||<=R^2/3. Hence

    ||chi_D||_infinity <= [R^2/(18(1-7KR^2/3))]||t||_infinity.

The constant is finite at the actual KR^2. The factor bound can be conservative; it is an honest finite bound, not an optimal response estimate or N-uniform B-point-source synthesis.

For smooth-even radial inputs, the integral equation and differentiated radial equation give continuous linear maps in the smooth-even Frechet topology. Uniformly for nu in a compact interval, every output derivative seminorm is bounded by a finite input derivative seminorm with a finite parameter-dependent constant. One way to see center regularity uniformly is to use s=r^2: w_m=r^m a(s), and
f'(r)/r=integral_0^1 theta^m a(r^2 theta^2)/a(r^2) [F(r theta)+zf(r theta)] dtheta.
Repeated differentiation of this identity controls each even derivative seminorm. Away from0 the usual differentiated integral formula suffices. The constant may depend on derivative order and V. This is stronger than a C0 potential bound; the differentiated full tensor reconstruction uses these seminorms.

Here is a precise superposition statement, with NO assertion that an arbitrary source has such a representation. Let J be a compact parameter space, nu:J->[−V,V] measurable, and let rho_j be strongly measurable H^s(B) distributions with (Y-nu(j))rho_j=0 on a fixed B chart. Suppose a finite signed/complex measure sigma obeys integral_J ||rho_j||_(H^s) d|sigma|(j)<infinity. The source A,P is fixed. The parameter-dependent radial response maps above are continuous (equivalently obtained from their Volterra equations rather than a discontinuous root labeling). Their Bochner integrals define full distributional fields, and every finite-order differential equation passes under the integral by continuity into a lower Sobolev/distribution space. The source is the actual compact radial profile tensor integral rho_j d sigma.

Thus one gains a nonfinite bounded-spectral-family response, when that family and integrability are supplied. A concrete simpler instance is a finite family of actual analytic B eigen-germs. No completeness theorem, bounded spectral projector for the indefinite B operator, or representation of delta_B is asserted. Allowing V→infinity would require uniform integrable bounds for the supplied family and derivatives; the displayed constants grow and do not establish that limit.

For a fixed compact smooth conserved metric test F, pairing with h is continuous under these data limits, because h converges in distributions and all reconstruction differentiations are finite order. This is stability of a specified supplied-response observation, not physical uniqueness or calibrated observability.

## 4. Restore splitter descent by an explicit overlap prescription

Independent center-zero inverses of the scalar and TT equations are not presumed to match on the overlap. Fixing chi_D defines the constructed source-to-response map. To make its extension to another regular splitter explicit, write

    chi=chi_D+a psi, b=b_D-a b_psi,
    psi(R)=1, (X+7K)psi=0, Tpsi=R(b_psi).

The fixed response above remains the base response. For nu not equal to -mu or -5K, prescribe the overlap response using

    q=rho/[c(nu+mu)], W=rho/(nu+5K).

K2558's exact eigenline/cofactor identities give Q_s=Q_t=-rE q Tpsi and
z_s-z_t=-(rE/2)Lie_(W grad_A psi)G. Define the scalar and TT extensions by adding a times these respective overlap responses with opposite source signs. Their combined original-metric change is exactly that diffeomorphism; Q and auxiliary e2 are unchanged. Compact conserved metric observations are therefore independent of a under this synchronized prescription.

This is an explicit correction to a naive independently center-zero prescription, not a proof that those naive responses already agree. At nu=-mu or -5K the fixed-Dirichlet construction in section2 still exists; only this pure-eigenmode overlap formula has a pole. One may use K2558's separately justified generalized B solutions to synchronize there, but that leaves the single eigenspace and is outside this bounded-eigenmode formula. Uniform overlap bounds require distance from both poles.

## 5. Exact remaining source gap

A nonzero B point delta is not a finite-mode eigendistribution: (Y-nu)delta has a nonzero second-derivative principal part for every nu, since the B metric is nondegenerate. More generally no nonzero polynomial F(Y) annihilates delta, because its highest derivative symbol is the nonzero polynomial in the nondegenerate quadratic symbol of Y. Thus finite spectral sums cannot equal the actual invariant point source. An infinite parameter representation plus sufficient estimates, or a different direct distributional domain construction, is still needed.

The new result solves the actual radial cutoff in a complementary full-source class and gives controlled bounded spectral synthesis, but does not erase that B-localization debt. Source-disjoint observations can still depend on the supplied preparation; K2558's homogeneous ambiguity remains. No native GU or empirical conclusion follows.

## Executed unbounded-parameter discriminator

The bounded-spectral theorem does not hide a tame all-parameter estimate for the same center-zero inverse. There is an exact counterexample to such an estimate using the actual positive radial source. For the K2531 nonzero nonnegative compact A and repaired P, K2552 proves chi_D>0 throughout [0,R). Fix 0<r0<R and a=min_[0,r0] chi_D>0. Take nu=-z-12K with z>0 in the scalar Einstein factor, so

    w_z=R_2(z)chi_D.

For 0<r<R,

    4alpha+2beta <=2/r,

because alpha<0 and sqrt(K)cot(sqrt(K)r)<1/r. Equivalently w2(r)/r^2 is decreasing. Hence w2(v)/w2(s)>=(v/s)^2 for0<v<=s, and the positive curved Volterra operator dominates the flat three-dimensional radial Volterra operator Tflat. Positivity and iteration, restricted to [0,r0], give

    w_z(r0)>=a sum_(n>=0) z^n r0^(2n+2)/(2n+3)!
            =a/z [sinh(sqrt(z)r0)/(sqrt(z)r0)-1].

The right side grows exponentially in sqrt(z)r0, faster than every power of z. Thus this particular regular-center radial inverse family has no polynomial-in-|nu| bound from radial supremum forcing to radial supremum potential. This is a lower bound on the selected scalar potential w, not a lower bound on the full reconstructed original metric h: derivative reconstruction, other fields and cancellations must be analyzed before such an inference. Nor does it classify alternative boundary inverses or prove that delta_B lacks a response.

The result rules out extending the bounded-family construction by merely asserting a polynomial spectral estimate for these same center-zero maps. The next useful attempt must change the inverse/preparation, prove weighted spectral decay strong enough for these growth constants, exploit a rigorously controlled cancellation in the actual full response, or solve the compact-profile point-source domain directly. No unspecified N-to-infinity convergence remains implicit in the present construction.

## A different inverse repairs one spectral end and encounters a genuine resonance

The exponential lower bound belongs to the zero-center selection. A regular Dirichlet inverse has a different and demonstrably useful behavior for the SAME positive compact radial source. Let A_r=-X with regular center and zero outer value, acting in H=L2([0,R],w2 dr). K2552 constructs its positive closed Dirichlet form and proves A_r>=3/R^2. Its inverse B has the symmetric kernel

    G(r,v)=integral_(max(r,v))^R w2(s)^(-1) ds

relative to measure w2(v)dv. The weight comparison gives 0<G(r,v)<=2/max(r,v) for interior r,v. Consequently

    integral integral G(r,v)^2 w2(r)w2(v) dr dv
       <=2R^4/3 < infinity.

Thus B is compact, self-adjoint and positivity improving. Its largest eigenvalue beta1>0 has a nonnegative eigenfunction: maximizing the Rayleigh quotient and replacing a candidate by its absolute value cannot lower the quotient. Compactness gives a maximizer; the strictly positive kernel then makes it strictly positive in the interior. This yields a regular positive ground state phi1 of A_r with eigenvalue lambda1=1/beta1>=3/R^2. Smooth regular-center behavior follows from the weighted ODE; the outer value is zero. These assertions concern this positive auxiliary radial Hilbert space, not the indefinite physical pairing.

For nu=-12K-z with z>0, the scalar Einstein equation becomes

    -(A_r+z)w=chi_D.

The positive closed form a(w,w)+z||w||^2 is coercive, so the Hilbert-space variational inverse gives a unique regular Dirichlet solution

    w_D=-(A_r+z)^(-1)chi_D,
    ||w_D||_H <= ||chi_D||_H/(lambda1+z)
               <= ||chi_D||_H/(3/R^2+z).

For the smooth radial source this weak solution is the smooth-even classical radial solution. This changes the unbounded negative-nu conclusion: the exponentially growing center-zero potential can be replaced by a decaying operator bound in this explicitly different preparation. The center value is now determined by the outer boundary and is generally nonzero. No claim equates the two selected responses.

The same Dirichlet prescription does not solve every real spectral parameter. At

    nu_res=lambda1-12K>0,

its scalar equation is (lambda1-A_r)w=chi_D. For the actual nonzero nonnegative compact A and repaired P, chi_D>0 in the interior. Pairing with phi1 gives the impossible compatibility condition

    0=<phi1,chi_D>_H>0.

Hence this exact forced scalar problem has no solution in the regular Dirichlet operator domain (or its finite-energy weak domain) at nu_res. Nonzero local B eigen-germs with this parameter remain available by the inherited analytic construction, so the resonant forcing is an admissible member of the fixed-mode family. This is not a failure inferred from a numerical near-resonance.

The conclusion restricts this sufficient scalar-potential construction and its stated radial boundary condition. It is not nonexistence of every full coupled response, a physical spectral exclusion, or an obstruction to the center-zero inverse, which remains entire in nu. Together the two exact results price a concrete next choice: a mixed or parameter-dependent preparation can avoid these particular defects but needs its own uniform bounds and splitter compatibility; a fixed Dirichlet prescription alone cannot be promoted to an unrestricted B-point-source inverse.

Normalize ||phi1||_H=1 and put a1=<phi1,chi_D>_H>0. Every regular Dirichlet solution away from nu_res obeys <phi1,w_nu>_H=a1/(nu-nu_res), hence ||w_nu||_H>=a1/abs(nu-nu_res). The compact positive inverse makes this ground eigenvalue isolated, giving a genuine resolvent pole on a punctured neighborhood. Uniform bounds on a spectral family crossing this parameter therefore fail for this scalar Dirichlet inverse. No full-field cancellation is ruled out.

## Verification and next condition

The exact probe checks the new weight and factorial constants, determinant degree/root-bound data, four scalar-equation signs, center jets, bounded-family identities and overlap poles. It distinguishes reused full intertwinings from new constructions, and rejects missing curvature, source normalization and point-source eigenmode assumptions. The universal Volterra convergence, regular-center extension and distributional passage are the proofs above, not finite sample counts.

The next source question is unrestricted B localization with a justified integrable spectral representation or another direct common domain, while preserving actual compact radial forcing and independently justified preparation. The current exponential parameter bound supplies no such unbounded synthesis. No source or physics ledger verdict changes.

[Actual source reduction](k2552-localized-source-domain-2026-11-04.md),
[finite-radial distributional construction](k2556-distributional-source-response-2026-11-05.md),
[synchronized overlap](k2558-distributional-splitter-overlap-2026-11-05.md),
[probe](../../tests/channel-swings/k2560_compact_source_response_probe.py),
[report](../../lab/process/k2560-compact-source-response.json).
