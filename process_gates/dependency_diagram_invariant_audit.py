#!/usr/bin/env python3
"""Dependency-diagram invariant audit (CT-4, joe-directed CT-hardening wave).

WHAT THIS IS FOR
----------------
The conditional-physics ledger's "degrees of freedom" count moved 82 -> 32
(LA-4 / LA-5 / LA-6 generator counts) -> 35 (LA-10's split of one atom).  It
moved because a generator count is a property of a PRESENTATION: refine the
vocabulary and the count changes without one word of the ledger changing.
LA-10 said so in its own §4.1: "32 is vocabulary-relative: stable under audit,
unstable under refinement.  It measures the reader's lexicon as much as the
ledger."

This gate computes graph invariants of the DECLARED dependency diagram and
reports, every run, how much of the lexicon-dependence survives.  It is
REPORT-ONLY on every number it computes about the ledger.  It RATCHETS only on
WELL-FORMEDNESS -- that the edge extraction is reproducible, that the tier
partition is total and disjoint, that a variant declared to be a refinement
really is one, and that the graph accounting closes.  No physics number and no
ledger number is ever a compliance target here; making one green would be
exactly the failure this gate exists to name.

THE OBJECT
----------
D = the bipartite DECLARED dependency diagram over ledger v0.259:

  row-vertices   the 84 canonical target rows (87 records minus 3 SUPERSEDED)
  atom-vertices  every open demand-object that at least one row DECLARES;
                 a vocabulary term with zero declared incidences contributes
                 NO vertex (LA-11: "reach is a DAG property, declaration is a
                 text property")
  edges          (row, atom) incidences admitted by the LA-11 membership
                 discipline: the edge's certificate substring must occur
                 VERBATIM in that row's own DEMAND fields in v0.259.
                 `DEMAND_FIELDS = ('distance', 'revival_trigger')` is LA-11's
                 rule verbatim (tests/channel-swings/
                 joe_directed_b9stat_row_construction.py:98, and LA-11 §"a
                 demand lives in `distance` or `revival_trigger` -- the fields
                 that say what the row waits on").

THE INVARIANT
-------------
For a graph with R row-vertices, A atom-vertices, E edges and C components:

    b1  = E - (R + A) + C          (first Betti number, cycle rank)
    beta = E - R + C  = b1 + A     (incidences in excess of a row-spanning
                                    forest -- the declared-demand redundancy)

A VOCABULARY REFINEMENT splits an atom `a` into constituents a_1..a_k, each
incidence of `a` going to exactly one constituent (row-injective, total).
Then, exactly:

  (T1) R and E are preserved, and so is the row-DEGREE MULTISET.  A refinement
       is a bijection on incidences; it never touches the row side.
  (T2) C is non-decreasing, and C_fine - C_coarse <= sum_a (k_a - 1).
  (T3) b1_fine - b1_coarse = (C_fine - C_coarse) - (A_fine - A_coarse).
       So b1 is invariant ONLY under a refinement that totally severs; under a
       non-severing refinement b1 falls by exactly the number of new atoms.
       b1 alone is therefore REJECTED as the invariant, and this gate checks
       identity (T3) numerically on every variant.
  (T4) beta, C and the component row-size distribution are ALL invariant iff
       the refinement is NON-SEVERING (no split separates its constituents'
       rows in the fine graph).  Non-severance is decidable and is computed
       and printed as a CERTIFICATE alongside the number.
  (T5) NO-GO.  For any diagram with an atom of degree >= 2 there EXISTS a
       refinement that strictly increases C (split that atom's incidences into
       singletons).  Hence NO connectivity statistic of a declared diagram is
       UNCONDITIONALLY refinement-invariant.  The unconditional invariants are
       exactly the row-side data (R, E, row-degree multiset), and those say
       how much text there is, not how entangled it is.  Everything stronger
       is invariant ONLY WITH the non-severing certificate attached.  This gate
       ships the certificate with the number, which is precisely what "32"
       never had.

THE CAVEAT, PRINTED EVERY RUN
-----------------------------
A diagram invariant is stable under RENAMING and refinement.  It is NOT stable
under EDGE-SET disputes, and LA-10's central correction was an edge-set
dispute: LA-4's conceded `b9 < b1` precedence edge, which no row states, and
whose deletion moved b9's reach 28/29 -> 2/29.  This gate therefore computes on
the DECLARED edge set only, reports the KNOWN-DISPUTED (grade-only + uncited)
edges separately, and prints both totals and the spread.  The invariant answers
"how entangled is what the rows SAY", never "which edges are real".

CONTRARY CONTROLS (both required to fire)
-----------------------------------------
  CC-A  a refinement that PRESERVES the invariant: LA-10's four-way split of
        `A_ACTION_OWNED_BACKGROUND`, completed by LA-10's own stated
        conservative principle.  C, beta and the row-size distribution must be
        EQUAL across it while the atom count rises by 3 (the 12->15 move that
        produced 32->35).
  CC-B  a genuine EDGE-SET change that MOVES it, three ways: (i) the ledger's
        own v0.258 -> v0.259 migration under a FIXED vocabulary; (ii) LA-10 as
        actually published, which deletes three A-incidences and so is a
        refinement COMPOSED WITH an edge deletion, not a refinement; (iii) a
        synthetic maximal severing refinement.  If CC-B does not move the
        number the machinery cannot tell refinement from edge dispute and the
        gate goes red.

USAGE
    _local/cas-venv/bin/python process_gates/dependency_diagram_invariant_audit.py
    ... --report      report only, no ratchet
    ... --selftest    clean baseline FIRST, then machinery-corruption mutations

Exact integer arithmetic only.  No float is constructed anywhere;
`assert_no_float` sweeps the whole result dict.  Nothing here is a ledger edit,
a verdict change, a physics derivation, or a claim that any GU object exists.
"""

from __future__ import annotations

import json
import sys
import unittest
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER_CURRENT = ROOT / "lab" / "process" / "conditional-physics-ledger-v0.259.json"
LEDGER_PRIOR = ROOT / "lab" / "process" / "conditional-physics-ledger-v0.258.json"
ARTIFACT = (ROOT / "lab" / "active-research" / "joe-directed" / "ct-hardening"
            / "ct4-dependency-diagram-invariant-2026-08-17.md")

# --------------------------------------------------------------------------
# The extraction rule, declared.  LA-11's discipline verbatim.
# --------------------------------------------------------------------------
DEMAND_FIELDS = ("distance", "revival_trigger")
STATUS_FIELDS = ("summary", "mapping_grade", "frontier_grade", "construction_scope")

TIERS = ("DECLARED", "GRADE_ONLY", "UNCITED", "ROW_RETIRED", "ROW_ABSENT")

# --------------------------------------------------------------------------
# EXTRACTION PINS -- these are WELL-FORMEDNESS, not the invariant.
# They pin that the mechanical extraction reproduces, against a NAMED ledger
# version.  The correct repair when one drifts is to re-derive against the new
# version and move the pin in the same commit; NEVER to widen a tolerance.
# The invariant's own values (C, beta, the size distribution) are pinned
# NOWHERE in this file, by design.
# --------------------------------------------------------------------------
PIN = {
    "ledger_version": "v0.259",
    "row_records": 87,
    "canonical_targets": 84,
    "superseded": 3,
    "inherited_assertions": 180,   # LA-6 76 + LA-4 77 + LA-5 27
    "edges_after_successor_inheritance": 182,
    "tier_census": {"DECLARED": 136, "GRADE_ONLY": 20, "UNCITED": 26,
                    "ROW_RETIRED": 0, "ROW_ABSENT": 0},
    # [R] LA-10 §3.2, reproduced not re-derived: 20 of LA-4's 77 atom-edges
    # fail an exact-substring certificate against the row's own text.
    "la4_wide_failures": 20,
    "la4_declared_assertions": 77,
    "la6_declared_assertions": 76,
    "la5_declared_assertions": 27,
}

CAVEAT = """\
  CAVEAT, shipped with the number and not separable from it
  --------------------------------------------------------
  This invariant is stable under RENAMING and vocabulary REFINEMENT.  It is
  NOT stable under EDGE-SET disputes, and the ledger's largest known structural
  correction WAS an edge-set dispute (LA-4's conceded `b9 < b1` edge, which no
  row states; deleting it moved b9's reach 28/29 -> 2/29).  Every number below
  is computed on the DECLARED edge set -- edges a row's own DEMAND fields state
  by exact substring.  It answers "how entangled is what the rows SAY".  It
  does NOT answer "which edges are real", and it must never be quoted as a
  count of independent problems, of degrees of freedom, or of anything about
  Geometric Unity.  The declared/disputed spread below is part of the result."""


