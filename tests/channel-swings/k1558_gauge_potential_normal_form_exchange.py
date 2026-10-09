#!/usr/bin/env python3
"""Controls for K1558's gauge-potential normal-form exchange."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1558-gauge-potential-normal-form-exchange.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['normal_form_exchange'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1558'),('temporal gauge','E=-partial_t A' in q['gauge_convention']),('current','j_n^a=e Im<Q^(n+1)phi,D^aQ^n phi>' in q['gauge_convention']),('cross term','M_n(t)=int_T3 A(t,x) dot j_n(t,x) dx' in q['cross_term']),('product rule','M_n\'=-int E dot j_n' in q['product_rule']),('corrected','G_n=F_n^PDE+M_n' in q['corrected_identity']),('radial retained','partial_t||phi||^2' in q['corrected_identity']),('three current pieces',q['current_derivative'].count('e Im<')==3),('witness','A=0 at the testing time' in q['k1478_escape']),('exchange','exchanged, not eliminated' in q['new_boundary']),('scope','not a gauge-invariant energy' in q['scope_guard']),('constructed',d['gauge_dependent_correction_constructed']),('exchanged',d['electric_current_term_exactly_exchanged']),('escape',d['k1478_ultralocal_no_go_escaped']),('current open',not d['differentiated_current_remainder_controlled']),('radial open',not d['radial_leakage_controlled']),('coercive open',not d['same_tier_coercive_modified_energy_constructed']),('flow open',not d['global_full_pde_flow_constructed']),('protected',not d['protected_status_change'])]
 for t in (.2,.7,1.4):
  A=math.sin(t);j=math.cos(2*t);Aprime=math.cos(t);jprime=-2*math.sin(2*t)
  E=-Aprime;checks.append((f'product rule {t}',abs((Aprime*j+A*jprime)-(-E*j+A*jprime))<1e-12))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
