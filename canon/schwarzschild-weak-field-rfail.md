---
title: "GU Linearized Schwarzschild — R_fail Vanishes at O(M/r)"
status: canon
doc_type: canon
promoted_from:
  - "explorations/geometry-curvature-emergence/rfail-schwarzschild-oq2-weak-field-2026-06-23.md"
promoted_at: "2026-06-23"
verdict: OPEN
verdict_changed_from: CONDITIONALLY_RESOLVED
verdict_changed_at: "2026-06-26"
correction: "CORRECTION RFAIL-02 (2026-06-26): re-downgraded CONDITIONALLY_RESOLVED -> OPEN, following the CR-02 precedent (competing candidate live + discriminating computation unperformed). The headline 'GU passes solar-system tests' was compatibility-as-derivation on an IMPORTED Schwarzschild metric: the R_fail^GR=0 leg is trivial (any vacuum metric, no GU content; line 38), and the only genuine GU object (the Willmore-EL residual) is NONZERO with an UNRECONCILED leading order — O(M/r^4) (flat-space Laplacian Delta(M/r^2)=2M/r^4) vs the companion note's O(M/r^3) Weyl-proportional estimate, which by this file's own failure condition F1 would FALSIFY solar-system compatibility. The discriminating computation OQ2-A (the full gimmel Willmore-EL on the Schwarzschild section) is UNPERFORMED, so neither order is settled. The weak-field suppression is a compatibility check on an assumed answer, not a derivation of weak-field GR from GU.\n\nCORRECTION RFAIL-03 (2026-06-30): the RFAIL-02 order dispute is RESOLVED by direct computation — BOTH competing linear-in-M estimates were wrong, so BOTH are RETRACTED. (Script: tests/chase/MOVE-3/willmore_el_order.py, exact sympy on the imported linearized Schwarzschild graph section.) (1) The premise H_Schw ~ O(M/r^2) is a misidentification of mean curvature with the connection/distortion: the true linearized mean-curvature vector is H^(1)_ab = (M/r) eta_ab with signature (-1,+1,+1,+1), i.e. H^(1) ~ O(M/r), and (M/r) is HARMONIC (Delta(M/r)=0; only Delta(M/r^2)=2M/r^4 != 0). (2) Because H^(1) ~ M/r is harmonic, the linear-in-M Willmore-EL residual Delta H^(1) is IDENTICALLY ZERO — so the companion note's FALSIFYING O(M/r^3) AND this file's 'safe' linear O(M/r^4) are BOTH artifacts of the wrong H~M/r^2 premise; neither a=1 term exists. (3) The correct leading residual is O(M^2/r^4) — quadratic in M, the SAME object as the standing GENUINE_OBSTRUCTION Q(B) ~ B^2 ~ O(M^2/r^4). The exact r-exponent within the a=2 sector (candidates n in {3,4,6}) is not pinned, but every candidate is quadratic in M, hence safe for M/r<<1. (4) Failure condition F1 does NOT fire; solar-system smallness holds a fortiori (O(M^2/r^4) is strictly smaller than the retracted O(M/r^4)). NOTE: this is a computation on an IMPORTED Schwarzschild metric, NOT a derivation of GU dynamics. Verdict remains OPEN: the full gimmel Willmore-EL from GU's OWN action (OQ2-A) is still the open object; RFAIL-03 removes a false red flag, it does not close the derivation."
---

# GU Linearized Schwarzschild — R_fail Vanishes at O(M/r) [verdict OPEN, see RFAIL-02]

Canon means: safe to cite as the current public spine of the project. It does not mean proved physics.

> **VERDICT: OPEN (CORRECTION RFAIL-02, 2026-06-26; order dispute RESOLVED by RFAIL-03, 2026-06-30).** This is a weak-field smallness/compatibility check on an ASSUMED Schwarzschild metric, NOT a derivation of weak-field GR from GU. The `R_fail^GR = 0` leg is trivial (true for any vacuum metric — no GU content). The RFAIL-02 order dispute is now settled by direct computation (tests/chase/MOVE-3/willmore_el_order.py): **BOTH competing linear-in-M estimates were wrong and are RETRACTED.** The premise `H_Schw ~ M/r^2` misidentified mean curvature with the connection/distortion; the true linearized mean curvature is `H^(1)_ab = (M/r) eta_ab ~ O(M/r)`, and `M/r` is HARMONIC, so the linear-in-M Willmore-EL residual `Delta H^(1)` is IDENTICALLY ZERO. Thus the falsifying O(M/r^3) AND the "safe" linear O(M/r^4) are both artifacts; the correct leading residual is **O(M^2/r^4)** — quadratic in M, the same object as the standing Q(B) obstruction — so F1 does NOT fire and solar-system smallness holds a fortiori. Verdict stays OPEN because the full gimmel Willmore-EL from GU's OWN action (OQ2-A) is still unbuilt; RFAIL-03 removes a false red flag, it does not close the derivation. Do not cite "GU passes solar-system tests" as established.

