#!/usr/bin/env python3
"""Hostile mutations for K1581."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/'lab/process/k1581-profiled-gaussian-residual-descent.json').read_text())
def valid(x):
 q=x['residual_descent'];z=x['decision'];return all([x['claim_id']=='K1581','degree at most two' in q['nonzero_residual'],'nonzero quartic' in q['nonzero_residual'],'span{G_N,u_N}' in q['ritz_matrix'],'strictly below' in q['ritz_matrix'],'translation invariant' in q['symmetry'],'No cutoff-uniform' in q['scope_guard'],z['gaussian_eigenstate_excluded'],z['strict_finite_cutoff_descent'],z['translation_invariant_descent'],not z['uniform_asymptotic_gap'],not z['unrestricted_coefficient_identified'],not z['protected_status_change']])
def main():
 assert valid(D); m=[(('claim_id',),'K1580')]+[(('residual_descent',k),'changed') for k in ('nonzero_residual','ritz_matrix','symmetry','scope_guard')]+[(('decision',k),False) for k in ('gaussian_eigenstate_excluded','strict_finite_cutoff_descent','translation_invariant_descent')]+[(('decision',k),True) for k in ('uniform_asymptotic_gap','unrestricted_coefficient_identified','protected_status_change')]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
