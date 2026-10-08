#!/usr/bin/env python3
"""Controls for K1517's admission replay."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1517-moderate-deviation-tilt-admission.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 c,q=D['bridge_census'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1517'),('sum',c['row_count']==c['satisfied_count']+c['conditional_count']+c['excluded_count']+c['missing_count']),('rows',c['row_count']==221),('satisfied',c['satisfied_count']==142),('conditional',c['conditional_count']==10),('excluded',c['excluded_count']==65),('missing',c['missing_count']==4),('new satisfied seven',len(c['new_satisfied_rows'])==7),('new excluded two',len(c['new_excluded_rows'])==2),('missing four',len(c['missing_rows'])==4),('moderate deviations',q['moderate_deviation_window_proved']),('tilt',q['truncated_exponential_tilt_transferred']),('weighted cost',q['weighted_malliavin_cost_proved']),('rate',q['polynomial_variational_rate_proved']),('recenter',q['polynomial_recentering_window_excluded']),('optimal fenced',not q['optimal_rate_or_endpoint_proved']),('lower fenced',not q['many_chaos_ground_energy_lower_bound_constructed']),('limit fenced',not q['ground_energy_recentered_limit_constructed']),('PDE fenced',not q['full_spacetime_pde_repair_constructed']),('source fenced',not q['source_selected_reduction_constructed']),('counts fixed',not q['k1145_k1150_candidate_counts_move']),('protected fixed',not q['protected_status_change']),('ledger fixed','33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED' in D['source_and_ledger_effect']),('source fixed','SOURCE_REGISTER_UNCHANGED' in D['source_and_ledger_effect'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
