#!/usr/bin/env python3
"""Hostile mutations for K1619's endpoint and nonlinear scope."""
import json
from copy import deepcopy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def reject(d):
 q,z=d['endpoint_obstruction'],d['decision']
 return ('every nonzero merged endpoint-jump vector' in q['obstruction'] and 'does not derive' in q['scope_guard']
         and z['nonzero_endpoint_jump_obstructs_holonomy_L1'] and not z['distinct_jump_cancellation_can_restore_L1']
         and not z['electric_field_L1_proved'] and not z['source_owned_flow'] and not z['protected_status_change'])
def main():
 d=json.loads((ROOT/'lab/process/k1619-endpoint-jump-holonomy-obstruction.json').read_text());c=[('baseline',reject(d))]
 for name,key,x,y in [('allow cancellation','obstruction','every nonzero merged endpoint-jump vector','generic endpoint jumps'),
                      ('promote flow','scope_guard','does not derive','derives')]:
  m=deepcopy(d);m['endpoint_obstruction'][key]=m['endpoint_obstruction'][key].replace(x,y);c.append((name,not reject(m)))
 for key in ('nonzero_endpoint_jump_obstructs_holonomy_L1','distinct_jump_cancellation_can_restore_L1','electric_field_L1_proved','source_owned_flow','protected_status_change'):
  m=deepcopy(d);m['decision'][key]=not m['decision'][key];c.append((f'flip {key}',not reject(m)))
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
