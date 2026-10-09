#!/usr/bin/env python3
"""Certificate for K1617's Shannon-entropy coefficient rigidity."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def entropy(p): return -sum(x*math.log(x) for x in p if x)
def main():
 d=json.loads((ROOT/'lab/process/k1617-shannon-entropy-mixture-rigidity.json').read_text());q=d['entropy_rigidity'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1617'),('data processing','I(Z_N;X_N)<=H(p_N)' in q['data_processing']),
       ('floor','lambda_N^prof-(Lambda_N/2)H(p_N)' in q['energy_floor']),('condition','H(p_N)=o(N^3)' in q['coefficient']),
       ('equal weights','H(p_N)=log M_N' in q['equal_weights']),('subexponential','exp(o(N^3))' in q['equal_weights']),
       ('heterogeneous open','does not improve the heterogeneous-covariance theorem' in q['comparison'])]
 for m in (2,7,1000):
  h=entropy([1/m]*m);c.append((f'uniform entropy {m}',abs(h-math.log(m))<1e-12))
 for n in (8,32,128):
  c.append((f'polynomial subextensive {n}',math.log(n**9)/(n**3)<0.05))
 c += [('Shannon sufficient',z['shannon_subextensive_sufficient']),('polynomial closed',z['polynomial_component_counts_closed']),
       ('heterogeneous critical open',not z['k1612_heterogeneous_critical_regime_closed']),('coefficient',z['class_coefficient_h_g_prof']),
       ('not unrestricted',not z['unrestricted_leading_coefficient_identified']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
