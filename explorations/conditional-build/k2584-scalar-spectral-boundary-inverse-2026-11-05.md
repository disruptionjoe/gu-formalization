---
title: "K2584 Scalar cofactor inverse on a fixed spectral boundary preparation"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: all-mode scalar cofactor right inverse and actual compact-source response under chosen spectral traces; no physical selection
scripts:
  - tests/channel-swings/k2584_scalar_spectral_boundary_inverse_probe.py
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
result: K2584
carrier: scalar and trace-controlled radial TT source modules of the selected curved seven-plus-seven system LAYER=toy CHIRALITY=N/A
pairing: indefinite tensor-test duality and auxiliary positive Sobolev norms ON=declared_carrier
real_structure: real data; complex impedance explicitly represents two real quadratures
grading: scalar amplitudes, TT tensor, shifted and original metric, auxiliary grade2 kept distinct
action_owner: repository-construction -- stated conditional model
target: scalar cofactor domain and full prescribed-source response MAP-TYPE=evaluation
```

# Complete the scalar complement with explicit boundary traces

## Result and scope

The actual scalar determinant admits a fixed, input-independent spectral boundary preparation on the same B annulus as K2580/K2582. Its FIVE roots are confined uniformly using the full mixed determinant, and complex factors have polynomial inverse bounds with sign-adapted impedance. Ten explicit traces define the order-ten cofactor problem. Repeated roots need no partial fractions or root-gap bound.

The released source consumer is consequential: the actual compact smooth radial-pressure source automatically satisfies the otherwise nontrivial TT residual compatibility after K2582's trace lift. Composing the scalar and TT constructions therefore solves all four K2552 response equations for that prescribed source class on this fixed annulus. This does not replace the different full-source constructions already obtained in K2562/K2564.

This is conditional mathematics on a repository-selected curved product and action completion. SC-ACT-01, SC-GEO-03 and SC-GEO-55 remain ASSERTS; SC-META-53 remains UNCERTAIN. Ledger0.263 LT-GR6b/10/11 and LT-SM8, canon and physical selection are unchanged. No causal evolution, calibrated observation, native Met(X) realization, unique physical response or novelty is claimed. Complex auxiliary fields represent two real quadratures; their real final response solves the real equations but generally not the same complex homogeneous trace prescription by itself.

## 1. Scalar radial spectrum and the ACTUAL determinant

Use kappa!=0, K=35kappa²/3624192, R=1/|kappa| and K2552 notation S,C,alpha,beta. The scalar operator

    A2=-X, X=partial_r²+(4alpha+2beta)partial_r,
    w2=C^4 S²

has regular-center/Dirichlet realization on L²(w2 dr), with eigenvalues sigma>=3kappa². Conjugation by sqrt(w2)=C²S gives an ordinary one-dimensional Dirichlet Schrödinger operator with bounded smooth potential at the center; thus compact resolvent and the usual smooth radial spectral calculus hold. The TT operator A5=-D5 has weight C^6S^4 and a DIFFERENT basis, with gap5kappa². No common-eigenfunction claim is made.

K2554's complete six-row matrix has

    d_kappa(X,Y)=kappa^6 d1(X/kappa²,Y/kappa²),
    d1(X,Y)=P(X+Y)+XY Q(X+Y),
    L=leading(P)=-2605746313310516251459584/22521658027326625.

Q is nonzero of degree2. The coefficient bank is in the K2554 report; the probe checks its actual matrix at independent rational points and retains this mixed term. Put s=sigma/kappa²>=3, Z=Y/kappa²-s. Then

    d1(-s,Z+s)/L=Pnorm(Z)-s(Z+s)Qnorm(Z),
    Pnorm=Z^5+p4 Z^4+...+p0.

The exact rational coefficient inequalities are

    |p4|<9/8, |pj|<1/32 (j=0,1,2,3), |qj|<1/10^8 (j=0,1,2).

On |Z|=r=s/2>=3/2, the ratio of every term other than Z^5 to |Z|^5 is at most

    3/4+(1/32)(4/9+8/27+16/81+32/243)
      +(6/10^8)(2/3+4/9+8/27)
      =4759375513/6075000000 <4/5<1.              (1)

For the mixed part use s=2r and |Z+s|<=3r. Rouché's theorem now places ALL five roots y_j of d_kappa(-sigma,Y), with multiplicities, inside

    |y_j-sigma|<sigma/2.                          (2)

This is an all-sigma analytic bound, not sampled root finding. It gives Re y_j>sigma/2 and |y_j|<3sigma/2. The scalar Einstein root yE=sigma-12K also satisfies these inequalities since12K<sigma/2. The cofactor root structure cannot be inferred from P alone.

## 2. A uniform complex-factor inverse

On the B annulus t in[asinh1,asinh2], retain

    zeta=sinh²t in[1,4],
    x=log[tanh(t/2)/tanh(asinh1/2)] in[0,d],
    J=sinh t cosh(t)^(3/2), Lell=ell(ell+2), n=m+1.

For (Y-yj)u=F, the exact Liouville transform v=Ju gives

    v''-Pj v=f=-J zeta F/K,
    Pj=n²+(35/4-yj/K)zeta-(Lell+3/4)zeta/(1+zeta).

Choose the SAME positive scale for all five roots and the scalar Einstein root,

    k²=36+n²+Lell+6sigma/K.                       (3)

Equations(2) and zeta<=4 give |Pj|<=k², and

    partial_zeta RePj=35/4-Re(yj)/K-(Lell+3/4)/(1+zeta)²<0.

The last sign uses sigma>=3kappa² and the actual K/kappa², not a large-frequency approximation. It holds for every angular degree and multiplicity.

Write ImPj=-epsilon b zeta, b=|Im yj|/K, epsilon=sign(Im yj), choosing epsilon=+1 if the root is real. Impose

    v'(0)+i epsilon k v(0)=0,
    v'(d)-i epsilon k v(d)=0.                     (4)

The sign adapts to the root, not to the forcing. Holding the same sign for both conjugate roots would invalidate the following coercivity argument.

Let CG be the fixed REAL monotone Green constant proved in K2580 §3, which bounds the real-part inverse G0 from L1 to Linfinity by CG k. Negative epsilon is its complex conjugate and has the same bound. Set beta=1/(8d CG)>0.

**Near-real roots, b<=beta/k.** Treat -i epsilon b zeta as a multiplication perturbation of the real operator, keeping(4). The Linfinity operator norm of its Green composition is at most4d CG k b<=1/2. Neumann inversion therefore gives

    ||v||infinity<=2CG k sqrt(d)||f||2.           (5)

This includes the real roots and proves existence and uniqueness there.

**Remaining roots, b>=beta/k.** Integration by parts gives the exact imaginary identity

    k(|v(0)|²+|v(d)|²)+b integral zeta|v|²
       =epsilon Im integral f conjugate(v).     (6)

Thus ||v||2<=||f||2/b. The real identity then gives

    ||v'||2²<= (k²/b²+1/b)||f||2².                (7)

For zero forcing(6) proves uniqueness. A second-order regular ODE has a two-dimensional homogeneous solution space; injectivity of its two boundary functionals implies surjectivity for arbitrary forcing, hence existence. The one-dimensional H1 inequality bounds the supremum by a fixed multiple of ||v||2+||v'||2. Since b>=beta/k and k>=1, equations(6)–(7) yield a uniform bound C k²||f||2.

Both cases combine into

    ||v||infinity<=C k²||f||2,
    ||v'||infinity<=C' k³||f||2.                 (8)

For the derivative, use the ODE and one-sided Taylor on an interval of length h=min(d/2,1/k) in a direction lying inside[0,d]: |v'|<=2||v||infinity/h+h k²||v||infinity/2+sqrt(h)||f||2. This also treats endpoints. The constants depend only on the fixed annulus/real bound, not the root, radial index, angular indices or a root separation. Higher regularity follows by differentiating this ODE with its smooth coefficient functions. Polynomial coefficient bounds persist under every fixed number of x derivatives.

Nonzero endpoint data v'(0)+i epsilon k v0=k g0 and v'(d)-i epsilon k vd=k gd can be lifted by

    ell(x)=k[g0 x(1-x/d)²+gd x²(x-d)/d²].         (9)

It has zero endpoint values and the required derivatives. Applying(8) to forcing f-(ell''-Pell) gives the conservative bound C[k²||f||2+k^5|g|]. We use homogeneous intermediate data below; (9) explicitly shows how other supplied boundary data enter. These estimates are sufficient, not sharp or physical energy estimates.

## 3. Ten traces, sequential inversion and full rows

For each scalar radial eigenvalue fix one deterministic ordering of the five roots (lexicographic real/imaginary parts, counting multiplicity, suffices). Define G_j as the factor inverse with(3)–(4). With Lkappa=L kappa^-4 set

    F0=chi/Lkappa, Fj=G_j F_(j-1) (j=1,...,5), U=F5.

Then (Y-y5)U=F4, followed by cancellation through the preceding factors, gives

    d_kappa(-sigma,Y)U=chi.                      (10)

No commutation of the inverses is assumed. The polynomial differential factors commute on smooth functions, but their boundary inverses need not. Repeated roots are solved sequentially without dividing by a root gap.

Equivalently define Fj=product_(h=j+1..5)(Y-yh)U for j=1,...,5. Require the two boundary traces(4) of JFj for EACH j. These TEN explicit traces form one input-independent spectral preparation for the order-ten scalar equation, with the scalar radial realization retained. They specify intermediate transformed fields, not arbitrary independent component Dirichlet conditions. Sequential uniqueness proves uniqueness in this scalar auxiliary problem, not uniqueness modulo all gauge/full-system solutions.

Repeated composition of(8), bounded Liouville multipliers and interval L2 inclusions costs at most ten powers of the joint scale k for U, before finite cofactor and tensor derivatives; U_x costs one further power. Every fixed higher derivative has a finite polynomial loss. Rapid decay in the scalar radial and angular eigenindices, with all x derivatives, is therefore preserved. This proves a smooth right inverse on the intersection of all such weighted spectral spaces, retaining ALL angular modes and multiplicities. It is not a claimed sharp finite-Sobolev theorem for the original tensor components.

The scalar Einstein inverse solves (X+Y+12K)w=chi with root yE=sigma-12K and the same construction. Reuse K2552's ACTUAL polynomial identities, including all six scalar/skew rows:

    vsrc=(-X-6K,0,1,0,0,0)^T,
    s0=(X+5K,-X-7K,0,0,1,0)^T,
    M adj(M)=d I, E s0=(X+Y+12K)vsrc[:5],
    Q_s=-rE T[adj(M)vsrc U], z_s=-rE T[s0 w]/2.

Here T reconstructs the actual tensor from the six scalar potentials, including its skew component; E above denotes its five symmetric potential rows.

Together with K2580/K2582's TT responses, set Q=Q_s+Q_TT, z=z_s+z_TT, h=z-rE sym(Q), e2=-A_aux^-1 B_aux Q. The actual source and every selected linear equation hold. Cofactors are finite polynomials in the commuting scalar operators; the proved rapid spectral decay justifies applying them and reconstructing the smooth tensor. This uses the stated action completion, not native I1B.

## 4. Released consumer: the prescribed compact source satisfies compatibility

Let the ORIGINAL radial pressure satisfy P'+4alpha(P-A)=0, with smooth even data and support strictly inside R as in K2552, and multiply by arbitrary smooth rho on the closed B annulus and BOTH angular spheres. The source is j_A rho, with j_A eigenvalues A/2 on observer directions and P/2 on the three normal directions. Retain t=(4A+3P)/2.

The fixed splitter chi_D=(A2-7K)^-1(t/6) lies in every scalar Dirichlet power: t is smooth and vanishes in a neighborhood of the outer endpoint. Its regular center is the three-dimensional radial scalar lift. The new scalar inverses therefore apply.

For the actual TT residual use K2552's exact formula

    b_D=P/2+(4alpha+2beta)chi_D'+6Kchi_D.

Outside source support, P=0 and (X+7K)chi_D=0, hence

    b_D=-(chi_D''+Kchi_D), D5 b_D=21K b_D.         (11)

Let psi be the regular overlap mode of K2582, psi(R)=1, and bpsi=psi''+Kpsi, with bpsi(R)<-4K/3. Set

    a=b_D(R)/bpsi(R), b0=b_D-a bpsi.              (12)

The residual b0 has zero trace. In an entire outer neighborhood it obeys D5 b0=21K b0, so

    (D5^m b0)(R)=(21K)^m b0(R)=0  for every m.    (13)

Smooth regular-even b0 consequently lies in every A5 Dirichlet power. This is the higher compatibility that merely subtracting the trace of an arbitrary smooth amplitude does NOT imply. The actual compact source supplies it via its tail equation. Thus K2580 handles b0 rho and K2582 handles a bpsi rho; their sum retains the canceling scalar/TT source tails exactly. No source truncation, TT replacement or radial basis identification occurs.

An explicit nonzero source family is obtained from any nonnegative smooth A supported in an interior subinterval, with

    C(r)^4 P(r)=-integral_r^R 4C(s)^3 C'(s)A(s) ds.

Differentiation gives the actual conservation law. Because C'<0, P>=0; it is zero beyond the support and regular even near the center. Thus t is nonnegative and nonzero, and K2552's positive splitter is nonzero. This family, times rho=1 or any smooth angular/B profile, is admitted without selecting source-dependent boundaries. The probe checks the conservation and tail equations and the exact source reconstruction identities; no explicit closed-form spectrum or numerical eigenfunction approximation is required for this existence consumer.

## 5. Splitter orbit and reality

The Dirichlet cofactor inverse above acts on chi_D. It must NOT be applied directly to psi, whose nonzero trace excludes it from that radial domain. Extend the response along chi_D+a(B)psi by K2582's direct scalar-overlap eigenline, synchronized with the identical TT response and its explicit Einstein pure-gauge correction. Opposite changes in the split sources then cancel in ALL total fields, preserving total boundary values and every defined readout. This gives a single linear response rule on the splitter orbit while preserving the different component domains.

All equations and source coefficients are real. The constructed complex solution has real part solving the same real forced equations; its imaginary part is homogeneous. That observation does not turn(4) into a real self-adjoint Robin law or assert that ReU separately obeys the complex auxiliary traces. Root ordering and impedance signs are fixed mathematical preparation choices, not fitted to the source or selected by the physical action. In particular the two angular signature sectors, compact source construction and polynomial bounds do not establish causal propagation or physical positivity.

## Verification and next question

The probe verifies exact coefficient inequalities and the all-sigma Rouché envelope, independent full-matrix determinant/adjugate points, actual Liouville/potential signs, the complex flux orientation, cubic endpoint lift, repeated-factor cancellation and source-tail compatibility. A wrong-sign impedance genuinely destroys the sign-definite identity; dropping mixed determinant terms fails exact matrix checks. Finite identities and supporting fixtures are not a count of universal theorems. The global domain and smooth synthesis claims are the arguments above.

The scalar complement and actual compact-source compatibility on THIS fixed annulus are now constructed at the independently reviewed scope. A strongest next physics question is whether an independently justified real preparation and conserved readout can select this response or distinguish its boundary-dependent homogeneous freedom. Sharper finite-order estimates or the original B point distribution require their own analysis; smooth input here does not admit that delta automatically. Native displacement/action and physical measurement bridges remain open.

[K2552 source and complete rows](k2552-localized-source-domain-2026-11-04.md), [K2554 actual determinant](k2554-analytic-source-response-2026-11-05.md), [K2580 radial TT inverse](k2580-radial-angular-source-domain-2026-11-05.md), [K2582 trace and overlap repair](k2582-affine-radial-boundary-response-2026-11-05.md), [probe](../../tests/channel-swings/k2584_scalar_spectral_boundary_inverse_probe.py), [report](../../lab/process/k2584-scalar-spectral-boundary-inverse.json).

Independent internal acceptance: field specialists cross-reviewed both constructions and a distinct integrated hostile review returned no remaining findings. Exact producer/replay and affected native checks passed. This is internal review, not external or proof-assistant certification.
