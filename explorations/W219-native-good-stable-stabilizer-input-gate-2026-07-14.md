---
artifact_type: exploration
label: W219
created: 2026-07-14
status: exploration
posture: adversarial; truth-seeking; native-object first; no verdict movement
title: "W219 native good-stable stabilizer input gate: kinematic Cartan centralizer derived, dynamical good stable not yet defined"
grade: "EXACT for the finite-dimensional Lie-group dimension and corrected compact-stabilizer calculations; SOURCE-AUDIT for the dependency classification; OPEN for the interacting vacuum, physical state space, observable algebra, and dynamical isotropy group. Machine regression: tests/W219_native_good_stable_stabilizer_gate.py. No canon, RESEARCH-STATUS, bar (b), or H59 change."
depends_on:
  - explorations/wave8/H23-source-action-construction-2026-07-11.md
  - explorations/W132-graded-optical-theorem-physical-subspace-2026-07-14.md
  - explorations/W173-brst-cohomology-mirror-sector-2026-07-14.md
  - explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md
  - explorations/W206-decisive-bit-counterfactual-invariance-2026-07-14.md
  - explorations/W213-true-vacuum-effective-potential-2026-07-14.md
  - explorations/W214-true-vacuum-rg-flow-2026-07-14.md
  - explorations/W215-true-vacuum-dynamical-systems-2026-07-14.md
  - explorations/W216-true-vacuum-spectral-condensate-2026-07-14.md
  - explorations/W218-lean-Rsrc-unification-check-2026-07-14.md
  - papers/drafts/structurally-forced-internally-undecidable/HARDENING-REPORT.md
scripts:
  - tests/W219_native_good_stable_stabilizer_gate.py
---

# W219 native good-stable stabilizer input gate

## Result in one paragraph

The first decisive task splits into one exact result and one hard missing object. At the full program-native spinor level, the Cartan centralizer of the constructed Krein parity in `Sp(32,32;H)` is the maximal compact subgroup `Sp(32) x Sp(32)`. This is not the 14-frame surrogate `SO(9) x SO(5)`. On the fundamental quaternionic split, the positive and negative modules belong to different compact factors, so the corrected compact-stabilizer theorem gives a unique admissible fundamental symmetry, not a free `Z/2`. But this is only a kinematic Cartan statement. The repository does not yet supply a native interacting vacuum or rolling order parameter, physical state space, and observable algebra whose dynamical isotropy group can be computed. The actual good-stable stabilizer therefore remains undefined.

## 1. Construction fork

This gate keeps two constructions separate.

- **Program-native construction.** The spin lift of `so(9,5)` preserves the indefinite quaternionic form `beta_S` and lands in the noncompact arena `Sp(32,32;H)`. Ghost clearance is keep-and-grade and ultimately requires a genuine interacting grading with `[P,S]=0`.
- **Standard-field proxy.** A finite-dimensional positive majorant, a selected matrix sign, or a mean-field BdG Hamiltonian can test algebraic consequences after a grading is supplied. It cannot derive the native vacuum, state quotient, or observable algebra.

The result below uses the native group and Cartan form for the kinematic calculation. It does not promote a positive-majorant proxy into GU dynamics.

## 2. Exact kinematic stabilizer

Let

```
G = Sp(32,32;H)
```

act on its fundamental quaternionic module with Hermitian form

```
beta = diag(I_32,-I_32).
```

H23 constructs the spinor form and verifies its real signature as `(+64,-64)` after complex realization. The Cartan involution is implemented by `P = beta`. The elements preserving both the indefinite form and the positive majorant `beta P = I` commute with `P`, hence are block diagonal. Therefore

```
K_cartan = Z_G(P) = Sp(32) x Sp(32).
```

The dimension check is exact:

```
dim_R Sp(32,32;H) = 64(2*64+1) = 8256,
dim_R [Sp(32) x Sp(32)] = 2*32(2*32+1) = 4160,
dim_R p = 4*32*32 = 4096,
4160 + 4096 = 8256.
```

Inside the 91-dimensional spin-lift image, the analogous Cartan centralizer is `Spin(9) x Spin(5)`, with Lie algebra dimension `36+10=46`. These are related levels of the construction, not identical groups:

| level | full arena | kinematic Cartan centralizer | real dimension of centralizer |
|---|---|---|---:|
| 14-frame / spin-lift image | `SO(9,5)` or `Spin(9,5)` | `SO(9)xSO(5)` or its spin cover | 46 |
| full quaternionic source arena | `Sp(32,32;H)` | `Sp(32)xSp(32)` | 4160 |

