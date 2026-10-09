#!/usr/bin/env python3
"""Controls for K1560's cutoff Weyl coefficients."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1560-cutoff-weyl-coefficients.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['weyl_coefficients'],D['decision']
 ell=math.log((1+math.sqrt(3))/math.sqrt(2));c_c=12*ell-math.pi;c_o=2*math.sqrt(3)+8*ell-math.pi/3
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1560'),('cube cutoff','||k||_infinity<=N' in q['cutoff']),('covariance cube coefficient','12 log((1+sqrt(3))/sqrt(2))-pi' in q['covariance_sum']),('trace cube coefficient','2sqrt(3)+8 log((1+sqrt(3))/sqrt(2))-pi/3' in q['frequency_trace']),('cube integrals','[-1,1]^3' in q['proof_route']),('real counting','no extra factor two' in q['real_mode_guard']),('scope','not a source normalization' in q['scope_guard']),('C decision',d['covariance_cube_coefficient_proved']),('Omega decision',d['frequency_trace_cube_coefficient_proved']),('mode decision',d['real_mode_counting_fixed']),('bounded open',not d['bounded_error_expansion_proved']),('source open',not d['source_normalization_selected']),('protected',not d['protected_status_change'])]
 checks += [('c_C numeric',abs(c_c-4.760154727959107)<1e-12),('c_Omega numeric',abs(c_o-7.684735651640424)<1e-12)]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
