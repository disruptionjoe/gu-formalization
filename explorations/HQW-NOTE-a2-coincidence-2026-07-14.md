---
artifact_type: exploration
label: HQW-NOTE-H11
status: "note (honesty/methodology consolidation of an already-DONE, machine-checked result; no canon, claim-status, H-number, bar, verdict, or posture movement)"
created: 2026-07-14
title: "HQW-NOTE (H11) -- The a2 = -(a1)^2 coincidence: a magnitude that looked structural was a basis artifact, caught in the covariant basis"
grade: "EXACT / MACHINE-VERIFIED that the identity is a COINCIDENCE. tests/W157_a2_equals_minus_a1_squared_keystone.py (exit 0, all checks PASS) shows a2=-(a1)^2 holds ONLY for the MSS-slice coefficient a2_MSS=-1/9 and breaks by a factor of 4 at the covariant scalaron coefficient c_R=-4/9; it is normalization dependent and holds on only a codimension-one locus of the shape family. GU-INDEPENDENT: the statement and its diagnosis are facts about induced higher-derivative couplings and basis choice."
gu_independent: true
depends_on:
  - explorations/W126-beyond4th-vacuum-lift-2026-07-13.md
  - explorations/W130-native-graviton-oneloop-block-2026-07-14.md
  - explorations/W157-a2-equals-minus-a1-squared-keystone-2026-07-14.md
  - explorations/W159-tachyon-escapes-2026-07-14.md
scripts:
  - tests/W157_a2_equals_minus_a1_squared_keystone.py
---

# HQW-NOTE (H11) -- The a2 = -(a1)^2 coincidence

## 0. Result first

The induced conformal-graph functional |II|^2 decomposes, on the potential slice reduced along the maximally-symmetric-space (MSS) direction, to an F(R) with

```text
    F(R) = 2 + R/3 - R^2/9,     i.e.  a1 = 1/3,   a2_MSS = -1/9,
```

which satisfies the eye-catching exact identity

```text
    a2_MSS = -(a1)^2        (   -1/9 = -(1/3)^2   ).
```

It looks structural: exact, scale-mode invariant, non-automatic. If real, it would say the R^2-channel tachyon is the literal "square shadow" of the Einstein coefficient a1 -- the tachyon would be a now-understood consequence of attractive gravity, and a debit would convert to a feature.

**It is not structural. It is a coincidence of the MSS slice basis and the a0 = 2 normalization.** The decisive fact: the coefficient that actually sets the scalaron mass is not the MSS-slice number a2_MSS = -1/9 but the covariant coupling

```text
    c_R = a2s + a3s/3 = -4/9      (W130),
```

and -4/9 != -(1/3)^2 = -1/9. The apparent identity breaks by a factor of 4 the moment one computes in the covariant basis. What survives is only the sign, sign(a2 / a1) < 0 ("tachyonic iff attractive"), which is basis- and normalization-invariant.

This note consolidates an already-DONE, machine-checked result (W157) into a standalone honesty/methodology write-up. It changes no canon, no claim status, no bar, no verdict.

## 1. The statement, precisely

Two different R^2 coefficients can be extracted from the same slice data (a0, a1, a2s, a3s) = (2, 1/3, 8/9, -4):

- the **MSS-slice** coefficient, obtained by the MSS reduction Ric^2 -> R^2/4:
  `a2_MSS = a2s + a3s/4 = 8/9 - 1 = -1/9`;
- the **covariant** coefficient, obtained by the Gauss-Bonnet-reduced physical map Ric^2 -> R^2/3 (GB topological in 4D, C^2 the spin-2 channel):
  `c_R = a2s + a3s/3 = 8/9 - 4/3 = -4/9`.

The identity a2 = -(a1)^2 holds for a2_MSS and fails for c_R:

```text
    a2_MSS = -1/9 = -(a1)^2        holds
    c_R     = -4/9                 c_R / a1 = -4/3,  so c_R = -(4/3) a1 != -(a1)^2
```

The physical scalaron mass is governed by c_R (f_0^2 = 1/(6 c_R), m_0^2 < 0 because c_R < 0), not by a2_MSS. So the coefficient that carries the physics is exactly the one that breaks the identity.

## 2. Why it is a basis artifact -- the decisive covariant-vs-slice distinction

On the potential slice (dphi = 0) the curvature basis {R^2, Ric^2, C^2, GB} is only 2-dimensional, so the split into a2s R^2 + a3s Ric^2 is NOT a unique covariant {R^2, C^2} split -- it is a slice representation. Reducing that slice representation to a single R^2 coefficient requires a choice of how to trade Ric^2 for R^2, and the two natural choices disagree:

```text
    MSS slice    :  Ric^2 -> R^2 / 4     (the maximally-symmetric-space relation)
    covariant    :  Ric^2 -> R^2 / 3     (GB freedom cancelled; the physical spin-0 channel)
```

The identity a2 = -(a1)^2 lives ONLY on the /4 reduction. It is an artifact of reading the R^2 coefficient in the MSS slice basis; the same theory in the correct covariant basis is the "breaking family member." This is the decisive point: a magnitude that appears structural in a convenient slice basis is diagnosed as a coincidence the moment it is recomputed in the physically load-bearing covariant basis.

