---
title: "K1483--K1487 Wick third-moment and recentering-window boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1483--K1487 Wick third-moment and recentering-window boundary

Classification is `SOURCE_NATIVE_ROUTE` because the packet tests the positive
Hamiltonian prerequisite bordering SC-META-53. The Gaussian cutoff field,
Ritz compression, nonlinear Hamiltonians and BRST tower are repository
controls, not released GU data.

```gu-typed-objects
result: exact fourth-Wick-chaos third-moment triangle, vacuum--chaos Ritz asymptotic, scalar-recentering exclusion window and BRST transfer
carrier: beta=1 Gaussian reduced Fock space tensored with the Gaussian gauge-boson/ghost complex LAYER=toy BRIDGE=positive-state-requirements CHIRALITY=N/A
pairing: Gaussian Q-space pairing and tensor-product BRST Hilbert pairing ON=repository_owned_controls
real_structure: Gaussian real field and coordinatewise complex conjugation
grading: spatial frequency, Wiener chaos, particle number, cutoff filtration and ghost number
action_owner: repository-construction -- no released source measure, ground-energy counterterm, renormalized Hamiltonian, BRST charge, physical quotient or observed map
target: SC-META-53 interacting-positive-state boundary MAP-TYPE=restriction
```

## Preflight bookend

K1479's generic fourth-chaos hypercontractive estimate is the weakest seam in
the projective-recentering exclusion. Before attempting the much larger
two-sided ground-energy and compactness problem, compute the exact third moment.
For three normal-ordered quartic vertices, the contraction graph is forced by
degree alone. Its triangle form admits a direct Young bound, so no large Wick
diagram enumeration or numerical cutoff sweep is needed.

The positive result releases the exact two-dimensional Ritz eigenvalue. Its
negative alternative would have left only K1479's fixed-small-amplitude bound.
The gauge-dependent PDE repair and source-owned carrier selector remain
independent, but require new spacetime or action inputs not supplied by this
Gaussian calculation.

## K1483 — exact third-moment triangle and `O(N^6)` bound

On normalized `T3`, write

```text
V_N = integral :phi_N(x)^4: dx,
C_N(x-y) = E(phi_N(x)phi_N(y)),
sigma_N^2 = E(V_N^2) = 24 integral C_N(z)^4 dz,
S_N = integral C_N(z)^2 dz = sum_k q_k^2.
```

In `E(V_N^3)`, normal ordering forbids contractions within one vertex. If
`n_12,n_13,n_23` count edges between the three quartic vertices, their degree
equations are

```text
n_12+n_13=4,
n_12+n_23=4,
n_13+n_23=4.
```

Thus `n_12=n_13=n_23=2`; this is the unique contraction multigraph. Its
number of labeled contractions is

```text
(4!)^3/(2!)^3 = 1728.
```

Translation invariance therefore gives the exact formula

```text
m3_N := E(V_N^3)
 = 1728 integral integral
     C_N(x)^2 C_N(y)^2 C_N(x-y)^2 dx dy.
```

The integrand is nonnegative. With `f_N=C_N^2`, Young's convolution inequality
on normalized `T3` yields

```text
integral integral f_N(x)f_N(y)f_N(x-y) dx dy
 = <f_N*f_N,f_N>
 <= ||f_N||_1 ||f_N||_2^2
 = S_N integral C_N^4.
```

Consequently

```text
0 <= m3_N/sigma_N^2 <= 72 S_N.
```

For the three-dimensional beta-one covariance, `S_N=O(N)` and K1470 gives
`sigma_N^2=Theta(N^5)`, so `m3_N=O(N^6)`. This improves the generic
hypercontractive `O(sigma_N^3)=O(N^(15/2))` ceiling without claiming a
matching third-moment asymptotic.

## K1484 — exact Ritz value and the leading negative correction

Use the orthonormal basis

```text
e0=1,                 e1=V_N/sigma_N
```

in the form domain of

```text
K_N^proj=H_N-6gC_N^2=H0+gV_N.
```

Writing `h_N=<V_N,H0V_N>`, its exact compression is

```text
M_N = [ 0          g sigma_N ]
      [ g sigma_N  d_N       ],

d_N = h_N/sigma_N^2 + g m3_N/sigma_N^2.
```

K1479 gives `h_N/sigma_N^2<=4 omega_max(N)=O(N)`, while K1483 gives
`0<=m3_N/sigma_N^2<=72S_N=O(N)`. Hence `0<=d_N=O(N)`. The lower Ritz
eigenvalue is exactly