Earlier notes moved between these levels without deriving which one acts faithfully on the physical state space.

## 3. Corrected grading read

Under `Sp(32)xSp(32)`, the positive standard quaternionic module is charged under the first factor and the negative standard module under the second. They are inequivalent factor-labelled irreducibles. No irreducible type occurs with both signs. The corrected compact-stabilizer theorem therefore gives

```
dim_R F_K(beta) = 0,
```

so the admissible commuting fundamental symmetry is unique at this kinematic level. There is still a two-dimensional space of invariant block metrics, but it is not a grading-sign space. This reproduces, at the native quaternionic level, the central correction made in the hardened paper.

## 4. Why this is not yet the physical good-stable stabilizer

A dynamical stabilizer is the isotropy group of an actual solution or state together with all physical structures that must be preserved. The audited inputs do not provide that tuple.

| input | what it really supplies | why it does not finish the gate |
|---|---|---|
| H23 | exact spin lift, indefinite `beta_S`, kinematic Cartan parity, free-symbol Krein self-adjointness | the soldering `A=spin-lift(grad^gimmel)` is not forced; the calculation is not an interacting vacuum or S-matrix |
| W132 | exact finite-dimensional pseudo-unitary expansion identity and a constructed C-metric coexistence example | the QFT conclusion is conditional on an interacting `C` |
| W173 | a free-complex closed-not-exact calculation | the stabilized complex, secondary constraint, and curvature input are unbuilt |
| W203 | a one-dimensional ultralocal equivariant kernel, conditional on W154 | the nonlocal source action and interacting state are not built |
| W206 | a 14-frame maximal-compact calculation | it explicitly takes the good stable as given and its old free-sign conclusion is false |
| W213 | exact inverted quadratic in its truncation | no stationary vacuum inside validity |
| W214 | native-basin RG result | no sensible stationary endpoint on the native basin |
| W215 | a rolling toy dynamical system | no stable fixed point; the attractor sits at the validity edge |
| W216 | a mean-field BdG condensate proxy | it assumes an operative `C`, an unbuilt source lift, and W211's killed one-bit premise |
| W218 | an explicit ultralocal carrier/operator comparison | it selects `C=sign(K_c)` and uses a pushforward stand-in; it does not derive a vacuum or physical metric |

The three native-potential or flow routes W213-W215 agree on the negative input: there is no stationary good stable inside their built validity regime. W216 does not override that result because its favorable branch begins by supplying the operative grading whose derivation is at issue.

## 5. First gate verdict

```
KINEMATIC-CARTAN-STABILIZER: DERIVED
  full native arena: Sp(32) x Sp(32)
  spin-lift image:   Spin(9) x Spin(5)
  admissible grading at either canonical compact level: unique

DYNAMICAL-GOOD-STABLE-STABILIZER: NOT YET DEFINED
```

This is not a claim that GU has no good stable. It is the narrower result that the present repository inputs do not define one at native interacting grade. bar (b) and H59 remain OPEN.

## 6. Next bounded sub-goal

Before computing any further stabilizer, determine the representation type of the only currently built candidate background, the rolling record-count/conformal mode `p(tau)` from W153/W166/W215:

1. Is `p` a singlet under the full `Sp(32,32;H)` arena, a field in the 91-dimensional spin-lift image, or a section-space/geometric variable on which that group does not act directly?
2. If it is a singlet, its roll cannot compactify the noncompact group, so its isotropy remains the full noncompact arena and Proposition 1 forbids an invariant positive majorant.
3. If it is nontrivial, write its exact representation and compute the isotropy of a nonzero rolling background.
4. If no representation map exists, the next construction is that map, not another assumed stabilizer.

This `p`-representation/isotropy calculation is the next hourly pickup. It is the shortest route that can either produce a genuine dynamical reduction or kill the rolling background as a source of the desired good stable.

## 7. Machine receipt

Run:

```
python -u tests/W219_native_good_stable_stabilizer_gate.py
```

Result: `29/29` checks passed, exit 0. The test checks the native and 14-frame Cartan dimensions, the corrected uniqueness read, the source sufficiency boundaries, and the new hourly front door. It is a regression gate, not a construction of the missing vacuum.

## Governance

Exploration grade only. No canon or scientific-status change. No cross-repository identity. bar (b) and H59 remain OPEN.
