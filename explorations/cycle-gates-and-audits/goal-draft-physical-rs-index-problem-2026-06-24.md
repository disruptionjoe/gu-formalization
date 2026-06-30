---
title: "Goal Draft: Physical RS Index Problem After the K3 Raw-Index Result"
date: 2026-06-24
status: exploration
doc_type: goal_draft
verdict: "DRAFT_GOAL: derive the physical constrained/gauge-fixed GU RS complex and index it; the raw K3 RS index is a control, not the physical GU index."
owned_path: "explorations/cycle-gates-and-audits/goal-draft-physical-rs-index-problem-2026-06-24.md"
depends_on:
  - "explorations/generation-sector/generation-count-rs-k3-symbol-index-attempt-2026-06-24.md"
  - "explorations/generation-sector/generation-count-rs-symbol-index-contract-2026-06-24.md"
  - "explorations/generation-sector/generation-count-rs-clifford-projector-computation-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/gu-typed-operator-action-spine-2026-06-24.md"
  - "tests/rs_k3_symbol_index_formula_audit.py"
  - "tests/rs_clifford_projector_model.py"
  - "explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md"
  - "RESEARCH-STATUS.md"
---

# Goal Draft: Physical RS Index Problem After the K3 Raw-Index Result

## Goal Statement

Derive and compute the physical constrained/gauge-fixed Geometric Unity
Rarita-Schwinger index on the compact K3 model, without using the desired
generation count, `ind_H(D_RS)=8`, `rank_eff=4`, or any physical
degree-of-freedom count as input.

The ambitious goal is not to repackage the raw gamma-trace-free K3 operator.
It is to construct the actual physical GU RS elliptic operator or elliptic
BRST/gauge complex, identify its K-theory symbol class in `K^0_c(T*K3)`, and
evaluate its Atiyah-Singer or APS index with every coefficient, Chern character,
H-structure, gauge subtraction, and boundary correction exposed.

The required outcome is a decision, not a preferred number:

```text
CANDIDATE_A                 if the independently derived H-index is 8
CANDIDATE_B                 if the independently derived H-index is 16
OTHER_INDEX                 if the independently derived H-index is another fixed value
NON_ELLIPTIC                if the physical symbol/complex is not elliptic
OPEN_BACKGROUND_DEPENDENT   if the answer depends on an unspecified GU background class
COMPLEX_ONLY_H_MISSING      if only a complex index is justified
OPEN_MISSING_SYMBOL_DATA    if the physical complex cannot yet be derived
INVALID_CIRCULAR            if any target value is used as an input
```

This should become the central RS generation-count gate. It should be strong
enough that a negative or "other index" answer is as useful as a favorable one.

## Why This Matters

The generation-count claim now lives or dies on an analytic-index problem, not
on raw ranks, representation dimensions, or numerological normalizations. The
spin-1/2 and additivity story can only produce a physical generation count after
the RS leg is independently computed.

This is worth doing because it separates three things that have repeatedly been
blurred:

```text
raw finite-dimensional Clifford/projector algebra
raw elliptic gamma-trace-free RS index on K3
physical constrained/gauge-fixed GU RS index
```

Only the third object can support the physical GU generation-count claim. If it
lands on `8`, the Candidate A path becomes live in a non-circular way. If it
lands on `16`, Candidate B becomes live. If it lands elsewhere, or fails to be
elliptic, the program learns something hard and valuable about where the
generation-count mechanism breaks.

The point is not to protect three generations. The point is to find out whether
the actual GU field content and gauge structure have a physical index theorem
behind them.

## What The Raw K3 Result Changed

The K3 raw-index pass changed the problem from vague to sharp.

It established a defensible raw gamma-trace-free RS symbol class. For
`V = T_C^*K3` and internal bundle `F`, the raw class is:

```text
E_raw = (V + 1) tensor F
```

In the notation `n = rank_C(F)` and `k = ch_2(F)[K3]`, the raw complex index is:

```text
ind_C(raw) = -38 n + 5 k
```

For the flat/trivial `F` branch with `n = 16` and `k = 0`, this gives:

```text
ind_C(raw) = -608
ind_H(raw) = -304   only if the right-H structure is globally verified
```

That result is not Candidate A and not Candidate B. It is also not the physical
GU index unless the physical GU complex is shown to have exactly that raw symbol
class.

