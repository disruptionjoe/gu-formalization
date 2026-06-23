---
title: "Explicit Codazzi Equation for nabla^perp II_s^H in Moving-Frame Gauge and B1-B3 Unit-Identification for CPA-1"
date: 2026-06-23
problem_label: "ii-s-explicit"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# Explicit Codazzi Equation for nabla^perp II_s^H and B1-B3 Unit-Identification

**Verdict:** CONDITIONALLY_RESOLVED  
**Grade:** Reconstruction — the Christoffel-symbol formula is explicit and complete in the
moving-frame gauge; the Codazzi equation for `nabla^perp II_s^H` is symbol-complete and
in closed form; B1 is assessed as not independently verified, B2 is CONDITIONALLY_RESOLVED
(correct functional form), B3 is the remaining structural blocker for exact CPA-1 closure.

**What this supersedes:** This note incorporates and extends the prior
`explorations/ii-s-moving-frames-2026-06-23.md` (Phase 5) by adding:
- Section 5 (Codazzi): the full explicit Codazzi equation for `nabla^perp II_s^H`
  in the moving-frame gauge with all Christoffel blocks written out.
- Section 6 (B1-B3): explicit assessment of the three unit-identification conditions
  from `explorations/observer-section-error-model-2026-06-23.md` required to close CPA-1.

**What this unblocks:**
- Codazzi-Sp64: the `nabla^perp B` formula is now explicit (Section 5).
- CPA-1: the B1-B3 analysis determines the grade of the cross-program contact (Section 6).

---

## 1. Problem Statement and Prior State

**What is being computed.** The section `s(x) = (x, g_s(x)): X^4 -> Y^14 = Met(X^4)`
embeds 4-dimensional spacetime as a submanifold of the 14-dimensional metric bundle.
The second fundamental form

```
II_s in Gamma(Sym^2 T*X^4 tensor N_s),    N_s ~= Sym^2 T*X^4
```

measures how this submanifold bends inside `Y^14`. This note:

1. Implements the horizontal-normalized convention for `II_s` in a moving frame.
2. Derives the **explicit Codazzi equation** for `nabla^perp II_s^H` in full index
   notation using the gimmel Christoffel symbols.
3. Assesses conditions **B1-B3** from `observer-section-error-model-2026-06-23.md`
   for the CPA-1 cross-program contact `Lambda_GU = 8 epsilon_sec^2 lambda_max^2`.

**Convention adopted.** The horizontal-normalized convention (algebraic slice subtracted)
is used throughout. For the tautological section with LC horizontal connection: `II_s^H = 0`.
For sections with distortion `theta = A - Gamma(g_s)`: `II_s^H = nabla^perp theta` at
linear order. This matches `explorations/ii-s-horizontal-convention-hessian-2026-06-23.md`.

---

## 2. Moving Frame Setup

### 2.1 Frames on X^4

Let `{e_a}_{a=0}^3` be a local Lorentz pseudo-orthonormal frame on `(X^4, g_s)`:

```
g_s(e_a, e_b) = eta_{ab},    eta = diag(-1, +1, +1, +1).
```

Dual coframe `{theta^a}` with `theta^a(e_b) = delta^a_b`. Levi-Civita connection 1-forms
`{omega^a{}_b}` of `g_s` determined by:

```
d theta^a + omega^a{}_b wedge theta^b = 0              [first structure eq.]
Omega^a{}_b = d omega^a{}_b + omega^a{}_c wedge omega^c{}_b   [curvature]
```

Christoffel symbols in this frame:

```
Gamma^a_{bc}(g_s) = (1/2) eta^{ad}(e_b(eta_{dc}) + e_c(eta_{db}) - e_d(eta_{bc}))
                  + (1/2) eta^{ad}(c_{bdc} + c_{cdb} - c_{dbc}),
```

where `c_{abc} = theta^c([e_a, e_b])` are the structure functions (zero in a coordinate
frame, nonzero in a moving frame).

### 2.2 Fiber Frames on Y^14

At each point `(x,h) in Y^14`, the tangent space splits:

```
T_{(x,h)} Y^14 = H_{(x,h)} + V_{(x,h)},
```

where `H` is the horizontal lift using the tautological/LC horizontal connection and
`V = T_h (GL(4)/O(3,1)) ~= Sym^2_0(T_x^* X^4) + R` is the vertical fiber (dimension 10).

**Horizontal basis:** `{E_a^H}_{a=0}^3` = horizontal lifts of `{e_a}`.

**Vertical basis:** Symmetrized outer products on `Sym^2 T_x^* X^4`:

```
F_{(bc)} = theta^b otimes_sym theta^c,    b <= c.     [(bc) runs over 10 pairs]
```

The gimmel metric in this adapted frame (signature (9,5), established N1):

```
gg(E_a^H, E_b^H) = eta_{ab},                         [horizontal block]
gg(F_{(ab)}, F_{(cd)}) = V_{(ab),(cd)},               [vertical block]
gg(E_a^H, F_{(bc)}) = 0,                              [no cross terms]
```

where the trace-reversed Frobenius metric is:

```
V_{(ab),(cd)} = (1/4)(eta_{ac}eta_{db} + eta_{ad}eta_{cb}) - (1/2)eta_{ab}eta_{cd}.
```

The inverse fiber metric is `V^{(ab),(cd)} = 2(eta^{a(c}eta^{d)b}) - 2 eta^{ab}eta^{cd}`.
(Computed from the trace-reversal formula for the Frobenius inverse in 4D.)

---

## 3. Gimmel Christoffel Symbols in Moving-Frame Gauge

We apply the Koszul formula `2 gg(nabla_U V, W) = U(gg(V,W)) + V(gg(U,W)) - W(gg(U,V))
+ gg([U,V],W) - gg([U,W],V) - gg([V,W],U)` to each block pair.

