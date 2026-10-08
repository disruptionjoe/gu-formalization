#!/usr/bin/env python3
"""Hostile mutations for K1530."""
import json,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1530-matrix-ultraviolet-shell-cost.json').read_text())
def valid(x):
 q,d=x['matrix_shell_cost'],x['decision']
 return all([x['claim_id']=='K1530','>=kappa C_N' in q['spectral_data'],'V_N=Tr(Lambda S)' in q['integrated_variance'],'=Theta(N^2)' in q['low_variance_deficit'],'A=Omega^(1/2)(I-S)S^(-1/2)' in q['frobenius_factorization'],'Frobenius Cauchy' in q['matrix_cauchy'],'=O(1)' in q['dual_shell_bound'],'q0>=cN^4' in q['free_cost_consequence'],'c_gN^4' in q['high_variance_consequence'],'No step assumes that S commutes' in q['noncommutative_guard'],'arbitrary positive Gaussian covariance' in q['scope_guard'],d['matrix_shell_cauchy_proved'],not d['stationarity_required'],not d['covariance_diagonality_required'],not d['off_diagonal_escape_exists'],not d['nongaussian_lower_bound_proved'],not d['protected_status_change']])
def main():
 muts=[]
 for path,value in [(('claim_id',),'K1529'),(('matrix_shell_cost','spectral_data'),'no shell mass'),(('matrix_shell_cost','integrated_variance'),'constant only'),(('matrix_shell_cost','low_variance_deficit'),'small'),(('matrix_shell_cost','frobenius_factorization'),'scalar only'),(('matrix_shell_cost','matrix_cauchy'),'reversed'),(('matrix_shell_cost','dual_shell_bound'),'O(N2)'),(('matrix_shell_cost','free_cost_consequence'),'N2'),(('matrix_shell_cost','high_variance_consequence'),'N2'),(('matrix_shell_cost','noncommutative_guard'),'S commutes'),(('matrix_shell_cost','scope_guard'),'all states'),(('decision','matrix_shell_cauchy_proved'),False),(('decision','stationarity_required'),True),(('decision','covariance_diagonality_required'),True),(('decision','off_diagonal_escape_exists'),True),(('decision','nongaussian_lower_bound_proved'),True),(('decision','protected_status_change'),True)]:
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;muts.append(x)
 assert valid(D)
 for i,x in enumerate(muts,1):assert not valid(x),i;print(f'PASS {i:02d}: rejected mutation')
 print(f'RESULT: PASS {len(muts)}/{len(muts)}')
if __name__=='__main__':main()
