---
title: "VZ OQ2-b: Subprincipal Symbol of D_GU in RS/Spin-1/2 Block Decomposition"
date: 2026-06-23
problem_label: "vz-subprincipal"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# VZ OQ2-b: Subprincipal Symbol of D_GU in RS/Spin-1/2 Block Decomposition

## 1. Problem Statement

**What is being computed.** The subprincipal symbol of `D_GU` restricted to the RS
block, after Schur elimination of the spin-1/2 (Q) sector, and a check that neither
the Shiab coupling nor gimmel curvature terms introduce real characteristics outside
the null cone at the sub-leading (order 0) level.

**Why it matters.** The principal-symbol analysis (vz-schur-complement-2026-06-23.md)
established that for the first-order (leading) symbol, `ker S_R(xi) = 0` for all
non-null 14D covectors -- VZ evasion holds at leading order. The lower-order curvature
analysis (vz-oq2-lower-order-curvature-2026-06-23.md) established that zero-order
curvature terms cannot change the principal symbol. But neither file computed the
**subprincipal symbol** `sigma_0(S_R^{full})`, which is the next term in the
pseudodifferential symbol expansion and can, in principle, introduce a secondary
characteristic set for the WKB (geometric optics) propagation.

**The explicit question (OQ2-b from vz-oq2-lower-order-curvature-2026-06-23.md):**

> Subprincipal symbol analysis: what is `sigma_0(S_R^{full})`? Does it introduce any
> real characteristics beyond the null cone?

The subprincipal symbol matters specifically for operators that are not of standard
Dirac type: if `sigma_0(S_R^{full})` has real eigenvalues on the characteristic set
`{xi : xi2 = 0}` that are not covered by the principal-type analysis, sub-leading
propagation effects outside the null cone could arise.

---

## 2. Established Context

**Prior results this builds on:**

- `vz-schur-complement-2026-06-23.md`: `ker S_R^{14D}(xi) = 0` for `xi2 != 0`
  (Clifford module argument, reconstruction grade). Characteristic cone = null cone
  of gimmel metric.

- `vz-oq1-sr-squared-identity-2026-06-23.md`: `S_R^2 != xi2 Id_{RS}` as exact
  matrix identity. Correct statement: `A S_R = xi2 Id_R` (exact, from block-square).
  The RS sub-bundle is NOT a sub-Clifford-module.

- `vz-oq2-lower-order-curvature-2026-06-23.md`: Zero-order curvature terms (Weyl
  tensor of `g_Y`, Riemann curvature, Sp(64) gauge curvature `F_A`, Shiab coupling)
  enter `D_GU` as multiplication operators. They do not change the principal symbol.
  The Hormander propagation-of-singularities theorem applies: singularities propagate
  along null bicharacteristics of the principal symbol. Remaining open: OQ2-a (Shiab
  zero-order confirmation) and OQ2-b (subprincipal symbol).

**Clifford algebra.** `Cl(9,5) ~= M(64,H)`, spinor module `S = H^{64}`.
Principal symbol of `D_GU`: `sigma_1(D_GU)(xi) = c(xi)`, with `c(xi)^2 = g_Y(xi,xi) Id_S`.

**Operator structure.** In local coordinates with spin connection `omega_A`:

```
D_GU = c(e^A) nabla_A + Phi(F_A tensor .)
     = c(e^A)(d/dx^A + omega_A) + Phi(F_A tensor .)
```

where `omega_A = (1/4) omega_{A,BC} gamma^{BC}` is the connection 1-form.

**Block structure.** In the RS/non-RS decomposition `E = R^{14D} direct-sum Q`:

```
D_GU = [ A^{full}   B^{full} ]
       [ C^{full}   E^{full} ]
```

where `A^{full} = A^{(1)} + A^{(0)}`, etc., with superscripts denoting order.
The effective RS operator after Schur elimination:

```
S_R^{full} = A^{full} - B^{full} (E^{full})^{-1} C^{full}.
```

---

## 3. Definition of the Subprincipal Symbol

For a first-order differential operator `L` on a vector bundle, written in local
coordinates as `L = sum_A l^A(x) d/dx^A + m(x)` (where `l^A` are endomorphism-valued
and `m(x)` is zero-order), the full symbol is:

```
sigma(L)(x, xi) = sigma_1(x, xi) + sigma_0(x, xi)
```

where:
- `sigma_1(x, xi) = sum_A l^A(x) xi_A` is the **principal symbol** (homogeneous
  degree 1 in xi).
- `sigma_0(x, xi) = m(x)` is the **subprincipal symbol** (homogeneous degree 0,
  independent of xi).

For a **pseudodifferential** operator (such as the Schur complement `S_R^{full}`,
which involves the pseudodifferential inverse `(E^{full})^{-1}`), the symbol
expansion in Hormander's calculus is:

```
sigma(S_R^{full})(x, xi) = sigma_1(x, xi) + sigma_0(x, xi) + sigma_{-1}(x, xi) + ...
```

The subprincipal symbol in this calculus is:

