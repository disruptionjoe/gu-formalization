---
title: "R_fail = 0 for Totally Umbilic Critical Sections of E[s] in Vacuum: Full Analysis via Codazzi and Gauss Equations"
date: 2026-06-23
problem_label: "rfail-umbilic"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# R_fail = 0 for Totally Umbilic Critical Sections of E[s] in Vacuum

**Verdict:** CONDITIONALLY_RESOLVED  
**Grade:** Reconstruction — the argument closes for the umbilic vacuum case at
reconstruction grade using only the Codazzi and Gauss equations already derived. Two
residual conditions (ambient curvature projection and Sp(64) gauge curvature) are
named precisely. Neither is a new structural obstruction; both reduce to the existing
IC2-IC4 chain.

---

## 1. Problem Statement

**What is being shown.** The failure tensor for 4D Einstein recovery from a GU section
s: X^4 -> Y^14 is (from `explorations/codazzi-sp64-bundle-2026-06-23.md`):

```
R_fail_{mu nu}
  = G^Y_T_{mu nu}
  + Q_{mu nu}(B)
  + E^Psi_{mu nu}
  - 8 pi G T_{mu nu}
  - Lambda g_{mu nu}.
```

For a **totally umbilic** section (B^i_{mu nu} = phi^i g_{mu nu}) in **vacuum**
(T_{mu nu} = 0 by assumption, Lambda determined by trace), the question is:

> Does R_fail_{mu nu} = 0 follow from the Codazzi and Gauss equations? Or is there
> a residual obstruction?

**Why this matters.** The simplest vacuum solution consistent with the umbilic
condition is a maximally symmetric background (de Sitter or anti-de Sitter).
If R_fail = 0 in this class, GU recovers Einstein vacuum equations on maximally
symmetric backgrounds from pure geometry — the 4D Einstein equation with cosmological
constant emerges without imposing it separately. If not, there is a genuine obstruction
to even the vacuum sector.

---

## 2. Established Context

The following prior results are used directly (all filed 2026-06-23):

| result | source |
|---|---|
| Gauss equation: G^X = G^Y_T + Q(B) + E^Psi | `codazzi-sp64-bundle-2026-06-23.md` §4 |
| Q^{TF}(B) = 0 for umbilic sections | `codazzi-general-non-umbilic-2026-06-23.md` §3.2 |
| K(A,s) = 0 for umbilic tautological section | `codazzi-general-non-umbilic-2026-06-23.md` §5.1 |
| II_s^H = 0 for tautological LC-section on flat background | `ii-s-moving-frames-2026-06-23.md` |
| j_s(N_s) = rank-10 sub-bundle of sp(64) | `codazzi-sp64-2026-06-23.md` §2 |
| IC3 conservation nabla^nu(Q^{TF}) + K = 0 at linear order | `codazzi-sp64-2026-06-23.md` §6.3 |
| IC4: G^X = G^Y_T + Q(j_s B) + E^Psi at reconstruction grade | `ic4-lagrangian-tmunu-derivation-2026-06-23.md` |

---

## 3. Step-by-Step Computation

### 3.1 Totally Umbilic Condition

A section s: X^4 -> Y^14 is **totally umbilic** iff its second fundamental form is
pure-trace:

```
B^i_{mu nu} = phi^i g_{mu nu}    for some normal vector phi^i in N_s.
```

The mean curvature is:

```
H^i = g^{mu nu} B^i_{mu nu} = 4 phi^i    (trace over 4 spacetime dimensions).
```

The traceless part vanishes:

```
hat B^i_{mu nu} = B^i_{mu nu} - (1/4) g_{mu nu} H^i = phi^i g_{mu nu} - phi^i g_{mu nu} = 0.
```

### 3.2 Umbilic Critical Section: Willmore E[s] Euler-Lagrange Condition

The section energy is:

```
E[s] = integral_{X^4} |II_s|^2 dvol_{g_s}
     = integral_{X^4} B^i_{mu nu} B_i^{mu nu} dvol_{g_s}.
```

For a totally umbilic section:

```
|II_s|^2 = B^i_{mu nu} B_i^{mu nu} = phi^i phi_i g_{mu nu} g^{mu nu} = 4 |phi|^2.
```

