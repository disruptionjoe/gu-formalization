---
title: "OQ3a Willmore: Is Ricci-flat the Only Way to Achieve E=0 on a Compact 4-Manifold?"
date: 2026-06-23
problem_label: "oq3a-willmore-k3-selection"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# OQ3a Willmore: E=0 Critical Sections and K3 Selection

## 1. Problem Statement

**The question:** Among all critical sections s: X^4 -> Y^14 of the Willmore energy

```
E[s] = integral_{X^4} |II_s|^2 dvol_{g_s},
```

which have Ricci-flat (K3-type) fibers, and is Ricci-flat the ONLY way to achieve E=0 on
a compact 4-manifold fiber? Does the Willmore inequality combined with Gauss-Bonnet force
Ricci-flat as the unique E=0 topology?

**Why this matters:** The established context (oq3a-k3-variational-selection-2026-06-23.md)
showed that the factor of 2 in m_H(S(6,4)) = 24 is topologically forced by Rokhlin + ind_H
= 24, and that the Willmore principle selects the hyperkahler metric within the K3 class.
But the exact question "is Ricci-flat the unique E=0 topology among compact 4-manifolds?"
was NOT fully answered. Here we address it directly.

**Failure condition if missed:** If other fiber topologies also achieve E=0 critical sections,
the Willmore principle does not uniquely select K3-type fibers, and the factor of 2 must be
justified by Rokhlin alone (which it is, but the Willmore selection argument would be weaker
than claimed).

---

## 2. Established Context

From `explorations/generation-sector/oq3a-k3-variational-selection-2026-06-23.md` (reconstruction grade):

- The LC section s_g (tautological: A = Gamma_LC) satisfies II_s^H = 0 for ANY metric g on
  ANY compact X^4. Therefore E[s_LC] = 0 for all LC sections, regardless of fiber topology.
- The Willmore principle is FLAT across topological classes: LC sections over S^4, T^4, K3,
  or any other compact smooth 4-manifold all achieve E[s_LC] = 0.
- Within the K3 topological class, the Willmore principle selects the hyperkahler Yau metric
  as the preferred E=0 representative (E > 0 for non-Ricci-flat connections on K3-type
  backgrounds with non-tautological sections).

The new question is: can a NON-Ricci-flat metric g on a compact 4-manifold X^4 admit
a non-LC section s with E[s] = 0?

---

## 3. The Willmore Energy: LC Sections vs. Non-LC Sections

### 3.1 Decomposition of E[s]

The second fundamental form II_s measures the failure of s(X^4) to be totally geodesic in
(Y^14, g_Y). In the horizontal-normalized convention (from ii-s-moving-frames-2026-06-23.md):

```
II_s^H = nabla^{g_Y,perp}(s_*v) - s*(nabla^{g_s}_v),
```

which in the tautological LC gauge simplifies to:

```
II_s^H = nabla^perp theta,   where theta = A - Gamma_LC(g_s).
```

For the LC section (A = Gamma_LC): theta = 0, so II_s^H = 0 and E[s_LC] = 0.

For a NON-LC section (theta != 0): E[s] = integral|nabla^perp theta|^2 >= 0.

**Can a non-LC section have E = 0?** Yes: if and only if nabla^perp theta = 0, i.e., theta
is parallel with respect to the normal connection. This is a condition on the distortion
theta, not on the fiber topology of X^4.

**Conclusion:** E[s] = 0 does NOT require Ricci-flat fiber topology. It requires either
(a) the LC choice A = Gamma_LC, or (b) a non-LC section with parallel distortion.

### 3.2 Parallel-distortion sections

A section s with II_s^H = 0 but A != Gamma_LC (parallel distortion theta with nabla^perp
theta = 0) is called a horizontal-totally-geodesic section. These exist on any Riemannian
manifold admitting parallel sections of the adjoint bundle ad(P).

For Y^14 = Met(X^4), ad(P) is related to the gauge structure of the Sp(64) bundle.
Parallel distortion sections are preserved by holonomy; their existence depends on the
holonomy representation, not on Ricci-flatness of X^4.

