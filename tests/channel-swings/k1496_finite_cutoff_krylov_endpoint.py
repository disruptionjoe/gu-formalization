#!/usr/bin/env python3
"""Controls for K1496's fixed-cutoff full-tower endpoint."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1496-finite-cutoff-krylov-endpoint.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 a,q=D['finite_cutoff_endpoint'],D['decision']
 checks += [('claim',D['claim_id']=='K1496'),('square','(phi_N(x)^2-3C_N)^2' in a['square_completion']),('lower','-L_N' in a['square_completion']),('support','sqrt(3C_N)' in a['exact_essential_infimum']),('essential inf','ess inf X_N=-L_N' in a['exact_essential_infimum']),('Hardy','Hardy criterion' in a['hardy_determinacy']),('exponential','E exp(c_N sqrt(Z_N))<infinity' in a['hardy_determinacy']),('tower','decreasing to ess inf X_N' in a['tower_limit']),('endpoint scale','Theta(N^(3/2))' in a['endpoint_scale']),('limit fence','does not prove that c_d is unbounded' in a['noncommuting_limits']),('exact decision',q['exact_fixed_cutoff_multiplication_infimum']=='-6C_N^2/sigma_N'),('tower decision',q['fixed_cutoff_polynomial_tower_reaches_infimum']),('scale decision',q['fixed_cutoff_endpoint_order']=='N^(3/2)'),('no interchange',not q['degree_and_cutoff_limits_interchanged']),('no uniform cost',not q['degree_dependent_free_cost_controlled_uniformly']),('no ground asymptotic',not q['ground_energy_asymptotic_determined']),('protected fenced',not q['protected_status_change'])]
 L=3.0;support=[-L,0.0,2.0];weights=[.2,.5,.3]
 indicators=[]
 for x in support:
  p=((x-0.0)*(x-2.0))/((-L-0.0)*(-L-2.0));indicators.append(p)
 checks += [('degree-two interpolation isolates lower atom',abs(indicators[0]-1)<1e-12 and abs(indicators[1])<1e-12 and abs(indicators[2])<1e-12),('isolated Rayleigh endpoint',abs(sum(w*p*p*x for w,p,x in zip(weights,indicators,support))/sum(w*p*p for w,p in zip(weights,indicators))+L)<1e-12),('scaling algebra',all(abs((n**4)/(n**2.5)-n**1.5)<1e-9 for n in (2,4,8)))]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
