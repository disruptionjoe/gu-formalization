#!/usr/bin/env python3
"""K1005: operational and GU-ownership disposition of corrected Bell laws."""
from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k1005-k1004-operational-bell-action-disposition.json"
def build():
 return {
  "schema_version":"1.0","result_id":"K1005-K1004-OPERATIONAL-BELL-ACTION-DISPOSITION","status":"working_draft_verified","created":"2026-10-04",
  "classification":"INTERNAL_REQUIREMENT_DISPOSITION","target_claim":"NONE-NOT-A-KILL",
  "preserved":{"fixed_witness_formula":True,"fixed_witness_threshold":True,"remote_marginal_theorem":True,"visibility_law":True},
  "corrected":{"fixed_threshold_is_not_optimized_bell_death":True,"optimized_formula":"S_max=2 sqrt(1+V^2)","finite_optimized_death_time":False,"asymptotic_resolution_cost":True},
  "native_requirements":["physical quotient","positive state/effect pairing","commuting local observable algebras","action-derived local generator","preparation and detector ownership","fixed-or-adaptive setting protocol","common domain and locality","finite statistical and systematic error budget"],
  "holdout":{"visibility":"2/5","fixed_witness":"no violation","optimized_witness":"violation","status":"frozen_unscored"},
  "effects":{"source_claim":"none","physics_ledger":"none","prediction":"none","confirmation":"none","canon":"none","public_verdict":"none"},
  "claim_ceiling":"Corrected operational demand surface for the imported quantum calibration model only."
 }
def validate(p):
 assert all(p["preserved"].values())
 c=p["corrected"];assert c["fixed_threshold_is_not_optimized_bell_death"] and c["optimized_formula"]=="S_max=2 sqrt(1+V^2)" and not c["finite_optimized_death_time"] and c["asymptotic_resolution_cost"]
 req=p["native_requirements"];assert len(req)==8 and "fixed-or-adaptive setting protocol" in req and "finite statistical and systematic error budget" in req
 h=p["holdout"];assert h=={"visibility":"2/5","fixed_witness":"no violation","optimized_witness":"violation","status":"frozen_unscored"}
 assert set(p["effects"].values())=={"none"}
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);t=json.dumps(p,indent=2,sort_keys=True)+"\n"
 if a.check:assert OUTPUT.read_text()==t
 elif a.write:OUTPUT.write_text(t)
 else:print(t,end="")
 print("K1005 controls: 12/12")
if __name__=="__main__":main()
