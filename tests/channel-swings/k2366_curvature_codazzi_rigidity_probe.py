"""Exact actual-metric curvature hypotheses for the analytic Codazzi rigidity proof."""
from pathlib import Path
import sympy as s
import json,hashlib,sys,itertools
R=Path(__file__).resolve().parents[2];st='k2366-curvature-codazzi-rigidity';checks={};faults={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
p=R/'tests/channel-swings/k2345_curved_bundle_ricci_obstruction_probe.py';src=p.read_text();ns={'__file__':str(p),'__name__':'metric_backend'};exec(compile(src[:src.index('Ric=ricci()')],str(p),'exec'),ns)
g,G,Gi,Es,Ga,D=[ns[k] for k in ['g','G','Gi','Es','Ga','D']];n=14;q=s.Rational;zero=s.zeros(n);e=[s.eye(n)[:,i] for i in range(n)];Gam=[s.Matrix.hstack(*[Ga[i,j] for j in range(n)]) for i in range(n)]
rm={}
for i in range(n):
 for j in range(i+1,n):
  rm[i,j]=s.Matrix.hstack(*[D(i,j,k)-D(j,i,k) for k in range(n)])+Gam[i]*Gam[j]-Gam[j]*Gam[i]
def rr(i,j):return zero if i==j else rm[i,j] if i<j else -rm[j,i]
def cur(X,Y):return sum((X[i]*Y[j]*rr(i,j) for i in range(n) for j in range(n) if X[i] and Y[j]),s.zeros(n))
def vert(U):
 v=s.zeros(n,1)
 for a,(i,j) in enumerate(( (i,j) for i in range(4) for j in range(i,4))):v[a+4]=U[i,j]
 return v
def hor(x):return x.col_join(s.zeros(10,1))
t=vert(g/2);check('trace_norm', (t.T*G*t)[0]==-1)
Us=[vert(E) for E in Es];Ss=[g*E for E in Es]
# Reconstruct Ricci by a separate contraction of full curvature matrices.
Ric=s.Matrix(n,n,lambda b,d:sum(rr(a,d)[a,b] for a in range(n)))
RV=s.Matrix(10,10,lambda a,b:-q(5,4)*s.trace(g*Es[a]*g*Es[b])+s.trace(g*Es[a])*s.trace(g*Es[b])/4)
check('all_Ricci_entries',Ric==s.diag(g/4,RV));check('Ricci_spectrum',(Gi*Ric).eigenvals()=={q(1,4):5,-q(5,4):9})
check('curvature_metric_skew',all(M.T*G+G*M==zero for M in rm.values()))
for a,(U,S) in enumerate(zip(Us,Ss)):
 check(f'vertical_trace_operator_{a}',cur(U,t)==zero)
 for mu in range(4):
  X=e[mu];x=X[:4,:]
  check(f'mixed_trace_{mu}_{a}',cur(X,U)*t==hor(-S*x/8))
  check(f'trace_mixed_{mu}_{a}',cur(t,X)*U==hor(S*x/8))
  for b,(V,T) in enumerate(zip(Us,Ss)):
   check(f'mixed_vertical_{mu}_{a}_{b}',cur(X,U)*V==hor(-T*S*x/4))
   check(f'vertical_commutator_{mu}_{a}_{b}',cur(U,V)*X==hor(-(S*T-T*S)*x/4))
# The only Ricci blocks with equal eigenvalues are H plus trace. Its cross with traceless is forbidden.
PH=s.diag(s.eye(4),s.zeros(10));Pt=-(t*t.T*G);Ps=s.eye(n)-PH-Pt
check('projector_splitting',Pt*Pt==Pt and Ps*Ps==Ps and PH+Pt+Ps==s.eye(n));check('Ricci_projectors',Gi*Ric==q(1,4)*(PH+Pt)-q(5,4)*Ps)
S0=s.diag(3,1,-1,-3);boosts=[]
for j in range(1,4):
 T=s.zeros(4);T[0,j]=1;T[j,0]=-1
 check(f'traceless_selfadjoint_{j}',s.trace(T)==0 and T.T*g==g*T)
 boosts.append(S0*T-T*S0)
check('boost_common_kernel',s.Matrix.vstack(*boosts).rank()==4)
S1=s.diag(1,1,-1,-1);check('invertible_traceless_control',s.trace(S1)==0 and S1.det()==1)
# Actual curvature compatibility kills a mixed trace-horizontal test A and an anisotropic H block.
def compat(A,X,Y,Z):return cur(X,Y)*A*Z+cur(Y,Z)*A*X+cur(Z,X)*A*Y
U=vert(g*S1);X=e[0];A=e[0]*(t.T*G)+t*(e[0].T*G)
check('mixed_A_selfadjoint',A.T*G==G*A)
check('mixed_A_rejected',compat(A,X,U,t)!=s.zeros(n,1))
AH=e[0]*e[0].T;check('anisotropic_horizontal_rejected',any(compat(AH,X,vert(g*S0),vert(g*T))!=s.zeros(n,1) for T in [s.Matrix([[0,1,0,0],[-1,0,0,0],[0,0,0,0],[0,0,0,0]])]))
check('scalar_compatibility',all(compat(s.eye(n),e[i],e[j],e[k])==s.zeros(n,1) for i,j,k in [(0,4,5),(0,1,4),(4,5,7),(1,6,13)]))
u,v=s.symbols('u v');H=s.hessian(u**3+u*v*v,(u,v));check('flat_nonconstant_Hessian',s.diff(H,u)!=s.zeros(2) and all(s.diff(H[i,k],[u,v][j])==s.diff(H[i,j],[u,v][k]) for i,j,k in itertools.product(range(2),repeat=3)))
check('reused_product_witness_nonscalarity',s.diag(*([1]*7+[-1]*7))!=s.eye(14))
faults['erase_mixed_curvature']=['mixed_trace_0_0'] if hor(-Ss[0]*s.eye(4)[:,0]/8)!=s.zeros(n,1) else []
faults['reverse_mixed_curvature_sign']=['mixed_trace_0_0'] if cur(e[0],Us[0])*t!=hor(Ss[0]*s.eye(4)[:,0]/8) else []
faults['single_boost_instead_of_three']=['boost_common_kernel'] if boosts[0].rank()<4 else []
faults['all_geometry_rigidity']=['flat_nonconstant_Hessian'] if s.diff(H,u)!=s.zeros(2) else []
assert all(faults.values())
deps=[str(p.relative_to(R)),f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R)),'lab/process/k2363-variable-projector-stationarity.json','lab/process/k2357-curved-native-stationarity.json','lab/process/k2360-anisotropic-native-stationarity.json']
out=dict(result_id='K2366',checks=len(checks),check_names=list(checks),altered_input_and_algebraic_scope_controls=faults,evidence_kind='exact rational actual metric curvature identities and linear algebra; universal rigidity proof in note; parallel-product premise reused from K2360',details=dict(curvature_matrices=len(rm),metric_dimension=14,symmetric_coordinates=105,conclusion='all smooth self-adjoint Codazzi fields constant scalar; no selected symmetric grade-one translation stationary field',scope_escape='nonsymmetric or mixed grades; changed metric; independent geometry/domain equations open'),dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
p=R/f'lab/process/{st}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print('PASS',len(checks),len(faults));print(json.dumps(out['details']))
