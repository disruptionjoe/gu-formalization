"""Arbitrary planar Choi support, scalar saddle reduction and rigorous gap."""
from pathlib import Path
import ast,json,hashlib,sys
from itertools import combinations
import sympy as s
from flint import arb,ctx
R=Path(__file__).resolve().parents[2];Q=s.Rational;I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);paulis=[X,Z]
checks={};controls={}
def ck(n,b):
 checks[n]=bool(b)
 if not b:raise AssertionError(n)
def ctrl(n,b):
 controls[n]=bool(b)
 if not b:raise AssertionError(n)
p=R/'tests/channel-swings/k2419_positive_visibility_dual_probe.py'
for node in ast.parse(p.read_text()).body:
 if isinstance(node,ast.FunctionDef) and node.name in ['simp','choi','ptr','minors','psd','channel']:
  exec(compile(ast.Module(body=[node],type_ignores=[]),str(p),'exec'),globals())
def support_matrix(v,M):return simp((sum((v[a]*s.kronecker_product(paulis[a],I) for a in range(2)),s.zeros(4))+sum((M[a,b]*s.kronecker_product(paulis[a],paulis[b].T) for a in range(2) for b in range(2)),s.zeros(4)))/2)
def support(v,M):
 H=v*v.T-M*M.T;gap=s.sqrt((H[0,0]-H[1,1])**2+4*H[0,1]**2);h=(s.trace(H)+gap)/2;delta=abs(M.det());T=s.trace(M*M.T)
 return s.sqrt(T+2*delta if h<=delta else T+h+delta**2/h)
fixtures=[('nonsymmetric',s.Matrix([3,0]),s.Matrix([[0,2],[1,0]]),s.Matrix([7*s.sqrt(30)/50,0]),s.Matrix([[0,s.sqrt(30)/25],[s.sqrt(30)/10,0]]),-Q(2,5),3*s.sqrt(30)/5),('rank_one',s.Matrix([0,1]),s.Matrix([[0,2],[0,0]]),s.Matrix([0,1/s.sqrt(5)]),s.Matrix([[0,2/s.sqrt(5)],[0,0]]),0,s.sqrt(5)),('reflection',s.zeros(2,1),s.diag(1,-1),s.zeros(2,1),s.diag(1,-1),-1,s.Integer(2)),('preparation',s.Matrix([3,4]),s.zeros(2),s.Matrix([Q(3,5),Q(4,5)]),s.zeros(2),0,s.Integer(5)),('zero',s.zeros(2,1),s.zeros(2),s.zeros(2,1),s.zeros(2),0,s.Integer(0))]
certs=[]
for name,v,M,t,A,y,phi in fixtures:
 J=choi(lambda op:channel(t,A,y,op));H=support_matrix(v,M);zvec=A.T*v+M.T*t;Zd=(phi*I+zvec[0]*X+zvec[1]*Z)/2;D=simp(s.kronecker_product(I,Zd)-H)
 ck(name+'_formula',s.simplify(support(v,M)-phi)==0)
 ck(name+'_original_Choi_CP_TP',psd(J) and ptr(J)==I)
 ck(name+'_original_support',s.simplify(s.trace(H*J)-phi)==0)
 ck(name+'_dual_PSD',psd(D));ck(name+'_complementarity',simp(D*J)==s.zeros(4) and s.trace(Zd)==phi)
 certs.append({'fixture':name,'support':str(phi),'Choi_rank':J.rank(),'dual_slack_rank':D.rank()})
