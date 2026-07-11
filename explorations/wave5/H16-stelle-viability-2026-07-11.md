---
title: "H16 — Stelle Viability: is the cleared gravity branch physically viable, or a relocated problem?"
artifact_type: exploration
status: exploration
updated_at: "2026-07-11"
wave: 5
condorcet_rank: 1
depends_on:
  - "tests/wave5/H16_stelle_viability.py"
  - "tests/wave3/H15_gravity_fork_R_term.py"
  - "tests/wave4/H18_forcing_II_vs_H.py"
  - "explorations/wave3/H15-gravity-fork-2026-07-11.md"
  - "explorations/wave4/H18-forcing-computation-2026-07-11.md"
  - "canon/ghost-parity-krein-synthesis.md"
  - "canon/schwarzschild-weak-field-rfail.md"
external_ref:
  - "Bateman & Turok, 'Escape from Ostrogradsky via Hidden Ghost Parity', arXiv:2607.00096 (30 Jun 2026)"
  - "Stelle, 'Renormalization of Higher Derivative Quantum Gravity', Phys. Rev. D 16, 953 (1977)"
  - "Mannheim, 'Making the Case for Conformal Gravity', Found. Phys. 42, 388 (2012), arXiv:1101.2186"
  - "arXiv:2603.07150 (massive tensor ghost -> inverted-harmonic-oscillator / DQFT), arXiv:2305.12549 (Anselmi purely-virtual particles)"
verdict: "CONTESTED-CORNER — not killed (R^X sign is attractive), not cleared (loop unitarity inherited-open). Confidence: moderate-high."
---

# H16 — Stelle Viability

**Discipline.** Exploration-grade. Compute → adversarially verify → honest grade. The
reproducible check is `tests/wave5/H16_stelle_viability.py` (exit 0, all PASS). No target
number imported. Where a bar is not computable from GU (loop unitarity), it is fenced with
primary sources and flagged tree-vs-loop, not asserted.

---

## The question H16 settles

H18 (Wave 4) upgraded H15's "verdict C, lean A" to **"A strongly favored / structurally
forced"**: GU gravity is Stelle-type `R^X + Weyl²` with a DeWitt `Λ`, and the resulting
distinct massive spin-2 ghost clears at **tree level** via Bateman-Turok's Krein ghost-parity.
The philosopher's caution H16 must answer: a *structural* clear that inherits **Stelle + a
massive ghost** may simply have relocated the problem into the **contested Stelle-Mannheim
corner** — renormalizable but with an unresolved massive-ghost unitarity dispute. Is the
branch genuinely **VIABLE**, or a relocated problem?

Four viability bars. Two are computable from GU's structure (BAR 3 sign, BAR 2 scale); two are
not (BAR 1 loop unitarity, BAR 4 GU-rescue) and are fenced with primary sources.

## BAR 3 — the R^X sign (the sharpest potential KILL): **PASS**

**This was the live kill.** An induced Einstein-Hilbert term of the wrong sign gives a
**repulsive / antigravity** disaster (a ghostly massless graviton, negative Newton constant).
H15 gave the Gauss identity `|II|² = |H|² − R^X`, so the Einstein term enters the energy
`E = ∫(|H|² − R^X)` with a **`−R^X`** sign. Does that sign attract or repel?

**Computed exactly (test BAR 3).** The `|H|²` (Bach/`Weyl²`) part fixes the `box²` coefficient
`+1` (forced by the positive-definite norm-square energy); the `−R^X` part adds `+m² box`
(H15 Part B/E: on TT `G⁽¹⁾ = −½ box`, so `−R^X → −(G⁽¹⁾) = +½ box`). Operator symbol
`P(s) = s(s + m²)`, propagator `1/(s(s+m²))`:

- **massless graviton pole `s = 0`: residue `+1/m² > 0` → HEALTHY.**
- massive spin-2 pole `s = −m²`: residue `−1/m² < 0` → the ghost.

This is the **correct Stelle ordering**: a healthy massless graviton (attractive, positive
Newton constant) plus a distinct massive ghost. The hypothetical **flip** `+R^X` gives
`P(s) = s(s − m²)`, massless residue `−1/m² < 0` → the **massless graviton itself becomes the
ghost → repulsive KILL**. The Gauss equation forces the *first* (attractive) sign.

**Loophole closed.** A residual worry: could a sign-convention mismatch between the Gauss `R^X`
and the standard "sphere has `R > 0`" convention secretly flip attraction to repulsion? Computed:
a round `n`-sphere has `R^X = n(n−1)/a² > 0` (all principal curvatures `1/a > 0`), sign-aligned
with the standard convention. So `−R^X` genuinely subtracts *positive* curvature; no hidden flip.

**The two signs are locked.** The same `−R^X` that makes the massless graviton healthy makes
`m² = +½ > 0` (real, non-tachyonic ghost). Attractive gravity and a real ghost mass are the
*same* consequence of the Gauss sign — you cannot get one without the other. **BAR 3 passes at
flat-ambient / structural grade.**

