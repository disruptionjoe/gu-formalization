"""Exact original-channel fixture; universal all-CPTP proofs are in the note."""
from pathlib import Path
from itertools import combinations
import sympy as s
import json, hashlib, sys
R=Path(__file__).resolve().parents[2]; Q=s.Rational
I=s.eye(2); X=s.Matrix([[0,1],[1,0]]); Y=s.Matrix([[0,-s.I],[s.I,0]]); Z=s.diag(1,-1)
checks={}; controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v: raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v: raise AssertionError(k)
def simp(M): return M.applyfunc(s.simplify)
def choi(fn):
 J=s.zeros(4)
 for i in range(2):
  for j in range(2):
   E=s.zeros(2); E[i,j]=1; J+=s.kronecker_product(fn(E),E)
 return simp(J)
def ptr(J): return simp(J[:2,:2]+J[2:,2:])
def psd(M):
 return M==M.H and all(s.simplify(M.extract(ix,ix).det())>=0 for k in range(1,M.rows+1) for ix in combinations(range(M.rows),k))
def prep(t,op): return s.trace(op)*(I+t[0]*X+t[1]*Z)/2
means=[s.Matrix([Q(125,338),Q(150,169)]),s.Matrix([Q(49,250),-Q(84,125)])]
weights=[Q(73,100),Q(37,52)]; radii=[Q(24,13),Q(48,25)]
dirs=[(Q(12,13),Q(5,13)),(Q(24,25),-Q(7,25))]
p=[Q(259,624),Q(365,624)]; t0=s.Matrix([Q(4,5),0]); E0=Q(2701,5200)
eps=Q(1,180); co=(1-eps**2)/(1+eps**2); si=2*eps/(1+eps**2)
t=s.Matrix([Q(160093,200000),Q(34157,10000000)]); U=(I-s.I*eps*Y)/s.sqrt(1+eps**2)
G=s.Matrix([[co,si],[-si,co]])
ck('good_unitary',simp(U*U.H)==I)
Jgood=choi(lambda op:U*op*U.H)
ck('good_actual_Choi_CP_TP',psd(Jgood) and ptr(Jgood)==I)
ck('bad_preparation_norm',t.dot(t)==Q(64075588323149,100000000000000) and t.dot(t)<1)
Jprep=choi(lambda op:prep(t,op))
ck('bad_actual_Choi_CP_TP',psd(Jprep) and ptr(Jprep)==I)
ck('positive_dual_weights',all(x>0 for x in p) and sum(p)==1)
ck('weighted_rotation_cancellation',sum(pp*w*b for pp,w,(_,b) in zip(p,weights,dirs))==0)
ck('unweighted_rotation_does_not_cancel',sum(pp*b for pp,(_,b) in zip(p,dirs))!=0)
# Unnormalized Bell vectors, ordered Phi+, Phi-, Psi+, Psi-.
V=s.Matrix([[1,1,0,0],[0,0,1,1],[0,0,1,-1],[1,-1,0,0]])
ck('Bell_basis_normalization',V.T*V==2*s.eye(4))
Jid=choi(lambda op:op); gaps=[]; safe=[]; complete=[]; bads=[]
for j,(m,w,rr,(aa,bb)) in enumerate(zip(means,weights,radii,dirs)):
 rho=[Q(25,26),Q(7,10)][j]; axis=m/rho; prob=(1+rho)/2
 ck('actual_physical_axis_law_'+str(j),axis.dot(axis)==1 and 0<prob<1 and (2*prob-1)*axis==m)
 def block(op,sgn):
  rv=s.Matrix([s.trace(op*X),s.trace(op*Z)])
  return (s.trace(op)+sgn*m.dot(rv))*I/4
 for sg in [-1,1]: ck('sign_instrument_CP_%s_%s'%(j,sg),psd(choi(lambda op:block(op,sg))))
 ck('sign_instrument_TP_'+str(j),ptr(choi(lambda op:block(op,1)+block(op,-1)))==I)
 f0=t0.dot(m); k0=t0[0]*m[1]-t0[1]*m[0]
 ck('baseline_support_direction_'+str(j),(2-f0)==rr*aa and k0==rr*bb and aa**2+bb**2==1)
 ck('baseline_global_gradient_'+str(j),-aa*m[0]+bb*m[1]==0 and -aa*m[1]-bb*m[0]==-2*bb/t0[0])
 ck('baseline_equal_error_'+str(j),w*(1+rr)/4==E0)
 # Check the affine support identity, not just the derivative at one point.
 tx,tz=s.symbols('tx tz',real=True)
 ell=aa*(2-tx*m[0]-tz*m[1])+bb*(tx*m[1]-tz*m[0])
 ck('global_affine_support_'+str(j),s.expand(w*(1+ell)/4-E0+w*bb*tz/(2*t0[0]))==0)
 def bad(op): return simp(prep(t,block(op,1))+Y*prep(t,block(op,-1))*Y)
 def full(op): return simp((1-w)*U*op*U.H+w*bad(op))
 jb=choi(bad); jf=choi(full); bads.append(jb); complete.append(jf)
 ck('bad_composed_CP_TP_'+str(j),psd(jb) and ptr(jb)==I)
 ck('complete_composed_CP_TP_'+str(j),psd(jf) and ptr(jf)==I)
 B=t*m.T; T=(1-w)*G+w*B; C=s.eye(2)-T; d=w
 for k,op in enumerate([I/2,X,Y,Z]):
  rv=s.Matrix([s.trace(op*X),s.trace(op*Z)]); v=T*rv
  expected=(s.trace(op)*I+v[0]*X+(1-w)*s.trace(op*Y)*Y+v[1]*Z)/2
  ck('original_complete_composition_%s_%s'%(j,k),simp(full(op)-expected)==s.zeros(2))
 L2=s.trace(C)**2+(C[0,1]-C[1,0])**2
 H2=(C[0,0]-C[1,1])**2+(C[0,1]+C[1,0])**2
 ck('proper_SVD_determinant_'+str(j),C.det()>0)
 ck('triangle_upper_'+str(j),H2==w*w*t.dot(t)*m.dot(m) and H2<d*d)
 ck('triangle_lower_'+str(j),L2>d*d)
 # Independently derive the Bell-output blocks from original channel composition.
 D=simp(V.T*(Jid-jf)*V/2)
 inds=[(0,3),(1,2)]
 ck('actual_Bell_block_sparsity_'+str(j),all(D[a,b]==0 for a in inds[0] for b in inds[1]) and all(D[a,b]==0 for a in inds[1] for b in inds[0]))
 b0=D.extract(inds[0],inds[0]); b1=D.extract(inds[1],inds[1])
 ck('Bell_positive_block_trace_'+str(j),s.trace(b0)==d)
 ck('Bell_positive_block_discriminant_'+str(j),s.trace(b0)**2-4*b0.det()==L2)
 ck('Bell_negative_block_trace_'+str(j),s.trace(b1)==-d)
 ck('Bell_negative_block_discriminant_'+str(j),s.trace(b1)**2-4*b1.det()==H2)
 ck('Bell_inertia_one_positive_'+str(j),b0.det()<0 and b1.det()>0)
 # Those characteristic polynomials give norm(Jid-Jfull)=d+sqrt(L2).
 # Bell input divides unnormalized Choi by2; half trace distance divides by2 again.
 gap=(4*E0-w)**2-L2; gaps.append(gap); safe.append(gap/(8*(4*E0-w)))
 ck('strict_complete_gain_'+str(j),4*E0-w>0 and gap>0)
 deriv=bb*((1-w)-Q(2,5)*w)/2
 ck('strict_first_order_gain_'+str(j),deriv==[-Q(11,2600),-Q(7,13000)][j])
 # Incorrect good-rotation sign changes original complete error and loses gain.
 wrong=(2-2*(1-w)*co-w*t.dot(m))**2+(-2*(1-w)*si+w*(t[0]*m[1]-t[1]*m[0]))**2
 ctrl('reversed_good_rotation_changes_channel_'+str(j),wrong!=L2)
 if j==1: ctrl('reversed_good_rotation_loses_worst_case_gain',wrong>(4*E0-w)**2)
 ctrl('skew_cannot_be_dropped_'+str(j),L2>(2-2*(1-w)*co-w*t.dot(m))**2)
