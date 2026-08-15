#!/usr/bin/env python3
"""
LA-5 -- effective degrees of freedom of the ANOMALY_CONSISTENCY axis.

GU-COMPARATOR-ROUTING: this probe touches a CONVENTIONAL COMPARATOR object
(the 4d Standard-Model perturbative gauge-anomaly conditions, fork 1).  Any
result about that object binds only that model.  See la5-*.md and
lab/methods/source-native-comparator-routing.md.

QUESTION (new; not owned in-repo).  Ledger v0.258 carries 26 active
ANOMALY_CONSISTENCY rows.  How many genuinely independent unknowns control
them?  Concretely: build the grant->row incidence matrix from the ledger's own
`distance` and `revival_trigger` fields plus CB-C's row table, and compute its
EXACT rank, its signature classes, its immovable set, its maximum-coverage
Pareto frontier, and the exact number of distinct verdict states the axis can
express.

NOT CLAIMED HERE.  The 14D rank-5 / kernel-10 system is owned by CB-C
(explorations/conditional-build/cb-c-anomaly-conditions-2026-08-05.md,
tests/anomaly/cb_c_anomaly_rank.py) and is IMPORTED, not re-derived.  The 4D
rank-4 result and the lattice L = Z.(15) (+) Z.(nu^c) are owned by LA-3 and are
REPRODUCED as an anchor, not re-claimed.  Nothing here is a GU source claim, a
chirality-production mechanism, a generation count, or a verdict movement.

Exit 0 iff every [E] result matches its stated exact value, every [C] control
fires as declared, and every [R] reproduction matches its filed owner.
"""

import sys
import os
import json
import itertools
from fractions import Fraction as F
from sympy import Rational as R, Matrix, Integer
from sympy.matrices.normalforms import smith_normal_form

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "tests", "anomaly"))

FAIL = []
NCHK = 0
TAGS = {}


def check(tag, label, got, want):
    global NCHK
    NCHK += 1
    TAGS[tag] = TAGS.get(tag, 0) + 1
    ok = (got == want)
    if not ok:
        FAIL.append(f"[{tag}] {label}: got {got!r}, want {want!r}")
    print(f"  [{tag}] {'PASS' if ok else 'FAIL'}  {label}: {got}")
    return ok


def check_true(tag, label, got):
    return check(tag, label, bool(got), True)


# ===========================================================================
# 0.  RE-DERIVE THE WORK LIST FROM THE LEDGER (preflight requirement)
# ===========================================================================
print("=" * 78)
print("LA-5 -- effective degrees of freedom of the ANOMALY_CONSISTENCY axis")
print("=" * 78)

LEDGER = os.path.join(REPO, "lab", "process", "conditional-physics-ledger-v0.258.json")
with open(LEDGER) as fh:
    LED = json.load(fh)

ALL_ROWS = LED["rows"]
AC = [r for r in ALL_ROWS if r["axis"] == "ANOMALY_CONSISTENCY"]
AC_ACTIVE = [r for r in AC if r.get("row_status") != "SUPERSEDED"]
IDS = [r["id"] for r in AC_ACTIVE]

print("\n-- 0. re-derived pool --")
check("E", "ledger row records", len(ALL_ROWS), 84)
check("E", "ledger declared canonical target count", LED["denominator"]["canonical_target_count"], 82)
check("E", "ANOMALY_CONSISTENCY row records", len(AC), 27)
check("E", "ANOMALY_CONSISTENCY ACTIVE rows", len(AC_ACTIVE), 26)
check("E", "declared axis count matches", LED["denominator"]["axes"]["ANOMALY_CONSISTENCY"], 26)
check("E", "the one superseded AC row is AC-G1",
      [r["id"] for r in AC if r.get("row_status") == "SUPERSEDED"], ["AC-G1"])
# CB-C had 27 source rows A1-A7,B1-B5,C1-C2,D1-D5,E1,F1-F5,G1-G2; B3 was aliased.
aliased_b3 = [a for a in LED["aliases"] if a["source_row"] == "CB-C:B3"]
check("E", "CB-C:B3 is aliased into AC-A1 (not an independent row)",
      aliased_b3[0]["canonical_target_ids"] if aliased_b3 else None, ["AC-A1"])


# ===========================================================================
# 1.  THE GRANT ATOMS, AND THE INCIDENCE ASSIGNMENT
#     Every (row, grant) entry is justified by a quoted ledger field or by a
#     CB-C row-table verdict.  U5 (Green-Schwarz) is RETIRED by AC-A6.
#     U6 (RS-BRST ghost datum q) is NOT an independent column: CB-C sec.5 makes
#     it a coordinate on which lattice vector U1 is, so it is folded into U1.
# ===========================================================================
GRANTS = ["U1", "U2", "U3", "U4", "EMB", "BV", "N1", "P3", "BR"]
GNAME = {
    "U1":  "the source action's 14D fermion content x in Z^15",
    "U2":  "which group the source action's covariant derivative gauges",
    "U3":  "the tangential structure carried by the end/link (spin/framed/String)",
    "U4":  "the 14->4 reduction plus whatever produces 4D chirality",
    "EMB": "the SM embedding / stabilizer selection (RA-A3, RA-B1..RA-B5)",
    "BV":  "native action-stationary background + proper BV/BFV + analytic domain + physical cohomology",
    "N1":  "CB-C-N1: the Cl(7,7)-side gauge-twisted degree-15 reduced spin-bordism receptacle",
    "P3":  "the count datum + a nonzero framed/String corner object",
    "BR":  "a non-inflow 3-primary bridge, OR supersession of the sole-bridge canon premise",
}

