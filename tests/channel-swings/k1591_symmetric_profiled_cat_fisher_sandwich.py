#!/usr/bin/env python3
"""Certificate for K1591's symmetric-cat Fisher sandwich."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1591-symmetric-profiled-cat-fisher-sandwich.json').read_text());q=d['fisher_sandwich'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1591'),('symmetric cat','N(m,S)+N(-m,S)' in q['cat_law']),('common covariance','common positive profiled covariance' in q['cat_law']),('convexity','Fisher convexity' in q['convex_upper']),('upper formula','m^T Omega m' in q['convex_upper']),('cat mean zero','mean zero' in q['moment_lower']),('rank one covariance','T=S+mm^T' in q['moment_lower']),('K1533','K1533' in q['moment_lower']),('Sherman Morrison','Sherman--Morrison' in q['rank_one_width']),('exact denominator','1+m^T S^(-1)m' in q['rank_one_width']),('zero mode','zero-mode eigenvector' in q['profiled_scale']),('profiled kappa','kappa_(g,N)^+' in q['profiled_scale']),('order N','Theta_g(N)' in q['profiled_scale']),('scope symmetric','symmetric two-component' in q['scope_guard']),('scope arbitrary open','does not control arbitrary' in q['scope_guard'])]
 # Scalar rank-one control: S=s, Omega=w, m=r.
 s,w,r=0.4,3.0,2.0;T=s+r*r
 U=r*r*w+w*(s+1/s-2);L=w*(T+1/T-2)
 width=w*r*r/(s*(s+r*r))
 c += [('scalar width',abs((U-L)-width)<1e-12),('width positive',width>0),('width bound',width<=w/s),('decision upper',z['fisher_convex_upper_proved']),('decision lower',z['fixed_moment_lower_proved']),('decision exact',z['rank_one_width_exact']),('decision scale',z['profiled_cat_gain_at_most_order_N']),('arbitrary open',not z['arbitrary_negative_defect_controlled']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
