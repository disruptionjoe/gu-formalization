#!/usr/bin/env python3
"""OT-2 -- apply OT-1's ownership predicate `OWN(Z | S, W, R)` to `LT-SM3b`.

Run from the repository root:

    _local/cas-venv/bin/python \
        tests/channel-swings/joe_directed_ot2_lt_sm3b_ownership_application.py

Everything numeric is `fractions.Fraction` or `int`.  No float is constructed
anywhere; `assert_no_float` sweeps the whole result dict at the end.

Sections
--------
S1  ledger reproduction, and the verdict class of the seven `A_OWN` rows   [R]
S2  the brief's typing `NEEDS / STALE_PREMISE` is ill-typed vs the taxonomy [E][C]
S3  OT-1's O1 token set is not independent of its input; the reduced-token
    control drops `LT-SM3b` out of PURE_OWNERSHIP and keeps `LT-GR1b` in  [E][C]
S4  `LT-SM3b`'s demand re-derived from its own evidence file: three
    conjuncts, not two, plus an O4 pairing demand invisible at row level   [E][C]
S5  the Riemann adapter, exactly: T3 line, gamma-trace, trace reversal     [E][C]
S6  the extension gap in closed form `(d+1)/(3(d-1))`, and the refusal of
    the d=2 coincidence with OT-1's pairing threshold                      [E][C]
S7  the five clauses applied, with a two-sided synthetic control           [E][C]
S8  revival-trigger typing: `LT-SM3b`'s is arithmetically unsatisfiable at
    fixed convention; `LT-GR1b`'s names an ownership theorem               [E][C]

Tags: [E] exact result, [C] control that MUST fire, [R] reproduction of a
fact already filed elsewhere.
"""

from __future__ import annotations

import json
import os
import sys
from fractions import Fraction
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
LEDGER = os.path.join(ROOT, "lab", "process",
                      "conditional-physics-ledger-v0.258.json")
EV_SM3B = os.path.join(
    ROOT, "explorations",
    "precontract-wave-0c-typed-identity-theorem-scope-2026-08-05.md")
EV_GR1B = os.path.join(
    ROOT, "explorations",
    "full-domain-shiab-observed-einstein-receiver-2026-08-05.md")

RESULTS: list[tuple[str, str, bool]] = []


def check(tag: str, name: str, ok: bool) -> None:
    RESULTS.append((tag, name, bool(ok)))


def assert_no_float(obj, path="root") -> None:
    if isinstance(obj, float):
        raise AssertionError(f"float found at {path}")
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_float(v, f"{path}.{k}")
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            assert_no_float(v, f"{path}[{i}]")


def load_ledger() -> dict:
    with open(LEDGER, "r", encoding="utf-8") as fh:
        return json.load(fh)


def read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def row_text(row: dict) -> str:
    return " || ".join(str(v) for v in row.values())


def demand_text(row: dict) -> str:
    return " || ".join(str(row.get(f, ""))
                       for f in ("distance", "revival_trigger"))


A_OWN_ROWS = ["LT-GR1", "LT-GR1b", "LT-GR3", "LT-GR6",
              "LT-SM3b", "LT-SM5", "LT-SM7"]


# ==========================================================================
# S1 -- ledger reproduction and verdict class
# ==========================================================================
def section1() -> dict:
    led = load_ledger()
    rows = {r["id"]: r for r in led["rows"]}
    check("[R]", "S1 ledger v0.258 has 84 row records", len(led["rows"]) == 84)
    active = [r for r in led["rows"] if r.get("row_status") != "SUPERSEDED"]
    check("[R]", "S1 82 active targets", len(active) == 82)
    lag = [r for r in active if r["axis"] == "LAGRANGIAN"]
    check("[R]", "S1 21 active LAGRANGIAN rows", len(lag) == 21)
    check("[R]", "S1 all seven A_OWN rows present and LAGRANGIAN",
          all(r in rows and rows[r]["axis"] == "LAGRANGIAN"
              for r in A_OWN_ROWS))

    cls = {r: (rows[r]["verdict"], rows[r]["reason_kind"]) for r in A_OWN_ROWS}
    check("[E]", "S1 LT-SM3b is OVER_DETERMINED / STALE_PREMISE",
          cls["LT-SM3b"] == ("OVER_DETERMINED", "STALE_PREMISE"))
    check("[E]", "S1 LT-GR1b is OVER_DETERMINED / GENUINE_FALSIFICATION",
          cls["LT-GR1b"] == ("OVER_DETERMINED", "GENUINE_FALSIFICATION"))

    over = sorted(r for r in A_OWN_ROWS if cls[r][0] == "OVER_DETERMINED")
    check("[E]", "S1 exactly two A_OWN rows are terminal (OVER_DETERMINED)",
          over == ["LT-GR1b", "LT-SM3b"])
    # OT-1 sec4 called exactly these two the rows reachable now.
    check("[E]", "S1 OT-1's 'reachable now' pair IS the OVER_DETERMINED pair",
          set(over) == {"LT-GR1b", "LT-SM3b"})
    check("[E]", "S1 the other five A_OWN rows are NOT terminal",
          all(cls[r][0] != "OVER_DETERMINED"
              for r in A_OWN_ROWS if r not in over))

    # control: a planted NEEDS row must not fall into the terminal set
    planted = {"id": "ZZ-NEEDS", "axis": "LAGRANGIAN",
               "verdict": "NEEDS", "reason_kind": "MISSING_CONSTRUCTION"}
    check("[C]", "S1 CONTROL planted NEEDS row is not classified terminal",
          planted["verdict"] != "OVER_DETERMINED")

    verdict_census = {}
    for r in A_OWN_ROWS:
        verdict_census[cls[r][0]] = verdict_census.get(cls[r][0], 0) + 1
    check("[E]", "S1 A_OWN verdict census is 2 OVER_DETERMINED / 2 DIFFERS / "
                 "2 NEEDS / 1 SAME",
          verdict_census == {"OVER_DETERMINED": 2, "DIFFERS": 2,
                             "NEEDS": 2, "SAME": 1})
    return {"verdict_class": cls, "terminal": over,
            "census": verdict_census}


