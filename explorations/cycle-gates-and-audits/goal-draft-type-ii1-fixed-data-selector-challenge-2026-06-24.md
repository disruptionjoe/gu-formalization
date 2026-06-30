---
title: "Goal Draft: Type II_1 Fixed-Data Selector Challenge"
date: "2026-06-24"
status: exploration
doc_type: goal_draft
verdict: "AMBITIOUS_FIXED_DATA_SELECTOR_CHALLENGE"
owner: "Codex"
depends_on:
  - "explorations/type-ii1-spectral/type-ii1-selector-or-nogo-theorem-2026-06-24.md"
  - "explorations/type-ii1-spectral/type-ii1-selector-anti-smuggling-theorem-2026-06-24.md"
  - "explorations/type-ii1-spectral/type-ii1-selector-candidate-2026-06-24.md"
  - "explorations/type-ii1-spectral/type-ii1-construction-or-nogo-gate-2026-06-24.md"
  - "canon/type-ii1-spectral-sm-checklist.md"
  - "specifications/type-ii1-spectral-sm/type-ii1-extension-requirements.md"
  - "explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md"
---

# Goal Draft: Type II_1 Fixed-Data Selector Challenge

## Goal Statement

Decide whether Type II_1 spectral/subfactor data can do real Standard Model
selection work, rather than merely host finite Connes-Chamseddine data or relabel
an already chosen generation count.

The ambitious goal is:

```text
Construct, or refute within a named scope, a fixed-data Type II_1 selector

X = (N subset M, tau, A, H, D, J, gamma, Phi_CC)

whose data are fixed by independent Type II_1 spectral-SM requirements and are
not parameterized by the desired number of generations, such that X selects at
least one observer-facing finite-control datum:

T_A = A_F = C oplus H oplus M_3(C),
T_G = SU(3) x SU(2) x U(1) / Z_6,
T_1 = one SM generation module,
T_3 = exactly three equivalent SM generation sectors.
```

The realistic first target is the narrow one:

```text
fixed Type II_1 data -> exactly three generation sectors
```

but the goal must keep the stronger targets visible. If the result selects only
`T_3` relative to a separately supplied one-generation finite CC module, it must
say so plainly and must not claim selection of `T_A`, `T_G`, or `T_1`.

The challenge is deliberately binary at the research-roadmap level:

1. Produce a proof-grade fixed-data selector theorem.
2. Or prove that every candidate in the named scope collapses to host-only,
   cardinality-only, external-attachment, or trace-equivalence-only status.

Either outcome is valuable. A positive result would be the first genuine Type
II_1 explanatory contribution to the finite-control problem. A negative result
would cleanly demote the Type II_1 selector lane while preserving the semifinite
hosting lane.

## Why This Matters

The current Type II_1 path has passed the easiest no-go checks. A hyperfinite
or semifinite ambient algebra can host imported finite CC data, and the KO-6
sign package is not presently a clean obstruction. That is mathematically useful
but not yet explanatory.

The finite CC Standard Model already contains the central finite-control data:

```text
A_F,
the SM gauge quotient,
the one-generation fermion representation package,
three generation copies.
```

If Type II_1 only embeds these data after they are supplied, it changes the
ambient substrate but does not explain a Standard Model datum. The selector
question is therefore the load-bearing question for whether Type II_1 adds new
finite-control content.

This matters especially for the non-embeddable motivation. If the same
observer-facing selector can be reproduced in the hyperfinite `C_n` toys, then
non-embeddability and MIP* = RE are background motivation, not load-bearing
physics. A fixed-data selector would identify what the Type II_1 or
non-embeddable regime contributes that finite CC and hyperfinite hosting do not.

## Current No-Go / Filter Result

The current filter result is negative for all instantiated selector classes.

The Type II_1 hosting lane is still open:

```text
finite CC data -> embedded or hosted in a semifinite Type II_1 setting.
```

But the Type II_1 selector lane has no positive instance:

```text
Type II_1 data -/-> A_F, SM gauge group, one-generation module, or exactly
three generations,
```

except in constructions where the target was already inserted.

The anti-smuggling theorem rules out cardinality-only selectors. A construction
fails as explanatory if it starts with an `n`-fold object and returns only an
unordered `n`-tuple of equal-trace, equal-Markov-weight, or symmetric sectors.
The canonical examples are:

```text
C3 -> C_n,
index 3 -> index n,
three arms -> n arms,
three equal projections -> n equal projections,
K_SM tensor C^3 -> K_SM tensor C^n.
```

The C3/D4 candidate is therefore a useful toy failure. It gives a clean triple
after choosing an order-3, index-3, or three-arm object. It does not select the
SM finite algebra, the SM representation package, or the physical meaning of
the three labels as generations.

Visible triples are not enough. Cardinality-only selectors are not enough.
Equal trace is not enough. Murray-von Neumann equivalence inside a II_1 factor
is not enough. A graph with three arms is not enough. A `Phi_CC` that attaches
an externally supplied `K_SM` to each sector is not enough.

The only open class is the uninstantiated fixed-data rigidity class:

```text
fixed Type II_1 spectral/subfactor data
  -> canonical three-sector orbit, index lattice, or Connes-channel image
  -> named obstruction for all nearest n != 3 replacements.
```

## Fixed-Data Standard

A candidate counts as fixed-data only if the input object is justified without
using the desired output as a parameter.

Allowed input shape:

```text
X = (N subset M, tau, A, H, D, J, gamma, Phi_CC)
```

where the ingredients are forced or independently motivated by Type II_1
spectral-SM requirements such as:

```text
semifinite spectral-triple axioms,
KO-6 real-even signs,
order-zero and order-one conditions,
tau-compactness and bounded commutators,
Breuer-Fredholm index or cyclic-cohomology constraints,
standard-invariant rigidity,
Connes-channel compatibility,
observer-facing anomaly cancellation.
```

Disallowed fixedness claims:

```text
choose C3 because there are three generations,
choose an index-3 inclusion,
choose a D4/triple-arm graph,
choose three equal projections,
choose a finite CC Hilbert space with dimension 96,
attach K_SM to each of three sector labels,
normalize an index after observing that it gives 3.
```

The candidate may contain a three-sector output. It may not contain a hidden
three-sector input.

## Exact Deliverables

### D1. Candidate-Scope Declaration

State the selector scope precisely. The scope may be broad:

```text
all finite-index Type II_1 subfactor candidates satisfying the Type II_1
spectral-SM checklist,
```

or narrow:

```text
a named fixed-data inclusion or index-rigidity object X.
```

Either way, list the allowed inputs and the forbidden target data. The scope
must say whether it is trying to select:

```text
T_A, T_G, T_1, T_3,
```

or only a relative `T_3` once `T_1` is supplied elsewhere.

### D2. Fixedness Proof Or Fixedness Failure

Give a short proof that the candidate data are not parameterized by the target
count or target finite CC data. If this cannot be proven, report the precise
failure:

```text
the candidate starts from an order-3 group,
the candidate starts from index 3,
the candidate starts from three graph arms,
the candidate starts from three chosen projections,
the candidate starts from A_F or K_SM in the selector input.
```

### D3. Standard-Invariant / Index Ledger

For the candidate `N subset M`, compute or formally specify:

```text
relative-commutant idempotents or sector objects,
Markov traces or tau-dimensions,
Connes-fusion classes,
standard-invariant automorphism orbits,
Breuer-Fredholm or cyclic-cohomology index values,
whether any orbit is canonically of size three.
```

The ledger must distinguish:

```text
equal trace,
equal Markov weight,
Murray-von Neumann equivalence,
equivalence as Connes correspondences,
equivalence as finite CC representation content under Phi_CC.
```

Only the last two are physically serious generation-equivalence candidates.

### D4. Connes-Channel Construction

Define the shadow map:

```text
Phi_CC:
  Type II_1 spectral/subfactor data
  -> finite CC control data or a declared partial shadow.
```

The construction must state which data are selected and which are imported.

For a full selector, `Phi_CC` must recover the finite-control target without
supplying it as an argument. For a narrow generation-count selector, it may be
relative to an independently selected or externally supplied one-generation CC
module, but then the claim is only:

```text
Type II_1 data select the number and equivalence of generation slots,
not the one-generation SM representation package.
```

### D5. Replacement-Family Audit

Construct the nearest replacements:

```text
X_2, X_4, and if possible X_n.
```

If no replacement exists, prove why. If a replacement exists, re-run the sector,
index, spectral, anomaly, and Connes-channel checks.

A positive selector must identify the first obstruction for `n != 3`, such as:

```text
KO-6/order-one/tau-compactness failure,
Breuer-Fredholm or cyclic-cohomology lattice obstruction,
standard-invariant rigidity with no neighboring n-sector analog,
Connes-channel functoriality failure,
anomaly/Freed-Hopkins incompatibility,
gauge/representation compatibility failure.
```

If the replacement changes only `C^3` to `C^n`, the selector fails.

### D6. Spectral-SM Compatibility Audit

Check the candidate against the Type II_1 spectral-SM requirements:

```text
tracial dimension behavior,
semifinite spectral triple framework,
KO-6 real structure and grading,
order-zero and order-one conditions,
bounded or twisted commutators,
tau-compact resolvent,
spectral-action convergence posture,
finite-case recovery or declared shadow,
absence of extra anomalous observer-facing modes.
```

The audit must not use these checks only at `n = 3`. It must say which checks
also pass at `n = 2` and `n = 4`.

### D7. Selector Theorem Or Demotion Theorem

The final technical artifact must have one of these theorem shapes.

Positive shape:

```text
Theorem. The fixed data X determine a canonical unordered orbit
{q_1, q_2, q_3} of sector objects, equivalent in the required Connes-channel
sense, compatible with J, gamma, D, order-one, and anomaly constraints, and the
nearest n != 3 replacements fail by named obstruction O.
```

Negative shape:

```text
Theorem. Every candidate in scope either imports the finite CC target, factors
through a cardinality-only n-tuple, uses only trace-equivalence data, or admits
a replacement family X_n with the same Connes-channel proof.
```

### D8. Status Update For The Claim DAG

Record the resulting status in the live-claim discipline:

```text
TYPEII1-HOST: remains conditional hosting lane unless a host obstruction fires.
TYPEII1-SELECTOR: upgrades only under the positive theorem; otherwise remains
negative_filter or demotes to host_only in the named scope.
```

The status update must name the exact dependency or closure condition that
changed.

## Acceptance Criteria

A positive fixed-data selector is accepted only if all of the following hold.

1. **Input independence.** The candidate does not start from `C3`, index `3`,
   a triple-arm graph, three chosen projections, three CC copies, `dim H_F=96`,
   or a target-normalized index.

2. **Selected output.** At least one of `T_A`, `T_G`, `T_1`, or `T_3` is
   computed from the Type II_1 data. If only `T_3` is selected, the artifact
   must state whether `T_1` is imported or separately selected.

3. **Canonical sector orbit.** For a generation-count selector, the three
   sectors form a canonical unordered orbit from the standard invariant, index
   theory, or Connes-channel construction. The orbit is not a manually chosen
   projection partition.

4. **Strong equivalence.** The sectors are equivalent in a physically relevant
   sense: as Connes correspondences compatible with `J`, `gamma`, `D`, and
   order-one, or as finite CC representation packets under a functorial
   `Phi_CC`. Equal trace alone fails this criterion.

5. **Replacement obstruction.** The nearest `n = 2` and `n = 4` replacements
   are computed or ruled out. The first failure for `n != 3` is named and is
   tied to the Type II_1 spectral-SM requirements.

