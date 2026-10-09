#!/usr/bin/env python3
"""Hostile mutations for K1617's entropy and covariance scope."""
import json
from copy import deepcopy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def reject(d):
 q,z=d['entropy_rigidity'],d['decision']
 return ('H(p_N)=o(N^3)' in q['coefficient'] and 'one common covariance' in q['comparison']
         and z['shannon_subextensive_sufficient'] and not z['k1612_heterogeneous_critical_regime_closed']
         and not z['unrestricted_leading_coefficient_identified'] and not z['protected_status_change'])
def main():
 d=json.loads((ROOT/'lab/process/k1617-shannon-entropy-mixture-rigidity.json').read_text());c=[('baseline',reject(d))]
 for name,key,x,y in [('drop entropy condition','coefficient','H(p_N)=o(N^3)','H(p_N) arbitrary'),
                      ('drop common covariance','comparison','one common covariance','all covariances')]:
  m=deepcopy(d);m['entropy_rigidity'][key]=m['entropy_rigidity'][key].replace(x,y);c.append((name,not reject(m)))
 for key in ('shannon_subextensive_sufficient','k1612_heterogeneous_critical_regime_closed','unrestricted_leading_coefficient_identified','protected_status_change'):
  m=deepcopy(d);m['decision'][key]=not m['decision'][key];c.append((f'flip {key}',not reject(m)))
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
