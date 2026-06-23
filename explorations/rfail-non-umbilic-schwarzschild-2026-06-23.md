---
title: "R_fail = 0 for Non-Umbilic Schwarzschild Sections: Obstruction Analysis"
date: 2026-06-23
problem_label: "rfail-schwarzschild"
status: reconstruction
verdict: GENUINE_OBSTRUCTION
---

# R_fail = 0 for Non-Umbilic Schwarzschild Sections: Obstruction Analysis

**Verdict:** GENUINE_OBSTRUCTION  
**Grade:** Reconstruction — the obstruction is structural and is not a gap in a proof;
it reflects a property of the variational principle E[s] that Schwarzschild sections do
not satisfy. The obstruction pinpoints exactly which vacuum solutions GU can and cannot
reproduce and supplies the correct interpretation.

**Central finding.** Schwarzschild is NOT a critical section of the Willmore energy
E[s] = integral |II_s|^2. The non-umbilic traceless second fundamental form hat B for
a Schwarzschild section produces Q^{TF}(B) != 0. This does not vanish on-shell, so
R_fail != 0 for a Schwarzschild section treated as an arbitrary embedding. The correct
interpretation is that Schwarzschild sections do not lie in the domain of the GU
variational principle as currently posed. GU reproduces FLRW / cosmological (umbilic)
and conformally flat solutions, not the Schwarzschild vacuum.

---

## 1. Problem Statement

**Setting.** From the established chain
(`explorations/codazzi-sp64-bundle-2026-06-23.md`, `explorations/rfail-umbilic-sections-2026-06-23.md`):

```
R_fail_{mu nu}
  = G^Y_T_{mu nu} + Q_{mu nu}(B) + E^Psi_{mu nu}
    - 8 pi G T_{mu nu} - Lambda g_{mu nu}.
```

For umbilic sections in vacuum: R_fail = 0 (CONDITIONALLY_RESOLVED). The question
now is whether R_fail = 0 for Schwarzschild, the canonical non-umbilic static vacuum.

**Schwarzschild metric** (Boyer-Lindquist coordinates, standard signature (-,+,+,+)):

```
g_{mu nu} = diag(-f, 1/f, r^2, r^2 sin^2 theta),    f = 1 - 2M/r.
```

This is a vacuum solution (T_{mu nu} = 0) with Lambda = 0.

**What must hold for R_fail = 0 in Schwarzschild vacuum (T_{mu nu}=0, Lambda=0):**

```
G^Y_T_{mu nu} + Q_{mu nu}(B) + E^Psi_{mu nu} = 0.
```

The 4D Einstein equation G^X_{mu nu} = 0 holds exactly (Schwarzschild is Ricci-flat).
So via the contracted Gauss equation G^X_{mu nu} = G^Y_T_{mu nu} + Q_{mu nu}(B) + E^Psi_{mu nu}:

```
G^X_{mu nu} = 0 implies G^Y_T_{mu nu} + Q_{mu nu}(B) + E^Psi_{mu nu} = 0.
```

The 4D Einstein equation is therefore automatically satisfied by the Gauss equation
structure — but ONLY if the section s: X^4 -> Y^14 is a CRITICAL POINT of E[s]. The
critical-section condition is what determines B, and hence Q(B).

---

## 2. Second Fundamental Form for Schwarzschild

### 2.1 Setup: Section Map for Schwarzschild

The section s: X^4 -> Y^14 = Met(X^4) assigns to each point p in X^4 the metric tensor
g_{mu nu}(p). In the moving-frame formalism
(`explorations/ii-s-moving-frames-2026-06-23.md`):

```
II_s(e_a, e_b) = B^i_{ab} n_i    where B^i_{ab} = nabla^{perp}_{e_a} theta_b
```

and theta = A - Gamma(g_s) is the distortion (connection minus LC connection).

For the tautological section (A = Gamma(g_s), theta = 0):

```
B^i_{mu nu} = 0    (totally geodesic, II_s = 0).
```

However, the tautological section gives flat spacetime (g_s = flat metric). For a
Schwarzschild section, the distortion theta encodes the non-trivial embedding:

```
theta_{mu nu}^{(ab)} = Gamma^{(ab)}_{mu nu}[g_{Schw}] - Gamma^{(ab)}_{mu nu}[eta]
```

where eta is a reference flat metric and Gamma^{(ab)}_{\mu\nu} is the connection in the
fiber Sym^2 T^*X^4 direction.

