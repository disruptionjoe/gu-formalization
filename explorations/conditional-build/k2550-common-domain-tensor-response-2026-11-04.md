---
title: "K2550 A common curved domain and source-disjoint tensor response"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied one-coordinate TT sector boundary realization; no radial-pressure inverse, physical boundary selection or native GU claim
scripts:
  - tests/channel-swings/k2550_common_domain_tensor_response_probe.py
---

# K2550 Prescribe the source and retain both boundary problems

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
result: K2550
carrier: original metric and full reconstructed displacement on the stationary curved product; TT tensor times one-coordinate profiles LAYER=toy CHIRALITY=N/A
pairing: inherited indefinite tensor contraction; positive weighted interval L2 only for the restricted scalar boundary problem ON=declared_carrier
real_structure: real kappa nonzero, product signature (7,7), real smooth sources and compact tests
grading: original metric h, shifted metric z, symmetric displacement Q and auxiliary grade2 remain distinct
action_owner: repository-construction -- selected comm/symi/symi I1 completion of K2537
target: common reduced-sector domain, prescribed source response, off-source observation and boundary sensitivity MAP-TYPE=evaluation
```

## Result and inference boundary

The two scalar factors in [K2544](k2544-constrained-tensor-response-2026-11-04.md)
now have a specified common curved Dirichlet domain. Every prescribed smooth
source in the stated tensor/one-coordinate class has a unique response in
that domain, satisfying all selected bulk equations. For a nonnegative,
nonzero source compactly supported inside the interval, the ORIGINAL metric and an explicit class of gauge-invariant
tensor observations are nonzero away from the source. This is an actual
boundary response construction; [K2548](k2548-compact-coupled-metric-detectors-2026-11-04.md)'s
compact contact identities alone cannot supply it.

The boundary restriction is essential. A second construction keeps the same
source AND the same original-metric endpoint values but changes the interior
metric observation. Fixing metric Dirichlet data alone does not fix the
independent displacement boundary data. The restricted positive interval
estimate also fails for arbitrary tangential dependence on the actual
indefinite product. Neither fact excludes other viable domains.

SC-ACT-01 ASSERTS the first-order action, SC-GEO-55 ASSERTS displacement from
gauge-rotated Levi-Civita, SC-GEO-03 ASSERTS Y=Met(X), and SC-META-53 remains
UNCERTAIN about indefinite spectra. The independent ambient metric, selected
completion, TT source class and boundary prescription here are supplied
conditional objects. This does not answer K2531's radial-pressure source,
select a physical detector or causal propagator, construct native Met(X), or
change ledger0.263 LT-GR6b/10/11/SM8. No empirical or novelty claim follows.

## 1. Keep the actual curved source sector

Reuse K2544's nonzero analytic A-tensor

    T=Hess_A f+K f G_A, Box_A f=-7Kf,
    tr T=div T=0, Box_A T=7KT, Riem_A T=-KT,
    K=35 kappa²/3624192, kappa!=0.

Its nonzero analytic germ and Codazzi identities were constructed there;
ambient coordinate functions with T=0 remain excluded. On A times B set

    j=J(B)T, C=u(B)T, K_skew=0, z=v(B)T.

The source is conserved for arbitrary J(B) because only its A indices enter
the divergence. The complete bulk equations, including skew, mixed and B
rows, reduce exactly to

    (D+e)v=rE J, c(D+mu)u=-rE J,
    h=H T, H=v-rE u, Q=C, e2=-A2^(-1) BQ,
    D=Box_B, a0=-5kappa/2288,
    e=175kappa²/3624192,
    c=970112/(13395kappa), mu=611557655kappa²/39953092608,
    rE=1/(6a0)=-1144/(15kappa),
    rT=rE²/c=127699/(1590kappa).

All remaining grades vanish by K2535's actual covariant grade preservation.
A2 is the algebraic auxiliary inverse, and BQ contains first derivatives.
This reuses the full curved equations, not a principal-symbol truncation.
The Einstein linearization is E(HT)=-(D+e)H T/2.

## 2. An actual space-form chart with a common interval domain

Let ell=1/|kappa|, I=(-ell,ell), and choose a local six-dimensional space
form (Sigma,gSigma) with signature (2,4) and sectional curvature K. Put

    Cwarp(t)=cos(sqrt(K)t),
    G_B=dt²+Cwarp(t)² gSigma, w(t)=Cwarp(t)^6.

The radial sectional curvature is -Cwarp''/Cwarp=K, and the tangential one
is (K-Cwarp'^2)/Cwarp²=K. Thus this is the ACTUAL B space-form geometry of
signature (3,4); no flat donor or change to the seed is involved. The chart
is nonsingular throughout the closed interval. For functions independent
of Sigma, D=w^(-1)(w u')'. This source class is extended along Sigma; it is
not compactly localized in all seven B coordinates.

Use the Hilbert space L²(I,w dt) and

    A=-w^(-1)(w d/dt)', Dom(A)=H²(I) intersect H¹_0(I).

Weighted and ordinary Sobolev norms are equivalent since w is smooth and
bounded away from zero. Integration by parts gives the closed positive form
integral w|u'|² on H¹_0, with regular Sturm--Liouville operator A on the
displayed domain. One can construct its zero-mass inverse explicitly below,
so no general multidimensional Green theorem is assumed.

For x=sqrt(K)t, cos²x=1-sin²x>=1-x². Hence on I

    1>=w>=(1-K ell²)^3>=1-3K ell²>1/2.

The elementary endpoint estimate |u(t)|²<=2ell integral |u'|² implies
integral |u|²<=4ell² integral |u'|². It follows that

    <u,A u>_w>=kappa²||u||_w²/8.

The exact inherited coefficients satisfy

    0<e<mu<kappa²/64.

Consequently both R_e=(A-e)^(-1) and R_mu=(A-mu)^(-1) exist on the SAME
domain and obey

    ||R_m||_(L²_w to L²_w)<=64/(7kappa²), m=e,mu.       (1)

Indeed A^-1 exists by the explicit positive kernel below and the energy
bound. The series R_m=sum_(n>=0)m^n A^(-n-1) converges in operator norm
because m||A^-1||<1/8. This proves invertibility and positivity preservation
without treating A-e as a maximum-principle operator with an unchecked sign.

## 3. Prescribed forcing and a source-disjoint observation

For ANY prescribed J in L²_w, define

    v=-rE R_e J, u=(rE/c) R_mu J,
    H=-rE R_e J-rT R_mu J.                            (2)

Since D=-A, substitution proves both original equations. Their individual
Dirichlet conditions u=v=0 select this unique sector solution. h,Q are
locally H² on the full product chart, and e2 is locally H¹. Smooth J gives
smooth reconstructed fields. No Dirichlet condition on e2 is asserted:
its trace can include nonzero u'. This is a common reduced-sector boundary
realization satisfying all bulk equations, not a proof of a self-adjoint
boundary realization of the entire original action.

For nonzero J>=0, strict positivity is transparent. Define

    p(t)=integral_(-ell)^t w(x)^(-1)dx,
    q(t)=integral_t^ell w(x)^(-1)dx, Lw=p(ell).

The inverse A^-1 has kernel

    G0(t,s)=p(min(t,s))q(max(t,s))/Lw                 (3)

against w(s)ds. It vanishes at the endpoints, has the required unit flux
jump, and is strictly positive for interior t,s. Thus A^-1J>0, and the
positive Neumann series gives R_m J>=A^-1J>0. The resolvent identity

    R_mu-R_e=(mu-e)R_mu R_e

also gives R_mu J>=R_e J. Because

    kappa(rE+rT)=429/106>0,

(2) proves, for either sign of kappa,

    kappa H<=-(429/106)R_e J<0.                      (4)

Opposite signed residues therefore do NOT cancel the prescribed response.
Now assume in addition that J has compact support inside I (for example
J in C_c^infinity(I)), so a nonempty open source complement exists.
Outside supp(J), the Einstein tensor is

    E h=-(rT/2)(mu-e)(R_mu J)T,                     (5)

nonzero wherever T is nonzero. Choose a relatively compact component patch
where T has a nonzero component and a compact smooth dual test tensor W (with invariant density in the pairing)
there, with B support disjoint from supp(J), such that <E h,W>!=0. Then

    O_W=<h,E W>=<E h,W>

is finite and invariant under linearized diffeomorphisms, since E is formally
self-adjoint and annihilates Lie_xi G on this Einstein seed. A positive dual
component test, rather than the indefinite squared norm of T, proves the
nonzero pairing. This detector is not the compact displacement-cancelling
family of K2548; its dependence on the imposed boundary data is explicit.
No experimental coupling to O_W has been derived.

## 4. Released quantitative response and stability

Put the nonnegative source inside [-ell/4,ell/4] and the detector slab inside
[ell/2,3ell/4]. In (3), p(s)>=3ell/4, q(t)>=ell/4 and Lw<=4ell. Therefore

    G0(t,s)>=3ell/64,
    R_e J,R_mu J>=(3ell/64) integral_I Jw dt.        (6)

This is a fixed positive source--detector separation, not a shrinking
contact limit. In particular

    |H(t)|>=(429/(106|kappa|))(3ell/64) integral Jw,
    |coefficient_T(Eh)(t)|>=
       (|rT|/2)(mu-e)(3ell/64) integral Jw.          (7)

For signed source errors, (1) instead supplies

    ||delta H||_w<=
      (|rE|+|rT|)64/(7kappa²) ||delta J||_w.         (8)

Compact finite detector errors follow by Cauchy--Schwarz and smooth fixed
A/Sigma test factors. These are mathematical auxiliary norm estimates;
they are neither physical energy positivity nor measured noise sensitivity.
They do not control arbitrary omitted tangential modes.

## 5. Released boundary counterconstruction with the metric fixed

The choice in section3 fixes BOTH sector boundary values. Fixing only the
original metric at the endpoints is weaker. Define

    psi_m=1+m R_m 1.

Then (D+m)psi_m=0 and psi_m=1 at both endpoints. For the SAME source add

    delta u=psi_mu, delta v=rE psi_e,
    delta H=rE(psi_e-psi_mu).                       (9)

Both homogeneous bulk equations still hold and delta H vanishes at the
endpoints. However

    psi_mu-psi_e=(mu-e)R_mu(1+e R_e1)>0

inside I. Thus delta H is nonzero, as is

    E(delta h)=(e-mu)psi_mu T/(12a0).               (10)

A compact off-source observation can detect this difference. Multiplying
(9) by an arbitrary real amplitude gives arbitrarily different interior
observations with the same source and metric endpoint data. This does not
contradict uniqueness under u=v=0: (9) changes displacement-sector endpoint
data. It prices exactly what was imported into that uniqueness statement.
The effect is not a pure metric diffeomorphism because E(delta h)!=0.

## 6. The actual tangential obstruction to extending the estimate

For general B-dependent fields the quadratic form of -Box_B is

    integral w[|partial_t f|²+
      Cwarp^(-2)gSigma^(ab) partial_a f conjugate(partial_b f)].

Choose a small Sigma chart with a negative coordinate covector and a compact
amplitude, and multiply it by exp(iN x) in that direction and a fixed compact
t-profile. The leading N² contribution is strictly negative; lower-order
terms are O(N) or bounded. Normalizing its L² norm yields energies tending
to minus infinity, while still satisfying zero endpoint data. Real sine and
cosine components give the same conclusion for real fields. Thus the positive
bound A>=kappa²/8 is false on unrestricted tangential modes. Domain selection
cannot be inferred from the one-coordinate solution. This is an obstruction
to THAT estimate, not a theorem that every full tensor boundary problem fails.

## Evidence and next condition

The probe checks exact mass/gap/residue constants, original forced rows,
warped curvature, flux jump, original off-source coefficient and boundary
counterconstruction algebra, with wrong-sign/omitted-sector controls. The
universal existence, positivity, regularity, observation and high-frequency
arguments are the proofs above, not finite fixture counts. Independent
internal review checks them; no proof-assistant or external-expert certification.

The next physical construction needs a source/observation-compatible domain
for the actual localized radial-pressure source, retaining all B dependence,
and a justification for the additional boundary data. This TT source family
proves that conditional nonlocal response is possible; it cannot be promoted
to that missing construction. Another one-coordinate profile or contact
cofactor will not resolve the domain-selection debt.

[Probe](../../tests/channel-swings/k2550_common_domain_tensor_response_probe.py),
[report](../../lab/process/k2550-common-domain-tensor-response.json),
[original sector](k2544-constrained-tensor-response-2026-11-04.md),
[contact identity](k2548-compact-coupled-metric-detectors-2026-11-04.md).
