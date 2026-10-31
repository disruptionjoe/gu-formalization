---
title: "K2337 Finite aperture count test with exact all-multipole aliasing"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU, survey or hardware acceptance
scripts:
  - tests/channel-swings/k2337_pixel_beam_count_test_probe.py
---

# K2337 Finite aperture count test with exact all-multipole aliasing

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
result: K2337
carrier: two isotropic real Gaussian angular fields and twelve finite cap-aperture samples per channel LAYER=toy CHIRALITY=N/A
pairing: spherical L2 harmonics and positive Gaussian covariance ON=declared_carrier
real_structure: real coefficients and complex adjoint where required
grading: all angular multipoles; five extracted real quadrupole coordinates
action_owner: repository-construction -- K2331 full compact-band count law with analytically bounded higher angular spectrum, heat beam and cap response
target: finite observation, alias-sign discrimination and identifiability boundary MAP-TYPE=evaluation
```

## Outcome and actual response

The continuous inverse weighting of [K2335](k2335-angular-response-recovery-2026-10-30.md) is replaced by twelve explicit apertures. All higher multipoles remain present. Their covariance aliases into the five outputs with a calculated scalar coefficient, so an isotropic Gaussian tail can preserve the five independent sign pairs even though arbitrary-sky quadrupole recovery is impossible. This supplies a finite conditional observational interface. The follow-through below bounds the actual higher multipoles of the SAME K2331 compact-band model through [K2329](k2329-robust-count-covariance-test-2026-10-30.md), without a second ODE bank computation.

Use real harmonics normalized by integral Y_lm Y_kn=delta_lk delta_mn, and covariance
Cov(a_ilm,a_jkn)=a S_l,ij delta_lk delta_mn, a>=0, with every S_l a positive semidefinite 2x2 matrix. Set S_2=M, the SAME certified full-count matrix in [K2331](k2331-certified-count-window-covariance-2026-10-30.md): 228<M11<273,230<M12<273,231<M22<273. Initially the other S_l are arbitrary supplied isotropic spectra, not values inferred from M; the actual K2331 spectrum is constructed and bounded below. Joint Gaussianity and isotropy are assumptions. Finite L2 second moment suffices below; heat smoothing permits weaker domains if separately justified.

Let phi=(1+sqrt5)/2. The twelve unit directions are cyclic arrangements of (0,+/-1,+/-phi)/sqrt(phi+2). Each aperture averages a spherical cap v·n>=c=1/2 AFTER the heat beam exp(t Delta_S2), t=log(2)/2. These are overlapping 60-degree cap apertures, not disjoint survey pixels. Their harmonic response is

    b_l=2^[-l(l+1)/2] p_l,
    p_l=integral[c,1] P_l(u)du/(1-c),
    y_ij=sum_lm b_l a_ilm Y_lm(v_j)+epsilon_ij.       (1)

Independent centered Gaussian detector errors with variance sigma_i²>0 per aperture, independent between channels and OF THE SKY, are supplied as a reference model. Actual overlap-correlated noise requires the explicit error allowance below; independence does not follow from cap geometry. Calibration, heat width and aperture shape are exact in (1).

SC-ACT-01/GEO-55/COS-50/51/54 ASSERTS and SC-META-53 UNCERTAIN remain unchanged. Ledger0.263 LT-GR2e/GR6b/SM8 is not advanced. Positive-Hilbert probability, this response and higher spectra are imported assumptions, not native GU constructions.

## Exact extraction and every multipole

Write Q_jm=Y_2m(v_j). Direct coordinate moments give sum x²=4, sum x⁴=12/5, sum x²y²=4/5 and all required odd moments zero, hence

    Q^T Q=3 I5/pi, Q^T 1=0,
    T=pi Q^T/(3b2), b2=3/64, T b2 Q=I5.            (2)

The twelve points form six antipodal lines; distinct lines have absolute dot product 1/sqrt5. Odd l cancel under T. For even l, the harmonic addition theorem makes the six-line sample covariance constant on diagonal and off diagonal. Q is orthogonal to constants, so its five columns all receive the same eigenvalue; no unproved group irreducibility is needed. Consequently for K_l=T b_l Y_l,

    K_l K_l^T=k_l I5,
    k_l=(2l+1)/12 [1+(-1)^l]
                [1-P_l(1/sqrt5)] (b_l/b2)².         (3)

Here k0=0,k2=1, all odd k_l=0, and k4=45/4194304>0 (p4=-15/128). Noise covariance is d_i I5, d_i=4096 pi sigma_i²/27. Thus all five real output pairs are independent Gaussian, with the SAME two-channel covariance

    a [M + sum_even l>=4 k_l S_l] + diag(d1,d2).      (4)

All multipoles, including observer monopole/dipole, have been accounted for. No compact radial spectrum is mistaken for angular truncation. The five modes are one sky, not five sky realizations. Provided the cross entry C12 of the bracket in (4) is nonnegative, each discordant-sign event has probability at most1/2 and the predeclared event E that ALL five pairs are discordant has P(E)<=1/32. This tests the supplied family; it does not test a physically unspecified cosmology.

## Executed infinite-tail budget and noise robustness

For s>=0 assume

    sum_l>=4 (2l+1)[1+l(l+1)]^s S_l,ii <= R_i².      (5)

Positivity gives |S_l,12|<=sqrt(S_l,11 S_l,22). Since |p_l|<=1, |P_l|<=1 and b2²=9/4096,

    k_l/( (2l+1)[1+l(l+1)]^s )
       <= 1/(6912*21^s), l>=4.

Cauchy-Schwarz therefore yields |sum k_l S_l,12|<=R1 R2/(6912*21^s). At s=0,R1=R2=1024 this is4096/27<230, so C12>0. This is an explicit all-tail budget, not a finite cutoff or a numerical estimate of an unknown spectrum. A nonempty infinite spectrum is S_l=2^-l I2 for l>=4; its sum(2l+1)2^-l is11/8, within the budget. Anti-correlated spectra are also allowed if (5) holds.

For this robustness extension the ACTUAL extracted law remains jointly Gaussian; covariance control alone does not cover non-Gaussian noise. Let D=diag(d1 I5,d2 I5). If raw detector covariance is D_raw+E_raw with ||D_raw^-1/2 E_raw D_raw^-1/2||<=delta<1, extraction transfers the bound relative to D by coisometry, provided detector noise remains independent of the sky; otherwise the full covariance, including cross terms, must satisfy the corresponding relative bound. A deterministic extracted mean b has beta=||D^-1/2 b||. Comparing the actual law with (4), whose covariance is >=D, reproduces the derived K2335 bound

    P(E)<=1/32+sqrt(5delta²/[4(1-delta)]+beta²/4).     (6)

At delta=1/128,beta=1/64 the level is strictly below1/20. Response errors on RANDOM skies generally modify the full signal covariance and may correlate with it; they cannot be inserted as independent detector noise. Arbitrary quadrupole foreground remains outside the supplied S_2=M law. Actual survey beam/pixel/noise calibration must authenticate these hypotheses.

## Follow-through: the actual count model meets the infinite-tail budget

Keep the SAME K2331 seed P(k)=1 on[1,2], positive normalized windows and initial/evolution equations. Define the actual S_l,ij=16pi² integral_1^2 k² b_i,l(k)b_j,l(k)dk using the ALL-l kernel of K2329(1). These are PSD Gram matrices. They are no longer unspecified replacements for the actual transfer.

Here is a cheap analytic certificate on the whole cone. The algebraic p=(5+sqrt73)/4 satisfies13/4<p<17/5<7/2. Since x*^p=(2/5)(1+p/2)<27/25 and (6400/6241)^13>(27/25)^4, x*<6400/6241 and r*=2(1-1/sqrt(x*))<1/40. Thus1<=x<21/20. The rational inequality (21/20)^7<(5/4)^2 gives x^-p>4/5, hence3/5<=F<17/25. The background equations give

    5/7<a<1, |H|<1/2, |u|<4, 6<d<10,
    |V'|<30, |V''|<55, q=k²/a²<8, |beta|<1/2.      (7)

For explicit bounds, H's numerator lies between-1/10 and4/25, x^(3/2)<11/10 and F^(-3/2)<9/4. Also |u|<(5/4)(2/5)(7/2)(9/4)<4 and |V|<15. In K2305's potential derivatives,0<nu<1/7 gives2<b_pot<129/56<7/3 and0<c_pot<425/448<1; therefore |V'|<(5/6)(7/3)15<30 and |V''|<(2/3)(49/9)15<55. The remaining statements in(7) are direct rational substitutions.

For weighted coordinates (Phi,chi,pi/10,v), the ACTUAL K2331 J matrix has absolute row sums bounded by(15/2,10,659/20,7/2). The third is bounded by

    (8+60+10+16)/10 +(8+55+32+3+15)/10
       +(3/2+2)+(80+15/2)/10 =659/20 <33.

As y_z=r*aJy and the initial weighted norm is<=1, Gronwall gives weighted norm<exp(33/40)<e<3. Hence |Phi|,|chi|,|v|<3 and |pi|<30. Direct reconstruction then yields |nJ|<69, |PhiJ|,|PsiJ|<5, |dotPsiJ|<38, |W|<6, |dotW|<46, and0<A<2/r. For example |nJ|<[(32)3+(6+30+5)3+15(3)+4(30)]/6+9/2=137/2<69. The full K2329 source kernel therefore obeys

    |g_l| <= (122+10/r)|j_l(kr)|+17|j_l''(kr)|
          +(17/r)|j_l'(kr)|
          +integral_0^r [104/r+6l(l+1)/s]|j_l(ks)|ds.  (8)

This includes both source and foreground contributions down to the observer. For l>=4,0<=z<=1/20 and d=0,1,2, the entire Bessel series gives

    |j_l^(d)(z)| <= 2(l)_d z^(l-d)/(2l+1)!!.

Indeed successive undifferentiated absolute terms have ratio z²/[2(m+1)(2l+2m+3)]. Differentiation multiplies this ratio by at most5/2 (the worst d2 case occurs at l+2m=4), making every ratio<=1/3520. Twice the first term safely bounds the full series, including its continuous zero-argument limit. Substitution in(8) bounds |g_l| by

    2(2r)^(l-2)/(2l+1)!! times
    [17l(l+1)+40r+488r²+416r²/(l+1)+24r²(l+1)].

For r<=1/40,l>=4 the bracket is <20l(l+1): its extra terms are bounded by2+3(l+1)/200<3l(l+1). Positive normalized windows yield

    |b_i,l(k)| <= q_l=40l(l+1)20^(2-l)/(2l+1)!!,
    q4=2/945, q_(l+1)/q_l=(l+2)/[20l(2l+3)]<1/100.

Since (2l+3)/(2l+1)<=11/9<2,

    sum_l>=4(2l+1)q_l² <=9(2/945)² 5000/4999 <1/20000.

Finally16pi² integral_1^2 k²dk<400 (pi<22/7 suffices), so for BOTH actual channels

    sum_l>=4(2l+1)S_l,ii <1/50,
    |sum_even l>=4 k_l S_l,12| <1/345600,
    C12>230-1/345600>0.                                 (9)

Thus the SAME actual compact-band count law meets(5), and(4)-(6) give its finite-aperture sign test including every higher multipole. The actual tail is small because the supplied radial/spectral domain has kr<1/20; this is an estimate, NOT an angular truncation. K2331's existing quadrupole interval certificate is reused by dependency; no new interval ODE run is asserted. The new tail bound is analytic with exact rational controls. A different physical spectrum or tracer need not obey these constants.

## Negative successor: aliasing defeats unrestricted recovery and sign claims

The displayed fourth-degree moments also imply 1^T Y4=0, so every l4 sample lies in the antipodally even zero-sum sample subspace. For l4, that subspace is exactly the five-dimensional range of Q. Since K4 K4^T=k4 I and k4>0, for any quadrupole x choose a fourth-multipole coefficient vector h4=-K4^T x/k4. Then T(b2 Q x+b4 Y4 h4)=0. Both summands lie in that same sample subspace, and T is injective on it; therefore their RAW twelve observations cancel. Nonzero quadrupoles can be hidden using only l4. Heat smoothing and full-sky aperture coverage do not create arbitrary-sky identifiability. This is distinct from the open-zero-mask obstruction of K2335.

The statistical test also needs its tail sign condition. Choose S4=L[[1,-1],[-1,1]], L=10^8, all other higher spectra zero, a=1 and d1=d2=1. Let A=k4 L. Since A>820, certified M bounds give rho<(273-A)/(274+A)<-1/2. Each discordance probability is >2/3, so P(E)>(2/3)^5=32/243>1/20. This is a genuine PSD high-mode contamination example; it violates (5) and does not refute the budgeted theorem. A full angular spectrum must be bounded or integrated before the quadrupole-only test is exported.

## Verification and next construction

The probe independently checks vertex moments, the actual spherical addition kernels for several degrees, aperture multipliers, noise normalization, exact budget/margin and contaminated-sign inequalities. Faults alter samples, response, spectrum or noise before applying the fixed checks. Universal all-l and Gaussian claims use the written derivation, not sampled harmonics. [Delsarte, Goethals and Seidel, Spherical codes and designs](https://www.math.unipd.it/~alvise/PHD_2024/LEZIONI/SPHERE/PDF/DELSARTE%20Spherical%20codes%20and%20designs.pdf) is established design context; no novelty is claimed for cubature.

The actual K2331 compact-band tail is now bounded. Next replace its supplied spectrum/tracer by a physically justified family and include measured response, correlated shot noise and calibration in(4)-(6). This finite mathematical interface does not authenticate those physical inputs. Repeating ideal response inversion or the completed compact-band tail estimate cannot supply them.