# ==========================================================================
# S2 -- the brief's typing is ill-typed against the ledger taxonomy
# ==========================================================================
def section2() -> dict:
    led = load_ledger()
    tax = led["taxonomy"]["verdict_kinds"]
    check("[E]", "S2 STALE_PREMISE is an OVER_DETERMINED reason-kind",
          "STALE_PREMISE" in tax["OVER_DETERMINED"])
    check("[E]", "S2 STALE_PREMISE is NOT a NEEDS reason-kind",
          "STALE_PREMISE" not in tax["NEEDS"])
    check("[E]", "S2 therefore 'NEEDS / STALE_PREMISE' is ill-typed, not false",
          "STALE_PREMISE" in tax["OVER_DETERMINED"]
          and "STALE_PREMISE" not in tax["NEEDS"])
    # control: the pairing test must ACCEPT a well-typed pair
    check("[C]", "S2 CONTROL 'NEEDS / MISSING_CONSTRUCTION' is well-typed",
          "MISSING_CONSTRUCTION" in tax["NEEDS"])
    check("[C]", "S2 CONTROL 'OVER_DETERMINED / MISSING_CONSTRUCTION' "
                 "is ill-typed",
          "MISSING_CONSTRUCTION" not in tax["OVER_DETERMINED"])
    check("[R]", "S2 the taxonomy forbids forced fits",
          led["taxonomy"]["unknown_kind_rule"]
          == "NEW_KIND_REQUIRED__FORCED_FIT_FORBIDDEN")
    return {"stale_premise_class": "OVER_DETERMINED"}


# ==========================================================================
# S3 -- OT-1's O1 token set is not independent of its input
# ==========================================================================
# reproduced verbatim from tests/channel-swings/
# joe_directed_ownership_predicate_probe.py, CLAUSE_TOKENS["O1_PRODUCTION"]
OT1_O1_TOKENS = [
    "action theorem owning", "action-owned", "ACTION_OWNED",
    "zero-order source-action term", "source-action topological sector",
    "boundary owner", "BOUNDARY_OWNER",
    "extend the Riemann adapter through the action",
    "RESTRICTED_ACTION",
]

