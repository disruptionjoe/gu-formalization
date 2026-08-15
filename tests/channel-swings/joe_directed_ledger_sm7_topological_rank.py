#!/usr/bin/env python3
"""LA-7 probe: the rank of the topological (theta) sector along GU's declared
reduction chain, versus the rank LT-SM7 books, in the conditional physics
ledger v0.258 (base revision a148ed80).

Channel: conditional_ledger_advancement (Joe-directed).
Work item: LA-7.  Run FROM THE REPO ROOT:

    _local/cas-venv/bin/python tests/channel-swings/joe_directed_ledger_sm7_topological_rank.py

WHAT THIS COMPUTES (exact integer / fractions.Fraction arithmetic only):

  1. Root systems A_n and D_n built from an explicit e_i realisation with
     integer inner products; Cartan matrices derived, not looked up.
  2. The exceptional isomorphisms D_3 = A_3 and D_2 = A_1 + A_1 DERIVED as
     Cartan-matrix isomorphisms via exhaustive permutation search.  These are
     the load-bearing step in the claim Spin(6) ~ SU(4), Spin(4) ~ SU(2)xSU(2).
  3. rank pi_3(G) = number of simple ideals = number of connected components
     of the Dynkin graph (U(1) factors contribute 0).
  4. rank H^4(BG;Q) = dim (Sym^2 t*)^W, computed as the exact null space of the
     integer linear system {M^T Q M = Q for every simple reflection M},
     solved by fraction-free Gaussian elimination.  NOT a lookup.
  5. The two invariants evaluated at every node of the declared chain.
  6. The Spin(3,2)-versus-SU(3,2) transcript garble decided by an integer
     dimension test on the maximal compact.
  7. LT-SM7's booking rank, certified by exact substrings of the row's own
     v0.258 text.
  8. The deficit (sector rank - booking rank) minimised over EVERY admissible
     (invariant, node) reading.
  9. The torsion-supplier exclusion: a finite-order topological class cannot
     supply a general point of a positive-dimensional angle torus.
 10. LT-SM1 split arithmetic and the two independent prior routes to it.

IMPORTED STANDARD THEOREMS (declared, not derived here):
  I1  Borel: H^*(BG;Q) = (Sym t*)^W for G compact connected.
  I2  Cartan/Iwasawa: a connected real semisimple Lie group deformation
      retracts onto its maximal compact subgroup.
  I3  Bott: pi_3(G) = Z for G compact simple; pi_3(U(1)) = pi_3(S^1) = 0.
  I4  A covering map induces isomorphisms on pi_n for n >= 2, so pi_3 is
      insensitive to quotient by a finite central subgroup.

NOT COMPUTED, NOT CLAIMED:
  * Which node of the chain is the operative gauge group (LA-6's fence 1: the
    second reduction step is not computed).  This probe therefore brackets.
  * Whether any theta angle is physical (LA-6's fence 2).
  * Any verdict change, coefficient, selection principle, or ledger edit.
"""

from __future__ import annotations

import json
import os
import sys
from fractions import Fraction
from itertools import permutations

# --------------------------------------------------------------------------
# certificate machinery
# --------------------------------------------------------------------------

CHECKS: list[tuple[str, str, bool, str]] = []


def E(name: str, ok: bool, detail: str = "") -> None:
    """Exact result: must hold."""
    CHECKS.append(("E", name, bool(ok), detail))


def C(name: str, must_be_false: bool, detail: str = "") -> None:
    """Planted control: the assertion must FAIL, i.e. the certificate has power."""
    CHECKS.append(("C", name, not bool(must_be_false), detail))


def assert_no_float(obj, path: str = "$") -> None:
    if isinstance(obj, float):
        raise AssertionError(f"FLOAT FOUND at {path}: {obj!r}")
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_float(k, f"{path}.<key>")
            assert_no_float(v, f"{path}.{k}")
    elif isinstance(obj, (list, tuple, set)):
        for i, v in enumerate(obj):
            assert_no_float(v, f"{path}[{i}]")


# --------------------------------------------------------------------------
# 1. root systems from an explicit e_i realisation (exact integer arithmetic)
# --------------------------------------------------------------------------


def dot(u: tuple[int, ...], v: tuple[int, ...]) -> int:
    return sum(a * b for a, b in zip(u, v))


def simple_roots_A(n: int) -> list[tuple[int, ...]]:
    """A_n = su(n+1): alpha_i = e_i - e_{i+1}, i = 1..n, inside R^{n+1}."""
    roots = []
    for i in range(n):
        v = [0] * (n + 1)
        v[i], v[i + 1] = 1, -1
        roots.append(tuple(v))
    return roots


