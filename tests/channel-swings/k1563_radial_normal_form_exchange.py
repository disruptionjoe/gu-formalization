#!/usr/bin/env python3
"""Controls for K1563's radial normal-form exchange."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1563-radial-normal-form-exchange.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['radial_exchange'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1563'),('correction','-(lambda/2)' in q['correction']),('identity','H_n\'' in q['exact_identity']),('same tier','(|lambda|/m)' in q['same_tier_bound']),('combined','A dot partial_t j_n' in q['combined_k1558_identity']),('advance','partial_t|phi|^2 is removed' in q['advance']),('scope','not a coercive gauge-invariant modified energy' in q['scope_guard']),('K1450 guard','replacement of K1450' in q['scope_guard']),('correction decision',d['radial_correction_constructed']),('cancel decision',d['radial_time_derivative_cancelled']),('bound decision',d['same_tier_bound_proved']),('combined decision',d['combined_normal_form_identity_proved']),('current open',not d['differentiated_current_controlled']),('coercivity open',not d['coercive_modified_energy_constructed']),('flow open',not d['global_full_pde_flow_constructed']),('protected',not d['protected_status_change'])]
 for m,x,y in ((1,.4,.7),(2,3,1),(5,.2,4)):
  H=.5*(y*y+m*m*x*x);checks.append((f'young {m}',x*y<=H/m+1e-12))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
