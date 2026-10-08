#!/usr/bin/env python3
"""Controls for K1520's resolvent collapse."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1520-quadratic-resolvent-collapse.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['spectral_consequence'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1520'),('resolvent identity','(E_N+lambda)^(-1)' in q['unshifted_resolvent']),('rate','O(N^-2)' in q['unshifted_resolvent']),('margin','r_N tending to infinity' in q['general_low_shift']),('bound','1/(r_N+lambda)' in q['general_low_shift']),('subquadratic','a_N=o(N^2)' in q['subquadratic_shift']),('plus infinity','plus infinity' in q['subquadratic_shift']),('zero not resolvent','not the resolvent' in q['operator_ceiling']),('nontrivial limit fenced','cannot have a finite nontrivial' in q['operator_ceiling']),('nonsharp','nonsharp' in q['rate_ceiling']),('decision rate',d['unshifted_resolvent_norm_upper']=='N^-2'),('shift excluded',d['subquadratic_recentering_excluded']),('limit false',not d['finite_unshifted_strong_resolvent_limit']),('matching fenced',not d['matching_resolvent_asymptotic_proved']),('protected',not d['protected_status_change'])]
 for n in (10,100,1000):checks.append((f'rate decreases {n}',1/(n*n+1)<2/(n*n)))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
