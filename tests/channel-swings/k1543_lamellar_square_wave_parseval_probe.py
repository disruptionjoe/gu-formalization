#!/usr/bin/env python3
"""Hostile mutations for K1543."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1543-lamellar-square-wave-parseval.json').read_text())
def valid(x):
 q,d=x['lamellar_parseval'],x['decision'];return all([x['claim_id']=='K1543','sgn(p_R)=s' in q['sign_lemma'],'8/pi^2' in q['exact_tail'],'r=R+1' in q['exact_tail'],'Theta((R+1)^(-1))' in q['tail_scale'],'one-coordinate' in q['scope_guard'],d['actual_center_sign_identified'],d['parseval_tail_exact'],d['uniform_partial_sum_bound'],not d['arbitrary_texture_controlled'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1542'),(('lamellar_parseval','sign_lemma'),'changed'),(('lamellar_parseval','exact_tail'),'changed'),(('lamellar_parseval','tail_scale'),'changed'),(('lamellar_parseval','scope_guard'),'changed'),(('decision','actual_center_sign_identified'),False),(('decision','parseval_tail_exact'),False),(('decision','uniform_partial_sum_bound'),False),(('decision','arbitrary_texture_controlled'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