## Scope

In Geometric Unity the section s: X4 -> Y14 = Met(X4) satisfies a field equation derived from the Willmore energy E[s] = integral |II_s^H|^2. The companion note (rfail-non-umbilic-schwarzschild-2026-06-23.md) established that exact Schwarzschild is NOT a Willmore-critical section — the section equation residual (Willmore-EL failure) is non-zero at nonlinear order O(M^2/r^4).

This result establishes that both failure modes are suppressed in the linearized (post-Newtonian weak-field) regime.

**Convention — two distinct failure objects.** This canon entry uses R_fail^{full}, a non-standard combined failure tensor. Readers using the standard GR definition should note:

```
R_fail^{GR}_{mu nu}  := G^X_{mu nu}[g_s] - 8piG T_{mu nu} - Lambda g_{mu nu}
                        [standard: Einstein equation residual on induced metric]

[Willmore-EL residual]_{mu nu} := -(delta E / delta s)_{mu nu}
                        [GU-specific: section equation residual]

R_fail^{full}_{mu nu} := R_fail^{GR}_{mu nu} + [Willmore-EL residual]_{mu nu}
                        [non-standard combined object used here]
```

These two failure modes are conceptually distinct: (A) measures whether the induced metric satisfies the Einstein equation; (B) measures whether the section satisfies the GU variational principle. They are independent at the level of definitions and must not be conflated.

**Claim.** For the GU section corresponding to linearized Schwarzschild (g_{mu nu} = eta_{mu nu} + h_{mu nu} with h ~ O(M/r)):

- R_fail^{GR}_{mu nu} = 0 exactly (Schwarzschild is vacuum Ricci-flat by definition — this is trivial and carries no GU-specific content).
- [Willmore-EL residual]_{mu nu}: the linear-in-M part is **IDENTICALLY ZERO** (RFAIL-03). The true linearized mean curvature is `H^(1)_ab = (M/r) eta_ab ~ O(M/r)`, which is HARMONIC, so `Delta H^(1) = 0`. The leading residual is therefore **O(M^2/r^4)** (quadratic in M — the same object as Q(B)). ~~O(M/r^4)~~ and ~~O(M/r^3)~~ are BOTH RETRACTED artifacts of the wrong premise `H_Schw ~ M/r^2`.
- Therefore R_fail^{full}_{mu nu} = 0 at O(M/r) **and at O(M/r^2)** — the first nonzero contribution is O(M^2/r^4), safe for M/r<<1.

The GU section-equation residual on the ASSUMED Schwarzschild metric is genuinely small — leading order O(M^2/r^4), quadratic in M (RFAIL-03, verified by tests/chase/MOVE-3/willmore_el_order.py). The prior O(M/r^3) vs O(M/r^4) dispute is dissolved: both were linear-in-M estimates built on a misidentification of mean curvature. This is a weak-field compatibility check on an imported metric, NOT a derivation that GU passes solar-system tests; the "passes solar-system tests" reading is RETRACTED (RFAIL-02). The full gimmel Willmore-EL from GU's own action (OQ2-A) remains the open object.

## Proof

**The Gauss identity (exact).**

For any section s: X4 -> Y14, the following holds as a differential-geometric tautology:

```
G^X_{mu nu} = G^Y_T_{mu nu} + Q_{mu nu}(B) + E^Psi_{mu nu}    [GAUSS IDENTITY]
```

where G^X is the 4D Einstein tensor on the induced metric g_s = s*(g), G^Y_T is the tangential projection of the 14D Einstein tensor, Q(B) is the extrinsic stress (quadratic in the second fundamental form B = II_s^H), and E^Psi is the Sp(64) gauge curvature contribution.

**Q(B) is quadratic — vanishes at O(M/r).**

From the explicit formula (codazzi-general-non-umbilic-2026-06-23.md §3.3):