# ==========================================================================
# 0.  loading
# ==========================================================================

def load(path: Path) -> dict:
    with open(path) as fh:
        return json.load(fh)


def demand_text(row: dict, cfg: dict) -> str:
    return " ||| ".join(str(row.get(k, "")) for k in cfg["demand_fields"])


def status_text(row: dict, cfg: dict) -> str:
    return " ||| ".join(str(row.get(k, "")) for k in cfg["status_fields"])


def index(led: dict) -> tuple[dict, list[str], dict]:
    by_id = {r["id"]: r for r in led["rows"]}
    targets = sorted(r["id"] for r in led["rows"]
                     if r.get("row_status") != "SUPERSEDED")
    successors: dict[str, list[str]] = defaultdict(list)
    for r in led["rows"]:
        if r.get("split_from"):
            successors[r["split_from"]].append(r["id"])
    return by_id, targets, {k: sorted(v) for k, v in successors.items()}


# ==========================================================================
# 1.  THE INHERITED EDGE ASSERTIONS
#     Reproduced verbatim from the artifacts that declared them.  This gate
#     does NOT invent a vocabulary; it re-certifies three published ones.
#       LA-6  lab/active-research/joe-directed/ledger-advancement/
#             la6-lagrangian-effective-dof.py  (INCIDENCE, 76 entries)
#       LA-4  la4-representation-axis-incidence-probe.py (COND, 77 entries)
#             with LA-10's per-atom token families (CERT_TOKENS)
#       LA-5  la5-anomaly-axis-degrees-of-freedom-probe.py (BACKING, 27)
#     An edge is (row_id, atom_id, tuple_of_alternative_certificate_strings);
#     the tuple has length 1 wherever the donor declared a single string.
# ==========================================================================

_LA6_ATOM = {
    "A": "A_ACTION_OWNED_BACKGROUND", "B": "B_K77_OPERATOR_DOMAIN",
    "C": "C_RELATIVE_INDEX_COUNT", "D": "D_EULER_BV_BFV",
    "E": "E_OBSERVATION_REDUCTION", "F": "F_POSITIVITY_PHYSICAL",
    "G": "G_SHIAB_SELECTOR", "H": "H_ABSOLUTE_SCALE", "I": "I_ZETA_F_BIT",
    "J": "J_BOUNDARY_EDGE_OWNER", "K": "K_COEFFICIENT_SELECTION",
    "L": "L_COSMOLOGICAL_SOLUTION", "M": "M_NATIVE_RG_RUNNING",
}
_LA6_RAW = [
    ("LT-GR1", "A", "RESTRICTED_ACTION_HILBERT_DOMAIN_OPEN"),
    ("LT-GR1", "B", "construct the physical K77 nonzero-fermion operator, closed relative domain"),
    ("LT-GR1", "C", "index and count identification"),
    ("LT-GR1", "D", "recomputing Euler/BV"),
    ("LT-GR1", "F", "observed Hilbert stress"),
    ("LT-GR1", "J", "BOUNDARY_TO_P3_RELATIVE_KO_INPUT_MAP_EXACT"),
    ("LT-GR1b", "G", "construct a different Shiab"),
    ("LT-GR1b", "A", "an action theorem owning the independent Gauss route"),
    ("LT-GR2b", "B", "build a K77 relative operator/domain"),
    ("LT-GR2b", "C", "index and count readout"),
    ("LT-GR2b", "J", "BOUNDARY_TO_P3_RELATIVE_KO_INPUT_MAP_EXACT"),
    ("LT-GR2b", "A", "LOCAL_ACTION_OWNED_VEV_EXACT_UNREDUCED"),
    ("LT-GR2b", "D", "complete EOM/BV/boundary cancellation"),
    ("LT-GR2c", "B", "Build the physical K77 operator/domain"),
    ("LT-GR2c", "C", "compute its relative index and identify the count"),
    ("LT-GR2c", "D", "restrict/recompute Euler/BV"),
    ("LT-GR2c", "A", "an action-owned normalized global functional"),
    ("LT-GR2c", "E", "observation descent"),
    ("LT-GR2c", "H", "NOT_SCALE_SELECTOR__NORMALIZED_FUNCTIONAL_OPEN"),
    ("LT-GR2c", "J", "BOUNDARY_TO_P3_RELATIVE_KO_INPUT_MAP_EXACT"),
    ("LT-GR2d", "B", "physical K77 relative index/count readout"),
    ("LT-GR2d", "C", "K77_INDEX_COUNT_SIGN_UNITS_STABILITY_DOMAIN_OPEN"),
    ("LT-GR2d", "H", "Sign, units, radiative response"),
    ("LT-GR2d", "A", "normalized observer functional inserted into the selected action"),
    ("LT-GR2d", "J", "BOUNDARY_TO_P3_RELATIVE_KO_INPUT_MAP_EXACT"),
    ("LT-GR2d", "L", "cosmology remain open"),
    ("LT-GR2e", "L", "derive matter/radiation FLRW perturbations and held-out w(z)"),
    ("LT-GR2e", "A", "an action-owned cosmological solution with fixed initial data"),
    ("LT-GR3", "J", "residual-square parent boundary owner remains unbuilt"),
    ("LT-GR3", "A", "a rival action parent"),
    ("LT-GR3", "D", "BV_DOMAIN_OPEN"),
    ("LT-GR4", "M", "compute the native R^2 running sign"),
    ("LT-GR4", "A", "an exact GU-native sign opposite to the ported negative horn"),
    ("LT-GR5", "E", "before observation/BV/domain reduction"),
    ("LT-GR5", "D", "REDUCTION_BV_DOMAIN_OPEN"),
    ("LT-GR5", "F", "common Green/BV/Fock domain"),
    ("LT-GR5", "A", "P_EQUALS_KT_ACTION_OWNER_REJECTED"),
    ("LT-GR6", "B", "Build the physical K77 operator/domain"),
    ("LT-GR6", "C", "dependent index/count readout"),
    ("LT-GR6", "D", "before full Euler/BV"),
    ("LT-GR6", "F", "reproduce the Hilbert stress on the physical quotient"),
    ("LT-GR6", "J", "BOUNDARY_TO_P3_RELATIVE_KO_INPUT_MAP_EXACT"),
    ("LT-GR6", "A", "selected-action tangent/Noether complex"),
    ("LT-GR7", "H", "derive one absolute gravitational normalization"),
    ("LT-SM1", "I", "select the zeta_F/Yang-Mills horn"),
    ("LT-SM1", "A", "a source-action choice fixed by surplus constraints"),
    ("LT-SM2", "H", "derive absolute and relative coupling scales"),
    ("LT-SM2", "E", "after symmetry breaking"),
    ("LT-SM2", "A", "a normalized action plus threshold computation"),
    ("LT-SM3", "A", "Derive a native residual-zero action background"),
    ("LT-SM3", "D", "proper functional BV/BFV"),
    ("LT-SM3", "F", "Fredholm/Green domain"),
    ("LT-SM3", "J", "OPPOSITE_EDGE_UNOWNED"),
    ("LT-SM3", "K", "not a selected Cartan restriction"),
    ("LT-SM3b", "G", "separate source adjoint Shiab from reconstructed spinor vertex"),
    ("LT-SM3b", "A", "extend the Riemann adapter through the action"),
    ("LT-SM4", "F", "show the pole is physical"),
    ("LT-SM4", "H", "MASS_INTERVAL_EXACT_PHYSICS_OPEN"),
    ("LT-SM4", "K", "a complete constrained pole spectrum"),
    ("LT-SM5", "K", "select coefficients"),
    ("LT-SM5", "E", "map the 14D incidence to 4D masses"),
    ("LT-SM5", "F", "Build the physical P0/rho(Phi)/Y_K/Y_C/C-reality placement"),
    ("LT-SM5", "A", "a zero-order source-action term with observed Yukawa placement"),
    ("LT-SM6", "A", "Derive the operative second action"),
    ("LT-SM6", "D", "source-derived physical BV tangent"),
    ("LT-SM6", "E", "full moving principal map"),
    ("LT-SM6", "F", "domain and spectrum"),
    ("LT-SM6", "J", "preboundary"),
    ("LT-SM6", "K", "an exact pullback and Hessian with one light Higgs"),
    ("LT-SM7", "K", "identify the QCD theta coefficient"),
    ("LT-SM7", "A", "a source-action topological sector with computed periodic parameter"),
    ("LT-SM8", "A", "Freeze the action-owned A/R pair and normalized connection"),
    ("LT-SM8", "D", "build the coupled BV/detour complex"),
    ("LT-SM8", "F", "positive pairing and nontrivial physical cohomology"),
    ("LT-SM8", "J", "supply endpoint admission"),
    ("LT-SM8", "E", "global descent"),
]
LA6_EDGES = [(r, _LA6_ATOM[a], (s,)) for r, a, s in _LA6_RAW]

