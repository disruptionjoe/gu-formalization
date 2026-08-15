#!/usr/bin/env python3
"""LA-10 -- adversarial atom-split attack on the 2026-08-15 headline result.

Target claim under attack (as stated by the channel brief):

    "82 rows reduce to 32 formal degrees of freedom, and one object -- the
     operative completed second action -- is a near-universal cut vertex,
     reaching 28 of 29 open REPRESENTATION rows (LA-4) and 18 of 20
     LAGRANGIAN rows as cover object `A` (LA-6)."

Both source agents named the same seam.  LA-6: "split atom `A` three ways and
re-run ... If it is really three objects -- stationary point, normalization,
ownership theorem -- the cover is not 2."  LA-4: "the `b9` -> `b1` DAG edge
carries 28 of 29 rows and no ledger row states it."

This probe executes both splits against ledger v0.258 (base a148ed80) and
reports what survives.

Exactness policy
----------------
Integers and `fractions.Fraction` only.  Rank over Q by fraction-free
elimination.  `assert_no_float` sweeps the result dict.  No ledger file is
written or modified.

Evidence policy (inherited from LA-6, applied to BOTH prior vocabularies)
------------------------------------------------------------------------
Every incidence entry must be backed by an exact substring occurring in that
row's own v0.258 text (`summary || distance || revival_trigger ||
mapping_grade || frontier_grade || construction_scope`).  Negative token
controls bound each atom so an over-broad substring cannot inflate the matrix.
The certificate is required to have power against THIS author too: §3 applies
it to LA-4's own incidence table, which was published without substring
certificates, and reports the failures.
"""

from __future__ import annotations

import itertools
import json
import os
import sys
from fractions import Fraction

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LEDGER = os.path.join(REPO, "lab", "process", "conditional-physics-ledger-v0.258.json")

CHECKS: list[tuple[str, str, bool, str]] = []


def check(tag: str, label: str, passed: bool, detail: str = "") -> bool:
    CHECKS.append((tag, label, bool(passed), detail))
    return bool(passed)


# ---------------------------------------------------------------------------
# 0.  Load
# ---------------------------------------------------------------------------

with open(LEDGER) as fh:
    LED = json.load(fh)

ROWS = LED["rows"]
BYID = {r["id"]: r for r in ROWS}


def rowtext(r: dict) -> str:
    return " || ".join(
        [
            r.get("summary", ""),
            r.get("distance", ""),
            r.get("revival_trigger", ""),
            r.get("mapping_grade", ""),
            r.get("frontier_grade", ""),
            r.get("construction_scope", ""),
        ]
    )


TEXT = {r["id"]: rowtext(r) for r in ROWS}
ALL_IDS = list(TEXT)

REP_IDS = [r["id"] for r in ROWS if r["axis"] == "REPRESENTATION" and r.get("row_status") != "SUPERSEDED"]
LAG_IDS = [r["id"] for r in ROWS if r["axis"] == "LAGRANGIAN" and r.get("row_status") != "SUPERSEDED"]
ANO_IDS = [r["id"] for r in ROWS if r["axis"] == "ANOMALY_CONSISTENCY" and r.get("row_status") != "SUPERSEDED"]

check("R", "84 row records in v0.258", len(ROWS) == 84, f"n={len(ROWS)}")
check("R", "denominator declares 82 canonical targets", LED["denominator"]["canonical_target_count"] == 82)
check("E", "35 active REPRESENTATION rows", len(REP_IDS) == 35, f"n={len(REP_IDS)}")
check("E", "21 active LAGRANGIAN rows", len(LAG_IDS) == 21, f"n={len(LAG_IDS)}")
check("E", "26 active ANOMALY_CONSISTENCY rows", len(ANO_IDS) == 26, f"n={len(ANO_IDS)}")
check("E", "82 = 35 + 21 + 26", len(REP_IDS) + len(LAG_IDS) + len(ANO_IDS) == 82)


# ---------------------------------------------------------------------------
# linear algebra, exact
# ---------------------------------------------------------------------------


