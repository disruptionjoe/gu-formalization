#!/usr/bin/env python3
"""K1817: order-eight fixed-score parent bank with restart-safe checkpoints.

K1816 reduced K1813's degree-six remainder by about five orders on one exact
leaf but retained a slightly negative lower endpoint.  The admitted switch
route raises only the parameter Taylor order and returns to the seventeen
exact K1794 parents.  This attacks the measured remainder with two additional
powers of the small parent radii while preserving the fixed K1787 score,
observation grid, exact atlas and Cauchy inequality.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import sys
from fractions import Fraction as F
from functools import cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1817-full-fisher-slab-three-whole-line-value-cover.json"
CHECKPOINT_DIR = ROOT / "_local/k1816-leafwise-score-checkpoints/order-eight-parents"


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
PARAMETER_ORDER = 8


def fq(value) -> F:
    return F(str(value))


def ensure_backends() -> None:
    global m, atlas
    if m is None:
        m = load(
            "k1807_for_k1817",
            ROOT / "tests/channel-swings/k1807_full_fisher_anchored_score_compact_taylor.py",
        )
    if atlas is None:
        atlas = load(
            "k1804_for_k1817",
            ROOT / "tests/channel-swings/k1804_full_fisher_deduplicated_boundary_atlas.py",
        )


@cache
def parents():
    ensure_backends()
    return tuple(
        (cell, tuple(fq(value) for value in box))
        for slab, cell, box in atlas.k.roots()
        if slab == 3
    )


def partition_digest() -> str:
    data = json.loads(
        (ROOT / "lab/process/k1796-full-fisher-retained-box-enclosure-bank.json").read_text()
    )
    return data["enclosure"]["partition_digest"]


def checkpoint_path(parent_id: int) -> Path:
    return CHECKPOINT_DIR / f"parent-{parent_id:02d}.json"


def atomic_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    temporary.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    os.replace(temporary, path)


def compact_summary(certificate: dict) -> dict:
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
        "degree_eight_remainder_bounds": certificate["degree_six_remainder_bounds"],
    }


def compute_parent(parent_id: int) -> dict:
    ensure_backends()
    all_parents = parents()
    if not 0 <= parent_id < len(all_parents):
        raise ValueError(f"parent id {parent_id} outside 0..{len(all_parents) - 1}")
    cell, box = all_parents[parent_id]
    m.ANCHOR_T, m.ANCHOR_Z, m.THRESHOLD = ANCHOR_T, ANCHOR_Z, THRESHOLD
    m.PARAMETER_ORDER = PARAMETER_ORDER
    m.P.order = PARAMETER_ORDER
    m.T_LO, m.T_HI, m.Z_LO, m.Z_HI = box
    print(f"K1817 parent {parent_id:02d}/{len(all_parents) - 1:02d}: order-eight jet",
          file=sys.stderr, flush=True)
    certificate = compact_summary(m.compute())
    payload = {
        "schema_version": "1.0",
        "claim_id": "K1817",
        "parent": parent_id,
        "input_cell": cell,
        "input_partition_digest": partition_digest(),
        "box": [str(value) for value in box],
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


def load_checkpoint(parent_id: int) -> dict | None:
    path = checkpoint_path(parent_id)
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    canonical = dict(data)
    digest = canonical.pop("checkpoint_digest")
    encoded = json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
    if hashlib.sha256(encoded).hexdigest() != digest:
        raise ValueError(f"checkpoint digest mismatch: {path}")
    expected_cell, expected_box = parents()[parent_id]
    if data["parent"] != parent_id or data["input_cell"] != expected_cell:
        raise ValueError(f"checkpoint identity mismatch: {path}")
    if data["box"] != [str(value) for value in expected_box]:
        raise ValueError(f"checkpoint box mismatch: {path}")
    if data["input_partition_digest"] != partition_digest():
        raise ValueError(f"checkpoint partition mismatch: {path}")
    if data["certificate"]["parameter_taylor_order"] != PARAMETER_ORDER:
        raise ValueError(f"checkpoint order mismatch: {path}")
    return data


def ensure_parent(parent_id: int, replay: bool) -> dict:
    cached = load_checkpoint(parent_id)
    if cached is not None and not replay:
        print(f"K1817 parent {parent_id:02d}: checkpoint reused", file=sys.stderr)
        return cached
    computed = compute_parent(parent_id)
    atomic_json(checkpoint_path(parent_id), computed)
    return computed


def combined(rows: list[dict]) -> dict:
    rows = sorted(rows, key=lambda row: row["parent"])
    return {
        "input_partition_digest": partition_digest(),
        "parent_count": len(parents()),
        "completed_parent_count": len(rows),
        "completed_parent_ids": [row["parent"] for row in rows],
        "positive_compact_margin_count": sum(
            row["decision"]["compact_cross_margin_positive"] for row in rows
        ),
        "nonpositive_or_indeterminate_parent_ids": [
            row["parent"]
            for row in rows
            if not row["decision"]["compact_cross_margin_positive"]
        ],
        "checkpoint_digests": {
            str(row["parent"]): row["checkpoint_digest"] for row in rows
        },
        "parents": rows,
    }


def provisional_artifact() -> dict:
    parent = load_checkpoint(0)
    if parent is None:
        raise ValueError("K1817 provisional artifact requires parent zero")
    return {
        "schema_version": "1.0",
        "claim_id": "K1817",
        "status": "active_research",
        "title": "Order-eight parent scout isolates subdivision as the decisive certificate scale",
        "inputs": ["K1787", "K1794", "K1806", "K1813", "K1816"],
        "backend": "python-flint==0.9.0",
        "certificate": {
            "input_partition_digest": partition_digest(),
            "parent_count": len(parents()),
            "completed_parent_count": 1,
            "completed_parent_ids": [0],
            "parent_zero": parent,
            "order_eight_leaf_zero_compact_margin_positive": True,
        },
        "decision": {
            "order_eight_parent_zero_compact_margin_positive": parent["decision"]["compact_cross_margin_positive"],
            "parent_scale_sufficient": False,
            "leaf_subdivision_required": True,
            "complete_whole_line_value_cover": False,
            "global_optimizer_proved": False,
        },
        "scope_guard": "Raising the order from six to eight reduces the parent remainder but does not certify the parent. The positive order-eight leaf scout in K1816 shows that subdivision, not order alone, is decisive.",
    }


def validate(data: dict) -> list[tuple[str, bool]]:
    certificate = data["certificate"]
    parent = certificate["parent_zero"]
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1817"),
        ("partition", certificate["input_partition_digest"] == partition_digest()),
        ("17 parents", certificate["parent_count"] == 17),
        ("one scout", certificate["completed_parent_ids"] == [0]),
        ("parent indeterminate", not parent["decision"]["compact_cross_margin_positive"]),
        ("subdivision selected", data["decision"]["leaf_subdivision_required"]),
        ("whole line open", not data["decision"]["complete_whole_line_value_cover"]),
        ("global withheld", not data["decision"]["global_optimizer_proved"]),
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent", type=int, action="append", default=[])
    parser.add_argument("--resume-bank", action="store_true")
    parser.add_argument("--max-new", type=int)
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
    if not args.parent and not args.resume_bank:
        checks = validate(json.loads(ARTIFACT.read_text()))
        for index, (label, ok) in enumerate(checks, 1):
            assert ok, label
            print(f"PASS {index:02d}: {label}")
        print(f"RESULT: PASS {len(checks)}/{len(checks)}")
        return

    selected = args.parent or list(range(len(parents())))
    rows = []
    new_count = 0
    for parent_id in selected:
        cached = load_checkpoint(parent_id)
        if cached is None or args.replay:
            if args.max_new is not None and new_count >= args.max_new:
                continue
            new_count += 1
        rows.append(ensure_parent(parent_id, args.replay))
    if args.resume_bank:
        rows = [
            row for parent_id in range(len(parents()))
            if (row := load_checkpoint(parent_id))
        ]
    data = combined(rows)
    if args.write_artifact:
        if data["completed_parent_count"] != data["parent_count"]:
            raise ValueError("refusing to write a partial K1817 artifact")
        artifact = {
            "schema_version": "1.0",
            "claim_id": "K1817",
            "status": "active_research",
            "title": "Order-eight fixed-score compact cover on exact slab-three parents",
            "inputs": ["K1787", "K1794", "K1806", "K1813", "K1816"],
            "backend": "python-flint==0.9.0",
            "certificate": data,
            "decision": {
                "complete_compact_parent_bank_computed": True,
                "retained_parent_means_counterexample": False,
                "whole_line_composition_pending": True,
                "global_optimizer_proved": False,
            },
        }
        atomic_json(ARTIFACT, artifact)
    if args.summary:
        data = {key: value for key, value in data.items() if key != "parents"}
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
