"""Exact rational finite-jet checks; --write saves the reproducible report."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import permutations

n=14
eta=(1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1)
pairs=((0,1),(4,2),(5,3),(6,10),(7,11),(8,12),(9,13))
owner={i:r for r,p in enumerate(pairs) for i in p}
lam=[F(27,28) if i in {0,1,2,3,10} else F(-15,28) for i in range(n)]
t=[lam[p]+lam[q] for p,q in pairs]
d=[[F(0) if owner[i]==r else lam[i]/6+t[r]/70+t[owner[i]]/420 for i in range(n)] for r in range(7)]
assert all(sum(row)==0 for row in d)
assert all(sum(d[r][i] for r in range(7))==lam[i] for i in range(n))
K=[defaultdict(F) for l in range(n)]
for r,(p,q) in enumerate(pairs):
    for i in range(n):
        for a in (p,q):
            K[p][i,i,a]+=eta[i]*d[r][i]
            K[p][i,a,i]-=eta[i]*d[r][i]
K=[{key:v for key,v in A.items() if v} for A in K]
def get(A,i,j,k):return A.get((i,j,k),F(0))
def hook(A):
    for i,j,k in A:
        assert get(A,i,j,k)==-get(A,i,k,j)
        assert get(A,i,j,k)+get(A,j,k,i)+get(A,k,i,j)==0
    assert all(sum(eta[i]*get(A,i,i,k) for i in range(n))==0 for k in range(n))
def gram(A,B):return sum(F(eta[i]*eta[j]*eta[k],2)*v*get(B,i,j,k) for (i,j,k),v in A.items())
def polar_sigma(A,B):
    out=defaultdict(F)
    for (i,j,k),a in A.items():
        if j>=k:continue
        for (ii,l,m),b in B.items():
            if ii!=i or l>=m or len({j,k,l,m})!=4:continue
            seq=(j,k,l,m)
            sign=(-1)**sum(seq[x]>seq[y] for x in range(4) for y in range(x+1,4))
            out[tuple(sorted(seq))]+=eta[i]*sign*a*b
    return {key:v for key,v in out.items() if v}
for A in K:hook(A)
assert any(K)
for l in range(n):
    for m in range(n):
        assert gram(K[l],K[m])==0
        assert not polar_sigma(K[l],K[m])
B=[[sum(eta[k]*get(K[k],i,k,j) for k in range(n)) for j in range(n)] for i in range(n)]
assert all(B[i][j]==(-eta[i]*lam[i] if i==j else 0) for i in range(n) for j in range(n))
assert F(90,7)-F(279,196)*F(280,31)==0
# Failure-capable controls: remove a null partner, and use nonzero sigma hook.
p,q=pairs[0]
bad={key:v for key,v in K[p].items() if q not in key[1:]}
assert gram(bad,bad)!=0
def H(a,b,c):return {(a,b,c):F(1),(a,c,b):F(-1),(b,a,c):F(1),(b,c,a):F(-1)}
A=H(0,4,5);A.update(H(0,6,7))
assert polar_sigma(A,A)
# K2375's old jet remains incompatible; independently build and contract it.
g=lambda i,j:eta[i] if i==j else 0
S0={(i,i):-F(13,168)*eta[i]*lam[i] for i in range(n)}
def J(l,T):
    out={}
    for i in range(n):
        for j in range(n):
            for k in range(n):
                v=g(l,j)*T.get((i,k),0)-g(l,k)*T.get((i,j),0)-(g(i,j)*T.get((l,k),0)-g(i,k)*T.get((l,j),0))/F(n-1)
                if v:out[i,j,k]=v
    return out
old=[J(l,S0) for l in range(n)]
assert sum(eta[l]*gram(old[l],old[l]) for l in range(n))==F(1755,3136)
# Check the full right inverse on tracefree symmetric, hook, signed, mixed C.
C3={(0,0,0):F(1)}
for key in set(permutations((0,4,4))):C3[key]=F(-1)
def hook_C(a,b):
    out={}
    for q,sign in ((a,1),(b,-1)):
        out[0,q,q]=F(2*sign*eta[q])
        out[q,0,q]=out[q,q,0]=F(-sign*eta[q])
    return out
Cs=[C3,hook_C(4,5),hook_C(1,5)]
mix=defaultdict(F)
for idx,C in enumerate(Cs):
    for key,v in C.items():mix[key]+=(idx+1)*v
Cs.append(dict(mix))
def cget(C,l,i,j):return C.get((l,i,j),F(0))
for C in Cs:
    assert all(cget(C,l,i,j)==cget(C,l,j,i) for l,i,j in C)
    assert all(sum(eta[i]*cget(C,l,i,i) for i in range(n))==0 for l in range(n))
    assert all(sum(eta[i]*cget(C,i,i,l) for i in range(n))==0 for l in range(n))
    S={}
    for l in range(n):
        for i in range(n):
            for j in range(n):
                sym=(cget(C,l,i,j)+cget(C,i,l,j)+cget(C,j,l,i))/3
                v=F(13,180)*sym+F(26,363)*(cget(C,l,i,j)-sym)
                if v:S[l,i,j]=v
    assert all(sum(eta[i]*cget(S,l,i,i) for i in range(n))==0 for l in range(n))
    assert all(sum(eta[i]*cget(S,i,i,l) for i in range(n))==0 for l in range(n))
    # Memoize J_m(S_l); assemble symmetric L sparsely.
    Js={(l,m):J(m,{(i,j):v for (ll,i,j),v in S.items() if ll==l}) for l in range(n) for m in range(n)}
    L={}
    for l in range(n):
        for m in range(n):
            keys=set(Js[l,m])|set(Js[m,l])
            L[l,m]={key:(Js[l,m].get(key,0)+Js[m,l].get(key,0))/2 for key in keys}
            L[l,m]={key:v for key,v in L[l,m].items() if v}
            hook(L[l,m])
    assert all(L[l,m]==L[m,l] for l in range(n) for m in range(n))
    for l in range(n):
        for i in range(n):
            for j in range(n):
                value=sum(eta[m]*(get(L[l,m],i,m,j)+get(L[l,m],j,m,i)) for m in range(n))
                assert value==cget(C,l,i,j),(l,i,j,value,cget(C,l,i,j))
print('PASS: hook, actual B, 196 Gram pairs, 196 sigma pairs, failed controls, four second-jet right-inverse fixtures')


# Exact next compatibility test and actual geometry backend verification.
"""Tiny exact successor calculation; analytic curvature formulas require backend cross-check."""
from fractions import Fraction as F
import sympy as s
n=14;eta=(1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1)
pairs=((0,1),(4,2),(5,3),(6,10),(7,11),(8,12),(9,13))
owner={i:r for r,p in enumerate(pairs) for i in p}
lam=[F(27,28) if i in {0,1,2,3,10} else F(-15,28) for i in range(n)]
t=[lam[p]+lam[q] for p,q in pairs]
d=[[F(0) if owner[i]==r else lam[i]/6+t[r]/70+t[owner[i]]/420 for i in range(n)] for r in range(7)]
K={}
for r,(p,q) in enumerate(pairs):
    for i in range(n):
        for j in (p,q):
            if d[r][i]:
                K[p,i,i,j]=eta[i]*d[r][i]
                K[p,i,j,i]=-eta[i]*d[r][i]
kg=lambda l,i,j,k:K.get((l,i,j,k),F(0))
P=[[sum(eta[i]*kg(i,i,a,b) for i in range(n)) for b in range(n)] for a in range(n)]
assert not any(v for row in P for v in row)
X=sum(F(eta[i]*eta[j]*eta[a]*eta[b],2)*kg(i,j,a,b)*kg(j,i,a,b) for i in range(n) for j in range(n) for a in range(n) for b in range(n))
Y=sum(eta[i]*eta[j]*eta[a]*eta[b]*kg(j,a,i,b)*kg(i,a,j,b) for i in range(n) for j in range(n) for a in range(n) for b in range(n))
Bnorm=sum(v*v for v in lam)
rhs=F(4,3)*(Bnorm+Y-2*X)
# Actual adapted orthonormal frame: E_a=g*S_a in vertical symmetric matrices.
g=s.diag(1,-1,-1,-1);rt=s.sqrt(2)
S={4:s.diag(1,1,-1,-1)/2,5:s.diag(1,-1,1,-1)/2,6:s.diag(1,-1,-1,1)/2,10:s.eye(4)/2}
for a,(mu,nu) in zip((7,8,9,11,12,13),((1,2),(1,3),(2,3),(0,1),(0,2),(0,3))):
    E=s.zeros(4);E[mu,nu]=E[nu,mu]=1/rt;S[a]=g*E
def vf(A,B):return s.trace(A*B)-s.trace(A)*s.trace(B)/2
assert all(vf(S[a],S[b])==(eta[a] if a==b else 0) for a in S for b in S)
comm=lambda A,B:A*B-B*A
def Rapaq(a,p,q):
    """Component (R(e_a,e_q)e_p)^a, i.e. R^a_{p a q}."""
    if a==q:return s.Integer(0)
    if a<4 and p<4 and q<4:return s.Rational(1,4)*(g[p,q]-(g[a,p] if a==q else 0))
    if a>=4 and p<4 and q<4:return -eta[a]*(g*S[a]*S[a])[q,p]/4
    if a<4 and p>=4 and q>=4:return -(S[p]*S[q])[a,a]/4
    if a>=4 and p>=4 and q>=4:return eta[a]*s.trace(comm(S[a],S[p])*comm(S[a],S[q]))/4
    return s.Integer(0)
lhs=s.simplify(2*sum(s.Rational(d[r][a].numerator,d[r][a].denominator)*(Rapaq(a,p,p)-Rapaq(a,p,q)) for r,(p,q) in enumerate(pairs) for a in range(n)))
cross=s.simplify(2*sum(s.Rational(d[r][a].numerator,d[r][a].denominator)*Rapaq(a,p,q) for r,(p,q) in enumerate(pairs) for a in range(n)))
curvature_result={'X':str(X),'Y':str(Y),'Bnorm':str(Bnorm),'double_div_Q':str(rhs),'curvature_K':str(lhs),'cross':str(cross),'defect':str(s.factor(lhs-s.Rational(rhs.numerator,rhs.denominator)))}
assert curvature_result['defect']=='-751/70'
print(curvature_result)

# Optional backend verification: run only serialized by the lead. This rebuilds K2345 metric jet.
if True:
    import sys
    if True:
        from pathlib import Path
        root=Path(__file__).resolve().parents[2]
        path=root/'tests/channel-swings/k2345_curved_bundle_ricci_obstruction_probe.py'
        src=path.read_text();ns={'__file__':str(path),'__name__':'metric_backend'}
        exec(compile(src[:src.index('Ric=ricci()')],str(path),'exec'),ns)
        G=ns['G'];Ga=ns['Ga'];D=ns['D'];e=[s.eye(n)[:,i] for i in range(n)]
        frame=[]
        for a in range(n):
            v=s.zeros(n,1)
            if a<4:v[a]=1
            else:
                E=g*S[a]
                for b,(i,j) in enumerate(( (i,j) for i in range(4) for j in range(i,4))):v[b+4]=E[i,j]
            frame.append(v)
        assert all((frame[a].T*G*frame[b])[0]==(eta[a] if a==b else 0) for a in range(n) for b in range(n))
        Gam=[s.Matrix.hstack(*[Ga[i,j] for j in range(n)]) for i in range(n)]
        cache={}
        def rr(i,j):
            if (i,j) not in cache:cache[i,j]=s.Matrix.hstack(*[D(i,j,k)-D(j,i,k) for k in range(n)])+Gam[i]*Gam[j]-Gam[j]*Gam[i]
            return cache[i,j]
        def cur(X,Y):return sum((X[i]*Y[j]*rr(i,j) for i in range(n) for j in range(n) if X[i] and Y[j]),s.zeros(n))
        for r,(p,q) in enumerate(pairs):
            for a in range(n):
                if d[r][a]:
                    for input_index in (p,q):
                      for b in (p,q):
                        got=s.simplify(eta[a]*(frame[a].T*G*cur(frame[a],frame[b])*frame[input_index])[0])
                        assert got==Rapaq(a,input_index,b),(a,input_index,b,got,Rapaq(a,input_index,b))
        print('PASS actual curvature contraction entries')

betas=s.symbols('b0:7',real=True)
beta=None
K={}
for r,(p,q) in enumerate(pairs):
    beta=betas[r]
    for l,weight in ((p,1+beta),(q,beta)):
        for i in range(n):
            for j in (p,q):
                if d[r][i]:
                    K[l,i,i,j]=weight*eta[i]*d[r][i]
                    K[l,i,j,i]=-weight*eta[i]*d[r][i]
kg=lambda l,i,j,k:K.get((l,i,j,k),s.Integer(0))
P=[[sum(eta[i]*kg(i,i,a,b) for i in range(n)) for b in range(n)] for a in range(n)]
assert not any(s.expand(v) for row in P for v in row)
X=s.expand(sum(F(eta[i]*eta[j]*eta[a]*eta[b],2)*kg(i,j,a,b)*kg(j,i,a,b) for i in range(n) for j in range(n) for a in range(n) for b in range(n)))
Y=s.expand(sum(eta[i]*eta[j]*eta[a]*eta[b]*kg(j,a,i,b)*kg(i,a,j,b) for i in range(n) for j in range(n) for a in range(n) for b in range(n)))
rhs=s.expand(F(4,3)*(Bnorm+Y-2*X))
lhs=s.expand(2*sum(s.Rational(d[r][a].numerator,d[r][a].denominator)*((1+betas[r])*(Rapaq(a,p,p)-Rapaq(a,p,q))-betas[r]*(Rapaq(a,q,p)-Rapaq(a,q,q))) for r,(p,q) in enumerate(pairs) for a in range(n)))
defect=s.factor(lhs-rhs)
Q=s.hessian(defect,betas)/2
z={b:0 for b in betas}
v=s.Matrix([s.diff(defect,b).subs(z) for b in betas])
c=defect.subs(z)
print({'seven_parameter_defect':str(defect),'Q':str(Q),'linear':str(v),'constant':str(c),'rank':Q.rank(),'eigenvalues':str(Q.eigenvals())})

common=s.factor(defect.subs({b:betas[0] for b in betas}))
assert s.expand(common+(280*betas[0]**2+421*betas[0]+3004)/280)==0
assert 421**2-4*280*3004<0
repair={b:0 for b in betas};repair[betas[1]]=-s.Rational(9012,493)
assert defect.subs(repair)==0
assert s.factor(defect.subs({betas[0]:0,betas[2]:-betas[1],betas[3]:0,betas[4]:0,betas[5]:0,betas[6]:0})-(betas[1]**2/3-s.Rational(751,70)))==0


# Actual metric derivative and third-order fixed-second-jet obstruction.
G=ns['G'];Ga=ns['Ga'];Es=ns['Es'];Ug=ns['U']
frame=[]
for a in range(n):
    v=s.zeros(n,1)
    if a<4:v[a]=1
    else:
        E=g*S[a]
        for b,(i,j) in enumerate(((i,j) for i in range(4) for j in range(i,4))):v[b+4]=E[i,j]
    frame.append(v)
Fmat=s.Matrix.hstack(*frame)
assert s.simplify(Fmat.T*G*Fmat)==s.diag(*eta)
RV=s.Matrix(10,10,lambda a,b:-s.Rational(5,4)*s.trace(g*Es[a]*g*Es[b])+s.trace(g*Es[a])*s.trace(g*Es[b])/4)
Ric=s.diag(g/4,RV)
dr=[s.zeros(n) for _ in range(n)]
for c in range(10):
    RVc=s.Matrix(10,10,lambda a,b:-s.Rational(5,4)*s.trace(Ug[c]*Es[a]*g*Es[b]+g*Es[a]*Ug[c]*Es[b])+(s.trace(Ug[c]*Es[a])*s.trace(g*Es[b])+s.trace(g*Es[a])*s.trace(Ug[c]*Es[b]))/4)
    dr[c+4]=s.diag(Es[c]/4,RVc)
Gam=[s.Matrix.hstack(*[Ga[i,j] for j in range(n)]) for i in range(n)]
cov=[dr[l]-Gam[l].T*Ric-Ric*Gam[l] for l in range(n)]
# Known actual geometry control: vertical projectors/Ricci are covariantly parallel.
assert all(cov[l]==s.zeros(n) for l in range(4,n))
C={}
for l in range(n):
    M=s.simplify(-2*Fmat.T*sum((frame[l][a]*cov[a] for a in range(n) if frame[l][a]),s.zeros(n))*Fmat)
    for i in range(n):
        for j in range(n):
            if M[i,j]:C[l,i,j]=M[i,j]
cg=lambda A,l,i,j:A.get((l,i,j),s.Integer(0))
assert C
assert all(s.simplify(sum(eta[i]*cg(C,l,i,i) for i in range(n)))==0 for l in range(n))
assert all(s.simplify(sum(eta[i]*cg(C,i,i,l) for i in range(n)))==0 for l in range(n))
St={}
for l in range(n):
    for i in range(n):
        for j in range(n):
            sym=(cg(C,l,i,j)+cg(C,i,l,j)+cg(C,j,l,i))/3
            v=s.simplify(s.Rational(13,180)*sym+s.Rational(26,363)*(cg(C,l,i,j)-sym))
            if v:St[l,i,j]=v
metric=lambda i,j:eta[i] if i==j else 0
def J(m,T):
    out={}
    for i in range(n):
        for j in range(n):
            for k in range(n):
                v=metric(m,j)*T.get((i,k),0)-metric(m,k)*T.get((i,j),0)-(metric(i,j)*T.get((m,k),0)-metric(i,k)*T.get((m,j),0))/s.Integer(n-1)
                if v:out[i,j,k]=v
    return out
Js={(l,m):J(m,{(i,j):v for (ll,i,j),v in St.items() if ll==l}) for l in range(n) for m in range(n)}
L={}
for l in range(n):
    for m in range(n):
        keys=set(Js[l,m])|set(Js[m,l])
        L[l,m]={key:s.simplify((Js[l,m].get(key,0)+Js[m,l].get(key,0))/2) for key in keys}
        L[l,m]={key:v for key,v in L[l,m].items() if v}
get=lambda A,i,j,k:A.get((i,j,k),s.Integer(0))
for l in range(n):
    for i in range(n):
        for j in range(n):
            assert s.simplify(sum(eta[m]*(get(L[l,m],i,m,j)+get(L[l,m],j,m,i)) for m in range(n))-cg(C,l,i,j))==0
def gram(A,B):return s.simplify(sum(s.Rational(eta[i]*eta[j]*eta[k],2)*v*get(B,i,j,k) for (i,j,k),v in A.items()))
def ps(A,B):
    out={}
    for (i,j,k),a in A.items():
        if j>=k:continue
        for (ii,l,m),b in B.items():
            if ii!=i or l>=m or len({j,k,l,m})!=4:continue
            seq=(j,k,l,m);key=tuple(sorted(seq))
            sign=(-1)**sum(seq[x]>seq[y] for x in range(4) for y in range(x+1,4))
            out[key]=out.get(key,0)+eta[i]*sign*a*b
    return {key:s.simplify(v) for key,v in out.items() if s.simplify(v)}

p,q=pairs[0]
H0={}
for i in range(n):
    for j in (p,q):
        v=eta[i]*d[0][i]
        if v:H0[i,i,j]=v;H0[i,j,i]=-v
sig00={key:s.simplify(6*v) for key,v in ps(L[0,0],H0).items()}
sig11={key:s.simplify(6*v) for key,v in ps(L[1,1],H0).items()}
expected=-s.Rational(167063,2032800)*s.sqrt(2)
assert sig00[(0,1,2,12)]==expected and sig11[(0,1,3,8)]==expected
assert expected!=0
# Normalize two required zero equations: (1+b0)-b0=1 contradicts zero.
assert s.expand((1+betas[0])-betas[0])==1
third_result={'actual_Ricci_derivative_nonzero_components':len(C),'sigma000_slot':'0,1,2,12','sigma111_slot':'0,1,3,8','common_coefficient':str(expected),'witness':'sigma000/c - sigma111/c = 1','scope':'All seven first-jet parameters with the displayed fixed second jet only; arbitrary second-jet kernels remain open.'}

# General 77-dimensional common-null repeated-index subspace, not only seven fixed hooks.
null_basis=[]
for rr,(pp,qq) in enumerate(pairs):
    allowed=[ii for ii in range(n) if ii not in (pp,qq)]
    anchor=allowed[0]
    for ii in allowed[1:]:
        hb={}
        for jj,dd in ((ii,1),(anchor,-1)):
            for kk in (pp,qq):
                hb[jj,jj,kk]=eta[jj]*dd;hb[jj,kk,jj]=-eta[jj]*dd
        null_basis.append(hb)
assert len(null_basis)==77
for hb in null_basis:
    for pp,qq in pairs:
        for mm in range(n):assert get(hb,pp,mm,qq)==0 and get(hb,qq,mm,pp)==0
assert cg(C,2,4,2)==s.Rational(3,4)
xx=s.eye(4)[:,2]
assert s.Rational(3,2)*(xx.T*g*S[4]*xx)[0]==s.Rational(3,4)
null_repair={'dimension':77,'forced_receiver':'D_2,4,2=0','actual_C':'3/4','scope':'second derivatives valued in this common-null subspace only'}
from pathlib import Path
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[2]
dep='explorations/conditional-build/k2375-axial-hook-stationarity-2026-10-31.md'
report={'result_id':'K2378','checks':15,'check_groups':['row and column constraints','all slice hook identities','actual Ricci divergence','196 pairwise Gram zeros','196 polarized sigma zeros','critical kappa signed norm','retained failed old jet','four full second-jet right inverse fixtures','actual curvature entries and double-divergence defect','all common-parameter repairs excluded','seven-parameter polynomial','rational scalar repair','actual differentiated Ricci and full PDE','two-row third-sigma inconsistency for all seven parameters','77-dimensional null-subspace second-jet repair excluded'],'changed_input_controls':['delete null partner fails Gram','nonzero hook sigma fixture detected'],'scope':'Finite second jet only: algebraic constraints through two derivatives, first-order Euler through one derivative. No higher integrability or local solution.','null_subspace_repair':null_repair,'third_constraint':third_result,'curvature':curvature_result,'seven_parameter_defect':str(defect),'scalar_repair':{'b1':'-9012/493','others':'0'},'dependencies':{dep:hashlib.sha256((ROOT/dep).read_bytes()).hexdigest(),'tests/channel-swings/k2345_curved_bundle_ricci_obstruction_probe.py':hashlib.sha256((ROOT/'tests/channel-swings/k2345_curved_bundle_ricci_obstruction_probe.py').read_bytes()).hexdigest()}}
text=json.dumps(report,indent=2,sort_keys=True)+'\n'
if '--write' in sys.argv:(ROOT/'lab/process/k2378-null-hook-jet-compatibility.json').write_text(text)
print(text)
