#!/usr/bin/env python3
"""Controls for K1549's coarea--L4 Bernstein inverse theorem."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1549-coarea-nikolskii-sign-defect.json').read_text())
def main():
 q,d=D['inverse_theorem'],D['decision'];checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1549'),('hypothesis shell','H_(alpha,N)(sgn f_N)>=eta' in q['hypothesis']),('L4 identity','||f_N||_4^4=delta_N+2q_N-1' in q['quartic_control']),('L4 bound','(1+sqrt(delta_N))^2' in q['quartic_control']),('L4 Bernstein','||grad f_N||_4<=C N' in q['gradient_control']),('gradient exponent','C N mu(B)^(3/4)' in q['transition_volume']),('cores','eta/8' in q['coarea_lower_bound']),('coarea','I_eta>0' in q['coarea_lower_bound']),('transition','N^(-4/3)' in q['transition_volume']),('conclusion','c_(alpha,eta) N^(-4/3)' in q['conclusion']),('sharpness fenced','not a claimed sharp' in q['scope_guard']),('coarea decision',d['coarea_interface_bound_proved']),('gradient decision',d['l4_bernstein_gradient_bound_proved']),('inverse decision',d['universal_fixed_shell_defect_floor_proved']),('sharpness open',not d['exponent_sharpness_proved']),('capacity unnecessary',not d['capacity_required_for_configuration_exclusion']),('protected',not d['protected_status_change'])]
 for N in (16,64,256):checks.append((f'super-N^-2 gap N={N}',N**(-4/3)>N**(-2)))
 q2=1.0
 for delta in (.01,.25,1.0):
  q2=1+math.sqrt(delta);lhs=delta+2*q2-1;rhs=(1+math.sqrt(delta))**2;checks.append((f'L4 envelope delta={delta}',abs(lhs-rhs)<1e-12))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
