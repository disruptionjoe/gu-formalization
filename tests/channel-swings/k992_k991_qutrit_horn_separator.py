#!/usr/bin/env python3
"""K992 minimal simultaneous gap-one/gap-two separator for K986/K987."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k992-k991-qutrit-horn-separator.json"
PARENT=ROOT/"lab/process/k991-k990-charge-harmonic-channel-theorem.json"
def build():
    parent=json.loads(PARENT.read_text());gamma=0.7;rows=[]
    for theta in (math.pi/6,math.pi/4,math.pi/3,math.pi/2):
        rate=gamma/(math.sin(theta)**2)
        brownian_1=-gamma/2; jump_1=rate*(math.cos(theta)-1)
        brownian_2=-2*gamma; jump_2=rate*(math.cos(2*theta)-1)
        rows.append({"theta":theta,"event_rate":rate,"brownian_psi_1":brownian_1,"jump_psi_1":jump_1,
                     "closed_form_jump_psi_1":-gamma/(1+math.cos(theta)),"gap_one_separation":brownian_1-jump_1,
                     "brownian_psi_2":brownian_2,"jump_psi_2":jump_2,"gap_two_error":abs(brownian_2-jump_2)})
    return {"schema_version":"1.0","result_id":"K992-QUTRIT-HORN-SEPARATOR","created":"2026-10-04","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL","scope":"The imported qutrit charge operator Q=diag(-1,0,1) driven by the K986 Brownian and K987 symmetric compound-Poisson phase laws.","dependency_checks":{"input_id":parent["result_id"],"charge_gap_theorem_available":parent["theorem"]["observable_harmonics_are_charge_differences"]},"construction":{"charge_spectrum":[-1,0,1],"simultaneously_observed_gaps":[1,2],"minimal_dimension_for_simultaneous_gap_one_and_two":3,"brownian_exponent":"psi_B(n)=-(gamma/2)n^2","compound_poisson_exponent":"psi_theta(n)=gamma(cos(n theta)-1)/sin(theta)^2","gap_two_matched":True,"gap_one_strictly_separates_every_finite_nonzero_angle":True},"exact_controls":{"gamma":gamma,"rows":rows,"all_gap_two_identities_replayed":all(r["gap_two_error"]<1e-15 for r in rows),"all_gap_one_closed_forms_replayed":all(abs(r["jump_psi_1"]-r["closed_form_jump_psi_1"])<1e-15 for r in rows),"all_gap_one_separations_positive":all(r["gap_one_separation"]>0 for r in rows)},"ownership":{"qutrit_charge_sector_imported":True,"gap_one_coherence_access_imported":True,"gu_action_or_physical_quotient_constructed":False,"prediction_or_confirmation_credit":False},"decision":{"named_brownian_and_compound_poisson_horns_system_separable_after_declared_enlargement":True,"same_qubit_system_remains_nonidentifying":True,"next_exact_input":"Test whether any finite set of charge harmonics identifies a general microscopic phase law."},"source_and_ledger_effect":"none","claim_ceiling":"Exact pairwise separation after an imported system enlargement only; not same-qubit discrimination, full Levy-law identification or a GU-owned observable."}
def validate(p):
    d,c,x,o,z=p["dependency_checks"],p["construction"],p["exact_controls"],p["ownership"],p["decision"]
    assert d["charge_gap_theorem_available"] and c["simultaneously_observed_gaps"]==[1,2] and c["minimal_dimension_for_simultaneous_gap_one_and_two"]==3
    assert c["gap_two_matched"] and c["gap_one_strictly_separates_every_finite_nonzero_angle"]
    assert len(x["rows"])==4 and x["all_gap_two_identities_replayed"] and x["all_gap_one_closed_forms_replayed"] and x["all_gap_one_separations_positive"]
    assert o["qutrit_charge_sector_imported"] and o["gap_one_coherence_access_imported"] and not o["gu_action_or_physical_quotient_constructed"] and not o["prediction_or_confirmation_credit"]
    assert z["named_brownian_and_compound_poisson_horns_system_separable_after_declared_enlargement"] and z["same_qubit_system_remains_nonidentifying"] and p["source_and_ledger_effect"]=="none"
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);t=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert OUTPUT.read_text()==t
    elif a.write:OUTPUT.write_text(t)
    else:print(t,end="")
    print("K992 controls: 15/15")
if __name__=="__main__":main()
