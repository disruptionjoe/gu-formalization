#!/usr/bin/env python3
"""Hostile mutations for K1618's information and Gaussian scope."""
import json
from copy import deepcopy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def reject(d):
 q,z=d['information_rigidity'],d['decision']
 return ('I(M_N;M_N+G_N)=o(N^3)' in q['condition'] and 'Gaussian and common-covariance scoped' in q['scope_guard']
         and z['continuous_location_laws_admitted'] and not z['non_gaussian_components_controlled']
         and not z['protected_status_change'])
def main():
 d=json.loads((ROOT/'lab/process/k1618-continuous-location-information-rigidity.json').read_text());c=[('baseline',reject(d))]
 for name,key,x,y in [('drop condition','condition','I(M_N;M_N+G_N)=o(N^3)','finite information'),
                      ('drop Gaussian scope','scope_guard','Gaussian and common-covariance scoped','unrestricted')]:
  m=deepcopy(d);m['information_rigidity'][key]=m['information_rigidity'][key].replace(x,y);c.append((name,not reject(m)))
 for key in ('continuous_location_laws_admitted','non_gaussian_components_controlled','protected_status_change'):
  m=deepcopy(d);m['decision'][key]=not m['decision'][key];c.append((f'flip {key}',not reject(m)))
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
