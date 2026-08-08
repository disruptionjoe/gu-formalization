---
artifact_type: exploration_result
created: 2026-08-08
status: MH9_MISSPECIFIED_AND_HALF_DONE__TIER0_BASE_FS_FLIP_COMPUTED__REGISTER_UNDERCOUNTS_COMPLETION_BY_8_TO_10X
run_id: GUH-20260808T060000Z-register-side-track
grade: "TWO RESULTS. (1) An exact certificate,
  tests/mh9_base_fs_indicator_horn_flip.py, green, integer-exact, residual 0.0 --
  the base Frobenius-Schur indicator flips between horns while the fibre does
  not. Preregistered before running. (2) A sampled classification of 29 unmarked
  grade-C/H register rows against their actual target surfaces, every target
  resolved by content. The extrapolated completion rate is an estimate and is
  reported as a range."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
priority_change: none
row_change: none
residue_touched: []
---

# M-H9 Tier 0, and what the register actually contains

## Part 1 — M-H9 is mis-specified, half done, and one bit is now computed

### It names the wrong module

M-H9's action reads "compute the ten indicators via the in-file Racah-Speiser
machinery; rerun under (7,7)". That machinery
(`tests/shiab_b5_observer_symbol_multiplicity_matrix.py`) exists and runs green,
but it is **complexified and signature-blind** — its own docstring fixes
`H_C = Spin(4,C) x Spin(10,C)`. It carries no conjugation, no real structure and
no pairing, so it cannot emit a Frobenius-Schur indicator.

And the two horns differ **only in the base**, `(3,1)` versus `(1,3)`: the DeWitt
fibre form is quadratic in `g`, so it stays `(6,4)` under `g -> -g`. Both horns
therefore share one complexification, and **rerunning that module under (7,7)
returns bit-identical output**. Taken literally, M-H9's stated action cannot
discriminate the fork.

The sign-carrying object is `C_perp = K . J_obs`, in
`tests/channel-swings/full20_dewitt_loop_transport_probe.py`.

### It is already half done

`full20_dewitt_loop_transport_probe.py`, committed 2026-07-30 and green, forces
**all ten `delta_e` equal** — Gamma-naturality plus the 136 written coefficient
intertwiners kill every relative freedom. So `k` was already restricted to
`{0,10}`: **endpoints only, derived on 2026-07-30.**

Both the improvement register and the Layer-0 fork registry still describe the
residual as eleven pairs. The fork registry's `named_resolver` note saying
"STATUS 2026-08-07: NOT EXECUTED" was written on 2026-08-07 **by this session**
and is corrected alongside this artifact. That is the fourth register item in two
days found partly-done-and-unmarked, and the only one where this session
amplified the stale claim rather than just finding it.

### The specification also needs restating, and this is load-bearing

`explorations/dc-h1-orbit-signs-monodromy-check-2026-08-04.md` shows that under
`C -> -C` the even and breaking subspaces exchange — `d -> 136 - d`, i.e.
`58 <-> 78` — and that this sign is a nontrivial holonomy class `w != 0` in
`H^1(F;Z/2)` **with no global section**. Only the unordered pair is
loop-invariant.

**So "(9,5) => (58,78)" as an absolute ordered claim is not well posed.** Within a
single signature the DeWitt loop already swaps the pair. M-H9's decisive quantity
is the **relative** sign between horns, not either endpoint.

Independently, that same file identifies the firing `Z/2` as the **O(1) time
reflection** of the Lorentz stabiliser — which is exactly what `(3,1) <-> (1,3)`
changes. Two unrelated routes landing on the same object is the reason to take
the mechanism seriously and the reason to state it relatively.

### Tier 0 result

`tests/mh9_base_fs_indicator_horn_flip.py`, preregistered before running:

```text
BASE (the only structure differing between horns)
  (3,1)  base of the (9,5) horn : J.conj(J) = +1 I   real type      residual 0.00e+00
  (1,3)  base of the (7,7) horn : J.conj(J) = -1 I   quaternionic   residual 0.00e+00

FIBRE (control, asserted unchanged)
  (6,4) DeWitt fibre            : J.conj(J) = +1 I   unchanged      residual 0.00e+00

RELATIVE base sign: OPPOSITE -> endpoint flip
VERDICT: BASE-FS-INDICATOR-FLIPS-BETWEEN-HORNS__FIBRE-UNCHANGED
```

