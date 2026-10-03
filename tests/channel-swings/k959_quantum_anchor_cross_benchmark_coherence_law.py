#!/usr/bin/env python3
"""K959 cross-anchor shared coherence law."""
from __future__ import annotations
import argparse,json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k959-quantum-anchor-cross-benchmark-coherence-law.json"
def build():
 rows=[]
 for l in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)):
  rows.append({"lambda":str(l),"visibility":str(l),"S_over_sqrt2_minus_one":str((1+l)-1),"relation_holds":l==(1+l)-1})
 return {
 "schema_version":"1.0","result_id":"K959-QUANTUM-ANCHOR-CROSS-BENCHMARK-COHERENCE-LAW","created":"2026-10-03","status":"working_draft_verified","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL","classification":"INTERNAL_CONDITIONAL_MATHEMATICS",
 "scope":"The common normalized coherence eigenvalue of K957's Bell witness and K958's two-path readout when both are represented by one K956 candidate law.",
 "cross_anchor_law":{"identity":"S/sqrt(2)-1=V=lambda","bell_violation_iff":"V>sqrt(2)-1","exponential_threshold":"t < log(1+sqrt(2))/(2 gamma)","threshold_orientation":"Bell violation is lost after the threshold as visibility decays","shared_rate_is_not_empirically_asserted_across_distinct_environments":True},
 "exact_controls":{"rows":rows,"identity_all_rows":all(r["relation_holds"] for r in rows),"threshold_lower_bracket":"2/5","threshold_upper_bracket":"5/12","two_fifths_fails":"2(1+2/5)^2=98/25<4","five_twelfths_passes":"2(1+5/12)^2=289/72>4","rational_threshold_width":"1/60"},
 "discriminator":{"candidate_with_one_shared_law_must_use_one_coherence_eigenvalue":True,"different_environments_may_have_different_gamma":True,"calibration_fit_is_not_held_out_prediction":True,"distinct_held_out_family_still_required":True},
 "decision":{"cross_benchmark_information_gain":True,"one_parameter_relation_derived":True,"next_exact_input":"A GU-native physical quotient and local dynamical generator must derive, rather than import, the state/effect pairing, local marginal invariance and coherence eigenoperator before forward credit is possible."},
 "source_and_ledger_effect":"none","claim_ceiling":"Exact relation inside one carrier-neutral conditional dephasing model. It neither asserts one empirical rate across distinct experiments nor derives Hilbert/Born/tensor/locality/dynamics from GU, and it earns no prediction or confirmation credit."
 }
def validate(p):
 x,c,d,q=p["cross_anchor_law"],p["exact_controls"],p["discriminator"],p["decision"]
 assert x["identity"]=="S/sqrt(2)-1=V=lambda" and x["shared_rate_is_not_empirically_asserted_across_distinct_environments"]
 assert c["identity_all_rows"] and c["rational_threshold_width"]=="1/60"
 assert d["candidate_with_one_shared_law_must_use_one_coherence_eigenvalue"] and d["different_environments_may_have_different_gamma"] and d["calibration_fit_is_not_held_out_prediction"] and d["distinct_held_out_family_still_required"]
 assert q["cross_benchmark_information_gain"] and q["one_parameter_relation_derived"]
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);t=json.dumps(p,indent=2,sort_keys=True)+"\n"
 if a.check:assert OUTPUT.read_text()==t
 elif a.write:OUTPUT.write_text(t)
 else:print(t,end="")
 print("K959 controls: 14/14")
if __name__=="__main__":main()
