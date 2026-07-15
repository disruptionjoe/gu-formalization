---
artifact_type: exploration
label: W224
created: 2026-07-15
status: exploration
posture: adversarial; truth-seeking; native-object first; construction-fork explicit; no verdict movement
title: "W224 native good-stable DYNAMICAL vacuum: the only built vacuum candidate is an internal singlet, so its dynamical isotropy is the full non-compact Sp(32,32;H) and no good-stable grading is dynamically supplied -- a precise input failure, not a free Z/2 and not a moduli space"
grade: "EXACT for the finite-dimensional Lie-group dimensions and the singlet-isotropy / Proposition-1 consequence; SOURCE-AUDIT for the vacuum-arc synthesis (W213-W217) and the representation-type identification of the order parameter; STRUCTURAL for the located gap (what a dynamical good stable would have to supply); OPEN for the interacting mirror-sector condensate, the source action, the physical state space, and the observable algebra. Machine regression: tests/W224_native_good_stable_dynamical_vacuum.py (35/35, exit 0, positive controls first). No canon, RESEARCH-STATUS, verdict, bar(b), H59, or generation-count change."
depends_on:
  - explorations/W213-true-vacuum-effective-potential-2026-07-14.md
  - explorations/W214-true-vacuum-rg-flow-2026-07-14.md
  - explorations/W215-true-vacuum-dynamical-systems-2026-07-14.md
  - explorations/W216-true-vacuum-spectral-condensate-2026-07-14.md
  - explorations/W217-true-vacuum-geometric-everpresent-2026-07-14.md
  - explorations/W219-native-good-stable-stabilizer-input-gate-2026-07-14.md
  - papers/drafts/structurally-forced-internally-undecidable/HARDENING-REPORT.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W224_native_good_stable_dynamical_vacuum.py
---

# W224 native good-stable DYNAMICAL vacuum

## Result in one paragraph

The dynamical half of the good-stable gate closes with a clean, honest negative. The five-method
vacuum arc (W213-W217) builds exactly one vacuum candidate: the record-saturated de Sitter rolling /
fading attractor, whose order parameter is the record-count / conformal-scale mode `p`
(`N = 4-volume = e^{4p}`). That order parameter is a spacetime-geometric scalar, hence a SINGLET of
the program-native internal arena `Sp(32,32;H)` -- the internal group acts on the quaternionic spinor
fiber, not on the base conformal factor. A singlet is fixed by every group element, so the DYNAMICAL
isotropy group of the only built vacuum is the FULL non-compact `Sp(32,32;H)` (dimension 8256), not
the compact Cartan reduction `Sp(32) x Sp(32)` that W219 found kinematically. By Proposition 1 of the
hardened paper (an invariant positive majorant exists exactly for relatively compact image), the
non-compact arena admits NO admissible commuting fundamental symmetry: `F_{Sp(32,32;H)}(eta)` is
EMPTY. Therefore the dynamically-built vacuum does NOT supply a good-stable grading, and the both-signs
/ moduli question is VACUOUS on it (`F` empty is stronger than "`F` nonempty of dimension 0"). This is
a precise INPUT FAILURE: a dynamical good stable would require an order parameter that breaks the full
4096-generator non-compact block to leave the compact 4160, and the built attractor breaks zero of
them. The only arc candidate whose order parameter transforms nontrivially -- the mirror-sector BCS
condensate (W216) -- is exactly the object conditional on the operative-`C` branch and the unbuilt
source action. bar(b) and H59 remain OPEN; the count is unchanged.

## 1. Construction fork (mandatory)

The load-bearing object is the vacuum ORDER PARAMETER, and it has a genuine fork.

- **Standard-physics reading.** Default to a Higgs-like order parameter living in a nontrivial
  representation of the gauge group, and assume the vacuum spontaneously breaks the group to its
  maximal compact form, "recovering" the good stable by fiat. Under this default one silently imports
  the very compactification whose dynamical origin is the open question.
- **Program-native reading.** GU's actually-built vacuum candidate (the object the five methods
  converge on) is the record-count / conformal-scale mode `p` (W153/W166/W215/W217): `N = 4-volume`
  is a diffeomorphism-invariant geometric scalar on the base `X^4` (equivalently a scale coordinate on
  the fiber `Y^14 = Met(X^4)`). The internal `Sp(32,32;H)` is the spin lift of `so(9,5)` acting on the
  quaternionic spinor module; it does not act on the base conformal factor. Natively, `p` is a
  SINGLET.

**Which side, and why.** The answer lives on the native side, and it is decisive: the built order
parameter is a singlet, so it does not compactify the group. Defaulting to the physics reading would
have manufactured the good stable that native dynamics does not provide. Per the fork discipline, the
kill is checked in the OTHER construction: in the physics reading, IF an internal adjoint condensate
`<O> ~ P` existed, its centralizer WOULD be the compact `Sp(32) x Sp(32)` and W219's uniqueness would
apply. So the kill is specific -- GU's built background is the wrong TYPE of object (a singlet), not a
proof that no compactifying object can exist. That distinction is the entire located gap (Section 4).

