#!/usr/bin/env python3
"""LA-6 -- effective degrees of freedom of the LAGRANGIAN axis, ledger v0.258 (base a148ed80).

Exactness policy
----------------
Every number produced here is an integer or a `fractions.Fraction`.  No float is
constructed anywhere; `assert_no_float` walks the result dict at the end and
fails if any float appears.  The rank is computed by fraction-free integer
Gaussian elimination over Q, not by numpy.

Certificate policy
------------------
The incidence matrix B is a DECLARED TYPING, not a machine inference.  To keep it
auditable every 1 in B must be backed by an exact substring that occurs in the
row's own v0.258 text (`distance || revival_trigger || mapping_grade ||
frontier_grade`).  The script verifies all of them and fails on the first miss.
Negative controls assert that certain tokens appear in exactly the rows claimed
and nowhere else, so an over-broad substring cannot silently inflate B.

What is computed
----------------
  (1) rank_Q(B)                 -- controllability rank: how many independent
                                   directions of the 21-dim row-state space any
                                   combination of grants can move.
  (2) row-signature partition   -- rows with identical B-rows can never be moved
                                   apart; each class is one effective handle.
  (3) bipartite components      -- independent sub-programs.
  (4) exact minimum set cover   -- cheapest certificate set (brute force, k<=16).
  (5) articulation atoms        -- single points of failure.
  (6) left null space dim       -- redundant row directions (over-counting).
  (7) fork arithmetic           -- ledger's 9 open forks / horn product 1152
                                   against the layer-0 registry's open rows.
"""

from __future__ import annotations

import json
import itertools
import os
import sys
from fractions import Fraction

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
LEDGER = os.path.join(REPO, "lab", "process", "conditional-physics-ledger-v0.258.json")
FORKS = os.path.join(REPO, "lab", "process", "layer0-fork-registry.yaml")

CHECKS: list[tuple[str, str, bool]] = []  # (tag, label, passed)


def check(tag: str, label: str, passed: bool) -> None:
    CHECKS.append((tag, label, bool(passed)))


# --------------------------------------------------------------------------
# 0.  Load the axis
# --------------------------------------------------------------------------

with open(LEDGER) as fh:
    LED = json.load(fh)

ALL_ROWS = LED["rows"]
LT = [r for r in ALL_ROWS if r["axis"] == "LAGRANGIAN" and r.get("row_status") != "SUPERSEDED"]
LT_SUPERSEDED = [r for r in ALL_ROWS if r["axis"] == "LAGRANGIAN" and r.get("row_status") == "SUPERSEDED"]

check("E", "84 row records in v0.258", len(ALL_ROWS) == 84)
check("E", "21 active LAGRANGIAN rows", len(LT) == 21)
check("E", "1 superseded LAGRANGIAN row (LT-GR2)", [r["id"] for r in LT_SUPERSEDED] == ["LT-GR2"])
check("E", "denominator.axes.LAGRANGIAN == 21", LED["denominator"]["axes"]["LAGRANGIAN"] == 21)
check("E", "canonical_target_count == 82", LED["denominator"]["canonical_target_count"] == 82)

IDS = [r["id"] for r in LT]
BYID = {r["id"]: r for r in LT}


def rowtext(rid: str) -> str:
    r = BYID[rid]
    return " || ".join(
        [
            r.get("distance", ""),
            r.get("revival_trigger", ""),
            r.get("mapping_grade", ""),
            r.get("frontier_grade", ""),
        ]
    )


TEXT = {rid: rowtext(rid) for rid in IDS}

# --------------------------------------------------------------------------
# 1.  The declared atomic-unknown basis
# --------------------------------------------------------------------------
# Each atom is one open object the axis's rows are currently waiting on, named
# in the ledger's own vocabulary.  `gloss` states the typing; `probe` is a token
# used by the negative controls to bound where the atom may legitimately appear.

ATOMS: dict[str, str] = {
    "A_ACTION_OWNED_BACKGROUND": "a stationary, action-owned background / normalized global functional exists",
    "B_K77_OPERATOR_DOMAIN": "the physical K77 operator together with a closed relative (analytic) domain",
    "C_RELATIVE_INDEX_COUNT": "the relative index and its count readout on that operator",
    "D_EULER_BV_BFV": "the Euler / BV / BFV variational-cohomology closure",
    "E_OBSERVATION_REDUCTION": "the observation / reduction / quotient descent map to 4D",
    "F_POSITIVITY_PHYSICAL": "positive pairing, physical carrier, physical cohomology (Krein exit)",
    "G_SHIAB_SELECTOR": "which Shiab / which product assignment",
    "H_ABSOLUTE_SCALE": "one imported absolute scale (mu_DW-class length^2 / normalization)",
    "I_ZETA_F_BIT": "the fundamental-versus-induced Yang-Mills bit zeta_F in {0,1}",
    "J_BOUNDARY_EDGE_OWNER": "the boundary / edge owner and its P3 relative-KO bridge",
    "K_COEFFICIENT_SELECTION": "selection of the charged numerical coefficients (texture, placement, polarization)",
    "L_COSMOLOGICAL_SOLUTION": "an action-owned FLRW solution with initial data and w(z)",
    "M_NATIVE_RG_RUNNING": "a GU-native renormalization-group running computation",
}

