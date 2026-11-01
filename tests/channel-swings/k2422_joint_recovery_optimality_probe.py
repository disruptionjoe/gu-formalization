"""Exact joint recovery dual, gap identity and paired-law minimax controls."""
from pathlib import Path
import ast,json,hashlib,sys
import sympy as s
from itertools import combinations
R=Path(__file__).resolve().parents[2];Q=s.Rational;I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);paulis=[X,Z]
checks={};controls={}
def ck(name,value):
 checks[name]=bool(value)
 if not value:raise AssertionError(name)
def ctrl(name,value):
 controls[name]=bool(value)
 if not value:raise AssertionError(name)
p=R/'tests/channel-swings/k2419_positive_visibility_dual_probe.py';tree=ast.parse(p.read_text())
for node in tree.body:
 if isinstance(node,ast.FunctionDef) and node.name in ['simp','choi','ptr','minors','psd','rot','channel']:
  exec(compile(ast.Module(body=[node],type_ignores=[]),str(p),'exec'),globals())
def support(v,M):return simp((sum((v[a]*s.kronecker_product(paulis[a],I) for a in range(2)),s.zeros(4))+sum((M[a,b]*s.kronecker_product(paulis[a],paulis[b].T) for a in range(2) for b in range(2)),s.zeros(4)))/2)
def moment(law):return (sum((p*n for p,n,v in law),s.zeros(2,1)),sum((p*v*n*n.T for p,n,v in law),s.zeros(2)))
def block(law,op,sg):
 rr=s.Matrix([s.trace(op*X),s.trace(op*Z)]);out=s.zeros(2)
 for p,n,v in law:out+=p*(s.trace(op)+sg*n.dot(rr))/2*(I+v*(n[0]*X+n[1]*Z))/2
 return simp(out)
def full(law,w,t,A,b,G,op):return simp((1-w)*channel(s.zeros(2,1),G,1,op)+w*(channel(t,A,b,block(law,op,1))+Y*channel(t,A,b,block(law,op,-1))*Y))
Jid=choi(lambda op:op);Bell=s.Matrix([[1,1,0,0],[0,0,1,1],[0,0,1,-1],[1,-1,0,0]])
def norms(law,w,t,A,b,G):
 m,mm=moment(law);B=t*m.T+A*mm;C=I-(1-w)*G-w*B;ell=s.Matrix([s.trace(C),C[0,1]-C[1,0]]);L2=ell.dot(ell);H2=(C[0,0]-C[1,1])**2+(C[0,1]+C[1,0])**2
 jf=choi(lambda op:full(law,w,t,A,b,G,op));D=simp(Bell.T*(Jid-jf)*Bell/2);b0=D.extract((0,3),(0,3));b1=D.extract((1,2),(1,2))
 ck('original_full_channel_CP_TP',psd(jf) and ptr(jf)==I)
 ck('original_composition',all(full(law,w,t,A,b,G,op)==channel(s.zeros(2,1),I-C,1-w,op) for op in [I/2,X,Y,Z]))
 ck('original_Bell_blocks',all(D[a,b]==0 for a in (0,3) for b in (1,2)) and s.trace(b0)==w and s.trace(b1)==-w and s.trace(b0)**2-4*b0.det()==L2 and s.trace(b1)**2-4*b1.det()==H2)
 return ell,L2,H2
axes=[s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([Q(3,5),Q(4,5)])]
laws=[[(Q(3,4),axes[0],Q(1,2)),(Q(1,4),-axes[0],Q(1,2))],[(Q(2,5),axes[0],Q(1,3)),(Q(3,5),axes[1],Q(4,5))],[(Q(1,3),axes[2],1),(Q(2,3),axes[1],Q(1,4))]]
weights=[Q(7,10),Q(4,5),Q(3,4)];values=[];details=[]
for index,(law,w) in enumerate(zip(laws,weights)):
 ck('physical_law_'+str(index),sum(p for p,n,v in law)==1 and all(p>0 and n.dot(n)==1 and 0<=v<=1 for p,n,v in law))
 reverse=[(p,-n,v) for p,n,v in law];m,mm=moment(law);mr,mrQ=moment(reverse);tr=s.trace(mm)
 ck('opposite_mean_same_Q_'+str(index),mr==-m and mrQ==mm and psd(mm) and 0<=tr<=1)
 for label,law2 in [('plus',law),('minus',reverse)]:
  for sg in [-1,1]:ck('original_sign_CP_'+str(index)+label+str(sg),psd(choi(lambda op:block(law2,op,sg))))
  ell,L2,H2=norms(law2,w,s.zeros(2,1),I,1,I)
  ck('identity_complete_error_'+str(index)+label,L2==w*w*(2-tr)**2 and H2<=w*w<=L2)
 # Equal pair weights cancel translation, exact singular dual matches identity.
 H=support(s.zeros(2,1),w*mm);Zd=w*tr*I/2;D=s.kronecker_product(I,Zd)-H
 val=w*(3-tr)/4;dual=(w+2-2*(1-w)-s.trace(Zd))/4
 ck('paired_original_dual_PSD_'+str(index),psd(D))
 ck('paired_complementary_slackness_'+str(index),D*Jid==s.zeros(4) and dual==val)
 ck('paired_dual_trace_TP_'+str(index),s.trace(s.kronecker_product(I,Zd)*Jid)==s.trace(Zd))
 values.append(val);details.append({'law':index,'loss':str(w),'mean':list(map(str,m)),'moment':[[str(x) for x in row] for row in mm.tolist()],'optimum':str(val),'dual_slack_rank':D.rank()})