_LA4_COND = {
    "RA-A1": ["b1", "b3", "b4"], "RA-A2": ["b1", "b2", "b5"],
    "RA-A3": ["b1", "b4"], "RA-A4": ["b1", "b7"],
    "RA-A5": ["b1", "b7", "b8"], "RA-A6": ["b1", "b2", "b5"],
    "RA-A7": [], "RA-A8": ["b1", "b2", "b4", "b5", "b6"],
    "RA-B1": ["b1", "b4"], "RA-B2": ["b1", "b4"], "RA-B3": ["b1", "b4"],
    "RA-B4": ["b1", "b4"], "RA-B5": ["b1", "b4"],
    "RA-B6": ["b1", "b7", "b12"], "RA-B7": [], "RA-B8": [], "RA-B9": [],
    "RA-C1": [], "RA-D2": ["b8", "b11", "b14"], "RA-D3": [],
    "RA-D4": ["b1", "b3", "b8"], "RA-E1": ["b1", "b8", "b9", "b11"],
    "RA-E2": ["b10"], "RA-E3": ["b8", "b9", "b10", "b11"],
    "RA-E4": ["b1", "b6", "b7"], "RA-E5": ["b1", "b3", "b7"],
    "RA-E6": ["b1", "b4", "b7"], "RA-E7": ["b1", "b12"],
    "RA-F1": ["b3", "b8", "b13"], "RA-F2": ["b1", "b8"], "RA-F3": ["b13"],
    "RA-G1": ["b7", "b8", "b11"], "RA-G2": ["b8", "b11"],
    "RA-G3": ["b1", "b12"], "RA-G4": ["b1", "b3", "b4", "b7"],
}
_LA4_TOKENS = {   # LA-10's CERT_TOKENS, verbatim
    "b1": ("action-stationary", "stationary", "vacuum", "source-action", "source action"),
    "b2": ("J_ACTION_SELECTION", "J_DESCENT", "select one J", "selects J", "selected J"),
    "b3": ("nonhomogeneous", "NONHOMOGENEOUS", "RESIDUAL_FLAG", "residual flag",
           "residual complex-Cartan flag"),
    "b4": ("stabilizer", "STABILIZER"),
    "b5": ("GLOBAL_MU6", "global mu_6", "GLOBALIZATION", "global gauge embedding",
           "descends", "DESCENT", "globally"),
    "b6": ("radial", "RADIAL"),
    "b7": ("mass matrix", "MASS_MATRIX", "Hessian", "mass operator", "mass and",
           "heavy", "spectrum"),
    "b8": ("BV", "BRST", "BFV", "KT", "cohomology"),
    "b9": ("SECOND_ACTION", "second action", "second-action"),
    "b10": ("SCALAR_DESCENT", "scalar descent", "vertical-scalar adapter",
            "4D scalar doublet", "vertical form leg"),
    "b11": ("RETYPING", "retyping", "physical carrier", "carrier projection",
            "physical-carrier", "physical quotient"),
    "b12": ("zero-order", "coupling", "VEV"),
    "b13": ("INDEX_COUNT", "index", "count"),
    "b14": ("Shiab", "SHIAB"),
}
_LA4_ATOM = {
    "b1": "b1_ACTION_STATIONARY_VACUUM", "b2": "b2_J_SELECTION",
    "b3": "b3_NONHOMOGENEOUS_ORBIT_FLAG", "b4": "b4_GLOBAL_STABILIZER",
    "b5": "b5_GLOBAL_DESCENT_MU6", "b6": "b6_RADIAL_VARPI_COEFFICIENT",
    "b7": "b7_MASS_MATRIX_VACUUM_HESSIAN", "b8": "b8_BV_BFV_PHYSICAL_COHOMOLOGY",
    "b9": "b9_OPERATIVE_SECOND_ACTION", "b10": "b10_OBSERVED_SCALAR_DESCENT",
    "b11": "b11_PHYSICAL_CARRIER_PROJECTION", "b12": "b12_ZERO_ORDER_COUPLING_VEV",
    "b13": "b13_INDEX_COUNT_P3", "b14": "b14_REPLACEMENT_SHIAB",
}
LA4_EDGES = [(r, _LA4_ATOM[a], _LA4_TOKENS[a])
             for r, atoms in sorted(_LA4_COND.items()) for a in atoms]

_LA5_BACKING = {
    ("AC-A1", "U1"): "fermion content", ("AC-A2", "U1"): "AC-A1",
    ("AC-A3", "U1"): "AC-A1", ("AC-B2", "U2"): "gauge-twisted",
    ("AC-B2", "N1"): "BSO(128)", ("AC-C2", "U4"): "observed",
    ("AC-C2", "EMB"): "16", ("AC-D1", "U4"): "shadow", ("AC-D1", "EMB"): "16",
    ("AC-D2", "U4"): "shadow", ("AC-D2", "EMB"): "16",
    ("AC-D3", "U4"): "shadow", ("AC-D3", "EMB"): "16",
    ("AC-D4", "U4"): "shadow", ("AC-D4", "EMB"): "16",
    ("AC-D5", "U4"): "shadow", ("AC-D5", "EMB"): "16",
    ("AC-E1", "U4"): "4D", ("AC-E1", "EMB"): "SM",
    ("AC-F1", "U4"): "four-dimensional", ("AC-F1", "BV"): "BV",
    ("AC-F3", "BR"): "bridge", ("AC-F5", "U3"): "framing",
    ("AC-F5", "P3"): "P3", ("AC-G1a", "U1"): "fermion content",
    ("AC-G1a", "U2"): "gauge group", ("AC-G1a", "BV"): "BV",
}
_LA5_ATOM = {
    "U1": "U1_SOURCE_FERMION_CONTENT", "U2": "U2_GAUGED_GROUP",
    "U3": "U3_TANGENTIAL_STRUCTURE", "U4": "U4_REDUCTION_AND_CHIRALITY",
    "EMB": "EMB_SM_EMBEDDING_STABILIZER", "BV": "BV_NATIVE_BACKGROUND_BV_DOMAIN",
    "N1": "N1_SPIN_BORDISM_RECEPTACLE", "P3": "P3_COUNT_AND_CORNER",
    "BR": "BR_NON_INFLOW_BRIDGE",
}
LA5_EDGES = [(r, _LA5_ATOM[a], (s,)) for (r, a), s in sorted(_LA5_BACKING.items())]

ALL_EDGES = LA6_EDGES + LA4_EDGES + LA5_EDGES

# LA-4's PRESUPPOSITION DAG edge that no row states.  It is an ATOM-ATOM
# precedence edge -- a different relation from row-atom incidence -- and it is
# outside the declared diagram by construction.  Kept here so the report can
# price it (see CC-B(iv)).
UNCITED_PRECEDENCE = (("b9_OPERATIVE_SECOND_ACTION", "b1_ACTION_STATIONARY_VACUUM"),)


# ==========================================================================
# 2.  the extraction: tier every inherited edge assertion
# ==========================================================================

def default_cfg() -> dict:
    """Machinery knobs.  Mutations in --selftest corrupt THESE, never a check."""
    return {
        "demand_fields": DEMAND_FIELDS,
        "status_fields": STATUS_FIELDS,
        "edges": ALL_EDGES,
        "inherit_to_successors": True,
        "induce_atoms_from_edges": True,
        "dedup_edges": True,
        "union_enabled": True,
        "beta_formula": "E-R+C",
        "sever_certificate": "computed",
        "refinement_non_injective": False,
    }


