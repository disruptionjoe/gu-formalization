---
artifact_type: conditional_physics_ledger_view
created: 2026-08-05
version: "0.17"
machine_source: lab/process/conditional-physics-ledger-v0.17.json
predecessor: lab/process/conditional-physics-ledger-v0.16.json
status: APPEND_ONLY_SELECTED_CUBIC_QFT_THRESHOLD_AND_NUMERATOR_GATE_UPDATE
---

# Conditional physics ledger v0.17

## Progress meter

```text
Ledger v0.17 — 82/82 active target rows mapped (100% of denominator)
33 SAME · 19 DIFFERS · 24 NEEDS · 6 OVER-DETERMINED
Fixed-background TT C: unchanged, exact on the free-connected component
Scalar-enlarged vacuum Hessian: no new block; the cubic Hessian is zero there
Continuum odd channels: real shell for either scalar parity
Decisive missing object: selected on-shell momentum numerator
Residue — 84 continuous real before quotient + >=19 function-valued
          + 9 open discrete forks
Quotients ranked: 4 scoped; no global physical residue reduction booked
```

Coverage, verdict counts, global residue and quotient count are unchanged.
Four row distances move. This wave replaces a mistyped matrix enlargement
with the first correctly typed continuum state-space gate.

## What moved

The complete cubic

```text
V3 = c theta (q0 + qm)^2
```

has a zero full Hessian at `(q0,qm,theta)=0`. At fixed `theta_bar`, only the
predecessor's two-by-two TT block survives. The next interaction is therefore
not a larger three-by-three background `C`.

Instead, the complete parity bank and continuum thresholds are now exact:

- even `theta`: `theta q0 qm` is odd; for unequal positive scalar and massive-
  TT masses, the heavier species can transition to the lighter plus massless
  `q0`; equality is a soft boundary;
- odd `theta`: `theta q0^2` is odd and a positive-mass scalar is above the
  two-massless threshold.

The energy denominator therefore has a real zero for either parity under the
stated positive-mass hypotheses. No `Q1` pole is booked, because the actual
selected momentum numerator on that shell is not built. The exact negative
control `N=D*R` makes the apparent pole removable.

## What did not move

- The fixed-background `C(u)` and its exceptional-locus classification remain
  valid in their stated two-field scope.
- No physical on-shell numerator, `Q1`, higher-order `C`, physical-sheet pole,
  width, loop theorem or common BV/Green/Fock domain is built.
- The observed continuum proxy is not identified with the complete native
  `Y^14` quantum state space.
- Super-IG global descent and the normalized observer functional remain
  independent open constructions.
- P1/P2/P3 remain unused.

## Row movements

| row | verdict/kind retained | distance now |
| --- | --- | --- |
| `LT-GR2b` | `SAME/DERIVED_PARTIAL` | derive the selected on-shell cubic numerator and its native/observed descent |
| `LT-GR3` | `DIFFERS/STRUCTURAL_DIFFERENCE` | restrict the curvature-squared odd numerator to the exact shells, then run physical-sheet H59/W132 |
| `LT-GR5` | `DIFFERS/STRUCTURAL_DIFFERENCE` | include moving trace, Shiab, augmented torsion and compensators in the cubic numerator on a common domain |
| `LT-SM8` | `NEEDS/PROVEN_UNSUPPLYABLE` | construct regular Q1 or carry a nonzero shell into the complete even-BV/Fock metric; super-IG stays separate |

Every other row is unchanged.

## Next gates

1. Derive the full selected `Y^14` cubic momentum vertex, descend it through
   observation and the even-BV quotient, and evaluate its odd numerator on the
   exact shells.
2. If the numerator is nonzero, run physical-sheet/self-energy H59; if it is
   divisible by the denominator, build regular `Q1` and continue to `Q2`.
3. Independently globalize the mixed super-IG bracket.
4. Independently derive or supply the covariant normalized observer functional
   and place it in one action before advancing dark-energy prediction rows.

Evidence:

- `selected-cubic-qft-threshold-and-numerator-gate-2026-08-05.md`;
- `selected_cubic_qft_threshold_numerator_probe.py`;
- `selected_cubic_qft_threshold_numerator_independent.sage`;
- `selected-cubic-qft-threshold-and-numerator-gate-source-reinspection-2026-08-05.md`;
  and
- `2026-08-05-selected-cubic-qft-threshold-and-numerator-gate-review.md`.
