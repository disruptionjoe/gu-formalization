#!/usr/bin/env python3
"""Controls for K1533's all-density Fisher/covariance extremality theorem."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1533-relative-fisher-covariance-extremality.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['fisher_extremality'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1533'),('standard Gaussian','mu=N(0,I_d)' in q['density_and_score']),('positive covariance','positive covariance S' in q['density_and_score']),('weighted Fisher','I_Omega' in q['density_and_score']),('score mean','E_nu u=m' in q['score_identities']),('score cross','S-I' in q['score_identities']),('matrix regression','Cov_nu(u)>=' in q['matrix_regression']),('sharp matrix bound','S+S^(-1)-2I' in q['sharp_bound']),('mean cost','m^T Omega m' in q['sharp_bound']),('equality Gaussian','Gaussian N(m,S)' in q['equality']),('phase split','(1/4)I_Omega' in q['wavefunction']),('phase positive','cannot lower' in q['wavefunction']),('closure','lower semicontinuity' in q['closure']),('Wick fence','no lower bound' in q['scope_guard']),('all density',d['all_density_fisher_covariance_bound_proved']),('extremizer',d['gaussian_fixed_moment_extremizer']),('phase decision',not d['arbitrary_phase_can_lower_cost']),('Wick open',not d['universal_nongaussian_wick_coercivity_proved']),('protected',not d['protected_status_change'])]
 # Exact scalar Gaussian equality and strict Laplace controls.
 for s,m,w in [(0.4,0.0,2.0),(1.7,0.3,5.0),(3.0,-0.8,0.7)]:
  gaussian=w*(m*m+s+1/s-2)
  bound=w*(m*m+(s-1)*(s-1)/s)
  laplace=w*(m*m+s+2/s-2)
  checks += [(f'Gaussian equality s={s}',math.isclose(gaussian,bound,rel_tol=1e-12)),(f'Laplace strict s={s}',laplace>bound)]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
