#!/usr/bin/env python3
"""Replay K1797's slab-two contraction and admission boundary."""
import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
ARTIFACT=ROOT/"lab/process/k1797-full-fisher-slab-two-global-kkt.json"
K1796=ROOT/"lab/process/k1796-full-fisher-retained-box-enclosure-bank.json"
K1788=ROOT/"lab/process/k1788-full-fisher-first-two-slab-exclusion.json"


def validate(data):
    bank=json.loads(K1796.read_text())["enclosure"]
    row=bank["by_slab"][0]
    local=json.loads(K1788.read_text())
    certificate=data["certificate"];decision=data["decision"]
    return [
        ("schema",data["schema_version"]=="1.0"),
        ("claim",data["claim_id"]=="K1797"),
        ("inputs",data["inputs"]==["K1788","K1793","K1796"]),
        ("digest",certificate["degree_eleven_partition_digest"]==bank["partition_digest"]),
        ("input leaves",certificate["input_leaves"]==row["input_leaves"]==8),
        ("pruned",certificate["pruned_leaves"]==row["pruned_leaves"]==19),
        ("retained",certificate["retained_leaves"]==row["retained_leaves"]==7),
        ("area",Fraction(certificate["retained_fraction_of_slab_input_area"])==Fraction(7,128)),
        ("local KKT",decision["local_boundary_kkt_isolated"] and local["decision"]["unique_local_boundary_kkt_points"]==2),
        ("strict contraction",decision["strict_outer_frontier_contraction"]),
        ("slab open",not decision["complete_slab_two_sublevel_excluded"]),
        ("boundary open",not decision["every_slab_two_face_and_corner_closed"]),
        ("not global",not decision["global_optimizer_proved"]),
    ]


def main():
    checks=validate(json.loads(ARTIFACT.read_text()))
    for index,(label,ok) in enumerate(checks,1):
        assert ok,label;print(f"PASS {index:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__=="__main__":main()
