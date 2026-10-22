#!/usr/bin/env python3
"""Independent support embeddings, enumerated spectra and SWAP routing controls."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import sympy as S
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def recurrent(n,q,deg=2):
    cs=[1]
    for _ in range(n):
        nxt=[0]*(len(cs)+1)
        for i,c in enumerate(cs):nxt[i]+=c;nxt[i+1]+=deg*c
        cs=nxt
    assert sum(cs)==3**n,'shell dimension'
    left=3**n//2**n;p=Q(0)
    for j,c in enumerate(cs):
        take=min(left,c);p+=take*(q/2)**j*(1-q)**(n-j);left-=take
        if not left:return p

def spectra(deg=2):
    for n in range(1,6):
        for q in [Q(1,21),Q(1,3),Q(2,3)]:
            ps=[1-q,q/2,q/2];ws=[]
            for word in product(range(3),repeat=n):
                p=Q(1)
                for x in word:p*=ps[x]
                ws.append(p)
            assert sum(sorted(ws,reverse=True)[:3**n//2**n])==recurrent(n,q,deg),'sorted spectral mass'
    return 15

def embedding(fault=False):
    es=[S.Matrix([1,0]),S.Matrix([0,1]),S.Matrix([1,1])/S.sqrt(2),S.Matrix([1,S.I])/S.sqrt(2)]
    vectors=[S.kronecker_product(x,y) for x in es for y in es];Vs=[]
    for e in vectors:
        V=S.zeros(9,2)
        for alpha in range(4):
            for j in range(2):V[2*alpha+j,j]=e[alpha]
        Vs.append(V)
    if fault:Vs[0][0,1]=1
    for i,V in enumerate(Vs):
        assert S.simplify(V.adjoint()*V-S.eye(2))==S.zeros(2),'support isometry'
        for j,W in enumerate(Vs):
            z=(vectors[j].adjoint()*vectors[i])[0]
            assert S.simplify(W.adjoint()*V-z*S.eye(2))==S.zeros(2),'complete Gram compression'
    return 256

def routing(fault=False):
    for word in product(range(3),repeat=4):
        expected=list(word);expected[3]=(expected[3]+expected[0])%3
        w=list(word)
        for i in [2,1]:w[i],w[i+1]=w[i+1],w[i]
        w[1]=(w[1]+w[0])%3
        for i in ([1] if fault else [1,2]):w[i],w[i+1]=w[i+1],w[i]
        assert w==expected,'nonadjacent gate identity'
    return 81

def report(fault=False,pin=False):
    r=json.loads((ROOT/'lab/process/k1920-local-block-thermal-channel-construction.json').read_text())
    if fault:r['finite_example']['mass']='1'
    if pin:r['dependencies'][next(iter(r['dependencies']))]='0'*64
    f=r['finite_example'];p=recurrent(f['b'],Q(f['q']));e=1-p
    assert p==Q(f['mass']) and e==Q(f['tail']),'finite report mass'
    assert e<Q(1,100000000) and f['blocks']*e<Q(f['error_upper']),'finite block error'
    assert f['blocks']*e/p<Q(f['preparation_D_upper']),'finite D upper'
    for dep,d in r['dependencies'].items():assert hashlib.sha256((ROOT/dep).read_bytes()).hexdigest()==d,'dependency pin'

def reject(fn,label):
    try:fn()
    except AssertionError as e:assert str(e);print('CAUGHT',label,':',e);return
    raise AssertionError('missed mutation '+label)
if __name__=='__main__':
    print('BASELINE spectra',spectra(),'Gram pairs',embedding(),'basis routes',routing());report()
    reject(lambda:spectra(deg=1),'shell dimension')
    reject(lambda:embedding(True),'support column')
    reject(lambda:routing(True),'inverse swap')
    reject(lambda:report(True),'report')
    reject(lambda:report(pin=True),'pin')
    print('PASS K1920 independent algebra; 3 math input faults, report and pin faults')