## 2. Synthesis of the vacuum arc (W213-W217), read and reconciled

Five independent methods built the record-condensed true vacuum. They do converge, on one object:

| wave | method | verdict | order parameter used |
|---|---|---|---|
| W213 | effective-potential / variational | RUNAWAY-NO-VACUUM (in-validity) | scale mode `u` on the record-count slice |
| W214 | RG-flow | RUNAWAY-NO-VACUUM (native basin) | native tree point, scalaron mass runs |
| W215 | dynamical-systems / rolling | RUNAWAY-NO-VACUUM (graceful de Sitter ROLLING attractor) | record-count mode `p`, `N = e^{4p}` |
| W216 | spectral / BCS condensate | EXISTS-SENSIBLE (operative-C) / EXISTS-PATHOLOGICAL | mirror-sector gap `Delta` in `ker(Gamma)` |
| W217 | geometric / everpresent-Lambda | EXISTS-SENSIBLE (operative sign) / EXISTS-PATHOLOGICAL | de Sitter attractor `Lambda ~ 1/sqrt(N)` |

The reconciliation is the one W217 already stated and I confirm: the RUNAWAY vs EXISTS-SENSIBLE split
is a SUCCESS-CRITERION difference (finite-field stable minimum vs sensible asymptotic state), not a
contradiction. Three hard agreements survive:

1. **No in-validity, finite-field, stable minimum** -- W213/W214/W215 unanimous. The native potential
   is exactly quadratic and inverted; the only finite fixed point is the empty false vacuum, a
   hyperbolic saddle.
2. **The built endpoint is a graceful de Sitter ROLLING / FADING attractor with the arrow holding** --
   W215 and W217 agree object-for-object. Its order parameter is the record-count / conformal-scale
   mode `p`.
3. **The genuinely non-perturbative object EXISTS and is SENSIBLE only conditional on one external
   sign** -- W216 (operative-`C`) and W217 (operative reservoir Krein sign) agree, including the
   conditional. Its order parameter is the mirror-sector condensate, which requires the unbuilt source
   action.

The decisive reading for the stabilizer question: the ONLY UNCONDITIONALLY-BUILT vacuum candidate is
the rolling scale attractor (agreement 2). The compactification-capable candidate (agreement 3) is
conditional and unbuilt. So the dynamical isotropy must be computed on the scale attractor.

Per NEXT-STEPS, no premise here rests on W211's Godel / one-bit language; the hardening report
supersedes it for this question. The mirror condensate is treated only as "conditional on the
operative-`C` branch and the unbuilt source action," which is what W216 itself states.

## 3. The dynamical isotropy computation (EXACT)

Scope: the good-stable stabilizer is the isotropy of the vacuum in the INTERNAL grading arena
`Sp(32,32;H)` (the group in which the Krein fundamental symmetry lives). Spacetime isometries of the
de Sitter background are a separate factor and are not the object W219 / the queue asks for.

Let the built vacuum be the rolling attractor with order parameter `p` in the singlet
representation of `G = Sp(32,32;H)`. The isotropy group of a singlet configuration is

```
Stab_G(p . 1) = { g in G : g fixes the singlet } = G = Sp(32,32;H).
```

Every internal gauge transformation acts trivially on the base conformal factor `p`, so nothing is
broken. Quantitatively, using the exact real dimensions (reproduced from W219):

```
dim_R Sp(32,32;H)       = 64(2*64+1) = 8256
dim_R [Sp(32) x Sp(32)] = 2 * 32(2*32+1) = 4160
dim_R (non-compact block p) = 4 * 32 * 32 = 4096,     4160 + 4096 = 8256

generators broken by the built vacuum = 8256 - 8256 = 0.
```

The dynamical isotropy is the full non-compact `Sp(32,32;H)`. It is NOT the compact Cartan reduction
W219 derived kinematically, because the singlet background cannot select the Cartan parity
`P = beta = diag(I_32, -I_32)`: a configuration fixed by all of `G` commutes with every element and so
distinguishes none.

## 4. Proposition 1 on the dynamical isotropy: no admissible fundamental symmetry

