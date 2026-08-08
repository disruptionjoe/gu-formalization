---
artifact_type: exploration_result
created: 2026-08-07
status: ONE_QUOTIENT_RANKED_83_TO_81__LARGEST_QUOTIENT_BLOCKED_ON_A_DECLARATION_ROW__COUNT_IS_A_FUNCTION_NOT_A_NUMBER
run_id: GUH-20260808T024447Z-source-action-parameter-structure
grade: "CLASSIFICATION AND EXACT COORDINATE MATCHING over filed text. The one
  ranked quotient is computed by intersecting a named rank-3 rescaling group's
  three rows against the packet's own charged-coordinate list; the arithmetic is
  integer and checkable by eye. No orbit dimension was computed from numerics.
  The structural result about genesis-dependence is a dependency argument, not a
  computation, and is labelled as such."
ledger: lab/process/conditional-physics-ledger-v0.39.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
priority_change: none
row_change: none
residue_touched: []
ledger_rows_declared_before_work: "none. This ranks a quotient against the CB-D
  parameter ledger; it is not a Build on a conditional-physics row. No meter
  movement is claimed and none occurred."
deposit: "PRE-DEPOSIT. Not citable until hostile-reviewed under the standing
  2026-08-03 rule."
follows:
  - explorations/declaration-viable-region-2026-08-07.md
---

# Quotient ranking, first pass: 83 -> 81, and why the rest is blocked

## Outcome

CB-D states that the source action's `83` real continuous parameters are "an
upper bound before quotients" with **zero** quotients ranked, and that "the
cheapest available way to move this lane's number is to rank one quotient."

**One quotient is now ranked. It removes two parameters, not three.**

```text
before                                                    83
normalization rescaling quotient (rank 3, 2 rows charged)  -2
after                                                     81
```

**And the largest remaining quotient cannot be ranked at all until a
`DECLARATION` row is fixed.**

## The ranked quotient

`PRED-NORM-RANK` supplies a rescaling group of rank three with exactly three
rows (`tests/normalization-scoping/pred_norm_rank.py:104-108`):

```text
row 1  (kappa:+1, Z_U:-1)
row 2  (mu_DW:+1, m_pole:+1, lambda_pole:-1, rho_quarter:+1)
row 3  (source_norm:+1)
```

Intersected against the packet's twelve charged local action coefficients
(`zeta_F, g_A^-2, Z_U, kappa, alpha_II, beta_0, Lambda_bare, lambda_SW,
lambda_F, m_sel, mu_DW, m_2,eff`):

| row | charged coordinates touched | contributes |
|---|---|---|
| 1 | `kappa`, `Z_U` | 1 |
| 2 | `mu_DW` only (`m_pole`, `lambda_pole`, `rho_quarter` are not charged) | 1 |
| 3 | none — `source_norm` is not a charged coordinate | **0** |

**Rank 3 as a group, but only 2 directions act on charged coordinates.** The
naive reading would have booked 3. Reporting 2 per the run plan's kill condition
that a smaller-than-expected reduction is reported as found.

`m_R = sqrt(m_2,eff)*mu_DW` and `ell^2 = Z_U*kappa` are already recorded as
derived rather than independently charged, and are correctly not touched here.

## The largest quotient, and why it is blocked

The single biggest block in the ledger is the **provenance Yukawa**: `Y_K, Y_C`
in `M_3(C)`, charged at **36 real** — 43% of the whole count. In any theory of
this shape the physical content of a Yukawa pair is far smaller than its entry
count, because field redefinitions of the fermion multiplets act on it. That is
the classic reduction and it is where the money is.

**It cannot be computed yet.** The available redefinition group is determined by
the field space, and the field space is `SA-C1` — a `DECLARATION` row, explicitly
undecidable by the built structure, currently open between carrier B
(`ker Gamma`, index `-38`) and carrier A (full field space + BRST, index `-42`).
Different carriers admit different redefinitions, so the Yukawa quotient has a
different dimension on each branch.

The same dependency appears again at `SA-Y5`/`SA-Y4`: a derived `Z/3` is already
recorded as reducing nine complex couplings to three in the physical Yukawa,
which is a large reduction on one branch of a genesis choice and not on others.
Whether the packet's `36` and that `9 -> 3` describe the same object is **not
settled here** and must be Layer-0 typed before either is used; the names are
close enough to be a homonym hazard.

## What this means

**The free-parameter count is not a number. It is a function on the genesis
space.**

Write `N : V -> Nat`, taking a viable genesis configuration to the number of
continuous parameters that survive quotienting under it. Reporting a single `83`
treats `N` as a constant. It is not, because at least one quotient — the largest
one — has a dimension that depends on which `DECLARATION` branch is taken.

This composes directly with the Test A result:

- **Test A:** the genesis set does not constrain itself; the target does the
  constraining, and the target is booked nowhere.
- **Test B:** the continuous count cannot even be *computed* until the genesis is
  fixed.

Together they say the headline `83 real continuous parameters + 9 discrete
forks` is a conflation. It presents a continuous count and a discrete count as
two independent columns, when the first is a function of the second. The honest
object is a table of `N(g)` over the viable region, or at minimum `N` evaluated
at the branches the program actually leans toward.

**Consequence for the lane's own stated goal.** CB-D says the constraint column
is near-empty against an "83-plus-infinite-dimensional parameter column" and that
this gap "is the number this lane exists to drive down." If `N` is genesis-
dependent, that gap is also genesis-dependent, and driving it down means choosing
a branch first — which is the thing the program has been deferring.

## What was and was not done

- **Ranked:** the normalization rescaling quotient. Exact, integer, checkable.
- **Identified and blocked:** the field-redefinition quotient on the 36-real
  Yukawa block, blocked on `SA-C1`.
- **Not attempted:** gauge, functional, topology, domain and discrete-search
  quotients. Each needs construction that does not exist.
- **Not done:** any orbit-dimension computation. Nothing here required one, and
  nothing here may be cited as one.

## Fragility

- The `2` depends on the packet's charged-coordinate list being complete as
  transcribed. If `source_norm` or the pole variables are charged somewhere the
  transcription missed, the reduction is 3 rather than 2. The method survives;
  the number moves by one.
- The genesis-dependence of the Yukawa quotient is a **dependency argument**: the
  redefinition group depends on the field space, and the field space is
  undecided. It is not a computation of two different dimensions. Computing both
  branch dimensions would upgrade it from argument to result and is the obvious
  next step.
- `N : V -> Nat` is a proposed reframing. It is well-defined only if every
  quotient's dimension is genesis-determined; one genesis-independent quotient
  does not refute it, but a proof that all are genesis-independent would.

## Fences

No verdict, row, distance, revival trigger, residue count, quotient count, fork,
canon entry, lane, priority or queue rank moves. The ledger's residue line is
**unchanged**: this artifact does not renumber it, because a first-pass ranking
against one block is not a residue recount and the remaining quotients are
unranked.