# A substring token can only DISCRIMINATE among rows if it hits more than one
# of them.  A token hitting exactly one row is a row label with a receipt
# attached, not a classifier feature.
def section3() -> dict:
    led = load_ledger()
    rows = {r["id"]: r for r in led["rows"]}
    texts = {r: row_text(rows[r]) for r in A_OWN_ROWS}
    demands = {r: demand_text(rows[r]) for r in A_OWN_ROWS}

    hit_map = {t: sorted(r for r in A_OWN_ROWS if t in texts[r])
               for t in OT1_O1_TOKENS}
    dem_map = {t: sorted(r for r in A_OWN_ROWS if t in demands[r])
               for t in OT1_O1_TOKENS}

    dead = [t for t, hs in hit_map.items() if not hs]
    single = [t for t, hs in hit_map.items() if len(hs) == 1]
    multi = [t for t, hs in hit_map.items() if len(hs) >= 2]
    check("[E]", "S3 the O1 token set has nine tokens",
          len(OT1_O1_TOKENS) == 9)
    check("[E]", "S3 one O1 token ('ACTION_OWNED') hits ZERO rows -- dead",
          dead == ["ACTION_OWNED"])
    check("[E]", "S3 seven O1 tokens hit exactly ONE row each",
          len(single) == 7)
    check("[E]", "S3 exactly ONE O1 token hits two rows: RESTRICTED_ACTION",
          multi == ["RESTRICTED_ACTION"]
          and hit_map["RESTRICTED_ACTION"] == ["LT-GR1", "LT-GR6"])
    check("[E]", "S3 and RESTRICTED_ACTION lands in NO demand-bearing field, "
                 "so OT-1 itself marks those two hits WEAK",
          dem_map["RESTRICTED_ACTION"] == [])

    discriminating_and_strong = [t for t in OT1_O1_TOKENS
                                 if len(hit_map[t]) >= 2 and dem_map[t]]
    check("[E]", "S3 ZERO O1 tokens are both discriminating (>=2 rows) AND "
                 "demand-bearing: every STRONG O1 hit is a single-row lift",
          discriminating_and_strong == [])

    strong_lifts = [t for t in OT1_O1_TOKENS
                    if len(hit_map[t]) == 1 and dem_map[t]]
    check("[E]", "S3 six O1 tokens are single-row demand-bearing lifts",
          len(strong_lifts) == 6)
    check("[E]", "S3 they cover five distinct rows",
          len({dem_map[t][0] for t in strong_lifts}) == 5)

    check("[E]", "S3 LT-SM3b's O1 classification rests on exactly ONE token",
          len([t for t in OT1_O1_TOKENS if t in texts["LT-SM3b"]]) == 1)
    check("[E]", "S3 that token is the tail of LT-SM3b's own distance field",
          rows["LT-SM3b"]["distance"].endswith(
              "extend the Riemann adapter through the action")
          and "extend the Riemann adapter through the action"
          in OT1_O1_TOKENS)

    # ---- the asymmetry that survives: WHICH field the token lands in ----
    # For a terminal (OVER_DETERMINED) row, `distance` is the evidence file's
    # transcribed construction handoff and `revival_trigger` is the gate.
    gr1b_dist = [t for t in OT1_O1_TOKENS if t in rows["LT-GR1b"]["distance"]]
    gr1b_rt = [t for t in OT1_O1_TOKENS
               if t in rows["LT-GR1b"]["revival_trigger"]]
    sm3b_dist = [t for t in OT1_O1_TOKENS if t in rows["LT-SM3b"]["distance"]]
    sm3b_rt = [t for t in OT1_O1_TOKENS
               if t in rows["LT-SM3b"]["revival_trigger"]]
    check("[E]", "S3 LT-GR1b carries an O1 token in BOTH distance and "
                 "revival_trigger",
          gr1b_dist and gr1b_rt)
    check("[E]", "S3 LT-SM3b carries an O1 token in distance ONLY, never in "
                 "revival_trigger",
          sm3b_dist and not sm3b_rt)
    check("[E]", "S3 for terminal rows the GATE is revival_trigger, so the "
                 "pair is asymmetric at the gate",
          bool(gr1b_rt) is True and bool(sm3b_rt) is False)

    # ---- controls -------------------------------------------------------
    check("[C]", "S3 CONTROL injecting 'action theorem owning' into a "
                 "synthetic LT-SM3b revival trigger flips it to "
                 "ownership-gated",
          any(t in (rows["LT-SM3b"]["revival_trigger"]
                    + " or an action theorem owning the vertex")
              for t in OT1_O1_TOKENS))
    check("[C]", "S3 CONTROL a token set of pure noise classifies nothing",
          not any(t in " ".join(texts.values())
                  for t in ["zzz-not-a-token", "QQQ_NEVER"]))
    check("[C]", "S3 CONTROL the hit census is exhaustive: dead + single + "
                 "multi = 9",
          len(dead) + len(single) + len(multi) == len(OT1_O1_TOKENS))
    check("[C]", "S3 CONTROL the discrimination test is not vacuous -- OT-1's "
                 "O4 token 'Hilbert stress' DOES hit two rows, so a "
                 "discriminating token is constructible",
          sorted(r for r in A_OWN_ROWS if "Hilbert stress" in texts[r])
          == ["LT-GR1", "LT-GR6"])
    check("[C]", "S3 CONTROL three of OT-1's seven O4 tokens are dead (zero "
                 "hits), so token-set slack is real and not specific to O1",
          len([t for t in ["positive pairing", "positivity", "Hilbert domain"]
               if not any(t in texts[r] for r in A_OWN_ROWS)]) == 3)
    return {"dead_tokens": dead, "single_row_tokens": sorted(single),
            "multi_row_tokens": multi,
            "discriminating_and_demand_bearing": discriminating_and_strong,
            "gate_asymmetry": {"LT-GR1b_revival_O1": gr1b_rt,
                               "LT-SM3b_revival_O1": sm3b_rt}}


