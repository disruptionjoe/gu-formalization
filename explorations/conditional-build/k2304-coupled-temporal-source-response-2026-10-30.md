---
title: "K2304 Coupled temporal source response"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional construction only; no native physical acceptance
scripts:
  - tests/channel-swings/k2304_coupled_temporal_source_response_probe.py
---

# K2304 Coupled temporal source response

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
result: K2304
carrier: flat selected K77 I1B temporal symmetric metric and full ambient Clifford distortion LAYER=ambient CHIRALITY=N/A
pairing: native trace/Hodge bilinear form; auxiliary Fourier norm is separately supplied ON=declared_carrier
real_structure: real coefficients with complex Fourier or Hilbert representation where stated
grading: explicitly stated native Clifford or ordinary scalar/number grades; no transfer between them
action_owner: repository-construction -- same K127-K129 T=0 coupled Hessian and K2301 companion
target: six spatial metric source equations coupled to the full temporal distortion MAP-TYPE=evaluation
```

## Question and scope

[K2301](k2301-native-companion-time-domain-2026-10-30.md) prescribed only h11. Its restricted response pole need not survive solving the metric jointly. Here all six components of H=(hij), i,j=1,2,3, vary. The four time-component source rows vanish; we fix h0mu=0. Their nonzero-frequency gauge interpretation does not justify a global Schwartz gauge primitive or remove constant modes. The source is a supplied time-dependent symmetric stress J with J0mu=0, with no companion source. This is a conditional sector of the selected I1B Hessian, not physical matter, full spatial dynamics, or a GU Green operator. SC-ACT-01/02 and SC-GEO-55 remain ASSERTS; ledger0.263, including LT-GR1b/6b/10/11, is unchanged.

## Native reducing block

Set Wi=dx^i gamma_i and Ui=dx^i gamma_0i for i=1..13. Use odd basis
(W1,W2,W3,Vn=sum_i=4..13 Wi,M12,M13,M23), where Mij=dx^i gamma_j+dx^j gamma_i, and the corresponding even basis (U1,U2,U3,Un,N12,N13,N23). These are Clifford grades one and two, not a physical fermionic grading. With D=d/dt and kappa real nonzero, the companion is kappa+LD,

    G7=diag(1,1,1,10,2,2,2), G14=diag(G7,-G7),
    L=[[0,B],[B,0]], B=diag(B4,-2I3),
    B4=[[-1,1,1,10],[1,-1,1,10],
        [1,1,-1,10],[1,1,1,8]].                         (1)

The native coefficient probe checks every column, both Grams, and all ten metric covectors. The sector is nondegenerate and invariant under the native skew coefficient L, hence its G-orthogonal complement is also invariant. It contains the complete temporal A-image, so distortion in its complement cannot change the forced metric response. This does not assert that the complement has no homogeneous solutions.

Order metric coordinates h=(h11,h22,h33,h12,h13,h23). The odd forcing R h'' has first four rows (h22+h33,h11+h33,h11+h22,tr H), and final rows (-h12,-h13,-h23). The even forcing is zero. The actual metric source is

    j=R^T G7 Todd'', (j11,j22,j33,j12,j13,j23)
      =(J11,J22,J33,2J12,2J13,2J23).                   (2)

The factor two is the symmetric offdiagonal variation, not a changed physical coupling. With companion source zero,

    S(z)=-kappa z^4 R^T G7(kappa²I-z²B²)^-1 R.         (3)

## Joint trace and tracefree response

Write H=Htf+qI3, J=Jtf+jI3, q=tr H/3,j=tr J/3, and Delta=(kappa²-121D²)(kappa²-4D²). Direct native composition gives

    Jtf= -kappa D^4/(kappa²-4D²) Htf,
    j= -2kappa D^4(17kappa²-113D²)/Delta q.             (4)

Inverting all six equations replaces the restricted K2301 poles ±kappa/sqrt13 by a genuine scalar pair ±kappa sqrt(17/113). The tracefree response inverse has no nonzero exponential pole. The two-sided companion inverse used in deriving (3) must not be relabeled a retarded inverse without checking the complete equations.

This can be checked directly at z*=kappa sqrt(17/113): kappa+z*L is invertible (z* differs from ±kappa/11 and ±kappa/2), q nonzero and H=qI3 give T=-(kappa+z*L)^-1 Rz*²h with A*T=0. Thus (H,T) exp(z*t) solves BOTH homogeneous coupled rows. The scalar pole is not an artifact of eliminating a singular companion. The raw companion poles cancel from the forced source-to-(H,T) rational map; they are not poles of this coupled response.

An explicit full-row witness avoids relying only on elimination. Let P=diag(1,1,1,0,...,0) in13 dimensions and a²=17kappa²/113. With H=exp(at)I3, use the odd/even matrix representatives

    Todd=exp(at) (17kappa/270)(6P-I13),
    Teven=exp(at) (17a/270)(12P-7I13).                  (5a)

The metric coefficient is2(5)+10(-1)=0; the even companion vanishes identically; the odd residual is exp(at)(17kappa²-113a²)(6P-I13)/270. These verify both signs of a without a singular companion inversion.

The six-component Schur realization on L²(R;Sym3) with the Frobenius norm is closed and self-adjoint with domain H²: both real Fourier multipliers are nonzero away from zero and grow as a nonzero constant times omega². It is injective with dense nonclosed range, since both vanish to order4 at zero. Its inverse is unbounded. This Schur domain is not by itself a closed realization of the full mixed-order Hessian.

On the full line, the real-frequency multipliers have only their fourth-order zero at omega=0. Each of the six tensor-source components in Schwartz space admits a unique Schwartz H exactly when its first four time moments vanish. Division by omega^4 then preserves Schwartz class, and T from the companion multiplier is Schwartz. Uniqueness here is for the forced reducing sector modulo temporal metric gauge, not a global quotient theorem for the ambient theory.

## Actual followthrough: retarded obstruction and exact repairs

For a scalar compact source j=D^4 psi with psi nonnegative, nonzero and smooth compactly supported, the moments vanish but the retarded inverse

    q=-Delta/[2kappa D^4(17kappa²-113D²)] j             (5)

has a nonzero future exponential tail. At the positive root the numerator Delta is nonzero, and the weighted moment integral exp(-z*s)psi(s) ds is strictly positive. Polynomial delta/contact terms from the rational inverse do not remove that tail. Retarded solutions exist as distributions; this source has no retarded tempered solution in this coupled temporal sector. The unique Schwartz solution is two-sided. Tempered solutions are nonunique because polynomial homogeneous modes survive.

For an arbitrary smooth compact scalar source, the retarded growing tail vanishes exactly when integral exp(-a s)j(s) ds=0, a=abs(kappa)sqrt(17/113). Polynomial tails from D^-4 are tempered and are a separate issue. Imposing the four ordinary moments as well gives a Schwartz retarded response; compactness additionally requires the opposite exponential moment. On a time circle, zero source mean suffices, with zero-mean metric fixing the constant kernel. These domain choices are supplied, not physical boundary laws.

For any Sym3 polynomial H of degree at most3, Todd=-R h''/kappa and Teven=B R h'''/kappa² solve both homogeneous rows. They are tempered. In particular H=t²I3 has nonzero linearized curvature, so these cannot all be removed as temporal metric gauge. This is why the Schwartz uniqueness statement cannot be broadened to tempered uniqueness.

The assertion is not universal for all sources. For tracefree Jtf=D^4 Psi with Psi smooth compact and tracefree, (4) yields compact Htf=-(kappa²-4D²)Psi/kappa. The factors in the companion also cancel, yielding compact T. For the scalar branch choose j=D^4(17kappa²-113D²)psi; then q=-Delta psi/(2kappa) and T are compact. These are nontrivial matched-source counterconstructions. They require source restrictions; no matter action was derived to supply them.

At zero frequency, arbitrary compact sources can create polynomial tails from D^-4 even on the tracefree branch. Moment conditions remove those tails but do not remove scalar exponential tails. A supplied flat spatial13-torus lets spatial averaging isolate this forced sector; this is not localized finite energy on R13 or selected physical spacetime. General spatial sources, nonzero companion forcing, physical source/readout ownership, nonflat backgrounds, and alternative boundary laws remain open.

## Verification and next condition

The probe independently recomputes native columns/pairings from the exact coefficient bank, tests the six-column rational source map, scalar/tracefree decomposition, full homogeneous residual and compact repairs. Mutants change native coefficients, offdiagonal normalization and transfer denominators. Continuum results follow from the displayed Fourier and weighted-moment proofs, not finite samples. Internal review is not Lean, external-expert certification or novelty.

The useful next discriminator is a source-action/readout construction or a nonzero spatial symbol for this same coupled system: do allowed source conservation/positivity and boundary data suppress or expose the scalar coupled mode? Neither repeating the restricted h11 pole nor freely choosing matched compact sources answers that question.
