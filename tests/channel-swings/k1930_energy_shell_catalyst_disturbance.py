"""Exact conserving matrices, all complex channel entries and return states."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,itertools
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def vectors():return [s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([1,1])/s.sqrt(2),s.Matrix([1,s.I])/s.sqrt(2)]
def equal(x,y):return all(s.simplify(a-b)==0 for a,b in zip(x,y)) if isinstance(x,(s.MatrixBase,list,tuple)) else s.simplify(x-y)==0

def construct(d=5,m=2,t=s.Rational(1,2),coherent=False,fault=None):
    spacing=2 if m==2 else 3;S=list(range(1,d-1,spacing));weights=[t**a for a in S];Z=sum(weights)
    sigma=s.zeros(d)
    for a,w in zip(S,weights):sigma[a,a]=w/Z
    if coherent and len(S)==2:
        a,b=S;sigma[a,b]=sigma[b,a]=s.sqrt(sigma[a,a]*sigma[b,b])
    tau=s.diag(*[t**b/sum(t**c for c in range(m)) for b in range(m)])
    Omega=s.Matrix(s.kronecker_product(tau,sigma));H=s.diag(*[b+a for b in range(m) for a in range(d)])
    us=[s.eye(m*d) for _ in range(4)];vs=vectors();root=s.sqrt(2)
    if fault=='phase':vs[3]=s.conjugate(vs[3])
    for E in range(d+m-1):
        ids=[b*d+a for b in range(m) for a in range(d) if a+b==E]
        active=[i for i in ids if i%d in S]
        if not active:continue
        assert len(active)==1,'rank-one shell'
        a=active[0];b=next(i for i in ids if i!=a)
        W=s.Matrix([[1,1],[1,-1]])/root
        for j,v in enumerate(vs):
            x=W*v
            M=s.Matrix([[x[0],-s.conjugate(x[1])],[x[1],s.conjugate(x[0])]])
            for r,idx in enumerate((a,b)):
                for c,jdx in enumerate((a,b)):us[j][idx,jdx]=M[r,c]
    if fault=='unitary_entry':us[2][1,1]+=1
    if fault=='bath_weight':Omega[1,1]+=s.Rational(1,100)
    if fault=='energy':H[1,1]+=s.Rational(1,7)
    return S,sigma,Omega,H,us

def partial_B(X,d,m):return s.Matrix(d,d,lambda a,b:sum(X[c*d+a,c*d+b] for c in range(m)))

def calculate(fault=None):
    n=0
    def check(x,label):
        nonlocal n
        if not x:raise AssertionError(label)
        n+=1
    vs=vectors();projectors=[v*v.H for v in vs]
    check(s.Matrix.hstack(*[s.Matrix(list(p)) for p in projectors]).rank()==4,'extreme projectors')
    for d,m,coherent in [(3,2,False),(5,2,False),(5,2,True),(6,3,False)]:
        S,sigma,Omega,H,us=construct(d,m,coherent=coherent,fault=fault)
        P=s.diag(*[int(a in S) for a in range(d)]);mean=s.zeros(d)
        for j,U in enumerate(us):
            check(equal(U*U.H,s.eye(d*m)),'unitary')
            check(equal(U*H,H*U),'energy commutator')
            out=partial_B(U*Omega*U.H,d,m)
            check(equal(s.trace(out),1),'output trace')
            for l,V in enumerate(us):
                check(equal(s.trace(U*Omega*V.H),(vs[l].H*vs[j])[0]),'all matrix-unit target coefficient')
            if j<2:mean+=out/2
            if not coherent:
                c=[s.Rational(1,2),s.Rational(1,2),1,s.Rational(1,2)][j]
                check(equal(P*out*P,c*sigma),'support survival')
                distance=sum(abs(out[a,a]-sigma[a,a]) for a in range(d))/2
                check(equal(distance,1-c),'sharp marginal return')
        check(equal(s.trace(P*mean),s.Rational(1,2)),'coherent-safe half support probability')
    S,sigma,Omega,H,us=construct();o=2*partial_B(us[0]*Omega*us[0].H,5,2)-sigma
    check(equal(list(o.diagonal()),[s.Rational(8,15),0,s.Rational(2,5),0,s.Rational(1,15)]),'explicit displaced state')
    for d in range(3,10):
        for t in (F(1,2),F(2,3)):
            best=F(0)
            for bits in itertools.product((0,1),repeat=d):
                cells=[[a for b in range(3) for a in range(d) if a+b==E] for E in range(d+2)]
                ok=all(2*sum(bits[a] for a in cell)<=len(cell) for cell in cells)
                if ok:best=max(best,sum(t**a for a in range(d) if bits[a]))
            M=d//3;p=t*(1-t**(3*M))/((1+t+t*t)*(1-t**d))
            check(best/sum(t**a for a in range(d))==p,'qutrit Gibbs optimizer')
    return {'exact_checks':n,'optimal_uniform_return':'1/2','qubit_example_displaced_state':['8/15','0','2/5','0','1/15'],'finite_error_bound_claimed':False}

def report():
    data=calculate();data['evidence_kind']='finite exact complex matrices and rational enumeration; universal scope is analytic'
    data['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();return data
if __name__=='__main__':
    import sys
    out=report()
    if '--write' in sys.argv:(ROOT/'lab/process/k1930-energy-shell-catalyst-disturbance.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))
