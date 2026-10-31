"""Exact contact, graph second-jet and declared four-dimensional block curvature."""
import sympy as s
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

q=s.Rational
g=s.diag(1,-1,-1,-1);Es=[]
for i in range(4):
 for j in range(i,4):
  E=s.zeros(4);E[i,j]=E[j,i]=1;Es.append(E)
def pairing(A,B):return s.trace(g*A*g*B)-s.trace(g*A)*s.trace(g*B)/2
GV=s.Matrix(10,10,lambda a,b:pairing(Es[a],Es[b]));Gi=GV.inv()
check('dewitt_nondegenerate',GV.det()!=0)
# Full inverse tensor and curvature from actual Christoffel product.
invcheck=[];rc=[]
for i in range(4):
 for j in range(4):
  for k in range(4):
   for l in range(4):
    def K(i,j,k,l):return sum(Gi[a,b]*Es[a][i,j]*Es[b][k,l] for a in range(10) for b in range(10))
    invcheck.append(K(i,j,k,l)==(g[i,k]*g[j,l]+g[i,l]*g[j,k]-g[i,j]*g[k,l])/2)
    Rijkl=-(K(i,k,l,j)-K(i,l,k,j))/4
    rc.append(Rijkl==(g[i,k]*g[j,l]-g[i,l]*g[j,k])/4)
check('all_256_inverse_components',all(invcheck));check('all_256_curvature_components',all(rc))
A=s.diag(-59,29,29,29)/91;avec=s.Matrix([A[i,j] for i in range(4) for j in range(i,4)])
check('actual_kernel_dewitt_norm',pairing(A,A)==-q(4654,8281))
check('actual_kernel_coordinate_norm',(avec.T*GV*avec)[0]==-q(4654,8281))
lam=s.symbols('lam',nonzero=True);t,eps=s.symbols('t eps',real=True)
check('moving_cross_nonzero',GV*lam*avec!=s.zeros(10,1))
# Independently differentiate literal graph pullback along diagonal K2316 mode.
gs=g+eps*A*s.exp(lam*t);igs=gs.inv();vel=eps*lam*A*s.exp(lam*t)
gamma00=gs[0,0]+s.trace(igs*vel*igs*vel)-s.trace(igs*vel)**2/2
second=s.simplify(s.diff(gamma00,eps,2).subs(eps,0))
check('literal_graph_second_jet',s.simplify(second+q(9308,8281)*lam**2*s.exp(2*lam*t))==0)
# Independent fibre derivative along A using inverse differentiation.
K=-g*A*g
dGV=s.Matrix(10,10,lambda a,b:s.trace(K*Es[a]*g*Es[b]+g*Es[a]*K*Es[b])-(s.trace(K*Es[a])*s.trace(g*Es[b])+s.trace(g*Es[a])*s.trace(K*Es[b]))/2)
check('moving_fibre_derivative_nonzero',dGV!=s.zeros(10))
# Full tensor reconstruction using an independent directional derivative of G(y).
ysmetric=g+eps*A;ysinv=ysmetric.inv()
fib=s.Matrix(10,10,lambda a,b:s.trace(ysinv*Es[a]*ysinv*Es[b])-s.trace(ysinv*Es[a])*s.trace(ysinv*Es[b])/2)
directd=fib.diff(eps).subs(eps,0)
check('fibre_derivative_direct_replay',s.simplify(directd-dGV)==s.zeros(10))
Jac=s.zeros(14);N=s.zeros(10);N[0,0]=1;N[1,2]=2;N[3,1]=-1
for a in range(10):
 Jac[4+a,0]=lam*avec[a]
 for b in range(10):Jac[4+a,4+b]=N[a,b]