# --------------------------------------------------------------------------
# 2.  The incidence, with a positive substring certificate for every 1
# --------------------------------------------------------------------------
# (row, atom, exact substring that must occur in that row's v0.258 text)

INCIDENCE: list[tuple[str, str, str]] = [
    # ---- LT-GR1
    ("LT-GR1", "B_K77_OPERATOR_DOMAIN", "construct the physical K77 nonzero-fermion operator, closed relative domain"),
    ("LT-GR1", "C_RELATIVE_INDEX_COUNT", "index and count identification"),
    ("LT-GR1", "D_EULER_BV_BFV", "recomputing Euler/BV"),
    ("LT-GR1", "F_POSITIVITY_PHYSICAL", "observed Hilbert stress"),
    ("LT-GR1", "J_BOUNDARY_EDGE_OWNER", "BOUNDARY_TO_P3_RELATIVE_KO_INPUT_MAP_EXACT"),
    ("LT-GR1", "A_ACTION_OWNED_BACKGROUND", "RESTRICTED_ACTION_HILBERT_DOMAIN_OPEN"),
    # ---- LT-GR1b  (OVER_DETERMINED; the two named exits)
    ("LT-GR1b", "G_SHIAB_SELECTOR", "construct a different Shiab"),
    ("LT-GR1b", "A_ACTION_OWNED_BACKGROUND", "an action theorem owning the independent Gauss route"),
    # ---- LT-GR2a  (no atoms: distance is "none at source-typing grade")
    # ---- LT-GR2b
    ("LT-GR2b", "B_K77_OPERATOR_DOMAIN", "build a K77 relative operator/domain"),
    ("LT-GR2b", "C_RELATIVE_INDEX_COUNT", "index and count readout"),
    ("LT-GR2b", "J_BOUNDARY_EDGE_OWNER", "BOUNDARY_TO_P3_RELATIVE_KO_INPUT_MAP_EXACT"),
    ("LT-GR2b", "A_ACTION_OWNED_BACKGROUND", "LOCAL_ACTION_OWNED_VEV_EXACT_UNREDUCED"),
    ("LT-GR2b", "D_EULER_BV_BFV", "complete EOM/BV/boundary cancellation"),
    # ---- LT-GR2c
    ("LT-GR2c", "B_K77_OPERATOR_DOMAIN", "Build the physical K77 operator/domain"),
    ("LT-GR2c", "C_RELATIVE_INDEX_COUNT", "compute its relative index and identify the count"),
    ("LT-GR2c", "D_EULER_BV_BFV", "restrict/recompute Euler/BV"),
    ("LT-GR2c", "A_ACTION_OWNED_BACKGROUND", "an action-owned normalized global functional"),
    ("LT-GR2c", "E_OBSERVATION_REDUCTION", "observation descent"),
    ("LT-GR2c", "H_ABSOLUTE_SCALE", "NOT_SCALE_SELECTOR__NORMALIZED_FUNCTIONAL_OPEN"),
    ("LT-GR2c", "J_BOUNDARY_EDGE_OWNER", "BOUNDARY_TO_P3_RELATIVE_KO_INPUT_MAP_EXACT"),
    # ---- LT-GR2d
    ("LT-GR2d", "B_K77_OPERATOR_DOMAIN", "physical K77 relative index/count readout"),
    ("LT-GR2d", "C_RELATIVE_INDEX_COUNT", "K77_INDEX_COUNT_SIGN_UNITS_STABILITY_DOMAIN_OPEN"),
    ("LT-GR2d", "H_ABSOLUTE_SCALE", "Sign, units, radiative response"),
    ("LT-GR2d", "A_ACTION_OWNED_BACKGROUND", "normalized observer functional inserted into the selected action"),
    ("LT-GR2d", "J_BOUNDARY_EDGE_OWNER", "BOUNDARY_TO_P3_RELATIVE_KO_INPUT_MAP_EXACT"),
    ("LT-GR2d", "L_COSMOLOGICAL_SOLUTION", "cosmology remain open"),
    # ---- LT-GR2e
    ("LT-GR2e", "L_COSMOLOGICAL_SOLUTION", "derive matter/radiation FLRW perturbations and held-out w(z)"),
    ("LT-GR2e", "A_ACTION_OWNED_BACKGROUND", "an action-owned cosmological solution with fixed initial data"),
    # ---- LT-GR3
    ("LT-GR3", "J_BOUNDARY_EDGE_OWNER", "residual-square parent boundary owner remains unbuilt"),
    ("LT-GR3", "A_ACTION_OWNED_BACKGROUND", "a rival action parent"),
    ("LT-GR3", "D_EULER_BV_BFV", "BV_DOMAIN_OPEN"),
    # ---- LT-GR4
    ("LT-GR4", "M_NATIVE_RG_RUNNING", "compute the native R^2 running sign"),
    ("LT-GR4", "A_ACTION_OWNED_BACKGROUND", "an exact GU-native sign opposite to the ported negative horn"),
    # ---- LT-GR5
    ("LT-GR5", "E_OBSERVATION_REDUCTION", "before observation/BV/domain reduction"),
    ("LT-GR5", "D_EULER_BV_BFV", "REDUCTION_BV_DOMAIN_OPEN"),
    ("LT-GR5", "F_POSITIVITY_PHYSICAL", "common Green/BV/Fock domain"),
    ("LT-GR5", "A_ACTION_OWNED_BACKGROUND", "P_EQUALS_KT_ACTION_OWNER_REJECTED"),
    # NOTE: an LT-GR5 / H_ABSOLUTE_SCALE incidence was asserted on a first pass and
    # REJECTED by the substring certificate -- the `NOT_SCALE_SELECTOR__NORMALIZED_
    # FUNCTIONAL_OPEN` tokens belong to LT-GR2c's frontier grade, not to LT-GR5.
    # LT-GR5 names no scale requirement in v0.258.  Kept as a live control that the
    # certificate has power against the author's own typing.
    # ---- LT-GR6
    ("LT-GR6", "B_K77_OPERATOR_DOMAIN", "Build the physical K77 operator/domain"),
    ("LT-GR6", "C_RELATIVE_INDEX_COUNT", "dependent index/count readout"),
    ("LT-GR6", "D_EULER_BV_BFV", "before full Euler/BV"),
    ("LT-GR6", "F_POSITIVITY_PHYSICAL", "reproduce the Hilbert stress on the physical quotient"),
    ("LT-GR6", "J_BOUNDARY_EDGE_OWNER", "BOUNDARY_TO_P3_RELATIVE_KO_INPUT_MAP_EXACT"),
    ("LT-GR6", "A_ACTION_OWNED_BACKGROUND", "selected-action tangent/Noether complex"),
    # ---- LT-GR7
    ("LT-GR7", "H_ABSOLUTE_SCALE", "derive one absolute gravitational normalization"),
    # ---- LT-SM1
    ("LT-SM1", "I_ZETA_F_BIT", "select the zeta_F/Yang-Mills horn"),
    ("LT-SM1", "A_ACTION_OWNED_BACKGROUND", "a source-action choice fixed by surplus constraints"),
    # ---- LT-SM2
    ("LT-SM2", "H_ABSOLUTE_SCALE", "derive absolute and relative coupling scales"),
    ("LT-SM2", "E_OBSERVATION_REDUCTION", "after symmetry breaking"),
    ("LT-SM2", "A_ACTION_OWNED_BACKGROUND", "a normalized action plus threshold computation"),
    # ---- LT-SM3
    ("LT-SM3", "A_ACTION_OWNED_BACKGROUND", "Derive a native residual-zero action background"),
    ("LT-SM3", "D_EULER_BV_BFV", "proper functional BV/BFV"),
    ("LT-SM3", "F_POSITIVITY_PHYSICAL", "Fredholm/Green domain"),
    ("LT-SM3", "J_BOUNDARY_EDGE_OWNER", "OPPOSITE_EDGE_UNOWNED"),
    ("LT-SM3", "K_COEFFICIENT_SELECTION", "not a selected Cartan restriction"),
    # ---- LT-SM3b
    ("LT-SM3b", "G_SHIAB_SELECTOR", "separate source adjoint Shiab from reconstructed spinor vertex"),
    ("LT-SM3b", "A_ACTION_OWNED_BACKGROUND", "extend the Riemann adapter through the action"),
    # ---- LT-SM4
    ("LT-SM4", "F_POSITIVITY_PHYSICAL", "show the pole is physical"),
    ("LT-SM4", "H_ABSOLUTE_SCALE", "MASS_INTERVAL_EXACT_PHYSICS_OPEN"),
    ("LT-SM4", "K_COEFFICIENT_SELECTION", "a complete constrained pole spectrum"),
    # ---- LT-SM5
    ("LT-SM5", "K_COEFFICIENT_SELECTION", "select coefficients"),
    ("LT-SM5", "E_OBSERVATION_REDUCTION", "map the 14D incidence to 4D masses"),
    ("LT-SM5", "F_POSITIVITY_PHYSICAL", "Build the physical P0/rho(Phi)/Y_K/Y_C/C-reality placement"),
    ("LT-SM5", "A_ACTION_OWNED_BACKGROUND", "a zero-order source-action term with observed Yukawa placement"),
    # ---- LT-SM6
    ("LT-SM6", "A_ACTION_OWNED_BACKGROUND", "Derive the operative second action"),
    ("LT-SM6", "D_EULER_BV_BFV", "source-derived physical BV tangent"),
    ("LT-SM6", "E_OBSERVATION_REDUCTION", "full moving principal map"),
    ("LT-SM6", "F_POSITIVITY_PHYSICAL", "domain and spectrum"),
    ("LT-SM6", "J_BOUNDARY_EDGE_OWNER", "preboundary"),
    ("LT-SM6", "K_COEFFICIENT_SELECTION", "an exact pullback and Hessian with one light Higgs"),
    # ---- LT-SM7
    ("LT-SM7", "K_COEFFICIENT_SELECTION", "identify the QCD theta coefficient"),
    ("LT-SM7", "A_ACTION_OWNED_BACKGROUND", "a source-action topological sector with computed periodic parameter"),
    # ---- LT-SM8
    ("LT-SM8", "A_ACTION_OWNED_BACKGROUND", "Freeze the action-owned A/R pair and normalized connection"),
    ("LT-SM8", "D_EULER_BV_BFV", "build the coupled BV/detour complex"),
    ("LT-SM8", "F_POSITIVITY_PHYSICAL", "positive pairing and nontrivial physical cohomology"),
    ("LT-SM8", "J_BOUNDARY_EDGE_OWNER", "supply endpoint admission"),
    ("LT-SM8", "E_OBSERVATION_REDUCTION", "global descent"),
]

