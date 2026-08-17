#!/usr/bin/env python3
"""CT-4 -- the dependency-diagram invariant, and what it is NOT.

GU-COMPARATOR-ROUTING: this probe's object is the LEDGER, not the physics.
Every number is a property of a declared vocabulary over v0.259 prose.
Classification: INTERNAL_STRUCTURAL_ONLY.  Nothing here is evidence for or
against Weinstein's source-native mechanism and nothing here binds any
conventional comparator.

QUESTION.  The ledger's "degrees of freedom" count moved 82 -> 32 -> 35 because
a generator count is a property of a PRESENTATION.  Is there a number computed
from the same dependency structures that does NOT move under vocabulary
refinement -- and does it earn the word "invariant", or does it just relocate
the lexicon-dependence into the edge extraction?

ANSWER, in three parts, all certified below.

  (1) A NO-GO.  For any incidence diagram with an atom of degree >= 2 there
      EXISTS a refinement that strictly increases the component count (split
      that atom's incidences into singletons).  So NO connectivity statistic of
      a declared diagram is UNCONDITIONALLY refinement-invariant.  The
      unconditional refinement-invariants are exactly the row-side data
      (R, E, row-degree multiset), and those measure how much text there is,
      not how entangled it is.  This RETIRES the internal target claim below.

  (2) A CONDITIONAL invariant that does survive the measured instability:
      C (components), beta = E - R + C (the REDUCED cycle rank: incidences in
      excess of a row-spanning forest), and the component row-size
      distribution -- invariant under any refinement carrying a decidable
      NON-SEVERING certificate, which this probe computes and ships with the
      number.  The naive cycle rank b1 is REJECTED: b1 falls by exactly the
      number of new atoms under a non-severing refinement (identity T3), so b1
      is as presentation-dependent as the generator count it would replace.

  (3) The honest caveat, quantified.  Refinement-stability buys much less than
      edge-set stability costs.  On v0.259 the whole 32 -> 35 vocabulary
      instability is worth 0 in (C, beta, rowdist), while the declared-versus-
      disputed edge spread is 11 components and 35 in beta.  The invariant
      answers "how entangled is what the rows SAY", never "which edges are
      real".

REPRODUCE
    cd /path/to/gu-formalization
    _local/cas-venv/bin/python tests/channel-swings/joe_directed_ct4_dependency_diagram_invariant.py
    ... --selftest      (failure path: mutations must each drive a [FAIL])

Exact integer arithmetic; no float is constructed anywhere.  The engine, the
edge tables and the extraction rule live in
process_gates/dependency_diagram_invariant_audit.py and are imported, not
copied, so this probe and the gate cannot drift apart.

NOT: a ledger edit, a verdict change, a reason-kind change, a physics
derivation, a coefficient, a selection principle, a claim-status movement, a
count of independent problems, or any statement that a GU object exists.
"""

from __future__ import annotations

import importlib.util
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
_spec = importlib.util.spec_from_file_location(
    "ddia", ROOT / "process_gates" / "dependency_diagram_invariant_audit.py")
G = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(G)

CHECKS: list[tuple[str, str, bool, str]] = []


