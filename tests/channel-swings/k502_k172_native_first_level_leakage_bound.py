#!/usr/bin/env python3
"""K502 native first-bath-level K500 leakage upper bounds from K170/K172."""
from __future__ import annotations
import argparse, importlib.util, json, sys
from fractions import Fraction
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
OUTPUT=ROOT/"lab/process/k502-k172-native-first-level-leakage-bound.json"
def load(name,file):
 s=importlib.util.spec_from_file_location(name,HERE/file);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
K170=load("k170_for_k502","k170_direct_gram_reference_shape_slice.py")
K172=load("k172_for_k502","k172_continuum_first_block_graph_tail.py")
K501=load("k501_for_k502","k501_k500_rank_one_leakage_variance.py")
def qstr(x:Fraction)->str:return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"

def sector(seed:str)->dict[str,Any]:
 block=K172.first_block(seed)
 h_lower=Fraction(block["profile_norm_interval"][0])
 multiplicity=int(block["normal_ordered_self_energy_multiplicity_per_component"])
 correction=Fraction(block["D_h_norm_upper_used"])
 bound=multiplicity*correction/h_lower
 if not h_lower>0 or not bound>0:raise AssertionError("native first-level bound left its positive branch")
 return {"seed":seed,"charge":block["charge"],"bath_level":1,"cyclic_level_vector":"v_1=G_256 phi","components":block["n1_transition_components"],"normal_multiplier":f"256-{multiplicity}*D_256(omega(p))","scalar_256_contributes_to_leakage":False,"profile_norm_lower":qstr(h_lower),"D_h_norm_upper":qstr(correction),"D_multiplicity":multiplicity,"normal_leakage_norm_upper":qstr(bound),"derivation":"K501 scalar-shift invariance and orthogonal-residual contraction give leakage <=m*||D_256 h||/||h||; identical orthogonal components cancel from the ratio","uniform_all_level_bound":False}

def build()->dict[str,Any]:
 rows=[sector("vacuum"),sector("one_impurity")]
 return {"schema_version":"1.0","result_id":"K502-K172-NATIVE-FIRST-LEVEL-LEAKAGE-BOUND","created":"2026-09-25","status":"working_draft_verified","classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL","scope":"The actual bath-number-one blocks generated from the K162 q00 vacuum and q10 one-impurity zero-bath seeds in the fixed K139 chart.","premises":{"rank_one_identity":"K501-K500-RANK-ONE-LEAKAGE-VARIANCE","word_norm":"K170 exact outward continuum point-profile interval","normal_action":"K172 exact W_1 g_1=(256-m D_256)h block","correction_norm":"K172 rigorous ||D_256 h||<=1/16"},"native_sector_bounds":rows,"decision":{"actual_native_level_evaluated":True,"q00_and_q10_first_level_leakage_finite":True,"complete_K500_uniform_leakage_emitted":False,"noncyclic_floor_emitted":False,"K473_released":False,"next_exact_input":"Produce a uniform normalized all-level variance bound, or native lower word norms sufficient to divide the held absolute action-orbit tails; separately bound the noncyclic compressed-form floor."},"source_and_ledger_effect":"none","claim_ceiling":"Rigorous native upper bounds on the bath-number-one leakage only. They do not control the supremum over all levels, the noncyclic floor, K473 beta, K152 interval, source, ledger, canon, paper, public or physical conclusions."}

def main():
 p=argparse.ArgumentParser();p.add_argument("--write",action="store_true");a=p.parse_args();d=build()
 if a.write:OUTPUT.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
 else:print(json.dumps(d,indent=2,sort_keys=True))
 return 0
if __name__=="__main__":raise SystemExit(main())