G=s.diag(g,GV);coord=s.diag(A,directd)+G*Jac+Jac.T*G
formula=s.diag(A,dGV+N.T*GV+GV*N)
for a in range(10):formula[0,4+a]=formula[4+a,0]=(GV*lam*avec)[a]
def tensor_acceptance(candidate):return s.simplify(candidate-coord)==s.zeros(14)
check('complete_moving_tensor',tensor_acceptance(formula))
withoutmixed=formula.copy()
for a in range(10):withoutmixed[0,4+a]=withoutmixed[4+a,0]=0
withoutfiber=formula-s.diag(s.zeros(4),dGV)
withoutnormal=formula-s.diag(s.zeros(4),N.T*GV+GV*N)
# A genuinely normal-dependent contact field; first prolongation in two base/fibre coordinates.
x0,x1,y0,y1=s.symbols('x0 x1 y0 y1');ps=s.symbols('p00 p01 p10 p11');xs=[x0,x1];ys=[y0,y1];p=s.Matrix(2,2,ps);u=[x0*y0+y1**2,x1*y1+x0*y0*y1]
coords=xs+ys+list(ps)
def total(f,mu):return s.diff(f,xs[mu])+sum(p[b,mu]*s.diff(f,ys[b]) for b in range(2))
def lift(omit=False):return [0,0]+u+[s.diff(u[a],xs[mu]) if omit else total(u[a],mu) for a in range(2) for mu in range(2)]
theta=[]
for a in range(2):form=[-p[a,0],-p[a,1],int(a==0),int(a==1),0,0,0,0];theta.append(form)
def lie(V,form):return [s.expand(sum(V[k]*s.diff(form[i],coords[k])+form[k]*s.diff(V[k],coords[i]) for k in range(8))) for i in range(8)]
expected=[[s.expand(sum(s.diff(u[a],ys[b])*theta[b][i] for b in range(2))) for i in range(8)] for a in range(2)]
check('normal_dependent_contact_ideal',all(lie(lift(),theta[a])==expected[a] for a in range(2)))
# Actual holonomic polynomial section versus total derivative formula through second order.
ysection=[x0**2+x1,x0*x1+1];subs=dict(zip(ys,ysection));subs.update({p[b,mu]:s.diff(ysection[b],xs[mu]) for b in range(2) for mu in range(2)})
errs=[]
for a in range(2):
 for mu in range(2):
  for nu in range(2):
   expr=s.diff(u[a],xs[mu],xs[nu])+sum(p[b,nu]*s.diff(u[a],xs[mu],ys[b])+p[b,mu]*s.diff(u[a],xs[nu],ys[b])+s.diff(ysection[b],xs[mu],xs[nu])*s.diff(u[a],ys[b]) for b in range(2))+sum(p[b,mu]*p[c,nu]*s.diff(u[a],ys[b],ys[c]) for b in range(2) for c in range(2))
   errs.append(s.expand(expr.subs(subs,simultaneous=True)-s.diff(u[a].subs(dict(zip(ys,ysection)),simultaneous=True),xs[mu],xs[nu]))==0)
check('second_prolongation_holonomic',all(errs))
# Chain rule, with nonstationary versus stationary exact consumers.
z,alpha,beta=s.symbols('z alpha beta');Phi=eps*alpha+eps**2*beta/2
for name,F in [('nonstationary',z+z*z/2),('stationary',z*z/2)]:
 direct=s.diff(F.subs(z,Phi),eps,2).subs(eps,0);chain=s.diff(F,z,2).subs(z,0)*alpha**2+s.diff(F,z).subs(z,0)*beta
 check(name+'_full_chain_rule',s.expand(direct-chain)==0)
check('stationarity_controls_embedding_term',s.diff((z+z*z/2),z).subs(z,0)==1 and s.diff(z*z/2,z).subs(z,0)==0)
faults['omit_normal_total_derivative']=['normal_dependent_contact_ideal'] if any(lie(lift(True),theta[a])!=expected[a] for a in range(2)) else []
faults['omit_graph_slope_term']=['literal_graph_second_jet'] if s.diff(gs[0,0],eps,2)==0 and second!=0 else []
faults['omit_mixed_metric_terms']=['complete_moving_tensor'] if not tensor_acceptance(withoutmixed) else []
faults['omit_fibre_derivative']=['complete_moving_tensor'] if not tensor_acceptance(withoutfiber) else []
faults['omit_vertical_jacobian']=['complete_moving_tensor'] if not tensor_acceptance(withoutnormal) else []
wrong=s.trace(g*A*g*A) # omit trace reversal on actual kernel
faults['omit_trace_reversal']=['actual_kernel_dewitt_norm'] if wrong!=pairing(A,A) else []
faults['drop_embedding_term_off_shell']=['nonstationary_full_chain_rule'] if s.diff((z+z*z/2).subs(z,Phi),eps,2).subs(eps,0)!=alpha**2 else []
finish('k2342-holonomic-metric-lift',{'dewitt_kernel_norm':str(pairing(A,A)),'gamma_second_00':str(second),'curvature_components_checked':256,'R0101':'-1/4','R1212':'1/4'},'exact symbolic/rational geometric controls; universal contact/existence/chain-rule statements proved in note',['explorations/conditional-build/k2316-induced-metric-coupled-pencil-2026-10-30.md','explorations/conditional-build/k2339-induced-normal-localization-2026-10-30.md','explorations/geometry-curvature-emergence/ii-s-coordinate-formula-2026-06-23.md'])
