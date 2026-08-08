---
artifact_type: method_improvement
created: 2026-08-07
status: FIVE_CONSTRUCTION_IMPROVEMENTS__LARGEST_BLOCK_CHARGED_BY_DEFAULT_NOT_CLOSED__TARGET_LEDGER_OPENED__COLLISION_REGISTER_OPENED
grade: "METHOD plus two small registers. Sections 1, 2 and 3 are method statements
  supported by the reduction history already in the repository. Section 4 books
  four target impositions identified in the 2026-08-07 Test A run. Section 5 is a
  symbol-collision register verified by direct search. No physics is computed
  here and nothing in this file is a result."
ledger: lab/process/conditional-physics-ledger-v0.39.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
priority_change: none
queue_change: none
row_change: none
residue_touched: []
follows:
  - explorations/declaration-viable-region-2026-08-07.md
  - explorations/quotient-ranking-first-pass-2026-08-07.md
---

# Building the conditional geometry faster and more precisely

Five improvements, from the 2026-08-07 Test A/Test B runs. Aimed at construction
speed and precision only. Nothing here moves a row.

## 1. Carry the genesis tuple symbolically, as CB-D already carries `U1..U18`

CB-D's central technique is to carry the unbuilt action's loads **symbolically**
as `U1..U18` so downstream clusters can compute without waiting for values. That
technique is currently applied one level too low.

Test B showed the continuous parameter count is not a number but a function
`N : V -> Nat` on the genesis space, because at least one quotient's dimension
depends on which `DECLARATION` branch is taken. Today that reads as a blocker:
"we cannot compute until `SA-C1` is decided."

**It is not a blocker if the genesis tuple is carried symbolically too.** Write
the construction as a function of `g`, evaluate at the branches, and let
contradictory branches self-eliminate. Test A bounded the space: `1536`
configurations coarsely, `96` after target imposition. Ninety-six is tractable.

This converts branch choice from a decision that is deferred into a computation
that is run. It is the single largest available speedup and it requires no new
technique — only applying the lane's own existing one at the level above.

## 2. Hunt locks, not derivations

The reduction history of this program is unambiguous:

| reduction | mechanism |
|---|---|
| four sign bits -> one (`SRC-COH-1` co-flip) | proved co-variation |
| `83 -> 81` (2026-08-07, Test B) | ranked a rescaling quotient |
| nine complex -> three (`SA-Y4` `Z/3` texture) | a grading symmetry |

**No parameter has ever been removed from this ledger by deriving a value.**
Every reduction on record came from proving that directions cannot vary
independently.

A quotient and a co-flip are the same operation at different types — one
continuous, one discrete. Both say "these directions are not separately free."
Both reduce the count **without deciding any physics**, which means they cannot
be wrong about physics; the worst case is that the lock fails to exist.

The conditional lane is currently organized around imposing downstream
requirements and propagating back. That produces `OVER-DETERMINED` rows, which
are valuable. But lock-hunting is cheaper per unit of count reduction and carries
strictly less risk. It should be a standing channel activity, not an incidental
by-product.

## 3. The largest block is charged BY DEFAULT, not by a proved absence of quotient

The provenance Yukawa (`Y_K, Y_C in M_3(C)`, 36 real) is 43% of the continuous
count and looks like the obvious place for a large field-redefinition quotient.

Three statuses must be kept apart here, and collapsing them is easy:

1. **CLOSED — importing the flavor quotient.** The unified packet states that
   `Y_K, Y_C` "act on the three **provenance summands**. They are **not
   generation matrices**. The full `3x3` matrices are charged because the older
   `Z/3` texture **cannot be imported** after the multiplicity/index Layer-0
   correction." Standard flavor-redefinition counting does not transfer, and the
   `9 -> 3` `Z/3` reduction applying to `SA-Y4`'s physical Yukawa is a
   **different object**. Reasoning from "Yukawa matrices always have a big
   redefinition quotient" imports a homonym. This disqualification is correct.
2. **NOT ESTABLISHED — that the block admits no quotient.** The packet
   disqualifies one *candidate import*. It does not report a search.
3. **ACTUAL STATUS — charged by default.** Direct search finds **no artifact that
   has ever looked for a symmetry acting on the provenance summands**. Every
   in-repo mention of them is either the count row using them as an input or a
   warning against identifying them with generations.

