"""Finite exact controls for the analytic covariance averaging theorem."""
from pathlib import Path
import sympy as s
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
def trA(X):return s.Matrix(2,2,lambda i,j:sum(X[2*i+a,2*j+a] for a in range(2)))
def trS(X):return s.Matrix(2,2,lambda a,b:sum(X[2*i+a,2*i+b] for i in range(2)))
def calc(fault=None):
    n=0
    def ck(ok,msg):
        nonlocal n
        assert ok,msg;n+=1
    H=s.diag(0,1);HH=s.kronecker_product(H,s.eye(2))+s.kronecker_product(s.eye(2),H)
    U=s.eye(4);U[1,1]=U[2,2]=s.Rational(3,5);U[1,2]=s.Rational(4,5);U[2,1]=-s.Rational(4,5)
    if fault=='energy':U.row_swap(0,1)
    ck(U.H*U==s.eye(4),'unitarity');ck(U*HH==HH*U,'energy conservation')
    sigma=s.Matrix([[s.Rational(2,3),s.I/4],[-s.I/4,s.Rational(1,3)]]);sd=s.diag(*sigma.diagonal())
    V=s.diag(1,s.I);sigmas=[V**k*sigma*(V.H)**k for k in range(4)]
    ck(sum(sigmas,s.zeros(2))/4==sd,'phase twirl is energy pinching')
    ck(s.trace(H*sigma)==s.trace(H*sd),'mean energy retained')
    for i in range(2):
      for j in range(2):
        X=s.zeros(2);X[i,j]=1
        avS=s.zeros(2);avA=s.zeros(2)
        for k in range(4):
            W=V**k;Y=W.H*X*W
            actual=U*s.kronecker_product(X,sigmas[k])*U.H
            base=U*s.kronecker_product(Y,sigma)*U.H
            ck(trA(actual)==W*trA(base)*W.H,'channel orbit covariance')
            ck(trS(actual)==W*trS(base)*W.H,'return orbit covariance')
            avS+=W*trA(base)*W.H;avA+=W*trS(base)*W.H
        direct=U*s.kronecker_product(X,sd)*U.H
        ck(avS/4==trA(direct),'channel average linearity');ck(avA/4==trS(direct),'return average linearity')
    # Covariant dephasing target: coherent plus causes maximal return; pinched state has zero return.
    plus=s.ones(2)/2;CZ=s.diag(1,1,1,-1)
    for i in range(2):
      for j in range(2):
        X=s.zeros(2);X[i,j]=1;target=X if i==j else s.zeros(2)
        for sig in (plus,s.eye(2)/2):ck(trA(CZ*s.kronecker_product(X,sig)*CZ)==target,'same exact covariant channel')
    minus=s.Matrix([[1,-1],[-1,1]])/2
    ck(trS(CZ*s.kronecker_product(s.diag(0,1),plus)*CZ)==minus,'coherent return orthogonal')
    # SWAP implements a noncovariant reset: twirling changes the target.
    SW=s.eye(4);SW.row_swap(1,2)
    if fault=='swap':SW=s.eye(4)
    a=trA(SW*s.kronecker_product(s.diag(1,0),plus)*SW)
    b=trA(SW*s.kronecker_product(s.diag(1,0),s.eye(2)/2)*SW)
    ck(a!=b,'noncovariant target counterexample')
    return {'exact_checks':n,'exact_covariant_example':'dephasing via CZ: coherent plus return 1, pinched return 0','noncovariant_counterexample':'SWAP reset plus changes to reset I/2','theorem':'same unitary, pinched catalyst, no larger covariant-target diamond error or worst-case marginal/product-return error','scope':'finite systems; invariant bath; conserving unitary; convex invariant feasible preparation set'}
def report():
    x=calc();x['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();x['evidence_kind']='finite matrix controls; analytic convexity/covariance proof carries generality';return x
if __name__=='__main__':
    import sys
    r=report()
    if '--write' in sys.argv:(ROOT/'lab/process/k1933-covariant-catalyst-dephasing-reduction.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r))