**Honest gate.** The PASS assumes (i) the overall `+` energy sign (natural for a norm-square,
but the Lorentzian continuation / YM overall-sign convention is not built) and (ii) the
**flat ambient**. In a curved ambient `|II|² = |H|² − R^X + R^Y_tangential`, and the DeWitt
`R^Y` correction could in principle shift — or, if it dominated with opposite sign, flip — the
effective EH coefficient. So BAR 3 is a PASS *gated on the unbuilt DeWitt `R^Y` normalization*
not overturning the sign. This is the same reconstruction-grade gate H15 Part E flagged.

## BAR 2 — the ghost scale: **plausibly SAFE (Planckian), magnitude gated**

`m² = +½` is a **dimensionless** coefficient ratio in H15's flat-ambient units. The physical
ghost mass² carries `[mass]²`, so it must be `m_ghost² = ½ · μ_DW²`, where `μ_DW` is the only
available dimensionful scale: the ambient **DeWitt metric-on-metrics normalization** on
`Y¹⁴ = Met(X⁴)` — the same coefficient that sets the induced `R^X` Planck scale.

- If `μ_DW ~ M_Planck` (the natural expectation for a metric-on-metrics normalization) →
  `m_ghost² = M_Pl²/2` → **Planckian → decouples → empirically SAFE** (this is exactly why
  generic Stelle's ghost is not phenomenologically excluded: at the Planck mass it is out of
  reach).
- Empirical **exclusion** would require `m_ghost` at an *observable* scale, i.e.
  `μ_DW << M_Pl` — an unnatural sub-Planckian hierarchy for a metric-on-metrics normalization.

So safety is the natural outcome and danger the fine-tuned one — but the **magnitude is
undetermined** without the unbuilt normalization. BAR 2 is *plausibly safe, unproven*. This is
a scaling/dimensional argument, not a magnitude computation, and is honestly labelled as such
in the test.

## BAR 1 — loop-level unitarity: **OPEN (inherited from generic Stelle)** — fenced

Fetched and read the primary source (Bateman & Turok, arXiv:2607.00096, full text).

- **BT prove positivity at TREE level only.** Their Conclusions: *"a general proof of the
  positivity of transition probabilities at tree level. The main obstacle to extending the
  proof to higher orders is that, like QCD, the massless theory has collinear infrared
  divergences which affect asymptotic states. These need to be carefully regulated and
  resummed."* (The abstract's "unitarity ... to all orders" refers to the optical-theorem
  *form* following from the spectral condition; the *positivity of probabilities* — the actual
  ghost-clearing result — is the tree-level theorem.)
- **BT's theory is a scalar, not gravity.** It is the "perfect-square" four-derivative scalar
  `S = −½∫(□ϕ + λ(∂ϕ)²)²`. The gravity connection (ref [25], *to appear*) is the
  **conformally-flat limit** of quadratic gravity, in which — their words — *"the spin two
  graviton, its ghost counterpart and a vector mode decouple, leaving the conformal factor of
  the metric as the only interacting degree of freedom."* I.e. BT's positivity, even at tree
  level, covers the conformal-factor scalar; **the massive spin-2 graviton ghost of Stelle
  gravity is precisely the mode that decouples and is *not* covered.**
- The `[P,S]=0`-under-renormalization analog (their diffeomorphism Ward identity preserving the
  PS form) is asserted only for that conformally-flat/scalar sector, in a to-appear companion,
  not proven for the spin-2 ghost.

**Consequence:** loop-level unitarity for the *full Stelle massive spin-2 ghost* is **open** in
BT — exactly the long-standing problem that keeps generic Stelle-Mannheim contested. The
generic corner is genuinely *contested*, not a proven kill: multiple competing, mutually
unaccepted proposed resolutions coexist — BT Krein/ghost-parity; Anselmi purely-virtual
"fakeons" (arXiv:2305.12549); Mannheim PT-symmetric / Pais-Uhlenbeck (arXiv:1101.2186);
inverted-harmonic-oscillator / direct-sum QFT (arXiv:2603.07150). None is a proven kill; none
is universally accepted.

## BAR 4 — does GU's specific structure help? **Kinematically yes, dynamically no**

- **Native ghost parity (a real asset).** Where generic Stelle must *posit* a ghost parity `κ`,
  GU supplies it structurally: canon `ghost-parity-krein-synthesis.md` (machine-checked,
  residual `0.0e+00`) shows the Krein form `K` *implements the Cartan involution of `so(9,5)`*
  and *equals* the ghost parity on the generation triplet. GU's `O(96,96)` Krein / `Sp(64)`
  fiber gives BT's required `κ` for free. This is the one place GU genuinely **helps**.
- **But it does not derive the loop condition.** The same canon *fences* (2026-07-06 big-swing,
  approved 2026-07-07): on the 192-dim triplet sector every GU-native core is spectrally
  sign-blind, a dynamics-*derived* parity never arises, and `[P,S]=0` requires `S` to be
  Krein-diagonalizable with real **simple** spectrum — yet at GU's three-generation
  **degeneracies** the `C`-operator exists but is **non-unique**. So GU provides `κ`
  kinematically and does **not** resolve `[P,S]=0` any better than generic Stelle.
