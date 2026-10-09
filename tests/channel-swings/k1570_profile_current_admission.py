#!/usr/bin/env python3
"""Controls for K1570's protected admission replay."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1570-profile-current-admission.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 c,p,d=D['bridge_census'],D['protected_state'],D['decision'];checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1570'),('sum',c['row_count']==c['satisfied_count']+c['conditional_count']+c['excluded_count']+c['missing_count']),('rows',c['row_count']==285),('satisfied',c['satisfied_count']==206),('five new',len(c['new_satisfied_rows'])==5),('four missing',len(c['protected_missing_rows'])==4),('source fixed','SC-META-53 remains UNCERTAIN' in p['source_claims']),('ledger fixed','33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED' in p['physics_ledger']),('counts fixed','0/7' in p['candidate_counts']),('protected surfaces',not any(p[k] for k in ('canon_change','paper_change','prediction_or_confirmation','public_posture_change'))),('advance',d['conditional_mathematical_advance']),('profile',d['profiled_gaussian_coefficient_reduction_proved']),('all g',d['vacuum_coefficient_beaten_for_all_positive_couplings']),('spatial',d['differentiated_current_spatial_loss_removed']),('two radius',d['two_radius_analytic_boundary_proved']),('ratio open',not d['ground_energy_ratio_convergence']),('O1 open',not d['ground_energy_to_bounded_error']),('PDE open',not d['full_pde_leakages_closed']),('BRST open',not d['continuum_interacting_brst_operator']),('source open',not d['source_owned_gu_hamiltonian']),('protected',not d['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
