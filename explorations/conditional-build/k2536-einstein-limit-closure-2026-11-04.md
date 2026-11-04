---
title: "K2536 Compact-interval Einstein closure of the sourced family"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: analytic compact-interval closure for one well-prepared positive-parameter family; no empirical or native GU claim
scripts:
  - tests/channel-swings/k2536_einstein_limit_closure_probe.py
---

# K2536 A family-level boundary on background discrimination

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
result: K2536
carrier: supplied four-dimensional flat FLRW sourced quadratic metric action on fixed finite redshift interval LAYER=toy CHIRALITY=N/A
pairing: real scalar ODE energy and common finite positive-definite observation covariance ON=declared_carrier
real_structure: positive real a and x, fixed Omega in (0,1)
grading: exact finite-a solutions, uniform limiting history, derivatives and physical prediction are distinct
action_owner: repository-construction -- K2534 sourced quadratic comparator with dust and no radiation
target: uniform Einstein-history closure and joint background-observable consequence MAP-TYPE=evaluation
```

## Result and source boundary

For every fixed finite redshift interval, the sourced family in [K2534](k2534-calibrated-family-refit-2026-11-04.md) contains positive-branch solutions converging uniformly to the flat dust-plus-Lambda expansion history at fixed Omega. The error is O(1/a) in the history variable and O(1/sqrt(a)) in its first derivative. Thus no fixed positive separation from that reference can hold for all this family using continuous background distances and finite drift measurements alone. Exact equality at finite a is still false. This supplies the uniform argument that the earlier three numerical samples did not establish.

SC-COS-50 ASSERTS its conditional variable-dark-energy demand; SC-COS-51 ASSERTS the displacement/VEV claim; SC-COS-54 ASSERTS the stated two-movable-fields claim. They do not supply this quadratic metric action, dust normalization or observation/stellar model. LT-GR2e and ledger0.263 remain unchanged. This is not a GU prediction or source falsification. The path varies rho and dimensional dust normalization with a while keeping the action-normalized Omega fixed; it does not prove convergence with all dimensional sources fixed.

## 1. Exact original-equation split

Use s=3log(1+z), t=exp(s), x=U/U0, y=x', a=alpha/U0^(4/3), b=rho/U0^(8/3). Fix 0<Omega<1 and

    x(0)=1, y(0)=3Omega/4,
    b=6a(1-Omega)+b0,
    b0=-(81/2)Omega²-72(1-3Omega/4)Omega.

K2534's original reduced equation is

    x''=x'-a/(36x^(1/3))
        +[b+6(a+12(1-3Omega/4))Omega exp(s)]/(216x^(5/3)).

Set L=1-Omega+Omega exp(s), r=L^(3/4), u=x-r, and

    f(s,u)=[(r+u)^(-1/3)-L(r+u)^(-5/3)]/36,
    g(s)=b0/216+(1-3Omega/4)Omega exp(s)/3,
    h(s,u)=r'-r''+g(s)(r+u)^(-5/3).

Then exactly u''-u'+a f(s,u)=h(s,u), with u(0)=u'(0)=0. Here f(s,0)=0 and

    f_u=[5L-(r+u)^(4/3)]/[108(r+u)^(8/3)],
    h0(s)=h(s,0)
         =(exp(s)-1)Omega[1/3+Omega(3exp(s)-1)/16]L^(-5/4).

For s>0, h0>0: u identically zero is not a finite-a solution. At s=0 h0=0, which is precisely the second-jet match, not an exact-history identity.

## 2. Uniform nonlinear energy proof

Fix S>0. On the compact tube 0<=s<=S, |u|<=1/2, x>=1/2 and x/r belongs to[1/2,3/2]. Therefore f_u has a strictly positive minimum m independent of a: 5-(3/2)^(4/3)>0. Define finite nonnegative constants on that tube

    k=sup |f_su|, d=sup |h_u|,
    H=sup |h0|, J=sup |h0'|,
    K=H²/m+1, C=3+d(1+2/m)+2k/m.

The s derivative in f_su holds u fixed. Since f(s,0)=0, also f_s(s,0)=0. With V(s,u)=integral_0^u f(s,v)dv, both signs of u satisfy V>=m u²/2 and |V_s|<=k u²/2. Use the modulated energy

    E= u'²/2+a V-h0 u+K/a.

Completing a square gives

    E >= u'²/2+a m u²/4+1/a.

Differentiating along the ORIGINAL equation cancels a f u':

    E'=u'²+(h-h0)u'+a V_s-h0'u.

The estimates |h-h0|<=d|u|, |u|²<=4E/(am), |u'|²<=2E and
J|u|<=am u²/4+J²/(am) imply, for a>=1,

    E' <= C E+J²/(am).

Since E(0)=K/a, integration gives E<=B/a, where

    B=K exp(CS)+[J²/(mC)](exp(CS)-1).

Consequently, with D=2sqrt(B/m),

    sup |x-r| <= D/a,
    sup |x'-r'| <= sqrt(2B/a).

Taking a>2D closes the first-exit argument strictly inside |u|<1/2. The smooth ODE extends throughout[0,S]: x stays bounded away from zero and x' is bounded, excluding every finite-time continuation obstruction there. This proves the estimate for actual solutions, not only a conditional tube trajectory. All constants depend on S and Omega, never a. They are deliberately conservative; no practical certified alpha threshold or optimal rate constant is claimed.

For sufficiently large a, b>0 and

    F/U0^(4/3)=a+12x^(1/3)(x-x')>0,

because x and x' are uniformly bounded. Thus the path is inside the positive rho,F branch for the entire interval, not a formal approximation outside the admitted family. U0>0 is fixed; alpha=a U0^(4/3), rho=b U0^(8/3).

## 3. Execute the common observation consumer

H/H0=E_H=x^(2/3), and the reference is sqrt(L). On x>=1/2, the mean-value theorem gives

    |E_H-sqrt(L)| <= 2^(4/3) D/(3a),
    |1/E_H-1/sqrt(L)| <= 2^(8/3) D/(3a).

Hence chi(z)=integral_0^z dz'/E_H converges uniformly with error at most z times the second bound. At a fixed common H0 and ruler, luminosity/angular distances and H(z) converge. At finitely many positive-redshift nodes their logarithmic distance moduli also converge. Proper-time drift H0-H(z)/(1+z) converges at the SAME H0; a forecast mean at H0=70 is not automatically the calibrated limiting H0.

For any fixed admissible common nuisance tuple theta=(M,H0,r_d) and fixed finite positive-definite covariance, the joint calibrated SN+BAO loss J_a(theta) converges to J_LCDM(theta). Calibrator rows retain precedence and shared nuisances; no duplicate SH0ES prior or independent row repair is introduced. It follows without any optimizer-continuity assumption that

    inf_(quadratic family,theta) J <= inf_theta J_LCDM.

The inequality concerns this family at the same Omega and supplied likelihood assumptions. It does not claim attainment, a located global minimum, or a numerical best-fit value. Under K2534's explicit full-rank SN design, nonzero BAO design, and strictly positive limiting profiled BAO amplitude, its analytic nuisance minimizers and profiled losses converge as well. All these consumers use one sequence of histories, so they are joint rather than separately repaired fits.

An absolute observational rejection remains possible if the limiting calibrated LCDM realization itself fits the data badly, if finite parameter bounds exclude the sequence, or if independent physical requirements constrain it. The theorem rules out a uniform positive BACKGROUND separation from an admitted limiting realization; it does not prove agreement with data, growth/slip, local gravity or a full perturbation theory. Derivative-dependent tests require their own uniform bounds.

## 4. Oscillatory and initial-data countercontrols

The C0/C1 proof does not control x''. This has a concrete nonlinear boundary-case control. At Omega=0, b=6a, set epsilon=a^(-1/2), x(0)=1, x'(0)=c epsilon with c!=0. This is a near-prepared family, NOT the exactly matched Omega=.3 seed above. Write tau=s/epsilon and x=1+epsilon²w(tau). Its exact equation is

    w''=epsilon w'+[(1+epsilon²w)^(-5/3)
                   -(1+epsilon²w)^(-1/3)]/(36epsilon²),
    w(0)=0, w'(0)=c.

The smooth extended epsilon=0 equation is w''=-w/27. Finite-time continuous dependence in tau gives w tending in C2 to c sqrt(27)sin(tau/sqrt(27)). At tau*=pi sqrt(27)/2,

    x''(epsilon tau*) -> -c/sqrt(27),

while the same energy estimate, with E(0)=(K+c²/2)/a, still yields the whole fixed-s C0/C1 convergence. Thus those rates alone cannot imply C2 convergence even for nearby data. This is not evidence that the exactly jet-matched seed lacks a stronger estimate.

The exact linearized mode exp(s/2)sin(omega s)/omega, omega²=a/27-1/4, independently checks the sign and fast frequency. Negative a reverses the restoring sign and creates a growing root of order sqrt(|a|); this proof does not apply there. An a-independent initial displacement also plainly prevents uniform convergence at s=0. Infinite-redshift uniformity and arbitrary initial-data attraction are not claimed.

## Evidence, prior art and next question

The written nonlinear energy and bootstrap argument proves the continuum statement. The probe verifies original-force, residual, coercivity, completed-square and Gronwall identities plus exact shared-nuisance and contrary fixtures; its Boolean count is not the theorem. Independent review must assess the proof and applicability. No numerical bank is needed.

The Einstein limit of metric f(R) is established research territory: [Olmo, Phys.Rev.D75,023511 (2007)](https://arxiv.org/abs/gr-qc/0612047) discusses its scalar-tensor representation and source response. That work is not a substitute for this explicit dust initial-value estimate; no novelty claim is made here.

This closes the proposed uniform background-gap route for the stated unbounded positive family. A meaningful successor must impose an independently justified finite parameter/initial-data constraint or test a distinct perturbation, source/readout or high-derivative observable with its own uniform control. Repeating finite background fits or three sampled large-a points cannot restore the excluded separation premise.
