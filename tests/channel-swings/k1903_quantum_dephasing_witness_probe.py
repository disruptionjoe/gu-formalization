"""Separate exact derivation and hostile probes; no producer import."""
from pathlib import Path
import copy,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
COUNT=0
def check(ok,name):
    global COUNT
    assert bool(ok),name
    COUNT+=1
def eq(a,b,name):check(s.simplify(a-b)==0,name)
def mat(a,b,name):check((a-b).applyfunc(s.simplify)==s.zeros(*a.shape),name)
def reject(fn,label):
    try:fn()
    except AssertionError:return label
    raise AssertionError('fault survived: '+label)
def pinned(d):
    expected=hashlib.sha256((ROOT/'explorations/conditional-build/k1900-sharp-phase-noise-cost-2026-10-21.md').read_bytes()).hexdigest()
    check(d['dependency_sha256']==expected,'dependency pin')

def algebra(imag=s.I,delta=6-4*s.sqrt(2)):
    q=s.sqrt(2)
    # Construct the environmental overlap directly, independently of B or producer V.
    states=[s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([1,1])/q,s.Matrix([1,-s.I])/q]
    C=s.Matrix(4,4,lambda j,k:(states[k].conjugate().T*states[j])[0])
    a=s.Matrix([-1,-1,q,0]);b=s.Matrix([-1,imag,0,q])
    H=a.conjugate()*a.T+b.conjugate()*b.T
    eq(s.trace(H*C),0,'environment annihilates witness')
    eq((2+q)**2*delta,4,'global residual lower-bound constant')
    z=s.Matrix([1,1,1,(1-s.I)/q]);eq((z.conjugate().T*H*z)[0],delta,'witness attained')
    check(C.rank()==2,'two dimensional pure environment')
    # An eight-dimensional isometry and explicit partial trace.
    W=s.zeros(8,4)
    for j,st in enumerate(states):
        for e in range(2):W[2*j+e,j]=st[e]
    mat(W.conjugate().T*W,s.eye(4),'isometry')
    joint=W*(s.ones(4)/4)*W.conjugate().T
    reduced=s.Matrix(4,4,lambda j,k:sum(joint[2*j+e,2*k+e] for e in range(2)))
    mat(reduced,C/4,'explicit partial trace')
    eq(s.trace(H*reduced),0,'single input quantum test')
    eq(sum(abs(H[j,k]) for j in range(4) for k in range(4) if j!=k),10*q,'independent tolerance sum')
    # Build actual Fock annihilators then restrict even bilinears to one-particle sector.
    ann=[]
    for j in range(4):
        op=s.zeros(16)
        for bits in range(16):
            if bits & (1<<j):op[bits^(1<<j),bits]=(-1)**((bits&((1<<j)-1)).bit_count())
        ann.append(op)
    embed=s.zeros(16,4)
    for j in range(4):embed[1<<j,j]=1
    for j in range(4):
        for k in range(4):
            unit=s.zeros(4);unit[j,k]=1
            mat(embed.T*ann[j].T*ann[k]*embed,unit,'neutral bilinear matrix unit')
    eq(s.trace(H),8,'mixture noise slope')
    return C,H
def reporting(d,C,H):
    parse=lambda key:s.Matrix([[s.sympify(x) for x in row] for row in d[key]])
    mat(parse('C'),C,'serialized channel');mat(parse('H'),H,'serialized witness')
    eq(s.sympify(d['delta']),6-4*s.sqrt(2),'serialized gap')
    eq(s.sympify(d['noise_exclusion_threshold']),(6-4*s.sqrt(2))/8,'noise threshold')
if __name__=='__main__':
    d=json.loads((ROOT/'lab/process/k1903-quantum-dephasing-witness.json').read_text());C,H=algebra();n=COUNT;reporting(d,C,H);pinned(d)
    faults=[reject(lambda:algebra(imag=-s.I),'wrong complex conjugation'),reject(lambda:algebra(delta=1),'wrong classical gap')]
    bad=copy.deepcopy(d);bad['H'][0][1]='1+I';faults.append(reject(lambda:reporting(bad,C,H),'serialized witness conjugation'))
    badpin=copy.deepcopy(d);badpin['dependency_sha256']='0'*64;faults.append(reject(lambda:pinned(badpin),'dependency pin'))
    print(json.dumps({'baseline_math_checks':n,'faults_rejected':faults}))
