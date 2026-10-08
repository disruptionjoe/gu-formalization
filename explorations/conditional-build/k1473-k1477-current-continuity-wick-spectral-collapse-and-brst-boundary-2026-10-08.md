---
title: "K1473--K1477 current continuity, Wick spectral collapse and BRST boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1473--K1477 current continuity, Wick spectral collapse and BRST boundary

Classification is `SOURCE_NATIVE_ROUTE` because the packet tests global-state
and positive-Hamiltonian requirements bordering SC-META-53. The scalar-current
Fourier symbols, Gaussian field, cutoff Hamiltonians and BRST tower are
repository controls, not released GU data.

```gu-typed-objects
result: exact longitudinal-versus-transverse current-conservation boundary, Gaussian entropy localization barrier, unshifted Wick resolvent collapse and BRST spectral transfer
carrier: repository Maxwell--massive-matter Fourier control and beta=1 Gaussian reduced Fock space tensored with the Gaussian gauge-boson/ghost complex LAYER=toy BRIDGE=positive-state-requirements CHIRALITY=N/A
pairing: Lorentz current pairing, free Gaussian relative entropy and positive tensor-product Hilbert pairing ON=repository_owned_controls
real_structure: Fourier conjugation, Gaussian real field and coordinatewise complex conjugation
grading: spatial frequency, Wiener chaos, particle number, cutoff filtration and ghost number
action_owner: repository-construction -- no released source current decomposition, measure, ground-energy counterterm, renormalized Hamiltonian, BRST charge, physical quotient or observed map
target: SC-META-53 global-dynamics and interacting-positive-state boundary MAP-TYPE=restriction
```

## K1473 — continuity does not control the transverse current

For equal-mass positive-frequency scalar modes at momenta `k` and `k+p`, the
bilinear current has the standard symbol

```text
J_0=omega(k+p)+omega(k),       J=2k+p,
q=(omega(k+p)-omega(k),p).
```

The continuity identity is exact:

```text
q_0 J_0-p dot J
=omega(k+p)^2-omega(k)^2-(|k+p|^2-|k|^2)
=0.
```

It determines `p dot J`, hence only the current component parallel to `p`.
For the Coulomb projector `P_T(p)=I-p tensor p/|p|^2`, every transverse
polarization `e dot p=0` satisfies

```text
e dot P_T J=e dot J=2 e dot k.
```

On K1463's ray `p=(1,0,0)`, `k=(K,1,0)`, `e=(0,1,0)`, continuity holds while
`e dot J=2` and the phase remains `Theta(K^-2)`. The quotient is still
`Theta(K^2)`. Thus adding the time component and current conservation does not
by itself manufacture K1461's Lorentz numerator inside the Coulomb-transverse
leakage. A secondary bilinear cancellation, spacetime estimate or nonlinear
modified energy remains possible.

## K1474 — Gaussian entropy makes low-potential localization expensive

Let

```text
W_N=integral (phi_N^2-3C_N)^2 dx,
A_N={W_N<=3C_N^2}.
```

The threshold is half the free-vacuum mean. K1470 and Chebyshev give
`delta_N=mu(A_N)=O(N^-3)`. For a normalized form vector `psi`, put
`f=|psi|^2` and `m_N=int_A_N f dmu`. Data processing of relative entropy to
the two-point partition `{A_N,A_N^c}` gives

```text
Ent_mu(f) >= m_N log(1/delta_N)-log 2.
```

Since `H_0=dGamma(omega)` has `omega>=omega_0>0`, the Gaussian Gross
log-Sobolev inequality supplies a cutoff-independent constant `c_LS` with

```text
Ent_mu(|psi|^2) <= c_LS q_0[psi].
```

Consequently

```text
m_N <= (c_LS q_0[psi]+log 2)/log(1/delta_N).
```

For large `N`, either `q_0[psi]>=log(1/delta_N)/(4c_LS)`, or `m_N<=1/2` and
the Wick-square energy is at least `(3/2)C_N^2`. For every fixed `g>0`,

```text
inf_{||psi||=1} [q_0[psi]+g int W_N|psi|^2 dmu]
 >= min(log(1/delta_N)/(4c_LS),(3g/2)C_N^2)
 = Omega(log N).
```

This uses the free Gaussian representation and the unshifted nonnegative
square. It does not determine the sharp ground-energy asymptotic.

## K1475 — the unshifted resolvents collapse

Let `H_N` be K1466's self-adjoint operator and `E_N=inf spec(H_N)`. K1474
gives `E_N -> infinity`, at least logarithmically. Hence, for every
`lambda>0`,

```text
||(H_N+lambda)^(-1)|| = 1/(E_N+lambda) -> 0.
```

Zero is not the resolvent of a densely defined self-adjoint operator, so the
unshifted family has no finite self-adjoint strong-resolvent limit. It escapes
to the generalized infinite operator.

For `K_N=H_N-a_N`, a uniformly lower-bounded nontrivial norm-resolvent or
semibounded Mosco limit requires

```text
E_N-a_N=O(1).
```

Thus the scalar counterterm must track the true interacting ground energy up
to bounded error. K1469's exact projective shift `6gC_N^2` is not known to do
so. Proving `E_N-6gC_N^2=O(1)`, or finding another ground-energy counterterm
with recovery-sequence compactness, is a new theorem.

## K1476 — the BRST factor inherits the collapse

K1471 gives

```text
mathbb H_N=H_N tensor 1+1 tensor Delta_BRST,
```

where `Delta_BRST>=0` has a zero-energy harmonic gauge/ghost vacuum. Therefore
`inf spec(mathbb H_N)=E_N` and the unshifted full resolvents also converge to
zero in norm. If `P_harm` denotes the harmonic-vacuum projection, then

```text
P_harm(mathbb H_N-a_N+lambda)^(-1)P_harm
=(H_N-a_N+lambda)^(-1) tensor P_harm.
```

Any nontrivial continuum Hamiltonian on degree-zero BRST cohomology must first
supply the recentered matter limit with the same counterterm. The fixed closed
differential remains algebraically stable, but it cannot create the missing
matter-domain compactness or Hamiltonian limit.

## K1477 — admission replay

The bridge census is now 152 rows: 95 satisfied, ten conditional, 43 excluded
and four missing. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains
`UNCERTAIN`, the physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS /
2 OVER-DETERMINED, K1145/K1150 stay `0/7`, and no source, canon, paper,
prediction, confirmation or public status moves.

## Exact next input

For the PDE, continuity alone is exhausted: construct a genuine bilinear
spacetime or secondary-null estimate for the transverse current together with
the radial leakage, or a nonlinear modified energy that cancels both. For the
quantum arc, estimate the true interacting ground energy `E_N`, choose and
justify `a_N=E_N+O(1)`, and prove Mosco recovery/liminf plus compactness on one
common limiting domain. Only that recentered matter limit can support a
continuum version of K1471's BRST-compatible Hamiltonian.
