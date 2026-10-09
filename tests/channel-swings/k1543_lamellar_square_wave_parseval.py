#!/usr/bin/env python3
"""Controls for K1543's square-wave Parseval tail."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1543-lamellar-square-wave-parseval.json').read_text())
def main():
 q,d=D['lamellar_parseval'],D['decision'];checks=[]
 for name,pin in D['pinned_inputs'].items(): checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1543'),('square wave','sgn(sin t)' in q['definitions']),('odd harmonics','2r+1' in q['definitions']),('sign lemma','sgn(p_R)=s' in q['sign_lemma']),('Dirichlet derivative','sin(2(R+1)t)/(2sin t)' in q['sign_lemma']),('uniform bound','independent of R' in q['uniform_bound']),('tail coefficient','8/pi^2' in q['exact_tail']),('tail index','r=R+1' in q['exact_tail']),('tail scale','Theta((R+1)^(-1))' in q['tail_scale']),('scope family','one-coordinate' in q['scope_guard']),('scope capacity','not a Gaussian capacity' in q['scope_guard']),('sign decision',d['actual_center_sign_identified']),('tail decision',d['parseval_tail_exact']),('uniform decision',d['uniform_partial_sum_bound']),('texture fenced',not d['arbitrary_texture_controlled']),('protected',not d['protected_status_change'])]
 for R in (0,1,4,12):
  vals=[]
  for j in range(1,1000):
   t=math.pi*j/1000; p=4/math.pi*sum(math.sin((2*r+1)*t)/(2*r+1) for r in range(R+1)); vals.append(p)
  checks.append((f'sign sample R{R}',min(vals)>0))
 for i,(label,ok) in enumerate(checks,1): assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
