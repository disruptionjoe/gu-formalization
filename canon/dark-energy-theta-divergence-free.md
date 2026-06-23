---
title: "Dark Energy Theta Field — Divergence-Free and Dynamic"
status: canon
doc_type: canon
promoted_from:
  - "explorations/dark-energy-divergence-free-proof-2026-06-22.md"
  - "explorations/dark-energy-noether-closure-2026-06-22.md"
promoted_at: "2026-06-23"
verdict: CONDITIONALLY_RESOLVED
correction: "CORRECTION DARK-ENERGY-01 (2026-06-23): Downgraded from RESOLVED. The C3 Noether path closes D_A* theta = 0 only if Assumption 3 holds (structural identification, reconstruction grade). Assumption 3 is not proved. Neither the C3 path nor the C1+C2 path is complete."
---

# Dark Energy Theta Field — Divergence-Free and Dynamic

Canon means: safe to cite as the current public spine of the project. It does not mean proved physics.

## Scope

GU replaces the cosmological constant Lambda·g_{mu nu} with a dynamical object theta = pi - epsilon^{-1} B epsilon, where (epsilon, B) is an element of the inhomogeneous gauge group IG = G semidirect Omega^1(Y, ad P). The two central claims are:

1. theta is not forced constant (unlike Lambda).
2. D_A* theta = 0 (theta is divergence-free, analogous to the contracted Bianchi identity for G_{mu nu}).

## Proof

**Step 1 — Setup.**

Fix a distinguished connection nabla_aleph and define the tau-plus homomorphism:
```
tau^+: G -> IG,    g |-> (g, d_{nabla_aleph}(g) · g^{-1})
```
This is a group homomorphism by direct computation from the IG multiplication law. For omega = (epsilon, B) in IG, define:
```
theta = pi - Ad(epsilon^{-1}) B     (= pi - epsilon^{-1} B epsilon)
```
where pi = nabla - epsilon · nabla_aleph (the distortion).

**Step 2 — Equivariance (PROVED, unconditional).**

Under the double-coset action tau^+(g_a) · omega · tau^+(g_b):
- The left factor g_a has NO effect on theta. The Maurer-Cartan correction in the left multiplication cancels exactly with the shift in pi. `[verified — direct computation from tau^+ definition]`
- The right factor g_b acts by: theta |-> Ad(g_b)^{-1} theta. `[verified]`

Therefore theta is G-equivariant under the right action of tau^+(G), transforming in the adjoint representation.

**Step 3 — Not forced constant (PROVED, unconditional).**

Lambda · g_{mu nu} is forced constant by the Levi-Civita annihilation of the metric: nabla^mu g_{mu nu} = 0, which forces partial^mu Lambda = 0. This mechanism does NOT apply to theta: theta is in Omega^1(Y, ad P) and its divergence-free property comes from G-equivariance (Step 2), not from any annihilation equation that would force theta to be covariantly constant. The field theta can vary from point to point as the curvature F_A varies. `[verified]`

**Step 4 — D_A* theta = 0 via Noether's second theorem (C3 path, CONDITIONALLY COMPLETE).**

The C3 path closes the divergence-free claim conditional on Assumption 3 (see below). It does not require explicit verification of gimmel G-invariance (the C1+C2 path), but Assumption 3 is itself reconstruction grade and unproved. The argument:

The GU action on Y^14 contains a Yang-Mills sector S[A] = integral ||F_A||^2. This action is gauge-invariant under G. By Noether's second theorem, for any gauge-invariant action functional S[A], the Euler-Lagrange derivative E_A = delta S / delta A satisfies:

```
D_A* E_A = 0     (on-shell and off-shell)
```

The GU field equations identify theta as proportional to the gauge-potential sector of E_A (the sector of delta S / delta A that does not involve the metric sector of IG). The explicit identification is:

```
theta = (gauge potential sector of E_A)    [structural identification, reconstruction grade]
```

With this identification, D_A* theta = 0 follows from Noether's second theorem for the Yang-Mills action, without computing gimmel G-invariance separately. The gauge-invariance of the Yang-Mills action on Y^14 is standard. `[verified for the Yang-Mills action; reconstruction for the structural identification that theta is the relevant E_A sector]`

## Assumptions

1. The tau^+ homomorphism is correctly defined as above (standard).
2. The GU action contains a gauge-invariant Yang-Mills sector on Y^14.
3. **Structural identification (reconstruction grade, unproved):** theta = pi - epsilon^{-1} B epsilon is the gauge-potential sector of the Euler-Lagrange derivative E_A for the GU action. This identification is inferred from the schematic field equation in the transcript ([00:25:56]); no coordinate computation or variational derivation from a written GU action has been supplied.

