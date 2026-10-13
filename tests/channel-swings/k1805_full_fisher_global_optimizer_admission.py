#!/usr/bin/env python3
"""Protected global admission after K1801--K1804."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1805-full-fisher-global-optimizer-admission.json"
FILES = {
    "k1801": ROOT / "lab/process/k1801-full-fisher-third-order-compact-jet.json",
    "k1802": ROOT / "lab/process/k1802-full-fisher-slab-two-taylor-bank.json",
    "k1803": ROOT / "lab/process/k1803-full-fisher-slab-two-global-kkt.json",
    "k1804": ROOT / "lab/process/k1804-full-fisher-deduplicated-boundary-atlas.json",
}


def compute():
    data = {key: json.loads(path.read_text()) for key, path in FILES.items()}
    atlas = data["k1804"]["certificate"]
    return {
        "compact_third_order_parameter_jet_certified": bool(
            data["k1801"]["decision"]["compact_third_order_parameter_jet_certified"]),
        "degree_thirteen_projection_only_closure_rejected": bool(
            data["k1802"]["decision"]["degree_thirteen_projection_only_closure_rejected"]),
        "positive_projection_complement_at_slab_two_kkt_gt_2_5e_minus_14": bool(
            data["k1802"]["certificate"]["full_fisher_minus_projection_gt_2_5e_minus_14"]),
        "slab_two_residual_union_exact_rectangle": bool(
            data["k1804"]["decision"]["slab_two_residual_union_is_one_exact_rectangle"]),
        "residual_exposed_atomic_faces": atlas["exposed_atomic_faces"],
        "residual_exposed_boundary_vertices": atlas["exposed_boundary_vertices"],
        "slab_two_globally_excluded": bool(data["k1803"]["decision"]["slab_two_globally_excluded"]),
        "complete_slab_three_stationary_classification": False,
        "all_exposed_boundaries_certified": bool(
            data["k1804"]["decision"]["all_exposed_faces_and_corners_certified"]),
    }


def validate(data, got=None):
    got = compute() if got is None else got
    decision = data["decision"]
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1805"),
        ("inputs", data["inputs"] == ["K1801", "K1802", "K1803", "K1804"]),
        ("composition", data["entry_state"] == got),
        ("jet retained", got["compact_third_order_parameter_jet_certified"]),
        ("projection route rejected", got["degree_thirteen_projection_only_closure_rejected"]),
        ("complement floor", got["positive_projection_complement_at_slab_two_kkt_gt_2_5e_minus_14"]),
        ("geometry contracted", got["residual_exposed_atomic_faces"] == 122
         and got["residual_exposed_boundary_vertices"] == 122),
        ("slab two open", not got["slab_two_globally_excluded"]),
        ("slab three open", not got["complete_slab_three_stationary_classification"]),
        ("boundaries open", not got["all_exposed_boundaries_certified"]),
        ("global withheld", not decision["global_optimizer_proved"]),
        ("source protected", not decision["source_owned_physical_theory"]),
    ]


def main():
    got = compute()
    if not ARTIFACT.exists() or "--print" in __import__("sys").argv:
        print(json.dumps(got, indent=2))
        return
    checks = validate(json.loads(ARTIFACT.read_text()), got)
    for index, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {index:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
