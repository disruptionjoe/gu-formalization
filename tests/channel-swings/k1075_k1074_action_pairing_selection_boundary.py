#!/usr/bin/env python3
"""K1075: reconcile the action/pairing mass-selection boundary."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1075-k1074-action-pairing-selection-boundary.json"


def build():
    rows=[
        ("positive_mass_family","K1071","pass",False,False),
        ("fixed_common_pairing_obstruction","K1072","pass",False,False),
        ("pairing_ratio_selector","K1073","pass_conditional",False,False),
        ("multimode_affine_stiffness","K1074","pass_conditional",False,False),
        ("source_action_pairing","SC-ACT-01/02/06 and LT-SM8/LT-GR6b","open",False,False),
        ("measured_apparatus","K1070 open rows","open",False,False),
    ]
    return {
        "schema_version":"1.0","result_id":"K1075-K1074-ACTION-PAIRING-SELECTION-BOUNDARY","status":"working_draft_verified","created":"2026-10-04",
        "requirements":[{"id":i,"evidence":e,"candidate_grade":g,"gu_source_owned":o,"scorable":s} for i,e,g,o,s in rows],
        "counts":{"mathematical_pass_or_conditional":4,"gu_source_owned":0,"scorable":0,"open_physical_or_source":2},
        "selection_result":"structural compatibility admits every positive mass when its energy pairing is rebuilt with that mass; one independently fixed positive pairing selects at most one coefficient",
        "circularity_result":"the K1037 mass-dependent energy form cannot be reused as independent selection evidence",
        "source_scope":{"SC-ACT-01":"ASSERTS","SC-ACT-02":"ASSERTS","SC-ACT-06":"ASSERTS","SC-META-53":"UNCERTAIN"},
        "ledger_effect":"none -- LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "next_condition":"supply a source/action-owned positive functional pairing or Hessian with common mode normalization; verify its affine stiffness law and read the mass intercept before composing the measured apparatus",
        "target_claim":"NONE-NOT-A-KILL",
    }


def validate(d):
    rows=d["requirements"]
    assert len(rows)==6 and len({r["id"] for r in rows})==6
    assert sum(r["candidate_grade"].startswith("pass") for r in rows)==4
    assert all(r["gu_source_owned"] is False and r["scorable"] is False for r in rows)
    assert d["counts"]=={"mathematical_pass_or_conditional":4,"gu_source_owned":0,"scorable":0,"open_physical_or_source":2}
    assert "admits every positive mass" in d["selection_result"] and "selects at most one" in d["selection_result"]
    assert "cannot be reused" in d["circularity_result"]
    assert d["source_scope"]=={"SC-ACT-01":"ASSERTS","SC-ACT-02":"ASSERTS","SC-ACT-06":"ASSERTS","SC-META-53":"UNCERTAIN"}
    assert d["ledger_effect"].startswith("none") and d["ledger_effect"].endswith("NEEDS")
    assert "source/action-owned positive functional pairing" in d["next_condition"]
    assert d["target_claim"]=="NONE-NOT-A-KILL"


if __name__=="__main__":
    data=build(); validate(data); OUTPUT.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n"); print("K1075 controls: 9/9")