```text
lambda_N^- = (d_N-sqrt(d_N^2+4g^2 sigma_N^2))/2.
```

Since `sigma_N=Theta(N^(5/2))`,

```text
lambda_N^-=-g sigma_N+O(N),
lambda_N^-/(g sigma_N) -> -1,
E_N <= 6gC_N^2-g sigma_N+O(N).
```

For the normalized lower eigenvector
`u_N=alpha_N e0+beta_N e1`, choose `alpha_N>0`. Then

```text
beta_N/alpha_N=lambda_N^-/(g sigma_N)->-1,
alpha_N->1/sqrt(2),     beta_N->-1/sqrt(2).
```

K1480 proves `e1` converges weakly to zero, so `u_N` converges weakly to the
nonzero vector `1/sqrt(2)`. This is an asymptotic of the two-dimensional Ritz
value, not a matching asymptotic for the full ground energy.

## K1485 — a scalar-recentering exclusion window

Let `K_N(a)=H_N-a_N`. Uniform semiboundedness would require
`a_N<=E_N+O(1)`. K1484 therefore gives the necessary one-sided condition

```text
a_N <= 6gC_N^2-g sigma_N+O(N).
```

More explicitly, fix `epsilon>0`. If eventually

```text
a_N >= 6gC_N^2-(g-epsilon)sigma_N,
```

then

```text
inf spec K_N(a)
 <= -epsilon sigma_N+O(N)
 -> -infinity.
```

The same normalized Ritz eigenvectors have a nonzero weak vacuum limit while
their `K_N(a)` form values tend to minus infinity. Thus the entire stated
window fails Mosco weak liminf for every finite semibounded limiting form on
the fixed Gaussian Hilbert space. K1480's exact projective shift is the
special case `a_N=6gC_N^2`; the new boundary excludes every shift that
recovers less than `g sigma_N` by a fixed positive fraction.

This necessary boundary does not exclude `a_N=E_N+O(1)`, a shift at or below
`6gC_N^2-g sigma_N+O(N)`, or a different representation.

## K1486 — harmonic BRST transfer

For K1471's tensor construction,

```text
mathbb K_N(a)
 = (H_N-a_N) tensor 1 + 1 tensor Delta_BRST.
```

Let `eta` be the normalized degree-zero harmonic BRST vacuum. Then
`Delta_BRST eta=0`, and `u_N tensor eta` has exactly the K1485 matter form
value. It converges weakly to the nonzero harmonic vector
`(1/sqrt(2))1 tensor eta`. The full forms and their degree-zero harmonic
compression therefore inherit the same spectral-bottom divergence and Mosco
weak-liminf failure throughout the excluded scalar window.

Finite-cutoff nilpotence and positive harmonic cohomology remain valid. They
do not select the matter energy origin or construct a continuum interacting
BRST domain.

## K1487 — admission replay

The bridge census is now 170 rows: 106 satisfied, ten conditional, 50 excluded
and four missing. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains
`UNCERTAIN`, the physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS /
2 OVER-DETERMINED, K1145/K1150 stay `0/7`, and no source, canon, paper,
prediction, confirmation or public status moves.

## Postflight hostile review

The strongest overclaim would replace the full interacting ground energy by
the two-dimensional Ritz eigenvalue. K1484 is an upper bound only; higher
chaoses can lower `E_N` further, so the actual counterterm may sit strictly
below this boundary. The strongest contrary route is precisely a many-chaos
lower bound plus compactness for the ground-energy-recentered family; nothing
here excludes it. The weakest transfer seam is representation dependence:
the weak-limit argument uses the fixed Gaussian Hilbert space and does not
survive automatically under singular dressing or a changed measure.

Within those ceilings, the result is decision-grade. It replaces a generic
moment estimate by an exact graph identity, identifies the leading
two-dimensional variational correction and removes a whole scalar-recentering
window before a continuum-domain campaign spends on an energy origin that is
still too high.

## Exact next input

For the quantum arc, prove a lower bound on `E_N` that matches a useful part of
the `g sigma_N` correction, or directly establish localization/compactness and
Mosco liminf/recovery after the true `E_N+O(1)` recentering. For the PDE,
construct a genuinely gauge/Maxwell-dependent bilinear spacetime or
secondary-null estimate, or a derivative/nonlocal modified energy controlling
both K1413 leakages. Only a recentered matter limit can support a continuum
version of K1471's BRST-compatible Hamiltonian.