# ---- [E] every incidence is substring-certified against the row's own v0.258 text
for rid, atom, sub in INCIDENCE:
    check("E", f"cert {rid}/{atom[:1]} -> {sub[:44]!r}", rid in TEXT and atom in ATOMS and sub in TEXT[rid])

# ---- [C] negative controls: bound the tokens that could over-broaden B
def rows_containing(tok: str) -> set[str]:
    return {rid for rid in IDS if tok in TEXT[rid]}


check("C", "'zeta_F' occurs in exactly {LT-SM1}", rows_containing("zeta_F") == {"LT-SM1"})
check("C", "'FLRW' occurs in exactly {LT-GR2e}", rows_containing("FLRW") == {"LT-GR2e"})
check("C", "'Shiab' occurs in exactly {LT-GR1b, LT-SM3b}", rows_containing("Shiab") == {"LT-GR1b", "LT-SM3b"})
check("C", "'QCD theta' occurs in exactly {LT-SM7}", rows_containing("QCD theta") == {"LT-SM7"})
check("C", "'R^2 running' occurs in exactly {LT-GR4}", rows_containing("R^2 running") == {"LT-GR4"})
check(
    "C",
    "P3 relative-KO input map exact in exactly the 5-row K77 block",
    rows_containing("BOUNDARY_TO_P3_RELATIVE_KO_INPUT_MAP_EXACT")
    == {"LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR6"},
)
check("C", "LT-GR2a distance is 'none at source-typing grade'", BYID["LT-GR2a"]["distance"].startswith("none at source-typing grade"))
check("C", "no atom is asserted for LT-GR2a", not any(rid == "LT-GR2a" for rid, _, _ in INCIDENCE))

