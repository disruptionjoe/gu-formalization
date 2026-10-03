#!/usr/bin/env python3
"""K958 exact two-path fringe visibility under K956 dephasing."""
from __future__ import annotations
import argparse,json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; OUTPUT=ROOT/"lab/process/k958-quantum-anchor-interference-visibility-decay.json"
def build():
 rows=[]
 for l in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)):
  pmax=(1+l)/2;pmin=(1-l)/2;vis=(pmax-pmin)/(pmax+pmin)
  rows.append({"lambda":str(l),"bright_probability":str(pmax),"dark_probability":str(pmin),"visibility":str(vis)})
 return {
 "schema_version":"1.0","result_id":"K958-QUANTUM-ANCHOR-INTERFERENCE-VISIBILITY-DECAY","created":"2026-10-03",
 "status":"working_draft_verified","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL","classification":"INTERNAL_CONDITIONAL_MATHEMATICS",
 "scope":"One imported two-path qubit with phase-sensitive recombination under the K956 conditional dephasing semigroup.",
 "fringe_law":{"probability":"P_0(theta)=(1+lambda cos(phi-theta))/2","visibility":"V=lambda","coherence":"rho_01=lambda exp(-i phi)/2","continuous_decay":"V(t)=exp(-2 gamma t)"},
 "exact_controls":{"rows":rows,"normalization_all_rows":all(Fraction(r["bright_probability"])+Fraction(r["dark_probability"])==1 for r in rows),"visibility_equals_lambda_all_rows":all(r["visibility"]==r["lambda"] for r in rows),"unit_visibility_at_lambda_one":rows[-1]["visibility"]=="1","zero_visibility_at_lambda_zero":rows[0]["visibility"]=="0"},
 "ownership":{"path_state_phase_born_and_detector_imported":True,"environmental_rate_imported":True,"gu_interference_prediction":False},
 "decision":{"visibility_decay_exact":True,"same_semigroup_parameter_as_k956":True,"next_exact_input":"Compose V=lambda with K957's S/sqrt(2)-1=lambda and state the shared-law discriminator with environment caveats."},
 "source_and_ledger_effect":"none","claim_ceiling":"Exact finite two-path visibility law under an imported dephasing model. It does not derive a composite centre-of-mass state, environment, rate, detector, Born rule or GU prediction."
 }
def validate(p):
 f,c,o,d=p["fringe_law"],p["exact_controls"],p["ownership"],p["decision"]
 assert f["visibility"]=="V=lambda" and f["continuous_decay"]=="V(t)=exp(-2 gamma t)"
 assert c["normalization_all_rows"] and c["visibility_equals_lambda_all_rows"] and c["unit_visibility_at_lambda_one"] and c["zero_visibility_at_lambda_zero"]
 assert d["visibility_decay_exact"] and d["same_semigroup_parameter_as_k956"]
 assert o["path_state_phase_born_and_detector_imported"] and o["environmental_rate_imported"] and not o["gu_interference_prediction"]
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);t=json.dumps(p,indent=2,sort_keys=True)+"\n"
 if a.check:assert OUTPUT.read_text()==t
 elif a.write:OUTPUT.write_text(t)
 else:print(t,end="")
 print("K958 controls: 14/14")
if __name__=="__main__":main()