Proposition 1 (HARDENING-REPORT, "existence of an invariant positive majorant exactly for relatively
compact image"): `F_H(eta)` is nonempty exactly when the image of `H` has compact closure. Here
`H = Sp(32,32;H)` is non-compact with non-compact image, so

```
F_{Sp(32,32;H)}(eta) = empty.
```

There is NO invariant positive majorant, hence NO admissible commuting fundamental symmetry, on the
dynamically-built vacuum. Consequences, graded honestly:

- The dynamical good-stable grading is NOT supplied by the built vacuum. This is an INPUT FAILURE, and
  it is precise.
- The both-signs / moduli question is VACUOUS on this background. `F` EMPTY is strictly stronger than
  "`F` nonempty of dimension 0" (W219's kinematic uniqueness): there is no admissible `C` to decompose,
  so neither "unique grading" nor "continuous residual of dimension `sum_lambda dim_R(D_lambda)
  a_lambda b_lambda`" applies. Reporting a `Z/2`, or any residual dimension, on this background would
  be a category error -- exactly the error the hardening report killed at the kinematic level, here
  ruled out at the dynamical level for a different reason (empty `F`, not shared-vs-unshared types).
- The contrast is sharp and is the whole content: on the counterfactual COMPACT reduction (given `P`),
  `F` is nonempty and W219's read applies -- positive standard module in the first `Sp(32)` factor,
  negative in the second, no shared type, residual dimension 0, unique grading. The dynamical build
  simply never reaches that reduction.

## 5. The located gap: what a nonperturbative completion must supply

The input failure is not "GU has no good stable"; it is "the only vacuum GU currently builds is the
wrong type of object to define one." A dynamical good stable requires:

- an order parameter transforming in a NONTRIVIAL representation of `Sp(32,32;H)` (adjoint or
  fundamental), whose VEV Higgses the arena to a subgroup of compact image;
- the cleanest realization is an adjoint condensate `<O> ~ P` (the Cartan generator), breaking exactly
  the 4096 non-compact boost generators and leaving the compact 4160 = `Sp(32) x Sp(32)`; then W219's
  uniqueness (`F_K` dimension 0) becomes the dynamical answer.

The built de Sitter attractor breaks 0 of those 4096; it falls short by the entire non-compact block.
The only arc candidate whose order parameter transforms nontrivially -- and therefore could break the
block -- is the mirror-sector BCS gap `Delta` (W216), living in the 96 hyperbolic null pairs of
`ker(Gamma)` in `Cl(9,5) = M(64,H)`. On the good branch its off-diagonal pairing (`H = xi tau3 +
Delta tau1`) is exactly an adjoint-valued VEV that pairs Krein partners. But W216 supplies it only
conditional on the operative-`C` branch, with a fit-gated magnitude, sourced by the unbuilt promotion
-gate source action (W154/W203). So the nonperturbative completion GU would need is precisely:

1. the interacting mirror-sector condensate built from the native source action (not a mean-field BdG
   proxy), with its own dynamics rather than an assumed operative `C`; and
2. a demonstration that its VEV lands in the direction (adjoint `~ P`, or a fundamental orbit with the
   same centralizer) that reduces `Sp(32,32;H)` to a compact-image subgroup.

Only after (1)-(2) is the both-signs / moduli test even applicable to a DYNAMICAL good stable. Until
then the dynamical good stable is undefined for the correct, computed reason: the built vacuum is an
internal singlet.

## 6. Verdict

```
DYNAMICAL-GOOD-STABLE-STABILIZER (built vacuum candidate = record-count de Sitter attractor):
  order parameter p                : internal SINGLET of Sp(32,32;H)
  dynamical isotropy group         : the FULL non-compact Sp(32,32;H) (dim 8256)
  admissible fundamental symmetry  : NONE (Proposition 1: F_H empty for non-compact image)
  both-signs / moduli question     : VACUOUS (no admissible C to decompose)
  => INPUT FAILURE, precisely located; not a free Z/2, not a moduli space.

GAP (what a nonperturbative completion must supply):
  an order parameter breaking the full 4096-generator non-compact block to leave the compact 4160;
  the only arc candidate is the mirror-sector condensate (W216), conditional + unbuilt.
```

This does not claim GU has no good stable. It is the narrower, computed result that the only vacuum
the repository currently builds cannot define one, and it names exactly the missing object.
bar(b), H59, and the generation count remain OPEN / unchanged; no canon or verdict moves.

## 7. Joe-gated items borne on but NOT moved

- **H59** (native interacting Krein-unitarity / good-stable program): this result is directly
  ABOUT the H59 object. It is left OPEN and unmoved; the finding SHARPENS what H59 must construct (a
  compactifying interacting condensate), it does not resolve it. FLAGGED, not moved.
- **bar(b)**: unchanged. No debit added or cleared; a singlet-isotropy input failure is a located
  gap, not a new falsification.
- **Generation count / RESEARCH-STATUS / verdicts**: untouched.

## 8. Machine receipt

```
python -u tests/W224_native_good_stable_dynamical_vacuum.py
```

35/35 checks passed, exit 0. Positive controls run FIRST and each fires on a real falsifier: the
counterfactual adjoint `~ P` condensate compactifies (breaks 4096, residual 4160); a singlet breaks
0; Proposition 1 is enforced both directions so a wrongly-claimed majorant on a non-compact group is
caught; a genuinely shared isotypic type leaves a continuous positive-dimensional residual (the
machinery detects real moduli, so its "empty / vacuous" verdict here is not a blind spot). The actual
checks then compute the singlet isotropy, the empty `F`, the vacuous both-signs test, the located
4096-generator gap, and the vacuum-arc reconciliation guards.

## Governance

Exploration grade only. No canon, RESEARCH-STATUS, verdict, bar(b), H59, or generation-count change.
No cross-repository identity asserted; the mirror-condensate branch selector stays a gated
temporal-issuance / time-as-finality object and is not claimed here. bar(b) and H59 remain OPEN.
