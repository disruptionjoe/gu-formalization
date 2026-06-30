---
title: "Dark Energy Assumption 3 — Variational Derivation and Algebraic Route"
date: 2026-06-23
problem_label: "dark-energy-assumption3-variational"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# Dark Energy Assumption 3 — Variational Derivation and Algebraic Route

## Problem Statement

Assumption 3 in `canon/dark-energy-theta-divergence-free.md` is the load-bearing gap in the
dark-energy divergence-free argument:

> **Assumption 3 (reconstruction grade, unproved):** theta = pi - epsilon^{-1} B epsilon is
> the gauge-potential sector of the Euler-Lagrange derivative E_A for the GU action. This
> identification is inferred from a transcript schematic; no coordinate computation or
> variational derivation from a written GU action has been supplied.

The task: derive Assumption 3 by either
1. **Variational route**: Write the GU action schematically, vary with respect to the
   connection A, and identify the resulting E_A sector with theta.
2. **Algebraic route**: Show that any G-equivariant element of Omega^1(Y^14, ad P) in the
   adjoint representation is automatically divergence-free.

Clear failure condition (from problem statement): if neither route produces D_A* theta = 0
without invoking Assumption 3, the canon remains CONDITIONALLY_RESOLVED and a specific
new falsification condition (derivation gap) must be recorded.

## Established Context

From prior explorations (reconstruction grade unless noted):

