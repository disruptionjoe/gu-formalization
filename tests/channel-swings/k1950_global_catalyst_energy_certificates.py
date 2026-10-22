"""Finite exact certificates for global energy-penalized catalyst return."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse, hashlib, json, math, warnings
import numpy as np
from scipy.optimize import linprog
from k1943_arbitrary_preparation_catalyst_energy import cell, canonical_paths, rate, shell_witness
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1950-global-catalyst-energy-certificates.json'
INPUTS=['lab/process/k1943-arbitrary-preparation-catalyst-energy.json','tests/channel-swings/k1943_arbitrary_preparation_catalyst_energy.py']
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def rank(rows):
    A=[list(r) for r in rows];r=0
    for j in range(len(A[0])):
        pivot=next((i for i in range(r,len(A)) if A[i][j]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r];z=A[r][j];A[r]=[v/z for v in A[r]]
        for i in range(r+1,len(A)):
            z=A[i][j]
            if z:A[i]=[v-z*w for v,w in zip(A[i],A[r])]
        r+=1
    return r

def verify_record(rec,t,b):
    S=rec['support'];n=len(S);A,rhs,c,eq=cell(t,S,F(0),rec['orientation']);A=A[:-1];rhs=rhs[:-1]
    c=[v+(b*S[i] if i<n else 0) for i,v in enumerate(c)]
    x=list(map(F,rec['x']));y=list(map(F,rec['y']));a=F(rec['intercept'])
    assert len(x)==2*n and len(y)==len(A),'dimensions'
    assert min(x)>=0 and dot(eq,x)==1,'nonnegative normalized primal'
    assert all(dot(row,x)<=0 for row in A),'orientation and deficit constraints'
    assert all(v<=0 for v in y),'dual signs'
    slack=[c[j]-a*eq[j]-sum(y[i]*A[i][j] for i in range(len(A))) for j in range(2*n)]
    assert min(slack)>=0,'dual coefficient domination'
    assert dot(c,x)==a,'exact primal dual equality'
    assert rate(t,S,x[:n])[0]+b*dot(S,x[:n])==a,'actual marginal return plus energy'
    active=[eq]+[row for row,v in zip(A,y) if v<0]+[[F(int(i==j)) for i in range(2*n)] for j,v in enumerate(slack) if v>0]
    return len(A)+2*n+6,rank(active)

def discover(t,b,K):
    rows=[]
    warnings.filterwarnings('ignore',message='Unrecognized options detected')
    for S in canonical_paths(K):
        for o in product((-1,1),repeat=len(S)-1):
            A,rhs,c,eq=cell(t,S,F(0),o);A=A[:-1];rhs=rhs[:-1];n=len(S)
            c=[v+(b*S[i] if i<n else 0) for i,v in enumerate(c)]
            ans=linprog(np.array(c,float),A_ub=np.array(A,float),b_ub=np.array(rhs,float),A_eq=[np.array(eq,float)],b_eq=[1.],bounds=(0,None),method='highs-ds',options={'threads':1})
            assert ans.success,'discovery LP failed'
            cv=lambda v:str(F(float(v)).limit_denominator(10**9))
            rec={'support':S,'orientation':list(o),'x':list(map(cv,ans.x)),'y':list(map(cv,ans.ineqlin.marginals)),'intercept':cv(ans.eqlin.marginals[0])}
            verify_record(rec,t,b);rows.append(rec)
    return {'t':str(t),'slope':str(b),'cutoff':K,'intercept':str(min(F(r['intercept']) for r in rows)),'cells':rows}

def validate(bank):
    checks=0
    for cert in bank:
        t,b,a=map(F,[cert['t'],cert['slope'],cert['intercept']]);K=cert['cutoff']
        expected={(tuple(s),o) for s in canonical_paths(K) for o in product((-1,1),repeat=len(s)-1)}
        actual=[(tuple(r['support']),tuple(r['orientation'])) for r in cert['cells']]
        assert len(actual)==len(set(actual)) and set(actual)==expected,'complete finite path and orientation census'
        assert b>0 and a<=F(1,2)+b and b*K>=a+F(1,2),'global tail domination'
        assert min(F(r['intercept']) for r in cert['cells'])==a,'finite minimum intercept'
        for rec in cert['cells']:
            n,rr=verify_record(rec,t,b);checks+=n
            if b==F(3,20) and F(rec['intercept'])==a:
                assert rr==len(rec['x']),'unique equality preparation in each optimal cell'
                p=list(map(F,rec['x'][:len(rec['support'])]));occupied=[(e,w) for e,w in zip(rec['support'],p) if w]
                assert occupied in [[(1,F(9,10)),(3,F(1,10))],[(1,F(2,5)),(3,F(3,5))]],'only two global equality preparations'
                checks+=2
        checks+=3
    return checks

def consumers():
    rows=[];checks=0;t=F(1,2)
    # Whole first affine segment attained on one finite physical ladder.
    for E in [F(1),F(21,20),F(11,10),F(6,5)]:
        p=[(3-E)/2,(E-1)/2];v,n=shell_witness(t,[1,3],p,list(range(7)))
        assert v==F(3,4)-E/4 and dot([1,3],p)==E
        rows.append({'kind':'attained_first_segment','energy':str(E),'return':str(v),'weights':list(map(str,p))});checks+=n+2
    # The next supporting segment is attained on one connected three-site support.
    for E in [F(11,5),F(9,4),F(23,10),F(19,8)]:
        theta=(E-F(11,5))/(F(19,8)-F(11,5));p=[(1-theta)*a+theta*b for a,b in zip([F(2,5),F(3,5),F(0)],[F(3,8),F(9,16),F(1,16)])]
        v,n=shell_witness(t,[1,3,5],p,list(range(9)))
        assert v==F(15,28)-F(3,28)*E and dot([1,3,5],p)==E
        rows.append({'kind':'attained_third_segment','support':['1','3','5'],'energy':str(E),'return':str(v),'weights':list(map(str,p))});checks+=n+2
    # Exact separated physical approximation to a representative interior infimum.
    E=F(3,2);weight=(F(11,5)-E)/(F(11,5)-F(6,5));target=F(63,100)-F(3,20)*E
    for eps in [F(1,100),F(1,1000),F(1,10000)]:
        energy=E+(2-weight)*eps;scale=(E-1)/(energy-1)
        S=[F(1),1+eps,3+eps,1+2*eps,3+2*eps];p=[1-scale,scale*weight*F(9,10),scale*weight/10,scale*(1-weight)*F(2,5),scale*(1-weight)*F(3,5)]
        A=sorted({F(0),F(1),F(2)}|{F(j)+i*eps for i in [1,2] for j in range(7)})
        actual,n=shell_witness(t,S,p,A)
        assert dot(S,p)==E and actual==scale*target+(1-scale)/2>target
        err=(2-weight)*eps/(E-1+(2-weight)*eps)*(F(1,2)-target)
        assert actual-target==err
        rows.append({'kind':'finite_nonattaining_approximation','energy':str(E),'epsilon':str(eps),'support':list(map(str,S)),'weights':list(map(str,p)),'physical_spectrum':list(map(str,A)),'return':str(actual),'infimum':str(target),'gap':str(err)});checks+=n+3
    return rows,checks

def produce(write=False):
    if write:bank=[discover(F(1,2),F(1,4),5),discover(F(1,2),F(3,20),8),discover(F(1,2),F(3,28),11)]
    else:bank=json.loads(OUT.read_text())['global_duals']
    checks=validate(bank);rows,n=consumers();checks+=n
    return {'result_id':'K1950','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','global_duals':bank,'consumers':rows,'exact_controls':checks,'sharp_segments':[{'energies':['1','6/5'],'intercept':'3/4','slope':'1/4','attainment':'finite'}, {'energies':['6/5','11/5'],'intercept':'63/100','slope':'3/20','attainment':'endpoints finite; interior infimum not attained in finite nondegenerate class'}, {'energies':['11/5','19/8'],'intercept':'15/28','slope':'3/28','attainment':'finite'}],'scope':'Fixed exact extreme Schur channel, t=1/2 faithful four-level bath; arbitrary finite nondegenerate nonnegative catalyst spectra and coherent preparations by pinching. No all-energy evaluated formula or native GU result.','inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS}}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=produce(a.write)
    if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
    else:assert v==json.loads(OUT.read_text()),'certificate drift'
    print('PASS K1950',v['exact_controls'],'exact controls;',sum(len(b['cells']) for b in v['global_duals']),'global dual cells')