The executable Clifford/projector model also made the raw finite algebra
concrete:

```text
ker_C(gamma-trace with F=C^16) = 96
```

and it showed that the raw projected RS symbol does not automatically kill the
projected gauge image in the tested finite model. Therefore the raw
gamma-trace-free operator is not already the physical gauge quotient. Gauge
fixing and/or ghosts are additional structure that must be derived.

A standard-looking BRST/anomaly-style virtual class would be:

```text
E_BRST_style = (V - 1) tensor F
ind_C(BRST_style) = -42 n + 3 k
```

and in the flat `n=16`, `k=0` branch:

```text
ind_C(BRST_style) = -672
ind_H(BRST_style) = -336   only if H-linear
```

But this is only a comparison class until the GU gauge fixing actually derives
the two spinor ghost/subtraction complexes. Subtracting ghosts because the
formula is familiar, or because a target number is desired, is invalid.

The raw result therefore changed the next goal: stop asking whether a raw K3 RS
operator can be indexed. It can. Ask instead which elliptic complex, if any, is
the physical constrained/gauge-fixed GU RS complex.

## Exact Deliverables

The project should produce a proof-grade note plus executable audits with the
following deliverables.

1. A typed derivation of the physical RS field complex from the GU carrier.

   The note must state whether the starting operator is the actual `D_GU`, the
   proposal-level `D_roll`, or a deliberately different GU-sourced operator.
   It must give the bundles over K3, the chirality conventions, the coefficient
   bundle `F = s^*S(6,4)`, the gamma-trace maps, the gauge transformations, the
   gauge condition, and the ghost or subtraction fields.

2. A principal-symbol construction.

   The artifact must construct `sigma_RS^phys(xi)` or an elliptic complex for
   all nonzero covectors `xi`. It must say explicitly how the raw projectors
   `P_+`, `P_-`, the gauge map, gauge-fixing block, and ghost complex combine.
   It must not call a raw rank or raw projector the physical symbol.

3. An ellipticity certificate.

   The certificate may be a symbolic proof, a representation-theoretic theorem
   with exact hypotheses, or an exact finite Clifford computation generalized to
   all `xi != 0`. A sampled covector is not enough except as an executable
   sanity check.

4. A K-theory symbol class.

   The deliverable must identify:

   ```text
   [sigma_RS^phys] in K^0_c(T*K3)
   ```

   or the equivalent elliptic-complex class. It must reduce to a virtual
   coefficient bundle only after the physical symbol has been derived.

5. A characteristic-class index formula.

   The formula must expose:

   ```text
   rank_C(F)
   ch_2(F)[K3]
   Ahat(K3) = 2
   p1(TK3)[K3] = -48
   all ghost/gauge-fixing contributions
   all sign and chirality conventions
   ```

   It must keep `k = ch_2(F)[K3]` symbolic unless the actual GU background
   proves a value.

6. A right-H index certificate.

   The complex index may be divided by two only after showing that the relevant
   bundles carry the right-H structure globally, the pulled-back connection
   preserves it, and the physical operator or complex commutes with it.

7. APS data if a boundary model is used.

   Closed K3 needs no APS correction. Any punctured K3, collar, or boundary
   model must supply the boundary operator for the same projected/gauge-fixed
   physical complex and compute or justify:

   ```text
   eta(A_RS^phys)
   h(A_RS^phys)
   index_APS = bulk_index - (eta + h)/2
   ```

8. A decision report.

   The report must emit one of the decision labels in the goal statement,
   include the rule that fired, and compare with Candidate A/B only after the
   independent computation is complete.

9. Executable tests.

   At minimum, extend the existing audit style with tests that distinguish:

   ```text
   raw operator
   BRST-style comparison class
   physical derived complex
   missing H-structure
   unresolved ch_2(F)
   non-ellipticity
   circular target insertion
   ```

## Acceptance Criteria

The goal is accepted only if all of the following are true.

1. The physical complex is derived before it is indexed.

   The artifact must show the actual GU source of the gauge condition and ghost
   or subtraction complex. It is not enough to write down a familiar RS BRST
   complex unless the GU operator/action forces it.

