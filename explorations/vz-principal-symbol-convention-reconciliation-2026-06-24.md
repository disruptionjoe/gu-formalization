---
title: "VZ Principal-Symbol Convention Reconciliation"
date: 2026-06-24
status: exploration/convention-reconciliation
verdict: COHERENT_AS_ROLLED_COMPOSITE_BUT_UNDERDEFINED_IN_CANON
target_gate: FC-VZ-1
owned_path: explorations/vz-principal-symbol-convention-reconciliation-2026-06-24.md
depends_on:
  - explorations/vz-proof-grade-verification-gate-2026-06-24.md
  - explorations/vz-e-block-independent-rederivation-2026-06-24.md
  - explorations/vz-schur-complement-2026-06-23.md
  - explorations/vz1-schur-complement-symbol-2026-06-23.md
  - explorations/sc1-shiab-domain-codomain-2026-06-23.md
  - explorations/sc1-oq2-ellipticity-split-signature-2026-06-23.md
  - explorations/sc1-oq2-split-signature-ellipticity-lemma-2026-06-23.md
  - explorations/sc1-oq3-gauge-equivariance-2026-06-23.md
  - canon/no-go-class-relative-map.md
  - canon/shiab-existence-cl95.md
  - DERIVATION-PROGRESS.md
---

# VZ Principal-Symbol Convention Reconciliation

## Verdict

There is a coherent convention under which the VZ principal-symbol formula

```text
sigma_D(xi)(u, psi) = (i_xi psi, xi tensor u + F_xi psi)
(F_xi psi)_A = xi_A gamma^B psi_B - gamma(xi) psi_A
```

is valid: the first-order `F_xi` block must be the principal symbol of the composite

```text
Phi_2 o d_A : Omega^1(Y^14) tensor S -> Omega^1(Y^14) tensor S,
```

where `Phi_2` is the SC1 algebraic shiab map on 2-forms.

This does **not** contradict the SC1/OQ2 statement that the shiab `Phi_2` itself is
zero-order. The derivative order comes from `d_A`, not from `Phi_2`.

However, the current repo is still underdefined at the proof-grade level. The canon files
state the algebraic map `Phi_2` and many lower-order VZ files state a zero-order curvature
term `Phi(F_A tensor psi)`, but there is not yet one primary typed definition of the actual
rolled-up GU operator saying whether the one-form block contains `Phi_2(d_A psi)`. Until
that primary definition is supplied, FC-VZ-1 and the VZ E-block formula remain conditional.

## Distinct Operators Currently Called `Phi` Or Shiab

### 1. Algebraic shiab on 2-forms

This is the SC1/canon object:

```text
Phi_2: Omega^2(Y^14) tensor S -> Omega^1(Y^14) tensor S
Phi_2(alpha tensor s)_A = c(i_{e_A} alpha) s
```

or, in the ad-valued gauge-equivariant version,

```text
Phi_2: Omega^2(Y^14, ad P) tensor S -> Omega^1(Y^14) tensor S
Phi_2(alpha tensor psi)_A = rho_*(i_{e_A} alpha) psi.
```

Derivative order in the spinor field: **0**. It is fiberwise. It has no `xi`-dependent
order-1 symbol.

This is the operator established by:

- `canon/shiab-existence-cl95.md`
- `explorations/sc1-shiab-domain-codomain-2026-06-23.md`
- `explorations/sc1-oq3-gauge-equivariance-2026-06-23.md`

### 2. Shiab applied to a covariant derivative

This is the first-order composite used in the original VZ Schur-symbol note:

```text
Phi_d := Phi_2 o d_A
Phi_d: Omega^1(Y^14) tensor S -> Omega^1(Y^14) tensor S.
```

For a pure one-form spinor `beta tensor s`, the order-1 part of `d_A(beta tensor s)` is
`xi wedge beta tensor s`. With the VZ wedge convention,

```text
i_{e_A}(xi wedge beta) = xi_A beta - beta_A xi,
```

so

