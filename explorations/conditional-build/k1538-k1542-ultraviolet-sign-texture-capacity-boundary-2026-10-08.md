---
title: "K1538--K1542 ultraviolet sign-texture capacity boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1538--K1542 ultraviolet sign-texture capacity boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification is `SOURCE_NATIVE_ROUTE` because the packet tests the positive
Hamiltonian prerequisite bordering SC-META-53. The cutoff field, nonlinear
Hamiltonian, endpoint sign tube and BRST complex are repository controls, not
released GU data.

```gu-typed-objects
result: exact low-Wick amplitude rigidity, all-density ultraviolet-shell covariance necessity, global-sign endpoint exclusion, ultraviolet sign-texture reduction and sharpened endpoint carre-du-champ bound
carrier: beta=1 Gaussian reduced Fock space LAYER=toy BRIDGE=positive-state-requirements CHIRALITY=N/A
pairing: Gaussian Q-space pairing ON=repository_owned_control
real_structure: real cutoff Fourier covariance basis with arbitrary finite-Fisher likelihood and optional complex phase
grading: spatial frequency, fixed-ratio ultraviolet shell, pointwise amplitude, spatial sign field, centered covariance, relative Fisher information, Wick-square energy and cutoff filtration
action_owner: repository-construction -- no released source measure, counterterm, renormalized Hamiltonian, BRST charge, physical quotient or observed map
target: SC-META-53 interacting-positive-state boundary MAP-TYPE=restriction
```

## Preflight bookend

K1533--K1537 leave a precise endpoint-capacity question, but the phrase
"two-well endpoint" still conflates two different objects. A random choice
between the two constant wells changes only the zero mode. A spatial sign
field can instead retain ultraviolet content while its pointwise magnitude
stays near the wells. The first object is too rigid; the second is the actual
remaining escape.

The cheapest structural route is to split amplitude from sign before
attempting another probability asymptotic. The elementary factorization of
`phi_N^2-3C_N` gives an exact amplitude bound for every configuration. In the
independent direction, K1533's all-density Fisher inequality and K1530's
noncommutative shell factorization show that every state with subquartic free
energy must retain order-`C_N` centered covariance in the ultraviolet shell.
These facts are incompatible on the union of the two global sign cones.

## K1538 — exact amplitude rigidity

Put

```text
A_N=sqrt(3C_N),
D_N(phi)=phi_N^2-A_N^2,
W_N=||D_N(phi)||_2^2.
```

Pointwise,

```text
(|phi_N|-A_N)^2
 =D_N(phi)^2/(|phi_N|+A_N)^2
 <=D_N(phi)^2/A_N^2.
```

Therefore every cutoff configuration satisfies

```text
|||phi_N|-A_N||_2^2<=W_N/(3C_N).
```

No Gaussian law, moment condition, sign choice or likelihood assumption is
used. Averaging under any law `nu` gives

```text
E_nu|||phi_N|-A_N||_2^2
 <=E_nu W_N/(3C_N).
```

Since `C_N=Theta(N^2)`, an endpoint state with `E_nu W_N=O(N^2)` has only
`O(1)` expected squared amplitude error around a target whose squared norm is
`A_N^2=Theta(N^2)`. Low Wick square freezes the amplitude. It does not freeze
the spatial sign field

```text
s_phi(x)=sgn(phi_N(x)).
```

That distinction is load-bearing below.

## K1539 — subquartic free energy requires shell covariance

Let `nu=rho mu` have real-coordinate mean `m` and positive covariance `S`.
Write

```text
T_N=Tr(P_N Lambda S),
C_sh,N=Tr(P_N Lambda)>=kappa C_N,
P_N Lambda^2 Omega^(-1)P_N<=a_N P_N Lambda,
a_N<=L N^(-2).
```

Here `P_N` is K1530's fixed-ratio ultraviolet-shell projector. If
`T_N<=C_sh,N/2`, then

```text
delta_N
 =Tr[P_N Lambda(I-S)]
 =C_sh,N-T_N
 >=C_sh,N/2.
```

K1530's Frobenius factorization, now followed by K1533's all-density Fisher
bound, gives

```text
q0[psi]
 >=delta_N^2/(4a_N T_N).
```

This is valid for every finite-Fisher density and arbitrary phase. It does not
assume a Gaussian likelihood, diagonal covariance, stationarity or commutation
of `S` with the frequency operators. Since `T_N<=C_sh,N/2=O(N^2)`, the right
side is at least order `N^4`. Consequently

```text
q0[psi]=o(N^4)
  implies
T_N>C_sh,N/2>=kappa C_N/2
```

for all sufficiently large `N`. A coherent constant-mode shift or a random
global plus/minus well cannot supply this centered ultraviolet covariance.

## K1540 — the global sign cones cost `N^6`

Let `G_N` be the union of the two global sign cones: each configuration is
nonnegative almost everywhere or nonpositive almost everywhere, while the
choice of sign may vary between configurations. For `phi_N` in `G_N`, choose
`sigma(phi)` so that `sigma(phi)phi_N=|phi_N|`. The constant
`sigma(phi)A_N` has no `P_N` component, hence

