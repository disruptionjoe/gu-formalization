#!/usr/bin/env python3
"""K2235 exact finite controls; universal results use the written proofs."""
from fractions import Fraction as F
import json
import argparse
import hashlib
from pathlib import Path

class Q:
    def __init__(self, re=0, im=0):
        if isinstance(re,Q): self.re,self.im=re.re,re.im
        else: self.re,self.im=F(re),F(im)
    def __add__(self,b):
        b=Q(b);return Q(self.re+b.re,self.im+b.im)
    __radd__=__add__
    def __neg__(self):return Q(-self.re,-self.im)
    def __sub__(self,b):return self+-Q(b)
    def __rsub__(self,b):return Q(b)+-self
    def __mul__(self,b):
        b=Q(b);return Q(self.re*b.re-self.im*b.im,self.re*b.im+self.im*b.re)
    __rmul__=__mul__
    def __eq__(self,b):
        b=Q(b);return self.re==b.re and self.im==b.im
    def conj(self):return Q(self.re,-self.im)
    def norm2(self):return self.re*self.re+self.im*self.im

def zero(n):return [[Q() for _ in range(n)] for _ in range(n)]
def eye(n):return [[Q(i==j) for j in range(n)] for i in range(n)]
def unit(n,i,j):
    a=zero(n);a[i][j]=Q(1);return a