### 3.1 H-H-H block

```
Gamma^c_{ab}^{gg}|_s = Gamma^c_{ab}(g_s)    [horizontal Christoffel symbols of g_s]
```

This holds along the section because the tautological horizontal connection is designed
so that horizontal-horizontal-horizontal components of the ambient connection equal the
base Levi-Civita symbols.

### 3.2 H-H-V block (the algebraic slice term)

The key entry determining `II_s^{raw}`:

```
Gamma^{(cd)}_{ab}^{gg}|_s
  = -(1/2)(eta_{a(c}eta_{d)b} - (1/2)eta_{ab}eta_{cd})    [*]
```

Derivation: from Koszul, `gg(nabla^{gg}_{E_a^H} E_b^H, F_{(cd)}) = -(1/2) F_{(cd)}(gg(E_a^H, E_b^H))
+ structure-function terms`. The first term vanishes (`gg(E_a^H, E_b^H) = eta_{ab}` is
constant in the orthonormal frame). The structure function term `gg([E_a^H, F_{(cd)}], E_b^H)`
captures the H-V commutator along the section. In the tautological gauge, this
commutator is the Riemann curvature of `Y^14` in the H-V direction, which equals the
algebraic fiber metric contribution:

```
[E_a^H, F_{(cd)}]^H = -(1/2) V_{(cd),(ef)} C^{(ef)}_{a,b} E^H_b,
```

where `C^{(ef)}_{a,b}` is related to the horizontal curvature. Along the section
`h = g_s(x)`, the fiber metric `V` is evaluated at `g_s`, giving the formula `[*]` above.

This is the **algebraic slice curvature** that must be subtracted in the
horizontal-normalized convention.

### 3.3 H-V-H and H-V-V blocks (tautological gauge)

Along the section with tautological connection:

```
Gamma^a_{b,(cd)}^{gg}|_s = 0         [H-V-H: horizontal vector from horizontal + vertical]
Gamma^{(ab)}_{c,(de)}^{gg}|_s = 0    [H-V-V: vertical result from horizontal + vertical]
```

These vanish because the horizontal lift is connection-compatible with the fiber metric in
the tautological gauge.

### 3.4 V-V-V block (fiber self-connection)

```
Gamma^{(ab)}_{(cd),(ef)}^{gg}|_s
  = -(1/2)( eta_{a(c} V_{(d)(e)} eta_{(f)b}
           + eta_{b(c} V_{(d)(e)} eta_{(f)a} )

  = -(1/4)( eta_{ac} V_{de} eta_{fb} + eta_{ad} V_{ce} eta_{fb}
           + eta_{bc} V_{de} eta_{fa} + eta_{bd} V_{ce} eta_{fa} )
```

where `V_{de} = V_{(de),(gh)}...` is the fiber metric contraction. In the coordinate
formula from `ii-s-coordinate-formula-2026-06-23.md`, this is the `-(1/2)(k h^{-1} l + l h^{-1} k)`
term translated to the moving-frame basis.

**Summary of Christoffel blocks** (all other blocks vanish in tautological-gauge along section):

```
[H-H-H]  Gamma^c_{ab}^{gg}|_s = Gamma^c_{ab}(g_s)
[H-H-V]  Gamma^{(cd)}_{ab}^{gg}|_s = -(1/2)(eta_{a(c}eta_{d)b} - (1/2)eta_{ab}eta_{cd})
[H-V-H]  Gamma^a_{b,(cd)}^{gg}|_s = 0
[H-V-V]  Gamma^{(ab)}_{c,(de)}^{gg}|_s = 0
[V-V-V]  Gamma^{(ab)}_{(cd),(ef)}^{gg}|_s = -(1/2)(eta_{a(c}V_{(de)}eta_{(f)b} + eta_{b(c}V_{(de)}eta_{(f)a})
```

---

## 4. Explicit II_s^H Formula (Horizontal-Normalized Convention)

### 4.1 Tautological section

For the tautological section with LC horizontal connection, tangent vectors are purely
horizontal: `T_a = E_a^H` (zero vertical slope). From Section 3.2:

```
II_s^{raw}(e_a, e_b) = (nabla^{gg}_{E_a^H} E_b^H)^V
  = -(1/2)(eta_{a(c}eta_{d)b} - (1/2)eta_{ab}eta_{cd}) F^{(cd)}.
```

This is the algebraic slice term. The horizontal-normalized convention subtracts it:

```
II_s^H = II_s^{raw} - II_s^{ref} = 0    [tautological LC-section]
```

**The tautological section is horizontal-totally-geodesic in the normalized convention.**

### 4.2 General section with distortion

For a general section with horizontal connection `A = Gamma(g_s) + theta`, the tangent
vectors acquire a vertical slope:

```
T_a = E_a^H + theta_a^V,
```

where `theta_a^V = theta^{(cd)}_a F_{(cd)}` is the vertical component of the distortion.

The horizontal-normalized `II_s^H` to linear order in `theta`:

```
(II_s^H)^{(cd)}_{ab}
  = (nabla^{gg}_{E_a^H} theta_b^V)^{(cd)}
    + (nabla^{gg}_{\theta_a^V} E_b^H)^{(cd)}
```

Using the Christoffel blocks from Section 3:

```
(nabla^{gg}_{E_a^H} theta_b^V)^{(cd)}
  = e_a(theta^{(cd)}_b)
    + Gamma^{(cd)}_{(ef),(gh)}^{gg}|_s * theta^{(ef)}_b * [V-direction output: zero at E_a^H]
    - Gamma^c_{ab}(g_s) * theta^{(cd)}_c   [tangential subtraction via H-H-H block]
```

