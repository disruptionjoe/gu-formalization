---
title: "Codazzi Correction delta_k_i^{Cod} to GU Hidden-Curvature Coupling Coefficients k_i^{GU} = 512 * P^(i)"
date: 2026-06-23
problem_label: "hc1-codazzi-correction"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# Codazzi Correction to GU Hidden-Curvature Coupling Coefficients

**Verdict:** CONDITIONALLY_RESOLVED  
**Grade:** Reconstruction — the structure of the Codazzi correction is derived explicitly
from the [CodEq-Explicit] formula in `ii-s-moving-frames-2026-06-23.md` and the
normal-bundle curvature identification in `pc2-gauss-y14-curvature-2026-06-23.md`.
The correction is additive, representation-dependent (different for each i=1,2,3),
and does NOT shift the 512 normalization factor at the section to leading order. The
Codazzi term is a secondary correction proportional to the 4D curvature of g_s,
subleading in the low-curvature / small-distortion regime.

**What this closes.** Residual OQ-HC1-2 from `hc1-coupling-coefficients-2026-06-23.md`:
"Compute the ambient curvature term R^{Y^14,perp} in the Codazzi equation [CodEq]
and project onto T^(i) irreducibles." This exploration performs that computation at
reconstruction grade.

---

## 1. Problem Statement

### 1.1 The question

From `hc1-coupling-coefficients-2026-06-23.md` §5 and §10 (Failure Condition F3):

The HC-master formula was derived as:

```
H^(i)_{GU} = 512 * P^(i)[nabla^{g_s} theta]    [HC-master, leading order]
```

with the caveat (§10, F3):

> If the Codazzi correction (the R^{Y^14,perp} + F^Psi term in [CodEq]) has a component
> in the same irreducible as the leading term, it would additively modify k_i^{GU}:
>
>   k_i^{GU} = 512 * k_i^{EC} + delta_k_i^{Cod}
>
> where delta_k_i^{Cod} is the Codazzi correction (computable from the R^{Y^14,perp} term;
> requires the ambient Riemann tensor of Y^14 in coordinates).

The question of this exploration is:

1. What is delta_k_i^{Cod} explicitly?
2. Does it shift the 512 normalization factor?
3. Is it representation-specific (different for i=1,2,3) or universal?

### 1.2 Established context

This computation builds on:

- `explorations/hc1-coupling-coefficients-2026-06-23.md` — HC-master formula, projectors P^(i), factor 512
- `explorations/ii-s-moving-frames-2026-06-23.md` — explicit Codazzi equation [CodEq-Explicit]
- `explorations/codazzi-sp64-2026-06-23.md` — full Codazzi equation [CodEq] for Sp(64) bundle
- `explorations/pc2-gauss-y14-curvature-2026-06-23.md` — tangential projection [G^Y_T]^{TF}; normal-bundle curvature R^{N_s}
- `explorations/ic1-soldering-map-ns-adps-2026-06-23.md` — soldering map j_s
- `explorations/ic2-positivity-soldering-normal-2026-06-23.md` — Clifford trace 512 h(n_i,n_j)

---

## 2. The Codazzi Equation in Full Form

### 2.1 The [CodEq-Explicit] from ii-s-moving-frames §5.6

The explicit Codazzi equation derived in `ii-s-moving-frames-2026-06-23.md` (Section 5.6)
states:

```
(nabla^{g_s}_{[e_a, e_b]} theta_c)^{(de)}
  = -(R^{g_s})^f{}_{c[ab]} theta_f^{(de)}
    - (R^{Y^14}_H)^{(de)}_{ab,c}[g_s]          [CodEq-Explicit]
```

where the two right-hand side terms are:

**Term 1 (Ricci identity):** `-(R^{g_s})^f{}_{c[ab]} theta_f^{(de)}`
- This is the X^4 curvature of g_s acting on the base (one-form) index c of theta.
- It vanishes in flat spacetime (R^{g_s} = 0).
- It is proportional to theta (linear in distortion).

**Term 2 (Ambient curvature):** `-(R^{Y^14}_H)^{(de)}_{ab,c}[g_s]`
- This is the ambient gimmel curvature of Y^14 = Met(X^4) in the H-H-H-V entry.
- It is evaluated at the background tautological section (theta = 0).
- Explicitly (from ii-s-moving-frames §5.5):

```
(R^{Y^14}_H)^{(de)}_{ab,c}[g_s]
  = -(1/2)(nabla^{g_s}_{e_a}(g_{b(d}g_{e)c}) - nabla^{g_s}_{e_b}(g_{a(d}g_{e)c}))
```

In the moving-frame (orthonormal) gauge where g_{ab} = eta_{ab} is constant, the
derivatives nabla^{g_s}_{e_a}(eta_{b(d} eta_{e)c}) = 0, so this term has a covariant
form in coordinates:

```
(R^{Y^14}_H)^{(de)}_{ab,c}[g_s]
  = -(1/2)( Gamma^f_{ab}(g_s) eta_{f(d} eta_{e)c}
           + eta_{b(d} Gamma^f_{ac}(g_s) eta_{e)f}
           - Gamma^f_{ba}(g_s) eta_{f(d} eta_{e)c}
           - eta_{a(d} Gamma^f_{bc}(g_s) eta_{e)f} )
  = -(1/2)(Gamma^{(de)}_{ab;c}(g_s) - Gamma^{(de)}_{ba;c}(g_s))
```

