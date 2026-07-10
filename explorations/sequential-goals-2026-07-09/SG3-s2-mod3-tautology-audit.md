---
artifact_type: exploration
status: exploration
created: 2026-07-09
title: "SG3 -- closing S2's mod-3 tautology gap: derive the residue + a discriminating test"
grade: "COMPUTED (exact sympy). Epistemic-honesty / test-quality result. Internal. No scientific verdict change; recommends an honesty alignment of the RS-S2 doc language."
depends_on:
  - explorations/big-swing-2026-07-07/RS-S2-relative-index-nogo.md
  - explorations/big-swing-2026-07-07/BIG-SWING-RS-INDEX-STILL-GATED.md
  - tests/big-swing/rs_s2_relative_index_nogo.py
scripts:
  - tests/big-swing/sg3_s2_mod3_tautology_audit.py
---

# SG3 -- closing the S2 mod-3 tautology gap (synthesizer next-step #3, constructive horn)

## The swing

BIG-SWING-RS-INDEX downgraded route S2 from "all three legs THEOREM / universal no-go" to **PARTIAL**,
because its decisive Leg-B mod-3 sweep is a **tautology** with zero discriminating power. Next-step #3
asks to either **derive** the twisted-index formula (not assert it) and **replace** the
coefficient-divisible sweep with a discriminating test, **or** downgrade the S2 language. This goal
does the constructive horn.

## What was computed (`tests/big-swing/sg3_s2_mod3_tautology_audit.py`, exit 0)

Taking the stated spin index `ind_full = 12k + 16 m^2 d' - 2 sigma` (the RS operator itself remains
unbuilt; this is the stated index from the h2 canon pieces):

- **[A] The tautology, reproduced.** S2 sweeps `ind_full - (m^2 d' + sigma) == 0 (mod 3)` over random
  integers. The difference is `15 m^2 d' + 12 k - 3 sigma`; **every coefficient (15, 12, -3) is
  divisible by 3**, so the check is `0 == 0 (mod 3)` identically. Its 200 passes are circular -- they
  add no evidence for *why* that residue holds.
- **[B] The derivation.** Reducing `ind_full` mod 3 coefficient-by-coefficient (`16 == 1`, `-2 == 1`,
  `12 == 0`) **derives** `ind_full == m^2 d' + sigma (mod 3)` -- the correct residue, now derived from
  the stated index rather than asserted.
- **[C] The discriminating test.** Exact polynomial equality mod 3 against a panel of mutant residues
  (`m^2 d' + 2 sigma`, `2 m^2 d' + sigma`, `m^2 d'`, `sigma`, `d' + sigma`): the true residue PASSES,
  every mutant FAILS. (S2's random method does reject the mutants; its precise flaw is the *circular*
  confirmation of the true residue plus the *un-derived* formula, both fixed here.)
- **[D] What survives.** Carrier 3-inertness (every natively selected twist has `m^2 == 1 mod 3`, so
  the mod-3 class is import-carried), the discriminating control `O(3)` (`m^2 == 0`), and the
  double-import structure (`3 | ind` for all sections `<=> 3|m AND 3|sigma`) are **true** and
  independent of the tautology.

## Verdict

The underlying content **survives and is now derived**: `ind == m^2 d' + sigma (mod 3)`, carrier
3-inert, escape = double external import. But the **"universal no-go over all relative/equivariant/rank
invariants"** claim is **not established** (native-scope only), matching the synthesizer's PARTIAL.

**Recommendation (honesty alignment, not a verdict flip):** the `RS-S2-relative-index-nogo.md` "all
three legs THEOREM / no-go proven" framing should read as native-scope ("the located-carrier bridge is
not established and is arithmetically implausible via native data"), per the claim-status-consistency
rule. A dated alignment note is appended to that doc pointing to this certificate. No scientific
verdict changes: generation count stays OPEN (located, not forced).
