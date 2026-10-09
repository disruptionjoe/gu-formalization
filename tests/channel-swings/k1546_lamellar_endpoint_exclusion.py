#!/usr/bin/env python3
"""Controls for K1546's family-scoped endpoint exclusion."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1546-lamellar-endpoint-exclusion.json').read_text())
def main():
 q,d=D['lamellar_exclusion'],D['decision'];checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1546'),('cubic','Omega(N^3)' in q['quadratic_budget']),('quadratic miss','W_N=O(N^2)' in q['quadratic_budget']),('K1541 shell','K1541' in q['k1541_compatible_branch']),('quartic','Omega(N^4)' in q['k1541_compatible_branch']),('capacity order','before any relative-Fisher' in q['capacity_position']),('survivor nonlamellar','non-lamellar' in q['surviving_route']),('scope 3d','three-dimensional' in q['scope_guard']),('scope asymptotic','ground-energy asymptotic' in q['scope_guard']),('excluded decision',d['canonical_lamellar_order_N2_route_excluded']),('quartic decision',d['k1541_lamellar_branch_has_quartic_interaction']),('no Fisher needed',not d['fisher_cost_needed_for_family_exclusion']),('all textures fenced',not d['all_sign_textures_excluded']),('asymptotic fenced',not d['unrestricted_ground_energy_asymptotic_proved']),('protected',not d['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
