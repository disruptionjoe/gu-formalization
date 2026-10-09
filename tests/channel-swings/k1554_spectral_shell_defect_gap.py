#!/usr/bin/env python3
"""Controls for K1554's fixed-shell spectral defect gap."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1554-spectral-shell-defect-gap.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['spectral_gap'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1554'),('shell hypothesis','H_(alpha,N)(s_N)>=eta' in q['hypothesis']),('transfer','sqrt(eta)/2' in q['shell_transfer']),('gradient floor','alpha^2 eta N^2/4' in q['gradient_floor']),('transition volume','16delta_N/9' in q['transition_set']),('square degree','degree(g_N)<=2N' in q['outer_gradient']),('outer delta','4N^2 delta_N' in q['outer_gradient']),('inner root delta','C N^2 sqrt(delta_N)' in q['inner_gradient']),('constant gap','c_(alpha,eta)>0 uniformly in N' in q['defect_gap']),('scope shell','nonvanishing fixed-ratio shell mass' in q['scope_guard']),('transfer decision',d['sign_shell_transferred_to_field']),('gradient decision',d['order_N2_gradient_floor_proved']),('split decision',d['transition_and_complement_gradient_split_proved']),('gap decision',d['cutoff_independent_defect_gap_proved']),('old exponent not sharp',not d['k1549_Nminus4over3_bound_sharp']),('capacity open',not d['weighted_capacity_computed']),('protected',not d['protected_status_change'])]
 for eta,delta in ((.4,.01),(.2,.001)):
  checks.append((f'shell triangle {eta}',math.sqrt(eta)-math.sqrt(delta)>=math.sqrt(eta)/2))
 for delta in (.01,.04,.2):checks.append((f'transition split positive {delta}',4*delta+8*math.sqrt(delta)>0))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
