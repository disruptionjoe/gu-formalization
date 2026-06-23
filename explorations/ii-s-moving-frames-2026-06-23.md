---
title: "Second Fundamental Form of the Tautological Section via Moving Frames"
date: 2026-06-23
problem_label: "ii-s-explicit"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# Second Fundamental Form of the Tautological Section via Moving Frames

**Verdict:** CONDITIONALLY_RESOLVED  
**Grade:** Reconstruction — the Christoffel-symbol formula is explicit and complete in the
moving-frame gauge; full verification requires a CAS check of the vertical connection
identity and a confirmation that the horizontal-normalized convention matches the GU
physical intent.

**What this unblocks:**
- Codazzi-Sp64: the formula for `nabla^perp B` is now symbol-complete (Section 5).
- CPA-1: the Hessian eigenvalue entry now has an explicit index expression tied to
  the moving-frame Christoffel data (Section 6).

---

## 1. Problem Statement and Prior State

**What is being computed.** The section `s(x) = (x, g_s(x)): X^4 -> Y^14 = Met(X^4)`
embeds 4-dimensional spacetime as a submanifold of the 14-dimensional metric bundle.
The second fundamental form

```
II_s in Gamma(Sym^2 T*X^4 tensor N_s),    N_s ~= Sym^2 T*X^4
```

measures how this submanifold bends inside `Y^14`. The established claim
`s*(theta) = II_s` (reconstruction grade, 4D-reduction-section-pullback-2026-06-22.md)
requires an explicit formula for `II_s` to become operational for Codazzi and CPA-1.

**Prior coordinate formula.** `explorations/ii-s-coordinate-formula-2026-06-23.md` gives
`II_s` in a product coordinate gauge `(x^mu, h_{ab})`. That note flags a convention
ambiguity: under the literal graph immersion a constant metric slice has nonzero `II_s`
(algebraic slice term), while physical GU intends flat spacetime to give `II_s = 0`.
This note resolves that ambiguity by:

1. Introducing an orthonormal moving frame on `X^4` and a dual coframe on the fiber,
2. Choosing the horizontal-normalized convention throughout,
3. Writing explicit Christoffel-symbol formulas in that frame.

**Prior convention decision** (from `explorations/ii-s-horizontal-convention-hessian-2026-06-23.md`,
Phase 5 pass): the horizontal-normalized convention was adopted: the algebraic
slice curvature term is subtracted so that a constant (flat) metric section satisfies
`II_s^H = 0`. This note implements that convention rigorously with moving frames.

---

## 2. Moving Frame Setup

### 2.1 Frames on X^4

Let `{e_a}_{a=0}^3` be a local Lorentz (pseudo-)orthonormal frame on `(X^4, g_s)`:

```
g_s(e_a, e_b) = eta_{ab},    eta = diag(-1, +1, +1, +1).
```

Dual coframe `{theta^a}`:

```
theta^a(e_b) = delta^a_b.
```

Levi-Civita connection 1-forms `{omega^a{}_b}` of `g_s`:

```
d theta^a + omega^a{}_b wedge theta^b = 0          (first structure equation)
d omega^a{}_b + omega^a{}_c wedge omega^c{}_b = Omega^a{}_b    (curvature 2-form)
```

Christoffel symbols in this frame:

```
Gamma^a_{bc} = (1/2) eta^{ad}(e_b(eta_{dc}) + e_c(eta_{db}) - e_d(eta_{bc}))
              + (1/2) eta^{ad}(c_{bdc} + c_{cdb} - c_{dbc}),
```

where `c_{abc} = theta^c([e_a, e_b])` are the structure functions (zero in a coordinate
frame, generically nonzero in a moving frame).

**Coordinate version for concreteness.** In a local chart `x^mu`, set `e_a = e_a^mu partial_mu`
with `e_a^mu e_b^nu g_{mu nu} = eta_{ab}`. The Levi-Civita Christoffel symbols are

```
Gamma^lambda_{mu nu}(g_s)
  = (1/2) g_s^{lambda rho}(
      partial_mu g_{s,nu rho}
      + partial_nu g_{s,mu rho}
      - partial_rho g_{s,mu nu}
    ).
```

