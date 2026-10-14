#!/usr/bin/env python3
"""K1816: restart-safe leafwise fixed-score bank on slab three.

K1813 measured that the fixed K1787-score witness loses its sign on a complete
K1794 parent almost entirely through the absolute degree-six remainder.  This
producer changes only that proved source of loss: it recenters a normalized
Arb jet on each exact K1796 leaf.  Each leaf is written
atomically to ignored local checkpoint storage, so interruption never turns a
partial bank into evidence and completed leaves are replayable without another
quadrature.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import sys
from functools import cache
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1816-full-fisher-slab-three-leafwise-score-bank.json"
CHECKPOINT_DIR = ROOT / "_local/k1816-leafwise-score-checkpoints"


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


m = None
atlas = None

ANCHOR_T = F(265664669701527, 5000000000000000)
ANCHOR_Z = F(8805034043103, 15625000000000)
THRESHOLD = F(7958932265249, 50000000000000000000)


def fq(value) -> F:
    return F(str(value))


def ensure_backends() -> None:
    global m, atlas
    if m is None:
        m = load(
            "k1807_for_k1816",
            ROOT / "tests/channel-swings/k1807_full_fisher_anchored_score_compact_taylor.py",
        )
    if atlas is None:
        atlas = load(
            "k1804_for_k1816",
            ROOT / "tests/channel-swings/k1804_full_fisher_deduplicated_boundary_atlas.py",
        )


@cache
def leaves():
    ensure_backends()
    return tuple(
        (cell, tuple(fq(value) for value in box))
        for slab, cell, box in atlas.retained_boxes()
        if slab == 3
    )


def partition_digest() -> str:
    data = json.loads(
        (ROOT / "lab/process/k1796-full-fisher-retained-box-enclosure-bank.json").read_text()
    )
    return data["enclosure"]["partition_digest"]


def compact_summary(certificate: dict, parameter_order: int) -> dict:
    return {
        "rectangle": certificate["rectangle"],
        "center": certificate["center"],
        "radius": certificate["radius"],
        "anchor": certificate["anchor"],
        "threshold": certificate["threshold"],
        "window": certificate["window"],
        "cell_half_width": certificate["cell_half_width"],
        "observation_taylor_order": certificate["observation_taylor_order"],
        "parameter_taylor_order": certificate["parameter_taylor_order"],
        "compact_cell_count": certificate["compact_cell_count"],
        "compact_bounds": certificate["compact_bounds"],
        f"degree_{parameter_order}_remainder_bounds": certificate[
            "degree_six_remainder_bounds"
        ],
    }


def checkpoint_path(leaf_id: int, parameter_order: int) -> Path:
    suffix = "" if parameter_order == 6 else f"-order-{parameter_order:02d}"
    return CHECKPOINT_DIR / f"leaf-{leaf_id:03d}{suffix}.json"


def atomic_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    temporary.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    os.replace(temporary, path)


def compute_leaf(leaf_id: int, parameter_order: int) -> dict:
    ensure_backends()
    all_leaves = leaves()
    if not 0 <= leaf_id < len(all_leaves):
        raise ValueError(f"leaf id {leaf_id} outside 0..{len(all_leaves) - 1}")
    cell, box = all_leaves[leaf_id]
    m.ANCHOR_T, m.ANCHOR_Z, m.THRESHOLD = ANCHOR_T, ANCHOR_Z, THRESHOLD
    m.PARAMETER_ORDER = parameter_order
    m.P.order = parameter_order
    m.T_LO, m.T_HI, m.Z_LO, m.Z_HI = box
    print(
        f"K1816 leaf {leaf_id:02d}/77: order-{parameter_order} centered jet",
        file=sys.stderr,
        flush=True,
    )
    certificate = compact_summary(m.compute(), parameter_order)
    payload = {
        "schema_version": "1.0",
        "claim_id": "K1816",
        "leaf": leaf_id,
        "input_cell": cell,
        "input_partition_digest": partition_digest(),
        "box": [str(value) for value in box],
        "parameter_taylor_order": parameter_order,
        "certificate": certificate,
        "decision": {
            "compact_cross_margin_positive": certificate["compact_bounds"][
                "cross_margin_positive"
            ],
            "negative_margin_is_counterexample": False,
        },
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["checkpoint_digest"] = hashlib.sha256(canonical).hexdigest()
    return payload


def load_checkpoint(leaf_id: int, parameter_order: int) -> dict | None:
    path = checkpoint_path(leaf_id, parameter_order)
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    canonical = dict(data)
    digest = canonical.pop("checkpoint_digest")
    encoded = json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
    if hashlib.sha256(encoded).hexdigest() != digest:
        raise ValueError(f"checkpoint digest mismatch: {path}")
    expected_cell, expected_box = leaves()[leaf_id]
    if data["leaf"] != leaf_id or data["input_cell"] != expected_cell:
        raise ValueError(f"checkpoint identity mismatch: {path}")
    if data["box"] != [str(value) for value in expected_box]:
        raise ValueError(f"checkpoint box mismatch: {path}")
    if data["input_partition_digest"] != partition_digest():
        raise ValueError(f"checkpoint partition mismatch: {path}")
    recorded_order = data.get(
        "parameter_taylor_order", data["certificate"]["parameter_taylor_order"]
    )
    if recorded_order != parameter_order:
        raise ValueError(f"checkpoint order mismatch: {path}")
    return data


def ensure_leaf(leaf_id: int, parameter_order: int, replay: bool) -> dict:
    cached = load_checkpoint(leaf_id, parameter_order)
    if cached is not None and not replay:
        print(f"K1816 leaf {leaf_id:02d}/77: checkpoint reused", file=sys.stderr)
        return cached
    computed = compute_leaf(leaf_id, parameter_order)
    atomic_json(checkpoint_path(leaf_id, parameter_order), computed)
    return computed


def combined(rows: list[dict], parameter_order: int) -> dict:
    rows = sorted(rows, key=lambda row: row["leaf"])
    return {
        "input_partition_digest": partition_digest(),
        "parameter_taylor_order": parameter_order,
        "leaf_count": len(leaves()),
        "completed_leaf_count": len(rows),
        "completed_leaf_ids": [row["leaf"] for row in rows],
        "positive_compact_margin_count": sum(
            row["decision"]["compact_cross_margin_positive"] for row in rows
        ),
        "nonpositive_or_indeterminate_leaf_ids": [
            row["leaf"]
            for row in rows
            if not row["decision"]["compact_cross_margin_positive"]
        ],
        "checkpoint_digests": {
            str(row["leaf"]): row["checkpoint_digest"] for row in rows
        },
        "leaves": rows,
    }


def provisional_artifact() -> dict:
    """Embed the calibrated scouts and completed production leaves."""
    order_six = load_checkpoint(0, 6)
    order_eight = load_checkpoint(0, 8)
    order_seven = [
        row for leaf_id in range(len(leaves()))
        if (row := load_checkpoint(leaf_id, 7)) is not None
    ]
    if order_six is None or order_eight is None or len(order_seven) < 2:
        raise ValueError("K1816 provisional artifact requires 6/7/8 calibration and two order-seven leaves")
    return {
        "schema_version": "1.0",
        "claim_id": "K1816",
        "status": "active_research",
        "title": "Leafwise order-seven fixed-score calibration on the slab-three frontier",
        "inputs": ["K1787", "K1796", "K1806", "K1813"],
        "backend": "python-flint==0.9.0",
        "certificate": {
            "input_partition_digest": partition_digest(),
            "leaf_count": len(leaves()),
            "selected_parameter_order": 7,
            "fallback_parameter_order": 8,
            "completed_order_seven_leaf_count": len(order_seven),
            "completed_order_seven_leaf_ids": [row["leaf"] for row in order_seven],
            "order_six_leaf_zero": order_six,
            "order_seven_completed_leaves": order_seven,
            "order_eight_leaf_zero": order_eight,
            "measured_minutes_per_order_seven_leaf": "approximately 18",
            "estimated_remaining_serial_hours": "approximately 23",
            "resume_command": "UV_CACHE_DIR=/private/tmp/uv-cache-gu-science uv run --offline --with python-flint==0.9.0 --with sympy==1.14.0 python tests/channel-swings/k1816_full_fisher_slab_three_leafwise_score_bank.py --resume-bank --parameter-order 7 --summary",
        },
        "decision": {
            "leafwise_recentering_validated": True,
            "order_seven_selected_for_production": True,
            "order_eight_fallback_validated": True,
            "complete_compact_leaf_bank_computed": len(order_seven) == len(leaves()),
            "retained_leaf_means_counterexample": False,
            "whole_line_composition_separate": True,
            "global_optimizer_proved": False,
        },
        "scope_guard": "The first two order-seven leaves have strict compact margins. The remaining 76 leaves, whole-line tails, stationary rejection and exposed boundary still require completion before any global promotion.",
    }


def validate(data: dict) -> list[tuple[str, bool]]:
    certificate = data["certificate"]
    seven = certificate["order_seven_completed_leaves"]
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1816"),
        ("partition", certificate["input_partition_digest"] == partition_digest()),
        ("78 leaves", certificate["leaf_count"] == 78),
        ("two production leaves", certificate["completed_order_seven_leaf_ids"] == [0, 1]),
        ("order seven positive", all(row["decision"]["compact_cross_margin_positive"] for row in seven)),
        ("sixth order indeterminate", not certificate["order_six_leaf_zero"]["decision"]["compact_cross_margin_positive"]),
        ("eighth order fallback positive", certificate["order_eight_leaf_zero"]["decision"]["compact_cross_margin_positive"]),
        ("bank incomplete", not data["decision"]["complete_compact_leaf_bank_computed"]),
        ("global withheld", not data["decision"]["global_optimizer_proved"]),
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--leaf", type=int, action="append", default=[])
    parser.add_argument("--resume-bank", action="store_true")
    parser.add_argument("--max-new", type=int)
    parser.add_argument("--parameter-order", type=int, choices=(6, 7, 8), default=6)
    parser.add_argument("--replay", action="store_true")
    parser.add_argument("--write-artifact", action="store_true")
    parser.add_argument("--write-provisional-artifact", action="store_true")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()

    if args.write_provisional_artifact:
        artifact = provisional_artifact()
        atomic_json(ARTIFACT, artifact)
        print(json.dumps(artifact, indent=2))
        return
    if not args.leaf and not args.resume_bank:
        checks = validate(json.loads(ARTIFACT.read_text()))
        for index, (label, ok) in enumerate(checks, 1):
            assert ok, label
            print(f"PASS {index:02d}: {label}")
        print(f"RESULT: PASS {len(checks)}/{len(checks)}")
        return

    selected = args.leaf or list(range(len(leaves())))
    rows = []
    new_count = 0
    for leaf_id in selected:
        cached = load_checkpoint(leaf_id, args.parameter_order)
        if cached is None or args.replay:
            if args.max_new is not None and new_count >= args.max_new:
                continue
            new_count += 1
        rows.append(ensure_leaf(leaf_id, args.parameter_order, args.replay))

    if args.resume_bank:
        rows = [
            row
            for leaf_id in range(len(leaves()))
            if (row := load_checkpoint(leaf_id, args.parameter_order))
        ]
    data = combined(rows, args.parameter_order)
    if args.write_artifact:
        if data["completed_leaf_count"] != data["leaf_count"]:
            raise ValueError("refusing to write a partial K1816 artifact")
        artifact = {
            "schema_version": "1.0",
            "claim_id": "K1816",
            "status": "active_research",
            "title": "Leafwise recentered fixed-score bank on the complete slab-three frontier",
            "inputs": ["K1787", "K1796", "K1806", "K1813"],
            "backend": "python-flint==0.9.0",
            "certificate": data,
            "decision": {
                "complete_compact_leaf_bank_computed": True,
                "retained_leaf_means_counterexample": False,
                "whole_line_composition_separate": True,
                "global_optimizer_proved": False,
            },
        }
        atomic_json(ARTIFACT, artifact)
    if args.summary:
        data = {key: value for key, value in data.items() if key != "leaves"}
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