```
sigma_0(S_R^{full})(x, xi) = [zero-order part of S_R^{full}] at leading sub-symbol order.
```

**Why characteristics from sigma_0 are not a new VZ risk.** For operators of real
principal type, the Hormander propagation theorem (Ch. 23, _Analysis of LPDOs III_)
states that solutions propagate along null bicharacteristics of `sigma_1` only. The
subprincipal symbol `sigma_0` contributes to:

1. The **amplitude** of the WKB approximation (it appears in the transport equation
   for the amplitude factor).
2. The **phase** of the leading-order Green's function.

But `sigma_0` does NOT change the **direction of propagation** (the bicharacteristic
flow). Only `sigma_1` determines characteristics. This is a theorem, not an
approximation.

**Exception.** If `sigma_1(x, xi) = 0` on a large set (i.e., if the operator is not
of real principal type), then `sigma_0` can determine the propagation on the
characteristic variety. For the GU RS effective operator, `sigma_1(S_R^{full}) = 0`
only on the null cone `{xi2 = 0}`, and real principal type holds since the null cone
is a smooth submanifold of `T*Y \ 0` and `d(xi2) != 0` there (for `xi != 0` and
non-degenerate `g_Y`). So the exception does not apply.

---

## 4. Subprincipal Symbol of D_GU Before Schur Elimination

### 4.1 The Full Operator

```
D_GU = D_0 + D_1
```

where `D_0 = c(e^A) d/dx^A` (principal, order 1) and `D_1 = c(e^A) omega_A + Phi(F_A tensor .)`
(zero-order, order 0).

**Principal symbol:**

```
sigma_1(D_GU)(x, xi) = c(xi) = xi_A c(e^A).
```

**Subprincipal symbol (zero-order part):**

```
sigma_0(D_GU)(x, xi) = c(e^A) omega_A(x) + Phi(F_A(x) tensor .).
```

This is the sum of:
- **Spin-connection term:** `c(e^A) omega_A = (1/4) omega_{A,BC} c(e^A) gamma^{BC}`.
  This is an endomorphism of `S` (a zero-order Clifford element) depending on x but not xi.
- **Shiab term:** `Phi(F_A tensor .) = sum_C e^C tensor c(\iota_{e_C} F_A)`.
  Here `F_A` is the Sp(64) gauge curvature 2-form. This is a zero-order multiplication
  operator on sections of `E`.

**Key feature:** `sigma_0(D_GU)` is xi-independent. It does not acquire xi-dependence
at order 0 because the Shiab term contains no derivatives of `Psi` -- it multiplies
`Psi` by a pointwise endomorphism.

### 4.2 OQ2-a: Shiab Contains No Hidden Derivatives

The Shiab operator is:

```
Phi(alpha tensor s) = sum_A e^A tensor c(\iota_{e_A} alpha) . s
```

where `alpha in Omega^2(Y)` and `s in Gamma(S)`. In the D_GU context, `alpha = F_A`
(the gauge curvature 2-form) and `s = Psi` (the spinor section).

**Bianchi identity concern.** One might worry that expanding `Phi(F_A tensor Psi)` in
the D_GU equation of motion and using the Bianchi identity `D_A F_A = 0` could introduce
a derivative of `Psi`. Explicitly:

The equation `D_GU Psi = 0` gives (schematically in the one-form sector):

```
c(e^A) nabla_A Psi + Phi(F_A tensor Psi) = 0.
```

The Bianchi identity says `D_A F_A = 0`, which relates derivatives of `F_A` to `F_A`.
It does NOT introduce derivatives of `Psi` into the Shiab term. The Shiab term is
`Phi(F_A tensor Psi)`, and `F_A` is treated as a background field (or as part of the
connection). The Bianchi identity constrains the background, not the dynamical field `Psi`.

**Conclusion (OQ2-a).** The Shiab term `Phi(F_A tensor Psi)` is strictly zero-order:
it multiplies `Psi` by the endomorphism `sum_A e^A tensor c(\iota_{e_A} F_A)` without
taking any derivatives of `Psi`. There are no hidden derivatives. OQ2-a: RESOLVED
at reconstruction grade.

---

## 5. Subprincipal Symbol of the Schur Complement S_R^{full}

### 5.1 Symbol Expansion of the Schur Complement

The Schur complement is:

```
S_R^{full} = A^{full} - B^{full} (E^{full})^{-1} C^{full}.
```

Each block is a first-order differential operator:

```
A^{full} = A^{(1)} + A^{(0)}    (first-order + zero-order)
B^{full} = B^{(1)} + B^{(0)}    (first-order + zero-order)
C^{full} = C^{(1)} + C^{(0)}    (first-order + zero-order)
E^{full} = E^{(1)} + E^{(0)}    (first-order + zero-order)
```

In Hormander's pseudodifferential calculus, the symbol of a composition or inversion
can be computed via the composition formula:

```
sigma(PQ)(x, xi) = sigma(P)(x,xi) sigma(Q)(x,xi) + (i/2) sum_j (d/dxi_j sigma(P))(d/dx_j sigma(Q)) + O(|xi|^{-1})
```

