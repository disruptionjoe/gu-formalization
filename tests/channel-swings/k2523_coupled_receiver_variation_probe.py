"""Exact independent normal-jet and full coupled-response controls for K2523."""
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
basis=[s.diag(1,1,0,0)/s.sqrt(2),s.diag(1,-1,2,0)/s.sqrt(6),s.diag(1,-1,-1,3)/s.sqrt(12)]
for i,j in [(1,2),(1,3),(2,3),(0,1),(0,2),(0,3)]:
 a=s.zeros(4);a[i,j]=a[j,i]=1/s.sqrt(2);basis.append(a)
basis.append(g/2);pairs=[(i,j) for i in range(4) for j in range(i,4)]
L=s.Matrix([[a[i,j] for a in basis] for i,j in pairs]);II=[-sign[a]*basis[a]/2 for a in range(10)];H=[s.trace(g*a) for a in II]
ck('inherited_free_graph_receiver',L.rank()==10)
alpha,beta=s.symbols('alpha beta');mom=[alpha*a+beta*g*hh for a,hh in zip(II,H)]
coeff=s.Matrix([[s.diff(a[i,j],v) for v in (alpha,beta)] for a in mom for i,j in pairs]);ck('full_graph_moment_forces_both_coefficients_zero',coeff.rank()==2 and coeff.nullspace()==[])
ck('moment_trace_identity',all(s.simplify(s.trace(g*a)-(alpha+4*beta)*hh)==0 for a,hh in zip(mom,H)))
# Full symmetric tensor map splits trace and traceless subspaces; no norm test substitutes.
vecg=s.Matrix([g[i,j] for i,j in pairs]);trace=s.Matrix([[g[i,i] if i==j else 0 for i,j in pairs]])
Tmap=vecg*trace;M=alpha*s.eye(10)+beta*Tmap
ck('trace_map_eigenvalue_four',Tmap*Tmap==4*Tmap)
ck('bending_map_generic_determinant',s.factor(M.det())==alpha**9*(alpha+4*beta))
ck('generic_bending_rank_ten',M.subs({alpha:1,beta:1}).rank()==10)
ck('tracefree_bending_map_kernel_one',M.subs({alpha:1,beta:-s.Rational(1,4)}).rank()==9 and M.subs({alpha:1,beta:-s.Rational(1,4)})*vecg==s.zeros(10,1))
ck('mean_only_bending_map_rank_one',M.subs({alpha:0,beta:1}).rank()==1)
ck('tracefree_receiver_dimension_nine',len(trace.nullspace())==9)
ck('umbilic_receiver_rank_at_most_one',(vecg*s.ones(1,10)).rank()==1)
# Actual ambient metric G_ij(y)=g_ij+sum yA*dAij has induced constant g;
# Christoffel products compute its tangential scalar (no x derivatives).
def scalar_tan(ds):
 value=0
 for i,j in itertools.product(range(4),repeat=2):
  # <R(e_i,e_j)e_j,e_i>; Gamma^i_iA Gamma^A_jj - Gamma^i_jA Gamma^A_ij
  value+=g[i,i]*g[j,j]*sum(sign[a]*(ds[a][i,j]**2-ds[a][i,i]*ds[a][j,j])/4 for a in range(10))
 return s.simplify(value)
def norm2(arr):return sum(sign[a]*s.trace(g*arr[a]*g*arr[a]) for a in range(10))
def mean2(arr):return sum(sign[a]*s.trace(g*arr[a])**2 for a in range(10))
ds=[-2*sign[a]*II[a] for a in range(10)]
ck('actual_connection_Gauss_scalar',s.simplify(scalar_tan(ds)+mean2(II)-norm2(II))==0)
# All 100 independent normal jets, including symmetric off-diagonal multiplicity.
jetok=[];gaussok=[];nonzero=[]
for A in range(10):
 for i,j in pairs:
  J=s.zeros(4);J[i,j]=J[j,i]=1
  dII=-sign[A]*J/2
  delta_norm=2*sign[A]*s.trace(g*II[A]*g*dII);delta_mean=2*sign[A]*H[A]*s.trace(g*dII)
  direct=(alpha*delta_norm+beta*delta_mean)/2
  expected=-s.trace(g*mom[A]*g*J)/2
  jetok.append(s.simplify(direct-expected)==0)
  # Differentiate actual Christoffel-product scalar under this metric normal jet.
  dt=0
  for k,l in itertools.product(range(4),repeat=2):
   dt+=g[k,k]*g[l,l]*sign[A]*(2*ds[A][k,l]*J[k,l]-J[k,k]*ds[A][l,l]-ds[A][k,k]*J[l,l])/4
  gaussok.append(s.simplify(dt+delta_mean-delta_norm)==0)
  nonzero.append(s.simplify(delta_mean-delta_norm)!=0)
