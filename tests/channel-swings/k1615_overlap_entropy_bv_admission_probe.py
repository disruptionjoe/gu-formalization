#!/usr/bin/env python3
"""Hostile mutations for K1615 census and protected boundaries."""
import json
from copy import deepcopy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def reject(d):
 x=d['census'];p=d['protected_boundaries']
 return (x['satisfied']+x['conditional']+x['excluded']+x['missing']==x['rows'] and all(v is False for v in p.values())
         and x['k1145_k1150_scorable_rows']=='0/7' and len(d['next_wakes'])==3)
def main():
 d=json.loads((ROOT/'lab/process/k1615-overlap-entropy-bv-admission.json').read_text());c=[('baseline',reject(d))]
 for key in d['protected_boundaries']:
  m=deepcopy(d);m['protected_boundaries'][key]=True;c.append((f'flip {key}',not reject(m)))
 for key in ('satisfied','conditional','excluded','missing'):
  m=deepcopy(d);m['census'][key]+=1;c.append((f'census {key}',not reject(m)))
 m=deepcopy(d);m['census']['k1145_k1150_scorable_rows']='1/7';c.append(('scorable drift',not reject(m)))
 m=deepcopy(d);m['next_wakes']=m['next_wakes'][:2];c.append(('wake loss',not reject(m)))
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