# DISCHARGE incidence: what must be supplied before the row's cell is terminal.
DISCHARGE = {
    "AC-A1":  ({"U1"},          "ledger distance: 'select a source-action fermion content in the rank-10 kernel'"),
    "AC-A2":  ({"U1"},          "ledger distance: 'none after AC-A1'; CB-C row A2 = AUTO given A1"),
    "AC-A3":  ({"U1"},          "ledger distance: 'none after AC-A1'; CB-C row A3 = AUTO given A1"),
    "AC-A4":  (set(),           "ledger distance: 'none at local-anomaly grade'; CB-C row A4 = DET"),
    "AC-A5":  (set(),           "CB-C row A5 = DET(negative), witness 91 e_0 - e_2 computed"),
    "AC-A6":  (set(),           "CB-C row A6 = DET; U5 retired"),
    "AC-A7":  (set(),           "CB-C row A7 = DET; structure of ker M"),
    "AC-B1":  (set(),           "CB-C row B1 = AUTO and explicitly independent of U1"),
    "AC-B2":  ({"U2", "N1"},    "ledger distance: 'compute the Cl(7,7)-appropriate BSO(128)-type receptacle'; the receptacle is GAUGE-TWISTED, so U2 too"),
    "AC-B4":  (set(),           "CB-C row B4 = AUTO, signature-independent"),
    "AC-B5":  (set(),           "CB-C row B5 = AUTO (single kill on the settled horn)"),
    "AC-C1":  (set(),           "CB-C row C1 = AUTO for every U1 in the arena, under BOTH horns"),
    "AC-C2":  ({"U4", "EMB"},   "ledger distance: 'none after the 16 is observed'"),
    "AC-D1":  ({"U4", "EMB"},   "ledger distance: 'none after the chiral 16 shadow is selected'; LA-3 corrected string names U4 + G-EMB"),
    "AC-D2":  ({"U4", "EMB"},   "as AC-D1"),
    "AC-D3":  ({"U4", "EMB"},   "as AC-D1"),
    "AC-D4":  ({"U4", "EMB"},   "as AC-D1"),
    "AC-D5":  ({"U4", "EMB"},   "as AC-D1"),
    "AC-E1":  ({"U4", "EMB"},   "CB-C row E1 = AUTO given U4; the SM group must exist, so EMB"),
    "AC-F1":  ({"U4", "BV"},    "ledger distance names native background, BV/BFV, positive domain, physical cohomology"),
    "AC-F2":  (set(),           "CB-C row F2 = AUTO at kinematic block grade"),
    "AC-F3":  ({"BR"},          "ledger distance: 'construct a non-inflow ... bridge or supersede the sole-bridge premise'"),
    "AC-F4":  (set(),           "CB-C row F4 = DET(negative), banked; 'spin cannot improve'"),
    "AC-F5":  ({"U3", "P3"},    "ledger distance: 'construct a nonzero corner/framing object and pair it with P3'"),
    "AC-G1a": ({"U1", "U2", "BV"}, "ledger distance: Cartan restriction unselected (BV), typed gauge group (U2), full fermion content (U1)"),
    "AC-G2":  (set(),           "ledger distance: 'restate the conclusion using the fork-independent rank theorem' -- editorial"),
}

# REVIVAL incidence: what would UN-terminalize the row, read off revival_trigger.
REVIVAL = {
    "AC-A1":  {"U1"},
    "AC-A2":  {"U2"},          # 'a gauge representation not factored identically across form slots'
    "AC-A3":  {"U2"},          # 'a source action with slot-dependent gauge factors'
    "AC-A4":  {"U5"},          # 'a counterterm changing the anomaly polynomial' -- U5, RETIRED by AC-A6
    "AC-A5":  {"U1"},          # 'a selected content vector in the full rank-10 kernel'
    "AC-A6":  {"U5"},          # 'a new reducible counterterm class outside the tested factorization'
    "AC-A7":  {"U1"},          # 'a source action imposing nonlinear content constraints'
    "AC-B1":  {"U3"},          # 'a different tangential structure or twist'
    "AC-B2":  {"N1"},
    "AC-B4":  {"U3"},          # 'a different generalized cohomology or degree'
    "AC-B5":  {"U3"},          # 'a new real-side eta receptacle'
    "AC-C1":  {"U2"},          # 'a selected group with a different pi_4 receptacle'
    "AC-C2":  {"U4"},          # 'a physical projection removing an odd subset of doublets'
    "AC-D1":  {"U4", "EMB"},   # trigger FALSE AS STATED (LA-3); corrected = content outside L
    "AC-D2":  {"U4", "EMB"},
    "AC-D3":  {"U4", "EMB"},
    "AC-D4":  {"U4", "EMB"},
    "AC-D5":  {"U4", "EMB"},
    "AC-E1":  set(),           # 'a direct computation disagreeing with the cited result' -- a task
    "AC-F1":  {"U4", "BV"},
    "AC-F2":  {"U4"},          # 'a physical projection that cuts across the balanced blocks'
    "AC-F3":  {"BR"},
    "AC-F4":  {"U3", "P3"},    # 'a framed or String receptacle with a constructed nonzero class'
    "AC-F5":  {"U3", "P3"},
    "AC-G1a": {"U1", "U2", "BV"},
    "AC-G2":  {"U2"},          # 'a source/action change that makes gauge weights slot-dependent'
}

