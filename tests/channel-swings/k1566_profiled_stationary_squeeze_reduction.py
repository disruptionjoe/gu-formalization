#!/usr/bin/env python3
"""Controls for K1566's profiled stationary squeeze reduction."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1566-profiled-stationary-squeeze-reduction.json').read_text())
def grid(n=26):
 return [math.sqrt(x*x+y*y+z*z) for x in [(i+.5)/n for i in range(n)] for y in [(j+.5)/n for j in range(n)] for z in [(k+.5)/n for k in range(n)]]
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['profile_reduction'],D['decision'];rs=grid();w=8/len(rs)
 A=lambda k:.5*w*sum(1/math.sqrt(r*r+k) for r in rs)
 F=lambda k:.25*w*sum(math.sqrt(r*r+k)+r*r/math.sqrt(r*r+k)-2*r for r in rs)
 c=A(0);ks=(.01,.1,1.0);As=[A(k) for k in ks];Rs=[k/(c-a) for k,a in zip(ks,As)]
 k=.1;a=A(k);s=a/c;Fu=.25*w*sum(r*(s+1/s-2) for r in rs)
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1566'),('data','A[s]=(1/2)int_Q s/r' in q['continuum_data']),('profile','r/sqrt(r^2+kappa)' in q['fixed_variance_minimizer']),('convexity','strictly convex' in q['proof']),('derivative',"F_*'(A)=-kappa(A)/2" in q['reduced_derivative']),('ratio','strictly increasing from 0 to infinity' in q['ratio_monotonicity']),('uniform strict','strict convexity' in q['uniform_comparison']),('scope','not an unrestricted lower bound' in q['scope_guard']),('A monotone',As[0]>As[1]>As[2]>0),('R monotone',Rs[0]<Rs[1]<Rs[2]),('profile beats uniform',F(k)<Fu),('minimizer',d['fixed_variance_profile_minimizer_proved']),('reduction',d['continuum_reduction_to_one_parameter_proved']),('ratio decision',d['profile_ratio_strictly_monotone']),('uniform decision',d['uniform_profile_strictly_suboptimal_at_fixed_nonvacuum_variance']),('lower open',not d['unrestricted_ground_energy_coefficient_proved']),('O1 open',not d['bounded_error_recentering_proved']),('protected',not d['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
