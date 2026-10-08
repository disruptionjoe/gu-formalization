#!/usr/bin/env python3
"""Controls for K1530's matrix ultraviolet-shell inequality."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1530-matrix-ultraviolet-shell-cost.json').read_text())
def mm(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def tr(a):return sum(a[i][i] for i in range(len(a)))
def inv2(s):
 d=s[0][0]*s[1][1]-s[0][1]*s[1][0];return [[s[1][1]/d,-s[0][1]/d],[-s[1][0]/d,s[0][0]/d]]
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['matrix_shell_cost'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1530'),('projector','ultraviolet-shell projector' in q['spectral_data']),('positive fraction','>=kappa C_N' in q['spectral_data']),('variance trace','V_N=Tr(Lambda S)' in q['integrated_variance']),('deficit N2','=Theta(N^2)' in q['low_variance_deficit']),('A factor','A=Omega^(1/2)(I-S)S^(-1/2)' in q['frobenius_factorization']),('B factor','B=S^(1/2)P_N Lambda Omega^(-1/2)' in q['frobenius_factorization']),('matrix Cauchy','Frobenius Cauchy' in q['matrix_cauchy']),('dual O1','=O(1)' in q['dual_shell_bound']),('low N4','q0>=cN^4' in q['free_cost_consequence']),('high N4','c_gN^4' in q['high_variance_consequence']),('noncommutative','No step assumes that S commutes' in q['noncommutative_guard']),('scope Gaussian','arbitrary positive Gaussian covariance' in q['scope_guard']),('proof decision',d['matrix_shell_cauchy_proved']),('no stationarity',not d['stationarity_required']),('no diagonal',not d['covariance_diagonality_required']),('no offdiag escape',not d['off_diagonal_escape_exists']),('nongaussian fenced',not d['nongaussian_lower_bound_proved']),('protected',not d['protected_status_change'])]
 # Direct two-mode instances of delta^2 <= Q Tr(D S), including shell/complement mixing.
 omega=[4.0,9.0];lam=[1/(2*x) for x in omega]
 for s in ([[0.3,0.12],[0.12,1.5]],[[0.7,-0.4],[-0.4,2.0]],[[1.8,0.5],[0.5,0.9]]):
  si=inv2(s);qfree=sum(omega[i]*(s[i][i]+si[i][i]-2) for i in range(2))
  delta=lam[0]*(1-s[0][0]);dual=(lam[0]**2/omega[0])*s[0][0]
  checks.append((f'matrix Cauchy {s}',delta*delta<=qfree*dual+1e-12))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
