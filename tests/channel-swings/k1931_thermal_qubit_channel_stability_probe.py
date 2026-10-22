"""Independent shell enumeration, coherence and positive-witness controls."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import importlib.util,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
P=Path(__file__).with_name('k1931_thermal_qubit_channel_stability.py')
spec=importlib.util.spec_from_file_location('producer',P);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

def independent():
    n=0
    def ck(x,label):
        nonlocal n
        assert bool(x),label;n+=1
    # Enumerate shells directly; optimize retained support instead of producer rounding.
    for d in range(1,6):
        supports=[bits for bits in product((0,1),repeat=d) if not bits[0] and not bits[-1] and not any(bits[a]*bits[a+1] for a in range(d-1))]
        for raw in product(range(3),repeat=d):
            if not sum(raw):continue
            p=[F(x,sum(raw)) for x in raw]
            for q in (F(1,4),F(1,2)):
                alpha=F(0)
                for energy in range(d+1):
                    weights=[p[a]*((1-q) if b==0 else q) for b in (0,1) for a in range(d) if a+b==energy]
                    alpha+=len(weights)*min(weights)
                retained=max(sum(p[a]*bits[a] for a in range(d)) for bits in supports)
                ck(1-retained<=alpha/q,'independent optimum support bound')
    # Conservation makes the actual catalyst measurement insensitive to coherence.
    # A two-level A has no exact-feasible support; this tests the dephasing identity only.
    O=s.kronecker_product(s.diag(s.Rational(2,3),s.Rational(1,3)),s.Matrix([[s.Rational(1,2),s.Rational(1,3)],[s.Rational(1,3),s.Rational(1,2)]]))
    Hd=s.diag(0,1,1,2);R=s.eye(4);R[1,1]=R[2,2]=s.Rational(3,5);R[1,2]=-s.Rational(4,5);R[2,1]=s.Rational(4,5)
    P_A=s.diag(1,0,1,0)
    ck(R.H*R==s.eye(4),'rational conserving unitary')
    ck(R*Hd==Hd*R,'exact energy conservation')
    ck(s.trace(P_A*R*(O-s.diag(*O.diagonal()))*R.H)==0,'physical catalyst measurement dephases')
    # The same identity for contractions, with nonzero population leakage.
    A=s.diag(1,s.Rational(3,5),s.Rational(4,5),1)
    ck(s.trace((O-s.diag(*O.diagonal()))*(s.eye(4)-A.H*A))==0,'coherent leakage dephases')
    ck(s.trace(O*(s.eye(4)-A.H*A))>0,'nonzero leakage control')
    # Wrong-direction convex-distance inference is never used: positive pieces add.
    X=s.Matrix([[1,s.I],[s.Rational(1,2),0]]);D=s.diag(s.Rational(1,5),s.Rational(2,5));Ds=s.eye(2)/5;De=D-Ds
    ck(s.trace(X.H*X*D)==s.trace(X.H*X*Ds)+s.trace(X.H*X*De),'positive residual linearity')
    ck(s.trace(X.H*X*De)>=0,'positive excess residual')
    # Independent symbolic 2x2 spectral-bound determinant factorization.
    a,b,z=s.symbols('a b z',real=True)
    ck(s.expand((1+z-a)*(1+z-b)-z*z-((1-a)*(1-b)+z*(2-a-b)))==0,'Gershgorin determinant factorization')
    # Explicit complex phase is indispensable for four-projector spanning.
    projectors=[s.Matrix([[1,0],[0,0]]),s.Matrix([[0,0],[0,1]]),s.Matrix([[1,1],[1,1]])/2,s.Matrix([[1,-s.I],[s.I,1]])/2]
    ck(s.Matrix.hstack(*[s.Matrix(list(p)) for p in projectors]).det()!=0,'complex tomography independent')
    ck(s.Matrix.hstack(*[s.Matrix(list(p)) for p in projectors[:-1]+[projectors[2]]]).det()==0,'real-only negative control')
    # Full complex matrix-unit target, not only a real-projector or spectrum check.
    rt=s.sqrt(2)
    cols=[s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([1,1])/rt,s.Matrix([1,s.I])/rt]
    C=s.Matrix([[1,0,1/rt,1/rt],[0,1,1/rt,-s.I/rt],[1/rt,1/rt,1,(1-s.I)/2],[1/rt,s.I/rt,(1+s.I)/2,1]])
    for j in range(4):
        for l in range(4):ck(s.simplify((cols[l].H*cols[j])[0]-C[j,l])==0,'complex matrix-unit comparison')
    wrong=rt*cols[3]-cols[0]+s.I*cols[1]
    ck(wrong==s.Matrix([0,2*s.I]),'conjugate witness negative control')
    ck((wrong.H*wrong)[0]==4,'wrong phase nonzero residual')
    return n

def verify_report(data):assert data==m.report(),'report equality/pin'
if __name__=='__main__':
    import sys
    n=independent()
    path=Path(sys.argv[sys.argv.index('--report')+1]) if '--report' in sys.argv else ROOT/'lab/process/k1931-thermal-qubit-channel-stability.json'
    data=json.loads(path.read_text());verify_report(data)
    print('BASELINE PASS',n,'independently reconstructed exact controls')
    for fault in ('phase','scalar_weight','adjacency'):
        try:m.calculate(fault)
        except AssertionError as exc:print('DETECTED mathematical input',fault,str(exc))
        else:raise AssertionError('missed '+fault)
    for field in ('bound','script_sha256'):
        bad=dict(data);bad[field]='corrupted'
        try:verify_report(bad)
        except AssertionError as exc:print('DETECTED reporting/pin',field,str(exc))
        else:raise AssertionError('missed '+field)
    print('PASS',n,'independent controls;3math/1report/1pin faults')