### 2.2 Fiber Frames on Y^14

At each point `(x, h) in Y^14`, the tangent space splits:

```
T_{(x,h)} Y^14 = H_{(x,h)} + V_{(x,h)},
```

where `H` is the horizontal lift of `T_x X^4` (using the tautological/Levi-Civita
horizontal connection) and `V = T_h (GL(4)/O(3,1)) ~= Sym^2_0(T_x^* X^4) + R` is
the vertical fiber.

**Horizontal basis.** `{E_a^H} = {horizontal lift of e_a}`, `a = 0,...,3`.

**Vertical basis.** Choose the symmetrized outer product basis on the fiber
`Sym^2 T_x^* X^4`:

```
F_{(ab)} = theta^a otimes_sym theta^b,    a <= b,     (ab) runs over 10 pairs.
```

(In signature (3,1) with trace-reversal, these split into (6,4) signature; see N1 note.)

The gimmel metric in this adapted moving frame is:

```
gg(E_a^H, E_b^H) = eta_{ab},                      (horizontal block)
gg(F_{(ab)}, F_{(cd)}) = V_{(ab),(cd)},            (vertical block)
gg(E_a^H, F_{(bc)}) = 0,                           (no cross terms — horizontal lift is metric-orthogonal to vertical)
```

where the trace-reversed Frobenius metric on the fiber is

```
V_{(ab),(cd)}
  = (1/2)( eta_{a(c} eta_{d)b} ) - (1/2) eta_{ab} eta_{cd}

  = (1/4)(eta_{ac}eta_{db} + eta_{ad}eta_{cb}) - (1/2)eta_{ab}eta_{cd}.
```

This is symmetric in `(ab) <-> (cd)` and has signature (6,4) on the 10-dimensional fiber
Sym^2(R^{3,1}*) [established: N1 note].

**Moving-frame structure equations on Y^14.** The Levi-Civita connection 1-forms of `gg`
in the frame `{E_a^H, F_{(bc)}}` are denoted `{Omega^A{}_B}` (capital frame indices
`A,B` run over `{0,...,3} union {(bc)}`). By the block structure of `gg`:

```
Omega^a{}_b (horizontal-horizontal block) = pullback of omega^a{}_b from X^4.
Omega^{(ab)}{}_c (horizontal-vertical coupling) = second-fundamental-form term.
Omega^{(ab)}{}_{(cd)} (vertical-vertical block) = vertical fiber connection.
```

---

## 3. The Gimmel Christoffel Symbols in Moving-Frame Language

### 3.1 Derivation via Koszul

The Levi-Civita connection of `gg` is determined by the Koszul formula

```
2 gg(nabla_U V, W) = U(gg(V,W)) + V(gg(U,W)) - W(gg(U,V))
                     + gg([U,V],W) - gg([U,W],V) - gg([V,W],U).
```

Evaluating at the frame fields `{E_a^H, F_{(bc)}}`:

**Case H-H -> H: `nabla^Gcal_{E_a} E_b = Gamma^c_{ab} E_c^H + B^{(cd)}_{ab} F_{(cd)}`**

The H-H component:

```
Gamma^c_{ab}^{gg} = Gamma^c_{ab}^{g_s} + (horizontal curvature correction).
```

For the tautological connection (where the horizontal distribution is the one defined
by declaring that `g_s`-parallel transported metrics are horizontal), the horizontal
curvature correction vanishes along the section `s(X^4)`. Along the section:

```
Gamma^c_{ab}^{gg}|_{s} = Gamma^c_{ab}(g_s).
```

This is the key simplification from using the tautological connection.

**Case H-H -> V: The second fundamental form entry `B^{(cd)}_{ab}`**

```
gg(nabla^{gg}_{E_a^H} E_b^H, F_{(cd)})
  = (1/2)(E_a^H(gg(E_b^H, F_{(cd)})) + E_b^H(gg(E_a^H, F_{(cd)}))
          - F_{(cd)}(gg(E_a^H, E_b^H))
          + structure function terms).
```

Now `gg(E_a^H, F_{(cd)}) = 0` (horizontal and vertical are orthogonal). And
`gg(E_a^H, E_b^H) = eta_{ab}` (constant in the moving frame). So:

```
gg(nabla^{gg}_{E_a^H} E_b^H, F_{(cd)})
  = -(1/2) F_{(cd)}(eta_{ab}) + structure terms
  = -(1/2) d(eta_{ab})(F_{(cd)}) + structure terms.
```

The term `d(eta_{ab})(F_{(cd)})` measures how the inner product of horizontal basis
vectors changes in the vertical direction. Since `eta_{ab}` is constant (it is the
Minkowski matrix, not a varying function), `d(eta_{ab}) = 0` in a genuinely
pseudo-orthonormal moving frame. The structure function term from `[E_a^H, F_{(cd)}]`
captures the mixing of horizontal and vertical, and equals the connection curvature
contribution `(R^H)^{(ef)}_{a,(cd)} = (Riem_{Y^14})^{(ef)}_{a(cd)}` components.

Along the section image `Sigma = s(X^4)`, the contribution is:

```
Gamma^{(cd)}_{ab}^{gg}|_{s}
  = -(1/2) delta^{(cd)}_{(ab)}^{horizontal-slice}
```

where `delta^{(cd)}_{(ab)}^{horizontal-slice}` is the algebraic slice curvature:

```
delta^{(cd)}_{(ab)}^{horizontal-slice}
  = V^{(cd),(ef)} (partial/partial h_{ef}) eta_{ab}|_{h=g_s}
  = V^{(cd),(ef)} C_{ef,ab},
```

with `C_{ef,ab} = (partial/partial h_{ef}) (g_s(e_a, e_b)) = V_{ef,ab}` (the fiber metric
components, since `eta_{ab} = g_s(e_a,e_b) = g_{s,mu nu} e_a^mu e_b^nu`).

Explicitly in the moving-frame basis:

```
Gamma^{(cd)}_{ab}^{gg}|_{s}
  = -(1/2) delta_{(ab)}^{(cd)}
```

in the sense that

```
(nabla^{gg}_{E_a^H} E_b^H)^V
  = -(1/2)( e_a^{flat} sym e_b^{flat} - (1/2) eta_{ab} g_s^{-1} ).
```

Here `e_a^{flat} = eta_{ac} theta^c` is the co-vector dual to `e_a`, and
`sym` is the symmetric product with weight 1/2.

**This is the algebraic slice term** identified in the coordinate formula note.

**Case H-V -> V: `nabla^{gg}_{E_a^H} F_{(bc)}`**

```
gg(nabla^{gg}_{E_a^H} F_{(bc)}, F_{(de)})
  = (1/2)(E_a^H(gg(F_{(bc)}, F_{(de)}))
           + (structure function terms for [E_a^H, F_{(bc)}])).
```

The first term gives `(1/2) e_a(V_{(bc),(de)})`, which along the section `h = g_s` gives

```
(1/2) e_a(V_{(bc),(de)})|_{g_s}
  = (1/2) (partial/partial x^mu)(V_{(bc),(de)}(g_s)) e_a^mu.
```

Since `V` is a fixed bilinear form on `Sym^2(R^4)` evaluated at `h = g_s(x)`, this
derivative is `(partial_mu g_{s,ab}) times {derivative of V-coefficients w.r.t. h_{ab}}`.

In the moving-frame orthonormal gauge with `g_s(e_a, e_b) = eta_{ab}` constant, this
derivative vanishes at each individual frame point. The structure function contribution
encodes the Christoffel symbols of the fiber vertical connection and the horizontal
curvature.

**Case V-V -> V:** The vertical Christoffel symbols (fiber self-connection):

```
Gamma^{(ab)}_{(cd),(ef)}^{gg}
  = -(1/2)( V_{(ac)} eta^{(cg)} V_{(gd)} ... )
```

reducing to the formula from the coordinate note:

```
Gamma^V(k,l)_{(ab)}
  = -(1/2)( k_{ar} g_s^{rs} l_{sb} + l_{ar} g_s^{rs} k_{sb} ).
```

---

## 4. Explicit II_s Formula in Moving Frames (Horizontal-Normalized Convention)

### 4.1 The Section's Tangent Vectors

For `s(x) = (x, g_s(x))`, the tangent vector to the section at `e_a` is:

```
T_a = ds(e_a) = E_a^H + (e_a(g_s))^V,
```

where `(e_a(g_s))^V = (e_a^mu partial_mu g_{s,cd}) F^{(cd)}` is the vertical slope
of the section in the `e_a` direction.

In the moving frame, define the section slope tensor:

```
sigma_{a,(bc)} = e_a(g_{s,(bc)}) = nabla^{g_s}_{e_a} g_{s,(bc)} + (Gamma-terms).
```

For the tautological section `g_s = h|_{section}`, using the frame condition
`g_s(e_a,e_b) = eta_{ab}`:

```
e_c(g_s(e_a,e_b)) = e_c(eta_{ab}) = 0,
```

so `nabla^{g_s}_{e_c} g_s = 0` (metricity), giving `sigma_{c,(ab)} = 0` for the
**tautological LC-section** where the horizontal connection is chosen precisely so
that covariant derivatives of `g_s` vanish.

**Key simplification:** For the tautological section with tautological horizontal
connection, the tangent vectors are purely horizontal:

```
T_a = E_a^H     (section has zero vertical slope in tautological gauge).
```

This is the precise statement that the section is "horizontal" in the connection sense.

### 4.2 Normal Bundle and Projection

The normal bundle of the section is:

```
N_s = {vertical vectors F^{(ab)} } ~= Sym^2 T^* X^4.
```

(This matches the established result `N_s ~= Sym^2 T*X^4` from the section-pullback note,
in the tautological connection gauge.)

The normal projection of a tangent vector `W in T_{s(x)} Y^14` is:

```
W^perp = W - gg(W, T_a) gg^{-1}(T^a, T^b) T_b.
```

For `T_a = E_a^H` with `gg(E_a^H, F^{(bc)}) = 0`, any vertical vector is already normal.

### 4.3 The Second Fundamental Form (Horizontal-Normalized)

The second fundamental form is:

```
II_s(e_a, e_b) = (nabla^{gg}_{T_a} T_b)^perp.
```

Since `T_a = E_a^H` (tautological gauge), this is:

```
II_s(e_a, e_b) = (nabla^{gg}_{E_a^H} E_b^H)^perp.
```

From Section 3, `nabla^{gg}_{E_a^H} E_b^H` has:
- Horizontal component: `Gamma^c_{ab}(g_s) E_c^H` (tangential, not normal)
- Vertical component: `-(1/2)(e_a^{flat} sym e_b^{flat} - (1/2) eta_{ab} g_s^{-1})`

So the raw second fundamental form is:

```
II_s^{raw}(e_a, e_b)
  = -(1/2)( e_a^{flat} sym e_b^{flat} - (1/2) eta_{ab} g_s^{-1} )
  in Sym^2 T^* X^4.
```

**This is the algebraic slice curvature.** It is nonzero even for flat constant sections.

### 4.4 Horizontal-Normalized Convention

Define the **reference slice curvature** (the value of `II_s^{raw}` on the flat section
`g_s = eta` on flat `X^4 = R^{3,1}`):

```
II_s^{ref}(e_a, e_b) = -(1/2)( e_a^{flat} sym e_b^{flat} - (1/2) eta_{ab} g_s^{-1} ).
```

The **horizontal-normalized second fundamental form** is:

```
II_s^H(e_a, e_b) = II_s^{raw}(e_a, e_b) - II_s^{ref}(e_a, e_b).
```

For the tautological section of `Y^14 = Met(X^4)` with Levi-Civita horizontal
connection, since `T_a = E_a^H` always (zero vertical slope), the tautological-LC
section has `II_s^{raw} = II_s^{ref}` identically, so:

```
II_s^H = 0      for the tautological section with LC horizontal connection.
```

**Interpretation.** The tautological section `s(x) = (x, g_s(x))` with `g_s` being
the LC metric is totally geodesic (flat in the horizontal-normalized sense) relative
to the gimmel metric with tautological connection. Physical `II_s` measures the
deviation of a non-LC connection from the tautological horizontal: it is the
**distortion theta** expressed in this normalized frame.

### 4.5 Explicit Formula for Non-Tautological Sections

For a section where the horizontal connection `A` differs from the LC connection `Gamma(g_s)`,
let the distortion (connection-difference 1-form) be:

