---
artifact_type: construction_and_scope_result
created: 2026-08-11
ledger_version: "0.181"
result: LOCAL_BOUNDARY_BRST_AND_OBSERVATION_NATURALITY_CLOSE__W_AND_MIRROR_RESTRICTIONS_FAIL__COMMON_H640_ACTION_CLOSURE_FOUND__SOURCE_SELECTION_AND_PHYSICAL_BV_OPEN
grade: "exact rational BRST/associated-bundle composition plus complete rank-1920 two-prime finite-field carrier test"
canon_verdict_change: none
fork_assumed: none
fork_note: "Real K77, selected Spin, Curt's two U(32,32) halves, full U(64,64), and both action-pairing horns remain distinct conditional objects."
source_return: SOURCE-SILENT
ledger_rows: [RA-D4, RA-F1, RA-F2, RA-G2, LT-SM3, AC-F1]
---

# Selected K77 boundary BRST, observation and carrier closure

## Plain-English result

The local gauge symmetry and the moving incoming-boundary condition fit
together: if the fields, ghost and projector are transported consistently,
the boundary relation is preserved by the ordinary gauge BRST differential
and descends across observation frames.

The proposed physical `W` and mirror sectors do **not** separately fit that
boundary dynamics. Each has rank 320, but the action sends 128 directions out
of it. Their rank-512 union still leaks by rank 128. Consequently it is not yet
mathematically meaningful to ask for the physical cohomology restricted to
`W` or to its mirror.

The constructive surprise is that `W`, the mirror and their union all generate
the same minimal closure under the three tested spatial action generators. It
has rank 640 and projects as 512 one-form directions plus the complete 128
zero-form spinor. Call it `H640` provisionally. This is a conditional
action-closure theorem after a seed is supplied; it is not yet evidence that
the source action selects `H640`, and it is not the earlier one-form rank-640
carrier merely because the dimensions agree.

## Layer 0

| phrase | exact object | not established |
| --- | --- | --- |
| BRST closure | the ordinary even gauge differential and its moving projector relation | the full physical BV/Koszul–Tate differential |
| observation descent | three-patch associated-bundle/frame naturality | complete nonlinear `4+10` Euler faithfulness |
| `W` or mirror sector | a supplied rank-320 complete four-field seed | an invariant boundary subcomplex or selected matter space |
| `H640` | common spatial-action hull of `W`, mirror or their union | source selection, uniqueness among controls, or equality with the old one-form 640 |
| cohomology | a question requiring an invariant complex | a computed physical cohomology, index or generation count |
| Pin exchange | exact exchange of the one-form carrier labels | a symmetry of the complete four-field operator or fixed-normal boundary problem |

## Exact result

The local rational comparator proves

```text
s varpi = [c,varpi] - dc,      s Pi_in = [c,Pi_in],
s(Pi_in Psi) = c(Pi_in Psi),  s^2 = 0,
```

and the same relation descends on three noncommuting observation patches. A
frozen projector and a transported ghost without projector transport both
fail as planted controls.

On the complete rank-1,920 conditional K77 principal carrier, independently
over `GF(1009)` and `GF(1013)`:

| carrier | rank | incoming intersection | incoming leakage | one-normal hull |
| --- | ---: | ---: | ---: | ---: |
| `W` | 320 | 96 | 128 | 448 |
| mirror | 320 | 96 | 128 | 448 |
| `W + mirror` | 512 | 192 | 128 | 640 |

Under all three tested spatial Clifford evolutions, all three seeds generate
the same rank-640 hull. Its projections have ranks `512 + 128`. The probe
passes 45 checks, including four firing plants, with zero failures.

## Adaptive specialist pre-assessment

- **Layer-0/source:** demanded separation of source covariance grammar,
  ordinary gauge BRST, full BV/KT and physical cohomology.
- **BRST/BV:** allowed a local small-gauge subcomplex result but refused to
  identify it with the missing physical Koszul–Tate differential.
- **Principal-bundle geometry:** made simultaneous transport of the ghost,
  field and projector the naturality test.
- **Representation/Clifford:** required complete rank-1,920 tests and prevented
  the equal rank-640 numbers from becoming an identification.
- **Symplectic/BFV:** required the boundary relation to be tested against the
  action's Green structure and kept unrestricted boundary charges open.
- **Analytic/operator:** treated finite exact ranks as symbol-level data, not a
  Sobolev/Fredholm theorem.
- **Krein/reality:** retained both pairing horns and both chiral halves.
- **Exact computation:** required two primes and planted wrong-transport and
  wrong-symmetry controls.

## Pin control

The one-form Pin map exchanges `W` and its mirror exactly. The obvious
block-diagonal lift to the complete four-field space does not intertwine the
operator, reverse the fixed normal correctly, or exchange incoming and
outgoing—even in the equal-weight control. This kills that naive lift only;
other complete Pin lifts remain open.

## What moved and what did not

Closed:

- local ordinary-gauge BRST covariance of the moving incoming relation;
- associated-bundle observation-frame naturality; and
- the exact common conditional action closure `H640 = 512 + 128` generated by
  `W`, its mirror or their union.

Rejected as mistyped:

- computing restricted `W` or mirror physical cohomology before proving an
  invariant boundary complex.

Still open:

- whether `H640` is distinguished against random rank-192 seeds, the older
  one-form 640 and the 832 carrier;
- a source/action-derived full BV/Koszul–Tate differential on the carrier
  selected by those controls;
- global analytic domains, null BFV, full nonlinear observation descent,
  horn/`p` selection, chirality, index and count.

Selected Spin, the two `U(32,32)` halves and full `U(64,64)` remain distinct.
P1/P2/P3 are unchanged and unused. No verdict, residue, quotient, canon verdict
or public posture changes.

## Frontier

```text
headline_delta: none
frontier_conditions_closed: 3
  - local ordinary-gauge boundary BRST covariance
  - associated-bundle observation-frame descent
  - common conditional spatial-action closure H640 = 512 + 128
frontier_conditions_opened: 1
  - distinguish H640 from generic and previously named carrier controls
remaining_named_conditions: 2
  - H640 discriminator/source-selection test
  - full physical BV/KT plus global analytic/null/index closure
```

## Next gate

`CONTROL_H640_AGAINST_RANDOM192_OLD_ONE_FORM640_AND832__THEN_DERIVE_BV_KT_ON_H640_OR_FULL1920_AS_CONTROLS_DECIDE`.

Probe:
`tests/channel-swings/selected_k77_boundary_bv_observation_cohomology_probe.py`.