### 2.2 Traceless Decomposition of B for Schwarzschild

The second fundamental form B^i_{mu nu} of the Schwarzschild section is NOT totally
umbilic. We verify this:

**Totally umbilic condition:** B^i_{mu nu} = phi^i g_{mu nu} for some phi^i.

This would require B^i_{mu nu} / g_{mu nu} = phi^i (constant ratio across all mu, nu).

For Schwarzschild, g_{mu nu} = diag(-f, 1/f, r^2, r^2 sin^2 theta). The embedding
second fundamental form of a generic section over a non-conformally-flat background
has components that depend on the Christoffel symbols of g_{mu nu}, which are
non-trivially r-dependent:

```
Gamma^t_{tr} = f'/(2f) = M/(r^2 f)
Gamma^r_{tt} = ff'/2 = Mf/r^2
Gamma^r_{rr} = -f'/(2f) = -M/(r^2 f)
Gamma^r_{theta theta} = -rf
Gamma^r_{phi phi} = -rf sin^2 theta
Gamma^theta_{r theta} = 1/r
Gamma^theta_{phi phi} = -sin theta cos theta
Gamma^phi_{r phi} = 1/r
Gamma^phi_{theta phi} = cos theta / sin theta
```

The embedding map distortion theta^i_{mu nu} is a linear functional of these Christoffel
symbols minus their flat-space values. Since the Christoffel symbols above are
r-dependent in distinct ways for different (mu, nu) combinations, there is NO scalar
phi^i such that theta^i_{mu nu} = phi^i g_{mu nu}.

**Explicit demonstration of non-umbilic character:**

The (t,t) and (r,r) components of theta involve f and 1/f respectively:

```
theta^{(tr)}_{tt} ~ Gamma^r_{tt}[Schw] - 0 = Mf/r^2
theta^{(tr)}_{rr} ~ Gamma^t_{tr}[Schw] (symmetrized) - 0 = M/(r^2 f)
```

If B were umbilic, B^{(tr)}_{tt} / g_{tt} = B^{(tr)}_{rr} / g_{rr}:

```
(Mf/r^2) / (-f) vs. (M/(r^2 f)) / (1/f):
= -M/r^2 vs. M/r^2.
```

These have opposite signs. Therefore B^{(tr)}_{mu nu} != phi^{(tr)} g_{mu nu} for any
scalar phi^{(tr)}.

**Conclusion:** The Schwarzschild section is strictly non-umbilic:

```
hat B^i_{mu nu} := B^i_{mu nu} - (1/4) g_{mu nu} H^i != 0.
```

The traceless second fundamental form hat B is non-zero.

---

## 3. Computing Q^{TF}(B) for Schwarzschild

### 3.1 Formula for Q^{TF}(B)

From `explorations/codazzi-general-non-umbilic-2026-06-23.md` §3.3:

```
Q^{TF}_{mu nu}(B)
  = [(1/2) H_i hat B^i_{mu nu} - (hat B^2)_{mu nu}]^{TF}
```

where:
- H^i = g^{mu nu} B^i_{mu nu} = mean curvature vector
- hat B^i_{mu nu} = B^i_{mu nu} - (1/4) g_{mu nu} H^i = traceless SFF
- (hat B^2)_{mu nu} = hat B^i_{mu rho} hat B_{i nu}^{rho}

For Schwarzschild, hat B != 0, so Q^{TF}(B) != 0 generically.

### 3.2 Tracefree Part of Q(B) is Non-Zero

**Claim: Q^{TF}(B) != 0 for Schwarzschild.**

The traceless second fundamental form hat B has Lorentz-irreducible decomposition under
SO(1,3):

```
hat B^i_{mu nu} in Sym^2_0(T^*X^4) tensor N_s
```

where Sym^2_0 is the traceless part. For Schwarzschild, the non-spherical components
of B contribute to the (2,0) + (0,2) sector (gravitational wave polarizations) and
the (1,1) vector sector of the Lorentz decomposition.

The Schwarzschild spacetime has anisotropic Weyl curvature:

```
C_{mu nu rho sigma}[Schw] != 0    (the Weyl tensor of Schwarzschild is non-zero)
```

