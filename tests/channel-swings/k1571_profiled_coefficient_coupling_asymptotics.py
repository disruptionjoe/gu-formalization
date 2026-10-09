#!/usr/bin/env python3
"""Controls for K1571's profiled coefficient coupling asymptotics."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1571-profiled-coefficient-coupling-asymptotics.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['coupling_asymptotics'],D['decision'];a=math.pi/2
 for k in (1e-4,1e-7,1e-10):
  model=lambda u:a*u*math.log(1/u)
  integ=a*(.5*k*k*math.log(1/k)+.25*k*k)
  gap=.5*integ-.25*k*model(k)
  checks.append((f'gap constant model {k}',abs(gap/k**2-math.pi/16)<1e-10))
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1571'),('origin','pi/2' in q['cube_origin']),('weak scale','1/(12pi)' in q['weak_coupling_scale']),('gap','pi/16' in q['weak_coupling_gap'] and '1/(6pi)' in q['weak_coupling_gap']),('large A','4kappa^(-1/2)-2kappa^(-3/2)' in q['large_kappa_data']),('strong root','sqrt(24c_C g)-2/c_C' in q['strong_coupling_scale']),('strong coefficient','4sqrt(24c_C g)-4/c_C-c_Omega/2' in q['strong_coupling_scale']),('scope','do not prove an unrestricted lower coefficient' in q['scope_guard']),('weak decision',d['weak_coupling_exponential_scale_proved']),('gap decision',d['weak_coupling_gap_constant_proved']),('strong decision',d['strong_coupling_square_root_scale_proved']),('constant decision',d['strong_coupling_constant_term_proved']),('lower open',not d['unrestricted_ground_energy_coefficient_proved']),('O1 open',not d['bounded_error_recentering_proved']),('protected',not d['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