- Y^14 = Met(X^4), total signature (9,5). Gauge group G = Sp(64). Principal bundle P -> Y^14.
- theta = pi - Ad(epsilon^{-1}) B in Omega^1(Y^14, ad P), where (epsilon, B) in IG = G semidirect Omega^1(Y^14, ad P).
- C1 ESTABLISHED (reconstruction): gimmel metric g_gimmel is G-invariant because G acts trivially on Y^14 as a base manifold; Killing form is Ad-invariant.
- C2 FAILS independently: equivariance of theta under G does not yield D_A* theta = 0 without identifying theta as the Noether current or as E_A.
- C3 path (Noether's second theorem): gauge invariance of S[A] -> D_A* E_A = 0 off-shell. Closes D_A* theta = 0 conditional on Assumption 3 (theta = E_A).
- `explorations/dark-energy-cosmology/dark-energy-c1-c2-path-gimmel-ginvariance-2026-06-23.md`: identifies the specific blocking point — identifying theta with D_A* F_A is Assumption 3 restated.

## Route 1 — Variational Derivation of Assumption 3

### 1.1 GU Action Structure

The GU action lives on Y^14 and couples the gauge field A (a connection on P -> Y^14) to
the spinor field psi in Omega^0(Y^14, S) and the IG-valued field (epsilon, B) encoding the
metric/connection data. Based on transcript schematic ([00:25:56]) and the structure of the
inhomogeneous gauge group, the GU action takes the form:

```
S_GU[A, psi, epsilon, B] = S_YM[A] + S_Dirac[A, psi] + S_IG[epsilon, B, A]
```

where:

```
S_YM[A]       = integral_{Y^14} ||F_A||^2_gimmel dvol_gimmel
S_Dirac[A,psi] = integral_{Y^14} <psi, D_A psi>_S dvol_gimmel
S_IG[...]     = integral_{Y^14} ||theta||^2_gimmel dvol_gimmel
              = integral_{Y^14} ||pi - Ad(epsilon^{-1}) B||^2_gimmel dvol_gimmel
```

The third term S_IG is the "distortion energy" of the IG splitting. Here pi = A - Gamma_epsilon
is the distortion of A from the Levi-Civita connection determined by epsilon.

**Notation:** pi depends on both A and epsilon. We write pi = A - Gamma(epsilon), where
Gamma(epsilon) is the Levi-Civita connection of the metric induced by epsilon in IG.

### 1.2 Variation with Respect to A

We vary S_GU with respect to the gauge connection A, holding epsilon and B fixed. Under
A -> A + delta A (where delta A in Omega^1(Y^14, ad P)):

**Variation of S_YM:**

```
delta S_YM = 2 integral_{Y^14} <F_A, D_A delta A>_gimmel dvol_gimmel
           = 2 integral_{Y^14} <D_A* F_A, delta A>_gimmel dvol_gimmel    [integration by parts]
```

So the S_YM contribution to delta S / delta A is:

```
E_A^{YM} = 2 D_A* F_A in Omega^1(Y^14, ad P)
```

**Variation of S_Dirac:**

The Dirac term <psi, D_A psi> depends on A through the covariant derivative D_A = d + [A, .].
Varying A -> A + delta A:

```
delta S_Dirac = integral_{Y^14} <psi, [delta A, psi]>_S dvol_gimmel
              = integral_{Y^14} tr_S(psi* [delta A, psi]) dvol_gimmel
```

This is a fermionic bilinear term — it contributes to the gauge field equation but is of the
form J_fermion (a fermionic current), not a divergence-free identity structure. We set it aside
as an on-shell source term.

**Variation of S_IG:**

This is the critical term. We vary:

```
S_IG = integral_{Y^14} ||pi - Ad(epsilon^{-1}) B||^2_gimmel dvol_gimmel
```

with respect to A. Since pi = A - Gamma(epsilon) depends on A linearly (Gamma(epsilon) is
independent of A for fixed epsilon), we have:

```
delta pi = delta A
```

So:

```
delta S_IG = 2 integral_{Y^14} <pi - Ad(epsilon^{-1}) B, delta pi>_gimmel dvol_gimmel
           = 2 integral_{Y^14} <theta, delta A>_gimmel dvol_gimmel
```

(using theta = pi - Ad(epsilon^{-1}) B and delta pi = delta A).

Therefore the S_IG contribution to delta S / delta A is:

```
E_A^{IG} = 2 theta in Omega^1(Y^14, ad P)
```

### 1.3 The Full Euler-Lagrange Derivative

Combining (ignoring fermionic sources for the vacuum equation):

```
E_A = delta S_GU / delta A = 2 D_A* F_A + 2 theta + (fermionic bilinear)
```

Setting E_A = 0 (vacuum Euler-Lagrange equation) and ignoring fermionic sources:

```
D_A* F_A + theta = 0    (*)
```

This is the GU vacuum gauge field equation. It reads: the Yang-Mills force (D_A* F_A) is
balanced by the dark energy distortion term (theta). Rearranging:

```
theta = - D_A* F_A    (on the vacuum solution)
```

### 1.4 Identification with Assumption 3

The computation above shows:

**Claim A (derived, not assumed):** theta = pi - Ad(epsilon^{-1}) B is exactly the gauge-potential
sector of E_A^{IG} = delta S_IG / delta A. This follows from the linear dependence pi = A - Gamma(epsilon),
giving delta pi = delta A, so delta S_IG / delta A = 2 theta.

**Claim B (on-shell, derived):** From the vacuum field equation (*), theta = -D_A* F_A. Since
Noether's second theorem gives D_A* E_A = 0 off-shell (for the full E_A of any gauge-invariant
action), and E_A = 2 D_A* F_A + 2 theta, we get:

```
D_A*(D_A* F_A + theta) = 0    (off-shell, from gauge invariance of S_GU)
```

On the vacuum solution, theta = - D_A* F_A, so this becomes:

```
D_A*(-theta + theta) = D_A* 0 = 0
```

which is trivially satisfied. This is not the desired result D_A* theta = 0.

However, Noether's second theorem applied to the FULL gauge-invariant action S_GU gives:

```
D_A* E_A = D_A* (2 D_A* F_A + 2 theta) = 0    (off-shell identity)
```

This expands as:

```
2 D_A*(D_A* F_A) + 2 D_A* theta = 0    (off-shell)
```