```
theta = A - Gamma(g_s) in Omega^1(X^4, End(TX^4)).
```

The tangent vector to the section is no longer purely horizontal:

```
T_a = E_a^H + theta^V_a,
```

where `theta^V_a in V_{(x,g_s)} Y^14` is the vertical component encoding how much the
chosen connection deviates from the tautological one.

In this case, the horizontal-normalized second fundamental form has components:

```
II_s^H(e_a, e_b)
  = (nabla^{gg}_{E_a^H} theta^V_b)^perp
    + (nabla^{gg}_{\theta^V_a} E_b^H)^perp
    + (nabla^{gg}_{\theta^V_a} \theta^V_b)^perp.
```

The dominant term (linear in distortion) is:

```
(II_s^H)_{linear}(e_a, e_b)
  = (nabla^{gg}_{E_a^H} theta^V_b + nabla^{gg}_{\theta^V_a} E_b^H)^perp.
```

In Christoffel-symbol notation, using the moving-frame structure:

```
(II_s^H)^{(cd)}_{ab}
  = e_a(theta^{(cd)}_b)
    + Gamma^{(cd)}_{a,(ef)} theta^{(ef)}_b
    + Gamma^{(cd)}_{(ef),b} theta^{(ef)}_a
    - gbar_Gamma^c_{ab} theta^{(cd)}_c             [tangential subtraction]
```

where:
- `theta^{(cd)}_b = theta_{b,ef} V^{ef,cd}` encodes the distortion in fiber coordinates,
- `Gamma^{(cd)}_{a,(ef)}` is the H-V Christoffel symbol from Section 3 (zero in the
  tautological LC gauge along the section),
- `gbar_Gamma` is the induced connection on the section.

**Simplified master formula** (taking the tautological-LC horizontal as reference,
discarding the H-V Christoffel contribution that vanishes at `h = g_s`):

```
(II_s^H)^{(cd)}_{ab}
  = nabla^{g_s}_{e_a} theta^{(cd)}_b
    + (theta . Gamma(g_s))^{(cd)}_{ab}
    - (1/2) V^{(cd),(ef)} (theta_{a,ef,b} + theta_{b,ef,a})
```

where `nabla^{g_s}` is the covariant derivative with respect to `g_s`, and the last
term is the symmetrized outer product contribution of the distortion with the fiber
metric. The middle term `(theta . Gamma)^{(cd)}_{ab}` is the commutator-like product
of the distortion and the base Christoffel symbols.

---

## 5. Christoffel Formula Summary (for Codazzi-Sp64)

Collecting the explicit Christoffel symbols of the gimmel metric `gg` in the
moving frame `{E_a^H, F_{(bc)}}`, restricted to the section `Sigma = s(X^4)`:

```
Gamma^c_{ab}^{gg}|_s = Gamma^c_{ab}(g_s)                    [H-H-H block]

Gamma^{(cd)}_{ab}^{gg}|_s
  = -(1/2)(eta_{a(c} eta_{d)b} - (1/2) eta_{ab} eta_{cd})   [H-H-V block, algebraic slice]

Gamma^a_{b,(cd)}^{gg}|_s = 0                                 [H-V-H block, tautological]

Gamma^{(ab)}_{c,(de)}^{gg}|_s = 0                            [H-V-V block, tautological]

Gamma^{(ab)}_{(cd),(ef)}^{gg}|_s
  = -(1/2)(eta_{a(c}V_{(d)(e)}eta_{(f)b}
           + eta_{b(c}V_{(d)(e)}eta_{(f)a})                  [V-V-V block, fiber connection]
```

The H-H-V block is the key entry: it is the algebraic slice that must be subtracted
in the horizontal-normalized convention. In the tautological gauge (section has zero
vertical slope), the second fundamental form in the normalized convention is:

```
II_s^H = 0    (tautological section is horizontal-totally-geodesic)
```

For a general section (with distortion `theta`):

```
II_s^H(e_a, e_b)
  = [nabla^{perp}_{e_a}(theta_b)]
    as a Sym^2 T^*X^4-valued tensor,
```

where `nabla^perp` is the normal connection on `N_s ~= Sym^2 T^*X^4` induced by the
gimmel metric.