def check(tag: str, label: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((tag, label, bool(ok), str(detail)))
    return bool(ok)


def run_probe(cfg: dict | None = None) -> dict:
    CHECKS.clear()
    cfg = cfg or G.default_cfg()
    res = G.analyse(cfg)
    G.assert_no_float(res)
    targets = G.index(G.load(G.LEDGER_CURRENT))[1]
    _t, declared, disputed = G.edge_sets(G.load(G.LEDGER_CURRENT), cfg)
    both = sorted(set(declared) | set(disputed))
    d, b = res["declared"], res["declared_plus_disputed"]

    # =====================================================================
    # [R] -- reproduce every banked number BEFORE extending it
    # =====================================================================
    check("R", "v0.259 declares 87 row records and 84 canonical targets",
          res["row_records"] == 87 and res["targets"] == 84,
          (res["row_records"], res["targets"]))
    check("R", "LA-6 declares 76 LAGRANGIAN atom-edges", len(G.LA6_EDGES) == 76)
    check("R", "LA-4 declares 77 REPRESENTATION atom-edges", len(G.LA4_EDGES) == 77)
    check("R", "LA-5 declares 27 ANOMALY atom-edges", len(G.LA5_EDGES) == 27)
    check("R", "LA-10 sec 3.2: 20 of LA-4's 77 atom-edges fail an exact-substring "
          "certificate", res["reproductions"]["la4_wide_failures"] == 20,
          res["reproductions"]["la4_wide_failures"])
    check("R", "LA-10 sec 3.3: b9 (the operative second action) is named by exactly "
          "RA-E1 and RA-E3", res["reproductions"]["b9_declared_rows"] == ["RA-E1", "RA-E3"],
          res["reproductions"]["b9_declared_rows"])
    check("R", "LA-10's A-split assigns 15 of A's 18 v0.258 incidences (PARTIAL)",
          len(G.LA10_SPLIT) == 15, len(G.LA10_SPLIT))
    check("R", "LA-10's four constituents are A_ID / A_STAT / A_NORM / A_OWN",
          sorted(set(G.LA10_SPLIT.values())) == ["A_ID", "A_NORM", "A_OWN", "A_STAT"])
    check("R", "LA-11's demand-field rule is ('distance', 'revival_trigger')",
          G.DEMAND_FIELDS == ("distance", "revival_trigger"), str(G.DEMAND_FIELDS))
    check("R", "LA-4's b9 < b1 precedence edge is the one edge no row states",
          G.UNCITED_PRECEDENCE == (("b9_OPERATIVE_SECOND_ACTION",
                                    "b1_ACTION_STATIONARY_VACUUM"),))

    # =====================================================================
    # [E] -- the extraction, and the diagram
    # =====================================================================
    check("E", "180 inherited edge assertions, 182 after successor inheritance",
          len(G.ALL_EDGES) == 180 and sum(res["tier_census"].values()) == 182,
          (len(G.ALL_EDGES), sum(res["tier_census"].values())))
    check("E", "tier partition is total and disjoint",
          sum(res["tier_census"].values())
          == res["declared_edges"] + res["disputed_edges"]
          + res["tier_census"]["ROW_RETIRED"] + res["tier_census"]["ROW_ABSENT"])
    check("E", "DECLARED edge set is 136", res["declared_edges"] == 136,
          res["declared_edges"])
    check("E", "KNOWN-DISPUTED edge set is 46 = 20 grade-only + 26 uncited",
          (res["disputed_edges"], res["disputed_grade_only"], res["disputed_uncited"])
          == (46, 20, 26),
          (res["disputed_edges"], res["disputed_grade_only"], res["disputed_uncited"]))
    check("E", "the declared diagram has 84 row-vertices, 35 atom-vertices, 136 edges",
          (d["R"], d["A"], d["E"]) == (84, 35, 136), (d["R"], d["A"], d["E"]))
    check("E", "C = 35 = 7 linked components + 28 isolated rows",
          (d["C"], d["linked_components"], d["isolated_rows"]) == (35, 7, 28),
          (d["C"], d["linked_components"], d["isolated_rows"]))
    check("E", "linked component row sizes are (24, 19, 6, 4, 1, 1, 1)",
          d["linked_rowdist"] == (24, 19, 6, 4, 1, 1, 1), str(d["linked_rowdist"]))
    check("E", "beta = E - R + C = 87 and b1 = 52, with beta = b1 + A",
          (d["beta"], d["b1"]) == (87, 52) and d["beta"] == d["b1"] + d["A"],
          (d["beta"], d["b1"], d["A"]))
    check("E", "no declared edge crosses an axis: the three published lexicons never "
          "touch", all(len({x.split('-')[0] for x in c[0]}) == 1
                       for c in d["components"] if c[1]),
          str([sorted({x.split('-')[0] for x in c[0]}) for c in d["components"] if c[1]]))

    # =====================================================================
    # [E] -- THE ACCEPTANCE TEST: the measured 32 -> 35 instability, re-run
    # =====================================================================
    acc = res["variants"]["residue_to_A_OWN"]["declared"]
    check("E", "ACCEPTANCE: the refinement raises the atom count by 3, mirroring "
          "LA-10's rank 12 -> 15 and the ledger-wide 32 -> 35",
          acc["dA"] == 3, acc["dA"])
    check("E", "ACCEPTANCE: C is EQUAL under both vocabularies",
          acc["coarse"]["C"] == acc["fine"]["C"] == 35,
          (acc["coarse"]["C"], acc["fine"]["C"]))
    check("E", "ACCEPTANCE: beta is EQUAL under both vocabularies",
          acc["coarse"]["beta"] == acc["fine"]["beta"] == 87,
          (acc["coarse"]["beta"], acc["fine"]["beta"]))
    check("E", "ACCEPTANCE: the component row-size distribution is EQUAL",
          acc["core_equal"])
    check("E", "ACCEPTANCE: R, E and the row-degree multiset are EQUAL "
          "(unconditional, theorem T1)", acc["unconditional_equal"])
    check("E", "ACCEPTANCE holds with the disputed edges included too",
          res["variants"]["residue_to_A_OWN"]["declared_plus_disputed"]["core_equal"])
    check("E", "the naive cycle rank b1 FALLS by exactly 3 -- it is as "
          "presentation-dependent as the generator count",
          acc["fine"]["b1"] - acc["coarse"]["b1"] == -3,
          (acc["coarse"]["b1"], acc["fine"]["b1"]))
    check("E", "identity T3: db1 = dE - dA + dC, verified on every variant",
          all(v[e]["b1_identity"] for v in res["variants"].values()
              for e in ("declared", "declared_plus_disputed")))
    check("E", "the refinement carries a NON-SEVERING certificate, and it is what "
          "licenses the equality",
          acc["severing"]["non_severing_certificate"]
          and acc["severing"]["certificate_matches_recount"], str(acc["severing"]))

    # =====================================================================
    # [C] -- CONTRARY CONTROL A: a refinement that PRESERVES the invariant
    # =====================================================================
    sw = res["reassignment_sweep"]
    check("C", "CONTRARY-A: 42 single re-assignments of the split were swept",
          sw["variants"] == 42, sw["variants"])
    check("C", "CONTRARY-A: the invariant is preserved in 39 of 42 re-assignments, "
          "so the equality is not an artifact of one typing",
          (sw["preserved"], sw["moved"]) == (39, 3), (sw["preserved"], sw["moved"]))
    check("C", "CONTRARY-A: all three movers are the same row leaving A_ID "
          "(LT-SM6), which strands LT-SM1a on a degree-1 atom",
          sorted({m[0] for m in sw["movers"]}) == ["LT-SM6"],
          str(sw["movers"]))

    # =====================================================================
    # [C] -- CONTRARY CONTROL B: genuine edge-set changes that MOVE it
    # =====================================================================
    mc = res["migration_control"]
    check("C", "CONTRARY-B(i): the ledger's own v0.258 -> v0.259 migration, under a "
          "FIXED vocabulary, MOVES the invariant",
          mc["moved"] and (mc["v0258"]["C"], mc["v0259"]["C"]) == (31, 35),
          (mc["v0258"], mc["v0259"]))
    pub = res["variants"]["la10_as_published"]["declared"]
    check("C", "CONTRARY-B(ii): LA-10 as published is NOT a refinement -- it deletes "
          "a declared incidence (E 136 -> 135)",
          (not pub["legality"]["is_refinement"]) and pub["dE"] == -1,
          (pub["legality"], pub["dE"]))
    check("C", "CONTRARY-B(ii): and that deletion MOVES C by +1, so the machinery "
          "separates refinement from edge dispute",
          pub["dC"] == 1 and not pub["core_equal"], (pub["dC"], pub["core_equal"]))
    ms = res["maximal_severing_control"]
    check("C", "CONTRARY-B(iii): a maximal severing refinement is a LEGAL refinement "
          "that still MOVES C -- theorem T5's witness",
          ms["is_refinement"] and ms["moved"] and ms["fine_C"] > ms["coarse_C"],
          (ms["coarse_C"], ms["fine_C"], ms["is_refinement"]))
    check("C", "CONTRARY-B(iii): and the certificate REPORTS the severing rather "
          "than hiding it",
          not ms["severing"]["non_severing_certificate"])
    sev = res["variants"]["residue_own_atom"]["declared"]
    check("C", "CONTRARY-B(iv): the OTHER legal completion of LA-10's partial map "
          "severs, and the certificate names the atom",
          (not sev["core_equal"]) and sev["severing"]["severed_atoms"],
          str(sev["severing"]["severed_atoms"]))
    pc = res["precedence_edge_control"]
    check("C", "CONTRARY-B(v): LA-4's ONE uncited precedence edge swings its reach "
          "statistic 2/29 -> 28/29 but moves beta by exactly 1 in 87 and C by 0",
          (pc["la4_reach_without"], pc["la4_reach_with"]) == (2, 28)
          and pc["C_with"] - pc["C_without"] == 0
          and pc["beta_with"] - pc["beta_without"] == 1,
          (pc["C_without"], pc["C_with"], pc["beta_without"], pc["beta_with"]))

    # =====================================================================
    # [C] -- planted controls: the extractor must have power
    # =====================================================================
    check("C", "planted-positive: a certificate absent from every field tiers "
          "UNCITED", G._planted_absent(cfg))
    check("C", "planted-positive: a certificate present only in mapping_grade tiers "
          "GRADE_ONLY", G._planted_grade_only(cfg))
    check("C", "planted-negative: a certificate present in a demand field tiers "
          "DECLARED", G._planted_present(cfg))
    check("C", "every DECLARED edge re-verifies against the row's own demand text",
          G._recheck_declared(cfg))
    check("C", "no GRADE_ONLY or UNCITED edge leaked into the declared diagram",
          G._no_disputed_leak(cfg))
    check("C", "union-find agrees with an independent BFS on both edge sets",
          d["C"] == len(G.components_bfs(targets, declared))
          and b["C"] == len(G.components_bfs(targets, both)),
          (d["C"], len(G.components_bfs(targets, declared))))

    # =====================================================================
    # [E] -- THE CAVEAT, QUANTIFIED: edge dispute dominates vocabulary dispute
    # =====================================================================
    dC = b["C"] - d["C"]
    dbeta = b["beta"] - d["beta"]
    check("E", "declared -> declared+disputed moves C by -11 and beta by +35",
          (dC, dbeta) == (-11, 35), (dC, dbeta))
    check("E", "the EDGE-SET spread (|dbeta| = 35) is strictly larger than the whole "
          "vocabulary instability the invariant repairs (0)",
          abs(dbeta) > 0 and acc["coarse"]["beta"] == acc["fine"]["beta"],
          (abs(dbeta), acc["coarse"]["beta"], acc["fine"]["beta"]))
    check("E", "and larger than the presentation count's own 32 -> 35 move (3)",
          abs(dbeta) > 3, abs(dbeta))
    check("E", "15 rows are severing-vulnerable: they share at most one atom with "
          "any other row, so ANY refinement touching them can move C",
          len(res["severing_vulnerable_rows"]) == 15,
          str(res["severing_vulnerable_rows"]))

    # =====================================================================
    # [E] -- THE KILL: the target claim is retired by construction
    # =====================================================================
    # Target: "the ledger's 82 rows resolve to N formal degrees of freedom" as a
    # vocabulary-independent statement, in every arithmetic (N = 32 or N = 35).
    # T5's witness above is a LEGAL refinement of the declared diagram that
    # moves C.  So not even the diagram invariant is unconditionally
    # vocabulary-independent, and the generator count -- which has no
    # certificate at all -- is strictly worse off.
    check("E", "KILL: a legal refinement exists that moves C, so NO connectivity "
          "statistic is unconditionally refinement-invariant",
          ms["is_refinement"] and ms["fine_C"] != ms["coarse_C"])
    check("E", "KILL: the unconditional refinement-invariants are the ROW-side data "
          "only -- R, E and the row-degree multiset -- and they are equal across "
          "every refinement variant tested",
          all(v[e]["unconditional_equal"] for v in res["variants"].values()
              for e in ("declared", "declared_plus_disputed")
              if v["declared_type"] == "REFINEMENT"))
    check("E", "KILL: what replaces the bare number is the number PLUS a decidable "
          "non-severing certificate, which '32' never carried",
          isinstance(acc["severing"]["non_severing_certificate"], bool)
          and acc["severing"]["certificate_matches_recount"])

    # =====================================================================
    # [W] -- the gate's own well-formedness ratchet must be green
    # =====================================================================
    _r, wf = G.run(cfg, quiet=True)
    check("C", "the process gate's well-formedness ratchet is green",
          all(o for _t, _l, o, _d in wf),
          str([l for _t, l, o, _d in wf if not o]))
    return res


def emit(res: dict) -> int:
    G.report(res)
    npass = sum(1 for _t, _l, o, _d in CHECKS if o)
    by: dict[str, list[int]] = {}
    for tag, _l, o, _d in CHECKS:
        e = by.setdefault(tag, [0, 0])
        e[1] += 1
        e[0] += 1 if o else 0
    print()
    for tag, label, ok, detail in CHECKS:
        if not ok:
            print(f"  [FAIL] [{tag}] {label}   got: {detail}")
    print("-" * 78)
    print(f"CERTIFICATE: {npass}/{len(CHECKS)} checks pass; no load-bearing float (swept).")
    print("  by class:", {k: f"{v[0]}/{v[1]}" for k, v in sorted(by.items())})
    print("-" * 78)
    return 0 if npass == len(CHECKS) else 1


# =========================================================================
# --selftest: clean baseline FIRST, machinery-corruption mutations only
# =========================================================================

def _m_union(cfg):
    cfg["union_enabled"] = False


def _m_demand(cfg):
    cfg["demand_fields"] = G.DEMAND_FIELDS + ("mapping_grade",)


def _m_succ(cfg):
    cfg["inherit_to_successors"] = False


def _m_beta(cfg):
    cfg["beta_formula"] = "E-R"


def _m_atoms(cfg):
    cfg["induce_atoms_from_edges"] = False


def _m_sever(cfg):
    cfg["sever_certificate"] = "always-non-severing"


def _m_noninj(cfg):
    cfg["refinement_non_injective"] = True


def _m_status(cfg):
    cfg["status_fields"] = ()


def _m_drop(cfg):
    cfg["edges"] = list(cfg["edges"])[1:]


def _m_empty_cert(cfg):
    e = list(cfg["edges"])
    r, a, _s = e[0]
    e[0] = (r, a, ("",))
    cfg["edges"] = e


def _m_split_map(cfg):
    cfg["_split_map_gutted"] = True


MUTATIONS = [
    ("union_find_disabled", _m_union),
    ("demand_fields_widened_to_grades", _m_demand),
    ("successor_inheritance_dropped", _m_succ),
    ("beta_formula_corrupted", _m_beta),
    ("atom_vertices_not_induced", _m_atoms),
    ("severing_certificate_forced_true", _m_sever),
    ("refinement_made_non_injective", _m_noninj),
    ("status_fields_emptied", _m_status),
    ("one_edge_assertion_dropped", _m_drop),
    ("empty_certificate_admitted", _m_empty_cert),
    ("split_map_gutted", _m_split_map),
]


def selftest() -> int:
    print("=" * 78)
    print("CT-4 SELFTEST -- clean baseline verified FIRST, then mutations")
    print("=" * 78)
    try:
        run_probe(G.default_cfg())
    except Exception as exc:                                     # noqa: BLE001
        print(f"  BASELINE CRASHED: {type(exc).__name__}: {exc}")
        print("  ABORT RED (VERIFICATION.md rule 1).")
        return 1
    base_fail = [c for c in CHECKS if not c[2]]
    if base_fail:
        print(f"  CLEAN BASELINE IS RED ({len(base_fail)} failures) -- ABORT RED.")
        for tag, label, _o, detail in base_fail:
            print(f"    [FAIL] [{tag}] {label}  got: {detail}")
        return 1
    print(f"  clean baseline: {len(CHECKS)}/{len(CHECKS)} checks pass  [OK]")
    print()

    saved_split = dict(G.LA10_SPLIT)
    bad = []
    for name, mutate in MUTATIONS:
        cfg = G.default_cfg()
        mutate(cfg)
        gut = cfg.pop("_split_map_gutted", False)
        if gut:
            G.LA10_SPLIT.clear()
            G.LA10_SPLIT.update({k: "A_OWN" for k in saved_split})
        try:
            run_probe(cfg)
            fails = [c for c in CHECKS if not c[2]]
            if fails:
                verdict, note = "CAUGHT", f"{len(fails)} [FAIL]: {fails[0][1][:58]}"
            else:
                verdict, note = "MISSED", "no [FAIL] line -- mutation is invisible"
        except Exception as exc:                                 # noqa: BLE001
            verdict, note = "CRASH-NOT-DETECTION", f"{type(exc).__name__}: {exc}"
        finally:
            G.LA10_SPLIT.clear()
            G.LA10_SPLIT.update(saved_split)
        if verdict != "CAUGHT":
            bad.append((name, verdict, note))
        print(f"  mutation {name:<36s} {verdict:<20s} {note}")

    print()
    for name, verdict, note in bad:
        print(f"  [FAIL] mutation {name}: {verdict} -- {note}")
    print("-" * 78)
    print(f"SELFTEST: {len(MUTATIONS) - len(bad)}/{len(MUTATIONS)} mutations produced "
          "a GENUINE failing check; crash-catches are rejected.")
    print("-" * 78)
    return 1 if bad else 0


if __name__ == "__main__":
    if "--selftest" in sys.argv or "--self-test" in sys.argv:
        sys.exit(selftest())
    sys.exit(emit(run_probe()))
