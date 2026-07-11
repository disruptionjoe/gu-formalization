# H15 — The Gravity Fork: does GU's forced geometry generate an Einstein-Hilbert R term?

2026-07-11. Wave 3, Condorcet #1. The decisive swing that H9 (wave 2) reduced the whole
gravity+ghost story to: **does GU's section-shape functional necessarily generate an intrinsic
scalar-curvature (R) term** — making gravity Stelle-type `R + Weyl^2` (a *distinct massive
ghost*, Bateman-Turok-ready, ghost **clears**) — **or does it leave gravity pure conformal
Bach `box^2`** (the *degenerate coincident-pole* case, ghost **open**)?

Companion test: `tests/wave3/H15_gravity_fork_R_term.py` (exact sympy / exact linear algebra,
15 checks, exit 0). No target number imported; every number returned (`4*pi`, `-1/2`, `+1/2`,
`1/2 eta_mn`, the residue pair `(+1/m2, -1/m2)`) is what the computation gives.

---

## The result in one line

**The fork collapses to exactly one binary — GU's OQ2-A functional choice `|II|^2` vs `|H|^2` —
and the two branches are now *computed*, not guessed:**

- **`|II|^2`-class** (full second fundamental form / full distortion norm `|theta|^2`) **⟹
  Branch A: Stelle `R + Weyl^2`, ghost CLEARS.** By the Gauss equation `|II|^2 = |H|^2 - R^X`,
  and because `int R^X` is **dynamical in 4D** (not topological — the 4D topological density is
  the Euler class `E_4`, not `R`), the `|II|^2` functional *necessarily* carries a genuine
  two-derivative Einstein-Hilbert kinetic term. That lifts the `box^2` degeneracy to
  `box(box + m^2)` — two distinct poles, a healthy graviton + a massive ghost — the
  non-degenerate case where Bateman-Turok's O(1,1)/Krein ghost parity applies.
- **`|H|^2`-class** (mean-curvature / conformal Willmore) **⟹ Branch B: pure Bach `box^2`,
  ghost OPEN.** Coincident double pole, the Pais-Uhlenbeck equal-frequency Jordan case where
  the split is singular.

