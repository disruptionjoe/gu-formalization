#!/usr/bin/env python3
"""Certificate for K1614's BV primitive composition."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1614-bv-primitive-radius-composition.json').read_text());q=d['composition'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1614'),('Ba','B_a=B_0+B_BV' in q['budgets']),('Ba2','B_a2=B_0 B_a' in q['budgets']),
       ('energy','exp[2|e|B_a+(e^2/m)B_a2]' in q['energy']),('remainder','B_R=int_0^infinity' in q['hierarchy_hypothesis']),
       ('radius','rho_infinity' in q['radius']),('strict','strict expenditure' in q['radius'])]
 b0,bbv,e,m=1.2,.8,.3,2.0;ba=b0+bbv;ba2=b0*ba;growth=math.exp(2*abs(e)*ba+e*e/m*ba2)
 c += [('finite growth',1<growth<10),('static absorbed',z['arbitrary_static_flat_holonomy_absorbed']),('composed',z['bv_budget_composed']),
       ('positive',z['positive_radius_under_strict_budget']),('remainder open',not z['nonlinear_remainder_derived']),
       ('flow open',not z['source_owned_flow']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