2. Raw index is not promoted to physical index.

   The draft must explicitly preserve:

   ```text
   raw K3 gamma-trace-free RS index != physical GU RS index
   ```

   unless the physical complex is derived and proved to have the same symbol
   class.

3. Ellipticity is proved for the physical object.

   The proof must apply to the gauge-fixed operator or elliptic complex, not just
   to the sampled raw projected symbol.

4. The symbol class is explicit.

   The final class must be stated in `K^0_c(T*K3)` or as an equivalent elliptic
   complex, with all virtual-bundle terms justified.

5. The index formula carries background dependence honestly.

   If `ch_2(F)[K3]` is not fixed by the physical `Sp(64)` background and section
   pullback, the decision must be `OPEN_BACKGROUND_DEPENDENT`, not Candidate A,
   Candidate B, or other fixed index.

6. The H-linear conversion is certified.

   If the right-H structure or connection compatibility is missing, the result
   remains complex-only and must not be compared as an H-index.

7. The computation is non-circular.

   The forbidden values `8`, `16`, `24`, `rank_eff=4`, `rank_eff=8`, and "three
   generations" appear only in the final comparison layer, never as inputs.

8. Boundary corrections match the operator.

   Any APS eta or kernel term must belong to the same physical RS boundary
   operator. Older spin-1/2 or unrelated `S^3` eta arguments cannot be imported
   by name only.

9. The result changes the live claim DAG.

   The final artifact must update the RS-symbol/generation-count status in the
   governance sense: closed to Candidate A/B/other, demoted to non-elliptic, or
   left open for a named missing dependency.

## Failure And Demotion Criteria

The goal fails, or must be demoted, under any of the following conditions.

1. The attempted proof identifies the raw gamma-trace-free K3 index with the
   physical GU index without deriving the physical complex.

2. The attempted proof uses `ind_H(D_RS)=8`, `rank_eff=4`, total index `24`, or
   three generations to choose a virtual class, ghost subtraction, normalization,
   Chern class, or sign.

3. The only completed computation is a raw rank such as `416`, `96`, `48_H`, or
   `24_H`.

4. The physical gauge-fixed symbol is missing, or the gauge map/gauge condition
   is described only in prose and not as bundles and maps.

5. The physical object is not elliptic. In that case the Atiyah-Singer/APS route
   does not compute a generation-count index as stated.

6. The symbol class depends on an unspecified `ch_2(F)[K3]` or background
   `Sp(64)` class while the report claims a fixed index.

7. The complex index is halved without proving the right-H structure and
   connection compatibility.

8. APS boundary terms are assumed away for a boundary operator that is not the
   same physical projected/gauge-fixed RS operator.

9. The computed physical index is an "other index" incompatible with the current
   generation normalization. That is not a proof failure, but it demotes the
   generation-count claim until the normalization or physical model is revised.

10. The actual GU typed operator/action lacks the first-order and gauge data
    used by the proposed RS complex. Then the complex is a useful comparison
    model, not the physical GU index.

## Dependencies

This goal depends on the following objects being fixed or deliberately branched.

1. The GU operator/action source.

   The typed spine currently offers a proposal-level carrier and a candidate
   rolled-up operator:

   ```text
   D_roll(u,psi) = (d_A^* psi, d_A u + Phi_2(d_A psi)) + Z_A(u,psi)
   ```

   A proof-grade RS index must say whether this is the physical source or only a
   convention. If the actual GU operator lacks the relevant `Phi_d` and
   gauge-fixing structure, the RS complex must be rebuilt.

2. The section-pullback K3 model.

   K3 is the compact model used for the current analytic gate. The computation
   must not silently promote this compact model to a theorem about the full
   noncompact `Y^14`.

3. The internal coefficient bundle.

   The working bundle is:

   ```text
   F = s^*S(6,4)
   rank_C(F) = 16
   rank_H(F) = 8, if the H-structure is verified
   ```

   Its actual `ch_2(F)[K3]` is not yet fixed.

4. The raw Clifford/projector controls.

   The existing executable model supplies `Cl(4,0)` matrices, gamma-trace maps,
   kernel projectors, and raw rank checks. These are controls and starting
   ingredients, not a physical index theorem.

5. The raw K3 formula audit.

   The existing audit verifies the arithmetic for:

   ```text
   E(q) = (T_C^*K3 + q) tensor F
   ```

   and confirms that raw and BRST-style comparison branches are large
   other-index branches in the flat `F` case.

