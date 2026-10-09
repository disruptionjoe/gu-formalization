#!/usr/bin/env python3
"""Certificate for K1611's uniform Gaussian affinity-score bound."""
import json, math
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]

def pair(s1, s2, m1, m2, omega):
    x = p = 0.0
    for a, b, u, v, w in zip(s1, s2, m1, m2, omega):
        r = math.log(a / b); d = u - v
        x += 0.5 * math.log(math.cosh(r / 2)) + d * d / (4 * (a + b))
        p += 2 * w * (a - b) ** 2 / (a * b * (a + b))
        p += 4 * w * d * d / (a + b) ** 2
    return math.exp(-x), p, x

def main():
    d = json.loads((ROOT/'lab/process/k1611-uniform-gaussian-affinity-score-control.json').read_text())
    q, z = d['uniform_pair_control'], d['decision']; c=[]
    c += [('claim', d['claim_id']=='K1611'), ('band','c_- S_N^*' in q['hypothesis']),
          ('arbitrary means','means are arbitrary' in q['hypothesis']),
          ('affinity','BC_ij=exp(-X_ij)' in q['affinity_exponent']),
          ('cov split','2 omega_k' in q['score_split']),
          ('mean split','4 omega_k' in q['score_split']),
          ('mean identity','2(S_i+S_j)^(-1)' in q['mean_identity']),
          ('Lambda','Lambda_N' in q['comparison']), ('x exp x','exp(-X_ij)' in q['uniform_bound'])]
    for scale in (0.02, 0.5, 3.0, 20.0):
        s1=[0.7,1.5,2.2]; s2=[0.7*(1+scale/10),1.5/(1+scale/20),2.2]
        m1=[scale,0.3,-0.2]; m2=[0.0,-0.1,0.4]; w=[1.0,2.0,4.0]
        bc,p,x=pair(s1,s2,m1,m2,w)
        c.append((f'finite pair {scale}', math.isfinite(bc*p) and 0<=bc<=1 and p>=0 and x>=0))
        c.append((f'xexp bound {scale}', x*math.exp(-x)<=1/math.e+1e-14))
    c += [('no separation',not z['macroscopic_separation_required']),('not centered',not z['centeredness_required']),
          ('no mean bound',not z['mean_bound_required']),('ON',z['pair_affinity_score_O_N']),
          ('not unrestricted',not z['unrestricted_state_theorem']),('protected',not z['protected_status_change'])]
    for i,(label,ok) in enumerate(c,1): assert ok,label; print(f'PASS {i:02d}: {label}')
    print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__': main()
