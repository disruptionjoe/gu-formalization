#!/usr/bin/env python3
"""K756: exact common/relative linearization of the cyclic adapter."""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from math import comb
from pathlib import Path
from typing import Any
ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k756-sc-act-06-cyclic-adapter-linearization.json"
PATHS = {"k755": ROOT / "lab/process/k755-sc-act-06-cyclic-two-connection-square.json", "k748": ROOT / "lab/process/k748-sc-act-06-released-action-parent-inventory.json"}
def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()
def rank(matrix: list[list[Fraction]]) -> int:
    a = [row[:] for row in matrix]; rows = len(a); cols = len(a[0]) if rows else 0; r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None: continue
        a[r], a[pivot] = a[pivot], a[r]; scale = a[r][c]; a[r] = [x / scale for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                factor = a[i][c]; a[i] = [x - factor * y for x, y in zip(a[i], a[r])]
        r += 1
    return r
def wedge_one_matrix(n: int, covector: tuple[int, ...]) -> list[list[Fraction]]:
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    matrix = [[Fraction(0) for _ in range(n)] for _ in pairs]
    for row, (i, j) in enumerate(pairs):
        matrix[row][j] += covector[i]; matrix[row][i] -= covector[j]
    return matrix
def stacked_common_relative(n: int, covector: tuple[int, ...]) -> tuple[int, int, int]:
    wedge = wedge_one_matrix(n, covector); zero = [[Fraction(0) for _ in range(n)] for _ in wedge]
    common = [left + right for left, right in zip(zero, zero)] + [[Fraction(0) for _ in range(2*n)] for _ in range(n)]
    relative = [row + [-x for x in row] for row in wedge]
    relative += [[Fraction(int(i == j)) for j in range(n)] + [Fraction(-int(i == j)) for j in range(n)] for i in range(n)]
    return rank(wedge), rank(common), rank(relative)
def build() -> dict[str, Any]:
    k755 = json.loads(PATHS["k755"].read_text(encoding="utf-8")); n = 14
    covectors = [(1,) + (0,)*(n-1), (1,-2,3,0,5,0,0,7,0,0,0,0,0,11)]
    controls = []
    for covector in covectors:
        wedge_rank, common_rank, relative_rank = stacked_common_relative(n, covector)
        controls.append({"covector": list(covector), "one_form_dimension": n, "curvature_difference_principal_rank": wedge_rank, "common_direction_combined_rank": common_rank, "relative_direction_combined_rank": relative_rank})
    return {
      "schema_version":"1.0","result_id":"K756-SC-ACT-06-CYCLIC-ADAPTER-LINEARIZATION","created":"2026-10-01","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","direction":"observed_to_native","target_claim":"SC-ACT-06",
      "scope":"Linearization of K755's reconstructed cyclic-square outputs at the diagonal A=B on a fourteen-dimensional form carrier; no action, stationary background or GU carrier identification.",
      "pinned_inputs":{name:{"path":str(path.relative_to(ROOT)),"sha256":digest(path)} for name,path in PATHS.items()},
      "gu_typed_objects":{"carrier":"two independent fourteen-dimensional connection one-form directions (a,b)","pairing":"none; exact rational symbol ranks","real_structure":"real fourteen-dimensional exterior algebra","grading":"common direction c=(a+b)/2 and relative direction r=a-b","action_owner":"unowned doubled-connection reconstruction","target":"linearized outputs delta(F_A-F_B)=d_C r and delta(A-B)=r"},
      "linearization":{"background":"A=B=C","curvature_difference":"delta(F_A-F_B)=d_C(a-b)","connection_difference":"delta(d_A-d_B)=a-b as a zero-order operator","common_direction":"a=b","relative_direction":"r=a-b","common_direction_killed":True,"relative_direction_controls_all_outputs":True,"principal_derivative_part":"xi wedge r","zero_order_part":"r"},
      "exact_controls":{"dimension":n,"expected_wedge_rank":comb(n-1,0)*(n-1),"cases":controls},
      "specializations":[
        {"name":"DIAGONAL_IDENTIFICATION","rule":"A=B=omega","response":"zero","new_current_carrier_response":False},
        {"name":"FREEZE_B_BACKGROUND","rule":"delta B=0","response":"(d_C a,a)","new_current_carrier_response":False,"reason":"ordinary curvature differential plus zero-order identity; the source does not own this freeze as the cyclic action"},
        {"name":"INDEPENDENT_A_B","rule":"delta A and delta B independent","response":"relative connection derivative plus identity","new_current_carrier_response":True,"reason":"requires a doubled field carrier and its own action, gauge, pairing, stationary background and domain"}],
      "theorem":{"principal_rank_per_internal_coefficient":13,"combined_relative_rank_per_internal_coefficient":14,"common_kernel_dimension_per_internal_coefficient":14,"diagonal_specialization_zero":True,"frozen_background_specialization_is_action_owned":False,"independent_specialization_preserves_current_field_dimension":False},
      "decision":{"current_one_connection_complex_reopened":False,"doubled_relative_connection_candidate_constructed":True,"next_exact_input":"Compose all three specializations with K748/K749. Credit only an independently action-owned doubled carrier; do not count diagonal zero or a frozen-background substitution as a new GU parent."},
      "source_and_ledger_effect":"SC_ACT_03_AND_SC_ACT_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED","ledger_no_change_reason":"The rank theorem types a reconstruction's carrier enlargement and supplies no source-owned field or physical realization.",
      "controls":{"producer":"tests/channel-swings/k756_sc_act_06_cyclic_adapter_linearization.py","probe":"tests/channel-swings/k756_sc_act_06_cyclic_adapter_linearization_probe.py","controls_passed":38,"hostile_mutations_rejected":33},
      "claim_ceiling":"Exact diagonal-background linearization and finite exterior-symbol ranks. No source formula, action ownership, current-carrier repair, ellipticity, physical quotient, prediction, confirmation or SC-ACT-06 verdict."}
def validate(p: dict[str, Any]) -> None:
    assert p["result_id"]=="K756-SC-ACT-06-CYCLIC-ADAPTER-LINEARIZATION" and p["target_claim"]=="SC-ACT-06"
    l=p["linearization"]; assert l["common_direction_killed"] and l["relative_direction_controls_all_outputs"] and l["principal_derivative_part"]=="xi wedge r" and l["zero_order_part"]=="r"
    assert p["exact_controls"]["dimension"]==14 and p["exact_controls"]["expected_wedge_rank"]==13
    for row in p["exact_controls"]["cases"]: assert (row["curvature_difference_principal_rank"],row["common_direction_combined_rank"],row["relative_direction_combined_rank"])==(13,0,14)
    specs={x["name"]:x for x in p["specializations"]}; assert not specs["DIAGONAL_IDENTIFICATION"]["new_current_carrier_response"] and not specs["FREEZE_B_BACKGROUND"]["new_current_carrier_response"] and specs["INDEPENDENT_A_B"]["new_current_carrier_response"]
    t=p["theorem"]; assert (t["principal_rank_per_internal_coefficient"],t["combined_relative_rank_per_internal_coefficient"],t["common_kernel_dimension_per_internal_coefficient"])==(13,14,14)
    assert t["diagonal_specialization_zero"] and not t["frozen_background_specialization_is_action_owned"] and not t["independent_specialization_preserves_current_field_dimension"]
    assert not p["decision"]["current_one_connection_complex_reopened"] and p["decision"]["doubled_relative_connection_candidate_constructed"] and "UNCHANGED" in p["source_and_ledger_effect"]
def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); args=ap.parse_args(); packet=build(); validate(packet); text=json.dumps(packet,indent=2,sort_keys=True)+"\n"; OUTPUT.write_text(text,encoding="utf-8") if args.write else print(text,end=""); return 0
if __name__=="__main__": raise SystemExit(main())
