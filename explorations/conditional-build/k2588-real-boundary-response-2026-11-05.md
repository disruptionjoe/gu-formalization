---
title: "K2588 Real symmetric preparation on the fixed annulus"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: real symmetric scalar preparation and per-mode self-adjoint realization; no physical selection or global positive energy
scripts:
  - tests/channel-swings/k2588_real_boundary_response_probe.py
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
result: K2588
carrier: fixed-annulus scalar cofactor and Einstein response on the selected curved product LAYER=toy CHIRALITY=N/A
pairing: invariant positive density for scalar adjoints; indefinite tensor duality for conserved readouts ON=declared_carrier
real_structure: complex conjugate factors averaged to a real response
grading: scalar radial eigenmodes, angular modes and reconstructed tensor components remain distinct
action_owner: repository-construction -- selected conditional action
target: real symmetric preparation and its source response MAP-TYPE=evaluation
```

# Construct a real preparation without calling it physically selected

## Result and scope

K2584/86 supply a complex, ordered, ten-trace scalar cofactor inverse. Here a finite average of its conjugate and order-reversed constructions supplies a REAL SYMMETRIC right inverse on the same fixed annulus. For each fixed radial and angular mode, its inverse on its range is a closed self-adjoint realization of the real scalar determinant. The selected full coupled system admits the corresponding real source response and compact conserved observations, with K2586's polynomial distribution/regularization bounds retained. This is a DIFFERENT mathematical preparation from the original ordered complex prescription; neither is physically selected.

Self-adjointness below is for the scalar determinant in its positive scalar L2 density, not the full coupled tensor operator, physical energy, positivity, a causal Green operator or native Met(X). SC-ACT-01/GEO-03/GEO-55 remain ASSERTS and SC-META-53 UNCERTAIN. Ledger0.263 and canon do not change. No source claim is falsified or recovered.

## 1. Factor transpose in the actual measure

Use K2584's fixed scalar radial eigenvalue sigma and angular labels ell,m. Its determinant is

    d_sigma(Y)=Lkappa product_(j=1..5)(Y-y_j),

with real nonzero Lkappa, conjugation-stable roots (multiplicity retained), and each root inside |y_j-sigma|<sigma/2. The Einstein factor is also real. Write G_j for the inverse of (Y-y_j) with its sign-adapted complex separated Robin data. Root signs are as in K2584; BOTH signs are allowed for real roots. K2584's real/complex estimates apply equally to conjugates.

In Liouville coordinates, v=Ju, f=-J zeta F/K. The invariant scalar density is K^(-7/2)J² zeta dx. If g_j(x,t) is the Green kernel of the transformed v equation relative to dt, the ORIGINAL inverse kernel relative to that density is

    G_j(x,t)=-K^(5/2) g_j(x,t)/(J(x)J(t)).       (1)

The regular second-order expression with separated Robin data is bilinearly symmetric: integration by parts has zero bilinear boundary form for two functions obeying the SAME complex Robin condition. Its Green kernel therefore satisfies g_j(x,t)=g_j(t,x). This is transpose symmetry, not Hermitian symmetry for a nonreal root. Equation(1) proves transpose symmetry in the actual invariant measure; ignoring its weights would not suffice. Complex conjugation sends G_y,epsilon to G_conj(y),-epsilon.

For a real root replace its chosen G_j by H_j=(G_j,+ + G_j,-)/2. For a nonreal root put H_j=G_j with the prescribed sign. Every H_j is a right inverse of its root factor, bilinearly symmetric, and the labeled multiset {H_j} is conjugation-stable. Distinct labels for a repeated root cause no gap denominator.

## 2. Symmetrize all orders; do not commute boundary inverses

Define

    R_sigma=(1/(Lkappa 5!)) sum_(pi in permutations(1..5))
                 H_pi(1) H_pi(2) ... H_pi(5).   (2)

Each summand is a right inverse of d_sigma: reorder the commuting DIFFERENTIAL factors to cancel adjacent inverses successively. This never commutes the boundary inverses themselves. For smooth input the cancellation is classical; it extends to L2 and the K2586 measure sources distributionally. Thus d_sigma R_sigma=I.

Transposition reverses each product, and reversal permutes all 5! terms. Conjugation permutes the labeled factors (real roots were already averaged). Consequently

    R_sigma^T=R_sigma, conjugate(R_sigma)=R_sigma,
    R_sigma^*=R_sigma.                          (3)

The finite average is input-independent and retains the original spectral coefficients. It does not impose all the original ten-trace prescriptions at once: (2) defines the new preparation. A single ordered product is generally neither symmetric nor real. Averaging only conjugates ensures reality but need not ensure symmetry; averaging only orders need not ensure reality when real roots retain a single impedance sign.

## 3. An actual closed real per-mode domain

Fix sigma,ell,m. In the positive weighted L2 interval space, every factor inverse has a continuous Green kernel and is bounded/compact. Hence R_sigma is bounded, compact and self-adjoint. It is injective: R_sigma f=0 implies f=d_sigma R_sigma f=0. Its range is dense because (Ran R_sigma)^perp=ker R_sigma^*=0.

Set D_sigma=Ran R_sigma and A_sigma=R_sigma^-1 on D_sigma. This is a densely defined real self-adjoint operator. For completeness, symmetry follows from R_sigma symmetry, and A_sigma±i is onto since I±iR_sigma has a bounded inverse for bounded self-adjoint R_sigma; (A_sigma±i)^-1=R_sigma(I±iR_sigma)^-1. Closedness also follows directly: if u_n->u and A_sigma u_n->f, then u_n=R_sigma A_sigma u_n->R_sigma f, so u=R_sigma f and A_sigma u=f. Distributionally A_sigma u=d_sigma u. Regular ODE regularity makes D_sigma a subspace of H10 on this fixed interval. For compactly supported smooth phi, symmetry and integration by parts give <f,R_sigma d_sigma phi>=<d_sigma R_sigma f,phi>=<f,phi>, hence R_sigma d_sigma phi=phi: this realization contains the minimal differential domain. This gives an actual domain, not merely the assertion that a real part solves a real equation.

The range prescription is a valid spectral boundary domain; no claim is made that it equals the old component Dirichlet or intermediate Robin domain, or that the full coupled boundary problem is self-adjoint. Constants may grow polynomially with sigma/ell/m. The orthogonal direct sum of these self-adjoint scalar realizations is self-adjoint on the domain sum ||u_j||²+||A_j u_j||²<infinity. A uniformly bounded global L2 inverse does NOT follow. Distributional sources use the weighted spectral synthesis below, not an unjustified global L2 resolvent.

## 4. Execute the source, regularization and reciprocity consequences

For the real Einstein factor use (G_+ + G_-)/2. Apply the same conjugate averaging to the real TT factor inverses on their DISTINCT radial basis. For each cofactor ordering/sign choice reconstruct the full scalar, TT, shifted/original metric and auxiliary fields with K2584's actual polynomial identities, then average the full linear responses. The coefficients, source and equations are real; each summand solves the same source, so the average does too. Retain K2582/84's synchronized splitter correction within EVERY summand before averaging. Linear equality of the two synchronized descriptions then survives averaging; unrelated scalar and TT radial eigenbases are never identified. This is not a claim that arbitrary unsynchronized preparations agree.

The estimates for every permutation and allowed conjugate sign are uniform because they use the same joint scale and finite number of factors. K2586's first measure factor costs k5 and the remaining four factors k8, giving k13 again. Triangle inequality for an average introduces no factorial growth beyond the maximal bound. Its full local H^-43 synthesis and point-position/mollifier O(epsilon) error in H^-44 therefore carry over, with the same conservative norm orders. This is a point response on the new preparation, not a pointwise metric value. The original complex preparation remains available independently.

For real smooth scalar test sources f,g at a fixed mode,

    <f,R_sigma g>=<R_sigma f,g> in real L2.      (4)

This is reciprocal scalar response. It does NOT assert reciprocity of the reconstructed tensor response: cofactor reconstruction, observation and source injection are different maps. A compact conserved tensor detector D_W(h)=<E W,h>, with W smooth compact and E the formally self-adjoint Einstein operator, remains gauge-insensitive to compactly admissible metric gradients and obeys the inherited weak distribution bound. Its actual scalar transfer is the transpose of the FULL reconstruction/source maps around R_sigma, not R_sigma alone. Reality and boundedness of this transfer do not calibrate W physically.

## 5. Explicit real-boundary consumer and adverse examples

The interval model L=d²/dx² on [0,1], k=1, with v'(0)+iv(0)=0 and v'(1)-iv(1)=0 illustrates why a real response has a new domain. For real f, write v=u+iw. Then w''=0, and eliminating its two affine coefficients gives

    u(1)=-u(0), u'(1)+u'(0)=u(0).               (5)

For f=1 the exact solution is

    v=x²/2-x/2-i/2, u=x²/2-x/2.

The imaginary part here is nonzero although the source is real. The real solution obeys(5) and solves u''=1, but does not obey the old complex Robin condition: u'(0)=-1/2. At f=x, the probe solves the actual complex BVP, takes the real part, and checks the new real traces and the bilinear reciprocity integral against the f=1 response. The homogeneous real problem(5) has only zero, independently checking uniqueness. Equation(5) is a concrete example of a nonlocal real endpoint law; it is not the boundary formula for the curved five-factor problem.

The probe also uses exact noncommuting symmetric Green-matrix analogues to check order symmetrization, complex-conjugate closure and omitted order or conjugate averaging. Those finite matrices validate the algebra and adverse controls, not the universal ODE domain theorem. Kernel density conversion and distribution exponents are checked separately. The proofs above and K2584/86 carry the analytic result.

## Verification and next question

Exact probes and independent review are required before acceptance. Mathematical real preparation is now constructive, so it should not be requeued as absent. Which independently justified physical boundary/observation selects among these preparations, whether tensor response is reciprocal under its actual pairing, and which causal/time-domain statement is available remain distinct questions. No finite test count establishes them.

[K2584](k2584-scalar-spectral-boundary-inverse-2026-11-05.md), [K2586](k2586-fixed-annulus-point-response-2026-11-05.md), [probe](../../tests/channel-swings/k2588_real_boundary_response_probe.py), [report](../../lab/process/k2588-real-boundary-response.json).

Independent read-only field specialists and a distinct integrated hostile reviewer found no remaining substantive defects after endpoint, sign and evidence-wording corrections. K2588 passes23 exact/supporting checks and8 contrary controls; K2589 passes34 and8 including the released post2 bracket. Universal ODE/domain and all-policy proofs remain separate from finite interval, matrix and reporting checks. No external-expert, proof-assistant, remote-CI or physical certification.
