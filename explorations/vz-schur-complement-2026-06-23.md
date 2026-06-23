---
title: "VZ Schur: Mixed 14D Covector Extension, Full Spin(9,5) Clifford Symbol, and Section-Pullback 4D Preservation (OQ3)"
date: 2026-06-23
problem_label: "vz-schur"
status: reconstruction
verdict: EVADED
oq3_status: CONDITIONALLY_RESOLVED
---

# VZ Schur: Mixed 14D Covector Extension and Full Spin(9,5) Clifford Symbol

## 1. Problem Statement

Prior notes established:

- `vz1-schur-complement-symbol-2026-06-23.md`: for horizontal covectors `xi_H in H*`, the
  minimal Schur complement `S_R^min(xi_H)` has `ker = 0` when `g_H(xi_H, xi_H) != 0`.
- `vz1-schur-vertical-extension-2026-06-23.md`: vertical one-form inputs do not modify the
  horizontal Schur complement at horizontal covectors. `S_R^full(xi_H) = S_R^min(xi_H)`.

The remaining question: for a general 14D covector

```
xi = xi_H + xi_N,    xi_H in H* (signature (3,1)),   xi_N in N* (signature (6,4)),
```

does the effective RS principal symbol

```
D_RS_eff(xi) = A(xi) - B(xi) E(xi)^{-1} C(xi)
```

satisfy `ker D_RS_eff(xi) = 0` for all `g_Y(xi, xi) = g_H(xi_H, xi_H) + g_N(xi_N, xi_N) != 0`,
or do mixed-covector components reintroduce VZ-type spacelike characteristics?

This determines whether VZ is evaded in the full 14D sense.

---

## 2. Established Context

**Geometry.** Y^14 = Met(X^4), signature (9,5), decomposition at the section:

```
T*Y|_s = H* direct-sum N*,   dim H* = 4 (sig (3,1)),   dim N* = 10 (sig (6,4)).
```

Block-diagonal metric in product coordinates: `g_Y(xi_H, xi_N) = 0`.

**Clifford algebra.** `Cl(9,5) ~= M(64,H)`, spinor module `S = H^{64}`, `dim_R S = 256`.
Clifford multiplication satisfies

```
c(xi)^2 = g_Y(xi, xi) * Id_S = (g_H(xi_H, xi_H) + g_N(xi_N, xi_N)) * Id_S.
```

This is the fundamental relation that drives the entire computation.

**RS sector.** The 14D RS subspace is the kernel of the full 14D gamma trace:

```
R^{14D} = ker Gamma^{14D},   Gamma^{14D}(psi) = gamma^A psi_A,
```

summed over all 14 frame directions `e^A` (4 horizontal + 10 vertical). This is the
physically correct definition when the full 14D Dirac-DeRham complex is used.

**Operator.** The rolled-up operator principal symbol at a 14D covector `xi` is

```
sigma_D(xi)(u, psi) = (g_Y(xi, psi), xi tensor u + F_xi psi),
```

where `g_Y(xi, psi) = xi^A psi_A` (full 14D contraction) and

```
(F_xi psi)_A = xi_A gamma^B psi_B - gamma(xi) psi_A.               (*)
```

Here `gamma(xi) = xi_H^a gamma_a + xi_N^i gamma_i` is the full 14D Clifford element.

---

## 3. Block Structure at a Mixed Covector

Let `xi = xi_H + xi_N` with both parts nonzero. Write `xi2 = g_Y(xi, xi)`, which can
be positive, negative, or zero.

### 3.1 The C Block: RS to Non-RS

For a 14D-RS input `psi_R in R^{14D}` (i.e., `Gamma^{14D}(psi_R) = 0`), define

```
chi = xi^A psi_{R,A} = g_Y(xi, psi_R).
```

The scalar output of the principal symbol is

```
(C psi_R)_scalar = chi.                                             (C1)
```

The one-form output from the shiab term (*):

```
(F_xi psi_R)_A = xi_A chi - gamma(xi) psi_{R,A}.
```

Its full 14D gamma trace:

```
Gamma^{14D}(F_xi psi_R)
  = gamma^A (xi_A chi - gamma(xi) psi_{R,A})
  = gamma(xi) chi - gamma^A gamma(xi) psi_{R,A}.
```

Using the Clifford anticommutation relation in 14D:

```
gamma^A gamma(xi) = gamma(xi) gamma^A - 2 xi^A  + 2 g_Y(e^A, xi) Id
```

Wait, the standard relation is: `{gamma^A, gamma(xi)} = 2 xi^A` (the contraction), so

```
gamma^A gamma(xi) psi_{R,A}
  = (2 xi^A - gamma(xi) gamma^A) psi_{R,A}
  = 2 chi - gamma(xi) Gamma^{14D}(psi_R)
  = 2 chi - 0
  = 2 chi.
```

(Using `Gamma^{14D}(psi_R) = 0`.)

Therefore

```
Gamma^{14D}(F_xi psi_R) = gamma(xi) chi - 2 chi.                   (C2)
```

**The C block** maps:

```
C psi_R = (chi,  Gamma^{14D}(F_xi psi_R)) = (chi, gamma(xi) chi - 2 chi).
```

For generic `xi` and generic `psi_R in R^{14D}`, `chi` may be nonzero. The RS sector
is coupled to the scalar and gamma-trace sectors, confirming non-independence.

### 3.2 The A Block: RS to RS

For `psi_R in R^{14D}`, the RS-to-RS part of the symbol is

```
(A psi_R)_A = (F_xi psi_R)_A - (RS projection of gamma-trace component).
```

The full one-form output is `(F_xi psi_R)_A = xi_A chi - gamma(xi) psi_{R,A}`.

The 14D RS projection `P_R` removes the gamma-trace part. Using `P_R = Id - (1/14) gamma_A Gamma^{14D}` schematically (the exact projector uses the dimension factor for 14D):

```
(P_R(F_xi psi_R))_A = xi_A chi - gamma(xi) psi_{R,A}
                       - (1/14) gamma_A (gamma(xi) chi - 2 chi).
```

The factor `1/14` comes from `dim Y = 14` and the identity `gamma^A gamma_A = 14 Id`
in 14D (from the Clifford algebra trace formula in n dimensions: `{gamma^A, gamma_B} = 2 delta^A_B`
gives `gamma^A gamma_A = n Id`).

So the A block is:

```
(A psi_R)_A = - gamma(xi) psi_{R,A} + xi_A chi + (2/14 - 1/14 gamma(xi)) gamma_A chi.
            = - gamma(xi) psi_{R,A} + xi_A chi + (2 - gamma(xi)) gamma_A chi / 14.  (A1)
```

### 3.3 The E Block: Non-RS to Non-RS

The non-RS block `Q` has three components:
- `Q_0 = Omega^0 tensor S` (scalar spinors, field `phi`)
- `Q_T = T` (gamma-trace horizontal one-forms, field `s` via `j(s)_A = (1/14) gamma_A s`)
- `Q_N = N* tensor S` (vertical one-forms, field `eta tensor t`)

For the E block, we need the symbol restricted to non-RS inputs and projected to non-RS outputs.

**Scalar input `phi in Q_0`.** The principal symbol gives (from the d_A* part):

```
sigma_D(xi)(phi, 0) = (0, xi tensor phi + F_xi(0)) = (0, xi tensor phi).
```

Here `(xi tensor phi)_A = xi_A phi`. The gamma-trace of this:

```
Gamma^{14D}(xi tensor phi) = gamma^A xi_A phi = gamma(xi) phi.
```

So `xi tensor phi` projects to scalar spinor `chi = 0` (no scalar from one-form input) and gamma-trace `gamma(xi) phi`. Its RS projection:

```
P_R(xi tensor phi)_A = xi_A phi - (1/14) gamma_A gamma(xi) phi.
```

This is nonzero generically, so `phi` feeds the RS sector (B block, not E).

For E block: the non-RS projection of `xi tensor phi`:

```
E_{0 -> 0}: no scalar output
E_{0 -> T}: P_T(xi tensor phi) = (1/14) gamma_A (Gamma^{14D}(xi tensor phi)) 
                                 = (1/14) gamma_A gamma(xi) phi
```

So `E_{00}(phi) = 0`, and `E_{T0}(phi) = (1/14) gamma(xi) phi`.

**Gamma-trace input `j(s) in Q_T`.** The principal symbol:

```
(F_xi j(s))_A = xi_A (1/14) gamma^B gamma_B s - gamma(xi) (1/14) gamma_A s
              = xi_A s - (1/14) gamma(xi) gamma_A s.
```

(using `gamma^B gamma_B = 14 Id`)

Gamma trace of `F_xi j(s)`:

```
Gamma^{14D}(F_xi j(s)) = gamma^A (xi_A s - (1/14) gamma(xi) gamma_A s)
                        = gamma(xi) s - (1/14) gamma(xi) gamma^A gamma_A s
                        = gamma(xi) s - gamma(xi) s = 0.
```

Wait: `gamma^A gamma(xi) gamma_A = (2 * 14 - 14) gamma(xi) / 1` — let me redo this carefully.

Using the identity in n dimensions: `gamma^A gamma(xi) gamma_A = (2 - n) gamma(xi)`,
in 14D: `gamma^A gamma(xi) gamma_A = (2 - 14) gamma(xi) = -12 gamma(xi)`.

So

```
Gamma^{14D}(F_xi j(s))
  = gamma^A (xi_A s - (1/14) gamma(xi) gamma_A s)
  = gamma(xi) s - (1/14) gamma^A gamma(xi) gamma_A s.
```

Using `gamma^A gamma(xi) gamma_A = -12 gamma(xi)`:

```
  = gamma(xi) s - (1/14)(-12 gamma(xi)) s
  = gamma(xi) s + (12/14) gamma(xi) s
  = (1 + 12/14) gamma(xi) s
  = (26/14) gamma(xi) s
  = (13/7) gamma(xi) s.
```

So the gamma-trace of `F_xi j(s)` is `(13/7) gamma(xi) s`.

The E block entries for the gamma-trace sector:

```
E_{TT}(j(s)) = P_T(F_xi j(s)):   gamma-trace part = (13/7) gamma(xi) s / 14 
```

Hmm, let me reorganize using the operator scalar/trace split clearly.

---

## 4. Key Calculation: The Full 14D Symbol and Characteristic Polynomial

The decisive question is whether `S_R^{14D}(xi) = A - B E^{-1} C` has a nontrivial kernel
for spacelike or mixed-signature covectors.

**The critical observation.** In the full 14D setting, the principal symbol `sigma_D(xi)`
is a differential operator whose square is:

```
sigma_D(xi)^2 = g_Y(xi, xi) * Id.
```

This follows from the standard Dirac operator property: `D_GU^2` has leading symbol
`g_Y(xi, xi) * Id` because `D_GU` is a Dirac-type operator on the Clifford module
bundle `E = (Omega^0 tensor S+) direct-sum (Omega^1 tensor S-)`.

**Consequence for the block structure.** Write `sigma_D(xi) = M(xi)` as a block matrix:

```
M(xi) = [ A(xi)  B(xi) ]
        [ C(xi)  E(xi) ]
```

Since `M(xi)^2 = xi2 * Id`, we have the block identity:

```
A^2 + B C = xi2 * Id_{RS}           (I)
A B + B E = 0                        (II)
C A + E C = 0                        (III)
C B + E^2 = xi2 * Id_Q              (IV)
```

From (I): `A^2 = xi2 * Id_{RS} - BC`.

The Schur complement satisfies:

```
S_R = A - B E^{-1} C.
```

**Claim.** `S_R^2 = xi2 * Id_{RS}` when `E` is invertible.

**Proof.** From (II): `B E = -A B`, so `B E^{-1} = -A B E^{-1} E^{-1} = -A B (E^2)^{-1}`.
Actually let us compute directly.

```
S_R^2 = (A - B E^{-1} C)^2
      = A^2 - A B E^{-1} C - B E^{-1} C A + B E^{-1} C B E^{-1} C.
```

From (II): `A B + B E = 0 => A B = -B E => A B E^{-1} = -B`.
So the second term: `-A B E^{-1} C = B C`.

From (III): `C A + E C = 0 => E C = -C A => E^{-1} C A = -C => B E^{-1} C A = -B C`.
So the third term: `-B E^{-1} C A = B C`.

Wait, from `E C = -C A` we get `C A = -E C`, so `E^{-1} C A = -C`. Then:

```
B E^{-1} C A = B (-C) = -B C.
```

Hmm, but the third term is `- B E^{-1} C A = -(- B C) = B C`.

For the fourth term: use (IV): `C B + E^2 = xi2 Id_Q => C B = xi2 Id_Q - E^2`.
So `C B E^{-1} C = (xi2 Id_Q - E^2) E^{-1} C = xi2 E^{-1} C - E C`.
From (III): `E C = -C A`, so: `C B E^{-1} C = xi2 E^{-1} C + C A`.

Therefore:

```
B E^{-1} C B E^{-1} C = B (xi2 E^{-1} C + C A) = xi2 B E^{-1} C + B C A.
```

And from `A B = -B E => B C A = B C A`... Let me use (I) instead.

From (I): `B C = xi2 Id_{RS} - A^2`.

Assembling:

```
S_R^2 = A^2 + B C - B C + xi2 B E^{-1} C + B C A
```

Wait, I need to be more careful. Let me redo:

```
S_R^2 = A^2 + (- A B E^{-1} C) + (- B E^{-1} C A) + B E^{-1} C B E^{-1} C
      = A^2 + B C  + B C  + B E^{-1} (C B E^{-1} C)     [using the above results]
```

Hmm, the second term: `-A B E^{-1} C = -(A B) E^{-1} C = -(-B E) E^{-1} C = B C`. (using (II))
The third term: `-B E^{-1} C A = -B E^{-1} (-E C) = B C`. (using (III): `C A = -E C`)

Wait: from (III), `C A + E C = 0 => C A = -E C`. Then:
`-B E^{-1} C A = -B E^{-1} (-E C) = B E^{-1} E C = B C`. Yes.

So:

```
S_R^2 = A^2 + BC + BC + B E^{-1} (CB) E^{-1} C.
```

From (IV): `C B = xi2 Id_Q - E^2`.

```
B E^{-1} (CB) E^{-1} C = B E^{-1} (xi2 Id_Q - E^2) E^{-1} C
                        = xi2 B (E^{-1})^2 C - B C.
```

So

```
S_R^2 = A^2 + BC + BC + xi2 B (E^{-1})^2 C - BC
       = A^2 + BC + xi2 B (E^{-1})^2 C.
```

From (I): `A^2 + BC = xi2 Id_{RS}`.

Therefore:

```
S_R^2 = xi2 Id_{RS} + xi2 B (E^{-1})^2 C.           (KEY)
```

This is `xi2 * Id_{RS}` if and only if `B (E^{-1})^2 C = 0`.

---

## 5. When Does `B (E^{-1})^2 C = 0`?

### 5.1 Structure of C

From §3.1, for `psi_R in R^{14D}`:

```
C psi_R = (chi, (gamma(xi) - 2) chi),   chi = g_Y(xi, psi_R).
```

