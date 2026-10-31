"""Exact non-mirror uncertainty, physical-channel and minimax-threshold fixtures."""
from pathlib import Path
import importlib.util,json,hashlib,sys
import sympy as s
R=Path(__file__).resolve().parents[2];p=R/'tests/channel-swings/k2398_uncertain_clock_law_recovery_probe.py';sp=importlib.util.spec_from_file_location('old',p);old=importlib.util.module_from_spec(sp);sp.loader.exec_module(old)
Q=s.Rational;I,X,Y,Z=old.I,old.X,old.Y,old.Z;pa=[X,Y,Z];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
means=[s.Matrix([Q(1,2),0]),s.Matrix([Q(3,10),Q(2,5)]),s.Matrix([Q(3,10),-Q(1,5)])];M=s.eye(2)/2;nu=Q(1,4);axes=[s.Matrix([1,0]),s.Matrix([-1,0]),s.Matrix([0,1]),s.Matrix([0,-1])]
for j,m in enumerate(means):
 probs=[Q(1,4)+m[0]/2,Q(1,4)-m[0]/2,Q(1,4)+m[1]/2,Q(1,4)-m[1]/2]
 ck('law_'+str(j),all(w>=0 for w in probs) and sum(probs)==1 and sum((w*a for w,a in zip(probs,axes)),s.zeros(2,1))==m and sum((w*a*a.T for w,a in zip(probs,axes)),s.zeros(2))==M)
 ck('moment_positivity_'+str(j),old.psd(M-m*m.T))
ck('triangle_no_reflection',len(set((means[i]-means[j]).dot(means[i]-means[j]) for i,j in [(0,1),(0,2),(1,2)]))==3)
closest=means[1]/3+2*means[2]/3
ck('closest_mean',closest==s.Matrix([Q(3,10),0]) and all(m[0]>=Q(3,10) for m in means))
vcrit=3*s.sqrt(2)/10
ck('threshold_equality',old.psd(vcrit**2*M-closest*closest.T) and (vcrit**2*M-closest*closest.T).det()==0)
ck('threshold_above',old.psd(Q(1,2)**2*M-closest*closest.T))
ck('threshold_below',Q(1,4)**2/2<Q(9,100))
# Identity criterion is exactly K2395's spectral condition by Cayley-Hamilton.
a,b,c,v=s.symbols('a b c v',real=True);MM=s.Matrix([[a,b],[b,1-a]])
ck('trace_one_Cayley_Hamilton',s.simplify(MM*MM+MM.det()*s.eye(2)-MM)==s.zeros(2))
cc=xx=Q(12,25);yy=Q(3,5);zz=Q(4,5)
def decoder(op):
 tr=s.trace(op);rv=[s.trace(op*P) for P in pa]
 return s.simplify((tr*I+(cc*tr+xx*rv[0])*X+yy*rv[1]*Y+zz*rv[2]*Z)/2)
J=old.choi_apply(decoder);ck('decoder_CP_TP_rank2',old.psd(J) and old.ptr(J)==I and J.rank()==2)
def blocks(op,sign,m,Qm):
 rv=s.Matrix([s.trace(op*X),s.trace(op*Z)]);tr=s.trace(op);out=Qm*rv*sign
 # Conditional pointer mean E[v_axis n] need not equal v*m for variable visibility;
 # supply that mean separately in the caller below when needed.
 out=out+nu*m*tr
 return s.simplify(((tr+sign*m.dot(rv))*I+out[0]*X+out[1]*Z)/4)