```text
||P_N phi_N||_2^2
 <=||phi_N-sigma(phi)A_N||_2^2
 <=W_N/(3C_N).
```

If `nu` is supported on `G_N`, then

```text
T_N
 <=E_nu||P_N phi_N||_2^2
 <=E_nu W_N/(3C_N).
```

Thus `E_nu W_N=O(N^2)` forces `T_N=O(1)`. Returning to the quantitative K1539
bound, `delta_N=Theta(N^2)` while `a_NT_N=O(N^-2)`, so

```text
q0[psi]>=cN^6.
```

No normalized state supported on the global sign cones can have both
`q0[psi]=O(N^2)` and `E_nuW_N=O(N^2)`. Randomizing the global sign only adds
constant-mode covariance, so it does not help.

The support hypothesis is essential. The theorem does not classify densities
carried by spatially sign-changing configurations and does not promote the
K1534 cat/squeeze calculation to every two-well likelihood.

## K1541 — the remaining escape is ultraviolet sign texture

Suppose, only to derive necessary conditions, that a normalized state obeys

```text
q0[psi]+gE_nuW_N<=KN^2.
```

K1538 and K1539 give simultaneously

```text
E_nu|||phi_N|-A_N||_2^2=O_g(1),
T_N>=kappa C_N/2=Theta(N^2).
```

Write

```text
e_phi=|phi_N|-A_N,
phi_N=A_Ns_phi+s_phi e_phi.
```

Projection contraction gives

```text
||P_N(phi_N-A_Ns_phi)||_2<=||e_phi||_2.
```

Because `E||P_Nphi_N||_2^2>=T_N` and

```text
||x||^2<=2||y||^2+2||x-y||^2,
```

one obtains

```text
E_nu||P_Ns_phi||_2^2
 >=kappa/12-o(1).
```

The missing order-`N^2` trial must therefore live on configurations whose
magnitudes are almost frozen but whose spatial sign fields retain a
nonvanishing component in the fixed-ratio ultraviolet shell. The exact
remaining target is the Gaussian weighted Dirichlet capacity of this
sign-texture tube, not the probability or capacity of two constant wells.

The direct bump estimate also sharpens. With `D_N=phi_N^2-3C_N`, projection
contraction gives

```text
Gamma_Omega(W_N)
 <=8 int D_N^2 phi_N^2
 =8 int(D_N^3+3C_ND_N^2).
```

Since `D_N` is `2N`-bandlimited, the three-dimensional Nikolskii inequality
gives

```text
||D_N||_infinity<=cN^(3/2)sqrt(W_N).
```

Therefore

```text
Gamma_Omega(W_N)
 <=c{N^(3/2)W_N^(3/2)+C_NW_N},
```

which is `O(N^(9/2))` on `W_N=O(N^2)`, improving the crude `N^5` local
prefactor. This still does not control the relative transition mass in the
normalized bump quotient. It neither constructs an order-`N^2` state nor
proves a superquadratic capacity lower bound.

Harmonic BRST tensoring transfers only these scoped finite-cutoff Rayleigh
conditions. It constructs no continuum interacting charge or physical GU
cohomology.

## K1542 — admission replay

The bridge census is now 256 rows: 177 satisfied, ten conditional, 65 excluded
and four missing. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains
`UNCERTAIN`, the physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS /
2 OVER-DETERMINED, K1145/K1150 stay `0/7`, and no source, canon, paper,
prediction, confirmation or public status moves.

## Postflight hostile review

The strongest overclaim would replace "global sign cones" by "all two-well
states." That is false. A spatial sign texture is not a random global sign.
K1540 excludes only densities supported on configurations with one sign across
space; K1541 preserves the spatially sign-changing branch as the entire live
endpoint.

The strongest contrary construction is precisely such a textured likelihood.
It must keep `|phi_N|` within order-one squared `L2` error of `A_N` while
retaining a fixed amount of sign energy on the outer shell. Neither a concrete
finite-Fisher density nor its `O(N^2)` capacity quotient is presently known.

The weakest proof seam is the centered-versus-uncentered shell distinction.
K1539 requires `T_N=Tr(P_NLambda S)`, while K1540 first bounds the uncentered
quantity `E||P_Nphi_N||_2^2`. The latter is an upper bound on `T_N`, so the
direction used is valid; a global random sign can inflate only the constant
mode and cannot change this shell estimate.

The source boundary is unchanged. These are repository-owned controls
bordering SC-META-53, not an action-owned GU quantization.

## Exact next input

Compute the Gaussian weighted Dirichlet capacity of the amplitude-rigid
ultraviolet sign-texture tube. Either construct a finite-Fisher likelihood with
`E W_N=O(N^2)`, `T_N=Theta(C_N)` and total free cost `O(N^2)`, or prove a
superquadratic capacity lower bound for every such sign-textured law. In
parallel, K1413 still requires a genuinely gauge/Maxwell-dependent spacetime,
secondary-null or derivative/nonlocal estimate, and source admission still
requires one action-owned primitive circle, kinetic normalization, physical
carrier and faithful observed intertwiner.
