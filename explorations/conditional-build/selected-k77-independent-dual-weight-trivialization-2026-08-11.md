---
artifact_type: construction_and_composition_result
created: 2026-08-11
ledger_version: "0.175"
result: SOURCE_NATIVE_INDEPENDENT_DUAL_ORBIT_REMOVES_BOTH_WEIGHTS__P_REALITY_CONDITIONAL_ONLY
grade: "complete constant nonzero diagonal left/right orbit classification on the selected real-K77 independent-dual operator; anti-linear reality and global domain open"
canon_verdict_change: none
fork_assumed: none
fork_note: "Real K77 is a labelled conditional comparator; no signature or action-parent row is settled."
search_space_dim: "eight left/right sector scalars subject to four unit-block equations; the two-weight orbit is decided wholesale"
free_object_delta: "zero new fields or data; zero booked residue change"
residue_touched:
  - "RA-D4:T2_DISTANCE_ONLY"
  - "RA-F1:T2_DISTANCE_ONLY"
  - "RA-F2:T2_DISTANCE_ONLY"
  - "RA-G2:T2_DISTANCE_ONLY"
  - "LT-SM3:T2_DISTANCE_ONLY"
  - "AC-F1:T2_DISTANCE_ONLY"
ledger_rows: [RA-D4, RA-F1, RA-F2, RA-G2, LT-SM3, AC-F1]
source_return: SOURCE-CORRECTS
scripts:
  - tests/channel-swings/selected_k77_independent_dual_weight_trivialization_probe.py
registry: lab/process/selected-k77-independent-dual-weight-trivialization.json
---

# Selected K77 independent-dual weight trivialization

## Plain-English result

The last apparent K77 weight parameter is not yet physical.

Ledger v0.174 correctly found that `p=w_+w_-` cannot be removed by a single
pairing-preserving transformation applied congruently to a reality-reduced
fermion. But Weinstein's displayed action has four independent barred and
unbarred fields. That parent allows independent invertible changes of
coordinates on the two action slots.

The complete normalization-preserving left/right orbit sends every nonzero
weight pair to the equal-weight representative while leaving both unit
cross-degree `d/d*` blocks exactly normalized. It also sends the reciprocal
southeast coefficients to `11/12`. Thus neither `w_+`, `w_-`, nor their
product is invariant on the source-native four-field action.

This does not make v0.174 false. Its two local Grassmann pairing horns and
product invariant become relevant if a later anti-linear reality condition
ties barred and unbarred fields together, restricting left/right equivalence
to congruence. No such reality or global physical domain has been built.

## Layer 0

- independent barred/unbarred action is not a reality-reduced congruent
  quadratic action;
- left/right equivalence is not pairing-preserving isometry;
- transporting observation under a field coordinate change is not holding its
  coordinate matrix fixed;
- a source-native orbit coordinate is not a physical coupling after reality;
- selected Spin, two `U(32,32)` halves and full `U(64,64)` remain distinct.

## Complete scalar orbit

Let `(a,b,c,d)` scale the unbarred `Omega^1_+`, `Omega^1_-`, `Omega^0_+`,
`Omega^0_-` sectors and `(alpha,beta,gamma,delta)` scale their independent
barred rows. Keeping the two chirality-preserving cross-degree blocks unit
gives

```text
alpha*c = beta*d = gamma*a = delta*b = 1.
```

The weighted odd blocks transform as

```text
w_+   -> beta*a*w_+
w_-   -> alpha*b*w_-
ell_+ -> delta*c*ell_+
ell_- -> gamma*d*ell_-.
```

Choosing `(a,b,c,d)=(1,1,w_-,w_+)` maps

```text
(w_+, w_-, ell_+, ell_-)
  -> (1, 1, 11/12, 11/12).
```

The crossed products `w_+ ell_-` and `w_- ell_+` are invariant, but v0.173
already fixed both to `11/12` as the semisimplicity conditions. There is no
remaining scalar invariant on this source-native orbit.

## Exact carrier and nonlinear-natural tests

The certificate reproduces the equivalence on the complete 1,920-dimensional
operator over `GF(1009)` and `GF(1013)`:

- all fourteen derivative axes;
- four independent noncentral even Clifford insertions in the connection-cell
  grammar;
- both unit cross-degree blocks;
- two noncentral even gauge generators, showing the field equivalences commute
  with the gauge/Noether action;
- a rank-640 observation map transported as `O -> O R`.

Holding the coordinate matrix `O` fixed is a firing plant, not a physical
counterexample. An odd connection insertion and a wrong crossed product also
fire. The theorem is for constant nonzero scalar weights; if future work makes
them functions on `Y`, derivatives of the field redefinition create new
connection terms and require a separate test.

## Source return

The 2021 extraction explicitly calls the barred and unbarred fields four
distinct fields, wraps the operator in covariance factors and presents
"operators like" the displayed matrix rather than a uniqueness theorem. It
does not construct an anti-linear K77 reality, a global domain or a physical
normalization that would forbid the left/right orbit.

Return:
`SOURCE_CONFIRMS_FOUR_INDEPENDENT_FIELDS_AND_COVARIANT_OPERATOR_FAMILY__SOURCE_CORRECTS_P_FROM_SOURCE_NATIVE_INVARIANT_TO_REALITY_CONGRUENCE_CONDITIONAL__SOURCE_SILENT_ON_ANTILINEAR_REALITY_GLOBAL_DOMAIN_AND_PHYSICAL_NORMALIZATION`.

## Frontier and next gate

Closed: both constant source-native weights and `p` as independent-dual
invariants; connection/gauge/Noether and transported-observation compatibility
of the equivalence.

Open: anti-linear reality, its moving global Green/domain, observation
basicness on that domain, physical BV/cohomology, mirror removal, index and
count. No booked residue moves because v0.174 did not book `p`.

Next:
`CONSTRUCT_OR_KILL_ANTILINEAR_REALITY_INVOLUTION_AND_GLOBAL_GREEN_DOMAIN__ONLY_THEN_RETEST_CONGRUENCE_INVARIANT_P`.
