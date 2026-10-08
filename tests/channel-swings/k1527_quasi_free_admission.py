#!/usr/bin/env python3
"""Controls for K1527's protected admission replay."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1527-quasi-free-admission.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 c,p,d=D['bridge_census'],D['protected_state'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1527'),('count sum',c['row_count']==c['satisfied_count']+c['conditional_count']+c['excluded_count']+c['missing_count']),('rows',c['row_count']==234),('satisfied',c['satisfied_count']==155),('conditional',c['conditional_count']==10),('excluded',c['excluded_count']==65),('missing',c['missing_count']==4),('six new',len(c['new_satisfied_rows'])==6),('four protected missing',len(c['protected_missing_rows'])==4),('source fixed','SC-META-53 remains UNCERTAIN' in p['source_claims']),('ledger fixed','33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED' in p['physics_ledger']),('K counts','0/7' in p['candidate_counts']),('untouched source','lab/sources/source-claim-register.yaml' in p['untouched_surfaces']),('untouched canon','canon/' in p['untouched_surfaces']),('public fixed',not p['public_posture_change']),('advance',d['conditional_mathematical_advance']),('class classified',d['stationary_quasi_free_route_classified']),('outside fenced',not d['arbitrary_gaussian_or_nongaussian_route_classified']),('source fenced',not d['source_owned_gu_hamiltonian']),('asymptotic fenced',not d['matching_ground_energy_asymptotic']),('prediction fenced',not d['prediction_or_confirmation']),('protected',not d['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
