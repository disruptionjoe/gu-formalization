"""Exact all-CPTP dual and original positive-visibility instrument witnesses."""
from pathlib import Path
from itertools import combinations
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];Q=s.Rational;I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);paulis=[X,Z]
checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def simp(M):return M.applyfunc(s.cancel)
def choi(fn):
 ans=s.zeros(4)
 for i in range(2):
  for j in range(2):
   E=s.zeros(2);E[i,j]=1;ans+=s.kronecker_product(fn(E),E)
 return simp(ans)
def ptr(J):return simp(J[:2,:2]+J[2:,2:])
def minors(M):return [s.cancel(M.extract(ix,ix).det()) for k in range(1,M.rows+1) for ix in combinations(range(M.rows),k)]
def psd(M):return M==M.H and all(v>=0 for v in minors(M))
def rot(t):return s.Matrix([[(1-t*t)/(1+t*t),2*t/(1+t*t)],[-2*t/(1+t*t),(1-t*t)/(1+t*t)]])
def channel(t,A,b,op):
 rr=s.Matrix([s.trace(op*X),s.trace(op*Z)]);z=simp(s.trace(op)*t+A*rr)
 return simp((s.trace(op)*I+z[0]*X+z[1]*Z+b*s.trace(op*Y)*Y)/2)