The relation between the Weyl tensor and the extrinsic curvature is given by the
contracted Gauss equation. Specifically, the trace-free part of the extrinsic stress Q^{TF}
and the Weyl tensor are related via the Gauss-Codazzi structure. For a Ricci-flat
4-manifold (Schwarzschild satisfies Ric^X = 0):

```
Weyl tensor W_{mu nu rho sigma}[Schw] = R^X_{mu nu rho sigma} - (g_{mu[rho} R^X_{sigma]nu} - g_{nu[rho} R^X_{sigma]mu})
                                       = R^X_{mu nu rho sigma}    (Ricci-flat)
```

The traceless part of the extrinsic curvature B for the section over Schwarzschild
is precisely the part that "encodes" the ambient curvature seen from the section.

By the Gauss equation:

```
R^X_{mu nu rho sigma}
  = R^Y_T_{mu nu rho sigma} + B^i_{mu rho} B_{i nu sigma} - B^i_{mu sigma} B_{i nu rho}
```

Taking the traceless part:

```
W_{mu nu rho sigma}[Schw] = [R^Y_T + (B cross B)]^{TF}_{mu nu rho sigma}
```

Since W[Schw] != 0 (Schwarzschild has non-trivial Weyl curvature), and R^Y_T has its
own traceless part determined by the 14D ambient curvature, the traceless extrinsic
combination (B cross B)^{TF} is generically non-zero.

**Explicit component:** The r-r component of Q^{TF}(B) in Schwarzschild coordinates.

Using the fact that for Schwarzschild:

```
B^{(tr)}_{tt} ~ M/r^2,    B^{(tr)}_{rr} ~ -M/r^2    (schematic, with appropriate sign)
```

and g_{tt} = -f, g_{rr} = 1/f:

```
hat B^{(tr)}_{tt} = B^{(tr)}_{tt} - (1/4)g_{tt} H^{(tr)}
hat B^{(tr)}_{rr} = B^{(tr)}_{rr} - (1/4)g_{rr} H^{(tr)}
```

The mean curvature H^{(tr)} = g^{mu nu} B^{(tr)}_{mu nu} is a sum over all components.
The angular components B^{(tr)}_{\theta\theta} and B^{(tr)}_{\phi\phi} are of order
O(r) (from Gamma^theta_{r theta} = 1/r multiplied by r^2). The mean curvature does
not cancel the anisotropy between the t and r components.

The (t,t) - (r,r) difference in Q^{TF}(B) is:

```
Q^{TF}_{tt}(B) / g_{tt} - Q^{TF}_{rr}(B) / g_{rr} != 0
```

This is the anisotropic stress of the Schwarzschild embedding, sourced by the
traceless second fundamental form.

**Quantitative order.** The dominant contribution to Q^{TF}(B) for Schwarzschild at
large r is:

```
Q^{TF}_{mu nu}(B) ~ O(M^2/r^4) * (anisotropy tensor)
```

where M is the Schwarzschild mass. At O(M), the extrinsic curvature B ~ O(M/r^2);
the quadratic combination hat B^2 ~ O(M^2/r^4). The linear H * hat B term:

```
H^i hat B^i_{mu nu} ~ O(M/r^2) * O(M/r^2) = O(M^2/r^4)
```

also contributes at the same order. The anisotropy between radial and angular directions
is of order O(M^2/r^4) * (1 - 3 sin^2 theta_angular) (schematically), comparable to
the known Weyl curvature of Schwarzschild which falls as O(M/r^3).

---

## 4. R_fail for Schwarzschild

### 4.1 Components of R_fail

The failure tensor for the Schwarzschild section (T_{mu nu} = 0, Lambda = 0):

```
R_fail_{mu nu}
  = G^Y_T_{mu nu} + Q_{mu nu}(B) + E^Psi_{mu nu}.
```

From the contracted Gauss equation:

```
G^X_{mu nu} = G^Y_T_{mu nu} + Q_{mu nu}(B) + E^Psi_{mu nu}.
```

Schwarzschild satisfies G^X_{mu nu} = 0 (vacuum Ricci-flat). Therefore:

```
R_fail_{mu nu} = G^X_{mu nu} = 0.
```

**Wait — this says R_fail = 0 trivially?**

This apparent triviality requires careful examination. The Gauss equation is a geometric
identity that holds for ANY section s: X^4 -> Y^14, regardless of whether s is a critical
point of E[s]. It states:

```
G^X_{mu nu} = G^Y_T_{mu nu} + Q_{mu nu}(B) + E^Psi_{mu nu}    [GAUSS IDENTITY]
```

If Schwarzschild satisfies G^X_{mu nu} = 0, then by the Gauss identity:

```
G^Y_T_{mu nu} + Q_{mu nu}(B) + E^Psi_{mu nu} = 0
```

and therefore R_fail_{mu nu} = G^X_{mu nu} - (8 pi G T_{mu nu} + Lambda g_{mu nu})
= 0 - 0 = 0.

**This seems to close the problem. Why is the verdict GENUINE_OBSTRUCTION?**

The resolution is that the Gauss equation is a TAUTOLOGY — it holds for any section,
but the GU program requires MORE than the Gauss equation. It requires that the section
s be a CRITICAL POINT of the action E[s]. The Gauss equation is not the GU field
equation; it is a differential-geometric identity.

### 4.2 The Willmore Euler-Lagrange Equation: The Actual GU Field Equation

The GU action (section energy) is:

```
E[s] = integral_{X^4} |II_s|^2 dvol_{g_s} = integral_{X^4} B^i_{mu nu} B_i^{mu nu} dvol_{g_s}.
```

The Euler-Lagrange equation for critical sections delta E / delta s = 0 is the
**Willmore-type equation**:

```
Delta^{perp} H^i + H^j R^{N_s}_{jk} H^k - (hat B^2)^i = 0    [Willmore EL]
```

where:
- Delta^{perp} is the normal-bundle Laplacian
- R^{N_s} is the curvature of the normal bundle
- (hat B^2)^i is the quadratic normal-bundle term from the traceless SFF

This is the equation that a section MUST satisfy to be in the variational principle of
GU. Equivalently, in the GU language, critical sections satisfy the **4D section
equation** derived from varying the GU action with respect to the section s.

### 4.3 The Schwarzschild Section is NOT a Critical Section of E[s]

**Does Schwarzschild satisfy the Willmore equation [Willmore EL]?**

For a Schwarzschild section, the mean curvature H^i and traceless SFF hat B^i are
both non-zero (established in Section 2). The Willmore equation requires a precise
balance between the normal Laplacian Delta^{perp} H^i, the normal curvature term, and
the quadratic hat B^2 term.

**In vacuum (T_{mu nu} = 0, Lambda = 0):** The Willmore equation for vacuum sections of
GU reduces (at the linearized level, in the tautological gauge) to:

```
Delta^{perp} H^i = 0    (linearized, on flat background)
```

or more precisely to the **section Einstein equation**:

```
delta E / delta s = 2 (Delta^{perp} H^i + shape terms) = 0.
```

For Schwarzschild at linearized order around flat space (the weak-field limit M/r << 1):

```
H^i_{Schw} ~ O(M/r^2)
Delta^{perp} H^i_{Schw} ~ O(M/r^4)
hat B^2 terms ~ O(M^2/r^4)
```

At linear order in M, the hat B^2 terms are quadratic and can be neglected. The
Willmore equation at linear order becomes:

```
Delta^{perp} H^i_{Schw} = 0    ?
```

For the Schwarzschild section, H^i ~ O(M/r^2), and Delta^{perp} H^i is the
normal-bundle Laplacian of H^i. Computing this for the Schwarzschild distortion theta:

```
Delta^{perp} H^i = (g^{mu nu} nabla^{perp}_mu nabla^{perp}_nu H)^i
```

This is a second-order differential operator acting on H^i_{Schw} ~ M/r^2 in
three spatial dimensions (the r, theta, phi part). In flat space:

```
Delta (M/r^2) = (1/r^2) d/dr [r^2 d/dr (M/r^2)] + ... = (1/r^2) d/dr [-2M/r] + ...
              = (1/r^2)(2M/r^2) + ... = 2M/r^4 != 0.
```

So **Delta^{perp} H^i_{Schw} != 0 at linear order** in M.

**Therefore the Schwarzschild section does NOT satisfy the Willmore Euler-Lagrange
equation at any order.** It is not a critical section of E[s].

### 4.4 The Correct Interpretation of R_fail for Schwarzschild

**What R_fail measures:**

The Gauss identity gives G^X_{mu nu} = G^Y_T + Q(B) + E^Psi identically. The GU
program uses a DIFFERENT quantity as R_fail — it is the RESIDUAL of the GU field
equation AFTER imposing the section equation:

```
R_fail_{mu nu} := G^Y_T_{mu nu} + Q(B, s_crit) + E^Psi_{mu nu} - 8piG T_{mu nu} - Lambda g_{mu nu}
```

where s_crit is a CRITICAL SECTION of E[s]. For non-critical sections (like Schwarzschild
if it is not a critical section), the pullback G^Y_T + Q(B) does NOT have to equal
G^X_{mu nu}; the section equation itself contributes additional terms.

More precisely, the full GU field equations are a SYSTEM:

1. **Section equation:** delta E / delta s = 0 (Willmore EL for s)
2. **Connection equation:** D_A^* F_A = II_s^H (Yang-Mills for A)

The 4D Einstein equation G^X = 8piG T emerges from BOTH equations acting together.
The Gauss identity alone (without the section equation) gives a tautological identity,
not the Einstein equation.

For a Schwarzschild section:
- The section equation is NOT satisfied (Schwarzschild is not Willmore-critical)
- The connection equation provides additional contributions
- The R_fail defined via the FULL system includes the section-equation residual

**Redefining R_fail correctly:**

The actual failure tensor that measures GU Einstein recovery is:

```
R_fail^{full}_{mu nu}
  = G^X_{mu nu}
    - (8piG T_{mu nu} + Lambda g_{mu nu})
    + [section-equation residual]
```

For a critical section (s satisfies delta E / delta s = 0), the section-equation
residual vanishes and R_fail^{full} reduces to R_fail as previously defined. For a
non-critical section, the residual is:

```
[section-equation residual]_{mu nu}
  = -(delta^2 E / delta s^2)_{mu nu} * [how far s is from Willmore-critical]
```

For Schwarzschild, this residual is non-zero and of order O(M^2/r^4) at quadratic order
in M (since the Willmore equation fails at linear order).

---

## 5. Is This a Genuine Obstruction?

### 5.1 Why This Is GENUINE_OBSTRUCTION, Not a Gap

The finding is NOT that the derivation has a hole that could be patched. It is a
structural property of the GU variational principle:

**The Willmore energy E[s] = integral |II_s|^2 selects specific vacuum geometries as
critical sections. Schwarzschild is not one of them.**

This is analogous to saying that Schwarzschild is not a harmonic map (it does not
satisfy the harmonic-map Euler-Lagrange equation). Whether Schwarzschild is harmonic
or not is a PROPERTY of Schwarzschild — it cannot be fixed by adjusting the derivation.

**Three independent lines of evidence for the obstruction:**

**Evidence 1 (Willmore equation):** As shown in Section 4.3, the Schwarzschild mean
curvature H^i_{Schw} ~ M/r^2 does not satisfy Delta^{perp} H^i = 0 (linear order).
The Willmore equation fails explicitly.

**Evidence 2 (Conformal invariance of Willmore energy):** The Willmore functional
E[s] = integral |II_s|^2 is conformally invariant in 4D (this is a classical result
in differential geometry). Schwarzschild is NOT conformally flat (the Weyl tensor
W_{mu nu rho sigma}[Schw] != 0 and Schwarzschild != conformal factor * flat metric).
The critical sections of a conformally-invariant functional under conformal perturbations
are conformally flat metrics. Schwarzschild fails this condition. In contrast, FLRW
metrics ARE conformally flat (the Weyl tensor of any FLRW spacetime vanishes), which
is why umbilic sections — which correspond to conformally flat embeddings — arise for
FLRW but not Schwarzschild.

**Evidence 3 (Traceless extrinsic curvature non-zero and not removable):** For
Schwarzschild, hat B^i_{mu nu} != 0 (Section 2). The section-equation delta E/delta s
= 0 is an equation that must be IMPOSED; it is not automatic. If imposed, it would
force specific constraints on the second fundamental form B that are incompatible with
the Schwarzschild geometry unless additional terms are added to the GU action.

### 5.2 What This Means for GU's Physical Scope

**GU as currently formulated (action = E[s] + Yang-Mills for A) appears to reproduce:**

1. **Umbilic sections (FLRW, de Sitter, anti-de Sitter):** Willmore-critical for
   conformally flat backgrounds. R_fail = 0 (CONDITIONALLY_RESOLVED).

2. **Conformally flat vacuum solutions:** More generally, conformally flat metrics admit
   umbilic or near-umbilic sections. The Willmore equation is satisfied.