- **No mass-ratio rescue.** The DeWitt `Λ` (H15 Part D, 0-derivative) and the ghost mass (H15
  Part A/E, the `R^X`/`Weyl²` ratio) are distinct objects; their ratio is **not fixed** by the
  built structure. GU adds no extra predictive constraint that would pin the ghost scale.

Net: GU helps *kinematically* (native `κ`), not *dynamically*. It does not worsen Stelle; it
also does not rescue the loop problem.

## VERDICT: CONTESTED-CORNER (the honest most-likely). Confidence moderate-high.

| Bar | Result | Grade |
|---|---|---|
| **3 — R^X sign** (sharpest kill) | **PASS** — Gauss `−R^X` → healthy massless graviton, attractive, positive `G`; the ghost is the massive spin-2 (correct Stelle order). Kill avoided. | exact computation, *flat-ambient* / gated on DeWitt `R^Y` |
| **2 — ghost scale** | plausibly **SAFE** — `m_ghost² = ½ μ_DW²`, Planckian for natural `μ_DW ~ M_Pl` → decouples | scaling/dimensional; magnitude gated on unbuilt normalization |
| **1 — loop unitarity** | **OPEN** — BT tree-only; their spin-2 ghost decouples; full-Stelle loop ghost unproven; contested corner (competing unaccepted resolutions) | primary-source fenced; *not* computed |
| **4 — GU rescue** | kinematic **yes** (native `κ`), dynamic **no** (`[P,S]=0` not derived; ratio unfixed) | canon-fenced |

**The branch is NOT KILLED.** The sharpest potential kill — a wrong-sign `R^X` giving
antigravity — does **not** fire: the Gauss equation forces the attractive sign, the massless
graviton is healthy, the Newton constant positive, the ghost real and (plausibly) Planckian,
and a native ghost parity + tree-level BT positivity are in hand. A genuine, non-trivial pass
on the load-bearing sign.

**But it does NOT fully CLEAR.** It survives *formally* while inheriting generic
Stelle-Mannheim's **unresolved loop-unitarity dispute**, which BT explicitly leave open (tree
only; spin-2 ghost uncovered) and which GU's structure resolves no better than the generic
theory. The residual gate is exactly GU's long-standing missing piece: a **ghost-parity-
preserving source-action dynamics** (`[P,S]=0` at loops), plus the DeWitt `R^Y`
sign/scale normalization. The philosopher's caution is **substantially vindicated**: the
structural clear does land in the contested corner — but it lands *on the good (attractive)
side* of it, having retired the wrong-sign kill.

### Honest caveats — what stays gated

- **BAR 3 is flat-ambient.** The overall `+` energy sign and the ambient `R^Y` correction are
  assumed/flagged, not built. A curved-ambient `R^Y` of opposite sign and larger magnitude
  could in principle flip the effective EH sign — the one scenario that would turn the PASS
  into a kill. This is the single most valuable next computation.
- **BAR 2 is scaling, not magnitude.** "Planckian → safe" is the natural expectation, not a
  derived number; the DeWitt normalization is unbuilt.
- **BAR 1 is not computed.** It is fenced with BT's own tree-vs-loop boundary and the contested
  literature; no GU computation bears on loops here.
- **Tree vs loop throughout.** Every "ghost clears" in this branch is a *tree-level* BT
  statement. The loop question is the frontier and is identical to GU's unbuilt source action.

## RE-RANK signal

- **Gravity does NOT fully clear; it stays CONTESTED (not killed).** Downgrade the internal
  read from "cleared modulo H16" to **"survives on the attractive side of the contested corner;
  the wrong-sign kill is retired; loop-unitarity remains the open gate."**
- **The wrong-sign KILL risk is retired** — this is H16's positive deliverable and removes a
  live falsification path. Councils should stop treating "wrong-sign antigravity" as an open
  threat to this branch (flat-ambient); it is closed pending only the `R^Y` sign check.
- **The next council reflection should focus on the two residual gates, in order:**
  1. **The ambient DeWitt `R^Y` sign/scale** — does the curved-ambient correction preserve the
     attractive `−R^X` sign (BAR 3's only gate) and set `μ_DW ~ M_Pl` (BAR 2's only gate)? Both
     the sign PASS and the scale SAFE collapse onto this single unbuilt normalization. Highest
     leverage: it can *confirm both* or *flip the sign into a kill*.
  2. **The loop `[P,S]=0`** — the genuinely hard, generic-Stelle-shared frontier, identical to
     GU's missing ghost-parity-preserving source-action dynamics. Not resolvable without the
     source action; the honest boundary is that GU is no better (and no worse) than generic
     Stelle here until that action exists.
- **The entropic/H5 route does not rise** (it would only rise on the H-class branch H18 argued
  against). The source-action build remains the joint gate on H15/H16/H18/H1 simultaneously.

---

*Filed 2026-07-11. Wave 5, Condorcet #1. Reproducible: `python tests/wave5/H16_stelle_viability.py`
(exit 0). Exploration-grade; not promoted to canon.*
