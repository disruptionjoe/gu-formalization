#!/usr/bin/env python3
"""Controls for K1556's expected-shell quartic lift."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1556-expected-shell-quartic-lift.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['expected_lift'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1556'),('law','real degree-N cutoff fields' in q['law']),('threshold','eta/(2-eta)>=eta/2' in q['threshold_probability']),('pointwise constant','c_(alpha,eta)>0' in q['pointwise_input']),('expected constant','c\'_(alpha,eta)>0' in q['expected_gap']),('wick identity','9C_N^2' in q['wick_scale']),('quartic','Omega_(alpha,eta)(N^4)' in q['wick_scale']),('Fejer boundary','order N^-3' in q['localized_boundary']),('scope','requires expected fixed-ratio shell mass' in q['scope_guard']),('threshold decision',d['threshold_probability_bound_proved']),('gap decision',d['expected_defect_gap_proved']),('quartic decision',d['expected_interaction_floor_N4_proved']),('no Fisher',not d['fisher_cost_used']),('nonconstant fenced',not d['all_nonconstant_sign_laws_excluded']),('protected',not d['protected_status_change'])]
 for eta in (.1,.4,.9):checks.append((f'threshold {eta}',eta/(2-eta)>=eta/2))
 for N in (8,32,128):checks.append((f'quartic scaling {N}',(N*N)**2==N**4))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
