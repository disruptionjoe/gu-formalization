#!/usr/bin/env python3
"""Independent Fraction response inversion and genuine coefficient fault controls."""
from fractions import Fraction as F
from pathlib import Path
import json,copy
ROOT=Path(__file__).resolve().parents[2]

def inv2(a):
    d=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]
def pair(c,a,d):return sum(c[i]*a[i][j]*d[j] for i in range(2) for j in range(2))
def witness_ok(d):
    a,b=map(F,d['masses_squared']);c=list(map(F,d['source']));o=list(map(F,d['readout']))
    return a>0 and b>0 and a!=b and c[0]*o[0]/a+c[1]*o[1]/b==0 and c[0]*o[0]/(1+a)+c[1]*o[1]/(1+b)!=0

def main():
    n=0
    def ck(v):
        nonlocal n
        assert v;n+=1
    for h in range(1,7):
        K=[[F(h+1),F(1)],[F(1),F(h+2)]]
        M=[[F(3),F(1)],[F(1),F(1)]]
        last=None
        for z in [F(0),F(1,10),F(1),F(10)]:
            G=inv2([[z*K[i][j]+M[i][j] for j in range(2)] for i in range(2)])
            for c in [[F(1),F(2)],[F(-2),F(1)],[F(0),F(1)]]:
                ck(pair(c,G,c)>0)
            val=pair([F(1),F(2)],G,[F(1),F(2)])
            if last is not None:ck(val<last)
            last=val
    for a,b in [(F(1),F(4)),(F(2),F(7)),(F(3,2),F(1,4))]:
        for z in [F(0),F(1,3),F(1),F(20)]:
            v=1/(z+a)-b/a/(z+b)
            ck(v==(a-b)*z/(a*(z+a)*(z+b)))
            ck(1/(z+a)-1/a==-z/(a*(z+a)))
        ck(1/a+(-b/a+F(1,100))/b==F(1,100)/b)
    report=json.loads((ROOT/'lab/process/k1844-screening-positive-response.json').read_text())
    ck(witness_ok(report['cross_readout_fixture']))
    # Baseline above must pass before mutations of the actual fixture.
    mathematical_faults=0
    for field,idx,value in [('readout',1,-3),('masses_squared',1,5),('source',0,2)]:
        w=copy.deepcopy(report['cross_readout_fixture']);w[field][idx]=value
        ck(not witness_ok(w));mathematical_faults+=1
    def scope_ok(r):return r['scope']=='conditional_positive_quadratic_scalar_action' and not any(r[k] for k in ['static_is_late_limit','signed_cross_residue_is_ghost','source_owned','all_screening_excluded','ledger_changes'])
    ck(scope_ok(report));reporting=0
    for field in ['static_is_late_limit','signed_cross_residue_is_ghost','source_owned','all_screening_excluded','ledger_changes']:
        r=copy.deepcopy(report);r[field]=True;ck(not scope_ok(r));reporting+=1
    print(f'K1844 independent rational checks {n}; mathematical faults {mathematical_faults}; reporting faults {reporting}')
if __name__=='__main__':main()