6. The live claim DAG.

   The current governance status is:

   ```text
   RS-RAW: advanced_but_open
   RS-SYMBOL: specified_open
   GEN-COUNT: open
   ```

   The new work should change these statuses only by meeting the stated closure
   conditions.

## First 3 Concrete Work Packets

### Work Packet 1: Derive the physical GU RS complex

Write a short proof note that starts from the GU typed carrier and derives the
K3 RS field content. The output should include:

```text
E_RS^+
E_RS^-
gamma-trace maps G_+, G_-
projectors P_+, P_-
gauge maps from spinor parameters
gauge condition
ghost and antighost bundles, if any
principal symbol blocks
```

The central question for this packet is:

```text
What exact elliptic operator or elliptic complex is the physical GU RS object?
```

This packet succeeds if the answer is typed enough that a second worker can
construct its symbol without guessing. It also succeeds, in a useful negative
way, if it shows that the current GU action/operator data are insufficient and
therefore the correct status is `OPEN_MISSING_SYMBOL_DATA`.

### Work Packet 2: Prove ellipticity and extract the K-theory class

Build an executable and symbolic audit for the physical complex from Work
Packet 1. Start with the existing `Cl(4,0)` projector model, but extend it from
raw gamma-trace-free projectors to the actual gauge-fixed or BRST complex.

The output should include:

```text
all nonzero-xi symbol maps
rank/kernel or exact inverse proof
failure certificate if non-elliptic
virtual coefficient bundle
class in K^0_c(T*K3)
comparison to E_raw = (V + 1) tensor F
comparison to E_BRST_style = (V - 1) tensor F, if relevant
```

This packet succeeds if the physical class is known, even if it is not the
class anyone hoped for.

### Work Packet 3: Compute the index and emit the decision

Use the K-theory class from Work Packet 2 to compute the characteristic-class
index. Keep `k = ch_2(F)[K3]` symbolic unless the GU background fixes it.

The output should include:

```text
index_C formula
H-structure certificate or complex-only warning
index_H formula, only if justified
APS eta/h terms, only if a boundary model is used
decision label
rule that fired
comparison with Candidate A/B after the computation
```

This packet should also add or extend tests in the style of
`rs_k3_symbol_index_formula_audit.py`, including explicit regression cases for
circular input, missing H-structure, unresolved `ch_2(F)`, and non-ellipticity.

## What This Would Lead To

If the physical index is `ind_H(D_RS)=8`, the project gets its first
non-circular Candidate A route. Then the next task is to combine it with the
spin-1/2 contribution and index-additivity gates to test the total
generation-count normalization.

If the physical index is `ind_H(D_RS)=16`, Candidate B becomes the live route,
and the generation-count story must confront a four-generation or altered
normalization consequence.

If the physical index is fixed but neither `8` nor `16`, the RS lane becomes an
`OTHER_INDEX` result. That would be a major clarification: the current compact
K3 generation-count mechanism would not produce the advertised count without a
new physical ingredient.

If the index remains dependent on `ch_2(F)[K3]`, the next frontier is not more
RS projector algebra. It is the physical `Sp(64)` background and section-pullback
Chern-character problem.

If the physical symbol is non-elliptic, the Atiyah-Singer/APS generation-count
route fails as currently formulated. The project would need a different analytic
framework, a different gauge fixing, or an honest demotion of the compact K3
index route.

If the GU operator/action is not yet specified enough to derive the complex,
the immediate next lead is action closure: fix the actual `D_GU`, gauge
symmetry, and gauge-fixing data before asking for an index.

In the best case, this work produces a publishable theorem or no-go theorem:

```text
Given the GU typed carrier, section-pulled K3 model, physical gauge fixing, and
specified Sp(64) background, the physical RS complex has index I.
```

That theorem would finally let the generation-count discussion move from
status management to mathematics.

## Non-Smuggling Rule

The raw K3 result is now a control surface:

```text
raw gamma-trace-free K3 RS index:
  computable, large, and not the physical GU index by itself

physical constrained/gauge-fixed GU RS index:
  still open until the physical complex is derived
```

No future note should write "the RS index" without saying which of these two
objects it means.