Therefore, Ricci-flat fiber topology is NOT forced by E=0 from the Willmore principle alone
on sections of general fiber topology.

---

## 4. Gauss-Bonnet and the Willmore Inequality on Compact 4-Manifolds

### 4.1 The Willmore inequality in 4D

For an immersed submanifold Sigma^4 in a higher-dimensional ambient space (Y^14, g_Y), the
Willmore functional E = integral|II_s|^2 satisfies the Willmore inequality:

```
E[s] >= C * chi(X^4) / vol(X^4)^{1/2}
```

for a topological-type constant C depending on the ambient curvature and the topology of X^4.
This is the analog of the Li-Yau inequality in higher codimension.

However, for EMBEDDED sections s: X^4 -> Y^14 (which are always embeddings since s is a
section of the bundle pi: Y^14 -> X^4), the relevant constraint is different: the section
is a GRAPH over X^4, and the Willmore energy is not subject to the same lower bound that
applies to free immersions in a fixed ambient manifold.

**For graph sections in a fiber bundle:** The Gauss-Bonnet-Chern theorem on X^4 gives

```
integral_{X^4} (|W_s|^2 - 2|S_0^s|^2 + R_s^2/24) dvol_{g_s} = 8 pi^2 chi(X^4),
```

where W_s = Weyl tensor, S_0^s = traceless Ricci tensor, R_s = scalar curvature of g_s.

The Gauss equation (from codazzi-sp64-2026-06-23.md) relates the curvature of g_s to the
ambient curvature of g_Y and the second fundamental form:

```
R^{g_s}_{abcd} = R^{g_Y}_{abcd}|_{T X^4} + II_s^H * II_s^H (schematic)
```

Substituting into Gauss-Bonnet:

```
8 pi^2 chi(X^4) = integral(|W_s|^2 + II_s^2 - 2|S_0^s|^2 + R_s^2/24) + ambient terms
```

This gives a constraint between E[s] = integral|II_s|^2 and the topological type chi(X^4),
but does NOT force E[s] = 0 to imply Ricci-flat (the |II_s|^2 terms and |W_s|^2 terms can
compensate each other for different topological types).

### 4.2 Can Gauss-Bonnet force E=0 => Ricci-flat?

The critical case is: suppose E[s] = 0 (II_s = 0). Then from Gauss-Bonnet:

```
8 pi^2 chi(X^4) = integral(|W_s|^2 - 2|S_0^s|^2 + R_s^2/24) + ambient curvature terms.
```

This equation does NOT force g_s to be Ricci-flat. It is a topological identity that holds
for any metric on X^4, independently of whether g_s is Einstein, Kähler, or Ricci-flat.

**Example (S^4):** chi(S^4) = 2. The round metric on S^4 is Einstein (Ricci = (4-1) g = 3g)
but NOT Ricci-flat. The LC section s_{S^4} has II_s^H = 0 (tautological) and E = 0. This
is a concrete counterexample: E[s] = 0 with a non-Ricci-flat metric on X^4 = S^4.

**Example (T^4):** chi(T^4) = 0. The flat metric on T^4 is Ricci-flat. The LC section has
E = 0. But T^4 with any flat metric (including tilted torus metrics) is also E=0; the flat
metric is not unique in the LC-section class.

**Example (CP^2 with Fubini-Study):** chi(CP^2) = 3. Fubini-Study is Einstein (not Ricci-
flat). LC section has E = 0. So Einstein-but-not-Ricci-flat metrics also achieve E=0 via
the LC section.

**Conclusion from these examples:** The Willmore condition E[s] = 0 (achieved by LC sections)
does NOT force Ricci-flat topology. Any compact smooth 4-manifold with ANY metric achieves
E = 0 via the LC section.

---

## 5. What the Willmore Principle Does Select

### 5.1 Clarification: the GU selection problem is different

The question "does the Willmore principle select K3-type fiber topology?" has two versions:

**Version A (Weaker):** Among all LC sections (which all have E=0), does the Willmore
principle distinguish a preferred topology? No: all LC sections achieve E=0 and the
energy functional cannot distinguish topologies at E=0.