def recovered(op,m):return s.simplify(decoder(blocks(op,1,m,nu*M))+Y*decoder(blocks(op,-1,m,nu*M))*Y)
values=[];skews=[];radicals=[];jid=old.choi_apply(lambda op:op)
for j,m in enumerate(means):
 B=s.Matrix([cc,0])*m.T+nu*s.diag(xx,zz)*M;f=s.trace(B);k=B[0,1]-B[1,0];rad=(2-f)**2+k*k;values.append(f);skews.append(k);radicals.append(rad)
 for h,op in enumerate([I/2,X,Y,Z]):
  rv=s.Matrix([s.trace(op*X),s.trace(op*Z)]);out=B*rv
  ck('original_sign_composition_%s_%s'%(j,h),s.simplify(recovered(op,m)-(s.trace(op)*I+out[0]*X+out[1]*Z)/2)==s.zeros(2))
 for sign in [-1,1]:ck('instrument_CP_%s_%s'%(j,sign),old.psd(old.choi_apply(lambda op:blocks(op,sign,m,nu*M))))
 jr=old.choi_apply(lambda op:recovered(op,m));ck('recovered_CP_TP_'+str(j),old.psd(jr) and old.ptr(jr)==I)
 ck('independent_Bell_norm_'+str(j),s.simplify(old.trace_norm_hermitian(jid-jr)/4-(1+s.sqrt(rad))/4)==0)
ck('endpoint_trace_and_skew',values==[Q(2,5),Q(38,125),Q(38,125)] and skews==[0,Q(24,125),-Q(12,125)])
ck('strict_nonlinear_uniform_gain',max(radicals)==Q(45520,15625) and max(radicals)<Q(49,16))
# Two actual convex mixtures verify the affine receiver and norm bound directly.
for weights in [(Q(1,3),)*3,(0,Q(1,3),Q(2,3))]:
 m=sum((w*mm for w,mm in zip(weights,means)),s.zeros(2,1));B=s.Matrix([cc,0])*m.T+nu*s.diag(xx,zz)*M
 ck('mixture_'+str(weights),s.simplify((2-s.trace(B))**2+(B[0,1]-B[1,0])**2)<=max(radicals))
ctrl('dropping_skew_understates_error',radicals[1]>(2-values[1])**2)
# SO(2) covariance admits a genuine unitary quarter-turn of the plane.
Jp=s.Matrix([[0,-1],[1,0]]);angle=s.symbols('theta',real=True);rot=s.Matrix([[s.cos(angle),-s.sin(angle)],[s.sin(angle),s.cos(angle)]])
ctrl('SO2_does_not_imply_symmetric_planar_block',s.simplify(Jp*rot-rot*Jp)==s.zeros(2) and Jp!=Jp.T)
# Orientation threshold examples with physical four-axis laws.
for beta,cosbeta in [(0,1),(s.pi/3,Q(1,2)),(s.pi/2,0),(s.pi,0)]:
 ck('arc_threshold_'+str(beta),s.sqrt(2)*Q(1,2)*max(s.cos(beta),0)==s.sqrt(2)*Q(1,2)*cosbeta)
ck('cyclic_zero_mean',sum((Jp**j*means[0] for j in range(4)),s.zeros(2,1))==s.zeros(2,1))
# Verify the constructive gain bound's algebra (the inequality premises are proved).
al,d,k,Delta=s.symbols('a d k Delta',real=True)
ck('mixture_radial_expansion',s.expand((al-Delta*d)**2+Delta**2*k*k-al**2+2*al*Delta*d-Delta**2*(d*d+k*k))==0)
# Variable trace: construct actual axis/visibility instruments at both endpoints.
def prep(op):return s.trace(op)*(I+X)/2
def mixdec(op):return (op+prep(op))/2
ck('variable_trace_decoder_CP_TP',old.psd(old.choi_apply(mixdec)) and old.ptr(old.choi_apply(mixdec))==I)
variable=[(s.zeros(2,1),s.eye(2)/2,s.zeros(2,1)),(s.Matrix([1,0]),s.zeros(2),s.zeros(2,1))]
for idx,(m,Qm,vmean) in enumerate(variable):
 def block(op,sign):
  rv=s.Matrix([s.trace(op*X),s.trace(op*Z)]);tr=s.trace(op);oo=vmean*tr+sign*Qm*rv
  return s.simplify(((tr+sign*m.dot(rv))*I+oo[0]*X+oo[1]*Z)/4)
 for sign in [-1,1]:ck('variable_trace_instrument_CP_%s_%s'%(idx,sign),old.psd(old.choi_apply(lambda op:block(op,sign))))
 fn=lambda op:s.simplify(mixdec(block(op,1))+Y*mixdec(block(op,-1))*Y)
 jj=old.choi_apply(fn);ck('variable_trace_exact_recovery_'+str(idx),old.psd(jj) and old.ptr(jj)==I and old.trace_norm_hermitian(jid-jj)/4==Q(5,8))
