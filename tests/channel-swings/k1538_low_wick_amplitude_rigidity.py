#!/usr/bin/env python3
"""Controls for K1538's exact amplitude-rigidity reduction."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1538-low-wick-amplitude-rigidity.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['amplitude_rigidity'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1538'),('A definition','sqrt(3C_N)' in q['definitions']),('identity','(|phi_N|-A_N)^2=' in q['pointwise_identity']),('denominator','(|phi_N|+A_N)^2' in q['pointwise_identity']),('configuration','W_N/(3C_N)' in q['configuration_bound']),('all laws','For every probability law' in q['state_bound']),('quadratic error','O(1)' in q['quadratic_endpoint']),('sign survives','spatial sign field' in q['interpretation']),('capacity fenced','neither a small-ball exponent nor a Dirichlet-capacity bound' in q['scope_guard']),('identity decision',d['exact_amplitude_identity_proved']),('all configs',d['all_configuration_bound_proved']),('order one',d['quadratic_wick_implies_order_one_amplitude_error']),('no sign',not d['global_sign_selected']),('capacity open',not d['endpoint_capacity_computed']),('protected',not d['protected_status_change'])]
 for A,x in [(2.0,-5.0),(3.0,-.5),(4.0,0.0),(5.0,7.0)]:
  lhs=(abs(x)-A)**2;rhs=(x*x-A*A)**2/(abs(x)+A)**2
  checks += [(f'identity {A,x}',math.isclose(lhs,rhs)),(f'bound {A,x}',lhs<=(x*x-A*A)**2/A**2+1e-12)]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
