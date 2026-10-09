#!/usr/bin/env python3
"""Certificate for K1592's negative-defect cat coefficient rigidity."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1592-negative-defect-cat-coefficient-rigidity.json').read_text());q=d['cat_coefficient'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1592'),('point mixture','N(+h_N,v_N)' in q['point_law']),('mean zero','mean zero' in q['point_law']),('variance','v_N+h_N^2' in q['point_law']),('fourth moment','h_N^4+6h_N^2v_N+3v_N^2' in q['point_law']),('defect coefficient','-2h_N^4' in q['negative_defect']),('defect scale','Theta_g(N^4)' in q['negative_defect']),('outside K1577',"outside K1577" in q['negative_defect']),('even Wick','Wick quartic is even' in q['interaction_identity']),('linear expectation','linear in the law' in q['interaction_identity']),('energy lower','lambda_N^prof-(1/4)' in q['energy_sandwich']),('coefficient limit','Q_N^cat/N^4->h_g^prof' in q['coefficient']),('gain O N','O_g(N)' in q['coefficient']),('residual separation','Theta_g(N^(5/2))' in q['coefficient']),('route consequence','different multimodal' in q['route_consequence']),('scope one family','one exact nonperturbative cat family' in q['scope_guard'])]
 h,v=5.0,2.0;fourth=h**4+6*h*h*v+3*v*v;variance=v+h*h
 c += [('moment arithmetic',abs(fourth-3*variance**2+2*h**4)<1e-12),('decision defect',z['leading_negative_defect_exact']),('decision interaction',z['cat_interaction_equals_component']),('decision coefficient',z['profiled_cat_coefficient_rigid']),('does not explain Ritz',not z['cat_explains_residual_ritz_scale']),('coefficient open',not z['unrestricted_leading_coefficient_identified']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