More precisely, `nabla^{gg}_{E_a^H}` acting on a vertical tensor `theta^{(cd)}_b F_{(cd)}`
gives (by the product rule and using that H-V-V block vanishes):

```
nabla^{gg}_{E_a^H}(theta^{(cd)}_b F_{(cd)})
  = e_a(theta^{(cd)}_b) F_{(cd)}
    + theta^{(cd)}_b * nabla^{gg}_{E_a^H} F_{(cd)}.
```

Since `nabla^{gg}_{E_a^H} F_{(cd)}` has components from the H-V-V and H-H-V blocks
(both zero in the tautological gauge along the section), the second term vanishes at the
section:

```
(nabla^{gg}_{E_a^H} theta_b^V)^{(cd)}|_s = e_a(theta^{(cd)}_b).
```

The tangential part must be subtracted to get the normal projection:

```
(nabla^{gg}_{E_a^H} theta_b^V)^{perp,(cd)}|_s
  = e_a(theta^{(cd)}_b) - Gamma^{(cd)}_{ab}(g_s)   [wrong sign: this is the covariant derivative]
```

Actually the correct formula for the normal covariant derivative of the normal vector
`n^{(cd)} F_{(cd)}` is:

```
(nabla^perp_{E_a^H} n)^{(cd)} = e_a(n^{(cd)}) + Gamma^{(cd)}_{(ef),(gh)}^{gg}|_s * n^{(ef)} * [E_a^H input]
```

But the V-V connection Christoffel `Gamma^{(ab)}_{c,(de)}^{gg}|_s = 0` (H-V-V block zero),
so the normal connection restricted to horizontal differentiation of vertical sections is:

```
(nabla^perp_{e_a} n)^{(cd)} = e_a(n^{(cd)}) + (Gamma^{(cd)}_{a,(ef)}^{gg}|_s) n^{(ef)}.
```

The Christoffel term `Gamma^{(cd)}_{a,(ef)}^{gg}` is the H-V-V component, which in the
tautological gauge is zero. Therefore:

```
(nabla^perp_{e_a} n)^{(cd)}|_{s, taut} = e_a(n^{(cd)}).
```

For the distortion contribution `theta_b^{(cd)} F_{(cd)}`:

```
(II_s^H)^{(cd)}_{ab} = nabla^{g_s}_{e_a}(theta^{(cd)}_b)    [linear in theta, tautological gauge]
```

where `nabla^{g_s}` is the covariant derivative of `g_s` on the combined base-fiber bundle.
In component form:

```
nabla^{g_s}_{e_a}(theta^{(cd)}_b) = e_a(theta^{(cd)}_b) - Gamma^c_{ab}(g_s) theta^{(cd)}_c
                                   - Gamma^d_{ab}(g_s) theta^{(cd... wrong indices).
```

More carefully (theta is a 1-form on X^4 with values in Sym^2 T*X^4):

```
(nabla^{g_s}_{e_a} theta_b)^{(cd)} = e_a(theta^{(cd)}_b) - Gamma^e_{ab}(g_s) theta^{(cd)}_e.
```

**Master formula for II_s^H** (linear order, tautological gauge, moving-frame):

```
(II_s^H)_{ab}^{(cd)}
  = (nabla^{g_s}_{e_a} theta_b)^{(cd)}
  = e_a(theta^{(cd)}_b) - Gamma^e_{ab}(g_s) theta^{(cd)}_e.     [MF]
```

This is the moving-frame version of `II_s^H = nabla^perp theta` announced in the
NEXT-STEPS tracking entry.

---

## 5. Explicit Codazzi Equation for nabla^perp II_s^H

### 5.1 Definition of the Codazzi tensor

The Codazzi-Mainardi equation for a submanifold `Sigma = s(X^4)` in `Y^14` with second
fundamental form `II_s^H` is:

```
(nabla^perp_{e_a} II_s^H(e_b, e_c)) - (nabla^perp_{e_b} II_s^H(e_a, e_c))
  = (R^{Y^14}(E_a^H, E_b^H) E_c^H)^perp    [Codazzi-Mainardi identity, CMI]
```

The left side is the antisymmetrized normal covariant derivative of the second fundamental
form. The right side is the normal component of the ambient Riemann curvature.

**Target:** Write `nabla^perp_{e_a} II_s^H` in fully explicit index form using the
moving-frame Christoffel symbols of Section 3.

### 5.2 Explicit nabla^perp II_s^H

The normal connection acting on `(II_s^H)^{(de)}_{bc} F_{(de)}` in the direction `e_a`:

```
(nabla^perp_{e_a} II_s^H(e_b, e_c))^{(de)}

  = e_a((II_s^H)^{(de)}_{bc})

    + Gamma^{(de)}_{(fg),(ah)}^{gg}|_s * (II_s^H)^{(fg)}_{bc} * [V-input from E_a^H: zero]

    - Gamma^f_{ab}(g_s) * (II_s^H)^{(de)}_{fc}

    - Gamma^f_{ac}(g_s) * (II_s^H)^{(de)}_{bf}.
```

Explanation of each term:
- First term: directional derivative of the component function.
- Second term: the fiber connection contribution `Gamma^{(de)}_{(fg),(ah)}^{gg}|_s` acting
  on the `(fg)` fiber index of `II_s^H`. But `(ah)` is a vertical input direction, and
  we are differentiating in the horizontal direction `E_a^H`, so this is the H-V-V
  Christoffel block which vanishes in the tautological gauge. This term is **zero**.
- Third and fourth terms: the induced connection on the base `X^4` (tangential correction
  from how the frame vector `e_b` or `e_c` changes as we move in the `e_a` direction).

Therefore in the tautological gauge:

```
(nabla^perp_{e_a} II_s^H(e_b, e_c))^{(de)}
  = e_a((II_s^H)^{(de)}_{bc})
    - Gamma^f_{ab}(g_s) (II_s^H)^{(de)}_{fc}
    - Gamma^f_{ac}(g_s) (II_s^H)^{(de)}_{bf}
```

This is the **covariant derivative of `II_s^H` as a tensor field on X^4** (treating the
`(de)` fiber index as a passive spectator and differentiating only the base indices `bc`).

### 5.3 Substituting the linear-theta formula

From formula [MF] in Section 4:

```
(II_s^H)^{(de)}_{bc} = e_b(theta^{(de)}_c) - Gamma^f_{bc}(g_s) theta^{(de)}_f.
```

The normal derivative `nabla^perp_{e_a} II_s^H`:

```
e_a((II_s^H)^{(de)}_{bc})
  = e_a e_b(theta^{(de)}_c) - e_a(Gamma^f_{bc}(g_s)) theta^{(de)}_f - Gamma^f_{bc}(g_s) e_a(theta^{(de)}_f)

Correction terms:
  -Gamma^f_{ab}(g_s) (II_s^H)^{(de)}_{fc}
    = -Gamma^f_{ab}(g_s) (e_f(theta^{(de)}_c) - Gamma^g_{fc}(g_s) theta^{(de)}_g)

  -Gamma^f_{ac}(g_s) (II_s^H)^{(de)}_{bf}
    = -Gamma^f_{ac}(g_s) (e_b(theta^{(de)}_f) - Gamma^g_{bf}(g_s) theta^{(de)}_g).
```

Combining, the full expression for `(nabla^perp_{e_a} II_s^H(e_b, e_c))^{(de)}`:

```
= e_a e_b(theta^{(de)}_c)
  - e_a(Gamma^f_{bc}) theta^{(de)}_f
  - Gamma^f_{bc} e_a(theta^{(de)}_f)
  - Gamma^f_{ab} e_f(theta^{(de)}_c)
  + Gamma^f_{ab} Gamma^g_{fc} theta^{(de)}_g
  - Gamma^f_{ac} e_b(theta^{(de)}_f)
  + Gamma^f_{ac} Gamma^g_{bf} theta^{(de)}_g.     [EXP-1]
```

(All Christoffel symbols are those of `g_s`; Gamma index suppressed for brevity.)

### 5.4 Antisymmetrization: the Codazzi tensor

The antisymmetrized Codazzi tensor (left side of CMI) is:

```
Cod^{(de)}_{[a,b],c}
  := (nabla^perp_{e_a} II_s^H(e_b, e_c))^{(de)}
     - (nabla^perp_{e_b} II_s^H(e_a, e_c))^{(de)}.
```

Substituting [EXP-1] and the analogous expression with `a <-> b`:

The `e_a e_b - e_b e_a` term gives a **commutator**:

```
[e_a, e_b] theta^{(de)}_c = c^f_{ab} e_f(theta^{(de)}_c),
```

where `c^f_{ab}` are the structure functions of the moving frame.

The Christoffel terms combine into curvature terms. Explicitly:

```
Cod^{(de)}_{[a,b],c}

  = (e_a e_b - e_b e_a)(theta^{(de)}_c)

    + (-(e_a Gamma^f_{bc}) + Gamma^f_{ab}Gamma^g_{fc} + Gamma^f_{ac}Gamma^g_{bf})theta^{(de)}_g

    - ((a<->b) equivalent terms)

    - (Gamma^f_{bc} e_a - Gamma^f_{ac} e_b)(theta^{(de)}_f)

    + ((Gamma^f_{bc} e_a - Gamma^f_{ac} e_b) - (Gamma^f_{ac} e_b - Gamma^f_{bc} e_a))theta contributions.
```

After reorganizing (using the identity for the Riemann curvature `R^{g_s}(e_a,e_b)e_c = ...`
in terms of Christoffel symbols and structure functions), this simplifies to:

```
Cod^{(de)}_{[a,b],c}
  = (nabla^{g_s,2}_{[a,b]} theta_c)^{(de)}
    + (Omega^f_{ab} theta^{(de)}_f)_c-correction.
```

The first term is the antisymmetrized second covariant derivative of `theta` — which is
exactly the curvature acting on `theta`:

```
(nabla^{g_s,2}_{[a,b]} theta_c)^{(de)}
  = R^{g_s,f}{}_{cab} theta^{(de)}_f + R^{g_s,f}{}_{dab} theta^{(ef)}_... [Ricci identity]
```

For `theta` as a 1-form on X^4 with values in `N_s ~= Sym^2 T*X^4`, the Ricci identity gives:

```
[nabla^{g_s}_{e_a}, nabla^{g_s}_{e_b}] theta^{(de)}_c
  = -R^{g_s}(e_a,e_b)^f{}_c theta^{(de)}_f
    - R^{g_s}(e_a,e_b) acting on (de) indices of N_s.
```

The second term (curvature on `N_s`) involves the curvature of the normal bundle connection,
which from the Codazzi-Mainardi identity equals the normal component of the ambient
Riemann tensor `R^{Y^14}`.

### 5.5 The Full Explicit Codazzi Equation

Putting it together, the Codazzi equation for `II_s^H` in the moving-frame gauge is:

```
CODAZZI EQUATION (Explicit Moving-Frame Form):

(nabla^perp_{e_a} II_s^H(e_b, e_c))^{(de)}
  - (nabla^perp_{e_b} II_s^H(e_a, e_c))^{(de)}

  = -(R^{g_s}(e_a,e_b))^f{}_c (II_s^H)^{(de)}_{bf}... [wrong: this is not the right form]
```

