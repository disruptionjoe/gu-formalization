"""Independent exact controls and assertion-only mutation harness."""
from pathlib import Path
import json,hashlib,copy
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
N=0
def ck(ok,label):
    global N
    assert bool(ok),label
    N+=1
def eq(a,b,label):ck(s.simplify(s.expand_complex(a-b))==0,label)
def adj(a):return a.conjugate().T
def meq(a,b,label):ck((a-b).applyfunc(s.expand_complex).applyfunc(s.simplify)==s.zeros(*a.shape),label)

def math(fault=None):
    global N
    N=0;q=s.sqrt(2);I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]])
    a=s.pi/4 if fault!='angle' else s.pi/2
    U=[I,X,s.cos(s.pi/4)*I-s.I*s.sin(s.pi/4)*Y,s.cos(a)*I-s.I*s.sin(a)*X]
    cols=[u[:,0] for u in U]
    expected=s.Matrix([[1,0,1/q,1/q],[0,1,1/q,s.I/q],[1/q,1/q,1,(1+s.I)/2],[1/q,-s.I/q,(1-s.I)/2,1]])
    D=s.Matrix(4,4,lambda j,k:(adj(cols[k])*cols[j])[0]);meq(D,expected,'independent cosine branch Gram')
    # Explicit reduced channel on matrix units, without producer's Gram multiplication.
    for j in range(4):
        for k in range(4):
            out=sum(cols[j][a]*s.conjugate(cols[k][a]) for a in range(2))
            eq(out,expected[j,k],'Kraus matrix-unit action')
    # Product ordering is material only in occupied multi-site sectors.
    correct=U[3]*U[2]*U[1];supplied=correct if fault!='order' else U[1]*U[2]*U[3]
    meq(supplied*s.Matrix([1,0]),correct*s.Matrix([1,0]),'multi-particle branch order')
    ck(U[3]*U[2]!=U[2]*U[3],'order negative control is nontrivial')
    energy=[abs(x[1])**2 for x in cols];ck(energy==[0,1,s.Rational(1,2),s.Rational(1,2)],'excited memory probabilities')
    # Norm from the spectrum, not the producer's stated sum.
    generators=[s.pi*(I-X)/2,s.pi*Y/4,s.pi*X/4]
    norms=[max(abs(x) for x in g.eigenvals()) for g in generators]
    eq(sum(norms),3*s.pi/2,'spectral control norm');eq(sum(energy)/4,s.Rational(1,2),'uniform energy')
    return N

def report(d):
    ck(d['fock_dimension']==32,'Fock report');eq(s.sympify(d['error_budget']),(6-4*s.sqrt(2))/(8*(4+s.sqrt(2))),'error report')

def verify(d):
    report(d)
    ck(d['dependency_sha256']==hashlib.sha256((ROOT/'explorations/conditional-build/k1903-quantum-dephasing-witness-2026-10-21.md').read_bytes()).hexdigest(),'dependency pin')
if __name__=='__main__':
    count=math();d=json.loads((ROOT/'lab/process/k1905-causal-quantum-memory-realization.json').read_text());verify(d)
    print('PASS independent exact mathematical controls',count,'plus reporting and pin baseline')
    caught=[]
    for fault in ['angle', 'order']:
        try:math(fault)
        except AssertionError as e:print('[FAIL expected mathematical input]',fault,str(e));caught.append(fault)
        else:raise AssertionError('uncaught mathematical fault '+fault)
    for fault in ['report','pin']:
        bad=copy.deepcopy(d)
        if fault=='pin':bad['dependency_sha256']='0'*64
        else:
            key={'k1904-spacelike-dephasing-locality':'signal_expectations','k1905-causal-quantum-memory-realization':'fock_dimension','k1906-dephasing-divisibility-boundary':'cp_divisible_continuous_target'}['k1905-causal-quantum-memory-realization'];bad[key]=None
        try:verify(bad)
        except AssertionError as e:print('[FAIL expected reporting/provenance]',fault,str(e));caught.append(fault)
        else:raise AssertionError('uncaught reporting fault '+fault)
    print('PASS',len(caught),'assertion-based faults: 2 mathematical inputs, 1 report, 1 pin')