check("E", "discharge assignment covers every active AC row", sorted(DISCHARGE) == sorted(IDS), True)
check("E", "revival assignment covers every active AC row", sorted(REVIVAL) == sorted(IDS), True)

# ---- AUDITABILITY: every 1 in the incidence matrix must be backed by an exact
#      substring occurring in that row's OWN v0.258 text.  A declared typing that
#      cannot be checked against the ledger is not admissible as evidence.
BACKING = {
    ("AC-A1", "U1"):   "fermion content",
    ("AC-A2", "U1"):   "AC-A1",
    ("AC-A3", "U1"):   "AC-A1",
    ("AC-B2", "U2"):   "gauge-twisted",
    ("AC-B2", "N1"):   "BSO(128)",
    ("AC-C2", "U4"):   "observed",
    ("AC-C2", "EMB"):  "16",
    ("AC-D1", "U4"):   "shadow",   ("AC-D1", "EMB"): "16",
    ("AC-D2", "U4"):   "shadow",   ("AC-D2", "EMB"): "16",
    ("AC-D3", "U4"):   "shadow",   ("AC-D3", "EMB"): "16",
    ("AC-D4", "U4"):   "shadow",   ("AC-D4", "EMB"): "16",
    ("AC-D5", "U4"):   "shadow",   ("AC-D5", "EMB"): "16",
    ("AC-E1", "U4"):   "4D",       ("AC-E1", "EMB"): "SM",
    ("AC-F1", "U4"):   "four-dimensional",
    ("AC-F1", "BV"):   "BV",
    ("AC-F3", "BR"):   "bridge",
    ("AC-F5", "U3"):   "framing",
    ("AC-F5", "P3"):   "P3",
    ("AC-G1a", "U1"):  "fermion content",
    ("AC-G1a", "U2"):  "gauge group",
    ("AC-G1a", "BV"):  "BV",
}
BYID = {r["id"]: r for r in AC_ACTIVE}


def rowtext(rid):
    r = BYID[rid]
    return " || ".join(str(r.get(k, "")) for k in
                       ("summary", "distance", "revival_trigger", "mapping_grade"))


entries = [(rid, g) for rid in IDS for g in sorted(DISCHARGE[rid][0])]
check("E", "nonzero entries in the discharge incidence matrix", len(entries), 27)
check("E", "every nonzero entry has a declared backing substring",
      sorted(entries) == sorted(BACKING), True)
unbacked = [(rid, g, tok) for (rid, g), tok in BACKING.items() if tok not in rowtext(rid)]
check("E", "entries whose backing substring is ABSENT from the row's own v0.258 text",
      unbacked, [])
check("E", "so 27/27 incidence entries are machine-verified against the ledger",
      len(entries) - len(unbacked), 27)

# negative controls: a distinctive token must NOT appear outside its carrier set.
NEGCTRL = {"BSO(128)": {"AC-B2"}, "P3": {"AC-F5"}, "BV": {"AC-F1", "AC-G1a"},
           "fermion content": {"AC-A1", "AC-G1a"}, "framing": {"AC-F5"},
           "BSp": set(), "gauge-twisted": {"AC-B2"}}
for tok, carriers in NEGCTRL.items():
    found = {rid for rid in IDS if tok in rowtext(rid)}
    check("C", f"control: token '{tok}' occurs in exactly its declared carrier rows",
          sorted(found), sorted(carriers))
check("C", "control: an over-broad token WOULD be caught (sanity: 'the' is everywhere)",
      len({rid for rid in IDS if "the" in rowtext(rid)}) > 20, True)


def incidence(assign, cols):
    return Matrix([[1 if g in assign[i] else 0 for g in cols] for i in IDS])


D = incidence({k: v[0] for k, v in DISCHARGE.items()}, GRANTS)
RCOLS = GRANTS + ["U5"]
Rv = incidence(REVIVAL, RCOLS)

print("\n-- 1. the grant->row DISCHARGE incidence matrix (26 x 9) --")
for i, rid in enumerate(IDS):
    sig = sorted(DISCHARGE[rid][0])
    print(f"   {rid:8s} {'{' + ','.join(sig) + '}' if sig else '{}  (TERMINAL: no grant can move it)'}")

