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
    N=0;q=s.sqrt(2);I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1)
    # Spectral construction derived directly from two phase histories.
    phases=[s.Matrix([1,1,1,1]),s.Matrix([1,s.I,-1,s.I])]
    D=sum((z*adj(z)/2 for z in phases),s.zeros(4))
    bath=s.Matrix([1,0,0,1])/q
    diagrows=[[1,1,1,1],[1,1,s.I,s.I],[1,-1,1,-1],[1,-s.I,-1,s.I]]
    U=[s.diag(*row) for row in diagrows]
    if fault=='phase': U[3]=s.diag(1,-s.I,-1,-s.I)
    for j in range(4):
        for k in range(4):eq((adj(bath)*adj(U[k])*U[j]*bath)[0],D[j,k],'spectral mixture pair')
    # Trace the memory explicitly on Bob, for each preparation by Alice.
    p=s.Matrix([1,1])/q;m=s.Matrix([1,-1])/q
    outcomes=[]
    for memory in [p,m]:
        joint=(s.kronecker_product(s.Matrix([1,0]),memory)+s.kronecker_product(s.Matrix([0,1]),X*memory))/q
        rho=joint*adj(joint);reduced=s.Matrix(2,2,lambda j,k:sum(rho[2*j+a,2*k+a] for a in range(2)))
        outcomes.append(s.simplify(s.trace(X*reduced)))
    ck(outcomes==[1,-1],'partial-trace forward signal')
    B=s.Matrix([[-1,-1,q,0],[-1,s.I,0,q]]);H=adj(B)*B
    factor=20*q+(1 if fault=='norm' else 0)
    eq(2*sum(abs(H[j,k]) for j in range(4) for k in range(4) if j!=k),factor,'operator approximation factor')
    # V0 need not commute with its own Rj: explicit same-site noncommuting vacuum unitary.
    A0=s.kronecker_product(X,I);A1=s.kronecker_product(Z,I);B0=s.kronecker_product(I,X);B1=s.kronecker_product(I,Z)
    meq(A1*B0,(A0*B0)*(adj(A0)*A1),'vacuum relative left ordering')
    meq(A0*B1,(A0*B0)*(adj(B0)*B1),'second vacuum relative ordering')
    return N

def report(d):
    ck(d['signal_expectations']==[1,-1],'signal report');eq(s.sympify(d['commuting_distance_floor']),(6-4*s.sqrt(2))/(20*s.sqrt(2)),'distance report')

def verify(d):
    report(d)
    ck(d['dependency_sha256']==hashlib.sha256((ROOT/'explorations/conditional-build/k1903-quantum-dephasing-witness-2026-10-21.md').read_bytes()).hexdigest(),'dependency pin')
if __name__=='__main__':
    count=math();d=json.loads((ROOT/'lab/process/k1904-spacelike-dephasing-locality.json').read_text());verify(d)
    print('PASS independent exact mathematical controls',count,'plus reporting and pin baseline')
    caught=[]
    for fault in ['phase', 'norm']:
        try:math(fault)
        except AssertionError as e:print('[FAIL expected mathematical input]',fault,str(e));caught.append(fault)
        else:raise AssertionError('uncaught mathematical fault '+fault)
    for fault in ['report','pin']:
        bad=copy.deepcopy(d)
        if fault=='pin':bad['dependency_sha256']='0'*64
        else:
            key={'k1904-spacelike-dephasing-locality':'signal_expectations','k1905-causal-quantum-memory-realization':'fock_dimension','k1906-dephasing-divisibility-boundary':'cp_divisible_continuous_target'}['k1904-spacelike-dephasing-locality'];bad[key]=None
        try:verify(bad)
        except AssertionError as e:print('[FAIL expected reporting/provenance]',fault,str(e));caught.append(fault)
        else:raise AssertionError('uncaught reporting fault '+fault)
    print('PASS',len(caught),'assertion-based faults: 2 mathematical inputs, 1 report, 1 pin')
