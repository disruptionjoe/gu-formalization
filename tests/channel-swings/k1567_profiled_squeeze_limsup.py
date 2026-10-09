#!/usr/bin/env python3
"""Controls for K1567's profiled squeeze limsup."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1567-profiled-squeeze-limsup.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['profiled_upper'],D['decision'];n=28;u=[(i+.5)/n for i in range(n)];rs=[math.sqrt(x*x+y*y+z*z) for x in u for y in u for z in u];w=8/len(rs)
 A=lambda k:.5*w*sum(1/math.sqrt(r*r+k) for r in rs);F=lambda k:.25*w*sum(math.sqrt(r*r+k)+r*r/math.sqrt(r*r+k)-2*r for r in rs);c=A(0)
 for g in (.02,.1,1.0):
  f=lambda k:k-24*g*(c-A(k));lo=1e-8;hi=max(1,24*g*c)
  while f(hi)<0:hi*=2
  for _ in range(70):
   mid=(lo+hi)/2
   if f(mid)<0:lo=mid
   else:hi=mid
  k=(lo+hi)/2;a=A(k);checks.append((f'strict profile {g}',F(k)+6*g*a*(2*c-a)<6*g*c*c))
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1567'),('functional','J_g(A)=F_*(A)+6gA(2c_C-A)' in q['reduced_functional']),('equation','R(kappa_g)=24g' in q['self_consistency']),('all g','for every g>0' in q['all_coupling_strictness']),('origin','nonperturbatively small' in q['origin_mechanism']),('recovery','omega_k/sqrt(omega_k^2+kappa_g N^2)' in q['finite_cutoff_recovery']),('limsup','limsup_' in q['unrestricted_limsup']),('uniform threshold','strictly improves' in q['uniform_family_comparison']),('scope','not a matching unrestricted lower coefficient' in q['scope_guard']),('unique',d['unique_profiled_minimizer_proved']),('recovery decision',d['finite_cutoff_recovery_sequence_constructed']),('strict decision',d['vacuum_coefficient_beaten_for_every_positive_coupling']),('threshold decision',d['uniform_family_threshold_is_not_full_gaussian_threshold']),('limsup decision',d['explicit_unrestricted_limsup_improved']),('convergence open',not d['ground_energy_ratio_convergence_proved']),('O1 open',not d['bounded_error_recentering_proved']),('protected',not d['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
