#!/usr/bin/env python3
"""Replay K1800's protected global-optimizer admission boundary."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1800-full-fisher-global-optimizer-admission.json";K1796=ROOT/"lab/process/k1796-full-fisher-retained-box-enclosure-bank.json";K1799=ROOT/"lab/process/k1799-full-fisher-face-corner-census.json"
def validate(data):
    bank=json.loads(K1796.read_text())["enclosure"];boundary=json.loads(K1799.read_text());census=data["bridge_census"];entry=data["entry_state"];decision=data["decision"];protected=data["protected_state"]
    return [("schema",data["schema_version"]=="1.0"),("claim",data["claim_id"]=="K1800"),("inputs",data["inputs"]==["K1795","K1796","K1797","K1798","K1799"]),("census arithmetic",census["total"]==census["satisfied"]+census["conditional"]+census["excluded"]+census["missing"]),("exact replay",entry["degree_eleven_exact_partition_replayed"]),("resource block removed",entry["fixed_cutoff_symbolic_resource_block_removed"]),("area",Fraction(entry["excluded_fraction_of_original_input_area"])==Fraction(bank["excluded_fraction_of_original_input_area"])==Fraction(15019,15104)),("slab one",entry["slab_one_complete_sublevel_excluded"] and decision["slab_one_globally_excluded"]),("residual leaves",entry["slab_two_retained_leaves"]+entry["slab_three_retained_leaves"]==bank["retained_leaves"]==85),("cover open",not entry["complete_complement_cover_available"]),("slab two open",not decision["slab_two_globally_excluded"]),("slab three open",not decision["unique_stationary_point_on_complete_slab_three"]),("boundary open",not decision["all_residual_faces_and_corners_closed"] and not boundary["decision"]["all_residual_faces_closed"]),("global open",not decision["global_optimizer_proved"]),("physical open",not decision["source_owned_physical_theory"]),("protected",not any(value for key,value in protected.items() if key.endswith("_changed"))),("K1145",protected["k1145_score"]=="0/7"),("K1150",protected["k1150_score"]=="0/7")]
def main():
    checks=validate(json.loads(ARTIFACT.read_text()))
    for index,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {index:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
