"""Exact physical channels and primal/dual fixture; universal proofs are in the note."""
from pathlib import Path
from itertools import combinations
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];Q=s.Rational
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);pa=[X,Y,Z]
checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def simp(M):return M.applyfunc(s.simplify)
def choi(fn):
 J=s.zeros(4)
 for i in range(2):
  for j in range(2):
   E=s.zeros(2);E[i,j]=1;J+=s.kronecker_product(fn(E),E)
 return simp(J)
def ptr(J):return simp(J[:2,:2]+J[2:,2:])
def psd(M):
 return M==M.H and all(s.simplify(M.extract(idx,idx).det())>=0 for k in range(1,M.rows+1) for idx in combinations(range(M.rows),k))
def normh(M):return s.simplify(sum(abs(x)*mult for x,mult in M.eigenvals().items()))
def dec(op):return (op+4*s.trace(op)*(I+X)/2)/5
J=choi(dec);ck('actual_decoder_CP_TP',psd(J) and ptr(J)==I)
means=[s.Matrix([Q(11,68),Q(27,68)]),s.Matrix([Q(1099,3604),-Q(3237,3604)]),s.Matrix([Q(1,4),Q(3,4)])]
p=[Q(1,4),Q(53,132),Q(23,66)];rad=3*s.sqrt(10)/5
ck('positive_normalized_dual_weights',all(z>0 for z in p) and sum(p)==1)
ck('dual_mean',sum((w*m for w,m in zip(p,means)),s.zeros(2,1))==s.Matrix([Q(1,4),0]))
ck('mean_norms',[(m.dot(m)) for m in means]==[Q(25,136),Q(6485,7208),Q(5,8)])
ck('scalene_triangle',len(set((means[i]-means[j]).dot(means[i]-means[j]) for i,j in combinations(range(3),2)))==3)
As=[];Bs=[];Ks=[];jid=choi(lambda op:op)
for k,m in enumerate(means+[s.Matrix([1,0])]):
 visible=k==3;qm=s.diag(1,0) if visible else s.zeros(2);hm=m if visible else s.zeros(2,1)
 moment=s.Matrix([[s.trace(qm),hm[0],hm[1]],[hm[0],qm[0,0],qm[0,1]],[hm[1],qm[1,0],qm[1,1]]])
 ck('physical_moment_cone_'+str(k),psd(moment) and (m-hm).dot(m-hm)<=(1-s.trace(qm))**2)
 if not visible:
  rho=s.sqrt(m.dot(m));axis=m/rho;pp=(1+rho)/2
  ck('actual_antipodal_law_'+str(k),0<=pp<=1 and s.simplify(axis.dot(axis))==1 and simp((2*pp-1)*axis)==m)
 def block(op,sgn):
  tr=s.trace(op);rv=s.Matrix([s.trace(op*X),s.trace(op*Z)]);out=hm*tr+sgn*qm*rv
  return simp(((tr+sgn*m.dot(rv))*I+out[0]*X+out[1]*Z)/4)
 for sg in [-1,1]:ck('instrument_CP_%s_%s'%(k,sg),psd(choi(lambda op:block(op,sg))))
 fn=lambda op:simp(dec(block(op,1))+Y*dec(block(op,-1))*Y)
 B=s.Matrix([Q(4,5),0])*m.T+qm/5;f=s.trace(B);sk=B[0,1]-B[1,0];rr=s.simplify((2-f)**2+sk**2)
 for j,op in enumerate([I/2,X,Y,Z]):
  rv=s.Matrix([s.trace(op*X),s.trace(op*Z)]);out=B*rv
  ck('original_sign_composition_%s_%s'%(k,j),simp(fn(op)-(s.trace(op)*I+out[0]*X+out[1]*Z)/2)==s.zeros(2))
 jr=choi(fn);ck('recovered_CP_TP_'+str(k),psd(jr) and ptr(jr)==I)
 ck('endpoint_radius_'+str(k),rr==(1 if visible else Q(18,5)))
 ck('Bell_norm_'+str(k),s.simplify(normh(jid-jr)/4-(1+s.sqrt(rr))/4)==0)
 if not visible:
  aa=(2-f)/rad;bb=sk/rad;As.append(aa);Bs.append(bb)
  ck('unit_direction_'+str(k),s.simplify(aa*aa+bb*bb)==1)
  # Q=0: f=t_x*m_x+t_z*m_z, k=t_x*m_z-t_z*m_x.
  cx=s.simplify(-aa*m[0]+bb*m[1]);cz=s.simplify(-aa*m[1]-bb*m[0])
  Ks.append(s.kronecker_product(cx*X+cz*Z,I)/2)