```
Q^{TF}_{mu nu}(B) = [(1/2) H_i hat B^i_{mu nu} - (hat B^2)_{mu nu}]^{TF}
```

Both terms are quadratic in B. The second fundamental form B ~ O(M/r^2) at connection-level (or O(M/r^3) at curvature-level). In either case:

```
Q(B) ~ B^2 ~ O(M^2/r^4)    or better.
```

At O(M/r): Q(B) = 0. `[verified — algebraic quadraticity of the Q formula]`

**G^X = 0 for Schwarzschild (exact).**

Schwarzschild is an exact vacuum solution of 4D GR: G^X_{mu nu}[g_{Schw}] = 0 identically (Ricci-flat). This holds at all orders, not just at O(M/r). `[verified — standard GR]`

**Willmore-EL residual: linear-in-M part is identically zero; leading order is O(M^2/r^4).**

The Willmore-EL equation Delta^perp H^i = 0 is not satisfied for Schwarzschild (the exact-section obstruction). The linear-in-M part of the residual is:

```
[Willmore-EL residual]^{(1)}_{mu nu} ~ Delta H^{(1)}
```

**CORRECTED (RFAIL-03).** The prior estimate assumed `H^i_{Schw} ~ O(M/r^2)`, which is a misidentification of the mean curvature with the connection/distortion. Direct computation of the second fundamental form of the linearized Schwarzschild graph section (tests/chase/MOVE-3/willmore_el_order.py, exact sympy) gives the mean-curvature vector

```
H^{(1)}_ab = (M/r) eta_ab        [i.e. H^{(1)} ~ O(M/r), NOT O(M/r^2)]
```

Since `M/r` is HARMONIC (`Delta(M/r) = 0`; the graph-Hessian mean curvature `Box h_ab = 0` by harmonicity, and the horizontal `M/r^2` channel is also killed because `partial(M/r)` stays harmonic), the linear-in-M Willmore-EL operator vanishes identically:

```
Delta H^{(1)}_ab = 0    (all components — verified exactly)
```

So there is NO linear-in-M residual. Both the falsifying O(M/r^3) and the prior "safe" linear O(M/r^4) are RETRACTED artifacts of the wrong `H~M/r^2` premise. The leading nonzero residual is quadratic in M — see below. `[verified — tests/chase/MOVE-3/willmore_el_order.py]`

**E^Psi at O(M/r).**

In the linearized Schwarzschild vacuum (T_{mu nu} = 0, Lambda = 0), the natural gauge vacuum is Psi = 0 (or Psi ~ O(M/r)^2). Under this condition, E^Psi ~ O(M^2/r^4) and does not contribute at O(M/r). `[reconstruction — condition F2 below]`

**Assembly.**

The two failure modes are assessed separately:

```
R_fail^{GR}_{mu nu}  = G^X_{mu nu}[g_{Schw}] - 8piG T_{mu nu} - Lambda g_{mu nu}
                     = 0 - 0 - 0
                     = 0     (exact, all orders — Schwarzschild is Ricci-flat by definition)

[Willmore-EL residual]_{mu nu}
                     = Delta H^{(1)} + hat-B^2 terms
                     = 0 (linear-in-M) + O(M^2/r^4) (quadratic)   [RFAIL-03]
                     = 0     at O(M/r) AND at O(M/r^2)
                     ~ O(M^2/r^4)   [leading nonzero; = Q(B) obstruction]
```

(The exact r-exponent within the a=2 sector — candidates n in {3,4,6} from
(algebraic~M/r)x(Hessian~M/r^3), (Hessian~M/r^3)^2, and the note's
(connection-level B~M/r^2)^2 — is not pinned, but every candidate is
quadratic in M, hence safe for M/r<<1.)

Combined (non-standard convention):

```
R_fail^{full}_{mu nu} = R_fail^{GR}_{mu nu} + [Willmore-EL residual]_{mu nu}
                      = 0 + O(M^2/r^4)
                      = 0     at O(M/r) and O(M/r^2).
```

(The Gauss identity converts: G^X = G^Y_T + Q(B) + E^Psi. With Q(B) = 0 and E^Psi = 0 at O(M/r), G^Y_T = G^X = 0 for Schwarzschild. The combined failure tensor reduces to the Willmore-EL residual alone, whose linear-in-M part vanishes identically by harmonicity (RFAIL-03); the first nonzero contribution is O(M^2/r^4), the same quadratic object as Q(B).)

## Solar-System Implications

