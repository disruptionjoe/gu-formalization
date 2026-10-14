#!/usr/bin/env python3
"""K1813: fixed-score sixth-order certificate on the first K1794 parent."""
import importlib.util,json,sys
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1813-full-fisher-slab-three-stationary-cover.json"
P=ROOT/"tests/channel-swings/k1807_full_fisher_anchored_score_compact_taylor.py";s=importlib.util.spec_from_file_location("k1807_for_k1813",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
m.ANCHOR_T=F(265664669701527,5000000000000000);m.ANCHOR_Z=F(8805034043103,15625000000000);m.THRESHOLD=F(1591786453049800,10**22);m.T_LO=F(887855469,17179869184);m.T_HI=F(14713917917,274877906944);m.Z_LO=F(73,128);m.Z_HI=F(293,512)
def compute():
 d=m.compute();return {k:d[k] for k in ("rectangle","anchor","threshold","compact_bounds","degree_six_remainder_bounds")}
def validate(d,got=None):
 got=compute() if got is None else got;c=d["certificate"]
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1813"),("inputs",d["inputs"]==["K1787","K1806","K1807"]),("exact replay",c==got),("A positive",c["compact_bounds"]["a_positive"]),("margin indeterminate",not c["compact_bounds"]["cross_margin_positive"]),("method limit",d["decision"]["sixth_order_parent_certificate_indeterminate"]),("global open",not d["decision"]["global_optimizer_proved"])]
def main():
 got=compute()
 if not ARTIFACT.exists() or "--print" in sys.argv:print(json.dumps(got,indent=2));return
 checks=validate(json.loads(ARTIFACT.read_text()),got)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
