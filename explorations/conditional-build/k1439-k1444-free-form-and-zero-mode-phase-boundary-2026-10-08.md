---
title: "K1439--K1444 free-form and zero-mode phase boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1439--K1444 free-form and zero-mode phase boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE` only because the packet tests the
positive-state and global-dynamics requirements bordering SC-META-53. The
Gaussian/Fock Hamiltonian and Maxwell--matter phase are repository controls,
not released GU data.

```gu-typed-objects
result: free-Hamiltonian form-domain obstruction and strict zero-harmonic phase classification
carrier: symmetric Fock space over the massive equal-time torus field and the repository multi-charge Maxwell--matter Fourier phase space LAYER=toy BRIDGE=maximal-compact-charge-reduction CHIRALITY=N/A
pairing: positive Fock pairing and weighted sequence-space pairing ON=repository_owned_controls
real_structure: Fourier conjugation on the real scalar field and compatible-real charge sectors
grading: particle number, Wiener chaos degree, free-Hamiltonian scale, charge and spatial Sobolev tier
action_owner: repository-construction -- no released source measure, renormalization prescription, action-stationary selector or observed-state map
target: SC-META-53 interacting-positive-state and global-dynamics boundary MAP-TYPE=restriction
```

## K1439 — obstruction on the fixed free form domain

Let `H_0=dGamma(omega)` be K1430's positive free Hamiltonian,
`omega_k=sqrt(m^2+|k|^2)`, and let

```text
W_N = (integral :phi_N^4: dx) Omega
```

be the fourth-particle vector created from the vacuum. The Fock energy is
diagonal on that sector, so

```text
||(H_0+1)^(-1/2) W_N||^2
 = 24 sum_(k1+...+k4=0)
      product_i (2 omega_ki)^(-1) / (1+sum_i omega_ki).
```

Use K1433's cone: choose `k1,k2,k3` componentwise between `N/8` and
`N/4`, with `k4=-(k1+k2+k3)`. There are order `N^9` terms, four covariance
weights cost order `N^-4`, and the free-form resolvent weight costs order
`N^-1`. Hence the squared dual norm grows at least as `c_m N^4`.

A cutoff-uniform form estimate on `D((H_0+1)^(1/2))` would, after fixing the
second argument to the vacuum, make this vector uniformly bounded in the
dual form norm. It does not. Vacuum and quadratic counterterms lie in the
zeroth and second particle sectors, so they cannot cancel the fourth-particle
component. Thus a fixed nonzero coupling does not give a uniform KLMN form on
the unchanged free form domain with only those counterterms.

This is not a general operator no-go. A changed representation or domain,
cutoff-dependent dressing, field-strength or quartic-sector counterterm, or a
strong-resolvent construction not obtained by fixed-domain form convergence
remains outside the theorem.

## K1440--K1441 — sharp negative scale and running-coupling boundary

For general free-Hamiltonian smoothing exponent `s`, set

```text
S_s(N)=||(H_0+1)^(-s/2)W_N||^2.
```

Comparable-momentum dyadic cone blocks of radius `R` contribute at least
`c R^(5-s)`. They force divergence for `s<5`; at `s=5`, disjoint dyadic
blocks each contribute a fixed positive amount. Conversely, order the dyadic
radii `L~N1~N2>=N3>=N4`. Momentum conservation lets one count by
`k1,k3,k4`, giving the unweighted shell estimate

```text
L^3 N3^3 N4^3 L^-2 N3^-1 N4^-1
 = L N3^2 N4^2.
```

The dyadic sums are dominated by `C L^5`, and the energy weight adds `L^-s`.
Therefore `W_N` converges in the negative scale for every `s>5` and is
unbounded for every `s<=5`. The form-dual exponent is `s=1`, far below the
threshold.

If the quartic is multiplied by `g_N`, the K1439 cone gives

```text
||(H_0+1)^(-1/2) g_N W_N||^2 >= c |g_N|^2 N^4.
```

Uniform control on the same free domain therefore requires
`|g_N|=O(N^-2)`. That decay only removes this necessary vacuum-sector
obstruction; it does not construct a nonzero interacting limit or settle any
other particle sector.

## K1442 — strict zero-harmonic phase is nonresonant

For a nonzero Maxwell mode `p`, charge-dependent positive mass
`M_q^2=m^2+mu q^2`, and `omega_q(k)=sqrt(M_q^2+|k|^2)`, consider

```text
Phi_q(k,p)=|p|+omega_q(k)-omega_q(k+p).
```

The exact rationalization is

```text
Phi_q(k,p)
 = 2(|p| omega_q(k)-p.k)
   / (|p|+omega_q(k)+omega_q(k+p)).
```

Writing `k_parallel=k.p/|p|` and `k_perp=k-k_parallel p/|p|`, the numerator is

```text
|p| omega_q(k)-p.k
 = |p|(M_q^2+|k_perp|^2)/(omega_q(k)+k_parallel) > 0.
```

Thus every strict nonzero mode in this sign branch is nonresonant. K1435's
harmonic `p=0` witness does not transfer. But along `k=K p/|p|`,

```text
Phi_q(k,p) ~ M_q^2 |p|/(2K^2),
```

so there is no uniform spectral gap.

## K1443--K1444 — optimal derivative cost and admission

For fixed `p!=0`, the scalar homological multiplier

```text
(T_p f)(k)=Phi_q(k,p)^(-1) f(k)
```

obeys `Phi_q(k,p)^(-1)<=C_(p,M_q)<k>^2`; hence it maps `h^(s+2)` to
`h^s`. The parallel sequence gives the matching quadratic growth, so loss of
two spatial derivatives is optimal. In particular, if cutoff forcing is
Cauchy in `h^(s+2)`, its transformed sequence is Cauchy in `h^s` for each
fixed nonzero mode.

This is the explicit finite-tier scalar consequence requested after K1438,
but it is not the full current normal form: differentiated numerators, the sum
over Maxwell modes, nonlinear composition, constraints, coercive energy and
global evolution remain open. Strict zero-harmonic restriction removes exact
resonance, not the same-tier obstruction.

The bridge census now has 113 rows: 76 satisfied, nine conditional, 24
excluded and four missing. Source selection, one source action, completed
interacting positive cohomology/global PDE evolution, and observed export
remain missing. K1145/K1150 remain `0/7`; protected statuses do not move.

## Exact next input

The quantum arc now requires a genuinely dressed or changed-domain
renormalization construction—stating every additional counterterm and proving
semibounded closed forms or a self-adjoint resolvent limit beyond fixed-domain
KLMN convergence. The PDE arc requires a gauge-covariant spacetime/null-form
estimate or a summed nonzero-mode higher-tier hierarchy that absorbs the
differentiated current and yields cutoff-uniform nonlinear Cauchy control.
Source admission still requires an action-stationary observed-carrier selector
fixing `Q` and its normalization.
