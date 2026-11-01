"""Exact minimal supported/full-family coordinates and physically scoped error controls."""
from pathlib import Path
from itertools import product,combinations
import ast,json,hashlib,sys
import sympy as s
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[2];Q=s.Rational;checks={};controls={}
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);pa=[I,X,Y,Z]
phi=s.Matrix([1,0,0,1])/s.sqrt(2);Phi=phi*phi.H
basis=[s.kronecker_product(a,b) for a,b in product(pa,repeat=2)]
def ck(k,b):
 checks[k]=bool(b)
 if not b:raise AssertionError(k)
def ctrl(k,b):
 controls[k]=bool(b)
 if not b:raise AssertionError(k)
def simp(M):return M.applyfunc(s.simplify)
def ptr(M):return s.Matrix(2,2,lambda i,j:sum(M[2*i+k,2*j+k] for k in range(2)))
def choi(fn):return simp(sum((s.kronecker_product(s.eye(2)[:,i]*s.eye(2)[j,:],fn(s.eye(2)[:,i]*s.eye(2)[j,:])) for i,j in product(range(2),repeat=2)),s.zeros(4))/2)
def psd(M):return M==M.H and all(s.simplify(M.extract(ix,ix).det())>=0 for k in range(1,M.rows+1) for ix in combinations(range(M.rows),k))
def dist(M):return s.simplify(sum(abs(v)*m for v,m in M.eigenvals().items())/2)
def coeff(M):return s.Matrix([s.simplify(s.trace(B*M)) for B in basis])
def unpack(v):return simp(sum((v[i]*basis[i]/4 for i in range(16)),s.zeros(4)))
def law_data():
 p=ROOT/'tests/channel-swings/k2419_positive_visibility_dual_probe.py';env={'s':s,'Q':Q}
 for node in ast.parse(p.read_text()).body:
  if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ['means','weights','norms'] for t in node.targets):exec(compile(ast.Module(body=[node],type_ignores=[]),str(p),'exec'),env)
 return env['means'],env['weights'],env['norms']
def instrument(mean,w,n):
 axis=mean/n
 def block(op,z):
  rr=s.Matrix([s.trace(op*X),s.trace(op*Z)])
  return simp(sum((prob*(s.trace(op)+z*nv.dot(rr))/2*(I+(nv[0]*X+nv[1]*Z)/2)/2 for prob,nv in [((1+n)/2,axis),((1-n)/2,-axis)]),s.zeros(2)))
 return [(1-w)*Phi,w*choi(lambda op:block(op,1)),w*choi(lambda op:block(op,-1))]
idx=[4*a+b for a in range(4) for b in range(1,4)]
def data29(B):return s.Matrix([s.simplify(s.trace(B[0])),*coeff(B[1]),*[coeff(B[2])[j] for j in idx]])
def rec29(v,tangent=False):
 g=v[0];x=s.Matrix(v[1:17]);yy=iter(v[17:]);z=s.Matrix([((0 if tangent else 1)-g)*int(a==0)-x[4*a] if b==0 else next(yy) for a,b in product(range(4),repeat=2)])
 return [g*Phi,unpack(x),unpack(z)]
def data44(B):return s.Matrix([*coeff(B[0]),*coeff(B[1]),*[coeff(B[2])[j] for j in idx]])
def rec44(v,tangent=False):
 g=s.Matrix(v[:16]);x=s.Matrix(v[16:32]);yy=iter(v[32:]);z=s.Matrix([int(a==0 and not tangent)-g[4*a]-x[4*a] if b==0 else next(yy) for a,b in product(range(4),repeat=2)])
 return [unpack(g),unpack(x),unpack(z)]
for dim,recon,observe in [(29,rec29,data29),(44,rec44,data44)]:
 cols=[]
 for k in range(dim):
  v=s.eye(dim)[:,k];B=recon(v,True);ck(f'{dim}_deletion_tangent_{k}',observe(B)==v and sum((ptr(x) for x in B),s.zeros(2))==s.zeros(2));cols.append(s.Matrix.vstack(*[x.reshape(16,1) for x in B]))
 ck(f'{dim}_tangent_full_column_rank',s.Matrix.hstack(*cols).rank()==dim)
