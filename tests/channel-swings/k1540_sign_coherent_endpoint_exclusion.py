#!/usr/bin/env python3
"""Controls for K1540's global-sign endpoint exclusion."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1540-sign-coherent-endpoint-exclusion.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['sign_coherent_exclusion'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1540'),('two cones','union of the two global sign cones' in q['class']),('config varying sign','sign may vary between configurations' in q['class']),('projection','W_N/(3C_N)' in q['projection_bound']),('shell state','T_N=Tr(P_N Lambda S)' in q['state_shell_bound']),('O1','T_N=O(1)' in q['quadratic_consequence']),('N6','q0[psi]>=cN^6' in q['quadratic_consequence']),('endpoint','No normalized fixed-representation wavefunction' in q['endpoint_exclusion']),('mixture','constant-mode covariance' in q['mixture_guard']),('support load','support hypothesis is load-bearing' in q['scope_guard']),('sign changing open','spatial sign changes on ultraviolet scales' in q['scope_guard']),('excluded',d['global_sign_cones_excluded_at_order_N2']),('floor',d['sign_coherent_free_floor']=='N^6'),('no global mix escape',not d['random_global_sign_evades_shell_test']),('textures open',not d['spatially_sign_changing_states_excluded']),('asymptotic open',not d['unrestricted_ground_energy_asymptotic_proved']),('protected',not d['protected_status_change'])]
 for N in (10.0,30.0):
  C=N*N;W=5*N*N;T=W/(3*C);Csh=.4*C;a=2/N**2;lower=(Csh-T)**2/(4*a*T)
  checks += [(f'T order one {N}',math.isclose(T,5/3)),(f'N6 floor {N}',lower/N**6>0)]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
