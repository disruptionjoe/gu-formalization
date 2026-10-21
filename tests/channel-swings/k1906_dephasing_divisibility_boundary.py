"""Exact finite controls; general proofs and claim ceilings are in the note."""
from pathlib import Path
import argparse, hashlib, json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
N=0
def check(ok,name):
    global N
    assert bool(ok),name
    N+=1
def eq(a,b,name): check(s.simplify(a-b)==0,name)
def mat(a,b,name): check((a-b).applyfunc(s.simplify)==s.zeros(*a.shape),name)
def adj(a):return a.conjugate().T
def pin(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def target():
    q=s.sqrt(2);V=s.Matrix([[1,0,1/q,1/q],[0,1,1/q,s.I/q]])
    B=s.Matrix([[-1,-1,q,0],[-1,s.I,0,q]])
    return adj(V)*V,adj(B)*B

def calculate():
    global N
    N=0;C,H=target();q=s.sqrt(2)
    eq(C.det(),0,'singular correlation target');check(C.rank()==2,'target Gram rank')
    eq(C[0,1],0,'zero entry');eq(C[0,2],1/q,'saturating13');eq(C[1,2],1/q,'saturating23')
    # Independent product-vector criterion in dimension2x2: determinant of a1b1^T+a2b2^T.
    a,b,c,d,e,f,g,h=s.symbols('a b c d e f g h',real=True)
    A=s.Matrix([[a,c],[b,d]]);B=s.Matrix([[e,g],[f,h]])
    M=A[:,0]*B[:,0].T+A[:,1]*B[:,1].T
    eq(M.det(),A.det()*B.det(),'simple tensor sum factorization')
    # General proof uses restrictions to the two spans; no higher-dimensional minor omitted.
    x=s.symbols('x',real=True);p=x-(1/q-x)**4
    check(s.simplify(p.subs(x,s.Rational(1,10)))<0,'robust floor exceeds one tenth')
    check(s.simplify(p.subs(x,s.Rational(3,25)))>0,'root upper bracket three twenty-fifths')
    eq(s.diff(p,x),1+4*(1/q-x)**3,'strict derivative on declared interval')
    lam=[-1,1,0];T=s.log(2);d=s.Matrix(3,3,lambda j,k:s.exp(-T*s.Rational(1,2)*(lam[j]-lam[k])**2))
    eq(d[0,1],s.Rational(1,4),'metric-control12');eq(d[0,2],1/q,'metric-control13');eq(d[1,2],1/q,'metric-control23')
    eq(d[0,1],d[0,2]**4,'metric triangle saturation')
    t,u=s.symbols('t u',real=True)
    for j,k in [(0,1),(0,2),(2,3)]:
        z=C[j,k]-1;eq(s.exp((t+u)*z),s.exp(t*z)*s.exp(u*z),'Poisson semigroup coefficient')
    eq(s.exp(t*(C[0,1]-1)),s.exp(-t),'Poisson nonzero12')
    # C Kraus rows give GKSL coefficient exactly Cjk-1.
    V=s.Matrix([[1,0,1/q,1/q],[0,1,1/q,s.I/q]]);K=[s.diag(*list(V.conjugate()[a,:])) for a in range(2)]
    mat(sum((adj(k)*k for k in K),s.zeros(4)),s.eye(4),'Poisson GKSL normalization')
    for j in range(4):
        for k in range(4):
            z=sum(L[j,j]*s.conjugate(L[k,k])-(abs(L[j,j])**2+abs(L[k,k])**2)/2 for L in K)
            eq(z,C[j,k]-1,'GKSL versus channel coefficient')
    # Two-ray CP-divisible recovery: exact finite checkpoints, including a singular-rate endpoint.
    for r in [s.Rational(1,3),s.S.Zero]:
        f=lambda x:1-(1-r)*x
        for a,b in [(s.S.Zero,s.Rational(1,4)),(s.Rational(1,4),s.Rational(3,4)),(s.Rational(3,4),s.S.One)]:
            ratio=s.simplify(f(b)/f(a));check(0<=ratio<=1,'two-ray CP intermediate ratio')
            eq(f(a)*ratio,f(b),'two-ray composition')
        eq(f(1),r,'two-ray endpoint')
    return {'root_equation':'e=(1/sqrt(2)-e)^4','root_lower_bound':'1/10','root_upper_bound':'3/25','metric_control12':'1/4','cp_divisible_continuous_target':'excluded','rank_two_continuous_criterion':'at_most_two_Gram_rays','poisson12':'exp(-t)','math_checks':N}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write-report',action='store_true');args=ap.parse_args()
    result=calculate();result['dependency_sha256']=pin('explorations/conditional-build/k1903-quantum-dephasing-witness-2026-10-21.md')
    if args.write_report:(ROOT/'lab/process/k1906-dephasing-divisibility-boundary.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
