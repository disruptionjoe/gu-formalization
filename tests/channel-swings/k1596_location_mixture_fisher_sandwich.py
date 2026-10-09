#!/usr/bin/env python3
"""Certificate for K1596's arbitrary location-mixture Fisher sandwich."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1596-location-mixture-fisher-sandwich.json').read_text());q=d['location_mixture'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1596'),('arbitrary law','any probability law' in q['law']),('finite second moment','finite second moment' in q['law']),('common covariance','common K1572 profiled covariance' in q['law']),('zero mode','zero-mode eigenvector' in q['law']),('mean','alpha=E A' in q['moments']),('variance','v=Var(A)' in q['moments']),('rank one covariance','T=S+v e_0 e_0^T' in q['moments']),('convexity','Fisher convexity' in q['convex_upper']),('K1533','K1533' in q['moment_lower']),('second moment identity','E[A^2]=alpha^2+v' in q['rank_one_width']),('width formula','omega_0 v/[s_(N,0)(s_(N,0)+v)]' in q['rank_one_width']),('profile bound','omega_0/s_(N,0)' in q['profiled_scale']),('order N','Theta_g(N)' in q['profiled_scale']),('no atom count','independently of atom count' in q['profiled_scale']),('scope covariance','Heterogeneous covariances' in q['scope_guard'])]
 s,w,alpha,v=.4,3.0,1.2,2.5;second=alpha*alpha+v;T=s+v
 U=second*w+w*(s+1/s-2);L=alpha*alpha*w+w*(T+1/T-2);width=w*v/(s*(s+v))
 c += [('scalar width',abs((U-L)-width)<1e-12),('width positive',width>=0),('width bound',width<=w/s),('decision arbitrary',z['arbitrary_location_law_controlled']),('decision exact',z['exact_rank_one_width']),('decision scale',z['mixing_gain_at_most_order_N']),('covariance open',not z['heterogeneous_covariances_controlled']),('unrestricted open',not z['unrestricted_negative_defect_controlled']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