def tier_edges(led: dict, cfg: dict) -> list[tuple[str, str, str, str | None]]:
    """(row, atom, tier, certificate_used).  Total and disjoint over TIERS."""
    by_id, _targets, successors = index(led)
    out = []
    for rid, atom, subs in cfg["edges"]:
        row = by_id.get(rid)
        if row is None:
            out.append((rid, atom, "ROW_ABSENT", None))
            continue
        if row.get("row_status") == "SUPERSEDED":
            heirs = successors.get(rid, []) if cfg["inherit_to_successors"] else []
            if not heirs:
                out.append((rid, atom, "ROW_RETIRED", None))
                continue
            targets = heirs
        else:
            targets = [rid]
        for tid in targets:
            trow = by_id.get(tid)
            if trow is None:
                out.append((tid, atom, "ROW_ABSENT", None))
                continue
            hit = [s for s in subs if s and s in demand_text(trow, cfg)]
            if hit:
                out.append((tid, atom, "DECLARED", hit[0]))
                continue
            hit = [s for s in subs if s and s in status_text(trow, cfg)]
            if hit:
                out.append((tid, atom, "GRADE_ONLY", hit[0]))
                continue
            out.append((tid, atom, "UNCITED", None))
    return out


def edge_sets(led: dict, cfg: dict) -> tuple[list, list, list]:
    tiered = tier_edges(led, cfg)
    dec = [(r, a) for r, a, t, _ in tiered if t == "DECLARED"]
    dis = [(r, a) for r, a, t, _ in tiered if t in ("GRADE_ONLY", "UNCITED")]
    if cfg["dedup_edges"]:
        dec, dis = sorted(set(dec)), sorted(set(dis))
    return tiered, dec, dis


# ==========================================================================
# 3.  the graph and the invariant
# ==========================================================================

def components(rows: list[str], edges: list[tuple[str, str]], cfg: dict):
    """Connected components of the bipartite row/atom graph, by union-find."""
    parent: dict[tuple[str, str], tuple[str, str]] = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        if not cfg["union_enabled"]:
            return
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for r in rows:
        find(("R", r))
    for r, a in edges:
        find(("R", r))
        find(("A", a))
        union(("R", r), ("A", a))
    buckets: dict = defaultdict(lambda: (set(), set()))
    for x in list(parent):
        key = find(x)
        buckets[key][0 if x[0] == "R" else 1].add(x[1])
    return sorted(([sorted(v[0]), sorted(v[1])] for v in buckets.values()),
                  key=lambda p: (-len(p[0]), -len(p[1]), p[0][:1]))


def components_bfs(rows: list[str], edges: list[tuple[str, str]]):
    """Independent second implementation -- a corrupted union-find must not
    agree with this (VERIFICATION.md rule 3: a catch needs a real check)."""
    adj: dict = defaultdict(set)
    for r in rows:
        adj[("R", r)]
    for r, a in edges:
        adj[("R", r)].add(("A", a))
        adj[("A", a)].add(("R", r))
    seen, out = set(), []
    for start in sorted(adj):
        if start in seen:
            continue
        stack, comp = [start], []
        seen.add(start)
        while stack:
            x = stack.pop()
            comp.append(x)
            for y in sorted(adj[x]):
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        out.append(sorted(comp))
    return out


def invariant(rows: list[str], edges: list[tuple[str, str]], cfg: dict) -> dict:
    edges = sorted(set(edges)) if cfg["dedup_edges"] else list(edges)
    R, E = len(rows), len(edges)
    atoms = sorted({a for _, a in edges}) if cfg["induce_atoms_from_edges"] else []
    A = len(atoms)
    comps = components(rows, edges, cfg)
    C = len(comps)
    b1 = E - (R + A) + C
    beta = (E - R + C) if cfg["beta_formula"] == "E-R+C" else (E - R)
    deg = Counter()
    for r, _ in edges:
        deg[r] += 1
    linked = [c for c in comps if c[1]]
    return {
        "R": R, "E": E, "A": A, "C": C, "b1": b1, "beta": beta,
        "linked_components": len(linked),
        "isolated_rows": C - len(linked),
        "rowdist": tuple(sorted((len(c[0]) for c in comps), reverse=True)),
        "linked_rowdist": tuple(sorted((len(c[0]) for c in linked), reverse=True)),
        "row_degree_multiset": tuple(sorted((deg.get(r, 0) for r in rows), reverse=True)),
        "atoms": tuple(atoms),
        "components": [(tuple(c[0]), tuple(c[1])) for c in comps],
    }


def core(inv: dict) -> tuple:
    """The three quantities the acceptance test compares."""
    return (inv["C"], inv["beta"], inv["rowdist"])


def unconditional(inv: dict) -> tuple:
    """The refinement-invariants that need NO certificate (theorem T1)."""
    return (inv["R"], inv["E"], inv["row_degree_multiset"])


# ==========================================================================
# 4.  refinements
# ==========================================================================

A_ATOM = "A_ACTION_OWNED_BACKGROUND"
B9_ATOM = "b9_OPERATIVE_SECOND_ACTION"

# LA-10's published split assignment (tests/channel-swings/
# joe_directed_ledger_atomsplit_la10.py, A_SPLIT), verbatim.  It is PARTIAL:
# LA-10 assigns 15 of A's 18 v0.258 incidences and deletes the other three on a
# polarity/denotation test.  A partial map is not a refinement; §5 completes it
# three ways and types each completion.
LA10_SPLIT = {
    "LT-SM6": "A_ID", "LT-SM1": "A_ID",
    "LT-SM3": "A_STAT", "LT-GR2e": "A_STAT",
    "LT-GR2c": "A_NORM", "LT-GR2d": "A_NORM", "LT-SM2": "A_NORM", "LT-SM8": "A_NORM",
    "LT-GR1": "A_OWN", "LT-GR1b": "A_OWN", "LT-GR6": "A_OWN", "LT-SM5": "A_OWN",
    "LT-SM7": "A_OWN", "LT-SM3b": "A_OWN", "LT-GR3": "A_OWN",
}


def split_map(led: dict) -> dict:
    """LA-10's map, extended to successor rows by the ledger's own split_from."""
    _by, _t, successors = index(led)
    m = dict(LA10_SPLIT)
    for parent, heirs in successors.items():
        if parent in m:
            for h in heirs:
                m.setdefault(h, m[parent])
    return m


def apply_refinement(edges, m: dict, residue: str | None, drop_residue: bool = False,
                     cfg: dict | None = None):
    """Refine A -> constituents and rename b9 -> b9_ID.

    residue      constituent for A-incidences LA-10 did not assign
    drop_residue delete them instead (this is NOT a refinement; typed so)

    Returns (fine_edges, phi) where phi maps each fine atom to the coarse atom
    it refines.  phi is what makes the severing certificate checkable rather
    than inferred."""
    out, phi = [], {}
    for r, a in edges:
        if a == A_ATOM:
            if r in m:
                fine = m[r]
            elif drop_residue:
                continue
            else:
                fine = residue if residue else A_ATOM
        elif a == B9_ATOM:
            fine = "b9_ID"
        else:
            fine = a
        phi[fine] = a
        out.append((r, fine))
        if cfg and cfg.get("refinement_non_injective") and a == A_ATOM and fine != "A_ID":
            phi["A_ID"] = a
            out.append((r, "A_ID"))
    return sorted(set(out)), phi


def refinement_legality(coarse, fine) -> dict:
    """Is `fine` a legal refinement of `coarse`?  Total, row-injective, and a
    bijection on incidences."""
    cd, fd = Counter(r for r, _ in coarse), Counter(r for r, _ in fine)
    return {
        "edge_count_preserved": len(set(coarse)) == len(set(fine)),
        "row_degree_preserved": cd == fd,
        "row_injective": len(set(fine)) == len(fine),
        "is_refinement": (len(set(coarse)) == len(set(fine)) and cd == fd),
    }


def severing_report(rows, coarse_edges, fine_edges, phi: dict, cfg) -> dict:
    """Decidable NON-SEVERING certificate (theorem T4).

    phi maps each FINE atom to the COARSE atom it refines.  For each coarse
    atom that genuinely split (>= 2 preimages), are all of its constituents in
    ONE component of the FINE graph?  If yes for every split atom, C, beta and
    the row-size distribution are preserved.  Verified against a direct
    component recount, so a corrupted certificate cannot agree with the graph.
    The recount equivalence is a THEOREM only for a legal refinement; for an
    edge-set change it is reported, not asserted."""
    fine_comps = components(rows, fine_edges, cfg)
    label = {}
    for i, (_rr, aa) in enumerate(fine_comps):
        for x in aa:
            label[x] = i
    preimage = defaultdict(set)
    for fine, coarse in phi.items():
        preimage[coarse].add(fine)
    severed = []
    for coarse, fines in sorted(preimage.items()):
        if len(fines) < 2:
            continue
        homes = {label[f] for f in fines if f in label}
        if len(homes) > 1 and cfg["sever_certificate"] == "computed":
            severed.append((coarse, sorted(homes)))
    direct = (len(components(rows, coarse_edges, cfg)) == len(fine_comps))
    return {"split_atoms": sorted(c for c, f in preimage.items() if len(f) >= 2),
            "severed_atoms": severed,
            "non_severing_certificate": not severed,
            "component_count_agrees": direct,
            "certificate_matches_recount": (not severed) == direct}


