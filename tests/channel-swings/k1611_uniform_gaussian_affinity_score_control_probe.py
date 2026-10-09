#!/usr/bin/env python3
"""Hostile mutations for K1611 scope and structure."""
import json
from copy import deepcopy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def reject(d):
 q,z=d['uniform_pair_control'],d['decision']
 return ('fixed relative band' in q['scope_guard'] and 'stationary diagonal Gaussian' in q['scope_guard']
         and 'X_ij exp(-X_ij)' in q['uniform_bound'] and z['pair_affinity_score_O_N']
         and not z['unrestricted_state_theorem'] and not z['protected_status_change'])
def main():
 d=json.loads((ROOT/'lab/process/k1611-uniform-gaussian-affinity-score-control.json').read_text()); c=[('baseline',reject(d))]
 muts=[('drop band',('uniform_pair_control','scope_guard','fixed relative band','arbitrary covariance class')),
       ('drop diagonal',('uniform_pair_control','scope_guard','stationary diagonal Gaussian','all Gaussian')),
       ('drop xexp',('uniform_pair_control','uniform_bound','X_ij exp(-X_ij)','X_ij'))]
 for name,(a,b,x,y) in muts:
  m=deepcopy(d);m[a][b]=m[a][b].replace(x,y);c.append((name,not reject(m)))
 for key in ('pair_affinity_score_O_N','unrestricted_state_theorem','protected_status_change'):
  m=deepcopy(d);m['decision'][key]=not m['decision'][key];c.append((f'flip {key}',not reject(m)))
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
