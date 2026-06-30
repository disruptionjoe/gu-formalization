---
title: "D_GU Guarded Symbol Certificate"
date: "2026-06-26"
status: exploration
doc_type: proof_gate
verdict: "GUARDED_SYMBOL_CERTIFICATE; PHI_ZERO_ORDER; NON_ELLIPTIC_SPLIT_SIGNATURE"
owned_path: "explorations/anomaly-and-bordism/dgu-guarded-symbol-certificate-2026-06-26.md"
depends_on:
  - "active-research/topological-generation-count-families-k3-chi-gate-2026-06-26.md"
  - "canon/shiab-existence-cl95.md"
  - "explorations/generation-sector/generation-count-cl95-dirac-derham-2026-06-22.md"
  - "explorations/shiab-operator/sc1-oq2-ellipticity-split-signature-2026-06-23.md"
  - "explorations/shiab-operator/sc1-oq2-split-signature-ellipticity-lemma-2026-06-23.md"
---

# D_GU Guarded Symbol Certificate

## 1. Verdict

This note records the safe symbol-level content of the Dirac-DeRham plus shiab
operator:

```text
D_GU = (d + d*) tensor 1_S + Phi_hat
```

on the rolled-up graded bundle

```text
V = (Omega^even tensor S^+) plus (Omega^odd tensor S^-),
S = H^64.
```

The certificate is deliberately guarded:

```text
Phi is zero-order and does not change the principal symbol.
The characteristic set remains the split-signature null cone.
Standard Riemannian ellipticity is not obtained for the physical (9,5) operator.
```

So this note narrows the symbol gate, but it does not close the families-index or
Fredholm pushforward gate.

## 2. Principal Symbol

For the unperturbed twisted de Rham part, the first-order principal symbol at a
covector `xi in T*_y Y14` is Clifford multiplication:

```text
sigma_1((d + d*) tensor 1_S)(xi) = c_Y(xi) tensor 1_S.
```

The shiab operator is the Clifford contraction from the Layer 1 canon:

```text
Phi(alpha tensor s) = sum_a e^a tensor c(iota_{e_a} alpha) . s.
```

It contains no derivatives of the field variable. Therefore:

```text
sigma_1(Phi_hat)(xi) = 0
```

and the full first-order principal symbol is:

```text
sigma_1(D_GU)(xi) = c_Y(xi) tensor 1_S.
```

## 3. Characteristic Set

In the physical split-signature geometry, `Y14` carries the gimmel metric of
signature `(9,5)`. The Clifford identity is:

```text
c_Y(xi)^2 = g_Y^{-1}(xi, xi) Id.
```

Consequences:

| covector type | symbol behavior |
|---|---|
| `g_Y^{-1}(xi,xi) != 0` | `c_Y(xi)` is invertible |
| `xi != 0` and `g_Y^{-1}(xi,xi) = 0` | `c_Y(xi)` is nilpotent/non-invertible |

Therefore the characteristic set is:

```text
Char(D_GU) = { xi != 0 : g_Y^{-1}(xi, xi) = 0 }.
```

This is the light cone/null cone. Since `Phi_hat` is zero-order, it does not
remove or deform that characteristic set.

## 4. What This Does Not Prove

This certificate does not prove standard ellipticity of the physical operator.
The false shortcut is:

```text
xi != 0 implies c_Y(xi) invertible.
```

That implication is true in a positive-definite Riemannian Clifford model. It is
false in split signature because nonzero null covectors exist.

This certificate also does not prove:

```text
D_t = (d + d*) tensor 1_S + t Phi_hat
```

remains in a fixed H-linear Fredholm class. Such a statement requires compatible
domains, end/boundary conditions, and a valid Fredholm framework.

## 5. Impact On The Topological Generation-Count Gate

The safe update to the topological families/K3 route is:

```text
shiab role = LOWER_ORDER_BUT_DOMAIN_OPEN
```

not:

```text
shiab role = INDEX_PRESERVING_HOMOTOPY
```

and not:

```text
whole operator = standard elliptic Dirac operator on physical Y14.
```

Index-theorem use still requires one of the following independent analytic
replacements:

1. An explicit Riemannian compactification or Wick-rotated control model.
2. APS boundary conditions on a specified spatial/end cutoff.
3. b/0/scattering Fredholm theory for the noncompact fibration.
4. A deformation or bounded-transform argument proving the same H-linear index
   class for the physical operator.

Until one of those is supplied, the active gate remains:

```text
OPEN_GATED; FAMILIES_PUSHFORWARD_NOT_CLOSED.
```

## 6. Machine-Readable Summary

```json
{
  "artifact": "D_GU_GUARDED_SYMBOL_CERTIFICATE",
  "version": "2026-06-26",
  "status": "exploration",
  "verdict": "GUARDED_SYMBOL_CERTIFICATE_PHI_ZERO_ORDER_NON_ELLIPTIC_SPLIT_SIGNATURE",
  "principal_symbol": "sigma_1(D_GU)(xi)=c_Y(xi) tensor 1_S",
  "phi_order": 0,
  "characteristic_set": "null_cone_gY_xi_xi_equals_0",
  "standard_riemannian_ellipticity_for_physical_operator": false,
  "families_pushforward_closed": false,
  "safe_gate_value": "LOWER_ORDER_BUT_DOMAIN_OPEN",
  "blocked_shortcuts": [
    "xi_nonzero_implies_c_xi_invertible_in_split_signature",
    "phi_zero_order_implies_standard_ellipticity",
    "symbol_certificate_implies_fredholm_pushforward",
    "symbol_certificate_implies_generation_count"
  ]
}
```
