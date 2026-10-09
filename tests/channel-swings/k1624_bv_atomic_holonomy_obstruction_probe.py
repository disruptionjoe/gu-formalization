#!/usr/bin/env python3
"""Hostile mutations for K1624's necessity-only BV theorem."""
import json
from copy import deepcopy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def reject(d):
 q,z=d["atomic_obstruction"],d["decision"]
 return ("not sufficient" in q["sharpness"] and "does not prove" in q["scope_guard"]
  and z["every_nonzero_derivative_atom_obstructs_L1"] and z["finite_jump_restriction_removed"]
  and not z["atom_free_is_sufficient"] and not z["electric_field_L1_proved"]
  and not z["source_owned_flow"] and not z["protected_status_change"])
def main():
 d=json.loads((ROOT/"lab/process/k1624-bv-atomic-holonomy-obstruction.json").read_text());checks=[("baseline",reject(d))]
 for name,key,x,y in [("promote sufficiency","sharpness","not sufficient","sufficient"),("promote flow","scope_guard","does not prove","proves")]:
  m=deepcopy(d);m["atomic_obstruction"][key]=m["atomic_obstruction"][key].replace(x,y);checks.append((name,not reject(m)))
 for key in ("every_nonzero_derivative_atom_obstructs_L1","finite_jump_restriction_removed","atom_free_is_sufficient","electric_field_L1_proved","source_owned_flow","protected_status_change"):
  m=deepcopy(d);m["decision"][key]=not m["decision"][key];checks.append((f"flip {key}",not reject(m)))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