# Independent original carrier constraint matrices, not just inverse coordinates.
for dim,observer in [(33,data29),(48,data44)]:
 carrier=[]
 if dim==33:carrier.append([Phi,s.zeros(4),s.zeros(4)])
 for z in ([1,2] if dim==33 else [0,1,2]):
  for H in basis:
   B=[s.zeros(4),s.zeros(4),s.zeros(4)];B[z]=H;carrier.append(B)
 A=s.Matrix.hstack(*[sum((ptr(x) for x in B),s.zeros(2)).reshape(4,1) for B in carrier]);M=s.Matrix.hstack(*[observer(B) for B in carrier])
 ck(f'carrier_{dim}_TP_rank4',A.rank()==4)
 ck(f'carrier_{dim}_augmented_injective',A.col_join(M).rank()==dim)
# Generic polynomial identities underlying the stated conditioning constants.
for dim,recon in [(29,rec29),(44,rec44)]:
 v=s.Matrix(s.symbols('e0:'+str(dim),real=True));B=recon(v,True)
 if dim==29:
  dg=v[0];dx=v[1:17];dy=v[17:];pred=[dg*dg,sum(x*x for x in dx)/4,(sum(x*x for x in dy)+sum((dx[4*a]+dg*int(a==0))**2 for a in range(4)))/4]
 else:
  dg=v[:16];dx=v[16:32];dy=v[32:];pred=[sum(x*x for x in dg)/4,sum(x*x for x in dx)/4,(sum(x*x for x in dy)+sum((dg[4*a]+dx[4*a])**2 for a in range(4)))/4]
 ck(f'generic_{dim}_Frobenius_identity',all(s.expand(s.trace(H*H)-target)==0 for H,target in zip(B,pred)))
means,weights,norms=law_data();fixtures=[]
for k,(mean,w,n) in enumerate(zip(means,weights,norms)):
 B=instrument(mean,w,n);ck(f'original_CP_TP_{k}',all(psd(x) for x in B) and sum((ptr(x) for x in B),s.zeros(2))==I/2)
 ck(f'original_support_{k}',[x.rank() for x in B]==[1,4,4]);ck(f'original29_inverse_{k}',rec29(data29(B))==B);ck(f'original44_inverse_{k}',rec44(data44(B))==B)
 phimin=s.Matrix([1,0,0,-1])/s.sqrt(2);psi=Q(3,5)*phi+s.I*Q(4,5)*phimin;C=[(1-w)*psi*psi.H,B[1],B[2]];p=s.simplify(s.trace((s.eye(4)-Phi)*C[0]));dd=dist(simp(C[0]-B[0]));g=1-w
 ck(f'coherent_leak_CP_TP_{k}',all(psd(simp(x)) for x in C) and simp(sum((ptr(x) for x in C),s.zeros(2)))==I/2)
 ctrl(f'29_misses_coherent_leak_{k}',data29(C)==data29(B) and dd>0)
 ck(f'sharp_sqrt_leak_{k}',dd**2==g*p and p==g*Q(16,25));ck(f'leak_Pauli_formula_{k}',s.simplify((3*g-coeff(C[0])[5]+coeff(C[0])[10]-coeff(C[0])[15])/4-p)==0)
 ctrl(f'full44_detects_leak_{k}',data44(C)!=data44(B));fixtures.append({'law':k+1,'good_weight':str(g),'coherent_leak':str(p),'actual_distance':str(dd),'moment29':list(map(str,data29(B)))})
B=instrument(means[0],weights[0],norms[0]);eps=Q(1,100000);C=[B[0],B[1],B[2]+eps*s.kronecker_product(Z,I)];ck('nonTP_state_physical',all(psd(x) for x in C) and sum(s.trace(x) for x in C)==1)
ctrl('omitting_TP_defect_false',data29(C)==data29(B) and sum(dist(x-y) for x,y in zip(C,B))>0)
E=sum((ptr(x) for x in C),s.zeros(2))-I/2;ck('TP_defect_bound_exact',sum(dist(x-y) for x,y in zip(C,B))==dist(E))
ck('Pauli_Gram',s.Matrix([[s.trace(A*B) for B in basis] for A in basis])==4*s.eye(16))
# Exact full outcome distribution checks all48 estimator means/second moments, including complex directions.
Kcomplex=(s.kronecker_product(Y,Y)+s.kronecker_product(I,Y)+s.kronecker_product(X,Y))/4
B=[Phi/3,(s.eye(4)+Kcomplex)/12,(s.eye(4)-Kcomplex)/12]
ck('complex_fixture_CP_TP',all(psd(x) for x in B) and sum((ptr(x) for x in B),s.zeros(2))==I/2)
distribution=[]
for A,Baxis,sg,sb,z in product(range(1,4),range(1,4),[-1,1],[-1,1],range(3)):
 effect=s.kronecker_product((I+sg*pa[A])/2,(I+sb*pa[Baxis])/2);pr=s.simplify(s.trace(B[z]*effect)/9);distribution.append((A,Baxis,sg,sb,z,pr))