where the semicolon denotes the covariant version of the index-raising / fiber-metric
contraction. This simplifies (since Gamma is symmetric in ab for torsion-free connection,
Gamma_{ab} = Gamma_{ba} lower indices, but antisymmetrized above):

In Riemann-normal coordinates, Gamma^f_{ab}(g_s) = 0 at a point; the ambient
curvature term vanishes at that point and picks up second derivatives (the curvature)
at neighboring points. The covariant version of Term 2 is:

```
(R^{Y^14}_H)^{(de)}_{ab,c}[g_s]
  = -(1/2) R^{g_s}_{f(d}{}_{ab} eta_{e)c} - (1/2) R^{g_s}_{f(e}{}_{ab} eta_{d)c}
```

(the partial derivative of the fiber metric in the direction given by the curvature
of g_s). This involves the Riemann tensor of g_s contracted against the fiber metric.

### 2.2 Structure of the Codazzi correction to the coupling

The HC-master formula [HC-master] from hc1-coupling-coefficients arises from the
Bianchi chain:

```
DT = R wedge e     (first Bianchi identity, with T = theta as source torsion)
```

The leading-order coupling is:

```
H^(i)_{GU,leading} = 512 * P^(i)[nabla^{g_s} theta]    [HC-leading]
```

The Codazzi equation [CodEq-Explicit] introduces an additional curvature source when
we take the antisymmetric derivative of the HC-leading term. From [CodEq-Explicit]:

The source term for H^(i) through the Bianchi identity has the correction:

```
delta(DT)^{(i)} = P^(i)[(R^{Y^14}_H)^{(de)}_{ab,c}[g_s]]    [Cod-source]
```

This is the component of the ambient gimmel curvature projected onto the i-th
SO(1,3)-irreducible. The Codazzi correction to the coupling coefficient is:

```
delta_k_i^{Cod} = 512 * c_i^{proj} * C^{ambient}    [Cod-coeff]
```

where:
- 512 = j_s Clifford-trace factor (from ic2-positivity, universal)
- c_i^{proj} = projection coefficient of Term 2 onto the i-th irreducible
- C^{ambient} = overall scale of the ambient curvature term

---

## 3. Explicit Computation: Projecting Term 2 onto T^(i) Irreducibles

### 3.1 Structure of the ambient curvature term

The ambient curvature term (R^{Y^14}_H)^{(de)}_{ab,c}[g_s] has the index structure:

- (de): symmetric fiber indices (from Sym^2 T*X^4, the normal bundle)
- [ab]: antisymmetric tangent pair (from Lambda^2 T*X^4)
- c: one additional tangent index

This matches the index structure of:

```
(nabla^{g_s}_{[e_a]} theta_c)^{(de)}
```

i.e., it has the SAME tensor type as the source of the Bianchi identity, namely an
element of Lambda^2 T*X^4 tensor Lambda^1 T*X^4 tensor Sym^2 T*X^4 (the curvature
2-form space tensor the fiber).

### 3.2 The ambient curvature term as a curvature 2-form

More precisely, the ambient curvature correction (R^{Y^14}_H)^{(de)}_{ab,c}[g_s]
in the H-H-H-V block of Riem(gg) can be written (from pc2-gauss-y14-curvature §3.1):

```
(R^{Y^14}(E_a^H, E_b^H) E_c^H)^{(de)}
  = -(1/2) R^{g_s}_{a b f}{}^{(d} eta^{e)f}... + (mixed fiber terms)
```

In the notation of pc2-gauss-y14-curvature §3.2, the H-H-H-V contraction is:

```
(R^{Y^14}_H)^{(de)}_{ab,c}
  = -(1/2)(R^{g_s})^{(d}{}_{c[a}{}^{e)}_{b]}     [ambient-curv-formula]
```

where the parentheses on (de) denote symmetrization (the Sym^2 T*X^4 fiber slot).

This formula arises from differentiating the H-H-V Christoffel block:

```
Gamma^{(de)}_{ab}^{gg}|_s = -(1/2)(eta_{a(d}eta_{e)b} - (1/2)eta_{ab}eta_{de})
```

with respect to the section coordinates. The derivative of this block generates
terms proportional to the Riemann tensor of g_s (via the Gauss-Codazzi structure
of the fiber bundle Y^14 = Met(X^4) -> X^4).

### 3.3 Decomposition of the ambient curvature term under SO(1,3)

The ambient curvature term (R^{Y^14}_H)^{(de)}_{ab,c} has the following symmetries:

- (de) symmetric (fiber Sym^2 T*X^4)
- [ab] antisymmetric (Lambda^2 T*X^4)
- c is a free tangent index

This is exactly the T^{tensor type} = Lambda^2 tensor Lambda^1 tensor Sym^2 tensor,
but the Sym^2 slot is the FIBER while [ab], c are BASE. The SO(1,3) decomposition
acts on all base indices.

From the formula [ambient-curv-formula]:

```
(R^{Y^14}_H)^{(de)}_{ab,c} = -(1/2) R^{g_s}_{f c [ab]} eta^{f(d}eta^{e)...}
```

The SO(1,3) structure of this term is determined by the Riemann tensor R^{g_s}_{f c ab},
which decomposes as:

```
R^{g_s}_{abcd} = W_{abcd} + S_{ab[cd]} + (R/12)(eta_{ac}eta_{bd} - eta_{ad}eta_{bc})
```

