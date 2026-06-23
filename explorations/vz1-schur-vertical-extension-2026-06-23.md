---
title: "VZ1: Full 14D Schur Complement — Vertical One-Form Extension"
status: exploration
doc_type: research_note
updated_at: "2026-06-23"
verdict: "VERTICAL_SECTOR_DOES_NOT_MODIFY_HORIZONTAL_SCHUR_RESULT; MIXED_COVECTOR_CASE_REMAINS_OPEN"
depends_on:
  - "explorations/vz1-schur-complement-symbol-2026-06-23.md"
  - "explorations/n1-signature-audit-y14-clifford-algebra-2026-06-22.md"
  - "NEXT-STEPS.md F1"
---

# VZ1: Full 14D Schur Complement — Vertical One-Form Extension

## Purpose

The prior note `vz1-schur-complement-symbol-2026-06-23.md` computed the Schur complement
for the minimal non-RS block

```
Q_min = (Omega^0 tensor S) direct-sum T
```

and noted that the vertical one-form sector `N* tensor S` was excluded. This note fills
that gap for the case of horizontal covectors `xi in H*` and determines whether the
vertical sector changes the conclusion.

**Bottom line.** For horizontal covectors `xi` (i.e., covectors in the `X^4` directions),
the vertical one-form sector contributes zero to `C psi_R` — the RS-to-non-RS output
block — because the principal symbol of `D_GU` at a horizontal covector sends purely
horizontal RS inputs to scalar and horizontal one-form spinors only. Therefore the full
Schur complement at horizontal covectors equals the minimal one. The favorable
`ker = 0` conclusion from the prior note is stable under vertical-sector extension.

The remaining open case is horizontal/vertical mixed covectors `xi = xi_H + xi_N`. That
case requires a fresh computation.

---

## 1. Setup: Full Non-RS Block

The split of the total spinor bundle along the section is

```
T*Y|_{Sigma} = H* direct-sum N*
dim H* = 4,   signature (3,1)    (horizontal = X^4 directions)
dim N* = 10,  signature (6,4)    (vertical = metric-fiber directions)
```

The full non-RS block is

```
Q_full = (Omega^0 tensor S) direct-sum T direct-sum (N* tensor S)
```

where `T = im j = {(1/4) gamma_a s e^a : s in S}` is the gamma-trace horizontal sector
and `N* tensor S` is the vertical one-form sector.

The Schur complement with the full `Q_full` block is

```
S_R^full(xi) = A(xi) - B_full(xi) E_full(xi)^{-1} C_full(xi).
```

---

## 2. The C Block at Horizontal Covectors

`C = P_Q sigma_D P_R` maps RS inputs to non-RS outputs.

For a purely RS input `psi_R in R` and a horizontal covector `xi in H*`:

```
sigma_D(xi)(0, psi_R) = (i_xi psi_R,  xi tensor 0 + F_xi psi_R).
```

The scalar spinor output:

```
i_xi psi_R = xi^a psi_a = chi in Omega^0 tensor S.
```

The one-form spinor output `F_xi psi_R`:

```
(F_xi psi_R)_a = xi_a gamma^b psi_b - gamma(xi) psi_a = xi_a chi - gamma(xi) psi_a.
```

This is a sum of horizontal one-form spinors. In particular, `F_xi psi_R in H* tensor S`
with no vertical one-form component.

**Conclusion for `C_N`.** For horizontal `xi`, the principal symbol maps any horizontal
RS input to

```
sigma_D(xi)(0, psi_R) in (Omega^0 tensor S) direct-sum (H* tensor S).
```

No vertical one-form component arises. Therefore

```
C_N psi_R := P_{N* tensor S} sigma_D(xi) psi_R = 0.
```

The RS-to-vertical output is zero at horizontal covectors.

---

## 3. B Block for Vertical One-Form Inputs

`B = P_R sigma_D P_Q` maps non-RS inputs to RS outputs.

For a vertical one-form input `eta tensor s` (with `eta in N*`):

```
sigma_D(xi)(0, eta tensor s) = (i_xi(eta tensor s),  F_xi(eta tensor s)).
```

Scalar spinor component. Since `xi in H*` and `eta in N*` and the gimmel metric is block
diagonal in the product coordinate gauge:

```
i_xi(eta tensor s) = g_Y(xi, eta) s = 0.
```

One-form spinor component:

```
F_xi(eta tensor s) = xi tensor c(eta)s - eta tensor c(xi)s.
```

The horizontal part is `xi tensor c(eta)s in H* tensor S`. Its RS projection:

```
P_R(xi tensor c(eta)s)_a = xi_a c(eta)s - (1/4) gamma_a gamma(xi) c(eta)s.
```

Gamma trace of this:

```
Gamma(P_R(xi tensor c(eta)s))
  = gamma^a(xi_a c(eta)s) - (1/4)(gamma^a gamma_a) gamma(xi) c(eta)s
  = gamma(xi) c(eta)s - gamma(xi) c(eta)s
  = 0.
```

(using `gamma^a gamma_a = 4` in 4D and the fact that anticommutation
`{gamma(xi), c(eta)} = 2 g_Y(xi,eta) = 0` for orthogonal H* and N*.)

So `P_R(xi tensor c(eta)s) in R`. Therefore the vertical one-form sector does
contribute to the B block:

```
B_N(eta tensor s) = P_R(F_xi(eta tensor s))
                  = xi_a c(eta)s - (1/4) gamma_a gamma(xi) c(eta)s.
```

