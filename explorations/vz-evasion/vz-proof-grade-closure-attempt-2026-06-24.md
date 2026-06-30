---
title: "VZ Proof-Grade Closure Attempt From The Typed GU Operator Spine"
date: 2026-06-24
status: exploration/closure_attempt
doc_type: vz_proof_grade_closure_attempt
verdict: "CONDITIONAL_TYPED_SPINE_PRINCIPAL_SYMBOL_CLOSED__PRIMARY_GU_OPERATOR_GATE_OPEN"
owned_path: "explorations/vz-evasion/vz-proof-grade-closure-attempt-2026-06-24.md"
depends_on:
  - "explorations/cycle-gates-and-audits/goal-draft-primary-gu-action-operator-spec-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/gu-typed-operator-action-spine-2026-06-24.md"
  - "explorations/vz-evasion/vz-principal-symbol-convention-reconciliation-2026-06-24.md"
  - "explorations/vz-evasion/vz-proof-grade-verification-gate-2026-06-24.md"
  - "explorations/vz-evasion/vz-e-block-independent-rederivation-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md"
companion_audit:
  - "tests/vz_typed_symbol_gate.py"
---

# VZ Proof-Grade Closure Attempt From The Typed GU Operator Spine

## 1. Verdict: conditional

The typed-spine principal-symbol calculation closes cleanly:

```text
If the actual 14D GU 0/1 operator has principal block

  sigma_D(xi)(u, psi) = (i_xi psi, xi tensor u + F_xi psi)

with F_xi = sigma_1(Phi_2 o d_A)(xi) and nonzero coefficient lambda_d,
then the full 14D spin-3/2 Schur principal symbol has no non-null kernel.
```

For the typed spine as written, `lambda_d = 1`, and the effective spin-3/2 symbol is:

```text
(S_R(xi) psi)_A
  =
  -G psi_A + 16 xi_A G chi / q - gamma_A chi,

G = gamma(xi),
q = g_Y(xi, xi),
chi = xi^B psi_B,
Gamma psi = gamma^B psi_B = 0.
```

For every `q != 0`, `ker S_R(xi) = 0`.

This is not a global VZ proof-grade promotion for GU. The closure is conditional on the
typed spine being the actual primary GU operator/action output. The repo still records
that as a canonical proposal, not as a source-closed fact. If the actual operator has
`lambda_d = 0` and only the zero-order curvature insertion `Phi_F`, the spin-3/2 Schur
principal symbol below collapses to zero and the VZ closure attempt is refuted for that
operator.

So the honest status is:

```text
typed-spine 14D principal-symbol Schur gate: closed, conditional on lambda_d != 0
typed-spine lambda_d = 1 arithmetic: closed
primary GU VZ claim: conditional, not proof-grade closed
full 4D/subprincipal/dynamical VZ claim: still gated
```

## 2. What I derived directly from the typed operator

Let

```text
V = T_y Y,       dim V = n = 14,
g_Y has signature (9,5),
S = S^+ plus S^-,
G = gamma(xi),
q = g_Y(xi, xi).
```

The typed spine proposes the 0/1 operator

```text
D_roll(u, psi)
  =
  (d_A^* psi, d_A u + Phi_2(d_A psi)) + Z_A(u, psi).
```

I keep a coefficient in the principal term while deriving, because this is the exact
operator-provenance gate:

```text
D_lambda(u, psi)
  =
  (d_A^* psi, d_A u + lambda_d Phi_2(d_A psi)) + Z_A(u, psi).
```

At principal-symbol order, all `Z_A` terms vanish and:

```text
sigma_lambda(xi)(u, psi)
  =
  (i_xi psi, xi tensor u + lambda_d F_xi psi),

(F_xi psi)_A
  =
  xi_A gamma^B psi_B - G psi_A.
```

This is the actual spin-3/2 starting point supplied by the typed spine. The curvature
insertion

```text
Phi_F(A) = Phi_2(F_A tensor -)
```

is zero-order in `psi` and does not contribute to this symbol.

Define the full 14D gamma trace and trace injection:

```text
Gamma(psi) = gamma^A psi_A,
j(s)_A = (1/n) gamma_A s,
Gamma j = Id.
```

Then

```text
R = ker Gamma
Q = S^+ direct-sum Im(j)
V^* tensor S^- = R direct-sum Im(j).
```

For `psi in R`, write

```text
chi = i_xi psi = xi^A psi_A.
```

The raw block maps in trace coordinate `(phi, s)` for `Q` are:

```text
A_lambda psi
  =
  lambda_d(-G psi_A + (2/n) gamma_A chi),

C_lambda psi
  =
  (chi, -2 lambda_d chi),

B_lambda(phi, s)_A
  =
  xi_A phi - (1/n) gamma_A G phi
  + lambda_d ((n - 2)/n) (xi_A s - (1/n) gamma_A G s).
```

The spin-3/2 principal symbol is therefore not the diagonal `A_lambda` block. It is the
Schur symbol

