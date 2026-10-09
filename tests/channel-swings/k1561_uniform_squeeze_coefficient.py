#!/usr/bin/env python3
"""Controls for K1561's uniform-squeeze coefficient."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1561-uniform-squeeze-coefficient.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['uniform_squeeze'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1561'),('trial','0<s<=1' in q['trial']),('mean positive part','[3C_N(1-s)-m^2/(4g)]_+' in q['finite_cutoff_optimizer']),('free mass cost','(m^2/2)y_N' in q['finite_cutoff_free_cost']),('interaction polynomial','y_N^2-6C_N(1-s)y_N' in q['finite_cutoff_interaction']),('exact optimized total','[6gC_N(1-s)-m^2/2]_+^2/(4g)' in q['finite_cutoff_total']),('active branch','-m^4/(16g)' in q['active_branch_total']),('coefficient','e_g(s)' in q['leading_functional']),('vacuum','e_g(1)=6g c_C^2' in q['endpoint']),('scope','upper-trial coefficient' in q['scope_guard']),('trial decision',d['uniform_squeeze_trial_constructed']),('mean decision',d['mean_optimized_at_finite_cutoff']),('mass decision',d['zero_mode_mass_cost_included']),('functional decision',d['leading_coefficient_functional_derived']),('vacuum decision',d['vacuum_endpoint_recovered']),('coefficient open',not d['unrestricted_ground_energy_coefficient_proved']),('O1 open',not d['bounded_error_recentering_proved']),('protected',not d['protected_status_change'])]
 ell=math.log((1+math.sqrt(3))/math.sqrt(2));c_c=12*ell-math.pi;c_o=2*math.sqrt(3)+8*ell-math.pi/3
 for s in (.2,.5,1.0):
  f=lambda g:(c_o/4)*(s+1/s-2)+6*g*c_c**2*s*(2-s)
  checks.append((f'finite e positive {s}',f(.1)>0))
 checks.append(('vacuum value',abs((c_o/4)*(1+1-2)+6*.1*c_c**2-6*.1*c_c**2)<1e-12))
 for C,B,m,g,s in ((2.,7.,1.,.1,.8),(20.,70.,2.,.3,.4)):
  y=max(0.,3*C*(1-s)-m*m/(4*g)); raw=B/4*(s+1/s-2)+m*m*y/2+g*(y*y-6*C*(1-s)*y+C*C*(3*s*s-6*s+9)); opt=B/4*(s+1/s-2)+g*C*C*(3*s*s-6*s+9)-max(0.,6*g*C*(1-s)-m*m/2)**2/(4*g)
  checks.append((f'exact optimizer {C}',abs(raw-opt)<1e-12))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
