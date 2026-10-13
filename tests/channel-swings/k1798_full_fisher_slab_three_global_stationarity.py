#!/usr/bin/env python3
"""Replay K1798's slab-three contraction and uniqueness boundary."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1798-full-fisher-slab-three-global-stationarity.json";K1796=ROOT/"lab/process/k1796-full-fisher-retained-box-enclosure-bank.json";K1787=ROOT/"lab/process/k1787-full-fisher-stationary-krawczyk.json"
def validate(data):
    bank=json.loads(K1796.read_text())["enclosure"];row=bank["by_slab"][1];local=json.loads(K1787.read_text());certificate=data["certificate"];decision=data["decision"]
    return [("schema",data["schema_version"]=="1.0"),("claim",data["claim_id"]=="K1798"),("inputs",data["inputs"]==["K1787","K1794","K1796"]),("digest",certificate["degree_eleven_partition_digest"]==bank["partition_digest"]),("input leaves",certificate["input_leaves"]==row["input_leaves"]==17),("pruned",certificate["pruned_leaves"]==row["pruned_leaves"]==51),("retained",certificate["retained_leaves"]==row["retained_leaves"]==78),("area",Fraction(certificate["retained_fraction_of_slab_input_area"])==Fraction(39,136)),("local stationary",certificate["named_local_stationary_box_strictly_isolated"] and local["decision"]["unique_whole_line_stationary_point_in_named_box"]),("strict contraction",decision["strict_outer_frontier_contraction"]),("complete uniqueness open",not decision["unique_stationary_point_on_complete_slab_three"]),("boundary open",not decision["every_slab_three_face_and_corner_closed"]),("not global",not decision["global_optimizer_proved"])]
def main():
    checks=validate(json.loads(ARTIFACT.read_text()))
    for index,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {index:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
