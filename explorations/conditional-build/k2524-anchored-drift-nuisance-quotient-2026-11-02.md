---
title: "K2524 Anchored drift: affine calibration, exact repair and remaining ambiguity"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional measurement mathematics; no native GU or empirical certification
scripts:
  - tests/channel-swings/k2524_anchored_drift_nuisance_quotient_probe.py
---

# K2524 Anchored drift nuisance quotient

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
result: K2524
carrier: same-source rest-line wavelengths and positive homogeneous FLRW expansion on one reference lightcone LAYER=toy CHIRALITY=N/A
pairing: proper-time wavelength rates, one shared absolute reduced distance and joint error covariance ON=declared_carrier
real_structure: real positive expansion; effective calibration parameter may have either sign
grading: cosmic drift, instrument drift, absolute ruler and reconstruction uncertainty are distinct
action_owner: repository-construction -- inherited K2367 sourced quadratic metric comparator only
target: actual affine spectrograph nuisance removal and common-anchor weak-test input MAP-TYPE=evaluation
```

## Result and scope

[K2522](k2522-redshift-drift-interface-2026-11-02.md) supplied a real drift-to-expansion map but bounded calibration errors separately. Here the common wavelength-scale error cancels EXACTLY in its nonlinear anchored reconstruction. A wavelength-offset drift does not cancel. We construct two histories with the same single-line drift and one absolute distance, one outside the entire inherited action family and the other inside its vacuum subset. Two distinct lines from the same comoving source remove that particular ambiguity, with an explicit noise cost. Finite residual-shape bounds and a covariance projection then supply the actual existing weak test.

SC-COS-50/51/54 ASSERTS retain their source polarity; LT-GR2e and ledger0.263 remain unchanged. No dataset, sensitivity claim, empirical exclusion, native connection-distortion bridge, or novelty certification is supplied. Peculiar acceleration and nonlinear wavelength errors remain real inputs. [Loeb's original drift proposal](https://arxiv.org/abs/astro-ph/9802122) is prior art for the cosmic drift relation; [the ACCELERATION analysis](https://academic.oup.com/mnras/article/492/2/2044/5672637) discusses instrument and barycentric calibration. The exact affine nuisance class below is a declared model, not a claim that it exhausts an actual instrument's errors.

## 1. Derive the instrument operator before projecting errors

Let x=1+z, cosmic drift g=x H0-H(z), and lambda_i>0 be stable rest wavelengths of lines from the SAME comoving source. Use a correctly calibrated reference epoch t0, fixed observer proper-time units, and instantaneous local instrument law

    lambda_obs(t)=A(t)lambda_true(t)+B(t),
    A(t0)=1, B(t0)=0, A'(t0)=b1, B'(t0)=b0.

Since lambda_true=lambda_i x, the observed drift of line i is

    m_i = g + b1 x + b0/lambda_i.                    (1)

This is a differentiated wavelength map, not an arbitrary nuisance matrix. Reference redshift-label error, clock-scale error, source acceleration and finite-baseline remainder require their own bounds. K2522's Taylor bounds remain applicable to the measured source track when their derivative assumptions hold. The identities here concern its instantaneous rate, not a finite-difference approximation with no remainder.

For a continuous measured function G, an absolute reduced distance C>0 to z=a>0 defines p by

    integral_0^a dz/[x p-G(z)] = C,  Hhat=x p-G>0.   (2)

The admissible domain is POSITIVE DENOMINATOR, not p>0 and not G(0)=0. The latter conditions belonged to uncorrupted cosmic drift. Strict decrease in p gives uniqueness on its domain when a root exists; no unconditional existence is asserted. Under G→G+b x, p→p+b solves the identical equation and leaves Hhat unchanged. The effective p need not equal physical H0; the reconstruction gives Hhat(0)=p-G(0). With the absolute anchor unchanged (or its correlated error retained explicitly as c below), common multiplicative wavelength drift is therefore an exact null direction of the reconstructed expansion, even nonlinearly. Treating its amplitude as an independent H0 error double-counts a nuisance that cancels here.

## 2. A one-line error can hide action membership

Take the exact K2522 window a=11/25, C=log(1+a), in fixed H* units. Coasting H_c=x has g_c=0 and this distance. K2520 already proves this history fails its sourced weak equation for EVERY common constant alpha,rho,q0; that result is reused, not reproved as a new theorem.

Now take de Sitter H_d=K=a/log(1+a)>0. Its true H0=K, g_d=K z, and distance a/K=C. It solves the inherited equation

    U_ss-U_s+alpha/(36 U^(1/3))
                -(rho+2q0 exp(s))/(216 U^(5/3))=0

with U=K^(3/2), q0=0, rho=6 alpha K^2. For the inherited f(R)=alpha R+R²/2-rho, R=12K² and F=alpha+R, this also gives FR-2f=0 and 3F K²=(FR-f)/2. Thus the full homogeneous vacuum metric equations hold, not just the necessary weak equation. Taking alpha>0 gives F>0, without claiming quantum stability. This is the VACUUM SUBSET with freely selected shared coefficients, not K2367's fixed fitted dust model. Set b1=-K and b0=K lambda_1. Equation(1) yields m_1=0 for every z. Thus the whole single-line drift function plus the same absolute anchor cannot distinguish these two histories in the declared nuisance class. Ignoring the affine nuisance could falsely exclude a member of the action family.

The ambiguity also has an exact finite-time realization. In de Sitter, a fixed comoving source obeys x(t)=1+z0 exp(Kt) about t0=0. Choose A(t)=exp(-Kt), B(t)=lambda_1[1-exp(-Kt)]. Then A(t)lambda_1 x(t)+B(t)=lambda_1(1+z0) is constant for all t in the model, with A(0)=1,B(0)=0. Thus the first line has zero measured drift even over a finite baseline; this negative witness does not rely on an uncontrolled derivative approximation. The anchor is matched at the reference epoch, not asserted constant over observation time.

No small or physically achieved instrument-error amplitude is alleged. A separately justified tight bound may exclude the counterfamily. Additional exact distances also need not agree: for b in (0,a), log(1+b)/b is strictly decreasing, so log(1+b) > b log(1+a)/a. A second absolute anchor at b separates this particular pair. This is a constructive repair of this pair, not universal identification of arbitrary histories from two anchors.

## 3. Two rest lines remove the offset, with a price

For lambda_1 != lambda_2 define

    G=(lambda_1 m_1-lambda_2 m_2)/(lambda_1-lambda_2)
      =g+b1 x.                                    (3)

The b0 term cancels and equation(2) removes b1. This reconstructs H exactly whenever the common instantaneous affine model, same-source line motion, continuous function and absolute anchor assumptions hold. In the counterfamily, G=-K, the valid root is p=0 and Hhat=K. An erroneous positivity restriction on p would reject the correct reconstruction.

With rate errors epsilon_i and covariance Sigma on their joint measurements, the two-line weights w=(lambda_1,-lambda_2)/(lambda_1-lambda_2) give

    e=w epsilon,  Var(e)=w Sigma w^T.               (4)

Keep cross-redshift/time covariance as well. Closely spaced lines amplify error. For lambda=(1,2) the weights are(-1,2), with variance5 sigma^2 for independent equal errors; perfectly common equal rate errors instead yield sigma^2. Neither is a measured noise model. Physical source acceleration common to all lines survives (3); it is not a wavelength-offset error.

For N lines with positive-definite Sigma, minimize w^T Sigma w subject to sum w_i=1 and sum w_i/lambda_i=0. Put D=[1,1/lambda], c=(1,0)^T. If D has rank2,

    w=Sigma^-1 D(D^T Sigma^-1 D)^-1 c,
    variance=c^T(D^T Sigma^-1 D)^-1 c.              (5)

The constrained quadratic decomposition proves optimality. Degenerate covariance requires separate support treatment; all-equal wavelengths have rank1, whereas at least two distinct values give rank2. This is standard constrained least squares, used on the derived instrument operator. It adds a practical design choice without inventing line availability or a survey.

## 4. Exact finite error depends on shape, not common offset

Let true H=x H0-g>0, reconstructed Hhat=x p-(g+e)>0, and measured anchor C+c. Define delta p=p-H0 and

    J=integral x/(H Hhat) dz,
    <f>_w=J^-1 integral x f/(H Hhat) dz.

Subtract the two anchor integrals exactly:

    delta p = <e/x>_w-c/J,
    Hhat-H = x[<e/x>_w-e/x-c/J].                   (6)

For e/x=b+r(z), the b term disappears. Hence, with all ranges on [0,a],

    |Hhat-H|(z) <= x[osc(r)+|c|/J].                (7)

No linearization or independent-error assumption enters (6)-(7). If H,Hhat<=B(z), J>=Jmin=integral x/B(z)^2 dz. This is a conditional bound requiring an independently justified positive envelope/root; it cannot bootstrap its own unverified envelope. A constant residual is harmless with an exact anchor; an arbitrary redshift-dependent residual is not. The one-sided convex-hull bound can improve the global oscillation bound at a specific z.

For the actual K2522 coasting window, an established H,Hhat in [1/2,2] gives Jmin=((36/25)^2-1)/8. Its existing sufficient h-error threshold eta*=3.30264588738e-10 (exact rational in the inherited report) can be used by requiring

    (36/25)[osc(r)+|c|/Jmin] <= eta*.               (8)

For example the allocated inequalities osc(r)<=eta*/[2(36/25)] and |c|<=Jmin eta*/[2(36/25)] guarantee its half-margin. This is a sufficient conditional requirement, not achievable precision or an optimal design. It replaces the old independent delta_H0 plus delta_g pricing with a same-realization bound; the inherited weak test still excludes every shared coefficient only when ALL allowed histories meet the band.

## 5. Released covariance map and remaining non-identifiability

At a positive nominal H, let J0=integral x/H^2. The derivative of (6) is

    delta H(z)=x/J0 integral e(u)/H(u)^2 du-e(z)-x c/J0.  (9)

Compose this operator with the two-line map BEFORE propagating the joint covariance of line errors and the distance anchor. Include their cross-covariance. The operator annihilates e=b x,c=0. A finite quadrature control with nodes x_i and positive weights omega_i has a_j=omega_j/H_j^2/J0, P=x a^T-I and P x=0. Its covariance is [P,-x/J0] Sigma_joint [P,-x/J0]^T. The finite fixture verifies this algebra; continuum coverage needs controlled quadrature/regularity and no finite Gaussian covariance alone supplies a uniform band. Higher-order error is governed by (6), not silently neglected.

Even perfectly repaired instrument drift does not settle arbitrary physical nuisance. For any two positive smooth histories H1,H2 with the same anchor, an unconstrained common rate error e=g1-g2 makes their observed cosmic-plus-error drift identical. An acceleration model or other independent information is therefore required; the affine instrument repair is not a universal cosmological identification theorem. The next physical input is a justified line/anchor joint error model, finite-baseline and interpolation control, and residual acceleration shape; the strongest alternative remains an independently accessible observation configuration. Native action, ledger and empirical credit stay unchanged.

## 6. Executed follow-through: polynomial distortion and minimal line count

The affine repair suggests its own strongest contrary test. At a correctly calibrated reference epoch, permit wavelength-rate distortion F(lambda)=sum_(r=0)^d a_r lambda^r with d>=1. Multiplying each rate by its rest wavelength gives

    y_i=lambda_i m_i=lambda_i g+F(x lambda_i).

This is a degree-d polynomial in lambda_i; its linear coefficient is g+a1 x. For d+1 distinct positive rest wavelengths, let L_i(lambda) be their Lagrange basis polynomials. Then

    G=sum_i w_i m_i,  w_i=lambda_i L_i'(0),
    sum_i w_i lambda_i^(r-1)=1 if r=1, else0, 0<=r<=d.  (10)

Interpolation proves exact recovery of the sole anchor-null coefficient. This is a polynomial instrumental class, not a finite reconstruction of arbitrary cosmic g(z) from redshift samples. Same-source lines are required at each redshift and the anchor still needs continuous-band control.

The count is sharp for unrestricted degree-d distortion and these same-source samples: with n<=d distinct positive wavelengths, P(lambda)=product_i(lambda-lambda_i) has degree<=d, vanishes at every sampled wavelength, and P'(0)=-P(0) sum_i(1/lambda_i) !=0. Adding P changes the desired linear coefficient without changing the samples. This is a pointwise coefficient-identification lower bound, not a global no-go exploiting all cross-source observations under a shared calibration law.

A quadratic wavelength drift is a concrete failure of the two-line repair: it leaves a2 x^2(lambda_1+lambda_2), which divided by x is not constant. Three wavelengths(1,2,3) have weights(-5/2,8,-9/2), canceling constant and quadratic distortions and preserving the linear coefficient. For independent equal line-rate noise their variance multiplier is181/2, versus5 for the affine two-line example. Extra lines, actual covariance and constrained least squares may reduce this cost. These dimensionless wavelength ratios illustrate conditioning, not a recommendation for available transitions.

For a distortion remainder R(lambda), the surviving drift error is sum_i w_i R(x lambda_i)/lambda_i. A justified |R(x lambda_i)|<=r_i gives the explicit bound sum_i |w_i| r_i/lambda_i; combine its variation divided by x with(7), not merely with an uncorrelated sum. Same-source astrophysical line shifts, blend errors, reference wavelength uncertainties and missing continuous-redshift coverage remain independent limitations. This released construction supplies the required instrumental specification; data or externally justified residual bounds are still needed for any physical test.
