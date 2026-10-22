#!/usr/bin/env python3
"""Independent word enumeration and recurrent shell counts; no producer import."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
def direct(N,q):
    weights=[1-q,q/2,q/2];allp=[]
    for w in product(range(3),repeat=N):
        p=Q(1)
        for x in w:p*=weights[x]
        allp.append(p)
    assert sum(allp)==1,'word normalization'
    return sum(sorted(allp,reverse=True)[:3**N//2**N])
def recurrent(N,q,deg=2,weight_divisor=2):
    counts=[1]
    for _ in range(N):
        nxt=[0]*(len(counts)+1)
        for i,c in enumerate(counts):nxt[i]+=c;nxt[i+1]+=deg*c
        counts=nxt
    assert sum(counts)==3**N,'degeneracy total'
    left=3**N//2**N;p=Q(0)
    for j,c in enumerate(counts):
        take=min(c,left);p+=take*(q/weight_divisor)**j*(1-q)**(N-j);left-=take
        if not left:return p
    raise AssertionError('rank not filled')
def math_checks(deg=2,weight_divisor=2):
    for N in range(1,7):
        for q in [Q(0),Q(1,21),Q(1,3),Q(2,3)]:
            assert direct(N,q)==recurrent(N,q,deg,weight_divisor),'exact sorted word mass'
    for N in range(1,5):
        q=Q(1,3);p=direct(N,q);purity=(1-q)**2+q*q/2
        assert p*p<=(3**N//2**N)*purity**N,'independent Holder alpha2'
    return 24

def report(mutate=False,pin=False):
    r=json.loads((ROOT/'lab/process/k1918-collective-thermal-preparation-threshold.json').read_text())
    if mutate:r['finite_example']['mass']='1'
    if pin:r['dependencies'][next(iter(r['dependencies']))]='0'*64
    x=r['finite_example'];p=recurrent(x['N'],Q(x['q']))
    assert p==Q(x['mass']),'reported finite mass'
    assert 1-p==Q(x['error']) and 1-p<Q(1,10000),'finite certified error'
    assert (1-p)/p<Q(1,9999),'finite certified entropy'
    for dep,sha in r['dependencies'].items():assert hashlib.sha256((ROOT/dep).read_bytes()).hexdigest()==sha,'dependency pin'

def rejected(fn,label):
    try:fn()
    except AssertionError as ex:
        assert str(ex),'empty failed check';print('CAUGHT',label,':',ex);return
    raise AssertionError('missed mutation '+label)
if __name__=='__main__':
    print('BASELINE exact sorted-word comparisons:',math_checks());report()
    rejected(lambda:math_checks(deg=1),'mathematical degeneracy')
    rejected(lambda:math_checks(weight_divisor=1),'mathematical eigenvalue weight')
    rejected(lambda:report(mutate=True),'report finite mass')
    rejected(lambda:report(pin=True),'dependency pin')
    print('PASS K1918 independent 24 exact word checks plus recurrent N300; 2 math faults, 1 report fault, 1 pin fault')
