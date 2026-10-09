#!/usr/bin/env python3
"""Controls for K1568's differentiated-current identity."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1568-differentiated-current-integration-by-parts.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['current_identity'],D['decision'];checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1568'),('fields','psi_n=Q^n phi' in q['fields']),('three pieces',q['differentiation'].count('e Im<')==3),('ibp','partial^a A_a' in q['integration_by_parts'] and 'D^a psi_(n+1)' in q['integration_by_parts']),('commutator','electric curvature' in q['commutator']),('bound','sqrt(H_n H_(n+1))' in q['tame_bound']),('correction','sqrt(H_n H_(n+1))' in q['normal_form_size']),('advance','no spatial derivative' in q['advance'] and 'adjacent charge tier' in q['advance']),('scope','does not make M_n gauge invariant' in q['scope_guard']),('identity decision',d['differentiated_current_identity_proved']),('ibp decision',d['covariant_integration_by_parts_proved']),('spatial decision',d['spatial_derivative_loss_removed']),('shift',d['one_charge_shift_remains']),('coercive open',not d['single_tier_coercive_modified_energy_proved']),('flow open',not d['global_full_pde_flow_constructed']),('protected',not d['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
