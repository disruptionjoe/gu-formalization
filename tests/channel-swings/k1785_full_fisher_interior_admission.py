#!/usr/bin/env python3
"""Validate K1785's scope-preserving interior admission packet."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1785-full-fisher-interior-admission.json"
def validate(d):
 c=d["bridge_census"];p=d["protected_state"];e=d["entry_state"];z=d["decision"]
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1785"),("inputs",d["inputs"]==["K1780","K1781","K1782","K1783","K1784"]),("census",c=={"total":485,"satisfied":406,"conditional":10,"excluded":65,"missing":4}),("partition",sum(c[k] for k in ("satisfied","conditional","excluded","missing"))==c["total"]),("protected",all(v is False for k,v in p.items() if k.endswith("_changed"))),("compact jet",e["compact_window_second_order_jet_available"]),("chain finite",e["three_slab_chart_chain_rule_finite"]),("pilot",e["directed_slab_pilot_available"]),("locator",e["slab_three_rational_locator_available"]),("tail open",not e["whole_line_parameter_jet_available"]),("Newton open",not e["three_slab_interval_newton_completed"]),("slabs open",not z["slabs_one_and_two_excluded"]),("stationary open",not z["stationary_box_isolated"]),("global open",not z["global_optimizer_proved"]),("physical fenced",not z["source_owned_physical_theory"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