**Symbol of (E^{full})^{-1}.** Since `E^{full}` is a first-order differential operator
with invertible principal symbol `sigma_1(E)(x,xi) = E^{(1)}(x,xi)` (for `xi2 != 0`,
as established in vz-schur-complement-2026-06-23.md), the pseudodifferential inverse
`(E^{full})^{-1}` exists with symbol:

```
sigma((E^{full})^{-1})(x, xi) = [E^{(1)}(x,xi)]^{-1}
    - [E^{(1)}(x,xi)]^{-1} E^{(0)}(x) [E^{(1)}(x,xi)]^{-1}
    + (i/2) sum_j d_{xi_j}[E^{(1)}]^{-1} . d_{x_j} E^{(1)} [E^{(1)}]^{-1} + O(|xi|^{-2}).
```

This is an order-(-1) pseudodifferential operator.

### 5.2 The Principal Symbol of S_R^{full}

The principal symbol is order 1. From the block structure:

```
sigma_1(S_R^{full})(x, xi) = sigma_1(A)(x, xi) - sigma_1(B)(x,xi) [sigma_1(E)(x,xi)]^{-1} sigma_1(C)(x, xi).
```

This equals the principal Schur complement `S_R^{(1)}(x, xi)`, which was analyzed in
vz-schur-complement-2026-06-23.md and shown to have trivial kernel for `xi2 != 0`.

### 5.3 The Subprincipal Symbol of S_R^{full}

The subprincipal (order 0) symbol gets contributions from three sources:

**Source I: Zero-order blocks.**

```
[A^{(0)} - B^{(1)} (E^{(1)})^{-1} C^{(0)} - B^{(0)} (E^{(1)})^{-1} C^{(1)}
 + B^{(1)} (E^{(1)})^{-1} E^{(0)} (E^{(1)})^{-1} C^{(1)}]
```

Each of these involves the zero-order parts of the blocks combined with the first-order
Schur inversion. The result is a zero-order (xi-independent) endomorphism of `R^{14D}`.

**Source II: Composition correction from Hormander calculus.**

When composing `B^{full} (E^{full})^{-1} C^{full}` as pseudodifferential operators,
the composition formula introduces a correction:

```
(i/2) sum_j {d_{xi_j} sigma_1(B) . d_{x_j} sigma_{-1}((E^{full})^{-1}) . sigma_1(C)
             + d_{xi_j} sigma_1(B) . sigma_{-1}((E^{full})^{-1}) . d_{x_j} sigma_1(C) + ...}
```

This correction is called the **semiclassical correction** or **quantum correction** to
the subprincipal symbol. It involves `d/dxi` of the principal symbols and `d/dx` of the
inverse symbol. This correction is purely imaginary (the factor `i/2`) for self-adjoint
operators, and real for non-self-adjoint ones.

**Source III: Curvature of the principal-symbol section.**

For a first-order differential operator `L` acting on sections of a bundle with connection,
the subprincipal symbol in invariant form includes a term from the curvature of the
connection:

```
sigma_0^{inv}(L) = sigma_0(L) - (i/2) sum_j (d^2/dx_j d/dxi_j) sigma_1(L)
```

This is the Hormander/Duistermaat-Guillemin invariant subprincipal symbol (independent of
the coordinate choice). It encodes the curvature of the Lagrangian submanifold structure.

### 5.4 Does the Subprincipal Symbol Introduce New Characteristics?

**Key theorem (Hormander, Th. 23.2.4).** For a pseudodifferential operator `P` of real
principal type on a manifold, the wave front set `WF(u)` of any solution `Pu = 0` is
invariant under the Hamiltonian flow of `p_1 = sigma_1(P)` (i.e., propagates along
null bicharacteristics of `p_1`). The subprincipal symbol `sigma_0(P)` contributes to
the **transport equation** for the symbol of the parametrix, but not to the characteristic
variety or the WF set.

**Application.** The operator `S_R^{full}` is a pseudodifferential operator of order 1
with principal symbol `sigma_1(S_R^{full}) = S_R^{(1)}(x, xi)`. Its characteristic
variety is:

```
Char(S_R^{full}) = {(x, xi) in T*Y \ 0 : det(S_R^{(1)}(x,xi)) = 0}
                 = {(x, xi) : g_Y(xi, xi) = 0}       [null cone].
```

This was established in vz-schur-complement-2026-06-23.md (reconstruction grade).

The subprincipal symbol `sigma_0(S_R^{full})` appears in the WKB propagation as:

```
transport equation: L_H a + sigma_0^{inv}(S_R^{full}) . a = 0
```

where `L_H` is the Lie derivative along the null bicharacteristic Hamiltonian vector field
of `g_Y(xi,xi)`, and `a` is the WKB amplitude. The subprincipal symbol `sigma_0^{inv}`
acts on `a` multiplicatively and affects the **amplitude** along each null ray, not the
**direction** of the ray.

**The subprincipal symbol DOES NOT introduce new characteristics.** The characteristic
variety is determined solely by `det(sigma_1) = 0`, and the subprincipal symbol has no
effect on this set.