def add(a,b):return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def scale(a,c):return [[c*x for x in ar] for ar in a]
def mul(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),Q()) for j in range(len(b))] for i in range(len(a))]
def adj(a):return [[a[j][i].conj() for j in range(len(a))] for i in range(len(a))]
def kron(a,b):return [[a[i//len(b)][j//len(b)]*b[i%len(b)][j%len(b)] for j in range(len(a)*len(b))] for i in range(len(a)*len(b))]
def trace(a):return sum((a[i][i] for i in range(len(a))),Q())
def tau(p):return [[Q(1-p),Q()],[Q(),Q(p)]]
def ptr_last(a):return [[sum((a[2*i+k][2*j+k] for k in range(2)),Q()) for j in range(len(a)//2)] for i in range(len(a)//2)]
def ptr_first(a):return [[sum((a[2*k+i][2*k+j] for k in range(2)),Q()) for j in range(2)] for i in range(2)]
def exchange(c,s):return [[Q(1),Q(),Q(),Q()],[Q(),Q(c),Q(0,-s),Q()],[Q(),Q(0,-s),Q(c),Q()],[Q(),Q(),Q(),Q(1)]]
S=[[Q(i==[0,2,1,3][j]) for j in range(4)] for i in range(4)]
X=add(unit(4,1,2),unit(4,2,1))

def run(fault=None):
    checks=[]
    def ck(v,n):checks.append((n,bool(v)))
    c,s,p=F(3,5),F(4,5),F(2,7)
    U=exchange(c,s)
    if fault=='partial-swap-as-exchange':U=add(scale(eye(4),c),scale(S,Q(0,-s)))
    if fault=='wrong-exchange-phase':U[2][1]=Q(0,s)
    bath=tau(p/2 if fault=='wrong-gibbs-ancilla' else p)
    ck(mul(adj(U),U)==eye(4),'exchange-unitarity')
    N=[[Q((i//2)+(i%2)) if i==j else Q() for j in range(4)] for i in range(4)]
    if fault=='detuned-ancilla':N[1][1]=Q(2);N[3][3]=Q(3)
    ck(mul(N,X)==mul(X,N),'resonant-energy-commutator')
    # Exact eigenvectors for the positive interaction I+X.
    K=add(eye(4),X)
    if fault=='unshifted-positive-control':K=X
    for vec,lam in [([1,0,0,0],1),([0,0,0,1],1),([0,1,1,0],2),([0,1,-1,0],0)]:
        ck(all(sum((K[i][j]*vec[j] for j in range(4)),Q())==lam*vec[i] for i in range(4)),'positive-interaction-spectrum')
    def gad(a):
        r=len(a)//2;y=zero(len(a))
        for i in range(r):
            for j in range(r):
                aa,bb=a[i][j],a[i+r][j+r];d=p*aa-(1-p)*bb
                y[i][j]=(1-p)*(aa+bb)+c*c*d
                y[i+r][j+r]=p*(aa+bb)-c*c*d
                y[i][j+r]=c*a[i][j+r];y[i+r][j]=c*a[i+r][j]
        return y
    # B,F,A order. Lift U_BA through untouched finite F explicitly.
    for r in (1,2):
        W=zero(4*r)
        for b in range(2):
            for f in range(r):
                for a in range(2):
                    for bp in range(2):
                        for ap in range(2):W[(b*r+f)*2+a][(bp*r+f)*2+ap]=U[2*b+a][2*bp+ap]
        for i in range(2*r):
            for j in range(2*r):
                x=unit(2*r,i,j)
                y=ptr_last(mul(mul(W,kron(x,bath)),adj(W)))
                ck(y==gad(x),'reference-matrix-unit-channel')
    # Full exchange is exact replacement, including Bell reference.
    bell=scale([[Q(i in (0,3) and j in (0,3)) for j in range(4)] for i in range(4)],F(1,2))
    V=exchange(0,1)
    W=zero(8)
    for b in range(2):
        for f in range(2):
            for a in range(2):
                for bp in range(2):
                    for ap in range(2):W[(2*b+f)*2+a][(2*bp+f)*2+ap]=V[2*b+a][2*bp+ap]
    ck(ptr_last(mul(mul(W,kron(bell,tau(p))),adj(W)))==kron(tau(p),scale(eye(2),F(1,2))),'full-exchange-reference-decoupling')
    # Partial-SWAP foil has complex multiplier and extra contraction.
    VP=add(scale(eye(4),c),scale(S,Q(0,-s)))
    off=ptr_last(mul(mul(VP,kron(unit(2,0,1),tau(p))),adj(VP)))[0][1]
    ck(off==Q(c*c,-c*s*(1-2*p)),'partial-swap-actual-coherence')
    ck(off.norm2()<c*c,'partial-swap-extra-contraction')
    # Incoming correlations are a mathematical input, not only marginals.
    # Entangled thermal marginals are NOT independent thermal stock: at p=1/2,
    # (|01>+i|10>)/sqrt2 has both Gibbs marginals, but exchange changes B.
    cc=zero(4);cc[1][1]=cc[2][2]=Q(F(1,2))
    cc[1][2]=Q(0,F(-1,2));cc[2][1]=Q(0,F(1,2))
    ck(ptr_last(cc)==tau(F(1,2)) and ptr_first(cc)==tau(F(1,2)),
       'entangled-input-has-gibbs-marginals')
    cc_in=kron(tau(F(1,2)),tau(F(1,2))) if fault=='replace-correlated-entry-by-product' else cc
    outcc=ptr_last(mul(mul(exchange(c,s),cc_in),adj(exchange(c,s))))
    ck(outcc[1][1]==F(1,50),'correlated-entry-breaks-gad-marginal')
    ck(outcc[1][1]!=F(1,2),'gibbs-marginals-not-independent-stock')
    # Same ancilla twice differs from two independent fresh ancillas.
    initial=kron(tau(F(1,5)),tau(p))
    once=mul(mul(exchange(c,s),initial),adj(exchange(c,s)))
    next_in=kron(ptr_last(once),tau(p)) if fault=='reuse-spent-as-fresh' else once
    twice=ptr_last(mul(mul(exchange(c,s),next_in),adj(exchange(c,s))))
    expected_same=p+(2*c*c-1)**2*(F(1,5)-p)
    expected_fresh=p+c**4*(F(1,5)-p)
    ck(twice[1][1]==expected_same,'same-ancilla-return-population')
    ck(twice[1][1]!=expected_fresh,'spent-ancilla-is-not-fresh')
    # Exact finite ancillary heat and energy conservation for coherent input.
    rho=[[Q(F(2,3)),Q(F(1,7),F(1,11))],[Q(F(1,7),-F(1,11)),Q(F(1,3))]]
    joint=kron(rho,tau(p));out=mul(mul(exchange(c,s),joint),adj(exchange(c,s)))
    bout,aout=ptr_last(out),ptr_first(out)
    heat=aout[1][1]-p
    if fault=='reverse-heat-sign':heat=-heat
    ck(heat==(1-c*c)*(F(1,3)-p),'finite-ancillary-heat')
    ck(heat==F(1,3)-bout[1][1],'bare-energy-conservation')
    ck(trace(mul(add(eye(4),X),joint))==1,'fresh-ancilla-interaction-expectation')
    ck(trace(mul(add(eye(4),X),out))==trace(mul(add(eye(4),X),joint)),'conserved-coupling-work-observable')
    # Rational product contractions: two GAD steps multiply c factors.
    r1=p+c*c*(F(1,5)-p);r2=p+c*c*(r1-p)
    ck(r2==expected_fresh,'fresh-two-step-population')
    # Exact 100-collision consumer; no irrational matrix arithmetic required.
    count=99 if fault=='missing-fresh-collision' else 100
    eta=F(1,2)**count
    ck(eta==F(1,2**100),'one-hundred-collision-contraction')
    eps=1701*(F(1,2**51)+eta)
    q=F(3*100**1700,3*100**1700+7*101**1700)
    ck(eps<F(7554,10**16),'renewal-error-ceiling')
    ck(1000*(q+eps)<F(19306566,10**12),'thousand-reset-error-ceiling')
    fresh=1701*count*1000
    ck(fresh==170100000,'finite-fresh-stock-including-final')
    ck(1701*100*999==169929900,'finite-fresh-stock-no-final')
    ck(1701*999+1701==1701000,'full-exchange-stock-no-saving')
    return checks

FAULTS=['partial-swap-as-exchange','wrong-exchange-phase','wrong-gibbs-ancilla','detuned-ancilla','unshifted-positive-control','replace-correlated-entry-by-product','reuse-spent-as-fresh','reverse-heat-sign','missing-fresh-collision']

def main():
    baseline=run();bad=[name for name,ok in baseline if not ok]
    if bad:raise AssertionError(('baseline',bad))
    caught={}
    for fault in FAULTS:
        misses=[name for name,ok in run(fault) if not ok]
        if not misses:raise AssertionError(('undetected',fault))
        caught[fault]=misses
    report={'result':'K2235','controls':[{'name':n,'passed':v} for n,v in baseline], 'faults':caught,'fresh_ancillas_per_renewal':170100,'fresh_ancillas_1000_with_final':170100000,'claim_ceiling':'exact finite controls; universal statements use written proofs; no physical bath or clock certification'}
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--controls-only',action='store_true',help='Scratch controls without certificate checks; not publication validation')
    args=parser.parse_args()
    if args.controls_only:
        print(json.dumps(report,indent=2));return
    root=Path(__file__).resolve().parents[2]
    note='explorations/conditional-build/k2235-microscopic-thermal-renewal-2026-10-29.md'
    probe='tests/channel-swings/k2235_microscopic_thermal_renewal_probe.py'
    dependencies=['explorations/conditional-build/k2229-finite-step-thermal-reset-work-2026-10-28.md','explorations/conditional-build/k2232-smooth-reset-and-thermal-renewal-2026-10-29.md']
    report['sha256']={name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in [note,probe]+dependencies}
    cert=root/'lab/process/k2235-microscopic-thermal-renewal.json'
    if args.write:
        cert.write_text(json.dumps(report,indent=2)+'\n')
    else:
        if not cert.exists() or json.loads(cert.read_text())!=report:
            raise AssertionError('stale or missing K2235 certificate; regenerate only after review')
    print(json.dumps({'result':'K2235','controls':len(baseline),'faults':{k:len(v) for k,v in caught.items()}}))

if __name__=='__main__':main()
