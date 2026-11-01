"""Original positive-visibility instrument, strict recovery gain and full-error bounds."""
from pathlib import Path
import sympy as s
import contextlib,io,json,hashlib,sys
R=Path(__file__).resolve().parents[2];p=R/'tests/channel-swings/k2413_joint_recovery_optimum_probe.py';ns={'__file__':str(p),'__name__':'inherited'};argv=sys.argv;sys.argv=[str(p),'--verify-only']
with contextlib.redirect_stdout(io.StringIO()):exec(compile(p.read_text(),str(p),'exec'),ns)
sys.argv=argv;base=ns['ns'];Q=s.Rational;I,X,Y,Z=[base[k] for k in ['I','X','Y','Z']];choi,psd,ptr,simp,prep=[base[k] for k in ['choi','psd','ptr','simp','prep']]
checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
t=base['t'];G=base['G'];U=base['U'];ee=Q(19,100);nu=Q(1,2);unit=I
ck('rounded_decoder_feasible',t.dot(t)<(1-ee)**2)
def decoder(op):return ee*op+prep(t,op)-ee*s.trace(op)*I/2
jd=choi(decoder);ck('decoder_original_Choi_CP_TP',psd(jd) and ptr(jd)==I)
# Exact universal polynomial identity, independent of the fixture.
a,b,c,d,w,eps,q11,q12,q22=s.symbols('a b c d w eps q11 q12 q22',real=True);C=s.Matrix([[a,b],[c,d]]);M=s.Matrix([[q11,q12],[q12,q22]]);C1=C-eps*w*M
L=lambda B:s.trace(B)**2+(B[0,1]-B[1,0])**2
ck('PSD_moment_changes_only_trace',s.expand(L(C1)-L(C)+2*eps*w*s.trace(M)*s.trace(C)-eps**2*w**2*s.trace(M)**2)==0)
# For nonsymmetric X, conformal length is bounded by nuclear norm. Test exact
# singular-value identity supporting the general proof in the note.
ck('conformal_length_vs_frobenius_det',s.expand(L(C)-(sum(z*z for z in C)+2*C.det()))==0)
controls_full=[];errors=[];losses=base['weights'];means=base['means'];V=base['V'];Jid=base['Jid'];lower0=Q(5194114591,10**10)
for j,(m,w,norm) in enumerate(zip(means,losses,base['norms'])):
 axis=m/norm;probs=[(1+norm)/2,(1-norm)/2];axes=[axis,-axis]
 moment=sum((pr*nu*n*n.T for pr,n in zip(probs,axes)),s.zeros(2));h=sum((pr*nu*n for pr,n in zip(probs,axes)),s.zeros(2,1))
 ck('physical_second_moment_'+str(j),moment==nu*axis*axis.T and s.trace(moment)==nu and h==nu*m)
 def block(op,sg):
  rr=s.Matrix([s.trace(op*X),s.trace(op*Z)]);val=s.zeros(2)
  for pr,n in zip(probs,axes):
   prob=(s.trace(op)+sg*n.dot(rr))/2;state=(I+nu*(n[0]*X+n[1]*Z))/2;val+=pr*prob*state
  return simp(val)
 for sg in [-1,1]:ck('original_sign_block_CP_%s_%s'%(j,sg),psd(choi(lambda op:block(op,sg))))
 ck('original_sign_blocks_TP_'+str(j),ptr(choi(lambda op:block(op,1)+block(op,-1)))==I)
 def bad(op):return simp(decoder(block(op,1))+Y*decoder(block(op,-1))*Y)
 def full(op):return simp((1-w)*U*op*U.H+w*bad(op))
 jf=choi(full);ck('original_full_CP_TP_'+str(j),psd(jf) and ptr(jf)==I)
 B=t*m.T+ee*moment;T=(1-w)*G+w*B;C=I-T;d=w;L2=L(C);H2=(C[0,0]-C[1,1])**2+(C[0,1]+C[1,0])**2
 for k,op in enumerate([I/2,X,Y,Z]):
  rr=s.Matrix([s.trace(op*X),s.trace(op*Z)]);v=T*rr
  expect=(s.trace(op)*I+v[0]*X+(1-w)*s.trace(op*Y)*Y+v[1]*Z)/2
  ck('original_affine_composition_%s_%s'%(j,k),simp(full(op)-expect)==s.zeros(2))
 D=simp(V.T*(Jid-jf)*V/2);inds=[(0,3),(1,2)];b0=D.extract(inds[0],inds[0]);b1=D.extract(inds[1],inds[1])
 ck('complete_Bell_blocks_'+str(j),all(D[a,b]==0 for a in inds[0] for b in inds[1]) and s.trace(b0)==d and s.trace(b1)==-d and s.trace(b0)**2-4*b0.det()==L2 and s.trace(b1)**2-4*b1.det()==H2)
 ck('complete_branch_margins_'+str(j),H2<d*d<L2 and b0.det()<0 and b1.det()>0)
 # Certified rational complete error upper bound, stronger than the uniform theorem.
 upper=Q(51,100);ck('whole_error_below_51_percent_'+str(j),(4*upper-w)>0 and L2<(4*upper-w)**2)
 ck('gain_over_zero_visibility_optimum_'+str(j),upper<lower0-Q(1,200))
 Czero=I-(1-w)*G-w*t*m.T
 ctrl('preparation_only_discards_visibility_'+str(j),L(Czero)>L2)
 ctrl('replacing_Q_with_nu_identity_changes_actual_map_'+str(j),moment!=nu*I)
 errors.append({'law':j,'L_squared':str(L2),'H_squared':str(H2),'complete_upper':'51/100','moment':[[str(v) for v in row] for row in moment.tolist()]});controls_full.append(jf)
