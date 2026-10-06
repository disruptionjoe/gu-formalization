#!/usr/bin/env python3
"""Compile exact anisotropic projective controls for every order-ten codimension."""
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
K415=ROOT/"lab/process/k415-order-ten-face-program-compiler.json";K1193=ROOT/"lab/process/k1193-order-ten-normal-projective-atlas.json";K1194=ROOT/"lab/process/k1194-order-ten-projective-measure-and-boundary-routing.json";OUTPUT=ROOT/"lab/process/k1195-order-ten-anisotropic-projective-controls.json"
def q(v:Fraction)->str:return str(v.numerator) if v.denominator==1 else f"{v.numerator}/{v.denominator}"
def digest(v:Any)->str:return "sha256:"+hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",", ":")).encode()).hexdigest()
def proportions(axes:list[str])->dict[str,Fraction]:
    weights={a:Fraction(i+1) for i,a in enumerate(axes)};total=sum(weights.values(),Fraction());return {a:w/total for a,w in weights.items()}
def build()->dict[str,Any]:
    k415=json.loads(K415.read_text());k1193=json.loads(K1193.read_text());k1194=json.loads(K1194.read_text());programs=k415["face_programs"]
    rows=[]
    for c in k1193["fixed_control"]["reachable_codimensions"]:
        p=next(r for r in programs if int(r["codimension"])==c);ps=proportions(p["zeroed_axes"]);anchor=max(ps,key=ps.get);ratios={a:ps[a]/ps[anchor] for a in p["zeroed_axes"] if a!=anchor};den=1+sum(ratios.values(),Fraction());rebuilt={anchor:Fraction(1,1)/den,**{a:r/den for a,r in ratios.items()}}
        rows.append({"codimension":c,"program_id":p["program_id"],"axis":p["axis"],"zeroed_axes":p["zeroed_axes"],"anchor_axis":anchor,"projective_proportions":{a:q(v) for a,v in ps.items()},"maximum_chart_ratios":{a:q(v) for a,v in ratios.items()},"proportions_sum_to_one":sum(ps.values(),Fraction())==1,"direction_is_strictly_positive":all(v>0 for v in ps.values()),"direction_is_not_equal_normal":len(set(ps.values()))>1,"anchor_is_unique_maximum":sum(v==ps[anchor] for v in ps.values())==1,"ratios_strictly_between_zero_and_one":all(0<v<1 for v in ratios.values()),"chart_inverse_reconstructs_direction":rebuilt==ps})
    return {"schema_version":"1.0","result_id":"K1195-ORDER-TEN-ANISOTROPIC-PROJECTIVE-CONTROL-BANK","created":"2026-10-06","classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native",
      "fixed_control":{"predecessor_manifests":[str(K415.relative_to(ROOT)),str(K1193.relative_to(ROOT)),str(K1194.relative_to(ROOT))],"reachable_codimensions":k1193["fixed_control"]["reachable_codimensions"],"selected_controls":len(rows),"face_programs_in_scope":len(programs),"unique_zero_masks_in_scope":k1193["fixed_control"]["unique_zero_masks"],"control_bank_digest":digest(rows)},
      "coordinate_contract":{"one_exact_non_equal_positive_rational_direction_per_reachable_codimension":True,"maximum_chart_selected_by_unique_largest_weight":True,"all_ratio_coordinates_strictly_inside_zero_and_one":True,"exact_inverse_required":True,"controls_are_coordinates_not_integrand_intervals":True,"no_Arb_or_Bessel_evaluation_claimed":True},
      "anisotropic_control_bank":rows,
      "decision":{"anisotropic_projective_coordinate_interface_complete":True,"preconditioned_integrand_intervals_executed":False,"zero_inclusive_boundary_majorants_complete":False,"recursive_positive_interior_cover_complete":False,"complete_hybrid_integrals_emitted":False,"next_exact_input":"Build a factorized or cached group evaluator before executing interval boxes around these sixteen exact interior directions; do not replay 936 unique complete programs directly."},
      "release_test":{"exactly_16_reachable_codimensions":len(rows)==16,"all_directions_exact_positive_and_non_equal":all(r["proportions_sum_to_one"] and r["direction_is_strictly_positive"] and r["direction_is_not_equal_normal"] for r in rows),"all_unique_maximum_charts_are_interior":all(r["anchor_is_unique_maximum"] and r["ratios_strictly_between_zero_and_one"] for r in rows),"all_chart_inverses_exact":all(r["chart_inverse_reconstructs_direction"] for r in rows),"integrand_intervals_not_overclaimed":True,"complete_order_ten_remainder_not_overclaimed":True,"native_K152_interval_not_emitted":True},
      "ledger_effect":k415["ledger_effect"],"source_routing":k415["source_routing"],"claim_ceiling":"Exact rational anisotropic maximum-chart control bank for all sixteen reachable K415 codimensions. Each control is strictly positive, non-equal, has one unique maximal coordinate, lies in the open ratio cube and reconstructs exactly through K1193's inverse. These are coordinate controls only: no preconditioned integrand interval, zero-boundary envelope, recursive cover, Peano remainder, integral, action column, K152 interval, source, ledger, canon, paper, public or physical claim is emitted."}
def validate_payload(p:dict[str,Any])->None:
    f=p["fixed_control"]
    if (f["selected_controls"],f["face_programs_in_scope"],f["unique_zero_masks_in_scope"])!=(16,936,121):raise AssertionError("K1195 census changed")
    rows=p["anisotropic_control_bank"]
    if len(rows)!=16 or not all(r["proportions_sum_to_one"] and r["direction_is_strictly_positive"] and r["direction_is_not_equal_normal"] and r["anchor_is_unique_maximum"] and r["ratios_strictly_between_zero_and_one"] and r["chart_inverse_reconstructs_direction"] for r in rows) or not all(p["release_test"].values()):raise AssertionError("K1195 controls changed")
    if p["decision"]["preconditioned_integrand_intervals_executed"] or not p["coordinate_contract"]["no_Arb_or_Bessel_evaluation_claimed"]:raise AssertionError("K1195 overclaimed numerical execution")
def main()->int:
    a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");x=a.parse_args();p=build();validate_payload(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if x.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())