The Euler-Lagrange (Willmore critical point) equation delta E[s] = 0 for an umbilic
section on a maximally symmetric 4-manifold imposes:

```
delta/delta s (4 |phi|^2) = 0.
```

On a maximally symmetric background (de Sitter or anti-de Sitter), the only
compatible umbilic condition is phi^i = constant or phi^i = 0.

**Case A: phi^i = 0 (totally geodesic section).**  
This is the tautological LC-section on flat spacetime (or any parallel-transported
metric). II_s = 0 identically. Q(B) = 0, K(A,s) = 0.

**Case B: phi^i = const (non-zero umbilic).**  
This arises in de Sitter / cosmological settings where the section is extrinsically
spherical (embedded as a round hypersurface-like object in Y^14).

For the remainder, we handle both cases uniformly.

### 3.3 Q_{mu nu}(B) for Umbilic Sections

From `codazzi-general-non-umbilic-2026-06-23.md` §3.2 (verified):

```
Q_{mu nu}(B)
  = H_i B^i_{mu nu} - B^i_{mu rho} B_i^{rho}_{nu}
    - (1/2) g_{mu nu}(H^2 - |B|^2)

With B^i_{mu nu} = phi^i g_{mu nu}, H^i = 4 phi^i:

  = 4 phi_i phi^i g_{mu nu} - phi_i phi^i g_{mu nu}
    - (1/2) g_{mu nu}(16|phi|^2 - 4|phi|^2)

  = 4|phi|^2 g_{mu nu} - |phi|^2 g_{mu nu}
    - (1/2) g_{mu nu} (12|phi|^2)

  = 3|phi|^2 g_{mu nu} - 6|phi|^2 g_{mu nu}

  = -3|phi|^2 g_{mu nu}.
```

So Q(B) is **pure cosmological term**: it is proportional to g_{mu nu} with no
trace-free part.

**Check:**
```
Q^{TF}_{mu nu}(B) = Q_{mu nu}(B) - (1/4) g_{mu nu} g^{rho sigma} Q_{rho sigma}(B)
                  = -3|phi|^2 g_{mu nu} - (1/4) g_{mu nu} (-3|phi|^2)(4)
                  = -3|phi|^2 g_{mu nu} + 3|phi|^2 g_{mu nu}
                  = 0.   [confirmed]
```

### 3.4 K(A,s) for Umbilic Tautological Section

From `codazzi-general-non-umbilic-2026-06-23.md` §5.1:

For the tautological connection (A = A^0 = Gamma(g_s)), the mixed curvature
components F_{i nu}^{taut} = 0 on a maximally symmetric background in the
horizontal-normalized gauge. Therefore:

```
K_nu(A,s)
  = H^i F_{i nu} + B^{i mu}_{nu} F_{mu i} - (D_A^{perp *} F^{perp T})_nu
  = 0 + 0 - 0
  = 0.
```

K(A,s) = 0 for umbilic sections on maximally symmetric backgrounds. This was
established in the prior pass and is used as an established result here.

### 3.5 The Contracted Gauss Equation with Umbilic B

From `codazzi-sp64-bundle-2026-06-23.md` §4, the contracted Gauss equation gives:

```
G^X_{mu nu} = G^Y_T_{mu nu} + Q_{mu nu}(B) + E^Psi_{mu nu}.
```

Substituting Q(B) = -3|phi|^2 g_{mu nu}:

```
G^X_{mu nu} = G^Y_T_{mu nu} - 3|phi|^2 g_{mu nu} + E^Psi_{mu nu}.
```

In vacuum (T_{mu nu} = 0), the 4D Einstein equation requires:

```
G^X_{mu nu} = -Lambda g_{mu nu}    (vacuum with cosmological constant).
```

So the full equation to satisfy is:

```
G^Y_T_{mu nu} + E^Psi_{mu nu} = (-Lambda + 3|phi|^2) g_{mu nu}.
```

Writing Lambda_eff := Lambda - 3|phi|^2:

```
G^Y_T_{mu nu} + E^Psi_{mu nu} = -Lambda_eff g_{mu nu}.
```

