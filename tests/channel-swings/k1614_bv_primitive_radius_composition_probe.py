#!/usr/bin/env python3
"""Hostile mutations for K1614 conditional composition."""
import json
from copy import deepcopy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def reject(d):
 q,z=d['composition'],d['decision']
 return ('remains conditional' in q['scope_guard'] and not z['nonlinear_remainder_derived']
         and not z['source_owned_flow'] and not z['protected_status_change'])
def main():
 d=json.loads((ROOT/'lab/process/k1614-bv-primitive-radius-composition.json').read_text());c=[('baseline',reject(d))]
 m=deepcopy(d);m['composition']['scope_guard']=m['composition']['scope_guard'].replace('remains conditional','is unconditional');c.append(('unconditional',not reject(m)))
 for key in ('nonlinear_remainder_derived','source_owned_flow','protected_status_change'):
  m=deepcopy(d);m['decision'][key]=not m['decision'][key];c.append((f'flip {key}',not reject(m)))
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
