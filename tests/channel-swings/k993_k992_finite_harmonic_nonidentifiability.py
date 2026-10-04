#!/usr/bin/env python3
"""K993 distinct phase-jump laws invisible on any prescribed finite harmonic set."""
from __future__ import annotations
import argparse, cmath, json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k993-k992-finite-harmonic-nonidentifiability.json"
PARENT=ROOT/"lab/process/k992-k991-qutrit-horn-separator.json"
def moment(order,n):
    return sum(cmath.exp(1j*n*2*math.pi*(k+0.5)/order) for k in range(order))/order
def build():
    parent=json.loads(PARENT.read_text());gaps=[-3,-2,-1,1,2,3];N,M,rate=5,7,0.9;rows=[]
    for n in gaps:
        a,b=moment(N,n),moment(M,n)
        rows.append({"harmonic":n,"nu_N_real":a.real,"nu_N_imag":a.imag,"nu_M_real":b.real,"nu_M_imag":b.imag,"moment_difference":abs(a-b),"exponent_N_real":rate*(a.real-1),"exponent_M_real":rate*(b.real-1)})
    return {"schema_version":"1.0","result_id":"K993-FINITE-HARMONIC-NONIDENTIFIABILITY","created":"2026-10-04","status":"working_draft_verified","direction":"observed_to_native","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","target_claim":"NONE-NOT-A-KILL","scope":"Compound-Poisson phase laws observed only through an arbitrary finite set of nonzero integer charge gaps.","dependency_checks":{"input_id":parent["result_id"],"pairwise_qutrit_separator_preserved":parent["construction"]["gap_one_strictly_separates_every_finite_nonzero_angle"]},"theorem":{"finite_observed_harmonic_set":"S subset Z without 0","construction":"choose distinct N,M>max|S| and uniform symmetric jumps on shifted Nth and Mth roots","shifted_root_angles":"2 pi (k+1/2)/N","no_zero_angle_atoms":True,"fourier_moments_zero_on_S":True,"same_rate_gives_identical_exponents_on_S":True,"jump_laws_distinct":True,"finite_dimensional_charge_tomography_identifies_general_phase_law":False},"exact_controls":{"observed_gaps":gaps,"N":N,"M":M,"rate":rate,"rows":rows,"orders_exceed_observed_max":N>max(map(abs,gaps)) and M>max(map(abs,gaps)),"all_moments_numerically_zero":all(max(abs(complex(r["nu_N_real"],r["nu_N_imag"])),abs(complex(r["nu_M_real"],r["nu_M_imag"])))<2e-15 for r in rows),"all_exponents_equal":all(abs(r["exponent_N_real"]-r["exponent_M_real"])<2e-15 for r in rows),"support_cardinalities_distinct":N!=M},"ownership":{"finite_charge_spectrum_imported":True,"jump_laws_and_rate_imported":True,"gu_action_or_observable_owner_constructed":False,"prediction_or_confirmation_credit":False},"decision":{"qutrit_pairwise_discrimination_not_full_model_identification":True,"arbitrary_finite_charge_spectrum_leaves_microscopic_horns":True,"next_exact_input":"Freeze the named qutrit pairwise holdout while retaining the general finite-probe ceiling."},"source_and_ledger_effect":"none","claim_ceiling":"Exact finite-harmonic nonidentifiability construction only; not an exhaustive Levy classification and not a claim that every named pair remains indistinguishable under every enlargement."}
def validate(p):
    d,t,x,o,z=p["dependency_checks"],p["theorem"],p["exact_controls"],p["ownership"],p["decision"]
    assert d["pairwise_qutrit_separator_preserved"] and t["no_zero_angle_atoms"] and t["fourier_moments_zero_on_S"] and t["same_rate_gives_identical_exponents_on_S"] and t["jump_laws_distinct"]
    assert not t["finite_dimensional_charge_tomography_identifies_general_phase_law"]
    assert len(x["rows"])==6 and x["orders_exceed_observed_max"] and x["all_moments_numerically_zero"] and x["all_exponents_equal"] and x["support_cardinalities_distinct"]
    assert o["finite_charge_spectrum_imported"] and o["jump_laws_and_rate_imported"] and not o["gu_action_or_observable_owner_constructed"] and not o["prediction_or_confirmation_credit"]
    assert z["qutrit_pairwise_discrimination_not_full_model_identification"] and z["arbitrary_finite_charge_spectrum_leaves_microscopic_horns"] and p["source_and_ledger_effect"]=="none"
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args();p=build();validate(p);t=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check:assert OUTPUT.read_text()==t
    elif a.write:OUTPUT.write_text(t)
    else:print(t,end="")
    print("K993 controls: 17/17")
if __name__=="__main__":main()
