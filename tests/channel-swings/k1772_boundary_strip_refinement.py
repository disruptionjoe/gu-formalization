#!/usr/bin/env python3
"""Exact adaptive degree-seven refinement of K1769's lower strip."""
import importlib.util
import json
from hashlib import sha256
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
ARTIFACT=ROOT/"lab/process/k1772-boundary-strip-refinement.json"
SOURCE=ROOT/"tests/channel-swings/k1768_bernstein_sublevel_partition.py"
s=importlib.util.spec_from_file_location("k1768",SOURCE);k1768=importlib.util.module_from_spec(s);s.loader.exec_module(k1768)
BOUNDARY=(k1768.Q(11863283,536870912),k1768.Q(2026730637,68719476736),k1768.Q(0),k1768.Q(1,128))

def enc(x): return k1768.encode_fraction(x)

def replay():
    _,_,_,terms=k1768.threshold_polynomial(7)
    stack=[(BOUNDARY,0,0)];pruned=[];retained=[]
    while stack:
        box,dt,dz=stack.pop()
        lo,_=k1768.bernstein_bound(terms,(box[0],box[1]),(box[2],box[3]))
        if lo>0:
            pruned.append((box,lo));continue
        if dt==dz==16:
            retained.append(box);continue
        if dt<=dz and dt<16:
            mid=(box[0]+box[1])/2
            stack.extend([((box[0],mid,box[2],box[3]),dt+1,dz),((mid,box[1],box[2],box[3]),dt+1,dz)])
        else:
            mid=(box[2]+box[3])/2
            stack.extend([((box[0],box[1],box[2],mid),dt,dz+1),((box[0],box[1],mid,box[3]),dt,dz+1)])
    pruned.sort(key=lambda x:x[0]);retained.sort()
    rows=["P:"+":".join(enc(x) for x in b) for b,_ in pruned]+["R:"+":".join(enc(x) for x in b) for b in retained]
    hull=[min(b[i] for b in retained) if i%2==0 else max(b[i] for b in retained) for i in range(4)]
    return {
      "degree":7,"threshold":enc(k1768.UPPER),"local_depth_t":16,"local_depth_z":16,
      "input_boundary_strip":[enc(x) for x in BOUNDARY],"pruned_leaves":len(pruned),
      "retained_leaves":len(retained),"unresolved_leaves":0,
      "retained_cells":[[enc(x) for x in b] for b in retained],"retained_hull":[enc(x) for x in hull],
      "partition_digest":sha256("\n".join(rows).encode()).hexdigest(),
    }

def main():
    got=replay()
    if not ARTIFACT.exists() or "--print" in __import__("sys").argv: print(json.dumps(got,indent=2));return
    d=json.loads(ARTIFACT.read_text());z=d["decision"]
    checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1772"),("exact replay",d["refinement"]==got),("44 pruned",got["pruned_leaves"]==44),("two retained",got["retained_leaves"]==2),("zero unresolved",got["unresolved_leaves"]==0),("not Fisher",not z["full_fisher_exclusion_proved"]),("not optimizer",not z["global_optimizer_proved"])]
    for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