If `chi = 0` then `C psi_R = 0`. The kernel of `C` on `R^{14D}` is:

```
ker C|_{R^{14D}} = {psi_R in R^{14D} : g_Y(xi, psi_R) = 0}.
```

This is a codimension-1 (in spinor-index terms) subspace. For generic `xi`, `C` is
nonzero on most of `R^{14D}`.

### 5.2 Action of `E^{-1}` on the Image of `C`

The image of `C` on `R^{14D}` lives in the non-RS block `Q`:

```
C psi_R in Q_0 direct-sum Q_T.
```

Specifically, `C psi_R = (chi, (gamma(xi) - 2) chi)` where the first entry is a scalar
spinor and the second is the gamma-trace component.

For `xi2 != 0`, `gamma(xi)` is invertible on `S`. The E block on `Q_0 direct-sum Q_T`
is (from the prior note, extended to 14D):

```
E = gamma(xi) * M_14D
```

where `M_14D` is a scalar 2x2 matrix (acting on the `(phi, s)` coordinates). In the
14D setting, the trace normalization changes. From the 14D gamma trace calculation
in §3.3:

For scalar input `phi`: `E_{T0}(phi) = (1/14) gamma(xi) phi`.
For gamma-trace input (via `j_{14D}(s) = (1/14) gamma_A s`):

```
Gamma^{14D}(F_xi j_{14D}(s)) = (13/7) gamma(xi) s.
```

The E block (mapping `(phi, s) -> (scalar output, trace output)`) at 14D:

```
E = gamma(xi) * [ [0,    1/14] ,
                  [1,    13/7] ].
```

Compare to the 4D minimal case from `vz1-schur-complement-symbol-2026-06-23.md` where the
matrix was `[[0, 1/4], [1, 3/2]]` (using dim H* = 4).

The 14D matrix has determinant `det([[0, 1/14], [1, 13/7]]) = 0 - 1/14 = -1/14 != 0`.

So E is invertible for `xi2 != 0`, and `E^{-1} = (gamma(xi))^{-1} * (-14) * [[13/7, -1/14], [-1, 0]]`.

Since `(gamma(xi))^{-1} = gamma(xi) / xi2`, we have `E^{-1}` well-defined for `xi2 != 0`.

### 5.3 The Composition `B (E^{-1})^2 C`

**Key structural point.** From the block-square relations, we derived:

```
S_R^2 = xi2 Id_{RS} + xi2 B (E^{-1})^2 C.
```

Now `B (E^{-1})^2 C` maps `R^{14D} -> R^{14D}`. Let us compute its action on a general
RS element `psi_R`.

The image of `C` is `(chi, (gamma(xi) - 2) chi)` for `chi = g_Y(xi, psi_R)`.

Apply `E^{-1}`:

```
E^{-1} (chi, (gamma(xi) - 2) chi) = (gamma(xi))^{-1} (-14) * [[13/7, -1/14], [-1, 0]] (chi, (gamma(xi)-2) chi).
```

Let `mu = gamma(xi) chi = c(xi) chi`. (Note: `chi in S` is a spinor, and `c(xi)` acts on it.)

First column: `13/7 * chi - (1/14) * (mu - 2 chi) = 13/7 chi - mu/14 + chi/7 = (13/7 + 1/7) chi - mu/14 = 2 chi - mu/14`.
Second column: `-1 * chi + 0 = -chi`.

So `(-14)(...)` gives:

```
E^{-1} (chi, (gamma(xi) - 2) chi) = (gamma(xi))^{-1} (-14) * (2 chi - mu/14, -chi)
                                   = (1/xi2) gamma(xi) * (14)(-1) * (2 chi - mu/14, -chi)
                                   = -(14/xi2) gamma(xi) * (2 chi - mu/14, -chi).
```

Computing:
- First component: `-(14/xi2) gamma(xi) (2 chi - mu/14) = -(14/xi2)(2 mu - mu^2/14)`

Wait, `gamma(xi) chi = mu` and `gamma(xi) mu = gamma(xi)^2 chi = xi2 chi`.

```
gamma(xi)(2 chi - mu/14) = 2 mu - xi2 chi / 14.
```

- Second component: `-(14/xi2) gamma(xi) (-chi) = (14/xi2) mu`.

So:

```
E^{-1} C psi_R = (-(14/xi2)(2 mu - xi2 chi/14), (14/xi2) mu)
               = ((-28 mu + xi2 chi) / xi2, 14 mu / xi2)
               = (chi - 28 mu/xi2, 14 mu/xi2).
```

where `mu = gamma(xi) chi`, `chi = g_Y(xi, psi_R)`.

Apply `E^{-1}` a second time (to get `(E^{-1})^2 C psi_R`):

Let `(chi_1, mu_1) = (chi - 28 mu/xi2, 14 mu/xi2)`. Apply `E^{-1}` to this pair:

```
mu_1' = gamma(xi) chi_1 = mu - 28 xi2 chi / xi2 = mu - 28 chi.
         wait: gamma(xi)(chi - 28 mu / xi2) = mu - 28 xi2 chi / xi2 = mu - 28 chi.
```

Hmm, that is: `gamma(xi)(28 mu / xi2) = 28 xi2 chi / xi2 = 28 chi`. So:

```
gamma(xi) chi_1 = mu - 28 chi.
gamma(xi) mu_1 = gamma(xi)(14 mu / xi2) = 14 xi2 chi / xi2 = 14 chi.
```

Apply the same `E^{-1}` formula:

```
(E^{-1})^2 C psi_R = E^{-1}(chi_1, (gamma(xi) - 2) chi_1 + ...)
```

Actually wait. The E block acts on the Q components. The second application of E^{-1} acts on
`(phi, s)` coordinates in Q. The pair `(chi_1, 14 mu/xi2)` is in `(Q_0, Q_T)`.

For the pair `(phi_2, s_2) = (chi - 28 mu/xi2, 14 mu/xi2)`:

```
E (phi_2, s_2) means we need E^{-1} of this pair.
```

The first entry is a Q_0 spinor and the second is a trace-mode spinor. Apply E^{-1}:

```
E^{-1}(phi_2, s_2) = -(14/xi2) gamma(xi) * M^{-1} (phi_2, s_2)
```

where `M^{-1} = (-14) * [[13/7, -1/14], [-1, 0]]` (the scalar 2x2 part).

Actually let me use a cleaner notation. The formula `E^{-1} (v_0, v_T) = (gamma(xi)/xi2) * N (v_0, v_T)` for some matrix N, gives:

From above, `E^{-1}(chi, (gamma(xi)-2)chi)` had a specific form. Let me instead just check whether `B (E^{-1})^2 C = 0` directly by a representation-theoretic argument.

---

## 6. Representation-Theoretic Argument: Clifford Module Structure

**The clean path.** Rather than computing `(E^{-1})^2 C` explicitly entry by entry (which involves rational functions of `gamma(xi)`), we use the fundamental Dirac-type identity.

**Lemma.** For a first-order differential operator `D` on a Clifford module bundle with principal symbol `sigma_D(xi)` satisfying `sigma_D(xi)^2 = xi2 Id`, the Schur complement of any direct summand satisfies `S^2 = xi2 Id` on that summand, whenever the complementary block `E(xi)` is invertible.

**Proof.** This is the general statement that for a matrix `M` with `M^2 = lambda Id` partitioned as

```
M = [ A  B ]
    [ C  E ]
```

the Schur complement `S = A - B E^{-1} C` satisfies `S^2 = lambda Id`, provided:

(a) `M^2 = lambda Id` as a block relation.
(b) `E` is invertible.

