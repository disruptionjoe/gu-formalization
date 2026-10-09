#!/usr/bin/env python3
"""Controls for K1574's analytic-weight shift tradeoff."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1574-analytic-weight-shift-tradeoff.json').read_text())
def ratio(w,H):
 G=sum(a*b for a,b in zip(w,H));S=sum(w[n]*math.sqrt(H[n]*H[n+1]) for n in range(len(H)-1));return S/G
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['weight_tradeoff'],D['decision'];rho=.8
 for N in (4,12,30):
  wf=[rho**(2*n)/math.factorial(n) for n in range(N+2)];H=[0]*(N+2);H[N]=1/wf[N];H[N+1]=1/wf[N+1];checks.append((f'factorial witness {N}',abs(ratio(wf,H)-math.sqrt(N+1)/(2*rho))<1e-12))
 wg=[rho**(2*n) for n in range(40)];H=[1/(n+1) for n in range(40)];checks.append(('geometric bound',ratio(wg,H)<=1/rho+1e-12))
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1574'),('criterion','if and only if' in q['criterion'] and 'sqrt(w_n/w_(n+1))' in q['criterion'] and 'C<=q' in q['criterion']),('factorial','sqrt(n+1)/rho' in q['factorial_obstruction']),('geometric','ratio is 1/rho' in q['geometric_control']),('Leibniz','(n+1)/rho' in q['leibniz_tradeoff']),('routes','radius expenditure' in q['consequence']),('scope','does not exclude all modified energies' in q['scope_guard']),('criterion decision',d['general_weight_shift_criterion_proved']),('factorial decision',d['factorial_same_radius_shift_excluded']),('geometric decision',d['geometric_same_radius_shift_controlled']),('simultaneous no',not d['factorial_leibniz_and_bounded_shift_simultaneously_available']),('repairs open',not d['all_pde_repairs_excluded']),('flow open',not d['global_full_pde_flow_constructed']),('protected',not d['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