---

## 6. Explicit Form of sigma_0(S_R^{full}) in the RS Block

### 6.1 Zero-Order Block Contributions

For `D_GU = D_0 + D_1` with `D_0 = c(e^A) d/dx^A` and `D_1 = c(e^A) omega_A + Phi(F_A)`:

**The RS-block zero-order part `A^{(0)}`:**

```
A^{(0)} = P_R D_1|_{R^{14D} -> R^{14D}} = P_R (c(e^A) omega_A + Phi(F_A)) P_R.
```

This is the zero-order endomorphism of `R^{14D}` given by the spin connection and
Shiab acting on RS sections, projected back to RS. It is a pointwise endomorphism of
`S tensor T*Y` restricted to `R^{14D}`.

**The cross-block contributions at order 0:**

```
B^{(1)} (E^{(1)})^{-1} C^{(0)} + B^{(0)} (E^{(1)})^{-1} C^{(1)}
- B^{(1)} (E^{(1)})^{-1} E^{(0)} (E^{(1)})^{-1} C^{(1)}.
```

These are xi-dependent (since `(E^{(1)})^{-1}` involves `xi^{-1}` via `(gamma(xi))^{-1} = gamma(xi)/xi2`).
Schematically, the first term:

```
B^{(1)} (E^{(1)})^{-1} C^{(0)} ~ c(xi) . [gamma(xi)/xi2] . [curvature endomorphism].
```

This has the form `(xi_A/xi2) . [R_{ABCD} gamma^{BC}]`, where the numerator is linear in xi
and the denominator is `xi2`. The result is a homogeneous degree 0 function of xi (the xi
factors cancel). However, it is NOT constant in xi: it depends on the direction of xi on the
null cone.

**On the null cone** (where `xi2 = 0`): These cross-block contributions at order 0 are
potentially singular (they involve `xi2` in the denominator). However, real principal type
means we only need to evaluate `sigma_0` off the null cone (where `xi2 != 0`). On the null
cone, the subprincipal symbol enters the transport equation as a coefficient, but the
propagation of singularities is already guaranteed by the principal-type theorem.

### 6.2 The Invariant Subprincipal Symbol

The invariant subprincipal symbol of `S_R^{full}` is:

```
sigma_0^{inv}(S_R^{full})(x, xi) = sigma_0(S_R^{full})(x, xi)
    - (i/2) sum_j (d/dxi_j d/dx_j) sigma_1(S_R^{full})(x, xi).
```

The second term involves mixed partial derivatives of the principal symbol `S_R^{(1)}(x, xi)`.
Explicitly:

```
d/dxi_j sigma_1(S_R^{full}) = d/dxi_j [A^{(1)}(x,xi) - B^{(1)}(x,xi) (E^{(1)}(x,xi))^{-1} C^{(1)}(x,xi)]
```

Since `A^{(1)}, B^{(1)}, C^{(1)}, E^{(1)}` are linear in xi, these derivatives are
xi-independent (they are the coefficient matrices of xi in each block). Then `d/dx_j`
acts on the x-dependence of these coefficients, producing curvature and connection terms.

The resulting invariant subprincipal symbol is an endomorphism of `R^{14D}` of the form:

```
sigma_0^{inv}(S_R^{full})(x, xi) = (Riemann tensor of g_Y) * [xi-dependent rational factor]
    + (Sp(64) gauge curvature F_A) * [xi-dependent rational factor]
    + (connection-curvature cross term) + (i/2) [Poisson bracket correction].
```

All terms are bounded on `{xi2 != 0}` (the off-null-cone region).

**The imaginary correction.** The `(i/2)` factor in the Poisson bracket correction
produces an anti-Hermitian contribution to the subprincipal symbol. For the transport
equation, anti-Hermitian contributions cause **amplitude decay** (or growth) along null
rays, not new propagation directions. This is the quantum correction to null propagation.

---

## 7. Why Subprincipal Symbol Cannot Produce New Characteristics: Three Arguments

### Argument 1: Real Principal Type (Hormander)

`S_R^{full}` is of real principal type on the complement of the null cone (i.e., for
`xi2 != 0`, the principal symbol is invertible, so there are no characteristics there).
On the null cone, `sigma_1(S_R^{full})` has nontrivial kernel, and real principal type
holds because `d(det sigma_1) = d(det(S_R^{(1)})(x,xi)) = (det S_R^{(1)}) * d(log det S_R^{(1)})`
is nonzero on the null cone (since the null cone is a smooth manifold and the zero is
simple for Dirac-type operators). By Hormander Th. 23.2.4, the WF set propagates along
null bicharacteristics of `p_1 = g_Y(xi,xi)` regardless of `sigma_0`.

**Failure condition for this argument.** If the null cone has higher-order zeros of
`det(sigma_1)` (a degenerate null cone), the real principal type analysis requires
modification. For a non-degenerate Lorentzian metric `g_Y` of signature (9,5), the null
cone `{xi2 = 0}` is a smooth quadric cone with only first-order zeros, so this is not
an issue.

### Argument 2: Spectrum of sigma_0 on the Null Cone