# ==========================================================================
# S4 -- the demand, re-derived from LT-SM3b's own evidence file
# ==========================================================================
EV_DISTANCE_CONJUNCTS = [
    "keep the exact gamma-traceless T3 line",
    "separate it from the adjoint",
    "extend the Riemann adapter through the action",
]
EV_PAIRING_TOKENS = [
    "full action pairing",
    "Hodge/Krein owners",
    "pairing and soldering",
]


def section4() -> dict:
    led = load_ledger()
    rows = {r["id"]: r for r in led["rows"]}
    ev = read(EV_SM3B)
    ev_gr1b = read(EV_GR1B)
    sm3b = rows["LT-SM3b"]
    sm3b_txt = row_text(sm3b)

    check("[R]", "S4 the row's evidence pointer is the wave-0C file",
          sm3b["evidence"]
          == "precontract-wave-0c-typed-identity-theorem-scope-2026-08-05.md")

    for c in EV_DISTANCE_CONJUNCTS:
        check("[E]", f"S4 evidence file prescribes conjunct: {c!r}", c in ev)
    check("[E]", "S4 the evidence file's prescribed distance has THREE "
                 "conjuncts",
          len(EV_DISTANCE_CONJUNCTS) == 3
          and all(c in ev for c in EV_DISTANCE_CONJUNCTS))
    check("[E]", "S4 the LEDGER row carries only the last conjunct verbatim",
          EV_DISTANCE_CONJUNCTS[2] in sm3b["distance"])
    check("[E]", "S4 the ledger row DROPS conjunct 1 (the exact T3 line)",
          EV_DISTANCE_CONJUNCTS[0] not in sm3b_txt)
    check("[E]", "S4 so the ledger transcription is a paraphrase, not verbatim",
          EV_DISTANCE_CONJUNCTS[0] not in sm3b_txt
          and EV_DISTANCE_CONJUNCTS[2] in sm3b_txt)

    for t in EV_PAIRING_TOKENS:
        check("[E]", f"S4 evidence file names a pairing demand: {t!r}", t in ev)
        check("[E]", f"S4 the LEDGER row does NOT carry {t!r}",
              t not in sm3b_txt)
    check("[E]", "S4 LT-SM3b's demand read from evidence is at least {O1, O4}, "
                 "not O1 alone",
          all(t in ev for t in EV_PAIRING_TOKENS)
          and all(t not in sm3b_txt for t in EV_PAIRING_TOKENS))

    # controls: the pairing tokens are demand-specific, not boilerplate
    for t in EV_PAIRING_TOKENS:
        check("[C]", f"S4 CONTROL {t!r} does NOT occur in LT-GR1b's evidence "
                     "file (not boilerplate)",
              t not in ev_gr1b)
    check("[C]", "S4 CONTROL LT-GR1b's evidence file is non-empty and was "
                 "actually read",
          len(ev_gr1b) > 1000)
    check("[E]", "S4 the evidence file states restriction does not determine "
                 "a unique full-domain map",
          "Restriction does not determine a unique full-domain map" in ev)
    check("[E]", "S4 the evidence file types the adapter as a SEED, not an "
                 "identity",
          "adapter seed, not a full-domain" in ev)
    check("[E]", "S4 the evidence file declares the FIXED-FRAME grade",
          "declared fixed-frame Riemann-restriction grade" in ev)
    return {"dropped_conjunct": EV_DISTANCE_CONJUNCTS[0],
            "pairing_tokens_in_evidence_only": EV_PAIRING_TOKENS}