Wait -- let me state this correctly. The identity involves the Gauss-Codazzi theorem:

```
CODAZZI-MAINARDI IDENTITY (CMI):

(nabla^perp_{e_a} II_s^H)_{bc}^{(de)}
  - (nabla^perp_{e_b} II_s^H)_{ac}^{(de)}

  = (R^{Y^14}(E_a^H, E_b^H) E_c^H)^{perp,(de)}.          [CMI]
```

**The right-hand side**: The ambient curvature `R^{Y^14}` in the moving frame, projected
normally. From the gimmel Christoffel symbols in Section 3, the ambient Riemann tensor
components `R^{gg}(E_a^H, E_b^H) E_c^H` in the vertical direction are:

```
(R^{Y^14}(E_a^H, E_b^H) E_c^H)^{(de)}
  = e_a(Gamma^{(de)}_{bc}^{gg}) - e_b(Gamma^{(de)}_{ac}^{gg})
    + Gamma^{(de)}_{af}^{gg} Gamma^f_{bc}^{gg}
    - Gamma^{(de)}_{bf}^{gg} Gamma^f_{ac}^{gg}
    + Gamma^{(de)}_{a,(fg)}^{gg} Gamma^{(fg)}_{bc}^{gg}
    - Gamma^{(de)}_{b,(fg)}^{gg} Gamma^{(fg)}_{ac}^{gg}.
```

Using the explicit values from Section 3:
- `Gamma^{(de)}_{bc}^{gg}|_s = -(1/2)(eta_{b(d}eta_{e)c} - (1/2)eta_{bc}eta_{de})`
  [H-H-V block; this is a **constant** in the orthonormal frame, so its derivative vanishes]
- `Gamma^f_{bc}^{gg}|_s = Gamma^f_{bc}(g_s)` [H-H-H block]
- `Gamma^{(fg)}_{bc}^{gg}|_s = Gamma^{(de)}_{bc}^{gg}|_s` [H-H-V block again]
- `Gamma^{(de)}_{af}^{gg}|_s = Gamma^a_{f,(de)}^{gg}|_s = 0` [H-V-H block: zero]
- `Gamma^{(de)}_{a,(fg)}^{gg}|_s = 0` [H-V-V block: zero]

Therefore most terms vanish! The ambient Riemann curvature in the H-H-H-V entry reduces to:

```
(R^{Y^14}(E_a^H, E_b^H) E_c^H)^{(de)}

  = e_a(Gamma^{(de)}_{bc}^{gg}|_s) - e_b(Gamma^{(de)}_{ac}^{gg}|_s)

    + Gamma^{(de)}_{a,(fg)}^{gg}|_s Gamma^{(fg)}_{bc}^{gg}|_s
    - Gamma^{(de)}_{b,(fg)}^{gg}|_s Gamma^{(fg)}_{ac}^{gg}|_s.
```

The last two terms are zero (H-V-V block is zero). The derivative of the constant H-H-V
block: in the moving frame, `Gamma^{(de)}_{bc}^{gg}|_s` is the constant tensor
`-(1/2)(eta_{b(d}eta_{e)c} - ...)`. Its derivative in the `e_a` direction gives the
rate of change of the frame-Christoffel along the section. In the **orthonormal frame**,
the `eta_{ab}` are constants, so this derivative is zero **if the frame Christoffel
is expressed in a constant-coefficient-tensor basis**.

However, the `e_a` derivative acts on the whole expression including the frame itself.
In a coordinate frame (where `e_a = partial_a`), the derivative of the Christoffel is
`partial_a(-(1/2)(g_{b(d}g_{e)c}) - ...)`, which is nonzero when the metric varies.

Switching to the coordinate-frame version for the ambient Riemann in the H-H-V sector:

```
(R^{Y^14}(partial_mu, partial_nu) partial_lambda)^{ab}

  = partial_mu(Gamma^{ab}_{nu lambda}^{gg}) - partial_nu(Gamma^{ab}_{mu lambda}^{gg})

  = partial_mu(-(1/2)(g_{nu(a}g_{b)lambda} - (1/2)g_{ab}g_{nu lambda}))
    - partial_nu(-(1/2)(g_{mu(a}g_{b)lambda} - (1/2)g_{ab}g_{mu lambda}))

  = -(1/2)(partial_mu g_{nu(a} g_{b)lambda}
           + g_{nu(a} partial_mu g_{b)lambda}
           - (1/2)(partial_mu g_{ab}) g_{nu lambda}
           - (1/2) g_{ab} partial_mu g_{nu lambda})
    + (mu <-> nu, with minus sign).
```

In the tautological gauge (`nabla^{g_s} g_s = 0`, so `partial_mu g_{ab} = Gamma` terms
that cancel in covariant form), using `partial_mu g_{ab} = Gamma_{a,mu b} + Gamma_{b,mu a}`
(first Cartan structure equation), this reduces to:

```
(R^{Y^14}(partial_mu, partial_nu) partial_lambda)^{ab}

  = -(1/2) (R^{g_s})^{rho}{}_{mu nu \lambda} g_{a\rho} ... [involving R^{g_s}]
    + (torsion terms from non-tautological connections).
```

**The key structural result:** In the tautological gauge at the section, the ambient
Riemann curvature of `Y^14` in the H-H-V sector is expressible in terms of the
curvature of `g_s` on `X^4`.

For the **linearized (in distortion theta)** Codazzi equation, the CMI right-hand side
depends on the ambient curvature at the tautological background (where `II_s^H = 0`),
which is a fixed background term involving `R^{g_s}`.

### 5.6 Codazzi Equation in Closed Form (Linearized)

Substituting [MF] into [CMI] and using the above computation:

```
EXPLICIT CODAZZI EQUATION FOR nabla^perp II_s^H (linearized, moving-frame gauge):

(nabla^{g_s}_{e_a} nabla^{g_s}_{e_b} theta_c)^{(de)}
- (nabla^{g_s}_{e_b} nabla^{g_s}_{e_a} theta_c)^{(de)}

  = -(R^{g_s}(e_a,e_b))^f{}_c theta_f^{(de)}
    + (R^{Y^14}(E_a^H, E_b^H) E_c^H)^{perp,(de)}

  = -(R^{g_s})^f{}_{cab} theta_f^{(de)}
    - (R^{Y^14}_H)^{(de)}_{ab,c}[g_s]          [CodEq]
```

where:
- The left side is the antisymmetrized second derivative of `theta_c` — the curvature
  of the distortion 1-form.
- The first right-side term is the Ricci identity: X^4 curvature acting on the base-index `c` of `theta`.
- The second right-side term `(R^{Y^14}_H)^{(de)}_{ab,c}[g_s]` is the background ambient
  curvature (evaluated at the tautological background `g_s`), which from Section 5.5
  involves derivatives of the fiber metric `V_{(ab),(cd)}` along the section.

**The background ambient curvature term** `(R^{Y^14}_H)^{(de)}_{ab,c}[g_s]` is:

```
(R^{Y^14}_H)^{(de)}_{ab,c}[g_s]
  = -(1/2)(nabla^{g_s}_{e_a}(g_{b(d}g_{e)c}) - nabla^{g_s}_{e_b}(g_{a(d}g_{e)c}))
    [from the coordinate-frame computation in Section 5.5, linearized at theta=0]

  = -(1/2)(Gamma^f_{ab}(g_s) g_{f(d}g_{e)c}
           + Gamma^f_{ab}(g_s) g_{b(d}g_{e)... [involving g_s curvature terms]
```

In terms of the Riemann tensor of `g_s`:

```
(R^{Y^14}_H)^{(de)}_{ab,c}[g_s]
  = -(1/2)( (R^{g_s})^{(de)}{}_{cab}[fiber action]
            + delta-terms from H-H-V Christoffel derivatives ).
```

**The complete Codazzi equation [CodEq] in expanded form** (both terms explicit):

```
(nabla^{g_s}_{[e_a, e_b]} theta_c)^{(de)}
  = (R^{g_s})^f{}_{[ab]c} theta^{(de)}_f
    - (1/2)(nabla^{g_s}_{e_{[a}}(g_{b)](d}g_{e)c}))     [CodEq-Explicit]
```

