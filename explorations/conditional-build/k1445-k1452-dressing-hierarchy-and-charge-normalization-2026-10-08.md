---
title: "K1445--K1452 dressing, hierarchy and charge-normalization boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1445--K1452 dressing, hierarchy and charge-normalization boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This packet contains a
> conventional hypercharge comparator only in K1451's scoped carrier test.
> W222's relative arithmetic is not source ownership. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification is `SOURCE_NATIVE_ROUTE` because the packet tests positive-state,
global-dynamics and observed-carrier requirements bordering SC-META-53. The
Gaussian fields, dispersions and Maxwell--matter hierarchy are repository
controls, not released GU data.

```gu-typed-objects
result: regular-dressing obstruction, UV-softened interacting control, charge-analytic PDE hierarchy and primitive-circle normalization boundary
carrier: coherent beta-Gaussian symmetric Fock spaces, repository multi-charge Maxwell--matter phase space, and one fixed spherical K-type LAYER=toy BRIDGE=maximal-compact-charge-reduction CHIRALITY=N/A
pairing: positive Gaussian/Fock, covariant energy and compact-circle Hilbert pairings ON=repository_owned_controls
real_structure: Gaussian real field, Fourier conjugation and compact-circle unitary real structure
grading: particle number, free-energy scale, charge powers, spatial Sobolev tier and integral circle weight
action_owner: repository-construction -- no released source renormalization, stationary selector, physical quotient or observed map
target: SC-META-53 interacting-positive-state, global-dynamics and observed-carrier boundary MAP-TYPE=restriction
```

## K1445--K1446 — regular dressings and resolvent columns

Let `A=H_0+1` and `B_N=gV_N+C_N`, where `g` is fixed and nonzero and
`C_N` contains only deterministic vacuum and quadratic counterterms. Suppose a
unitary `U_N` preserves `D(A^(1/2))` and both

```text
A^(1/2) U_N A^(-1/2),  A^(1/2) U_N^(-1) A^(-1/2)
```

are uniformly bounded. A uniform free-form estimate for the dressed form pulls
back through `U_N^(-1)` to a uniform estimate for the original form. K1439
contradicts that estimate. Thus a unitary dressing uniformly equivalent to the
free form graph cannot repair the obstruction. Any successful original-theory
dressing must be singular in that graph, genuinely change the representation or
domain, add fourth-chaos/field-strength structure, or use a non-form mechanism.

The corresponding vacuum column has a sharper numerical boundary. If

```text
G_(r,N) Omega = (H_0+1)^(-r) W_N,
```

then its squared norm is exactly K1440's `S_(2r)(N)`. It converges iff
`r>5/2`. At the endpoint, every disjoint comparable dyadic block contributes a
fixed amount. In particular, the usual one-resolvent column `r=1` diverges
before boundedness or invertibility of a Gross/IBC-style transform can be
asked. Existence above the threshold is only a vacuum-column fact.

## K1447--K1448 — a coherent positive changed-representation control

To test what ultraviolet change is actually sufficient, change the dispersion
and covariance together:

```text
epsilon_beta(k)=omega_k^beta,
q_beta(k)=1/(2 epsilon_beta(k)),
H_beta=dGamma(epsilon_beta).
```

For the corresponding Wick fourth-particle vector and smoothing exponent
`s>=0`,

```text
||(H_beta+1)^(-s/2) W_(beta,N)||^2
```

converges exactly when `beta(s+4)>9`. Comparable cone blocks give the lower
power `R^(9-beta(s+4))`; ordered dyadic shells give the matching upper power,
and equality diverges logarithmically across shells. The checks are exact:
`beta=1` returns `s>5`, `s=0` requires `beta>9/4`, and the form-dual exponent
`s=1` requires `beta>9/5`.

For `beta>3`, the point covariance

```text
C_beta=sum_k 1/(2 omega_k^beta)
```

is finite. The full cutoff Wick potential is

```text
V_(beta,N)=integral [phi_N^4-6 C_(beta,N)phi_N^2+3 C_(beta,N)^2] dx.
```

These are all counterterms. Since
`x^4-6Cx^2+3C^2 >= -6C^2`, the potentials share the lower bound
`-6C_beta^2`. They converge in `L2(mu_beta)`. For `g>=0`, the limiting form is
dense, closed and bounded below. In Gaussian Q-space, stationarity of the
Ornstein--Uhlenbeck process gives