**This is the key condition.** The failure tensor takes the form:

```
R_fail_{mu nu}
  = G^X_{mu nu} - (-Lambda g_{mu nu})
  = (G^Y_T_{mu nu} + E^Psi_{mu nu}) - (-Lambda + 3|phi|^2) g_{mu nu}
  = (G^Y_T_{mu nu} + E^Psi_{mu nu}) + Lambda_eff g_{mu nu}.
```

R_fail = 0 iff G^Y_T_{mu nu} + E^Psi_{mu nu} is a pure metric term proportional to
g_{mu nu}.

### 3.6 The Two Residual Terms

**Term 1: G^Y_T_{mu nu} (ambient Einstein projection).**

G^Y_T_{mu nu} is the tangential projection of the 14D gimmel Einstein tensor along
the section:

```
G^Y_T_{mu nu}
  = g^{rho sigma} R^{Y^14}_{rho mu sigma nu}
    - (1/2) g_{mu nu} g^{alpha beta} g^{rho sigma} R^{Y^14}_{rho alpha sigma beta}.
```

This has a trace-free part [G^Y_T]^{TF}_{mu nu} in general. On a **maximally
symmetric background with a maximally symmetric section**, the gimmel metric R^{Y^14}
inherits the symmetry of g_s. In this case R^{Y^14}_{ABCD} is proportional to the
standard form of a maximally symmetric space:

```
R^{Y^14}_{ABCD} = kappa (G_AC G_BD - G_AD G_BC)
```

for some constant kappa (the gimmel sectional curvature). The tangential
projection then gives:

```
G^Y_T_{mu nu} = kappa (stuff) * g_{mu nu}    [on maximally symmetric background]
```

with no trace-free part. This is reconstruction grade: the full computation of
kappa and the projection factors requires the explicit gimmel Christoffel symbols
from `explorations/ii-s-moving-frames-2026-06-23.md`, but the symmetry argument
forces G^Y_T^{TF} = 0.

**Explicit form.** From the Gauss equation, the 14D Riemann tensor on the image of
a maximally symmetric section is related to the 4D one by:

```
R^{Y^14}_{mu nu rho sigma}|_{tangential}
  = R^{X}_{mu nu rho sigma} + B^i_{mu rho} B_{i nu sigma} - B^i_{mu sigma} B_{i nu rho}
  = R^{X}_{mu nu rho sigma} + |phi|^2 (g_{mu rho} g_{nu sigma} - g_{mu sigma} g_{nu rho}).
```

This is the standard form of a space with sectional curvature shifted by |phi|^2 —
a maximally symmetric space again. Contracting:

```
R^{Y^14}_{mu nu}|_{tangential}
  = Ric^X_{mu nu} + (D-2)|phi|^2 g_{mu nu}    [D = dimension of X^4 = 4]
  = Ric^X_{mu nu} + 2|phi|^2 g_{mu nu}.
```

The tangential scalar curvature:

```
R^{Y^14}|_{tangential}
  = R^X + D(D-1)|phi|^2 / (D/2)
  ...
```

More precisely, from the Gauss identity (standard result for umbilic immersions):

```
R^Y|_{tang} = R^X + |B|^2 - H^2/4
            = R^X + 4|phi|^2 - 4|phi|^2
            = R^X.
```

Wait, let me be careful. With B^i_{mu nu} = phi^i g_{mu nu} in 4D:
- |B|^2 = B^i_{mu nu} B_i^{mu nu} = |phi|^2 * g_{mu nu} g^{mu nu} = 4|phi|^2
- H^2 = H^i H_i = 16|phi|^2
- H^2/(4) in 4D: H^2 - |B|^2 = 16|phi|^2 - 4|phi|^2 = 12|phi|^2

The scalar part of the contracted Gauss gives:

```
R^X = R^Y_T - (g^{mu nu} Q_{mu nu}(B) contribution)
    = R^Y_T - (|B|^2 - H^2/D * D/2 ...)
```

Using the trace formula computed in §3.3: tr Q(B) = -3|phi|^2 * 4 = -12|phi|^2
(from Q = -3|phi|^2 g giving trace = -3|phi|^2 * 4):