**Version B (Stronger, correctly posed):** Among all sections (LC and non-LC) with a
FIXED constraint (such as ind_H(D_GU) = 24), which have minimum Willmore energy? For this
constrained problem, the answer depends on the constraint.

**GU's actual selection problem is Version B:** Given the constraint ind_H(D_GU^s) = 24,
minimize E[s]. The constraint forces X^4 to have Â = 2 (from Rokhlin + 8*Â + 8 = 24 formula),
and within X^4 with Â = 2, the Willmore principle selects the Yau hyperkahler metric.

### 5.2 The E=0 equivalence class and the role of Ricci-flatness

For LC sections, E = 0 for all topologies. The Willmore energy CANNOT be the selection
mechanism for the topological type (it is constant = 0 on all LC sections).

Within a fixed topological class (say, Â = 2, K3-type), the Willmore principle distinguishes
between:

- The LC section s_{g_Yau} (E = 0): preferred.
- Non-LC sections s_{g, A!=Gamma} (E > 0 generically): not preferred unless parallel theta.
- Parallel-distortion sections (II_s = 0, A != Gamma): also E = 0.

The Yau metric is singled out not by E=0 uniqueness (other E=0 sections exist) but by the
additional Euler-Lagrange condition from delta E = 0, combined with:

1. The requirement that the section be "tautological" (s determines g_s self-consistently).
2. The Yau theorem: the unique Ricci-flat Kähler metric on K3 is the Yau metric.
3. The Codazzi-Einstein equation (IC3/IC4 from codazzi-sp64-2026-06-23.md): the GU field
   equation for the section s reduces to Ricci-flatness on-shell at leading order in theta.

**The precise role of Ricci-flatness:** The GU Euler-Lagrange equation from E[s] reduces
to the Einstein equation with zero cosmological constant (Ricci-flat) at the LC section on
K3, as shown in ic4-lagrangian-tmunu-derivation-2026-06-23.md. This is the correct sense
in which the Willmore principle selects Ricci-flat: not by E=0 uniqueness, but by the
FIELD EQUATION at the critical section.

### 5.3 Ricci-flat as the unique STABLE E=0 critical section

A stronger claim is available: among all STABLE (not just critical) E=0 sections, the
LC section over K3-Yau is the unique one within the Â=2 topological class.

Proof sketch (reconstruction grade):

Step 1. E=0 LC sections exist for all compact smooth X^4 with any metric. All are degenerate
critical points (Hessian has zero modes corresponding to metric deformations of X^4).

Step 2. The stability of an LC section under perturbations of the fiber metric requires the
Lichnerowicz operator L_{g_s} on Sym^2 T*X^4 to be non-negative. For Ricci-flat Kähler
manifolds (Yau), L_{g_s} >= 0 with kernel = harmonic symmetric 2-tensors (Bochner technique
for Kähler geometry, Berger-Ebin theorem).

Step 3. For NON-Ricci-flat metrics g_s on K3-type X^4:
- Einstein metrics on K3 with positive scalar curvature: K3 does not admit such metrics
  (Hitchin-Thorpe inequality, and K3 has sigma = -16, so no positive-curvature Einstein
  metric on K3 exists by the Miyaoka-Yau inequality for Kähler surfaces).
- Non-Kähler metrics: Not ruled out on K3 topologically, but no stable E=0 section is
  known for non-Kähler metrics on K3.

Step 4. The Yau hyperkahler metric is the UNIQUE Ricci-flat Kähler metric in each Kähler
class on K3 (Yau-Calabi theorem). It is the unique stable E=0 representative of the LC
section family within the Kähler-class moduli space.

**Conclusion (reconstruction grade):** Among compact 4-manifolds with Â=2, the LC section
over K3-Yau is the unique STABLE E=0 section in the sense that:
- It achieves E=0 (LC section, trivially).
- Its Hessian has no unstable directions in the graviton TT sector (L >= 0 on K3-Yau).
- No other metric on K3-type X^4 achieves a stable E=0 LC section (ruled out by Hitchin-
  Thorpe and Miyaoka-Yau for non-Ricci-flat Einstein metrics; non-Kähler metrics are not
  stable E=0 candidates by the Bochner argument).