ck('pinned_exact_squared_gaps',gaps==[Q(4388891640853658579,35044921600000000000000),Q(111236783282109406331,876123040000000000000000)])
ck('usable_rational_implementation_margin',min(safe)>Q(1,100000))
# Physical convex mixture uses loss-weighted conditional means.
lam=Q(2,5); wm=lam*weights[0]+(1-lam)*weights[1]
mm=(lam*weights[0]*means[0]+(1-lam)*weights[1]*means[1])/wm
Bmix=t*mm.T; Tmix=(1-wm)*G+wm*Bmix
def mixformula(op):
 rv=s.Matrix([s.trace(op*X),s.trace(op*Z)]); vv=Tmix*rv
 return (s.trace(op)*I+vv[0]*X+(1-wm)*s.trace(op*Y)*Y+vv[1]*Z)/2
ck('actual_complete_instrument_convex_mixture',choi(mixformula)==lam*complete[0]+(1-lam)*complete[1])
ctrl('unweighted_conditional_mixture_is_wrong',mm!=lam*means[0]+(1-lam)*means[1])
ctrl('wrong_dual_weights_fail',sum(w*b for w,(_,b) in zip(weights,dirs))!=0)
ctrl('invalid_preparation_is_not_CP',not psd(choi(lambda op:prep(s.Matrix([1,1]),op))))
# Generic exact Pauli trace-norm identity in its three possible dominant regimes.
for j,(a,b,c) in enumerate([(Q(3,5),Q(2,5),Q(1,2)),(1,Q(1,5),Q(1,10)),(Q(1,5),Q(1,10),1),(0,0,0)]):
 a,b,c=map(s.sympify,(a,b,c))
 coeff=[(a+b+c)/4,(a-b-c)/4,(-a+b-c)/4,(-a-b+c)/4]
 ck('Pauli_norm_all_regimes_'+str(j),sum(abs(x) for x in coeff)/2==max(a+b+c,2*a,2*b,2*c)/4)