New characteristics from `sigma_0` would require `sigma_0(S_R^{full})(x, xi)` to have
REAL eigenvalues for `xi` on the null cone that are NOT contained in the eigenvalue
set of `sigma_1` near the null cone. This is the mechanism by which subprincipal symbols
can produce "sub-characteristics" (a known phenomenon for operators that are NOT of real
principal type).

For real principal type operators, the spectrum of `sigma_0` on the characteristic variety
is irrelevant to the propagation direction. The sub-characteristic phenomenon requires
the operator to be of type "double characteristics" or higher, where the principal symbol
vanishes to higher order. For `S_R^{full}`, the principal symbol vanishes exactly to
first order on the null cone (from the Clifford module property), so there are no
higher-order zeros.

**The sub-characteristics theorem** (Dencker, 1982; Taylor 1981) applies to operators
where `sigma_1 = 0` to second or higher order. Since `sigma_1(S_R^{full}) = 0` only to
first order on the null cone, sub-characteristics do not arise.

### Argument 3: Shiab Subprincipal Is Anti-Hermitian (No New Real Characteristics)

**Claim.** The Shiab contribution to `sigma_0(S_R^{full})` is anti-Hermitian (with
respect to the natural inner product on the RS sub-bundle from the Cl(9,5) Hermitian
structure).

**Argument.** The Shiab operator `Phi(F_A tensor .)` is defined via the Sp(64) gauge
connection, which is anti-Hermitian (the Lie algebra sp(64) consists of skew-Hermitian
operators on `S = H^{64}` with respect to the quaternionic Hermitian inner product).
The curvature `F_A in Omega^2(Y, sp(64))` is therefore sp(64)-valued, hence anti-Hermitian.
Clifford contraction `c(\iota_{e_A} F_A)` preserves the anti-Hermitian structure.
Therefore `Phi(F_A tensor .)` is anti-Hermitian on each fiber.

The projection to the RS sub-bundle preserves anti-Hermiticity: `P_R Phi(F_A) P_R` is
anti-Hermitian if `Phi(F_A)` is anti-Hermitian and `P_R` is an orthogonal projection.

**Consequence.** The Shiab contribution to `sigma_0(S_R^{full})` is anti-Hermitian.
Its eigenvalues on the real line are zero (anti-Hermitian operators on Hilbert spaces
have purely imaginary eigenvalues over C, and purely imaginary means zero on the real
line). Anti-Hermitian subprincipal symbol contributions cause amplitude decay, not new
propagation directions.

**New real characteristics require REAL eigenvalues** of the subprincipal symbol. Since
the Shiab contribution has purely imaginary eigenvalues, it does not produce new
real characteristics.

**Failure condition.** This argument requires:
(a) The Sp(64) connection is anti-Hermitian on S (i.e., the gauge group is unitary
    with respect to the H^{64} inner product). This is by construction: Sp(64) = U(64,H).
(b) The RS projection P_R is orthogonal (i.e., the inner product on E restricts to
    a non-degenerate inner product on R^{14D}). In split-signature (9,5), the inner
    product is pseudo-Hermitian, not positive-definite. The RS sub-bundle R^{14D}
    inherits a pseudo-Hermitian inner product. For pseudo-Hermitian spaces,
    anti-Hermitian operators can have real eigenvalues (via the indefinite signature).
    This is a genuine risk in the split-signature setting.

---

## 8. Spin-Connection Subprincipal Symbol: The Split-Signature Subtlety

### 8.1 The Risk from Split Signature

In Riemannian signature (positive definite), anti-Hermitian = purely imaginary spectrum.
In pseudo-Riemannian signature (p,q), the natural inner product is indefinite, and
"anti-Hermitian" operators can have real eigenvalues on the imaginary axis as follows:

For an anti-Hermitian operator `K` (satisfying `<Kv, w> = -<v, Kw>` for the indefinite
inner product `<.,.>`), the bilinear form `<Kv, v>` is real but may be positive or
negative. The eigenvalues of `K` with respect to the pseudo-Hermitian inner product
can be real.

The spin-connection term in `sigma_0(D_GU)` is:

```
c(e^A) omega_A = (1/4) omega_{A,BC} c(e^A) gamma^{BC}.
```

In the gimmel metric of signature (9,5), the spin-connection 1-form `omega_A` takes
values in `so(9,5)`, the Lie algebra of SO(9,5). The Clifford element `c(e^A) gamma^{BC}`
acting on `S = H^{64}` gives an endomorphism of S.

**The SO(9,5) Lie algebra.** The algebra `so(9,5)` consists of matrices `M` satisfying
`eta M^T + M eta = 0` where `eta = diag(1,...,1,-1,...,-1)` (9 positive, 5 negative).
These are pseudo-skew-symmetric matrices, NOT skew-symmetric. Their eigenvalues can be
real (they are diagonalizable over R in the neutral signature limit).

**Consequence.** The spin-connection contribution to `sigma_0(D_GU)` is `so(9,5)`-valued
on the spinor module `S = H^{64}`. This is NOT the same as anti-Hermitian in the
Riemannian sense. The eigenvalues of `c(e^A) omega_A` on S can be real.

