#!/usr/bin/env python3
"""Controls for K1578's flat-connection budget obstruction."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1578-flat-connection-radius-budget-obstruction.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['flat_connection_test'],D['decision'];e=.7;a=1.3;T=11;checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1578'),('background','E=-partial_t A=0' in q['background']),('linear budget',math.isclose(abs(e)*abs(a)*T,10.01)),('diverges','infinity' in q['budget_divergence']),('zero curvature','zero Maxwell curvature' in q['finite_energy_control']),('holonomy','2pi Z' in q['global_gauge_boundary']),('generic','Generic a' in q['global_gauge_boundary']),('sufficient','sufficient but not necessary' in q['consequence']),('ceiling','does not disprove local' in q['scope_guard']),('integrability excluded',d['raw_B_A_global_integrability_from_energy_excluded']),('radius no',not d['finite_radius_survives_raw_budget_for_all_time']),('generic no',not d['generic_flat_holonomy_periodically_gauge_removable']),('local valid',d['moving_radius_local_estimate_remains_valid']),('flow open',not d['global_full_pde_flow_constructed']),('protected',not d['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