# Exact rational enclosures certify the algebraic optimum within good Y-axis
# unitary rotations, with arbitrary bad decoders reduced to preparation.
def iv(x): return (x,x)
def ia(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[1],-a[0])
def isu(a,b): return ia(a,neg(b))
def im(a,b):
 vals=[x*y for x in a for y in b];return (min(vals),max(vals))
def idiv(a,b):
 assert b[0]>0
 return im(a,(1/b[1],1/b[0]))
norms=[Q(25,26),Q(7,10)]
AA=[2*m/(w*n*n) for m,w,n in zip(means,weights,norms)]
BB=[(1-w)*a for w,a in zip(weights,AA)]
avec=AA[0]-AA[1]; bvec=BB[0]-BB[1]
an=(Q(6485025576372,10**12),Q(6485025576373,10**12))
bn=(Q(1822327939966,10**12),Q(1822327939967,10**12))
ck('restricted_optimizer_exact_sqrt_enclosures',an[0]**2<avec.dot(avec)<an[1]**2 and bn[0]**2<bvec.dot(bvec)<bn[1]**2)
co_opt=idiv(iv(avec.dot(bvec)),im(an,bn))
si_opt=idiv(iv(avec[0]*bvec[1]-avec[1]*bvec[0]),im(an,bn))
centers=[]
for a,b in zip(AA,BB):
 centers.append([isu(isu(iv(a[0]),im(co_opt,iv(b[0]))),im(si_opt,iv(b[1]))),ia(isu(iv(a[1]),im(co_opt,iv(b[1]))),im(si_opt,iv(b[0])))])
DD=isu(an,bn); al=[w*n for w,n in zip(weights,norms)]; den=iv(sum(al))
d1=idiv(ia(iv(weights[1]-weights[0]),im(iv(al[1]),DD)),den)
d2=isu(DD,d1)
topt=[idiv(ia(im(d2,centers[0][j]),im(d1,centers[1][j])),DD) for j in range(2)]
ck('restricted_optimizer_positive_distances',d1[0]>0 and d2[0]>0)
normupper=sum(max(abs(v[0]),abs(v[1]))**2 for v in topt)
ck('restricted_optimizer_preparation_feasible',normupper<Q(13,20))
ck('restricted_optimizer_exact_diamond_branch',al[0]*d1[0]>weights[0] and al[1]*d2[0]>weights[1])
valopt=idiv(ia(iv(weights[0]),im(iv(al[0]),d1)),iv(Q(4)))
ck('restricted_optimizer_value_enclosure',Q(5194114591,10**10)<valopt[0] and valopt[1]<Q(5194114592,10**10))

report={'result_id':'K2410','checks':checks,'controls':controls,'baseline_complete_optimum':str(E0),'squared_gaps':list(map(str,gaps)),'safe_complete_implementation_margin':str(min(safe)),'restricted_good_rotation_optimum_interval':['5194114591/10000000000','5194114592/10000000000'],'scope':'Exact original-channel CP/TP, composition, Bell-block and rational strict-gain checks. Universal norm, all-CPTP baseline, twelve-law and continuum results use written proofs and independent internal review.'}
deps=['explorations/conditional-build/k2398-uncertain-clock-law-recovery-2026-10-31.md','explorations/conditional-build/k2407-finite-minimax-certificates-2026-10-31.md']
report['dependencies']={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps}
pth=R/'lab/process/k2410-variable-loss-recovery.json'
if '--write' in sys.argv: pth.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
elif '--verify-only' not in sys.argv: assert json.loads(pth.read_text())==report
print(json.dumps(report,sort_keys=True))