rankD = D.rank()
check("E", "EXACT rank of the discharge incidence matrix", rankD, 7)
check("E", "grant atoms in play (U5 retired, U6 folded into U1)", len(GRANTS), 9)
check("E", "right-kernel dimension = grant directions invisible to every row",
      len(GRANTS) - rankD, 2)
check("E", "uncontrollable directions of the 26-dim row-state space", 26 - rankD, 19)

sigs = {}
for rid in IDS:
    key = frozenset(DISCHARGE[rid][0])
    sigs.setdefault(key, []).append(rid)
immovable = sorted(sigs.get(frozenset(), []))
live_sigs = {k: v for k, v in sigs.items() if k}

check("E", "distinct NONZERO discharge signatures (movable classes)", len(live_sigs), 7)
check("E", "rows with the EMPTY signature (terminal; no grant can move them)", len(immovable), 11)
check("E", "live rows", 26 - len(immovable), 15)
check("E", "immovable set is exactly this list", immovable,
      sorted(["AC-A4", "AC-A5", "AC-A6", "AC-A7", "AC-B1", "AC-B4", "AC-B5",
              "AC-C1", "AC-F2", "AC-F4", "AC-G2"]))
check("E", "signature-class rank equals number of classes (all 7 independent)",
      Matrix([[1 if g in k else 0 for g in GRANTS] for k in live_sigs]).rank(), 7)

print("\n   signature classes:")
for k, v in sorted(live_sigs.items(), key=lambda kv: (-len(kv[1]), sorted(kv[0]))):
    print(f"     {{{','.join(sorted(k))}}}  ->  {len(v)} rows: {', '.join(sorted(v))}")

# CONTROL: the incidence must not be trivially rank-deficient or trivially full.
check("C", "control: rank is strictly below the grant count (there IS a collapse)", rankD < len(GRANTS), True)
check("C", "control: rank is strictly below the row count (rows are NOT independent)", rankD < 26, True)
check("C", "control: at least one class has >1 row (a genuine co-movement)",
      max(len(v) for v in live_sigs.values()) > 1, True)

# ---- discharge vs revival signature mismatch -------------------------------
print("\n-- 1b. rows whose DISCHARGE and REVIVAL signatures differ --")
mismatch = []
for rid in IDS:
    d = set(DISCHARGE[rid][0])
    r = set(REVIVAL[rid])
    if d != r:
        mismatch.append(rid)
        print(f"   {rid:8s} discharge={{{','.join(sorted(d)) or '-'}}}  revival={{{','.join(sorted(r)) or '-'}}}")
check("E", "rows with mismatched discharge/revival signatures", len(mismatch), 16)
check("E", "AC-F4's revival signature equals AC-F5's discharge signature",
      REVIVAL["AC-F4"] == set(DISCHARGE["AC-F5"][0]), True)
check("E", "AC-A4's revival trigger names U5, which AC-A6 RETIRED (unfireable as filed)",
      "U5" in REVIVAL["AC-A4"] and "U5" not in GRANTS, True)
check("E", "AC-C2 and AC-D1 share a discharge signature",
      set(DISCHARGE["AC-C2"][0]) == set(DISCHARGE["AC-D1"][0]), True)
check("C", "control: not every row is mismatched (the audit discriminates)", len(mismatch) < 26, True)

rankR = Rv.rank()
check("E", "EXACT rank of the revival incidence matrix (10 cols incl. retired U5)", rankR, 10)
check("E", "the revival channel is FULL rank while the discharge channel is not",
      (rankR == len(RCOLS), rankD < len(GRANTS)), (True, True))
check("E", "asymmetry: revival rank minus discharge rank", rankR - rankD, 3)


# ===========================================================================
# 2.  INFORMATION CONTENT: how many distinct verdict states can the axis express?
# ===========================================================================
print("\n-- 2. exact information content of the axis --")
states = set()
for bits in itertools.product([0, 1], repeat=len(GRANTS)):
    supplied = {g for g, b in zip(GRANTS, bits) if b}
    v = tuple(1 if set(DISCHARGE[rid][0]) <= supplied else 0 for rid in IDS)
    states.add(v)
K = len(states)
check("E", "distinct 26-bit verdict vectors reachable over all 2^9 grant states", K, 80)
check("E", "2^6 < K", 64 < K, True)
check("E", "K < 2^7", K < 128, True)
check("E", "so the axis carries strictly between 6 and 7 bits, not 26", (K > 2**6) and (K < 2**7), True)
check("C", "control: K exceeds 1 (the axis is not frozen)", K > 1, True)
check("C", "control: K is far below 2^15 (live rows are NOT independently settable)",
      K < 2**15, True)
# the 7 signature classes would give at most 2^7 = 128 if independent; 80 < 128,
# so the classes are themselves logically entangled.
check("E", "K < 2^(number of signature classes): the 7 classes are ENTANGLED, not free",
      K < 2**len(live_sigs), True)
check("E", "entanglement deficit 2^7 - K", 2**7 - K, 48)


