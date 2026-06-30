import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-1702-cycle3-next-frontier-dependency-dag.md"


def load_summary():
    text = ARTIFACT.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    assert blocks, "artifact must contain a machine-readable JSON summary"
    return json.loads(blocks[-1])


def test_candidate_bank_has_at_least_18_quality_candidates():
    data = load_summary()
    candidates = data["quality_candidates"]
    assert data["quality_candidates_claimed"] == len(candidates)
    assert len(candidates) >= 18
    assert len(candidates) == len(set(candidates))


def test_recommended_next_five_are_exactly_five_and_disjoint():
    data = load_summary()
    lanes = data["recommended_next_five"]
    assert len(lanes) == 5

    route_families = [lane["route_family"] for lane in lanes]
    owned_surfaces = [lane["owned_surface"] for lane in lanes]
    lane_ids = [lane["id"] for lane in lanes]

    assert sorted(route_families) == ["DGU", "IG", "PTUJ", "QFT", "RS"]
    assert len(owned_surfaces) == len(set(owned_surfaces))
    assert data["immediate_parallel_safe_lanes"] == lane_ids


def test_recommended_lanes_are_not_downstream_replay():
    data = load_summary()
    forbidden_terms = [
        "FORMULA_VISIBILITY",
        "KEATING",
        "K_IG_FAMILY_IDENTITY",
        "VZ_REPLAY",
        "SYMBOL_CERTIFICATE",
        "TYPED_MINUS_ONE_OPERATOR",
        "PHYSICAL_QUOTIENT",
        "CHSH",
        "BELL",
        "RHO_AB",
    ]
    for lane in data["recommended_next_five"]:
        lane_id = lane["id"]
        assert not any(term in lane_id for term in forbidden_terms), lane_id


def test_sequential_deferred_and_dependency_edges_are_nonempty():
    data = load_summary()
    sequential = data["sequential_deferred"]
    edges = data["dependency_edges"]
    assert sequential
    assert edges
    assert len(sequential) >= 5
    assert len(edges) >= 10
    assert all(row["wait_for"] for row in sequential)
    assert all(edge["from"] and edge["to"] and edge["kind"] for edge in edges)


def test_zero_receipts_no_restart_no_target_import():
    data = load_summary()
    assert data["accepted_receipt_count"] == 0
    assert data["proof_restart"] is False
    assert data["proof_restart_allowed"] is False
    assert data["target_import"] is False
    assert data["target_import_used"] is False
    assert data["claim_promotion_allowed"] is False
    assert data["downstream_replay_allowed"] is False

    by_route = data["accepted_receipt_count_by_route"]
    assert set(by_route) == {"PTUJ", "IG", "DGU", "RS", "QFT"}
    assert all(count == 0 for count in by_route.values())


def test_anti_overlap_checks_pass():
    data = load_summary()
    checks = data["anti_overlap_checks"]
    assert checks
    names = {check["check"] for check in checks}
    required = {
        "route_family_disjoint",
        "owned_surface_descriptions_disjoint",
        "no_downstream_replay_in_recommended_lanes",
        "no_target_import",
        "no_same_mathematical_question_duplicates",
    }
    assert required.issubset(names)
    assert all(check["passed"] is True for check in checks)


def test_support_and_guard_lists_are_explicit():
    data = load_summary()
    support = data["support_lanes"]
    guards = data["demoted_guard_lanes"]
    assert support
    assert guards
    assert "GLOBAL_NO_RECEIPT_NO_PROOF_RESTART_FIREWALL" in guards
    assert "QFT_FINITE_EXTRACTION_RHO_AB_BELL_CHSH_FIREWALL" in guards


def test_recommended_lanes_are_quality_candidates():
    data = load_summary()
    candidates = set(data["quality_candidates"])
    for lane in data["recommended_next_five"]:
        assert lane["id"] in candidates