Three further independent computed reasons (all in W157) confirm the coincidence grading:

- **Normalization dependence.** Under an overall rescale W -> N W the identity becomes a2 = -N a1^2, holding only at N = 1 (the a0 = 2 flat-section pin). For any tachyonic theory (a2 < 0, a1 != 0) the choice N* = -a2 / a1^2 > 0 makes a2 = -a1^2 hold -- so the exact magnitude is a normalization convention available to every tachyon, not a constraint. On the covariant c_R = -4/9 the required N* = 4.
- **Inhomogeneity.** Geometrically the identity reads <II_1, II_1> = -4 <II_0, II_1>^2: degree 2 on the left, degree 4 on the right. It is inhomogeneous under II -> lambda II, so no conformal-weight or homogeneity argument can force it. The conformal weight fixes only the degree-2 ceiling (the functional is quadratic in the scale mode); it cannot force the cross-weight ratio w2 / w1^2.
- **Codimension-one in the shape family.** On F = alpha|II|^2 + beta|H|^2 the identity locus a2 + a1^2 = 0 is a curve; it holds at the pure-|II|^2 point (beta = 0) but fails at the other GU-named point beta/alpha = 2. A family-wide identity would vanish for all (alpha, beta); this one does not.

## 3. What survives

Only the SIGN survives as basis- and normalization-invariant:

```text
    sign(a2 / a1) < 0        (tachyonic iff attractive),
```

which holds in both bases (a2_MSS / a1 = -1/3, c_R / a1 = -4/3, both < 0) and under any positive rescale. The tachyon is correlated in sign with attractive gravity, but it is NOT the literal square-shadow of the Einstein coefficient. Whether that sign correlation is itself forced (is c_R < 0 forced by a1 > 0?) is a separate question, not settled by this note; it is the subject of W159/W165 and HQW-NOTE (H10).

## 4. Machine-check citation

`tests/W157_a2_equals_minus_a1_squared_keystone.py` (exit 0; all checks PASS). The load-bearing lines:

- PC1-PC5: reproduce (2, 1/3, 8/9, -4), a2_MSS = -1/9, c_R = -4/9, the MSS interpolant P(u) = -64u^2 - 8u + 2, and that the identity holds in the slice/MSS basis.
- T1 (decisive): a2_MSS = -(a1)^2 holds but c_R = -4/9 != -(a1)^2, breaking by a factor of 4; the identity lives on the Ric^2 -> R^2/4 reduction, not the physical Ric^2 -> R^2/3 one.
- T2: normalization dependence; N* = -a2/a1^2 makes any tachyon satisfy it; only the sign is scale-invariant.
- T3: the identity locus is a codimension-one curve in the shape family; fails at beta/alpha = 2.
- T4: the coefficients are signature-blind (identical for (1,3), (0,4), (2,2), (4,0)), which also refutes any story that the tachyon comes from the (9,5) indefiniteness.
- T5: the identity is inhomogeneous (degree 2 vs degree 4), so no conformal-weight argument can force it.

## 5. The methodological lesson (basis discipline / construction fork)

This is a clean instance of the construction-fork / basis-discipline pattern. A dimensionless magnitude coincidence, -1/9 = -(1/3)^2, was exact, reproducible, and non-automatic -- everything that usually flags a structural relation -- and it was graded a STRUCTURAL-CANDIDATE. The correct move was to ask which basis the coefficient lives in and to recompute the load-bearing quantity in the basis that carries the physics. In the MSS slice basis the identity is exact; in the covariant basis it breaks by a factor of 4. The physics is in the covariant basis, so the identity is a coincidence.

The transferable rules:

1. **A magnitude coincidence is not a structural claim until it survives the physically load-bearing basis.** Exactness, reproducibility, and non-automaticity are necessary but not sufficient; a slice/gauge basis can manufacture all three.
2. **When a coefficient is read off a lower-dimensional slice, name the reduction.** Here the slice basis was 2-dimensional in {R^2, Ric^2}; the ambiguity Ric^2 -> R^2/4 vs Ric^2 -> R^2/3 is exactly where the coincidence hid.
3. **Separate the invariant residue from the artifact.** The sign (tachyonic iff attractive) is invariant and honest; the exact magnitude was an artifact of the MSS slice and the a0 = 2 normalization. Keep the residue, retire the overclaim.

Because the grading was caught by computing in the covariant basis rather than by any external input, this note is a candidate observation for the methodology paper / ai-epistemology record; it is written here as the GU-side source note. GU-independence: the statement, the two-basis diagnosis, and the lesson are facts about induced higher-derivative couplings and basis choice, not about any GU-specific ingredient.

## 6. Consequence for the surrounding argument

The keystone conversion fails: debit-1 (the tachyon) does not become a now-understood consequence via the exact-magnitude a2 = -(a1)^2 argument; it stays an independent debit. The honest residue is the sign correlation alone. No bar clears by this route; the load returns to the genuine escapes tracked elsewhere (W128 AF-vs-AS branch fork, W126 gradient-sector saturation, and the shape-blind sign analysis of HQW-NOTE (H10) / W159 / W165).