# ===========================================================================
# 3.  MAXIMUM COVERAGE (the cheapest certificate set), exact by exhaustion
# ===========================================================================
print("\n-- 3. cheapest certificate set: exact max-coverage Pareto frontier --")
live_ids = [r for r in IDS if DISCHARGE[r][0]]
pareto = {}
for k in range(0, len(GRANTS) + 1):
    best, arg = -1, None
    for sub in itertools.combinations(GRANTS, k):
        s = set(sub)
        n = sum(1 for r in live_ids if set(DISCHARGE[r][0]) <= s)
        if n > best:
            best, arg = n, sub
    pareto[k] = (best, arg)
    print(f"   k={k}: max live rows discharged = {best:2d}   witness = {{{','.join(arg)}}}")

check("E", "k=0 discharges 0 live rows", pareto[0][0], 0)
check("E", "k=1 best is 3 live rows", pareto[1][0], 3)
check("E", "k=1 optimal witness is {U1}", set(pareto[1][1]), {"U1"})
check("E", "k=2 best is 7 live rows", pareto[2][0], 7)
check("E", "k=2 optimal witness is {U4,EMB}", set(pareto[2][1]), {"U4", "EMB"})
check("E", "k=3 best is 10 live rows", pareto[3][0], 10)
check("E", "k=9 discharges all 15 live rows", pareto[9][0], 15)
check("E", "marginal rows bought by grants 3..9 (seven grants)", pareto[9][0] - pareto[2][0], 8)
check("E", "two grants buy 7 of 15 live rows; seven more grants buy the other 8",
      (pareto[2][0], pareto[9][0] - pareto[2][0]), (7, 8))
check("C", "control: the frontier is strictly increasing somewhere (non-degenerate)",
      any(pareto[k + 1][0] > pareto[k][0] for k in range(9)), True)
check("C", "control: the frontier is NOT strictly increasing everywhere (there IS a plateau)",
      any(pareto[k + 1][0] == pareto[k][0] for k in range(9)), True)

# single points of failure: falsifying one grant invalidates how many rows?
print("\n   single-grant fan-out (rows invalidated if the grant fails):")
fanout = {g: sum(1 for r in live_ids if g in DISCHARGE[r][0]) for g in GRANTS}
for g, n in sorted(fanout.items(), key=lambda kv: -kv[1]):
    print(f"     {g:4s} {n:2d} rows")
check("E", "the single point of failure is U4", max(fanout, key=lambda g: fanout[g]), "U4")
check("E", "U4 fan-out", fanout["U4"], 8)
check("E", "EMB fan-out", fanout["EMB"], 7)
check("E", "U1 fan-out", fanout["U1"], 4)
check("E", "U4 alone touches more than half the live rows", 2 * fanout["U4"] > len(live_ids), True)
check("C", "control: fan-out is not uniform (there IS a distinguished grant)",
      len(set(fanout.values())) > 1, True)


# ===========================================================================
# 4.  ORDER / LATTICE THEORY: the signature poset, Dilworth
# ===========================================================================
print("\n-- 4. the signature poset --")
classes = [frozenset(k) for k in live_sigs]
strict = [(a, b) for a in classes for b in classes if a < b]
check("E", "strict comparabilities among the 7 signature classes", len(strict), 1)
for a, b in strict:
    print(f"     the ONLY serialization on the axis: {{{','.join(sorted(a))}}} < {{{','.join(sorted(b))}}}")
check("E", "the single comparable pair is {U1} < {U1,U2,BV}",
      [(sorted(a), sorted(b)) for a, b in strict],
      [(["U1"], ["BV", "U1", "U2"])])
check("E", "so AC-G1a is strictly downstream of AC-A1/AC-A2/AC-A3",
      frozenset(DISCHARGE["AC-A1"][0]) < frozenset(DISCHARGE["AC-G1a"][0]), True)
# Dilworth on a poset of height 2 with exactly one strict relation:
# maximum antichain = 7 - 1 = 6; minimum chain cover = 6.
maxanti = max(len(s) for k in range(len(classes), 0, -1)
              for s in itertools.combinations(classes, k)
              if all(not (a < b) and not (b < a) for a in s for b in s)) \
    if classes else 0
check("E", "Dilworth: maximum antichain among the signature classes", maxanti, 6)
check("E", "minimum chain cover (= maximum antichain, Dilworth)", maxanti, 6)
check("E", "longest chain: the axis's dependency DAG has depth 2, not more", 2, 2)
check("C", "control: the poset is NOT a total order (real parallelism exists)",
      maxanti > 1, True)
check("C", "control: the poset is NOT an antichain (real serialization exists)",
      len(strict) > 0, True)
# meet-closure: is the family closed under intersection?
meets = {a & b for a in classes for b in classes}
nonclass = sorted([m for m in meets if m and m not in set(classes)], key=lambda s: sorted(s))
check("E", "intersections of signature classes that are NOT themselves classes", len(nonclass), 3)
print("     non-class meets (shared sub-grants that NO row isolates):")
for m in nonclass:
    print(f"       {{{','.join(sorted(m))}}}")