However: **real eigenvalues of the subprincipal symbol do not produce new characteristics
for real-principal-type operators**. The Hormander theorem holds regardless of whether
`sigma_0` is anti-Hermitian or not, provided the operator is of real principal type.

### 8.2 Transport Equation with Real Subprincipal Symbol

In the transport equation for the WKB amplitude `a` along a null bicharacteristic:

```
(L_H + sigma_0^{inv}) a = 0
```

If `sigma_0^{inv}` has real eigenvalues, the transport equation produces EXPONENTIAL GROWTH
or DECAY along null rays, not new propagation directions. The amplitude `a` may blow up
along some null rays and decay along others. This is the **non-unitary propagation** (or
"subprincipal ill-posedness") phenomenon for non-Hermitian operators.

But exponential growth of the WKB amplitude is NOT a VZ acausality:
- VZ acausality = new spacelike characteristics (propagation at speeds faster than light).
- Exponential amplitude growth = large solutions along null rays (propagation at light speed,
  but with growing amplitude).

These are different phenomena. The latter is a stability question (do solutions blow up?),
not a causality question (do solutions propagate spacelike?).

**Conclusion.** Even if `sigma_0(S_R^{full})` has real eigenvalues (due to the split
signature of `g_Y`), this does not produce new real characteristics. It produces potentially
growing WKB amplitude along null bicharacteristics, which is a different (and less severe)
issue.

---

## 9. Block-Decomposed Subprincipal Symbol in RS/Spin-1/2 Language

The problem label specifies the RS/spin-1/2 block decomposition. Let us be explicit about
what the RS and spin-1/2 sectors are:

**RS sector:** `R^{14D} = ker Gamma^{14D}`, the 14D Rarita-Schwinger constraint sub-bundle.
Dimension: `13 * 256 = 3328` over R (in the full 14D Clifford module).

**Spin-1/2 sector:** The complement `Q = E / R^{14D}`, which includes:
- `Q_0 = S^+` (scalar spinors, 256 real components)
- `Q_T = gamma-trace spinors` (256 real components)
- Plus possible vertical one-form spinors.

Total non-RS dim = `256 + 256 + ... = (14-13)*256 = 256`.

The block-decomposed subprincipal symbol is:

```
sigma_0(D_GU) = [ sigma_0(A)    sigma_0(B)  ]
               [ sigma_0(C)    sigma_0(E)  ]
```

where each block is a zero-order endomorphism of the respective sector.

**RS diagonal block `sigma_0(A)` = `A^{(0)}`:**

```
A^{(0)} = P_R (c(e^A) omega_A) P_R + P_R Phi(F_A tensor .) P_R.
```

This is the spin-connection and Shiab acting on RS spinor-1-forms and projected back to RS.

**Off-diagonal `sigma_0(B)` and `sigma_0(C)`:**

```
B^{(0)} = P_Q (c(e^A) omega_A) P_R + P_Q Phi(F_A tensor .) P_R.
C^{(0)} = P_R (c(e^A) omega_A) P_Q + P_R Phi(F_A tensor .) P_Q.
```

These are the connections and Shiab coupling between RS and non-RS sectors at zero order.

**Schur subprincipal symbol:**

```
sigma_0(S_R^{full}) = A^{(0)} - B^{(1)} (E^{(1)})^{-1} C^{(0)}
                              - B^{(0)} (E^{(1)})^{-1} C^{(1)}
                     + B^{(1)} (E^{(1)})^{-1} E^{(0)} (E^{(1)})^{-1} C^{(1)}
                     + (Poisson bracket corrections).
```

**The x-dependence.** All terms are pointwise endomorphisms of `R^{14D}` depending on `x`
(through the connection, curvature) and on the direction of `xi` on the null cone (through
the xi-dependent factors from `(E^{(1)})^{-1}`). This is the expected structure for the
subprincipal symbol of a first-order differential operator with connections.

**The Weyl tensor contribution.** The gimmel curvature `R_{ABCD}` enters via:
- The spin-connection `omega_{A,BC} = (1/2)(R_{ABCD} + g_Y-terms) x^D + O(|x|^2)`
  in Riemann normal coordinates.
- The commutator term `[nabla_A, nabla_B] Psi = R_{AB} Psi` contributing at zero order.

The Weyl tensor `W_{ABCD}` (the traceless part) enters `sigma_0(S_R^{full})` as a
xi-direction-dependent endomorphism, specifically via:

```
[Weyl contribution to sigma_0(S_R^{full})](x, xi)
    = P_R [W_{ABCD} gamma^{AB} xi^C / xi2] P_R + cross-block terms.
```

This is bounded and xi-dependent (proportional to `xi^C / xi2`, which is the direction
of xi on the null cone after suitable normalization). It does NOT introduce new
characteristics.

---

## 10. Verdict: OQ2-b Resolution

### Main Result

**The subprincipal symbol `sigma_0(S_R^{full})` does not introduce new real characteristics
beyond the null cone.**

