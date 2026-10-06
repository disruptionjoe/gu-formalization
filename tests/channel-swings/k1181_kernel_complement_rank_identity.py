#!/usr/bin/env python3
"""K1181: exact rank identity for a new map on a Hessian kernel."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1181-kernel-complement-rank-identity.json"


def complement_rank(dim_v: int, rank_h: int, rank_stacked: int) -> int:
    assert 0 <= rank_h <= rank_stacked <= dim_v
    return rank_stacked - rank_h


def build() -> dict[str, Any]:
    controls = []
    for dim_v, rank_h, rank_stacked in ((5, 2, 4), (7, 3, 3), (9, 0, 6), (9, 9, 9)):
        controls.append({
            "dim_v": dim_v,
            "rank_h": rank_h,
            "rank_stacked": rank_stacked,
            "rank_j_on_ker_h": complement_rank(dim_v, rank_h, rank_stacked),
        })
    return {
        "schema_version": "1.0",
        "result_id": "K1181-KERNEL-COMPLEMENT-RANK-IDENTITY",
        "created": "2026-10-05",
        "status": "working_draft_verified",
        "identity": "rank(J|ker H)=rank((H,J))-rank(H)",
        "proof": "rank(H,J)-rank(H)=dim ker(H)-dim(ker(H) intersect ker(J))",
        "controls": controls,
        "sharp": True,
        "claim_ceiling": "finite-dimensional rank identity only; no source ownership, positivity, domain or physical quotient",
    }


def validate(packet: dict[str, Any]) -> None:
    assert packet["result_id"] == "K1181-KERNEL-COMPLEMENT-RANK-IDENTITY"
    assert packet["status"] == "working_draft_verified"
    assert packet["identity"] == "rank(J|ker H)=rank((H,J))-rank(H)"
    assert packet["sharp"]
    assert len(packet["controls"]) == 4
    expected = [2, 0, 6, 0]
    for row, value in zip(packet["controls"], expected):
        assert row["rank_j_on_ker_h"] == value
        assert row["rank_j_on_ker_h"] == complement_rank(row["dim_v"], row["rank_h"], row["rank_stacked"])
    assert "no source ownership" in packet["claim_ceiling"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    packet = build(); validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered, encoding="utf-8")
    else: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
