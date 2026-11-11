from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[2]
checks=[];controls=[]
def check(name,condition):
    assert bool(condition),name
    checks.append(name)
def control(name,rejected):
    assert bool(rejected),name
    controls.append(name)
def finish(slug,details):
    report=dict(artifact=slug,grade="exact finite supporting algebra; written universal proofs separate",supporting_checks=checks,contrary_controls=controls,details=details)
    report=json.loads(json.dumps(report))
    target=ROOT/"lab/process"/(slug+".json")
    if "--write" in sys.argv:target.write_text(json.dumps(report,indent=2)+"\n")
    else:assert json.loads(target.read_text())==report,"report replay mismatch"
    print(slug,len(checks),"supporting",len(controls),"contrary")
import sympy as s
I=s.I;E=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);Z=s.diag(1,-1)
gam=[s.kronecker_product(X,E),s.kronecker_product(Y,E),s.kronecker_product(Z,X),s.kronecker_product(Z,Y)]
results={}
for sig in [(1,1,1,1),(1,1,1,-1)]:
    g=[gam[j]*(1 if sig[j]==1 else I) for j in range(4)]
    check(str(sig)+" Clifford",all(g[j]*g[k]+g[k]*g[j]==2*(sig[j] if j==k else 0)*s.eye(4) for j in range(4) for k in range(4)))
    Gamma=s.Matrix.hstack(*g);lift=s.Matrix.vstack(*[sig[j]*g[j] for j in range(4)])/4
    P=s.eye(16)-lift*Gamma
    check(str(sig)+" projector and kernel",P*P==P and Gamma*P==s.zeros(4,16) and P.rank()==12)
    for xi in [(1,0,0,0),(1,2,0,0)]:
        cliff=sum((xi[j]*g[j] for j in range(4)),s.zeros(4))
        Q=P*s.diag(*([cliff]*4))*P
        check(str(sig)+str(xi)+" generic full constrained rank",Q.rank()==12)
    if sig[-1]==-1:
        xi=(1,0,0,1);cliff=g[0]+g[3];Q=P*s.diag(*([cliff]*4))*P
        h=s.Matrix.vstack(*[xi[j]*cliff for j in range(4)])
        check("null characteristic witness remains nonzero",h.rank()>0 and Gamma*h==s.zeros(4) and Q*h==s.zeros(16,4))
        control("null witness does not prove invertibility everywhere",Q.rank()<12)
        results['null_rank']=Q.rank();results['null_gauge_rank']=h.rank()
# Exact polynomial symbol coefficient constraints, not a sample-point verdict.
t,x=s.symbols('t x');D=s.Matrix([[t,x],[x,t]])
for m in range(4):
    coeff=s.symbols('c:'+str(2*(m+1)))
    R=s.Matrix([sum(coeff[j*(m+1)+k]*t**k*x**(m-k) for k in range(m+1)) for j in range(2)])
    equations=[v for f in D*R for v in s.Poly(f,t,x).coeffs()]
    A,_=s.linear_eq_to_matrix(equations,coeff)
    check('polynomial gauge degree'+str(m)+' has zero kernel',A.rank()==len(coeff))
control("characteristic restriction creates false global gauge",D.subs(t,x)*s.Matrix([1,-1])==s.zeros(2,1) and D*s.Matrix([1,-1])!=s.zeros(2,1))
H=s.Matrix([[t,t],[t,t]]);R=s.Matrix([1,-1])
check("coupled repair with invertible diagonal",H*R==s.zeros(2,1) and H[0,0]!=0 and H.det()==0)
check("Schur complement vanishes",s.cancel(H[1,1]-H[1,0]/H[0,0]*H[0,1])==0)
control("isolated block conclusion fails for coupled gauge",H[0,0]*R[0]!=0)
Hbad=H+s.Matrix([[0,0],[0,x]])
control("Schur mutation removes gauge identity",Hbad*R!=s.zeros(2,1) and Hbad.det()!=0)
finish('p3-rs-local-gauge-necessity',dict(clifford_dimension=4,signatures=['4,0','3,1'],null_control=results,polynomial_degrees=list(range(4)),universal_proof='highest-symbol polynomial identity and descending-order argument in note'))