**VERDICT: (C) UNDER-DETERMINED** at the level of the *built* action — the R-vs-no-R choice
*is* the `|II|^2`-vs-`|H|^2` OQ2-A datum, which GU's unbuilt source action has not fixed —
**but with a strong structural lean to Branch A (ghost clears).** Confidence: high on the
conditional computation (each branch's consequence is exact); moderate on the lean-to-A
(structural, not forced from the built action).

---

## What was computed (exact, reproducible)

### A. Gauss identity — the R-term source (exact, all dimensions)
For a submanifold in a flat ambient the traced-twice Gauss equation is the *pure algebra fact*
`R^X = (tr S)^2 - tr(S^2) = |H|^2 - |II|^2`, i.e.

```
|II|^2 = |H|^2 - R^X            (+ R^Y_tangential in a curved ambient)
```

Verified exactly for dim 2, 3, 4 (`R^X = 2·e_2(k)`, second elementary symmetric polynomial of
the principal curvatures). **The `|II|^2` functional carries the intrinsic scalar curvature
`R^X` with a definite minus sign; `|H|^2` does not.** This is *the* algebraic source of any
Einstein-Hilbert term. Cross-checked against the repo's own Gauss identity
(`G^X = G^Y_T + Q(B) + E^Psi`, canon/schwarzschild-weak-field-rfail.md): the trace of the
repo's `Q(B)` is exactly `tr Q(B) = |II|^2 - |H|^2 = -R^X` — same object.

### B. The dimensional crux — `int R^X` is topological in 2D, dynamical in 4D
This is the load-bearing discriminator, and it is where GU's being a **4D** theory decides the
fork:

- **2D:** `int K dA = 4*pi = 2*pi*chi` on a round sphere, radius-independent (Gauss-Bonnet) ⟹
  `int R^X` is **topological** ⟹ in 2D the `|II|^2 - |H|^2` difference is a pure topological
  term, **no R dynamics**. (This is why 2D Willmore is conformally invariant with no scale.)
- **4D:** the topological density is the Euler/Gauss-Bonnet `E_4 = Riem^2 - 4Ric^2 + R^2`,
  **not** `R`. The linearized Einstein-Hilbert EOM on a TT graviton is computed exactly:
  `G^(1)_yy = -1/2 box h_yy` — **second order and nonzero** (`R^(1) = 0` on TT, verified). So
  `int R^X` is the **genuine Einstein-Hilbert action**: a dynamical two-derivative,
  mass-carrying kinetic term, not a boundary/total-derivative and not topological.

**Consequence:** *once* `|II|^2` is the functional, 4D forces a dynamical `R^X`. Branch B
(pure Bach) requires the fine-tuned trace-only `|H|^2` with the `R^X` piece exactly absent.

### C. Operator / ghost consequence
- `|H|^2` leading Willmore-EL operator on TT `= box^2` (fourth order; matches the D-thread's
  `box^2 h = -4 Bach^(1)`). Symbol `P(s) = s^2` — **double root at s=0** (coincident pole,
  degenerate, Pais-Uhlenbeck equal-frequency Jordan case; Bateman-Turok O(1,1) split singular).
- `|II|^2 = |H|^2 - R^X` ⟹ operator `box^2 + m^2 box = box(box + m^2)`. Symbol `s(s + m^2)` —
  **two distinct roots** `s=0` (massless graviton) and `s=-m^2` (massive ghost). The TT
  propagator `1/(s(s+m^2))` partial-fractions into a **positive-residue** (healthy) pole and a
  **negative-residue** (ghost) pole `(+1/m^2, -1/m^2)` — the clean O(1,1)/Krein pair
  Bateman-Turok grade by ghost parity ⟹ **ghost clears**. As `m^2 → 0` the split coefficient
  `1/m^2 → ∞`: the pure-Bach (`|H|^2`) case is exactly the singular coincident-pole degeneration.

### D. Adversarial — the O(M^0) DeWitt background is Lambda, not R
The constant-section vertical SFF (ii-s-coordinate-formula sec 6.1, "constant sections are not
totally geodesic") has fiber-trace `eta^ab B_mn,ab = (1/2) eta_mn` **exactly** — a
cosmological-constant (Lambda) signature (stress `~ eta_mn`), **not** a scalar-curvature R
term. A Lambda term is **0-derivative**: it enters the EOM at `s^0`, shifting the vacuum/source,
and leaves the *kinetic* symbol `s(s+m^2)` and its pole structure **unchanged**. **So the DeWitt
`O(M^0)` piece does NOT lift the `box^2` degeneracy.** Only the `|II|^2` Gauss `R^X` term (a
`box`, `s^1`) does. This settles the task's sub-question (2) honestly: the DeWitt background is
branch-neutral — a Lambda candidate (per thread B), not the mass term that decides the fork.

### E. Sign
Flat-ambient model: `m^2 = (box coeff)/(box^2 coeff) = +1/2 > 0` — a **real, non-tachyonic**
massive pole, so the distinct massive ghost sits at a healthy real mass and Bateman-Turok
applies. The exact sign/magnitude is **gated** on (i) the OQ2-A normalization (`H` = trace vs
mean = trace/n rescales `m^2`) and (ii) the ambient DeWitt `R^Y` correction to the coefficient
(reconstruction-grade). Flagged, not overclaimed.

---

## Why the structural lean is to Branch A (Stelle / ghost clears)

Formally the branch is un-forced (the action is unbuilt), but three independent structural
facts push to `|II|^2`:

1. **GU is a Yang-Mills-type theory.** A YM action norms the *full* field strength `|F|^2`, not
   its trace. The GU-natural section functional is the full distortion norm
   `|theta|^2 = |II|^2`, not the trace-only `|H|^2`.
2. **The distortion is the full second fundamental form.** `s*(theta) = II_s` (DD1 /
   ii-s-coordinate-formula sec 7) is the *full* `II_s`, not its mean-curvature trace `H`.
3. **In 4D the R^X piece is unavoidably dynamical once `|II|^2` is chosen** (Part B). So Branch
   A is the *generic* outcome; Branch B needs the fine-tuned trace-only functional with `R^X`
   exactly absent.

Against the lean (honest): the repo's own leading statements sometimes write `E[s] = int |H|^2`
(the conformal-Willmore reading — schwarzschild-weak-field-rfail scope; D-thread D1), and the
`|II|^2`-vs-`|H|^2` binary is explicitly listed as the standing unbuilt OQ2-A datum
(willmore-residual-...-2026-07-11 "OQ2-A swing"). So the lean is a structural argument, not a
theorem.

---

## Honest grade and caveats

- **Grade:** *conditional computation* — each branch's consequence is exact and reproducible
  (Gauss identity exact all-dims; 4D EH linearization exact; propagator residues exact; DeWitt
  Lambda-trace exact). *Structural* for the lean-to-A and for the branch selection itself.
- **Caveats (not overclaimed):**
  1. **The branch is NOT forced.** This computes the *consequence* of `|II|^2` vs `|H|^2`, it
     does not derive which one GU's action selects. That is the residual OQ2-A datum. VERDICT is
     therefore (C), not (A) — the strong lean to A is structural.
  2. **Linearized about flat space.** The `box^2 + m^2 box` operator uses the exact Gauss
     *decomposition* of the functional plus the known linearization of each piece
     (`int|H|^2 → box^2`, `int R^X → G^(1) = -1/2 box`). The full nonlinear higher-codimension
     `|II|^2` first variation (Simons + normal-bundle curvature) is **not** computed here.
  3. **`m^2` magnitude is normalization-gated** (H-trace vs H-mean) and the coefficient receives
     an ambient DeWitt `R^Y` correction (reconstruction-grade). Only the *sign* (`m^2 > 0`,
     real pole) is the robust claim, and even it is flagged as convention/ambient-gated.
  4. **`E_4`-not-`R` topological fact in 4D** is used as a standard external result
     (Lanczos-Lovelock: the 4D Gauss-Bonnet EOM vanishes identically); the *positive* leg — EH
     linearized is nonzero second-order in 4D — is the part computed here.
  5. **Bateman-Turok tree-level Krein positivity** for a distinct massive ghost is an external
     fact (arXiv:2607.00096), used, not re-proved; loop-level and the interacting `[P,S]=0`
     remain open exactly as H9 fenced.

---

## RE-RANK signal

- **Does this CLEAR gravity?** *Not yet.* The gravity leg stays **REDUCED**, but from "pure
  Bach, ghost open, at-risk" to **"one computable binary away from clearing, with the
  ghost-clearing branch structurally favored."** The fork is no longer a vague conformal-vs-
  Einstein worry — it is the single datum "does OQ2-A norm the full `II` or only its trace `H`?"
- **The single forcing computation that decides it:** derive GU's section functional from its
  actual action (OQ2-A) and read whether it norms the full distortion (`|II|^2` → Branch A,
  ghost clears) or only the mean-curvature trace (`|H|^2` → Branch B, ghost open). Equivalently
  (D-thread framing): is OQ2-A the conformally-*invariant* Willmore combination (→ H-class, B)
  or the full `|II|^2` (→ II-class, A)?
- **Next council focus:** **H16 (Stelle viability)** becomes the natural #1 *conditional on* the
  forcing computation landing II-class — is the induced-`R` Einstein term the right sign, and is
  the ghost mass sensible once the ambient `R^Y` correction is included? Only if the action
  forces pure `|H|^2` does the entropic/H5 route rise instead. Either way, the highest-value
  next move is the **OQ2-A forcing computation** (`|II|^2` vs `|H|^2` from the action), which is
  now the sole gate on H15/H16/H1/H9 simultaneously.