```text
E integral_0^t |V_N-V|(X_tau) d tau = t ||V_N-V||_1.
```

The common lower bound dominates the Feynman--Kac exponentials, so the
semigroups and resolvents converge strongly. This is a genuine interacting
Hamiltonian control in the changed `beta>3` representation, not a construction
for the physical `beta=1` covariance and not an interacting BRST theorem.

## K1449--K1450 — harmonic regeneration and the full-PDE hierarchy

The strict zero-harmonic route is not a generic nonlinear invariant sector.
Spatially averaging Maxwell on normalized `T3` gives

```text
partial_t E_h = -bar(j)
```

up to the fixed sign convention. Gauss constrains neither side's harmonic
electric component. Smooth data

```text
A=E=0,  phi=a exp(i k.x)v_q,  pi=0,
```

with `q,k` nonzero have zero charge density but nonzero mean current
`e q |a|^2 k`. Hence `E_h(0)=0` and `partial_t E_h(0)!=0`. K1442's fixed
`p!=0` phase theorem remains valid; the nonlinear PDE simply does not stay in
that restricted sector for generic data.

The unrestricted hierarchy nevertheless has a conditional summed closure. For
K1413's energies `F_n`, smooth cutoff solutions obey

```text
|dF_n/dt| <= C B(t)[F_n+sqrt(F_n F_(n+1))],
B(t)=1+||E||_H2+||phi||_H2 ||D_t phi||_H2.
```

The first term controls the pointwise radial coefficient by `H2 -> L-infinity`;
the second controls lifted-current work and shifts charge degree once. With

```text
G_rho=sum_n rho^(2n)F_n/n!,
D_rho=sum_(n>=1) n rho^(2n)F_n/n!,
```

the shift satisfies

```text
sum_n a_n sqrt(F_nF_(n+1)) <= G_rho/2+D_rho/(2rho^2).
```

Choose `R=rho^2` with `R'=-CB`. The weight derivative absorbs the `D_rho`
term, and while `R>0`,

```text
G_(rho(t))(t) <= G_(rho(0))(0) exp(C integral_0^t B).
```

The resulting exponential charge tail plus K1396's local difference estimate
makes charge-spectral cutoffs Cauchy at every fixed charge tier on that
interval. This controls both K1413 leakages with cutoff-independent constants,
but it assumes a common integrable `H2` coefficient and enough initial charge
analyticity. It is not an unconditional global-radius or global-flow theorem.

## K1451--K1452 — what a normalized observed selector must supply

K1368's scale degeneracy extends to the local operator-charge action. For
`c>0`, simultaneously send

```text
Q -> cQ,  A -> A/c,  kappa -> c^2 kappa,  mu -> mu/c^2,
```

and rescale the gauge parameter or ghost by `1/c`. The covariant derivative,
gauge kinetic term, regularizer, Euler/Gauss equations and BRST/BFV system are
equivalent. Local data see `Q/sqrt(kappa)`, `mu kappa`, charge ratios and
spectral subspaces, not a separate normalization of `Q`.

Globally, a circle homomorphism has integer degree and is an automorphism only
at degree `plus_or_minus 1`. The missing selector must therefore supply a
primitive action-stationary circle, the same action's kinetic coefficient, an
action-derived physical carrier, and a faithful domain-preserving observed
intertwiner `QJ=plus_or_minus JY_prim`.

There is one concrete scoped exclusion. K1357's fixed 27-dimensional K-type
has weights `{-4,-2,0,2,4}`, gcd two, so `exp(i pi Q)=1`. W222's
comparator-only `6Y={1,-4,2,-3,6,0}` is primitive. The fixed K-type cannot be
the complete observed carrier through a circle automorphism. This says nothing
against other K-types, other circles, nonlinear observation, or a source-owned
reduction.

The bridge census is now 121 rows: 79 satisfied, ten conditional, 28 excluded
and four missing. The four missing rows, K1145/K1150 `0/7` counts, source
register, physics ledger and every protected verdict remain unchanged.

## Exact next input

For the original `beta=1` quantum theory, the next constructive input must be
a singular dressing or genuinely non-Gaussian/domain-changed construction that
controls every particle-number sector and states all additional counterterms.
For the PDE, the next input must keep the analytic radius positive globally or
replace its `H2` coefficient by a conserved/dispersive spacetime control. For
source admission, provide the primitive action-stationary circle, kinetic
normalization, physical carrier and faithful observed intertwiner as one owned
tuple.