Now D_A*(D_A* F_A): for Yang-Mills theory on any manifold, this identity D_A*(D_A* F_A) = 0
holds by the contracted Bianchi identity for the curvature:

```
D_A* D_A* F_A = 0    (identically, from D_A F_A = 0 by Bianchi and contracting)
```

Wait — this is not automatically true. Let us be precise. The Bianchi identity is:

```
D_A F_A = 0    (Bianchi, off-shell identity)
```

Taking the adjoint codifferential: D_A*(D_A* F_A) involves two adjoint operators. In general,
D_A* D_A* = 0 only if D_A* squares to zero, which is NOT the case (D_A is a first-order
operator and D_A^2 = F_A [curvature action], D_A*^2 is not generally zero).

**Correction to this line of reasoning:** D_A* D_A* theta != 0 in general. The off-shell
Noether identity gives:

```
D_A*(D_A* F_A + theta) = 0
```

This is ONE equation relating D_A* F_A and D_A* theta. It does NOT factorize into
D_A*(D_A* F_A) = 0 and D_A* theta = 0 separately.

### 1.5 Resolution: The Sector Identification IS the Key Step

The variational computation shows that theta contributes independently to E_A:

```
E_A = 2 D_A* F_A + 2 theta
```

This means theta is NOT the full gauge-potential sector of E_A — it is one of two contributions.
The sector identification "theta = gauge-potential sector of E_A" as stated in Assumption 3 is
ambiguous: it could mean:
- (3a) theta = E_A (the total EL derivative), or
- (3b) theta is a sector/summand of E_A contributing independently.

Under interpretation (3b), the derivation above CONFIRMS Assumption 3 at reconstruction grade:
theta appears as an independent additive sector of E_A^{IG}. The sector identification is
proved, not assumed, from the linear structure of pi = A - Gamma(epsilon).

Under interpretation (3a) (theta = full E_A), the derivation shows this is FALSE unless
D_A* F_A = 0 (Yang-Mills vacuum), which is not the general case.

**The correct reading of Assumption 3 for the Noether closure:**

The Noether's second theorem identity for the full gauge-invariant action S_GU gives:

```
D_A* E_A = 0    (off-shell)
D_A*(D_A* F_A + theta) = 0    (off-shell)
```

This is a JOINT identity, not D_A* theta = 0 separately. To extract D_A* theta = 0, one
needs an additional structure.

### 1.6 The IG Decomposition and Sector-Wise Divergence-Free Property

The key insight: the GU action decomposes as:

```
S_GU = S_YM + S_IG + S_Dirac
```

where S_YM and S_IG are SEPARATELY gauge-invariant (both couple to A through gauge-covariant
expressions: F_A for S_YM, and pi = A - Gamma(epsilon) for S_IG). If we treat S_YM and S_IG
as separately varying (which we can because they are separate sectors of the action), then
Noether's second theorem applied SEPARATELY to each sector gives:

**From S_YM alone (treating only the YM coupling to A):**

```
D_A* E_A^{YM} = D_A*(2 D_A* F_A) = 0    (off-shell, from gauge invariance of S_YM alone)
```

**From S_IG alone (treating only the IG distortion energy coupling to A):**

```
D_A* E_A^{IG} = D_A*(2 theta) = 2 D_A* theta = 0    (off-shell, from gauge invariance of S_IG alone)
```

**Question: Is S_IG separately gauge-invariant?**

S_IG = integral ||pi - Ad(epsilon^{-1}) B||^2_gimmel dvol_gimmel

Under a gauge transformation g in G:
- pi -> Ad(g)^{-1} pi (the distortion transforms in the adjoint)
- B -> Ad(g)^{-1} B + (something involving g and epsilon) — depends on how the IG transformation law acts on the B sector.
- epsilon -> g epsilon (left action on epsilon)

From the tau^+ equivariance of theta (proved at reconstruction grade in prior explorations):
theta = pi - Ad(epsilon^{-1}) B transforms as:

```
theta -> Ad(g_b)^{-1} theta    (right gauge transformation by g_b)
```

This means theta, and hence ||theta||^2_gimmel = ||theta||^2, transforms as:

```
||theta||^2 -> ||Ad(g_b)^{-1} theta||^2 = ||theta||^2    [Ad-invariance of the Killing form]
```

Therefore S_IG = integral ||theta||^2_gimmel dvol_gimmel IS separately gauge-invariant under
right G action. The gauge invariance of S_IG is a direct consequence of the equivariance of
theta (proved) and C1 (gimmel G-invariance, proved).

**Applying Noether's second theorem to S_IG alone:**

Since S_IG is gauge-invariant under local G transformations (local gauge invariance, not just
global — the equivariance theta -> Ad(g)^{-1} theta holds for all gauge transformations g,
including local/spacetime-dependent ones), Noether's second theorem for S_IG gives:

```
D_A* E_A^{IG} = 0    (off-shell)
E_A^{IG} = delta S_IG / delta A = 2 theta    [from 1.2 above]
```

Therefore:

```
D_A*(2 theta) = 0    (off-shell)
D_A* theta = 0    (off-shell, from gauge invariance of S_IG)
```

**This is the derivation of D_A* theta = 0 from a variational principle, without assuming
Assumption 3 in the original sense.**

The chain is:
1. S_IG = integral ||theta||^2 is gauge-invariant. [From equivariance of theta (proved) + gimmel G-invariance (proved).]
2. delta S_IG / delta A = 2 theta. [From linear structure pi = A - Gamma(epsilon), delta pi = delta A.]
3. By Noether's second theorem for the local gauge invariance of S_IG: D_A* E_A^{IG} = 0 off-shell.
4. E_A^{IG} = 2 theta (step 2).
5. Therefore D_A* theta = 0 off-shell.

### 1.7 Assessment of the Variational Route

**What is proved (reconstruction grade):**

The variational derivation succeeds conditionally. The three key inputs are:
- (V1) Equivariance of theta: theta -> Ad(g)^{-1} theta under right gauge transformations. [PROVED at reconstruction grade in prior explorations.]
- (V2) Linear structure: pi = A - Gamma(epsilon), with Gamma independent of A for fixed epsilon, giving delta pi = delta A. [DERIVED from the definition of pi as connection distortion; structurally sound but not verified from a primary written source.]
- (V3) S_IG is separately gauge-invariant. [Follows from V1 + gimmel G-invariance (C1, proved).]

With V1-V3, D_A* theta = 0 follows from Noether's second theorem applied to S_IG.

**Remaining gap at the reconstruction -> verified threshold:**

The action S_IG = integral ||theta||^2 dvol_gimmel must be part of the actual GU action as
written by Weinstein, or derivable from it. The transcript ([00:25:56]) describes field
equations schematically but does not write S_IG explicitly. The variational derivation is at
reconstruction grade because it reconstructs the action from the field equation structure,
rather than deriving the field equations from a primary written action.

The critical step V2 (linear structure delta pi = delta A) also requires the identification
pi = A - Gamma(epsilon), where Gamma(epsilon) is independent of A. This is the natural
definition of the distortion (connection minus reference connection), and it is linear in A
by construction. This step is structurally transparent, but its status depends on the explicit
form of Gamma(epsilon) in the GU construction.

## Route 2 — Algebraic Route: G-Equivariance Alone

### 2.1 The Algebraic Claim

The C1+C2 exploration showed (§C2-B, §C2-C) that G-equivariance of theta alone does NOT
imply D_A* theta = 0 without additional structure. The precise failure:

- G-equivariance: theta(A^g) = Ad(g)^{-1} theta(A) for all g in G. This says theta descends to the quotient W/G.
- D_A* theta = 0 requires knowledge of the spectrum of D_A* or a Bochner-type identity.