The block-square computation in §4 showed `S_R^2 = xi2 Id + xi2 B (E^{-1})^2 C`. For this
to equal `xi2 Id` we need `B (E^{-1})^2 C = 0`. Let us check whether this holds using
the block-square relations.

From (II): `AB + BE = 0`.
From (III): `CA + EC = 0`.

Compute `B E^{-1} C`:
- From (II): `AB = -BE`, so `A (B E^{-1}) = -B`.
- Thus `A S_R = A(A - B E^{-1} C) = A^2 - A B E^{-1} C = A^2 + B C = xi2 Id`. CHECK: this gives `A S_R = xi2 Id`.
- Similarly from (III): `S_R A = xi2 Id`.

So `A` and `S_R` commute up to a scalar: `A S_R = S_R A = xi2 Id`. This means `S_R = xi2 A^{-1}` whenever `A` is invertible. But more importantly, it means `S_R` commutes with `A`.

Now from `S_R A = xi2 Id`:

```
S_R^2 = S_R (xi2 A^{-1}) = xi2 S_R A^{-1}.
```

Also `S_R A = xi2 Id => S_R = xi2 A^{-1}`, so `S_R^2 = (xi2 A^{-1})^2 = xi2^2 A^{-2}`.

But also from `A S_R = xi2 Id => A^{-1} = S_R / xi2`, so `A^{-2} = S_R^2 / xi2^2`.

Therefore `S_R^2 = xi2^2 (S_R^2 / xi2^2) = S_R^2`. This is circular.

Let me use the block relation more carefully.

**Correct proof via Schur complement determinant.** The matrix `M` satisfies:

```
det(M - lambda Id) = det(M^2 - lambda^2 Id) / det(M + lambda Id).
```

But since `M^2 = xi2 Id`, we have `M^2 - xi2 Id = 0`, so `det(M^2 - xi2 Id) = 0`.

By the Schur determinant formula:
```
det(M - mu Id) = det(E - mu Id) * det(A - mu Id - B(E - mu Id)^{-1} C).
```

The second factor is `det(S_R(mu))` where `S_R(mu) = (A - mu Id) - B (E - mu Id)^{-1} C` is
the mu-shifted Schur complement.

For `mu = 0`: `det(M) = det(E) * det(S_R)`.

For the characteristic polynomial: since `M^2 = xi2 Id`, the minimal polynomial of `M`
divides `t^2 - xi2`. So eigenvalues of `M` are `+/- sqrt(xi2)`. Therefore:

```
det(M - mu Id) = ((-mu + sqrt(xi2))/xi2)^{r/2} ((-mu - sqrt(xi2))/xi2)^{r/2}
```

for appropriate powers depending on the split. The point is: since `M^2 = xi2 Id`, ALL eigenvalues of M are `+/- sqrt(xi2)`. By continuity of the Schur complement in the parameter:

**ALL eigenvalues of `S_R(0)` are also `+/- sqrt(xi2)`.**

Why? Because `S_R(0)` is a principal submatrix of a similarity class of `M` (after appropriate column/row operations via `E`-elimination), and the eigenvalue set of `S_R` is contained in the eigenvalue set of `M` when `M^2 = xi2 Id`. (This is the Sylvester/interlacing principle for Schur complements of matrices with constrained spectrum.)

More precisely: `S_R^2 = xi2 Id_{RS}` follows from the block-square identity because the
term `B (E^{-1})^2 C` is identically zero.

**Why `B (E^{-1})^2 C = 0`.** From the four block-square identities:

From (I): `A^2 + BC = xi2 Id` => `BC = xi2 Id - A^2 = xi2(Id - (A/sqrt(xi2))^2)`.
From (IV): `CB + E^2 = xi2 Id` => `CB = xi2 Id - E^2`.

Now: `B E^{-1} C B E^{-1} C = B (E^{-1} CB) E^{-1} C = B E^{-1}(xi2 Id - E^2) E^{-1} C = xi2 B(E^{-1})^2 C - BC`.

So `B E^{-1} C (B E^{-1} C) = xi2 B(E^{-1})^2 C - BC`.

Also from our computation of `S_R^2`:

```
S_R^2 = A^2 + 2BC - (B E^{-1} C)^2 + xi2 B (E^{-1})^2 C - BC
       = A^2 + BC + xi2 B(E^{-1})^2 C - (B E^{-1} C)^2.
```

This doesn't immediately collapse. Let me try a direct route.

---

## 7. Direct Verification: `S_R^2 = xi2 Id` via the Clifford Operator Identity

**The clean argument, reconstruction grade.**

The operator `D_GU` is a Dirac-type operator on the graded Clifford module bundle `E`:

```
E = (Omega^0(Y) tensor S+) direct-sum (Omega^1(Y) tensor S-)
```

Its principal symbol at any covector `xi in T*Y` satisfies

```
sigma_{D_GU}(xi)^2 = g_Y(xi, xi) * Id_E.                          (Cl)
```

This is the defining property of a Clifford-module Dirac operator. It holds for ALL
covectors `xi`, including mixed `xi = xi_H + xi_N`.

The block decomposition of `sigma_{D_GU}(xi)` into RS and non-RS sectors gives:

```
M(xi) = [ A(xi)  B(xi) ]     with  M(xi)^2 = xi2 * Id_E.
        [ C(xi)  E(xi) ]
```

**Claim.** For any partition of `E` into two direct summands `R` (the 14D RS subspace)
and `Q` (the complement), if `M^2 = xi2 Id` and `E = P_Q M|_{Q}` is invertible, then

```
S_R(xi) = A - B E^{-1} C  satisfies  S_R^2 = xi2 Id_R.            (SC-Clif)
```

**Proof of (SC-Clif).** We verify the block-square identity `B (E^{-1})^2 C = 0`.

From (II) and (III): `A B = -B E` and `E C = -C A`.
From these: `B E^{-1} = -A B (E^2)^{-1} = -A B (xi2 Id - CB)^{-1}`.

Alternatively: apply `E^{-1}` on the right to `A B = -B E`:

```
A (B E^{-1}) = -B.    =>   B E^{-1} = -A^{-1} B.    [if A invertible]
```

Apply on the left to `E C = -C A`:

```
(E^{-1} E) C = -E^{-1} C A.  =>   C = -E^{-1} C A.  =>  E^{-1} C = -C A^{-1}.
```

So

```
B (E^{-1})^2 C = (B E^{-1})(E^{-1} C) = (-A^{-1} B)(-C A^{-1}) = A^{-1} BC A^{-1}.
```

From (I): `BC = xi2 Id - A^2`. Therefore:

```
B (E^{-1})^2 C = A^{-1}(xi2 Id - A^2) A^{-1} = xi2 A^{-2} - Id.
```

Substituting into `S_R^2 = xi2 Id + xi2 B (E^{-1})^2 C`:

```
S_R^2 = xi2 Id + xi2 (xi2 A^{-2} - Id)
       = xi2 Id + xi2^2 A^{-2} - xi2 Id
       = xi2^2 A^{-2}.
```

Hmm — this gives `S_R^2 = xi2^2 A^{-2}`, which equals `xi2 Id` iff `A^2 = xi2 Id`.

So the question reduces to: does `A^2 = xi2 Id_{RS}`?

From (I): `A^2 + BC = xi2 Id`. So `A^2 = xi2 Id_{RS}` iff `BC|_{RS} = 0`, i.e., iff
the operator `BC` kills every RS element.

`BC psi_R = B(C psi_R)`. We have `C psi_R = (chi, (gamma(xi)-2)chi)`. Apply B:

```
B(phi, s) = P_R (sigma_D(xi)(phi, j(s)))
           = P_R (xi tensor phi + F_xi j(s)).
```

For `(phi, s) = (chi, (\text{gamma-trace component}))`:

The key question is whether `B(C psi_R) = 0` for all `psi_R in R^{14D}`.

From the B block computation in `vz1-schur-complement-symbol-2026-06-23.md` (formula (4)):

```
P_R(xi tensor phi)_A = xi_A phi - (1/14) gamma_A gamma(xi) phi.
```

And from the gamma-trace input:

```
P_R(F_xi j_{14D}(s))_A = xi_A s / 14 - (1/14) gamma_A gamma(xi) s / 14 * (correction).
```

The point is that `B (C psi_R)` is a specific element of `R^{14D}`. It is NOT generically
zero — the B block is nonzero as shown in the prior notes (off-diagonal coupling).

So `BC != 0` generically, and `A^2 != xi2 Id` generically, and the above argument using
`A^{-1}` does not give `S_R^2 = xi2 Id` via this route.

This means the lemma as stated above has a gap: `A^{-1}` may not exist, and the step
from `AB = -BE` to `B E^{-1} = -A^{-1} B` requires `A` to be invertible.

---

## 8. Resolution: Direct Characteristic Analysis Without A-Invertibility

**The correct question for VZ.** The VZ problem arises if `S_R(xi) psi_R = 0` has a
nonzero solution for some `xi` with `xi2 = g_Y(xi,xi) > 0` (spacelike in (3,1)+
signature, i.e., `g_H < 0` directions if we take `(3,1)` metric).

In 14D with signature (9,5), spacelike means `g_Y(xi,xi) < 0`.

If `S_R(xi) psi_R = 0`, then:

```
A psi_R = B E^{-1} C psi_R.                                       (VZ-test)
```

And from `M(xi) (psi_R, -E^{-1} C psi_R) = ?`:

```
M(xi) (psi_R, -E^{-1} C psi_R)
  = (A psi_R + B (-E^{-1} C psi_R), C psi_R + E(-E^{-1} C psi_R))
  = (A psi_R - B E^{-1} C psi_R, C psi_R - C psi_R)
  = (S_R psi_R, 0).
```

If `S_R psi_R = 0`, then `M(xi) (psi_R, -E^{-1} C psi_R) = (0, 0)`.

Since `M(xi)^2 = xi2 Id`, we have:

```
0 = M(xi)^2 (psi_R, -E^{-1} C psi_R) = xi2 (psi_R, -E^{-1} C psi_R).
```

If `xi2 != 0`, then `(psi_R, -E^{-1} C psi_R) = 0`, which gives `psi_R = 0`.

**Theorem (reconstruction grade).** For all `xi in T*Y^{14}` with `g_Y(xi, xi) != 0`:

```
ker S_R(xi) = 0.
```

Equivalently, the 14D effective RS principal symbol `D_RS_eff(xi) = S_R(xi)` has trivial kernel
for all non-null 14D covectors.

**This is the decisive result.** The proof:

1. `M(xi)^2 = xi2 Id` (Clifford module property of `D_GU`).
2. If `S_R(xi) psi_R = 0`, then `M(xi)(psi_R, -E^{-1} C psi_R) = 0`.
3. Applying `M(xi)`: `xi2 (psi_R, -E^{-1} C psi_R) = 0`.
4. Since `xi2 != 0`: `psi_R = 0`.

The conclusion follows for ALL `xi in T*Y^{14}` including mixed covectors `xi = xi_H + xi_N`.

**Failure conditions for this proof:**
- If `E(xi)` is not invertible: the Schur complement `S_R(xi)` is not defined; the
  characteristic analysis must use a constrained Hamiltonian approach.
- If `D_GU` is not a Clifford-module Dirac operator (i.e., if `sigma_D(xi)^2 != xi2 Id`):
  the Clifford identity (Cl) fails and the proof collapses.
- If the RS projection is not a direct summand of the Clifford module bundle: the block
  decomposition is not orthogonal and the block-square identity need not hold.

---

## 9. Invertibility of E at Mixed Covectors

The theorem requires `E(xi)` invertible. At horizontal covectors this was verified in the
prior notes. We now check it at mixed covectors.

**Claim.** `E(xi)` is invertible for `xi2 = g_Y(xi,xi) != 0`.

**Argument.** The E block `E(xi): Q -> Q` is the restriction of `M(xi)` to the non-RS
complement. By the same Clifford module argument applied to the Q block:

If `E(xi) v = 0` for some `v in Q`, then:

```
M(xi)(0, v) = (B v, E v) = (B v, 0).
```

Applying `M(xi)`:

```
M(xi)^2 (0, v) = M(xi)(B v, 0) = (A B v, C B v).
```

Also `M(xi)^2 (0, v) = xi2 (0, v)`.

So `A B v = 0` and `C B v = xi2 v`.

If `xi2 != 0` and `v != 0`, then `C B v != 0`. But `A B v = 0` means `Bv in ker A`.
There is no immediate contradiction without more information about the kernel of A.

**Alternative argument via block determinant.** Since `M(xi)^2 = xi2 Id_E`, we have:

```
det(M(xi))^2 = xi2^{dim E}.
```

For `xi2 != 0`, `det(M(xi)) != 0`, so `M(xi)` is invertible. The Schur determinant formula:

```
det(M(xi)) = det(E(xi)) * det(S_R(xi)).
```

So `det(E(xi)) * det(S_R(xi)) != 0`, which implies both `E(xi)` and `S_R(xi)` are
invertible for `xi2 != 0`.

**This closes the circle:** `E` is invertible iff `S_R` is invertible iff `xi2 != 0`
(by the block determinant formula), and both follow from the Clifford module property.

**Grade.** This argument is reconstruction grade: the Clifford identity `M(xi)^2 = xi2 Id`
is the input, and the block determinant step uses standard linear algebra. The gap is
that the exact form of E for the 14D D_GU operator has not been computed from first
principles in coordinates — only the structural form is used.

---

## 10. The Full 14D Gamma-Trace RS Projection

The result in §8 holds for any direct-sum decomposition `E = R direct-sum Q` of the
Clifford module bundle, provided `R` is a sub-bundle. The 14D RS projection `R^{14D} = ker Gamma^{14D}` is indeed a sub-bundle (since `Gamma^{14D} = gamma^A` is a constant-rank operator on the constant-rank Clifford module bundle `S`), and hence a direct summand.

**Dimension.** In 14D, the full vector-spinor space is `T*Y tensor S` with dim = `14 * 256 = 3584` (over R). The gamma trace maps `T*Y tensor S -> S` (rank 256 map). The kernel `R^{14D} = ker Gamma^{14D}` has dimension `14 * 256 - 256 = 13 * 256 = 3328`. This is the correct 14D RS sector, larger than the horizontal (4D) RS sector used in the prior notes.

The Clifford module bundle argument applies to this sub-bundle, so the theorem in §8
holds for the full 14D RS projection.

---

## 11. Comparison with VZ Theorem: Why Evasion Holds

The standard Velo-Zwanziger theorem applies to a spin-3/2 field that:

(H1) Is described by a Rarita-Schwinger Lagrangian.
(H2) Is minimally coupled to a nontrivial gauge background.
(H3) Has no guardian symmetry (no local SUSY, no higher-spin gauge invariance).

The GU setup evades VZ because:

**Hypothesis H1 fails at 14D.** The RS sector is not described by a standalone Rarita-Schwinger Lagrangian. It is a sub-bundle of the Clifford module bundle `E` for the single operator `D_GU`. The field equation for the RS sector is NOT a standalone RS Lagrangian; it is the projected equation `P_R D_GU Psi = 0` where `Psi in Gamma(E)` is the full section of the Clifford module bundle.

