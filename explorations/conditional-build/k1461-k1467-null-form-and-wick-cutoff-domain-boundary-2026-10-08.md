---
title: "K1461--K1467 null-form and Wick cutoff-domain boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1461--K1467 null-form and Wick cutoff-domain boundary

Classification is `SOURCE_NATIVE_ROUTE` because the packet tests global-state
and positive-Hamiltonian requirements bordering SC-META-53. The phases,
currents and Gaussian field are repository controls, not released GU data.

```gu-typed-objects
result: exact wave--Klein--Gordon null cancellation, transverse-current mismatch and finite-cutoff Wick nonlinear-domain construction
carrier: repository Maxwell--massive-matter Fourier control and beta=1 Gaussian symmetric Fock space LAYER=toy BRIDGE=positive-state-requirements CHIRALITY=N/A
pairing: Fourier energy pairing and positive Gaussian/Fock quadratic forms ON=repository_owned_controls
real_structure: Fourier conjugation and Gaussian real field
grading: spatial frequency, particle number, Wiener chaos and free energy
action_owner: repository-construction -- no released source null form, renormalized Hamiltonian, physical quotient or observed map
target: SC-META-53 global-dynamics and interacting-positive-state boundary MAP-TYPE=restriction
```

## K1461--K1463 — the exact null numerator and the actual-current seam

For `p != 0`, `M>0`,

```text
omega(k)=sqrt(M^2+|k|^2),
Phi(k,p)=|p|+omega(k)-omega(k+p),
N_0(k,p)=|p| omega(k)-p.k.
```

K1442's rationalization is exactly

```text
Phi = 2 N_0 / (|p|+omega(k)+omega(k+p)).
```

Consequently the Lorentz wave--Klein--Gordon null numerator cancels the small
divisor:

```text
N_0/Phi = (|p|+omega(k)+omega(k+p))/2.
```

The unnormalized correction loses one derivative, sharply, rather than the
two derivatives of `1/Phi`. With the energy/Riesz normalization
`N_0/(|p| omega(k))`, the quotient is bounded uniformly on the nonzero torus
modes:

```text
N_0/(|p| omega Phi)
 = (|p|+omega(k)+omega(k+p))/(2|p|omega(k))
 <= 1/|p|+1/omega(k) <= 1+1/M.
```

This is a genuine same-tier scalar multiplier for the declared branch, but it
contains the nonlocal normalizations `|nabla|^-1` and `omega(D)^-1`. It is not
yet a term in K1413's local lifted energy identity.

The actual Coulomb-transverse spatial current does not supply that numerator.
Let `p=(1,0,0)`, choose transverse polarization `e=(0,1,0)`, and take
`k=(K,1,0)`. Then

```text
e.(2k+p)=2,
Phi(k,p) ~ (M^2+1)/(2K^2),
e.(2k+p)/Phi(k,p) ~ 4K^2/(M^2+1).
```

Thus transversality kills the exactly parallel ray but not the fixed-offset
near-parallel rays responsible for the two-derivative loss. A successful PDE
repair must derive the full Lorentz null numerator, introduce the normalized
nonlocal structure, or use a different spacetime/modified-energy mechanism;
ordinary Coulomb projection alone does not close the hierarchy.

## K1464--K1466 — what finite-cutoff semiboundedness really buys

At every finite beta=1 cutoff, with point variance `C_N`, the Wick polynomial
satisfies the exact square completion

```text
x^4-6 C_N x^2+3 C_N^2=(x^2-3 C_N)^2-6 C_N^2.
```

On normalized `T^3`, adding the scalar vacuum shift `6 C_N^2` makes the
integrated interaction nonnegative. This gives more than the free-form test:
for `g>=0`, the sum of the free Fock form and

```text
g integral (phi_N(x)^2-3 C_N)^2 dx
```

is a dense closed nonnegative form on the nonlinear intersection domain. Its
Friedrichs operator controls every particle sector at each fixed cutoff.
K1459's obstruction therefore excludes uniform domination by the unchanged
free form, not finite-cutoff self-adjointness on a nonlinear domain.

The ultraviolet price is exact. If a scalar shift `d_N` is added to the
unshifted Wick polynomial, its lower bound is `d_N-6C_N^2`, while its free
vacuum expectation is `d_N`. Hence a cutoff-uniform lower bound forces

```text
d_N >= 6 C_N^2-O(1).
```

For the beta=1 covariance in three dimensions, `C_N=Theta(N^2)`, so the
vacuum expectation must grow at least as `N^4`. Choosing vacuum expectation
zero instead leaves the lower bound at `-6C_N^2`. No scalar energy shift alone
simultaneously gives a uniform lower bound and bounded free-vacuum expectation.
This is not a continuum no-go: non-Gaussian measures, singular dressings,
additional field-strength/fourth-chaos counterterms and nontrivial resolvent
renormalization remain open.

## K1467 — admission replay

The bridge census is now 137 rows: 85 satisfied, ten conditional, 38 excluded
and four missing. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains
`UNCERTAIN`, the physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS /
2 OVER-DETERMINED, K1145/K1150 stay `0/7`, and no source, canon, paper,
prediction, confirmation or public status moves.

## Exact next input

For the PDE, derive an action-compatible full Lorentz or normalized null
structure for the lifted current, or a spacetime/modified energy controlling
the near-parallel transverse ray together with the radial leakage. For the
original beta=1 quantum theory, prove cutoff convergence of the nonlinear
forms after every required counterterm, or construct a singular/non-Gaussian
domain in which the scalar vacuum-shift tension is absorbed. Only after an
admitted continuum Hamiltonian exists can the interacting BRST operator be
closed on its domain.
