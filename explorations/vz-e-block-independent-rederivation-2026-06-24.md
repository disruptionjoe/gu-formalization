---
title: "Independent Q-Sector E-Block Rederivation"
date: 2026-06-24
status: exploration/independent-rederivation
verdict: CONDITIONAL_PROGRESS_NO_UPGRADE
target_gate: FC-VZ-1
owned_path: explorations/vz-e-block-independent-rederivation-2026-06-24.md
depends_on:
  - explorations/vz-proof-grade-verification-gate-2026-06-24.md
  - explorations/vz-schur-complement-2026-06-23.md
  - explorations/vz1-schur-complement-symbol-2026-06-23.md
  - explorations/vz-14d-mixed-covectors-2026-06-23.md
  - explorations/vz-e-block-direct-clifford-2026-06-23.md
---

# Independent Q-Sector E-Block Rederivation

## Verdict

This pass rederives the numerical Q-sector coefficients from the gamma-trace projector
and the VZ Schur notes' principal-symbol formula. In particular, the embedded trace-sector
coefficients

```text
1/14,  13/98
```

do follow from `j(s)_A = (1/14) gamma_A s`, `P_T = j Gamma`, and the Clifford contraction
identity

```text
gamma^A gamma(xi) gamma_A = (2 - 14) gamma(xi) = -12 gamma(xi).
```

However, I do **not** recommend upgrading FC-VZ-1 yet. The derivation is proof-grade only
conditional on one still-missing canonical definition: the repo must state, in one
authoritative place, that the 14D GU principal symbol used for the VZ block computation is
exactly

```text
sigma_D(xi)(u, psi) = (i_xi psi, xi tensor u + F_xi psi)
(F_xi psi)_A = xi_A gamma^B psi_B - gamma(xi) psi_A.
```

The repo contains this formula in the VZ Schur files, and it is derived there from
`Phi(d_A psi)`. But other VZ/lower-order notes describe the shiab term as
`Phi(F_A tensor psi)`, which is zero-order and would not by itself produce the same
`F_xi` principal-symbol block. Until that operator-level convention is reconciled, this
note should be counted as strong conditional progress, not as an FC-VZ-1 upgrade.

## Inputs Used

I used only the following algebraic inputs from the VZ files:

```text
n = 14
G = gamma(xi) = xi_A gamma^A
G^2 = g_Y(xi, xi) Id
Gamma(alpha) = gamma^A alpha_A
j(s)_A = (1/14) gamma_A s
P_T alpha = j(Gamma alpha) = (1/14) gamma_A gamma^B alpha_B
Q = Q_0 direct-sum Im(P_T)
```

and, conditionally, the VZ Schur principal-symbol formula:

```text
sigma_D(xi)(u, psi) = (i_xi psi, xi tensor u + F_xi psi)
(F_xi psi)_A = xi_A gamma^B psi_B - G psi_A.
```

No determinant factorization is used below.

## Derivation Of The E-Block

Write an element of the Q-sector as `(phi, j(s))`, where `phi` is in the scalar spinor
sector and `j(s)_A = (1/14) gamma_A s` is in the gamma-trace one-form sector.

### Scalar input

For input `(phi, 0)`, the symbol gives no scalar output and one-form output

```text
(xi tensor phi)_A = xi_A phi.
```

Its gamma trace is

```text
Gamma(xi tensor phi) = gamma^A xi_A phi = G phi.
```

Therefore the trace-sector projection is

```text
P_T(xi tensor phi)_A = (1/14) gamma_A G phi = j(G phi)_A.
```

So the scalar-to-trace entry is `j(G phi)`. If the second row is written as an embedded
one-form with the common `gamma_A` suppressed, this is the `1/14 G` coefficient. If the
second row is written in trace coordinate `s`, it is the coefficient `1 * G`.

### Gamma-trace input

For input `(0, j(s))`, the scalar output is

```text
i_xi j(s) = xi^A (1/14) gamma_A s = (1/14) G s.
```

This gives the top-right coefficient `1/14`.

The one-form output is

```text
(F_xi j(s))_A
  = xi_A gamma^B (1/14) gamma_B s - G (1/14) gamma_A s
  = xi_A s - (1/14) G gamma_A s,
```

using `gamma^B gamma_B = 14 Id`.

Now take its gamma trace:

```text
Gamma(F_xi j(s))
  = gamma^A xi_A s - (1/14) gamma^A G gamma_A s
  = G s - (1/14)(-12 G s)
  = (1 + 12/14) G s
  = (13/7) G s.
```

Projecting back into the embedded trace sector gives

```text
P_T(F_xi j(s))_A
  = (1/14) gamma_A ((13/7) G s)
  = (13/98) gamma_A G s.
```

Thus the embedded trace-sector coefficient is `13/98`.

## Coordinate Convention Warning

The same map has two equivalent-looking 2 by 2 matrices depending on how `Im(P_T)` is
coordinatized.

In trace-coordinate form, identifying `j(s)` with `s`, the map is

```text
E_coord(phi, s) = ((1/14) G s, G phi + (13/7) G s)

E_coord = [[0,        (1/14) G],
           [1 * G,    (13/7) G]]
```

In embedded-one-form notation, where the second component is literally `j(t)_A =
(1/14) gamma_A t`, the same output is

```text
E(phi, j(s)) =
  ((1/14) G s, (1/14) gamma_A G phi + (13/98) gamma_A G s).
```