The vertical part `- eta tensor c(xi)s in N* tensor S` projects out of R.

---

## 4. Impact on the Schur Complement

The full Schur complement correction relative to the minimal one is

```
Delta S = S_R^full - S_R^min = -(B_N) E_full^{-1} (C_N).
```

Since `C_N = 0` (established in §2), we have

```
Delta S = -(B_N) E_full^{-1} * 0 = 0.
```

**Theorem (horizontal covectors).** For all horizontal `xi in H*`:

```
S_R^full(xi) = S_R^min(xi).
```

The full 14D Schur complement including vertical one-forms equals the minimal horizontal
Schur complement of the prior note.

**Corollary.** The conclusion `ker S_R^full(xi) = 0` for `g_H(xi,xi) != 0` holds for the
full extended block.

---

## 5. Internal Consistency: E Block Extension

For completeness, record the E block for vertical inputs. For `eta tensor s in N* tensor S`:

```
sigma_D(xi)(0, eta tensor s) has:
  scalar component:          0
  horizontal one-form:       xi tensor c(eta)s - (1/4) gamma_a gamma(xi) c(eta)s  in T
  vertical one-form:         -eta tensor c(xi)s                                   in N*
```

The non-RS projection is:

```
E_NN(eta tensor s) = -eta tensor c(xi)s.
```

For horizontal `xi` with `xi2 != 0`, `c(xi)` is invertible (since `c(xi)^2 = xi2 Id`),
so `E_NN` is invertible on `N* tensor S`. There is also an off-diagonal term `E_{TN}`:

```
E_{TN}(eta tensor s) = P_T(xi tensor c(eta)s) = (1/4) gamma(xi) c(eta) s in T.
```

These off-diagonal entries matter for the full inversion of `E_full`, but since `C_N = 0`,
they do not enter the Schur complement correction.

---

## 6. The Remaining Open Case: Mixed 14D Covectors

For a general 14D covector `xi = xi_H + xi_N` with `xi_N in N*` nonzero, the computation
changes.

**Mixed scalar output.** `i_xi(eta tensor s) = g_Y(xi, eta) s = g_N(xi_N, eta) s != 0`
for vertical eta. So `C_N psi_R` is no longer automatically zero when `xi` has a
vertical component.

Specifically, for an RS input with vertical pullback:

```
C_N psi_R = P_{N*} (i_{xi_N} psi_R)   (if psi_R has vertical pullback)
```

For the horizontal RS subspace as defined above, `psi_R` is a horizontal one-form spinor.
Then `i_{xi_N} psi_R = g(xi_N, e_a) psi^a_R = 0` since xi_N and e_a are orthogonal in
the block-diagonal metric.

But if the full 14D RS definition uses both horizontal and vertical one-forms (e.g., if
the physical RS sector is the full kernel of a 14D gamma trace, not just the horizontal
gamma trace), then the computation depends on the precise definition of R in 14D.

**This case is not resolved in this note.** The prior note used `R = ker gamma_H` (horizontal
gamma trace); a 14D definition may use `ker gamma_Y` (full 14D gamma trace). Under the full
14D gamma trace, mixed covectors can generate nontrivial `C_N`, and the vertical extension
of the Schur complement would be genuinely non-trivial.

---

## 7. VZ Consequence

This note strengthens the VZ evasion candidate for the horizontal characteristic analysis:

```
ker S_R^full(xi) = 0 for xi in H*, g_H(xi,xi) != 0.
```

This rules out spacelike or timelike horizontal characteristics in the full Q_full
model. No spacelike acausality arises from horizontal propagation at the principal-symbol
level, even after including vertical one-forms in the eliminated block.

**What this does not prove:**

- Evasion for mixed 14D characteristic covectors is unresolved.
- The section-pulled 4D effective RS symbol has not been computed (F4 in the prior note).
- Lower-order curvature and connection terms are not included.

---

## 8. Assumptions and Failure Conditions

**Assumptions used.**

A1. Gimmel metric is block diagonal in H* and N* at the section (product coordinate gauge).
A2. The physical RS sector is defined as `R = ker gamma_H` using horizontal gamma trace.
A3. D_GU principal symbol is the rolled-up first-order model from the prior note.

**Failure conditions.**

F1. If the physical RS sector uses the full 14D gamma trace (R = ker gamma_Y), vertical
    one-forms may contribute a nonzero `C_N` at mixed covectors.

F2. If the gimmel metric has off-diagonal H-N entries (e.g., after choosing a non-product
    horizontal connection), the block-diagonal argument breaks.

F3. Mixed 14D covectors remain unanalyzed.

---

## 9. Verdict

For horizontal covectors and the horizontal gamma-trace RS projection:

- Vertical one-form inputs do not modify the Schur complement.
- Full `ker S_R^full(xi) = 0` for `g_H(xi,xi) != 0` is confirmed.
- The decisive remaining test is the mixed-covector Schur complement under the full 14D
  gamma-trace RS definition.

VZ1 status: still OPEN. This note closes the horizontal-covector vertical-extension gap.
The mixed-covector case is the next bounded computation.

---

## References

- `explorations/vz1-schur-complement-symbol-2026-06-23.md` (prior horizontal minimal result)
- `explorations/vz1-velo-zwanziger-analysis-2026-06-22.md` (VZ setup and OQ1)
- `explorations/n1-signature-audit-y14-clifford-algebra-2026-06-22.md` (signature (9,5))
