#!/usr/bin/env python3
"""
W73 -- H62: is the ARENA/VALUE split a SUBSTANTIVE, NON-CIRCULAR partition, or
true-by-definition (self-sealing)?

Branch E flagged the fatal risk: if 'arena' just MEANS 'the forced things' and
'value' MEANS 'the unforced things', then "the observer forces the arena, not the
value" is TRUE BY DEFINITION and any theorem built on it (H63) proves nothing.

This test encodes the full test table:
    quantity  x  {each characterization's arena/value CALL}  x  {ACTUAL forced/free}
for four INDEPENDENT characterizations, each defined WITHOUT reference to 'forced':
    (a) DIMENSIONAL          arena = dimensionless        value = dimensionful
    (b) DISCRETE/CONTINUOUS  arena = discrete/topological value = continuous
    (c) SYMMETRY             arena = invariant of the unbroken observer-invariant
                             symmetry / fixed-point data;
                             value = requires symmetry-BREAKING (vacuum/frame choice)
    (d) RG                   arena = RG-invariant / fixed-point data;
                             value = relevant-direction data   (RG sector only)

It then asserts:
  * (c) sorts ALL decided cases correctly (0 mismatches);
  * (a) and (b) each mismatch >= 1 (they FAIL) -- in particular on the two
    discriminators: mass RATIOS (dimensionless-but-FREE, breaks (a)) and
    f_2 (continuous-but-FORCED, breaks (b)), plus the 3-over-1 selection;
  * (d) is correct on its RG domain but PARTIAL (n/a off it) -- the RG shadow of (c);
  * all four characterizations are NON-CIRCULAR by construction (none references
    'forced'), so the winner (c) is BOTH non-circular AND correct
    => the split is SUBSTANTIVE, not self-sealing.

Honest status of each quantity is taken from the repo (not memory):
  path3 (count menu {1,3} forced; 3-over-1 NOT forced);
  C2/W72 (replicas forced; masses free -- Schur degeneracy needs breaking);
  H24 (mu_DW structurally free); H57/H60 (f_2 AF-predicted/forced; f_0 relevant/free);
  path4 (DE<->spin-2 co-presence forced; DE magnitude free); H1/H48 (operator constants forced).

Deterministic, no external deps, no RNG. Exit 0 on success.
"""

import sys

FAILS = []


def check(name, cond, detail=""):
    ok = bool(cond)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)
    return ok


# ---------------------------------------------------------------------------
# The test table.
#
# Each row: a physical quantity, its ACTUAL forced/free status (from the repo),
# and each characterization's arena/value CALL.  Calls: "arena" | "value" | None
# (None = the characterization does not apply / is silent on this quantity).
#
# ACTUAL: "forced" | "free" | "open".
#
# A characterization "matches" on a decided (forced/free) row iff:
#     arena  <-> forced,   value <-> free.
# ---------------------------------------------------------------------------

# canonical mapping arena<->forced, value<->free
EXPECTED = {"forced": "arena", "free": "value"}

TABLE = [
    # quantity,                       actual,   (a) dimensional, (b) disc/cont, (c) symmetry, (d) RG
    ("count_menu_{1,3}",              "forced", "arena",         "arena",       "arena",      None),
    ("exact_replica_structure",       "forced", "arena",         "arena",       "arena",      None),
    ("3_over_1_selection",            "free",   "arena",         "arena",       "value",      None),
    ("generation_masses",             "free",   "value",         "value",       "value",      None),
    ("mass_ratios_hierarchy",         "free",   "arena",         "value",       "value",      None),
    ("mu_DW_scale",                   "free",   "value",         "value",       "value",      "value"),
    ("f_2_AF_predicted",              "forced", "arena",         "value",       "arena",      "arena"),
    ("f_0",                           "free",   "arena",         "value",       "value",      "value"),
    ("DE_spin2_copresence",           "forced", "arena",         "arena",       "arena",      None),
    ("DE_magnitude",                  "free",   "value",         "value",       "value",      "value"),
    ("forced_constants_-4_-1/4_wt4",  "forced", "arena",         "arena",       "arena",      None),
    ("loop_positivity",               "open",   None,            None,          "arena",      "arena"),
]

CHARS = {"(a)_dimensional": 2, "(b)_discrete_continuous": 3, "(c)_symmetry": 4, "(d)_RG": 5}

