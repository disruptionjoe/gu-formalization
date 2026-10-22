"""Independent amplitude construction, pair projector and coherence controls."""
from pathlib import Path
import sympy as s
import importlib.util,json
ROOT=Path(__file__).resolve().parents[2]
P=Path(__file__).with_name('k1930_energy_shell_catalyst_disturbance.py')
spec=importlib.util.spec_from_file_location('producer',P);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def independent():
    n=0
    def ck(x):
        nonlocal n
        assert x,'independent mathematical check';n+=1
    # Target amplitudes reconstructed directly, without calling producer vectors/W.
    xs=[s.Matrix([1,1])/s.sqrt(2),s.Matrix([1,-1])/s.sqrt(2),s.Matrix([1,0]),s.Matrix([1+s.I,1-s.I])/2]
    ck(s.simplify(xs[0]*xs[0].H+xs[1]*xs[1].H)==s.eye(2))
    C=s.Matrix([[1,0,1/s.sqrt(2),1/s.sqrt(2)],[0,1,1/s.sqrt(2),-s.I/s.sqrt(2)],[1/s.sqrt(2),1/s.sqrt(2),1,(1-s.I)/2],[1/s.sqrt(2),s.I/s.sqrt(2),(1+s.I)/2,1]])
    for j in range(4):
        for l in range(4):ck(s.simplify((xs[l].H*xs[j])[0]-C[j,l])==0)
    # Independent Kraus blocks indexed by initial/final bath index, d=5.
    d=5;sig=s.diag(0,s.Rational(4,5),0,s.Rational(1,5),0);tau=[s.Rational(2,3),s.Rational(1,3)]
    for j,x in enumerate(xs):
        q=s.zeros(d)
        for a in (1,3):
            for b in (0,1):
                weight=sig[a,a]*tau[b]
                q[a,a]+=s.simplify(weight*x[0]*s.conjugate(x[0]))
                other=a+(2*b-1)
                q[other,other]+=s.simplify(weight*x[1]*s.conjugate(x[1]))
        ck(s.trace(q)==1);ck(sum(abs(q[a,a]-sig[a,a]) for a in range(d))/2==[s.Rational(1,2),s.Rational(1,2),0,s.Rational(1,2)][j])
    # Rank-one shell projector bound in a three-dimensional shell, not just 2D identity.
    X=s.Matrix([1,1,1])/s.sqrt(3);Y=s.Matrix([1,-1,0])/s.sqrt(2)
    ck((X.H*Y)[0]==0)
    R=(X*X.H+Y*Y.H)/2
    ck(R[0,0]==s.Rational(5,12));ck(R[0,0]<=s.Rational(1,2))
    # Exact coherent sigma measurement dephasing identity for any block diagonal P.
    S,sigma,O,H,us=m.construct(5,2,coherent=True)
    P=s.diag(*[int(a in S) for b in range(2) for a in range(5)])
    for j,U in enumerate(us):
        for l,V in enumerate(us):ck(s.simplify(s.trace(U*O*V.H)-C[j,l])==0)
    deph=s.diag(*O.diagonal());out=(us[0]*O*us[0].H+us[1]*O*us[1].H)/2
    outd=(us[0]*deph*us[0].H+us[1]*deph*us[1].H)/2
    ck(s.simplify(s.trace(P*(out-outd)))==0)
    ck(s.simplify(s.trace(P*out))==s.Rational(1,2))
    return n

def verify_report(data):assert data==m.report(),'report equality/pin'
if __name__=='__main__':
    n=independent();data=json.loads((ROOT/'lab/process/k1930-energy-shell-catalyst-disturbance.json').read_text());verify_report(data)
    print('BASELINE PASS',n,'separately reconstructed exact controls')
    for fault in ('unitary_entry','bath_weight','energy','phase'):
        try:m.calculate(fault)
        except AssertionError as e:print('DETECTED mathematical input',fault,str(e))
        else:raise AssertionError('missed '+fault)
    for field in ('optimal_uniform_return','script_sha256'):
        bad=dict(data);bad[field]='corrupted'
        try:verify_report(bad)
        except AssertionError as e:print('DETECTED reporting/pin',field,str(e))
        else:raise AssertionError('missed '+field)
    print('PASS',n,'independent controls;4math/1report/1pin faults')
