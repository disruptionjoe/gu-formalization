---
artifact_type: exploration
label: HQW-NOTE-H10
status: "note (consolidation of an already-DONE, machine-checked result into citable lemma form; no canon, claim-status, H-number, bar, verdict, or posture movement)"
created: 2026-07-14
title: "HQW-NOTE (H10) -- The shape-blind c_R lemma: the covariant scalaron coupling of alpha|II|^2 + beta|H|^2 is c_R = -(4/9)(alpha+beta)"
grade: "EXACT / MACHINE-VERIFIED. The pure-invariant couplings c_R(|II|^2)=c_R(|H|^2)=-4/9 and the family collapse c_R(alpha,beta)=-(4/9)(alpha+beta) are reproduced by the verbatim W126 Route-1 machinery in tests/W165_universal_property_and_sign.py (exit 0, all checks PASS) and independently re-checked in tests/HQW_NOTE_shape_blind_cR.py (exit 0). GU-INDEPENDENT: this is a fact about the induced conformal-graph functional on a codimension-one submanifold shape family, stated without any GU-specific input."
gu_independent: true
depends_on:
  - explorations/W126-beyond4th-vacuum-lift-2026-07-13.md
  - explorations/W130-native-graviton-oneloop-block-2026-07-14.md
  - explorations/W159-tachyon-escapes-2026-07-14.md
  - explorations/W165-lens-abstraction-level-2026-07-14.md
  - explorations/W167-reduction-direct-sign-alpha-beta-2026-07-14.md
  - explorations/W187-gu-dressed-open-selfenergy-2026-07-14.md
scripts:
  - tests/W165_universal_property_and_sign.py
  - tests/HQW_NOTE_shape_blind_cR.py
---

# HQW-NOTE (H10) -- The shape-blind c_R lemma

## 0. Result first

On the two-parameter shape family of induced conformal-graph functionals

```text
    F = alpha |II|^2 + beta |H|^2
```

(with |II|^2 the full second-fundamental-form norm-square and |H|^2 the mean-curvature-vector norm-square), the covariant scalaron coupling -- the R^2-channel coefficient that sets the spin-0 scalaron mass -- is

```text
    c_R(alpha, beta) = -(4/9) (alpha + beta).
```

It depends only on the total weight alpha+beta, never on the shape ratio alpha:beta. Consequently

```text
    sign(c_R) = -sign(alpha + beta),
```

so the scalaron is tachyonic (c_R < 0) for every positive-total-weight member and healthy (c_R > 0) only for alpha+beta < 0. The "tachyonic-iff-attractive" sign correlation is therefore basis-, normalization-, and signature-invariant: it is a one-bit function of the total weight, and no choice of shape inside a positive-definite norm-square can flip it.

This note consolidates an already-DONE, machine-checked result (W165, and its inputs W126/W130/W159) into a standalone, citable higher-derivative-gravity lemma. It changes no canon, no claim status, no bar, no verdict.

## 1. Statement of the lemma

**Lemma (shape-blind scalaron coupling).** Let g = e^{2 phi} eta be the conformal-graph jet and let |II|^2 and |H|^2 be the induced norm-squares of the second fundamental form and its trace on the potential slice (dphi = 0), each expanded to the curvature basis

```text
    F = a0 + a1 R + a2s R^2 + a3s Ric^2,
```

and let the covariant R^2-channel coupling be the Gauss-Bonnet-reduced combination

```text
    c_R := a2s + a3s / 3
```

(GB topological in 4D, C^2 the spin-2 channel, so c_R is the coefficient that governs the physical scalaron via f_0^2 = 1/(6 c_R)). Then

1. the two pure invariants share the SAME covariant coupling,
   `c_R(|II|^2) = c_R(|H|^2) = -4/9`;
2. hence on the family F = alpha|II|^2 + beta|H|^2,
   `c_R(alpha, beta) = alpha c_R(|II|^2) + beta c_R(|H|^2) = -(4/9)(alpha + beta)`;
3. therefore c_R is shape-blind: `d c_R / d alpha = d c_R / d beta`, and
   `sign(c_R) = -sign(alpha + beta)`.

The healthy region c_R > 0 is exactly alpha + beta < 0; the sign boundary is the line alpha + beta = 0.

## 2. Proof sketch

The proof is a linearity-of-a-shared-value collapse, on top of two exact computations.

**(a) The two pure couplings are equal.** The verbatim W126 Route-1 construction (Convention-B vertical representative B^V plus normal lift) gives the exact slice decompositions

```text
    |II|^2 : (a0, a1, a2s, a3s) = ( 2, 1/3, 8/9, -4)   ->  c_R(|II|^2) = 8/9 - 4/3 = -4/9   (W126, W130)
    |H|^2  : (a0, a1, a2s, a3s) = (-1, 4/3, -4/9,  0)   ->  c_R(|H|^2)  = -4/9 + 0   = -4/9   (W159)
```

The equality c_R(|II|^2) = c_R(|H|^2) = -4/9 is the single non-obvious input; it is a genuine degeneracy of GU's induced action (see the negative control in Section 4), not automatic for an arbitrary degree-2 functional.

**(b) Linearity.** Every coefficient in the curvature-basis decomposition is linear in (alpha, beta), so c_R is too:
c_R(alpha, beta) = alpha c_R(|II|^2) + beta c_R(|H|^2).