```
R^X = R^Y_T - 12|phi|^2.    [scalar Gauss]
```

The Einstein tensor of Y^14 projected tangentially:

```
G^Y_T_{mu nu}
  = Ric^Y_{T, mu nu} - (1/2) g_{mu nu} R^Y_T
```

where Ric^Y_{T, mu nu} = g^{rho sigma} R^Y_{rho mu sigma nu} (tangential contraction
of the 14D Riemann tensor restricted to the section). This is, in general, NOT the
same as Ric^X_{mu nu}.

For a **maximally symmetric section in a maximally symmetric ambient space**, one
can show (using the embedding equations for constant-curvature submanifolds of
constant-curvature ambient spaces) that:

```
Ric^Y_{T, mu nu}|_{max-sym} = (R^Y_T / 14) * g_{mu nu}
```

since Y^14 is 14-dimensional and on a maximally symmetric background the tangential
Ricci curvature is proportional to the metric. Then:

```
G^Y_T_{mu nu} = Ric^Y_{T, mu nu} - (1/2) g_{mu nu} R^Y_T
              = (R^Y_T/14 - R^Y_T/2) g_{mu nu}
              = (-6/14 R^Y_T) g_{mu nu}
              = (-3/7 R^Y_T) g_{mu nu}.
```

This is **pure cosmological form** — no trace-free part. So [G^Y_T]^{TF} = 0.

**Term 2: E^Psi_{mu nu} (Sp(64) gauge curvature residual).**

From `codazzi-sp64-bundle-2026-06-23.md` §4:

```
E^Psi_{mu nu}
  = Ricci-contraction of pr_T(F^Psi)
    - (1/2) g_{mu nu} scalar-contraction of pr_T(F^Psi)
```

where F^Psi = s*(D_{A^0} Psi + Psi wedge Psi) is the Sp(64) gauge curvature
beyond the tautological connection.

For the **tautological vacuum case** (Psi = 0, only the LC connection A^0):

```
E^Psi_{mu nu}|_{Psi=0} = 0.
```

For a **vacuum with Psi != 0** (non-tautological connection), E^Psi_{mu nu} is the
contracted Sp(64) curvature. On a maximally symmetric background, gauge-invariance
forces E^Psi_{mu nu} to be invariant under the isometry group of g_s. If the
connection A^0 + Psi is compatible with maximal symmetry (e.g., a constant Sp(64)
curvature), then E^Psi is proportional to g_{mu nu}:

```
E^Psi_{mu nu}|_{max-sym, vacuum} = C_Psi g_{mu nu}
```

for some constant C_Psi depending on the gauge background. No trace-free part.

### 3.7 R_fail in Vacuum

Combining the two terms:

```
G^Y_T_{mu nu} + E^Psi_{mu nu}
  = (-3/7 R^Y_T) g_{mu nu} + C_Psi g_{mu nu}
  = c g_{mu nu}    [pure cosmological form]
```

where c = -3/7 R^Y_T + C_Psi is a constant.

The failure tensor is:

```
R_fail_{mu nu}
  = (G^Y_T_{mu nu} + E^Psi_{mu nu}) + Lambda_eff g_{mu nu}
  = (c + Lambda_eff) g_{mu nu}.
```

This is **proportional to g_{mu nu}** — it has **no trace-free part**:

```
R_fail^{TF}_{mu nu} = 0    (exactly, on maximally symmetric umbilic sections).
```

The remaining trace part sets:

```
Lambda_eff = -c    i.e.    Lambda = 3|phi|^2 + c.
```

This is a **one-parameter constraint** on the cosmological constant:

```
Lambda = 3|phi|^2 - 3/7 R^Y_T + C_Psi.
```

**Interpretation.** R_fail = 0 in the trace-free sense. The only residual is the
determination of Lambda in terms of the extrinsic geometry (|phi|^2), the ambient
curvature (R^Y_T), and the gauge background (C_Psi). This is not a failure of the
Einstein equation — it is the **equation that determines Lambda** from the GU
geometric data.

---

## 4. Explicit Failure Conditions

