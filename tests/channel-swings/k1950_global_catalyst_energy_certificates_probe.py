"""Independent bath-weight LP reconstruction, tail tests and input mutations."""
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
from copy import deepcopy
import hashlib,json
ROOT=Path(__file__).resolve().parents[2];REPORT=ROOT/'lab/process/k1950-global-catalyst-energy-certificates.json'
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def independent_paths(K):
    ans=[]
    for n in range(1,K+1):
        for s in combinations(range(1,K+1),n):
            ds=[b-a for a,b in zip(s,s[1:])]
            if not ds:
                if s==(1,):ans.append(s)
            elif s[0]==max(1,3-ds[0]) and all(d in [1,2,3] for d in ds) and all(a+b>=4 for a,b in zip(ds,ds[1:])):ans.append(s)
    return ans

def independent_cell(s,o,t,b):
    n=len(s);bath=[t**j/sum(t**i for i in range(4)) for j in range(4)];inc=[[F(0)]*n for _ in s];rows=[]
    for i,sgn in enumerate(o):
        j=i+1;edge=[F(0)]*n
        # Enumerate coincident bath labels, instead of using geometric-series coefficients.
        for low in range(4):
            for high in range(4):
                if s[i]+low==s[j]+high:edge[i]+=bath[low];edge[j]-=bath[high]
        rows.append([-sgn*v for v in edge]+[F(0)]*n)
        receiver=j if sgn==1 else i
        inc[receiver]=[v+sgn*w for v,w in zip(inc[receiver],edge)]
    rows += [[F(int(i==j))-inc[i][j] for j in range(n)]+[F(-int(i==j)) for j in range(n)] for i in range(n)]
    return rows,[b*e for e in s]+[F(1,2)]*n,[F(1)]*n+[F(0)]*n

def rank(a):
    a=[list(r) for r in a];r=0
    for j in range(len(a[0])):
        p=next((i for i in range(r,len(a)) if a[i][j]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r];pivot=a[r][j]
        for i in range(r+1,len(a)):
            z=a[i][j]
            a[i]=[pivot*x-z*y for x,y in zip(a[i],a[r])]
        r+=1
    return r

def shell_return(t,s,p):
    # Homogeneous bath-label method; zero populations stay to test removal directly.
    bath=[t**j/sum(t**i for i in range(4)) for j in range(4)];returned={e:F(0) for e in s}
    for e in {x+j for x in s for j in range(4)}:
        inputs=[(p[i]*bath[j],x) for i,x in enumerate(s) for j in range(4) if x+j==e]
        assert len(inputs)<=2,'physical occupied shell rank'
        greatest=max(w for w,x in inputs)
        for w,x in inputs:returned[x]+=greatest/2
    return sum(max(F(0),w-returned[x]) for x,w in zip(s,p))

def audit(v,math_only=False):
    count=0
    if not math_only:
        assert v['result_id']=='K1950','report identity'
        for p,h in v['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'input pin'
    for bank in v['global_duals']:
        t,b,a=map(F,[bank['t'],bank['slope'],bank['intercept']]);K=bank['cutoff']
        expected={(s,o) for s in independent_paths(K) for o in product([-1,1],repeat=len(s)-1)}
        keys=[(tuple(x['support']),tuple(x['orientation'])) for x in bank['cells']]
        assert len(keys)==len(set(keys)) and set(keys)==expected,'independent exhaustive cell census'
        assert b>0 and b*K-a-F(1,2)>=0,'tail coefficient pays every removed energy'
        for rec in bank['cells']:
            s=rec['support'];n=len(s);A,c,eq=independent_cell(s,rec['orientation'],t,b);x=list(map(F,rec['x']));y=list(map(F,rec['y']));a0=F(rec['intercept'])
            assert len(x)==len(c) and len(y)==len(A),'dimensions'
            assert min(x)>=0 and dot(eq,x)==1 and all(dot(r,x)<=0 for r in A),'actual primal restrictions'
            assert max(y)<=0,'dual sign'
            slack=[c[j]-a0*eq[j]-sum(r[j]*z for r,z in zip(A,y)) for j in range(2*n)]
            assert min(slack)>=0 and dot(c,x)==a0>=a,'independently reconstructed dual bound'
            assert shell_return(t,s,x[:n])+b*dot(s,x[:n])==a0,'direct bath return'
            if b==F(3,20) and a0==a:
                active=[eq]+[r for r,z in zip(A,y) if z<0]+[[F(int(i==j)) for i in range(2*n)] for j,z in enumerate(slack) if z>0]
                assert rank(active)==2*n,'equality face unique'
                assert [(e,p) for e,p in zip(s,x) if p] in [[(1,F(9,10)),(3,F(1,10))],[(1,F(2,5)),(3,F(3,5))]],'equality population endpoints'
                count+=2
            count+=6
        count+=2
    for rec in v['consumers']:
        E=F(rec['energy']);p=list(map(F,rec['weights']));s=list(map(F,rec.get('support',[1,3])))
        assert sum(p)==1 and dot(s,p)==E,'actual physical mean energy'
        assert shell_return(F(1,2),s,p)==F(rec['return']),'independent physical shell return'
        if rec['kind']=='finite_nonattaining_approximation':assert F(rec['return'])-F(rec['infimum'])==F(rec['gap'])>0,'strict finite gap'
        count+=3
    return count

def main():
    v=json.loads(REPORT.read_text());count=audit(v)
    # The analytic tail lemma is not proved by samples; these stress its actual boundary terms.
    for t in [F(1,4),F(1,2),F(3,4)]:
        for s in [[1,3,5,7],[2,3,6,7],[1,4,5,8]]:
            for weights in [(1,2,3,4),(7,1,1,1),(1,1,1,7)]:
                p=[F(w,sum(weights)) for w in weights];r=shell_return(t,s,p)
                for n in range(1,len(s)):
                    low=shell_return(t,s[:n],p[:n]);delta=sum(p[n:])
                    assert r>=low-delta/2,'unnormalized tail inequality';count+=1
    print('PASS K1950 independent baseline',count,'exact controls')
    faults=[]
    for fault in ['dual','population','slope','multiplier']:
        w=deepcopy(v);rec=w['global_duals'][1]['cells'][0]
        if fault=='dual':rec['intercept']=str(F(rec['intercept'])+1)
        if fault=='population':rec['x'][0]=str(F(rec['x'][0])+F(1,100))
        if fault=='slope':w['global_duals'][1]['slope']='1/100'
        if fault=='multiplier':rec['y'][0]='1'
        try:audit(w,True)
        except AssertionError as ex:faults.append(str(ex))
        else:raise AssertionError('undetected mathematical fault '+fault)
    reporting=[]
    for fault in ['identity','pin']:
        w=deepcopy(v)
        if fault=='identity':w['result_id']='K0'
        else:w['inputs'][next(iter(w['inputs']))]='0'*64
        try:audit(w)
        except AssertionError as ex:reporting.append(str(ex))
        else:raise AssertionError('undetected reporting fault')
    print('PASS mathematical faults',faults,'; report/pin faults',reporting)
if __name__=='__main__':main()