Assumption 3 is reconstruction-grade and is the load-bearing gap in the C3 path. The C3 Noether argument is valid for any gauge-invariant action functional, but the claim D_A* theta = 0 requires that theta IS the relevant E_A sector — a fact that must be derived, not assumed. The C1+C2 alternative path (gimmel G-invariance) remains open as an independent verification route and must be completed before either path can support a RESOLVED verdict.

## Known Failure Modes

- **F1 — C3 structural identification fails.** If theta is not the gauge-potential sector of the Euler-Lagrange derivative E_A for the GU action (e.g., if it is a different sector of the IG splitting, or if the GU field equation does not literally read D_A*F_A - theta = 0), the Noether argument does not close the divergence-free claim. This is the primary unresolved gap. Closure condition: derive the identification theta = D_A*F_A from a written variational principle for the GU action, not from transcript reconstruction.
- **F2 — C1+C2 path incomplete; neither path is fully verified.** The C1+C2 alternative (gimmel G-invariance) is explicitly acknowledged as open. The C3 path rests on reconstruction-grade Assumption 3. As of this writing, NEITHER path is complete. The CONDITIONALLY_RESOLVED verdict reflects that the C3 argument is structurally sound conditional on Assumption 3, not that a complete proof exists via either route.
- **F3 — Level mismatch between equivariance and divergence-free.** The equivariance proved in Step 2 is at the level of the gauge group acting on connections (affine space over Omega^1(Y, ad P)). The divergence-free claim is about a covariant divergence D_A* of a form on Y^14. The C3 route bypasses this by appealing to Noether's theorem at the action level, but the bypass is valid only if the action identification in F1 holds.
- **F4 — Full GU action modification.** The claim assumes the GU action is Yang-Mills type on Y^14. Modifications to the action (e.g., additional topological terms, Chern-Simons contributions, or IG-covariant corrections beyond the Yang-Mills sector) could alter the Euler-Lagrange sector structure and invalidate the identification theta = D_A*F_A.
- **F5 — Gimmel G-invariance not independently established.** The gauge-invariance of the Yang-Mills action on Y^14 requires that the gimmel metric is G-invariant (so that ||F_A||^2 is gauge-invariant). This is the C1 condition. At exploration grade it is taken as confirmed via the canonical Frobenius + trace-reverse + horizontal-pullback construction, but no full coordinate-level verification exists. If C1 fails, the Yang-Mills action is not gauge-invariant and the Noether argument does not apply.

## Upgrade Conditions (to RESOLVED)

Both of the following must be satisfied before this entry can be upgraded to RESOLVED:

1. **Prove Assumption 3 from a written variational principle.** Supply a coordinate or functorial derivation showing that theta as defined (pi - epsilon^{-1} B epsilon) is the gauge-potential sector of delta S / delta A for a specified GU action on Y^14.
2. **Complete at least one of C3 or C1+C2 as an independent verification.** Either close the structural identification (C3 complete) and verify gimmel G-invariance (C1 complete) as a cross-check, or complete the C1+C2 path (prove gimmel G-invariance and compute the Noether current directly from gauge-covariance of the gimmel metric) as an alternative independent route.

## What This Does Not Establish

- The 120-orders-of-magnitude problem is solved in the sense of a derivation from GU first principles. What is established is the STRUCTURAL resolution: the fine-tuning in Lambda-CDM arises because Lambda is forced constant; the analogous term in GU (theta) is not forced constant and is instead G-equivariant. Whether the effective dark energy vacuum expectation value tracks observations quantitatively requires a separate cosmological computation (see theta-field FLRW exploration).
- Gimmel G-invariance (the C1+C2 path). This remains an open verification cross-check.

## The Einstein Analogy

| Einstein G_{mu nu} | GU theta |
|---|---|
| Divergence-free via contracted Bianchi identity | Divergence-free via Noether's 2nd theorem |
| Lambda forced constant by nabla g = 0 | theta not forced constant — equivariance is not annihilation |
| Diffeomorphism orbits in Met(X) | Gauge orbits in Conn(P) |

## References

- Weinstein, E., UCSD April 2025 transcript, [00:02:05], [00:23:02], [00:25:56].
- Source explorations: dark-energy-divergence-free-proof-2026-06-22.md (§2: equivariance; §4: dynamism; §6: Bianchi analog) and dark-energy-noether-closure-2026-06-22.md (C3 path: Noether closure).
- Standard reference for Noether's second theorem: Brading, K. and Brown, H.R. (2000), "Noether's theorems and gauge symmetries," arXiv:hep-th/0009058.