**Can one prove that any G-equivariant element of Omega^1(Y^14, ad P) in the adjoint rep is
automatically divergence-free?**

**Answer: No, in general.** A counterexample sketch:

Let Y be any Riemannian manifold, P a principal G-bundle, A a connection. Define
phi_0 = F_A in Omega^2(Y, ad P). This is G-equivariant: F_{A^g} = Ad(g)^{-1} F_A. Now
let phi = *_Y F_A in Omega^{n-2}(Y, ad P) (Hodge dual). This is also G-equivariant.
For n != 2, phi is a form of degree n-2 and has D_A* phi = D_A*(* F_A), which is generally
nonzero (it equals D_A F_A^* up to signs, and D_A F_A = 0 only by Bianchi, but D_A F_A != D_A* F_A).

More directly: D_A* theta = 0 is a differential equation on Y^14. G-equivariance is a
symmetry statement about how theta transforms along gauge orbits. These are genuinely
independent conditions. Without a coupling through the action, G-equivariance does not
constrain the divergence.

**Verdict on Route 2:** The algebraic route FAILS. G-equivariance alone is insufficient to
derive D_A* theta = 0 without an action-level input.

### 2.2 IG-Equivariance as a Potential Strengthening

The distortion theta is more than G-equivariant — it is IG-equivariant, transforming under
the full inhomogeneous gauge group. Could IG-equivariance (which is a larger symmetry) be
strong enough to force D_A* theta = 0?

**Analysis:**

The IG action on Omega^1(Y^14, ad P) is by the affine action:
```
A -> epsilon * A * epsilon^{-1} + B    (symbolic IG action)
```
The equivariance of theta under IG means theta is invariant (in a specific sense) under this
larger symmetry group. However:

- IG acts on W = Conn(P) (the affine space of connections), not on Y^14 directly.
- The divergence D_A* is defined on Y^14 for each fixed A.
- IG-equivariance constrains how theta changes as A moves along IG orbits in W, not how theta
  behaves in the Y^14-direction for fixed A.

The Y^14-divergence D_A* theta is a statement about the Y^14-differential of theta. IG-equivariance
constrains the W-variation of theta. These are different directions: Y^14 is the base manifold,
W is the field-space over Y^14.

**Conclusion:** IG-equivariance does not directly imply D_A* theta = 0 without the variational
input from Route 1. The algebraic route, even strengthened to IG-equivariance, does not close
the gap independently.

## Summary and Verdict

### What the Variational Route Achieves

The variational derivation (Route 1) produces a reconstruction-grade proof of D_A* theta = 0
under three explicit assumptions:

**V1 (used, reconstruction grade):** theta = pi - Ad(epsilon^{-1}) B is G-equivariant
(theta -> Ad(g)^{-1} theta under right gauge transformations).

**V2 (used, structurally transparent):** The GU action contains an IG distortion sector
S_IG = integral ||theta||^2_gimmel dvol_gimmel, and the variation of pi with respect to A
is delta pi = delta A (from the linearity pi = A - Gamma(epsilon) with Gamma independent of A).

**V3 (derived from V1 and C1):** S_IG is separately gauge-invariant under local G transformations.

From V1-V3, Noether's second theorem applied to S_IG gives D_A* E_A^{IG} = 0 off-shell, and
E_A^{IG} = 2 theta, giving D_A* theta = 0.

**This improves Assumption 3 from "structural identification inferred from transcript schematic"
to "derived from the linear structure of the distortion pi and the equivariance of theta,"
at reconstruction grade.**

Assumption 3 in its original form ("theta IS the gauge-potential sector of E_A") is now
partially resolved: theta IS the gauge-potential sector of E_A^{IG} (proved via V2). The full
E_A = E_A^{YM} + E_A^{IG} = 2 D_A* F_A + 2 theta, and theta is identified as the IG sector.

### The Remaining Gap

