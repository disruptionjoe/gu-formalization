---
title: "Dark Energy C1+C2 Path — Gimmel G-Invariance and Noether's First Theorem"
date: 2026-06-23
problem_label: "dark-energy-c1-c2-path-gimmel-ginvariance"
status: reconstruction
verdict: OPEN
---

# Dark Energy C1+C2 Path — Gimmel G-Invariance and Noether's First Theorem

## Problem Statement

The canon file `canon/dark-energy-theta-divergence-free.md` is CONDITIONALLY_RESOLVED. The C3 Noether path closes D_A* theta = 0 conditional on Assumption 3 (structural identification: theta = gauge-potential sector of E_A), which is reconstruction-grade and unproved. This session attempts the C1+C2 alternative path:

- **C1:** Verify that the gimmel metric g_gimmel on Y^14 is preserved by the tau^+ double-coset IG action (G-invariance of the metric).
- **C2:** If C1 holds, apply Noether's first theorem to derive D_A* theta = 0 without invoking Assumption 3.

The instruction is to state which step is the blocking failure condition, and not to upgrade the dark-energy canon verdict.

## Established Context

- Y^14 = Met(X^4): bundle of Lorentzian metrics on 4-manifold X^4, total signature (9,5).
- Gauge group G = Sp(64), structure group of principal bundle P -> Y^14.
- Gimmel metric g_gimmel: vertical = Frobenius metric on fiber GL(4,R)/O(3,1), trace-reversed to signature (6,4); horizontal = pullback of cotangent bundle of X^4, contributing (3,1); combined (9,5).
- tau^+ homomorphism: tau^+(g) = (g, d_{nabla_aleph}(g) * g^{-1}), a group homomorphism G -> IG.
- theta = pi - Ad(epsilon^{-1})B, an ad-valued 1-form in Omega^1(Y^14, ad P).
- Equivariance result (reconstruction grade, prior explorations): theta transforms as Ad(g_b)^{-1} theta under right multiplication by tau^+(g_b); left factor g_a has no effect. Note: this result is labeled PROVED in prior exploration files but those files are reconstruction grade — no coordinate-level derivation from a written GU action exists. The claim is structurally sound and internally consistent, but has not been verified from a primary written source. Treating it as PROVED here would overstate the chain.
- Prior exploration `dark-energy-divergence-free-proof-2026-06-22.md` established C1 and C2 as the conditions needed for D_A* theta = 0 via the equivariance route.

## C1 — Gimmel G-Invariance

**Question:** Does the gauge group G = Sp(64) preserve the gimmel metric g_gimmel on Y^14?

**The key structural observation:** G = Sp(64) is the structure group of the principal bundle P -> Y^14. It acts on the fibers of P (the spinor/gauge data over Y^14), NOT on the base manifold Y^14 as a diffeomorphism group.

The base manifold Y^14 = Met(X^4) is a fixed geometric object — it is a fiber bundle over X^4 whose points are pointwise Lorentzian metrics on X^4. The gauge group G does not act on Y^14 as a transformation of the base. The gimmel metric g_gimmel is a tensor field on this base manifold Y^14, defined by the canonical Frobenius + trace-reverse + horizontal-pullback construction.

**Consequence:** Since G acts trivially on Y^14 as a manifold (it acts on the bundle data over Y^14, not on Y^14 itself), the gimmel metric g_gimmel is automatically G-invariant in the sense that:

```
(rho_g)* g_gimmel = g_gimmel    for all g in G
```

where rho_g: Y^14 -> Y^14 would be the base-manifold action of g. But since rho_g = id_{Y^14}, this is vacuously satisfied.

More precisely: the L^2 inner product on Omega^1(Y^14, ad P) is:

```
<alpha, beta>_{L^2} = integral_Y tr(alpha wedge star_gimmel beta) dvol_gimmel
```

Under the gauge group action on the ad P-valued factor: alpha mapsto Ad(g)^{-1} alpha, beta mapsto Ad(g)^{-1} beta:

```
<Ad(g)^{-1} alpha, Ad(g)^{-1} beta>_{L^2}
= integral_Y tr(Ad(g)^{-1} alpha wedge star_gimmel Ad(g)^{-1} beta) dvol_gimmel
```

The star_gimmel acts only on the form factor of alpha and beta (not on the ad P fiber). So:

```
= integral_Y tr(Ad(g)^{-1}(alpha wedge star_gimmel beta)) dvol_gimmel
= integral_Y tr(alpha wedge star_gimmel beta) dvol_gimmel    [Ad-invariance of tr]
= <alpha, beta>_{L^2}
```

