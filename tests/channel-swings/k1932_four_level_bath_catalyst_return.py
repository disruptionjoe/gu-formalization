"""Exact full-shell unitary construction and finite all-input marginal returns."""
from pathlib import Path
import hashlib,json
from fractions import Fraction as F
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def vectors():return [s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([1,1])/s.sqrt(2),s.Matrix([1,s.I])/s.sqrt(2)]
def zero(M):return all(s.simplify(x)==0 for x in M)
def shell(l,e,j,fault=None):
    m=4*l;U=s.zeros(m);v=vectors()[j]
    if fault=='phase' and j==3:v=s.conjugate(v)
    x=s.Matrix([[1,1],[1,-1]])*v/s.sqrt(2)
    for a in range(2*l):
        k=a if a<l else a-l;parity=e if a<l else 1-e
        rows=[parity+4*k,parity+4*k+2]
        if fault=='pair' and a==l:rows=[e+4*k,e+4*k+2]
        col=e+2*a;other=1-e+2*a
        U[rows[0],col]=x[0];U[rows[1],col]=x[1]
        U[rows[0],other]=-s.conjugate(x[1]);U[rows[1],other]=s.conjugate(x[0])
    return U

def edge_shell(m,b,j,fault=None):
    U=s.eye(m);v=vectors()[j]
    if fault=='phase' and j==3:v=s.conjugate(v)
    x=s.Matrix([[1,1],[1,-1]])*v/s.sqrt(2);other=b^1
    U[b,b]=x[0];U[other,b]=x[1]
    U[b,other]=-s.conjugate(x[1]);U[other,other]=s.conjugate(x[0])
    return U

def data(l,N,t,j,fault=None,refined=False):
    m=4*l;d=2*N+2*m-3;S=list(range(m-1,m-1+2*N,2));Z=sum(t**b for b in range(m))
    probs=[t**b/Z for b in range(m)];out=[s.S(0)]*d
    if fault=='bath':probs[0]+=s.Rational(1,100)
    us=[shell(l,e,j,fault) for e in (0,1)]
    for n in S:
        for b,p in enumerate(probs):
            E=n+b;e=(E-1)%2;U=us[e]
            if refined and len([bb for bb in range(m) if E-bb in S])==1:
                assert l==1;U=edge_shell(m,b,j,fault)
            assert m-1<=E<=d-1,'full occupied shell'
            for bout in range(m):
                aout=E-bout
                out[aout]+=p*s.simplify(s.conjugate(U[bout,b])*U[bout,b])/N
    if fault=='normalization':out[0]+=s.Rational(1,100)
    return S,[s.simplify(x) for x in out],probs

def expected(l,N,t,c=s.Rational(1,2)):
    m=4*l;Z=sum(t**b for b in range(m))
    return s.simplify(t**(2*l)/(1+t**(2*l))+sum((t**(2*a)+t**(2*a+1))*(a+1-c)/Z for a in range(l))/N)

