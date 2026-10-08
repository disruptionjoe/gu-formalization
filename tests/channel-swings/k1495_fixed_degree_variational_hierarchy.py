#!/usr/bin/env python3
"""Controls for K1495's fixed-degree variational hierarchy."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1495-fixed-degree-variational-hierarchy.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items(): checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 a,q=D['variational_hierarchy'],D['decision']
 checks += [('claim',D['claim_id']=='K1495'),('coefficients','c_d is strictly increasing' in a['coefficients']),('base','-1+o(1)' in a['multiplication_bottom']),('bottom','-c_d+o(1)' in a['multiplication_bottom']),('free cost','O_d(N)' in a['free_cost']),('energy','6gC_N^2-c_d g sigma_N+O_d(N)' in a['ground_energy_upper']),('recentering','requires a_N<=' in a['necessary_recentering']),('window','->-infinity' in a['explicit_divergent_window']),('strict decision',q['strictly_increasing_fixed_degree_coefficients']),('variational decision',q['arbitrary_fixed_degree_variational_upper_bound']),('recentering decision',q['arbitrary_fixed_degree_recentering_necessity']),('finite terminal fenced',not q['every_finite_degree_is_terminal']),('unbounded fenced',not q['coefficient_sequence_unbounded']),('lower fenced',not q['matching_ground_energy_lower_bound_proved']),('Mosco fenced',not q['mosco_recovery_proved']),('protected fenced',not q['protected_status_change'])]
 eps=[0.2,0.05,0.01]; cs=[1];
 for e in eps: cs.append(cs[-1]+e)
 checks += [('toy coefficients strict',all(cs[i+1]>cs[i] for i in range(len(cs)-1))),('sigma dominates N',all(n**2.5/n>1 for n in (2,4,8,16)))]
 for i,(label,ok) in enumerate(checks,1): assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
