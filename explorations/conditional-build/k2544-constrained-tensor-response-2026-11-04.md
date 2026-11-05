---
title: "K2544 Constraint-preserving curved tensor response and its data domain"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: prescribed-source response in an exact curved tensor sector and scoped ordinary Cauchy obstruction; no arbitrary localized inverse, physical domain or native GU claim
scripts:
  - tests/channel-swings/k2544_constrained_tensor_response_probe.py
---

# K2544 Construct the constrained sector before choosing an inverse

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
result: K2544
carrier: original ambient metric and grade-one displacement on stationary fourteen-dimensional Einstein product with a nonzero curved TT tensor LAYER=toy CHIRALITY=N/A
pairing: inherited indefinite action contraction and compact smooth tensor test densities ON=declared_carrier
real_structure: real nonzero kappa, product signature (7,7), analytic local space forms
grading: original metric, shifted Einstein variable, symmetric displacement and skew field remain distinct
action_owner: repository-construction -- selected comm/symi/symi I1 completion with moving soldering
target: prescribed tensor-class source, original readout and explicitly typed local data domain MAP-TYPE=evaluation
```

## Result and boundary

An explicit nonzero transverse-traceless (TT: zero divergence and trace) curved tensor closes the COMPLETE selected-action equations into two scalar equations. This gives local distributional solutions for arbitrary prescribed forcing within this tensor source class, and selected analytic germs for analytic forcing and supplied analytic data. The original metric retains both poles. A finite gauge-invariant tensor probe detects homogeneous modes that the preceding scalar-curvature probe cannot see.

The scalar sector also fails a precise unrestricted ordinary Cauchy well-posedness requirement on every nonnull product-B-normal slice. This uses a checked necessary theorem for the actual variable-coefficient operator, rather than transferring a flat symbol rank into a global verdict. Analytic data and restricted nonlocal/boundary alternatives survive. A flat donor calculation prices one such alternative, including its incompatibility with a nonzero source compact in all tangential coordinates.

SC-ACT-01 ASSERTS its first-order action, SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita, SC-GEO-03 ASSERTS Y=Met(X), and SC-META-53 remains UNCERTAIN about indefinite spectra. The independent ambient metric and selected I1 completion here retain their conditional status. Ledger0.263 GR6b/10/11, source polarities and physical-quotient/native-Met(X) debts are unchanged. The source class below is neither K2531's actual radial-pressure observer source nor a general conserved tensor. No GU verdict, physical Green function or empirical prediction follows.

## 1. Build a nonzero curved invariant tensor

Use the stationary product A times B, both seven-dimensional space forms with Ric=lambda G, lambda=35kappa^2/604032>0, K=lambda/6. The B signature is (3,4); A carries the complementary (4,3). All constructions are local. Choose an analytic scalar f on A satisfying

    Box_A f=-7K f,
    T=Hess_A f+K f G_A.                            (1)

Then

    tr_A T=0, div_A T=0,
    nabla_j T_ik-nabla_k T_ij=0,
    Box_A T=7K T.                                 (2)

For divergence, use div Hess f=d Box f+6K df. The Codazzi equation follows by the space-form commutator on df, whose curvature term cancels the differentiated KfG. For the final identity, the parallel-Ricci Hessian formula is

    Box Hess f=Hess Box f+14K Hess f-2K G Box f.

Substituting (1) and adding K(Box f)G gives the last line of (2). These are full curved identities; setting curvature to zero would change the result.

Nonzero T is a real prerequisite. In analytic normal coordinates at p choose a nonnull analytic Cauchy hypersurface, two tangential coordinates x1,x2 of the same metric sign, data f=x1^2-x2^2 and zero normal derivative. At p, f=df=0 and the tangential Hessian is nonzero and tracefree. The scalar PDE fixes the normal second derivative and is noncharacteristic. The analytic Cauchy theorem gives a local germ with T(p) nonzero. Ambient-coordinate eigenfunctions instead can satisfy Hess f=-KfG and give T=0; those are rejected witnesses. The theorem used is [Mizohata, Lectures on Cauchy Problem (1965), Chapter1 section3 Theorem1, printed p8](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr35.pdf). Its analytic coefficient/data hypotheses hold on these local space forms.

## 2. Substitute into every full equation

Reuse the actual reduced action and full covariant equations of [K2537](k2537-reduced-action-decoupling-2026-11-04.md) and [K2539](k2539-covariant-tensor-constraints-2026-11-04.md), not merely a symbol restriction:

    a0=-5kappa/2288, mS=158kappa/143, mH=893kappa/858,
    C=u(B)T, K_skew=0, z=v(B)T, j=J(B)T,
    D=Box_B.

The source j is conserved: div_A T=0, the connection is a product and no B index of j receives a derivative of J. The tensor has tau=0,b=div C=0,v_constraint=0,w=0. Hence the complete skew equation is zero. The symmetric equation contains no vector or trace term. Since Riem_A T=-K T and Box C=(D u+7K u)T, the K2539 hook divergence and Einstein linearization become

    S=2Box C-2lambda C+2Riem C=2(Du)T,
    E(C)=-(D+5K)uT/2.                             (3)

Mixed and B tensor components vanish as actual tensors, not by discarding their equations. The product Weyl contribution is included through Riem_A T=-KT. The remaining symmetric row and Einstein row are therefore exactly

    (D+e)v=J/(6a0),
    c(D+mu)u=-J/(6a0),                            (4)
    e=5K=175kappa^2/3624192,
    c=-4/mH-1/(6a0)=970112/(13395kappa),
    b_mass=mS-5K/(6a0)=136967kappa/123552,
    mu=b_mass/c=611557655kappa^2/39953092608.

The full original solution is

    h=(v-u/(6a0))T=H T,
    Q=C, e2=-A2^(-1) BQ,

with the other reduced grades zero as licensed by K2535's full grade-preservation result. A2 is the already proved algebraic auxiliary inverse; no new differential inverse is smuggled into its reconstruction.

For any distribution J, the separate second-order scalar factors in (4) are of real principal type: the nondegenerate principal quadratic form has nonzero covector derivative away from the zero section on its characteristic cone. The local distributional solvability theorem already applied and precisely cited in [K2541 section4](k2541-prescribed-product-source-response-2026-11-04.md) applies to each factor; shrink to a common chart. No theorem is applied directly to their fourth-order product. For analytic J, a supplied nonnull analytic B hypersurface and analytic values of u,normal-derivative u,v,normal-derivative v select unique analytic sector germs by the same analytic theorem. This is existence/selection within the sector, not arbitrary-source global uniqueness or stable unrestricted evolution.

## 3. Keep both forced sectors in the original readout

Write formally

    rE=1/(6a0)=-1144/(15kappa),
    rT=1/(36a0^2 c)=127699/(1590kappa).

These denote the coefficients of the two particular scalar solution maps if compatible maps are supplied; they are not an assertion that a unique inverse exists. Eliminating (4) directly gives an inverse-free identity for every constructed solution:

    (D+e)(D+mu)H
       =[429 D/(106kappa)-70547kappa/60632]J.       (5)

Both residues are nonzero, and

    mu-e=67736495kappa^2/4439232512>0.

The numerator evaluated at either pole is nonzero. Thus neither forced sector disappears from h. Identifying z with h, dropping the shifted tensor source or merging the distinct scalar factors changes the response. Signs of residues in an indefinite action do not prove physical positivity or ghosts without the actual state/quotient/domain.

## 4. A finite tensor observation sees the scalar blind sector

Take J=0,v=0 and a nonzero local analytic solution (D+mu)u=0. Such a germ exists by analytic Cauchy data. Then

    Rh=delta R[h]=0,
    E h=(e-mu)uT/(12a0)
       =13547299kappa uT/23282688 !=0.             (6)

The preceding K2543 scalar-curvature detector is blind to this mode. For any compact smooth symmetric test W, with invariant density included, define

    O_W=<h,E W>=<E h,W>.                          (7)

Formal self-adjointness of E follows from the Einstein quadratic action; E Lie_xi G=0 on this Einstein seed, so (7) is invariant under linearized diffeomorphisms. E W is conserved. Distributional h can always be paired with the compact smooth E W, so this is a finite observation with an explicit domain. Choose a compact dual component where uT is nonzero to obtain O_W!=0. An indefinite squared norm could vanish and is not used to infer detectability.

Adding this full homogeneous solution changes the metric tensor observation at fixed source while leaving Rh and K2543's joint scalar contact identity unchanged. It is an actual obstruction to source-only uniqueness of metric readout. It does not prove every fixed detector sees every high-frequency sequence, nor that an experimental detector couples to (7). Once analytic sector data are supplied, its local value is selected; general physical boundary/readout data remain unselected.

## 5. Test the ordinary product-slice Cauchy prescription precisely

For either scalar factor D+mass, choose any nonnull B covector n. Since both signature indices of B exceed one, its orthogonal complement contains a nonzero eta with the same sign q(eta) as q(n). Thus

    q(eta+zeta n)=q(eta)+zeta^2 q(n)

has nonreal roots in zeta. The actual curved scalar principal symbol therefore fails hyperbolicity with respect to every nonnull B-normal direction.

The applicable necessary result is [Iwasaki (1983), Definition1.1 and Theorem1.1, printed p929](https://ems.press/content/serial-article-files/42165): his local noncharacteristic Cauchy well-posedness formulation requires real characteristic roots. Both scalar factors have smooth coefficients and noncharacteristic n, so neither meets that formulation. In particular an ordinary unrestricted sourced Cauchy prescription cannot be asserted for this sector; this is not a proof of failure for every domain of the full coupled theory.

The scope matters. The theorem is applied to the actual scalar variable-coefficient operator, not inferred from a finite-rank symbol or a generic signature slogan. Analytic germs in section2 do not contradict it. No conclusion is made for characteristic data, nonlocal restricted data, other boundary realizations, the actual radial-pressure source, a physical quotient or observed-dimensional reduction. The existing [ultrahyperbolic correction](../../lab/sources/literature-ultrahyperbolic-wellposedness-2026-08-08.md) and path-dependency warning remain valid.

## 6. Price a concrete alternative on a flat donor

This section is deliberately a FLAT donor, not a constructed projector on the curved product. In signature (3,4), select one negative time t. For the scalar equation (Box+mass)u=0, Fourier transform the other coordinates into three positive directions xi and three negative directions eta. Then

    u_tt=(|eta|^2-|xi|^2+mass)u.

For two-sided oscillatory evolution of both factors a sufficient common support restriction is

    sigma=|xi|^2-|eta|^2>=mu>e,

with sigma>=mu+delta,delta>0 giving a gap for the usual frequency-adapted oscillator energy. This is not an isotropic elliptic Sobolev estimate on all tangential frequencies: sigma can stay bounded while |xi|+|eta| grows. It is a specified spectral restriction, following the distinction between two-sided center data and one-sided stable data in [Craig and Steven Weinstein, section2](https://arxiv.org/pdf/0812.0210). A one-sided decay prescription has different data and is not ruled out here.

There is a source cost. If a source at fixed time is compactly supported in all six tangential coordinates, its Fourier transform is entire. The exact support restriction forces it to vanish on a nonempty open unstable region, so analytic continuation forces the entire transform, and hence that source, to be zero. Therefore a nonzero compact tangential source cannot obey this exact center-support rule. This does not exclude noncompact source tails, a different boundary prescription, a nontranslation-invariant curved construction or a weaker spectral condition.

The original readout does not secretly cancel the flat donor's bad modes. At an extra-time Fourier frequency N, zero-data constant-in-time forcing gives

    H(t)=rE[1-cosh(sqrt(N^2+e)t)]/(N^2+e)
         +rT[1-cosh(sqrt(N^2+mu)t)]/(N^2+mu).

For fixed t>0, its leading large-N term is

    -429 exp(Nt)/(212kappa N^2),

because rE+rT=429/(106kappa)!=0. This is an explicit forced donor control, not an unproved transfer of that precise solution to the curved geometry or a claim about every fixed detector's Fourier sensitivity.

## Evidence and next construction

The exact probe recomputes curved TT commutator coefficients, all original forced rows, shifted/original reconstruction, residues/pole distinction, scalar-blind tensor detection and principal-root controls. Universal tensor identities, local theorem applications and analytic Fourier-support arguments are distinct from finite algebra and report consistency. Independent internal review checks those seams; no external-expert, proof-assistant, physical positivity or novelty certification is claimed.

The work removes the need to guess that componentwise scalar inversion preserves TT constraints: the explicit carrier proves it for this sector. It also identifies the additional domain problem that an arbitrary localized response must solve. The next substantial construction is an actual curved restricted/source-compatible domain, or a different justified observed reduction retaining original readout. The radial-pressure source still requires its own full response; this tensor class cannot stand in for it. Further finite ranks or a repeated unrestricted Cauchy assertion would not discharge that obligation.

[Probe](../../tests/channel-swings/k2544_constrained_tensor_response_probe.py), [report](../../lab/process/k2544-constrained-tensor-response.json), [K2543](k2543-localized-source-readout-2026-11-04.md).