The last step uses:
1. Ad-invariance of the Killing form: tr(Ad(g)^{-1} X Ad(g)^{-1} Y) = tr(XY) for all X, Y in g. (Standard: always true for the adjoint representation.)
2. G acts trivially on dvol_gimmel and star_gimmel (G does not act on Y^14 as a manifold).

**C1 RESULT: The gimmel metric is G-invariant (vacuously: G acts trivially on Y^14 as a base manifold). The L^2 inner product on Omega^1(Y^14, ad P) is G-invariant. This part succeeds at reconstruction grade.**

**Nuance on the double-coset IG action:** The tau^+ double-coset action is an action on IG (or on the space of connections W = Conn(P), which is an affine space over Omega^1(Y^14, ad P)). The double-coset action does NOT act on Y^14 directly; it acts on field configurations A in W. The gimmel metric is defined on Y^14, not on W. So "C1: gimmel preserved by double-coset action" is technically vacuous — the double-coset action does not touch Y^14.

The meaningful content of C1 is: the gauge group G acts on Omega^1(Y^14, ad P) in a way that preserves the L^2 structure needed for D_A* to be G-equivariant. This IS satisfied by the argument above.

## C2 — Noether's First Theorem Applied to Derive D_A* theta = 0

**Question:** Given C1 (gimmel G-invariance, hence G-invariance of the action S[A] = integral ||F_A||^2 dvol_gimmel), can Noether's first theorem yield D_A* theta = 0 without invoking Assumption 3?

**Noether's first theorem setup:** A GLOBAL (rigid) symmetry of a Lagrangian L gives a conserved on-shell current J via:

```
partial_I J^I = 0    (on-shell)
```

For the Yang-Mills action S[A] = integral_{Y^14} ||F_A||^2 dvol_gimmel invariant under constant (global) gauge transformations g_0 in G:

The infinitesimal gauge transformation is: delta_xi A = [xi, A] (adjoint action by a constant xi in Lie(G)). The Noether current for this global symmetry is:

```
J^I_a = delta L / delta (partial_I A^J_b) * (delta A^J_b / delta xi^a)
       = 2 g_gimmel^{IK} F_{KJ,b} * f^b_{ac} A^J_c
```

where f^b_{ac} are the structure constants of Lie(G). The on-shell conservation law is:

```
D_I J^I_a = 0    (on-shell)
```

(covariant conservation, replacing partial_I with D_I because A is a connection).

**The identification problem:** D_A* theta = 0 states that theta = pi - Ad(epsilon^{-1})B, viewed as an element of Omega^1(Y^14, ad P), has vanishing codifferential. For this to follow from Noether's first theorem, one would need:

```
theta = J    (theta equals the Noether current for the global G-symmetry)
```

The Noether current J is expressed in terms of F_A (the curvature). Specifically J ~ D_A* F_A. The identification theta = J is EQUIVALENT to the structural identification theta = D_A* F_A, which is Assumption 3 in the C3 path restated as "theta = Noether current."

**This is the blocking failure condition.**

Noether's first theorem for global G-symmetry gives D_A J = 0 on-shell for J ~ D_A* F_A. This does NOT give D_A* theta = 0 unless one additionally proves theta = J, i.e., theta = (Noether current) = D_A* F_A. This identification is the same structural identification as Assumption 3 in the C3 path, just approached from a different direction.

**Detailed failure analysis:**

There are three ways one might attempt C2:

**Attempt C2-A: theta is the Noether current**

Claim: theta = pi - Ad(epsilon^{-1}) B is the Noether current for global G-symmetry.

Status: UNPROVED. The Noether current for global G-symmetry of S = integral ||F_A||^2 is J ~ D_A* F_A (computed directly). Establishing theta = J requires either: (a) deriving theta from a variational principle showing it IS D_A* F_A (= Assumption 3, C3 path), or (b) showing that the GU field content forces theta and D_A* F_A to coincide by some algebraic identity. Neither (a) nor (b) is available without further GU-specific input.

**Attempt C2-B: Equivariance + G-invariant metric -> perpendicularity -> D_A* theta = 0**

Claim: Since theta is G-equivariant (proved) and g_gimmel is G-invariant (C1 proved), theta is L^2-perpendicular to all gauge-orbit tangent vectors D_A xi, hence D_A* theta = 0.

Analysis: The perpendicularity argument says: for all xi in Omega^0(Y^14, ad P):

```
<theta, D_A xi>_{L^2} = 0  ==>  D_A* theta = 0
```

The left side:
```
<theta, D_A xi>_{L^2} = integral_Y tr(theta wedge star_gimmel D_A xi) dvol_gimmel
```