```text
S_R^lambda(xi)
  =
  A_lambda - B_lambda E_lambda(xi)^(-1) C_lambda,
```

provided the Q-sector block `E_lambda(xi)` is invertible.

Using the Q-block inverse below gives the closed formula:

```text
(S_R^lambda(xi) psi)_A
  =
  lambda_d(
    -G psi_A + (n + 2) xi_A G chi / q - gamma_A chi
  ).
```

With `n = 14` and the typed spine's `lambda_d = 1`:

```text
(S_R(xi) psi)_A
  =
  -G psi_A + 16 xi_A G chi / q - gamma_A chi.
```

This formula is the derived principal symbol of the effective 14D spin-3/2 sector for the
typed operator. It is not imported from the older determinant argument.

## 3. The independent Q-sector E-block reconstruction

The Q-sector is

```text
Q = S^+ direct-sum Im(j).
```

There are two useful coordinate conventions.

In trace coordinates, an element is `(phi, s)` meaning `(phi, j(s))`. Directly from
`sigma_lambda(xi)`:

```text
E_coord(lambda)(xi)
  =
  [[0,        (1/n) G],
   [G, lambda_d (2(n - 1)/n) G]].
```

For `n = 14` and `lambda_d = 1`:

```text
E_coord(xi)
  =
  [[0,        (1/14) G],
   [G,        (13/7) G]].
```

In embedded one-form notation, where the second row is written as `j(s)` and the common
`(1/n) gamma_A` embedding is not removed:

```text
E_embed(lambda)(xi)
  =
  [[0,        (1/n) G],
   [(1/n) G, lambda_d (2(n - 1)/n^2) G]].
```

For `n = 14` and `lambda_d = 1`:

```text
E_embed(xi)
  =
  [[0,        (1/14) G],
   [(1/14) G, (13/98) G]].
```

The coefficients come from the following direct computations.

Scalar input:

```text
sigma(xi)(phi, 0) = (0, xi_A phi),
Gamma(xi tensor phi) = G phi,
P_T(xi tensor phi) = j(G phi).
```

This gives `1/n` in embedded notation and `1` in trace-coordinate row two.

Trace input:

```text
i_xi j(s) = (1/n) G s,
```

and

```text
(F_xi j(s))_A
  =
  xi_A s - (1/n) G gamma_A s.
```

Taking the gamma trace:

```text
Gamma(F_xi j(s))
  =
  G s - (1/n) gamma^A G gamma_A s.
```

The Clifford identity in dimension `n` is

```text
gamma^A G gamma_A = (2 - n) G.
```

Therefore

```text
Gamma(F_xi j(s))
  =
  (1 + (n - 2)/n) G s
  =
  (2(n - 1)/n) G s.
```

For `n = 14`, this is `(13/7) Gs` in trace coordinates and `(13/98) gamma_A Gs` after
embedding by `j`.

## 4. The non-null invertibility argument

### Q-sector E-block

For `q = g_Y(xi, xi) != 0`, `G` is invertible because

```text
G^2 = q Id.
```

The direct kernel proof for `E_embed` is:

```text
E_embed(phi, j(s)) = 0.
```

The scalar row gives

```text
(1/n) G s = 0.
```

Apply `G`:

```text
q s = G^2 s = 0,
```

so `s = 0`. With `s = 0`, the trace row gives `j(G phi) = 0`; since `j` is injective,
`G phi = 0`, and applying `G` gives `q phi = 0`, so `phi = 0`.

Thus:

```text
ker E_lambda(xi) = 0 for every q != 0.
```

This proof does not use `det(M) = det(E) det(S_R)`.

The embedded inverse is also explicit:

```text
E_embed(lambda)(xi)^(-1)
  =
  [[-2 lambda_d (n - 1) G/q,  n G/q],
   [ n G/q,                         0]].
```

For the typed spine:

```text
E_embed(xi)^(-1)
  =
  [[-26 G/q, 14 G/q],
   [ 14 G/q,       0]].
```

### Spin-3/2 Schur symbol

The E-block being invertible is necessary but not sufficient for VZ closure. The actual
spin-3/2 Schur symbol must also have no non-null kernel.

In trace coordinates,

```text
E_coord(lambda)^(-1)
  =
  [[-2 lambda_d (n - 1) G/q,  G/q],
   [ n G/q,                     0]].
```

For `psi in R`,

```text
E_coord(lambda)^(-1) C_lambda psi
  =
  (-2 lambda_d n G chi/q, n G chi/q).
```

Substituting this into `A - B E^{-1} C` gives:

```text
(S_R^lambda(xi) psi)_A
  =
  lambda_d(
    -G psi_A + (n + 2) xi_A G chi/q - gamma_A chi
  ).
```

Now assume `q != 0`, `lambda_d != 0`, `Gamma psi = 0`, and `S_R^lambda(xi) psi = 0`.
After dividing by `lambda_d`:

```text
G psi_A = (n + 2) xi_A G chi/q - gamma_A chi.
```

Apply `G/q` to the left and use

```text
G gamma_A = 2 xi_A - gamma_A G.
```