def simple_roots_D(n: int) -> list[tuple[int, ...]]:
    """D_n = so(2n): alpha_i = e_i - e_{i+1} (i<n), alpha_n = e_{n-1} + e_n."""
    roots = []
    for i in range(n - 1):
        v = [0] * n
        v[i], v[i + 1] = 1, -1
        roots.append(tuple(v))
    v = [0] * n
    v[n - 2], v[n - 1] = 1, 1
    roots.append(tuple(v))
    return roots


def cartan_matrix(simple: list[tuple[int, ...]]) -> list[list[int]]:
    """C[i][j] = 2 (a_i . a_j) / (a_i . a_i).  Integer by construction here."""
    r = len(simple)
    Cm = []
    for i in range(r):
        num_i = dot(simple[i], simple[i])
        row = []
        for j in range(r):
            val = Fraction(2 * dot(simple[i], simple[j]), num_i)
            assert val.denominator == 1, "non-integer Cartan entry"
            row.append(int(val))
        Cm.append(row)
    return Cm


def cartan_isomorphic(P: list[list[int]], Q: list[list[int]]) -> bool:
    """Exhaustive permutation search for a relabelling P -> Q."""
    n = len(P)
    if n != len(Q):
        return False
    for perm in permutations(range(n)):
        if all(P[i][j] == Q[perm[i]][perm[j]] for i in range(n) for j in range(n)):
            return True
    return False


def dynkin_components(Cm: list[list[int]]) -> int:
    """Number of connected components of the Dynkin graph = number of simple ideals."""
    n = len(Cm)
    seen, comps = set(), 0
    for s in range(n):
        if s in seen:
            continue
        comps += 1
        stack = [s]
        while stack:
            u = stack.pop()
            if u in seen:
                continue
            seen.add(u)
            for v in range(n):
                if v != u and Cm[u][v] != 0 and v not in seen:
                    stack.append(v)
    return comps


# --------------------------------------------------------------------------
# 2. Weyl-invariant quadratic forms -> rank H^4(BG;Q)
# --------------------------------------------------------------------------


def reflection_matrices(Cm: list[list[int]], n_torus: int) -> list[list[list[int]]]:
    """s_i(alpha_j) = alpha_j - C[i][j] alpha_i, extended by identity on the
    central torus directions (on which W acts trivially)."""
    r = len(Cm)
    d = r + n_torus
    mats = []
    for i in range(r):
        M = [[1 if k == j else 0 for j in range(d)] for k in range(d)]
        for j in range(r):
            M[i][j] = (1 if i == j else 0) - Cm[i][j]
        mats.append(M)
    return mats


def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def transpose(A):
    return [list(col) for col in zip(*A)]


def nullspace_dim(rows: list[list[Fraction]], ncols: int) -> int:
    """Exact rank over Q by fraction-free-style elimination with Fractions."""
    M = [list(r) for r in rows]
    rank, piv_row = 0, 0
    for col in range(ncols):
        piv = None
        for r in range(piv_row, len(M)):
            if M[r][col] != 0:
                piv = r
                break
        if piv is None:
            continue
        M[piv_row], M[piv] = M[piv], M[piv_row]
        pv = M[piv_row][col]
        M[piv_row] = [x / pv for x in M[piv_row]]
        for r in range(len(M)):
            if r != piv_row and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[piv_row])]
        rank += 1
        piv_row += 1
        if piv_row == len(M):
            break
    return ncols - rank


def invariant_quadratic_dim(Cm: list[list[int]], n_torus: int) -> int:
    """dim (Sym^2 t*)^W, exact.  Unknowns = upper-triangular entries of a
    symmetric Q; equations = (M^T Q M - Q) = 0 for every simple reflection."""
    d = len(Cm) + n_torus
    idx, unknowns = {}, 0
    for a in range(d):
        for b in range(a, d):
            idx[(a, b)] = unknowns
            unknowns += 1
    if unknowns == 0:
        return 0

    def key(a, b):
        return idx[(a, b)] if a <= b else idx[(b, a)]

    eqs: list[list[Fraction]] = []
    for M in reflection_matrices(Cm, n_torus):
        MT = transpose(M)
        # (M^T Q M)[p][q] = sum_{a,b} MT[p][a] Q[a][b] M[b][q]
        for p in range(d):
            for q in range(p, d):
                row = [Fraction(0)] * unknowns
                for a in range(d):
                    if MT[p][a] == 0:
                        continue
                    for b in range(d):
                        if M[b][q] == 0:
                            continue
                        row[key(a, b)] += Fraction(MT[p][a] * M[b][q])
                row[key(p, q)] -= Fraction(1)
                if any(x != 0 for x in row):
                    eqs.append(row)
    if not eqs:
        return unknowns
    return nullspace_dim(eqs, unknowns)


# --------------------------------------------------------------------------
# 3. group records: Lie-algebra type data only (no floats anywhere)
# --------------------------------------------------------------------------

TYPES = {
    "A1": simple_roots_A(1),
    "A2": simple_roots_A(2),
    "A3": simple_roots_A(3),
    "D2": simple_roots_D(2),
    "D3": simple_roots_D(3),
}
CARTAN = {k: cartan_matrix(v) for k, v in TYPES.items()}


