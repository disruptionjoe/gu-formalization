"""Exact algebraic checks for K2395; written proof supplies universal optimum."""
from pathlib import Path
from itertools import combinations
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2];Q=s.Rational
checks={};controls={}
def clean(x):return s.simplify(x)
def zero(x):return clean(x)==s.zeros(*x.shape) if isinstance(x,s.MatrixBase) else clean(x)==0
def check(n,v):
 checks[n]=bool(v)
 if not v:raise AssertionError(n)
def control(n,v):
 controls[n]=bool(v)
 if not v:raise AssertionError(n)
def psd(A):return all(bool(clean(A.extract(ix,ix).det())>=0) for j in range(1,A.rows+1) for ix in combinations(range(A.rows),j))
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);pa=[X,Y,Z];kron=s.kronecker_product
# Universal algebraic identities behind the maximization.
a,b,n,d,D,h,K,L,c=s.symbols('a b nu d D h K L c',real=True)
check('maximization_square_identity',s.expand(a*a*(1-d*d)+n*n*(L+d*d*K+2*d*D)-(n*n*(L+K)+2*n*n*D*d+(1-d*d)*(a*a-n*n*K)))==0)
q=n*n*(L+K)+2*n*n*D*d+(1-d*d)*h
check('interior_stationary_point',clean(s.diff(q,d).subs(d,n*n*D/h))==0)
check('interior_optimum_value',clean(q.subs(d,n*n*D/h)-(n*n*(L+K)+h+n**4*D**2/h))==0)
check('exact_gain_factorization',clean(n*n*(1-2*D)+h+n**4*D**2/h-n*n-(h-n*n*D)**2/h)==0)
z,j=s.symbols('z j',real=True);MM=s.Matrix([[z,j],[j,1-z]])
check('trace_one_cayley_hamilton',zero(MM*MM+MM.det()*I-MM))
# Canonical complete-positivity identities; not a numerical channel ansatz.
cc,dd=s.symbols('cc dd',real=True);tt2=(1-cc*cc)*(1-dd*dd)
check('canonical_two_choi_equalities',clean((1+cc*dd)**2-tt2-(cc+dd)**2)==0 and clean((1-cc*dd)**2-tt2-(cc-dd)**2)==0)
# Exact nonaligned fixture with a rational eigenaxis and polar numerator.
m=s.Matrix([Q(1,2),Q(23,72)]);M=s.diag(Q(3,4),Q(1,4));nu=Q(25,36);D=M.det();H=m*m.T-nu**2*M*M
kk=s.Matrix([Q(3,5),Q(4,5)]);ll=s.Matrix([Q(4,5),-Q(3,5)]);QQ=s.Matrix.hstack(ll,kk)
h=Q(1325,6912);d=Q(25,53);F=s.sqrt(Q(2300,4293));av=Q(5,9)
check('fixture_moment_feasible',psd(M-m*m.T) and (m.T*M.inv()*m)[0]==Q(961,1296))
check('fixture_top_eigenpair',zero(H*kk-h*kk) and h>s.trace(H)-h)
check('fixture_improvement_region',h>nu**2*D and d==nu**2*D/h)
check('fixture_closed_value',zero(F**2-(nu**2*s.trace(M*M)+h+nu**4*D**2/h)))
T=M*QQ*s.diag(1,d)
# For positive det T, W/S is the orthogonal polar factor maximizing tr(O T).
W=s.Matrix([[T[0,0]+T[1,1],T[1,0]-T[0,1]],[T[0,1]-T[1,0],T[0,0]+T[1,1]]])
S2=clean(s.trace(T.T*T)+2*T.det());SS=s.sqrt(S2);OO=W/SS
check('fixture_polar_rotation',zero(OO*OO.T-I) and clean(OO.det())==1 and zero(s.trace(OO*T)-SS))
c=clean(nu*SS/F);tv=clean(av*(1-d*d)/F)*kk;Ap=clean((nu/F)*QQ*s.diag(1,d)*W)
check('fixture_canonical_parameters',zero(c*c-Q(673,1219)) and zero(tv.dot(tv)-(1-c*c)*(1-d*d)))
check('fixture_planar_rotation',QQ.T*QQ==I and QQ.det()==1)
# Embed plane xz and physical perpendicular contraction.
t=s.Matrix([tv[0],0,tv[1]]);A=s.Matrix([[Ap[0,0],0,Ap[0,1]],[0,d,0],[Ap[1,0],0,Ap[1,1]]])
check('fixture_actual_objective',zero(m.dot(tv)+nu*s.trace(Ap*M)-F))
J=clean((kron(I+sum((t[i]*pa[i] for i in range(3)),s.zeros(2)),I)+sum((A[i,j]*kron(pa[i],pa[j].T) for i in range(3) for j in range(3)),s.zeros(4)))/2)
def ptr(J):return s.Matrix(2,2,lambda i,j:sum(J[2*a+i,2*a+j] for a in range(2)))
check('fixture_choi_trace',ptr(J)==I)
check('fixture_choi_all_principal_minors',psd(J))
check('fixture_choi_rank_two',J.rank()==2)
# Exact pivoted rank-two Cholesky recovers actual Kraus operators from J.
remaining=J;ks=[]
for count in range(2):
 pivot=next(i for i in range(4) if clean(remaining[i,i])>0)
 p=remaining[pivot,pivot];v=remaining[:,pivot]
 kv=v/s.sqrt(p);ks.append(s.Matrix(2,2,list(kv)))
 remaining=clean(remaining-v*v.T/p)