means=[s.Matrix([Q(125,338),Q(150,169)]),s.Matrix([Q(49,250),-Q(84,125)])];weights=[Q(73,100),Q(37,52)];norms=[Q(25,26),Q(7,10)];moments=[m*m.T/(2*n*n) for m,n in zip(means,norms)]
p=[Q(263,500),Q(237,500)];Fs=[rot(-Q(1,21)),rot(Q(1,19))]
ck('dual_probability_and_unit_support',sum(p)==1 and all(v>0 for v in p) and all(F.T*F==I for F in Fs))
c0=1+2*sum(pi*F[0,0] for pi,F in zip(p,Fs));h=sum(pi*(1-w) for pi,w in zip(p,weights));S=sum((pi*(1-w)*F for pi,w,F in zip(p,weights,Fs)),s.zeros(2));r2=S[0,0]**2+S[0,1]**2
v=sum((pi*w*F*m for pi,w,F,m in zip(p,weights,Fs,means)),s.zeros(2,1));M=sum((pi*w*F*mm for pi,w,F,mm in zip(p,weights,Fs,moments)),s.zeros(2));H=sum((v[a]*s.kronecker_product(paulis[a],I) for a in range(2)),s.zeros(4))/2
H+=sum((M[a,b]*s.kronecker_product(paulis[a],paulis[b].T) for a in range(2) for b in range(2)),s.zeros(4))/2
Zd=Q(1851,10000)*I+Q(37,1000)*X+Q(59,1000)*Z;slack=s.kronecker_product(I,Zd)-H;mm=minors(slack)
ck('all15_exact_dual_principal_minors_positive',len(mm)==15 and all(v>0 for v in mm))
ru=Q(1387,5000);ck('good_support_radius_bound',r2==Q(6250334491593,81252031250000) and ru*ru>r2)
lower=s.cancel((c0-h-2*ru-s.trace(Zd))/4);ck('full_all_CPTP_lower_bound',lower==Q(1786296137,4000100000) and lower>Q(4465,10000))
# Derive the Choi functional identity on a generic affine map, independently.
tx,tz,a,b,c,d,by=s.symbols('tx tz a b c d by',real=True);tg=s.Matrix([tx,tz]);Ag=s.Matrix([[a,b],[c,d]]);jg=choi(lambda op:channel(tg,Ag,by,op))
ck('original_Choi_support_identity',s.expand(s.trace(H*jg)-v.dot(tg)-sum(M[i,j]*Ag[i,j] for i in range(2) for j in range(2)))==0)
ck('dual_trace_TP_identity',s.expand(s.trace(s.kronecker_product(I,Zd)*jg)-s.trace(Zd))==0)
ctrl('bad_dual_shift_loses_PSD',not psd(slack-Q(1,10)*s.eye(4)))
# A fully rational physical extreme channel, with proper input/output rotations.
u=Q(187,1000);vv=Q(29,48);aa=(1-u*u)/(1+u*u);sa=2*u/(1+u*u);bb=(1-vv*vv)/(1+vv*vv);sb=2*vv/(1+vv*vv)
ck('canonical_extreme_CP_identities',s.cancel((1+aa*bb)**2-(sa*sb)**2-(aa+bb)**2)==0 and s.cancel((1-aa*bb)**2-(sa*sb)**2-(aa-bb)**2)==0)
e=rot(Q(1,186)).T*s.Matrix([1,0]);RR=rot(-Q(1,31));tt=sa*sb*RR*e;AA=RR*(aa*I+(aa*bb-aa)*e*e.T);GG=rot(Q(1,272))
# Rotations preserve perpendicular coordinate; verify CP directly too.
Jbad=choi(lambda op:channel(tt,AA,bb,op));Jgood=choi(lambda op:channel(s.zeros(2,1),GG,1,op));ck('original_decoder_CP_TP',psd(Jbad) and ptr(Jbad)==I);ck('original_good_CP_TP',psd(Jgood) and ptr(Jgood)==I)
Bell=s.Matrix([[1,1,0,0],[0,0,1,1],[0,0,1,-1],[1,-1,0,0]]);Jid=choi(lambda op:op);results=[]
for j,(m,w,n,moment) in enumerate(zip(means,weights,norms,moments)):
 axis=m/n;ck('original_physical_law_'+str(j),axis.dot(axis)==1 and 0<n<1 and moment==axis*axis.T/2)
 def block(op,sg):
  rr=s.Matrix([s.trace(op*X),s.trace(op*Z)]);ans=s.zeros(2)
  for prob,ax in [((1+n)/2,axis),((1-n)/2,-axis)]:
   ans+=prob*(s.trace(op)+sg*ax.dot(rr))/2*(I+(ax[0]*X+ax[1]*Z)/2)/2
  return simp(ans)
 ck('original_instrument_CP_TP_'+str(j),psd(choi(lambda op:block(op,1))) and psd(choi(lambda op:block(op,-1))) and ptr(choi(lambda op:block(op,1)+block(op,-1)))==I)
 for name,t,A,y,G,upper in [('identity',s.zeros(2,1),I,1,I,Q(73,160)),('rational',tt,AA,bb,GG,Q(447,1000))]:
  def full(op):return simp((1-w)*channel(s.zeros(2,1),G,1,op)+w*(channel(t,A,y,block(op,1))+Y*channel(t,A,y,block(op,-1))*Y))
  jf=choi(full);B=t*m.T+A*moment;T=(1-w)*G+w*B;C=I-T;L2=s.trace(C)**2+(C[0,1]-C[1,0])**2;H2=(C[0,0]-C[1,1])**2+(C[0,1]+C[1,0])**2
  ck(name+'_original_full_CP_TP_'+str(j),psd(jf) and ptr(jf)==I)
  ck(name+'_original_full_composition_'+str(j),all(full(op)==channel(s.zeros(2,1),T,1-w,op) for op in [I/2,X,Y,Z]))
  D=simp(Bell.T*(Jid-jf)*Bell/2);i0=(0,3);i1=(1,2);b0=D.extract(i0,i0);b1=D.extract(i1,i1)
  ck(name+'_original_Bell_norm_'+str(j),all(D[a,b]==0 for a in i0 for b in i1) and s.trace(b0)==w and s.trace(b1)==-w and s.trace(b0)**2-4*b0.det()==L2 and s.trace(b1)**2-4*b1.det()==H2)
  ck(name+'_complete_norm_branch_'+str(j),H2<w*w<L2)
  if name=='identity':ck('identity_exact_error_'+str(j),L2==9*w*w/4 and H2==w*w/4 and 5*w/8<=upper)
  else:ck('rational_strict_upper_'+str(j),4*upper>w and L2<(4*upper-w)**2)
  results.append({'law':j,'controller':name,'L2':str(L2),'H2':str(H2),'upper':str(upper)})
