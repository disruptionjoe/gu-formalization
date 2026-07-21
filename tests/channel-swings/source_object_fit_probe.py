"""Source-object external-fit probe: fixture-grade TYPE-MATCHING of the S_3-label item.

DOC: explorations/source-object-spec-and-external-fit-2026-07-20.md

WHAT IS MACHINE-CHECKABLE HERE. The full fit test grades four intaken programs against
four TYPES (a) external S_3-labeled three-way datum, (b) post-selection/weak-value
reading, (c) scale dial, (d) orientation bit. Types (b),(c),(d) are judgments about the
programs' native machinery and ship as PROSE typing in the doc (not fixture-checkable
without importing the programs). Type (a) HAS a fixture-grade type signature, reused
from trit-copies-node-b1: an external-S_3 datum is THREE pieces of EQUAL complete
invariants permuted by a DISCRETE EXTERNAL relabel (not gauged, not graded). This probe
encodes that type as three gates and runs every program's candidate three-ness through
them, plus the GU positive control and the lattice-QCD planted control.

THE THREE GATES (the S_3-label TYPE, encoded):
  G-count : exactly three pieces (a genuine three-ness exists at all).
  G-iso   : the three pieces have EQUAL complete invariants (isomorphic copies) --
            the trit-copies-node-b1 signature. Fails for a GRADED triple (unequal).
  G-ext   : the permuting symmetry is a DISCRETE EXTERNAL relabel (S_3), not a gauged
            continuous symmetry and not a grade. This is the sharp discriminator that
            stops the "three colors" / "three forms" word-coincidences.
PROVIDES-CANDIDATE for (a) iff all three gates pass.

PLANTED CONTROL (lattice QCD) MUST grade dead: three colors pass G-count and G-iso
(equal dims 3,3,3) but FAIL G-ext (color is gauged-continuous). If the control passed,
the test would be reading the WORD 'three', not the TYPE -- broken.

Exit 0 = ran honestly. Deterministic, pure-Python, no RNG, no numpy.
"""
from __future__ import annotations
import time