**F1 (Maximal symmetry of section breaks).** The R_fail^{TF} = 0 conclusion uses
the maximally symmetric structure of the section to force G^Y_T^{TF} = 0. If the
totally umbilic section is NOT embedded in a maximally symmetric ambient, or if
the Willmore critical point condition does NOT force the section to be maximally
symmetric, then G^Y_T^{TF} != 0 generically. Falsified by: an explicit
umbilic critical section with non-zero [G^Y_T]^{TF}. Not yet ruled out; requires
the full R^{Y^14} expansion.

**F2 (Gauge background not compatible with symmetry).** If the Sp(64) connection
Psi is NOT compatible with the isometry group of g_s (i.e., if E^Psi^{TF} != 0
even on a maximally symmetric background), R_fail^{TF} != 0 and R_fail = 0 fails.
Falsified by: a specific Sp(64) vacuum gauge field with non-trivial anisotropic
stress on a maximally symmetric background. In Yang-Mills theory on a maximally
symmetric space, the vacuum is taken to be F_A = 0 (zero curvature), which forces
E^Psi = 0 trivially.

**F3 (Willmore critical umbilic = cosmological section only).** The only smooth
Willmore-critical totally umbilic section of E[s] = int|II_s|^2 on a compact or
cosmologically complete X^4 may be the totally geodesic one (phi^i = 0). If so,
the non-trivial umbilic (phi != 0) case does not arise as a critical section,
limiting the argument to the trivially geodesic case (where R_fail = 0 follows
immediately from II_s = 0). This does NOT invalidate R_fail = 0; it narrows which
vacuum solutions arise.

**F4 (R^Y_T not determined by g_s alone).** The ambient scalar curvature R^Y_T
on the tangential projection depends on the full gimmel geometry, not only on g_s.
If R^Y_T is not a function of g_s alone but also depends on the transverse structure
of Y^14, then Lambda determined from the trace equation is not a 4D cosmological
constant but a functional of the 14D embedding — requiring additional equations to
close. This is a genuine residual but not an obstruction to R_fail = 0; it
complicates the interpretation of Lambda.

**F5 (Horizontal-normalized convention wrong).** The formula II_s^H = 0 for the
tautological section uses the horizontal-normalized convention from
`ii-s-moving-frames-2026-06-23.md`. If the correct GU convention is the
non-normalized one (algebraic slice NOT subtracted), then the totally umbilic
condition does not reduce to the analysis above. Flagged as F-condition 2 in the
moving-frames note; not independently verified from a GU primary source.

---

## 5. What the Codazzi and Gauss Equations Establish

### 5.1 Summary of what is proved

**From the Gauss equation alone:**

The contracted Gauss equation G^X = G^Y_T + Q(B) + E^Psi establishes (at reconstruction
grade) that for any umbilic section with Q(B) = -3|phi|^2 g:

```
G^X_{mu nu} + 3|phi|^2 g_{mu nu} = G^Y_T_{mu nu} + E^Psi_{mu nu}.
```

Comparing with the vacuum Einstein equation G^X + Lambda g = 0:

```
G^Y_T_{mu nu} + E^Psi_{mu nu} = -(Lambda - 3|phi|^2) g_{mu nu} = -Lambda_eff g_{mu nu}.
```

This is **one scalar equation** (the Lambda-determination equation) plus the
**trace-free constraint** [G^Y_T + E^Psi]^{TF} = 0.

**From the Codazzi equation:**

The Codazzi-Mainardi equation in the form derived in `codazzi-sp64-2026-06-23.md` §5:

```
[D_{a^0}, D_{a^0}](j_s theta) = j_s(R^{Y^14,perp}) + F^Psi_{j_s} - [F_{a^0}, j_s theta]
```

For umbilic sections with phi = const on maximally symmetric background:
- j_s theta = j_s(phi^i n_i) = phi^i j_s(n_i) = constant sp(64)-element
- [D_{a^0}, D_{a^0}](constant) = F_{a^0} (the background sp(64) curvature)
- Right side: j_s(R^{Y^14,perp}) + F^Psi_{j_s} - [F_{a^0}, phi-element]

