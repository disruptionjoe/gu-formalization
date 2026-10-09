#!/usr/bin/env python3
"""Controls for K1544's lamellar interaction scale."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1544-lamellar-interaction-defect.json').read_text())
def main():
 q,d=D['interaction_defect'],D['decision'];checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1544'),('cutoff','N=(2R+1)M' in q['cutoff_family']),('amplitude','sqrt(3C_N)' in q['cutoff_family']),('best approximation','Fourier best approximation' in q['best_approximation']),('all exact signs','every real degree-N' in q['best_approximation']),('lower defect','T_R<=delta_R' in q['defect_comparison']),('upper defect','(C_0+1)^2 T_R' in q['defect_comparison']),('W identity','9C_N^2' in q['wick_identity']),('family scale','Theta(N^3 M)' in q['family_scale']),('cubic floor','Omega(N^3)' in q['cubic_floor']),('quadratic miss','order-N^2' in q['cubic_floor']),('Fisher after','before Fisher cost' in q['cubic_floor']),('scope likelihood','likelihoods' in q['scope_guard']),('projection decision',d['fourier_best_approximation_bound_proved']),('scale decision',d['optimal_wick_scaling_proved']),('floor decision',d['lamellar_cubic_floor_proved']),('trial fenced',not d['order_N2_lamellar_center_constructed']),('textures fenced',not d['all_sign_textures_excluded']),('protected',not d['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
