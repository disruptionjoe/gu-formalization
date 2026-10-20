#!/usr/bin/env python3
"""Independent standard-library rational polynomial/Sturm and interval replay."""
from fractions import Fraction as F
from pathlib import Path
from math import prod
import json,copy
ROOT=Path(__file__).resolve().parents[2]
def trim(p):
    p=list(map(F,p))
    while len(p)>1 and not p[-1]:p.pop()
    return p
def add(p,q):return trim([(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0) for i in range(max(len(p),len(q)))])
def scale(p,c):return trim([v*c for v in p])
def mul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return trim(r)
def der(p):return trim([i*p[i] for i in range(1,len(p))] or [0])
def ev(p,x):
    v=F(0)
    for a in reversed(p):v=v*x+a
    return v
def rem(p,q):
    p=trim(p);q=trim(q)
    while len(p)>=len(q) and p!=[0]:
        h=len(p)-len(q);a=p[-1]/q[-1]
        p=add(p,[F(0)]*h+scale(q,-a))
    return p
def sturm(p):
    seq=[trim(p),der(p)]
    while seq[-1]!=[0]:
        r=scale(rem(seq[-2],seq[-1]),-1)
        if r==[0]:break
        r=scale(r,1/abs(r[-1]));seq.append(r)
    return seq
def variation(seq,x):
    vs=[p[-1] if x is None else ev(p,x) for p in seq]
    signs=[1 if v>0 else -1 for v in vs if v]
    return sum(a!=b for a,b in zip(signs,signs[1:]))
def roots(p,a,b):
    st=sturm(p);return variation(st,a)-variation(st,b)
def lower_cert(cfg):
    a,b,d,c,e=map(F,cfg['score']);A,B,C=map(F,cfg['minorant'])
    N=[a,b,d];D=[F(1),c,e];Y=[F(0),F(1)]
    h=add(add(scale(mul(N,D),2),scale(mul(Y,add(mul(der(N),D),scale(mul(N,der(D)),-1))),4)),scale(mul(Y,mul(N,N)),-1))
    P=add(h,scale(mul([A,B,C],mul(D,D)),-1))
    return c>0 and e>0 and P[0]>0 and roots(P,F(0),None)==0,P,A+B+2*C

def gm(n):return F(prod(range(1,2*n,2)))
def matrices(cfg):
    co=[[F(0),F(1)] if v=='t' else [F(v)] for v in cfg['primal']]
    n=len(co);Z=M=Q=E=[F(0)]
    for i in range(n):
        for j in range(n):
            term=mul(co[i],co[j])
            Z=add(Z,scale(term,gm(i+j)))
            M=add(M,scale(term,gm(i+j+1)))
            Q=add(Q,scale(term,gm(i+j+2)))
            energy=(16*i*j*gm(i+j-1) if i*j else 0)-4*(i+j)*gm(i+j)+gm(i+j+1)
            E=add(E,scale(term,energy))
    return Z,M,Q,E

def ibound(p,lo,hi):
    # Horner interval arithmetic, distinct from the producer's termwise bound.
    a=b=F(0)
    for c in reversed(p):
        corners=[a*lo,a*hi,b*lo,b*hi];a=min(corners)+c;b=max(corners)+c
    return a,b

def primal_cert(cfg,upper):
    Z,M,Q,E=matrices(cfg);T=add(mul(Q,Z),scale(mul(M,M),-2));lo,hi=map(F,cfg['root_interval'])
    if not (0<lo<hi and ev(T,lo)*ev(T,hi)<0 and roots(T,lo,hi)==1):return False,T,None
    zl,zh=ibound(Z,lo,hi);ml,mh=ibound(M,lo,hi);el,eh=ibound(E,lo,hi)
    if min(zl,ml,el)<=0:return False,T,None
    bound=eh*mh/zl**2
    return bound<upper,T,bound

def main():
    r=json.loads((ROOT/'lab/process/k1845-fisher-certified-moment-bounds.json').read_text());cfg=r['certificate'];n=0
    def ck(v):
        nonlocal n
        assert v;n+=1
    # Sturm planted-positive and known counts before relying on absence.
    ck(roots([-1,0,1],F(0),None)==1)
    ck(roots([1,0,1],F(0),None)==0)
    ck(roots([2,-3,1],F(0),None)==2)
    ok,P,L=lower_cert(cfg);ck(ok);ck(L==F(r['lower']))
    ck(P==list(map(F,r['residual_polynomial_low_to_high'])))
    ok,T,U=primal_cert(cfg,F(r['upper']));ck(ok)
    ck(T==list(map(F,r['moment_polynomial_low_to_high'])))
    ck(F(r['lower'])<U<F(r['upper']))
    ck(F(r['upper'])-F(r['lower'])==F(243,200000))
    # Rational fixtures independently test cleared denominator and moments.
    a,b,d,c,e=map(F,cfg['score']);A,B,C=map(F,cfg['minorant'])
    for y in [F(0),F(1,10),F(1),F(2),F(10),F(100)]:
        N=a+b*y+d*y*y;D=1+c*y+e*y*y
        H=2*N/D+4*y*((b+2*d*y)*D-N*(c+2*e*y))/D**2-y*N*N/D**2
        ck(H-A-B*y-C*y*y==ev(P,y)/D**2);ck(ev(P,y)>0)
    # Baseline passed. Mutate certificate inputs, never the checks.
    faults=0
    dcfg=copy.deepcopy(cfg);dcfg['minorant'][0]=str(F(cfg['minorant'][0])+F(1,10));ck(not lower_cert(dcfg)[0]);faults+=1
    dcfg=copy.deepcopy(cfg);dcfg['score'][0]='-2';ck(not lower_cert(dcfg)[0]);faults+=1
    dcfg=copy.deepcopy(cfg);dcfg['primal'][2]='1/20';ck(not primal_cert(dcfg,F(r['upper']))[0]);faults+=1
    dcfg=copy.deepcopy(cfg);dcfg['root_interval']=['1/10','1/5'];ck(not primal_cert(dcfg,F(r['upper']))[0]);faults+=1
    ck(not primal_cert(cfg,F(7,4))[0]);faults+=1
    def scope_ok(v):return v['scope']=='unrestricted_even_density_variance1_fourth2' and not any(v[k] for k in ['physical_claim','restricted_gap_quantified','novelty_claim'])
    ck(scope_ok(r));reporting=0
    for field in ['physical_claim','restricted_gap_quantified','novelty_claim']:
        v=copy.deepcopy(r);v[field]=True;ck(not scope_ok(v));reporting+=1
    print(f'K1845 independent rational controls {n}; mathematical faults {faults}; reporting faults {reporting}')
if __name__=='__main__':main()