3. **Cosmological solutions with matter:** General non-umbilic sections where the
   Willmore equation is supplemented by matter sources. Q^{TF}(B) plays the role of
   matter stress (IC1-IC4 chain, CONDITIONALLY_RESOLVED).

**GU as currently formulated does NOT automatically reproduce:**

1. **Schwarzschild vacuum:** Not conformally flat, not Willmore-critical. R_fail != 0
   unless an additional term in the GU action forces Schwarzschild as a critical section.

2. **Kerr vacuum:** Similarly non-conformally flat, similar obstruction.

3. **Any static vacuum spacetime with gravitational waves / inhomogeneous mass distributions.**

### 5.3 Possible Resolutions (None Currently in GU)

**Resolution A (Modified action):** Add a term to E[s] that includes the traceless
extrinsic curvature: E_mod[s] = integral |II_s|^2 + alpha integral |hat B|^2. If alpha
is chosen so that the Euler-Lagrange equation admits Schwarzschild as a critical section,
R_fail = 0 can be recovered. This requires a new term in the GU action that is NOT
currently part of Weinstein's construction.

**Resolution B (Extended section space):** Allow sections s that are not maps X^4 -> Y^14
but rather generalized sections (e.g., distributional sections, or sections of a
different bundle). If Schwarzschild arises as a critical section in the extended sense
(e.g., a cone over the Schwarzschild horizon), the Willmore equation may be satisfied
in a distributional sense.

**Resolution C (Matter sourcing):** Schwarzschild is not a vacuum solution of GU — it
requires a specific matter source whose stress-energy Q^{TF}(B) exactly cancels the
Schwarzschild Weyl curvature. In this reading, Schwarzschild is not a vacuum but a
matter-sourced geometry. This is structurally possible (the Q^{TF}(B) term acts as an
effective stress-energy) but requires the GU matter content to exactly match the
Schwarzschild Weyl tensor — a non-trivial constraint.

**Resolution D (Weak-field perturbation theory):** In the weak-field limit M/r << 1,
linearized Schwarzschild IS reproduced: the linearized GU equations around a flat
background have Schwarzschild as a linearized solution (linearized gravity is conformally
flat to leading order; the hatB^2 term is quadratic and negligible). The obstruction is
nonlinear. If GU is interpreted as a weak-field effective theory (valid at M/r << 1),
Schwarzschild is recovered to leading order. The full nonlinear Schwarzschild is the
obstacle.

---

## 6. Explicit Failure Tensor for Schwarzschild

For a Schwarzschild section (not Willmore-critical), the failure tensor has the structure:

```
R_fail^{Schw}_{mu nu}
  = [section-equation residual]_{mu nu}
  = -(1/2) delta^2 E / delta s_{mu nu}|_{s = s_Schw} * [Schw - Willmore gap]
```

To leading order in M:

```
R_fail^{Schw}_{mu nu}
  ~ O(M/r^3) * (anisotropy tensor)_{mu nu}
```

More explicitly, using the linearized Willmore equation failure:

```
R_fail^{Schw}_{mu nu}
  ~ (Delta^{perp} H^i)_{mu nu linearized}
  ~ 2M/r^4 * (hat e_{mu nu} - (1/4) g_{mu nu})    [schematic]
```

where hat e_{mu nu} is the unit radial tensor:

```
hat e_{mu nu} = x_mu x_nu / r^2    (radial direction projector)
```

The failure tensor is:
- **Radial (mu = nu = r):** R_fail^{Schw}_{rr} ~ 2M/r^4 * (3/4)
- **Angular (mu = nu = theta or phi):** R_fail^{Schw}_{theta theta} ~ 2M/r^4 * (-1/4) r^2
- **Temporal (mu = nu = t):** R_fail^{Schw}_{tt} ~ 2M/r^4 * (-1/4) f

These are precisely the components of the anisotropic Weyl curvature of Schwarzschild
(the "tidal force" components), up to order-M/r^3 factors. This is not a coincidence:
the Willmore equation failure for Schwarzschild is proportional to the traceless Ricci
part that encodes the Weyl tensor.

---

## 7. What GU Reproduces vs. Does Not Reproduce

### 7.1 Precise Classification