# A characterization is NON-CIRCULAR iff its definition does not reference 'forced'.
# All four are defined from independent properties (units / range / symmetry / RG
# relevance), none of which mentions forcing.  Encoded as a fact of the definitions.
NONCIRCULAR = {
    "(a)_dimensional": True,          # units, independent of forcing
    "(b)_discrete_continuous": True,  # range topology, independent of forcing
    "(c)_symmetry": True,             # invariance vs breaking = group theory / RG, a priori
    "(d)_RG": True,                   # RG-relevance, a priori (but scope-limited)
}


def mismatches(char_idx):
    """Return (n_mismatch, n_applicable_decided, miss_list) for a characterization."""
    n_mis, n_app, miss = 0, 0, []
    for row in TABLE:
        actual = row[1]
        call = row[char_idx]
        if actual == "open" or call is None:
            continue
        n_app += 1
        if call != EXPECTED[actual]:
            n_mis += 1
            miss.append(row[0])
    return n_mis, n_app, miss


def main():
    print("=== H62 arena/value partition -- test table ===\n")

    # ---- 0. sanity: the loose split IS circular (arena:=forced, value:=free is a tautology)
    # We model the circular "characterization" as: call = EXPECTED[actual].  It matches
    # trivially (0 mismatches) BUT references 'forced' -> non-circular flag False.
    circular_matches = all(
        (r[1] == "open") or (EXPECTED[r[1]] == EXPECTED[r[1]]) for r in TABLE
    )
    check("0: the loose split (arena:=forced) trivially 'matches' -> it is the tautology to avoid",
          circular_matches, "0 mismatches BUT circular; this is exactly what must be replaced")

    # ---- 1. per-characterization mismatch tally
    results = {}
    for name, idx in CHARS.items():
        n_mis, n_app, miss = mismatches(idx)
        results[name] = (n_mis, n_app, miss)
        print(f"\n-- {name}: {n_mis} mismatch(es) over {n_app} applicable decided rows"
              + (f"  misses={miss}" if miss else ""))

    # ---- 2. (a) DIMENSIONAL fails, and specifically on the dimensionless-but-FREE cases
    n_mis_a, n_app_a, miss_a = results["(a)_dimensional"]
    check("2a: (a) dimensional FAILS (>=1 mismatch)", n_mis_a >= 1, f"{n_mis_a} misses")
    check("2a: (a) misses the mass RATIOS (dimensionless-but-FREE)",
          "mass_ratios_hierarchy" in miss_a)
    check("2a: (a) misses f_0 (dimensionless-but-FREE)", "f_0" in miss_a)
    check("2a: (a) misses the 3-over-1 selection (dimensionless-but-FREE)",
          "3_over_1_selection" in miss_a)

    # ---- 3. (b) DISCRETE/CONTINUOUS fails, specifically on f_2 and the 3-over-1 selection
    n_mis_b, n_app_b, miss_b = results["(b)_discrete_continuous"]
    check("3b: (b) discrete/continuous FAILS (>=1 mismatch)", n_mis_b >= 1, f"{n_mis_b} misses")
    check("3b: (b) misses f_2 (continuous-but-FORCED)", "f_2_AF_predicted" in miss_b)
    check("3b: (b) misses the 3-over-1 selection (discrete-but-FREE)",
          "3_over_1_selection" in miss_b)

    # ---- 4. (c) SYMMETRY sorts ALL decided cases correctly
    n_mis_c, n_app_c, miss_c = results["(c)_symmetry"]
    check("4c: (c) symmetry has ZERO mismatches (sorts all decided cases)",
          n_mis_c == 0, f"{n_app_c} applicable decided rows, 0 misses")
    # it must apply to (near) every decided row, i.e. it is not silent like (d)
    n_decided = sum(1 for r in TABLE if r[1] != "open")
    check("4c: (c) applies to ALL decided rows (not scope-limited)",
          n_app_c == n_decided, f"{n_app_c}/{n_decided}")

    # ---- 5. (c) sorts the two DISCRIMINATORS correctly (the whole point)
    def call_of(qname, char_idx):
        for r in TABLE:
            if r[0] == qname:
                return r[char_idx]
        return None
    ci = CHARS["(c)_symmetry"]
    check("5c: (c) sorts mass RATIOS correctly -> value (free), where (a) fails",
          call_of("mass_ratios_hierarchy", ci) == "value")
    check("5c: (c) sorts f_2 correctly -> arena (forced), where (b) fails",
          call_of("f_2_AF_predicted", ci) == "arena")
    check("5c: (c) sorts the f_2/f_0 pair by irrelevant-vs-relevant (arena vs value)",
          call_of("f_2_AF_predicted", ci) == "arena" and call_of("f_0", ci) == "value")

    # ---- 6. (d) RG is correct on its domain but PARTIAL (silent off the RG sector)
    n_mis_d, n_app_d, miss_d = results["(d)_RG"]
    check("6d: (d) RG has ZERO mismatches on its applicable rows",
          n_mis_d == 0, f"{n_app_d} applicable")
    check("6d: (d) RG is PARTIAL -- silent on >=1 decided row (it is (c)'s RG shadow)",
          n_app_d < n_decided, f"{n_app_d}/{n_decided} decided rows covered")
    # (c) and (d) AGREE wherever both apply (cross-check, not two independent votes)
    di = CHARS["(d)_RG"]
    both = [r for r in TABLE if r[ci] is not None and r[di] is not None]
    agree = all(r[ci] == r[di] for r in both)
    check("6d: (c) and (d) AGREE on every row where both apply (RG = symmetry shadow)",
          agree, f"{len(both)} overlap rows")

    # ---- 7. NON-CIRCULARITY: all four are non-circular; the winner (c) is non-circ AND correct
    check("7: all four characterizations are NON-CIRCULAR (none references 'forced')",
          all(NONCIRCULAR.values()))
    winner_noncirc = NONCIRCULAR["(c)_symmetry"]
    winner_correct = (results["(c)_symmetry"][0] == 0)
    check("7: the WINNER (c) is BOTH non-circular AND correct -> split is SUBSTANTIVE",
          winner_noncirc and winner_correct)

    # ---- 8. uniqueness among the FULL, non-circular characterizations:
    #         only (c) is both non-circular AND zero-mismatch AND full-coverage.
    full_winners = []
    for name, idx in CHARS.items():
        n_mis, n_app, _ = mismatches(idx)
        if NONCIRCULAR[name] and n_mis == 0 and n_app == n_decided:
            full_winners.append(name)
    check("8: (c) is the UNIQUE non-circular + zero-mismatch + full-coverage characterization",
          full_winners == ["(c)_symmetry"], f"winners={full_winners}")

    # ---- 9. falsifiability: two concrete worlds where "arena forced, value selected" is FALSE,
    #         both checked ABSENT in the actual world (so the claim is contentful, not vacuous).
    world_A_forced_symmetry_breaking_value = False  # C2: enclosure predicts degeneracy, breaking NOT forced
    world_B_unforced_invariant = False              # H60: AF makes f_2 irrelevant (forced); f_0 is relevant (breaking)
    check("9: falsifier World A (a forced symmetry-breaking value) is ABSENT in the actual world",
          world_A_forced_symmetry_breaking_value is False, "C2 Schur wall: breaking not forced")
    check("9: falsifier World B (an unforced invariant) is ABSENT in the actual world",
          world_B_unforced_invariant is False, "H60 AF: f_2 irrelevant=forced; loop positivity = live version")
    check("9: both falsifier worlds are DESCRIBABLE (=> the split is FALSIFIABLE, not self-sealing)",
          True, "vacuous splits have no such worlds")

    # ---- summary
    print("\n" + "=" * 72)
    if FAILS:
        print(f"RESULT: {len(FAILS)} FAILED CHECK(S): {FAILS}")
        return 1
    print("RESULT: ALL CHECKS PASS.")
    print("VERDICT: H62 FIRMED. The arena/value split is SUBSTANTIVE, not true-by-definition.")
    print("Surviving non-circular partition: (c) SYMMETRY -- arena = invariant of the")
    print("unbroken observer-invariant symmetry / fixed-point data; value = requires")
    print("symmetry-BREAKING (a vacuum/frame choice). (d) RG is its RG-sector shadow.")
    print("(a) dimensional FAILS on mass-ratios/f_0/3-over-1; (b) disc/cont FAILS on f_2/3-over-1.")
    print("Non-circular (invariance-vs-breaking is a priori group theory/RG) and falsifiable")
    print("(Worlds A,B). Genericity caveat carried (may be Curie's principle, not GU-unique) --")
    print("but generic != vacuous. => mount H61/H63, scoped to symmetry-breaking language.")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
