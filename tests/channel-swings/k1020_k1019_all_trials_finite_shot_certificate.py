#!/usr/bin/env python3
"""K1020: finite-shot CHSH certificate after all-trials no-click assignment."""
import json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1020-k1019-all-trials-finite-shot-certificate.json"

def build():
    p=1.; v=.4; eta=.98; alpha=.05
    half=eta*eta*math.sqrt(p*p+v*v)+(1-eta)**2
    win=.5+half/4
    margin=win-.75
    n=math.floor(math.log(1/alpha)/(2*margin*margin))+1
    return {"schema_version":"1.0","result_id":"K1020-K1019-ALL-TRIALS-FINITE-SHOT-CERTIFICATE","status":"working_draft_verified","created":"2026-10-04",
      "protocol":"herald every trial before settings; assign every no-click locally to +1; retain every trial",
      "certificate":"w_hat>3/4+sqrt(log(1/alpha)/(2n))",
      "memory_scope":"arbitrary inter-trial device memory under fresh uniform settings independent of the devices",
      "forecast_model":"K1018 independent setting-independent equal-efficiency loss model",
      "frozen_point":{"p":"1","V":"2/5","eta":"49/50","alpha":"1/20","half_chsh":half,"win_rate":win,"margin":margin,"n_total":n,"penalty_at_n":math.sqrt(math.log(1/alpha)/(2*n)),"penalty_at_n_minus_one":math.sqrt(math.log(1/alpha)/(2*(n-1)))},
      "inference_boundary":"the empirical all-trials win-rate certificate itself needs no fair-sampling assumption; the 19,810-trial forecast does",
      "unowned_assumptions":["event-ready heralding","fresh measurement-independent settings","spacelike locality","fixed binary outcome convention","independent-loss forecast","complete systematic budget"],
      "ownership":{"gu_protocol_constructed":False,"loophole_free_experiment_claimed":False},"target_claim":"NONE-NOT-A-KILL"}

def validate(d):
    assert "retain every trial" in d["protocol"]
    assert d["certificate"].startswith("w_hat>3/4+")
    assert "arbitrary inter-trial" in d["memory_scope"]
    assert "independent setting-independent" in d["forecast_model"]
    assert d["frozen_point"]["n_total"]==19810
    assert d["frozen_point"]["margin"]>d["frozen_point"]["penalty_at_n"]
    assert d["frozen_point"]["margin"]<=d["frozen_point"]["penalty_at_n_minus_one"]
    assert d["frozen_point"]["eta"]=="49/50"
    assert "needs no fair-sampling assumption" in d["inference_boundary"]
    assert len(d["unowned_assumptions"])==6
    assert d["ownership"]["gu_protocol_constructed"] is False
    assert d["ownership"]["loophole_free_experiment_claimed"] is False
    assert d["target_claim"]=="NONE-NOT-A-KILL"

if __name__=="__main__":
    d=build(); validate(d); OUTPUT.write_text(json.dumps(d,indent=2,sort_keys=True)+"\n"); print("K1020 controls: 13/13")
