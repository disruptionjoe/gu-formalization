#!/usr/bin/env python3
"""Controls for K1528's arbitrary-Gaussian Q-space identity."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1528-general-gaussian-q-space-formula.json').read_text())
def matmul(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def tr(a):return sum(a[i][i] for i in range(len(a)))
def inv2(s):
 d=s[0][0]*s[1][1]-s[0][1]*s[1][0];return [[s[1][1]/d,-s[0][1]/d],[-s[1][0]/d,s[0][0]/d]]
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['general_gaussian_formula'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1528'),('arbitrary S','any real symmetric positive-definite covariance' in q['trial_class']),('phase allowed','linear-quadratic phase' in q['trial_class']),('normalized density','det(S)^(-1/2)' in q['density']),('gradient half','grad log psi=(1/2)' in q['logarithmic_gradient']),('exact trace','Tr[Omega(S+S^(-1)-2I)]' in q['exact_amplitude_cost']),('matrix factor','(I-S)S^(-1)(I-S)' in q['matrix_positivity']),('no commutation','without requiring [S,Omega]=0' in q['matrix_positivity']),('phase positive','cannot lower' in q['phase_guard']),('diagonal recovery','sum_j omega_j(s_j-1)^2/s_j' in q['diagonal_recovery']),('scope finite Gaussian','finite-cutoff Gaussian Q-space wavefunctions' in q['scope_guard']),('formula decision',d['arbitrary_positive_covariance_formula_proved']),('off diagonal',d['off_diagonal_covariance_included']),('nonstationary',d['nonstationary_covariance_included']),('phase cannot lower',not d['gaussian_phase_can_lower_cost']),('nongaussian fenced',not d['nongaussian_classified']),('protected',not d['protected_status_change'])]
 # Explicit noncommuting positive covariances: trace identity and positivity.
 omega=[[2.0,0.0],[0.0,5.0]]
 for s in ([[2.0,0.5],[0.5,1.0]],[[0.8,-0.2],[-0.2,1.7]],[[3.0,0.7],[0.7,0.6]]):
  si=inv2(s);i=[[1.0,0.0],[0.0,1.0]]
  lhs=tr(matmul(omega,[[s[r][c]+si[r][c]-2*i[r][c] for c in range(2)] for r in range(2)]))
  a=[[i[r][c]-s[r][c] for c in range(2)] for r in range(2)]
  rhs=tr(matmul(omega,matmul(matmul(a,si),a)))
  checks += [(f'factor identity {s}',math.isclose(lhs,rhs,rel_tol=1e-12,abs_tol=1e-12)),(f'positive cost {s}',lhs>=-1e-12)]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