**This is the over-fencing half of the two-sided charge.** Rigor correctly
disqualified an import, and the disqualification was then read as a quotient
result. Under §2 — locks are the only mechanism that has ever reduced this
ledger — the largest block in the count has never had a lock search at all.

**Why it has not been asked, and why §1 is its prerequisite.** The provenance
decomposition plausibly depends on the field-space declaration, which is
`SA-C1` — an open `DECLARATION` row. If so, the symmetry question is
genesis-dependent in exactly the `N(g)` sense Test B found, and therefore
**unaskable branch-independently**. The lane has been avoiding branch commitment,
so the question has stayed invisible rather than been rejected.

Carrying `g` symbolically (§1) makes it askable on both branches at once. That
composes the three improvements into one path rather than three observations:
**carry `g`, then run the lock search §2 prescribes, on the largest block §3
identifies.**

Whether the summands carry their own symmetry is the highest-value open lock in
the ledger by block size, and it is open — not closed.

## 4. Target-imposition ledger — opened here, four entries

Test A found that the genesis set does not constrain itself: zero of the five
named tensions exclude any genesis option, and the entire `4.00`-bit reduction
from `1536` to `96` comes from imposing target physics.

Imposing the target is legitimate — this is *conditional* geometry and
conditioning is the method. The defect is that impositions are unbooked, which is
what makes `P1/P2/P3` uninformative: they count slots for imported *facts* while
the imported *requirements* are counted nowhere.

**Standing rule proposed: never impose silently. Book every imposition.**

| # | imposition | genesis rows it fixes | bits |
|---|---|---|---:|
| TI-1 | the action must count-select at all | `SA-C1` -> carrier B | 1 |
| TI-2 | three generations | `SA-C3` -> rank 3 | 1 |
| TI-3 | same-chirality masses are wanted | `SA-Y8` -> spurion supplied | 1 |
| TI-4 | UV completeness (not finite-`Lambda` EFT) | `SA-U5` -> guardian required | 1 |
| | | **total** | **4** |

`SA-Y2`'s `k = 0` "for mass generation" is a fifth imposition but is not counted
here, because the `Lambda^k` choice was already excluded from the free count in
the Test A tabulation rather than charged and then removed. It must not be
double-booked.

Any future artifact that reduces the genesis space must add its imposition to
this table or state that it used none.

## 5. Symbol-collision register — five families, verified

Four homonyms surfaced in a single day of work, and one would have inverted a
conclusion. `GEOMETER-VS-PHYSICS-OBJECTS.md` governs object identity in
reasoning; it does not govern **symbol naming**, and these are naming collisions.

| symbol | distinct senses in use |
|---|---|
| `sigma` | `U7` the orientation `Z/2`; `sigma_A` the 12-real spurion block; `sigma_c` the `U12` compensator ghost; the spinor adjoint in `beta_S sigma + sigma^dagger beta_S`; statistical standard deviation ("3-sigma") |
| `tau` | `U8` the count datum; `tau_C` the charge-conjugation transpose sign |
| `eps` / `epsilon` | the transmitted orientation in `CH-REC`; `epsilon_C` the charge-conjugation sign; `epsilon_IG`; the primitive epsilon of the preboundary work |
| `D1` / `D2` | `D1^ext`/`D2^ext` (orientation, count) vs `D1^dom`/`D2^dom` (endpoint relation, asymptotic domain) — already recorded by CB-D |
| "the Shiab" | canon `Omega^2 (x) S -> Omega^1 (x) S` vs K77 `Omega^2(ad) -> Omega^13(ad)` — already recorded by CB-D |

**The sharpest case: `sigma` and `tau` are the names of the two external data
(`U7`, `U8`), and both collide with charge-conjugation-sector symbols.** The two
most load-bearing imports in the program carry overloaded names.

**Proposed precision rule:** a symbol entering a construction must be
disambiguated at first use in that artifact. And a bare token search is not
evidence — the `sigma` search that motivated this register returned four
confident hits, all false, most of them error bars.

## Fences

No verdict, row, distance, revival trigger, residue count, quotient, fork, canon
entry, lane, priority or queue rank moves. Sections 1-3 are method proposals, not
ratified process. Sections 4 and 5 open registers with their initial entries; the
target-imposition table is not claimed complete, and the collision register is
what one day's work surfaced rather than an exhaustive scan.