The reconstruction -> verified upgrade requires:
- (G1) The GU action explicitly contains S_IG as a separate gauge-invariant sector, derivable
  from a written GU action (not reconstructed from transcript). Without this, the variational
  derivation is a plausible reconstruction of GU, not a derivation from primary source.
- (G2) The local (spacetime-dependent) gauge invariance of S_IG must hold, not just global
  G-equivariance. The equivariance of theta proved in prior explorations shows theta -> Ad(g)^{-1}
  theta for ALL g in G (not just constant g), which does cover local gauge invariance. However,
  this proof itself is at reconstruction grade. If the equivariance were only for constant g,
  local gauge invariance would fail and Noether's second theorem would not apply.
- (G3) The separate applicability of Noether's second theorem to S_IG alone (treating S_YM
  as independent) requires that the coupling between S_YM and S_IG through A does not mix
  the Noether identities. If S_YM and S_IG couple through A in a non-additive way (e.g., if
  the GU action has cross-terms theta * F_A), the sector-wise Noether identity D_A* theta = 0
  would not follow independently.

### The Algebraic Route Result

The algebraic route fails. G-equivariance alone (or IG-equivariance) is insufficient to
derive D_A* theta = 0 without the variational structure. The obstruction is precise:
G-equivariance constrains field-space (W = Conn(P)) variation of theta; D_A* theta = 0 is
a base-manifold (Y^14) differential condition. These are orthogonal constraints.

## Result

**Assumption 3 is partially resolved at reconstruction grade.**

The variational route shows:
- theta is the gauge-potential sector of E_A^{IG} (derived from linear structure of pi = A - Gamma(epsilon)).
- S_IG is separately gauge-invariant (from equivariance of theta + gimmel G-invariance).
- By Noether's second theorem for S_IG, D_A* theta = 0 off-shell.

This is a structural derivation, not a reconstruction of transcript. It does not require Assumption 3 in its original form — rather, it proves Assumption 3's essential content (theta is a gauge-potential sector from which D_A* theta = 0 follows by Noether) from more primitive inputs.

**Verdict: CONDITIONALLY_RESOLVED.** The derivation is reconstruction-grade, not verified,
because:
- V2 (linear pi structure) is structurally transparent but not verified against a primary written GU action.
- V1 (equivariance of theta) is reconstruction-grade from prior explorations.
- G3 (sector-additivity of the GU action, no cross-terms theta * F_A) is not verified.

## Explicit Failure Conditions

**FC1 — GU action does not contain S_IG as a separate gauge-invariant sector.**
If the GU action contains theta only through coupling with F_A (e.g., S_cross = integral tr(theta * F_A)) and not as an independent ||theta||^2 term, then the sector-wise Noether argument does not apply. In that case, the full Noether identity D_A*(D_A* F_A + theta) = 0 gives a joint constraint, not D_A* theta = 0 separately. Falsification test: exhibit the GU action from a primary source and check whether ||theta||^2 appears independently.

**FC2 — Equivariance of theta is only global, not local.**
If the tau^+ equivariance of theta holds only for constant (global) g in G (not for local spacetime-dependent g(x)), then S_IG is invariant only under global G transformations. Noether's second theorem (for local gauge symmetry) would not apply, and only Noether's first theorem (for global symmetry) would give a conserved on-shell current — which, as shown in `dark-energy-c1-c2-path-gimmel-ginvariance-2026-06-23.md`, does not independently yield D_A* theta = 0. Falsification test: check whether the tau^+ equivariance proof in prior explorations explicitly uses local (x-dependent) gauge transformations or only global ones.

**FC3 — Linear structure pi = A - Gamma(epsilon) fails (Gamma depends on A).**
If the reference connection Gamma(epsilon) in the distortion pi = A - Gamma(epsilon) depends on A (rather than only on epsilon), then delta pi != delta A and the variation delta S_IG / delta A != 2 theta. The derivation of E_A^{IG} = 2 theta would fail, and theta would not be identified as a gauge-potential sector from a variational principle. Falsification test: verify from a primary source that Gamma(epsilon) depends only on the IG field epsilon and not on the gauge connection A.