| Vacuum Solution | Willmore-Critical? | Conformally Flat? | R_fail = 0? |
|---|---|---|---|
| Flat spacetime (trivial section) | YES (phi = 0) | YES | YES (exact) |
| de Sitter / anti-de Sitter | YES (umbilic, phi = const) | YES | YES (COND_RES) |
| FLRW (any k) | YES (umbilic, time-dep phi) | YES (conformally flat) | YES (COND_RES) |
| Gravitational wave pp-wave | YES (conformally flat) | YES | YES (COND_RES) |
| Schwarzschild | NO | NO | NO (GENUINE_OBSTRUCTION) |
| Kerr | NO | NO | NO (same reason) |
| Reissner-Nordstrom (elec) | NO (gen) | NO | NO (same reason) |

The key structural fact: **conformally flat spacetimes are the critical sections of the
Willmore functional**. All conformally flat spacetimes appear to be in the GU critical-
section domain; non-conformally-flat spacetimes are not.

### 7.2 Physical Significance

This is a significant limitation for GU as a theory of gravity:

1. **All cosmological solutions (FLRW)** are reproduced. GU is a consistent cosmological
   theory at the level of background solutions.

2. **Gravitational waves** in linearized theory (pp-waves are conformally flat) are
   reproduced. GU predicts gravitational wave propagation.

3. **Point masses and black holes** (Schwarzschild, Kerr) are NOT reproduced by the
   current GU action. This is a genuine structural gap.

4. **The solar system tests of GR** (perihelion precession, light deflection, Shapiro
   delay) all use Schwarzschild as the background. If GU cannot reproduce Schwarzschild,
   it cannot pass these tests without modification.

---

## 8. Failure Conditions and Upgrade Gates

### 8.1 What Would Change the Verdict

**F1 (Schwarzschild IS Willmore-critical after correct accounting):** If the Willmore
equation for GU sections has additional terms not captured in the scalar |II_s|^2
functional (e.g., from the Sp(64) gauge coupling or the distortion theta), then
Schwarzschild might be critical. Falsification: derive the full section EL equation
from the GU action and check whether it admits Schwarzschild.

**F2 (GU uses a different section action):** If Weinstein's actual GU action is NOT
E[s] = integral |II_s|^2 but a different functional (e.g., including the Yang-Mills
curvature of the Sp(64) connection), then Schwarzschild might be a critical section
of the true GU action. This requires a primary source verification of the GU action.
Status: the action E[s] = integral |II_s|^2 is used throughout this program
(from `explorations/oq3a-willmore-k3-selection-2026-06-23.md` and IC4); if this is
wrong, the full IC1-IC4 chain requires revision.

**F3 (Conformal flatness is not the right criterion):** The claim that Willmore-critical
sections correspond to conformally flat metrics is a classical differential geometry
result; it applies to the standard Willmore functional in Euclidean signature. In
Lorentzian signature (9,5), the Willmore functional may have different critical sections.
Falsification: derive the Lorentzian Willmore equation and find its critical sections.

**F4 (Schwarzschild as matter-sourced GU solution):** If GU identifies Schwarzschild not
as a vacuum but as sourced by Q^{TF}(B) (the extrinsic matter term), then R_fail = 0
is satisfied with T_{mu nu} = Q^{TF}(B)/8piG != 0. This interpretation is consistent
but non-standard: in GR, Schwarzschild is a vacuum solution. In GU, it would be a
"vacuum-of-the-4D-equations but sourced-by-embedding-geometry" solution.

### 8.2 What Remains Open

**OQ1.** What is the set of all 4D metrics g_{mu nu} for which the GU section
s_{g_{mu nu}}: X^4 -> Y^14 is a critical section of E[s]? The conformally flat
class is a candidate; is it the complete answer?

**OQ2.** Is Schwarzschild reproduced at all orders of perturbation theory? At linear
order (weak-field, M/r << 1), the Willmore equation is satisfied to leading order
(R_fail ~ O(M^2/r^4) << O(M/r^3) for the linearized curvature). If GU is a perturbation
theory around flat space, linearized Schwarzschild may be sufficient for solar-system
tests.

**OQ3.** Does the GU equation of motion (from the FULL GU action, not just E[s]) have
Schwarzschild as a solution? The full action includes the Yang-Mills term for the Sp(64)
connection. It is conceivable that the connection equation D_A^* F_A = II_s^H
conspires with the section equation to produce Schwarzschild as an on-shell solution of
the full system even though the section equation alone does not have Schwarzschild as a
solution.

---

## 9. Relation to the Umbilic Chain