The leading GU correction to solar-system observables is now known to be quadratic in M (RFAIL-03): the linear-in-M residual vanishes identically by harmonicity, so the first correction enters at O(M^2/r^4) in curvature units — smaller still than the O(M/r) relative estimate quoted below. Solar-system smallness therefore holds a fortiori:

```
|R_fail^{full}| / |G^X_{GR prediction}| ~ O(M/r)   [upper bound; actual leading term is O(M^2/r^4), smaller].
```

For Mercury: O(M_sun / r_Mercury) ~ 3 x 10^{-8} even as an upper bound; the true leading correction is quadratically suppressed below this. Current measurement precision is ~10^{-5} (Cassini PPN gamma). GU deviations are below current and planned mission sensitivity (BepiColombo, GAIA). `[verified upper bound — tests/chase/MOVE-3/willmore_el_order.py; smallness a fortiori]`

The ratio prediction for the GU theta-field dark energy sector is separate and independent of this solar-system result.

## Assumptions

1. The linearized approximation g = eta + h with |h| ~ M/r is valid.
2. The Gauss identity holds as a tautology for any section (standard).
3. Q(B) is quadratic in B (algebraically exact from the Codazzi formula).
4. Gauge vacuum: E^Psi ~ O(M/r)^2 in the linearized Schwarzschild background (F2 condition).

## Known Failure Modes and Conditions for Upgrade

**F1 (Willmore-EL order). — DOES NOT FIRE (RFAIL-03, 2026-06-30).** The concern was that a linear-in-M O(M/r^3) residual would put the GU correction at O(1) relative to GR and falsify solar-system compatibility. Direct computation on the imported linearized Schwarzschild metric (tests/chase/MOVE-3/willmore_el_order.py) shows the mean curvature is `H^(1) ~ M/r` (harmonic), so the ENTIRE linear-in-M residual `Delta H^(1)` is identically zero — there is no a=1 term at any r-power. The leading residual is O(M^2/r^4), quadratic in M. F1 is therefore CLOSED as a falsification risk for the imported-metric computation. CAVEAT: this is a computation on GU's ambient/imported Schwarzschild input, not on GU's own dynamics; the falsification test below (the full gimmel Willmore-EL from E[s], OQ2-A) remains the genuine open object.
- Falsification test: Derive the linearized Willmore-EL equation from E[s] in the gimmel geometry explicitly.

**F2 (E^Psi gauge term).** If the Sp(64) gauge field Psi has a non-trivial O(M/r) component in the linearized Schwarzschild background, E^Psi ~ O(M/r) and contributes to R_fail at leading order.
- Falsification test: Solve the linearized Yang-Mills equation D_A* F_A = II_s^H for the Schwarzschild section and check the order of F_A.

**F3 (Linearized gimmel tangential curvature).** If the linearized G^Y_T has O(1) h-independent contributions at the tangential level, these require separate background equations.
- Falsification test: Compute G^Y_T^{(1)}_{mu nu}[h] explicitly from the gimmel Christoffel symbols.

## What Remains Open

- OQ2-A: Full linearized Willmore-EL equation from GU's OWN action E[s] in gimmel geometry — STILL OPEN. (RFAIL-03 closed F1 for the IMPORTED Schwarzschild metric: linear-in-M residual is identically zero by harmonicity, leading order O(M^2/r^4). But that is a check on an imported input, not a derivation from GU dynamics; OQ2-A is the genuine open object.)
- OQ2-B: Linearized Yang-Mills on Schwarzschild background (closes F2).
- OQ2-C: GU vs. GR at 1PN — whether PPN parameters gamma, beta differ at measurable level.
- OQ2-D: Strong-field regime (r ~ 2M), where O(M^2/r^4) terms become O(1).

## References

- Source exploration: rfail-schwarzschild-oq2-weak-field-2026-06-23.md (full computation with discipline tags)
- Companion note: rfail-non-umbilic-schwarzschild-2026-06-23.md (exact Schwarzschild obstruction)
- Standard GR: Wald, R.M., General Relativity, U Chicago Press, 1984. Ch. 4 (Schwarzschild vacuum, Ricci-flat).
- Codazzi formula: codazzi-general-non-umbilic-2026-06-23.md §3.3 (Q formula, quadratic in B).
- Bertotti, B., Iess, L., Tortora, P. (2003). Cassini PPN bound |gamma - 1| < 2.3 x 10^{-5}. Nature 425, 374.