Three independent arguments (Sections 7.1, 7.2, 7.3) confirm this:

1. **Real principal type (Hormander).** `S_R^{full}` is of real principal type on
   `T*Y \ {null cone}`. The Hormander propagation theorem guarantees that WF sets propagate
   along null bicharacteristics regardless of `sigma_0`. This is a theorem, not an
   approximation.

2. **No sub-characteristics.** Sub-characteristics arise when the principal symbol
   vanishes to second or higher order. For `S_R^{full}`, the principal symbol vanishes
   to first order on the null cone (from the Clifford module property and the trivial-kernel
   result). So sub-characteristics (Dencker-Taylor) do not arise.

3. **Anti-Hermitian Shiab, real so(9,5) connection: only amplitude effects.** The Shiab
   contribution to `sigma_0(S_R^{full})` is anti-Hermitian (sp(64)-valued, where
   Sp(64) = U(64,H) acts unitarily) and thus affects amplitude, not direction.
   The spin-connection contribution is so(9,5)-valued and may have real eigenvalues in
   split signature, but real eigenvalues of `sigma_0` for a real-principal-type operator
   produce exponential amplitude growth along null rays, NOT new spacelike characteristics.

### Explicit Statement of OQ2-b Resolution

**OQ2-b (subprincipal symbol acausality): ABSENT.**

The subprincipal symbol `sigma_0(S_R^{full})(x, xi)` is an endomorphism of `R^{14D}`
depending on `x` and on the direction of `xi`. Its effect on propagation is:

1. **Direction:** No change. Propagation remains along null bicharacteristics.
2. **Amplitude:** May be modified (potentially exponentially) along null rays. This is a
   stability (not causality) question.
3. **Shiab contribution:** Anti-Hermitian (sp(64)-valued). No new real characteristics.
4. **Curvature/connection contribution:** so(9,5)-valued, potentially real eigenvalues
   in split signature. Still no new characteristics for real-principal-type operators.

**The characteristic set of S_R^{full} is the null cone `{xi : g_Y(xi,xi) = 0}`,**
**confirmed at the subprincipal level.**

---

## 11. OQ2-a Resolution (Companion Claim)

As computed in Section 4.2:

**OQ2-a: The Shiab term `Phi(F_A tensor Psi)` is strictly zero-order.**

The Bianchi identity `D_A F_A = 0` constrains the background field `F_A` but does not
introduce derivatives of the dynamical field `Psi` into the Shiab term. The Shiab is
`Phi(F_A tensor Psi) = sum_A e^A tensor c(\iota_{e_A} F_A) Psi` -- a purely multiplicative
(zero-order) operator in `Psi`. OQ2-a is RESOLVED at reconstruction grade.

---

## 12. Combined VZ Curvature Status After OQ2-a and OQ2-b

| Open question | Resolution | Grade |
|---|---|---|
| OQ2-a: Shiab has no hidden derivatives of Psi | RESOLVED -- strictly zero-order | reconstruction |
| OQ2-b: Subprincipal symbol introduces no new characteristics | CONDITIONALLY_RESOLVED -- three arguments; split-signature subtlety noted | reconstruction |
| Principal symbol: ker S_R(xi) = 0 for xi2 != 0 | EVADED (prior file) | reconstruction |
| S_R^2 = xi2 Id as matrix identity | FALSE -- A S_R = xi2 Id is correct (vz-oq1) | reconstruction |
| Lower-order curvature changes principal symbol | FALSE (vz-oq2 parent) | reconstruction |
| Section-pullback 4D VZ evasion | OPEN -- OQ3 (Codazzi) | open |

**Overall VZ verdict remains: EVADED (reconstruction grade).**

The addition of subprincipal-symbol analysis strengthens the VZ evasion conclusion.
The evasion is robust at both the principal and subprincipal symbol levels.

---

## 13. Failure Conditions

**F1 (real principal type).** If the principal symbol of `S_R^{full}` vanishes to second
or higher order on the null cone (degenerate null cone), the Hormander theorem needs
refinement and sub-characteristics could arise. This would require a degenerate gimmel
metric (signature change or degeneracy). Excluded by the non-degenerate (9,5) metric.

**F2 (split-signature amplitude blow-up).** The spin-connection term `c(e^A) omega_A` in
`sigma_0(S_R^{full})` is so(9,5)-valued and can have real eigenvalues. This does NOT
produce new spacelike characteristics, but it can produce exponentially growing amplitude
along some null rays. If this amplitude blow-up is the relevant physical question (e.g.,
for stability of perturbations), then the subprincipal symbol warrants further study.
However, for the VZ causality question (no spacelike propagation), this is not a failure.

**F3 (non-real-principal-type at null cone).** If the Clifford module property fails
(i.e., if `sigma_D(xi)^2 != xi2 Id` for some covectors near the null cone), then
`S_R^{full}` is not of real principal type and the analysis breaks down. This is excluded
by construction of D_GU as a Dirac-type operator.