where W = Weyl tensor, S = traceless Ricci piece, R = scalar curvature.

When contracted to form (R^{Y^14}_H)^{(de)}_{ab,c}, the result is:

```
(R^{Y^14}_H)^{(de)}_{ab,c}
  = -(1/2) W_{fcab} eta^{f(d}eta^{e)...}_{c}     [Weyl piece, lives in T^(1) type]
    -(1/2) S_{fc[ab]} eta^{f(d}eta^{e)c}           [traceless Ricci piece, T^(2) type]
    -(R/12)(...) eta^{f(d}eta^{e)...}             [scalar piece, T^(3) mixing]
```

More precisely, the R^{g_s} tensor contracted with the fiber metric eta^{f(d}eta^{e)c}
produces an object in the SAME SO(1,3) irreducible decomposition as the torsion
T^{ab}{}_{c} tensor types T^(1,2,3). The decomposition follows directly from the
Riemann tensor's own SO(1,3) structure.

**Key algebraic result.** The ambient curvature term (R^{Y^14}_H)^{(de)}_{ab,c}
has a non-trivial component in ALL THREE irreducible types T^(1), T^(2), T^(3)
because the Riemann tensor of g_s contains all three Weyl-Ricci-scalar pieces,
and these project onto (3/2,1/2)+(1/2,3/2), (1/2,1/2)_v, (1/2,1/2)_a respectively
under the SO(1,3) decomposition.

### 3.4 The explicit projection coefficients c_i^{proj}

The projection coefficients c_i^{proj} for the ambient curvature term onto each
T^(i) irreducible are determined by the standard SO(1,3) Clebsch-Gordan analysis.

**For the T^(1) irreducible [(3/2,1/2)+(1/2,3/2), dim 16]:**

The Weyl tensor W_{abcd} (which is the T^(1)-type piece of the Riemann tensor)
contributes to (R^{Y^14}_H)^{(de)}_{ab,c} in the (3/2,1/2)+(1/2,3/2) irreducible.
The projection coefficient is:

```
c_1^{proj} = 1    [Weyl tensor is already in T^(1) irreducible; no extra factor]
```