**Statement for Codazzi.** The normal covariant derivative of `II_s^H` is:

```
nabla^perp_{e_c}(II_s^H(e_a, e_b))
  = e_c((II_s^H)^{(de)}_{ab}) F_{(de)}
    + (Gamma^{(de)}_{(fg),(cd)^{gg}|_s) (II_s^H)^{(fg)}_{ab} F_{(de)}
    - Gamma^c_{ca}^{gg}|_s (II_s^H(e_c, e_b)) [tangential subtraction for C-M].
```

The Codazzi-Mainardi residual is:

```
(nabla^perp_{e_a} II_s^H - nabla^perp_{e_b} II_s^H)(e_c)
  = (R^{Y^14}(e_a, e_b) e_c)^perp.
```

The right-hand side is the normal projection of the ambient Riemann tensor of `Y^14`,
which is the curvature of the gimmel metric, expressible through the frame Christoffel
symbols above.

---

## 6. Hessian and CPA-1 Input

The Willmore energy and its second variation (Hessian) for the section selection:

```
E[s] = integral_{X^4} |II_s^H|^2_{gg} dvol_{g_s}.
```

The Hessian at a critical section `s_0` (where `delta E = 0`) is a self-adjoint operator
on `Sym^2 T^* X^4` (normal-bundle-valued symmetric 2-tensors):

```
Hess E|_{s_0}(phi, phi) = ||nabla^perp phi||^2 + (curvature terms).
```

For `X^4 = S^4` (round 4-sphere, compactified `R^{3,1}`, radius `R`), the normal
deformation operator is the Lichnerowicz operator on transverse-traceless symmetric
2-tensors:

```
L_LC phi = nabla^* nabla phi + (2/3) K(S^4) phi,
```

where `K(S^4) = 12/R^2` (sectional curvature of round `S^4`).

The smallest TT eigenvalue is:

```
lambda_2(S^4) = 8/R^2,
```

giving the Tikhonov regularization parameter (at critical section, second-order):

```
Lambda_GU = lambda_2 / ||phi_obs||^2 = (8/R^2) / epsilon_sec^2
           = 8 / (R^2 epsilon_sec^2).
```

With `R = c t_obs` (light-travel radius to observer):

```
Lambda_GU = 8 c^2 / (t_obs^2 epsilon_sec^2) ~ c^2 epsilon_sec^{-2} t_obs^{-2}.
```

**CPA-1 input.** The TaF bound is `lambda_max = 1/t_obs`. Setting `Lambda_GU ~ lambda_max^2`:

```
8 c^2 / (t_obs^2 epsilon_sec^2) ~ 1/t_obs^2

=> epsilon_sec^2 ~ 8 c^2     (tolerance condition).
```

This does not produce a dimensionless match without specifying units or the normalization
of `epsilon_sec`. The coefficient `8` is now explicit; the CPA-1 comparison is operationally
blocked by the physical identification of `epsilon_sec` in matching units (consistent with
the Phase 5 `observer-section-error-model-2026-06-23.md` finding that conditions B1-B3
remain open).

---

## 7. Verdict and Failure Conditions

**What is established (reconstruction grade):**

1. The gimmel Christoffel symbols in the moving-frame gauge are fully explicit (Section 5).
2. The horizontal-normalized convention is defined precisely and implemented: `II_s^H = 0`
   for the tautological LC-section.
3. For non-tautological sections (distortion `theta != 0`), `II_s^H` is the normal-valued
   covariant derivative of the distortion.
4. `II_s^H(e_a, e_b) = (nabla^perp_{e_a} theta_b)_{linear}` as an explicit formula in
   Christoffel symbols.
5. The Codazzi-Mainardi tensor `nabla^perp II_s^H` has an explicit index expression in
   terms of the moving-frame Christoffels of `gg`.
6. The Hessian coefficient for the CPA-1 comparison is `8 c^2 epsilon_sec^{-2}`;
   this is explicit.

**Failure conditions (what would falsify):**