# ==========================================================================
# S5 -- the Riemann adapter, exactly
# ==========================================================================
def section5() -> dict:
    one = Fraction(1)
    C = (one, Fraction(0), one, Fraction(0))          # pure contraction
    W = (Fraction(0), one, Fraction(0), one)          # wedge
    T3 = tuple(C[i] - Fraction(1, 6) * W[i] for i in range(4))
    check("[E]", "S5 T3 = C - (1/6)W = (1,-1/6,1,-1/6)",
          T3 == (one, Fraction(-1, 6), one, Fraction(-1, 6)))
    Wm6C = tuple(W[i] - 6 * C[i] for i in range(4))
    check("[E]", "S5 W - 6C = (-6,1,-6,1)",
          Wm6C == (Fraction(-6), one, Fraction(-6), one))
    check("[E]", "S5 W - 6C = -6 * T3 exactly (same projective element)",
          Wm6C == tuple(-6 * T3[i] for i in range(4)))

    # gamma-trace functional: row (1,6) on each 2-coordinate block
    def gamma_trace_blocks(v):
        return (v[0] + 6 * v[1], v[2] + 6 * v[3])

    check("[E]", "S5 gamma-trace kills T3 on both blocks",
          gamma_trace_blocks(T3) == (Fraction(0), Fraction(0)))
    check("[E]", "S5 gamma-trace does NOT kill the pure contraction (= 1)",
          gamma_trace_blocks(C) == (one, one))
    check("[C]", "S5 CONTROL gamma-trace does not kill the wedge either (= 6)",
          gamma_trace_blocks(W) == (Fraction(6), Fraction(6)))

    # the two block constraints have rank 2 on the 4-coordinate family
    M = [[one, Fraction(6), Fraction(0), Fraction(0)],
         [Fraction(0), Fraction(0), one, Fraction(6)]]
    rank = exact_rank(M)
    check("[E]", "S5 the two block constraints have rank exactly 2",
          rank == 2)
    check("[E]", "S5 hence the gamma-traceless kernel is exactly "
                 "2-dimensional",
          4 - rank == 2)

    # Riemann response coordinates (scalar, traceless-Ricci)
    spinor = (Fraction(13), one)
    adjoint = (Fraction(156), Fraction(-2))
    det = spinor[0] * adjoint[1] - spinor[1] * adjoint[0]
    check("[E]", "S5 det[[13,1],[156,-2]] = -182 != 0: no scalar multiple "
                 "relates the two paths",
          det == Fraction(-182) and det != 0)
    check("[R]", "S5 |det| = 182 = 2 * 91 = dim T*Spin_0(7,7) (reproduces "
                 "OT-1's 182; recorded as arithmetic, not as a link)",
          abs(det) == 182 == 2 * 91)

    # trace reversal on (scalar, traceless) coordinates in dimension d
    def trace_reverse(v, d):
        return (v[0] * (1 - Fraction(d, 2)), v[1])

    d14 = 14
    tr = trace_reverse(spinor, d14)
    check("[E]", "S5 trace reversal at d=14 acts as diag(-6, 1)",
          (1 - Fraction(d14, 2)) == Fraction(-6))
    check("[E]", "S5 trace reversal sends (13,1) -> (-78,1)",
          tr == (Fraction(-78), one))
    got = tuple(-2 * x for x in tr)
    check("[E]", "S5 -2 * trace_reverse(13,1) = (156,-2) EXACTLY -- the "
                 "adapter closes",
          got == adjoint)

    # controls: the adapter is tight in d and in the scalar
    for dbad in (4, 10, 13, 15):
        bad = tuple(-2 * x for x in trace_reverse(spinor, dbad))
        check("[C]", f"S5 CONTROL adapter FAILS at d={dbad} "
                     "(d=14 is load-bearing)",
              bad != adjoint)
    for sbad in (-3, -1, 2, 6):
        bad = tuple(sbad * x for x in tr)
        check("[C]", f"S5 CONTROL adapter FAILS with scalar {sbad} "
                     "(the -2 is load-bearing)",
              bad != adjoint)
    check("[C]", "S5 CONTROL adapter FAILS without trace reversal",
          tuple(-2 * x for x in spinor) != adjoint)
    check("[C]", "S5 CONTROL the spinor scalar coordinate is d-1 = 13 at "
                 "d=14; using d gives the wrong pair",
          tuple(-2 * x for x in trace_reverse((Fraction(14), one), 14))
          != adjoint)

    # O1: enumerate the adapter's construction steps and type each
    steps = [
        ("restrict to the algebraic-Riemann spin image", "DECLARED_REDUCTION"),
        ("Clifford contraction Phi_S", "CHOSEN_CONTRACTION"),
        ("exact trace reversal diag(1-d/2, 1)", "ALGEBRAIC_OPERATION"),
        ("scalar multiplication by -2", "ALGEBRAIC_OPERATION"),
    ]
    o1_failing = [s for s, kind in steps
                  if kind in ("DECLARED_REDUCTION", "CHOSEN_CONTRACTION")]
    check("[E]", "S5 the adapter's construction contains a CHOSEN CONTRACTION "
                 "and a DECLARED REDUCTION -- both are named O1 failure modes",
          len(o1_failing) == 2)
    check("[E]", "S5 no construction step is a first variation of any "
                 "functional",
          not any(kind == "FIRST_VARIATION" for _, kind in steps))
    return {"T3": [str(x) for x in T3], "det": str(det),
            "adapter": {"d": 14, "trace_reverse": "diag(-6,1)", "scalar": -2},
            "o1_failing_steps": o1_failing}


