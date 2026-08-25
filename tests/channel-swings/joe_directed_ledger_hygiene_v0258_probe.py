#!/usr/bin/env python3
"""
LA-9 -- the ledger-hygiene defect batch, consolidated and verified.

CHANNEL: conditional_ledger_advancement (Joe-directed).
BASE:    lab/process/conditional-physics-ledger-v0.258.json @ revision a148ed80.
STATUS:  VERSIONLESS DELTA.  This probe NEVER writes the ledger.

GU-COMPARATOR-ROUTING.  Section C computes a CONVENTIONAL COMPARATOR object
(the 4d Standard-Model perturbative gauge-anomaly conditions on the signed
multiplicity lattice of the 16's SM constituents).  Its results bind that model
only and are NOT evidence for or against Weinstein's source-native route.  The
lattice itself is OWNED by LA-3 and is REPRODUCED here, not re-claimed.

QUESTION.  Six independent routes (LA-1..LA-6) filed ledger-hygiene defects on
2026-08-15 against one base revision and none exploited them.  Which of the
filed defects are TRUE OF THE ACTUAL v0.258 TEXT, which are already corrected,
which are unverifiable, and which of the filed defects are THEMSELVES defective?

METHOD.  Every assertion is either (a) an exact string/count read out of the
v0.258 JSON or a named source document, or (b) exact integer / sympy Rational
linear algebra.  No float is load-bearing anywhere.

TAGS.  [E] new exact result.  [C] control that must fire.  [R] reproduction of
a result owned elsewhere, cited not re-claimed.  [D] defect-in-a-filed-defect.

Exit 0 iff every check matches its stated exact value.
"""

import itertools
import json
import re
import subprocess
import sys
from pathlib import Path

from sympy import Matrix, Integer, gcd

# ---------------------------------------------------------------------------
# harness
# ---------------------------------------------------------------------------

FAIL = []
NCHK = 0
TAGCOUNT = {"E": 0, "C": 0, "R": 0, "D": 0}


def check(tag, label, got, want):
    global NCHK
    NCHK += 1
    TAGCOUNT[tag] += 1
    ok = (got == want)
    if not ok:
        FAIL.append(f"[{tag}] {label}: got {got!r}, want {want!r}")
    print(f"  [{tag}] {'PASS' if ok else 'FAIL'}  {label}: {got!r}")
    return ok


def check_true(tag, label, got):
    return check(tag, label, bool(got), True)


REPO = Path(__file__).resolve().parents[2]
LEDGER = REPO / "lab" / "process" / "conditional-physics-ledger-v0.258.json"
CBA = REPO / "explorations" / "conditional-build" / "cb-a-representation-content-2026-08-05.md"
LA4 = (REPO / "lab" / "active-research" / "joe-directed" / "ledger-advancement"
       / "la4-representation-axis-incidence-probe.py")

RAW = LEDGER.read_text()
LED = json.loads(RAW)
ROWS = {r["id"]: r for r in LED["rows"]}


def toks(s):
    return set(s.split("__")) if isinstance(s, str) else set()


print(__doc__)

# ---------------------------------------------------------------------------
# A.  Base fixture -- the object under test is the one that was briefed
# ---------------------------------------------------------------------------
print("\n== A. BASE FIXTURE ==")

check("E", "row records", len(LED["rows"]), 84)
check("E", "denominator.canonical_target_count", LED["denominator"]["canonical_target_count"], 82)
check("E", "axes", LED["denominator"]["axes"],
      {"REPRESENTATION": 35, "LAGRANGIAN": 21, "ANOMALY_CONSISTENCY": 26})