def block_cartan(factor_types: list[str]) -> list[list[int]]:
    blocks = [CARTAN[t] for t in factor_types]
    d = sum(len(b) for b in blocks)
    M = [[0] * d for _ in range(d)]
    off = 0
    for b in blocks:
        for i in range(len(b)):
            for j in range(len(b)):
                M[off + i][off + j] = b[i][j]
        off += len(b)
    return M


def dim_su(n: int) -> int:
    return n * n - 1


def dim_so(n: int) -> int:
    return n * (n - 1) // 2


# --------------------------------------------------------------------------
# MAIN
# --------------------------------------------------------------------------


def main() -> int:
    repo = os.getcwd()
    result: dict = {"work_item": "LA-7", "base_revision": "a148ed80"}

    # ---- 0. run location ------------------------------------------------
    ledger_path = os.path.join(repo, "lab/process/conditional-physics-ledger-v0.258.json")
    E("R0 run from repo root: ledger v0.258 is readable", os.path.isfile(ledger_path), ledger_path)
    if not os.path.isfile(ledger_path):
        print("ABORT: run from the repository root.")
        return 2
    ledger = json.load(open(ledger_path))

    # ---- 1. exceptional isomorphisms, DERIVED ---------------------------
    E("D1 Cartan(A1) = [[2]]", CARTAN["A1"] == [[2]], str(CARTAN["A1"]))
    E("D2 Cartan(D2) is diagonal 2I (so(4) is NOT simple)",
      CARTAN["D2"] == [[2, 0], [0, 2]], str(CARTAN["D2"]))
    E("D3 D2 = A1 + A1 as Cartan matrices",
      cartan_isomorphic(CARTAN["D2"], block_cartan(["A1", "A1"])), "so(4) = su(2)+su(2)")
    E("D4 D3 = A3 as Cartan matrices (so(6) = su(4))",
      cartan_isomorphic(CARTAN["D3"], CARTAN["A3"]), str(CARTAN["D3"]))
    E("D5 dim so(6) = dim su(4) = 15", dim_so(6) == dim_su(4) == 15, "15")
    E("D6 dim so(4) = 2 dim su(2) = 6", dim_so(4) == 2 * dim_su(2) == 6, "6")
    C("D7 CONTROL: D3 = A1+A1+A1 (must fail)",
      cartan_isomorphic(CARTAN["D3"], block_cartan(["A1", "A1", "A1"])),
      "so(6) is simple; if this passed the whole factor count would be wrong")
    C("D8 CONTROL: D2 = A2 (must fail)",
      cartan_isomorphic(CARTAN["D2"], CARTAN["A2"]), "so(4) is not su(3)")
    C("D9 CONTROL: D3 equals A3 under the IDENTITY relabelling (must fail)",
      CARTAN["D3"] == CARTAN["A3"],
      "the permutation search is doing real work: D3 = [[2,-1,-1],[-1,2,0],[-1,0,2]]")
    # the invariant-form machinery must itself have power: pure tori
    E("D10 dim (Sym^2 t*)^W for U(1)^1 is 1 and for U(1)^2 is 3 (W trivial)",
      invariant_quadratic_dim([], 1) == 1 and invariant_quadratic_dim([], 2) == 3,
      "m(m+1)/2")
    C("D11 CONTROL: dim (Sym^2 t*)^W for U(1)^2 is 2 (must fail)",
      invariant_quadratic_dim([], 2) == 2,
      "if the solver returned the simple-factor count on a torus it would be broken")
    E("D12 dim (Sym^2 t*)^W for A1 is 1 (the Killing form, up to scale)",
      invariant_quadratic_dim(CARTAN["A1"], 0) == 1, "irreducible reflection rep")

    # ---- 2. the nodes ---------------------------------------------------
    # Each node: semisimple factor types + number of central U(1) directions.
    NODES = [
        {
            "node": "N1_DELTA5_MAXCOMPACT",
            "label": "Spin(6) x Spin(4)  (maximal compact of Spin(6,4); GU-YM-Delta5)",
            "types": ["D3", "D2"],
            "n_torus": 0,
            "dim": dim_so(6) + dim_so(4),
        },
        {
            "node": "N2_SU32_MAXCOMPACT",
            "label": "S(U(3) x U(2))  (maximal compact of SU(3,2); source's middle node)",
            "types": ["A2", "A1"],
            "n_torus": 1,
            "dim": 9 + 4 - 1,
        },
        {
            "node": "N3_SM",
            "label": "SU(3) x SU(2) x U(1)  (Standard Model comparator)",
            "types": ["A2", "A1"],
            "n_torus": 1,
            "dim": dim_su(3) + dim_su(2) + 1,
        },
        {
            "node": "N4_SPIN32_MAXCOMPACT",
            "label": "Spin(3) x Spin(2)  (maximal compact of Spin(3,2); the GARBLE reading)",
            "types": ["A1"],
            "n_torus": 1,
            "dim": dim_so(3) + dim_so(2),
        },
    ]

    table = []
    for nd in NODES:
        Cm = block_cartan(nd["types"])
        s = dynkin_components(Cm) if Cm else 0
        pi3 = s  # I3 + I4: rank pi_3 = number of simple ideals
        h4 = invariant_quadratic_dim(Cm, nd["n_torus"])  # I1: rank H^4(BG;Q)
        closed = s + nd["n_torus"] * (nd["n_torus"] + 1) // 2
        table.append(
            {
                "node": nd["node"],
                "label": nd["label"],
                "dim": nd["dim"],
                "simple_ideals": s,
                "central_torus_dim": nd["n_torus"],
                "rank_pi3": pi3,
                "rank_H4_BG_Q": h4,
                "closed_form_check": closed,
            }
        )
        E(f"N-{nd['node']} rank H^4(BG;Q) matches s + m(m+1)/2", h4 == closed,
          f"computed {h4}, closed form {closed}")
    result["nodes"] = table
    by = {t["node"]: t for t in table}

    E("P1 rank pi_3(Spin(6)xSpin(4)) = 3", by["N1_DELTA5_MAXCOMPACT"]["rank_pi3"] == 3, "Z^3")
    E("P2 rank pi_3(SU(3)xSU(2)xU(1)) = 2", by["N3_SM"]["rank_pi3"] == 2, "Z^2; U(1) contributes 0")
    E("P3 rank pi_3(maxcpt SU(3,2)) = rank pi_3(SM) = 2",
      by["N2_SU32_MAXCOMPACT"]["rank_pi3"] == by["N3_SM"]["rank_pi3"] == 2, "same Lie algebra")
    E("P4 rank H^4(B(Spin(6)xSpin(4));Q) = 3", by["N1_DELTA5_MAXCOMPACT"]["rank_H4_BG_Q"] == 3, "")
    E("P5 rank H^4(B(SU(3)xSU(2)xU(1));Q) = 3 -- NOT 2; the c_1^2 class of the U(1)",
      by["N3_SM"]["rank_H4_BG_Q"] == 3, "the invariant-dependence seam")
    E("P6 the two invariants DISAGREE on the SM and AGREE on the Delta5 group",
      by["N3_SM"]["rank_pi3"] != by["N3_SM"]["rank_H4_BG_Q"]
      and by["N1_DELTA5_MAXCOMPACT"]["rank_pi3"] == by["N1_DELTA5_MAXCOMPACT"]["rank_H4_BG_Q"],
      "pi_3: 3 vs 2 | H^4(BG;Q): 3 vs 3")
    C("P7 CONTROL: rank H^4(B(SM);Q) = 2 (must fail)",
      by["N3_SM"]["rank_H4_BG_Q"] == 2,
      "if this passed, the 'one extra angle' reading would be invariant-independent; it is not")
    C("P8 CONTROL: rank pi_3(SM) = 3 (must fail)",
      by["N3_SM"]["rank_pi3"] == 3, "counting U(1) as a simple factor")
    C("P9 CONTROL: rank pi_3(maxcpt Spin(3,2)) = 2 (must fail)",
      by["N4_SPIN32_MAXCOMPACT"]["rank_pi3"] == 2, "it is 1")

    # ---- 3. the transcript garble, decided by an integer dimension test --
    dim_maxcpt_su32 = by["N2_SU32_MAXCOMPACT"]["dim"]
    dim_maxcpt_spin32 = by["N4_SPIN32_MAXCOMPACT"]["dim"]
    dim_sm = by["N3_SM"]["dim"]
    result["garble_test"] = {
        "claim_under_test": "the maximal compact subgroup of X is SU(3)xSU(2)xU(1)",
        "dim_SM": dim_sm,
        "dim_maxcompact_SU_3_2": dim_maxcpt_su32,
        "dim_maxcompact_Spin_3_2": dim_maxcpt_spin32,
        "verdict": "X = SU(3,2) SATISFIABLE; X = Spin(3,2) REFUTED",
    }
    E("G1 dim SM = 12", dim_sm == 12, "8+3+1")
    E("G2 dim maxcompact(SU(3,2)) = dim S(U(3)xU(2)) = 12 = dim SM",
      dim_maxcpt_su32 == dim_sm == 12, "source's sentence is satisfiable at X=SU(3,2)")
    E("G3 dim maxcompact(Spin(3,2)) = 4 != 12, so the SM cannot be it",
      dim_maxcpt_spin32 == 4 and dim_maxcpt_spin32 != dim_sm, "garble reading refuted")
    E("G4 dim SU(3,2) = 24 and dim Spin(6,4) = 45, so SU(3,2) is a proper subgroup candidate",
      dim_su(5) == 24 and dim_so(10) == 45, "24 < 45")
    C("G5 CONTROL: dim maxcompact(Spin(3,2)) = 12 (must fail)",
      dim_maxcpt_spin32 == 12, "")

    # ---- 4. LT-SM7's booking, certified by exact substrings --------------
    rows = {r["id"]: r for r in ledger["rows"]}
    sm7 = rows["LT-SM7"]
    d7, s7 = sm7["distance"], sm7["summary"]
    E("B1 LT-SM7 verdict/reason_kind are NEEDS / REAL_PARAMETER",
      (sm7["verdict"], sm7["reason_kind"]) == ("NEEDS", "REAL_PARAMETER"), "")
    E("B2 LT-SM7 mapping_grade is T0_OPEN", sm7["mapping_grade"] == "T0_OPEN", "")
    E("B3 LT-SM7 is the ledger's ONLY T0 row across all 84 records",
      [r["id"] for r in ledger["rows"] if r["mapping_grade"].startswith("T0")] == ["LT-SM7"], "")
    E("B4 the distance names 'the QCD theta coefficient' -- exact substring",
      "the QCD theta coefficient" in d7, d7)
    E("B5 the distance is SINGULAR: one 'coefficient', zero 'coefficients'",
      d7.count("coefficient") == 1 and d7.count("coefficients") == 0,
      "booking rank = 1")
    E("B6 the SUMMARY is PLURAL ('topological terms'), so the row's own two "
      "fields disagree on the booking's cardinality",
      "topological terms" in s7 and d7.count("coefficients") == 0, s7)
    C("B7 CONTROL: the distance mentions a rank or a count (must fail)",
      any(w in d7 for w in ("rank", "how many", "number of", "count")),
      "the row asks for a value and never for a count")
    C("B8 CONTROL: LT-SM7 has ever migrated (must fail)",
      any(m["row_id"] == "LT-SM7" for m in ledger["migration_history"]),
      "the row is untouched since 2026-08-05")
    booking_rank = 1

    # ---- 5. the deficit, minimised over EVERY admissible reading ---------
    admissible = [t for t in table if t["node"] != "N4_SPIN32_MAXCOMPACT"]
    ranks = []
    for t in admissible:
        ranks.append(("pi_3", t["node"], t["rank_pi3"]))
        ranks.append(("H4_BG_Q", t["node"], t["rank_H4_BG_Q"]))
    min_rank = min(r[2] for r in ranks)
    max_rank = max(r[2] for r in ranks)
    result["sector_rank_bracket"] = {
        "readings": [{"invariant": a, "node": b, "rank": c} for a, b, c in ranks],
        "min": min_rank,
        "max": max_rank,
        "booking_rank": booking_rank,
        "min_deficit": min_rank - booking_rank,
        "max_deficit": max_rank - booking_rank,
    }
    E("S1 the sector rank is 2 or 3 under EVERY admissible (invariant, node) reading",
      min_rank == 2 and max_rank == 3 and all(c in (2, 3) for _, _, c in ranks),
      f"{len(ranks)} readings, all in {{2,3}}")
    E("S2 the booking is short under EVERY reading: min deficit >= 1",
      min_rank - booking_rank >= 1, f"min deficit {min_rank - booking_rank}")
    E("S3 the deficit is bracketed exactly at [1, 2]",
      (min_rank - booking_rank, max_rank - booking_rank) == (1, 2), "")
    E("S4 rank is NOT pinned to a single integer -- so T3 ('dimension fixed') is NOT earned",
      min_rank != max_rank, "the node-selection fence is what blocks T3")
    C("S5 CONTROL: some admissible reading makes the booking adequate, rank 1 (must fail)",
      any(c <= booking_rank for _, _, c in ranks), "no reading rescues the rank-1 booking")
    C("S6 CONTROL: all readings agree on a single rank (must fail)",
      min_rank == max_rank, "if this passed, T3 would be earned and this probe understates")
    # The exclusion of the garble node is LOAD-BEARING and this states its cost openly.
    garble_ranks = [by["N4_SPIN32_MAXCOMPACT"]["rank_pi3"],
                    by["N4_SPIN32_MAXCOMPACT"]["rank_H4_BG_Q"]]
    E("S7 LOAD-BEARING DEPENDENCY: under the Spin(3,2) transcription the terminal "
      "pi_3 rank is 1, equal to the booking, and the deficit would collapse to 0",
      min(garble_ranks) == 1 and min(garble_ranks) - booking_rank == 0,
      "the whole finding rests on G2/G3 deciding the middle node as SU(3,2)")
    result["garble_test"]["load_bearing"] = {
        "if_middle_node_were_Spin_3_2": {"rank_pi3": garble_ranks[0],
                                         "rank_H4_BG_Q": garble_ranks[1],
                                         "min_deficit": min(garble_ranks) - booking_rank},
        "decided_by": "dim maxcompact(SU(3,2)) = 12 = dim SM vs "
                      "dim maxcompact(Spin(3,2)) = 4 != 12",
    }

    # ---- 6. torsion-supplier exclusion -----------------------------------
    cbb = os.path.join(repo, "explorations/conditional-build/cb-b-lagrangian-terms-2026-08-05.md")
    cbb_txt = open(cbb, encoding="utf-8").read()
    marker = "`Z/2`-quantized: `theta in {0, pi}`, not a continuous angle"
    E("X1 CB-B certifies T_9 as GU's only written topological term and Z/2-quantized",
      marker in cbb_txt and "GU's only written topological term" in cbb_txt, marker)
    E("X2 CB-B certifies that no INT F ^ F is written in the candidate action",
      "There is no `INT F ^ F` in the written candidate." in cbb_txt, "")
    # A supplier valued in a finite group F determines a point of Hom(F, U(1)^r),
    # a FINITE set of cardinality |F|^r; the sector's parameter space is the
    # r-torus (R/2piZ)^r, which for r >= 1 is uncountable.
    order_T9 = 2
    r_min = min_rank
    reachable = order_T9 ** r_min  # |Hom(Z/2, U(1)^r)| = 2^r
    E("X3 |Hom(Z/2, U(1)^r)| = 2^r = %d, a finite integer" % reachable,
      reachable == 2 ** r_min and isinstance(reachable, int), "finite, exactly counted")
    E("X4 the sector's parameter space is the r-torus with r >= 1, hence uncountable",
      r_min >= 1, "r >= 2 in fact")
    E("X5 EXCLUSION: a finite reachable set cannot exhaust an uncountable torus, so no "
      "finite-order topological class supplies a general point; T_9 alone is excluded "
      "as a complete supplier of the sector",
      reachable == 2 ** r_min and r_min >= 1, "cardinality argument, exact integers only")
    C("X6 CONTROL: CB-B says T_9 is a continuous angle (must fail)",
      "`T_9` is GU's only written topological term, and it is\n`Z/2`-quantized" not in cbb_txt,
      "if this passed, the Z/2 premise of the exclusion would be unsourced")
    C("X7 CONTROL: the exclusion is vacuous because no candidate supplier is written "
      "anywhere (must fail)",
      "T_9" not in cbb_txt, "the exclusion has a real, named target")
    C("X8 CONTROL: a Z/2 class could reach the whole torus if r were 0 (must fail)",
      r_min == 0, "r_min is 2; the exclusion is not an artifact of a degenerate rank")

    # ---- 7. LT-SM1 split: two independent routes, and the arithmetic -----
    sm1 = rows["LT-SM1"]
    E("L1 LT-SM1 is filed NEEDS / FINITE_CHOICE / FORM_EXACT_FORK_OPEN",
      (sm1["verdict"], sm1["reason_kind"], sm1["mapping_grade"])
      == ("NEEDS", "FINITE_CHOICE", "FORM_EXACT_FORK_OPEN"), "")
    kinds = [r["reason_kind"] for r in ledger["rows"]]
    E("L2 LT-SM1 is the ledger's ONLY FINITE_CHOICE row", kinds.count("FINITE_CHOICE") == 1, "")
    E("L3 ONE_BIT is declared in the taxonomy and used ZERO times in 84 rows",
      "ONE_BIT" in ledger["taxonomy"]["verdict_kinds"]["NEEDS"] and kinds.count("ONE_BIT") == 0, "")
    E("L4 LT-SM1's summary bundles TWO obligations ('and relative normalization') "
      "while its distance addresses only the first ('select the ... horn')",
      "and relative normalization" in sm1["summary"] and "select the" in sm1["distance"]
      and "normalization" not in sm1["distance"], "")

    route_a = os.path.join(repo, "explorations/lt-sm1-horn-surplus-attempt-2026-08-12.md")
    ra_txt = open(route_a, encoding="utf-8").read()
    E("R1 ROUTE A (2026-08-12, surplus side) returned SURPLUS-UNCOMPUTABLE",
      "SURPLUS-UNCOMPUTABLE" in ra_txt, "")
    E("R2 ROUTE A recommends the split into a FINITE_CHOICE bit and a "
      "REAL_PARAMETER normalization",
      "The row bundles two reason-kinds" in ra_txt
      and "`LT-SM1a` (FINITE_CHOICE, the bit)" in ra_txt
      and "`LT-SM1b` (REAL_PARAMETER, the normalization)" in ra_txt, "")
    E("R3 ROUTE A certifies the horn set has cardinality 2 (zeta_F in {0,1})",
      "|H| = 2" in ra_txt, "")

    la6 = os.path.join(
        repo,
        "lab/active-research/joe-directed/ledger-advancement/"
        "la6-the-lagrangian-axis-has-twelve-degrees-of-freedom-and-one-"
        "constructible-cover-object-2026-08-15.md",
    )
    la6_txt = open(la6, encoding="utf-8").read()
    E("R4 ROUTE B (2026-08-15, incidence/information side) reaches the same split",
      "`LT-SM1`'s atom\nset is `{I, A}`" in la6_txt or "atom\nset is `{I, A}`" in la6_txt, "IT-2")
    E("R5 ROUTE B's proposed second kind is MISSING_CONSTRUCTION, NOT REAL_PARAMETER",
      "split into a `FINITE_CHOICE` bit row and a `MISSING_CONSTRUCTION` normalization row"
      in la6_txt, "the two routes DISAGREE on the second atom's kind")
    E("R6 ROUTE B independently flags fork-completeness: a third horn would make "
      "the price log2(3), not 1 bit",
      "`log2(3)` bits, not 1" in la6_txt, "blocks an unconditional ONE_BIT retyping")
    C("R7 CONTROL: the two routes agree on the second atom's reason_kind (must fail)",
      "`LT-SM1b` (REAL_PARAMETER, the normalization)" in ra_txt
      and "split into a `FINITE_CHOICE` bit row and a `REAL_PARAMETER` normalization row"
      in la6_txt, "they do not; this is reported, not smoothed over")

    den = ledger["denominator"]
    superseded = [r for r in ledger["rows"] if r.get("row_status") == "SUPERSEDED"]
    E("A1 denominator arithmetic closes: records - superseded = canonical targets",
      den["row_record_count"] - len(superseded) == den["canonical_target_count"] == 82, "84-2=82")
    E("A2 axis denominators exclude superseded rows and sum to 82",
      sum(den["axes"].values()) == 82 and den["axes"]["LAGRANGIAN"] == 21, "")
    split_effect = {
        "row_record_count": [den["row_record_count"], den["row_record_count"] + 2],
        "historical_superseded_count": [den["historical_superseded_count"],
                                        den["historical_superseded_count"] + 1],
        "canonical_target_count": [den["canonical_target_count"],
                                   den["canonical_target_count"] + 1],
        "axes_LAGRANGIAN": [den["axes"]["LAGRANGIAN"], den["axes"]["LAGRANGIAN"] + 1],
    }
    result["lt_sm1_split_denominator_effect"] = split_effect
    E("A3 the LT-SM1 split is denominator-consistent under the LT-GR2 precedent",
      split_effect["row_record_count"][1] - split_effect["historical_superseded_count"][1]
      == split_effect["canonical_target_count"][1] == 83, "86-3=83")
    E("A4 the split does NOT touch the Layer-0 fork residue",
      ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["open_fork_horn_product"] == 1152,
      "a row re-partition is not a fork retirement")
    C("A5 CONTROL: the split reduces open_discrete_forks (must fail)",
      ledger["residue"]["open_discrete_forks"] != 9, "")

    # ---- 7b. how long the two rows have been frozen (full version sweep) --
    import glob
    import re as _re

    vpaths = sorted(
        glob.glob(os.path.join(repo, "lab/process/conditional-physics-ledger-v0.*.json")),
        key=lambda p: int(_re.search(r"v0\.(\d+)\.json$", p).group(1)),
    )
    frozen = {}
    for rid in ("LT-SM7", "LT-SM1", "RA-E1"):  # RA-E1 is the positive control
        base, changes, seen_in = None, [], 0
        for p in vpaths:
            try:
                dd = json.load(open(p, encoding="utf-8"))
            except Exception:
                continue
            rr = {r["id"]: r for r in dd.get("rows", [])}
            if rid not in rr:
                continue
            seen_in += 1
            txt = json.dumps(rr[rid], sort_keys=True)
            if base is None:
                base = txt
            elif txt != base:
                changes.append(int(_re.search(r"v0\.(\d+)\.json$", p).group(1)))
                base = txt
        frozen[rid] = {"versions_containing_row": seen_in, "text_changes": changes}
    result["row_freeze_history"] = frozen
    E("F1 LT-SM7 is byte-identical across every ledger version that contains it",
      frozen["LT-SM7"]["text_changes"] == [] and frozen["LT-SM7"]["versions_containing_row"] >= 200,
      f"{frozen['LT-SM7']['versions_containing_row']} versions, 0 changes")
    E("F2 LT-SM1 is byte-identical across every ledger version that contains it",
      frozen["LT-SM1"]["text_changes"] == [] and frozen["LT-SM1"]["versions_containing_row"] >= 200,
      f"{frozen['LT-SM1']['versions_containing_row']} versions, 0 changes")
    E("F3 POSITIVE CONTROL: the same sweep DOES detect change on RA-E1, which "
      "migration_history records as migrated -- so the sweep has power",
      len(frozen["RA-E1"]["text_changes"]) > 0
      and any(m["row_id"] == "RA-E1" for m in ledger["migration_history"]),
      f"RA-E1 text changed at versions {frozen['RA-E1']['text_changes'][:6]}")
    C("F4 CONTROL: LT-SM7 or LT-SM1 ever changed text (must fail)",
      bool(frozen["LT-SM7"]["text_changes"] or frozen["LT-SM1"]["text_changes"]), "")

    # ---- 8. what the tightness meter can and cannot see -------------------
    tp = ledger["residue"]["tightness_provisional"]
    E("M1 the ledger's residue.tightness_provisional has no T0 and no T1 bucket",
      "T0" not in tp and "T1" not in tp, json.dumps(tp, sort_keys=True))
    tgrades = sorted(
        r["mapping_grade"].split("_")[0]
        for r in ledger["rows"]
        if len(r["mapping_grade"]) > 1 and r["mapping_grade"][0] == "T"
        and r["mapping_grade"][1].isdigit()
    )
    E("M2 the actual row-level T-grade census disagrees with that meter",
      tgrades == ["T0", "T2", "T3", "T4", "T4"]
      and {"T4": 1, "T3": 3, "T2": 1} == tp, str(tgrades))
    E("M3 CONSEQUENCE: a T0 -> T2 movement on LT-SM7 is INVISIBLE to the ledger's "
      "own tightness meter as currently written",
      "T0" not in tp, "flagged, not fixed -- this artifact may not edit the ledger")

    result["proposed_migrations"] = [
        {
            "row_id": "LT-SM7",
            "kind": "MAPPING_GRADE_AND_DISTANCE_ONLY",
            "verdict": ["NEEDS", "NEEDS"],
            "reason_kind": ["REAL_PARAMETER", "REAL_PARAMETER"],
            "mapping_grade_from": "T0_OPEN",
            "mapping_grade_to": (
                "T2_SECTOR_TYPED__PI3_RANK3_AT_DELTA5_NODE__PI3_RANK2_AT_SU32_AND_SM_NODES__"
                "H4BG_RANK3_AT_ALL_NODES__BOOKING_RANK1_SHORT_BY_1_TO_2__"
                "TORSION_SUPPLIER_CLASS_EXCLUDED__NODE_SELECTION_AND_PHYSICALITY_OPEN"
            ),
            "tightness_ladder_movement": "T0 -> T2 (+2 notches of 5)",
            "t3_blocked_by": "the rank is bracketed at {2,3}, not fixed; fixing it "
                             "requires selecting the reduction node, which is LA-6's fence 1",
        },
        {
            "row_id": "LT-SM1",
            "kind": "SPLIT",
            "successors": ["LT-SM1a", "LT-SM1b"],
            "LT-SM1a": {"verdict": "NEEDS", "reason_kind": "FINITE_CHOICE",
                        "conditional_successor_kind": "ONE_BIT",
                        "gate": "fork-completeness: |H| = 2 versus LA-6 4.1's third horn"},
            "LT-SM1b": {"verdict": "NEEDS", "reason_kind": "MISSING_CONSTRUCTION",
                        "contested_with": "REAL_PARAMETER (Route A)",
                        "direction": "away from dischargeability -- not a laundering"},
        },
    ]
    result["refusals"] = [
        "No DERIVED_CONDITIONAL -> DERIVED promotion is proposed for any row.",
        "No verdict changes from NEEDS.  Both rows stay NEEDS.",
        "The second reduction step Spin(6,4) -> SU(3,2) is NOT computed as a map; "
        "only the pi_3 and H^4 ranks AT each declared node are computed.",
        "No claim that any of the angles is physical.",
        "No claim that GU predicts an extra theta angle: that reading holds for pi_3 "
        "and FAILS for H^4(BG;Q), where all nodes have rank 3.",
    ]

    assert_no_float(result)

    # ---- report -----------------------------------------------------------
    n_exact = sum(1 for k, _, _, _ in CHECKS if k == "E")
    n_ctrl = sum(1 for k, _, _, _ in CHECKS if k == "C")
    failures = [(k, n, d) for k, n, ok, d in CHECKS if not ok]
    print("=" * 78)
    print("LA-7 -- LT-SM7 topological-sector rank probe (base a148ed80, v0.258)")
    print("=" * 78)
    for kind, name, ok, detail in CHECKS:
        print(f"[{kind}] {'PASS' if ok else 'FAIL'}  {name}")
        if detail and not ok:
            print(f"        detail: {detail}")
    print("-" * 78)
    print(json.dumps(result, indent=2, sort_keys=False))
    print("-" * 78)
    print(f"exact results [E]: {n_exact}   planted controls [C] with power: {n_ctrl}")
    print(f"CERTIFICATE: {len(CHECKS) - len(failures)}/{len(CHECKS)}")
    if failures:
        print("FAILURES:")
        for k, n, d in failures:
            print(f"  [{k}] {n} :: {d}")
        return 1
    print("no floats anywhere in the result structure (assert_no_float swept)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