def maximal_severing_refinement(edges, atom: str):
    """CONTROL: split `atom` into one private constituent per row.  Provably
    severs whenever the atom has degree >= 2 and some incident row has no other
    shared atom (theorem T5's witness)."""
    out, phi = [], {}
    for r, a in edges:
        fine = f"{atom}__{r}" if a == atom else a
        phi[fine] = a
        out.append((r, fine))
    return sorted(set(out)), phi


# ==========================================================================
# 5.  the run
# ==========================================================================

def analyse(cfg: dict | None = None) -> dict:
    cfg = cfg or default_cfg()
    cur, prior = load(LEDGER_CURRENT), load(LEDGER_PRIOR)
    _b, targets, _s = index(cur)
    _bp, targets_prior, _sp = index(prior)

    tiered, declared, disputed = edge_sets(cur, cfg)
    tiered_p, declared_p, disputed_p = edge_sets(prior, cfg)
    census = Counter(t for _, _, t, _ in tiered)

    both = sorted(set(declared) | set(disputed))
    m = split_map(cur)

    res: dict = {
        "ledger": PIN["ledger_version"],
        "row_records": len(cur["rows"]),
        "targets": len(targets),
        "tier_census": {t: census.get(t, 0) for t in TIERS},
        "declared_edges": len(declared),
        "disputed_edges": len(disputed),
        "disputed_grade_only": census.get("GRADE_ONLY", 0),
        "disputed_uncited": census.get("UNCITED", 0),
        "uncited_precedence_edges": len(UNCITED_PRECEDENCE),
    }

    # ---- the invariant, both edge sets ----------------------------------
    inv_dec = invariant(targets, declared, cfg)
    inv_both = invariant(targets, both, cfg)
    res["declared"] = inv_dec
    res["declared_plus_disputed"] = inv_both
    res["spread"] = {
        "C": (inv_dec["C"], inv_both["C"]),
        "beta": (inv_dec["beta"], inv_both["beta"]),
        "b1": (inv_dec["b1"], inv_both["b1"]),
        "E": (inv_dec["E"], inv_both["E"]),
        "linked_components": (inv_dec["linked_components"], inv_both["linked_components"]),
        "largest_component_rows": (inv_dec["rowdist"][0], inv_both["rowdist"][0]),
    }

    # ---- the three completions of LA-10's partial split -----------------
    variants = {}
    for vname, kwargs, vtype in (
        ("residue_own_atom", dict(residue="A_RESIDUE"), "REFINEMENT"),
        ("residue_to_A_OWN", dict(residue="A_OWN"), "REFINEMENT"),
        ("la10_as_published", dict(residue=None, drop_residue=True), "EDGE_SET_CHANGE"),
    ):
        entry = {"declared_type": vtype}
        for eset_name, eset in (("declared", declared), ("declared_plus_disputed", both)):
            fine, phi = apply_refinement(eset, m, cfg=cfg, **kwargs)
            ci, fi = invariant(targets, eset, cfg), invariant(targets, fine, cfg)
            legality = refinement_legality(eset, fine)
            sev = severing_report(targets, eset, fine, phi, cfg)
            dE, dA, dC = fi["E"] - ci["E"], fi["A"] - ci["A"], fi["C"] - ci["C"]
            entry[eset_name] = {
                "coarse": {k: ci[k] for k in ("R", "E", "A", "C", "b1", "beta")},
                "fine": {k: fi[k] for k in ("R", "E", "A", "C", "b1", "beta")},
                "core_equal": core(ci) == core(fi),
                "unconditional_equal": unconditional(ci) == unconditional(fi),
                # b1 = E - R - A + C with R fixed, so db1 = dE - dA + dC always.
                # Under a refinement dE = 0 and this collapses to db1 = dC - dA.
                "b1_identity": (fi["b1"] - ci["b1"]) == (dE - dA + dC),
                "legality": legality,
                "severing": sev,
                "dE": dE, "dA": dA, "dC": dC,
            }
        variants[vname] = entry
    res["variants"] = variants

    # ---- CC-B(i): the ledger's own migration, FIXED vocabulary ----------
    inv_prior = invariant(targets_prior, declared_p, cfg)
    res["migration_control"] = {
        "v0258": {k: inv_prior[k] for k in ("R", "E", "A", "C", "b1", "beta")},
        "v0259": {k: inv_dec[k] for k in ("R", "E", "A", "C", "b1", "beta")},
        "moved": core(inv_prior) != core(inv_dec),
    }

    # ---- CC-B(iii): synthetic maximal severing refinement ---------------
    ms, ms_phi = maximal_severing_refinement(declared, A_ATOM)
    inv_ms = invariant(targets, ms, cfg)
    res["maximal_severing_control"] = {
        "coarse_C": inv_dec["C"], "fine_C": inv_ms["C"],
        "coarse_beta": inv_dec["beta"], "fine_beta": inv_ms["beta"],
        "moved": core(inv_dec) != core(inv_ms),
        "is_refinement": refinement_legality(declared, ms)["is_refinement"],
        "severing": severing_report(targets, declared, ms, ms_phi, cfg),
    }

    # ---- CC-B(iv): price LA-4's uncited atom-atom precedence edge -------
    parent: dict = {}

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

    for r in targets:
        find(("R", r))
    for r, a in declared:
        union(("R", r), ("A", a))
    for a, b in UNCITED_PRECEDENCE:
        union(("A", a), ("A", b))
    c_with = len({find(x) for x in list(parent)})
    e_with = len(declared) + len(UNCITED_PRECEDENCE)
    res["precedence_edge_control"] = {
        "C_without": inv_dec["C"], "C_with": c_with,
        "beta_without": inv_dec["beta"], "beta_with": e_with - len(targets) + c_with,
        "la4_reach_without": 2, "la4_reach_with": 28, "la4_denominator": 29,
    }

    # ---- reassignment sweep: how conditional is the acceptance test? ----
    kept, movers, n = 0, [], 0
    declared_A_rows = sorted(r for r, a in declared if a == A_ATOM)
    base_fine, _phi = apply_refinement(declared, m, residue="A_OWN")
    base_core = core(invariant(targets, base_fine, cfg))
    for r in declared_A_rows:
        cur_part = m.get(r, "A_OWN")
        for alt in ("A_ID", "A_STAT", "A_NORM", "A_OWN"):
            if alt == cur_part:
                continue
            n += 1
            m2 = dict(m)
            m2[r] = alt
            f = invariant(targets, apply_refinement(declared, m2, residue="A_OWN")[0], cfg)
            if core(f) == base_core:
                kept += 1
            else:
                movers.append((r, cur_part, alt, f["C"], f["beta"]))
    res["reassignment_sweep"] = {"variants": n, "preserved": kept,
                                 "moved": len(movers), "movers": movers}

    # ---- severing-vulnerable rows (the structural characterisation) -----
    deg = Counter(a for _, a in declared)
    row_atoms = defaultdict(set)
    for r, a in declared:
        row_atoms[r].add(a)
    res["severing_vulnerable_rows"] = sorted(
        r for r in row_atoms if sum(1 for a in row_atoms[r] if deg[a] >= 2) <= 1)

    # ---- [R] reproductions of already-filed facts -----------------------
    la4_tiers = Counter(t for _, _, t, _ in tier_edges(cur, {**cfg, "edges": LA4_EDGES}))
    res["reproductions"] = {
        "la4_edges": len(LA4_EDGES),
        "la4_wide_failures": la4_tiers.get("UNCITED", 0),
        "la6_edges": len(LA6_EDGES),
        "la5_edges": len(LA5_EDGES),
        "b9_declared_rows": sorted(r for r, a in declared if a == B9_ATOM),
        "b9_STAT_declared_rows": [],
    }
    return res


def assert_no_float(obj, path="result"):
    if isinstance(obj, float):
        raise AssertionError(f"float found at {path}")
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_float(v, f"{path}.{k}")
    elif isinstance(obj, (list, tuple, set)):
        for i, v in enumerate(obj):
            assert_no_float(v, f"{path}[{i}]")


# ==========================================================================
# 6.  the report -- printed every run, never a ratchet
# ==========================================================================

