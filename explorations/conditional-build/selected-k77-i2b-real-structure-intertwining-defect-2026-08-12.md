---
artifact_type: construction_result
created: 2026-08-12
source_claims: [SC-ACT-02, SC-ACT-04]
source_return: SOURCE_CONFIRMS_RESIDUAL_SHELL_SQUARE_AND_MOVING_CONJUGATED_SHIAB_INGREDIENTS__REPO_CORRECTS_NONZERO_ADDITIVE_DESCENT_AND_WHOLESALE_IMAGE_EXCLUSION_READINGS__SOURCE_SILENT_ON_HQ_REAL_INVOLUTIONS_FIXED_OUTPUT_PROJECTION_AND_COMPENSATOR_NATURALITY
verdict: ADDITIVE_GALOIS_DESCENT_OBSTRUCTION_KILLED__Q13_FIXED_OUTPUT_ESCAPE_CONSTRUCTED__HELDOUT_Q12_NATURALITY_FAILS__ACTION_OWNER_OPEN
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
fork_assumed: none
search_space_dim: 99463
free_object_delta: 0
residue_touched:
  - "RA-E1:T2_DISTANCE_ONLY"
  - "RA-E3:T2_DISTANCE_ONLY"
  - "LT-SM6:T2_DISTANCE_ONLY"
---

# Selected K77 I2B real-structure intertwining defect

## Outcome

The complex-success/real-failure split in v0.202 is not a nonzero additive
Galois-descent class.  Over a real vector space, characteristic-zero averaging
kills that proposed obstruction whenever the operator intertwines the source
and target involutions.  The actual selected Shiab does not intertwine them.

On the complete `99,463`-column pointwise source bank, its fixed and anti-fixed
output pieces have exact ranks

```text
rank(P_+ A)       = 170
rank(P_- A)       = 195
rank(A)           = 364
rank(tau_t A-A)   = 195 on fixed sources
total realified defect rank = 390.
```

At the original q13 representative, the canonical fixed-output map `P_+ A`
does contain the displasion target.  This is a real local construction with no
new coefficient or datum.  But the identical recipe fails after moving the
trace direction and target to the held-out q12 representative.  It is therefore
not yet a natural source-action construction: an action-owned moving
compensator, a different codomain reality, or a different Shiab would be needed.

## Layer 0

The following are different objects:

1. a complex preimage of a real target;
2. a preimage in the fixed-point source of an intertwining real map;
3. a nonintertwining complex map followed by `P_+=(1+tau_t)/2`;
4. a sectorwise rephasing `P_+A - iP_-A`;
5. a pointwise formula at one `q`;
6. a compensator-aware natural family over moving `q`;
7. a global principal connection, its Bianchi curvature and its Euler map.

The result constructs item 3 at q13, rejects its naive extension to q12, and
does not promote it to items 6 or 7.

## Why additive descent is unavailable

Let `A:V_C -> W_C` intertwine real involutions and let `y` be fixed.  If
`Ax=y`, then `(x+tau_s x)/2` is fixed and has image `y`.  Equivalently, the
additive `H^1(Z/2,V)` of a real vector space vanishes by averaging.  A complex
preimage without a real preimage must therefore signal nonintertwining,
mistyped real structures, or a nonlinear/global constraint.  The exact defect
ranks above identify nonintertwining here.

## Canonical projections and controls

For q13:

```text
P_+ A                         rank 170, target admitted
-i P_- A                      rank 195, target excluded
span(P_+ A, -i P_- A)         rank 196, target admitted
P_+ A +/- i P_- A             rank 196, target admitted
```

The unequal ranks and the firing anti-fixed control show that the q13 result is
not a vacuous projection that makes every component work.  The held-out q12
test is more important: `P_+A` again has rank `170`, but adjoining its moved
target raises the rank to `171`.  The local escape is not invariant under this
naive co-moving replacement.

This does not yet prove that no compensator-aware family exists.  Earlier GU
work already found that constant label transport can fail where a moving
Lorentz compensator succeeds.  That is now the live burden.

## Source return and constraint accounting

`SC-ACT-02/04` own the residual shell and square, and source material owns
conjugated moving Shiab ingredients.  No inspected source owns the operative
`H_q` involutions, the post-composed `P_+`, the sectorwise rephasing, or the
compensator making them natural.

- New fields, parameters, data and selectors promoted: `0`.
- Candidate post-composition introduced: `1`, unowned and unpromoted.
- P1/P2/P3: unchanged and unused.
- Ledger verdicts, residue, canon and public posture: unchanged.

## What died and what survived

**Died:**

- a nonzero additive `H^1(Z/2,ker A)` explanation of v0.202;
- treating the selected Shiab as a single real intertwining map;
- promoting the q13 `P_+` escape as a frame-independent construction;
- the claim that complex success alone demonstrates a physical solution.

**Survived:**

- the exact v0.203 exclusion for the unmodified selected Shiab;
- q13 `P_+A` as a local witness that the target is not absent from every
  real-valued modification of the selected map;
- compensator-aware moving-reduction naturality;
- a degree-shifted target reality or alternate source-typed Shiab;
- global connection/Bianchi realization, Euler/preboundary, physical quotient,
  BV/domain and spectrum.

## Next gate

Construct the exact moving compensator transporting q13 to q12 and test whether

```text
g (P_+^{q13} A_{q13}) g^{-1} = P_+^{q12} A_{q12}
```

after transporting the selected Shiab, target and source action together.  If
it fails, the fixed-output escape is a frame artifact.  If it succeeds only
after a new term, that term must be located in the source action and priced.
Only then should the moving derivative and full Euler/preboundary map resume.