ctrl('transpose_Gram_changes_support',support(s.Matrix([0,1]),s.Matrix([[0,2],[0,0]]))!=2)
ctrl('reflection_needs_perpendicular_sign',not psd(choi(lambda op:channel(s.zeros(2,1),s.diag(1,-1),1,op))))
ctrl('independent_translation_plus_identity_not_CP',not psd(choi(lambda op:channel(s.Matrix([Q(1,2),0]),I,1,op))))
# Exact canonical saturation and polar-gradient formula, not rounded eigenvalues.
c,d,a,b=s.symbols('c d a b',real=True);h,delta,T=s.symbols('h delta T',real=True)
ck('scalar_quadratic_branch_identity',s.factor((T+2*delta*d+(1-d*d)*h).subs(d,delta/h)-(T+h+delta**2/h))==0)
ck('gain_over_unital_identity',s.factor(T+h+delta**2/h-(T+2*delta)-(h-delta)**2/h)==0)
v,M,t,A,y,phi=fixtures[0][1:];P=s.diag(1,0);dd=Q(2,5);co=s.Matrix([[M[1,1],-M[1,0]],[-M[0,1],M[0,0]]])
ck('gradient_translation_fixture',simp((1-dd**2)*P*v/phi-t)==s.zeros(2,1));ck('gradient_matrix_fixture',simp((M-(1-dd**2)*P*M-dd*co)/phi-A)==s.zeros(2))
# Symbolic original sign-instrument composition on both actual endpoint laws.
means=[s.Matrix([Q(125,338),Q(150,169)]),s.Matrix([Q(49,250),-Q(84,125)])];ws=[Q(73,100),Q(37,52)];lens=[Q(25,26),Q(7,10)];Qs=[m*m.T/(2*r*r) for m,r in zip(means,lens)]
tx,tz,aa,bb,cc,dd,yy,ga,gb=s.symbols('tx tz aa bb cc dd yy ga gb',real=True);tt=s.Matrix([tx,tz]);AA=s.Matrix([[aa,bb],[cc,dd]]);G=s.Matrix([[ga,gb],[-gb,ga]])
for idx,(m,r,w,M) in enumerate(zip(means,lens,ws,Qs)):
 n=m/r;law=[((1+r)/2,n),((1-r)/2,-n)]
 ck('actual_law_'+str(idx),n.dot(n)==1 and sum(p for p,n in law)==1 and all(p>=0 for p,n in law))
 def block(op,sg):
  rr=s.Matrix([s.trace(op*X),s.trace(op*Z)])
  return simp(sum((p*(s.trace(op)+sg*n.dot(rr))/2*(I+(n[0]*X+n[1]*Z)/2)/2 for p,n in law),s.zeros(2)))
 for sg in [-1,1]:ck('actual_sign_CP_'+str(idx)+str(sg),psd(choi(lambda op:block(op,sg))))
 B=tt*m.T+AA*M
 for j,op in enumerate([I/2,X,Y,Z]):
  full=(1-w)*channel(s.zeros(2,1),G,1,op)+w*(channel(tt,AA,yy,block(op,1))+Y*channel(tt,AA,yy,block(op,-1))*Y)
  ck('original_composition_'+str(idx)+'_'+str(j),simp(full-channel(s.zeros(2,1),(1-w)*G+w*B,1-w,op))==s.zeros(2))
ck('compact_cone_constants',[s.factor((2-w)**2/(w*(4-w))) for w in ws]==[Q(16129,23871),Q(4489,6327)])
ck('identity_upper_and_rectangle',max(w*(3-s.trace(q))/4 for w,q in zip(ws,Qs))==Q(73,160) and max((4*Q(73,160)-w)/(2*w) for w in ws)==Q(579,740))
# Certified interval follow-through. Search only suggested these rational inputs.
# Every subsequent operation uses Arb enclosures and the exact physical construction.
ctx.prec=256
def ar(x):return arb(int(s.numer(x)))/arb(int(s.denom(x)))
def ma(A):return [[ar(x) for x in row] for row in A.tolist()]
def trans(A):return [list(x) for x in zip(*A)]
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def plus(A,B,c=1):return [[a+c*b for a,b in zip(x,y)] for x,y in zip(A,B)]
def scale(A,c):return [[c*x for x in row] for row in A]
def outer(v,w):return [[x*y for y in w] for x in v]
def dot(v,w):return sum(x*y for x,y in zip(v,w))
def mv(A,v):return [dot(row,v) for row in A]
def norm(v):return dot(v,v).sqrt()
ident=[[arb(1),arb(0)],[arb(0),arb(1)]]
lrat=Q(518217355906395628505131873324,10**30);trat=Q(57537330873480255935665491873,10**30)
lam,tau=ar(lrat),ar(trat);qr=[[lam,-tau],[1-lam,tau]];rr=[norm(q) for q in qr];RR=sum(rr);ww=list(map(ar,ws));ms=[[ar(x) for x in m] for m in means];qq=list(map(ma,Qs));sv=[sum((1-w)*q[a] for w,q in zip(ww,qr)) for a in range(2)];V=[arb(0),arb(0)];N=[[arb(0),arb(0)],[arb(0),arb(0)]]
for w,q,m,Qm in zip(ww,qr,ms,qq):
 Fm=[[q[0],q[1]],[-q[1],q[0]]];V=[a+w*b for a,b in zip(V,mv(Fm,m))];N=plus(N,mm(Fm,Qm),w)