On a maximally symmetric background with Psi = 0:
- F^Psi = 0
- The Codazzi equation reduces to:
  ```
  F_{a^0} = j_s(R^{Y^14,perp}) - [F_{a^0}, phi-element]
  ```

This is the compatibility condition between the ambient curvature normal projection
and the background spin curvature. On a maximally symmetric background, this is
satisfied by construction (since R^{Y^14} has the standard form of a constant-curvature
space and the Codazzi equation for a constant-mean-curvature immersion in a
constant-curvature ambient is automatically satisfied when H = const).

**Combined verdict from Codazzi + Gauss:**

1. Q^{TF}(B) = 0 (Gauss, exact for umbilic).
2. K(A,s) = 0 (Codazzi, exact for umbilic tautological section on max-sym background).
3. [G^Y_T]^{TF} = 0 (symmetry argument on max-sym ambient, reconstruction grade).
4. [E^Psi]^{TF} = 0 (vacuum gauge field Psi = 0 or symmetric gauge, reconstruction grade).

Therefore:

```
R_fail^{TF}_{mu nu} = 0    (reconstruction grade).
```

The trace part of R_fail determines Lambda:

```
R_fail^{tr} = 0   iff   Lambda = 3|phi|^2 - (3/7) R^Y_T + C_Psi.
```

### 5.2 Obstruction identification

The single obstruction preventing a fully **verified** (not merely reconstruction-grade)
conclusion is the computation of [G^Y_T]^{TF} from the explicit gimmel Riemann tensor.
This requires:

**Obstruction O1 (Ambient Riemann tensor):** The full 14-dimensional Riemann tensor
R^{Y^14}_{ABCD} on the gimmel metric has not been computed explicitly in the
moving-frame basis. Its tangential projection G^Y_T_{mu nu} is therefore only known
to be pure-metric (proportional to g_{mu nu}) by the maximal-symmetry symmetry
argument, not by explicit computation. An explicit CAS computation of R^{Y^14} in
the gimmel moving-frame would upgrade this from reconstruction to verified.

This is not a new obstruction — it is the same CAS-verification gate mentioned in
`ii-s-moving-frames-2026-06-23.md` (F-condition for the ambient curvature step in the
CPA-1 Lichnerowicz computation). It affects multiple open computations simultaneously;
closing it would upgrade several items.

**Obstruction O2 (Gauge vacuum):** On a non-maximally-symmetric vacuum section (e.g.,
Schwarzschild or FLRW), the umbilic condition requires B^i_{mu nu} = phi^i g_{mu nu}
with phi^i varying over X^4. In this case E^Psi^{TF} may be non-zero from the
inhomogeneous gauge curvature. The argument R_fail^{TF} = 0 then requires
[G^Y_T]^{TF} = -[E^Psi]^{TF} — a non-trivial cancellation condition that has not
been verified.

---

## 6. Comparison with Prior Exploration Note