# Universal fixed-translation scalar-family derivative numerator.
tr0,sk,ev,ww,qq=s.symbols('tr0 sk ev ww qq',real=True)
rad=(tr0-ev*ww*qq)**2+sk**2
ck('full_scalar_family_derivative',s.expand(s.diff(rad,ev)+2*ww*qq*(tr0-ev*ww*qq))==0)
# Exact boundary fixture: ||t||=4/5 gives maximal mixing1/5.
tfamily=s.Matrix([Q(4,5),0]);efamily=Q(1,5)
ck('scalar_family_boundary_CPTP',psd(choi(lambda op:efamily*op+prep(tfamily,op)-efamily*s.trace(op)*I/2)))
ctrl('scalar_family_above_boundary_not_CP',not psd(choi(lambda op:Q(21,100)*op+prep(tfamily,op)-Q(21,100)*s.trace(op)*I/2)))
# Finite exact interval proof of the inherited algebraic constants used by the
# uniform positive-visibility theorem (not sampling the visibility domain).
ck('algebraic_translation_radius',base['normupper']<Q(13,20)<Q(81,100)**2)
ck('uniform_branch_lower_margin',4*ns['lo']-Q(219,100)*max(losses)>0)
ck('uniform_gain_coefficient',Q(19,100)*(Q(238,100)-Q(19,100))*Q(7,10)**2/16>Q(1,100))
ck('weights_above_seven_tenths',all(w>Q(7,10) for w in losses))
# A complete law mixture must use the full channels, preserving one controller.
lam=Q(2,5);jm=lam*controls_full[0]+(1-lam)*controls_full[1]
ck('complete_instrument_convex_hull_CP_TP',psd(jm) and ptr(jm)==I)
Vcost=sum(pp*wi*nu for pp,wi in zip(base['p'],losses));lower=ns['lo']-Vcost/4
ck('positive_visibility_lower_bound',Q(2,5)<lower<Q(51,100))
# Positivity itself bounds scalar identity mixing by 1-||t||. A planted larger
# value maps the aligned pure input outside the ball and its Choi is not CP.
wrong=Q(1,4)
ctrl('excess_identity_component_not_CP',not psd(choi(lambda op:wrong*op+prep(t,op)-wrong*s.trace(op)*I/2)))
# Released-capacity follow-through: rational anisotropic damping beats the
# best scalar decoder at the SAME fixed translation and good rotation.
ta=s.Matrix([Q(4,5),0]);Aani=s.diag(Q(1,5),Q(2,5))
def anisotropic(op):
 rr=s.Matrix([s.trace(op*X),s.trace(op*Z)]);v=s.trace(op)*ta+Aani*rr
 return (s.trace(op)*I+v[0]*X+Q(2,5)*s.trace(op*Y)*Y+v[1]*Z)/2
