---
title: "K1468--K1472 null-order, Wick-cocycle and finite-cutoff BRST boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1468--K1472 null-order, Wick-cocycle and finite-cutoff BRST boundary

Classification is `SOURCE_NATIVE_ROUTE` because the packet tests global-state
and positive-Hamiltonian requirements bordering SC-META-53. The Fourier
symbols, Gaussian field, cutoff Hamiltonians and BRST tower are repository
controls, not released GU data.

```gu-typed-objects
result: exact spatial-versus-Lorentz null-order boundary, semibounded Wick scalar cocycle, free-vacuum concentration and finite-cutoff BRST-compatible interacting Hamiltonian
carrier: repository Maxwell--massive-matter Fourier control and beta=1 Gaussian reduced Fock space tensored with the Gaussian gauge-boson/ghost complex LAYER=toy BRIDGE=positive-state-requirements CHIRALITY=N/A
pairing: Fourier energy pairing, free Gaussian expectation and positive tensor-product Hilbert pairing ON=repository_owned_controls
real_structure: Fourier conjugation, Gaussian real field and coordinatewise complex conjugation
grading: spatial frequency, Wiener chaos, particle number, cutoff filtration and ghost number
action_owner: repository-construction -- no released source null form, measure, renormalized Hamiltonian, BRST charge, physical quotient or observed map
target: SC-META-53 global-dynamics and interacting-positive-state boundary MAP-TYPE=restriction
```

## K1468 — one angular null factor is still one order short

Use K1463's near-parallel ray

```text
p=(1,0,0),       k=(K,1,0),
omega(k)=sqrt(M^2+K^2+1),
Phi=1+omega(k)-omega(k+p).
```

Rationalization gives the exact positive phase

```text
Phi = 2(M^2+1)/[(omega(k)+K)(1+omega(k)+omega(k+p))]
    = Theta(K^-2).
```

A spatial angular null numerator has only first-order angular vanishing:
`|p cross k|=1` on this ray. K1463's Coulomb-transverse numerator is likewise
`e dot (2k+p)=2` for `e=(0,1,0)`. Its raw quotient is therefore
`Theta(K^2)`, and even after one matter-energy normalization by `omega(k)` it
is `Theta(K)`. Spatial transversality or one `Q_ij`-type angular factor is not
same-tier.

The Lorentz numerator has one additional near-parallel order:

```text
N_0=omega(k)-K=(M^2+1)/(omega(k)+K)=Theta(K^-1).
```

Thus `N_0/Phi=Theta(K)` but `N_0/(omega(k)Phi)` tends to one. The missing
cancellation is precisely the time--space Lorentz combination. A successful
K1413 repair must recover that full-current structure, supply another
cancellation, or use a different spacetime/modified-energy mechanism. This
ray is not a no-go for those broader routes.

## K1469--K1470 — the semibounded square has a scalar cocycle and concentrates

On normalized `T^3`, write

```text
V_N = integral :phi_N^4: dx,
W_N = integral (phi_N^2-3C_N)^2 dx = V_N+6C_N^2.
```

K1431's Wick martingale implies, for `M>=N`,

```text
E(W_M | F_N)=W_N+6(C_M^2-C_N^2).
```

The defect is an exact additive scalar cocycle. Recentring `W_N+a_N` into an
exact martingale forces `a_N+6C_N^2` to be constant, returning `V_N` plus a
constant and a lower bound diverging to minus infinity. Retaining the
nonnegative square retains the divergent scalar cocycle. A scalar shift is a
dynamical phase but not invisible to spectral origins or resolvents.

The divergence is typical under the free vacuum, not merely a large mean.
Exact Wick orthogonality gives

```text
E W_N=6C_N^2,
Var(W_N)=24 integral C_N(z)^4 dz.
```

Since `|C_N(z)|<=C_N(0)` and Parseval gives
`integral C_N^2=sum q_k^2`, in three dimensions

```text
Var(W_N) <= 24 C_N(0)^2 sum q_k^2 = O(N^5).
```

K1433 supplies the matching `Omega(N^5)` cone bound, while
`C_N=Theta(N^2)`. Consequently

```text
E |W_N/(6C_N^2)-1|^2 = O(N^-3).
```

The nonnegative potential concentrates at its `N^4` free-vacuum scale. The
centered martingale has `L2` norm `Theta(N^(5/2))`, and no scalar recentering
makes the multiplication potentials `L2` bounded. This still does not prove
Mosco or strong-resolvent failure: cutoff-dependent states may move, localize
or change representation, and kinetic/domain compactness is a separate gate.

## K1471 — finite-cutoff interacting BRST compatibility

At every cutoff, tensor K1466's residual-invariant reduced Hilbert factor and
Friedrichs operator `A_N` with K1429's Gaussian based-gauge boson/ghost
factor. The differential

```text
D_N = 1 tensor d_gamma
```

remains densely defined, closed and nilpotent because the interaction is
reduced, residual-circle invariant and independent of based-gauge and ghost
coordinates. With `Delta_BRST={d_gamma,d_gamma^*}`,

```text
mathbb H_N=A_N tensor 1 + 1 tensor Delta_BRST
```

is nonnegative and self-adjoint as a tensor form sum. The two factors strongly
commute, `Delta_BRST` commutes with `d_gamma`, and `mathbb H_N` descends to
cohomology. Degree zero is the positive residual-invariant reduced factor
tensored with the gauge/ghost vacuum, the induced interacting Hamiltonian is
`A_N`, and higher cohomology remains zero.

This is a genuine finite-cutoff compatibility theorem, not a deformed or
source-derived interacting BRST charge. No common continuum form domain,
cutoff-stable commutator, interacting BRST limit or GU physical cohomology
follows.

## K1472 — admission replay

The bridge census is now 144 rows: 90 satisfied, ten conditional, 40 excluded
and four missing. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains
`UNCERTAIN`, the physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS /
2 OVER-DETERMINED, K1145/K1150 stay `0/7`, and no source, canon, paper,
prediction, confirmation or public status moves.

## Exact next input

For the PDE, derive the time component and continuity/constraint identity that
turns K1413's actual lifted current into the full Lorentz numerator, or prove a
bilinear spacetime/modified-energy estimate supplying the missing second
angular order together with the radial leakage. For the quantum arc, control
cutoff-dependent low-energy states and nonlinear form domains strongly enough
to prove or refute Mosco/strong-resolvent convergence after an explicitly
chosen energy recentering. Only on such a common limiting domain can the
finite-cutoff BRST compatibility be promoted to a closed interacting
continuum complex.