def calculate(fault=None):
    checks=0
    def check(ok,label):
        nonlocal checks
        if not ok:raise AssertionError(label)
        checks+=1
    vs=vectors();examples=[]
    for l in (1,2):
        m=4*l
        for e in (0,1):
            us=[shell(l,e,j,fault) for j in range(4)]
            for j,U in enumerate(us):
                check(zero(U.H*U-s.eye(m)),'shell unitary')
                for a in range(2*l):
                    col=e+2*a
                    for k,V in enumerate(us):
                        check(s.simplify((V[:,col].H*U[:,col])[0]-(vs[k].H*vs[j])[0])==0,'full complex Gram target')
                E=20+e
                H=s.diag(*[b+(E-b) for b in range(m)])
                check(zero(U*H-H*U),'additive energy shell')
        for N in (l,2*l,5*l):
            for t in (s.Rational(1,2),s.Rational(2,3)):
                distances=[]
                for j,c in enumerate([s.Rational(1,2),s.Rational(1,2),1,s.Rational(1,2)]):
                    S,out,p=data(l,N,t,j,fault);d=len(out)
                    check(sum(out)==1,'output normalization')
                    check(all(x>=0 for x in out),'positive output')
                    check(all(out[a]<=s.Rational(1,N) for a in S),'no support overshoot')
                    r=sum(abs(out[a]-(s.Rational(1,N) if a in S else 0)) for a in range(d))/2
                    check(s.simplify(r-expected(l,N,t,c))==0,'finite exact return formula')
                    check(s.simplify(r-(1-sum(out[a] for a in S)))==0,'support measurement tight')
                    distances.append(r)
                check(max(distances)==expected(l,N,t),'all input supremum')
                if t==s.Rational(1,2):examples.append({'bath_levels':4*l,'occupied_levels':N,'return':str(max(distances))})
    refined_examples=[]
    for N in (1,2,3,6):
        for t in (s.Rational(1,2),s.Rational(2,3)):
            pH=t*t/(1+t*t);target=pH+(s.Rational(1,2)-pH)/N
            for j,c in enumerate([s.Rational(1,2),s.Rational(1,2),1,s.Rational(1,2)]):
                S,out,p=data(1,N,t,j,fault,refined=True)
                check(sum(out)==1 and all(x>=0 for x in out),'refined positive normalization')
                check(all(out[a]<=s.Rational(1,N) for a in S),'refined no support overshoot')
                r=sum(abs(x-(s.Rational(1,N) if a in S else 0)) for a,x in enumerate(out))/2
                check(s.simplify(r-(pH*(1-s.Rational(1,N))+(1-c)/N))==0,'refined finite return')
                for b in range(4):
                    U=edge_shell(4,b,j,fault)
                    check(zero(U.H*U-s.eye(4)),'edge unitary')
                    for k in range(4):
                        V=edge_shell(4,b,k,fault)
                        check(s.simplify((V[:,b].H*U[:,b])[0]-(vs[k].H*vs[j])[0])==0,'edge complex Gram')
            loss=s.S(0)
            for E in range(len(out)+3):
                weights=[p[b]/N for b in range(4) if E-b in S]
                rnk=len(weights)
                if rnk:
                    eigenvalues=sorted([w/2 for w in weights for _ in range(2)],reverse=True)
                    loss+=sum(weights)-sum(eigenvalues[:rnk])
            check(s.simplify(loss-target)==0,'fixed preparation Ky Fan lower bound')
            if t==s.Rational(1,2):refined_examples.append({'occupied_levels':N,'minimax_return':str(target)})
    check(expected(1,2,s.Rational(1,2))==s.Rational(2,5),'first strict escape')
    for l in range(1,8):
        for N in (l,10*l,100*l):
            for t in (F(1,3),F(1,2),F(3,4)):
                Z=sum(t**b for b in range(4*l));r=t**(2*l)/(1+t**(2*l))+sum((t**(2*a)+t**(2*a+1))*(a+F(1,2))/Z for a in range(l))/N
                check(r<=t**(2*l)+(t*t/(1-t*t)+F(1,2))/N,'growing bath resource bound')
    return {'exact_checks':checks,'examples':examples,'refined_four_level_examples':refined_examples,'fixed_uniform_preparation_minimax':'t^2/(1+t^2)+(1/2-t^2/(1+t^2))/N','formula':'t^(2l)/(1+t^(2l)) + sum_a[(t^(2a)+t^(2a+1))/Z_B]*(a+1/2)/N','assumptions':'m=4l,N>=l,0<t<1, nondegenerate equally spaced energies, uniform odd-level catalyst, marginal return','global_optimum_claimed':False}

def report():
    out=calculate();out['evidence_kind']='exact finite shell matrices and rational controls; analytic proof carries all l,N,t';out['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();return out
if __name__=='__main__':
    import sys
    out=report()
    if '--write' in sys.argv:(ROOT/'lab/process/k1932-four-level-bath-catalyst-return.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))