ja=choi(anisotropic);ck('anisotropic_original_Choi_CP_TP',psd(ja) and ptr(ja)==I)
aniso=[]
for j,(m,w,norm) in enumerate(zip(means,losses,base['norms'])):
 axis=m/norm;moment=nu*axis*axis.T
 def jb(op,sg):
  rr=s.Matrix([s.trace(op*X),s.trace(op*Z)]);value=s.zeros(2)
  for pr,nn in [((1+norm)/2,axis),((1-norm)/2,-axis)]:
   value+=pr*(s.trace(op)+sg*nn.dot(rr))/2*(I+nu*(nn[0]*X+nn[1]*Z))/2
  return simp(value)
 def fa(op):return simp((1-w)*U*op*U.H+w*(anisotropic(jb(op,1))+Y*anisotropic(jb(op,-1))*Y))
 jf=choi(fa);ck('anisotropic_complete_Choi_CP_TP_'+str(j),psd(jf) and ptr(jf)==I)
 C=I-(1-w)*G-w*(ta*m.T+Aani*moment);L2=L(C);H2=(C[0,0]-C[1,1])**2+(C[0,1]+C[1,0])**2
 D=simp(V.T*(Jid-jf)*V/2);b0=D.extract((0,3),(0,3));b1=D.extract((1,2),(1,2))
 ck('anisotropic_original_Bell_norm_'+str(j),s.trace(b0)==w and s.trace(b1)==-w and s.trace(b0)**2-4*b0.det()==L2 and s.trace(b1)**2-4*b1.det()==H2 and H2<w*w<L2 and all(D[a,b]==0 for a in (0,3) for b in (1,2)))
 upper=Q(487,1000);ck('anisotropic_whole_error_upper_'+str(j),4*upper-w>0 and L2<(4*upper-w)**2)
 Cs=I-(1-w)*G-w*(ta*m.T+Q(1,5)*moment);Ls=L(Cs);Hs=(Cs[0,0]-Cs[1,1])**2+(Cs[0,1]+Cs[1,0])**2
 ck('best_same_translation_scalar_error_above_half_'+str(j),Hs<w*w<Ls and Ls>(2-w)**2)
 ctrl('isotropic_substitution_loses_gain_'+str(j),Ls>L2)
 aniso.append({'L_squared':str(L2),'H_squared':str(H2),'best_scalar_L_squared':str(Ls),'upper':'487/1000'})
ck('anisotropic_implementation_allowance',Q(487,1000)+Q(1,1000)<Q(1,2))
# Positivity of opposite inputs gives the universal translation-linear coupling.
tx,tz,ax,az=s.symbols('tx tz ax az',real=True)
ck('opposite_input_average_identity',s.expand(((tx+ax)**2+(tz+az)**2+(tx-ax)**2+(tz-az)**2)/2-(tx**2+tz**2+ax**2+az**2))==0)
report={'result_id':'K2416','checks':checks,'controls':controls,'inherited_checks':len(ns['checks']),'inherited_original_checks':len(base['checks']),'fixtures':errors,'new_optimum_outer_bracket':[str(lower),'487/1000'],'anisotropic_fixtures':aniso,'uniform_strict_gain':'min(trace(Q1),trace(Q2))/100 with algebraic tstar, epsilon=19/100','scope':'Positive-visibility upper construction and all-CPTP lower bound; exact new optimum unresolved. Physical moments must preserve the supplied means.'}
deps=['tests/channel-swings/k2413_joint_recovery_optimum_probe.py','tests/channel-swings/k2410_variable_loss_recovery_probe.py','lab/process/k2413-joint-recovery-optimum.json','lab/process/k2410-variable-loss-recovery.json','explorations/conditional-build/k2398-uncertain-clock-law-recovery-2026-10-31.md']
report['dependencies']={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps};out=R/'lab/process/k2416-positive-visibility-recovery.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
elif '--verify-only' not in sys.argv:assert json.loads(out.read_text())==report
print(json.dumps({'checks':len(checks),'controls':len(controls),'status':'pass'}))