ck('all_100_independent_normal_jet_coefficients',all(jetok))
ck('EH_cancellation_all_100_actual_connection_jets',all(gaussok))
ct('dropping_ambient_curvature_loses_nonzero_cancellation',any(nonzero))
ct('pure_II_graph_is_not_stationary',any(a.subs({alpha:1,beta:0})!=s.zeros(4) for a in mom))
ct('pure_mean_graph_is_not_stationary',any(a.subs({alpha:0,beta:1})!=s.zeros(4) for a in mom))
ct('tuned_tracefree_bending_still_fails_free_graph',any(a.subs({alpha:1,beta:-s.Rational(1,4)})!=s.zeros(4) for a in mom))
# Null-valued II can have zero norm and a nonzero moment.
nullII=[s.zeros(4) for _ in range(10)];nullII[0][0,0]=1;nullII[6][0,0]=1
ct('indefinite_zero_norm_does_not_kill_jet_source',norm2(nullII)==0 and nullII[0]!=s.zeros(4))
# Complete 2 ambient + 10 normal finite control with actual nontrivial receiver.
B=s.Matrix([[2,1],[1,3]]);C=s.diag(*[s.Rational(i+1)*(-1 if i%3==0 else 1) for i in range(10)])
RR=s.Matrix(10,2,lambda i,j:s.Rational((i+1)*(j+2),13)+(1 if i==j else 0))
P=RR.row_join(L);Q=s.diag(B,s.zeros(10))+P.T*C*P
change=s.eye(2).row_join(s.zeros(2,10)).col_join((-L.inv()*RR).row_join(L.inv()))
ck('full_coupled_hessian_diagonalizes',s.simplify(change.T*Q*change-s.diag(B,C))==s.zeros(12))
j=s.Matrix([s.Rational(i+1,7) for i in range(10)]);r=s.Matrix([s.Rational(11-i,9) for i in range(10)])
source=P.T*j;readout=P.T*r
ck('metric_conjugate_source_transforms',s.simplify(change.T*source-s.zeros(2,1).col_join(j))==s.zeros(12,1))
response=s.simplify((readout.T*Q.inv()*source)[0]);intrinsic=s.simplify((r.T*C.inv()*j)[0])
ck('full_induced_response_equals_intrinsic_response',response==intrinsic)
bulk_readout=s.eye(12)[:,0]
ct('dropping_ambient_source_changes_general_response',s.simplify((bulk_readout.T*Q.inv()*(source-s.zeros(2,1).col_join(L.T*j)))[0])!=0)
ck('intrinsic_readout_can_be_blind_to_changed_bulk_source',s.simplify((readout.T*Q.inv()*s.zeros(2,1).col_join(L.T*j))[0])==intrinsic)
general=s.Matrix([s.Rational(i+2,5) for i in range(12)]);jk=L.T.inv()*general[2:,:];jb=general[:2,:]-RR.T*jk
ck('general_source_dual_chain',s.simplify(change.T*general-jb.col_join(jk))==s.zeros(12,1))
Csing=C.copy();Csing[9,9]=0
ct('free_receiver_does_not_remove_intrinsic_kernel',(s.diag(B,s.zeros(10))+P.T*Csing*P).rank()==11)
x=s.symbols('x');gamma=x+x*x/2;action=(gamma-1)**2/2
ct('off_shell_second_chain_term_cannot_be_dropped',s.diff(action,x,2).subs(x,0)==0 and s.diff(gamma,x).subs(x,0)**2==1)
# A fixed-origin stress remains a nonzero covector, and invertible L cannot erase it.
stress=trace.T
ct('nonzero_tension_fails_free_normal_Euler',L.T*stress!=s.zeros(10,1))
paths=['explorations/conditional-build/k2523-coupled-receiver-variation-2026-11-02.md','tests/channel-swings/k2523_coupled_receiver_variation_probe.py','lab/process/k2521-free-observer-receiver.json','lab/active-research/joe-directed/prediction-kickoff/matter-light-reciprocity-2026-10-27.md','explorations/k77-wave2-full-source-action-defect-localization-moving-section-ward-bv-2026-08-05.md']
report={'result':'K2523','exact_identity_groups':checks,'contrary_controls':controls,'scope':'Universal variational and distribution arguments in note; grouped finite exact identities here, not theorem totals. Independent ambient metric class only.','bending_symmetric_map_determinant':str(s.factor(M.det())),'full_graph_coefficient_rank':coeff.rank(),'finite_full_response':str(response),'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
pth=R/'lab/process/k2523-coupled-receiver-variation.json'
if '--write' in sys.argv:pth.write_text(json.dumps(report,indent=2)+'\n')
else:
 saved=json.loads(pth.read_text());ck('saved_report_consistency',saved==report)
print('K2523 PASS',len(checks),'exact identity groups',len(controls),'contrary controls')
