#!/usr/bin/env python3
"""Controls for K1518's Gaussian quadratic-mass Chernoff bound."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1518-gaussian-quadratic-mass-chernoff.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['quadratic_mass_tail'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1518'),('real basis','real covariance eigenbasis' in q['mass_coordinate']),('independence','independent standard real Gaussians' in q['mass_coordinate']),('C scale','C_N=Theta(N^2)' in q['spectral_sums']),('B scale','B_N=sum_j lambda_(N,j)^2=O(N)' in q['spectral_sums']),('max scale','lambda_*(N)=max_j lambda_(N,j)=O(1)' in q['spectral_sums']),('Jensen','W_N>=(Q_N-3C_N)^2' in q['square_event']),('threshold','(2-sqrt(3))C_N' in q['square_event']),('exact product','log E exp' in q['exact_mgf']),('mgf domain','(2 lambda_*)^(-1)' in q['exact_mgf']),('quadratic mgf','2t^2 B_N' in q['bernstein_bound']),('Bernstein min','min(u^2/B_N,u/lambda_*)' in q['bernstein_bound']),('N3 branch','C_N^2/B_N=Omega(N^3)' in q['small_ball_consequence']),('N2 branch','C_N/lambda_*=Omega(N^2)' in q['small_ball_consequence']),('exp tail','exp(-cN^2)' in q['small_ball_consequence']),('real guard','not a double count' in q['normalization_guard']),('decision exponent',d['low_wick_square_probability_upper']=='exp(-cN^2)'),('Chebyshev superseded',d['polynomial_chebyshev_input_superseded']),('no matching',not d['matching_small_ball_asymptotic_proved']),('no localization',not d['ground_state_localization_proved']),('protected',not d['protected_status_change'])]
 eta=2-math.sqrt(3);checks += [('eta positive',0<eta<1),('event threshold',math.isclose((3-math.sqrt(3))-1,eta))]
 for n in (10,100,1000): checks.append((f'scale minimum {n}',min((n*n)**2/n,(n*n)/1)==n*n))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