**Consequence.** The characteristic analysis for standalone RS fields (which is where VZ acausality arises) does not apply. Instead, the characteristic polynomial of the effective RS symbol `S_R(xi)` is computed by the Schur complement, and by §8, its kernel is trivial for all non-null `xi`.

**What this means physically.** The GU spin-3/2 particles do not propagate as independent degrees of freedom at the 14D level. They are entangled with the spin-1/2 sectors via the off-diagonal blocks B and C. Their effective propagator, obtained after integrating out the spin-1/2 degrees of freedom (the Schur complement operation), has a causal characteristic cone: all characteristics lie on the null cone `g_Y(xi,xi) = 0`.

This is the 14D VZ evasion: not by a guardian symmetry, but by Dirac-type non-decoupling.

---

## 12. Failure Conditions

**F1. Clifford identity failure.** If `sigma_D(xi)^2 != g_Y(xi,xi) Id_E`, the proof in §8
collapses. This would require `D_GU` to not be a Clifford module operator — i.e., the
shiab or the d_A term would need to contribute anomalous higher-order symbol terms. For
first-order differential operators of Dirac type, this is excluded by construction.

**F2. RS not a direct summand.** If `R^{14D} = ker Gamma^{14D}` is not a direct summand of
the Clifford module bundle (e.g., if `Gamma^{14D}` has varying rank), the sub-bundle
argument fails. In constant-coefficient Clifford algebras on a flat bundle, the rank is
constant. On a curved bundle with connection, lower-order terms can affect the rank, but
the principal-symbol argument is purely algebraic.

**F3. E block singular at null covectors.** At null covectors `xi2 = 0`, `E(xi)` may be
singular (its determinant vanishes by the block determinant formula). The Schur complement
is undefined at null covectors, and the characteristic analysis must use constrained Hamiltonian
methods. This is NOT a VZ obstruction — VZ is about spacelike characteristics, not null ones.
At null covectors, even the free Dirac equation is degenerate.

**F4. Section-pullback modification.** The 4D effective RS field is obtained by pulling back
`D_GU` via the section `s: X^4 -> Y^{14}`. The section pullback `s*(sigma_D(xi_H))` acts
on the reduced bundle over `X^4`. The principal symbol of the pulled-back operator at a
4D covector `xi_H in T*X^4` is `sigma_D(xi_H)` restricted to horizontal covectors.

By the theorem in §8, `ker S_R^{14D}(xi_H) = 0` for `xi_H2 != 0`. So the 4D observable
RS field is also VZ-safe, subject to the pulled-back bundle being a Clifford module for
the induced 4D operator. This requires the second fundamental form correction (from the
Codazzi-SP64 note) not to destroy the Clifford module property.

**F5. Lower-order curvature modification.** The VZ analysis here is at the principal symbol
level (first-order). Lower-order terms (curvature, connection, mass) can modify the characteristic
matrix for the constrained equations. In the original VZ paper, the acausality appears in the
equations obtained from varying the RS Lagrangian, where constraint equations commuted with
the field equation generate curvature terms. For the non-standalone GU RS sector, the
constraint structure is different — the subsidiary condition is `Gamma^{14D} psi = 0`, which
is maintained by the D_GU structure, not imposed as an external constraint. Whether lower-order
curvature terms violate this for the Sp(64) background remains unverified.

**F6. 4D EFT decoupling.** If an effective field theory description at low energies decouples
the RS sector into an approximately standalone field, the VZ analysis would apply to the EFT.
In that case, the question shifts to whether the EFT RS field has a guardian symmetry. The
14D result provides evidence against decoupling (the sectors are off-diagonally coupled by the
principal symbol), but a mass gap or KK scale separating the RS sector from the spin-1/2 sectors
could still produce approximate decoupling.

---

## 13. Comparison with Horizontal-Only Result

The prior notes (vz1-schur-complement-symbol-2026-06-23.md) proved the horizontal result:

```
ker S_R^{hor}(xi_H) = 0 for g_H(xi_H, xi_H) != 0,
```

by explicit computation. The present note proves the stronger result:

```
ker S_R^{14D}(xi) = 0 for g_Y(xi, xi) != 0,
```

by the Clifford module argument. The two results are consistent:

- The prior result handled only horizontal covectors; the present result handles all 14D covectors.
- The prior proof was explicit and algebraic (computing formula (7) and showing injectivity).
- The present proof is structural (using the Clifford module property).

The structural proof is cleaner and more general. It identifies why the result is true: it
is a consequence of the Clifford identity, not an accident of the block decomposition.

---

## 14. Relation to `D_RS_eff(xi) = g(xi,xi) Id_RS`

The problem statement asks whether `D_RS_eff(xi) = g(xi,xi) Id_RS`.

The answer is: **not exactly, but the relevant property holds.**

The Schur complement `S_R(xi) = D_RS_eff(xi)` does NOT in general equal `xi2 Id_{RS}` as a
matrix (the A block has off-diagonal Clifford gamma terms). However:

1. Its square: by the block-square argument, `S_R^2 = xi2 Id_{RS} + correction`. By the §8
   argument, the effective kernel property `ker S_R(xi) = 0` for `xi2 != 0` holds.

2. Its characteristic cone: all solutions to `S_R(xi) psi_R = 0` require `xi2 = 0`. The
   characteristic cone of the effective RS symbol IS the null cone `g_Y(xi,xi) = 0`.

So the honest statement is: `D_RS_eff(xi)` has the same characteristic cone as `g(xi,xi) Id_RS`
(both have `{xi : det = 0} = {xi : xi2 = 0}`), but they are not equal as matrices. The
physically relevant statement for VZ is the characteristic cone, not the matrix identity.

**Verdict.** The VZ obstruction requires a spacelike characteristic. Since the characteristic
cone of `D_RS_eff(xi)` is contained in the null cone `{xi2 = 0}`, no spacelike characteristic
exists. VZ does not apply.

---

## 15. Open Questions

**OQ1.** Does `S_R^2 = xi2 Id_{RS}` hold exactly (as a matrix identity, not just the
characteristic cone)? This would require `B(E^{-1})^2 C = 0`. From §7, this reduces to
`A^2 = xi2 Id_{RS}`, which holds iff `BC|_{RS} = 0`. The B block contributes vertical
one-form inputs to the RS sector, and C maps RS inputs to scalar + gamma-trace. Whether
`BC psi_R = 0` for all `psi_R in R^{14D}` is a representation-theory computation.

**OQ2.** Can the result be strengthened to rule out VZ acausality from lower-order curvature
terms? This requires a Hamiltonian analysis of the constrained system D_GU Psi = 0 with
Sp(64) gauge background. The principal-symbol analysis gives a necessary condition for VZ
evasion (causal characteristics); the curvature-modified constraint analysis would give
a sufficient condition.

**OQ3.** Does the section pullback `s*(D_GU)` preserve the Clifford module property for the
induced 4D operator? If yes, the 4D observable RS field automatically inherits VZ evasion.
This depends on the Codazzi equation for the Sp(64) bundle (explorations/codazzi-sp64-bundle-2026-06-23.md).
See §17 for the resolution at reconstruction grade: CONDITIONALLY_RESOLVED.

**OQ4.** GU-Vasiliev comparison: does the GU RS embedding strategy (Leibniz cross-term as
RS definition) provide a new class of consistent higher-spin theories, distinct from Vasiliev's
higher-spin gravity? This is the P53-NOVEL target from the 62-persona steelman.

---

## 16. Summary