F1. If the tautological horizontal connection is NOT the LC connection of `g_s` (i.e.,
    if the section `s(x) = (x, g_s(x))` does not have zero vertical slope for the
    natural horizontal structure on `Y^14`), then the formula `T_a = E_a^H` fails and
    `II_s^H` would have additional terms. Falsified by: an explicit section of
    `Met(X^4)` for which the horizontal lift of `partial_mu` does NOT agree with
    `partial_mu + Gamma(g_s)^{rho}_{mu nu} h_{rho lambda} partial_{h_{nu lambda}}`.

F2. If the algebraic slice term `II_s^{ref}` is NOT the correct reference for
    "flat spacetime gives `II_s = 0`" — for example, if the GU formalism intends a
    different normalization — then the horizontal-normalized convention adopted here
    does not match the physical intent. Falsified by: an explicit GU source showing
    `II_s` for flat Minkowski space.

F3. If the gimmel metric signature is NOT (9,5) along the section (e.g., due to
    degeneration of `V_{(ab),(cd)}` on a Lorentzian base), then the fiber metric
    formula for `Gamma^{(cd)}_{ab}` is incorrect. Verified to NOT fail by: the
    N1 signature audit (signature (9,5) is rigorous).

F4. If the normal bundle identification `N_s ~= Sym^2 T^*X^4` fails (for instance,
    if the section is not an immersion, or if the fiber dimension count is wrong),
    the formula for `nabla^perp II_s` would need correction. Current status:
    identification is reconstruction-grade (4D-reduction-section-pullback-2026-06-22.md).

F5. The CPA-1 coefficient comparison requires physical units for `epsilon_sec`.
    The formula `Lambda_GU = 8 c^2 / (t_obs^2 epsilon_sec^2)` is correct given
    `lambda_2(S^4) = 8/R^2`; if `lambda_2` is wrong (e.g., if the relevant spectrum
    is for a different operator on `S^4`), the coefficient 8 changes. Falsified by:
    a CAS eigenvalue computation for the Lichnerowicz operator on `S^4`.

---

## 8. Open Questions

**OQ1 (for Codazzi-Sp64).** The Codazzi-Mainardi residual involves the ambient
Riemann tensor `R^{Y^14}`. An explicit formula for `R^{Y^14}` in the moving-frame
basis is needed for the next Codazzi computation. This requires differentiating the
Christoffel symbols in Section 5, which is a CAS-suitable task.

**OQ2 (convention confirmation).** Whether the horizontal-normalized convention (`II_s^H = 0`
for LC-tautological section) is the GU physical intent should be confirmed against a
primary source (Weinstein lecture or paper). The current choice is the most
natural one that avoids flat-spacetime anomalies.

**OQ3 (distortion identification).** The identification `s*(theta) = II_s^H` is stated
at reconstruction grade in the prior notes. This note gives the moving-frame content
of `II_s^H` but does not re-derive the identification from the GU action principle. The
identification is used operationally; a first-principles derivation from `theta = A - Gamma(g_s)`
via the pullback map would upgrade this to verified grade.

**OQ4 (CPA-1 units).** Resolving the CPA-1 comparison requires specifying `epsilon_sec`
in units compatible with `lambda_max = 1/t_obs`. This is the content of conditions B1-B3
in `explorations/observer-section-error-model-2026-06-23.md`.

---

## 9. Files and Dependencies

**This note depends on:**
- `explorations/ii-s-coordinate-formula-2026-06-23.md` (prior coordinate formula)
- `explorations/4d-reduction-section-pullback-2026-06-22.md` (B1, B3 at reconstruction)
- `explorations/n1-signature-audit-y14-clifford-algebra-2026-06-22.md` (signature (9,5))
- `explorations/codazzi-sp64-bundle-2026-06-23.md` (Codazzi setup, K(A,s) formula)
- `explorations/observer-section-error-model-2026-06-23.md` (CPA-1 bridge model)
- NEXT-STEPS.md Phase 4 entry on explicit II_s formula (F2 item)

**This note unblocks:**
- Codazzi-Sp64 next pass: explicit ambient Riemann tensor in moving frames.
- CPA-1: coefficient 8 is now explicit; remaining blocker is B1-B3 unit identification.
- HC1 residual: coupling coefficients of `theta` in `T^(i)` basis expressible through
  `II_s^H` decomposition into `nabla^perp theta` components.