Independently corroborated by `tests/channel-swings/p77_real_index_twin.py`,
which certifies `Cl(3,1) = M(4,R)` real and `Cl(1,3) = M(2,H)` quaternionic, and
`Cl(6,4) = M(32,R)` unchanged.

**Combined with the 2026-07-30 all-ten-equal result, the endpoint-flip mechanism
is confirmed.** A single global base sign applies to all ten edges, so `k` flips
`0 <-> 10` and the pair flips `(58,78) <-> (78,58)` between horns.

### What is still owed

Tier 1: propagate the base indicator through the actual `C_perp` and the 136
coefficient intertwiners under `(1,3)`. **This requires re-deriving
`mixed_rotation()`'s hardcoded `timelike_leg = 3`** — under `(1,3)` the timelike
leg is index 0, and relabelling rather than re-deriving produces an artefact
sign. Nothing here settles `SIGNATURE-AMBIENT`, moves a ledger row, or bears on
the generation count.

## Part 2 — the register undercounts completed work by roughly 8-10x

29 unmarked grade-C and grade-H rows from Q1/Q2 were classified against their
actual target surfaces, resolving every target **by content** because the
register's line references are stale in every case checked.

```text
ALREADY-SATISFIED : 23 / 29  (79%)   -- 18 clean, 5 with a named residual
STILL-LIVE        :  6 / 29  (21%)   -- four of the six are partial
CANNOT-TELL       :  0 / 29
```

Corroboration, not coincidence: **20 of the 23 satisfied rows carry a dated
`2026-08-03` correction stamp**, and six name their own register ID or audit
finding inside the fix text (`register P-C2/M-H6`, `register P-C3 and P-H8`,
`register M-C2`, `register M-H16`, `(P-H12)`, `audit F-02`). **The work was done
under the register and never written back to the rows.**

Blending Q1/Q2 at ~83% true completion with a four-item Q3 spot check at ~35-40%
gives **roughly 67-81 of 145 actually done — a true rate near 45-55%, against
the 5.5% the register displays.**

This reframes the side track opened at
`lab/process/runs/GUH-20260808T060000Z-register-side-track/`. The job is not
"work 137 items". It is **write back ~35 rows from evidence already in the tree,
then work the genuine remainder**, which is a much smaller and differently-shaped
task.

### The six still-live items, ranked

1. **`P-H20` — worse than the row claims, and the only one in the sample that is.**
   The register says 12 canon docs are missing from the Current Research Map; the
   actual count is **25+ of 57**. `RESEARCH-STATUS.md:738` still routes readers to
   `lab/active-research/signed-readout/` for a theorem that has been
   `status: canon` since 2026-07-03. The repo's own index misdescribes its own
   canon, on the primary status surface. Cheap, and highest value.
2. **`P-H9` — a real verification hole.** A paper certificate is genuinely unswept
   by any harness root, and `process_gates/reproduce_harness_scope_audit.py` reads
   the harness's own `PAPER_CERT_DIRS` as ground truth. **A self-certifying gate
   over an unreachable certificate** is exactly the failure class the register
   exists to kill.
3. **`P-H5` — a non-enforcing receipt behind a verified label.**
   `ResidualSelectionAxioms.lean` exits 0 even with `sorryAx`, sits outside the
   default target, and nothing greps its output — while being advertised
   `LEAN-VERIFIED`.
4. **`M-H15` — partial propagation, the most dangerous state.** The corrected
   coefficient `493/2419200` landed in two places, but the MOVE-1 owner cert still
   reads `13/37800` unannotated and `DERIVATION-PROGRESS` carries it bare. The
   correction exists, so nobody re-checks.
5. **`P-H6`** — no dated baseline receipt, so an outside RED is undiagnosable. The
   register already knows (`:519-521`): tracked debt, not oversight.
6. **`P-C1`** — lineage is on `main`; what remains is a placeholder `REVIEW_SHA`
   in the referee packet and an untracked `main.pdf`.

### Fence on Part 2

"Satisfied" means **the stated defect is no longer present at the named surface**,
not that the row closes with zero further edits — five of the 23 carry residuals.
The 45-55% figure is an extrapolation from a 29-row sample plus a four-row Q3
spot check, and is reported as a range for that reason. **No register row is
marked done on the strength of this artifact**; the write-back pass should
re-confirm each row it closes, using the evidence recorded here as its starting
point rather than its authority.