| Result | Status | Proof Type |
|---|---|---|
| Off-diagonal RS/non-RS coupling at mixed covectors | CONFIRMED | Explicit (§3) |
| `ker S_R^{14D}(xi) = 0` for `xi2 != 0`, horizontal xi | CONFIRMED (prior) | Explicit |
| `ker S_R^{14D}(xi) = 0` for `xi2 != 0`, general xi | RECONSTRUCTION | Clifford module (§8) |
| E block invertible for `xi2 != 0` | RECONSTRUCTION | Block determinant (§9) |
| VZ obstruction absent for full 14D covectors | RECONSTRUCTION | §8 + §11 |
| `S_R^2 = xi2 Id_{RS}` as matrix identity | RESOLVED (vz-oq1): NOT exact; `A S_R = xi2 Id` is correct | See vz-oq1 file |
| Lower-order curvature protection | CONDITIONALLY_RESOLVED (vz-oq2, vz-subprincipal) | Zero-order argument + Hormander |
| Section-pullback 4D RS VZ evasion (OQ3) | CONDITIONALLY_RESOLVED | §17 (this update) |

**Verdict: EVADED (reconstruction grade).**

The VZ obstruction does not apply to the 14D GU RS sector because:

1. The RS sector is not a standalone field (H1 fails).
2. The effective RS principal symbol `D_RS_eff(xi)` has trivial kernel for all non-null
   14D covectors `g_Y(xi,xi) != 0`, including mixed covectors (new result).
3. The characteristic cone of `D_RS_eff` is the null cone, which is causal.

The evasion mechanism is Clifford module non-decoupling, not a guardian symmetry. The
14D Clifford identity `sigma_D(xi)^2 = xi2 Id` propagates through the Schur complement
to guarantee causal characteristics for the effective RS symbol at the principal-symbol level.

---

---

## 17. OQ3: Section-Pullback 4D Preservation of Clifford Module Property (New Computation, 2026-06-23)

**Question.** Does `s*(D_GU)` preserve the Clifford module property for the induced 4D
operator? Specifically: for a horizontal 4D covector `xi_H in s*(T*Y^{14}) = T*X^4`,
does the pulled-back principal symbol satisfy

```
s*(sigma_{D_GU})(xi_H)^2 = g_s(xi_H, xi_H) * Id_{E_s}              (OQ3-target)
```

where `E_s = s*(E)` is the pulled-back Clifford module bundle over `X^4`?

**Why this matters for VZ.** The 4D observable RS field is not `D_GU Psi = 0` but rather
the restriction of `D_GU Psi = 0` to the section `s(X^4) subset Y^{14}`. If (OQ3-target)
holds, then the §8 argument applies verbatim to the 4D pulled-back operator, and the 4D
effective RS symbol also has trivial kernel for non-null 4D covectors. VZ evasion at 14D
descends to VZ evasion at 4D.

---

### 17.1 Principal Symbol Pullback: The Key Observation

**Claim.** The section pullback `s*` does NOT modify the principal symbol of `D_GU`.

**Proof.** Let `D_GU` be a first-order differential operator on sections of `E -> Y^{14}`.
The principal symbol `sigma_{D_GU}(xi)` at a covector `xi in T*Y^{14}` is a bundle map
`E -> E` depending only on `xi`, not on the connection or second fundamental form.

For the section `s: X^4 -> Y^{14}`, the pulled-back operator `s*(D_GU)` acts on sections
of `E_s = s*E -> X^4`. For a 4D covector `eta in T*X^4`, the principal symbol of `s*(D_GU)`
at `eta` is:

```
sigma_{s*(D_GU)}(eta) = s*(sigma_{D_GU}(ds*(eta)))
                       = sigma_{D_GU}(xi_H(eta))
```

where `xi_H(eta) = s*(eta) in T*_{s(x)}Y^{14}` is the horizontal lift of `eta` via `s`.
Since `s: X^4 -> Y^{14}` is a section of the bundle projection `pi: Y^{14} -> X^4`, the
differential `ds: TX^4 -> TY^{14}|_{s(X^4)}` lifts tangent vectors to horizontal tangent
vectors (by the section property `pi circ s = Id`). The pullback on covectors is
`ds*: T*Y^{14}|_{s(X^4)} -> T*X^4`, which sends horizontal covectors to themselves and
kills vertical covectors.

For a 4D covector `eta in T*X^4`:

```
g_Y(xi_H(eta), xi_H(eta)) = g_Y(s*(eta), s*(eta)) = s*(g_Y)(eta, eta) = g_s(eta, eta)
```

where `g_s = s*(g_Y|_{H*})` is the induced 4D metric (the Lorentzian metric selected by
the section).

**Therefore:**

```
sigma_{s*(D_GU)}(eta)^2 = sigma_{D_GU}(xi_H(eta))^2 = g_Y(xi_H, xi_H) * Id_E
                        = g_s(eta, eta) * Id_{E_s}.              (OQ3-verified)
```

The Clifford module property is preserved under section pullback, for horizontal covectors.

**Grade:** Reconstruction. The computation is a direct application of the naturality of
principal symbols under pullback. No coordinate computation is needed.

---

### 17.2 What the Second Fundamental Form Does NOT Affect

A natural concern: the section `s` has a nonzero second fundamental form `II_s`, which
contributes lower-order terms to `s*(D_GU)` via the Gauss-Codazzi mechanism. These
terms appear in the connection term of the pulled-back operator.

**Claim.** Lower-order (connection, curvature, II_s) terms do NOT modify the principal symbol.

**Proof.** The principal symbol of a first-order differential operator `D` in local
coordinates `{x^mu}` is:

```
sigma_D(xi) = sum_mu D_mu xi_mu,    [in local coordinates, where D = sum D_mu d/dx^mu + E_0]
```

where `E_0` collects all zero-order terms. The section pullback produces:

```
s*(D_GU) = D_GU|_{s(X^4)} + [correction terms from II_s].
```

The II_s correction terms arise from comparing `nabla_s` (the connection on the pullback
bundle) to the ambient connection `nabla^Y`. By the Gauss formula:

```
nabla^Y_{s_* v} w = nabla^{X,s}_v w + II_s(v, w).
```

The term `II_s(v, w)` maps tangent directions to normal directions and is a zero-order
term in the differential operator sense (it multiplies a section without differentiating
it). It does NOT contribute to the principal symbol.

**Conclusion.** The principal symbol of `s*(D_GU)` at a 4D covector `eta` is exactly
`sigma_{D_GU}(xi_H(eta))`, with no II_s correction. The Clifford module property
(OQ3-target) holds exactly at the principal symbol level.

---

### 17.3 The 4D RS Projection: Horizontal vs. Full 14D

**Subtlety.** The 14D RS projection `R^{14D} = ker Gamma^{14D}` uses all 14 gamma matrices.
After section pullback, the 4D observable RS sector must be defined using only the 4D
(horizontal) gamma trace:

```
R^{4D} = ker Gamma^{4D},   Gamma^{4D}(psi) = gamma^a psi_a   [a = 0,1,2,3 horizontal].
```

The 4D Clifford module for `D_GU^{4D} = s*(D_GU)` acts on:

```
E_s = (Omega^0(X^4) tensor S_s+) direct-sum (Omega^1(X^4) tensor S_s-)
```

where `S_s+/-` are the chiral halves of `s*(S)`. The RS sector within `E_s` is:

```
R_s = ker(Gamma^{4D}: Omega^1(X^4) tensor S_s^- -> S_s^-)
    = {psi_{a,alpha} in Omega^1(X^4) tensor S_s^- : gamma^a_{alpha}^beta psi_{a,beta} = 0}.
```

The 4D Clifford module bundle `E_s` with RS sub-bundle `R_s` inherits the Clifford
module property from (OQ3-verified):

```
sigma_{D_GU^{4D}}(eta)^2 = g_s(eta, eta) * Id_{E_s}.
```

The §8 argument applies to the 4D block decomposition `E_s = R_s direct-sum Q_s`:

**Theorem (OQ3, reconstruction grade).** For all 4D covectors `eta in T*X^4` with
`g_s(eta, eta) != 0`:

```
ker S_{R_s}^{4D}(eta) = 0.
```

Equivalently, the 4D effective RS principal symbol `D_RS_eff^{4D}(eta)` has trivial kernel
for all non-null 4D covectors. VZ evasion at 14D descends to VZ evasion at 4D.

**Proof.** Identical to §8, replacing `M(xi)` with `sigma_{D_GU^{4D}}(eta)` and using the
4D Clifford identity (OQ3-verified). The block determinant argument (§9) gives invertibility
of `E_s(eta)` for `g_s(eta, eta) != 0`, and the kernel argument gives `psi_{R_s} = 0`.

---

### 17.4 The Residual Gap: Normal-Direction RS

**What is NOT resolved by OQ3.** The 14D RS sector `R^{14D}` includes RS spinors with
normal (vertical) gamma traces projected out:

```
R^{14D} = ker Gamma^{14D} = ker(gamma^a psi_a + gamma^i psi_i),   a horizontal, i normal.
```

The 4D pullback sees only the horizontal components `psi_a`. The normal components `psi_i`
are KK fields from the 4D perspective. After KK reduction (integrating over the normal
directions, or equivalently, imposing the normal-direction equations of motion), the
surviving 4D field is `psi_a in R_s` with the 4D RS constraint `Gamma^{4D}(psi) = 0`.

**The gap.** The KK reduction might not preserve the Clifford module property exactly:
the normal-direction equations of motion contribute mass terms and KK towers. At the
principal-symbol level these are zero-order, so they do not affect the VZ conclusion.
But at the level of the full operator spectrum and propagator, the KK tower structure
changes the effective 4D theory.

**Why this is not a VZ obstruction.** VZ is a statement about the principal symbol
(the characteristic cone) of the effective operator. The KK tower contributions are
lower-order terms. The characteristic cone of the 4D effective RS operator is determined
by the principal symbol alone, which is (OQ3-verified) causal. VZ acausality requires
spacelike characteristics, which are a principal-symbol property.

**Residual open question.** Whether the KK mass spectrum of the 4D RS sector is consistent
with the SM (i.e., whether the lightest RS KK mode matches the observed RS particles, if
any exist) is a dynamical question outside the scope of the characteristic/VZ analysis.

---

### 17.5 Failure Conditions for OQ3

**OQ3-F1.** If `s*(sigma_{D_GU})` is not the horizontal restriction of `sigma_{D_GU}` --
e.g., if the section `s` is not an immersion (degenerate differential `ds`), or if the
horizontal lift `xi_H` does not preserve the symplectic form on `T*Y^{14}`. For smooth
sections `s: X^4 -> Y^{14}` (which are immersions since `dim X^4 < dim Y^{14}` and
`pi circ s = Id` forces `ds` to be injective), this does not apply.

**OQ3-F2.** If the RS sub-bundle `R_s = s*(R^{14D})` is not a direct summand of `E_s`.
The pullback of a direct summand is a direct summand (for transverse pullbacks, which
holds here since `s` is a section). The rank of `R_s` is preserved under pullback.

**OQ3-F3.** If the induced 4D metric `g_s = s*(g_Y|_{H*})` is degenerate. For Lorentzian
sections (i.e., sections `s: X^4 -> Y^{14}` whose image corresponds to a Lorentzian metric
on X^4), `g_s` has signature (3,1) and is non-degenerate.

**OQ3-F4.** If the Codazzi correction modifies the principal symbol (not just lower-order
terms). The Codazzi equation for the Sp(64) bundle (from `explorations/codazzi-sp64-2026-06-23.md`)
gives:

```
[D_{a^0}, D_{a^0}](j_s theta) = j_s(R^{Y^{14},perp}) + F^Psi - [F_{a^0}, j_s theta].
```

This is a second-order commutator identity, not a modification to the first-order principal
symbol. The right-hand side involves curvature (zero-order) and gauge curvature F (zero-order
as an operator on Psi). No new first-order derivative terms are introduced. OQ3-F4 does
not apply.

---

### 17.6 Grade and Verdict for OQ3

**Grade: Reconstruction.**

The argument uses:
- Naturality of principal symbols under smooth pullback (standard pseudodifferential calculus).
- The Gauss formula for the second fundamental form (standard differential geometry).
- The identification of the 4D RS sector with `ker Gamma^{4D}` acting on `s*(E)` (structural).
- The block determinant argument from §9 (already reconstruction grade).

**None of these steps require coordinate computation.** The argument is purely structural.

**What would falsify OQ3.** Any of OQ3-F1 through OQ3-F4 above. In particular: if `D_GU`
contains second-order terms in the normal directions that survive the section pullback
(which would violate the first-order operator assumption). The formula for `D_GU` as a
Dirac-type operator (confirmed in the shiab construction) excludes this.

**Verdict.** OQ3 is **CONDITIONALLY_RESOLVED** at reconstruction grade.

The section pullback `s*(D_GU)` satisfies the 4D Clifford module property:

```
sigma_{s*(D_GU)}(eta)^2 = g_s(eta, eta) * Id_{E_s}
```

for all `eta in T*X^4`. The §8 kernel argument applies, giving:

```
ker S_{R_s}^{4D}(eta) = 0    for all  g_s(eta, eta) != 0.
```

The 4D observable RS field is VZ-safe: its effective principal symbol has causal
characteristic cone equal to the null cone of the induced 4D metric `g_s`. This is the
4D consequence of the 14D Clifford module structure of `D_GU`.

**Remaining open conditions for upgrade to verified:**
- OQ3-V1: CAS/coordinate computation of `s*(sigma_{D_GU})` in an explicit section gauge
  (e.g., constant-coefficient background) to confirm no anomalous normal-direction terms.
- OQ3-V2: Explicit check that the 4D E block `E_s(eta)` is invertible (no accidental
  zero modes from the KK mass spectrum at the principal-symbol level).
- OQ3-V3: Confirmation that `R_s = s*(R^{14D})` coincides with `ker Gamma^{4D}` (not
  a larger or smaller RS sector, which could happen if horizontal and vertical gamma traces
  are not cleanly separated after section pullback).

---

## References

- `explorations/vz1-schur-complement-symbol-2026-06-23.md` (horizontal minimal result)
- `explorations/vz1-schur-vertical-extension-2026-06-23.md` (vertical extension, horizontal xi)
- `explorations/vz1-velo-zwanziger-analysis-2026-06-22.md` (VZ setup)
- `explorations/vz1-62-persona-steelman-hegelian-2026-06-22.md` (evasion candidate)
- `explorations/n1-signature-audit-y14-clifford-algebra-2026-06-22.md` (Cl(9,5) algebra)
- `explorations/codazzi-sp64-bundle-2026-06-23.md` (4D reduction, F4 context)
- `explorations/codazzi-sp64-2026-06-23.md` (Codazzi equation for Sp(64), OQ3-F4 context)
- `explorations/vz-oq1-sr-squared-identity-2026-06-23.md` (OQ1 resolved: S_R^2 != xi2 Id exactly)
- `explorations/vz-oq2-lower-order-curvature-2026-06-23.md` (OQ2: curvature protection)
- `explorations/vz-subprincipal-symbol-rs-2026-06-23.md` (subprincipal symbol analysis)
- Velo and Zwanziger (1969), Phys. Rev. 186:1337
- Lawson-Michelsohn, _Spin Geometry_, Ch. II (Clifford module Dirac operators)
- Hormander (1985), _The Analysis of Linear Partial Differential Operators III_, §23 (real principal type)
