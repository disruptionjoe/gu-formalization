"""Exact rational/algebraic certificates for the planar clock recovery theorem."""
from pathlib import Path
from itertools import combinations
import sympy as s
import json,sys,hashlib
R=Path(__file__).resolve().parents[2];Q=s.Rational;checks={};controls={}
def check(n,v):
 checks[n]=bool(v)
 if not v:raise AssertionError(n)
def control(n,v):
 controls[n]=bool(v)
 if not v:raise AssertionError(n)
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);pa=[X,Y,Z];k=s.kronecker_product
vec=s.Matrix([1,0,0,1]);Jid=vec*vec.T
m=s.Matrix([Q(3,4),0,Q(1,4)]);M=s.diag(Q(3,4),0,Q(1,4));nu=Q(19,20)
C=(k(m[0]*X+m[2]*Z,I)+nu*sum((M[i,j]*k(pa[i],pa[j].T) for i in range(3) for j in range(3)),s.zeros(4)))/2
def ptr(J):return s.Matrix(2,2,lambda i,j:sum(J[2*a+i,2*a+j] for a in range(2)))
def psd(A):return all(s.det(A.extract(ix,ix))>=0 for n in range(1,A.rows+1) for ix in combinations(range(A.rows),n))
check('identity_choi_trace',ptr(Jid)==I)
check('identity_objective',s.trace(C*Jid)==nu)
Yi=(nu*I+m[0]*X+m[2]*Z)/2;slack=k(I,Yi)-C
check('forced_identity_complementarity',slack*vec==s.zeros(4,1))
V=s.Matrix.hstack(s.Matrix(X).reshape(4,1),s.Matrix(Z).reshape(4,1),s.Matrix(s.I*Y).reshape(4,1))/s.sqrt(2)
H=s.Matrix([[nu/4,0,-Q(1,4)],[0,3*nu/4,Q(3,4)],[-Q(1,4),Q(3,4),nu]])
# Matrix-vector convention may reverse iY; a sign flip is an orthogonal basis change.
HB=s.simplify(V.T*slack*V)
check('Bell_complement_slack',HB==H or HB==s.diag(1,1,-1)*H*s.diag(1,1,-1))
control('identity_dual_negative_determinant',H.det()==-Q(2223,128000))
control('naive_aligned_transfer_passes_false_premise',Q(5,8)<nu**2*Q(7,10) and M*m!=Q(7,10)*m)
check('actual_moment_feasibility',psd(M-m*m.T))
check('identity_criterion_violated', (m.T*M.pinv()*m)[0]==1 and nu**2<1)
# Exact symbolic known feasible nonaligned decoder.
cu=19/s.sqrt(439);cv=Q(361,439);su=s.sqrt(1-cu**2);sv=s.sqrt(1-cv**2);t=s.simplify(su*sv);x=cu*cv;y=cu;zz=cv
check('extreme_channel_CP_equalities',s.simplify((1+x)**2-t*t-(y+zz)**2)==0 and s.simplify((1-x)**2-t*t-(y-zz)**2)==0 and 1-x>=t)
F=s.simplify(t/s.sqrt(2)+nu*(x+y)/2)
check('nonaligned_feasible_value',F==20/s.sqrt(439))
control('strict_improvement_over_wrong_transfer',s.simplify(F**2-nu**2)==Q(1521,175600))
# Rational near-optimal primal and dual. Numerical search is discovery only;
# every acceptance predicate below uses exact rational matrices.
def sc(z):return (2*z/(1+z*z),(1-z*z)/(1+z*z))
sa,ca=sc(Q(547,1772));sb,cb=sc(Q(203,4413));sp,cp=sc(Q(22184,9189));sq,cq=sc(Q(-19065,8629))
su=sb*ca-cb*sa;cu=cb*ca+sb*sa;sv=sb*ca+cb*sa;cv=cb*ca-sb*sa
rotp=s.Matrix([[cp,0,sp],[0,1,0],[-sp,0,cp]]);rotq=s.Matrix([[cq,0,sq],[0,1,0],[-sq,0,cq]])
tv=rotq*s.Matrix([0,0,su*sv]);A=rotq*s.diag(cu,cv,cu*cv)*rotp
J=(k(I+sum((tv[i]*pa[i] for i in range(3)),s.zeros(2)),I)+sum((A[i,j]*k(pa[i],pa[j].T) for i in range(3) for j in range(3)),s.zeros(4)))/2
check('rational_decoder_trace',ptr(J)==I)
check('rational_decoder_CP_all15_principal_minors',psd(J))
L=s.trace(C*J);upperY=(Q(50405768,105445577)+Q(1,10**7))*I+Q(56236105,160093158)*X+Q(77233853,750908558)*Z
S=k(I,upperY)-C;U=s.trace(upperY)
check('rational_dual_all15_principal_minors',psd(S))
check('exact_gap_below_one_millionth',0<=U-L<Q(1,10**6))
check('certified_lower_strictly_above_identity',L>nu)
check('Choi_Bloch_objective_match',L==(m.T*tv)[0]+nu*s.trace(A*M))
# True failure controls change the channel/certificate and rerun unchanged predicates.
control('changed_trace_rejected',ptr(J/2)!=I)
control('changed_dual_rejected',not psd(k(I,upperY-Q(1,100)*I)-C))
control('non_CP_matrix_rejected',not psd(Jid-Q(1,100)*s.eye(4)))
# Singular and noiseless exact threshold controls.
for mean,MM,v in [(s.zeros(3,1),s.diag(Q(1,2),0,Q(1,2)),Q(1,3)),(s.Matrix([Q(1,2),0,0]),s.diag(1,0,0),Q(1,2)),(m,M,Q(1))]:
 CC=(k(sum((mean[i]*pa[i] for i in range(3)),s.zeros(2)),I)+v*sum((MM[i,j]*k(pa[i],pa[j].T) for i in range(3) for j in range(3)),s.zeros(4)))/2
 YY=(v*I+sum((mean[i]*pa[i].T for i in range(3)),s.zeros(2)))/2
 assert psd(k(I,YY)-CC) and s.trace(CC*Jid)==v
check('uniform_singular_and_noiseless_duals',True)
control('unrealizable_singular_mean_rejected',not psd(s.diag(1,0)-s.Matrix([0,Q(1,2)])*s.Matrix([[0,Q(1,2)]])))
report={'result':'K2392','evidence_kind':'exact Choi/principal-minor and rational/algebraic certificates; universal optimization and transfer claims are written proofs','checks':checks,'controls':controls,'nonaligned_certificate':{'moment_mean':['3/4','0','1/4'],'moment_diagonal':['3/4','0','1/4'],'visibility':'19/20','primal_half_angle_tangents':['547/1772','203/4413','22184/9189','-19065/8629'],'dual_Y_coefficients':[str((Q(50405768,105445577)+Q(1,10**7))),str(Q(56236105,160093158)),str(Q(77233853,750908558))],'F_lower':str(L),'F_upper':str(U),'gap':str(U-L),'decimal_display_only':[str(s.N(L,15)),str(s.N(U,15))]},'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in ['lab/process/k2389-clock-pointer-recovery.json']}}
if '--write' in sys.argv:(R/'lab/process/k2392-nonaligned-clock-recovery.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps(report,sort_keys=True))