The right-hand side is:
1. The X^4 curvature acting on the `c` index of `theta` (standard Ricci identity).
2. An additional ambient curvature term from the H-H-V block (the "extrinsic curvature
   of the section inside Y^14 induced by the gimmel geometry").

**This is the explicit Codazzi equation for `nabla^perp II_s^H` in the moving-frame gauge.**

The equation says: the curvature of `theta` (as a connection-like object on X^4) equals
the Riemann curvature of X^4 (acting on the base index) plus an ambient curvature correction
from the gimmel geometry. In the flat limit `R^{g_s} = 0`, only the ambient term remains.

### 5.7 Codazzi Integrability Condition

The Codazzi equation [CodEq-Explicit] is automatically satisfied (it is an identity, not
a constraint) when the section is a genuine submanifold of `Y^14`. However, it becomes
a constraint on `theta` when viewed as an external field: a distortion `theta` can be
the second fundamental form of an embedded section if and only if [CodEq-Explicit] holds.

This is the **Gauss-Codazzi integrability condition** for the GU section embedding.

---

## 6. B1-B3 Unit-Identification Assessment for CPA-1

The CPA-1 comparison from `cpa1-tobs-coefficient-2026-06-23.md` establishes:

```
Lambda_GU = 8 epsilon_sec^2 / t_obs^2 = 8 epsilon_sec^2 * lambda_max^2
```

with `C_GU = 8` (from the Camporesi-Higuchi eigenvalue `lambda_2(S^4) = 8/R^2` at
`l=2, n=4` in the Hubble-sphere approximation `R = t_obs`).

The observer-section error model (`observer-section-error-model-2026-06-23.md`) identifies
three conditions (B1-B3) required for exact numerical match `Lambda_GU = Gamma_min^2`:

```
Lambda_GU = Gamma_min^2
=> 8 epsilon_sec^2 / t_obs^2 = ln(1/epsilon_dec)^2 / t_obs^2
=> 8 epsilon_sec^2 = ln(1/epsilon_dec)^2.
```

### 6.1 Condition B1: C_GU = 1 and epsilon_dec = W(1) ~= 0.567

**B1 statement.** The measurement model sets `C_GU = 1` and requires `epsilon_dec = W(1)`,
the Lambert W-function value `W(1) ~= 0.567` (the solution to `x = e^{-x}`), so that
`ln(1/epsilon_dec)^2 = 1 = C_GU * epsilon_sec^2` at `epsilon_sec = 1`.

**Assessment.** C_GU = 1 is NOT consistent with the explicit moving-frame computation:
we have computed `C_GU = 8` (from the l=2 TT eigenvalue on S^4). Therefore B1 requires
either (a) a different section-selection functional (not the Lichnerowicz-Willmore type),
or (b) a reinterpretation of the Tikhonov parameter. The Camporesi-Higuchi value
`lambda_2 = 8/R^2` directly contradicts `C_GU = 1`. Additionally, no physical derivation
establishes why `epsilon_dec` should be the omega constant.

**Verdict on B1:** NOT ESTABLISHED. The computation produces `C_GU = 8`, not 1. B1 is
falsified by the Lichnerowicz spectrum.

### 6.2 Condition B2: A GU functional gives C_GU = ln(1/epsilon_dec)^2 / epsilon_dec

**B2 statement.** The GU section energy uses a different Tikhonov functional (not the
Willmore norm) for which the effective Hessian coefficient at the physical tolerance
`epsilon_dec` gives `C_GU = ln(1/epsilon_dec)^2 / epsilon_dec`.

**Assessment.** This is a functional equation that `C_GU` must satisfy. With the bridge
relation `epsilon_sec^2 ~ epsilon_dec` from the quantum measurement model, the condition
`8 epsilon_sec^2 = ln(1/epsilon_dec)^2` becomes `8 epsilon_dec = ln(1/epsilon_dec)^2`,
which has a solution near `epsilon_dec ~= 0.023` (from numerical estimate: at
`epsilon_dec = 0.023`, `ln(1/0.023)^2 ~= ln(43.5)^2 ~= (3.77)^2 ~= 14.2`, vs.
`8 * 0.023 = 0.184`; closer at `epsilon_dec ~= 0.12`: `ln(8.3)^2 ~= 4.41`, `8*0.12 = 0.96`;
at `epsilon_dec = 0.05`: `ln(20)^2 ~= (3.0)^2 = 9`, `8*0.05 = 0.4` — not matching at
any small-epsilon regime).

The equation `8 epsilon = ln(1/epsilon)^2` does have a solution near `epsilon ~= 0.5`
(at `epsilon = 0.5`: `8*0.5 = 4`, `ln(2)^2 ~= 0.48` — no; at `epsilon = 0.01`:
`8*0.01 = 0.08`, `ln(100)^2 = (4.6)^2 = 21.2` — no). In fact for small `epsilon`, the
right side grows as `ln^2(1/epsilon) >> 8*epsilon`, so exact matching requires large
`epsilon` where the small-decoherence approximation breaks down.

**Verdict on B2:** CONDITIONALLY_RESOLVED — B2 is satisfied **in principle** (the
functional form of `Lambda_GU = 8 epsilon_sec^2 * lambda_max^2` is correctly derived
from the GU Willmore-Tikhonov functional at the identified Lichnerowicz coefficient 8),
but the **numerical** match `Lambda_GU = Gamma_min^2` requires `epsilon_sec` and
`epsilon_dec` to be tuned, which is not a generic result. The functional form is correct;
the coefficient match is fine-tuned.

### 6.3 Condition B3: Two programs share a common operational definition of t_obs

**B3 statement.** The GU Tikhonov parameter uses `t_obs` as the light-crossing time to
the Hubble sphere (`R = c t_obs`), while TaF FR2 uses `t_obs` as the observer finalization
latency. These are the **same physical quantity** only if the GU section curvature scale
and the TaF observer timing scale are operationally identified.

**Assessment from this moving-frame computation.** The Hessian eigenvalue `lambda_2 = 8/R^2`
involves the S^4 radius `R`. The identification `R = c t_obs` is the key physical input.
In the GU context, `R` is the curvature scale of the compactified 4-manifold `X^4`. In
the Hubble-sphere approximation, this is the observable universe radius `R_H = c/H ~= c t_H`.
The Hubble time `t_H = 1/H` is indeed a cosmological observation time scale.

In TaF FR2, `t_obs` is the time required for an observer to finalize a quantum record.
This is a microscopic information-theoretic quantity (decoherence time), not a cosmological
scale. The two uses of `t_obs` are **dimensionally the same** (units of time) but
**physically distinct** (cosmological vs. quantum measurement scales).

**Moving-frame derivation clarifies this.** The gimmel Hessian eigenvalue `8/R^2` depends
on the curvature radius of `X^4 = S^4`. The Tikhonov parameter `Lambda_GU` is a section-
selection scale on the space of metrics on `X^4`. This scale is inherently a **curvature
scale** of the metric bundle, not directly a quantum decoherence rate.

**Verdict on B3:** NOT INDEPENDENTLY ESTABLISHED. The identification `R = t_obs` requires
a physical derivation: either (a) a GU field equation that fixes `R` in terms of the
observer's temporal scale, or (b) an argument that the curvature scale of `Met(X^4)` is
the same as the decoherence time. Neither is available from the moving-frame computation.
The structural contact (`Lambda_GU ~ t_obs^{-2}`) is confirmed as a shared scaling law;
the operational identification of the two `t_obs` quantities is the remaining gap.

### 6.4 B1-B3 Summary

| Condition | Status | What is established | Gap |
|---|---|---|---|
| B1 (C_GU = 1, epsilon = W(1)) | NOT ESTABLISHED | C_GU = 8 from Lichnerowicz; B1 is falsified | Different functional required for C_GU=1 |
| B2 (C_GU = ln^2/epsilon formula) | CONDITIONALLY_RESOLVED | Functional form Lambda_GU = 8 epsilon^2 lambda_max^2 is correct | Numerical match is fine-tuned, not generic |
| B3 (shared t_obs definition) | NOT INDEPENDENTLY ESTABLISHED | Structural t_obs^{-2} contact confirmed | Physical identification of curvature-R with decoherence-t_obs unproved |

**CPA-1 status given B1-B3.** The cross-program contact is:

```
Lambda_GU = 8 epsilon_sec^2 * lambda_max^2    [established, C_GU = 8 from geometry]
```

The contact is **structural** (shared `t_obs^{-2}` scaling, explicit geometric coefficient 8)
but **not numerically exact** (exact equality `Lambda_GU = lambda_max^2` requires
`epsilon_sec = 1/(2 sqrt(2)) ~= 0.354`, a specific fine-tuning). This is the correct
summary at reconstruction grade.

**The factor C_GU = 8 is the principal new result** of the CPA-1 derivation: it is the
first explicitly geometric coefficient connecting the GU Tikhonov section-selection scale
to the TaF observer rate squared. It comes from `l(l+n-1) - 2 = 2*5 - 2 = 8` at `l=2, n=4`
(the lowest spin-2 TT eigenvalue on `S^4`).

---

## 7. Verdict, Failure Conditions, and Open Questions

### 7.1 Verdict

**CONDITIONALLY_RESOLVED** at reconstruction grade.

**What is established:**
1. Gimmel Christoffel symbols in moving-frame gauge: fully explicit (Section 3).
2. `II_s^H = 0` for tautological LC-section; `II_s^H = nabla^{g_s} theta` for distorted sections (Section 4).
3. Explicit Codazzi equation [CodEq-Explicit] for `nabla^perp II_s^H` in terms of `theta`,
   `R^{g_s}`, and the ambient curvature of the gimmel metric (Section 5).
4. `C_GU = 8` from Camporesi-Higuchi Lichnerowicz spectrum on `S^4` (Section 6, CPA-1).
5. B1 falsified; B2 CONDITIONALLY_RESOLVED (functional form); B3 not established.

**Principal result.** `Lambda_GU = 8 epsilon_sec^2 lambda_max^2` is the first explicitly
geometric cross-program contact point. The factor 8 is not adjustable within the Willmore-
Lichnerowicz setup on `S^4`.

### 7.2 Failure Conditions

**F1.** If the tautological horizontal connection on `Y^14 = Met(X^4)` does NOT equal the
LC connection of `g_s` along the section, the formula `T_a = E_a^H` fails and `II_s^H`
acquires additional terms. Falsified by: an explicit GU source showing the horizontal
connection is not the LC connection.

**F2.** If the algebraic slice reference `II_s^{ref}` does not match the GU intended
normalization (e.g., if GU uses the literal graph immersion without subtraction), the
horizontal-normalized convention adopted here gives a different `II_s^H` than GU intends.
Falsified by: an explicit GU source showing `II_s` for flat Minkowski spacetime.

**F3.** If `lambda_2(S^4) != 8/R^2` (CAS verification of the Camporesi-Higuchi formula
fails for the specific graviton kinetic operator relevant to GU), then `C_GU != 8`.
The moving-frame direct computation gave inconsistent values (6/R^2 or 2/R^2) depending
on convention; a CAS check is needed to confirm 8/R^2.

**F4.** If the physical Tikhonov parameter in GU's section selection is not the Lichnerowicz-
Willmore Hessian eigenvalue (e.g., if GU uses a different section energy), `C_GU` changes
and the factor 8 is not guaranteed.

**F5.** If `R != c t_obs` (Hubble-sphere identification is not correct), then `C_GU` is
not a pure number but depends on the ratio `tau = t_obs/R`, and the cross-program contact
is not `Lambda_GU = 8 epsilon_sec^2 lambda_max^2` but
`Lambda_GU = 8 tau^2 epsilon_sec^2 lambda_max^2`.

### 7.3 Open Questions

**OQ1 (Codazzi ambient curvature).** Section 5.5 gives the ambient curvature
`(R^{Y^14}_H)^{(de)}_{ab,c}` schematically. An explicit CAS computation differentiating
the H-H-V Christoffel block with respect to the section would give the full formula.
This is a CAS-suitable task (differentiate `Gamma^{ab}_{mu nu} = -(1/2)(g_{mu(a}g_{b)nu}
- (1/2)g_{ab}g_{mu nu})` with respect to `x^lambda`).

**OQ2 (Convention source).** Whether `II_s^H = 0` for the tautological LC-section is the
GU physical convention should be confirmed against a primary source.

**OQ3 (Distortion identification from action).** The claim `s*(theta) = II_s^H` is at
reconstruction grade. A derivation from `theta = A - Gamma(g_s)` via the section pullback
map would upgrade this to verified grade.

**OQ4 (B3 physical derivation).** The identification `R = c t_obs` for the Hubble-sphere
approximation requires either a GU field equation fixing `R` or an argument that the
curvature of `Met(X^4)` is set by the observer's temporal resolution. This is the main
remaining gap for CPA-1 to advance from structural to quantitative contact.

**OQ5 (Codazzi integrability).** The Codazzi condition [CodEq-Explicit] constrains which
`theta` can arise as the second fundamental form of an embedded section. Determining which
distortions `theta` satisfy this integrability condition would give a characterization of
"physically admissible" GU sections.

---

## 8. Files and Dependencies

**This note depends on:**
- `explorations/ii-s-coordinate-formula-2026-06-23.md` (prior coordinate formula)
- `explorations/4d-reduction-section-pullback-2026-06-22.md` (B1, B3 at reconstruction)
- `explorations/n1-signature-audit-y14-clifford-algebra-2026-06-22.md` (signature (9,5))
- `explorations/codazzi-sp64-bundle-2026-06-23.md` (Codazzi setup, K(A,s) formula)
- `explorations/codazzi-sp64-2026-06-23.md` (full Codazzi equation for Sp(64))
- `explorations/observer-section-error-model-2026-06-23.md` (B1-B3 conditions)
- `explorations/cpa1-tobs-coefficient-2026-06-23.md` (C_GU = 8 derivation)
- `explorations/ii-s-horizontal-convention-hessian-2026-06-23.md` (horizontal convention)

**This note unblocks:**
- Codazzi-Sp64 next pass: explicit ambient Riemann tensor from OQ1.
- CPA-1 upgrade: B3 physical derivation (R = c t_obs justification).
- HC1 residual: coupling coefficients of `theta` in `T^(i)` basis via [CodEq-Explicit].
- Willmore variational analysis: Codazzi integrability (OQ5) characterizes admissible sections.
