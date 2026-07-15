"""
W227 -- GAP-ANALYSIS-TO-UNCONDITIONAL register (machine-checkable INDEX).

This is a STEERING-REGISTER index check, not a computation. It asserts, as a single
machine-checkable record, the structure of the W227 register: the GOAL (unconditional +
one confirmed novel prediction), the two tracks, Track A's six conditionals (A1-A6) in
dependency order, Track B's single item (B1), the two standing monitors, the hourly
priority order, and the hygiene invariants (no canon/verdict movement; bar(b)/H59 OPEN;
count {1,3}).

Every fact asserted here is quoted from the register note and its cited source notes
(W219-W226 gauntlet; W201/W202/W203/W211/W154 + the paper-hardening report). No new
computation, no external import, no promotion.

Exit 0 on all-pass.

Run:  python tests/W227_gap_analysis_register.py
"""

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}   {detail}")
    if not ok:
        FAIL.append(name)


# ---------------------------------------------------------------------------
# THE GOAL
# ---------------------------------------------------------------------------
print("== GOAL ==")
goal = {
    "make_unconditional": True,          # close Track A conditionals
    "one_confirmed_novel_prediction": True,  # Track B
}
check("G1 goal has two legs: unconditional AND one confirmed novel prediction",
      goal["make_unconditional"] and goal["one_confirmed_novel_prediction"],
      "the two things needed to honestly clear the two-bar test")

two_bar_test = {
    "bar_a": "fewer flaws than every current explanation",
    "bar_b": "no more flaws but MORE unification",
}
check("G2 two-bar higher-order-truth test recorded", len(two_bar_test) == 2)

# GU is NOT proven; it SURVIVED a first non-naive gauntlet with gaps located.
gu_proven = False
gauntlet_survived_structure_intact = True
gaps_precisely_located = True
check("G3 posture: GU NOT proven; survived gauntlet, structure intact, gaps located",
      (not gu_proven) and gauntlet_survived_structure_intact and gaps_precisely_located,
      "truth-seeking: conditional/incomplete, not vindicated")

# ---------------------------------------------------------------------------
# THE GAUNTLET IT INDEXES (W219-W226)
# ---------------------------------------------------------------------------
print("\n== GAUNTLET (W219-W226) ==")
gauntlet_verdicts = {
    "W220-ppn": "SURVIVES",
    "W221-generation-count": "SURVIVES-WITH-A-GAP",
    "W222-sm-emergence": "SURVIVES",
    "W220-de / W226": "SURVIVES-WITH-TENSION",
    "W224-nielsen-ninomiya": "SURVIVES-BY-SMG",
    "W225-smg-realization": "OPEN-IN-THE-FIELD",
}
check("GA1 gauntlet spans W219-W226 with six recorded leg verdicts",
      len(gauntlet_verdicts) == 6, f"{sorted(gauntlet_verdicts)}")
check("GA2 no leg is a FALSIFIED (structure intact)",
      all(v != "FALSIFIED" for v in gauntlet_verdicts.values()),
      "credibility, NOT vindication")

# ---------------------------------------------------------------------------
# TRACK A -- the six conditionals in dependency order
# ---------------------------------------------------------------------------
print("\n== TRACK A (six conditionals) ==")
track_A = {
    "A1": {"name": "corrected reservoir-sign theorem (KEYSTONE)",
           "track": "paper-hardening", "hourly": "follow-ons"},
    "A2": {"name": "source-action nonlocal Z_U completion",
           "track": "constructive", "hourly": "LIVE"},
    "A4": {"name": "derive or replace the W154 identification",
           "track": "constructive", "hourly": "LIVE"},
    "A3": {"name": "dynamical SMG realization for the SO(10)-16 mirror",
           "track": "lattice-field-theory", "hourly": "toy/symmetry"},
    "A5": {"name": "pin (9,5) via the 2-primary Witten Z/2 anomaly",
           "track": "anomaly", "hourly": "targeted"},
    "A6": {"name": "characterize the count-import dependence honestly",
           "track": "characterization", "hourly": "honest-terminal"},
}
check("TA1 Track A has exactly six conditionals A1-A6",
      set(track_A) == {"A1", "A2", "A3", "A4", "A5", "A6"}, f"{sorted(track_A)}")

# A1 is the KEYSTONE and lives on the hardening track (not the hourly loop).
check("TA2 A1 is the KEYSTONE on the paper-hardening track (hourly = follow-ons only)",
      "KEYSTONE" in track_A["A1"]["name"] and track_A["A1"]["track"] == "paper-hardening"
      and track_A["A1"]["hourly"] == "follow-ons")

# The Godel one-bit framing was KILLED; no hourly run may use it as a premise.
godel_one_bit_killed = True
check("TA3 the Godel 'one undecidable bit' framing was KILLED this week",
      godel_one_bit_killed, "cone-of-positive-metrics vs admissible-C-gradings conflation")