6. **Connes-channel honesty.** `Phi_CC` declares every imported datum. A full
   selector does not take `A_F`, `K_SM`, or the SM gauge group as arguments. A
   relative generation selector may condition on a separately supplied `T_1`,
   but then it cannot claim to select the one-generation representation package.

7. **Spectral compatibility.** The selected sectors preserve the relevant
   semifinite spectral-triple controls: `J`, `gamma`, `D`, order-zero,
   order-one, tau-compactness, bounded or twisted commutators, and anomaly-safe
   observer-facing shadow.

8. **No decorative non-embeddability.** If non-embeddability is invoked, it must
   change the observer-facing selector or supply an invariant unavailable in the
   hyperfinite `C_n` families. Otherwise it is background motivation only.

9. **Proof-grade artifact.** The final result is a theorem, computation ledger,
   or executable/formal artifact strong enough to update the claim DAG without
   relying on narrative plausibility.

## Failure And Demotion Criteria

The candidate fails as an explanatory selector if any of these fire.

1. **Visible-three input.** The construction begins with an order-3 group,
   index-3 inclusion, D4/triple-arm graph, three projections, or three copied
   modules, and no independent theorem forces that input.

2. **Cardinality transport.** The same proof works after replacing:

   ```text
   C3 by C_n,
   index 3 by index n,
   three arms by n arms,
   three projections by n projections.
   ```

3. **External CC attachment.** The Connes-channel output is only:

   ```text
   Phi_CC(U_n) = K_SM tensor C^n
   ```

   with `K_SM`, `A_F`, and the finite spectral data supplied outside the
   selector.

4. **Trace-equivalence only.** The proof of generation equivalence uses only
   equal `tau` or Murray-von Neumann equivalence inside a diffuse factor.

5. **Standard-invariant count without spectral content.** A principal graph or
   standard invariant supplies a threefold label set but does not preserve
   `J`, `gamma`, `D`, order-one, and Connes-channel representation content.

6. **No obstruction for neighboring counts.** The candidate passes all checks
   at `n = 3`, but the same spectral, anomaly, and Connes-channel checks also
   pass at `n = 2` or `n = 4`.

7. **Host-only result.** The object embeds or hosts the already specified finite
   CC triple but selects none of `T_A`, `T_G`, `T_1`, or `T_3`.

8. **Decorative non-embeddability.** A non-embeddable factor is named, but the
   actual selector works identically in the hyperfinite setting or has no
   observer-facing effect.

If every candidate in the declared scope fails by these criteria, the correct
roadmap action is not to keep searching for visible triples. The correct action
is to mark the selector lane negative in that scope and retain Type II_1 only as
a conditional hosting or substrate-extension lane.

## Dependencies

This challenge depends on the following existing repo results.

- `type-ii1-construction-or-nogo-gate`: establishes the current separation
  between open hosting and missing selector content.
- `type-ii1-selector-candidate`: provides the C3/D4 candidate and shows why it
  is only a toy count-label mechanism.
- `type-ii1-selector-anti-smuggling-theorem`: supplies the cardinality-only
  negative filter and the `C_n` replacement test.
- `type-ii1-selector-or-nogo-theorem`: classifies instantiated selector classes
  and isolates fixed-data rigidity as the only remaining open class.
- `type-ii1-spectral-sm-checklist`: fixes the public Type II_1 posture and the
  high-value controls: KO-6, subfactor generation structure, and
  Freed-Hopkins-compatible shadow.
- `type-ii1-extension-requirements`: supplies the structural requirements for
  any Type II_1 or non-embeddable extension, including trace dimension,
  Breuer-Fredholm index, semifinite spectral triples, KO structure,
  standard-invariant data, non-embeddable separation, finite-case recovery, and
  spectral-action convergence.
- `live-claim-dag-fault-finality-ledger`: fixes the governance status:
  `TYPEII1-HOST` is conditional, while `TYPEII1-SELECTOR` is a negative filter
  with no positive selector finality.

The mathematical work depends on specialist competence in:

```text
finite-index subfactors and standard invariants,
planar algebras or fusion-category methods,
semifinite spectral triples,
Breuer-Fredholm and cyclic-cohomology index theory,
Connes-Chamseddine finite spectral data,
anomaly/Freed-Hopkins compatibility,
and the observer-facing Connes-channel shadow.
```

## First Three Concrete Work Packets

### Work Packet 1: Fixedness And Candidate Inventory

Build a short inventory of possible fixed-data candidates and immediately reject
anything whose "three" is visible at input.

Output:

```text
a candidate table with columns:
candidate X,
source of fixedness,
target claimed,
where 3 enters,
imported CC data,
nearest replacement X_n,
preliminary verdict.
```

Minimum candidates:

```text
C3/D4 as the negative control,
one non-C3 finite-index or standard-invariant candidate if a specialist can name it,
one Breuer-Fredholm or cyclic-cohomology index-rigidity candidate if available.
```

Pass condition for the work packet:

```text
at least one candidate survives the visible-three and imported-CC filters,
or the inventory proves that no candidate presently survives those filters.
```

### Work Packet 2: Sector / Index Ledger For The Lead Candidate

For the best surviving candidate, compute the sector and index data.

Output:

```text
relative-commutant idempotents or sector objects,
Markov traces or tau-dimensions,
fusion/equivalence data,
standard-invariant automorphism orbit,
Breuer-Fredholm or cyclic-cohomology index values,
whether a canonical three-sector orbit is forced.
```

The ledger must explicitly separate:

```text
cheap equal trace,
ambient Murray-von Neumann equivalence,
standard-invariant equivalence,
Connes-correspondence equivalence,
finite-CC representation equivalence.
```

Pass condition for the work packet:

```text
the lead candidate has a canonical three-sector structure stronger than equal
trace, or it is demoted with a named reason.
```

### Work Packet 3: Phi_CC And Replacement Obstruction Audit

Define `Phi_CC` for the lead candidate and run the nearest `n != 3`
replacement tests.

Output:

```text
Phi_CC on each sector,
list of selected versus imported finite-control data,
checks for J, gamma, D, order-one, tau-compactness, and anomaly shadow,
replacement audit for n = 2 and n = 4,
first obstruction for n != 3 or proof that no obstruction appears.
```

Pass condition for the work packet:

```text
either a named obstruction blocks all neighboring counts,
or the candidate is formally classified as cardinality transport.
```

## What This Would Lead To

A positive result would upgrade the Type II_1 pathway from:

```text
conditional host of finite CC data
```

to:

```text
operator-algebraic selector of an SM finite-control datum.
```

Even the narrow positive result:

```text
fixed Type II_1 data -> exactly three generation sectors
```

would be a major improvement over finite CC hand insertion, provided the
sectors are functorially compatible with the one-generation SM module and the
replacement family fails for a structural reason.

A stronger positive result that selects `A_F`, `T_G`, or `T_1` would be more
important still. It would turn Type II_1 data into a genuine finite-control
source rather than a generation-count add-on.

A negative result would also be valuable. It would justify the public posture:

```text
Type II_1 is a viable semifinite hosting/substrate-extension lane,
but not presently an explanatory SM selector.
```

It would prevent future work from cycling through visible triples, D4 arms,
order-3 groups, and equal-trace projection partitions. It would also clarify
that non-embeddable motivation must produce a new invariant or be treated as
decorative for Standard Model selection.

The clean next state after this challenge should be one of:

```text
FIXED_DATA_SELECTOR_FOUND,
FIXED_DATA_SELECTOR_FOUND_RELATIVE_TO_T1,
NO_GO_IN_DECLARED_SCOPE,
NO_CANDIDATE_SURVIVES_FIXEDNESS_FILTER,
OPEN_SPECIALIST_DEPENDENT_WITH_NAMED_CANDIDATE.
```

Anything weaker leaves the project in the current ambiguous state: a strong
hosting lane, a useful anti-smuggling theorem, and no positive Type II_1
selector.
