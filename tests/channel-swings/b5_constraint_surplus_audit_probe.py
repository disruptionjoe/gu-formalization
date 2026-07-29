#!/usr/bin/env python3
r"""
B5 CONSTRAINT-SURPLUS AUDIT.

Preregistered in explorations/prereg-b5-constraint-surplus-audit-2026-07-29.md.

Computes whether POSITING the B5 phase residual is a TEST or a FIT, by measuring

    surplus = (independent constraints expressible on the residual)
              - (free parameters of the residual)

Positive surplus: success was not guaranteed, so a surviving posit is evidence.
Zero or negative: accommodation with freedom to spare.

FREE-PARAMETER SIDE is exact and inherited from the two prior runs: ten
antilinear phases span 2^10 assignments whose entire effect on the real
coefficient dimension is a function of the signed sum -> 11 observable values,
and nothing in the ledger orients any of the ten.

CONSTRAINT SIDE uses a DECLARED PROXY: a FORCED row is potentially expressible
on the residual iff its cited test shares certified objects with the B5
observer-symbol ledger.  Sharing no objects means no bridge exists.  This is a
proxy for inexpressibility, NOT a proof of it, and is reported as such.

Deterministic, foreground, stdlib only, no writes, no network, no randomness.
EXIT 0 = ran and all controls passed; the PRINTED findings are the result.
"""
from __future__ import annotations

import os
import re
import sys
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "tests"))

import shiab_b5_observer_symbol_multiplicity_matrix as matrix  # noqa: E402

FAILURES: list[str] = []


def check(label: str, condition: bool) -> None:
    if condition:
        print(f"PASS: {label}")
    else:
        FAILURES.append(label)
        print(f"FAIL: {label}")


print("=" * 74)
print("B5 CONSTRAINT-SURPLUS AUDIT  --  is positing the residual a test or a fit?")
print("=" * 74)

# ------------------------------------------------------ free-parameter side
print("\n[P1] free-parameter side (kill condition 1)")
observable = {68 + sum(s) for s in product((-1, +1), repeat=10)}
check("1024 assignments", 2 ** 10 == 1024)
check("11 observable values", len(observable) == 11)
FREE_OBSERVABLE = len(observable)
print(f"  underlying assignments : 1024 (10 free signs)")
print(f"  observable values      : {FREE_OBSERVABLE} (the signed sum)")

# ------------------------------------------------- certified object inventory
print("\n[P2] certified B5 ledger object inventory")
# DISTINCTIVE objects only.  Provenance letters ("S", "X") and two-character
# h_types ("Lp", "Rm") occur as ordinary identifiers in unrelated files and
# produce false positives -- control N2 caught exactly that.  Require length
# >= 3 so a match means the file genuinely references a B5 ledger object.
B5_OBJECTS = {
    name for name in
    ({slot.h_type for slot in matrix.SLOTS} | set(matrix.TYPES.keys()))
    if len(name) >= 3
}
B5_OBJECTS |= {slot.name for slot in matrix.SLOTS}  # full colon-qualified names
check("ledger exposes a nonempty object inventory", len(B5_OBJECTS) > 0)
check("no single/two-character objects survive the distinctiveness filter",
      all(len(n) >= 3 for n in B5_OBJECTS))
print(f"  distinctive B5 objects: {len(B5_OBJECTS)}")

B5_TEST_TOKENS = {"shiab_b5", "observer_symbol", "krein_mirror_orbit",
                  "native_packet"}

# ------------------------------------------------------- the eight FORCED rows
FORCED = {
    "SA-Y1": ["tests/yukawa-scoping/yukawa_trilinear_channels.py"],
    "SA-Y7a": ["tests/W76_H64_mass_selection_swing.py"],
    "SA-G9": ["tests/wave22/H10_ppn_weak_field.py"],
    "SA-C2": ["tests/wave17/H40_terminal_sourceaction.py",
              "tests/wave35/source_action_carve.py"],
    "SA-C4": [],   # spec: named unbuilt, no test exists
    "SA-U1": ["tests/W48_H59_krein_loop_positivity_gate.py",
              "tests/W119_h59_frg_krein_negative_ratio.py"],
    "SA-U3": [],   # spec: the bound's derivation is itself open
    "SA-U4": [],   # spec: literature-anchored branch elimination
}

