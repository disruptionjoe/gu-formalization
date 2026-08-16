---
title: "Hostile review — K126 radial-momentum principal-scope correction"
status: reviewed_correction
created: "2026-08-15"
target: explorations/conditional-build/selected-k126-native-i1b-radial-momentum-principal-scope-correction-2026-08-15.md
---

# Hostile review — K126

## Strongest objection

The K124 computation may be mathematically correct while the phrase
“complete local principal TT bulk” is false. Its radial direction has zero
momentum and its two metric directions are back-to-back. In that kinematics
the total metric momentum kills `d(D2B_LC)` automatically. A general
three-point symbol does not have that simplification. But evaluating only the
new exterior cell in a co-moving connection while freezing the rest of the
natural packet is equally invalid.

## Adversarial checks

1. The second spin-Levi-Civita jet is reconstructed from the exact symmetric
   frame rather than replaced by the coordinate Christoffel jet.
2. The first jets reproduce K124's closed LC formula.
3. Restoring `d(D2B_LC)` on all back-to-back causal representatives leaves
   K124's `-24,+24,0` values unchanged.
4. A common-transverse TT configuration with nonzero null radial momentum
   gives partial `d(D2B_LC)=-24` while `B^2=0`.
5. An independent coordinate-curvature expansion gives complete value zero;
   the omitted natural transport is therefore `+24` and the planted partial
   inference fails.
6. The full common-transverse family yields
   `C_t_h_h=-6(p^2+q^2+3r^2)<DW>` and reproduces K124 at `r=0,q=-p`.
7. The noncyclic Shiab is evaluated directly. Its partial Cartan covector is
   retained as an adverse control, not the full representative.
8. The mixed `t-h-v` block remains zero on 120 entries and cannot receive a
   second-LC term with only one metric leg.
9. A coordinate background-connection witness is retained only as evidence
   that lower-order data depend on background jets, not promoted to a
   covariant coefficient.

## Verdict

Accept K124 as the back-to-back specialization and retain K125's covariance
theorem. Reject both the frozen-`dB` shortcut and the isolated-`d(D2B_LC)`
shortcut. Accept K126's common-transverse three-momentum polynomial and exact
`-24+24=0` adverse control. Do not promote the partial Cartan covector or claim a
curved lower-order operator, unique full pencil, BFV charge or global domain
until K127 selects and composes the missing background and representative
data.