---

## 6. Theorem Statement (Reconstruction Grade)

**Theorem (Willmore Stability + K3 Selection, reconstruction grade):**

Let X^4 be a simply-connected compact smooth spin 4-manifold with Â(X^4) = 2 (K3 type,
sigma = -16). Among all sections s: X^4 -> Y^14 = Met(X^4), the unique stable E=0 critical
section is the LC section s_{g_Yau} where g_Yau is the Yau hyperkahler metric on K3. This
section is:

(a) A critical section of E[s] (Euler-Lagrange equation satisfied trivially: II_s = 0).
(b) A STABLE critical section: the Hessian Hess_{g_Yau} E is non-negative on the TT
    graviton sector (no unstable directions in the physical graviton fluctuations).
(c) The UNIQUE stable E=0 section within the Kähler moduli of K3 (Yau-Calabi uniqueness
    of Ricci-flat metric per Kähler class).

**What is NOT proved by this theorem:** The selection of Â = 2 (K3-type) over other
topological classes. All topological classes have LC sections with E=0; the Willmore
energy cannot distinguish between topologies at the E=0 critical point. The selection
of Â = 2 requires Rokhlin + ind_H = 24 (established in oq3a-k3-variational-selection).

---

## 7. Is Ricci-flat the ONLY Way to Achieve E=0?

### 7.1 The direct answer

No. E=0 is achieved by:
1. The LC section s_{g} for ANY compact smooth metric g on ANY X^4. This is purely
   tautological (A = Gamma_LC gives II_s = 0 always), independent of curvature.
2. Parallel-distortion sections (A != Gamma_LC but nabla^perp theta = 0).

Ricci-flat is NOT the unique E=0 condition. The round S^4 (Einstein, not Ricci-flat),
flat T^4 (Ricci-flat), and Fubini-Study CP^2 (Einstein, not Ricci-flat) all achieve
E=0 via their LC sections.

### 7.2 The refined question: among STABLE E=0 sections within Â=2 class?

Within the Â=2 topological class (simply-connected compact smooth spin 4-manifold with
sigma=-16, i.e., K3 topology), are there stable E=0 sections with non-Ricci-flat fiber
metrics?

The answer from Section 5.3 above is: no stable E=0 non-Ricci-flat section is known
within the K3 topological class, and the Hitchin-Thorpe + Miyaoka-Yau inequalities
rule out positive-curvature Einstein metrics. The Yau-Calabi theorem gives uniqueness
of Ricci-flat in each Kähler class, making the Yau metric the canonical E=0 representative.

### 7.3 The GU-relevant formulation

For GU, the question is not "is Ricci-flat the ONLY E=0 compact 4-manifold?" but rather:

"Within the constrained variational problem (minimize E[s] subject to ind_H(D_GU^s) = 24),
what is the preferred section?"

The constraint ind_H = 24 forces X^4 to have Â=2 (K3 type). Within K3:
- All LC sections have E = 0.
- The Yau metric LC section is the stable E=0 critical point.
- The Euler-Lagrange equation of E[s] at the LC section reduces to Ricci-flatness of g_s
  (GU field equation, ic4-lagrangian-tmunu-derivation-2026-06-23.md, at leading order in theta).

Therefore, the GU variational principle DYNAMICALLY SELECTS Ricci-flat (Yau metric) not
because E=0 forces Ricci-flat, but because:

(A) The Euler-Lagrange equation at the LC section is equivalent to Ricci-flat (GU field
    equation gives this as the on-shell condition, not merely an E=0 condition).
(B) The Yau-Calabi theorem guarantees existence and uniqueness of the Ricci-flat metric
    in each Kähler class on K3.
(C) The stability Hessian is non-negative at K3-Yau (no unstable graviton modes).

---

## 8. Gauss-Bonnet Argument: What It Can and Cannot Give

### 8.1 Gauss-Bonnet for E=0 sections

For an E=0 section (II_s = 0, LC section), Gauss-Bonnet on X^4 becomes:

```
8 pi^2 chi(X^4) = integral_{X^4}(|W_s|^2 - 2|S_0^s|^2 + R_s^2/24) dvol_{g_s}
                  + ambient curvature correction terms from g_Y.
```

(From the Gauss equation with II_s = 0: the curvature of g_s is the tangential projection
of the ambient curvature R^{g_Y}, which includes Weyl tensor contributions from the gimmel
metric.)

**What Gauss-Bonnet gives:** A constraint relating |W_s|^2, |S_0^s|^2, R_s, and chi(X^4).
For K3: chi(K3) = 24, sigma(K3) = -16, so by Hirzebruch signature theorem:

```
integral |W|^2 = 8pi^2 chi + 12pi^2 sigma = 8pi^2*24 + 12pi^2*(-16) = 192pi^2 - 192pi^2 = 0.
```

Wait -- let us recompute. The standard formula is:

```
integral (|W_+|^2 - |W_-|^2) dvol = 4pi^2 sigma(K3) = 4pi^2 * (-16) = -64 pi^2.
```

And for Ricci-flat Kähler (Yau metric on K3):
```
integral |W|^2 = integral(|W_+|^2 + |W_-|^2),
integral |S_0|^2 = 0 (Ricci-flat => S_0 = 0),
R = 0 (Ricci-flat).
```

From Chern-Gauss-Bonnet in 4D with Ricci-flat metric:
```
8pi^2 chi(K3) = integral |W|^2 dvol
=> integral |W|^2 dvol = 8pi^2 * 24 = 192 pi^2.
```

(The formula for compact 4-manifolds: 8pi^2 chi = integral(|W|^2 + R^2/24 - 2|Ric_0|^2);
for Ricci-flat: 8pi^2 chi = integral |W|^2.)

**What this means for K3-Yau:** The Yau metric has integral |W|^2 = 192 pi^2 (nonzero!).
K3 with the Yau metric is NOT conformally flat. The Weyl tensor is large; the Ricci-flat
condition is compatible with a large Weyl tensor.

**Gauss-Bonnet does NOT force E=0 => Ricci-flat.** It gives a constraint integral |W|^2 +
corrections = 8pi^2 chi, and different metrics on the same X^4 can satisfy this identity
with different combinations of W, S_0, R.

### 8.2 What Willmore inequality adds

The Willmore inequality for immersed surfaces in R^3 states W >= 4pi (equality for round
spheres). In higher dimensions, the relevant generalization is the Li-Yau inequality:

```
E[s] = integral |II_s|^2 dvol >= 8pi / (n-1) * multiplicity_penalty >= 0.
```

For embedded sections in a fiber bundle, the immersion is always an embedding (section
condition forces s to be injective), so the Li-Yau multiplicity term is 1 and the inequality
gives E >= C * chi(X^4) / max_curvature_of_ambient.

However, for LC SECTIONS (which are the physically relevant ones), II_s = 0 and E = 0, so
the Willmore inequality gives 0 >= C * ..., which is a constraint on the ambient curvature
(not on X^4 topology). It does not force non-trivial behavior.

**The Willmore inequality does not help distinguish fiber topologies at the E=0 level.**
It is an inequality that becomes trivial when applied to totally geodesic sections.

---

## 9. Explicit Failure Conditions

**F1 (E=0 does not force Ricci-flat).** As shown explicitly above: the round S^4 (non-
Ricci-flat, Einstein) achieves E[s_LC] = 0 via the LC section. The Willmore variational
principle alone cannot distinguish K3-Yau (Ricci-flat) from S^4-round (non-Ricci-flat)
at the E=0 level. The K3 selection requires Rokhlin + ind_H = 24 (topological, not
variational). This is a CONFIRMED failure of the stronger claim "Ricci-flat is the ONLY
E=0 topology."

**F2 (GU field equation is the correct selector, not E=0).** The Euler-Lagrange equation
of E[s] at the LC section on K3-Yau gives delta E = 0 trivially (since E=0 at a minimum).
The CONTENT of the GU field equation comes from the second variation (stability) and from
the Codazzi-Einstein identification at IC3/IC4 level, which gives Ricci-flat as the on-shell
condition. If IC3 or IC4 fail (from codazzi-sp64-2026-06-23.md), the Ricci-flat selection
is lost.