check('fixture_kraus_reconstruct_choi',zero(remaining))
check('fixture_kraus_TP',zero(sum((K.T*K for K in ks),s.zeros(2))-I))
def apply(rho):return clean(sum((K*rho*K.T for K in ks),s.zeros(2)))
check('fixture_kraus_translation',zero(apply(I/2)-(I+t[0]*X+t[2]*Z)/2))
for jj in range(3):check('fixture_kraus_column_'+str(jj),zero(apply(pa[jj])-sum((A[i,jj]*pa[i] for i in range(3)),s.zeros(2))))
# Original sign instrument, including its input-dependent trace, composed with actual Kraus.
def blocks(rho,z):
 r=s.Matrix([s.trace(rho*X),s.trace(rho*Z)]);tr=s.trace(rho)
 v=nu*(m*tr+z*M*r)
 return ((tr+z*m.dot(r))*I+v[0]*X+v[1]*Z)/4
B=clean(tv*m.T+nu*Ap*M)
check('fixture_paired_B_symmetric_psd',B==B.T and psd(B) and zero(s.trace(B)-F))
for jj,rho in enumerate([I/2,X,Y,Z]):
 out=clean(apply(blocks(rho,1))+Y*apply(blocks(rho,-1))*Y)
 r=s.Matrix([s.trace(rho*X),s.trace(rho*Z)]);br=B*r
 target=(s.trace(rho)*I+br[0]*X+br[1]*Z)/2
 check('fixture_full_sign_composition_'+str(jj),zero(out-target))
wrong=clean(apply(blocks(I/2,1))+apply(Y*blocks(I/2,-1)*Y))
control('wrong_nonunital_sign_order_rejected',not zero(wrong-I/2))
control('transpose_is_not_CP',not psd((kron(I,I)+kron(X,X)-kron(Y,Y.T)+kron(Z,Z))/2))
control('changed_choi_trace_rejected',ptr(J/2)!=I)
control('changed_optimum_rejected',not zero(F**2+Q(1,1000)-(nu**2*s.trace(M*M)+h+nu**4*D**2/h)))
# Earlier independent rational certificate encloses the new exact radical answer.
old=json.loads((R/'lab/process/k2392-nonaligned-clock-recovery.json').read_text())
oldc=old['nonaligned_certificate'];low=Q(oldc['F_lower']);up=Q(oldc['F_upper'])
h0=(195+12*s.sqrt(10169))/6400;F02=Q(361,640)+h0+Q(1083,6400)**2/h0
check('prior_rational_interval_encloses_exact_optimum',bool(F02>low**2) and bool(F02<up**2))
control('naive_aligned_formula_rejected',bool(F02>Q(19,20)**2))
# Known endpoints, including zero visibility and singular moments.
def value2(mean,MM,v):
 HH=mean*mean.T-v*v*MM*MM;hh=(s.trace(HH)+s.sqrt((HH[0,0]-HH[1,1])**2+4*HH[0,1]**2))/2;det=MM.det()
 return clean(v*v if hh<=v*v*det else v*v*s.trace(MM*MM)+hh+v**4*det**2/hh)
for name,mean,MM,v,ans in [
 ('zero_visibility',m,M,Q(0),m.dot(m)),
 ('zero_mean',s.zeros(2,1),M,Q(2,3),Q(4,9)),
 ('noiseless',m,M,Q(1),Q(1)),
 ('antipodal_sign',s.Matrix([Q(4,5),0]),s.diag(1,0),Q(1,2),Q(16,25)),
 ('antipodal_clock',s.Matrix([Q(1,5),0]),s.diag(1,0),Q(1,2),Q(1,4)),
 ('aligned_interior',s.Matrix([Q(1,2),0]),I/2,Q(1,2),Q(1,3)),
 ('zero_all',s.zeros(2,1),I/2,Q(0),Q(0))]:check(name,zero(value2(mean,MM,v)-ans))
check('fixture_noise_margin_factorization',zero((F-nu)-(h-nu**2*D)**2/(h*(F+nu))))
report={'result':'K2395','evidence_kind':'exact symbolic identities, actual algebraic Kraus/sign-block composition, principal-minor checks and independent prior rational interval; universal optimum uses written proof and RSW rank-two theorem','checks':checks,'controls':controls,'fixture':{'mean':[str(x) for x in m],'M':[str(M[0,0]),str(M[1,1])],'nu':str(nu),'h':str(h),'F_squared':str(F**2),'F_display_only':str(s.N(F,15)),'translation':[str(x) for x in tv],'planar_A':[[str(Ap[i,j]) for j in range(2)] for i in range(2)]},'prior_fixture_exact_F_squared':str(F02),'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in ['lab/process/k2392-nonaligned-clock-recovery.json']}}
if '--write' in sys.argv:(R/'lab/process/k2395-planar-recovery-closed-form.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps(report,sort_keys=True))
