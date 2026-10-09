#!/usr/bin/env python3
"""Controls for K1573's moving-radius current absorption."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1573-moving-radius-current-absorption.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['moving_radius'],D['decision'];rho=.7;H=[1/(n+1)**2 for n in range(18)];a=[rho**(2*n)/math.factorial(n) for n in range(len(H))];G=sum(x*y for x,y in zip(a,H));dr=2/rho*sum(n*a[n]*H[n] for n in range(len(H)));S=sum(a[n]*math.sqrt(H[n]*H[n+1]) for n in range(len(H)-1))
 for eps in (.1,.5,1,3):checks.append((f'epsilon bound {eps}',S<=eps*dr/4+(eps+1/eps)*G/(2*rho)+1e-12))
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1573'),('derivative','partial_rho G_rho=(2/rho)' in q['analytic_energy']),('bound','(epsilon/4)partial_rho G_rho' in q['parameterized_shift_bound']),('proof','2uv<=epsilon u^2+epsilon^(-1)v^2' in q['proof']),('absorb','weight derivative' in q['radius_absorption']),('optimized','-rho\'=C_mB_A/4' in q['optimized_budget']),('budget','int B_A<rho(0)' in q['optimized_budget']),('ceiling','does not prove global coefficient integrability' in q['scope_guard']),('parameterized',d['parameterized_same_radius_derivative_bound_proved']),('moving',d['moving_radius_absorption_proved']),('budget decision',d['explicit_radius_budget_proved']),('no outer',not d['outer_radius_comparison_required_for_local_moving_estimate']),('global open',not d['global_positive_radius_proved']),('flow open',not d['global_full_pde_flow_constructed']),('protected',not d['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
