#!/usr/bin/env python3
"""K1025: compose detector, setting-TV, record-error and finite-shot budgets."""
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1025-k1024-composed-loophole-budget.json"


def build():
    p=1.; v=.4; eta=.98; epsilon=.001; record_rate=.001; alpha=.05
    half=eta*eta*math.sqrt(p*p+v*v)+(1-eta)**2
    win=.5+half/4
    effective_margin=win-.75-epsilon-record_rate
    n=math.floor(math.log(1/alpha)/(2*effective_margin*effective_margin))+1
    return {"schema_version":"1.0","result_id":"K1025-K1024-COMPOSED-LOOPHOLE-BUDGET","status":"working_draft_verified","created":"2026-10-04",
      "certificate":"w_hat_recorded>3/4+epsilon+R/n+sqrt(log(1/alpha)/(2n))",
      "forecast_model":"K1018 independent equal-efficiency loss plus K1021 conditional setting-TV bound plus K1024 deterministic record budget",
      "frozen_point":{"p":"1","V":"2/5","eta":"49/50","epsilon":"1/1000","record_rate":"1/1000","alpha":"1/20","half_chsh":half,"expected_win_rate":win,"effective_margin":effective_margin,"n_total":n,"penalty_at_n":math.sqrt(math.log(1/alpha)/(2*n)),"penalty_at_n_minus_one":math.sqrt(math.log(1/alpha)/(2*(n-1)))},
      "feasibility_condition":"expected_win_rate>3/4+epsilon+record_rate",
      "inference_boundary":"an empirical certificate may use audited bounds directly; the 33,412-trial number is only a forecast under the imported loss, setting-TV and record-rate model",
      "remaining_unowned_packet":["positive state/effect pairing","action-owned preparation and generator","pre-settings physical herald","fresh setting source and independence proof","commuting local observables","spacelike locality","detector response calibration","audited complete systematic-error budget"],
      "ownership":{"gu_protocol_constructed":False,"loophole_free_experiment_claimed":False},"target_claim":"NONE-NOT-A-KILL"}


def validate(d):
    assert "+epsilon+R/n+" in d["certificate"]
    assert "K1018" in d["forecast_model"] and "K1021" in d["forecast_model"] and "K1024" in d["forecast_model"]
    e=d["frozen_point"]
    assert e["n_total"]==33412
    assert e["effective_margin"]>e["penalty_at_n"]
    assert e["effective_margin"]<=e["penalty_at_n_minus_one"]
    assert e["epsilon"]=="1/1000" and e["record_rate"]=="1/1000"
    assert "expected_win_rate>" in d["feasibility_condition"]
    assert "only a forecast" in d["inference_boundary"]
    assert len(d["remaining_unowned_packet"])==8
    assert d["ownership"]["gu_protocol_constructed"] is False
    assert d["ownership"]["loophole_free_experiment_claimed"] is False
    assert d["target_claim"]=="NONE-NOT-A-KILL"


if __name__=="__main__":
    d=build(); validate(d)
    OUTPUT.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n")
    print("K1025 controls: 11/11")