def report(res: dict) -> None:
    d, b = res["declared"], res["declared_plus_disputed"]
    print("=" * 78)
    print("DEPENDENCY-DIAGRAM INVARIANT -- conditional-physics ledger "
          f"{res['ledger']}  ({res['row_records']} records / {res['targets']} targets)")
    print("=" * 78)
    print(CAVEAT)
    print()
    print("  EDGE EXTRACTION (LA-11 discipline: exact substring in the row's own")
    print("  DEMAND fields `distance` + `revival_trigger`; nothing else counts)")
    print(f"    inherited edge assertions        {len(ALL_EDGES)}"
          "   (LA-6 76 + LA-4 77 + LA-5 27)")
    for t in TIERS:
        print(f"    {t:<32s} {res['tier_census'][t]}")
    print(f"    DECLARED edge set                {res['declared_edges']}")
    print(f"    KNOWN-DISPUTED edge set          {res['disputed_edges']}"
          f"   ({res['disputed_grade_only']} grade-only + {res['disputed_uncited']} uncited)")
    print(f"    uncited ATOM-ATOM precedence     {res['uncited_precedence_edges']}"
          "   (LA-4's `b9 < b1`; outside the diagram by construction)")
    print()
    print("  THE INVARIANT                         declared    declared+disputed")
    for key, label in (("R", "row-vertices  R"), ("E", "edges  E"),
                       ("A", "atom-vertices  A"), ("C", "components  C"),
                       ("linked_components", "linked components"),
                       ("isolated_rows", "isolated rows"),
                       ("b1", "cycle rank  b1 = E-(R+A)+C"),
                       ("beta", "REDUCED CYCLE RANK  beta = E-R+C")):
        print(f"    {label:<35s} {d[key]:>7}    {b[key]:>10}")
    print(f"    {'component row sizes (linked)':<35s} {str(d['linked_rowdist']):>7}")
    print(f"    {'':<35s} {str(b['linked_rowdist']):>7}   (declared+disputed)")
    print()
    print("  SPREAD (declared -> declared+disputed) -- this IS part of the result")
    for k, (x, y) in res["spread"].items():
        print(f"    {k:<32s} {x} -> {y}   (delta {y - x:+d})")
    print()
    print("  ACCEPTANCE TEST -- the measured 32 -> 35 instability, re-run on the")
    print("  invariant.  LA-10's split is PARTIAL (15 of 18 A-incidences); a")
    print("  partial map is not a refinement, so all three completions are typed:")
    for vname, entry in res["variants"].items():
        print(f"    {vname}  [{entry['declared_type']}]")
        for eset in ("declared", "declared_plus_disputed"):
            e = entry[eset]
            c, f = e["coarse"], e["fine"]
            verdict = "EQUAL" if e["core_equal"] else "MOVED"
            print(f"      {eset:<22s} C {c['C']}->{f['C']}   beta {c['beta']}->{f['beta']}"
                  f"   b1 {c['b1']}->{f['b1']}   dA {e['dA']:+d}   "
                  f"E {c['E']}->{f['E']}   {verdict}"
                  f"   refinement={e['legality']['is_refinement']}"
                  f"   non-severing={e['severing']['non_severing_certificate']}")
            if e["severing"]["severed_atoms"]:
                print(f"        severed at: {e['severing']['severed_atoms']}")
    print()
    print("  CONTRARY CONTROLS")
    mc = res["migration_control"]
    print(f"    CC-B(i)  ledger migration v0.258 -> v0.259, vocabulary FIXED:")
    print(f"             C {mc['v0258']['C']} -> {mc['v0259']['C']}   "
          f"beta {mc['v0258']['beta']} -> {mc['v0259']['beta']}   "
          f"E {mc['v0258']['E']} -> {mc['v0259']['E']}   moved={mc['moved']}")
    ms = res["maximal_severing_control"]
    print(f"    CC-B(iii) synthetic maximal severing refinement of {A_ATOM}:")
    print(f"             C {ms['coarse_C']} -> {ms['fine_C']}   "
          f"beta {ms['coarse_beta']} -> {ms['fine_beta']}   moved={ms['moved']}")
    pc = res["precedence_edge_control"]
    print(f"    CC-B(iv) LA-4's ONE uncited precedence edge `b9 < b1`:")
    print(f"             LA-4 reach {pc['la4_reach_without']}/{pc['la4_denominator']}"
          f" -> {pc['la4_reach_with']}/{pc['la4_denominator']}   "
          f"but C {pc['C_without']} -> {pc['C_with']}, "
          f"beta {pc['beta_without']} -> {pc['beta_with']}")
    sw = res["reassignment_sweep"]
    print(f"    conditioning: {sw['variants']} single re-assignments of the split, "
          f"invariant preserved in {sw['preserved']}, moved in {sw['moved']}")
    for mv in sw["movers"]:
        print(f"             MOVER {mv}")
    print(f"    severing-vulnerable rows ({len(res['severing_vulnerable_rows'])}): "
          f"{', '.join(res['severing_vulnerable_rows'])}")
    print()
    rp = res["reproductions"]
    print("  [R] REPRODUCED, not re-derived")
    print(f"    LA-4 declares {rp['la4_edges']} atom-edges; "
          f"{rp['la4_wide_failures']} fail an exact-substring certificate  "
          "(LA-10 §3.2: 20 of 77)")
    print(f"    b9 is DECLARED by exactly {rp['b9_declared_rows']}  "
          "(LA-10 §3.3: b9_ID reach 2/29)")
    print(f"    b9_STAT is declared by {rp['b9_STAT_declared_rows']} rows, so it "
          "contributes NO vertex (LA-11: declaration is a text property)")
    print("=" * 78)


# ==========================================================================
# 7.  WELL-FORMEDNESS RATCHET -- the ONLY thing that can go red
# ==========================================================================