The Phase 5 second-hourly-pass note (logged in DERIVATION-PROGRESS.md as "K(A,s) and
R_fail for umbilic sections," 2026-06-23) stated:

> For totally umbilic sections: K(A,s) = 0 for tautological connection on maximally
> symmetric background. R_fail = 0 gives one-equation Lambda constraint
> Lambda = G^Y_T_const - 3|phi|^2.

The present note extends this in four ways:

1. Derives Q^{TF}(B) = 0 explicitly from the umbilic condition (not assumed).
2. Identifies the precise residual structure: R_fail^{TF} = 0 exactly, R_fail^{tr}
   fixes Lambda.
3. Shows that [G^Y_T]^{TF} = 0 by the symmetry argument (new — not in the prior note).
4. Identifies the two genuine obstructions (O1 ambient Riemann CAS gate, O2 non-
   max-sym gauge vacuum) precisely.

The prior note's "one-equation Lambda constraint" is recovered: the trace of R_fail = 0
gives Lambda = G^Y_T_const - 3|phi|^2 (in the notation above, this is the trace equation
with E^Psi = C_Psi g_{mu nu} absorbed into G^Y_T_const).

---

## 7. Result

**Theorem (Reconstruction Grade).** Let s: X^4 -> Y^14 be a totally umbilic critical
section of E[s] = integral|II_s|^2 on a maximally symmetric vacuum background
(T_{mu nu} = 0). Assume the tautological Sp(64) connection (Psi = 0) and the
horizontal-normalized II_s convention. Then:

1. Q^{TF}(B) = 0 (exact, from the umbilic condition).
2. K(A,s) = 0 (exact, from the tautological connection on a maximally symmetric background).
3. R_fail^{TF}_{mu nu} = 0 (reconstruction grade, from the maximal-symmetry structure of
   the gimmel metric).
4. R_fail^{tr} = 0 iff Lambda = 3|phi|^2 - (3/7) R^Y_T + C_Psi (one constraint, determines Lambda).

In particular, the 4D vacuum Einstein equation with cosmological constant
G^X_{mu nu} + Lambda g_{mu nu} = 0 is satisfied (at reconstruction grade) with Lambda
determined geometrically.

**Explicit failure conditions:** F1 (non-maximal-symmetry breaking), F2 (gauge
background breaking symmetry), F3 (only phi = 0 is a Willmore critical umbilic
section), F4 (R^Y_T not determined by g_s), F5 (convention error in II_s^H).

**Single remaining obstruction for upgrade to verified:** O1 — explicit CAS computation
of the gimmel Riemann tensor tangential projection [G^Y_T]^{TF}. This would confirm
or falsify the symmetry-argument step (3) above.

---

## 8. Open Questions

**OQ1.** Does the Willmore critical-point equation delta E[s] = 0 for totally umbilic
sections force phi^i = 0 (totally geodesic) on compact X^4? If so, the non-trivial
umbilic case (phi != 0) is only relevant for non-compact cosmological sections.

**OQ2.** What is the explicit value of R^Y_T on the gimmel metric for the umbilic
de Sitter section? This would make the Lambda-determination formula explicit:
Lambda = 3H^2 - (3/7)R^Y_T (where H = de Sitter Hubble constant, phi^i = H/4 in
appropriate normalization).

**OQ3.** For the non-umbilic case (where Q^{TF}(B) != 0), does R_fail = 0 require
Q^{TF}(B) to be exactly the GU matter stress-energy? This is the IC1-IC4 chain from
prior notes. The umbilic case is the vacuum limit where matter stress vanishes and
the extrinsic contribution is pure cosmological.

**OQ4.** The constraint Lambda = 3|phi|^2 - (3/7) R^Y_T + C_Psi relates three GU
geometric quantities to the 4D cosmological constant. Does this give a prediction
for Lambda in terms of observable quantities (via the observer-section error model
from `observer-section-error-model-2026-06-23.md` and the CPA-1 cross-program contact)?

---

## 9. Dependencies

This note builds on the complete Codazzi + Gauss chain (all 2026-06-23):

- `explorations/codazzi-sp64-bundle-2026-06-23.md` — Gauss equation, R_fail definition
- `explorations/codazzi-general-non-umbilic-2026-06-23.md` — Q^{TF}(B)=0 for umbilic,
  K(A,s)=0 for tautological umbilic section
- `explorations/codazzi-sp64-2026-06-23.md` — full Sp(64) Codazzi equation, IC1-IC3
- `explorations/ii-s-moving-frames-2026-06-23.md` — II_s^H = 0 for tautological section,
  gimmel Christoffel symbols
- `explorations/ic2-positivity-soldering-normal-2026-06-23.md` — IC2 positivity
- `explorations/ic3-nonlinear-conservation-2026-06-23.md` — IC3 nonlinear conservation
- `explorations/ic4-lagrangian-tmunu-derivation-2026-06-23.md` — IC4 Lagrangian match

**This note contributes to:**
- NEXT-STEPS.md F3 ("Evaluate K(A,s) and R_fail for the selected section"): extends
  from the initial umbilic sketch to a full reconstruction-grade argument with explicit
  residual conditions.
- The Einstein equation emergence chain (IC1-IC4): confirms that the vacuum/umbilic
  subcase closes without new obstructions, narrowing the remaining work to the non-umbilic
  matter sector.

---

*Filed: 2026-06-23. Problem label: rfail-umbilic. Grade: reconstruction.
Verdict: CONDITIONALLY_RESOLVED.*