**F3 (Stable E=0 on non-K3 Â=2 manifolds).** The Hitchin-Thorpe + Miyaoka-Yau argument
rules out positive-curvature Einstein metrics on K3, but does not rule out non-Kähler
metrics with negative or zero Ricci curvature. If a non-Kähler Ricci-flat metric on K3
topology exists (it is known that no non-Kähler Ricci-flat metric exists on K3 by Yau's
theorem, only Kähler Ricci-flat), this failure mode is closed.

**F4 (Parallel-distortion sections give E=0 for non-Ricci-flat metrics).** A parallel-
distortion section (nabla^perp theta = 0 but theta != 0) achieves E=0 without the LC
gauge. Such sections exist if the Sp(64) bundle over X^4 has parallel sections in the
adjoint bundle. These would provide non-LC E=0 sections with potentially non-Ricci-flat
g_s. Their existence is not excluded by the Willmore principle; they are excluded from
GU's preferred selection only by the tautological (section-determines-metric) self-
consistency condition of the GU setup.

**F5 (Ambient curvature correction in Gauss-Bonnet).** The Gauss equation expresses the
curvature of g_s in terms of the AMBIENT curvature R^{g_Y} and II_s. For E=0 sections
(II_s = 0), the Gauss-Bonnet formula involves R^{g_Y}|_{T X^4} (the tangential projection
of the 14D curvature). If R^{g_Y} is large (non-flat ambient space), the Gauss-Bonnet
constraint is modified by ambient terms. This could in principle relax the Ricci-flat
condition even within K3 topology.

---

## 10. Summary: The Willmore Selection Chain for K3

The complete selection chain is:

```
Step 1: ind_H(D_GU) = 24 (3 SM generations, required)
        |
        v
Step 2: 8 * Â(X^4) + 8 = 24 => Â(X^4) = 2  [from 2+1 split formula]
        |
        v
Step 3: Rokhlin => Â even; Â = 2 is minimal even positive value
        |
        v
Step 4: Donaldson + Freedman => X^4 with Â = 2, sigma = -16 is uniquely K3
        |
        v
Step 5: Within K3 topological class, LC sections all have E = 0 (variational floor)
        |
        v
Step 6: GU Euler-Lagrange (IC4) => field equation on-shell is Ricci-flat
        |
        v
Step 7: Yau-Calabi theorem => unique Ricci-flat Kähler metric per Kähler class
        |
        v
Step 8: K3-Yau is the preferred E=0 stable critical section
```

**The Willmore principle (E[s]) operates at Steps 5-6:**
- Step 5: E=0 is achieved by all LC sections (variational floor, topology-independent).
- Step 6: The GU field equation (Euler-Lagrange of E[s] combined with IC4) selects
  Ricci-flat as the on-shell metric for the section.

**The topological selection (K3 over other topologies) occurs at Steps 1-4:**
- Steps 1-3: Rokhlin + ind_H = 24 forces Â = 2.
- Step 4: K3 uniqueness in smooth 4-manifold theory.

**The metric selection within K3 occurs at Steps 6-8:**
- Steps 6-7: GU field equation selects Ricci-flat; Yau gives uniqueness in Kähler class.
- Step 8: K3-Yau is the physical ground state.

---

## 11. Verdict

**Grade: reconstruction.** The argument has three legs with different grades:
- Topological forcing (Steps 1-4): EXACT (Rokhlin theorem + Atiyah-Singer + K3 uniqueness
  by Donaldson + Freedman; all established mathematical theorems).
- Variational floor (Step 5): EXACT (LC section always has E=0; this is tautological).
- Metric selection (Steps 6-8): reconstruction (IC4 field equation is reconstruction-grade;
  Yau-Calabi theorem is exact but the identification of IC4 output with Ricci-flat requires
  the codazzi-sp64 reconstruction argument).