ck('variable_loss_family_exact_optimum',max(values)==Q(179,375))
# Central symmetry matters: a known deterministic axis can use constant decoding.
law=[(s.Integer(1),axes[0],Q(1,2))];w=Q(3,4);t=axes[0];Jconstant=choi(lambda op:channel(t,s.zeros(2),0,op));ck('constant_decoder_CP_TP',psd(Jconstant) and ptr(Jconstant)==I)
ell,L2,H2=norms(law,w,t,s.zeros(2),0,I)
ctrl('unpaired_law_beats_paired_formula',L2==w*w and H2==w*w and w/2<w*Q(5,8))
# Three active laws balance without any opposite-mean partner in the family.
tri_axes=[axes[0],axes[1],-axes[2]];tri_norm=[Q(3,8),Q(2,5),Q(3,5)];tri_v=[Q(1,2),s.Integer(1),Q(3,5)];tri_w=[Q(4,5),s.Integer(1),Q(5,6)];tri=[]
for n,r,vv,w0 in zip(tri_axes,tri_norm,tri_v,tri_w):
 law0=[((1+r)/2,n,vv),((1-r)/2,-n,vv)];tri.append(law0)
 el,ll,hh=norms(law0,w0,s.zeros(2,1),I,1,I)
 ck('balanced_three_original_error',ll==w0*w0*(2-vv)**2 and hh<=w0*w0<=ll and w0*(3-vv)/4==Q(1,2))
tri_m=[moment(l)[0] for l in tri];tri_Q=[moment(l)[1] for l in tri]
ck('active_weighted_means_balance',sum((w*m/3 for w,m in zip(tri_w,tri_m)),s.zeros(2,1))==s.zeros(2,1))
ck('three_laws_are_not_pairwise_antipodal',all(-m not in tri_m for m in tri_m))
Mtri=sum((w*q/3 for w,q in zip(tri_w,tri_Q)),s.zeros(2));Htri=support(s.zeros(2,1),Mtri);Ztri=s.trace(Mtri)*I/2;Dtri=s.kronecker_product(I,Ztri)-Htri
ck('balanced_three_matching_dual',psd(Dtri) and Dtri*Jid==s.zeros(4) and (sum(tri_w)-s.trace(Mtri))/4==Q(1,2))
# Exact gap decomposition on the actual asymmetric K2419 laws and its dual.
means=[s.Matrix([Q(125,338),Q(150,169)]),s.Matrix([Q(49,250),-Q(84,125)])];ws=[Q(73,100),Q(37,52)];lens=[Q(25,26),Q(7,10)];Qs=[m*m.T/(2*n*n) for m,n in zip(means,lens)]
ps=[Q(263,500),Q(237,500)];Fs=[rot(-Q(1,21)),rot(Q(1,19))];qs=[pi*s.Matrix([F[0,0],F[0,1]]) for pi,F in zip(ps,Fs)];ss=sum(((1-w)*q for w,q in zip(ws,qs)),s.zeros(2,1));v=sum((pi*w*F*m for pi,w,F,m in zip(ps,ws,Fs,means)),s.zeros(2,1));M=sum((pi*w*F*mm for pi,w,F,mm in zip(ps,ws,Fs,Qs)),s.zeros(2));H=support(v,M);Zd=Q(1851,10000)*I+Q(37,1000)*X+Q(59,1000)*Z;D=s.kronecker_product(I,Zd)-H
ck('K2419_dual_still_feasible',psd(D) and D.det()>0)
g=s.Matrix([1,0]);J=Jid;L=[];ells=[]
for w,mm in zip(ws,Qs):
 C=I-(1-w)*I-w*mm;e=s.Matrix([s.trace(C),C[0,1]-C[1,0]]);ells.append(e);L.append(s.sqrt(e.dot(e)))