## Implications for the Canon

The CONDITIONALLY_RESOLVED verdict for this derivation implies:

1. Assumption 3 in `canon/dark-energy-theta-divergence-free.md` is now partially resolved: the
   structural basis for identifying theta as a gauge-potential sector (from the linear structure
   of pi and equivariance of theta) is explicit. The remaining gap is verification against a
   primary source action.

2. The canon failure mode F1 ("structural identification fails because theta is not the
   gauge-potential sector of E_A") is partially discharged: the identification theta = E_A^{IG}
   is derived from construction. What remains is F1's verification clause (derive from a written
   variational principle, not a transcript).

3. The canon failure mode F3 ("level mismatch between equivariance and divergence-free") is
   addressed: the route from equivariance to D_A* theta = 0 goes through Noether's second
   theorem for S_IG, not through a direct functional-analytic argument from equivariance alone.

4. The canon upgrade condition 1 ("Prove Assumption 3 from a written variational principle")
   is partially met at reconstruction grade. Upgrade to RESOLVED requires FC1, FC2, and FC3
   to be verified or falsified.

5. The algebraic route failure (Route 2) is now documented as a GENUINE_OBSTRUCTION for that
   specific approach: G-equivariance alone cannot imply D_A* theta = 0.

## Open Questions

**OQ1 — Does the GU action explicitly contain ||theta||^2?**
The transcript ([00:25:56]) describes field equations schematically. A direct analysis of
any written GU action (if one exists from a Weinstein paper or lecture notes) would resolve
FC1. If ||theta||^2 appears as a separate sector, the derivation is confirmed. If it appears
only through coupling with F_A, FC1 fires.

**OQ2 — Local vs. global equivariance of theta.**
The prior explorations establish theta -> Ad(g)^{-1} theta. The proof uses the tau^+
homomorphism structure and double-coset identities. Does the proof hold for local g = g(x)
(spacetime-dependent gauge transformations)? If yes, FC2 is discharged and Noether's second
theorem applies. This is a targeted gap in the existing equivariance proof.

**OQ3 — Does D_A* theta = 0 hold off-shell or only on-shell?**
The derivation via Noether's second theorem for S_IG gives D_A* theta = 0 off-shell (the
Noether identity holds before imposing field equations). This is strictly stronger than the
on-shell version (which would follow from theta = -D_A* F_A on the vacuum solution). The
off-shell version is the correct characterization and is directly available from the variational
route if FC1-FC3 hold.

**OQ4 — Can FC3 be verified from the IG construction?**
The linearity pi = A - Gamma(epsilon) with Gamma independent of A is the structural claim.
In the IG context, epsilon encodes the metric/frame data, and Gamma(epsilon) is the
Levi-Civita connection of the metric induced by epsilon. This is standard (Gamma depends on
the metric, not on A), so FC3 should be dischargeable by a direct structural argument. A
coordinate-level verification would confirm this.

## References

- `canon/dark-energy-theta-divergence-free.md` — primary canon file with Assumption 3 statement and failure modes F1-F6.
- `explorations/dark-energy-cosmology/dark-energy-c1-c2-path-gimmel-ginvariance-2026-06-23.md` — C1 established, C2 fails independently; blocking failure condition identified.
- `explorations/dark-energy-cosmology/dark-energy-divergence-free-proof-2026-06-22.md` — equivariance of theta (V1), C1/C2 conditions identified.
- `explorations/dark-energy-cosmology/dark-energy-noether-closure-2026-06-22.md` — C3 path (Noether's second theorem for full S_GU).
- Brading, K. and Brown, H.R. (2000), "Noether's theorems and gauge symmetries," arXiv:hep-th/0009058 — Noether's second theorem and gauge identity.
- Weinstein, E., UCSD April 2025 transcript, [00:25:56] (schematic field equation).