ctrl('zero_mean_variable_trace_inference_false',Q(5,8)<Q(3,4))
# Outcome-released exact minimax of the variable-trace physical segment.
ystar=(9-s.sqrt(33))/6;zstar=s.sqrt(ystar);xstar=ystar*zstar;cstar=zstar*(1+ystar)/2
ck('variable_optimal_root',s.simplify(3*ystar**2-9*ystar+4)==0 and bool(0<ystar<1))
ck('variable_optimal_CP_identity',s.simplify(cstar**2-(1-ystar**2)*(1-zstar**2))==0)
ck('variable_optimal_equalizer',s.simplify(cstar-(xstar+zstar)/2)==0)
ck('variable_optimal_c_square',s.simplify(cstar**2-(69-11*s.sqrt(33))/18)==0)
ck('variable_optimal_strict_gain',bool(cstar**2>Q(1,4)))
def optdec(op):
 tr=s.trace(op);rv=[s.trace(op*P) for P in pa]
 return s.simplify((tr*I+(cstar*tr+xstar*rv[0])*X+ystar*rv[1]*Y+zstar*rv[2]*Z)/2)
jo=old.choi_apply(optdec)
ck('variable_optimal_actual_Choi_CP_TP',old.psd(jo) and old.ptr(jo)==I and jo.rank()==2)
for idx,(m,Qm,vmean) in enumerate(variable):
 def block2(op,sign):
  rv=s.Matrix([s.trace(op*X),s.trace(op*Z)]);tr=s.trace(op);oo=vmean*tr+sign*Qm*rv
  return ((tr+sign*m.dot(rv))*I+oo[0]*X+oo[1]*Z)/4
 fn=lambda op:s.simplify(optdec(block2(op,1))+Y*optdec(block2(op,-1))*Y)
 B=Qm*s.diag(xstar,zstar)+s.Matrix([cstar,0])*m.T
 for h,op in enumerate([I/2,X,Y,Z]):
  rv=s.Matrix([s.trace(op*X),s.trace(op*Z)]);oo=B*rv
  ck('variable_optimal_original_composition_%s_%s'%(idx,h),s.simplify(fn(op)-(s.trace(op)*I+oo[0]*X+oo[1]*Z)/2)==s.zeros(2))
 ck('variable_optimal_endpoint_trace_'+str(idx),s.simplify(s.trace(B)-cstar)==0 and B==B.T)
# Full CP envelope and equalizer are universal symbolic identities;
# the note proves maximality/monotonicity on the declared interval.
cy=s.symbols('cy',real=True)
ck('variable_support_derivative_monotonicity',s.factor(s.diff((1+cy)*(1-cy)**2,cy))==(cy-1)*(3*cy+1))
ctrl('old_simple_mixture_not_optimal',bool(cstar>Q(1,2)))
report={'result_id':'K2404','checks':checks,'controls':controls,'evidence_kind':'exact symbolic/matrix fixtures; universal criterion uses compact minimax, pointwise theorem and physical-mixture proof','sharp_fixture_threshold':str(vcrit),'fixture_worst_error':str((1+s.sqrt(Q(45520,15625)))/4),'fixture_gain':str(Q(11,16)-(1+s.sqrt(Q(45520,15625)))/4),'variable_trace_identity_error':'3/4','variable_trace_improved_error':'5/8','variable_trace_exact_optimum':str((3-cstar)/4),'dependencies':{pp:hashlib.sha256((R/pp).read_bytes()).hexdigest() for pp in ['tests/channel-swings/k2398_uncertain_clock_law_recovery_probe.py','explorations/conditional-build/k2395-planar-recovery-closed-form-2026-10-31.md','lab/process/k2395-planar-recovery-closed-form.json','lab/process/k2401-positive-visibility-minimax-recovery.json']}}
p=R/'lab/process/k2404-rotation-uncertain-recovery.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==report
print(json.dumps(report,sort_keys=True))