Suppressing the common embedded `gamma_A` in the second row yields the displayed block
used by the 2026-06-24 gate:

```text
E_embed = [[0,        (1/14) G],
           [(1/14) G, (13/98) G]]
```

This is a notation choice, not a new algebraic operator. A proof-grade file must state
which convention is used before writing an inverse. For example, the inverse matrix in
trace coordinates is not textually identical to the inverse matrix in embedded notation,
because the second component has been rescaled by `j`.

## Direct Kernel Proof

Assume the VZ principal-symbol formula above is the actual 14D symbol. Let
`xi2 = g_Y(xi, xi) != 0`, so `G^2 = xi2 Id` and `G` is injective.

Suppose

```text
E(phi, j(s)) = 0.
```

The scalar row gives

```text
(1/14) G s = 0,
```

hence `G s = 0`. Applying `G` again gives

```text
xi2 s = G^2 s = 0,
```

so `s = 0`.

With `s = 0`, the trace row gives

```text
j(G phi) = 0.
```

Since `j` is injective (`Gamma j = Id`), this implies `G phi = 0`. Applying `G` again:

```text
xi2 phi = G^2 phi = 0,
```

so `phi = 0`.

Therefore `ker E(xi) = 0` for all non-null `xi`, conditional on the stated symbol model.
Since the Q fiber is finite-dimensional, injectivity gives invertibility. This proof uses
only the Clifford square and the gamma-trace projector; it does not use
`det(M) = det(E) det(S_R)`.

At `xi2 = 0`, this proof intentionally fails. For nonzero null `xi`, `G^2 = 0`, and the
Clifford action has nontrivial kernel in the spin module. Any nonzero `s in ker G` gives
`(0, j(s))` in the kernel of the displayed E-block. That is the expected null
characteristic locus, not a spacelike VZ failure.

## Schur Replay Without Determinants

Once E-invertibility is independently available, the Schur kernel proof is short and does
not require determinant circularity.

Let the full symbol be

```text
M(xi) = [[A, B],
         [C, E]]
```

with `M(xi)^2 = xi2 Id`. If `S_R psi_R = 0`, define

```text
v = -E^{-1} C psi_R.
```

Then

```text
M(xi)(psi_R, v) = (S_R psi_R, 0) = 0.
```

Applying `M(xi)` again gives

```text
0 = M(xi)^2(psi_R, v) = xi2 (psi_R, v).
```

For `xi2 != 0`, `psi_R = 0`. This replay uses E-invertibility but does not use any block
determinant factorization.

## Exact Missing Definitions Blocking Upgrade

I would keep FC-VZ-1 conditional until these are fixed:

1. **Canonical 14D principal symbol.** The VZ Schur derivation uses
   `D_GU(u, psi) = (d_A^* psi, d_A u + Phi(d_A psi))` at symbol level, producing
   `F_xi`. Other VZ notes describe the shiab term as `Phi(F_A tensor psi)`, a zero-order
   curvature term. The repo needs a single typed operator statement explaining which term
   is principal, which is lower-order, and why the actual first-order symbol is exactly the
   `F_xi` formula used above.
2. **Typed chirality bookkeeping.** The maps should be written as
   `Gamma: V^* tensor S^- -> S^+`, `j: S^+ -> V^* tensor S^-`, and
   `G: S^+ <-> S^-` (or the repo's preferred chirality convention). Current notes often
   suppress this, which is harmless for scalar coefficients but not proof-grade.
3. **One Q-sector coordinate convention.** The repo must choose whether the E-block matrix
   is written in trace coordinates `(phi, s)` or embedded coordinates `(phi, j(s))`. The
   coefficients `13/7` and `13/98` are the same map in different coordinates; inverse
   formulas must not mix them.
4. **Authoritative "actual Q-sector" statement.** For the full 14D RS split, `Q` should be
   stated as exactly `Q_0 direct-sum Im(P_T)` relative to the full 14D gamma trace. Earlier
   horizontal/vertical notes include extra normal one-form components for a different
   intermediate decomposition; those should not leak into FC-VZ-1.

## Upgrade Recommendation

Do **not** upgrade FC-VZ-1 yet.

This note independently recovers the coefficient arithmetic and gives a determinant-free
kernel proof, but it is still conditional on the unresolved operator-definition issue above.
The right status is:

```text
FC-VZ-1: CONDITIONALLY_SUPPORTED / not yet proof-grade closed
14D VZ leg: remains CONDITIONALLY_EVADED
```

If a later pass supplies the canonical symbol statement and fixes the trace-coordinate
convention, the algebra in this note should be enough to close the E-block invertibility
piece without determinant circularity.

## Proof-Grade Checklist

- [x] Read the 2026-06-24 proof-grade gate and 2026-06-23 VZ Schur/E-block files.
- [x] Re-derived `1/14` from the gamma-trace injection `j(s)_A = (1/14) gamma_A s`.
- [x] Re-derived `13/98` from `P_T F_xi j(s)` and `gamma^A G gamma_A = -12 G`.
- [x] Gave a direct non-null kernel proof for E using `G^2 = xi2 Id`.
- [x] Replayed the Schur proof without determinant factorization.
- [ ] Canonical typed principal symbol for the actual GU operator is reconciled.
- [ ] Chiral domain/codomain conventions are fixed.
- [ ] Trace-coordinate versus embedded-coordinate matrix convention is fixed before using
      any explicit inverse formula.
- [ ] FC-VZ-1 upgraded. Current recommendation: **remain conditional**.
