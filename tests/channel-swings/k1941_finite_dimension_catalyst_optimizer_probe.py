"""Independent exhaustive set cover and oriented-shell return checks."""
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
import json,hashlib
import sympy as sy
import k1941_finite_dimension_catalyst_optimizer as p

def brute_cover(S):
    S=set(S);shells={s+b for s in S for b in range(4)};pool=sorted({e-b for e in shells for b in range(4)}-S)
    for size in range(len(pool)+1):
        for extra in combinations(pool,size):
            A=S|set(extra)
            if all(sum(e-b in A for b in range(4))>=2*sum(e-b in S for b in range(4)) for e in shells):return len(A)
    return None

def independent_reward(t,ds):
    n=len(ds)+1;Z=sum(t**i for i in range(4));coeff=[(sum(t**b for b in range(4-d))/Z,sum(t**b for b in range(d,4))/Z) for d in ds]
    best=0
    for mask in product((0,1),repeat=n-1):
        T=sy.zeros(n)
        for i in range(n):T[i,i]=sy.Rational(1-(coeff[i-1][0] if i else 0)-(coeff[i][1] if i<n-1 else 0))/2
        for i,side in enumerate(mask):
            L,H=coeff[i];j=i+side;w=H if side==0 else L
            T[i,j]+=sy.Rational(w)/2;T[i+1,j]+=sy.Rational(w)/2
        rewards=sy.ones(1,n)*(sy.eye(n)-T).inv();best=max(best,*rewards)
    return F(1)/F(best)

def checks(cover=None):
    cover=cover or p.completion;count=0
    for n in range(1,4):
        for ds in product((1,2,3),repeat=n-1):
            S=p.support_of(ds);A=cover(S);want=brute_cover(S)
            assert (len(A) if A else None)==want,'minimum interval-cover cardinality';count+=1
    for n in range(1,5):
        for ds in p.paths(n):
            for t in [F(1,2),F(3,4),F(9,10)]:
                r=independent_reward(t,ds);assert r==min(p.rooted(t,ds,i)[0] for i in range(n)),'all-orientation visit lower bound';count+=1
    # Check complete dimension optimizer by independent cover + orientation minima.
    for t in [F(1,2),F(3,4)]:
        for D in range(3,9):
            candidates=[]
            for n in range(1,(D-1)//2+1):
                for ds in p.paths(n):
                    if brute_cover(p.support_of(ds))<=D:candidates.append(independent_reward(t,ds))
            assert p.optimize(t,D)['rate']==min(candidates),'independent physical-D optimizer';count+=1
    return count

def detect(fn,label):
    try:fn()
    except AssertionError as e:print('DETECTED',label,':',e);return
    raise AssertionError('undetected '+label)

def report_check(r):
    assert r['source_sha256']==hashlib.sha256(Path(p.__file__).read_bytes()).hexdigest(),'producer pin'
    assert r==p.calculate(),'report replay'

if __name__=='__main__':
    print('PASS',checks(),'independent exact controls')
    r=json.loads(p.REPORT.read_text());report_check(r);print('PASS clean producer/report baseline')
    detect(lambda:checks(lambda S:p.completion(S,'earliest')),'wrong interval endpoint')
    detect(lambda:p.calculate('phase'),'complex phase input')
    detect(lambda:p.calculate('rate'),'physical rate input')
    bad=json.loads(json.dumps(r));bad['optima'][0]['rate']='0';detect(lambda:report_check(bad),'report consistency')
    bad=json.loads(json.dumps(r));bad['source_sha256']='0'*64;detect(lambda:report_check(bad),'pin consistency')