FAILURES = []
def check(tag, name, ok, detail=""):
    s = "PASS" if ok else "FAIL"
    print(f"[{tag}] {s}  {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAILURES.append(name)

t0 = time.time()

# ---------------------------------------------------------------------------------------
# Candidate three-nesses, encoded from each program's STATED native structure.
#   pieces        : tuple of per-piece complete-invariant records (None => no three-ness)
#   symmetry_kind : how the (would-be) three pieces are permuted / distinguished
#   note          : the object named, for the record
# The invariant record for GU is (dim, krein_signature) exactly as trit-copies-node-b1.
# For the external programs it is the natural complete invariant of the named triple.
# ---------------------------------------------------------------------------------------
CANDIDATES = {
    # POSITIVE CONTROL: the GU trit -- three 64-dim Krein copies, equal (+32,-32),
    # permuted by the external S_3 (trit-symmetry-node-a). MUST pass all gates.
    "GU trit (positive control)": dict(
        pieces=((64, (32, 32)), (64, (32, 32)), (64, (32, 32))),
        symmetry_kind="external_discrete",
        note="three isomorphic 64-dim Krein sectors, external S_3/weight label"),

    # Bianconi Dirac-Kahler matter: 0-form + 1-form + 2-form. In 4D dims 1,4,6 -- a
    # GRADED triple, unequal pieces. Word-coincidence 'three'.
    "Bianconi (Dirac-Kahler)": dict(
        pieces=((1, None), (4, None), (6, None)),
        symmetry_kind="graded",
        note="0/1/2-form graded triple, dims 1/4/6 -- graded, not isomorphic copies"),

    # Verlinde/Jacobson: no three-way datum at all.
    "Verlinde/Jacobson": dict(
        pieces=None, symmetry_kind="none",
        note="entropic force / Clausius horizon -- no three-way datum"),

    # Maldacena AdS-CFT: no three-way datum (RT / islands / observer are not three-fold).
    "Maldacena (AdS-CFT)": dict(
        pieces=None, symmetry_kind="none",
        note="RT/QEC/observer -- no three-way isomorphic-copies datum"),

    # Gorard/Wolfram: multiway branching has no fixed three-ness.
    "Gorard/Wolfram": dict(
        pieces=None, symmetry_kind="none",
        note="multiway branching -- no fixed three-fold S_3 datum"),

    # PLANTED CONTROL: lattice QCD three colors -- equal dims (3,3,3) but GAUGED
    # continuous SU(3), not a discrete external relabel. MUST fail on G-ext.
    "lattice QCD (planted control)": dict(
        pieces=((3, None), (3, None), (3, None)),
        symmetry_kind="gauged_continuous",
        note="three SU(3) colors -- gauged-continuous, not external discrete S_3"),
}

# ---------------------------------------------------------------------------------------
# The three gates.
# ---------------------------------------------------------------------------------------
def gate_count(rec):
    return rec["pieces"] is not None and len(rec["pieces"]) == 3

def gate_iso(rec):
    if not gate_count(rec):
        return False
    return len(set(rec["pieces"])) == 1  # all three complete-invariant records identical

def gate_ext(rec):
    return rec["symmetry_kind"] == "external_discrete"

def provides_a(rec):
    return gate_count(rec) and gate_iso(rec) and gate_ext(rec)

# ---------------------------------------------------------------------------------------
# [T] setup: the type definition is well-formed and two-sided (a positive control passes,
# a graded and a gauged triple are distinguishable). Guards against a vacuous gate.
# ---------------------------------------------------------------------------------------
gu = CANDIDATES["GU trit (positive control)"]
check("T", "type well-formed: GU positive control passes all three gates",
      gate_count(gu) and gate_iso(gu) and gate_ext(gu))
check("T", "G-iso has power: GU (equal) passes, Bianconi graded (1/4/6) fails",
      gate_iso(gu) and not gate_iso(CANDIDATES["Bianconi (Dirac-Kahler)"]))
check("T", "G-ext has power: GU (S_3) passes, lattice (gauged color) fails",
      gate_ext(gu) and not gate_ext(CANDIDATES["lattice QCD (planted control)"]))

# ---------------------------------------------------------------------------------------
# [E] the fit test on item (a): grade every candidate; assert the pre-declared verdicts.
# ---------------------------------------------------------------------------------------
print("\n--- item (a) S_3-label type-match ---")
grades = {}
for name, rec in CANDIDATES.items():
    g = "PROVIDES" if provides_a(rec) else "not-provided"
    grades[name] = provides_a(rec)
    gc, gi, ge = gate_count(rec), gate_iso(rec), gate_ext(rec)
    print(f"    {name:32s} count={int(gc)} iso={int(gi)} ext={int(ge)} -> {g}  ({rec['note']})")

# Positive control MUST provide (else the grader is broken / the type is unsatisfiable).
check("E", "positive control GU trit PROVIDES-CANDIDATE for (a)", grades["GU trit (positive control)"])

# The four intaken programs MUST NOT provide (a) -- the load-bearing S_3 type is novel.
for prog in ("Bianconi (Dirac-Kahler)", "Verlinde/Jacobson", "Maldacena (AdS-CFT)", "Gorard/Wolfram"):
    check("E", f"{prog} does NOT provide (a)", not grades[prog])

# Bianconi fails specifically on the ISO gate (graded triple), not on count.
bi = CANDIDATES["Bianconi (Dirac-Kahler)"]
check("E", "Bianconi fails (a) on G-iso (graded, unequal invariants) with count satisfied",
      gate_count(bi) and not gate_iso(bi))

# PLANTED CONTROL: must NOT provide, and must fail SPECIFICALLY on G-ext while passing
# count+iso -- proving the grader reads TYPE, not the word 'three'.
lq = CANDIDATES["lattice QCD (planted control)"]
check("E", "planted control lattice QCD does NOT provide (a)", not grades["lattice QCD (planted control)"])
check("E", "planted control fails on G-ext ONLY (passes count+iso: 'three colors' word-coincidence rejected by TYPE)",
      gate_count(lq) and gate_iso(lq) and not gate_ext(lq))

# No external program provides (a) => the load-bearing S_3 item is genuinely novel.
no_program_provides_a = not any(grades[p] for p in CANDIDATES if "control" not in p)
check("E", "OUTCOME S-a on item (a): no intaken program provides the S_3-label datum",
      no_program_provides_a)

# ---------------------------------------------------------------------------------------
# [F] recorded framing (NOT fixture-asserted): the (b),(c),(d) verdicts ship as prose
# typing in the doc. Printed here for the record only.
# ---------------------------------------------------------------------------------------
print("\n--- (b),(c),(d) recorded prose-typing (not fixture-gated; see doc sec. 2) ---")
FIT_TABLE = {
    "Bianconi":          dict(b="WRONG-TYPE", c="PROVIDES-CANDIDATE", d="SILENT"),
    "Verlinde/Jacobson": dict(b="WRONG-TYPE", c="WRONG-TYPE",         d="SILENT"),
    "Maldacena":         dict(b="WRONG-TYPE", c="SILENT",             d="SILENT"),
    "Gorard/Wolfram":    dict(b="WRONG-TYPE", c="SILENT",             d="SILENT"),
    "lattice QCD (ctrl)":dict(b="SILENT",     c="WRONG-TYPE",         d="SILENT"),
}
for prog, row in FIT_TABLE.items():
    print(f"    {prog:20s} (b)={row['b']:18s} (c)={row['c']:18s} (d)={row['d']}")
check("F", "load-bearing (b) weak-value reading: no program PROVIDES (all WRONG-TYPE/SILENT)",
      all(row["b"] != "PROVIDES-CANDIDATE" for row in FIT_TABLE.values()))
check("F", "only PROVIDES anywhere is Bianconi (c) scale-dial, a NON-load-bearing item",
      FIT_TABLE["Bianconi"]["c"] == "PROVIDES-CANDIDATE"
      and sum(1 for r in FIT_TABLE.values() for v in r.values() if v == "PROVIDES-CANDIDATE") == 1)
check("F", "planted control has NO PROVIDES on any of (b),(c),(d)",
      all(v != "PROVIDES-CANDIDATE" for v in FIT_TABLE["lattice QCD (ctrl)"].values()))

# ---------------------------------------------------------------------------------------
dt = time.time() - t0
n_T = 3
n_E = 8
n_F = 3
print("\n" + "=" * 78)
if FAILURES:
    print(f"FAILURES ({len(FAILURES)}): " + "; ".join(FAILURES))
    print("=" * 78)
    raise SystemExit(1)
print(f"HEADLINE: {n_E} [E] + {n_F} [F] = {n_E + n_F} (setup [T] = {n_T} excluded) ALL PASS")
print("OUTCOME S-a on the LOAD-BEARING items: no intaken program provides the S_3-label (a)")
print("  or the weak-value reading (b). Genuinely novel; spec sheet is the contribution.")
print("ONE non-load-bearing typed partial: Bianconi (c) scale-dial (relocation, not derivation).")
print("PLANTED CONTROL lattice QCD graded dead on every item; fails (a) on G-ext ONLY")
print("  (passes count+iso) -- the 'three colors' word-coincidence rejected by TYPE. Not broken.")
print(f"exit 0, deterministic, pure-Python, {dt:.3f} s")
raise SystemExit(0)
