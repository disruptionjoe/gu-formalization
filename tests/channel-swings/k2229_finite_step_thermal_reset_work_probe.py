#!/usr/bin/env python3
"""Exact small identities + rational interval certificate; no floating proof claims."""
from fractions import Fraction as F
from itertools import permutations
import json, argparse, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");args=ap.parse_args()

COUNT=0

def check(x):
    global COUNT
    assert x
    COUNT+=1

def log_bounds(x, n=100):
    x=F(x)
    if x<1:
        a,b=log_bounds(1/x,n)
        return -b,-a
    z=(x-1)/(x+1)
    s=sum((2*z**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
    tail=2*z**(2*n+1)/((2*n+1)*(1-z*z))
    return s,s+tail

def add(a,b): return a[0]+b[0],a[1]+b[1]
def scale(a,c): return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def entropy(p): return add(scale(log_bounds(p),-p),scale(log_bounds(1-p),p-1))
def kl(p,q): return add(scale(log_bounds(p/q),p),scale(log_bounds((1-p)/(1-q)),1-p))
def intersect(a,b): return max(a[0],b[0])<=min(a[1],b[1])
def subtract(a,b): return a[0]-b[1],a[1]-b[0]
def enclosure(x,scale10=10**12):
    return [str(F((x[0]*scale10).__floor__(),scale10)),str(F((x[1]*scale10).__ceil__(),scale10))]

def schedule(w,v,r,m,drop_final=False):
    odds=(1-v)/v
    ps=[1/(1+odds*r**j) for j in range(m+1)]
    x0=log_bounds(odds); dx=log_bounds(r)
    xs=[add(x0,scale(dx,j)) for j in range(m+1)]
    direct=add(scale(xs[0],w),scale(dx,sum(ps[:-1])))
    if not drop_final: direct=add(direct,scale(xs[-1],-ps[-1]))
    heat=scale(xs[0],w-ps[0])
    for j in range(1,m+1): heat=add(heat,scale(xs[j],ps[j-1]-ps[j]))
    diss=kl(w,v)
    for j in range(1,m+1): diss=add(diss,kl(ps[j-1],ps[j]))
    ent=add(subtract(entropy(w),entropy(ps[-1])),diss)
    return ps,xs,direct,heat,diss,ent

def fixture(w=F(1,3),v=F(1,4),r=F(2),m=3,drop_final=False):
    p,x,work,heat,diss,ent=schedule(w,v,r,m,drop_final)
    check(intersect(work,heat)); check(intersect(work,ent))
    check(diss[0]>0)
    upper=add(kl(w,v),scale(log_bounds(r),v-p[-1]))
    check(diss[1]<upper[1])
    return work

fixture();fixture(F(3,10),F(3,10),F(3,2),4)
# SWAP intertwines equal-gap number, preserves arbitrary matrix-unit input,
# and transfers record/reference correlations without using diagonal input.
S=[0,2,1,3]
for i in range(4):
    check(S[S[i]]==i)
    check((i//2+i%2)==(S[i]//2+S[i]%2))
for a in range(2):
    for b in range(2):
        for out0 in range(2):
            for out1 in range(2):
                value=F(0)
                for k,prob in enumerate([F(3,4),F(1,4)]):
                    l=S[2*a+k]; rr=S[2*b+k]
                    if l%2==rr%2 and l//2==out0 and rr//2==out1: value+=prob
                expected=([F(3,4),F(1,4)][out0] if a==b and out0==out1 else F(0))
                check(value==expected)
# Exact spectral projector establishes positivity and exponential SWAP at pi/2.
P=[[F(int(i==j)-int(S[j]==i),2) for j in range(4)] for i in range(4)]
check(all(P[i][j]==P[j][i] for i in range(4) for j in range(4)))
check(all(sum(P[i][k]*P[k][j] for k in range(4))==P[i][j] for i in range(4) for j in range(4)))
check(all(F(int(i==j))-2*P[i][j]==int(S[j]==i) for i in range(4) for j in range(4)))
# Gibbs bath with one and two qubits: every shell-preserving permutation
# leaves fixed-prior unwanted population >=w, unlike unconstrained sorting.
for N in (1,2):
    w=F(1,3);p=F(1,4);d=2**N
    probs=[(1-w if a==0 else w)*(1-p)**(N-b.bit_count())*p**b.bit_count() for a in range(2) for b in range(d)]
    shells=[[a*d+b for a in range(2) for b in range(d) if b.bit_count()==k] for k in range(N+1)]
    for sh in shells:
        baseline=sum(probs[i] for i in sh if i>=d)
        for dest in permutations(sh):
            check(sum(probs[i] for i,j in zip(sh,dest) if j>=d)>=baseline)
# Rational large consumer: interval summation prevents huge denominator LCM.
m=1700; scale10=10**24
A=3;B=7;sumlo=0
for j in range(m):
    sumlo+=(scale10*A)//(A+B)
    A*=100;B*=101
q=F(A,A+B)
sum_interval=(F(sumlo,scale10),F(sumlo+m,scale10))
x0=log_bounds(F(7,3));dx=log_bounds(F(101,100));xmax=add(x0,scale(dx,m))
wlo=F(3045489,10**7);whi=F(3046040,10**7)
source=json.loads((ROOT/'lab/process/k2223-stable-detector-resource-realization.json').read_text())
wa,wb=map(F,source['switch_certificate']['click_probability'])
check(wlo<wa<=wb<whi)
wbox=(wlo,whi)
coeff=(sum_interval[0]-m*q,sum_interval[1]-m*q)
work=( (wlo-q)*x0[0]+coeff[0]*dx[0], (whi-q)*x0[1]+coeff[1]*dx[1])
check(F(1930579,10**14)<q<F(1930581,10**14))
check(F(616212,10**6)<work[0]<work[1]<F(616260,10**6))
check(F(17762860,10**6)<xmax[0]<xmax[1]<F(17762861,10**6))
check(1000*q<F(1930581,10**11))
# Joint approximation/reset consumer uses the actual affine w coefficient.
delta=F(1,10000)
check(x0[1]<1)
check(delta+q<F(10001930581,10**14))
check(work[0]-x0[1]*delta>F(616112,10**6))
check(work[1]+x0[1]*delta<F(616360,10**6))
# baseline-first genuine faults: omit final quench; break resonance;
# replace SWAP by identity (fails replacement on excited input);
# reverse Gibbs odds (fails desired small-error condition).
faults=[]
try: fixture(drop_final=True)
except AssertionError: faults.append('omitted final gap quench')
check(len(faults)==1)
try:
    for i in range(4): assert i//2+2*(i%2)==S[i]//2+2*(S[i]%2)
except AssertionError: faults.append('nonresonant free Hamiltonian')
try:
    mutated_swap=list(range(4))
    excited_output=sum(prob for k,prob in enumerate([F(3,4),F(1,4)]) if mutated_swap[2+k]//2==1)
    assert excited_output==F(1,4)
except AssertionError: faults.append('identity substituted for SWAP')
try:
    reversed_gibbs_q=F(B,A+B)
    assert reversed_gibbs_q<F(1,1000)
except AssertionError: faults.append('reversed Gibbs odds')
check(len(faults)==4)
out={'result':'K2229','checks':COUNT,'faults':faults,'q_bounds':['0.00000001930579','0.00000001930581'],'beta_work_bounds':enclosure(work),'maximum_beta_gap_bounds':enclosure(xmax),'fresh_cells':1701,'certification':'exact rational controls/intervals plus reporting checks; universal claims use the written proof'}
deps=['explorations/conditional-build/k2229-finite-step-thermal-reset-work-2026-10-28.md','lab/process/k2223-stable-detector-resource-realization.json','explorations/conditional-build/k2226-thermal-register-reset-2026-10-28.md','explorations/conditional-build/k2228-continuum-energy-form-detector-control-2026-10-28.md']
out['probe_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
out['dependency_sha256']={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}
target=ROOT/'lab/process/k2229-finite-step-thermal-reset-work.json'
if args.write:target.write_text(json.dumps(out,indent=2)+'\n')
else:assert json.loads(target.read_text())==out,'stale certificate'
print(json.dumps({k:v for k,v in out.items() if k not in ['dependency_sha256','probe_sha256']}))
