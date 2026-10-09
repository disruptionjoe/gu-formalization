#!/usr/bin/env python3
"""Controls for K1551's expected-shell mixture lift."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1551-sign-shell-mixture-lift.json').read_text())
def main():
 q,d=D['mixture_lift'],D['decision'];checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1551'),('law cutoff','|k|_2<=N' in q['law']),('threshold','eta/(2-eta)>=eta/2' in q['threshold_probability']),('pointwise exponent','N^(-4/3)' in q['pointwise_input']),('expected exponent','N^(-4/3)' in q['expected_conclusion']),('W identity','9C_N^2' in q['wick_scale']),('W exponent','N^(8/3)' in q['wick_scale']),('Fejer boundary','N^(-3)' in q['fejer_boundary']),('scope fixed shell','requires expected fixed-ratio shell mass' in q['scope_guard']),('threshold decision',d['threshold_probability_bound_proved']),('defect decision',d['expected_defect_floor_proved']),('interaction decision',d['expected_interaction_floor_N8over3_proved']),('no Fisher',not d['fisher_cost_used']),('nonconstant fenced',not d['all_nonconstant_sign_laws_excluded']),('protected',not d['protected_status_change'])]
 for eta in (.05,.25,.75):checks.append((f'threshold algebra eta={eta}',eta/(2-eta)>=eta/2))
 for N in (16,64,256):checks.append((f'W exponent N={N}',abs(N**4*N**(-4/3)-N**(8/3))<1e-10*N**(8/3)))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