ck('nine_setting_distribution_normalized',sum(t[-1] for t in distribution)==1 and all(t[-1]>=0 for t in distribution))
for z,a,b in product(range(3),range(4),range(4)):
 w=3**int(a!=0)*3**int(b!=0);ev=0;ev2=0
 for A,Baxis,sg,sb,flag,pr in distribution:
  val=w*int(flag==z)*int(a==0 or A==a)*int(b==0 or Baxis==b)*(sg if a else 1)*(sb if b else 1);ev+=pr*val;ev2+=pr*val*val
 ck(f'estimator_{z}_{a}_{b}',s.simplify(ev-s.trace(B[z]*basis[4*a+b]))==0 and ev2<=w)
ctrl('single_Y_sign_matters',s.trace(s.kronecker_product(I,Y)*B[1])!=0 and B[1]!=s.conjugate(B[1]))
ctrl('Y_information_required',s.trace(s.kronecker_product(Y,Y)*B[1])!=0)
large=rec44(s.Matrix([10]+[0]*43),True);ctrl('signed_norm_not_clippable',sum(dist(M) for M in large)>1)
n=4_000_000_000;alpha=arb('.05');L=(arb(96)*n*(n+1)/alpha).log();r={w:(2*w*L/n).sqrt()+2*(w+1)*L/(3*n) for w in [1,3,9]};e=[r[3**int(a!=0)*3**int(b!=0)]+arb('.00002') for a,b in product(range(4),repeat=2)]
norm=lambda xs:sum((x*x for x in xs),arb(0)).sqrt()
e_g=r[1]+arb('.00002');b29=(e_g+norm(e)+norm([e[j] for j in idx]+[e[4*a]+(e_g if a==0 else 0) for a in range(4)]))/2
pupper=(3*(r[1]+arb('.00002'))+3*(r[9]+arb('.00002')))/4
b44=(2*norm(e)+norm([e[j] for j in idx]+[2*e[4*a] for a in range(4)]))/2;b48=3*norm(e)/2
ck('finite_sample_support_penalty_can_dominate',b29+2*pupper.sqrt()>b48);ck('nine_setting_variance_improvement',r[9]<(32*L/n).sqrt()+34*L/(3*n))
deps=['tests/channel-swings/k2419_positive_visibility_dual_probe.py','lab/process/k2438-mixed-instrument-certification.json',str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2439-minimal-flagged-tomography-2026-11-01.md']
report={'result_id':'K2439','checks':checks,'controls':controls,'tensor_order':'R,B; original K2419 B,R map is reconstructed in swapped order','fixtures':fixtures,'dimensions':{'supported':33,'supported_TP':29,'full':48,'full_TP':44},'prospective':{'n':n,'simultaneous_M':48,'statistical_widths':{str(w):str(x) for w,x in r.items()},'B29_without_leak':str(b29),'signed_leakage_upper_example':str(pupper),'B29_with_leak_using_g_le_1':str(b29+2*pupper.sqrt()),'B44':str(b44),'B48':str(b48),'status':'hypothetical residual1e-5 and readout1e-5; no measured data'},'evidence_kinds':{'exact':'original CP/TP laws,73 independent deletion tangents, coordinate inverses, full complex nine-axis outcomes and physical leakage/TP controls','rigorous_numeric':'Arb256 prospective widths and propagation','universal':'written affine-family minimum, stability, preparation transfer and simultaneous martingale proof'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2439-minimal-flagged-tomography.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2439',len(checks),'checks',len(controls),'controls PASS');print(json.dumps(report['prospective'],indent=2))