Kbar=simp(sum((w*K for w,K in zip(p,Ks)),s.zeros(4)))
ck('actual_Choi_dual_zero',Kbar==s.zeros(4))
ck('dual_value_equal_upper',s.simplify(2*sum(w*a for w,a in zip(p,As))-rad)==0)
ck('rotational_stationarity',s.simplify(sum(w*b for w,b in zip(p,Bs)))==0)
ck('fourth_endpoint_strict_slack',1<rad)
# Original formula at fixed rational real CPTP decoders verifies the Choi functional.
for j,(alpha,beta) in enumerate([(Q(1,3),Q(2,3)),(Q(1,2),0),(0,1)]):
 def testdec(op):return alpha*op+(1-alpha)*s.trace(op)*(I+beta*Z)/2
 jj=choi(testdec);ck('test_decoder_'+str(j),psd(jj) and ptr(jj)==I)
 for k,m in enumerate(means):
  t=s.Matrix([0,(1-alpha)*beta]);f=t.dot(m);sk=t[0]*m[1]-t[1]*m[0]
  ck('Choi_functional_%s_%s'%(j,k),s.simplify(s.trace(Ks[k]*jj)+As[k]*f-Bs[k]*sk)==0)
# Algebraic norm identity underlying the physical-net theorem.
a,b,c,d=s.symbols('a b c d',real=True);D=s.Matrix([[a,b],[c,d]])
ck('nuclear_norm_support_identity',s.expand((a+d)**2+(b-c)**2-s.trace(D.T*D)-2*D.det())==0)
# Full flagged Bell lower bound at actually composed arbitrary good channels.
for j,w in enumerate([Q(1,4),Q(2,3),1]):
 G=s.diag(Q(1,3),Q(2,3));gy=Q(1,2)
 # This Pauli channel is CP: all four Pauli probabilities nonnegative.
 def good(op):return (s.trace(op)*I+Q(1,3)*s.trace(op*X)*X+gy*s.trace(op*Y)*Y+Q(2,3)*s.trace(op*Z)*Z)/2
 ck('good_CP_TP_'+str(j),psd(choi(good)) and ptr(choi(good))==I)
 lower=w*(1+rad)/4+(1-w)*(1-gy+(rad/2)*(2-s.trace(G)))/4
 av=0
 for pi,m in zip(p,means):
  B=s.Matrix([Q(4,5),0])*m.T;T=(1-w)*G+w*B;Cy=1-(1-w)*gy
  diff=lambda op:(Cy*s.trace(op*Y)*Y+(s.eye(2)-T)[0,0]*s.trace(op*X)*X+(s.eye(2)-T)[0,1]*s.trace(op*Z)*X+(s.eye(2)-T)[1,0]*s.trace(op*X)*Z+(s.eye(2)-T)[1,1]*s.trace(op*Z)*Z)/2
  C=s.eye(2)-T;support=s.sqrt(s.trace(C)**2+(C[0,1]-C[1,0])**2)
  ck('complete_det_'+str((j,str(pi))),C.det()>=0)
  ck('complete_Bell_bound_'+str((j,str(pi))),s.simplify(normh(choi(diff))/4-(Cy+support)/4)>=0)
  av+=pi*(Cy+support)/4
 ck('complete_weighted_lower_'+str(j),s.simplify(av-lower)>=0)
ctrl('skew_term_is_essential',Q(18,5)>(2-Q(4,5)*means[0][0])**2)
ctrl('PSD_Q_trace_is_not_physical',not psd(s.Matrix([[1,1,0],[1,0,0],[0,0,1]])))
ctrl('law_dependent_rotations_change_objective',s.sqrt(means[0].dot(means[0]))>means[0][0])
ctrl('wrong_dual_weights_do_not_certify',simp(sum(Ks,s.zeros(4))/3)!=s.zeros(4))
deps=['tests/channel-swings/k2398_uncertain_clock_law_recovery_probe.py','explorations/conditional-build/k2404-rotation-uncertain-recovery-2026-10-31.md']
report={'result_id':'K2407','checks':checks,'controls':controls,'fixture_radius':'3*sqrt(10)/5','dual_weights':list(map(str,p)),'dual_matrix_zero':Kbar==s.zeros(4),'scope':'Exact finite original-channel and Choi checks. Universal physical moment, seven-law, flagged and covering theorems have written independently reviewed proofs.','dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps}}
pth=R/'lab/process/k2407-finite-minimax-certificates.json'
if '--write' in sys.argv:pth.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:assert json.loads(pth.read_text())==report
print(json.dumps(report,sort_keys=True))