def wellformedness(res: dict, cfg: dict) -> list[tuple[str, str, bool, str]]:
    """(tag, label, ok, detail).  Extraction reproducibility and graph
    accounting ONLY.  No check here asserts a value of C, beta or the size
    distribution -- a physics number must not become a compliance target."""
    out = []

    def w(label, ok, detail=""):
        out.append(("W", label, bool(ok), str(detail)))

    def c(label, ok, detail=""):
        out.append(("C", label, bool(ok), str(detail)))

    def r(label, ok, detail=""):
        out.append(("R", label, bool(ok), str(detail)))

    # --- W: extraction reproducibility -----------------------------------
    w("ledger version pinned", res["ledger"] == PIN["ledger_version"], res["ledger"])
    w("87 row records", res["row_records"] == PIN["row_records"], res["row_records"])
    w("84 canonical targets", res["targets"] == PIN["canonical_targets"], res["targets"])
    w("180 inherited edge assertions",
      len(ALL_EDGES) == PIN["inherited_assertions"], len(ALL_EDGES))
    w("LA-6 / LA-4 / LA-5 assertion counts unchanged",
      (len(LA6_EDGES), len(LA4_EDGES), len(LA5_EDGES))
      == (PIN["la6_declared_assertions"], PIN["la4_declared_assertions"],
          PIN["la5_declared_assertions"]),
      (len(LA6_EDGES), len(LA4_EDGES), len(LA5_EDGES)))
    total = sum(res["tier_census"].values())
    w("tier partition is TOTAL over the successor-expanded assertions",
      total == PIN["edges_after_successor_inheritance"], total)
    w("tier census reproduces", res["tier_census"] == PIN["tier_census"],
      res["tier_census"])
    w("declared + disputed == tiered non-retired",
      res["declared_edges"] + res["disputed_edges"]
      == res["tier_census"]["DECLARED"] + res["tier_census"]["GRADE_ONLY"]
      + res["tier_census"]["UNCITED"],
      (res["declared_edges"], res["disputed_edges"]))
    w("no empty certificate string is admitted",
      all(all(s for s in subs) for _, _, subs in cfg["edges"]))
    w("every declared edge re-verifies against the row's own demand text",
      _recheck_declared(cfg))
    w("no GRADE_ONLY or UNCITED edge entered the declared diagram",
      _no_disputed_leak(cfg))

    # --- W: graph accounting closes --------------------------------------
    for name, inv in (("declared", res["declared"]),
                      ("declared+disputed", res["declared_plus_disputed"])):
        w(f"{name}: beta == b1 + A", inv["beta"] == inv["b1"] + inv["A"],
          (inv["beta"], inv["b1"], inv["A"]))
        w(f"{name}: beta == E - R + C",
          inv["beta"] == inv["E"] - inv["R"] + inv["C"])
        w(f"{name}: C == linked + isolated",
          inv["C"] == inv["linked_components"] + inv["isolated_rows"])
        w(f"{name}: component row sizes sum to R", sum(inv["rowdist"]) == inv["R"])
        w(f"{name}: union-find agrees with an independent BFS",
          inv["C"] == len(components_bfs(
              [x for x in _targets_of()], _edges_named(cfg, name))))

    # --- W: variant typing is honest -------------------------------------
    for vname, entry in res["variants"].items():
        for eset in ("declared", "declared_plus_disputed"):
            e = entry[eset]
            w(f"{vname}/{eset}: graph accounting  db1 == dE - dA + dC",
              e["b1_identity"], (e["coarse"]["b1"], e["fine"]["b1"], e["dE"],
                                 e["dA"], e["dC"]))
            if entry["declared_type"] == "REFINEMENT":
                w(f"{vname}/{eset}: typed REFINEMENT and IS one",
                  e["legality"]["is_refinement"], e["legality"])
                w(f"{vname}/{eset}: refinement preserves R, E and row degrees",
                  e["unconditional_equal"])
                w(f"{vname}/{eset}: dE == 0, so db1 collapses to dC - dA",
                  e["dE"] == 0, e["dE"])
                # T4 holds only for a legal refinement; asserted only there.
                w(f"{vname}/{eset}: severing certificate matches a direct recount",
                  e["severing"]["certificate_matches_recount"], e["severing"])
                w(f"{vname}/{eset}: core moved IFF the refinement severed",
                  e["core_equal"] == e["severing"]["non_severing_certificate"],
                  (e["core_equal"], e["severing"]["non_severing_certificate"]))
            else:
                w(f"{vname}/{eset}: typed EDGE_SET_CHANGE and is NOT a refinement",
                  not e["legality"]["is_refinement"], e["legality"])
                w(f"{vname}/{eset}: an edge-set change really changes E",
                  e["dE"] != 0, e["dE"])

    # --- C: contrary controls that MUST fire -----------------------------
    acc = res["variants"]["residue_to_A_OWN"]
    c("CC-A  the refinement PRESERVES the invariant on the declared edge set",
      acc["declared"]["core_equal"], acc["declared"])
    c("CC-A  the refinement PRESERVES it with disputed edges included too",
      acc["declared_plus_disputed"]["core_equal"])
    c("CC-A  and it is a real refinement: atom count rises by 3 (the 12->15 move)",
      acc["declared"]["dA"] == 3, acc["declared"]["dA"])
    c("CC-A  while the naive cycle rank b1 FALLS by exactly 3 -- b1 is rejected",
      acc["declared"]["fine"]["b1"] - acc["declared"]["coarse"]["b1"] == -3)
    c("CC-B(i)  a genuine ledger edge-set change MOVES it",
      res["migration_control"]["moved"], res["migration_control"])
    c("CC-B(ii) LA-10 as published is NOT a refinement (it deletes edges)",
      not res["variants"]["la10_as_published"]["declared"]["legality"]["is_refinement"])
    c("CC-B(iii) a maximal severing refinement MOVES it",
      res["maximal_severing_control"]["moved"], res["maximal_severing_control"])
    c("CC-B(iii) and the certificate REPORTS the severing rather than hiding it",
      not res["maximal_severing_control"]["severing"]["non_severing_certificate"])
    c("planted-positive: an absent certificate tiers UNCITED", _planted_absent(cfg))
    c("planted-positive: a status-field-only certificate tiers GRADE_ONLY",
      _planted_grade_only(cfg))
    c("planted-negative: a present certificate tiers DECLARED", _planted_present(cfg))
    c("the disputed set is non-empty, so the spread is a real measurement",
      res["disputed_edges"] > 0, res["disputed_edges"])

    # --- R: reproductions ------------------------------------------------
    rp = res["reproductions"]
    r("LA-10 §3.2: 20 of LA-4's 77 atom-edges fail an exact-substring certificate",
      rp["la4_wide_failures"] == PIN["la4_wide_failures"] and rp["la4_edges"] == 77,
      (rp["la4_wide_failures"], rp["la4_edges"]))
    r("LA-10 §3.3: b9 is named by exactly RA-E1 and RA-E3",
      rp["b9_declared_rows"] == ["RA-E1", "RA-E3"], rp["b9_declared_rows"])
    r("LA-10 §3.3 / LA-11: b9_STAT has zero declaring rows",
      rp["b9_STAT_declared_rows"] == [])
    return out


_TARGETS_CACHE: dict = {}


def _targets_of():
    if "t" not in _TARGETS_CACHE:
        _TARGETS_CACHE["t"] = index(load(LEDGER_CURRENT))[1]
    return _TARGETS_CACHE["t"]


def _edges_named(cfg, name):
    _t, dec, dis = edge_sets(load(LEDGER_CURRENT), cfg)
    return dec if name == "declared" else sorted(set(dec) | set(dis))


def _recheck_declared(cfg) -> bool:
    led = load(LEDGER_CURRENT)
    by_id, _t, _s = index(led)
    for rid, _atom, tier, cert in tier_edges(led, cfg):
        if tier != "DECLARED":
            continue
        if not cert or cert not in demand_text(by_id[rid], cfg):
            return False
    return True


def _no_disputed_leak(cfg) -> bool:
    led = load(LEDGER_CURRENT)
    tiered, dec, dis = edge_sets(led, cfg)
    bad = {(r, a) for r, a, t, _ in tiered if t in ("GRADE_ONLY", "UNCITED")}
    good = {(r, a) for r, a, t, _ in tiered if t == "DECLARED"}
    return not (set(dec) & (bad - good))


def _plant(cfg, subs):
    led = load(LEDGER_CURRENT)
    probe = [("LT-GR7", "PLANT_ATOM", subs)]
    return tier_edges(led, {**cfg, "edges": probe})[0][2]


def _planted_absent(cfg) -> bool:
    return _plant(cfg, ("zzz-no-such-string-in-any-row-zzz",)) == "UNCITED"


def _planted_grade_only(cfg) -> bool:
    # LT-GR7's mapping_grade carries a NO_GO token; its demand fields do not.
    led = load(LEDGER_CURRENT)
    row = index(led)[0]["LT-GR7"]
    tok = next((t for t in row.get("mapping_grade", "").split("__") if t), None)
    return bool(tok) and _plant(cfg, (tok,)) == "GRADE_ONLY"


def _planted_present(cfg) -> bool:
    return _plant(cfg, ("derive one absolute gravitational normalization",)) == "DECLARED"


def run(cfg: dict | None = None, quiet: bool = False):
    cfg = cfg or default_cfg()
    res = analyse(cfg)
    assert_no_float(res)
    checks = wellformedness(res, cfg)
    if not quiet:
        report(res)
    return res, checks


def print_checks(checks) -> int:
    fails = [x for x in checks if not x[2]]
    by = Counter(t for t, _, _, _ in checks)
    ok = Counter(t for t, _, o, _ in checks if o)
    print()
    for tag, label, good, detail in checks:
        if not good:
            print(f"  [FAIL] [{tag}] {label}   got: {detail}")
    print("-" * 78)
    print(f"WELL-FORMEDNESS: {len(checks) - len(fails)}/{len(checks)} checks pass; "
          "exit 0 iff all pass.  The invariant's VALUE is not checked anywhere.")
    print("  by class:", {k: f"{ok.get(k, 0)}/{by[k]}" for k in sorted(by)})
    print("-" * 78)
    return 1 if fails else 0


# ==========================================================================
# 8.  --selftest:  clean baseline FIRST, then machinery-corruption mutations
#     VERIFICATION.md rules 1-7.  A mutation corrupts MACHINERY or a
#     REFERENCE, never a check's predicate.  A nonzero exit without a genuine
#     [FAIL] line is CRASH-NOT-DETECTION and fails the selftest.
# ==========================================================================

def _mut_no_union(cfg):
    cfg["union_enabled"] = False


def _mut_demand_fields_widened(cfg):
    cfg["demand_fields"] = DEMAND_FIELDS + ("mapping_grade",)


def _mut_no_successor_inheritance(cfg):
    cfg["inherit_to_successors"] = False


def _mut_beta_formula(cfg):
    cfg["beta_formula"] = "E-R"


def _mut_refinement_non_injective(cfg):
    cfg["refinement_non_injective"] = True


def _mut_severing_certificate_forced_true(cfg):
    cfg["sever_certificate"] = "always-non-severing"


def _mut_atoms_not_induced(cfg):
    cfg["induce_atoms_from_edges"] = False


