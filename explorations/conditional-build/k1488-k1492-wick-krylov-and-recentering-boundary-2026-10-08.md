---
title: "K1488--K1492 Wick Krylov and recentering boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1488--K1492 Wick Krylov and recentering boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification is `SOURCE_NATIVE_ROUTE` because the packet tests the positive
Hamiltonian prerequisite bordering SC-META-53. The Gaussian cutoff field,
Krylov compressions, nonlinear Hamiltonians and BRST tower are repository
controls, not released GU data.

```gu-typed-objects
result: eighth-chaos Krylov lower bound, two-dimensional Ritz nonquasimode theorem, strict three-dimensional variational improvement and enlarged scalar/BRST recentering exclusion
carrier: beta=1 Gaussian reduced Fock space tensored with the Gaussian gauge-boson/ghost complex LAYER=toy BRIDGE=positive-state-requirements CHIRALITY=N/A
pairing: Gaussian Q-space pairing and tensor-product BRST Hilbert pairing ON=repository_owned_controls
real_structure: Gaussian real field and coordinatewise complex conjugation
grading: spatial frequency, Wiener chaos, polynomial Krylov degree, particle number, cutoff filtration and ghost number
action_owner: repository-construction -- no released source measure, ground-energy counterterm, renormalized Hamiltonian, BRST charge, physical quotient or observed map
target: SC-META-53 interacting-positive-state boundary MAP-TYPE=restriction
```

## Preflight bookend

K1484 made the lower eigenvalue of the vacuum--fourth-chaos compression exact,
but its hostile review left higher chaoses as the decisive seam. Before seeking
a lower bound for the full ground energy, test whether the next Krylov vector
already changes the coefficient. The fourth-chaos product formula makes that
question structural: `V_N^2` has an eighth-chaos projection that neither the
vacuum nor `V_N` can remove.

The orthodox/operator lens asks whether this projection has full variance
scale. The frontier lens asks whether it makes the old Ritz vector fail even
as a quasimode. The pragmatic lens asks for a fixed finite-dimensional trial
whose free cost is lower order than `sigma_N`. The hostile lens keeps every
conclusion one-sided: a stronger upper bound is not a ground-energy asymptotic.
The PDE and source-selector challengers remain independent, but require new
spacetime or action-owned carrier input not produced by the Gaussian product
formula.

## K1488 — the quadratic Krylov direction cannot collapse

Write the integrated fourth Wick chaos as

```text
V_N=I_4(f_N),
sigma_N^2=E(V_N^2)=4! ||f_N||^2,
X_N=V_N/sigma_N,
mu_N=E(X_N^3).
```

The multiple-integral product formula gives

```text
V_N^2
 = sum_(r=0)^4 r! binom(4,r)^2
     I_(8-2r)(sym(f_N tensor_r f_N)).
```

Orthogonalize the square against the first two Krylov vectors:

```text
R_N=X_N^2-1-mu_N X_N,
tau_N^2=||R_N||_2^2=E(X_N^4)-1-mu_N^2.
```

The subtracted vectors live in chaoses zero and four. They cannot change the
eighth-chaos projection. In the symmetrization norm, the identity-pairing term
alone gives

```text
||P_8(V_N^2)||_2^2
 =8! ||sym(f_N tensor f_N)||^2
 >=(4!)^2 ||f_N||^4
 =sigma_N^4.
```

All terms in the kernel contraction expansion are nonnegative squared norms;
no sign assumption on the pointwise covariance is used. Therefore

```text
tau_N^2>=1.
```

The unit vector `Y_N=R_N/tau_N` exists at every cutoff, is orthogonal to
`1,X_N`, and satisfies

```text
<X_N,X_N Y_N>=tau_N>=1.
```

Thus the next multiplication coupling is never asymptotically small.

## K1489 — the two-dimensional Ritz state is not a quasimode

Let

```text
u_N=alpha_N 1+beta_N X_N
```

be K1484's normalized lower Ritz vector. Then
`alpha_N->1/sqrt(2)` and `beta_N->-1/sqrt(2)`. For the centered operator

```text
K_N^proj=H_0+g sigma_N X_N,
```

the component of its Ritz residual in the `Y_N` direction is

```text
<Y_N,(K_N^proj-lambda_N^-)u_N>
 =beta_N <Y_N,H_0X_N>+g sigma_N beta_N tau_N.
```

The first term is lower order. `X_N` has chaos degree four and `Y_N` degree
at most eight, so the cutoff bound for second quantization and Cauchy--Schwarz
give

```text
|<Y_N,H_0X_N>|=O(omega_max(N))=O(N).
```

Since `sigma_N=Theta(N^(5/2))` and `tau_N>=1`, for all large `N`,

