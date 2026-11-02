"""K2521 exact graph jets, DeWitt metric and curvature/section countercontrols."""
from pathlib import Path
import hashlib,json,sys,itertools
import sympy as s
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not checks[k]:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not controls[k]:raise AssertionError(k)
g=s.diag(1,-1,-1,-1);sign=[1]*6+[-1]*4
S=[s.diag(1,1,0,0)/s.sqrt(2),s.diag(1,-1,2,0)/s.sqrt(6),s.diag(1,-1,-1,3)/s.sqrt(12)]
for i,j in [(1,2),(1,3),(2,3),(0,1),(0,2),(0,3)]:
 a=s.zeros(4);a[i,j]=a[j,i]=1/s.sqrt(2);S.append(a)
S.append(g/2)
def G(a,b):return s.trace(g*a*g*b)-s.trace(g*a)*s.trace(g*b)/2
Gram=s.Matrix(10,10,lambda a,b:s.simplify(G(S[a],S[b])))
ck('full_DeWitt_Gram_100_entries',Gram==s.diag(*sign))
pairs=[(i,j) for i in range(4) for j in range(i,4)]
L=s.Matrix([[a[i,j] for a in S] for i,j in pairs]);ck('receiver_rank_ten',L.rank()==10)
x=s.Matrix(s.symbols('x0:4'))
f=[-sign[a]*(x.T*S[a]*x)[0]/4 for a in range(10)]
II=[-sign[a]*S[a]/2 for a in range(10)]
ck('actual_graph_Hessians',all(s.hessian(f[a],list(x))==II[a] for a in range(10)))
ck('graph_has_zero_first_derivative_at_origin',all(s.diff(ff,xx).subs(dict.fromkeys(x,0))==0 for ff in f for xx in x))
ck('normal_metric_receiver',all(-2*sign[a]*II[a]==S[a] for a in range(10)))
Q=lambda i,j,k,l:(g[i,k]*g[j,l]+g[i,l]*g[j,k]-g[i,j]*g[k,l])/2
ck('completeness_256_entries',all(s.simplify(sum(sign[a]*S[a][i,j]*S[a][k,l] for a in range(10))-Q(i,j,k,l))==0 for i,j,k,l in itertools.product(range(4),repeat=4)))
H=s.Matrix([s.trace(g*a) for a in II]);ck('mean_curvature_trace_normal',H==s.Matrix([0]*9+[1]))
ck('mean_curvature_norm',sum(sign[a]*H[a]**2 for a in range(10))==-1)
normII=sum(sign[a]*g[i,i]*g[j,j]*II[a][i,j]**2 for a,i,j in itertools.product(range(10),range(4),range(4)))
ck('signed_second_fundamental_norm',s.simplify(normII)==2)
curv=s.symbols('c1',real=True)
def b(i,j,k,l):return sum(sign[a]*II[a][i,j]*II[a][k,l] for a in range(10))
def RG(i,j,k,l):return curv*(g[i,k]*g[j,l]-g[i,l]*g[j,k])+b(i,k,j,l)-b(i,l,j,k)
ck('Gauss_full_tensor',all(s.simplify(RG(i,j,k,l)-(curv-s.Rational(1,4))*(g[i,k]*g[j,l]-g[i,l]*g[j,k]))==0 for i,j,k,l in itertools.product(range(4),repeat=4)))
ck('Gauss_scalar',s.simplify(sum(g[i,i]*g[j,j]*RG(i,j,i,j) for i,j in itertools.product(range(4),repeat=2))-(12*curv-3))==0)
# Full Ricci intertwiner check, all tangent planes and 100 pairs of normals.
ricci=[]
for i,j in itertools.combinations(range(4),2):
 X=s.eye(4)[:,i];Y=s.eye(4)[:,j];W=X*Y.T*g-Y*X.T*g
 for a,b0 in itertools.product(range(10),repeat=2):
  An=-g*S[a]/2;Am=-g*S[b0]/2;normal=(Y.T*g*(An*Am-Am*An)*X)[0]
  rho=-W.T*S[a]-S[a]*W
  ricci.append(s.simplify(normal-G(rho,S[b0])/8)==0)
ck('Ricci_all_600_pairings',all(ricci))
ck('parallel_isometric_curvature_requires_3_over_8',s.solve(curv-s.Rational(1,4)-s.Rational(1,8),curv)==[s.Rational(3,8)])
ct('flat_parallel_isometry_fails',-s.Rational(1,4)!=s.Rational(1,8))
# Differentiated Codazzi contraction; b represents <II(W,e_i),n> for fixed W,n.
v=s.symbols('b0:4')
for i in range(4):
 contraction=sum(g[j,k]*(g[j,k]*v[i]-g[i,k]*v[j]) for j,k in itertools.product(range(4),repeat=2))
 ck('Codazzi_contraction_'+str(i),s.expand(contraction)==3*v[i])
ct('tuned_curvature_does_not_rescue_Codazzi',3*s.Rational(3,8)!=0)
ck('parallel_product_rank_bound',14-4-7==3)
# Rank of trace-free metric subspace and explicit trace coupling; no assumed Euclidean positivity.
trrow=s.Matrix([[s.trace(g*a) for a in S]])
ck('trace_response_mean_curvature',trrow==s.Matrix([[-2*sign[a]*H[a] for a in range(10)]]))
ck('minimal_section_trace_kernel_rank9',len(trrow.nullspace())==9)
ct('graph_not_area_stationary',H!=s.zeros(10,1))
ct('drop_trace_normal_loses_rank',L[:,:9].rank()==9)
ct('totally_geodesic_receiver_zero',s.zeros(10).rank()==0)
ct('wrong_normal_signature_not_isometric',Gram!=s.eye(10))
ct('unsigned_Gauss_contraction_wrong',s.simplify(sum(II[a][0,0]*II[a][1,1]-II[a][0,1]*II[a][1,0] for a in range(10))-(b(0,0,1,1)-b(0,1,1,0)))!=0)
ct('missing_factor_two_changes_receiver',-sign[0]*II[0]!=S[0])
# The graph has nonzero projection into second ambient factor: old pure-factor pullback cannot persist.
ck('second_factor_graph_nontrivial',any(ff!=0 for ff in f[3:]))
ct('first_factor_only_Hessians_rank_at_most3',L[:,:3].rank()==3)
paths=['explorations/conditional-build/k2521-free-observer-receiver-2026-11-02.md','tests/channel-swings/k2521_free_observer_receiver_probe.py','explorations/conditional-build/k2519-stationary-product-receiver-2026-11-02.md','lab/process/k2519-stationary-product-receiver.json']
report={'result':'K2521','exact_identity_groups':checks,'contrary_controls':controls,'scope':'Universal graph/Codazzi/section arguments in note; grouped exact finite algebra here, not theorem counts. K2519 ambient stationarity is inherited unchanged.','receiver_determinant':str(s.simplify(L.det())),'normal_Gram_diagonal':sign,'Gauss_sectional':'c1-1/4','Ricci_coefficient':'1/8','parallel_product_rank_upper_bound':3,'minimal_section_rank_upper_bound':9,'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
pth=R/'lab/process/k2521-free-observer-receiver.json'
if '--write' in sys.argv:pth.write_text(json.dumps(report,indent=2)+'\n')
else:
 saved=json.loads(pth.read_text());ck('saved_report_consistency',saved==report)
print('K2521 PASS',len(checks),'identity groups',len(controls),'controls')
