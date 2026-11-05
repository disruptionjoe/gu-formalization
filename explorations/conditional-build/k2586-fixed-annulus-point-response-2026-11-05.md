---
title: "K2586 Point response and regularization on the fixed annulus"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed-annulus point-source distributional response and quantitative regularization; no physical preparation or pointwise field value
scripts:
  - tests/channel-swings/k2586_fixed_annulus_point_response_probe.py
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
result: K2586
carrier: compact smooth radial pressure times an interior B point distribution on the selected curved product LAYER=toy CHIRALITY=N/A
pairing: indefinite tensor-test duality and auxiliary positive Sobolev norms ON=declared_carrier
real_structure: real data; complex impedance explicitly represents two real quadratures
grading: scalar amplitudes, TT tensor, shifted and original metric, auxiliary grade2 kept distinct
action_owner: repository-construction -- stated conditional model
target: fixed-annulus point response and conserved smooth observations MAP-TYPE=evaluation
```

# Admit an actual point input without changing preparation

## Result and exact scope

K2584's fixed-annulus spectral prescription extends to the actual invariant B point distribution, while retaining the compact smooth radial-pressure source, all selected coupled equations and synchronized scalar/TT splitting. A conservative explicit bound places the reconstructed fields locally in C0(A;H^-43(B)). Moving or smoothing the point gives an O(epsilon) response error in the weaker local H^-44 norm and hence in every specified compact smooth conserved observation.

K2564 already constructed point-source responses on a DIFFERENT global B completion with parameter-switched radial inverses. This result does not claim first existence, superiority of norms across different domains, or domain independence. Its new content is admission on the fixed radial Dirichlet/trace-lift and B-annular preparation of K2580/82/84, plus a quantitative same-preparation regularization bound. Auxiliary positive norms measure distributions; they are not physical energy or positivity.

SC-ACT-01/GEO-03/GEO-55 remain ASSERTS and SC-META-53 UNCERTAIN. Ledger0.263 LT-GR6b/10/11 and LT-SM8, canon and physical preparation remain unchanged. The curved product/action completion is repository-selected, not native Met(X), a causal Green function, or a calibrated detector.

## 1. Actual annular measure and point normalization

Use t in [asinh1,asinh2], theta,omega in S3, and

    G_B=K^-1[-dt^2+cosh^2(t)dOmega_theta^2-sinh^2(t)dOmega_omega^2],
    x=log[tanh(t/2)/tanh(asinh1/2)], zeta=sinh^2(t),
    J=sinh(t)cosh(t)^(3/2), dx/dt=1/sinh(t).

The positive volume density for tensor distribution duality is

    dvol_B=K^(-7/2) J^2 zeta dx dtheta domega.    (1)

An invariant point at an INTERIOR x0 and angular location Omega0 therefore has coordinate representation

    rho=K^(7/2)/(J(x0)^2 zeta(x0)) delta_x0 delta_Omega0.

The actual Liouville forcing for (Y-y)u=rho is f=-J zeta rho/K, so

    f= -K^(5/2)/J(x0) delta_x0 delta_Omega0.      (2)

Dropping the density or treating rho as a bare coordinate delta would solve the wrong source problem. Endpoint sources are excluded: endpoint-delta and trace conventions would require a separate prescription.

## 2. Extend one actual complex factor to finite measures

Retain K2584's factor L=partial_x^2-P=L0+V, where L0 uses ReP with the SAME complex separated Robin conditions, V=i epsilon b zeta, and ||V||infinity<=k^2. Its previously proved inverse bounds are

    ||G0 f||infinity<=CG k ||f||L1,
    ||G f||infinity<=C2 k^2 ||f||L2.             (3)

The real-potential Green kernel is continuous; the first bound equivalently bounds its absolute kernel. It extends by integration to a finite measure mu with ||G0 mu||infinity<=CG k||mu||TV. Define, rather than assume,

    Gmu=G0mu-G(VG0mu).                          (4)

VG0mu is in L2 on the fixed finite interval, so this is meaningful. Distributionally L(G0mu)=mu+VG0mu and L G(VG0mu)=VG0mu; thus L Gmu=mu with the same homogeneous endpoint conditions. Uniqueness follows because a homogeneous distributional solution of this regular second-order ODE is smooth and K2584 already proves uniqueness. The bound is

    ||Gmu||infinity<=C5 k^5 ||mu||TV,
    C5=CG(1+sqrt(d)C2), k>=1.                   (5)

This is conservative, not a sharp measure bound. It uses the REAL-PART Green bound and full complex inverse; no indefinite-operator spectral theorem or unproved dual extension is inserted.

For the scalar Einstein root and ordinary TT roots, K2580/84 give the real monotone Green bound directly, with cost k rather than k^5. Tagged TT/splitter overlap roots -mu and -5K instead use K2582 §3: monotone/nonnegative potentials and its fixed finite-exception bound. They are not in K2584's positive-root disk. Their Green constants can be large but are fixed independent of angular degree. These real channels also extend directly to measures and are dominated by (5).

## 3. Five factors and all angular multiplicities

Apply (4) to the FIRST scalar cofactor factor. Four further factors see a continuous forcing and use the L2 bound(3), with bounded Liouville multipliers. The total cofactor-potential loss is at most

    k^(5+4*2)=k^13.                             (6)

The deterministic factor order and ten intermediate boundary traces remain those of K2584; repeated roots require no gap denominator. Cancellation is sequential, not commutation of boundary inverses. All inverse identities hold distributionally.

Let sigma_j denote the scalar radial Dirichlet eigenvalues and define

    r_j^2=1+sigma_j/K,
    a_(ell,m)^2=1+ell(ell+2)+m(m+2).

K2584's common scale satisfies

    k^2=30+a^2+6r^2<=37r^2a^2.                 (7)

Define Hrad^q by weights r_j^(2q) in the radial orthonormal basis and HΩ^s by weights a^(2s), with the full harmonic multiplicities. The point delta on S3 times S3 belongs to HΩ^-4. Indeed the addition theorem gives squared coefficient sum at degrees ell,m proportional to (ell+1)^2(m+1)^2. On the dyadic shell max(ell+1,m+1) in [N,2N), that sum is O(N^6), while a^-8 is O(N^-8); the dyadic contributions are O(N^-2), summable. This treats the six-dimensional angular product, not one sphere or one mode.

For the fixed radial splitter coefficients chi_j, (5)–(7) yield

    ||U||_(C_x(Hrad^q tensor HΩ^-17))
      <= C ||chi||_(Hrad^(q+13)) ||delta_Omega0||_(HΩ^-4). (8)

Here C_x means continuous functions in x with the displayed Hilbert norm; dominated coefficient sums prove continuity. The compact-pressure splitter belongs to every scalar Dirichlet power by K2584. Its trace-lifted TT residual belongs to every TT Dirichlet power, and the tagged smooth overlap mode is treated separately. No scalar/TT eigenbasis is identified. Thus every finite q in(8) is available. Ordinary TT, tagged overlap and Einstein channels have smaller losses and fit the same ceiling.

## 4. Reconstruct all fields and conserved readouts

K2552's actual algebraic identities reconstruct Q,z,h=z-rE symQ,e2 from the cofactor, Einstein and TT potentials, including mixed and skew rows and the direct source terms. K2562's verified degree count is unchanged: matrix entries have total degree<=2 in X,Y, five-by-five cofactors degree<=10, source column raises it to11; tensor reconstruction adds at most2 derivatives and auxiliary B adds1. This is at most25 derivatives; take separate safe margins DA=DB=26.

Choose q=30 in(8), requiring only Hrad^43 source data, supplied here. On compact A regions the regular auxiliary radial-ball elliptic estimates used in K2562/64 convert radial spectral control to the usual Sobolev control. Thirty radial derivatives leave four after the conservative26 loss, sufficient for C0 in the largest auxiliary radial dimension5. Tensor reconstruction regularity is the inherited regular-center construction, not an assumption that singular coordinate coefficients act arbitrarily on distributions.

Before reconstruction, L2_x HΩ^-17 embeds in local H^-17(B): by duality a compact test's L2_x HΩ^17 norm is bounded by its local H17 norm. Then ALL B derivatives, including x derivatives, are interpreted distributionally and the safe26 loss gives

    Q,z,h,e2 in C0_loc(A;H^-43_loc(B)).           (9)

No C0_B or pointwise metric value follows. Local restriction and smooth volume/tensor coefficients preserve these finite-order distribution spaces. Every selected equation holds by distributional differentiation of the mode limits; no unproved convergence of classical derivatives is used. The original source is exactly j_A(r)delta_B, with the actual compact cutoff and canceling split tails retained.

Approximate the interior point by smooth compact mollifiers and angular smoothing, keeping the same prescribed inverse and radial data. Section5 proves convergence. All smooth full-row identities pass to the limit. Extend changed splitters by K2582's matched direct scalar-overlap/TT responses and its Einstein gauge correction. Equality of ALL total fields for synchronized splits passes to the limit; it is stronger than equality only after a conserved test. Independently chosen preparations are not asserted equal.

For any specified compact smooth conserved symmetric test F, the original-metric observation <h,F> is finite and continuous. In particular F=E W with compact smooth W is conserved by the linearized Einstein identity on the fixed background. These tests are constructed mathematical readouts, not independently calibrated instruments or physical selection of the preparation.

## 5. Released consumer: quantitative point regularization

The scalar Green kernel has BILINEAR symmetry G(x,t)=G(t,x), without conjugation. For separated complex Robin data, the bilinear boundary Wronskian vanishes at both ends; the usual Lagrange identity proves the symmetry even when P is complex. It is not a self-adjoint/Hermitian assertion.

For a unit interior atom, v=G delta_t is continuous, v' has a unit jump and Lv=delta_t. Integrating Taylor over a one-sided interval h=min(d/2,1/k) bounds its one-sided derivative by

    |v'|<=2||v||infinity/h + h k^2||v||infinity/2 +1
          <=C k^6.                             (10)

The last1 accounts for the derivative jump; a smooth-forcing Taylor formula alone would omit it. Thus G is uniformly Lipschitz in its first variable, and bilinear symmetry gives the SAME source-variable bound. Keeping x0 in a fixed interior compact interval makes the normalization coefficient in(2) uniformly smooth. Moving x0 by epsilon therefore changes the first inverse by O(k^6 epsilon). Four later L2 inversions give O(k^14 epsilon).

Angularly, H5 on the six-dimensional compact product embeds in C1, so

    ||delta_Omega-delta_Omega'||_(HΩ^-5)<=C dist(Omega,Omega'). (11)

This follows by applying the fundamental theorem along a shortest geodesic to the test function and duality; no finite-mode cutoff is mistaken for the point. Radial displacement costs14 angular powers on HΩ^-4; angular displacement costs13 on HΩ^-5. Both land in HΩ^-18, with radial input Hrad^44 for q30. Hence, for points within the fixed interior compact set,

    ||h_point-h_point'||_(C0_loc(A;H^-44_loc(B)))
         <=C distance(point,point').             (12)

The same bound holds for the other reconstructed fields. Integrating(12) against a unit-mass nonnegative mollifier supported within distance epsilon yields an O(epsilon) approximation error, with fixed preparation, full source conservation and all equations preserved. Consequently

    |<h_epsilon-h_point,F>|<=C epsilon ||F||_(H44),
    |<h_epsilon-h_point,E W>|<=C' epsilon ||W||_(H46) (13)

for compact tests and the fixed radial source. Constants depend on kappa, the chosen preparation, source norms and compact sets. This is a constructive error estimate in a weak observation norm, not a practical experimental tolerance or pointwise convergence claim.

## Verification and remaining question

The probe checks the actual volume/forcing normalization, resolvent cancellation in a noncommuting finite operator fixture, exact outgoing-kernel endpoint/jump/symmetry and source-displacement formulas, multiplicity/shell estimates, derivative-loss arithmetic, and conserved-test cancellation identities inherited from the full-row construction. Wrong density, wrong resolvent sign, Hermitian-for-bilinear symmetry, omitted multiplicities and missing losses are rejected. Universal mode synthesis and distributional passage are the written proof, not finite probe totals.

Standard Sobolev/distribution duality is described in [Dyatlov's MIT notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf); its local positive auxiliary norms are used here only after the actual mixed-sign operator estimates are proved. No elliptic theorem is applied directly to Y. Physical preparation/readout selection, a sharp singularity description, causal propagation and native displacement/action ownership remain open. Arbitrary x-distributions and endpoint sources are outside this finite-measure theorem.

[K2584](k2584-scalar-spectral-boundary-inverse-2026-11-05.md), [K2582](k2582-affine-radial-boundary-response-2026-11-05.md), [K2580](k2580-radial-angular-source-domain-2026-11-05.md), [K2562](k2562-parameter-dependent-response-2026-11-05.md), [K2564](k2564-localized-spectral-response-2026-11-05.md), [probe](../../tests/channel-swings/k2586_fixed_annulus_point_response_probe.py), [report](../../lab/process/k2586-fixed-annulus-point-response.json).

Independent field specialists reviewed the concrete constructions and a distinct integrated hostile reviewer returned no remaining findings. Final exact probes and affected native checks passed. Universal distributional and all-policy proofs are distinct from finite identities, consumers and reporting checks. No external-expert, proof-assistant, remote-CI or physical certification.