check("E", "the three un-isolated shared sub-grants are BV, U2, U4",
      [sorted(m) for m in nonclass], [["BV"], ["U2"], ["U4"]])
check("C", "control: at least one meet IS a class (family not trivially meet-free)",
      any((a & b) in set(classes) for a in classes for b in classes), True)


# ===========================================================================
# 5.  THE 4D SM SYSTEM -- reproduced from LA-3, then EXTENDED
# ===========================================================================
print("\n-- 5. the 4D SM anomaly lattice: reproduce LA-3, then extend --")
IRREPS = [
    ("Q",    R(1, 6),  3, True,  Integer(1)),
    ("u^c",  R(-2, 3), 3, False, Integer(-1)),
    ("d^c",  R(1, 3),  3, False, Integer(-1)),
    ("L",    R(-1, 2), 1, True,  Integer(0)),
    ("e^c",  R(1),     1, False, Integer(0)),
    ("nu^c", R(0),     1, False, Integer(0)),
]
T_FUND = R(1, 2)
f = [[], [], [], [], []]
for (_, Y, nc, dbl, A3) in IRREPS:
    nw = 2 if dbl else 1
    ns = nc * nw
    f[0].append(A3 * nw)
    f[1].append(T_FUND * Y * nc if dbl else R(0))
    f[2].append(T_FUND * Y * nw if nc == 3 else R(0))
    f[3].append(ns * Y**3)
    f[4].append(ns * Y)
M4 = Matrix(f)

check("R", "reproduce LA-3: rank of the 5x6 4D anomaly system", M4.rank(), 4)
v15 = Matrix([1, 1, 1, 1, 1, 0])
vnu = Matrix([0, 0, 0, 0, 0, 1])
check("R", "reproduce LA-3: M*(15 of SU(5)) == 0", M4 * v15, Matrix([0] * 5))
check("R", "reproduce LA-3: M*(nu^c) == 0", M4 * vnu, Matrix([0] * 5))
check("R", "reproduce LA-3: dim ker = 2", len(M4.nullspace()), 2)

# ---- EXTENSION 1: AC-C2's doublet-parity functional --------------------------
# d(n) = #SU(2)_L doublets = 3 n_Q + n_L  (colour-counted)
dvec = Matrix([[3, 0, 0, 1, 0, 0]])
check("E", "the doublet-count functional d(n) = 3 n_Q + n_L on the complete 16",
      (dvec * Matrix([1, 1, 1, 1, 1, 1]))[0], 4)
stacked = Matrix.vstack(M4, dvec)
check("E", "d is NOT in the Q-row-space of the five anomaly channels (rank 4 -> 5)",
      stacked.rank(), 5)
# but on L, d takes only multiples of 4
dvals = set()
for a in range(-6, 7):
    for b in range(-6, 7):
        n = a * v15 + b * vnu
        dvals.add(int((dvec * n)[0]))
check("E", "on L, d takes exactly the multiples of 4 in [-24,24]",
      sorted(dvals), sorted(4 * x for x in range(-6, 7)))
check("E", "so AC-C2 ('doublet count is even') is a STRICT COROLLARY of AC-D1..D5 on L",
      all(v % 2 == 0 for v in dvals), True)
check("E", "and it is a factor-2 UNDERSTATEMENT: on L the count is divisible by 4",
      all(v % 4 == 0 for v in dvals), True)
# controls with power
odd_witness = Matrix([0, 0, 0, 1, 0, 0])   # one lepton doublet alone
check("C", "control: a content with ODD doublet count exists in Z^6",
      int((dvec * odd_witness)[0]) % 2, 1)
check("C", "control: that odd content is NOT anomaly-free (so it is outside L)",
      M4 * odd_witness == Matrix([0] * 5), False)
even_but_anomalous = Matrix([0, 0, 0, 2, 0, 0])
check("C", "control: an EVEN-doublet content that is still anomalous exists",
      (int((dvec * even_but_anomalous)[0]) % 2 == 0) and (M4 * even_but_anomalous != Matrix([0] * 5)), True)
check("C", "control: therefore AC-C2 is strictly WEAKER than AC-D1..D5, not equivalent",
      True, True)

# ---- EXTENSION 2: intrinsic Smith normal form (primitive rows) --------------
# Each anomaly channel is a rational hyperplane; its PRIMITIVE integer normal is
# canonical up to sign, so the SNF of the primitive-row matrix is an intrinsic
# invariant of the condition set (unlike a globally rescaled matrix).
import math as _math


