"""Independent bath-label, finite-support and infinite-series checks."""
from copy import deepcopy
from fractions import Fraction as Q
from pathlib import Path
from itertools import combinations
import hashlib
import json

ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/k2008-effective-thermal-dimension-approximation.json'


def mean(s,p): return sum(x*y for x,y in zip(s,p))


def direct_return(s,p,t):
    Z=sum(t**k for k in range(4))
    output=[]
    for x in s:
        retained=Q(0)
        for b in range(4):
            shell=x+b
            available=[v*t**k/Z for y,v in zip(s,p)
                       for k in range(4) if y+k==shell]
            retained+=max(available)/2
        output.append(retained)
    return sum(max(v-z,0) for v,z in zip(p,output))


def valid_shells(a,s):
    for energy in {x+b for x in s for b in range(4)}:
        physical=[(x,b) for x in a for b in range(4) if x+b==energy]
        occupied=[(x,b) for x in s for b in range(4) if x+b==energy]
        if len(physical)<2*len(occupied): return False
    return True


def sparse_weights(e,r,w):
    w=list(w)
    while len(ids:=[i for i,v in enumerate(w) if v])>2:
        i,j,k=ids[:3]
        z=[Q(0)]*len(w)
        z[i],z[j],z[k]=e[j]-e[k],e[k]-e[i],e[i]-e[j]
        if not any(z): z[i],z[j]=Q(1),Q(-1)
        if mean(z,r)>0: z=[-v for v in z]
        step=min(-w[i]/v for i,v in enumerate(z) if v<0)
        w=[v+step*u for v,u in zip(w,z)]
    return w


def split_blocks(a):
    cosets={}
    for x in a: cosets.setdefault(x % 1,[]).append(x)
    result=[]
    for group in cosets.values():
        current=[]
        for x in sorted(group):
            if current and x-current[-1]>3:
                result.append(current)
                current=[]
            current.append(x)
        if current: result.append(current)
    return result


def check(data,fault=None):
    data=deepcopy(data)
    checks=0
    for row in data['physical_cases']:
        a=list(map(Q,row['original_spectrum']))
        s=list(map(Q,row['original_support']))
        p=list(map(Q,row['original_populations']))
        A=list(map(Q,row['final_spectrum']))
        S=list(map(Q,row['final_support']))
        P=list(map(Q,row['final_populations']))
        N=row['N'];t=Q(row['t']);E=Q(row['budget'])
        q=sum((v for x,v in zip(s,p) if x>N),Q(0))
        low_s=[x for x in s if x<=N]
        low_p=[v for x,v in zip(s,p) if x<=N]
        assert sum(p)==1 and min(p)>=0 and mean(s,p)==E<N
        assert q==Q(row['tail_mass']) and q<1
        assert q<=(E-1)/(N-1)
        before=direct_return(s,p,t)
        low=direct_return(low_s,low_p,t)
        assert before==Q(row['before_return']) and before<=Q(1,2)
        assert low<=before+q/2
        assert mean(low_s,[v/(1-q) for v in low_p])<=E
        assert valid_shells([x for x in a if x<=N+3],low_s)
        if fault=='lost_normalization' and q:
            P=[v*(1-q) for v in P]
        if fault=='raised_mean':
            P=[Q(int(i==S.index(max(S)))) for i in range(len(S))]
        assert sum(P)==1 and min(P)>=0,'normalized physical preparation'
        assert mean(S,P)<=E,'upper mean energy preserved'
        assert valid_shells(A,S) and set(S)<=set(A)
        assert min(A)==0 and len(set(A))==len(A)
        assert min(y-x for x,y in zip(sorted(A),sorted(A)[1:]))>=Q(row['original_spacing'])
        assert len(A)<=2*N+7
        after=direct_return(S,P,t)
        assert after==Q(row['after_return'])
        assert after<=before+(E-1)/(N-E)
        # Separate null-vector construction on normalized low components.
        e=[];r=[];w=[]
        for block in split_blocks([x for x in a if x<=N+3]):
            pairs=[(x,v/(1-q)) for x,v in zip(low_s,low_p) if x in block]
            mass=sum(v for x,v in pairs)
            if mass:
                ss=[x for x,v in pairs];pp=[v/mass for x,v in pairs]
                e.append(mean(ss,pp));r.append(direct_return(ss,pp,t));w.append(mass)
        new=sparse_weights(e,r,w)
        assert sum(new)==1 and min(new)>=0 and sum(bool(v) for v in new)<=2
        assert mean(new,e)<=mean(w,e) and mean(new,r)<=mean(w,r)
        checks+=1
    # Completion at N+3 is a physical obligation, not a population cutoff.
    N=3;A=list(map(Q,range(7)));S=[Q(1),Q(3)]
    if fault=='drop_completion': A=[x for x in A if x<=N]
    assert valid_shells(A,S),'cutoff must retain bath-shell completion'
    checks+=1
    # Tight counting witness for two distinct integer cosets in the window.
    for N in range(2,12):
        A=list(map(Q,range(N+4)))+[Q(1,2)+j for j in range(N+3)]
        ceiling=2*N+7-(fault=='wrong_coset_count')
        assert len(set(A))<=ceiling,'two-coset window count'
        assert valid_shells(A,[Q(1),Q(3,2)])
        checks+=1
    for row in data['infinite_geometric_controls']:
        r=Q(row['r']);t=Q(row['t']);E=Q(row['E']);N=row['N']
        m=(N+1)//2;tail=r**m
        s=[Q(2*j+1) for j in range(m)]
        low=[(1-r)*r**j for j in range(m)]
        # Infinite direct-return coefficients from each site's four bath labels.
        Z=sum(t**b for b in range(4))
        def retention_coefficient(k):
            x=2*k+1
            return sum(max(r**j*t**b/Z
                       for j in range(max(0,k-1),k+2)
                       for b in range(4) if 2*j+1+b==x+c)
                       for c in range(4))/2
        root=max(Q(1)-retention_coefficient(0),0)
        interior=max(r-retention_coefficient(1),0)/r
        exact=(1-r)*root+r*interior
        if fault=='wrong_infinite_return': exact-=Q(1,10)
        assert exact==Q(row['exact_infinite_return']),'infinite geometric return from bath labels'
        assert E==(1+r)/(1-r) and tail==Q(row['tail_mass'])
        assert direct_return(s,low,t)<=exact+tail/2
        assert mean(s,[v/(1-tail) for v in low])<=E
        assert direct_return(s,[v/(1-tail) for v in low],t)<=exact+(E-1)/(N-E)
        checks+=1
    for row in data['effective_joint_resources']:
        E=Q(row['E']);eps=Q(row['epsilon']);N=row['N'];delta=Q(row['delta'])
        if fault=='underpaid_joint_spacing': delta=3*eps
        assert N>E and row['d']==2*N+7
        assert delta/2+(E-1)/(N-E)<=eps,'joint resource error budget'
        checks+=1
    return checks


if __name__=='__main__':
    data=json.loads(REPORT.read_text())
    count=check(data)
    rejected=[]
    for fault in ['lost_normalization','raised_mean','drop_completion',
                  'wrong_coset_count','wrong_infinite_return','underpaid_joint_spacing']:
        try: check(data,fault)
        except AssertionError as exc: rejected.append([fault,str(exc)])
        else: raise AssertionError('missed mathematical fault '+fault)
    for p,h in data['inputs'].items():
        assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    print('PASS K2008 independent',count,'exact control groups;',rejected)