```text
||(K_N^proj-lambda_N^-)u_N||>=g sigma_N/3.
```

The two-dimensional Ritz vector is not an `o(sigma_N)` quasimode. In
particular, the coefficient `-1` found by that compression cannot be promoted
to the leading full variational correction.

## K1490 — one more Krylov direction gives a strict coefficient gain

In the orthonormal basis `{1,X_N,Y_N}`, compression of multiplication by
`X_N` is

```text
M_N = [ 0       1       0     ]
      [ 1       mu_N    tau_N ]
      [ 0       tau_N  eta_N  ],

eta_N=E(X_N Y_N^2).
```

K1483 gives

```text
0<=mu_N<=72S_N/sigma_N=o(1).
```

Nelson hypercontractivity on degrees four and at most eight gives

```text
||X_N||_4<=3^2=9,
||Y_N||_4<=3^4=81,
|eta_N|<=||X_N||_2 ||Y_N^2||_2<=6561.
```

Set `t=1/6562` and test the coefficient vector `(1,-1,t)`. Once
`mu_N<=1/(2*6562)`, its normalized multiplication Rayleigh quotient obeys

```text
[-2+mu_N-2tau_N t+eta_N t^2]/[2+t^2]
 <= -1-c_star,

c_star=1/39372.
```

The trial has Wiener degree at most eight, so its normalized free form cost is
at most `8 omega_max(N)=O(N)`. Hence, for every fixed `g>0`,

```text
E_N
 <=6gC_N^2-(1+c_star)g sigma_N+O(N).
```

The constant is intentionally crude. Its role is qualitative but rigorous:
the first higher-chaos direction lowers the coefficient by a cutoff-independent
amount. This does not identify the true correction scale.

## K1491 — enlarged recentering and BRST window

Put `kappa=1+c_star`. Uniform semiboundedness of `H_N-a_N` now requires

```text
a_N<=6gC_N^2-kappa g sigma_N+O(N).
```

More explicitly, for fixed `0<epsilon<c_star`, any eventual shift satisfying

```text
a_N>=6gC_N^2-g(kappa-epsilon)sigma_N
```

has

```text
inf spec(H_N-a_N)<=-g epsilon sigma_N+O(N)->-infinity.
```

The normalized fixed trial has vacuum coefficient
`1/sqrt(2+t^2)`. Both `X_N` and `Y_N` are orthogonal to the vacuum. Every weakly
convergent subsequence therefore retains the same nonzero vacuum component.
Weak compactness supplies such a subsequence, while its recentered form values
tend to minus infinity. This violates Mosco weak liminf for every finite
semibounded limiting form on the fixed Gaussian Hilbert space throughout the
stated enlarged window.

For K1471's tensor construction, tensor the trial with the normalized
degree-zero harmonic BRST vacuum. The BRST Laplacian contributes zero, and the
weak limit retains a nonzero harmonic vacuum component. Both the full forms
and their harmonic compression inherit the same spectral-bottom divergence
and Mosco failure.

## K1492 — admission replay

The bridge census is now 179 rows: 111 satisfied, ten conditional, 54 excluded
and four missing. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains
`UNCERTAIN`, the physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS /
2 OVER-DETERMINED, K1145/K1150 stay `0/7`, and no source, canon, paper,
prediction, confirmation or public status moves.

## Postflight hostile review

The strongest overclaim would extrapolate one additional Krylov direction into
the true ground-energy asymptotic. K1490 remains an upper bound; further
polynomial directions may lower the energy by much more. The strongest contrary
route is a coercive many-chaos lower bound or direct localization theorem for
the true ground states. The weakest seam is the deliberately crude
hypercontractive constant: it is sufficient for a strict universal gain, not
an optimal coefficient.

The representation seam also remains exact. The weak-liminf counterexample
uses the fixed Gaussian Hilbert space and scalar recentering. Singular dressing,
a non-Gaussian reference measure, a changed representation and true-ground-
energy recentering remain open. Within those ceilings the result is
decision-grade: it proves the two-dimensional Ritz asymptotic is not even
variationally stable and prevents the next campaign from treating coefficient
one as the energy scale to match.

## Exact next input

For the quantum arc, extend the Krylov construction far enough to identify the
growth regime of the optimal polynomial coefficient, or prove a many-chaos
coercive lower bound/localization theorem that brackets the true `E_N` scale;
only then test compactness and Mosco recovery for `a_N=E_N+O(1)` on a common
nonlinear domain. For the PDE, construct a gauge/Maxwell-dependent bilinear
spacetime or secondary-null estimate, or a derivative/nonlocal modified energy
controlling both K1413 leakages. Continuum BRST closure still waits on the
recentered matter limit.