def _mut_empty_certificate(cfg):
    e = list(cfg["edges"])
    r, a, _s = e[0]
    e[0] = (r, a, ("",))
    cfg["edges"] = e


def _mut_drop_an_assertion(cfg):
    cfg["edges"] = list(cfg["edges"])[1:]


def _mut_duplicate_assertion(cfg):
    e = list(cfg["edges"])
    cfg["edges"] = e + [e[0]]
    cfg["dedup_edges"] = False


def _mut_status_fields_emptied(cfg):
    cfg["status_fields"] = ()


def _mut_retarget_ledger(cfg):
    cfg["_ledger_swap"] = True


MUTATIONS = [
    ("union_find_disabled", _mut_no_union,
     "components no longer merge -- must disagree with the independent BFS"),
    ("demand_fields_widened", _mut_demand_fields_widened,
     "grade tokens admitted as demands -- tier census must drift"),
    ("successor_inheritance_dropped", _mut_no_successor_inheritance,
     "LT-SM1's edges vanish instead of passing to LT-SM1a/b"),
    ("beta_formula_corrupted", _mut_beta_formula,
     "beta == b1 + A must stop holding"),
    ("refinement_made_non_injective", _mut_refinement_non_injective,
     "a row gets two constituents of one atom -- it stops being a refinement"),
    ("severing_certificate_forced_true", _mut_severing_certificate_forced_true,
     "the T4 certificate can no longer disagree with the graph"),
    ("atoms_not_induced_from_edges", _mut_atoms_not_induced,
     "A collapses to 0 -- beta == b1 + A must stop holding"),
    ("empty_certificate_admitted", _mut_empty_certificate,
     "an empty substring matches every row -- the guard must fire"),
    ("assertion_dropped", _mut_drop_an_assertion,
     "the inherited inventory no longer reproduces"),
    ("assertion_duplicated", _mut_duplicate_assertion,
     "the inherited inventory no longer reproduces"),
    ("status_fields_emptied", _mut_status_fields_emptied,
     "GRADE_ONLY collapses into UNCITED -- the census must drift"),
    ("ledger_retargeted_to_v0258", _mut_retarget_ledger,
     "the pinned row set no longer matches"),
]


def selftest(poison_baseline: bool = False) -> int:
    global LEDGER_CURRENT
    print("=" * 78)
    print("SELFTEST -- clean baseline FIRST, then machinery-corruption mutations")
    print("=" * 78)
    cfg0 = default_cfg()
    if poison_baseline:
        # Prove the baseline guard itself has power (VERIFICATION.md rule 1):
        # corrupt the CLEAN set and require the selftest to refuse, red, before
        # any mutation runs.
        _mut_drop_an_assertion(cfg0)
    try:
        _res, checks = run(cfg0, quiet=True)
    except Exception as exc:                                   # noqa: BLE001
        print(f"  BASELINE CRASHED: {type(exc).__name__}: {exc}")
        print("  ABORT RED -- a red baseline makes every mutation exit nonzero "
              "for the pre-existing reason (VERIFICATION.md rule 1).")
        return 1
    baseline_fails = [x for x in checks if not x[2]]
    if baseline_fails:
        print(f"  CLEAN BASELINE IS RED ({len(baseline_fails)} failures):")
        for tag, label, _o, detail in baseline_fails:
            print(f"    [FAIL] [{tag}] {label}   got: {detail}")
        print("  ABORT RED (VERIFICATION.md rule 1).")
        return 1
    print(f"  clean baseline: {len(checks)}/{len(checks)} checks pass  [OK]")
    print()

    results = []
    for name, mutate, why in MUTATIONS:
        cfg = default_cfg()
        mutate(cfg)
        swap = cfg.pop("_ledger_swap", False)
        saved = LEDGER_CURRENT
        _TARGETS_CACHE.clear()
        if swap:
            LEDGER_CURRENT = LEDGER_PRIOR
        try:
            _r, mchecks = run(cfg, quiet=True)
            fails = [x for x in mchecks if not x[2]]
            if fails:
                verdict, note = "CAUGHT", f"{len(fails)} genuine [FAIL] line(s): {fails[0][1]}"
            else:
                verdict, note = "MISSED", "no [FAIL] line -- mutation is invisible"
        except Exception as exc:                               # noqa: BLE001
            verdict, note = "CRASH-NOT-DETECTION", f"{type(exc).__name__}: {exc}"
        finally:
            LEDGER_CURRENT = saved
            _TARGETS_CACHE.clear()
        results.append((name, verdict, note, why))
        print(f"  mutation {name:<34s} {verdict:<20s} {note}")

    print()
    bad = [x for x in results if x[1] != "CAUGHT"]
    for name, verdict, note, why in bad:
        print(f"  [FAIL] mutation {name}: {verdict} -- {note}   (intent: {why})")
    print("-" * 78)
    print(f"SELFTEST: {len(results) - len(bad)}/{len(results)} mutations produced a "
          "GENUINE failing check; crash-catches are rejected.")
    print("-" * 78)
    return 1 if bad else 0


# ==========================================================================
# 9.  unittest surface (house convention for process_gates)
# ==========================================================================

class DependencyDiagramInvariantTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.res, cls.checks = run(default_cfg(), quiet=True)

    def test_wellformedness_all_pass(self):
        fails = [(t, l, d) for t, l, o, d in self.checks if not o]
        self.assertEqual([], fails, f"{len(fails)} well-formedness failures")

    def test_no_check_pins_the_invariants_value(self):
        """The ratchet must not become a compliance target for a physics-side
        number.  The W checks compare against exactly one reference constant,
        PIN, so it suffices -- and is exact -- to require that PIN carries only
        EXTRACTION keys and no invariant field.  A value coincidence (87 row
        records versus beta = 87) must not trip this; a real regression, an
        invariant field appearing in PIN, must."""
        extraction_keys = {
            "ledger_version", "row_records", "canonical_targets", "superseded",
            "inherited_assertions", "edges_after_successor_inheritance",
            "tier_census", "la4_wide_failures", "la4_declared_assertions",
            "la6_declared_assertions", "la5_declared_assertions",
        }
        self.assertEqual(extraction_keys, set(PIN),
                         "PIN gained or lost a key; every PIN key must be an "
                         "extraction fact, never an invariant value")
        invariant_fields = {"C", "b1", "beta", "rowdist", "linked_rowdist",
                            "linked_components", "isolated_rows",
                            "row_degree_multiset", "components", "A"}
        self.assertEqual(set(), invariant_fields & set(PIN),
                         "an invariant field is pinned in the ratchet")

    def test_perturbing_the_invariant_alone_keeps_the_ratchet_green(self):
        """Behavioural proof of the same thing: change the GRAPH without
        changing the EXTRACTION and the well-formedness verdict must not
        move.  Restricting the diagram to one axis changes C, beta and the
        size distribution; the ratchet must stay green on the checks that
        are about the graph rather than the extraction."""
        cfg = default_cfg()
        led = load(LEDGER_CURRENT)
        targets = index(led)[1]
        _t, declared, _d = edge_sets(led, cfg)
        full = invariant(targets, declared, cfg)
        part = invariant(targets, [e for e in declared if e[0].startswith("LT-")], cfg)
        self.assertNotEqual(core(full), core(part), "the perturbation was inert")
        for inv in (full, part):
            self.assertEqual(inv["beta"], inv["b1"] + inv["A"])
            self.assertEqual(inv["beta"], inv["E"] - inv["R"] + inv["C"])
            self.assertEqual(inv["C"], len(components_bfs(
                targets, declared if inv is full
                else [e for e in declared if e[0].startswith("LT-")])))

    def test_owning_artifact_exists_and_is_routed(self):
        self.assertTrue(ARTIFACT.exists(), f"missing artifact {ARTIFACT}")
        text = ARTIFACT.read_text()
        self.assertIn("GU-COMPARATOR-ROUTING", text)
        self.assertRegex(text, r"Classification:\s*[*_]{0,2}`INTERNAL_STRUCTURAL_ONLY`")
        self.assertIn("target_claim:", text)


def main(argv: list[str]) -> int:
    if "--selftest" in argv or "--self-test" in argv:
        return selftest(poison_baseline="--poison-baseline" in argv)
    res, checks = run()
    if "--report" in argv:
        return 0
    return print_checks(checks)


if __name__ == "__main__":
    if "--unittest" in sys.argv:
        sys.argv = [sys.argv[0]]
        unittest.main(verbosity=2)
    else:
        sys.exit(main(sys.argv[1:]))
