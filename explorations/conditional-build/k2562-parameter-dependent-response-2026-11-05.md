---
title: "K2562 Uniform radial inverses by switching the outer condition"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: uniform weighted radial inverse bounds and polynomially controlled supplied-family synthesis; no B point-source representation or physical preparation
scripts:
  - tests/channel-swings/k2562_parameter_dependent_response_probe.py
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
result: K2562
carrier: actual compact smooth radial pressure on the selected curved A7 times B7 product LAYER=toy CHIRALITY=N/A
pairing: radial weighted L2 and distribution duality with compact smooth conserved metric tests ON=declared_carrier
real_structure: real sources and real parts of complex factor solutions
grading: scalar/TT potentials and original metric remain distinct
action_owner: repository-construction -- selected comm/symi/symi product completion
target: full-source parameter-dependent response and supplied-family observation MAP-TYPE=evaluation
```

# K2562 Remove the radial resonance and growth obstruction

## Result and exact scope

For each complex spectral parameter, one of two fixed radial outer boundary conditions gives a uniformly bounded inverse for each of K2560's radial operators. Selecting that inverse separately for the actual five determinant factors yields a full response to the actual compact radial source with uniform weighted potential bounds and polynomial parameter growth of every finite derivative seminorm. This replaces the center-zero inverse's exponential growth and fixed-Dirichlet resonances. It extends K2560 from bounded to suitably polynomially integrable supplied real B eigenfamilies.

The selected boundary conditions are mathematical preparation, not source-selected physics. Their switches may be discontinuous. There is no root-order independence, causal Green prescription, full-system uniqueness, or representation of delta_B. SC-ACT-01/GEO-03/GEO-55 remain ASSERTS and SC-META-53 remains UNCERTAIN. Ledger0.263 LT-GR6b/10/11/SM8 and all native GU judgments remain unchanged. The conditional product/action/source objects retain K2552/K2560's typing.

## 1. Two fixed radial self-adjoint problems

Fix nonzero real kappa, K=35 kappa^2/3624192, R=1/abs(kappa), x=sqrt(K)r. Write C=cos(x), S=sin(x)/sqrt(K), and

    L2=X=d_r^2+(4alpha+2beta)d_r, w2=C^4 S^2,
    L4=D5=d_r^2+(6alpha+4beta)d_r, w4=C^6 S^4.

Set s_m=sqrt(w_m), h=s_m f. Unitary multiplication from L2(w_m dr) to L2(dr) sends A_m=-L_m to

    H_m=-d_r^2+V_m, V_m=s_m''/s_m,
    V2=2K tan^2(x)-7K,
    V4=2/r^2+W4,
    W4=6K tan^2(x)+2K[cot^2(x)-1/x^2]-17K.       (1)

Use the regular radial endpoint at0. For m2 this is h(0)=0 (the excluded constant h branch means f~1/r); for m4 it is the Friedrichs endpoint of 2/r^2 (regular h~r^2, excluded h~1/r). At R choose either D:h(R)=0 or N:h'(R)=0. N is the fixed Robin condition f'(R)+(s_m'/s_m)(R)f(R)=0, NOT ordinary f'(R)=0. The two forms have compact resolvent: for m2 the usual finite-interval H1 form, and for m4 its subspace with integral 2|h|^2/r^2 finite; the compact H1-to-L2 embedding applies. The smooth bounded potential perturbation does not change these form domains.

For 0<x<=sqrt(35/3624192), sin(x)<=x, tan(x)>=x and cos^2(x)>=1-x^2 give

    -1 <= cot^2(x)-1/x^2 <=0,
    tan^2(x)<=x^2/(1-x^2)<=2x^2.

Consequently |V2|<=8K and |W4|<=19K, including their removable limits at0. These are actual tube bounds, not numerical sampling.

## 2. Uniform separation of the two spectra

For the unperturbed m2 operator, positive frequencies are n*pi/R (D,n>=1) and (n-1/2)*pi/R (N,n>=1). For m4, a regular solution at frequency k is h(r)=sin(kr)/(kr)-cos(kr). Its D roots x_n and N roots y_n obey

    (n+1/4)pi < x_n < (n+1/2)pi,
    (n-1/4)pi < y_n < n*pi, n>=1.                (2)

For D, tan x=x has one root in (n*pi,n*pi+pi/2), and tan((n+1/4)pi)=1<(n+1/4)pi. For N, h' has numerator (x^2-1)sin x+x cos x. At (n-1/4)pi it has sign (-1)^(n+1), because x^2-x-1>0; at n*pi it has sign (-1)^n. The standard separated-endpoint variational interlacing gives exactly one N eigenvalue below the first D eigenvalue and one between consecutive D eigenvalues; positivity excludes nonpositive eigenvalues. The sign brackets find one in each such gap and therefore exhaust them. Interlacing itself follows by the codimension-one restriction h(R)=0 of the N form domain and the minmax principle; equality is excluded by ODE uniqueness if both outer value and derivative vanish. No B-signature spectral theorem is being invoked.

Every D/N frequency pair is separated by at least pi/(4R), with sum at least pi/R, so every pair of unperturbed energies is separated by at least pi^2/(4R^2). The bounded-potential Rayleigh quotient inequalities shift the nth eigenvalue by at most19K (8K suffices for m2). Therefore the actual curved spectra obey

    dist(spec A_m,D, spec A_m,N)>=delta,
    delta=pi^2/(4R^2)-38K >2/R^2.                 (3)

The final strict inequality follows already from pi>3 and 38KR^2=1330/3624192<1/4.

## 3. A bounded right inverse for every complex parameter

For z in C let d_D=dist(-Re z,spec A_m,D), d_N similarly. Choose D if d_D>=d_N and N otherwise, resolving ties by D. Both distances cannot be below delta/2, since that would put one eigenvalue from each spectrum less than delta apart. For the chosen self-adjoint operator,

    G_m(z)=-(A_m,choice+z)^(-1),
    (L_m-z)G_m(z)F=F,
    ||G_m(z)||_(L2(w_m)->L2(w_m))<=M=2/delta<R^2. (4)

Indeed complex distance is no smaller than the real distance and the orthonormal eigenfunction expansion bounds the inverse by the reciprocal distance. This proves the bound for all complex z, not just the real axis. Distance functions are continuous and tie-breaking is Borel; the selected inverse is strongly Borel, though not generally continuous. A fixed D or N choice alone still has poles at minus its eigenvalues. This is an explicitly parameter-dependent preparation.

## 4. Consume every factor of the actual compact-source problem

Keep the exact compact conserved A,P and Dirichlet splitter chi_D,b_D of K2560, including their cancelling source tails. Its full determinant d(X,nu), from K2554, has total degree5, constant nonzero leading X coefficient L, and the mixed X*nu*Q0(X+nu) term. For real nu choose a Borel ordering of the five complex roots z_j(nu), with multiplicities, and put

    v=rE G4(16K-nu)b_D,
    u=-(rE/c)G4(21K-mu-nu)b_D,
    w=G2(-nu-12K)chi_D,
    f0=chi_D/L, fj=G2(z_j)f_(j-1), U=Re f5.      (5)

Real source data make v,u,w real; d has real coefficients, so taking Re preserves d(X,nu)U=chi_D. Sequential cancellation is from the last factor backward: (X-z5)f5=f4, then (X-z4)f4=f3, and so on. Differential factors commute, but no commutation of inverse operators is asserted. Repeated roots are admitted. Root order and outer conditions are supplied data, not physically irrelevant choices.

In the respective weighted spaces,

    ||U||_2<=M^5 |L|^-1||chi_D||_2,
    ||w||_2<=M||chi_D||_2,
    ||v||_4<=|rE|M||b_D||_4,
    ||u||_4<=|rE/c|M||b_D||_4.                  (6)

All four scalar equations of K2552 are now solved through the actual radial cutoff. Reuse its full reconstruction z_TT=R(v)rho, Q_TT=R(u)rho, z_scalar=-(rE/2)S0(w rho), Q_scalar=-rE T[adj(Mscalar)vsrc(U rho)], h=z-rE sym Q, e2=-A2^-1 BQ. This retains skew, mixed, auxiliary, source-half and original-metric rows. It is not just a solution of a restricted Hessian block.

## 5. Polynomial regularity and an unbounded-family consumer

The normalized determinant coefficients of X^j have degree at most5-j in nu. Rescaling X=(1+|nu|)xi bounds all monic coefficients uniformly, hence the elementary Cauchy root bound gives |z_j|<=C_kappa(1+|nu|). This improves the crude unrescaled root bound but does not constrain an indefinite B spectrum.

For fixed m, regard a smooth-even f(r) as a smooth radial function on the ordinary auxiliary Euclidean ball of dimension m+1. L_m is its radial Laplacian plus a smooth radial first-order drift: w_m/r^m is smooth positive even. These auxiliary elliptic balls are an estimate device, not the signature of B or of the physical theory. Both fixed outer choices are smooth Dirichlet or Robin conditions. Their elliptic estimate, taking the maximum of the two constants, is

    ||f||_(H^(q+2)) <= C_q[||F||_(H^q)+(1+|z|)||f||_(H^q)], q>=0. (7)

The weighted norm is equivalent to the ball L2 norm. Starting with (4), induction for even orders yields

    ||G_m(z)F||_(H^(2j)) <= C_j(1+|z|)^j ||F||_(H^(2j)), j>=0.

No higher boundary compatibility is assumed on F; global elliptic regularity for a homogeneous D/Robin solution uses its Sobolev forcing, not powers of the operator domain. Applying this deliberately conservative estimate five times and using Sobolev embedding gives a polynomial bound for every radial derivative seminorm of U; v,u,w satisfy the single-factor version. Finite-order tensor reconstruction adds only finite powers of nu and finite B derivatives. Therefore for each compact radial/test seminorm there is a finite integer p and finite constant C, determined by that seminorm, kappa and the fixed smooth source, with response seminorm <=C(1+|nu|)^p times the supplied B-distribution seminorm.

Let a measurable real parameter family rho_j in H^s of a fixed B chart satisfy Y rho_j=nu(j)rho_j. If for every finite p needed by the chosen response/test regularity

    integral (1+|nu(j)|)^p ||rho_j||_(H^s) d|sigma|(j)<infinity,  (8)

then (5), with its Borel prescription, is integrable in the corresponding lower Sobolev/distribution spaces. Differentiation and the full linear equations pass through the Bochner integral. This constructs the actual radial source tensor integral rho_j d sigma for unbounded real nu, with continuous compact smooth metric-test observations under the weighted data norm. If smooth radial dependence of all orders is desired, require all polynomial moments. For a fixed finite-order distributional equation/test only finitely many are needed.

A concrete conservative consumer is available: the actual six-by-six scalar matrix entries have total degree at most2 in (X,Y), so its five-by-five cofactors have degree at most10 and the source column raises this to11. Tensor reconstruction adds at most2 spatial derivatives, and auxiliary B adds1, giving at most25 derivatives; use safe margins DA=DB=26. Taking j=15 in the five-factor H30 estimate and allowing nu-degree11 gives p=5*15+11=86. Thus the single sufficient nonsharp condition integral (1+|nu|)^86 ||rho_j||_(H^s) d|sigma|<infinity controls all reconstructed fields locally in C0(A;H^(s-26)(B)), their distributional equations and compact metric-test observations, for the fixed smooth radial source. Constants depend on kappa, source H30 norms and the compact region; this is not an optimal moment requirement.

This does not assert that delta_B, or arbitrary B distributions, possess (8). An indefinite B operator has no automatic positive-Hilbert spectral resolution; its representation/completeness and measure are distinct missing inputs. The prior inverse-growth obstruction has been removed, not that representation problem.

## 6. Synchronized splitter overlap and remaining choices

Use the chosen response of the Dirichlet splitter as base. For chi=chi_D+a psi and b=b_D-a b_psi, retain K2558's synchronized overlap corrections q=rho/[c(nu+mu)] and W=rho/(nu+5K). Away from both poles, Q is unchanged and the original metric changes only by the specified infinitesimal diffeomorphism. For |nu+mu|,|nu+5K|>=epsilon>0, the overlap introduces bounded rational multipliers and (8) still suffices. At the two poles (5) itself remains valid; this particular single-eigenspace synchronization formula does not. No claim of continuity through a pole or independence of independently switched scalar/TT inverses is made.

The next useful construction is an actual B distribution representation/domain for localized data compatible with these polynomial estimates, or a direct domain that bypasses it. A new physical boundary condition remains a separate selection. Repeating bounded-mode existence or claiming all-domain nonexistence from the old inverse poles is now dominated.

## Verification

The probe checks the curved conjugation potentials, root-bracket sign algebra, strict tube margin, actual determinant degree/coefficient growth, independent flat boundary responses and resonance controls. Universal spectral, regularity and synthesis arguments are the proof above; finite checks are not their replacement. K2552/K2554/K2558 reconstruction evidence is reused at its unchanged hypotheses. Independent internal specialist and integrated review are required; no external-expert, proof-assistant, novelty or physical certification.

The explicit flat regular function is the elementary spherical-Bessel formula in [NIST DLMF 10.49](https://dlmf.nist.gov/10.49); the proof uses its displayed elementary form and endpoint comparison directly.

[Probe](../../tests/channel-swings/k2562_parameter_dependent_response_probe.py), [report](../../lab/process/k2562-parameter-dependent-response.json), [K2560](k2560-compact-source-response-2026-11-05.md).