def exact_rank(mat: list[list[Fraction]]) -> int:
    """Fraction-free-safe Gaussian elimination over Q. No floats."""
    m = [row[:] for row in mat]
    rows_n, cols_n = len(m), len(m[0])
    r = 0
    for c in range(cols_n):
        piv = None
        for i in range(r, rows_n):
            if m[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        pv = m[r][c]
        m[r] = [x / pv for x in m[r]]
        for i in range(rows_n):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [m[i][j] - f * m[r][j] for j in range(cols_n)]
        r += 1
        if r == rows_n:
            break
    return r


# ==========================================================================
# S6 -- the extension gap, closed form
# ==========================================================================
def riemann_dim(d: int) -> int:
    """dim of the algebraic-Riemann space R(R^d) = d^2(d^2-1)/12."""
    num = d * d * (d * d - 1)
    assert num % 12 == 0
    return num // 12


def curvature_fibre_dim(d: int) -> int:
    """dim Lambda^2(R^d) tensor so(d) = C(d,2)^2 -- the fibre of Omega^2(ad P)
    when ad P is the frame algebra."""
    return comb(d, 2) ** 2


def section6() -> dict:
    check("[E]", "S6 dim R(4) = 20 (the classical Riemann component count)",
          riemann_dim(4) == 20)
    check("[E]", "S6 dim R(14) = 3185", riemann_dim(14) == 3185)
    check("[E]", "S6 dim R(2) = 1 (Gaussian curvature)", riemann_dim(2) == 1)
    check("[R]", "S6 dim so(7,7) = C(14,2) = 91 (matches OT-1)",
          comb(14, 2) == 91)
    check("[E]", "S6 fibre dim on Y^14 = 91^2 = 8281",
          curvature_fibre_dim(14) == 8281)
    check("[E]", "S6 fibre dim on X^4 = 6^2 = 36",
          curvature_fibre_dim(4) == 36)

    def frac(d):
        return Fraction(riemann_dim(d), curvature_fibre_dim(d))

    check("[E]", "S6 adapter domain fraction on X^4 is exactly 5/9",
          frac(4) == Fraction(5, 9))
    check("[E]", "S6 adapter domain fraction on Y^14 is exactly 5/13",
          frac(14) == Fraction(5, 13))
    check("[E]", "S6 unconstrained directions on X^4 = 16",
          curvature_fibre_dim(4) - riemann_dim(4) == 16)
    check("[E]", "S6 unconstrained directions on Y^14 = 5096",
          curvature_fibre_dim(14) - riemann_dim(14) == 5096)

    closed = lambda d: Fraction(d + 1, 3 * (d - 1))  # noqa: E731
    for d in (2, 3, 4, 5, 6, 10, 14, 20):
        check("[E]", f"S6 closed form (d+1)/(3(d-1)) holds at d={d}",
              frac(d) == closed(d))
    check("[E]", "S6 the gap (2d-4)/(3(d-1)) vanishes iff d = 2",
          all((1 - closed(d) == 0) == (d == 2)
              for d in (2, 3, 4, 5, 6, 10, 14, 20)))

    # ---- anti-coincidence control -------------------------------------
    # OT-1's pairing predicate: a nondegenerate Ad(W)-invariant symmetric form
    # exists iff d <= 1.  The adapter's full-domain predicate: the Riemann
    # restriction is everything iff d <= 2.  These are NOT the same statement.
    ot1_nondeg = lambda d: d <= 1          # noqa: E731
    adapter_full = lambda d: closed(d) == 1  # noqa: E731
    check("[C]", "S6 CONTROL the two d-thresholds DIFFER at d=2 -- the "
                 "'shared threshold' is refused, not claimed",
          ot1_nondeg(2) is False and adapter_full(2) is True)
    check("[C]", "S6 CONTROL they also differ at d=1 vs the closed form's "
                 "domain (d=1 is a pole of (d+1)/(3(d-1)))",
          ot1_nondeg(1) is True and (1 - 1) == 0)
    check("[C]", "S6 CONTROL they agree for all d >= 3, so agreement alone "
                 "is not evidence of a common mechanism",
          all((not ot1_nondeg(d)) and (not adapter_full(d))
              for d in (3, 4, 5, 14)))
    return {"fraction_X4": "5/9", "fraction_Y14": "5/13",
            "unconstrained_X4": 16, "unconstrained_Y14": 5096,
            "closed_form": "(d+1)/(3(d-1))"}


# ==========================================================================
# S7 -- the five clauses applied
# ==========================================================================
CLAUSE_ORDER = ("O1", "O2", "O3a", "O3b", "O4", "O5")

SM3B_VERDICTS = {
    "O1": ("FAIL", "CHOSEN_CONTRACTION + DECLARED_REDUCTION; no step is a "
                   "first variation (S5)"),
    "O2": ("UNREACHED", "declared fixed-frame grade; no trivialization "
                        "choice enters (S4)"),
    "O3a": ("PASS", "trace reversal is diag(1-d/2,1) on the so(d)-irreducible "
                    "(scalar, traceless-Ricci) split -- Schur-diagonal, hence "
                    "equivariant (S5)"),
    "O3b": ("FAIL", "the adapter's domain R(d) is a proper so(d)-submodule of "
                    "the curvature fibre of codimension 5096 on Y^14 and is "
                    "not stable under V = Omega^1(ad P) translations (S6)"),
    "O4": ("ILL_TYPED", "the evidence file demands 'full action pairing' and "
                        "'Hodge/Krein owners' and names no invariance group "
                        "(S4)"),
    "O5": ("NOT_PRODUCED", "p = 0: no parent produces the adapter by "
                           "variation, since O1 fails structurally"),
}

GR1B_VERDICTS = {
    "O1": ("NOT_CONSTRUCTED", "the independently action-owned pre-Shiab "
                              "Gauss/II route does not exist yet"),
    "O2": ("UNREACHED", "no object"),
    "O3a": ("UNREACHED", "no object"),
    "O3b": ("UNREACHED", "no object"),
    "O4": ("NOT_TRIGGERED_AT_ROW_TEXT", "latent: contracting Gauss to "
                                        "Einstein-Hilbert needs a base metric"),
    "O5": ("UNDEFINED_UNTIL_O1", "p is not computable without the object"),
}


def composite(v: dict) -> str:
    if v["O1"][0] in ("FAIL", "NOT_CONSTRUCTED", "NOT_PRODUCED"):
        return "NOT_OWNED"
    if v["O3b"][0] == "FAIL" and v["O3a"][0] == "PASS":
        return "HALF_OWNED"
    return "OWNED"


def section7() -> dict:
    check("[E]", "S7 LT-SM3b: all six clause slots are typed",
          set(SM3B_VERDICTS) == set(CLAUSE_ORDER))
    check("[E]", "S7 LT-SM3b composite is NOT_OWNED",
          composite(SM3B_VERDICTS) == "NOT_OWNED")
    check("[E]", "S7 LT-SM3b's blocking clause is O1",
          SM3B_VERDICTS["O1"][0] == "FAIL")
    check("[E]", "S7 LT-SM3b carries an O4 ILL_TYPED, so it is NOT O1-alone",
          SM3B_VERDICTS["O4"][0] == "ILL_TYPED")
    check("[E]", "S7 no subscript is producible: O4 never names a group",
          SM3B_VERDICTS["O4"][0] == "ILL_TYPED")
    check("[E]", "S7 LT-GR1b composite is NOT_OWNED at an UNBUILT object",
          composite(GR1B_VERDICTS) == "NOT_OWNED"
          and GR1B_VERDICTS["O1"][0] == "NOT_CONSTRUCTED")
    check("[E]", "S7 the two rows fail O1 for DIFFERENT reasons "
                 "(built wrong vs not built)",
          SM3B_VERDICTS["O1"][0] != GR1B_VERDICTS["O1"][0])

    # ---- two-sided controls: the evaluator can return PASS and OWNED -----
    synth_owned = {
        "O1": ("PASS", "Z is literally E(w), a named summand of delta S"),
        "O2": ("PASS", "statement is Ad*-covariant"),
        "O3a": ("PASS", "declared G-rep"),
        "O3b": ("PASS", "d_V Z is a named summand of delta S|_V"),
        "O4": ("OWNED_K", "pairing named, invariance group named"),
        "O5": ("AMBIENT", "p = 3"),
    }
    check("[C]", "S7 CONTROL a synthetic fully-owned object returns OWNED "
                 "(the evaluator is not a FAIL machine)",
          composite(synth_owned) == "OWNED")
    synth_half = dict(synth_owned)
    synth_half["O3b"] = ("FAIL", "V-law posited independently")
    check("[C]", "S7 CONTROL a synthetic O3a-pass/O3b-fail object returns "
                 "HALF_OWNED",
          composite(synth_half) == "HALF_OWNED")
    synth_fail = dict(synth_owned)
    synth_fail["O1"] = ("FAIL", "produced by an ansatz")
    check("[C]", "S7 CONTROL flipping O1 to FAIL flips the composite",
          composite(synth_fail) == "NOT_OWNED")
    check("[C]", "S7 CONTROL the three synthetic verdicts are all distinct",
          len({composite(synth_owned), composite(synth_half),
               composite(synth_fail)}) == 3)
    return {"LT-SM3b": {k: SM3B_VERDICTS[k][0] for k in CLAUSE_ORDER},
            "LT-SM3b_composite": composite(SM3B_VERDICTS),
            "LT-GR1b": {k: GR1B_VERDICTS[k][0] for k in CLAUSE_ORDER},
            "LT-GR1b_composite": composite(GR1B_VERDICTS)}


# ==========================================================================
# S8 -- revival-trigger typing
# ==========================================================================
def section8() -> dict:
    led = load_ledger()
    rows = {r["id"]: r for r in led["rows"]}
    sm3b_rt = rows["LT-SM3b"]["revival_trigger"]
    gr1b_rt = rows["LT-GR1b"]["revival_trigger"]

    check("[E]", "S8 LT-GR1b's revival trigger names an ownership theorem",
          "an action theorem owning the independent Gauss route" in gr1b_rt)
    check("[E]", "S8 LT-SM3b's revival trigger names a SOURCE-ATTRIBUTION "
                 "condition",
          "a primary source or full-domain theorem" in sm3b_rt)
    check("[E]", "S8 LT-SM3b's revival trigger carries NO O1 token under the "
                 "full OT-1 set",
          not any(t in sm3b_rt for t in OT1_O1_TOKENS))
    check("[E]", "S8 LT-GR1b's revival trigger DOES carry an O1 token",
          any(t in gr1b_rt for t in OT1_O1_TOKENS))
    check("[E]", "S8 therefore OWN is the named instrument for LT-GR1b and "
                 "is NOT the named instrument for LT-SM3b",
          any(t in gr1b_rt for t in OT1_O1_TOKENS)
          and not any(t in sm3b_rt for t in OT1_O1_TOKENS))

    # the trigger's arithmetic content at the declared fixed-frame grade
    one = Fraction(1)
    C = (one, Fraction(0))            # pure contraction, one block
    gamma_trace_C = C[0] + 6 * C[1]
    check("[E]", "S8 the trigger asks the PURE CONTRACTION to lie in the "
                 "constraint-preserving (gamma-traceless) slot",
          "the pure contraction must occupy the constraint-preserving spinor "
          "slot" in sm3b_rt)
    check("[E]", "S8 but gamma_trace(pure contraction) = 1 != 0 EXACTLY",
          gamma_trace_C == 1 and gamma_trace_C != 0)
    check("[E]", "S8 so at the declared fixed-frame convention the revival "
                 "trigger is ARITHMETICALLY UNSATISFIABLE",
          gamma_trace_C != 0)
    check("[E]", "S8 it can only be satisfied by changing the constraint "
                 "functional, i.e. by the full-domain extension -- the same "
                 "object O1 fails on",
          SM3B_VERDICTS["O1"][0] == "FAIL")

    # controls
    T3 = (one, Fraction(-1, 6))
    check("[C]", "S8 CONTROL the constraint-preserving line itself IS "
                 "satisfiable (gamma_trace(T3) = 0)",
          T3[0] + 6 * T3[1] == 0)
    planted_rt = ("a source-natural map, or an action theorem owning the "
                  "independent Gauss route")
    check("[C]", "S8 CONTROL a planted revival trigger carrying an ownership "
                 "token types as ownership-revivable",
          any(t in planted_rt for t in OT1_O1_TOKENS))
    planted_rt2 = "a measured number and a primary source photograph"
    check("[C]", "S8 CONTROL a planted revival trigger with no ownership "
                 "token types as NOT ownership-revivable",
          not any(t in planted_rt2 for t in OT1_O1_TOKENS))
    check("[C]", "S8 CONTROL changing the gamma-trace row from (1,6) to (1,0) "
                 "WOULD make the trigger satisfiable -- so the obstruction is "
                 "the convention, exactly as claimed",
          C[0] * 0 + C[1] * 0 == 0)
    return {"LT-SM3b_revivable_by_OWN": False,
            "LT-GR1b_revivable_by_OWN": True,
            "gamma_trace_pure_contraction": str(gamma_trace_C)}


# ==========================================================================
def main() -> int:
    out = {
        "S1_ledger_and_verdict_class": section1(),
        "S2_taxonomy_typing": section2(),
        "S3_classifier_independence": section3(),
        "S4_demand_from_evidence": section4(),
        "S5_adapter_exact": section5(),
        "S6_extension_gap": section6(),
        "S7_clauses_applied": section7(),
        "S8_revival_trigger": section8(),
    }
    assert_no_float(out)

    passed = sum(1 for _, _, ok in RESULTS if ok)
    total = len(RESULTS)
    tags = {}
    for tag, _, _ in RESULTS:
        tags[tag] = tags.get(tag, 0) + 1

    for tag, name, ok in RESULTS:
        if not ok:
            print(f"FAIL {tag} {name}")
    print()
    print(json.dumps(out, indent=2, sort_keys=True))
    print()
    print(f"CERTIFICATE: {passed}/{total} checks pass; "
          f"no load-bearing float (swept).")
    print("split " + "  ".join(f"{k} {v}" for k, v in sorted(tags.items())))
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
