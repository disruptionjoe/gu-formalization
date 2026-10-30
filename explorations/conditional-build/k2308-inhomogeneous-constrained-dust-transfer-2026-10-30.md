---
title: "K2308 Inhomogeneous constrained dust transfer"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics only; no native physical acceptance
scripts:
  - tests/channel-swings/k2308_inhomogeneous_constrained_dust_transfer_probe.py
---

# K2308 Inhomogeneous constrained dust transfer

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
result: K2308
carrier: four-dimensional scalar Fourier metric, canonical scalar and smooth variable-mass dust LAYER=toy CHIRALITY=N/A
pairing: declared native bilinear form or positive Hilbert/coordinate norm as specified ON=declared_carrier
real_structure: real physical fields; complex Fourier amplitudes only where explicitly stated
grading: native Clifford grades or ordinary particle number; no identification between them
action_owner: repository-construction -- fixed healthy K2302 designer action and K2305 background, radiation absent
target: regular fixed-k constrained transfer through the Einstein-frame turnaround MAP-TYPE=evaluation
```

## Same action, now nonzero spatial momentum

[K2305](k2305-regular-constrained-matter-transfer-2026-10-30.md) solves only homogeneous transfer. Keep exactly its healthy action and background, with beta=d log B/dphi=-1/(sqrt6 M), d>0, u=dot phi, and no radiation. Let q=k²/a²>0, Delta -> -k², and use Newtonian gauge

    ds²=-(1+2Phi)dt²+a²(1-2Phi)dx².

Linear anisotropic stress vanishes, so the two metric potentials agree. Define chi=delta phi, pi=dot chi, n=delta(number density)/background number density, and covariant dust velocity u_i=partial_i v. Dust mass density perturbation is delta d=d(n+beta chi), not d n. The scalar sector at k=0 has separate gauge issues and is not obtained by declaring this chart a homogeneous theorem.

## Action-derived equations and a propagated constraint

With P=dot Phi, the complete system is

    P=-H Phi+(u chi-d v)/(2M²),
    dot chi=pi,
    dot pi=-3H pi-(q+V''+beta²d)chi+4u P
             -2(V'+beta d)Phi-beta d n,
    dot n=3P+q v,
    dot v=-Phi-beta chi-beta u v.                     (1)

The particle action -m integral B(phi) ds gives
u^nu nabla_nu u_mu=-beta(delta_mu^nu+u_mu u^nu)partial_nu phi,
which fixes the velocity sign and drag. Number conservation fixes dot n; linearizing Box phi-V'=beta rho_d fixes both beta²d and the lapse term -2(V'+beta d)Phi. These separate derivations prevent a self-consistent sign typo from masquerading as physics.

The Hamiltonian residual is

    C=q Phi+3H(P+H Phi)
      +(u pi-u²Phi+V'chi+d(n+beta chi))/(2M²).         (2)

Using dot q=-2Hq and the background equations, direct off-constraint differentiation gives dot C=-3H C. Differentiating the momentum equation also gives

    Phi''+4H Phi'+(2H'+3H²)Phi
       =(u pi-u²Phi-V'chi)/(2M²).                     (3)

Thus the spatial trace equation is not missing. Equations(1)-(3) are derived for this fixed conventional action; SC-COS-50/51/54 remain ASSERTS and native ledger LT-GR2e remains NEEDS.

## Regular constrained transfer and determinant

Solve (2) for dust number:

    d n=-(2M²q-u²)Phi-(3Hu+V'+beta d)chi
                         +3Hd v-u pi.               (4)

This requires d>0, not H!=0 or2M²q-u²!=0. Substitution in(1) gives a four-dimensional linear system in(Phi,chi,pi,v), with diagonal(-H,0,-3H+beta u,-beta u). Hence its transition matrix obeys

    det K(t,t0)=(a(t0)/a(t))^4>0.                    (5)

For each fixed finite k and compact smooth background interval, coefficients are bounded; both forward and inverse transfer exist and have a Gronwall bound. This proves neither decay nor uniform-in-k PDE control: q grows with k², and dust can form nonlinear caustics.

On the SAME K2305 normalized crossing fixture x in[1,11/10], use |H|<1,|u|<4,d<12, |V'|<30,|V''|<58, |beta|<1/2, M=1 and a²=F/x²>=60/121. Thus q<=121 k²/60. Direct row sums of the reduced matrix are bounded by

    ||J_red||_infinity <330+121 k²/30.                (6)

The interval has Einstein-time duration<1/10, so forward/inverse norms are at most exp(33+121k²/300). This coarse explicit bound establishes finite transfer in these dimensionless fixture coordinates, not small amplification or stability. In this chart det K=(x/x0)^4(F0/F)^2; no zero occurs at H=0.

## Actual response and frame-defined readout

At turnaround choose constrained data(Phi,chi,pi,v)=(0,0,0,v0), which imply n=0. Then

    Phi'=-d v0/(2M²), chi'=0, pi'=-2ud v0/M²,
    n'=(q-3d/(2M²))v0, v'=-beta u v0.                (7)

This nonzero-velocity seed produces finite metric/scalar response. The n' cancellation at q=3d/(2M²) is real and retained as a control. There is no division singularity at that value or at2M²q=u².

Use the already frozen conformal relation g_J=B(phi)²g_E, with background Jordan time dt_J=B dt. The SAME coordinates remain Newtonian gauge and

    Phi_J=Phi+beta chi, Psi_J=Phi-beta chi,
    delta n_J/n_J=n-3beta chi,
    delta rho_J/rho_J=n-3beta chi.                    (8)

The last equality uses constant Jordan dust mass; d_E=B^4 rho_J and delta d_E/d_E=n+beta chi give the same result. Thus lensing-potential sum Phi_J+Psi_J=2Phi while the force-potential difference is2beta chi. This is a defined frame readout and slip, not a measured lensing signal: source initial statistics, light propagation, transfer to observations and normalization remain missing. Equation(7) makes the slip start at second order, chi=-ud v0 tau²/M²+O(tau³), while both potentials have the same first derivative. The selected datum therefore tests the coupled matter/scalar interface instead of freezing dust.

## Evidence and next condition

The probe checks symbolic off-shell constraint propagation, the independent Euler/number identities, full trace Einstein equation, reduced trace, constraint reconstruction, finite bound arithmetic and selected jets/frame conversion. Genuine coefficient/sign/mass-conversion changes must fail those equations. Universal existence follows from the displayed smooth finite-dimensional system; no numerical sampling is used as a PDE theorem.

Next supply a physical initial spectrum/readout on this fixed action or obtain controlled spatial/Jeans estimates. The regularity result must not be relabeled stability or native GU recovery. No source, ledger, canon, hardware or empirical verdict changes.
