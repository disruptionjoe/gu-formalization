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
    N=0;q=s.sqrt(2);v=[s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([1,1])/q,s.Matrix([1,s.I])/q]
    # The Gram relations force linear dependence, including phases.
    meq(v[2],(v[0]+v[1])/q,'third Gram relation')
    w=v[3] if fault!='phase' else s.Matrix([1,-s.I])/q
    meq(w,(v[0]+s.I*v[1])/q,'fourth Gram relation')
    # Three product vectors in a common line: genuine rank-two negative control.
    tensor=s.kronecker_product(v[0],v[0])+s.kronecker_product(v[1],v[1])
    ck(tensor.reshape(2,2).rank()==2,'independent-factor sum is not simple')
    common=s.kronecker_product(v[0],v[0])+s.kronecker_product(v[0],v[1])
    ck(common.reshape(2,2).rank()==1,'common-factor positive control')
    e=s.Rational(1,10);eq((1/q-e)**4-e,s.Rational(1801,10000)-s.Rational(51,500)*q,'exact robust rational margin')
    ck((1/q-e)**4-e>0,'one-tenth contradiction margin')
    rate=s.Rational(1,2) if fault!='rate' else s.Rational(1,4)
    vals=[-1,1,0];D=s.Matrix(3,3,lambda j,k:s.exp(-s.log(2)*rate*(vals[j]-vals[k])**2))
    eq(D[0,1],s.Rational(1,4),'metric saturating pair');eq(D[0,2],1/q,'metric arm')
    # Exact finite-time pair and diagonal coefficients of the Poisson control.
    t=s.log(2);C=s.Matrix(4,4,lambda j,k:(adj(v[j])*v[k])[0]);F=C.applyfunc(lambda x:s.exp(t*(x-1)))
    eq(F[0,1],s.Rational(1,2),'Poisson finite-time positive pair')
    for j in range(4):eq(F[j,j],1,'Poisson diagonal')
    # Direct Choi positivity for a repeated two-ray group and a nonzero phase gauge.
    z=s.Matrix([1,s.I,1,-s.I]);groups=[0,0,1,1]
    for cross in [s.S.Zero,s.Rational(2,3),s.S.One]:
        A=s.Matrix(4,4,lambda j,k:z[j]*s.conjugate(z[k])*(1 if groups[j]==groups[k] else cross))
        ck(all(x>=0 for x in A.eigenvals()),'two-ray channel positivity')
        ck(A.rank()==(1 if cross==1 else 2),'two-ray Gram rank')
    return N

def report(d):
    ck(d['cp_divisible_continuous_target']=='excluded','divisibility report');ck(d['metric_control12']=='1/4','metric report')

def verify(d):
    report(d)
    ck(d['dependency_sha256']==hashlib.sha256((ROOT/'explorations/conditional-build/k1903-quantum-dephasing-witness-2026-10-21.md').read_bytes()).hexdigest(),'dependency pin')
if __name__=='__main__':
    count=math();d=json.loads((ROOT/'lab/process/k1906-dephasing-divisibility-boundary.json').read_text());verify(d)
    print('PASS independent exact mathematical controls',count,'plus reporting and pin baseline')
    caught=[]
    for fault in ['phase', 'rate']:
        try:math(fault)
        except AssertionError as e:print('[FAIL expected mathematical input]',fault,str(e));caught.append(fault)
        else:raise AssertionError('uncaught mathematical fault '+fault)
    for fault in ['report','pin']:
        bad=copy.deepcopy(d)
        if fault=='pin':bad['dependency_sha256']='0'*64
        else:
            key={'k1904-spacelike-dephasing-locality':'signal_expectations','k1905-causal-quantum-memory-realization':'fock_dimension','k1906-dephasing-divisibility-boundary':'cp_divisible_continuous_target'}['k1906-dephasing-divisibility-boundary'];bad[key]=None
        try:verify(bad)
        except AssertionError as e:print('[FAIL expected reporting/provenance]',fault,str(e));caught.append(fault)
        else:raise AssertionError('uncaught reporting fault '+fault)
    print('PASS',len(caught),'assertion-based faults: 2 mathematical inputs, 1 report, 1 pin')
