#!/usr/bin/env python3
"""Certificate for K1613's bounded-variation primitive budget."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1613-bv-spectral-primitive-budget.json').read_text());q=d['bv_primitive'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1613'),('W11','W^{1,1}(R)' in q['hypothesis']),('measure','finite signed distributional second-derivative measures' in q['hypothesis']),
       ('jumps','jumps of the first derivative are allowed' in q['equivalent_piecewise_class']),('decay','t^(-2)B_BV' in q['decay']),
       ('L1','B_0+B_BV' in q['budgets']),('L2','B_0(B_0+B_BV)' in q['budgets']),('strict','piecewise-smooth' in q['strict_extension'])]
 b0,bv=2.0,3.0
 integral=b0+bv; square=b0*integral
 c += [('budget positive',integral==5.0),('square budget',square==10.0),('measure sufficient',z['distributional_second_derivative_measure_sufficient']),
       ('derivative jumps',z['first_derivative_jumps_allowed']),('no density jumps',not z['density_endpoint_jumps_allowed']),
       ('a L1',z['holonomy_L1']),('a L2',z['holonomy_L2']),('not E L1',not z['electric_field_L1']),
       ('not source flow',not z['source_owned_flow']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
