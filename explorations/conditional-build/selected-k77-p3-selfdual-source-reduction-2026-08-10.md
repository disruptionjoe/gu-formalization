---
artifact_type: exact_construction_composition_and_scoped_kill_result
created: 2026-08-10
status: CURRENT_NONZERO_SOURCE_FAMILY_NOT_SU2PLUS_REDUCED__DBP_SPLIT_PRESERVATION_INSUFFICIENT__PROJECTED_ACTION_REPLACEMENT_UNBUILT
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE_SILENT_P3_SOURCE_DIAGONAL_AND_RESTRICTED_ACTION__SOURCE_CORRECTS_SELF_DUALITY_AS_EINSTEINIAN_NOT_BARE_YANG_MILLS
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR2d, LT-GR6]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 P3 self-dual source reduction

## Result in plain English

The nonzero self-dual pairing found in v0.145 does not revive the current
source action.

The selected source curvature preserves the split between positive and
negative four-dimensional chirality.  But it occupies **both** corresponding
`SU(2)` factors.  The self-dual and anti-self-dual Lie-algebra spans each have
rank three, and both are nonzero whenever the remaining VEV amplitude `t` is
nonzero.  Consequently

```text
D_B P_sd = 0                 preserves the two-block split;
F_B valued only in su(2)+    selects the self-dual factor.
```

The first condition does not imply the second.  The predecessor's example
criterion `D_B P_sd=0` was therefore too weak.

For the exact family

```text
F_B=(t^2/3)(Phi1 wedge Phi1),
```

membership in the single self-dual factor forces `t=0`.  The current nonzero
stationary family is not a connection on the proposed `SU(2)+` reduction.
The direct and self-dual versions of the current P3 magnitude route are now
both killed at current-action grade.

There is still a constructive replacement: strengthen P3 from an auxiliary
operator twist to an explicit `SU(2)+` subbundle of the varied source parent,
restrict the source configuration space **before** variation, and recompute
the first action.  Restriction projects the Euler covector, so this replacement
is mathematically well typed and introduces no automatic continuous
coefficient.  But it is a new action/external-datum construction, not a hidden
property of the existing family.

## Layer 0

| phrase | exact object | not the same as |
| --- | --- | --- |
| chiral split | `S_4=S_4+ direct-sum S_4-` and projector `P_sd` | selection of one `SU(2)` factor |
| split-preserving connection | connection with `D_B P_sd=0` | `SU(2)+`-valued connection |
| self-dual source reduction | principal subbundle whose connection and curvature lie in `su(2)+` | chirality-weighted trace on the full source curvature |
| P3 BPST bundle | fixed auxiliary Hopf/anti-Hopf connection pulled back by the collapse map | subbundle of the varied source parent |
| restricted action | pullback of `I1` to a reduced configuration space before variation | projecting an already-solved curvature afterward |
| topological selection | existence of a global source connection in a fixed integral sector | a local algebraic rescaling of curvature |

The repeatable trap is that every Spin(4) bivector commutes with four-plane
chirality.  Thus `D_B P_sd=0` can hold while the connection still contains both
`su(2)+` and `su(2)-`.  A factor-selection theorem must test the factor itself,
not merely the grading it preserves.

## Exact calculation

For Euclidean four-plane Clifford generators `gamma_i`, set

```text
chi_4=gamma_1 gamma_2 gamma_3 gamma_4,
P_+=(1+chi_4)/2,
P_-=(1-chi_4)/2,
F_ij=gamma_i gamma_j.
```

Every `F_ij` commutes with `chi_4` and has zero cross blocks.  Nevertheless,

```text
rank span{P_+ F_ij P_+}=3,
rank span{P_- F_ij P_-}=3.
```

Both factors are present.  Their quadratic pairings are `+12` and `-12`,
which reproduces the v0.145 cancellation.  Scaling the anti-self-dual block by
`t^2/3` makes it zero only at `t=0`.