```text
sigma_1(Phi_d)(xi)(beta tensor s)_A
  = xi_A c(beta) s - beta_A c(xi) s.
```

For a general one-form spinor `psi = e^B tensor psi_B`, this is

```text
(F_xi psi)_A = xi_A gamma^B psi_B - gamma(xi) psi_A.
```

Derivative order in `psi`: **1**. The connection part of `d_A = d + A wedge` also creates
zero-order terms such as `Phi_2(A wedge psi)`, but the order-1 symbol is the displayed
`F_xi`.

This is the only identified source of the VZ `F_xi psi` block.

### 3. Zero-order curvature coupling

Several lower-order VZ files write the shiab contribution as

```text
Phi_F(A)(psi) := Phi_2(F_A tensor psi),
```

where `F_A` is the Sp(64) gauge curvature.

Derivative order in `psi`: **0**. If `A` is treated as a dynamical field, `F_A` contains
one derivative of `A`, but in the VZ characteristic problem for the spinor/RS field with
background connection fixed, this is a coefficient, not a derivative of `psi`.

This term contributes to `sigma_0(D_GU)`, not `sigma_1(D_GU)`. It cannot produce the
`F_xi psi` principal-symbol block, and it cannot by itself justify the E-block
trace-to-trace coefficient `13/98`, which comes from `P_T F_xi j(s)`.

### 4. Principal-symbol contribution `F_xi`

`F_xi` is not a standalone operator named shiab. It is the homogeneous degree-1 symbol of
`Phi_2 o d_A`:

```text
F_xi = sigma_1(Phi_2 o d_A)(xi).
```

Derivative order: **symbol of an order-1 composite**.

Its VZ role is to provide the one-form-to-one-form first-order block in

```text
sigma_D(xi)(u, psi) = (i_xi psi, xi tensor u + F_xi psi).
```

The E-block coefficients in the 2026-06-24 rederivation are conditional on precisely this
symbol:

- scalar input `phi` gives `P_T(xi tensor phi) = j(gamma(xi) phi)`;
- trace input `j(s)` gives scalar output `(1/14) gamma(xi) s`;
- trace input `j(s)` gives trace output through `P_T F_xi j(s)`, producing `13/98` in
  embedded coordinates.

If the actual GU operator has no `Phi_2 o d_A` term, this E-block is not the current
operator's E-block and must be rederived from scratch.

## Canonical Convention That Would Make VZ Coherent

The clean proof-grade convention should be stated as follows.

Let the algebraic shiab be denoted `Phi_2`. Define the rolled-up first-order operator on
the VZ `0/1` sector by

```text
D_roll(u, psi)
  = (d_A^* psi, d_A u + Phi_2(d_A psi)) + Z_A(u, psi),
```

where `Z_A` contains only zero-order terms, including spin-connection terms, mass terms,
section-pullback/extrinsic terms, and possible curvature insertions such as
`Phi_2(F_A tensor psi)`.

Then the order-1 symbol is exactly

```text
sigma_1(D_roll)(xi)(u, psi)
  = (i_xi psi, xi tensor u + F_xi psi),
```

with

```text
F_xi = sigma_1(Phi_2 o d_A)(xi).
```

Under this convention:

| Term | Operator type | Order in `psi` | Principal-symbol contribution |
|---|---:|---:|---|
| `d_A^* psi` | codifferential | 1 | `i_xi psi` |
| `d_A u` | covariant derivative of scalar spinor | 1 | `xi tensor u` |
| `Phi_2(d_A psi)` | algebraic shiab after derivative | 1 | `F_xi psi` |
| `Phi_2(A wedge psi)` inside `Phi_2(d_A psi)` | connection coefficient piece | 0 | none |
| `Phi_2(F_A tensor psi)` | curvature insertion | 0 in `psi` | none |
| `gamma^A omega_A psi` | spin connection | 0 | none |
| mass / `II_s` / section corrections | lower-order coefficients | 0 | none |

This convention is internally coherent and reconciles the language:

- `Phi_2` itself remains zero-order, as SC1 and SC1-OQ2 require.
- `Phi_2 o d_A` is first-order and supplies `F_xi`.
- `Phi_2(F_A tensor psi)` is a separate zero-order curvature coupling.
- The lower-order VZ files are correct only if they are read as discussing `Z_A`, not as
  defining the full first-order rolled-up operator.

## What Is Still Missing

The missing primary definition is:

```text
Actual GU rolled-up operator on the VZ 0/1 sector:
Does D_GU include Phi_2(d_A psi) in the one-form-to-one-form block,
or does it include only the zero-order curvature insertion Phi_2(F_A tensor psi)?
```

The repo currently contains both kinds of language:

- `explorations/vz1-schur-complement-symbol-2026-06-23.md` explicitly assumes
  `D_GU(u, psi) = (d_A^* psi, d_A u + Phi(d_A psi))` and defines
  `F_xi := sigma(Phi o d_A)(xi)`.
- `explorations/vz-oq2-lower-order-curvature-2026-06-23.md` and
  `explorations/vz-subprincipal-symbol-rs-2026-06-23.md` describe the shiab term as
  `Phi(F_A tensor psi)`, strictly zero-order.
- SC1 and its OQ files prove that the algebraic `Phi_2` is zero-order; they do not, by
  themselves, define whether the full operator contains the first-order composite
  `Phi_2 o d_A`.

These statements are compatible only if the repo reserves different names for the
different composites. Without that naming discipline, the same word "shiab" is doing two
operator-level jobs.

A proof-grade VZ upgrade also needs the typed chirality/domain convention for this operator:

```text
d_A psi in Omega^2 tensor S^{?}
Phi_2(d_A psi) in Omega^1 tensor S^{?}
d_A^* psi in Omega^0 tensor S^{?}
d_A u in Omega^1 tensor S^{?}
```

The VZ algebra suppresses these chiralities. That suppression is acceptable for the local
coefficient check, but not for a canonical FC-VZ-1 closure.

## Impact On Current VZ Claims

### If the canonical convention above is adopted

The VZ principal-symbol formula with `F_xi psi` is valid as a convention-level symbol
calculation. The 2026-06-24 E-block rederivation then correctly identifies the source of
the `13/98` trace-to-trace coefficient:

```text
P_T F_xi j(s).
```

In that case the remaining FC-VZ-1 work is not this convention issue but the already named
proof-grade package:

- authoritative typed operator definition;
- Q-sector coordinate convention;
- independent E-block derivation/provenance;
- inter-session or external verification of the non-null E-block kernel/inverse.

### If the actual operator has only zero-order shiab curvature coupling

Then the current VZ E-block computation is not a computation of the actual operator. The
principal block would not contain `F_xi psi`; in particular the displayed `13/98` entry
would not follow from the zero-order curvature coupling. FC-VZ-1 would remain open and the
Schur complement would need to be recomputed for the true first-order symbol.

### Present status

The honest current status is therefore:

```text
Convention-level reconciliation: coherent if D_GU contains Phi_2 o d_A.
Canonical repo definition: missing / underdefined.
FC-VZ-1: conditional, not proof-grade closed.
14D VZ: remains CONDITIONALLY_EVADED.
4D principal-symbol VZ: remains CONDITIONALLY_RESOLVED, with existing subprincipal and
full-dynamical gates unchanged.
```

This note does not upgrade VZ. It identifies the exact hinge: the repo must promote one
typed rolled-up operator definition to canon before the `F_xi` E-block can be used as
proof-grade evidence.

## Recommended Notation Fix

Use distinct symbols downstream:

```text
Phi_2                  algebraic zero-order 2-form contraction
Phi_d := Phi_2 o d_A   first-order rolled-up differential composite
Phi_F := Phi_2(F_A tensor -)   zero-order curvature coupling
F_xi := sigma_1(Phi_d)(xi)     principal-symbol map
```

Then the VZ statement can be made without ambiguity:

```text
The FC-VZ-1 E-block is computed for D_roll whose one-form block contains Phi_d.
It is not computed from Phi_F.
```

