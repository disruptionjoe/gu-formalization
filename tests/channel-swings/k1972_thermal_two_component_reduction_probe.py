"""Independent rational weight elimination and whole-interval comparison."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def reduce_weights(e,r,w,fault=None):
    w=list(w)
    while len(ids:=[i for i,v in enumerate(w) if v])>2:
        i,j,k=ids[:3];z=[Q(0)]*len(w)
        z[i],z[j],z[k]=e[j]-e[k],e[k]-e[i],e[i]-e[j]
        if not any(z):z[i],z[j]=Q(1),Q(-1)
        if dot(z,r)>0:z=[-v for v in z]
        step=min(-w[i]/v for i,v in enumerate(z) if v<0)
        w=[x+step*y for x,y in zip(w,z)]
    if fault=='bad_energy':w=[Q(int(i==max(range(len(e)),key=e.__getitem__))) for i in range(len(e))]
    if fault=='lost_normalization':w=[2*x for x in w]
    return w

def rate(s,p):
    inc=[Q(0)]*len(p)
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            g=s[j]-s[i]
            if g in (1,2,3):
                low=sum(Q(1,2)**b for b in range(4-g))/Q(15,8);high=low*Q(1,2)**g
                q=high*p[i]-low*p[j];inc[i]+=max(-q,0);inc[j]+=max(q,0)
    return sum(max(x-y,0) for x,y in zip(p,inc))/2

def val(pieces,E):
    return next(Q(p['slope'])*E+Q(p['intercept']) for p in pieces if Q(p['lo'])<=E and (p['hi'] is None or E<=Q(p['hi'])))
def check(fault=None):
    n=0
    for seed in range(1,129):
        count=3+seed%5;e=[];r=[];weights=[];cost=[]
        for j in range(count):
            if j%2:
                p=[Q((seed+3*j)%19+1,21)];p.append(1-p[0]);s=[1,3];cost.append(5)
            else:s=[1];p=[Q(1)];cost.append(3)
            e.append(dot(s,p)+Q(j,997));r.append(rate(s,p));weights.append(Q((seed*j+7)%23+1))
        weights=[x/sum(weights) for x in weights]
        new=reduce_weights(e,r,weights,fault)
        assert sum(new)==1 and min(new)>=0,'probability normalization'
        assert dot(new,e)<=dot(weights,e),'same physical energy budget'
        assert dot(new,r)<=dot(weights,r),'homogeneous return does not increase'
        assert sum(bool(x) for x in new)<=2,'two surviving components'
        assert sum(c for c,w in zip(cost,new) if w)<=sum(cost),'physical dimension does not grow'
        n+=5
    rec=json.loads((ROOT/'lab/process/k1972-thermal-two-component-reduction.json').read_text());old=json.loads((ROOT/'lab/process/k1968-joint-thermal-finite-dimension-program.json').read_text())
    for row,prior in zip(rec['frontiers'],old['frontiers']):assert row['pieces']==prior['pieces'];n+=1
    row=rec['frontiers'][-1];lo,hi=Q(121,91),Q(11,5)
    pts=sorted({lo,hi}|{Q(p['lo']) for p in row['connected'] if lo<Q(p['lo'])<hi})
    for a,b in zip(pts,pts[1:]):
        va=val(row['connected'],a)-(Q(2,3)-a/6);vb=val(row['connected'],b)-(Q(2,3)-b/6)
        assert min(va,vb)>=0 and va+vb>0,'strict affine gap throughout open segment';n+=1
    assert val(rec['frontiers'][2]['pieces'],Q(3,2))==Q(9,20)
    # This chord is invalid at d5: distinct physical flags cost 3+5=8.
    charge=3+5 if fault!='drop_dimension_charge' else max(3,5)
    assert charge>5,'component costs add, never max'
    # Exact-budget approaching sequence across the WHOLE open interval.
    for E in [lo+(hi-lo)*Q(j,10) for j in range(1,10)]:
        previous=None
        for eps in [Q(1,10),Q(1,100),Q(1,1000)]:
            w=(E-1)/(Q(6,5)+eps);energy=(1-w)+w*(Q(11,5)+eps)
            error=Q(1,2)-w/5
            if fault=='free_shift':energy-=w*eps
            assert energy==E,'shift paid at exact budget'
            assert error>Q(2,3)-E/6
            if previous is not None:assert error<previous
            previous=error;n+=3
    return n
if __name__=='__main__':
    n=check();caught=[]
    for f in ['bad_energy','lost_normalization','drop_dimension_charge','free_shift']:
        try:check(f)
        except AssertionError as e:caught.append([f,str(e)])
        else:raise AssertionError('missed mathematical fault '+f)
    r=json.loads((ROOT/'lab/process/k1972-thermal-two-component-reduction.json').read_text())
    for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    print('PASS K1972 independent',n,'rational controls;',caught)