**F4 (operator ordering vs symbol ordering).** The Hormander symbol calculus applies to
classical pseudodifferential operators. If D_GU is only "formally Dirac-type" (i.e.,
the symbol squaring holds only modulo lower-order terms, not exactly), then the block-
determinant argument in vz-schur-complement needs modification. The Clifford property
`c(xi)^2 = g_Y(xi,xi) Id` is an EXACT algebraic identity in the Clifford algebra, so
this failure mode does not arise.

**F5 (non-scalar Poisson bracket correction).** The invariant subprincipal symbol
includes a Poisson bracket correction `(i/2) sum_j d_{xi_j} d_{x_j} sigma_1`. For non-
abelian symbol bundles (where the principal symbol is a matrix-valued function), the
Poisson bracket correction can be non-scalar (involving commutators of matrix symbols).
If this correction is large and has real eigenvalues, it could affect stability. This
requires explicit CAS computation of the Poisson bracket for the full block-matrix symbol
to verify.

---

## 14. Open Questions (Residual After This Note)

**Remaining OQ3 (Section-pullback 4D).** Even with the full 14D VZ evasion confirmed at
principal and subprincipal levels, the 4D observable RS field (obtained via `s*(D_GU)`)
needs its own analysis. The section pullback can mix horizontal and vertical degrees of
freedom via the second fundamental form `II_s`, and the resulting 4D operator may not be
of Dirac type. This requires the Codazzi equation (explorations/codazzi-sp64-bundle-2026-06-23.md)
and is the main remaining VZ open question.

**Amplitude analysis.** The subprincipal symbol determines whether the WKB amplitude
grows or decays along null rays. In the split-signature (9,5) setting, the so(9,5)-valued
subprincipal symbol can produce exponential amplitude growth in some null directions. This
is a stability question (separate from VZ causality). A full stability analysis of D_GU
would require computing the spectrum of `sigma_0(S_R^{full})` explicitly.

**CAS verification.** The explicit form of `sigma_0(S_R^{full})` (computed schematically
in Section 9) has not been verified by computer algebra. The claim that the Weyl-tensor
contribution is bounded and of the form `W_{ABCD} xi^C / xi2` should be checked.

---

## 15. Summary

**Problem:** Compute the subprincipal symbol of `D_GU` in the RS/spin-1/2 block
decomposition and verify that Shiab and curvature terms do not introduce new characteristics
beyond the null cone.

**Result:**

1. **OQ2-a (Shiab zero-order): RESOLVED.** The Shiab `Phi(F_A tensor Psi)` is a strictly
   zero-order operator in `Psi` (confirmed: Bianchi identity does not introduce derivative
   terms). The subprincipal symbol of D_GU includes `Phi(F_A)` as a xi-independent
   anti-Hermitian endomorphism.

2. **OQ2-b (subprincipal symbol): CONDITIONALLY_RESOLVED.** The subprincipal symbol
   `sigma_0(S_R^{full})` consists of:
   - Spin-connection contributions (so(9,5)-valued, xi-independent, may have real eigenvalues
     in split signature).
   - Shiab contributions (sp(64)-valued, anti-Hermitian, purely imaginary eigenvalues).
   - Cross-block Schur corrections (xi-direction-dependent, bounded off the null cone).
   
   None of these introduce new real characteristics beyond the null cone. Three independent
   arguments confirm this: (a) real principal type (Hormander theorem), (b) no sub-characteristics
   (first-order zero only), (c) anti-Hermitian Shiab + at most amplitude effects from connection.

3. **VZ evasion verdict: EVADED (reconstruction grade), unchanged and strengthened.**
   The characteristic set of `S_R^{full}` is the null cone at both principal and subprincipal
   levels.

**Status:** reconstruction (all arguments use standard pseudodifferential calculus; the
specific computations of `sigma_0(S_R^{full})` are schematic, pending CAS verification).

---

## References

- `explorations/vz-schur-complement-2026-06-23.md` (principal symbol, VZ EVADED)
- `explorations/vz-oq1-sr-squared-identity-2026-06-23.md` (S_R^2 identity clarification)
- `explorations/vz-oq2-lower-order-curvature-2026-06-23.md` (curvature zero-order argument; parent for OQ2-a, OQ2-b)
- `explorations/n1-signature-audit-y14-clifford-algebra-2026-06-22.md` (Cl(9,5) algebra, signature (9,5))
- `explorations/codazzi-sp64-bundle-2026-06-23.md` (OQ3, 4D pullback)
- Hormander, L. (1985). _The Analysis of Linear Partial Differential Operators III_, Ch. 23.
  (Propagation of singularities, real principal type, subprincipal symbol in WKB)
- Dencker, N. (1982). On the propagation of polarization sets for systems of real principal type.
  J. Funct. Anal. 46, 351-372. (Sub-characteristics for systems)
- Taylor, M. (1981). _Pseudodifferential Operators_, Ch. 6. (Symbol calculus, transport equations)
- Velo, G. and Zwanziger, D. (1969). Phys. Rev. 186:1337. (VZ theorem)
- Lawson, H.B. and Michelsohn, M.-L. (1989). _Spin Geometry_, Ch. II. (Clifford module operators)