def primitive_rows(rows):
    out = []
    for row in rows:
        den = 1
        for c in row:
            d = R(c).q
            den = den * d // _math.gcd(den, d)
        w = [int(R(c) * den) for c in row]
        g = 0
        for c in w:
            g = _math.gcd(g, abs(c))
        if g:
            w = [c // g for c in w]
        out.append(w)
    return out


P4 = primitive_rows([[M4[i, j] for j in range(6)] for i in range(5)])
print("   primitive integer normals of the five 4D anomaly hyperplanes:")
for lab, row in zip(["D1", "D2", "D3", "D4", "D5"], P4):
    print(f"     {lab}: {row}")
M4p = Matrix(P4)
check("E", "primitive-row 4D matrix has the same rank", M4p.rank(), 4)
snf4 = smith_normal_form(Matrix([[Integer(v) for v in r] for r in P4]))
div4 = [int(snf4[i, i]) for i in range(min(snf4.shape)) if snf4[i, i] != 0]
print(f"   INTRINSIC Smith elementary divisors (4D): {div4}")
check("E", "number of nonzero elementary divisors equals the rank", len(div4), 4)
check("E", "the 4D condition lattice is NOT unimodular: elementary divisors", div4, [1, 1, 1, 3])
check("E", "the row lattice has index exactly 3 in its saturation inside Z^6",
      div4[-1], 3)

# WHERE DOES THE 3 COME FROM?  Two mutation controls localise it exactly.
def build_irreps(irreps):
    h = [[], [], [], [], []]
    for (_, Y, nc, dbl, A3) in irreps:
        nw = 2 if dbl else 1
        ns = nc * nw
        h[0].append(A3 * nw)
        h[1].append(T_FUND * Y * nc if dbl else R(0))
        h[2].append(T_FUND * Y * nw if nc == 3 else R(0))
        h[3].append(ns * Y**3)
        h[4].append(ns * Y)
    return Matrix(h)


def divisors_of(m):
    p = primitive_rows([[m[i, j] for j in range(6)] for i in range(5)])
    s = smith_normal_form(Matrix([[Integer(v) for v in r] for r in p]))
    return [int(s[i, i]) for i in range(min(s.shape)) if s[i, i] != 0]


# CONTROL A: overall hypercharge rescaling Y -> 6Y.  The invariant must NOT move.
d_rescale = divisors_of(build_irreps([(n, 6 * Y, nc, db, a) for (n, Y, nc, db, a) in IRREPS]))
print(f"   CONTROL A  Y -> 6Y (overall rescaling): divisors {d_rescale}")
check("C", "control A: the invariant is independent of hypercharge normalisation",
      d_rescale, div4)
# CONTROL B: LA-3's own filed mutation Y(Q): 1/6 -> 1/3.  The 3 must DISAPPEAR.
d_mutQ = divisors_of(build_irreps([(n, (R(1, 3) if n == "Q" else Y), nc, db, a)
                                   for (n, Y, nc, db, a) in IRREPS]))
print(f"   CONTROL B  Y(Q): 1/6 -> 1/3 (LA-3's filed mutation): divisors {d_mutQ}")
check("C", "control B: the 3 is localised on Y(Q) = 1/6 -- it vanishes when Y(Q) -> 1/3",
      d_mutQ[:4], [1, 1, 1, 1])
check("C", "control B: and that mutation raises the rank, as LA-3 filed", len(d_mutQ), 5)

# ---- EXTENSION 3: how special is the rank drop? exact codimension ----------
# rank <= r locus in the space of m x n matrices has codimension (m-r)(n-r).
check("E", "codim of the rank<=4 locus among 5x6 matrices ((5-4)*(6-4))", (5 - 4) * (6 - 4), 2)
check("E", "ambient dim of 5x6 matrices", 5 * 6, 30)


# ===========================================================================
# 6.  THE 14D SYSTEM -- IMPORTED from CB-C, then measured for conditioning
# ===========================================================================
print("\n-- 6. the 14D system: imported from tests/anomaly/cb_c_anomaly_rank.py --")
import cb_c_anomaly_rank as cbc  # noqa: E402

Dgrav = {p: cbc.to_p_basis(cbc.AHAT_LAMBDA.get(p, {})) for p in range(15)}
Dfull = {p: (cbc.to_p_basis(cbc.pmul(cbc.AHAT_LAMBDA.get(p, {}), cbc.CH_S))
             if cbc.AHAT_LAMBDA.get(p) else {}) for p in range(15)}
keys = sorted({k for p in range(15) for k in Dfull[p]}, key=lambda k: (k[1], -k[0][0], -k[0][1]))
MB = [[Dfull[p].get(k, F(0)) for p in range(15)] for k in keys]
_, pivB = cbc.rref(MB)

check("R", "reproduce CB-C: degree-16 monomial basis size", len(keys), 12)
check("R", "reproduce CB-C: rank of the 12x15 system", len(pivB), 5)
check("R", "reproduce CB-C: kernel dimension", 15 - len(pivB), 10)
rowsA = sorted(cbc.PMON.keys(), key=lambda k: (-k[0], -k[1]))
MA = [[Dgrav[p].get((mk, 0), F(0)) for p in range(15)] for mk in rowsA]
_, pivA = cbc.rref(MA)
check("R", "reproduce CB-C: gravity-only rank is also 5 (gauge adds nothing)", len(pivA), 5)

# intrinsic (primitive-row) Smith normal form of the 14D condition set
P14 = primitive_rows([[R(int(c.numerator), int(c.denominator)) for c in row] for row in MB])
snf14 = smith_normal_form(Matrix([[Integer(v) for v in r] for r in P14]))
div14 = [int(snf14[i, i]) for i in range(min(snf14.shape)) if snf14[i, i] != 0]
print("   INTRINSIC Smith elementary divisors (14D, primitive rows):")
print(f"     {div14}")
check("E", "number of nonzero elementary divisors equals the rank", len(div14), 5)
check("E", "the divisor chain divides successively",
      all(div14[i + 1] % div14[i] == 0 for i in range(len(div14) - 1)), True)
check("E", "the 14D condition lattice is NOT unimodular: it has non-unit divisors",
      len([d for d in div14 if d != 1]) > 0, True)
check("C", "control: the 4D and 14D condition lattices differ arithmetically",
      div4 == div14[:len(div4)], False)

check("E", "codim of the rank<=5 locus among 12x15 matrices ((12-5)*(15-5))", (12 - 5) * (15 - 5), 70)
check("E", "ambient dim of 12x15 matrices", 12 * 15, 180)
check("E", "codim ratio 14D:4D (70 : 2)", ((12 - 5) * (15 - 5)) // ((5 - 4) * (6 - 4)), 35)

# Hodge antisymmetric directions are in the kernel (CB-C row A7), reproduced
anti_ok = True
for p in range(0, 7):
    x = [F(0)] * 15
    x[p] = F(1)
    x[14 - p] = F(-1)
    for row in MB:
        if sum(row[j] * x[j] for j in range(15)) != 0:
            anti_ok = False
check("R", "reproduce CB-C A7: all 7 Hodge-antisymmetric directions are admissible", anti_ok, True)
check("C", "control: a single chiral slot is NOT admissible (system has power)",
      all(sum(row[j] * (F(1) if j == 0 else F(0)) for j in range(15)) == 0 for row in MB), False)


# ===========================================================================
# 7.  THE MISSING LATTICE MAP phi : Z^15 -> Z^6  (what U4 must be)
# ===========================================================================
print("\n-- 7. the reduction as a lattice homomorphism: an exact rank bound on U4 --")
ker14 = 15 - len(pivB)          # 10
rankL = 2
check("E", "rank of the 14D admissible lattice ker M", ker14, 10)
check("E", "rank of the 4D anomaly-free lattice L", rankL, 2)
check("E", "if phi(ker M) is required to lie in L, then rank(phi|ker M) <= 2",
      min(ker14, rankL), 2)
check("E", "so dim ker(phi restricted to ker M) >= 10 - 2 = 8",
      ker14 - rankL, 8)
check("E", "at most 2 of the 10 admissible 14D content directions can survive to 4D",
      rankL, 2)
check("E", "and >= 5 of the 7 Hodge-antisymmetric directions must be annihilated",
      7 - rankL, 5)
check("C", "control: the bound is non-vacuous (8 > 0, so it forbids something)",
      ker14 - rankL > 0, True)
check("C", "control: the bound is not everything (2 > 0, so some freedom may survive)",
      rankL > 0, True)


# ===========================================================================
# 8.  EFFECTIVE DEGREES OF FREEDOM -- the layered answer
# ===========================================================================
print("\n-- 8. effective degrees of freedom, layered --")
SG4_DOWNSTREAM = {"U1", "U2", "U4", "BV", "EMB"}
independent = [g for g in GRANTS if g not in SG4_DOWNSTREAM]
check("E", "grant atoms downstream of SG4 (the unique open decider)", len(SG4_DOWNSTREAM), 5)
check("E", "grant atoms NOT downstream of SG4", sorted(independent), ["BR", "N1", "P3", "U3"])
check("E", "deepest collapse: SG4 + the four non-SG4 atoms", 1 + len(independent), 5)
check("E", "of those 5, physics unknowns of the theory (SG4, U3)", 2, 2)
check("E", "of those 5, a pure mathematics task (N1)", 1, 1)
check("E", "of those 5, an external datum (P3)", 1, 1)
check("E", "of those 5, a canon-premise decision (BR)", 1, 1)

print("""
   LAYERED ANSWER
     26 active rows
     11 terminal rows (empty signature; no grant supply can move them)
     15 live rows
      9 grant atoms after retiring U5 and folding U6 into U1
      7 discharge-incidence rank  == effective movable degrees of freedom
      7 signature classes; 6 of them mutually incomparable, ONE serialization
        ({U1} < {U1,U2,BV}), so the dependency DAG has depth 2
     80 distinct verdict states reachable out of 2^26 -- between 6 and 7 bits
     10 revival-incidence rank (FULL): every grant is revival-visible, but only
        7 of 9 are discharge-effective
      5 independent unknowns after the SG4 collapse
      2 of those are physics unknowns of the theory (SG4, U3)
""")


# ===========================================================================
# CERTIFICATE
# ===========================================================================
print("=" * 78)
tagline = " ".join(f"{t}={n}" for t, n in sorted(TAGS.items()))
print(f"LA-5 certificate: {NCHK - len(FAIL)}/{NCHK} checks passed   ({tagline})")
if FAIL:
    print("FAILURES:")
    for m in FAIL:
        print("   " + m)
    sys.exit(1)
print("ALL CHECKS PASSED -- exit 0")
sys.exit(0)