TOKEN = re.compile(r"[A-Za-z_][A-Za-z_0-9+\-]*")


def objects_in(path: str) -> set[str]:
    full = os.path.join(REPO, path)
    if not os.path.exists(full):
        return set()
    with open(full, "r", encoding="utf-8", errors="ignore") as fh:
        text = fh.read()
    toks = set(TOKEN.findall(text))
    hits = toks & B5_OBJECTS
    if any(t in text for t in B5_TEST_TOKENS):
        hits.add("<imports-B5-ledger>")
    return hits


def classify(row: str, tests: list[str]) -> tuple[str, set[str]]:
    if not tests:
        return "OUTSIDE (no test exists)", set()
    shared: set[str] = set()
    for t in tests:
        shared |= objects_in(t)
    if shared:
        return "EXPRESSIBLE", shared
    return "OUTSIDE (no shared object)", set()


print("\n[CONSTRAINT SIDE] expressibility of each FORCED row on the residual")
expressible: list[str] = []
for row, tests in FORCED.items():
    verdict, shared = classify(row, tests)
    if verdict == "EXPRESSIBLE":
        expressible.append(row)
        detail = f" via {sorted(shared)[:4]}"
    else:
        detail = ""
    print(f"  {row:7s}: {verdict}{detail}")

# ------------------------------------------------------ N1 / N2 planted rows
print("\n[N1/N2] planted rows must classify correctly (kill condition 2)")
planted_yes, _ = classify(
    "PLANTED-YES", ["tests/shiab_b5_krein_mirror_orbit_reduction.py"])
planted_no, _ = classify(
    "PLANTED-NO", ["tests/oq_rk1_cl95_explicit_rep.py"])
check("planted B5-citing row classifies EXPRESSIBLE",
      planted_yes == "EXPRESSIBLE")
check("planted unrelated row does not classify EXPRESSIBLE",
      planted_no != "EXPRESSIBLE")
print(f"  planted-yes -> {planted_yes};  planted-no -> {planted_no}")

# ------------------------------------------------------------------- verdict
print("\n" + "=" * 74)
if FAILURES:
    print(f"CONTROLS FAILED: {FAILURES}")
    print("RESULT: VOID.")
    sys.exit(1)

n_expr = len(expressible)
surplus = n_expr - 1  # 1 free observable parameter (the signed-sum integer)

if n_expr < 2:
    verdict = "SURPLUS-UNCOMPUTABLE"
elif surplus > 0:
    verdict = "SURPLUS-POSITIVE"
else:
    verdict = "SURPLUS-NEGATIVE"

print(f"VERDICT: {verdict}")
print("=" * 74)
print(f"\n  expressible FORCED rows : {n_expr} of 8  {expressible}")
print(f"  free parameters         : 1 observable integer (11 values)")
print(f"  surplus                 : {surplus}")

if verdict == "SURPLUS-UNCOMPUTABLE":
    print(
        "\nREADING.  The meter reads UNKNOWN, not LOW.  Joe's argument stands\n"
        "untouched: under genuine surplus constraint a posit IS a test, and the\n"
        "orthodox 'shaped to fit teaches nothing' does not apply.  What this run\n"
        "shows is that the surplus cannot be COMPUTED yet, because almost no\n"
        "FORCED row is expressible on the same objects as the residual.\n"
        "\nSo the blocker on positing is not epistemic.  It is a MISSING BRIDGE.\n"
        "The reopener is precise and buildable: make ONE forced row expressible\n"
        "against the phase sum.  That single bridge converts the posit from an\n"
        "unmeasurable move into a measurable test."
    )
print(
    "\nPROXY LIMIT, BINDING: object-sharing is a proxy for expressibility, not a\n"
    "proof of inexpressibility.  A row classified OUTSIDE may still constrain\n"
    "the residual through a bridge nobody has built.  This run does not close\n"
    "any row; it reports which have no bridge TODAY."
)
print(
    "\nEARNS: nothing frozen, no phase selected, no operator built, no\n"
    "claim/canon/verdict/count/priority/posture movement."
)