G-equivariance of theta means: for any g in G, theta(A^g) = Ad(g)^{-1} theta(A). Differentiating at g = e in direction xi_0:

```
d/dt|_0 theta(A + t D_A xi_0) = delta theta / delta A . D_A xi_0
```

This is the linearization of theta along the gauge orbit — which is NOT automatically zero. G-equivariance is a statement about how theta transforms ALONG GAUGE ORBITS (equivariance under finite gauge transformations), not a statement that theta is L^2-perpendicular to the infinitesimal directions D_A xi.

The precise implication of G-equivariance for perpendicularity:

For G-equivariance to imply L^2-perpendicularity to gauge orbits, one needs:

```
d/dt|_0 ||theta(A + t D_A xi_0)||^2_{L^2} = 0    for all xi_0
```

This would follow if theta maps gauge orbits to gauge orbits in an isometric way. But theta is defined as a function on W = Conn(P) (an affine space), not as a section of a G-equivariant bundle over the moduli space W/G. The equivariance theta(A^g) = Ad(g)^{-1} theta(A) means theta DESCENDS to a section of the adjoint bundle over W/G, but this descent does not imply D_A* theta = 0 directly.

More concretely: the Einstein analogy (G_{mu nu} equivariant -> div G = 0) works because G_{mu nu} is a Diff(X)-equivariant section of Sym^2 T*X constructed from the Riemann curvature via the Hilbert action, and the Bianchi identity holds identically. The analogous statement for theta would be: theta is constructed as the Euler-Lagrange derivative of a gauge-invariant action (so D_A* theta = 0 by Noether's second theorem). But that is the C3 path, not a consequence of C1+C2 alone.

**Attempt C2-C: Use G-invariance of metric + G-equivariance of theta to build a direct functional-analytic argument**

One could try: the space Omega^1(Y^14, ad P) decomposes under the G-action as a direct sum of G-isotypic components. The component of theta in each isotypic subspace must satisfy D_A* = 0 within that component if the isotypic projection commutes with D_A*. But:

1. G-equivariance of D_A* (proved above: D_{A^g}* (Ad(g)^{-1} phi) = Ad(g)^{-1} D_A* phi) does confirm that D_A* commutes with the G-action. So D_A* maps each G-isotypic subspace to itself.

2. However, this does NOT imply D_A* theta = 0 on any isotypic subspace. It only says that D_A* theta lives in the same isotypic subspace as theta.

3. The isotypic decomposition argument would need an additional input: that the specific isotypic subspace containing theta is in the kernel of D_A*. This requires knowing the spectrum of D_A*, which in general is not trivial.

**Summary: C2 FAILS as an independent route to D_A* theta = 0.**

None of the three attempts can derive D_A* theta = 0 from C1 alone without invoking the structural identification theta = D_A* F_A (= Assumption 3). The C1+C2 path, as described in the canon file, does not provide an independent verification route.

## Blocking Failure Condition

**C2 is the blocking step. The specific failure condition is:**

Noether's first theorem for global G-symmetry of S[A] = integral ||F_A||^2 dvol_gimmel gives an on-shell conservation law D_A J = 0 for the Noether current J ~ D_A* F_A. To derive D_A* theta = 0 from this, one must identify theta with J (i.e., theta = D_A* F_A). This identification is precisely Assumption 3 from the C3 path (structural identification: theta is the gauge-potential sector of the Euler-Lagrange derivative E_A = D_A* F_A). The C1+C2 path does not avoid Assumption 3; it encounters the same logical gap at the identification step.

**Formally:** Let J_1 be the Noether's-first-theorem current for global G-symmetry. Then:
- Noether's first theorem gives: D_A* J_1 = 0 on-shell. (Here J_1 ~ D_A* F_A, computed by standard variation.)
- C1+C2 cannot derive: theta = J_1, because this identification requires a variational derivation showing theta appears as a sector of delta S / delta A.
- Without theta = J_1, knowing D_A* J_1 = 0 does not give D_A* theta = 0.

The gap is the same as Assumption 3 at a different level. The C1+C2 path, even with C1 fully established, does not supply an independent route.

## What C1 Does Provide

Even though C2 fails as a standalone route, C1 (gimmel G-invariance) is NOT vacuous — it plays a supporting role:

1. **It validates the gauge-invariance of the Yang-Mills action** S[A] = integral ||F_A||^2 dvol_gimmel. The gauge invariance uses C1 in the step tr(Ad(g)^{-1} F_A wedge star_gimmel Ad(g)^{-1} F_A) = tr(F_A wedge star_gimmel F_A). Without C1, this step fails.

2. **It is a necessary input into the C3 path.** The C3 path (Noether's second theorem for local gauge invariance) requires the Yang-Mills action to be gauge-invariant. C1 provides this. So C1 is a prerequisite for C3, not an alternative to it.

3. **It validates F5 in the canon file.** F5 (gimmel G-invariance not independently established) is discharged: C1 holds at reconstruction grade by the argument above (G acts trivially on Y^14 as a base manifold; gimmel is a base-manifold tensor; hence gimmel is G-invariant).

## Clarification on "Noether's First vs. Second Theorem"

The canon file describes the C1+C2 path as "verify gimmel G-invariance, then apply Noether's first theorem." However, the correct theorem for deriving D_A* E_A = 0 from gauge invariance is Noether's SECOND theorem (for local/gauge symmetry), not Noether's first theorem (for global/rigid symmetry).

- **Noether's first theorem** (global symmetry) -> conserved on-shell current J satisfying partial_I J^I = 0.
- **Noether's second theorem** (local/gauge symmetry) -> off-shell identity D_A* E_A = 0 for E_A = delta S / delta A.

The path "C1 (gimmel G-invariance) + Noether's second theorem" IS valid and gives D_A* E_A = 0 off-shell. But that is the C3 path, not a separate C1+C2 path. The C3 path then requires theta = E_A to conclude D_A* theta = 0 — which is Assumption 3.

If the C1+C2 path intends to use Noether's FIRST theorem (global G-invariance), then:
- C1 is needed and holds (reconstruction grade, as shown above).
- C2 (applying Noether's first theorem to derive D_A* theta = 0) fails because the Noether current for global G-symmetry is J ~ D_A* F_A, not theta, and identifying theta = J is equivalent to Assumption 3.

The C1+C2 path as described does not provide an independent route under either reading.

## Result

**C1: ESTABLISHED** at reconstruction grade. The gauge group G = Sp(64) acts trivially on Y^14 as a base manifold; the gimmel metric is therefore automatically G-invariant. The L^2 inner product on Omega^1(Y^14, ad P) is G-invariant (by Ad-invariance of the Killing form and trivial base-manifold action). Failure mode F5 in the canon file is discharged.

**C2: FAILS** as an independent route to D_A* theta = 0. The blocking failure condition:

> To derive D_A* theta = 0 from C1 and Noether's first theorem for global G-symmetry, one must identify theta as the Noether current J for global G-symmetry of S[A]. The Noether current is J ~ D_A* F_A. Establishing theta = J requires the structural identification theta = D_A* F_A — exactly Assumption 3 from the C3 path. The C1+C2 path does not avoid Assumption 3; it restates it.

**Verdict: OPEN.** The C1+C2 path does not close D_A* theta = 0. The dark-energy divergence-free claim remains CONDITIONALLY_RESOLVED (C3 path, conditional on Assumption 3). The canon verdict is not upgraded in this session.

## Open Questions

1. **Is there a C1+C2 variant that avoids Assumption 3?** One would need: a direct algebraic identity showing theta satisfies D_A* theta = 0 as a consequence of its construction (pi - Ad(epsilon^{-1})B), without referring to the variational sector identification. The algebraic route (§8, path 3 of dark-energy-divergence-free-proof-2026-06-22.md) is the closest candidate: show that any G-equivariant element of Omega^1(Y^14, ad P) in the adjoint representation of IG is automatically divergence-free with respect to the IG-invariant inner product. This would be a purely representation-theoretic statement about IG and would not require Assumption 3.

2. **Can C1 be upgraded to verified grade?** The argument above is at reconstruction grade (it appeals to the structural fact that G acts trivially on Y^14, but does not provide a coordinate-level verification of the gimmel metric components). A coordinate computation of g_gimmel in local coordinates on Met(X^4), explicitly checking G-invariance of each component, would upgrade C1 to verified.

3. **Does the C3 path gap have a shortcut?** Assumption 3 requires a variational derivation showing theta = delta S / delta A for some sector of the GU action. A direct computation starting from the GU field equations (as described in the transcript at [00:25:56]) and identifying which sector of delta S / delta A produces pi - Ad(epsilon^{-1}) B would close the gap.

## References

- `canon/dark-energy-theta-divergence-free.md` — primary canon file with CONDITIONALLY_RESOLVED verdict and explicit failure modes F1-F5.
- `explorations/dark-energy-divergence-free-proof-2026-06-22.md` — equivariance proof (§2), C1/C2 conditions identified (§5).
- `explorations/dark-energy-noether-closure-2026-06-22.md` — C3 path (Noether's second theorem).
- Brading and Brown (2000), "Noether's theorems and gauge symmetries," arXiv:hep-th/0009058 — distinction between first and second Noether theorems.