# ---- [C] controls that must have power: deliberately wrong certificates must fail
check("C", "planted-wrong certificate is rejected", "select the zeta_F/Yang-Mills horn" not in TEXT["LT-GR7"])
check(
    "C",
    "live control -- LT-GR5 names NO scale requirement (a first-pass incidence was rejected here)",
    "SCALE" not in TEXT["LT-GR5"] and "scale" not in TEXT["LT-GR5"],
)

ATOM_LIST = sorted(ATOMS)
AIDX = {a: i for i, a in enumerate(ATOM_LIST)}
B = [[0] * len(ATOM_LIST) for _ in IDS]
RIDX = {r: i for i, r in enumerate(IDS)}
for rid, atom, _ in INCIDENCE:
    B[RIDX[rid]][AIDX[atom]] = 1

check("E", "B has 21 rows", len(B) == 21)
check("E", "B has 13 columns", len(B[0]) == 13)
check("E", "every atom is used at least once", all(any(row[j] for row in B) for j in range(len(ATOM_LIST))))

# --------------------------------------------------------------------------
# 3.  rank over Q -- exact fraction-free elimination
# --------------------------------------------------------------------------


def rank_Q(mat: list[list[int]]) -> int:
    M = [[Fraction(x) for x in row] for row in mat]
    nr, nc = len(M), len(M[0])
    r = 0
    for c in range(nc):
        piv = None
        for i in range(r, nr):
            if M[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(nr):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
        if r == nr:
            break
    return r


RANK = rank_Q(B)
LEFT_NULL = len(B) - RANK
BT = [[B[i][j] for i in range(len(B))] for j in range(len(B[0]))]
check("E", "rank(B) == rank(B^T)", rank_Q(BT) == RANK)

# --------------------------------------------------------------------------
# 4.  row-signature partition, zero rows, components, cover, articulation
# --------------------------------------------------------------------------

SIG: dict[tuple[int, ...], list[str]] = {}
for rid in IDS:
    SIG.setdefault(tuple(B[RIDX[rid]]), []).append(rid)

ZERO_ROWS = [rid for rid in IDS if not any(B[RIDX[rid]])]
COUPLED = {tuple(v): k for k, v in SIG.items() if len(v) > 1}


def components(rows_on: list[str], atoms_on: list[str]) -> list[tuple[list[str], list[str]]]:
    """Connected components of the bipartite row/atom graph restricted to atoms_on."""
    parent: dict[str, str] = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for x in rows_on + atoms_on:
        find(x)
    aon = set(atoms_on)
    for rid, atom, _ in INCIDENCE:
        if rid in set(rows_on) and atom in aon:
            union(rid, atom)
    out: dict[str, tuple[list[str], list[str]]] = {}
    for x in rows_on + atoms_on:
        k = find(x)
        rr, aa = out.setdefault(k, ([], []))
        (rr if x in set(rows_on) else aa).append(x)
    return sorted(out.values(), key=lambda p: (-len(p[0]), p[0][:1]))


COMPS = components(IDS, ATOM_LIST)

COVERABLE = [rid for rid in IDS if any(B[RIDX[rid]])]
ROW_ATOMS = {rid: {a for a in ATOM_LIST if B[RIDX[rid]][AIDX[a]]} for rid in IDS}


def min_cover(targets: list[str]) -> tuple[int, list[tuple[str, ...]]]:
    need = [rid for rid in targets if ROW_ATOMS[rid]]
    for size in range(1, len(ATOM_LIST) + 1):
        hits = []
        for combo in itertools.combinations(ATOM_LIST, size):
            cs = set(combo)
            if all(ROW_ATOMS[rid] & cs for rid in need):
                hits.append(combo)
        if hits:
            return size, hits
    return len(ATOM_LIST), []


COVER_SIZE, COVER_SETS = min_cover(IDS)

# atoms that are the SOLE opener of some row (single points of failure)
SOLE: dict[str, list[str]] = {}
for rid in COVERABLE:
    if len(ROW_ATOMS[rid]) == 1:
        SOLE.setdefault(next(iter(ROW_ATOMS[rid])), []).append(rid)

# fan-out
FANOUT = {a: sum(B[i][AIDX[a]] for i in range(len(IDS))) for a in ATOM_LIST}

# articulation: removing the atom orphans a row entirely
ARTIC = {a: [rid for rid in COVERABLE if ROW_ATOMS[rid] == {a}] for a in ATOM_LIST}
ARTIC = {a: v for a, v in ARTIC.items() if v}

# --------------------------------------------------------------------------
# 5.  fork arithmetic against the layer-0 registry
# --------------------------------------------------------------------------

fork_open: list[tuple[str, int]] = []
cur_id, cur_horns, cur_status = None, 0, None
with open(FORKS) as fh:
    for raw in fh:
        s = raw.strip()
        if s.startswith("- id:"):
            if cur_id and cur_status == "open":
                fork_open.append((cur_id, cur_horns))
            cur_id, cur_horns, cur_status = s.split("- id:")[1].strip(), 0, None
        elif s.startswith("status:") and cur_id:
            cur_status = s.split("status:")[1].strip()
        elif s.startswith("- ") and cur_id and cur_status is None:
            cur_horns += 1
if cur_id and cur_status == "open":
    fork_open.append((cur_id, cur_horns))

prod_all = 1
for _, h in fork_open:
    prod_all *= h
LEDGER_FORKS = LED["residue"]["open_discrete_forks"]
LEDGER_PROD = LED["residue"]["open_fork_horn_product"]

sig_h = dict(fork_open).get("SIGNATURE-AMBIENT", 0)
check("E", "registry lists 10 open Layer-0 forks", len(fork_open) == 10)
check("E", "registry open-horn product == 2304", prod_all == 2304)
check("E", "ledger books 9 open forks / product 1152", (LEDGER_FORKS, LEDGER_PROD) == (9, 1152))
check(
    "E",
    "ledger product == registry product / SIGNATURE-AMBIENT horns (exactly one binary fork not booked)",
    sig_h == 2 and prod_all // sig_h == LEDGER_PROD and len(fork_open) - 1 == LEDGER_FORKS,
)
check("E", "1152 == 3*3*2^7 (two ternary + seven binary forks)", 1152 == 3 * 3 * 2**7)

# --------------------------------------------------------------------------
# 6.  bits per grant (information theory), exact as log2 of integers
# --------------------------------------------------------------------------
# Only forks with an integer horn count carry a finite, exactly-stated bit price.

BITS = {
    "I_ZETA_F_BIT": (2, 1),  # 2 horns -> exactly 1 bit
}
ROWS_PER_BIT = {a: (FANOUT[a], b[1]) for a, b in BITS.items()}

# --------------------------------------------------------------------------
# 7.  what moved: migration accounting on this axis
# --------------------------------------------------------------------------

MIGR = LED["migration_history"] + LED["migrations"]
lt_migr: dict[str, int] = {}
lt_meaning: dict[str, int] = {}
for m in MIGR:
    rid = m.get("row_id", "")
    if rid.startswith("LT-"):
        lt_migr[rid] = lt_migr.get(rid, 0) + 1
        if m.get("meaning_changed"):
            lt_meaning[rid] = lt_meaning.get(rid, 0) + 1
NEVER_MIGRATED = [rid for rid in IDS if rid not in lt_migr]

# verdict/reason_kind stability under migration
verdict_moves = 0
for m in MIGR:
    if m.get("row_id", "").startswith("LT-") and m["old"][:2] != m["new"][:2]:
        verdict_moves += 1
check("E", "zero LAGRANGIAN migration ever changed (verdict, reason_kind)", verdict_moves == 0)
check("E", "17 of 21 active LAGRANGIAN rows have never migrated", len(NEVER_MIGRATED) == 17)

# evidence-file concentration
ev: dict[str, list[str]] = {}
for rid in IDS:
    ev.setdefault(BYID[rid].get("evidence", ""), []).append(rid)
check(
    "E",
    "one evidence artifact carries 5 rows (the K77 relative-boundary block)",
    sorted(len(v) for v in ev.values())[-1] == 5,
)

# --------------------------------------------------------------------------
# 7b.  numerical-conditioning lens: single-entry perturbation sweep
# --------------------------------------------------------------------------
# The incidence is a declared typing, so the honest question is how much of the
# conclusion survives one entry being wrong.  Flip every one of the 21*13 cells
# and record whether rank, minimum-cover size, or the unique minimum cover moves.

pert_rank, pert_cover, pert_coverset = 0, 0, 0
LOAD_BEARING: list[str] = []
for i in range(len(IDS)):
    for j in range(len(ATOM_LIST)):
        B[i][j] ^= 1
        ra = {rid: {a for a in ATOM_LIST if B[RIDX[rid]][AIDX[a]]} for rid in IDS}
        saved, ROW_ATOMS = ROW_ATOMS, ra
        try:
            if rank_Q(B) != RANK:
                pert_rank += 1
            cs, sets = min_cover(IDS)
            if cs != COVER_SIZE:
                pert_cover += 1
                LOAD_BEARING.append(f"{IDS[i]}/{ATOM_LIST[j][:1]}:{cs}")
            elif set(sets) != set(COVER_SETS):
                pert_coverset += 1
        finally:
            ROW_ATOMS = saved
            B[i][j] ^= 1
CELLS = len(IDS) * len(ATOM_LIST)
check("E", "perturbation sweep visited every cell", CELLS == 273)
check("E", "B restored after sweep", sum(sum(r) for r in B) == len(INCIDENCE))

# --------------------------------------------------------------------------
# 7c.  optimization duality: exact integrality certificate for the cover
# --------------------------------------------------------------------------
# Lower bound = a set of rows that are pairwise disjoint in their atom sets
# (each needs its own atom).  If that matches the primal cover, the gap is 0.

DUAL = None
for a, b in itertools.combinations(COVERABLE, 2):
    if not (ROW_ATOMS[a] & ROW_ATOMS[b]):
        DUAL = (a, b)
        break
check("E", "dual witness: two rows with disjoint atom sets exist", DUAL is not None)
check("E", "duality gap is exactly 0 (cover 2 == dual bound 2)", COVER_SIZE == 2 and DUAL is not None)

# --------------------------------------------------------------------------
# 7d.  order theory: minimal elements of the atom-set containment poset
# --------------------------------------------------------------------------

MINIMAL = [
    rid
    for rid in COVERABLE
    if not any(other != rid and ROW_ATOMS[other] < ROW_ATOMS[rid] for other in COVERABLE)
]
HAS_BOTTOM = any(all(ROW_ATOMS[r] <= ROW_ATOMS[o] for o in COVERABLE) for r in COVERABLE)
check("E", "the atom-set poset has NO bottom element (no uniquely cheapest row)", not HAS_BOTTOM)

# --------------------------------------------------------------------------
# 7e.  port-Hamiltonian / passivity: stored exactness versus transmitted verdict
# --------------------------------------------------------------------------

EXACT_TOKENS = {rid: TEXT[rid].count("EXACT") for rid in IDS}
MIGRATED_ROWS = ["LT-SM3", "LT-SM5", "LT-SM6", "LT-SM8"]
STORED_IN_MIGRATED = sum(EXACT_TOKENS[r] for r in MIGRATED_ROWS)
STORED_TOTAL = sum(EXACT_TOKENS.values())
check("E", "verdict port is invariant while EXACT storage is nonzero", verdict_moves == 0 and STORED_TOTAL > 0)

# leakage: tokens that a migrating row once held in its mapping grade and that its
# CURRENT grade no longer carries.  The migration record keeps them; the row does not.
LEAK = {}
for rid in MIGRATED_ROWS:
    seen: set[str] = set()
    for m in MIGR:
        if m.get("row_id") == rid:
            for side in (m["old"], m["new"]):
                if len(side) > 2:
                    seen |= {t for t in side[2].split("__") if t.endswith("EXACT") or "_EXACT_" in t}
    cur = {t for t in (BYID[rid].get("mapping_grade", "") or "").split("__") if t.endswith("EXACT") or "_EXACT_" in t}
    LEAK[rid] = (len(seen), len(cur), len(seen - cur))
LEAK_TOTAL = sum(v[2] for v in LEAK.values())
GRADE_LEN_MIGRATED = sum(len(BYID[r].get("mapping_grade", "")) for r in MIGRATED_ROWS)
GRADE_LEN_FROZEN = sum(len(BYID[r].get("mapping_grade", "")) for r in IDS if r not in MIGRATED_ROWS)
check(
    "E",
    "mapping_grade is overwritten, not appended: the 4 worked rows carry fewer EXACT tokens than the 17 idle ones",
    STORED_IN_MIGRATED < STORED_TOTAL - STORED_IN_MIGRATED,
)
check("E", "at least one EXACT token is present in migration history but absent from the current grade", LEAK_TOTAL > 0)

# --------------------------------------------------------------------------
# 7f.  queueing: evidence age distribution (starvation, not scheduling)
# --------------------------------------------------------------------------

import re as _re

DATES = {}
for rid in IDS:
    m = _re.search(r"(\d{4})-(\d{2})-(\d{2})", BYID[rid].get("evidence", ""))
    DATES[rid] = "-".join(m.groups()) if m else "none"
AGE = {}
for rid, dt in DATES.items():
    AGE[dt] = AGE.get(dt, 0) + 1
check("E", "every LAGRANGIAN row's evidence carries a parseable date", "none" not in DATES.values())

# --------------------------------------------------------------------------
# 7g.  Hadamard well-posedness: which rows admit a UNIQUE answer vs a FAMILY
# --------------------------------------------------------------------------

FAMILY_ROWS = sorted({rid for rid in IDS if "FAMILY" in TEXT[rid] or "UNIQUENESS_RETRACTED" in TEXT[rid]})
UNIQUE_ROWS = sorted({rid for rid in IDS if "unique" in TEXT[rid].lower() and "UNIQUENESS_RETRACTED" not in TEXT[rid]})
check("E", "LT-GR2c carries an explicit retracted-uniqueness / one-amplitude family", "LT-GR2c" in FAMILY_ROWS)

# --------------------------------------------------------------------------
# 7h.  topological-term rank from the Delta-5 declared reduction (exact)
# --------------------------------------------------------------------------
# pi_3 of a connected Lie group equals pi_3 of its maximal compact, and pi_3 of a
# compact simple group is Z.  Spin(6) ~ SU(4) (one Z); Spin(4) ~ SU(2)xSU(2) (Z^2).
# Standard-Model comparator: pi_3(SU(3) x SU(2) x U(1)) = Z^2 (U(1) contributes 0).

PI3_GU_K = 1 + 2  # Spin(6) x Spin(4)
PI3_SM = 1 + 1 + 0  # SU(3) x SU(2) x U(1)
check("E", "pi_3 rank of Spin(6) x Spin(4) is 3", PI3_GU_K == 3)
check("E", "pi_3 rank of SU(3) x SU(2) x U(1) is 2", PI3_SM == 2)
check("E", "the Delta-5 group supplies exactly one more theta-angle than the SM", PI3_GU_K - PI3_SM == 1)
check("E", "LT-SM7 is the axis's only topological-term row", rows_containing("QCD theta") == {"LT-SM7"})

# --------------------------------------------------------------------------
# 7i.  so(7,7) integer family behind LT-SM3's 182 (consistency, NOT novelty)
# --------------------------------------------------------------------------

DIM_SO77 = 14 * 13 // 2
RANK_SO77 = 7
check("E", "dim so(7,7) == 91", DIM_SO77 == 91)
check("E", "cotangent parent 2*91 == 182", 2 * DIM_SO77 == 182)
check("E", "Cartan restriction 91+7 == 98", DIM_SO77 + RANK_SO77 == 98)
check("E", "regular coadjoint orbit 91-7 == 84", DIM_SO77 - RANK_SO77 == 84)
check("E", "moment-kernel is Lagrangian in the parent: 182 == 91+91", 2 * DIM_SO77 == DIM_SO77 + DIM_SO77)

# --------------------------------------------------------------------------
# 7j.  taxonomy lens: kinds declared but unused, and the LT-GR7 kind/grade split
# --------------------------------------------------------------------------

DECLARED_KINDS = [k for v in LED["taxonomy"]["verdict_kinds"].values() for k in v]
USED_KINDS = {r["reason_kind"] for r in ALL_ROWS}
UNUSED_KINDS = sorted(k for k in DECLARED_KINDS if k not in USED_KINDS)
check("E", "22 reason kinds are declared", len(DECLARED_KINDS) == 22)
check("E", "6 declared kinds are used zero times in 84 rows", len(UNUSED_KINDS) == 6)
check("E", "PROVEN_UNSUPPLYABLE is declared and unused", "PROVEN_UNSUPPLYABLE" in UNUSED_KINDS)
check("E", "EXTERNAL_DATUM is declared AND in use (so the promotion target exists)", "EXTERNAL_DATUM" in USED_KINDS)

REAL_PARAM_ROWS = sorted(r["id"] for r in LT if r["reason_kind"] == "REAL_PARAMETER")
NOGO_GRADE = sorted(r["id"] for r in LT if "NO_GO" in (r.get("mapping_grade") or ""))
check("E", "the axis has exactly 3 REAL_PARAMETER rows", REAL_PARAM_ROWS == ["LT-GR7", "LT-SM2", "LT-SM7"])
check("E", "LT-GR7 is the axis's only row whose mapping grade asserts a NO_GO", NOGO_GRADE == ["LT-GR7"])
check("E", "LT-SM7 is the ledger's only T0 row", sorted(r["id"] for r in ALL_ROWS if "T0" in (r.get("mapping_grade") or "")) == ["LT-SM7"])
check("E", "LT-GR7 has never migrated (kind unchanged since creation)", "LT-GR7" in NEVER_MIGRATED)

# --------------------------------------------------------------------------
# 8.  float sweep + report
# --------------------------------------------------------------------------


def assert_no_float(obj, path="result"):
    if isinstance(obj, float):
        raise AssertionError(f"float found at {path}")
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_float(v, f"{path}.{k}")
    if isinstance(obj, (list, tuple, set)):
        for i, v in enumerate(obj):
            assert_no_float(v, f"{path}[{i}]")


RESULT = {
    "active_rows": len(IDS),
    "atoms": len(ATOM_LIST),
    "incidence_ones": len(INCIDENCE),
    "rank_Q_B": RANK,
    "left_null_dim": LEFT_NULL,
    "distinct_row_signatures": len(SIG),
    "zero_rows": ZERO_ROWS,
    "coupled_classes": {"|".join(v): len(v) for v in SIG.values() if len(v) > 1},
    "components": [(len(r), len(a)) for r, a in COMPS],
    "min_cover_size": COVER_SIZE,
    "min_cover_count": len(COVER_SETS),
    "articulation_atoms": ARTIC,
    "fanout": FANOUT,
    "never_migrated": NEVER_MIGRATED,
    "migration_counts": lt_migr,
    "registry_open_forks": fork_open,
    "registry_horn_product": prod_all,
    "ledger_open_forks": LEDGER_FORKS,
    "ledger_horn_product": LEDGER_PROD,
    "rows_per_bit": ROWS_PER_BIT,
    "perturbation_cells": CELLS,
    "perturbations_changing_rank": pert_rank,
    "perturbations_changing_cover_size": pert_cover,
    "perturbations_changing_cover_set": pert_coverset,
    "dual_witness": DUAL,
    "poset_minimal_rows": MINIMAL,
    "poset_has_bottom": HAS_BOTTOM,
    "exact_tokens_per_row": EXACT_TOKENS,
    "exact_tokens_total": STORED_TOTAL,
    "exact_tokens_in_the_four_migrated_rows": STORED_IN_MIGRATED,
    "verdict_port_moves": verdict_moves,
    "evidence_date_histogram": AGE,
    "hadamard_family_rows": FAMILY_ROWS,
    "hadamard_unique_rows": UNIQUE_ROWS,
    "pi3_rank_delta5_group": PI3_GU_K,
    "pi3_rank_standard_model": PI3_SM,
    "unused_reason_kinds": UNUSED_KINDS,
    "real_parameter_rows": REAL_PARAM_ROWS,
    "no_go_grade_rows": NOGO_GRADE,
    "load_bearing_cells": LOAD_BEARING,
    "leak_per_row": LEAK,
    "leak_total": LEAK_TOTAL,
    "grade_len_migrated_4": GRADE_LEN_MIGRATED,
    "grade_len_frozen_17": GRADE_LEN_FROZEN,
}
assert_no_float(RESULT)

print("=" * 78)
print("LA-6  effective degrees of freedom -- LAGRANGIAN axis, ledger v0.258 / a148ed80")
print("=" * 78)
for k in [
    "active_rows",
    "atoms",
    "incidence_ones",
    "rank_Q_B",
    "left_null_dim",
    "distinct_row_signatures",
    "zero_rows",
    "min_cover_size",
    "min_cover_count",
]:
    print(f"  {k:26s} {RESULT[k]}")
print()
print("  coupled row classes (identical dependency signature -> never separable):")
for k, v in RESULT["coupled_classes"].items():
    print(f"    {v}  {k}")
print()
print("  bipartite components (rows, atoms):", RESULT["components"])
print()
print("  atom fan-out (rows opened):")
for a, n in sorted(FANOUT.items(), key=lambda kv: (-kv[1], kv[0])):
    star = "  <-- SOLE opener of " + ",".join(ARTIC[a]) if a in ARTIC else ""
    print(f"    {n:2d}  {a}{star}")
print()
print("  minimum certificate sets of size", COVER_SIZE, f"({len(COVER_SETS)} of them):")
for c in COVER_SETS:
    print("    {" + ", ".join(x.split("_", 1)[0] for x in c) + "}  =  " + ", ".join(c))
print()
print("  never migrated (17):", ", ".join(NEVER_MIGRATED))
print("  migrated:", RESULT["migration_counts"])
print()
print("  Layer-0 forks: registry open =", len(fork_open), "product =", prod_all)
print("                 ledger booked =", LEDGER_FORKS, "product =", LEDGER_PROD)
print("                 unbooked fork =", [f for f in fork_open if f[0] == "SIGNATURE-AMBIENT"])
print()
print(f"  conditioning: {CELLS} single-entry flips -> rank moves {pert_rank}, "
      f"cover-size moves {pert_cover}, cover-set moves {pert_coverset}")
print("  duality: primal cover 2 == dual witness", DUAL, "-> integrality gap 0")
print("  poset minimal rows (order-theoretically cheapest):", ", ".join(MINIMAL))
print("  poset has bottom element:", HAS_BOTTOM)
print("  load-bearing cells (flip changes min-cover size):", ", ".join(sorted(set(LOAD_BEARING))))
print("  grade length: 4 worked rows", GRADE_LEN_MIGRATED, "chars | 17 idle rows", GRADE_LEN_FROZEN, "chars")
print("  EXACT-token leak (history_seen, current, lost):", LEAK, "| total lost", LEAK_TOTAL)
print("  EXACT tokens: total", STORED_TOTAL, "| in the 4 migrated rows", STORED_IN_MIGRATED,
      "| verdict-port moves", verdict_moves)
print("  evidence-date histogram:", dict(sorted(AGE.items())))
print("  Hadamard FAMILY rows:", ", ".join(FAMILY_ROWS))
print("  Hadamard UNIQUE-claiming rows:", ", ".join(UNIQUE_ROWS))
print("  reason kinds declared but never used (84 rows):", ", ".join(UNUSED_KINDS))
print("  REAL_PARAMETER rows:", ", ".join(REAL_PARAM_ROWS), "| rows whose grade asserts NO_GO:", ", ".join(NOGO_GRADE))
print("  pi_3 rank: Delta-5 group Spin(6)xSpin(4) =", PI3_GU_K, "| SM SU(3)xSU(2)xU(1) =", PI3_SM)
print()

npass = sum(1 for _, _, ok in CHECKS if ok)
byclass: dict[str, list[int]] = {}
for tag, _, ok in CHECKS:
    d = byclass.setdefault(tag, [0, 0])
    d[1] += 1
    d[0] += 1 if ok else 0
print("-" * 78)
print(f"CERTIFICATE: {npass}/{len(CHECKS)} checks pass; no load-bearing float (swept).")
print("  by class:", {k: f"{v[0]}/{v[1]}" for k, v in sorted(byclass.items())})
for tag, label, ok in CHECKS:
    if not ok:
        print(f"  FAIL [{tag}] {label}")
print("-" * 78)
sys.exit(0 if npass == len(CHECKS) else 1)
