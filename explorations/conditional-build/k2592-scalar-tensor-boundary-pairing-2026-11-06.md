---
title: "K2592 Full pressure reciprocity reduced to finite boundary data and repaired"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact boundary defect and reciprocal source subclass on the existing preparation; reciprocal full smooth pressure response on a new preparation; not physical selection or inherited point-source bounds
scripts:
  - tests/channel-swings/k2592_scalar_tensor_boundary_pairing_probe.py
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
result: K2592
carrier: actual compact conserved radial-pressure sources and their scalar/TT response on the selected curved product LAYER=toy CHIRALITY=N/A
pairing: actual tensor contraction with invariant density; distinct scalar w2 and TT w5 coefficient densities ON=declared_carrier
real_structure: real order/conjugate-averaged inverse preparation from K2588
grading: source, TT amplitude, six scalar potentials, original metric and compact detector kept distinct
action_owner: repository-construction -- conditional curved-product completion
target: full source reciprocity boundary criterion and equation-preserving modal repair MAP-TYPE=evaluation
```

# Separate the actual boundary defect from the tensor bulk

## Result and scope

The full scalar/TT response to the ORIGINAL compact conserved radial-pressure source has an exact reciprocity defect supported on finite endpoint data. K2590 already proves TT response reciprocity. Here the actual cross tensor Gram is computed, its contribution cancels in the antisymmetric source pairing, and the remaining scalar cofactor defect is expressed by a polynomial Bezoutian. It has rank at most TEN per scalar radial/angular mode, rather than being an unknown bulk operator. This does not prove the defect is nonzero on the selected domain.

A nonzero infinite-dimensional family of actual conserved pressure sources is reciprocal against EVERY other admissible compact pressure source on the SAME preparation. A further construction checks the actual cofactor resultant against the actual radial spectrum and obtains an equation-preserving reciprocal full pressure response on a new fixed real preparation, with smooth all-mode synthesis. This repair explicitly changes the mathematical preparation. It is not a proof that the earlier preparation was already reciprocal, nor a physical choice of boundary conditions.

The underlying curved product and action completion are repository constructions. SC-ACT-01 ASSERTS its action, SC-GEO-03 ASSERTS Met(X), SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita, and SC-META-53 remains UNCERTAIN. Source polarities, ledger0.263 LT-GR6b/10/11 and LT-SM8, canon, native displacement, positivity and causal/physical selection remain unchanged. No novelty or external certification is claimed.

## 1. Actual tensor cross Gram

Use K2552/K2590 notation K=35kappa²/3624192, R=1/|kappa|, w2=C⁴S², w5=C⁶S⁴, alpha=C'/C, beta=S'/S, gamma=4alpha+2beta. The radial TT map is

    Rcal(b)=diag(t_b,b,a_b),
    t_b=-SC b'/4+(-3+7KS²)b/4,
    a_b= SC b'/2+(1-7KS²/2)b.

The actual six-potential realization has T_AA=fG_A+Hess_A p; its B and mixed entries do not contract with Rcal(b). Trace cancellation removes f. In the observer4/radial1/angular2 multiplicities,

    Rcal(b):Hess_A p=4t_b alpha p'+b p''+2a_b beta p'
                      =b p''+(b'+gamma b)p'.

The equality follows from the ACTUAL TT divergence equation. Hence

    <Rcal(b),T(f,g,p,q,r,s)>_A=[w2 b p']_0^R. (1)

The center term vanishes for smooth regular even amplitudes: w2=O(r²), p'=O(r). The same identity with p=chi gives <Rcal(b),L_A*chi>=[w2 b chi']. This is not scalar-L2 orthogonality. A zero-trace TT amplitude is orthogonal to every such scalar potential, while a general trace amplitude need not be.

Pairings are reduced per unit invariant observer volume with the A angular orbit volume normalized; B integrations use the inherited invariant density. No finite full-spacetime volume or conservation-breaking observer cutoff is assumed.

## 2. Full compact-source pairing and its sole remaining term

Keep the actual conserved pressure source j_A=diag(A/2,P/2,P/2) in its block multiplicities, with P'+4alpha(P-A)=0 and support away r=R, times smooth compact B dependence. Its exact split is

    j=L_A*chi+Rcal(b), t=(4A+3P)/2=-6(X+7K)chi,
    chi(R)=0, b=P/2+gamma chi'+6Kchi,
    b(R)=gamma(R)chi'(R).                      (2)

Arbitrary smooth compatible B dependence is allowed by linearity. K2590's original-metric TT amplitude H maps b=b0+a q to H_D b0+q H_q a, with a=b(R)/q(R). At R it is H_q b(R). Thus the complete TT contribution to <j1,h2> is

    B(b1,H b2)+w2(R)gamma(R)<chi1'(R),H_q chi2'(R)>_B. (3)

Both terms are symmetric: the first by K2590's actual tensor-Gram theorem, the second by the SAME real B preparation for H_q. No sign assumption on gamma is needed. The cross term has not been omitted.

For a compact conserved j, integration by parts removes its pairing with Hess_A p. Therefore <j,T(u)>=<t,f> even when the RESPONSE potential is not compact. Let E=X+Y+12K, G_E its real symmetric scalar inverse, Rd the real order/conjugate-averaged determinant inverse, and Ccof=adj(M)vsrc, vsrc=(-X-6K,0,1,0,0,0)^T. Put Pcof=e_f^T Ccof. The scalar contribution is exactly

    -(rE/2)<t1,(X+5K)G_E chi2>
      +rE²<t1,Pcof Rd chi2>, rE=-1144/(15kappa). (4)

The Einstein term is symmetric because the radial X preparation is the same self-adjoint Dirichlet spectral realization on each use, and G_E is symmetric in B. Cofactor reconstruction and its skew row remain present in the second term; a transpose of six Euclidean coefficient slots would not establish this formula.

Let X=-sigma be a scalar radial eigenvalue, ell,m the B angular labels, and lambda_sigma=6(sigma-7K)>0. Define P_sigma(Y)=Pcof(-sigma,Y), d_sigma(Y)=det M(-sigma,Y), and R_sigma=Rd at this mode. Then the ENTIRE original-metric reciprocity defect is

    Delta=<j1,h2>-<j2,h1>
         =rE² sum_(sigma,ell,m) lambda_sigma
           <chi1,(P_sigma R_sigma-R_sigma P_sigma)chi2>_B. (5)

For real angular bases the pairing is bilinear; equivalent conjugate paired complex-mode conventions give the same real result. Compact B inputs permit transfer of P_sigma onto the other factor. Equation(5) is exact on the existing compatible smooth source class and extends only where its sums/pairings are justified. Symmetry of R_sigma alone does NOT make this commutator zero.

## 3. An explicit finite boundary formula

Set U_i=R_sigma chi_i. Cramer's rule gives P_sigma by replacing column0 of the ACTUAL six-row M with vsrc, then taking its determinant. The probe computes the full polynomial numerator at kappa=1, proves degree_Y P=4 and degree_Y d=5, and checks all-six-row identities independently at exact fixtures. Homogeneous matrix scaling

    M_k(k²X,k²Y)=k D_k M_1(X,Y)D_k^-1,
    v_k(k²X,k²Y)=k²D_k v_1(X,Y),
    D_k=diag(1,1,k^-2,k^-2,k^-2,k^-2)

extends these degrees to every nonzero kappa. In particular d scales by k^6 and Pcof by k^7 in these variables.

Define the ordinary polynomial

    B_sigma(x,y)=[d_sigma(x)P_sigma(y)-P_sigma(x)d_sigma(y)]/(x-y)
                =sum b_ij x^i y^j.             (6)

It is symmetric and has degree at most4 in EACH variable. Define the B Green flux by <Yf,g>-<f,Yg>=[J_Y(f,g)] at the two annulus endpoints. In K2588's Liouville coordinate x, its normalization is

    J_Y(f,g)=-K^(-5/2)[(Jf)'Jg-Jf(Jg)'].       (7)

The sign and density are part of the result. Expanding(x-y)B in(6) and applying Green's identity term by term yields

    Delta=rE² sum lambda_sigma sum b_ij
           [J_Y(Y^i U1,Y^j U2)]_endpoints.     (8)

Only endpoint jets through order9 occur. Equation(8), restricted to the actual source class, is a necessary and sufficient vanishing criterion for reciprocity on that class. The polynomial is nonzero, but that fact does not prove its restriction to this preparation is nonzero. A separately labeled flat interval control checks the telescoping signs and a nonzero endpoint defect; it is not a curved pressure-source counterexample.

There is a stronger dimension statement. For compact B input chi, let D_sigma=P_sigma R_sigma-R_sigma P_sigma. Since the differential polynomials commute and d_sigma R_sigma=I,

    d_sigma D_sigma chi=0.                     (9)

The fixed-mode B radial ODE is regular of order10 with nonzero leading coefficient. Its homogeneous solution space has dimension10, so D_sigma has rank at most10 on these inputs. It is antisymmetric in the bilinear pairing, so any nonzero finite rank is even. This is a bound PER fixed radial/angular mode; the all-mode direct sum is not claimed finite rank. Also D_sigma d_sigma v=0 for compact v, because R_sigma d_sigma v=v and P_sigma v stays compact.

## 4. Same-preparation reciprocal full-source consumers

Choose v smooth compact in the B annulus and in an interior A radial interval; define

    chi=d(X,Y)E v, t=-6(X+7K)chi,
    P_pressure(r,B)=-2 C(r)^-7 integral_r^R alpha(s)C(s)^7 t(s,B) ds,
    A=(2t-3P_pressure)/4.                       (10)

Direct differentiation gives P_pressure'+7alpha P_pressure=2alpha t, equivalent to actual pressure conservation. Its trace is exactly t. It vanishes near R and is smooth even at the center: alpha=O(r), t is smooth even, and the integral has an even expansion. Pressure can extend inward to r=0; compact radial support here means support strictly inside the outer tube, not necessarily avoiding the center. The unique Dirichlet splitter for this t is precisely the constructed chi.

K2588's two-sided identity on compact test inputs gives the EXACT scalar solutions

    U=E v, w=d v.                             (11)

They satisfy dU=chi and Ew=chi on the SAME preparation, including every scalar/cofactor source row. The TT response remains the existing trace-compatible construction. Since chi is compact, its outer trace and derivative vanish; the boundary formula(8), or D_sigma d_sigma v=0 applied to Ev, proves the FULL original-metric response is reciprocal against every other actual admissible compact pressure source.

The family is genuinely nonzero. Choose v=eta(r)zeta(B), with eta=1 near an interior r*, and zeta a smooth cutoff times(t-t*)^12 in a noncharacteristic B radial chart; all other cutoffs equal1 near the test point. Its derivatives through order11 vanish there and the twelfth is nonzero. The leading B derivative in dE is L_kappa(g_B^{tt})^6 partial_t^12, with L_kappa!=0. At that point t_source has coefficient -42K L_kappa(g_B^{tt})^6 times that nonzero twelfth derivative; K!=0. Disjoint B supports give infinitely many linearly independent sources. These sources are generally SIGN-CHANGING; the result does not establish reciprocity for the separately motivated nonnegative matter-source subclass. No nonzero observed metric pairing is inferred solely from a nonzero source.

## 5. Execute the equation-preserving repair

The finite homogeneous defect suggests a concrete repair, not an assumed zero commutator. If d_sigma and P_sigma are coprime, choose Bezout polynomials A_sigma,B_sigma with

    A_sigma P_sigma+B_sigma d_sigma=1.

Set, for compact B chi,

    V=-A_sigma(Y)D_sigma chi/2,
    U_new=R_sigma chi+V.                       (12)

Equation(9) gives d_sigma V=0 and P_sigma V=-D_sigma chi/2. Consequently

    d_sigma U_new=chi,
    P_sigma U_new=(P_sigma R_sigma+R_sigma P_sigma)chi/2. (13)

Using Q_new=-rE T(Ccof U_new), keeping the Einstein and TT responses, and reconstructing the original metric and auxiliary field exactly as in K2552 preserves EVERY selected linear source equation, including the skew row. The new scalar volume transfer is symmetric. This is an explicitly CHANGED preparation; the old intermediate impedance or range traces are not also imposed.

### The actual cofactor has no resonance on the actual radial spectrum

The exact rational resultant at kappa=1 factors, up to a nonzero constant, as

    X³(3624192X+245)^4(39953092608X+611557655) F3(X) G3(X)^2,

    F3=115477741462089913860096 X³
       -129177230786889901634304 X²
       +4695605310234060958593 X+103146450706524329110,

    G3=825758752855751423013542710880363536738659980290377646080000 X³
       -217011059852567633631058836487116937474282161932248045589332070400 X²
       +14250307278499597489862324093863788455810295354642811227775748230672688 X
       +391738308802982309734173497966067973893941259445873366944953540838991043.

The report records the full normalization. The linear roots are above-3. Every coefficient of F3(-3-z) is negative for z>=0. G3 is strictly increasing for X<0 since its derivative coefficients have the required signs there, and its unique negative root lies STRICTLY between-28 and-27, by exact substitution. Thus simple sigma>=3 alone would not settle coprimality; the isolated possible resonance must be checked against the ACTUAL spectrum.

Put c0=1-(7/3)KR²>.99. K2552's actual weight obeys c0 r²<=w2<=r². Rayleigh quotient comparison and the min-max principle against the regular three-dimensional radial Dirichlet problem yield

    c0 n² pi² kappa² <= sigma_n <= n² pi² kappa²/c0.

The regular-center comparison problem has eigenvalues n²pi²/R², n>=1, by u=r f and Dirichlet u(0)=u(R)=0. From3<pi<22/7, sigma1<10kappa² while sigma_n>35kappa² for n>=2. No scaled eigenvalue hits(27,28). Scaling therefore proves Res_Y(d_sigma,P_sigma)!=0 for EVERY actual scalar radial eigenvalue. The repair(12) is available in every radial/angular mode. Exact extended-Euclidean fixtures check its full Bezout identity and half-defect cancellation; these fixtures illustrate the algebra, while spectral exclusion proves applicability to actual modes.

### All smooth modes, with an explicit loss boundary

The repair extends to every smooth compatible actual pressure source compact in B, not only finite spectral sums. This requires an estimate in addition to modewise invertibility. Solve the Sylvester linear system for A_sigma (degree at most4 in Y) and B_sigma using its adjugate and determinant. Its entries are polynomials in sigma, and its determinant is the computed resultant. Thus their coefficients are rational functions of sigma, with at most polynomial numerators and this fixed polynomial denominator.

After scaling by kappa², the actual spectrum lies in the two CLOSED sets[3,10] and[35,infinity). The denominator has no zeros on either set. Its reciprocal is bounded on every compact portion and has polynomial behavior at infinity, since its leading coefficient is nonzero. Hence every Bezout coefficient has at most polynomial growth on the whole actual spectrum, without an unsupported uniform constant across arbitrary kappa. Fix nonzero kappa as in the original preparation.

The inherited K2584 scalar inverse estimates bound every fixed B radial derivative with a polynomial loss in the joint radial/angular scale. A_sigma, P_sigma and d_sigma contain finitely many Y derivatives and polynomially bounded radial multipliers; R_sigma acting on their differentiated compact input has the same kind of bounds. Therefore D_sigma and V in(12), followed by the finite cofactor tensor reconstruction, have only a finite polynomial loss for each fixed smooth seminorm. Original compact radial-pressure t belongs to every power of the regular radial Dirichlet operator; chi=(-X-7K)^-1 t/6 has rapidly decaying compatible coefficients. B derivatives and the polynomially bounded radial multipliers preserve that rapid decay. Smooth compact B coefficients also decay rapidly in angular labels. The existing regular-center Cartesian compatibility and termwise differentiated synthesis therefore apply to U_new, Q_new, h_new and the reconstructed auxiliary field. The convergent sums justify the symmetric pairing in(13) and give FULL pressure-source reciprocity on this new preparation.

This constructs a fixed real linear response prescription for the full stated smooth pressure class. It does not assert a self-adjoint full tensor operator or the old impedance traces. If changing the splitter representative, extend the existing synchronized direct overlap prescription from this new Dirichlet base; do not apply the Dirichlet inverse to the non-Dirichlet overlap psi. The source-source theorem uses the original fixed splitter in(2).

No numerical Sobolev exponent for the new polynomial correction is derived here. In particular the earlier point-source H^-43/H^-44 and O(epsilon) estimates are NOT carried over to the repaired preparation. Measure-source extension requires its own quantified derivative-loss calculation. The same-preparation full-source family in section4 remains an independent result on the old preparation, established before and without the repair.

## Verification and next condition

The changed question is now precise: determine whether the old domain's finite boundary form vanishes, quantify the repaired preparation's distribution/measure-source loss, or identify an independently justified physical boundary/readout. Do not requeue the tensor cross Gram, the finite-rank reduction, actual resultant, repaired smooth response or reciprocal compact-range source family as missing. Any repair must retain the original-metric shift, full cofactor/skew system and source halves; a symmetric scalar matrix alone is insufficient. Independent physical boundary/readout selection and native displacement remain separate.

[K2590](k2590-boundary-aware-response-adjoint-2026-11-06.md), [K2588](k2588-real-boundary-response-2026-11-05.md), [K2552](k2552-localized-source-domain-2026-11-04.md), [K2548](k2548-compact-coupled-metric-detectors-2026-11-04.md), [probe](../../tests/channel-swings/k2592_scalar_tensor_boundary_pairing_probe.py), [report](../../lab/process/k2592-scalar-tensor-boundary-pairing.json).

Independent read-only field specialists and a distinct integrated hostile reviewer found no remaining substantive findings after scope and probe repairs. K2592 passes50 exact supporting checks and9 contrary controls; K2593 passes41 and6. Universal boundary, spectral-synthesis, convexity and all-policy proofs remain separate from algebraic fixtures, interval certificates and actual finite consumers. No external-expert, proof-assistant, remote-CI or physical certification.
