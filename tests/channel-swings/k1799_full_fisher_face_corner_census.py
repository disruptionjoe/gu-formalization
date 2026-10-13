#!/usr/bin/env python3
"""Replay K1799's conservative residual boundary-incidence census."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1799-full-fisher-face-corner-census.json";K1796=ROOT/"lab/process/k1796-full-fisher-retained-box-enclosure-bank.json"
def validate(data):
    bank=json.loads(K1796.read_text())["enclosure"];census=data["census"];decision=data["decision"]
    leaves=bank["retained_leaves"]
    return [("schema",data["schema_version"]=="1.0"),("claim",data["claim_id"]=="K1799"),("inputs",data["inputs"]==["K1796","K1797","K1798"]),("leaf total",census["retained_terminal_leaves"]==leaves==85),("slab decomposition",census["slab_two_leaves"]+census["slab_three_leaves"]==leaves),("face incidences",census["box_local_face_incidences"]==4*leaves),("corner incidences",census["box_local_corner_incidences"]==4*leaves),("face arithmetic",census["face_incidences_closed_by_this_wave"]+census["face_incidences_remaining"]==census["box_local_face_incidences"]),("corner arithmetic",census["corner_incidences_closed_by_this_wave"]+census["corner_incidences_remaining"]==census["box_local_corner_incidences"]),("not unique geometry",not census["incidence_count_is_unique_geometric_boundary_count"]),("census emitted",decision["complete_residual_boundary_census_emitted"]),("faces open",not decision["all_residual_faces_closed"]),("corners open",not decision["all_residual_corners_closed"]),("not global",not decision["global_optimizer_proved"])]
def main():
    checks=validate(json.loads(ARTIFACT.read_text()))
    for index,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {index:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