**(c) Collapse.** Substituting the shared value -4/9 gives c_R(alpha, beta) = -(4/9)(alpha + beta). A linear combination of two equal numbers depends only on the sum of the coefficients, hence the shape-blindness and the sign law. QED.

**Where the shape freedom actually lives.** The Einstein-channel coefficient a1 is NOT shape-blind:

```text
    a1(alpha, beta) = (alpha + 4 beta) / 3,
```

and the W159 independence determinant

```text
    det [[ a1(|II|^2), a1(|H|^2) ], [ c_R(|II|^2), c_R(|H|^2) ]] = det [[1/3, 4/3], [-4/9, -4/9]] = 4/9  !=  0
```

is carried entirely by a1. So (a1, c_R) are independent coordinates on the shape family: the shape freedom is real but it moves a1, and c_R is orthogonal to it. "Coherent shape freedom" and "the sign of the scalaron mass" are different axes.

## 3. Machine-check citation

Primary check: `tests/W165_universal_property_and_sign.py` (exit 0; all checks PASS). The load-bearing lines are:

- PC1-PC3: reproduce the |II|^2 tuple (2, 1/3, 8/9, -4) with c_R = -4/9, and the |H|^2 tuple (-1, 4/3, -4/9, 0) with c_R = -4/9, from the verbatim machinery.
- U2: `c_R(alpha,beta) = -(4/9)(alpha+beta)` is verified symbolically (the shape-blindness lever).
- U3: c_R is shape-blind while a1 = (alpha + 4 beta)/3 is not; the det = 4/9 independence lives in a1.
- U4-U5: the conformally-natural trace-free Willmore combination |II|^2 - c|H|^2 (c in (0,1)) has c_R = -(4/9)(1 - c) < 0, and every positive-total-weight norm-square forces c_R < 0.
- NC1: a hypothetical action with c_R(|II|^2) != c_R(|H|^2) does NOT collapse -- the degeneracy is load-bearing.

Confirming check (added with this note): `tests/HQW_NOTE_shape_blind_cR.py` (exit 0). It independently re-derives c_R(|II|^2) and c_R(|H|^2) from the same machinery, verifies c_R(alpha,beta) = -(4/9)(alpha+beta), and point-checks

```text
    (1, 0) GU pure-|II|^2 : c_R = -4/9  (tachyonic)
    (0, 1) pure-|H|^2     : c_R = -4/9  (tachyonic)
    (1, 1) positive cone  : c_R = -8/9  (tachyonic)
    (3, 1) positive cone  : c_R = -16/9 (tachyonic)
   (-2, 1) HEALTHY        : c_R = +4/9  (needs alpha + beta < 0)
    (1,-1) boundary       : c_R = 0     (the alpha + beta = 0 line)
```

with sign(c_R) = -sign(alpha+beta) at every point, plus the same negative control.

## 4. Why it is nontrivial (negative control)

The collapse is a special, load-bearing degeneracy of GU's induced action, not a triviality of any degree-2 functional. For a hypothetical functional with c_R(|II|^2) != c_R(|H|^2), the family coupling stays genuinely two-parameter:

```text
    c_R_generic(alpha, beta) = alpha c_R_II + beta c_R_H   does NOT reduce to a function of (alpha + beta).
```

Only the actual equality c_R(|II|^2) = c_R(|H|^2) = -4/9 forces the reduction. The shape-blindness is thus a real structural fact about the induced action, checked (NC1 in both scripts) rather than assumed.

## 5. GU-independence

Nothing in the lemma uses a GU-specific ingredient. |II|^2 and |H|^2 are the standard invariants of a codimension-one submanifold's second fundamental form; the conformal-graph jet g = e^{2 phi} eta and the curvature-basis reduction are standard higher-derivative-gravity constructions; the Gauss-Bonnet reduction c_R = a2s + a3s/3 is the ordinary 4D identity. The lemma is a reusable statement about induced R^2-channel couplings on shape families, independent of the GU program that motivated computing it.

## 6. Consequences and reuse

The lemma is used, directly or as the sign engine, by:

- **W157** (the a2 = -(a1)^2 coincidence keystone): the covariant c_R = -4/9 is exactly the coefficient that breaks the apparent MSS-slice identity a2 = -(a1)^2 by a factor of 4 (see HQW-NOTE (H11)).
- **W159** (tachyon escapes): the det = 4/9 independence -- the "sign-free" result that the tachyon is GU's specific-point property, not forced by attraction -- is the a1-axis complement of this lemma's c_R-axis.
- **W165** (abstraction-level lens): the shape-blindness is the lever showing that no norm-square universal property with positive total weight can force health; the conformally-natural Willmore/GJMS, Kempf-Ness, and spectral-action forced points all land at c_R < 0.
- **W167** (reduction, direct sign in alpha, beta): the sign map sign(c_R) = -sign(alpha+beta) is the direct-in-(alpha,beta) statement of the scalaron sign.
- **W187** (dressed open self-energy): consumes c_R < 0 as the tachyonic tree-level input to the open-system dressing.

The one honest caveat: health (c_R > 0) requires alpha + beta < 0, which a positive-definite norm-square cannot deliver; reaching it needs the two isotypic components (trace H and trace-free II_0) to carry opposite Krein signatures, an object on the (9,5) q=5 frontier that W165 leaves as a gated conjecture. This note asserts only the exact, GU-independent coupling formula and its sign law, not that healthy or tachyonic is "the right" reading.
