#!/usr/bin/env python3
"""Hostile mutations for K1613's BV and endpoint scope."""
import json
from copy import deepcopy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def reject(d):
 q,z=d['bv_primitive'],d['decision']
 return ('Density endpoint jumps are not allowed' in q['scope_guard'] and not z['density_endpoint_jumps_allowed']
         and not z['electric_field_L1'] and not z['source_owned_flow'] and z['holonomy_L1'] and z['holonomy_L2'])
def main():
 d=json.loads((ROOT/'lab/process/k1613-bv-spectral-primitive-budget.json').read_text());c=[('baseline',reject(d))]
 m=deepcopy(d);m['bv_primitive']['scope_guard']=m['bv_primitive']['scope_guard'].replace('not allowed','allowed');c.append(('density jump',not reject(m)))
 for key in ('density_endpoint_jumps_allowed','electric_field_L1','source_owned_flow','holonomy_L1','holonomy_L2'):
  m=deepcopy(d);m['decision'][key]=not m['decision'][key];c.append((f'flip {key}',not reject(m)))
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
