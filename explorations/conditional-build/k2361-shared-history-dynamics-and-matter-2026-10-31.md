---
title: "K2361 Shared-history scalar dynamics and matter rigidity"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematical and numerical results; no native GU or hardware certification
scripts:
  - tests/channel-swings/k2361_shared_history_dynamics_and_matter_probe.py
---

# K2361 Shared-history scalar dynamics and matter rigidity

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
result: K2361
carrier: positive-F real quadratic metric cosmology LAYER=toy CHIRALITY=N/A
pairing: canonical Einstein scalar action ON=declared_carrier
real_structure: real metric histories, real coefficients and real scalar perturbations
grading: metric background, constrained scalar perturbation and material source are distinct
action_owner: repository-construction -- quadratic metric f(R), not native connection distortion
target: same-history dynamics and matter continuation MAP-TYPE=evaluation
```

## Result and scope

The shared Pantheon+/DESI vacuum witness of [K2358](k2358-shared-history-supernova-test-2026-10-31.md) has a positive present constrained scalar mass, unlike the earlier BAO-only witness. The companion numerically evolves the regular constrained scalar on this SAME history, with common coefficients and explicit initial-state norm. It also proves a stronger matter-completion restriction: no regular vacuum history of this quadratic class can remain exactly the same history after nonzero conserved dust/radiation is added, even by retuning its two constant lower-order coefficients. A new matter background and new likelihood calculation are required. Neither this continuous-history theorem nor the numerical transfer excludes a fit at finitely many observed distances.

SC-COS-50/51/54 ASSERTS remain source facts. LT-GR2e and ledger0.263 do not change. The observed-side demand is that one history describe distance AND dynamics with physical matter; the scalar metric comparator is not the source's ad-valued connection distortion. No native prediction, population robustness, confidence level, nonlinear stability or empirical exclusion is claimed.

## 1. Reuse before calculation

K2291 already derived the constrained flat-gauge scalar mass, K2292 the dust/radiation background equations, K2294 the high-frequency transfer bound, and K2265/66 the ruler/scale degeneracy. Those are prerequisites, not new results here. The new object is K2358's joint witness (alpha,rho,U0,p0)=(55.85236076,929.86045772,2,.4885325972) in H_* units, b=-1. For s=3log(1+z),

    U_s=p, p_s=p-alpha/(36 U^(1/3))+rho/(216 U^(5/3)),
    h=U^(2/3), F=12 U^(1/3)(U-p)+alpha, beta=-3F_s/F.

F is dimensionless F_phys/H_*². Let D=alpha²+2rho, j=beta/(beta+2),

    x=dotphi/(M H_E)=sqrt(6)j,
    y=V_phi/(M H_E²)=(alpha-D/F)/(sqrt(6)h²(1+beta/2)²),
    w=V_phiphi/H_E²=(-alpha+2D/F)/(3h²(1+beta/2)²),
    m=mu_Q²/H_E²=w+2xy+3x²-x^4/2.

At z=0, F≈78.7043159242, beta≈.0008670164291, and m≈9.3387633286. The older K2291 negative mass belongs to different fitted coefficients. K2283 proves global U>0. Positive F along this new path is numerically supported, not interval-certified: its integrating-factor theorem would promote a certified positive endpoint to whole-path F>0, but no endpoint enclosure is claimed here. Conditional on F>0, the vacuum identity and positive initial H+dotF/(2F) ensure H_E>0. The new path crosses dotphi=0 close to today. Q=delta phi+(dotphi/H_E)psi stays regular; dividing by dotphi to use comoving curvature there would fail.

## 2. Actual finite-interval transfer

Choose Fref=F(0), a_E=exp(-s/3)sqrt(F/Fref), and dimensionless kbar=k/H_*. Fix a_J(0)=1. N=log a_E, ell=ds/dN=-6/(beta+2), epsilon=3j², and P=dQ/dN. The exact vacuum scalar system is

    d/ds [Q,P] = (1/ell) [[0,1],[-(K²+m),-(3-epsilon)]] [Q,P],
    K²=kbar² exp(2s/3)/(h²(1+beta/2)²).

Integrate from z=2.33 to today, with identity initial transfer matrix. The stored report gives matrices and singular values for kbar=.1,1,10; kbar=0 is a long-wavelength consistency control. The reported Euclidean norm is that of (Q,P), not canonical energy, a primordial spectrum, a gauge-invariant density-growth amplitude or an observed likelihood. Large/small singular values alone do not decide physical stability. DOP853 and RK45 with tighter tolerances are independent numerical convergence checks. The exact adiabatic solution Q proportional to x(s) supplies an independent k=0 solution check, without division by x at its zero. Liouville's determinant formula checks the friction integral. Sampled mass extrema are explicitly samples, never a whole-interval positivity proof.

Changing m to potential curvature alone changes the propagated matrix. The full lapse/shift constraint term matters even when both masses are positive. A matter model cannot simply reuse this single vacuum scalar: fluid perturbations introduce additional dynamical/source variables.

## 3. Exact no-retuning matter theorem

Let x=1+z on an open interval, y=H²>0, R=12y-3xy', and f=alpha R+R²/2-rho. Define

    Q[y]=R²/4-3yR+3xyR'.

The full00 equation is -Q+3alpha y-rho/2=q_d x³+q_r x⁴, where q_d,q_r are fixed conserved-source amplitudes in the chosen normalization. No trace-only replacement is used. Suppose y solves a vacuum equation with constants alpha0,rho0 and also the sourced equation with alpha1,rho1. Subtract:

    3(alpha1-alpha0)y-(rho1-rho0)/2=q_d x³+q_r x⁴.

If Delta alpha=0, polynomial independence forces q_d=q_r=0. Otherwise y=c0+c3x³+c4x⁴. Direct substitution gives

    Q=(81/4)c3²x^6+18c3c4x^7-36c0c4x^4.

The old vacuum equation's x^6 coefficient forces c3=0 (real coefficients). If c4 is nonzero, its x^4 coefficient forces c0=-alpha0/12; the constant equation forces rho0=-alpha0²/2. Consequently R=12c0=-alpha0 and F0=alpha0+R=0 identically, outside the regular positive-F hypothesis. If c4=0 then y is constant and the subtracted equation again has no nonzero dust/radiation amplitude. Thus no such common regular history exists. Signed q are covered as well; positivity is not needed for this algebraic obstruction.

The degenerate control F0=0 really allows the polynomial radiation branch, so its exclusion is essential. Allowing a changed R² coefficient does not repair the result when the old coefficient is nonzero: subtract a suitable constant multiple of the old equation to eliminate Q, recovering the same constant-span condition. Overall distance/ruler rescaling first scales the old vacuum coefficients and leaves this argument intact. Arbitrary evolving source, nonminimal coupling, changed action functional, approximate history equality or finitely many distances are outside the theorem.

## 4. Matter follow-through and perturbation boundary

Reuse K2292 for the new matter flow instead of adding dust to a frozen vacuum curve. A second explicit consequence concerns tensor propagation. For a minimally coupled conserved perfect fluid with zero tensor anisotropic stress, a_J the Jordan scale factor and v=dotF/F,

    q_T=(a_J sqrtF)''/(a_J sqrtF)
       =a_J²[2H²+2Hv-v²/4-kappa(rho_m+p_m)/(2F)].

The second equality uses ddotF=HdotF-2FdotH-kappa(rho_m+p_m); primes in q_T are conformal-time derivatives. Radiation is absent from the matter trace but contributes to this term and full00. Omitting it cannot be justified by trace-freedom. This is an action-specific propagation condition, not a measured ruler or a native GU bridge.

The next useful physical comparison requires a jointly solved matter background, fluid perturbations, initial spectrum and sound-horizon/selection model. The fixed-release vacuum likelihood stays a valid numerical result in its stated scope. No coefficient fit, scalar mass sample or transfer matrix supplies those inputs.

Background machinery: [De Felice and Tsujikawa](https://arxiv.org/abs/1002.4928). The exact subtraction/polynomial argument and finite transfer implementation are supplied here; no novelty or external-expert acceptance is claimed.