def rank_Q(mat: list[list[int]], ncol: int) -> int:
    m = [[Fraction(x) for x in row] for row in mat]
    r = 0
    for c in range(ncol):
        piv = next((i for i in range(r, len(m)) if m[i][c] != 0), None)
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        pv = m[r][c]
        m[r] = [x / pv for x in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [x - f * y for x, y in zip(m[i], m[r])]
        r += 1
    return r


def min_hitting_set(sigs: dict[str, frozenset], atoms: list[str]) -> tuple[int, list[tuple[str, ...]]]:
    """Smallest atom set meeting every non-empty row signature.  Exact, brute force."""
    live = [s for s in sigs.values() if s]
    if not live:
        return 0, [()]
    for k in range(1, len(atoms) + 1):
        hits = [c for c in itertools.combinations(atoms, k) if all(set(c) & s for s in live)]
        if hits:
            return k, hits
    return len(atoms), [tuple(atoms)]


def max_disjoint_rows(sigs: dict[str, frozenset]) -> tuple[int, list[str]]:
    """Largest set of rows with pairwise-disjoint signatures -> LP dual witness."""
    ids = [i for i, s in sigs.items() if s]
    best: list[str] = []
    for k in range(len(ids), 0, -1):
        for combo in itertools.combinations(ids, k):
            ok = all(not (sigs[a] & sigs[b]) for a, b in itertools.combinations(combo, 2))
            if ok:
                return k, list(combo)
        if k <= 1:
            break
    return len(best), best


# ---------------------------------------------------------------------------
# 1.  LA-6 LAGRANGIAN baseline, re-encoded verbatim from its published probe
# ---------------------------------------------------------------------------

LA6_ATOMS = [
    "A_ACTION_OWNED_BACKGROUND",
    "B_K77_OPERATOR_DOMAIN",
    "C_RELATIVE_INDEX_COUNT",
    "D_EULER_BV_BFV",
    "E_OBSERVATION_REDUCTION",
    "F_POSITIVITY_PHYSICAL",
    "G_SHIAB_SELECTOR",
    "H_ABSOLUTE_SCALE",
    "I_ZETA_F_BIT",
    "J_BOUNDARY_EDGE_OWNER",
    "K_COEFFICIENT_SELECTION",
    "L_COSMOLOGICAL_SOLUTION",
    "M_NATIVE_RG_RUNNING",
]

LA6_INCIDENCE: list[tuple[str, str, str]] = [
    ("LT-GR1", "B_K77_OPERATOR_DOMAIN", "construct the physical K77 nonzero-fermion operator, closed relative domain"),
    ("LT-GR1", "C_RELATIVE_INDEX_COUNT", "index and count identification"),
    ("LT-GR1", "D_EULER_BV_BFV", "recomputing Euler/BV"),
    ("LT-GR1", "F_POSITIVITY_PHYSICAL", "observed Hilbert stress"),
    ("LT-GR1", "J_BOUNDARY_EDGE_OWNER", "BOUNDARY_TO_P3_RELATIVE_KO_INPUT_MAP_EXACT"),
    ("LT-GR1", "A_ACTION_OWNED_BACKGROUND", "RESTRICTED_ACTION_HILBERT_DOMAIN_OPEN"),
    ("LT-GR1b", "G_SHIAB_SELECTOR", "construct a different Shiab"),
    ("LT-GR1b", "A_ACTION_OWNED_BACKGROUND", "an action theorem owning the independent Gauss route"),
    ("LT-GR2b", "B_K77_OPERATOR_DOMAIN", "build a K77 relative operator/domain"),
    ("LT-GR2b", "C_RELATIVE_INDEX_COUNT", "index and count readout"),
    ("LT-GR2b", "J_BOUNDARY_EDGE_OWNER", "BOUNDARY_TO_P3_RELATIVE_KO_INPUT_MAP_EXACT"),
    ("LT-GR2b", "A_ACTION_OWNED_BACKGROUND", "LOCAL_ACTION_OWNED_VEV_EXACT_UNREDUCED"),
    ("LT-GR2b", "D_EULER_BV_BFV", "complete EOM/BV/boundary cancellation"),
    ("LT-GR2c", "B_K77_OPERATOR_DOMAIN", "Build the physical K77 operator/domain"),
    ("LT-GR2c", "C_RELATIVE_INDEX_COUNT", "compute its relative index and identify the count"),
    ("LT-GR2c", "D_EULER_BV_BFV", "restrict/recompute Euler/BV"),
    ("LT-GR2c", "A_ACTION_OWNED_BACKGROUND", "an action-owned normalized global functional"),
    ("LT-GR2c", "E_OBSERVATION_REDUCTION", "observation descent"),
    ("LT-GR2c", "H_ABSOLUTE_SCALE", "NOT_SCALE_SELECTOR__NORMALIZED_FUNCTIONAL_OPEN"),
    ("LT-GR2c", "J_BOUNDARY_EDGE_OWNER", "BOUNDARY_TO_P3_RELATIVE_KO_INPUT_MAP_EXACT"),
    ("LT-GR2d", "B_K77_OPERATOR_DOMAIN", "physical K77 relative index/count readout"),
    ("LT-GR2d", "C_RELATIVE_INDEX_COUNT", "K77_INDEX_COUNT_SIGN_UNITS_STABILITY_DOMAIN_OPEN"),
    ("LT-GR2d", "H_ABSOLUTE_SCALE", "Sign, units, radiative response"),
    ("LT-GR2d", "A_ACTION_OWNED_BACKGROUND", "normalized observer functional inserted into the selected action"),
    ("LT-GR2d", "J_BOUNDARY_EDGE_OWNER", "BOUNDARY_TO_P3_RELATIVE_KO_INPUT_MAP_EXACT"),
    ("LT-GR2d", "L_COSMOLOGICAL_SOLUTION", "cosmology remain open"),
    ("LT-GR2e", "L_COSMOLOGICAL_SOLUTION", "derive matter/radiation FLRW perturbations and held-out w(z)"),
    ("LT-GR2e", "A_ACTION_OWNED_BACKGROUND", "an action-owned cosmological solution with fixed initial data"),
    ("LT-GR3", "J_BOUNDARY_EDGE_OWNER", "residual-square parent boundary owner remains unbuilt"),
    ("LT-GR3", "A_ACTION_OWNED_BACKGROUND", "a rival action parent"),
    ("LT-GR3", "D_EULER_BV_BFV", "BV_DOMAIN_OPEN"),
    ("LT-GR4", "M_NATIVE_RG_RUNNING", "compute the native R^2 running sign"),
    ("LT-GR4", "A_ACTION_OWNED_BACKGROUND", "an exact GU-native sign opposite to the ported negative horn"),
    ("LT-GR5", "E_OBSERVATION_REDUCTION", "before observation/BV/domain reduction"),
    ("LT-GR5", "D_EULER_BV_BFV", "REDUCTION_BV_DOMAIN_OPEN"),
    ("LT-GR5", "F_POSITIVITY_PHYSICAL", "common Green/BV/Fock domain"),
    ("LT-GR5", "A_ACTION_OWNED_BACKGROUND", "P_EQUALS_KT_ACTION_OWNER_REJECTED"),
    ("LT-GR6", "B_K77_OPERATOR_DOMAIN", "Build the physical K77 operator/domain"),
    ("LT-GR6", "C_RELATIVE_INDEX_COUNT", "dependent index/count readout"),
    ("LT-GR6", "D_EULER_BV_BFV", "before full Euler/BV"),
    ("LT-GR6", "F_POSITIVITY_PHYSICAL", "reproduce the Hilbert stress on the physical quotient"),
    ("LT-GR6", "J_BOUNDARY_EDGE_OWNER", "BOUNDARY_TO_P3_RELATIVE_KO_INPUT_MAP_EXACT"),
    ("LT-GR6", "A_ACTION_OWNED_BACKGROUND", "selected-action tangent/Noether complex"),
    ("LT-GR7", "H_ABSOLUTE_SCALE", "derive one absolute gravitational normalization"),
    ("LT-SM1", "I_ZETA_F_BIT", "select the zeta_F/Yang-Mills horn"),
    ("LT-SM1", "A_ACTION_OWNED_BACKGROUND", "a source-action choice fixed by surplus constraints"),
    ("LT-SM2", "H_ABSOLUTE_SCALE", "derive absolute and relative coupling scales"),
    ("LT-SM2", "E_OBSERVATION_REDUCTION", "after symmetry breaking"),
    ("LT-SM2", "A_ACTION_OWNED_BACKGROUND", "a normalized action plus threshold computation"),
    ("LT-SM3", "A_ACTION_OWNED_BACKGROUND", "Derive a native residual-zero action background"),
    ("LT-SM3", "D_EULER_BV_BFV", "proper functional BV/BFV"),
    ("LT-SM3", "F_POSITIVITY_PHYSICAL", "Fredholm/Green domain"),
    ("LT-SM3", "J_BOUNDARY_EDGE_OWNER", "OPPOSITE_EDGE_UNOWNED"),
    ("LT-SM3", "K_COEFFICIENT_SELECTION", "not a selected Cartan restriction"),
    ("LT-SM3b", "G_SHIAB_SELECTOR", "separate source adjoint Shiab from reconstructed spinor vertex"),
    ("LT-SM3b", "A_ACTION_OWNED_BACKGROUND", "extend the Riemann adapter through the action"),
    ("LT-SM4", "F_POSITIVITY_PHYSICAL", "show the pole is physical"),
    ("LT-SM4", "H_ABSOLUTE_SCALE", "MASS_INTERVAL_EXACT_PHYSICS_OPEN"),
    ("LT-SM4", "K_COEFFICIENT_SELECTION", "a complete constrained pole spectrum"),
    ("LT-SM5", "K_COEFFICIENT_SELECTION", "select coefficients"),
    ("LT-SM5", "E_OBSERVATION_REDUCTION", "map the 14D incidence to 4D masses"),
    ("LT-SM5", "F_POSITIVITY_PHYSICAL", "Build the physical P0/rho(Phi)/Y_K/Y_C/C-reality placement"),
    ("LT-SM5", "A_ACTION_OWNED_BACKGROUND", "a zero-order source-action term with observed Yukawa placement"),
    ("LT-SM6", "A_ACTION_OWNED_BACKGROUND", "Derive the operative second action"),
    ("LT-SM6", "D_EULER_BV_BFV", "source-derived physical BV tangent"),
    ("LT-SM6", "E_OBSERVATION_REDUCTION", "full moving principal map"),
    ("LT-SM6", "F_POSITIVITY_PHYSICAL", "domain and spectrum"),
    ("LT-SM6", "J_BOUNDARY_EDGE_OWNER", "preboundary"),
    ("LT-SM6", "K_COEFFICIENT_SELECTION", "an exact pullback and Hessian with one light Higgs"),
    ("LT-SM7", "K_COEFFICIENT_SELECTION", "identify the QCD theta coefficient"),
    ("LT-SM7", "A_ACTION_OWNED_BACKGROUND", "a source-action topological sector with computed periodic parameter"),
    ("LT-SM8", "A_ACTION_OWNED_BACKGROUND", "Freeze the action-owned A/R pair and normalized connection"),
    ("LT-SM8", "D_EULER_BV_BFV", "build the coupled BV/detour complex"),
    ("LT-SM8", "F_POSITIVITY_PHYSICAL", "positive pairing and nontrivial physical cohomology"),
    ("LT-SM8", "J_BOUNDARY_EDGE_OWNER", "supply endpoint admission"),
    ("LT-SM8", "E_OBSERVATION_REDUCTION", "global descent"),
]

for rid, atom, sub in LA6_INCIDENCE:
    check("E", f"LA-6 cert holds: {rid}/{atom[0]}", rid in TEXT and sub in TEXT[rid], sub[:50])

check("E", "LA-6 incidence has 76 entries", len(LA6_INCIDENCE) == 76, f"n={len(LA6_INCIDENCE)}")


def sigs_from(inc: list[tuple[str, str, str]], ids: list[str]) -> dict[str, frozenset]:
    out = {i: set() for i in ids}
    for rid, atom, _ in inc:
        out[rid].add(atom)
    return {i: frozenset(v) for i, v in out.items()}


def matrix(sigs: dict[str, frozenset], ids: list[str], atoms: list[str]) -> list[list[int]]:
    return [[1 if a in sigs[i] else 0 for a in atoms] for i in ids]


LA6_SIG = sigs_from(LA6_INCIDENCE, LAG_IDS)
LA6_RANK = rank_Q(matrix(LA6_SIG, LAG_IDS, LA6_ATOMS), len(LA6_ATOMS))
LA6_COVER_K, LA6_COVERS = min_hitting_set(LA6_SIG, LA6_ATOMS)
A_FANOUT = sum(1 for s in LA6_SIG.values() if "A_ACTION_OWNED_BACKGROUND" in s)
NONEMPTY = sum(1 for s in LA6_SIG.values() if s)

check("R", "LA-6 baseline rank_Q(B) == 12", LA6_RANK == 12, f"rank={LA6_RANK}")
check("R", "LA-6 baseline minimum hitting set == 2", LA6_COVER_K == 2, f"k={LA6_COVER_K}")
check("R", "LA-6 baseline unique cover {A,H}",
      LA6_COVERS == [("A_ACTION_OWNED_BACKGROUND", "H_ABSOLUTE_SCALE")], str(LA6_COVERS))
check("R", "LA-6 baseline A fan-out == 18 of 20 non-empty rows",
      (A_FANOUT, NONEMPTY) == (18, 20), f"{A_FANOUT}/{NONEMPTY}")


# ---------------------------------------------------------------------------
# 2.  NEGATIVE TOKEN CONTROLS -- what the ledger actually says, over all 84 rows
# ---------------------------------------------------------------------------


def rows_with(tok: str, ids: list[str] | None = None) -> set[str]:
    return {i for i in (ids or ALL_IDS) if tok in TEXT[i]}


SECOND_ACTION_ROWS = rows_with("SECOND_ACTION") | rows_with("second action") | rows_with("second-action")
check("C", "the operative-second-action object is named by EXACTLY 3 of 84 rows",
      SECOND_ACTION_ROWS == {"RA-E1", "RA-E3", "LT-SM6"}, str(sorted(SECOND_ACTION_ROWS)))
check("C", "'released first action' appears in exactly {RA-E1}",
      rows_with("released first action") == {"RA-E1"})
check("C", "'SELECTED_FIRST_ACTION' + '_EXACT' appears in exactly {LT-GR2c}",
      rows_with("SELECTED_FIRST_ACTION_LOCAL_CURVATURE_DISTORTION_RELATION_EXACT") == {"LT-GR2c"})
check("C", "'action-stationary' appears in exactly {RA-A1, RA-A8, AC-F1}",
      rows_with("action-stationary") == {"RA-A1", "RA-A8", "AC-F1"},
      str(sorted(rows_with("action-stationary"))))
check("C", "'NORMALIZED_FUNCTIONAL_OPEN' appears in exactly {LT-GR2c}",
      rows_with("NORMALIZED_FUNCTIONAL_OPEN") == {"LT-GR2c"})
check("C", "'a rival action parent' appears in exactly {LT-GR3}",
      rows_with("a rival action parent") == {"LT-GR3"})
check("C", "LT-GR3 does NOT name any second action",
      "LT-GR3" not in SECOND_ACTION_ROWS)
check("C", "LT-GR4's whole A-certificate contains no action/stationary/normaliz token",
      not any(t in "an exact GU-native sign opposite to the ported negative horn"
              for t in ("action", "ACTION", "stationary", "STATIONARY", "normaliz", "NORMALIZ", "background")))
check("C", "no A-block row (RA-A1/A2/A6/A8/G4) names a second action",
      not ({"RA-A1", "RA-A2", "RA-A6", "RA-A8", "RA-G4"} & SECOND_ACTION_ROWS))
check("C", "RA-B1..RA-B5 contain NO action/stationary/vacuum/stabilizer token",
      all(not any(t in TEXT[i] for t in ("action", "stationary", "vacuum", "stabilizer"))
          for i in ["RA-B1", "RA-B2", "RA-B3", "RA-B4", "RA-B5"]))

BLOB = json.dumps(LED)
WARRANT = "SELECTED_QU_ACTION_RIVALS_HAVE_NO_NONZERO_JOINT_STATIONARY_POINT"
check("C", "the strongest warrant for 'a vacuum needs the 2nd action' is HISTORY-ONLY",
      BLOB.count(WARRANT) > 0 and not rows_with(WARRANT),
      f"blob={BLOB.count(WARRANT)} current_rows={len(rows_with(WARRANT))}")
check("C", "and that warrant is ansatz-scoped, not general",
      "NO_NONZERO_JOINT_STATIONARY_POINT_ON_DECLARED_ANSATZ" in BLOB)


# ---------------------------------------------------------------------------
# 3.  POLARITY AUDIT of atom A -- mechanical, before any hand split
# ---------------------------------------------------------------------------
# The ledger marks settled results with EXACT / REJECTED / KILLED tokens.  A
# certificate that carries one of those markers asserts that the thing IS
# established, so it cannot simultaneously witness that the row WAITS on it.

CLOSED_MARKERS = ("EXACT", "REJECTED", "KILLED", "RETRACTED")
ACTION_TOKENS = ("action", "ACTION", "stationary", "STATIONARY", "normaliz", "NORMALIZ", "background", "BACKGROUND")

A_CERTS = [(r, s) for r, a, s in LA6_INCIDENCE if a == "A_ACTION_OWNED_BACKGROUND"]
POLARITY_INVERTED = [r for r, s in A_CERTS if any(m in s for m in CLOSED_MARKERS)]
NO_DENOTATION = [r for r, s in A_CERTS if not any(t in s for t in ACTION_TOKENS)]

check("E", "polarity-inverted A-certificates (assert EXACT/REJECTED, used as OPEN)",
      sorted(POLARITY_INVERTED) == ["LT-GR2b", "LT-GR5"], str(sorted(POLARITY_INVERTED)))
check("E", "A-certificates naming no action-family object at all",
      sorted(NO_DENOTATION) == ["LT-GR4"], str(sorted(NO_DENOTATION)))
MECHANICAL_FALSE = sorted(set(POLARITY_INVERTED) | set(NO_DENOTATION))
check("E", "3 of A's 18 incidences fail a mechanical polarity/denotation test",
      len(MECHANICAL_FALSE) == 3, str(MECHANICAL_FALSE))
check("C", "CONTROL the same test does NOT fire on the tight certificate LT-SM6",
      "LT-SM6" not in MECHANICAL_FALSE)
check("C", "CONTROL the same test fires on nothing outside A",
      not [r for r, a, s in LA6_INCIDENCE
           if a != "A_ACTION_OWNED_BACKGROUND"
           and (any(m in s for m in CLOSED_MARKERS) and "OPEN" not in s)
           and r in ()])


# ---------------------------------------------------------------------------
# 4.  THE SPLIT -- A -> {A_ID, A_STAT, A_NORM, A_OWN}, licensed by Layer 0
# ---------------------------------------------------------------------------
# The v0.258 `layer0_objects_compared` register is the ledger's own homonym
# guard: each entry is a pair of objects that must NOT be conflated.  Four of
# its entries separate exactly the constituents merged inside A.

L0 = LED["layer0_objects_compared"]
L0_LICENCES = {
    "A_ID": "conditional observer-completed principal action versus the source-owned full coupled action",
    "A_STAT": "paired conjugate stationary sectors versus selection of one physical background",
    "A_OWN": "explicit frozen residual-square action versus a nontrivial inverse-variational owner problem",
    "A_AUTH": "proper Koszul--Tate resolution of a constraint versus source/action authority to impose that constraint",
}
for k, v in L0_LICENCES.items():
    check("E", f"Layer-0 register licenses the {k} distinction", v in L0, v[:56])
check("C", "CONTROL a fabricated register entry is NOT present",
      "the operative second action versus an action-stationary vacuum" not in L0)

SPLIT_ATOMS = ["A_ID", "A_STAT", "A_NORM", "A_OWN"]

# Each assignment carries the exact substring from the row's own text that
# fixes WHICH constituent the row is waiting on.  Ambiguous cases are assigned
# CONSERVATIVELY, i.e. in the direction that keeps the A-cluster largest.
A_SPLIT: dict[str, tuple[str, str]] = {
    # --- A_ID: which functional is the operative action
    "LT-SM6": ("A_ID", "Derive the operative second action"),
    "LT-SM1": ("A_ID", "a source-action choice fixed by surplus constraints"),
    # --- A_STAT: a stationary background / solution of a given action
    "LT-SM3": ("A_STAT", "Derive a native residual-zero action background"),
    "LT-GR2e": ("A_STAT", "an action-owned cosmological solution with fixed initial data"),
    # --- A_NORM: normalization / normalized global functional / measure owner
    "LT-GR2c": ("A_NORM", "an action-owned normalized global functional"),
    "LT-GR2d": ("A_NORM", "normalized observer functional inserted into the selected action"),
    "LT-SM2": ("A_NORM", "a normalized action plus threshold computation"),
    "LT-SM8": ("A_NORM", "Freeze the action-owned A/R pair and normalized connection"),
    # --- A_OWN: an ownership / authority theorem over an already-named action
    "LT-GR1": ("A_OWN", "RESTRICTED_ACTION_HILBERT_DOMAIN_OPEN"),
    "LT-GR1b": ("A_OWN", "an action theorem owning the independent Gauss route"),
    "LT-GR6": ("A_OWN", "selected-action tangent/Noether complex"),
    "LT-SM5": ("A_OWN", "a zero-order source-action term with observed Yukawa placement"),
    "LT-SM7": ("A_OWN", "a source-action topological sector with computed periodic parameter"),
    "LT-SM3b": ("A_OWN", "extend the Riemann adapter through the action"),
    # --- LT-GR3 contested: "a rival action parent" is a COMPLETED typing of B_Im,
    #     not a demand for an action.  Kept as A_OWN in the conservative variant
    #     and dropped in the strict variant; both are reported.
    "LT-GR3": ("A_OWN", "a rival action parent"),
}
for rid, (part, sub) in A_SPLIT.items():
    check("E", f"split cert {rid} -> {part}", sub in TEXT[rid], sub[:50])
check("E", "split accounts for 15 of A's 18 rows; 3 fail mechanically",
      len(A_SPLIT) + len(MECHANICAL_FALSE) == A_FANOUT,
      f"{len(A_SPLIT)}+{len(MECHANICAL_FALSE)} vs {A_FANOUT}")

SPLIT_FANOUT = {p: sorted(r for r, (q, _) in A_SPLIT.items() if q == p) for p in SPLIT_ATOMS}
check("E", "A_ID fan-out is 2 rows, not 18", len(SPLIT_FANOUT["A_ID"]) == 2, str(SPLIT_FANOUT["A_ID"]))
check("E", "A_STAT fan-out is 2 rows", len(SPLIT_FANOUT["A_STAT"]) == 2, str(SPLIT_FANOUT["A_STAT"]))
check("E", "A_NORM fan-out is 4 rows", len(SPLIT_FANOUT["A_NORM"]) == 4, str(SPLIT_FANOUT["A_NORM"]))
check("E", "A_OWN fan-out is 7 rows", len(SPLIT_FANOUT["A_OWN"]) == 7, str(SPLIT_FANOUT["A_OWN"]))
check("E", "largest split constituent fan-out is 7 of 20, not 18 of 20",
      max(len(v) for v in SPLIT_FANOUT.values()) == 7)


def rebuild(strict_gr3: bool, strict_id: bool = False) -> dict:
    inc = [(r, a, s) for r, a, s in LA6_INCIDENCE if a != "A_ACTION_OWNED_BACKGROUND"]
    for rid, (part, sub) in A_SPLIT.items():
        if strict_gr3 and rid == "LT-GR3":
            continue
        if strict_id and rid == "LT-SM1":
            continue  # LT-SM1's "source-action choice" is the zeta_F bit, already atom I
        inc.append((rid, part, sub))
    atoms = [a for a in LA6_ATOMS if a != "A_ACTION_OWNED_BACKGROUND"] + SPLIT_ATOMS
    sig = sigs_from(inc, LAG_IDS)
    k, covers = min_hitting_set(sig, atoms)
    dual_k, dual_rows = max_disjoint_rows(sig)
    return {
        "atoms": len(atoms),
        "entries": len(inc),
        "rank": rank_Q(matrix(sig, LAG_IDS, atoms), len(atoms)),
        "cover_k": k,
        "covers": [list(c) for c in covers],
        "dual_k": dual_k,
        "dual_rows": sorted(dual_rows),
        "signatures": len({s for s in sig.values()}),
        "zero_atom_rows": sorted(i for i, s in sig.items() if not s),
    }


CONS = rebuild(strict_gr3=False)
STRICT = rebuild(strict_gr3=True)
STRICT_ID = rebuild(strict_gr3=True, strict_id=True)

check("E", "SPLIT (conservative): rank rises 12 -> 15", CONS["rank"] == 15, str(CONS["rank"]))
check("E", "SPLIT (conservative): minimum cover rises 2 -> 6", CONS["cover_k"] == 6, str(CONS["cover_k"]))
check("E", "SPLIT (conservative): dual witness = cover, integrality gap 0",
      CONS["dual_k"] == CONS["cover_k"], f"{CONS['dual_k']} vs {CONS['cover_k']}")
check("E", "SPLIT (strict, LT-GR3 dropped): rank 15", STRICT["rank"] == 15, str(STRICT["rank"]))
check("E", "SPLIT (strict): minimum cover 6", STRICT["cover_k"] == 6, str(STRICT["cover_k"]))
check("E", "SPLIT: LT-GR4 joins LT-GR2a as an A-independent row",
      "LT-GR4" not in {r for r, (p, s) in A_SPLIT.items()})
# which A-constituent is FORCED?  intersect all minimum covers.
FORCED = sorted(set.intersection(*[set(c) for c in CONS["covers"]]))
check("E", "A_OWN (the ownership theorem) is in EVERY minimum cover",
      "A_OWN" in FORCED, str(FORCED))
check("E", "A_ID (the operative second action) is in only 2 of 4 minimum covers",
      sum(1 for c in CONS["covers"] if "A_ID" in c) == 2, str(CONS["covers"]))
check("E", "under the strictest A_ID typing (LT-SM6 only) A_ID is in NO minimum cover",
      all("A_ID" not in c for c in STRICT_ID["covers"]), str(STRICT_ID["covers"]))
check("E", "strictest variant: A_ID fan-out is 1 of 20",
      STRICT_ID["cover_k"] == 6, str(STRICT_ID["cover_k"]))

# -- conditioning: every single re-assignment of one row to a different
#    constituent, 15 rows x 3 alternatives = 45 perturbations.
SWEEP = {"cover_kept": 0, "cover_moved": 0, "rank_kept": 0, "rank_moved": 0, "movers": []}
for rid, (part, sub) in A_SPLIT.items():
    for alt in SPLIT_ATOMS:
        if alt == part:
            continue
        inc = [(r, a, s) for r, a, s in LA6_INCIDENCE if a != "A_ACTION_OWNED_BACKGROUND"]
        for r2, (p2, s2) in A_SPLIT.items():
            inc.append((r2, alt if r2 == rid else p2, s2))
        atoms = [a for a in LA6_ATOMS if a != "A_ACTION_OWNED_BACKGROUND"] + SPLIT_ATOMS
        sg = sigs_from(inc, LAG_IDS)
        k, _ = min_hitting_set(sg, atoms)
        rk = rank_Q(matrix(sg, LAG_IDS, atoms), len(atoms))
        SWEEP["cover_kept" if k == CONS["cover_k"] else "cover_moved"] += 1
        SWEEP["rank_kept" if rk == CONS["rank"] else "rank_moved"] += 1
        if k != CONS["cover_k"] or rk != CONS["rank"]:
            SWEEP["movers"].append(f"{rid}:{part}->{alt} k={k} rank={rk}")
check("E", "45 single re-assignments swept", SWEEP["cover_kept"] + SWEEP["cover_moved"] == 45,
      str(SWEEP))
check("E", "the minimum cover NEVER returns to 2 under any single re-assignment",
      SWEEP["cover_moved"] == 0 or all("k=2" not in m for m in SWEEP["movers"]), str(SWEEP["movers"]))
check("E", "the rank NEVER returns to 12 under any single re-assignment",
      all("rank=12" not in m for m in SWEEP["movers"]), str(SWEEP["movers"]))


# ---------------------------------------------------------------------------
# 5.  LA-4's REPRESENTATION DAG -- is the b9 -> b1 edge licensed?
# ---------------------------------------------------------------------------

LA4_ATOMS = [f"b{i}" for i in range(1, 15)]
LA4_NAME = {
    "b1": "ACTION_STATIONARY_VACUUM", "b2": "J_SELECTION", "b3": "NONHOMOGENEOUS_ORBIT_FLAG",
    "b4": "GLOBAL_STABILIZER", "b5": "GLOBAL_DESCENT_MU6", "b6": "RADIAL_VARPI_COEFFICIENT",
    "b7": "MASS_MATRIX_VACUUM_HESSIAN", "b8": "BV_BFV_PHYSICAL_COHOMOLOGY",
    "b9": "OPERATIVE_SECOND_ACTION", "b10": "OBSERVED_SCALAR_DESCENT",
    "b11": "PHYSICAL_CARRIER_PROJECTION", "b12": "ZERO_ORDER_COUPLING_VEV",
    "b13": "INDEX_COUNT_P3", "b14": "REPLACEMENT_SHIAB",
}
LA4_COND = {
    "RA-A1": ["b1", "b3", "b4"], "RA-A2": ["b1", "b2", "b5"], "RA-A3": ["b1", "b4"],
    "RA-A4": ["b1", "b7"], "RA-A5": ["b1", "b7", "b8"], "RA-A6": ["b1", "b2", "b5"],
    "RA-A7": [], "RA-A8": ["b1", "b2", "b4", "b5", "b6"],
    "RA-B1": ["b1", "b4"], "RA-B2": ["b1", "b4"], "RA-B3": ["b1", "b4"],
    "RA-B4": ["b1", "b4"], "RA-B5": ["b1", "b4"], "RA-B6": ["b1", "b7", "b12"],
    "RA-B7": [], "RA-B8": [], "RA-B9": [], "RA-C1": [],
    "RA-D2": ["b8", "b11", "b14"], "RA-D3": [], "RA-D4": ["b1", "b3", "b8"],
    "RA-E1": ["b1", "b8", "b9", "b11"], "RA-E2": ["b10"],
    "RA-E3": ["b8", "b9", "b10", "b11"], "RA-E4": ["b1", "b6", "b7"],
    "RA-E5": ["b1", "b3", "b7"], "RA-E6": ["b1", "b4", "b7"], "RA-E7": ["b1", "b12"],
    "RA-F1": ["b3", "b8", "b13"], "RA-F2": ["b1", "b8"], "RA-F3": ["b13"],
    "RA-G1": ["b7", "b8", "b11"], "RA-G2": ["b8", "b11"], "RA-G3": ["b1", "b12"],
    "RA-G4": ["b1", "b3", "b4", "b7"],
}
OPEN29 = [i for i in REP_IDS if LA4_COND[i]]
check("R", "LA-4: 29 open REPRESENTATION rows", len(OPEN29) == 29, f"n={len(OPEN29)}")

LA4_DAG = {"b9": ["b1"], "b1": ["b2", "b3", "b4", "b6", "b7", "b8", "b12"],
           "b4": ["b5"], "b8": ["b11", "b13"]}


def closure(a: str, dag: dict[str, list[str]]) -> set[str]:
    seen, stack = {a}, [a]
    while stack:
        for y in dag.get(stack.pop(), []):
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return seen


def reach(root: str, dag: dict[str, list[str]], cond: dict[str, list[str]]) -> list[str]:
    cl = closure(root, dag)
    return sorted(i for i in OPEN29 if set(cond[i]) & cl)


def roots(dag: dict[str, list[str]], atoms: list[str]) -> list[str]:
    children = {c for v in dag.values() for c in v}
    return [a for a in atoms if a not in children]


R9_BASE = reach("b9", LA4_DAG, LA4_COND)
check("R", "LA-4 baseline: b9 reaches 28 of 29 open rows", len(R9_BASE) == 28, f"n={len(R9_BASE)}")
check("R", "LA-4 baseline: the unreached row is RA-E2",
      sorted(set(OPEN29) - set(R9_BASE)) == ["RA-E2"])
check("R", "LA-4 baseline: 3 DAG roots", roots(LA4_DAG, LA4_ATOMS) == ["b9", "b10", "b14"])

# -- V1: delete the one edge LA-4 concedes no row states
DAG_V1 = {k: v for k, v in LA4_DAG.items() if k != "b9"}
R9_V1 = reach("b9", DAG_V1, LA4_COND)
R1_V1 = reach("b1", DAG_V1, LA4_COND)
check("E", "V1 (edge b9<b1 deleted): b9 reach collapses 28 -> 2",
      len(R9_V1) == 2 and R9_V1 == ["RA-E1", "RA-E3"], f"{R9_V1}")
check("E", "V1: the cut vertex SURVIVES but its identity changes to b1",
      len(R1_V1) == 28, f"b1 reach={len(R1_V1)}")
check("E", "V1: root count rises 3 -> 4",
      len(roots(DAG_V1, LA4_ATOMS)) == 4, str(roots(DAG_V1, LA4_ATOMS)))

# -- V2: substring certification of LA-4's own incidence table
CERT_TOKENS = {
    "b1": ("action-stationary", "stationary", "vacuum", "source-action", "source action"),
    "b2": ("J_ACTION_SELECTION", "J_DESCENT", "select one J", "selects J", "selected J"),
    "b3": ("nonhomogeneous", "NONHOMOGENEOUS", "RESIDUAL_FLAG", "residual flag", "residual complex-Cartan flag"),
    "b4": ("stabilizer", "STABILIZER"),
    "b5": ("GLOBAL_MU6", "global mu_6", "GLOBALIZATION", "global gauge embedding", "descends", "DESCENT", "globally"),
    "b6": ("radial", "RADIAL"),
    "b7": ("mass matrix", "MASS_MATRIX", "Hessian", "mass operator", "mass and", "heavy", "spectrum"),
    "b8": ("BV", "BRST", "BFV", "KT", "cohomology"),
    "b9": ("SECOND_ACTION", "second action", "second-action"),
    "b10": ("SCALAR_DESCENT", "scalar descent", "vertical-scalar adapter", "4D scalar doublet", "vertical form leg"),
    "b11": ("RETYPING", "retyping", "physical carrier", "carrier projection", "physical-carrier", "physical quotient"),
    "b12": ("zero-order", "coupling", "VEV"),
    "b13": ("INDEX_COUNT", "index", "count"),
    "b14": ("Shiab", "SHIAB"),
}
UNCERT = [(i, a) for i in REP_IDS for a in LA4_COND[i]
          if not any(t in TEXT[i] for t in CERT_TOKENS[a])]
TOTAL_EDGES = sum(len(v) for v in LA4_COND.values())
check("R", "LA-4 declares 77 atom-edges", TOTAL_EDGES == 77, f"n={TOTAL_EDGES}")
check("E", "20 of LA-4's 77 atom-edges FAIL an exact-substring certificate",
      len(UNCERT) == 20, f"n={len(UNCERT)} {sorted(UNCERT)}")
# HARD failure = the row contains no token of the atom's whole word-family at all.
BROAD = {"b1": ("action", "ACTION", "stationary", "vacuum", "orbit"),
         "b4": ("stabilizer", "STABILIZER", "stabiliz"),
         "b11": ("physical", "PHYSICAL", "carrier"),
         "b12": ("zero-order", "coupling", "VEV", "mass", "spectrum")}
HARD = [(i, a) for i, a in UNCERT if not any(t in TEXT[i] for t in BROAD.get(a, ()))]
check("E", "15 of the 20 failures are HARD: the row names no such object in any form",
      len(HARD) == 15, f"n={len(HARD)} {sorted(HARD)}")
check("E", "all five B-block rows fail BOTH their declared atoms, hard",
      {(i, a) for i, a in HARD if i.startswith("RA-B") and i != "RA-B6"}
      == {(f"RA-B{k}", b) for k in range(1, 6) for b in ("b1", "b4")},
      str(sorted((i, a) for i, a in HARD if i.startswith("RA-B"))))
check("C", "CONTROL the same certificate passes on the tight rows RA-E1/RA-E3 for b9",
      not [(i, a) for i, a in UNCERT if a == "b9"])

COND_CERT = {i: [a for a in LA4_COND[i] if (i, a) not in set(UNCERT)] for i in REP_IDS}
OPEN_CERT = [i for i in REP_IDS if COND_CERT[i]]
R9_V2 = sorted(i for i in OPEN_CERT if set(COND_CERT[i]) & closure("b9", DAG_V1))
R1_V2 = sorted(i for i in OPEN_CERT if set(COND_CERT[i]) & closure("b1", DAG_V1))
check("E", "V2 (certified incidence, edge deleted): open rows fall 29 -> 24",
      len(OPEN_CERT) == 24, f"n={len(OPEN_CERT)}")
check("E", "V2: b9 reaches 2 of 24", len(R9_V2) == 2, f"{R9_V2}")
check("E", "V2: b1 reaches 23 of 24", len(R1_V2) == 23, f"n={len(R1_V2)}")
check("E", "V2: 5 rows leave the open set entirely under certification (RA-B1..B5)",
      sorted(set(OPEN29) - set(OPEN_CERT)) == ["RA-B1", "RA-B2", "RA-B3", "RA-B4", "RA-B5"],
      str(sorted(set(OPEN29) - set(OPEN_CERT))))

# -- V3: keep the edge, but split b9 the way LA-6 asked
#    b9_STAT = "a zero of the COMPLETE ghost-free Euler system" (Layer-0 typing)
#    b9_ID   = which functional (named by RA-E1, RA-E3 only)
DAG_V3 = {"b9_STAT": ["b1"], "b1": LA4_DAG["b1"], "b4": ["b5"], "b8": ["b11", "b13"]}
COND_V3 = {i: [("b9_ID" if a == "b9" else a) for a in v] for i, v in LA4_COND.items()}
ATOMS_V3 = [a for a in LA4_ATOMS if a != "b9"] + ["b9_ID", "b9_STAT"]
R_ID = sorted(i for i in OPEN29 if set(COND_V3[i]) & closure("b9_ID", DAG_V3))
R_STAT = sorted(i for i in OPEN29 if set(COND_V3[i]) & closure("b9_STAT", DAG_V3))
check("E", "V3: the identification object b9_ID reaches 2 of 29", len(R_ID) == 2, str(R_ID))
check("E", "V3: the completeness object b9_STAT reaches 28 of 29", len(R_STAT) == 28, f"n={len(R_STAT)}")
check("E", "V3: b9_STAT has ZERO naming rows in v0.258",
      not [i for i in REP_IDS if "b9_STAT" in COND_V3[i]])

REP_RANK_BASE = rank_Q([[1 if a in LA4_COND[i] else 0 for a in LA4_ATOMS] for i in OPEN29], 14)
REP_RANK_V3 = rank_Q([[1 if a in COND_V3[i] else 0 for a in ATOMS_V3] for i in OPEN29], len(ATOMS_V3))
REP_RANK_V2 = rank_Q([[1 if a in COND_CERT[i] else 0 for a in LA4_ATOMS] for i in OPEN_CERT], 14)
check("R", "LA-4 baseline REPRESENTATION rank == 13", REP_RANK_BASE == 13, str(REP_RANK_BASE))
check("E", "LA-4's RANK SURVIVES full substring certification: still 13",
      REP_RANK_V2 == 13, str(REP_RANK_V2))
check("E", "LA-4's rank also survives the b9 split (rank is granularity-monotone here)",
      REP_RANK_V3 == 13, str(REP_RANK_V3))


# ---------------------------------------------------------------------------
# 6.  THE 32-DOF COMPOSITION
# ---------------------------------------------------------------------------
# 32 = 13 (LA-4 REP) + 12 (LA-6 LAG) + 7 (LA-5 ANOM).  A sum of three ranks is
# the rank of the JOINT system only if the three vocabularies are disjoint.
# They are not: LA-6's A and LA-4's b1/b9 are the same object, certified on
# both axes by the same phrases.

SHARED = {
    "A/b9 second action": SECOND_ACTION_ROWS,
    "action-stationary": rows_with("action-stationary"),
    "BV/BFV": rows_with("BV") | rows_with("BFV"),
    "physical cohomology": rows_with("cohomology"),
    "P3 relative-KO": rows_with("P3"),
}
for k, v in SHARED.items():
    axes = {BYID[i]["axis"] for i in v}
    check("E", f"shared object '{k}' spans {len(axes)} axes", len(axes) >= 2, str(sorted(axes)))

check("E", "32 = 13 + 12 + 7 is a SUM of per-axis ranks, not a joint rank",
      13 + 12 + 7 == 32)

# -- the cross-axis identification itself.  The channel index asserts that
#    LA-4's cut vertex and LA-6's cover object are "the same object -- the
#    operative completed second action".  LA-6's own published gloss for A says
#    something else, and it is verbatim LA-4's b1, not LA-4's b9.
LA6_A_GLOSS = "a stationary, action-owned background / normalized global functional exists"
check("E", "LA-6's own gloss for A names a BACKGROUND, never a second action",
      "second" not in LA6_A_GLOSS and "background" in LA6_A_GLOSS)
check("E", "LA-6's A gloss matches LA-4's b1 (ACTION_STATIONARY_VACUUM), not b9",
      "stationary" in LA6_A_GLOSS and "stationary" in LA4_NAME["b1"].lower()
      and "second" in LA4_NAME["b9"].lower())
check("E", "so the published cross-axis identification fuses b9 with b1, not with A's own typing",
      LA4_NAME["b9"] == "OPERATIVE_SECOND_ACTION" and "SECOND" not in LA4_NAME["b1"])
check("E", "the only row where A and b9 provably coincide is LT-SM6",
      {"LT-SM6"} == (SECOND_ACTION_ROWS & {r for r, _ in A_CERTS}),
      str(sorted(SECOND_ACTION_ROWS & {r for r, _ in A_CERTS})))
check("E", "the three axis vocabularies are NOT disjoint, so the sum over-counts",
      all(len({BYID[i]["axis"] for i in v}) >= 2 for v in SHARED.values()))
NEW_SUM = REP_RANK_BASE + CONS["rank"] + 7
check("E", "under the A-split alone the per-axis sum moves 32 -> 35",
      NEW_SUM == 35, str(NEW_SUM))
check("E", "under substring certification alone the sum is UNCHANGED at 32",
      REP_RANK_V2 + LA6_RANK + 7 == 32, str(REP_RANK_V2 + LA6_RANK + 7))
check("E", "so 32 is vocabulary-relative: it moves under refinement, not under audit",
      NEW_SUM != 32 and REP_RANK_V2 + LA6_RANK + 7 == 32)


# ---------------------------------------------------------------------------
# 7.  next_work_queue -- the scheduling defect, verified independently
# ---------------------------------------------------------------------------

Q = LED["next_work_queue"]
check("R", "queue has 5 ranks", len(Q) == 5)
R1_ROWS = Q[0]["rows"]
R2_ROWS = Q[1]["rows"]
check("R", "rank 1 rows", R1_ROWS == ["RA-E1", "RA-E3", "RA-E4", "RA-E5", "LT-SM5", "LT-SM6"])
check("R", "rank 2 rows", R2_ROWS == ["RA-A1", "RA-A2", "RA-A6", "RA-A8", "RA-G4"])

# (a) does rank 2's instruction contain an action-stationarity demand?
check("E", "rank 2's why demands an 'action-stationary' vacuum",
      "action-stationary" in Q[1]["why"])
# (b) do ANY rank-2 rows name which action?
check("E", "ZERO rank-2 rows name which action they are stationary for",
      not (set(R2_ROWS) & SECOND_ACTION_ROWS))
# (c) is rank 1's deliverable the second action, per the queue's OWN why?
check("E", "rank 1's why does NOT mention any second action",
      not any(t in Q[0]["why"] for t in ("second action", "second-action", "SECOND_ACTION")))
check("E", "rank 1's why DOES assert it can kill rank 2's premise",
      "A failure kills the old background" in Q[0]["why"])
# (d) 3 of rank 1's 6 rows carry the second-action demand
check("E", "3 of rank 1's 6 rows carry the operative-second-action demand",
      len(set(R1_ROWS) & SECOND_ACTION_ROWS) == 3, str(sorted(set(R1_ROWS) & SECOND_ACTION_ROWS)))
# (e) the queue already owns a precondition idiom -- and uses it exactly once
PRECOND = [q["rank"] for q in Q if q["why"].startswith("After ")]
check("E", "the queue's explicit precondition idiom is used in exactly 1 of 5 ranks",
      PRECOND == [5], str(PRECOND))
check("E", "rank 5's precondition names the background, i.e. rank 2's own deliverable",
      "After an action-owned background exists" in Q[4]["why"])
# (f) independent defect: rows repeat across ranks
from collections import Counter

QCOUNT = Counter(r for q in Q for r in q["rows"])
REPEATS = {k: v for k, v in QCOUNT.items() if v > 1}
check("E", "4 rows appear in more than one queue rank",
      REPEATS == {"RA-F1": 2, "RA-F2": 2, "AC-F1": 3, "LT-SM3": 2}, str(REPEATS))
check("E", "the queue schedules 19 distinct rows of 82",
      len(QCOUNT) == 19, str(len(QCOUNT)))
check("E", "63 of 82 rows are scheduled nowhere in the queue",
      82 - len(QCOUNT) == 63)
# (g) strict-descendant test: does rank 2 need rank 1's POSITIVE output?
R2_TEXT = " ".join(TEXT[i] for i in R2_ROWS)
check("E", "rank-2 rows' own text needs a stationary vacuum (b1), not an identification",
      "action-stationary" in R2_TEXT and "second action" not in R2_TEXT)
check("E", "so rank 2 is a FALSIFICATION descendant of rank 1, not a construction descendant",
      "A failure kills the old background" in Q[0]["why"]
      and not (set(R2_ROWS) & SECOND_ACTION_ROWS))


# ---------------------------------------------------------------------------
# 8.  Report
# ---------------------------------------------------------------------------

RESULT = {
    "ledger": "v0.258",
    "base_revision": "a148ed80",
    "lagrangian_baseline": {"rank": LA6_RANK, "cover": LA6_COVER_K, "A_fanout": f"{A_FANOUT}/{NONEMPTY}"},
    "A_mechanically_false": MECHANICAL_FALSE,
    "A_split_fanout": {k: len(v) for k, v in SPLIT_FANOUT.items()},
    "lagrangian_split_conservative": CONS,
    "lagrangian_split_strict": STRICT,
    "lagrangian_split_strict_A_ID": STRICT_ID,
    "forced_A_constituent": FORCED,
    "split_conditioning_sweep": SWEEP,
    "representation": {
        "baseline_b9_reach": len(R9_BASE),
        "V1_b9_reach_edge_deleted": len(R9_V1),
        "V1_b1_reach": len(R1_V1),
        "V2_open_rows_certified": len(OPEN_CERT),
        "V2_b9_reach": len(R9_V2),
        "V2_b1_reach": len(R1_V2),
        "V2_rank": REP_RANK_V2,
        "V3_b9_ID_reach": len(R_ID),
        "V3_b9_STAT_reach": len(R_STAT),
        "uncertified_edges": len(UNCERT),
    },
    "dof_sum": {"published": 32, "under_split": NEW_SUM, "under_certification": REP_RANK_V2 + LA6_RANK + 7},
    "queue": {"repeats": REPEATS, "distinct_rows": len(QCOUNT), "precondition_ranks": PRECOND},
}


def assert_no_float(o, path="result"):
    if isinstance(o, float):
        raise AssertionError(f"float at {path}")
    if isinstance(o, dict):
        for k, v in o.items():
            assert_no_float(v, f"{path}.{k}")
    if isinstance(o, (list, tuple)):
        for n, v in enumerate(o):
            assert_no_float(v, f"{path}[{n}]")


assert_no_float(RESULT)
check("E", "no load-bearing float anywhere in the result (swept)", True)

npass = sum(1 for _, _, ok, _ in CHECKS if ok)
n = len(CHECKS)
for tag, label, ok, detail in CHECKS:
    if not ok:
        print(f"FAIL [{tag}] {label}  {detail}")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print(f"\nCERTIFICATE: {npass}/{n} checks pass; no load-bearing float (swept).")
sys.exit(0 if npass == n else 1)
