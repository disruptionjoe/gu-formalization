#!/usr/bin/env python3
"""Hostile mutations for K1612's effective-count and scope limits."""
import json
from copy import deepcopy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def reject(d):
 q,z=d['renyi_rigidity'],d['decision']
 return ('o(N^3)' in q['coefficient'] and 'Critical or supercritical effective count' in q['scope_guard']
         and z['renyi_half_subcubic_required'] and not z['critical_effective_count_closed']
         and not z['unrestricted_leading_coefficient_identified'] and not z['protected_status_change'])
def main():
 d=json.loads((ROOT/'lab/process/k1612-growing-mixture-renyi-rigidity.json').read_text());c=[('baseline',reject(d))]
 for name,a,b,x,y in [('weaken rate','renyi_rigidity','coefficient','o(N^3)','O(N^3)'),
                     ('erase critical','renyi_rigidity','scope_guard','Critical or supercritical effective count','No effective-count regime')]:
  m=deepcopy(d);m[a][b]=m[a][b].replace(x,y);c.append((name,not reject(m)))
 for key in ('renyi_half_subcubic_required','critical_effective_count_closed','unrestricted_leading_coefficient_identified','protected_status_change'):
  m=deepcopy(d);m['decision'][key]=not m['decision'][key];c.append((f'flip {key}',not reject(m)))
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