E=Q(73,160);radius=s.sqrt(ss.dot(ss));dual=sum(pi*w for pi,w in zip(ps,ws))+2*sum(q[0] for q in qs)-2*radius-s.trace(Zd)
terms=[sum(pi*(4*E-w-l) for pi,w,l in zip(ps,ws,L)),sum(pi*l-q.dot(e) for pi,l,q,e in zip(ps,L,qs,ells)),2*(radius-g.dot(ss)),s.trace(D*J)]
ck('four_original_gap_terms_nonnegative',all(x>=0 for x in terms))
ck('exact_gap_decomposition',s.simplify(4*E-dual-sum(terms))==0)
ctrl('strict_dual_slack_cannot_match_TP',D.det()>0 and s.trace(D*J)>0)
ctrl('omitted_channel_gap_breaks_identity',s.simplify(4*E-dual-sum(terms[:-1]))!=0)
eta=Q(1,100);Ztrial=Ztri-eta*I;Dtrial=s.kronecker_product(I,Ztrial)-Htri
ctrl('uncertified_negative_slack_is_not_dual',not psd(Dtrial))
ck('certified_dual_PSD_shift',psd(Dtrial+eta*s.eye(4)) and s.trace(Ztrial+eta*I)-s.trace(Ztrial)==2*eta)
# Affine map parameters recover Choi functional and TP normalization universally.
tx,tz,a,b,c,d,yy=s.symbols('tx tz a b c d yy',real=True);tt=s.Matrix([tx,tz]);AA=s.Matrix([[a,b],[c,d]]);Jg=choi(lambda op:channel(tt,AA,yy,op))
ck('arbitrary_original_support_identity',s.expand(s.trace(H*Jg)-v.dot(tt)-sum(M[i,j]*AA[i,j] for i in range(2) for j in range(2)))==0)
ck('full_Choi_trace_normalization',ptr(Jg)==I and s.trace(Jg)==2)
# Full variable-loss identity-optimality criterion, with singular-safe LMI.
aa,bb,cc,vx,vz=s.symbols('aa bb cc vx vz',real=True);Mg=s.Matrix([[aa,cc],[cc,bb]]);vg=s.Matrix([vx,vz]);Hg=support(vg,Mg);Zg=((aa+bb)*I+vx*X+vz*Z)/2;Dg=s.kronecker_product(I,Zg)-Hg
# Unnormalized mutually orthogonal Bell-complement columns (norm squared2).
BB=s.Matrix.hstack(s.Matrix([1,0,0,-1]),s.Matrix([0,-1,-1,0]),s.Matrix([0,1,-1,0]))
Tg=s.Matrix([[aa,cc,vx],[cc,bb,vz],[vx,vz,aa+bb]])
ck('original_Bell_identity_criterion',s.simplify(BB.T*Dg*BB/2-Tg)==s.zeros(3) and Dg*s.Matrix([1,0,0,1])==s.zeros(4,1))
ck('criterion_determinant',s.factor(Tg.det()-(s.trace(Mg)*Mg.det()-(vg.T*Mg.adjugate()*vg)[0]))==0)
for label,m0,Q0,expected0 in [('rank1_pass',s.Matrix([Q(1,4),0]),s.diag(Q(1,2),0),True),('rank1_fail',s.Matrix([1,0]),s.diag(Q(1,2),0),False),('zero_pass',s.zeros(2,1),s.zeros(2),True),('zero_fail',s.Matrix([Q(1,4),0]),s.zeros(2),False),('PD_pass',s.Matrix([Q(1,10),Q(1,5)]),s.diag(Q(1,4),Q(1,2)),True)]:
 dg=s.kronecker_product(I,(s.trace(Q0)*I+m0[0]*X+m0[1]*Z)/2)-support(m0,Q0)
 ck('singular_safe_criterion_'+label,psd(dg)==psd(s.trace(Q0)*Q0-m0*m0.T)==expected0)
# K2419 identity has one active worst law; it fails the exact criterion.
ck('asymmetric_identity_excluded_exactly',not psd(s.trace(Qs[0])*Qs[0]-means[0]*means[0].T))
ctrl('balance_is_not_necessary',psd(Q(1,2)*s.diag(Q(1,2),0)-s.Matrix([Q(1,4),0])*s.Matrix([[Q(1,4),0]])))
report={'result_id':'K2422','checks':checks,'controls':controls,'paired_family':details,'paired_family_optimum':str(max(values)),'balanced_three_law_optimum':'1/2','K2419_gap_decomposition':{'four_scaled_gap_terms':list(map(str,terms)),'scaled_gap':str(4*E-dual),'strict_slack':True},'identity_criterion':'Exists active p: v v^T <= tr(M) M; M=sum p w Q, v=sum p w m.','scope':'Complete identity-optimality criterion and attained finite variable-loss joint dual; exact sign-paired uncertainty optimum and gap certificate. Asymmetric K2419 exact optimum remains open; no hardware or native GU result.'}
deps=['tests/channel-swings/k2419_positive_visibility_dual_probe.py','explorations/conditional-build/k2419-positive-visibility-dual-2026-10-31.md','explorations/conditional-build/k2407-finite-minimax-certificates-2026-10-31.md'];report['dependencies']={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps};out=R/'lab/process/k2422-joint-recovery-optimality.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==report
print(json.dumps({'checks':len(checks),'controls':len(controls),'status':'pass'}))