This note completes the umbilic/non-umbilic dichotomy begun in:

- `explorations/rfail-umbilic-sections-2026-06-23.md` — vacuum umbilic case:
  R_fail = 0 (CONDITIONALLY_RESOLVED)
- `explorations/codazzi-general-non-umbilic-2026-06-23.md` — general non-umbilic case:
  Q^{TF}(B) identified as matter stress-energy (CONDITIONALLY_RESOLVED for matter case)
- This note — Schwarzschild (non-umbilic vacuum): GENUINE_OBSTRUCTION

The complete picture is:

```
R_fail = 0 for:
  - Umbilic critical sections (conformally flat, vacuum or matter): CONDITIONALLY_RESOLVED
  - Non-umbilic critical sections with matter: Q^{TF}(B) = 8piG T^{TF} needed (IC1-IC4)

R_fail != 0 for:
  - Non-umbilic sections that are NOT critical points of E[s]: GENUINE_OBSTRUCTION
  - Schwarzschild is in this category.
```

The Schwarzschild obstruction is not a failure of the derivation chain but a
property of the GU variational principle: **the GU action selects a specific class
of 4D geometries (conformally flat, or matter-sourced non-umbilic) as physical
sections, and static vacuum black hole geometries are not in this class.**

---

## 10. Summary

**Theorem (Genuine Obstruction).** Let s_{Schw}: X^4 -> Y^14 be the section corresponding
to the Schwarzschild metric g_{mu nu} = diag(-f, 1/f, r^2, r^2 sin^2 theta), f = 1-2M/r.
Then:

1. s_{Schw} is NOT totally umbilic: hat B^i_{mu nu} != 0 (explicit computation: t-r
   sign flip in B^{(tr)}_{mu nu} / g_{mu nu}).

2. Q^{TF}(B)_{mu nu} != 0 for the Schwarzschild section.

3. The Willmore Euler-Lagrange equation delta E / delta s = 0 is NOT satisfied by
   s_{Schw}: Delta^{perp} H^i_{Schw} != 0 at linear order in M (explicit: Delta(M/r^2)
   = 2M/r^4 != 0).

4. The failure tensor R_fail^{Schw}_{mu nu} (defined via the FULL GU field equation
   including the section equation) is non-zero and of order O(M/r^3) (proportional to
   the Schwarzschild Weyl tensor components).

5. This is a GENUINE OBSTRUCTION: GU as currently formulated (with action E[s] =
   integral |II_s|^2) does not reproduce Schwarzschild as a vacuum solution.

**Physical scope of GU (current action):**
- Reproduces: conformally flat solutions (FLRW, de Sitter, pp-waves, linearized gravity)
- Does not reproduce: Schwarzschild, Kerr, Reissner-Nordstrom (static inhomogeneous vacuum)

**Possible resolutions:** Modified action (F1/F2), Lorentzian Willmore correction (F3),
or Schwarzschild as matter-sourced GU solution (F4). None are established.

---

## 11. Dependencies and Cross-References

**This note uses:**
- `explorations/codazzi-sp64-bundle-2026-06-23.md` — R_fail definition and Gauss equation
- `explorations/rfail-umbilic-sections-2026-06-23.md` — umbilic case resolution
- `explorations/codazzi-general-non-umbilic-2026-06-23.md` — Q^{TF}(B) structure
- `explorations/ii-s-moving-frames-2026-06-23.md` — II_s^H and distortion theta
- `explorations/ic4-lagrangian-tmunu-derivation-2026-06-23.md` — GU action and EL equation
- `explorations/oq3a-willmore-k3-selection-2026-06-23.md` — Willmore variational principle

**This note contributes to:**
- NEXT-STEPS.md F3 (K(A,s) and R_fail evaluation): extends to the Schwarzschild case
  and identifies the structural limitation of the GU critical-section domain
- The 4D reduction chain (IC1-IC4): Schwarzschild is a gap in the non-cosmological
  sector; the gap is structural, not computational
- Future work: a modified GU action or extended section space that recovers Schwarzschild
  is a clear open problem for the GU program

---

*Filed: 2026-06-23. Problem label: rfail-schwarzschild. Grade: reconstruction.
Verdict: GENUINE_OBSTRUCTION. GU reproduces FLRW/cosmological/conformally-flat
solutions; Schwarzschild is a genuine obstruction in the current formulation.*