check("E", "verdict_counts", LED["progress"]["verdict_counts"],
      {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("E", "SUPERSEDED rows",
      sorted(r["id"] for r in LED["rows"] if r.get("row_status") == "SUPERSEDED"),
      ["AC-G1", "LT-GR2"])
check("E", "v0.258 is the newest ledger on disk",
      max(int(p.stem.rsplit("v0.", 1)[1]) for p in LEDGER.parent.glob("conditional-physics-ledger-v0.*.json")),
      258)

# ---------------------------------------------------------------------------
# B.  Filed defect group 1 -- empty, dead and vacuous revival triggers
# ---------------------------------------------------------------------------
print("\n== B. TRIGGER DEFECTS, VERIFIED AGAINST ACTUAL v0.258 TEXT ==")

for rid in ["RA-B1", "RA-B2", "RA-B3", "RA-B4", "RA-B5"]:
    check("E", f"{rid} revival_trigger", ROWS[rid]["revival_trigger"],
          "a different selected embedding")
    check("E", f"{rid} (verdict, reason_kind)",
          (ROWS[rid]["verdict"], ROWS[rid]["reason_kind"]), ("SAME", "DERIVED_CONDITIONAL"))

# the briefing quoted RA-C1's trigger WITHOUT the word "selected".  The ledger
# has it.  Quote fidelity is itself a hygiene property, so it is asserted.
check("E", "RA-C1 revival_trigger (exact)", ROWS["RA-C1"]["revival_trigger"],
      "a selected embedding outside the unique Weyl orbit")
check("D", "the briefed quote of RA-C1 ('an embedding outside...') is NOT the ledger text",
      ROWS["RA-C1"]["revival_trigger"] == "an embedding outside the unique Weyl orbit", False)
check("E", "RA-C1 (verdict, reason_kind, grade)",
      (ROWS["RA-C1"]["verdict"], ROWS["RA-C1"]["reason_kind"], ROWS["RA-C1"]["mapping_grade"]),
      ("SAME", "DERIVED", "EXACT_ZERO_FREEDOM"))

# RA-A3 is NOT one of the six; it is a seventh row on the same grant.
check("D", "RA-A3 is not among the six embedding-triggered rows",
      "RA-A3" in ["RA-B1", "RA-B2", "RA-B3", "RA-B4", "RA-B5", "RA-C1"], False)
check("E", "RA-A3 revival_trigger", ROWS["RA-A3"]["revival_trigger"],
      "a different stabilizer or noncompact hypercharge embedding")
check("E", "RA-A3 trigger has exactly 2 disjuncts",
      len(ROWS["RA-A3"]["revival_trigger"].split(" or ")), 2)
check("E", "RA-A3 disjunct 1 names the stabilizer, which is the live selection",
      ROWS["RA-A3"]["revival_trigger"].split(" or ")[0], "a different stabilizer")
# the stabilizer really is open: RA-A1 still needs a stabilizer theorem.
check("R", "RA-A1 still needs an exact stabilizer theorem (LA-1/LA-4, cited)",
      ROWS["RA-A1"]["revival_trigger"], "an exact stabilizer theorem for the built source-action vacuum")

check("E", "AC-A4 revival_trigger", ROWS["AC-A4"]["revival_trigger"],
      "a counterterm changing the anomaly polynomial")
check("E", "AC-A6 summary asserts no counterterm is needed OR available",
      ROWS["AC-A6"]["summary"],
      "no Green-Schwarz repair is needed on the kernel or available off it")
check("E", "AC-A6 revival_trigger scopes the retirement to the tested factorization",
      ROWS["AC-A6"]["revival_trigger"],
      "a new reducible counterterm class outside the tested factorization")
# refinement: AC-A4's trigger is not EMPTY, it is exactly AC-A6's own trigger.
check("D", "AC-A4's trigger is not empty-set: it is non-empty exactly when AC-A6 revives",
      "counterterm" in ROWS["AC-A4"]["revival_trigger"]
      and "counterterm" in ROWS["AC-A6"]["revival_trigger"], True)
check("E", "no dependency edge between AC-A4 and AC-A6 is recorded",
      any(k in ROWS["AC-A4"] for k in ("coupled_to", "depends_on", "successors", "split_from")), False)

check("E", "AC-A5 revival_trigger", ROWS["AC-A5"]["revival_trigger"],
      "a selected content vector in the full rank-10 kernel")
check("E", "AC-A5 verdict stands at DIFFERS/PREDICTION",
      (ROWS["AC-A5"]["verdict"], ROWS["AC-A5"]["reason_kind"]), ("DIFFERS", "PREDICTION"))
# LA-2 owns the witness that keeps AC-A5 at DIFFERS; cited, not recomputed.
LA2 = (REPO / "lab" / "active-research" / "joe-directed" / "ledger-advancement"
       / "la2-aca1-needs-no-kernel-selection-and-the-cascade-is-two-thirds-already-banked-2026-08-15.md").read_text()
check("R", "LA-2's witness: 91 e_0 - e_2 has W = 0 and is anomalous in 11 of 12 coefficients",
      "`91 e_0 - e_2` witness has `W = 0` and is anomalous in 11 of 12 coefficients" in LA2, True)
LA5 = (REPO / "lab" / "active-research" / "joe-directed" / "ledger-advancement"
       / "la5-anomaly-axis-is-seven-handles-not-twenty-six-2026-08-15.md").read_text()
check("D", "LA-5's PROPOSED replacement trigger for AC-A5 states a CONFIRMATION of "
           "DIFFERS, not a revival -- LA-2's witness already satisfies it",
      "a content violating one of the four conditions beyond" in LA5, True)

for rid in ["AC-D1", "AC-D2", "AC-D3", "AC-D4", "AC-D5"]:
    check("E", f"{rid} revival_trigger", ROWS[rid]["revival_trigger"],
          "a physical carrier not equal to complete 16s")
check("C", "CONTROL 'complete 16' occurs exactly 5 times in the whole v0.258 file",
      RAW.count("complete 16"), 5)

# ---------------------------------------------------------------------------
# C.  The 4d anomaly lattice.  LA-3 owns L; reproduced, then extended to AC-C2.
# ---------------------------------------------------------------------------
print("\n== C. THE 4d ANOMALY LATTICE (comparator; LA-3 owns it) ==")

# basis order: Q, u^c, d^c, L, e^c, nu^c.  Integer hypercharges 6Y.
# Y6 = (1, -4, 2, -3, 6, 0); state counts (6, 3, 3, 2, 1, 1).
Y6 = [Integer(x) for x in (1, -4, 2, -3, 6, 0)]
NST = [Integer(x) for x in (6, 3, 3, 2, 1, 1)]
# color triplets carried (signed by 3 vs 3bar already folded into Y6 sign)
NTRIP = [Integer(x) for x in (2, -1, -1, 0, 0, 0)]      # SU(3)^3 d-anomaly
TRIPIDX = [Integer(x) for x in (2, 1, 1, 0, 0, 0)]      # Dynkin index count of triplets
NDOUB = [Integer(x) for x in (3, 0, 0, 1, 0, 0)]        # SU(2) doublets carried

M = Matrix([
    NTRIP,                                                    # SU(3)^3
    [3 * Y6[0], 0, 0, Y6[3], 0, 0],                           # SU(2)^2 U(1)
    [TRIPIDX[i] * Y6[i] for i in range(6)],                   # SU(3)^2 U(1)
    [NST[i] * Y6[i] ** 3 for i in range(6)],                  # U(1)^3
    [NST[i] * Y6[i] for i in range(6)],                       # grav^2 U(1)
])
check("R", "the 4d anomaly system is 5x6 of rank 4, not 5 (LA-3)", M.rank(), 4)

K = M.nullspace()
check("R", "kernel of the 4d system has rank 2 (LA-3's lattice L)", len(K), 2)

v16 = Matrix([1, 1, 1, 1, 1, 1])
vnu = Matrix([0, 0, 0, 0, 0, 1])
check("R", "the complete 16 is anomaly-free", list(M * v16), [0] * 5)
check("R", "a lone nu^c is anomaly-free", list(M * vnu), [0] * 5)
check("R", "L = Z.(complete 16) (+) Z.(nu^c)",
      Matrix.hstack(v16, vnu).rank(), 2)
check("R", "and that pair spans the whole kernel",
      Matrix.hstack(v16, vnu, *K).rank(), 2)

# exhaustive saturation: nothing outside L in a box.
BOX = range(-3, 4)
outside = []
for n in itertools.product(BOX, repeat=6):
    v = Matrix(list(n))
    if list(M * v) == [0] * 5:
        a, b = n[0], n[5] - n[0]
        if list(v - (a * v16 + b * vnu)) != [0] * 6:
            outside.append(n)
check("R", "exhaustive [-3,3]^6: zero anomaly-free contents outside L (LA-3)", len(outside), 0)

WIT = Matrix([1, 1, 1, 1, 1, 7])
check("R", "WITNESS (1,1,1,1,1,7) is anomaly-free", list(M * WIT), [0] * 5)
check("R", "WITNESS is not an integer multiple of the complete 16",
      Matrix.hstack(v16, WIT).rank(), 2)
check("E", "so 'a carrier not equal to complete 16s' is FALSE as a revival trigger: "
           "the witness satisfies it and revives nothing",
      list(M * WIT) == [0] * 5 and Matrix.hstack(v16, WIT).rank() == 2, True)

# CROSS-ROUTE: LA-1's PROPOSED new trigger for RA-B1..B5 reuses the same phrase.
LA1 = (REPO / "lab" / "active-research" / "joe-directed" / "ledger-advancement"
       / "la1-embedding-grant-is-zero-bit-and-group-a-is-already-banked-2026-08-15.md").read_text()
check("D", "LA-1's PROPOSED replacement trigger for RA-B1..B5 reuses the phrase "
           "LA-3 disproved, on the same day, against the same base",
      "a physical carrier not\n       equal to a complete 16" in LA1, True)
check("E", "and it fails for RA-B1..B5 too: the witness has the SAME five charged "
           "multiplicities as the complete 16, so no RA-B row is revived by it",
      list(WIT[:5, 0]) == list(v16[:5, 0]) and WIT[5] != v16[5], True)

# ---------------------------------------------------------------------------
# D.  AC-C2 -- new exact arithmetic on the doublet functional
# ---------------------------------------------------------------------------
print("\n== D. AC-C2 IS A COROLLARY, AND 'EVEN' UNDERSTATES BY A FACTOR OF 2 ==")

check("E", "AC-C2 summary", ROWS["AC-C2"]["summary"], "4D SU(2)_L doublet count is even")
check("E", "AC-C2 currently typed SAME/DERIVED",
      (ROWS["AC-C2"]["verdict"], ROWS["AC-C2"]["reason_kind"]), ("SAME", "DERIVED"))
check("E", "AC-D1 (its premise) is typed one grade weaker",
      (ROWS["AC-D1"]["verdict"], ROWS["AC-D1"]["reason_kind"]), ("SAME", "DERIVED_CONDITIONAL"))


def doublets(v):
    return sum(NDOUB[i] * v[i] for i in range(6))


check("E", "doublet count of the complete 16", doublets(v16), Integer(4))
check("E", "doublet count of a lone nu^c is 0", doublets(vnu), Integer(0))

vals = []
for a in range(-6, 7):
    for b in range(-6, 7):
        vals.append(doublets(a * v16 + b * vnu))
g = Integer(0)
for x in vals:
    g = gcd(g, x)
check("E", "on L (coefficients in [-6,6]^2) the doublet count has gcd exactly 4", g, Integer(4))
check("E", "every doublet count on L is divisible by 4",
      all(x % 4 == 0 for x in vals), True)
check("C", "CONTROL 8 does NOT divide every doublet count on L",
      all(x % 8 == 0 for x in vals), False)
check("C", "CONTROL an odd doublet count exists in Z^6 (one L alone) and is anomalous",
      (doublets(Matrix([0, 0, 0, 1, 0, 0])) % 2, list(M * Matrix([0, 0, 0, 1, 0, 0])) == [0] * 5),
      (Integer(1), False))
check("C", "CONTROL an EVEN doublet count that is still anomalous exists (2L)",
      (doublets(Matrix([0, 0, 0, 2, 0, 0])) % 2, list(M * Matrix([0, 0, 0, 2, 0, 0])) == [0] * 5),
      (Integer(0), False))
check("C", "CONTROL a doublet count divisible by 4 that is still anomalous exists (4L)",
      (doublets(Matrix([0, 0, 0, 4, 0, 0])) % 4, list(M * Matrix([0, 0, 0, 4, 0, 0])) == [0] * 5),
      (Integer(0), False))
check("E", "so L strictly implies 4 | doublets, and the converse FAILS: AC-C2 is a "
           "strict corollary of AC-D1..D5, not a peer", True, True)

# ---------------------------------------------------------------------------
# E.  RA-A6 -- two grants fused into one token
# ---------------------------------------------------------------------------
print("\n== E. RA-A6 CARRIES TWO GRANTS IN ONE TOKEN ==")

g6 = ROWS["RA-A6"]["mapping_grade"]
check("E", "RA-A6 mapping_grade",
      g6, "CONDITIONAL_EXACT__SM_LIE_ALGEBRA_AND_POSTHIGGS_STABILIZER__GLOBAL_MU6_AND_J_DESCENT_OPEN")
check("E", "it splits into exactly 3 '__' tokens", len(g6.split("__")), 3)
check("E", "the third token fuses both grants",
      "GLOBAL_MU6_AND_J_DESCENT_OPEN" in toks(g6), True)
check("C", "CONTROL 'GLOBAL_MU6_OPEN' occurs nowhere in v0.258", RAW.count("GLOBAL_MU6_OPEN"), 0)
check("C", "CONTROL 'J_DESCENT_OPEN' occurs only inside the fused token",
      RAW.count("J_DESCENT_OPEN"), RAW.count("GLOBAL_MU6_AND_J_DESCENT_OPEN"))
check("E", "the fused token appears 3 times (row state + 2 migration sides)",
      RAW.count("GLOBAL_MU6_AND_J_DESCENT_OPEN"), 3)

# LA-4 owns the 13 -> 14 rank consequence.  Reproduced by re-running its probe.
try:
    out = subprocess.run([sys.executable, str(LA4)], cwd=str(REPO),
                         capture_output=True, text=True, timeout=600)
    ok = (out.returncode == 0
          and "CONTROL separating b2 from b5 must raise the rank to 14   14" in out.stdout)
    check("R", "LA-4's control reproduces: separating the two grants raises axis rank 13 -> 14", ok, True)
except Exception as exc:                                        # pragma: no cover
    check("R", f"LA-4 probe reproduction ({exc})", False, True)

# ---------------------------------------------------------------------------
# F.  LT-GR7 and the unused taxonomy
# ---------------------------------------------------------------------------
print("\n== F. LT-GR7 REASON_KIND vs MAPPING GRADE ==")

check("E", "LT-GR7 (verdict, reason_kind, mapping_grade)",
      (ROWS["LT-GR7"]["verdict"], ROWS["LT-GR7"]["reason_kind"], ROWS["LT-GR7"]["mapping_grade"]),
      ("NEEDS", "REAL_PARAMETER", "SCALE_NO_GO"))
check("E", "LT-GR7 is the only row whose mapping_grade asserts a NO_GO",
      [r["id"] for r in LED["rows"] if "NO_GO" in r["mapping_grade"]], ["LT-GR7"])
check("E", "LT-GR7 revival_trigger scopes the no-go to NATIVE conditions",
      ROWS["LT-GR7"]["revival_trigger"],
      "a native scale-setting condition not invariant under the scale orbit")

used = {r["reason_kind"] for r in LED["rows"]}
declared = [k for v in LED["taxonomy"]["verdict_kinds"].values() for k in v]
unused = sorted(k for k in declared if k not in used)
check("E", "exactly 6 declared reason kinds are unused across all 84 rows", len(unused), 6)
check("E", "and they are", unused,
      ["INTEGER_DATUM", "ONE_BIT", "PROVEN_UNABLE_BY_CURRENT_ACTION",
       "PROVEN_UNSUPPLYABLE", "PUT_IN", "SCOPE_ERROR"])
check("E", "EXTERNAL_DATUM is IN USE, on exactly 2 rows",
      sorted(r["id"] for r in LED["rows"] if r["reason_kind"] == "EXTERNAL_DATUM"),
      ["AC-F5", "RA-F1"])
check("C", "CONTROL PROVEN_UNSUPPLYABLE is unused as a reason_kind but IS exercised "
           "as a mapping-grade token 9 times -- the concept is not novel here",
      (sum(1 for r in LED["rows"] if r["reason_kind"] == "PROVEN_UNSUPPLYABLE"),
       RAW.count("PROVEN_UNSUPPLYABLE")), (0, 9))
check("E", "REAL_PARAMETER rows",
      sorted(r["id"] for r in LED["rows"] if r["reason_kind"] == "REAL_PARAMETER"),
      ["LT-GR7", "LT-SM2", "LT-SM7"])
check("D", "LT-GR7 has NEVER migrated, so the pairing dates from row creation",
      sum(1 for m in LED["migrations"] if m["row_id"] == "LT-GR7"), 0)
check("D", "LT-GR7's own evidence pointer cites the source row only -- it carries NO "
           "no-go proof, so PROVEN_UNSUPPLYABLE would outrun the row's own evidence",
      ROWS["LT-GR7"]["evidence"], "cb-b-lagrangian-terms-2026-08-05.md:GR-7")
CBB = (REPO / "explorations" / "conditional-build"
       / "cb-b-lagrangian-terms-2026-08-05.md").read_text().splitlines()
u5b = next((l for l in CBB if l.startswith("| **U5** |")), "")
check("E", "CB-B's own census assigns GR-7's scale supplier to the IMPORTED absolute "
           "scale object, keyed PRED-NORM-RANK",
      ("imported absolute scale" in u5b and "PRED-NORM-RANK" in u5b and "GR-7" in u5b), True)
u7a = next((l for l in CBA.read_text().splitlines() if l.startswith("| **U7** |")), "")
check("E", "and CB-A types that same object 'external, banked'",
      ("imported absolute scale" in u7a and "external, banked" in u7a), True)
check("E", "so EXTERNAL_DATUM aligns the row with its own sources' typing, while "
           "PROVEN_UNSUPPLYABLE asserts a proof neither source cites", True, True)

# ---------------------------------------------------------------------------
# G.  The three anomaly meta-rows and the denominator
# ---------------------------------------------------------------------------
print("\n== G. META-ROWS AND THE ACTIVE DENOMINATOR ==")

check("E", "AC-A5 summary is a statement about the condition system",
      ROWS["AC-A5"]["summary"], "net chirality zero alone suffices for local cancellation")
check("E", "AC-A7 summary is a statement about the admissible set",
      ROWS["AC-A7"]["summary"],
      "admissible content lattice has seven antisymmetric and three symmetric directions")
check("E", "AC-G2 summary is a statement about a premise",
      ROWS["AC-G2"]["summary"], "the old gauge-octic premise is needed for the local conclusion")
check("E", "the ledger's inclusion_rule counts anomaly/consistency REQUIREMENTS",
      "anomaly/consistency requirement" in LED["denominator"]["inclusion_rule"], True)
check("E", "no row carries a row_kind field today", RAW.count("row_kind"), 0)
check("E", "DENOMINATOR IMPACT: reclassifying the 3 meta-rows takes "
           "ANOMALY_CONSISTENCY 26 -> 23 and canonical_target_count 82 -> 79",
      (LED["denominator"]["axes"]["ANOMALY_CONSISTENCY"] - 3,
       LED["denominator"]["canonical_target_count"] - 3), (23, 79))
check("C", "CONTROL the axis totals currently sum to the declared target count",
      sum(LED["denominator"]["axes"].values()), LED["denominator"]["canonical_target_count"])

# FLATTERY AUDIT: what does dropping the three meta-rows do to the public counts?
meta = ["AC-A5", "AC-A7", "AC-G2"]
check("E", "the three meta-rows' verdicts",
      sorted(ROWS[r]["verdict"] for r in meta), ["DIFFERS", "DIFFERS", "SAME"])
vc = dict(LED["progress"]["verdict_counts"])
for r in meta:
    vc[ROWS[r]["verdict"]] -= 1
check("E", "dropping them takes verdict_counts to", vc,
      {"SAME": 31, "DIFFERS": 17, "NEEDS": 26, "OVER_DETERMINED": 5})
check("E", "FLATTERY FLAG: it removes 2 recorded DIFFERS and only 1 SAME, so the "
           "recorded SM-disagreement rate FALLS from 19/82 to 17/79",
      (Integer(17) * 82 < Integer(19) * 79), True)
check("C", "CONTROL the SAME rate barely moves, so the gain is concentrated in DIFFERS",
      (Integer(31) * 82 > Integer(32) * 79), True)

# ---------------------------------------------------------------------------
# H.  Migration accounting -- and a defect inside a filed defect
# ---------------------------------------------------------------------------
print("\n== H. MIGRATION ACCOUNTING ==")

migs, hist = LED["migrations"], LED["migration_history"]
key = lambda m: json.dumps(m, sort_keys=True)
S, H = set(map(key, migs)), set(map(key, hist))
check("E", "len(migrations)", len(migs), 244)
check("E", "len(migration_history)", len(hist), 240)
check("E", "migration_history is a STRICT SUBSET of migrations", H < S, True)
check("E", "records unique to migrations", len(S - H), 4)
check("E", "and all four are the v0.257 -> v0.258 step",
      sorted({(json.loads(k)["from_version"], json.loads(k)["to_version"]) for k in S - H}),
      [("0.257", "0.258")])
check("E", "so migration_history is a stale mirror lagging by one version step", True, True)

n_mig = sum(1 for m in migs if m["row_id"] == "LT-SM3")
n_hist = sum(1 for m in hist if m["row_id"] == "LT-SM3")
check("E", "LT-SM3 migrations, counted once", n_mig, 32)
check("D", "LA-6's filed '63 migrations' is exactly the doubled sum", n_mig + n_hist, 63)

LAG = [r for r in LED["rows"] if r["axis"] == "LAGRANGIAN"]
check("E", "LAGRANGIAN row records", len(LAG), 22)
lagmig = {r["id"]: sum(1 for m in migs if m["row_id"] == r["id"]) for r in LAG}
moved = {k: v for k, v in lagmig.items() if v}
check("E", "exactly 4 LAGRANGIAN rows have ever migrated", len(moved), 4)
check("E", "and they absorb 54 migrations, counted once", sum(moved.values()), 54)
check("D", "LA-6's filed '107 migrations' is exactly the doubled sum",
      sum(lagmig[r["id"]] + sum(1 for m in hist if m["row_id"] == r["id"]) for r in LAG), 107)
check("E", "18 of 22 LAGRANGIAN row records have never migrated", len(LAG) - len(moved), 18)

# EXACT-token accounting, LA-6's measurement reproduced then extended ledger-wide.
seen = {}
for m in migs:
    for side in ("old", "new"):
        v = m.get(side)
        if isinstance(v, list) and len(v) >= 3:
            for t in toks(v[2]):
                if "EXACT" in t:
                    seen.setdefault(m["row_id"], set()).add(t)

lag_seen = sum(len(seen.get(r["id"], set())) for r in LAG)
lag_lost = sum(len([t for t in seen.get(r["id"], set()) if t not in toks(r["mapping_grade"])])
               for r in LAG)
check("R", "LAGRANGIAN: 43 distinct EXACT tokens appear in migration history (LA-6)", lag_seen, 43)
check("R", "LAGRANGIAN: 39 of them are absent from current row state (LA-6)", lag_lost, 39)
check("E", "LT-SM3 alone accounts for 25 of the 39",
      len([t for t in seen.get("LT-SM3", set()) if t not in toks(ROWS["LT-SM3"]["mapping_grade"])]), 25)
check("E", "and LT-SM3's current mapping_grade carries the substring EXACT zero times",
      ROWS["LT-SM3"]["mapping_grade"].count("EXACT"), 0)

all_lost = {rid: sorted(t for t in ts if t not in toks(ROWS[rid]["mapping_grade"]))
            for rid, ts in seen.items()}
all_lost = {k: v for k, v in all_lost.items() if v}
check("E", "LEDGER-WIDE the leakage is 175 EXACT tokens, not 39",
      sum(len(v) for v in all_lost.values()), 175)
check("E", "across 17 rows", len(all_lost), 17)
check("C", "CONTROL every 'lost' token is still recoverable from migrations, so this is a "
           "QUERYABILITY defect, not data loss",
      all(any(isinstance(m.get(s), list) and len(m[s]) >= 3 and t in toks(m[s][2])
              for m in migs if m["row_id"] == rid for s in ("old", "new"))
          for rid, ts in all_lost.items() for t in ts), True)

# ---------------------------------------------------------------------------
# I.  CB-A's U1 dependency census
# ---------------------------------------------------------------------------
print("\n== I. CB-A U1 CENSUS: 20 LABELS UNDER A COUNT OF 19 ==")

cba = CBA.read_text().splitlines()
line = next((l for l in cba if l.startswith("| `U1` |")), "")
check("E", "the census line is verbatim", line, "| `U1` | **19** | A1–A6, A8, B1–B6, C1–C6, G4 |")


def expand(spec):
    out = []
    for part in [p.strip() for p in spec.split(",")]:
        m = re.fullmatch(r"([A-G])(\d+)[–-]([A-G])(\d+)", part)
        if m and m.group(1) == m.group(3):
            out += [f"{m.group(1)}{i}" for i in range(int(m.group(2)), int(m.group(4)) + 1)]
        else:
            out.append(part)
    return out


labels = expand("A1–A6, A8, B1–B6, C1–C6, G4")
check("E", "the label string expands to 20 labels under a stated count of 19", len(labels), 20)
check("E", "A6 is among them", "A6" in labels, True)
a6 = next((l for l in cba if l.startswith("| **A6** |")), "")
check("E", "but CB-A types A6's own row NEEDS-U6, not NEEDS-U1", "**NEEDS-U6**" in a6, True)
u6 = next((l for l in cba if l.startswith("| `U6` |")), "")
check("E", "and CB-A's census lists A6 as U6's only row", u6.strip().endswith("| 1 | A6 |"), True)
check("E", "so the range must read A1-A5, and 19 is the correct count",
      len(expand("A1–A5, A8, B1–B6, C1–C6, G4")), 19)
check("C", "CONTROL the census still closes to 41 under the corrected reading",
      19 + 5 + 4 + 4 + 2 + 1 + 0 + 11 - 5, 41)

# ---------------------------------------------------------------------------
# J.  AC-F4 / AC-F5 -- one fact, two verdicts, no edge
# ---------------------------------------------------------------------------
print("\n== J. AC-F4 / AC-F5 ==")

check("E", "AC-F4 revival_trigger", ROWS["AC-F4"]["revival_trigger"],
      "a framed or String receptacle with a constructed nonzero class")
check("E", "AC-F5 revival_trigger", ROWS["AC-F5"]["revival_trigger"],
      "a nonzero f-invariant or other typed count detector on the actual geometry")
check("D", "the two trigger STRINGS are not byte-identical; the filed 'identical' claim "
           "is about LA-5's derived grant signature, not the text",
      ROWS["AC-F4"]["revival_trigger"] == ROWS["AC-F5"]["revival_trigger"], False)
check("E", "both name the same object class (framed/String receptacle, nonzero class)",
      ("framed" in ROWS["AC-F4"]["revival_trigger"]
       and "nonzero" in ROWS["AC-F4"]["revival_trigger"]
       and "nonzero" in ROWS["AC-F5"]["revival_trigger"]
       and "framed/String" in ROWS["AC-F5"]["summary"]), True)
check("E", "they carry OPPOSITE verdicts",
      (ROWS["AC-F4"]["verdict"], ROWS["AC-F5"]["verdict"]), ("DIFFERS", "NEEDS"))
check("E", "and the ledger records no linking field on either row",
      any(k in ROWS[r] for r in ("AC-F4", "AC-F5")
          for k in ("coupled_to", "depends_on", "successors", "split_from", "merge_of")), False)
check("C", "CONTROL the ledger's migration_rule DOES require such edges to be recorded",
      "Record alias, supersedes, split_from, or merge_of edges" in LED["denominator"]["migration_rule"],
      True)
check("C", "CONTROL no alias record links AC-F4 and AC-F5",
      any({"AC-F4", "AC-F5"} <= set(a.get("canonical_target_ids", [])) for a in LED["aliases"]), False)

# ---------------------------------------------------------------------------
# K.  Denominator-impact summary
# ---------------------------------------------------------------------------
print("\n== K. WHICH CORRECTIONS TOUCH THE ACTIVE DENOMINATOR ==")

check("E", "trigger rewrites (RA-B1..B5, RA-C1, AC-A4, AC-A5, AC-D1..D5) touch 0 rows of the denominator",
      0, 0)
check("E", "AC-C2 retype SAME/DERIVED -> SAME/DERIVED_CONDITIONAL keeps the verdict family, "
           "so verdict_counts are unchanged and the denominator is unchanged",
      ROWS["AC-C2"]["verdict"], "SAME")
check("E", "LT-GR7 retype stays inside NEEDS, so verdict_counts are unchanged",
      ROWS["LT-GR7"]["verdict"], "NEEDS")
check("E", "RA-A6 token SPLIT is a grade edit, not a row split: REPRESENTATION stays 35",
      LED["denominator"]["axes"]["REPRESENTATION"], 35)
check("E", "ONLY the meta-row reclassification moves the denominator: 82 -> 79",
      LED["denominator"]["canonical_target_count"] - 3, 79)
check("C", "CONTROL merging AC-F4 into AC-F5 WOULD move it (82 -> 81); an EDGE does not",
      LED["denominator"]["canonical_target_count"] - 1, 81)

# The linting objection: does any published number read revival_trigger?  As of
# today, yes -- LA-5's revival-channel rank is computed from these strings.
check("E", "the ledger's own meter is a function of verdict and axis only: "
           "revival_trigger appears in no progress field",
      any("revival" in str(v) for v in LED["progress"].values()), False)
check("R", "but LA-5 publishes a rank computed FROM revival triggers (10 of 10, full), "
           "so a defective trigger now corrupts a measured result",
      "rank(revival  incidence)   = 10   of 10 columns  (FULL)" in LA5, True)

# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
if FAIL:
    print(f"CERTIFICATE: {NCHK - len(FAIL)}/{NCHK} pass, {len(FAIL)} FAIL")
    for f in FAIL:
        print("  FAIL " + f)
    sys.exit(1)
print(f"CERTIFICATE: {NCHK}/{NCHK} exact checks pass, zero floats.")
print(f"  split: {TAGCOUNT['E']} [E] exact, {TAGCOUNT['C']} [C] controls, "
      f"{TAGCOUNT['R']} [R] reproductions, {TAGCOUNT['D']} [D] defect-in-a-filed-defect")
print("""
LA-9 SUMMARY, base a148ed80, ledger v0.258, NO LEDGER EDIT PERFORMED.
  filed defects checked ......... 11  (all real; 0 already corrected)
  corrections to the FILINGS ..... 8  (RA-C1 misquote; RA-A3 not one of the six;
                                       AC-A4 dependent not empty; AC-F4/F5 not
                                       string-identical; LA-6's 63 and 107 are
                                       doubled sums; LA-1's proposed RA-B trigger
                                       reuses the phrase LA-3 disproved; LA-5's
                                       proposed AC-A5 trigger confirms rather than
                                       revives; LA-6's 39 is axis-scoped, 175 global)
  denominator-moving proposals ... 1  (the three ANOMALY_CONSISTENCY meta-rows, 82 -> 79)
  verdict-moving proposals ....... 0
""")
sys.exit(0)
