#!/usr/bin/env python3
"""Hostile mutations for K1616's shared-channel scope."""
import json
from copy import deepcopy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def reject(d):
 q,z=d['mmse_control'],d['decision']
 return ('One common Gaussian covariance is load-bearing' in q['scope_guard'] and 'D_N/4<=(Lambda_N/2)I(M_N;X_N)' in q['bound']
         and z['mutual_information_bound'] and not z['varying_covariance_controlled']
         and not z['unrestricted_state_theorem'] and not z['protected_status_change'])
def main():
 d=json.loads((ROOT/'lab/process/k1616-common-covariance-mmse-control.json').read_text());c=[('baseline',reject(d))]
 muts=[('drop common covariance',('mmse_control','scope_guard','One common Gaussian covariance is load-bearing','Covariance may vary by label')),
       ('drop information factor',('mmse_control','bound','(Lambda_N/2)I(M_N;X_N)','Lambda_N/2'))]
 for name,(a,b,x,y) in muts:
  m=deepcopy(d);m[a][b]=m[a][b].replace(x,y);c.append((name,not reject(m)))
 for key in ('mutual_information_bound','varying_covariance_controlled','unrestricted_state_theorem','protected_status_change'):
  m=deepcopy(d);m['decision'][key]=not m['decision'][key];c.append((f'flip {key}',not reject(m)))
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