The result is stronger than “the reduction is not yet proved”: the current
nonzero family positively fails membership in it.  It is narrower than “no
self-dual source action can work”: a different action varied on a reduced
configuration space has not been built.

## What a real replacement would require

The minimal conditional construction is now explicit:

1. replace or strengthen P3 with a principal-bundle map embedding its fixed
   `SU(2)` bundle as the tangential `SU(2)+` subbundle of the source parent on
   the framed cycle;
2. use connections on that subbundle as the action's varied field space,
   rather than project a full-parent solution afterward;
3. pull back `I1` to that field space and recompute **all** Euler rows, because
   the old `f(t),u(t),t` family no longer applies;
4. prove the reduction is compatible with the two-connection gauge action,
   observation descent, anomalies, presymplectic form, BV differential and
   common Green/Krein domain;
5. only then impose the integral P3 sector and test whether it discretizes a
   surviving amplitude without a free normalization.

At finite-dimensional variational grade, restricting first gives the projected
Euler covector `P_+ dI1`.  That establishes the type of the replacement.  It
does not supply the missing global bundle map or the GU coefficient bank.

## Constraint accounting

The current route removes zero continuous coordinates because its nonzero
family has empty intersection with the one-factor reduction.  The replacement
does not yet earn positive surplus.  It adds at least one function-valued
bundle-reduction/diagonal map and changes the admissible field space; whether
P3 fixes that map up to discrete equivalence must be proved before it can be
priced as external data rather than a new fit.

No P1/P2/P3 assignment changes.  In particular, P3 remains an auxiliary
`KO`/BPST operator twist until the explicit source-parent embedding is built.

## Source return

Weinstein's transcript says that instanton self-duality is “Einsteinian,” not
bare Yang--Millsian.  That supports treating the tangential self-dual factor as
geometric frame data rather than silently as an internal source gauge field.
The sources do not state the P3/source diagonal, the restricted action, or the
Euler closure.  Those remain repository constructions.

## Efficient specialist return

1. **Clifford algebra — ACTUAL MATH, very high.** Even bivectors commute with
   chirality, so split preservation cannot select a chiral ideal.
2. **Principal-bundle geometry — ACTUAL MATH, very high.** Curvature in both
   ideals forbids reduction of the nonzero connection to either one factor.
3. **Chern--Weil — ACTUAL MATH, very high.** The opposite nonzero factor
   pairings explain both the full cancellation and why factor projection is a
   different characteristic problem.
4. **Variational bicomplex — ACTUAL MATH, high.** Restriction must occur before
   variation; afterward projection changes the theory.
5. **Symplectic/BV--BFV — ACTUAL MATH, high.** A subbundle restriction is not a
   quotient. Its constraints, gauge algebra and boundary phase space must be
   rebuilt together.
6. **Source criticism — ACTUAL MATH, high.** The self-dual factor is typed as
   tangential at reconstruction grade; no source text supplies the P3 diagonal.
7. **Constraint accounting — ACTUAL MATH, high.** A function-valued reduction
   map cannot be priced as a free discrete choice until uniqueness is proved.

## Progress

```text
Ledger v0.146 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional parent range 84..86
Scoped quotients 5

headline_delta: none
frontier_conditions_closed: 1
frontier_conditions_opened: 1
remaining_named_conditions: 3
```

Next build or kill the explicit P3-to-source `SU(2)+` principal-bundle
diagonal and the corresponding restricted first action.  Do not carry the old
nonzero family into that action; its anti-self-dual block proves it belongs to
the unreduced theory.

Validation: exact SymPy route (`60/60`) and durability audit; planted split-versus-factor
and post-solution-projection confusions fire.  No canon, verdict, residue,
quotient, public posture or datum assignment moves.

Known inherited process red: `functional_channel_operating_contract_scope_audit.py`
still requires the superseded phrase `ACTION_OWNED_DEGREE14_GREEN_PRIMARY`,
which is absent at both the Run's starting revision and this result.  This Run
does not rewrite that out-of-scope predecessor gate.
