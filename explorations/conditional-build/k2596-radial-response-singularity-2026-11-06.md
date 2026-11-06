---
title: "K2596 Preparation-invariant radial cusp and finite-mode measure pairing"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed scalar A mode and finite B angular modes; scalar pressure-readable coefficient only, not full B point metric or physical boundary selection
scripts:
  - tests/channel-swings/k2596_radial_response_singularity_probe.py
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
result: K2596
carrier: fixed scalar A eigenmode and finite B angular modes with interior invariant radial measures LAYER=toy CHIRALITY=N/A
pairing: modal scalar form 6(sigma-7K) times integral F dmu dnu; not full tensor two-distribution contraction ON=declared_carrier
real_structure: K2592 real reciprocal repair of the K2588 order/conjugate average
grading: source, TT amplitude, six scalar potentials, original metric and compact detector kept distinct
action_owner: repository-construction -- conditional curved-product completion
target: sharp radial singularity, reciprocal two-measure pairing and regularization error MAP-TYPE=evaluation
```

# The full scalar pressure response has a nonremovable radial cusp

## Result and scope

K2594's full measure-response estimates are conservative all-mode distribution bounds. Here one fixes a scalar A radial eigenvalue X=-sigma and finite B angular modes, and computes the EXACT local singularity of the original-metric scalar coefficient f_h that enters the compact-pressure pairing <t,f_h>. It is continuous and locally Lipschitz, with a nonzero first-derivative jump. Its sharp local auxiliary Sobolev regularity is H^s for s<3/2, and not H^3/2. Every regular homogeneous change of preparation preserves this jump.

On K2592's reciprocal preparation, the continuous modal kernel defines a reciprocal pairing of TWO finite signed radial measures, including coincident atoms. Centered regularization has a nonzero linear self-readout error; symmetry of the mollifier does not improve it to quadratic order. These are useful consequences of the actual full scalar transfer, not claims about arbitrary distributions or the full tensor metric at a B point.

The fixed radial mode is a spectral component, not by itself a compact physical pressure source. The pairing below is a modal scalar pressure-volume form; reconstruction and summation remain separate. Hessian potentials can affect individual tensor components. No physical boundary condition, positivity, causality or native GU prediction is selected. SC-ACT-01 ASSERTS its action, SC-GEO-03 ASSERTS Met(X), SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita; SC-META-53 remains UNCERTAIN. Source, ledger0.263 and canon are unchanged.

## 1. Compute cancellation in the actual original-metric transfer

Use K2592's actual six-row matrix M, first cofactor P=e_f^T adj(M)vsrc, determinant d, K=35 kappa²/3624192 and rE=-1144/(15 kappa). At a fixed scalar mode the full scalar coefficient is

    f_h=[-rE (X+5K)(Y+X+12K)^-1/2 + rE² P(X,Y) Rnew] chi. (1)

K2592 already constructs Rnew with d Rnew=1, changing the old inverse only by homogeneous solutions. The new probe reconstructs M symbolically and computes the actual leading cofactor ratio at kappa=1:

    [Y^4]P / [Y^5]d
       = -67201455 X/9568214656 -140956375/412821988220928. (2)

It does not fit this ratio from a sample. The inherited exact matrix scaling makes its general-kappa coefficient kappa³ times(2) evaluated at X/kappa². Adding the Einstein term in(1), the coefficient of the local second-order inverse is

    C_kappa(X)=[-2842697 X/1045478 -136955 kappa²/946306944]/kappa. (3)

The sole zero at X=-sigma would require sigma/kappa²=73745/1385486784, below3. Every actual scalar radial eigenvalue has sigma>=3kappa². Thus there is NO cancellation of the cusp in this full scalar transfer for any actual mode or nonzero kappa. Using the cofactor alone would give the wrong coefficient.

## 2. Invariant density and exact jump

Keep the Liouville coordinate x distinct from hyperbolic radius t=t(x). K2588 gives

    zeta=sinh²t, J=sinh(t) cosh(t)^(3/2),
    rho(x)=K^(-7/2) J² zeta, a2(x)=-K/zeta,
    rho a2=-K^(-5/2)J².                                  (4)

Here rho dx is the invariant radial density and a2 is the leading coefficient of Y. The invariant atom delta^rho_x0 satisfies integral delta^rho_x0 phi rho dx=phi(x0); it is not an unweighted coordinate-delta forcing.

The determinant inverse's kernel has continuous target jets through eight and ninth jump 1/(Ld a2^5 rho), where Ld=[Y^5]d. Applying P contributes p4 a2^4 times this jump to its FIRST derivative. Lower derivative terms have continuous first derivatives. The second-order Einstein inverse contributes its own 1/(a2 rho) jump. Therefore, with right-minus-left convention,

    j_sigma(x0)=[partial_x F_sigma(x,x0)]_x0
       =C_kappa(-sigma)/(rho(x0)a2(x0))
       =-C_kappa(-sigma)K^(5/2)/J(x0)² !=0.               (5)

Regular one-dimensional ODE theory here is elementary: away from the source the finite-order equation has smooth coefficients and nonzero leading coefficient, and distributional jump matching supplies its finite jets. The difference between two right inverses solves the homogeneous regular tenth-order ODE and is smooth in the target variable. K2592's finite-rank boundary repair is smooth in both variables on an interior compact square: its boundary traces evaluate the old kernel away from its source. Hence it cannot change(5).

Locally, with z=x-x0,

    F_sigma(x,x0)=A+Bz+j_sigma(x0)|z|/2+O(z²).            (6)

The fixed-mode Green construction is jointly smooth on each side of the diagonal up to it, with smooth diagonal jump coefficients. Taylor expansion in both variables therefore gives a uniform quadratic remainder near any interior diagonal point. All branches are smooth. Localize by a smooth cutoff equal1 at the source. The second derivative is j_sigma delta_x0 plus piecewise smooth integrable terms. Their Fourier transform decays at least O(|xi|^-1), so the localized kernel has leading Fourier term j_sigma exp(-i xi x0)/(i xi)² and remainder O(|xi|^-3). The H^s integral converges exactly when 2s-4<-1, namely s<3/2. At equality each high-frequency dyadic shell has a nonzero limiting mass proportional to log2. This proves sharpness, not just an upper loss bound.

## 3. Two finite radial measures on the reciprocal preparation

The Einstein inverse is symmetric in invariant density, and K2592 makes P Rnew=(P R+R P)/2 symmetric. Thus F_sigma(x,y) is real symmetric and continuous, piecewise smooth on the diagonal. On a fixed compact interior square define

    B_sigma(mu,nu)=6(sigma-7K) integral integral F_sigma(x,y) dmu(x)dnu(y). (7)

For any finite signed radial measures, this is well-defined, symmetric, and bounded by

    |B_sigma(mu,nu)| <=6(sigma-7K) sup|F_sigma| ||mu||TV ||nu||TV.

Atoms, coincident atoms and finite sums are included. Weak convergence with uniformly bounded variation preserves this pairing on the compact set, by continuity of the kernel. Finite angular sums preserve the result termwise; no estimate uniform in arbitrarily high angular or A modes is claimed. Equation(7) is NOT an arbitrary distribution-distribution pairing. In particular it does not upgrade K2594 to a full B point self-interaction or define physical energy.

## 4. Execute regularization at the diagonal

Use the centered unit radial measure dmu_epsilon(y)=1_[x0-epsilon,x0+epsilon] dy/(2epsilon), uniform in the Liouville source coordinate y. The width epsilon is measured in that coordinate, not in hyperbolic radius t. Its density RELATIVE to rho(y)dy is 1/(2epsilon rho(y)). Kernel symmetry transfers(6) to the source variable. Centering removes its smooth linear part, while the cusp survives:

    (F_sigma mu_epsilon)(x0)-F_sigma(x0,x0)
       =j_sigma(x0)epsilon/4+O(epsilon²).                 (8)

Two independently regularized atoms give E|U-V|=2epsilon/3, hence

    B_sigma(mu_epsilon,mu_epsilon)-B_sigma(delta_x0,delta_x0)
       =6(sigma-7K)j_sigma(x0)epsilon/3+O(epsilon²).      (9)

The probe integrates these moments exactly. For the independent flat cusp j|x-y|/2 it also computes exact squared local L2 error j²epsilon³/40 and derivative L2 error j²epsilon/6 under uniform smoothing. These fixture rates are not asserted as full tensor or all-mode bounds. For a smooth even unit mollifier, replace1/4 by E|Z|/2 and1/3 by E|Z-Z'|/2. The nonzero coefficient proves genuinely first-order diagonal convergence even for centered smoothing. The finite self-value itself depends on preparation; only the jump and leading singular regularization term are preparation invariant.

## Verification and remaining question

The probe recomputes the actual matrix/cofactor leading ratio and full-metric cancellation, nonzero spectral coefficient, invariant-density jump, exact cusp moments and critical Fourier shell. The regular ODE, compact-kernel measure extension and Fourier asymptotics are written proofs; the flat jump fixture is not represented as the entire curved Green function. Independent field-specialist and distinct integrated hostile reviews returned final substantive findings[].

The next independent question is the old preparation's actual boundary reciprocity defect, or the full tensor/all-angular diagonal behavior. Do not identify a modal scalar cusp with a full point metric. Physical readout and source-native displacement remain separate.

[K2592](k2592-scalar-tensor-boundary-pairing-2026-11-06.md), [K2594](k2594-reciprocal-distributional-response-2026-11-06.md), [K2588](k2588-real-boundary-response-2026-11-05.md), [probe](../../tests/channel-swings/k2596_radial_response_singularity_probe.py), [report](../../lab/process/k2596-radial-response-singularity.json).
