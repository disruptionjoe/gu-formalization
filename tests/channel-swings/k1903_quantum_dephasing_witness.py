"""Exact finite controls; analytic scope is in the linked research note."""
from pathlib import Path
import argparse, hashlib, json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
COUNT=0
def check(ok, name):
    global COUNT
    assert bool(ok), name
    COUNT+=1
def eq(a,b,name): check(s.simplify(a-b)==0,name)
def mat(a,b,name): check((a-b).applyfunc(s.simplify)==s.zeros(*a.shape),name)
def pin(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()

def calculate(sign=1,delta_shift=0):
    global COUNT
    COUNT=0
    q=s.sqrt(2);V=s.Matrix([[1,0,1/q,1/q],[0,1,1/q,s.I/q]])
    C=V.conjugate().T*V;B=s.Matrix([[-1,-1,q,0],[-1,sign*s.I,0,q]]);H=B.conjugate().T*B
    mat(B*V.conjugate().T,s.zeros(2,2),'kernel annihilation')
    check(C.rank()==2,'positive Gram rank');check(list(C.diagonal())==[1]*4,'correlation diagonal')
    eq(s.trace(H*C),0,'quantum witness value')
    delta=6-4*q+delta_shift;eq(4/(2+q)**2,delta,'classical witness constant')
    z=s.Matrix([1,1,1,(1-s.I)/q]);eq((z.conjugate().T*H*z)[0],delta,'sharp phase control')
    eq(s.trace(H),8,'white-dephasing witness slope')
    lam=s.symbols('lam');eq((B*B.conjugate().T).charpoly(lam).as_expr(),lam**2-8*lam+14,'witness spectrum')
    offdiag=sum(abs(H[i,j]) for i in range(4) for j in range(4) if i!=j)
    eq(offdiag,10*q,'entrywise error coefficient')
    U=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[1,-1],[1,1]])/q,s.Matrix([[1,-s.I],[-s.I,1]])/q]
    for j,u in enumerate(U):
        mat(u.conjugate().T*u,s.eye(2),'environment unitary')
        mat(u[:,0],V[:,j].conjugate(),'environment overlap orientation')
    K=[s.diag(*list(V.conjugate()[j,:])) for j in range(2)]
    mat(sum((k.conjugate().T*k for k in K),s.zeros(4)),s.eye(4),'trace preservation')
    rho=s.ones(4)/4
    mat(sum((k*rho*k.conjugate().T for k in K),s.zeros(4)),C/4,'one preparation output')
    projectors=[V[:,j]*V[:,j].conjugate().T for j in range(4)]
    check(s.Matrix.hstack(*[p.reshape(4,1) for p in projectors]).rank()==4,'Hermitian span')
    return {'delta':'6-4*sqrt(2)','witness_norm':'4+sqrt(2)','offdiag_error_factor':'10*sqrt(2)','noise_exclusion_threshold':'(3-2*sqrt(2))/4','rank':2,'C':[[str(x) for x in C.row(i)] for i in range(4)],'H':[[str(x) for x in H.row(i)] for i in range(4)],'math_checks':COUNT}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write-report',action='store_true');args=ap.parse_args()
    result=calculate();result['dependency_sha256']=pin('explorations/conditional-build/k1900-sharp-phase-noise-cost-2026-10-21.md')
    if args.write_report: (ROOT/'lab/process/k1903-quantum-dephasing-witness.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