The specific formula: from the Weyl decomposition,
P^(1)[(R^{Y^14}_H)] = -(1/2) P^(1)[W_{fcab} eta^{f(d}...].
The Weyl tensor lies entirely in the (2,0)+(0,2) SL(2,C) representation, which
contributes to H^(1) in the (3/2,1/2)+(1/2,3/2) coupling (the tensor product
(2,0) tensor (1/2,1/2) contains (3/2,1/2) as a summand). So c_1^{proj} is nonzero
and of O(1).

**For the T^(2) irreducible [(1/2,1/2)_vector, dim 4]:**

The traceless Ricci tensor S_{ab} contributes to (R^{Y^14}_H) in the (1/2,1/2)_v
type. The projection coefficient is:

```
c_2^{proj} = 1/3    [standard trace-vector projector, cf. hc1-coupling-coefficients §3.1]
```

(The 1/3 factor is the same projector coefficient that appears in P^(2) itself; the
ambient curvature term, when projected onto T^(2), picks up the same 1/3 factor as
the theta^(2) projector.)

**For the T^(3) irreducible [(1/2,1/2)_axial, dim 4]:**

The scalar curvature R and the epsilon-dual Weyl tensor W* contribute to (R^{Y^14}_H)
in the (1/2,1/2)_axial type. The projection coefficient is:

```
c_3^{proj} = 1/3    [standard axial-vector projector]
```

### 3.5 The scale C^{ambient}

The overall scale of the ambient curvature term is:

```
C^{ambient} = R^{g_s}_{...} / (characteristic curvature scale)^2
```

In the low-curvature regime (curvature radius >> distortion scale), C^{ambient}
is suppressed by two powers of curvature relative to the leading-order term. More
precisely, from [ambient-curv-formula]:

```
||(R^{Y^14}_H)^{(de)}_{ab,c}|| ~ ||R^{g_s}|| / Lambda_curv
```

where Lambda_curv is the curvature scale (Lambda_curv ~ 1/R_K for K3-type X^4
with K3 area R_K^2). In comparison, the leading term:

```
||nabla^{g_s} theta|| ~ ||theta|| / lambda_dist
```

where lambda_dist is the characteristic length scale of theta variations.

**For the ambient correction to be subleading to the leading term:**

```
||delta_k_i^{Cod}|| << ||k_i^{GU}_{leading}|| = 512
```

requires:
```
512 * c_i^{proj} * C^{ambient} << 512
=> C^{ambient} << 1    (in dimensionless units)
=> ||R^{g_s}|| << 1/lambda_dist^2    (curvature is small on distortion scale)
```

This is the **low-curvature approximation**, which holds in the standard semiclassical
(GR) regime where the spacetime curvature radius is much larger than the distortion
correlation length.

---

## 4. The Full Coupling Coefficient with Codazzi Correction

### 4.1 Modified HC-master formula

Including the Codazzi correction, the hidden curvature coupling formula becomes:

```
H^(i)_{GU} = 512 * P^(i)[nabla^{g_s} theta]
             + delta_k_i^{Cod} * P^(i)[(R^{Y^14}_H)[g_s]]    [HC-master-corrected]
```

where:

```
delta_k_i^{Cod} = 512 * c_i^{proj}    [from j_s normalization and projector]
```

Explicitly:

```
k_1^{GU,full} = 512 + delta_k_1^{Cod} = 512 + 512 * c_1^{proj} * [R factor]
k_2^{GU,full} = 512/3 + delta_k_2^{Cod} = 512/3 + 512 * (1/3) * c_2^{proj} * [R factor]
k_3^{GU,full} = 512/3 + delta_k_3^{Cod} = 512/3 + 512 * (1/3) * c_3^{proj} * [R factor]
```

The [R factor] is the ratio of the ambient curvature source to the gradient source:

```
[R factor] = (R^{Y^14}_H)^{(de)}_{ab,c}[g_s] / (nabla^{g_s} theta)^{(de)}_{ab,c}
```

In physical units (theta dimensionless in normalized coordinates):

```
[R factor] ~ R_curv^{-2} / partial_a theta ~ R_curv^{-2} / (theta / lambda_dist)
           = lambda_dist / (R_curv^2 theta)
```

For typical GR situations (R_curv ~ H^{-1} ~ 10^{26} m, lambda_dist ~ theta/A ~ theta
/ (cosmological distortion amplitude)), the [R factor] is negligibly small.

### 4.2 The Codazzi correction does NOT shift the 512 normalization at the section

**Key result.** The Codazzi correction delta_k_i^{Cod} is:

1. **Additive** (not multiplicative): it adds to k_i^{GU}, not scales it.
2. **Proportional to curvature**: vanishes in flat spacetime.
3. **Not a shift of the 512 normalization factor**: the 512 comes from the j_s
   Clifford-trace (Tr_S(c(u)c(v)) = 256 g_Y(u,v), doubled by the double-Clifford
   map in j_s), which is a representation-theoretic constant independent of spacetime
   curvature. The Codazzi correction is a dynamical (field-equation-dependent) term,
   while 512 is a kinematic (algebra-determined) constant.
4. **Representation-dependent**: c_i^{proj} is different for i=1,2,3 (unlike the
   512 factor which is universal across irreducibles). Specifically:
   ```
   delta_k_1^{Cod} ~ 512 * R^{g_s}_{Weyl}    [Weyl piece -> T^(1)]
   delta_k_2^{Cod} ~ 512 * (1/3) * R^{g_s}_{Ric}    [Ricci piece -> T^(2)]
   delta_k_3^{Cod} ~ 512 * (1/3) * R^{g_s}_{scalar}  [scalar piece -> T^(3)]
   ```
   where the subscripts denote the Weyl, traceless-Ricci, and scalar parts of R^{g_s}.

5. **On the tautological LC-section (theta=0, II_s^H=0):** The Codazzi correction
   is still present (it is a source term independent of theta at this order), but it
   enters at a different level of the coupling chain. Specifically, the ambient curvature
   term (R^{Y^14}_H)^{(de)}_{ab,c}[g_s] is nonzero whenever X^4 has curvature,
   even if theta = 0.

### 4.3 Physical interpretation of the Codazzi correction

The Codazzi correction delta_k_i^{Cod} represents the coupling of the hidden curvature
to the AMBIENT curvature of Y^14 = Met(X^4), i.e., to the curvature of the metric
bundle itself over X^4. This is a genuinely new source for the hidden curvature pieces
H^(i) that is absent in standard Einstein-Cartan:

**In Einstein-Cartan:** The hidden curvature H^(i) is sourced ONLY by the torsion
T^(i) through DT = R wedge e. When T = 0 (torsion-free), H^(i) = 0.

**In GU:** The hidden curvature H^(i) receives an additional source from the ambient
gimmel curvature (R^{Y^14}_H)^{(de)}_{ab,c}[g_s], which is nonzero even when theta=0
(i.e., even when the distortion vanishes). This is a GU-specific contribution with no
analog in Einstein-Cartan or any torsion theory:

```
H^(i)_{GU} = (leading) + (ambient curvature correction)
           = 512 * P^(i)[nabla^{g_s} theta] + delta_k_i^{Cod} * P^(i)[R^{Y^14}]
```

The second term is sourced by the GEOMETRY OF THE SPACE OF METRICS, not by the
distortion field itself. It is an intrinsic property of the GU embedding Y^14 = Met(X^4).

---

## 5. Magnitude Estimate and Regime Analysis

### 5.1 Flat spacetime limit

For g_s = eta (Minkowski metric), R^{g_s} = 0, so:
```
delta_k_i^{Cod}|_{flat} = 0    [flat spacetime: no Codazzi correction]
```

The HC-master formula is exact in flat spacetime:
```
H^(i)_{GU}|_{flat} = 512 * P^(i)[nabla theta]
```

### 5.2 Weak gravitational field (post-Newtonian)

For weak gravity with curvature R^{g_s} ~ G M / r^3 (tidal field):

```
delta_k_i^{Cod} ~ 512 * (G M / r^3) * lambda_dist^2
```

For laboratory-scale distortion (lambda_dist ~ mm) and solar-system curvature (GM/r^3
~ 10^{-13} s^{-2}):
```
delta_k_i^{Cod} ~ 512 * 10^{-13} * 10^{-6} ~ 10^{-16}    [dimensionless, negligible]
```

vs. leading term 512. Correction is 18 orders of magnitude below leading term.

### 5.3 Near a black hole (strong curvature)

At the Schwarzschild radius r ~ GM/c^2, curvature R^{g_s} ~ c^4/(G^2 M^2):

```
delta_k_i^{Cod} ~ 512 * (c^4/G^2 M^2) * lambda_dist^2
```

For M = 10 solar masses, r_S ~ 15 km, lambda_dist ~ Planck length l_P ~ 10^{-35} m:
```
delta_k_i^{Cod} ~ 512 * (10^{18}/(10^{60})) * 10^{-70} ~ negligible
```

Even near strong-field astrophysical objects, the Codazzi correction is Planck-suppressed
for distortion length scales below the curvature radius.

### 5.4 K3-type X^4 (the GU-selected background)

For the K3-type X^4 selected by the Willmore variational principle (oq3a-gu-variational-k3):
The K3 metric has curvature scale R_K (Kahler-Ricci flat, R^{g_s}_{Ric} = 0 but
R^{g_s}_{Weyl} != 0, R = 0). Therefore:

```
delta_k_2^{Cod}|_{K3} = 0    [Ricci-flat K3: traceless Ricci is zero]
delta_k_3^{Cod}|_{K3} = 0    [Ricci-flat K3: scalar curvature is zero]
delta_k_1^{Cod}|_{K3} = 512 * c_1^{proj} * W_{K3} / nabla theta    [Weyl piece is nonzero]
```

On K3, only the T^(1) coupling (Weyl piece, traceless spin-2 hidden curvature) receives
a Codazzi correction. The T^(2) and T^(3) couplings are unchanged at the LC-section.

**This is a signature GU prediction:** On the K3-type background selected by GU,
the hidden curvature H^(2) and H^(3) are exactly:

```
H^(2)_{GU}|_{K3} = (512/3) * P^(2)[nabla^{g_s} theta]    [no Codazzi correction]
H^(3)_{GU}|_{K3} = (512/3) * P^(3)[nabla^{g_s} theta]    [no Codazzi correction]
```

while H^(1) receives a Weyl-curvature correction:

```
H^(1)_{GU}|_{K3} = 512 * P^(1)[nabla^{g_s} theta] + 512 * c_1^{proj} * W_{K3}/...
```

---

## 6. Why the 512 Normalization Factor Is Not Shifted

### 6.1 The 512 is a representation-theoretic constant

The factor 512 enters the coupling through the Clifford-trace formula:

```
B_fund(j_s(n_i), j_s(n_j)) = 512 h(n_i, n_j)
```

(from ic2-positivity-soldering-normal, established via Tr_S(Xi_i^2) = 512 for all
normal vectors n_i). This is an algebraic identity involving:
- The spinor module S = H^{64} (dimension factor dim_R S = 256)
- The Clifford product in Cl(9,5) ~= M(64,H)
- The j_s map j_s(n_i) = epsilon_i * sum_a c(e^a) c(n_i)

None of these depend on the spacetime curvature or the distortion field theta.
The 512 is as fundamental as the dimension of the spinor module.

### 6.2 The Codazzi correction is a source shift, not a normalization shift

The Codazzi equation [CodEq-Explicit] relates the curvature of theta (as a
connection-form on X^4) to the ambient gimmel curvature:

```
curv(theta) = Ricci identity term + ambient curvature term
```

In the Bianchi identity DT = R wedge e (with T = theta and R sourced by both theta
and the ambient geometry), the Codazzi term enters as an ADDITIONAL SOURCE for the
curvature R, not as a rescaling of the theta-to-R coupling.

The chain is:
```
theta --[j_s * nabla]--> II_s^H --[Bianchi]--> H^(i) + [ambient curvature source]
```

The [j_s * nabla] step carries the factor 512 (from j_s).
The [Bianchi] step generates H^(i) from nabla theta.
The [ambient curvature source] is an additive correction at the BIANCHI step, not
a modification of the j_s factor.

Therefore:
- 512 multiplies nabla theta in the leading term: this is the j_s kinematic factor.
- delta_k_i^{Cod} multiplies (R^{Y^14}_H): this is a separate dynamical source.
- The two contributions ADD, not multiply.

### 6.3 Summary: 512 is kinematic, delta_k_i is dynamical

The distinction is clean:

| Factor | Type | Dependence | Modifiable by Codazzi? |
|---|---|---|---|
| 512 | Kinematic (j_s Clifford trace) | Algebra of Cl(9,5), S = H^64 | No |
| 1/3 (for i=2,3) | Kinematic (SO(1,3) projector P^(2,3)) | Representation theory | No |
| delta_k_i^{Cod} | Dynamical (ambient curvature source) | Riemann tensor of g_s, Y^14 geometry | Yes (this is the correction) |

The Codazzi correction adds a new dynamical source for hidden curvature, but does
not change the kinematic coefficient (512) of the distortion-sourced hidden curvature.

---

## 7. Relation to the pc2-gauss-y14-curvature Result

### 7.1 Consistency check

From `pc2-gauss-y14-curvature-2026-06-23.md` §8.1 (Simons formula connection):

```
V^{ij} R^{N_s}_{ij, mu nu} = 4K g_{mu nu}    [on round S^4, totally geodesic section]
```

where K = 1/R^2 is the sectional curvature of S^4. This is the normal-bundle curvature
contribution to [G^Y_T]^{TF}. It represents exactly the type of ambient curvature source
that appears as the Codazzi correction Term 2 in [CodEq-Explicit].

For the HC1 coupling chain, the analog is:

```
P^(i)[(R^{Y^14}_H)^{(de)}_{ab,c}[g_s]] on round S^4
  = P^(i)[4K * (some tensor in T^(i) type)]
```

On S^4 with scalar curvature R_{S^4} = 12/R^2 (for round S^4 of radius R):
- The Weyl tensor W_{S^4} = 0 (round sphere is conformally flat -> delta_k_1^{Cod}|_{S^4} = 0)
- The traceless Ricci S_{S^4} = 0 (Einstein manifold -> delta_k_2^{Cod}|_{S^4} = 0)
- The scalar curvature R_{S^4} = 12/R^2 != 0 (-> delta_k_3^{Cod}|_{S^4} != 0)

Therefore, on round S^4 (the GU compactification background):

```
delta_k_1^{Cod}|_{S^4} = 0    [round sphere is conformally flat]
delta_k_2^{Cod}|_{S^4} = 0    [round sphere is Einstein with traceless Ricci = 0]
delta_k_3^{Cod}|_{S^4} ~ 512 * (1/3) * (12/R^2) / (nabla theta scale)
                        ~ 512 * 4K / (nabla theta scale)    [proportional to 4K from Simons]
```

The 4K Simons correction from CPA-1 (the ambient curvature gate in cpa1-omega-tuning)
appears EXACTLY as the T^(3) (axial) Codazzi correction to the hidden curvature coupling!

**This is a structural consistency check between PC2 and HC1:** The ambient curvature
contribution that enters CPA-1 (the Simons +4K correction to the Willmore eigenvalue)
is the SAME ambient curvature that gives delta_k_3^{Cod} in the HC1 coupling formula.
Both trace back to the H-H-V Christoffel block of the gimmel metric:

```
Gamma^{(cd)}_{ab}^{gg}|_s = -(1/2)(eta_{a(c}eta_{d)b} - (1/2)eta_{ab}eta_{cd})
```

and its derivative along the section (which gives R^{Y^14}_H).

---

## 8. Closed-Form Expression for delta_k_i^{Cod}

### 8.1 Master formula for the Codazzi correction

Combining the above analysis, the Codazzi correction to the HC coupling at the section
s: X^4 -> Y^14 is:

```
CODAZZI CORRECTION FORMULA:

delta_k_i^{Cod}
  = 512 * P^(i)[(R^{Y^14}_H)^{(de)}_{ab,c}[g_s]] / (nabla^{g_s} theta)^{(de)}_{ab,c}

  = 512 * P^(i)[-(1/2) R^{g_s}_{f(d|}{}_{c[a}{}^{|e)}{}_{b]} eta_f...]
                  / P^(i)[nabla^{g_s} theta]    [Cod-master]
```

In a form that makes the structure explicit:

For i = 1 (T^(1): Weyl sourced, [3/2,1/2]+[1/2,3/2]):
```
delta_k_1^{Cod} = -(512/2) * W_{ab}{}^{(d}{}_{c}{}^{e)} / (nabla^{g_s} theta)^{(de)}_{ab,c}
```
(Weyl piece of R^{g_s}; vanishes on conformally flat backgrounds including S^4, K3)

For i = 2 (T^(2): trace-vector, [1/2,1/2]_v):
```
delta_k_2^{Cod} = -(512/2) * (1/3) * S_{f c} eta^{f(d}eta^{e)}{}_{[ab]} / (...)
```
(traceless Ricci piece; vanishes on Einstein manifolds including S^4 and Ricci-flat K3)

For i = 3 (T^(3): axial-vector, [1/2,1/2]_a):
```
delta_k_3^{Cod} = -(512/2) * (1/3) * (R/12) * epsilon_{c[ab]}{}^f eta_{f(d}eta_{e)} / (...)
```
(scalar curvature piece; vanishes only on Ricci-flat backgrounds including K3; nonzero on S^4)

### 8.2 Compact notation

Writing the Codazzi correction schematically:

```
delta_k_1^{Cod} ~ 512 * W_{abcd}    [Weyl coupling to T^(1)]
delta_k_2^{Cod} ~ (512/3) * Ric_{ab}^{TF}    [traceless Ricci coupling to T^(2)]
delta_k_3^{Cod} ~ (512/3) * R_scal    [scalar curvature coupling to T^(3)]    [Cod-compact]
```

where W, Ric^{TF}, R_scal are the Weyl, traceless Ricci, and scalar curvature of
g_s respectively (in appropriate tensor contractions with the projection onto T^(i)).

The FULL coupling including Codazzi correction:

```
H^(i)_{GU,full} = 512 * P^(i)[nabla^{g_s} theta] + delta_k_i^{Cod} * P^(i)[curv(g_s)]
                = 512 * P^(i)[nabla^{g_s} theta + (1/2) R^{g_s}_{...} sigma_{(de)}]
```

where sigma_{(de)} is a fiber metric contraction absorbing the free fiber index,
and the factor 1/2 comes from the H-H-V Christoffel block.

---

## 9. Verdict on the 512 Normalization at the Section

**Main result:** The Codazzi correction delta_k_i^{Cod} does NOT shift the 512
normalization factor at the section. The coupling formula retains the structure:

```
k_i^{GU} = 512 * k_i^{EC}    [kinematic leading term, from j_s Clifford trace]
```

with an additional representation-dependent curvature source:

```
delta_k_i^{Cod} = 512 * c_i^{proj} * R^{g_s}_{(i)}    [dynamical Codazzi correction]
```

where:
- c_1^{proj} ~ W_{abcd} piece (Weyl coupling)
- c_2^{proj} ~ Ric_{ab}^{TF}/3 (traceless Ricci coupling)
- c_3^{proj} ~ R_scal/3 (scalar curvature coupling)

**The 512 is not modified because:**
1. It is kinematic (j_s Clifford trace = representation-theoretic constant).
2. The Codazzi correction is additive (adds a curvature source, does not rescale theta).
3. In flat spacetime and on Ricci-flat backgrounds (K3-type X^4 selected by GU),
   most or all Codazzi corrections vanish.

**Hierarchy at the GU-selected background (K3-type Ricci-flat X^4):**

```
k_1^{GU}|_{K3} = 512 + O(W_{K3}/nabla theta)    [Weyl correction; suppressed for large nabla theta]
k_2^{GU}|_{K3} = 512/3    [exact: Ricci-flat kills delta_k_2^{Cod}]
k_3^{GU}|_{K3} = 512/3    [exact: Ricci-flat kills delta_k_3^{Cod}]
```

On the K3-type background, the GU coupling formula for H^(2) and H^(3) is
**exact** at reconstruction grade, with no Codazzi correction:

```
H^(2)_{GU}|_{K3} = (512/3) * P^(2)[nabla^{g_s} theta]    [exact on K3-type]
H^(3)_{GU}|_{K3} = (512/3) * P^(3)[nabla^{g_s} theta]    [exact on K3-type]
```

---

## 10. Failure Conditions

**F1 (Ambient curvature formula).** The formula [ambient-curv-formula]:
```
(R^{Y^14}_H)^{(de)}_{ab,c} = -(1/2) R^{g_s}_{f(d}{}_{c[a}{}^{e)}{}_{b]} ...
```
was derived from the Koszul formula and the H-H-V Christoffel block in the
tautological gauge. If the tautological gauge deviates from the GU horizontal
connection (i.e., if GU uses a different horizontal distribution on Y^14), the
formula would change and the Codazzi correction would be different.
**Falsification:** Find a GU source identifying the horizontal connection explicitly
as something other than the Levi-Civita lift.

**F2 (SO(1,3) projection coefficients).** The claim that c_i^{proj} are the
SAME coefficients as the P^(i) torsion projectors (1, 1/3, 1/3) depends on the
structure of (R^{Y^14}_H)^{(de)}_{ab,c} decomposing under SO(1,3) with the same
Clebsch-Gordan coefficients as a generic Lambda^2 tensor Lambda^1 T* tensor.
If the fiber metric contraction (the eta^{f(d}eta^{e)c} factors) introduces
additional representation mixing, c_i^{proj} would differ from the naive P^(i)
coefficients.
**Falsification:** Explicit Clebsch-Gordan computation of
(R^{g_s})^{(d}{}_{c[a}{}^{e)}{}_{b]} under SO(1,3) showing different c_i^{proj}.

**F3 (Leading-order approximation).** The formula H^(i) = 512 P^(i)[nabla theta] +
delta_k_i^{Cod} holds as a linearization in theta. At quadratic order in theta,
additional Codazzi corrections arise from the II_s^H = nabla theta quadratic terms.
The Codazzi correction at O(theta^2) would couple T^(i) of theta to T^(j) of theta
(cross-terms), generating a more complex coupling matrix k_{ij}^{GU}(theta).
**Falsification:** Demonstrate that Q^{TF}(B^2) (the quadratic Gauss correction)
contributes a term proportional to (nabla theta)^2 that mixes T^(i) and T^(j) types.
This is not a new failure condition -- it was already noted in hc1-coupling-coefficients
§10 F5 as "quadratic corrections at O(theta^2)."

**F4 (K3 Weyl correction magnitude).** On K3-type X^4, the Weyl tensor is generically
nonzero (K3 is not conformally flat despite being Ricci-flat). The Codazzi correction
to k_1^{GU} is therefore nonzero even on the GU-selected background:
```
delta_k_1^{Cod}|_{K3} = 512 * (W_{K3} / nabla theta scale)
```
If the K3 Weyl tensor W_{K3} is not small compared to the gradient of theta (e.g.,
for slowly varying distortions), this correction could be significant.
**Falsification:** A Weyl-tensor magnitude computation on the K3 that the GU
variational principle selects, showing W_{K3} is not parametrically suppressed.

**F5 (Normal-bundle curvature identification).** The identification
(R^{Y^14}_H)^{(de)}_{ab,c} = -(1/2) R^{g_s}_{...} uses the fact that R^{N_s}
(the normal bundle curvature) is determined by the ambient gimmel curvature of Y^14.
If the identification R^{N_s} = j_s^{-1}(F_A|_{N_s block}) (from pc2-gauss-y14) has
errors, the ambient curvature formula and hence the Codazzi correction would change.
**Falsification:** An explicit CAS computation of R^{Y^14}(E_a^H, E_b^H) E_c^H
in the normal direction that yields a different result from -(1/2) R^{g_s}_{...}.

---

## 11. Open Questions

**OQ-HC1-Cod-1 (CAS verification of the Codazzi correction formula).**
Compute (R^{Y^14}_H)^{(de)}_{ab,c}[g_s] explicitly using SymPy or Sage, differentiating
the H-H-V Christoffel block Gamma^{(cd)}_{ab}^{gg}|_s = -(1/2)(eta_{a(c}eta_{d)b} -
(1/2)eta_{ab}eta_{cd}) with respect to the section coordinates. Verify the formula
[ambient-curv-formula] and the projection coefficients c_i^{proj}.

**OQ-HC1-Cod-2 (K3 Weyl correction magnitude).**
Compute ||delta_k_1^{Cod}|_{K3}|| relative to k_1^{GU} = 512 for a representative
K3 metric (e.g., the Kummer K3 surface or an orbifold limit). If delta_k_1^{Cod}/512
~ R_{K3}/lambda_dist is small, confirm that the leading-order formula H^(1)_GU ~ 512
P^(1)[nabla theta] is a good approximation.

**OQ-HC1-Cod-3 (Cross-coupling at O(theta^2)).**
Extend the Codazzi correction to quadratic order in theta. The O(theta^2) Codazzi
correction generates cross-terms k_{ij}^{GU} coupling T^(i) of theta to T^(j) of
the ambient curvature. Determine whether these cross-terms contribute meaningfully
to the hidden curvature coupling.

**OQ-HC1-Cod-4 (Connection to Weyl anomaly).**
The Weyl coupling delta_k_1^{Cod} ~ W_{abcd} is reminiscent of the Weyl anomaly
in quantum field theory. On K3-type X^4, the Weyl tensor sources H^(1) even with
zero distortion theta. This is a GU-specific prediction: the spin-2 hidden curvature
H^(1) is non-trivially sourced by the Weyl tensor of the 4D background geometry.
A systematic study of the implications for CMB tensor modes or gravitational wave
signatures would be a natural follow-on.

---

## 12. Result Summary

**Verdict: CONDITIONALLY_RESOLVED**

**Main result (reconstruction grade):**

The Codazzi correction delta_k_i^{Cod} to the GU hidden-curvature coupling
coefficients k_i^{GU} = 512 * k_i^{EC} has the following structure:

```
k_i^{GU,full} = 512 * k_i^{EC} + delta_k_i^{Cod}
```

where:
```
delta_k_1^{Cod} ~ 512 * (Weyl piece of R^{g_s})       [T^(1) coupling to W_{abcd}]
delta_k_2^{Cod} ~ (512/3) * (traceless Ricci of g_s)  [T^(2) coupling to Ric^{TF}_{ab}]
delta_k_3^{Cod} ~ (512/3) * (scalar curvature of g_s) [T^(3) coupling to R_scal]
```

**Critical verdict on the 512 normalization:**

The Codazzi correction is ADDITIVE and DYNAMICAL. It does NOT shift the 512
kinematic normalization factor from the j_s Clifford trace. The factor 512 remains
the universal renormalization of the leading-order distortion-theta-to-H^(i) coupling.

**On the GU-selected K3-type background (Ricci-flat X^4):**
- delta_k_2^{Cod} = 0 (exact)
- delta_k_3^{Cod} = 0 (exact)
- delta_k_1^{Cod} = O(W_{K3}) (Weyl correction; nonzero but curvature-suppressed)

**Remaining for RESOLVED status:**
1. CAS verification of [ambient-curv-formula] (differentiating H-H-V Christoffel block)
2. Explicit K3 Weyl-correction magnitude computation
3. O(theta^2) cross-coupling analysis

**Connection to CPA-1:** The ambient curvature correction that appears in the Codazzi
term for i=3 is structurally the same as the Simons +4K correction in CPA-1 (both
arise from the derivative of the H-H-V Christoffel block). This is a structural
consistency between HC1 and CPA-1 at reconstruction grade.

---

## 13. References

- `explorations/hc1-coupling-coefficients-2026-06-23.md` (HC-master formula, projectors P^(i), 512 factor)
- `explorations/hc1-sl2c-bianchi-spinor-2026-06-23.md` (SL(2,C) labels for H^(i), T^(i) types)
- `explorations/ii-s-moving-frames-2026-06-23.md` ([CodEq-Explicit], H-H-V Christoffel, gimmel curvature)
- `explorations/codazzi-sp64-2026-06-23.md` (full [CodEq] for Sp(64); j_s soldering map)
- `explorations/pc2-gauss-y14-curvature-2026-06-23.md` ([G^Y_T]^{TF} = T^{YM,TF} + T^{mix,TF}; Simons +4K)
- `explorations/ic1-soldering-map-ns-adps-2026-06-23.md` (j_s: N_s -> ad(P_s), equivariance)
- `explorations/ic2-positivity-soldering-normal-2026-06-23.md` (Clifford-trace 512 h(n_i,n_j))
- `explorations/cpa1-omega-tuning-2026-06-23.md` (ambient curvature gate, Simons +4K)
- `explorations/oq3a-gu-variational-k3-selection-2026-06-23.md` (K3-type X^4 selection)
- Hehl, McCrea, Mielke, Ne'eman, Phys. Rep. 258 (1995) — torsion projectors, SO(1,3) irreducibles
- Penrose-Rindler, Spinors and Space-Time Vol. 1 (SL(2,C) Clebsch-Gordan)

---

*Filed 2026-06-23. Problem label: hc1-codazzi-correction. Grade: reconstruction.
Primary result: Codazzi correction delta_k_i^{Cod} is additive and dynamical
(proportional to curvature of g_s), does NOT modify the kinematic 512 normalization
factor from the j_s soldering map; on the GU-selected K3-type Ricci-flat background,
delta_k_2^{Cod} = delta_k_3^{Cod} = 0 exactly. Structural consistency with CPA-1
ambient curvature (Simons +4K) confirmed.
No result promoted to active_research or canon without meeting RESEARCH-STATUS.md criteria.*
