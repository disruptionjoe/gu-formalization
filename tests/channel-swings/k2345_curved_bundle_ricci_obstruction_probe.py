"""Exact full14 metric two-jet Ricci, conditional Euler and receiver controls."""
import sympy as s,itertools
from pathlib import Path
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];checks={};faults={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def finish(st,details,evidence,deps):
 deps=[f'explorations/conditional-build/{st}-2026-10-30.md',str(Path(__file__).relative_to(R))]+deps
 out=dict(result_id=st.split('-')[0].upper(),checks=len(checks),check_names=list(checks),evidence_kind=evidence,mutation_failed_checks=faults,details=details,dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
 assert faults and all(faults.values())
 p=R/f'lab/process/{st}.json'
 if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 else:assert json.loads(p.read_text())==out
 print(json.dumps({'result':out['result_id'],'checks':len(checks),'faults':len(faults)}))

q=s.Rational;n=14;g=s.diag(1,-1,-1,-1);Es=[]
for i in range(4):
 for j in range(i,4):
  E=s.zeros(4);E[i,j]=E[j,i]=1;Es.append(E)
def pair(A,B):return s.trace(g*A*g*B)-s.trace(g*A)*s.trace(g*B)/2
V=s.Matrix(10,10,lambda a,b:pair(Es[a],Es[b]));G=s.diag(g,V);Gi=G.inv()
dg=[s.zeros(n) for _ in range(n)];ddg={(a,b):s.zeros(n) for a in range(4,n) for b in range(4,n)}
U=[-g*E*g for E in Es]
for a in range(10):
 dV=s.Matrix(10,10,lambda b,c:s.trace(U[a]*Es[b]*g*Es[c]+g*Es[b]*U[a]*Es[c])-(s.trace(U[a]*Es[b])*s.trace(g*Es[c])+s.trace(g*Es[b])*s.trace(U[a]*Es[c]))/2)
 dg[a+4]=s.diag(Es[a],dV)
for a in range(10):
 for b in range(10):
  W=g*Es[a]*g*Es[b]*g+g*Es[b]*g*Es[a]*g
  def second(c,d):
   A=Es[c];B=Es[d]
   return s.trace(W*A*g*B+U[a]*A*U[b]*B+U[b]*A*U[a]*B+g*A*W*B)-(s.trace(W*A)*s.trace(g*B)+s.trace(U[a]*A)*s.trace(U[b]*B)+s.trace(U[b]*A)*s.trace(U[a]*B)+s.trace(g*A)*s.trace(W*B))/2
  ddg[(a+4,b+4)]=s.diag(s.zeros(4),s.Matrix(10,10,second))
zero=s.zeros(n)
def dd(a,b):return ddg.get((a,b),zero)
lo={};Ga={}
for b in range(n):
 for c in range(n):
  lo[b,c]=s.Matrix([dg[b][d,c]+dg[c][d,b]-dg[d][b,c] for d in range(n)])/2
  Ga[b,c]=Gi*lo[b,c]
dGa={}
for k in range(4,n):
 dGi=-Gi*dg[k]*Gi
 for b in range(n):
  for c in range(n):
   dGa[k,b,c]=dGi*lo[b,c]+Gi*s.Matrix([dd(k,b)[d,c]+dd(k,c)[d,b]-dd(k,d)[b,c] for d in range(n)])/2
zv=s.zeros(n,1)
def D(k,b,c):return dGa.get((k,b,c),zv)
def ricci(drop_derivatives=False,drop_mixed=False):
 def C(a,b,c):return 0 if drop_mixed and ((b<4)!=(c<4) or (a<4)!=(b<4)) else Ga[b,c][a]
 return s.Matrix(n,n,lambda b,d:sum((0 if drop_derivatives else D(a,d,b)[a]-D(d,a,b)[a])+sum(C(a,a,m)*C(m,d,b)-C(a,d,m)*C(m,a,b) for m in range(n)) for a in range(n)))
Ric=ricci();RV=s.Matrix(10,10,lambda a,b:-q(5,4)*s.trace(g*Es[a]*g*Es[b])+s.trace(g*Es[a])*s.trace(g*Es[b])/4);expected=s.diag(g/4,RV)
check('all196_full_Ricci_entries',Ric==expected);check('Ricci_symmetric',Ric==Ric.T)
sc=s.trace(Gi*Ric);check('full_scalar',sc==-10);check('mixed_Ricci_zero',Ric[:4,4:]==s.zeros(4,10))
def curvature(i,j,k,l):return sum(G[i,a]*(D(k,l,j)[a]-D(l,k,j)[a]+sum(Ga[k,m][a]*Ga[l,j][m]-Ga[l,m][a]*Ga[k,j][m] for m in range(n))) for a in range(n))
check('horizontal_convention_0101',curvature(0,1,0,1)==-q(1,4));check('horizontal_convention_1212',curvature(1,2,1,2)==q(1,4))
raiseR=Gi*Ric;check('raised_Ricci_eigenvalues',raiseR.eigenvals()=={q(1,4):5,-q(5,4):9})
check('vertical_inertia',sum(m for ev,m in V.eigenvals().items() if ev>0)==6 and sum(m for ev,m in V.eigenvals().items() if ev<0)==4)
Ein=raiseR-sc*s.eye(n)/2;check('Einstein_eigenvalues',Ein.eigenvals()=={q(21,4):5,q(15,4):9})
check('cosmological_shift_obstruction',q(21,4)-q(15,4)==q(3,2));check('selected_radial_Euler',12*sc==-120)
lam,t=s.symbols('lam t',nonzero=True);H=s.diag(-59,29,29,29)*s.exp(lam*t)/91
observed=s.diff(H[0,0],t,2)-s.diff(s.trace(g*H),t,2)
check('actual_observed_scalar',s.simplify(observed-q(87,91)*lam**2*s.exp(lam*t))==0)
# Universal pullback inverse identity tested on nonlinear vertical translation flow F(x,y)=(x,y+eps*x*x).
x,eps=s.symbols('x eps');y=s.symbols('y',positive=True)
metric=s.diag(y,1/y**2);J=s.Matrix([[1,0],[2*eps*x,1]]);pulled=J.T*metric.subs(y,y+eps*x*x)*J
section=1-eps*x*x;vel=s.Matrix([1,s.diff(section,x)]);observed_full=s.simplify((vel.T*pulled.subs(y,section)*vel)[0])
check('simultaneous_receiver_exact',observed_full==1)
frozen=s.Matrix([1,0]);wrong=s.simplify((frozen.T*pulled.subs(y,1)*frozen)[0])
check('frozen_receiver_changes',wrong!=1)
faults['omit_vertical_connection_derivatives']=['all196_full_Ricci_entries'] if ricci(True)!=expected else []
faults['omit_mixed_Christoffels']=['all196_full_Ricci_entries'] if ricci(drop_mixed=True)!=expected else []
faults['horizontal_Ricci_trace_only']=['full_scalar'] if s.trace(g*Ric[:4,:4])!=sc else []
faults['freeze_receiver_during_transport']=['simultaneous_receiver_exact'] if wrong!=1 else []
finish('k2345-curved-bundle-ricci-obstruction',{'scalar':str(sc),'Ricci_eigenvalues':{'1/4':5,'-5/4':9},'metric_inertia':[7,7],'selected_conditional_radial_Euler':'-120','observed_scalar_coefficient':'87/91'},'exact rational full metric two-jet and196 Ricci entries; covariance and analytic tensor proofs in note',['explorations/conditional-build/k2342-holonomic-metric-lift-2026-10-30.md','explorations/conditional-build/selected-action-curvature-graph-six-versus-four-2026-08-06.md'])