H=plus(outer(V,V),mm(N,trans(N)),-1);eigengap=((H[0][0]-H[1][1])**2+4*H[0][1]**2).sqrt();hh=(H[0][0]+H[1][1]+eigengap)/2;loweig=hh-eigengap;det=N[0][0]*N[1][1]-N[0][1]*N[1][0]
ck('candidate_compact_domain',trat**2<=Q(16129,23871)*lrat**2 and trat**2<=Q(4489,6327)*(1-lrat)**2)
ck('interval_simple_improving_positive_det',eigengap>0 and det>0 and hh>det)
delt=det;d0=delt/hh;TT=sum(x*x for row in N for x in row);phi0=(TT+hh+delt*delt/hh).sqrt();proj=scale(plus(H,ident,-loweig),1/eigengap);tv=[(1-d0*d0)*x/phi0 for x in mv(proj,V)];cof=[[N[1][1],-N[1][0]],[-N[0][1],N[0][0]]];AA0=scale(plus(plus(N,mm(proj,N),-(1-d0*d0)),cof,d0),1/phi0);g=[x/norm(sv) for x in sv];GG=[[g[0],g[1]],[-g[1],g[0]]]
dual=(dot(ww,rr)+2-2*norm(sv)-phi0)/(4*RR);errors=[];L2s=[];H2s=[]
for w,m,Qm in zip(ww,ms,qq):
 B=plus(outer(tv,m),mm(AA0,Qm));C=plus(plus(ident,GG,-(1-w)),B,-w);ell=[C[0][0]+C[1][1],C[0][1]-C[1][0]];L2=dot(ell,ell);H2=(C[0][0]-C[1][1])**2+(C[0][1]+C[1][0])**2;errors.append((w+L2.sqrt())/4);L2s.append(L2);H2s.append(H2)
ck('original_full_norm_branch',all(H2<w*w<L2 for w,H2,L2 in zip(ww,H2s,L2s)))
lower=Q(446966996608947629838642518,10**27);upper=Q(446966996608947629838642519,10**27)
ck('rigorous_global_lower',dual>ar(lower));ck('rigorous_constructed_upper',all(e<ar(upper) for e in errors));ck('certified_gap_1e_minus27',upper-lower==Q(1,10**27))
ctrl('rounded_claim_above_primal_not_lower',dual<ar(upper));ctrl('old_nonstationary_dual_not_exact',Q(263,500)*(-Q(21,221))+Q(237,500)*Q(19,181)!=0)
report={'result_id':'K2424','checks':checks,'controls':controls,'support_fixtures':certs,'rational_dual_candidate':{'lambda':str(lrat),'t':str(trat)},'certified_bracket':{'lower':str(lower),'upper':str(upper),'width':str(upper-lower),'dual_enclosure':str(dual),'primal_endpoint_enclosures':list(map(str,errors)),'precision_bits':ctx.prec},'scope':'Closed arbitrary real planar Choi support; exact compact two-scalar global maximum; original physical radical primal and dual certify a 1e-27 bracket. Exact maximizing algebraic point, uniqueness, physical apparatus and GU interpretation unproved.'}
deps=['tests/channel-swings/k2419_positive_visibility_dual_probe.py','explorations/conditional-build/k2395-planar-recovery-closed-form-2026-10-31.md','explorations/conditional-build/k2422-joint-recovery-optimality-2026-10-31.md']
import flint
report['software']={'sympy':s.__version__,'python_flint':flint.__version__}
report['dependencies']={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps};out=R/'lab/process/k2424-recovery-saddle-reduction.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:assert json.loads(out.read_text())==report
print(json.dumps({'checks':len(checks),'controls':len(controls),'bracket':report['certified_bracket']}))
