#!/usr/bin/env python3
"""Controls for K1569's two-radius current normal form."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1569-two-radius-current-normal-form-boundary.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['two_radius_bound'],D['decision'];rho=1.7;sigma=.9;Hs=[(i%5+1)/7 for i in range(40)];a=lambda r,n:r**(2*n)/math.factorial(n);S=sum(a(sigma,n)*math.sqrt(Hs[n]*Hs[n+1]) for n in range(len(Hs)-1));G=sum(a(rho,n)*Hs[n] for n in range(len(Hs)));C=.5*(1+rho**-2*(1-(sigma/rho)**2)**-2)
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1569'),('energies','G_rho=sum_' in q['analytic_energies']),('estimate','(1-(sigma/rho)^2)^(-2)' in q['nested_radius_estimate']),('numerical bound',S<=C*G+1e-12),('modified','B_A' in q['modified_energy_control']),('combined','outer analytic energy' in q['combined_identity']),('obstruction','sqrt(N+1)/rho' in q['same_radius_obstruction']),('consequence','does not create a same-radius coercive energy' in q['consequence']),('scope','does not prove global coefficient integrability' in q['scope_guard']),('two radius',d['two_radius_cross_term_bound_proved']),('conditional sum',d['differentiated_current_analytic_sum_controlled_conditionally']),('one radius no',not d['single_radius_uniform_relative_bound_exists']),('collapse open',not d['k1450_radius_collapse_repaired']),('coercive open',not d['coercive_global_modified_energy_constructed']),('flow open',not d['global_full_pde_flow_constructed']),('protected',not d['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
