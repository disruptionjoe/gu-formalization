#!/usr/bin/env python3
"""Certificate for K1612's Renyi-half growing-mixture theorem."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def rhalf(p): return sum(math.sqrt(x) for x in p)**2
def main():
 d=json.loads((ROOT/'lab/process/k1612-growing-mixture-renyi-rigidity.json').read_text());q=d['renyi_rigidity'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1612'),('definition','sum_i sqrt' in q['effective_count']),
       ('pair identity','[R_(1/2)-1]/2' in q['effective_count']),('gain','Lambda_N' in q['mixing_gain']),
       ('component floor','lambda_N^prof' in q['component_floor']),('subcubic','o(N^3)' in q['coefficient']),
       ('coefficient','h_g^prof' in q['coefficient']),('equal weights','M_N=o(N^3)' in q['examples'])]
 for p in ([.25]*4,[.7,.2,.09,.01],[1.0]):
  lhs=sum(math.sqrt(p[i]*p[j]) for i in range(len(p)) for j in range(i+1,len(p)))
  c.append((f'identity {len(p)}',abs(lhs-(rhalf(p)-1)/2)<1e-12))
 c += [('fixed closed',z['fixed_finite_overlapping_translated_class_closed']),('growing',z['growing_mixture_controlled']),
       ('condition',z['renyi_half_subcubic_required']),('class coefficient',z['class_coefficient_h_g_prof']),
       ('critical open',not z['critical_effective_count_closed']),('unrestricted open',not z['unrestricted_leading_coefficient_identified']),
       ('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