This gives

```text
psi_A = n xi_A chi/q + gamma_A G chi/q.
```

Take the gamma trace:

```text
0 = Gamma psi
  = n G chi/q + n G chi/q
  = 2n G chi/q.
```

Since `q != 0`, `G` is invertible, so `chi = 0`. Then the displayed formula for `psi_A`
gives `psi_A = 0`.

Therefore:

```text
ker S_R^lambda(xi) = 0 for every q != 0, provided lambda_d != 0.
```

This is the determinant-free non-null kernel proof for the typed-spine spin-3/2
principal symbol.

The exact failure at the operator gate is also sharp:

```text
if lambda_d = 0, then S_R^lambda(xi) = 0 on R.
```

So an operator with only the zero-order curvature insertion `Phi_F` does not merely lose
the `13/98` coefficient. It loses the effective spin-3/2 first-order Schur symbol supplied
by `Phi_d`. That branch is refuted as a VZ closure route.

## 5. What this means for the Velo-Zwanziger claim

The typed-spine VZ principal-symbol claim is algebraically stronger than the current
ledger wording, but only inside the typed-spine assumption.

What is now derived:

```text
1. The Q-sector E-block is reconstructed from the typed operator, not from a determinant.
2. The coefficients 1/14 and 13/98 follow from j(s)_A = (1/14) gamma_A s.
3. E(xi) is invertible for every non-null 14D covector.
4. The full 14D spin-3/2 Schur symbol is explicit.
5. The Schur symbol has no non-null kernel when lambda_d != 0.
6. For the typed spine's lambda_d = 1, the null locus is exactly the expected q = 0 cone.
```

What is not established:

```text
1. The primary GU action/operator has not been source-closed as D_roll.
2. The coefficient lambda_d = 1 is still a typed-spine proposal, not a canonically derived
   Euler-Lagrange fact.
3. The chirality packaging must be fixed in the primary spec, although it does not change
   the scalar coefficients above.
4. The 4D section-pulled effective RS dynamics must still be checked with II_s^H,
   curvature, masses, gauge constraints, and IG/theta terms in Z_A.
5. A standalone low-energy RS Lagrangian, if later derived, would require its own VZ
   constraint-propagation analysis.
```

Thus the VZ claim should not be promoted unqualified. The precise update is:

```text
FC-VZ-1 algebra relative to typed D_roll: conditionally closed.
VZ-OPERATOR node: still specified_open until primary D_GU is fixed.
VZ-14D node: can upgrade only after VZ-OPERATOR closes with lambda_d != 0
             and the review policy accepts this derivation/audit.
VZ-4D and full dynamical VZ: remain conditional.
```

## 6. Next proof obligation if not closed

The next proof obligation is not another determinant or random matrix check. It is the
operator/action provenance gate:

```text
Write or cite the primary GU action/operator definition and prove that its 0/1 sector has

  d_A u + lambda_d Phi_2(d_A psi)

with lambda_d != 0, preferably lambda_d = 1 under the same normalization used here.
```

If that succeeds, the follow-on obligations are:

```text
1. Lock one Q-sector convention: trace coordinates or embedded coordinates.
2. Record the above Schur symbol as the typed 14D spin-3/2 principal symbol.
3. Re-run the 4D section-pullback/subprincipal gate using II_s^H and the actual Z_A ledger.
4. Check whether the action produces a standalone RS equation; if yes, analyze its
   constraint propagation separately.
5. Keep mass terms, Phi_F, theta/IG terms, and curvature insertions in lower order unless
   a reduction turns them into effective first-order constraints.
```

If the primary operator has `lambda_d = 0`, the VZ route using this typed Schur symbol
fails. The Q-sector E-block may remain invertible off the null cone, but the spin-3/2
principal Schur symbol is zero and cannot establish VZ evasion.

## Companion audit

I added:

```text
tests/vz_typed_symbol_gate.py
```

Run it with:

```text
python tests/vz_typed_symbol_gate.py
```

It checks the rational Q-block coefficients, the two-sided inverse in both coordinate
conventions, the typed-spine Schur coefficients, and the `lambda_d = 0` collapse case.

## Sources read

- `explorations/cycle-gates-and-audits/goal-draft-primary-gu-action-operator-spec-2026-06-24.md`
- `explorations/cycle-gates-and-audits/gu-typed-operator-action-spine-2026-06-24.md`
- `explorations/vz-evasion/vz-principal-symbol-convention-reconciliation-2026-06-24.md`
- `explorations/vz-evasion/vz-proof-grade-verification-gate-2026-06-24.md`
- `explorations/vz-evasion/vz-e-block-independent-rederivation-2026-06-24.md`
- `explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md`

Additional context checked for the Schur-block typing:

- `explorations/vz-evasion/vz-schur-complement-2026-06-23.md`
- `explorations/vz-evasion/vz1-schur-complement-symbol-2026-06-23.md`
- `explorations/vz-evasion/vz-e-block-direct-clifford-2026-06-23.md`