# A2 + A4 are the constructive spine and the LIVE hourly work.
live_spine = [k for k, v in track_A.items() if v["hourly"] == "LIVE"]
check("TA4 A2 and A4 are the constructive spine and the LIVE hourly work",
      set(live_spine) == {"A2", "A4"}, f"live={sorted(live_spine)}")

# Dependency read: A1 gates A3; A2 feeds on A4.
deps = {"A3": ["A1"], "A2": ["A4"]}
check("TA5 dependency read: A1 gates A3; A4 feeds A2",
      deps["A3"] == ["A1"] and deps["A2"] == ["A4"])

# A6 may already be at its honest terminal state.
a6_maybe_terminal = True
check("TA6 A6 may already be at its honest terminal (say-so-precisely pass)",
      a6_maybe_terminal, "external Z/3 free-input downgrade vs structurally constrained")

# ---------------------------------------------------------------------------
# TRACK B -- one confirmed novel prediction
# ---------------------------------------------------------------------------
print("\n== TRACK B (one novel prediction) ==")
track_B = {
    "B1": {
        "job": "scan for GU's sharpest distinctive checkable novel prediction, then confront it",
        "generic_DE_too_weak": True,   # 'dynamical dark energy' is TOO GENERIC
        "priority": "SM-sector mass/coupling (Yukawa) relation checkable NOW",
        "backup": "distinctive DE feature (w(z) width ~1 e-fold / fsigma8 sign) for DESI DR3 / Euclid ~2027",
        "prioritize_today_over_2027": True,
    }
}
check("TB1 Track B has exactly one item, B1", set(track_B) == {"B1"})
check("TB2 B1 rejects the generic 'dynamical dark energy' claim as too weak",
      track_B["B1"]["generic_DE_too_weak"], "a phantom crossing is not uniquely GU")
check("TB3 B1 prioritizes a today-checkable SM Yukawa relation over the 2027 DE backup",
      track_B["B1"]["prioritize_today_over_2027"]
      and "Yukawa" in track_B["B1"]["priority"])

# ---------------------------------------------------------------------------
# MONITORS (standing; NOT hourly work)
# ---------------------------------------------------------------------------
print("\n== MONITORS (standing, not hourly) ==")
monitors = {
    "DE-amplitude-tripwire": {"source": "W226", "margin_2sigma": +1.11,
                              "resolves": "DESI DR3 / Euclid ~2027"},
    "SMG-dynamical-realization": {"source": "W225", "status": "OPEN-IN-THE-FIELD"},
}
check("M1 exactly two standing monitors recorded", len(monitors) == 2)
check("M2 DE tripwire monitor: W226 2-sigma margin +1.11, resolves ~2027",
      abs(monitors["DE-amplitude-tripwire"]["margin_2sigma"] - 1.11) < 1e-9
      and "2027" in monitors["DE-amplitude-tripwire"]["resolves"],
      "supersedes the W220 +0.032 central-value artifact")
check("M3 SMG monitor: W225 OPEN-IN-THE-FIELD",
      monitors["SMG-dynamical-realization"]["status"] == "OPEN-IN-THE-FIELD")

# ---------------------------------------------------------------------------
# HOURLY PRIORITY ORDER (the designation)
# ---------------------------------------------------------------------------
print("\n== HOURLY PRIORITY ORDER ==")
hourly_order = ["A2/A4", "A3", "A5", "A6", "B1"]
check("H_order1 hourly queue order is A2/A4 -> A3 -> A5 -> A6 -> B1",
      hourly_order == ["A2/A4", "A3", "A5", "A6", "B1"])
check("H_order2 A1 is NOT in the hourly queue (hardening track; follow-ons only)",
      not any("A1" in step for step in hourly_order))

# ---------------------------------------------------------------------------
# DECISIVE-UNDER-EITHER-OUTCOME
# ---------------------------------------------------------------------------
print("\n== DECISIVE UNDER EITHER OUTCOME ==")
decisive = {
    "close-a-conditional": "succeeds (unconditional) OR exposes a real hidden flaw",
    "the-prediction": "confirms (discriminating success) OR falsifies (GU wrong, cheaply)",
}
check("D1 each item is decisive whichever way it resolves", len(decisive) == 2)

# ---------------------------------------------------------------------------
# HYGIENE: no canon/verdict movement; bar(b), H59 OPEN; count {1,3}
# ---------------------------------------------------------------------------
print("\n== HYGIENE ==")
canon_moved = False
verdict_moved = False
bar_b_open = True
h59_open = True
count = {1, 3}
check("HY1 no canon/verdict/claim-status/posture movement",
      (not canon_moved) and (not verdict_moved), "steering register; exploration grade")
check("HY2 bar(b) and H59 stay OPEN", bar_b_open and h59_open)
check("HY3 count stays {1,3}", count == {1, 3})
uses_godel_claim = False
check("HY4 register uses no killed Godel / one-bit premise", not uses_godel_claim)

# ---------------------------------------------------------------------------
print("\n" + ("ALL PASS -- W227 register index consistent." if not FAIL
              else f"FAILURES: {FAIL}"))
raise SystemExit(1 if FAIL else 0)
