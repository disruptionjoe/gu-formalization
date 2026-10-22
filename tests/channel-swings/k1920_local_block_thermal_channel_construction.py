#!/usr/bin/env python3
"""Exact finite block mass and full-channel error accounting."""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2];REPORT=ROOT/'lab/process/k1920-local-block-thermal-channel-construction.json'
def mass(n,q):
    left=3**n//2**n;out=Q(0)
    for j in range(n+1):
        take=min(left,comb(n,j)*2**j);out+=take*(q/2)**j*(1-q)**(n-j);left-=take
        if not left:return out
    raise AssertionError('support count')
def partition(N,b):
    assert N>=b>=1
    m,r=divmod(N,b);out=[b]*m;out[-1]+=r;return out

def payload():
    checks=[]
    def check(ok,label):assert ok,label;checks.append(label)
    for N,b in [(10,3),(12,3),(19,10),(600001,600)]:
        parts=partition(N,b);check(sum(parts)==N and min(parts)>=b and max(parts)<2*b,'full partition '+str(N))
    for n in range(1,7):
        slots=3**n//2**n;check(2**n*slots<=3**n<2**n*(slots+1),'support embedding '+str(n))
        p=mass(n,Q(1,21));check(0<p<1,'faithful tail '+str(n))
        for m in [2,5]:check(1-p**m<=m*(1-p),'whole-channel mixture '+str((n,m)))
    p=mass(600,Q(1,21));e=1-p
    check(e<Q(1,100000000),'b600 tail <1e-8')
    check(1000*e<Q(1,100000),'N600000 whole-block error <1e-5')
    check(1000*e/p<Q(1,99999),'alternative total D <1/99999')
    dep='explorations/conditional-build/k1918-collective-thermal-preparation-threshold-2026-10-22.md'
    return dict(result_id='K1920',status='active_research',evidence_kind='analytic block synthesis/concentration plus exact rational finite controls',mathematical_controls=checks,finite_example=dict(b=600,N=600000,blocks=1000,q='1/21',mass=str(p),tail=str(e),tail_decimal_for_orientation=float(e),error_upper='1/100000',preparation_D_upper='1/99999'),dependencies={dep:hashlib.sha256((ROOT/dep).read_bytes()).hexdigest()},gate_model='arbitrary U(12) and adjacent U(144), continuous controls, no energy conservation restriction',bounds=dict(equal_blocks_gates='O(N*144^b)',unequal_blocks_gates='O(N*144^(2b))',gate_error='tail+G*epsilon'),not_claimed=['fixed depth','energy conserving control','practical efficiency','finite gate-set compilation','native GU','novelty'])
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=payload()
    if a.write:REPORT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert json.loads(REPORT.read_text())==r,'report consistency'
    print('PASS K1920 finite controls',len(r['mathematical_controls']),'; tail',r['finite_example']['tail_decimal_for_orientation'])