ctrl('identity_improves_old_anisotropic_bound',Q(73,160)<Q(487,1000))
ctrl('nonzero_translation_with_identity_is_unphysical',not psd(choi(lambda op:channel(s.Matrix([Q(1,10),0]),I,1,op))))
ck('certified_gap_under_438_millionths',Q(447,1000)-lower<Q(438,10**6))
# Structural follow-through: conformal projection preserves L for arbitrary good block.
a0,b0,c0s,d0=s.symbols('ag bg cg dg',real=True);ww=s.symbols('w',nonnegative=True);xx,yy,zz,tt0=s.symbols('bx by bz bt',real=True)
G0=s.Matrix([[a0+c0s,b0+d0],[-b0+d0,a0-c0s]]);P0=s.Matrix([[a0,b0],[-b0,a0]]);B0=s.Matrix([[xx,yy],[zz,tt0]])
cc0=I-(1-ww)*G0-ww*B0;cc1=I-(1-ww)*P0-ww*B0
lf=lambda C:s.trace(C)**2+(C[0,1]-C[1,0])**2
ck('arbitrary_good_conformal_projection_preserves_L',s.expand(lf(cc0)-lf(cc1))==0)
# Physical interior rotation mixture and its dominating boundary unitary.
P=s.Matrix([[Q(3,10),Q(4,5)],[-Q(4,5),Q(3,10)]]);PU=s.Matrix([[Q(3,5),Q(4,5)],[-Q(4,5),Q(3,5)]])
ck('good_mixture_and_boundary_unitary_CP',psd(choi(lambda op:channel(s.zeros(2,1),P,1,op))) and psd(choi(lambda op:channel(s.zeros(2,1),PU,1,op))) and PU.T*PU==I)
for j,(w,B) in enumerate(zip(weights,moments)):
 c1=I-(1-w)*P-w*B;c2=I-(1-w)*PU-w*B
 ck('same_unitary_strictly_dominates_mixture_'+str(j),lf(c2)<lf(c1))
ck('loss_one_good_channel_irrelevant',s.simplify((I-(1-ww)*P-ww*B0).subs(ww,1)-(I-(1-ww)*PU-ww*B0).subs(ww,1))==s.zeros(2))
ctrl('opposite_circle_boundary_can_worsen_error',lf(I-PU)<lf(I+PU))
report={'result_id':'K2419','checks':checks,'controls':controls,'lower_bound':str(lower),'upper_bound':'447/1000','gap_upper':str(Q(447,1000)-lower),'dual':{'p':list(map(str,p)),'support_half_angles':['-1/21','1/19'],'Z':[[str(v) for v in row] for row in Zd.tolist()],'principal_minors':list(map(str,mm)),'good_radius_squared':str(r2)},'controller':{'t':list(map(str,tt)),'A':[[str(v) for v in row] for row in AA.tolist()],'y':str(bb),'G':[[str(v) for v in row] for row in GG.tolist()]},'original_channel_results':results,'good_channel_reduction':'One proper Y-axis unitary suffices for any uncertainty family of the stated physical planar instruments; proof in note.','scope':'Certified bracket over all shared good/bad CPTP recovery channels for the two supplied visibility-half laws and convex hull; not exact optimality, device calibration or native GU evidence.'}
deps=['tests/channel-swings/k2416_positive_visibility_recovery_probe.py','explorations/conditional-build/k2413-joint-recovery-optimum-2026-10-31.md'];report['dependencies']={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps};out=R/'lab/process/k2419-positive-visibility-dual.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
elif '--verify-only' not in sys.argv:assert json.loads(out.read_text())==report
print(json.dumps({'checks':len(checks),'controls':len(controls),'lower':str(lower),'upper':'447/1000','status':'pass'}))