**Verdict: CONDITIONALLY_RESOLVED.**

The Willmore principle E[s] does NOT select K3-type fiber topology by forcing E=0 => Ricci-
flat. Ricci-flat is NOT the unique E=0 topology among compact 4-manifolds: any LC section
achieves E=0 for any metric on any compact X^4. The factor of 2 (Â(K3) = 2) is topologically
forced by Rokhlin + ind_H = 24, not by the Willmore variational principle.

The Willmore principle's actual role is:
1. To provide the variational floor (E=0 for LC sections), making the LC section the
   preferred gauge for the GU field configuration.
2. To yield, via its Euler-Lagrange equation and the Codazzi-Einstein identification (IC4),
   the on-shell condition Ricci-flat for the preferred metric g_s within the K3 class.
3. To select the Yau hyperkahler metric as the unique stable E=0 Kähler representative
   within K3 (by stability of the Lichnerowicz operator + Yau-Calabi uniqueness).

**The factor of 2 is not ambiguous:** It is forced by Rokhlin + ind_H = 24 (Steps 1-4 in
the selection chain). The Willmore principle provides structural consistency by selecting
the K3-Yau metric (Ricci-flat) as the physical ground state within the forced topological
class, but does not generate the factor of 2.

---

## 12. Open Questions

**OQ1 (Priority).** Verify IC4 (Euler-Lagrange of E[s] reduces to Ricci-flat on-shell)
at verified grade. This requires the full Lagrangian derivation of T_{mu nu} from the GU
action (ic4-lagrangian-tmunu-derivation-2026-06-23.md, currently reconstruction grade).
Closure would upgrade Steps 6-7 in the selection chain.

**OQ2.** Verify that no parallel-distortion E=0 section with non-Ricci-flat induced metric
arises within K3 topology. This requires a classification of sections with nabla^perp theta
= 0 on Met(K3) = Y^14|_{K3}. Currently untouched.

**OQ3.** The ambient Gauss-Bonnet correction (F5 failure condition above): compute
R^{g_Y}|_{T K3 x {g_Yau}} explicitly from the gimmel metric of Y^14 and assess whether it
modifies the Ricci-flat selection within K3. The gimmel metric is reconstructed in
ii-s-moving-frames-2026-06-23.md but the full Riemann tensor component R^{g_Y}_{abcd} at
the K3-Yau LC section is not computed.

---

## 13. References

- Gauss-Bonnet-Chern in 4D: Chern (1945); Hirzebruch signature theorem (1956).
- Willmore energy and Li-Yau inequality: Li-Yau (1982); Marques-Neves (2014) for min-max.
- Yau-Calabi: Yau (1978) Calabi conjecture proof.
- Hitchin-Thorpe inequality: Hitchin (1974); Thorpe (1969).
- Miyaoka-Yau inequality for Kähler surfaces: Yau (1977).
- K3 uniqueness: Donaldson (1983) smooth structures; Freedman (1982) topological classification.
- IC4 GU Lagrangian: `explorations/geometry-curvature-emergence/ic4-lagrangian-tmunu-derivation-2026-06-23.md`.
- Prior OQ3a computation: `explorations/generation-sector/oq3a-k3-variational-selection-2026-06-23.md`.
- Moving frames for II_s: `explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md`.
- Codazzi/Sp(64): `explorations/geometry-curvature-emergence/codazzi-sp64-2026-06-23.md`.

---

## 14. Verdict Summary

**Label:** oq3a-willmore-k3-selection

**Verdict: CONDITIONALLY_RESOLVED (reconstruction)**

**One sentence:** E=0 critical sections of the Willmore energy on Y^14 are achieved by
ALL LC sections regardless of fiber topology (the round S^4 achieves E=0 just as K3-Yau
does), so Ricci-flat is not the unique E=0 topology; instead, K3 topology is selected by
Rokhlin + ind_H=24 (topological forcing), and the Willmore principle selects the Yau metric
within K3 by the GU field equation (IC4 Euler-Lagrange = Ricci-flat on-shell), making the
Willmore principle a metric selector within a topologically forced class rather than a
topology selector.
