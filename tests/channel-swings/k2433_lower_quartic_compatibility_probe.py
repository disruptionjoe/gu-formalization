def frame_eighth_certificate():
 """New original T7 minor; inherited k<=6 upper-bound/image data."""
 import json,hashlib
 from math import comb
 from pathlib import Path
 root=Path(__file__).resolve().parents[2]
 srcpath=root/'tests/channel-swings/k2429_shared_eighth_euler_extension_probe.py'
 src=srcpath.read_text();prefix=src[:src.index("ck('ordinary_T6_original_minor'")]
 assert prefix.count('for degree in [6]:')==1
 assert prefix.count('pivot_ids.append([name,pivot])')==1
 prefix=prefix.replace('pivot_ids.append([name,pivot])','pivot_ids.append([count-1,pivot])')
 ns={'__file__':str(srcpath),'__name__':'original_T7_certificate'}
 exec(compile(prefix.replace('for degree in [6]:','for degree in [7]:'),str(srcpath),'exec'),ns)
 new=ns['results'];assert len(new)==1
 assert new[0]['rank_mod_prime']==new[0]['universal_upper']==178002
 prior29=json.loads((root/'lab/process/k2429-shared-eighth-euler-extension.json').read_text())
 old=ns['prior']['transverse_ranks']+prior29['new_ordinary_map']
 assert [x['degree'] for x in old]==list(range(7))
 assert all(hashlib.sha256((root/p).read_bytes()).hexdigest()==h for p,h in prior29['dependencies'].items())
 total=sum(comb(13-k,6)*v['rank_mod_prime'] for k,v in enumerate(old+new))
 assert total==104*comb(20,13)-comb(18,13)
 return {'column_id_encoding':'zero-based index in the original constants-then-linear enumeration; paired with original row index','ordinary_T7':new[0],'full_octic_frame_rank':total,'universal_upper':104*comb(20,13)-comb(18,13),'prime':1000003,'scope':'Original octic frame-preserving Euler image. Together with inherited sextic compatibility, retains Euler through8 in the formal Gram/sigma construction; no all-degree Euler claim.'}

# This independent certificate can be rerun without repeating unaffected
# original tensor reconstruction. Default/--check still replays BOTH branches.
import sys as _sys,json as _json
from pathlib import Path as _Path
if '--frame-update' in _sys.argv or '--frame-check' in _sys.argv:
 _path=_Path(__file__).resolve().parents[2]/'lab/process/k2433-lower-quartic-compatibility.json'
 _frame=frame_eighth_certificate();_report=_json.loads(_path.read_text())
 if '--frame-check' in _sys.argv:assert _report['frame_eighth_extension']==_frame
 else:
  _report['frame_eighth_extension']=_frame
  _report['checks']['original_T7_full_octic_frame_image']=True
  _report['scope']='Original-section obstruction, full common null section, formal ambient Gram/sigma extension and Euler through8 by written shared-input composition; no all-order Euler or convergence.'
  _report['formal_boundary_section']['scope']='Common null W scalar sequence; ambient formal extension follows the written actual-K and normal-ideal division proof.'
  _path.write_text(_json.dumps(_report,indent=2,sort_keys=True)+'\n')
 print('K2433 independent frame eighth certificate PASS',_frame['full_octic_frame_rank'],flush=True)
 raise SystemExit(0)

"""Fixed-boundary lower-forcing obstruction and automatic-section discriminator."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'tests/channel-swings/k2431_quintic_vanishing_ideal_probe.py'
text=p.read_text(); exec(compile(text[:text.index('\nimport sys,hashlib')],str(p),'exec'))
import sys,hashlib
from sage.all import vector,sage_eval,PolynomialRing
checks={};controls={}
def ck(k,v):
 checks[k]=bool(v);print(k,bool(v),flush=True)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v);print(k,bool(v),flush=True)
 if not v:raise AssertionError(k)
env={'rt2':rt,**{str(z):z for z in w}}
def pp(z):return P(sage_eval(z,locals=env))
prior=json.loads((ROOT/'lab/process/k2431-quintic-vanishing-ideal.json').read_text())
ck('original_section_targets',L*D0==identity_matrix(F,14))
ck('original_section_Gram',D0.transpose()*G*D0==0)
ck('original_q_complete',all(changed[j]==sum(m*Q[i,j] for i,m in enumerate(mons)) for j in range(168)))
J=P.ideal(list(w[:3]));I=P.ideal(q0)
ck('J_squared_contained_in_I',all(I.reduce(a*b)==0 for a in w[:3] for b in w[:3]))
ck('q_image_contained_in_J',all(J.reduce(q)==0 for q in qpoly))
# Original tensor coefficients, not stored theorem flags.
def tensorpoly(bank):
 keys=set().union(*(set(h) for h in bank.values()))
 return {key:sum(h.get(key,F(0))*ns['mono'](mon) for mon,h in bank.items()) for key in keys}
Tp=tensorpoly(TF);Rp=tensorpoly(RF)
ck('original_T_W_in_J_componentwise',all(J.reduce(z)==0 for z in Tp.values()))
ck('original_R4W_in_J_componentwise',all(J.reduce(z)==0 for z in Rp.values()))
ck('all_K_section_T_pairings_in_J',all(J.reduce(z)==0 for z in tall[:7]))
ck('R4_norm_in_I',I.reduce(Rnorm)==0)
# d[6G(K,R5)+15G(N,R4)+10G(T,T)] at K(W)=0 gives
# k_i=-(5/2)(G(N_i,R4W)+q(U_i))-(10/3)G(TW,T_i).
# All terms belong to J; mixed-quartic changes at fixed R4W belong to I.
# Independently check the universal scalar differentiation coefficients.
Z=PolynomialRing(QQ,names=('y','k','n0','n1','u','r','t','v'));y,k,n0,n1,u,r4,t,v=Z.gens()
der=(6*y*k+15*(n0+n1*y)*(r4+u*y)+10*(t+v*y)**2).derivative(y).subs({y:0})
ck('sixth_boundary_derivative_coefficients',der==6*k+15*n1*r4+15*n0*u+20*t*v)
ctrl('omitted_mixed_quartic_derivative_wrong',der!=6*k+15*n1*r4+20*t*v)
ck('all_mixed_forcing_generators_annihilated_mod_I',all(I.reduce(a*b)==0 for a in tall[:7] for b in qpoly))
ck('all_J_forcing_annihilated_mod_I',all(I.reduce(a*b)==0 for a in tall[:7] for b in w[:3]))
S7=-F(5)/3*sum(pair(h,k)*ns['mono'](a+b) for a,h in TF.items() for b,k in RF.items())
f=list(S7.lift(I));ck('original_seventh_lift',sum(a*b for a,b in zip(f,q0))==S7)
sy=I.syzygy_module();ck('complete_syzygy_original_identities',sy*vector(P,q0)==0)
tsyz=[sum(a*b for a,b in zip(row,Tpol)) for row in sy.rows()];E=P.ideal(q0+tsyz)
pairwise=[]
for i in range(7):
 for j in range(i+1,7):
  ei=list(mons[i].dict())[0];ej=list(mons[j].dict())[0];common=tuple(max(a,b) for a,b in zip(ei,ej));row=[P(0)]*7
  row[i]=P({tuple(a-b for a,b in zip(common,ei)):F(1)})
  row[j]=-P({tuple(a-b for a,b in zip(common,ej)):F(1)})
  pairwise.append([z.subs({w[3]:w[3]-F(20736)/1445*rt*w[4]}) for z in row])
ck('independent_pairwise_syzygy_identities',all(sum(a*b for a,b in zip(row,q0))==0 for row in pairwise))
Ep=P.ideal(q0+[sum(a*b for a,b in zip(row,Tpol)) for row in pairwise])
ck('same_complete_syzygy_image',all(E.reduce(g)==0 for g in Ep.gens()) and all(Ep.reduce(g)==0 for g in E.gens()))
B8=56*sum(a*b for a,b in zip(f,Tpol))+35*Rnorm;rem=E.reduce(B8)
ctrl('actual_lower_forcing_cannot_repair_fixed_section',rem!=0 and rem==pp(prior['coupled_eighth']['fixed_K_zero_remainder']))
relaxed=list(map(pp,prior['coupled_eighth']['relaxed_K_targets']))
ctrl('relaxed_K_not_admissible_on_Z',any(J.reduce(z)!=0 for z in relaxed))
co=relaxed[3].monomial_coefficient(w[3]**5)
ck('exact_relaxed_counterexample_coefficient',co==-F(90681668802186242375)/13512914273983063262333239296)
# Outcome-contingent follow-through: can another constant q-section suppress
# the full first normal layer of T before imposing nullity?
allT=[sum(pair({key:ff(val) for key,val in h.items()},k)*ns['mono'](mon) for mon,k in TF.items()) for h in reps]
exps=sorted({e for z in allT for e in z.dict() if sum(e[:3])==1})
Tb=matrix(F,[[z.monomial_coefficient(P({e:F(1)})) for z in allT] for e in exps])
A=L.stack(Tb);rhs=matrix(F,[[0]*7 for _ in range(7)]+[[int(i==j) for j in range(7)] for i in range(7)]+[[0]*7 for _ in exps])
rank=A.rank();aug=A.augment(rhs).rank();sol=None;dual=None
if rank==aug:
 sol=A.solve_right(rhs);ck('automatic_section_linear_solution',A*sol==rhs)
else:
 for row in A.left_kernel().basis():
  if row*rhs!=0:
   dual=row;break
 ck('automatic_section_exact_dual',dual is not None and dual*A==0 and dual*rhs!=0)
# Preserve the added linear targets while constructing a null section.
newsection=None;newmethod=None
Aq=G.inverse()*Q.transpose()
ck('q_dual_null',Aq.transpose()*G*Aq==0)
correction_preserves=Tb*Aq==0
if sol is not None and correction_preserves:
 newsection=sol-Aq*(sol.transpose()*G*sol)/2
 newmethod='q_dual_half_Gram_correction'
 ck('new_section_all_linear_targets',A*newsection==rhs)
 ck('new_section_null_Gram',newsection.transpose()*G*newsection==0)
elif sol is not None:
 # Stronger covector test: when the full independent row span is isotropic,
 # nullification of the simultaneous right inverse preserves every target.
 piv=A.transpose().pivots();Aind=A[list(piv),:];dualG=Aind*G.inverse()*Aind.transpose()
 if dualG==0:
  ri=Aind.solve_right(identity_matrix(F,len(piv)));nullri=ri-G.inverse()*Aind.transpose()*(ri.transpose()*G*ri)/2
  newsection=nullri*rhs[list(piv),:];newmethod='complete_isotropic_constraint_right_inverse'
  ck('new_section_all_linear_targets',A*newsection==rhs)
  ck('new_section_null_Gram',newsection.transpose()*G*newsection==0)
if newsection is not None:
 newt=list(vector(P,allT)*matrix(P,newsection))
 ck('new_section_T_pairings_in_I',all(I.reduce(z)==0 for z in newt))
 # This q-only null section fixes K=0; an arbitrary actual K extension needs
 # a full14-column null extension, not an implied choice of lower forcing.
 newR5=matrix(P,newsection)*vector(P,f)
 ck('new_q_section_seventh_original_replay',sum(qpoly[j]*newR5[j] for j in range(168))==S7)
 new8=56*sum(a*b for a,b in zip(newt,f))+35*Rnorm
 ck('new_q_section_eighth_source_in_I',I.reduce(new8)==0)
 new6=list((-new8/28).lift(I))
 ck('new_q_section_eighth_exact_lift',28*sum(a*b for a,b in zip(q0,new6))+new8==0)
# Full common null section suppressing both first-normal pairing layers.
from sage.all import binomial
allR=[sum(pair({key:ff(val) for key,val in h.items()},k)*ns['mono'](mon) for mon,k in RF.items()) for h in reps]
rexps=sorted({e for z in allR for e in z.dict() if sum(e[:3])==1})
Rb=matrix(F,[[z.monomial_coefficient(P({e:F(1)})) for z in allR] for e in rexps])
extra=Tb.stack(Rb);AF=L.stack(extra);BF=identity_matrix(F,14).stack(matrix(F,extra.nrows(),14))
ck('full_T_R_linear_consistency',AF.rank()==AF.augment(BF).rank())
Dlin=AF.solve_right(BF)
# Exact field split bank from original Gram, with explicit all-ones matrix.
signs=[G[12*i,12*i]/2 for i in range(14)];std=identity_matrix(F,12)+matrix(F,[[1]*12 for _ in range(12)])
ck('original_fourteen_signed_Gram_blocks',all(G[12*i:12*i+12,12*j:12*j+12]==(signs[i]*std if i==j else 0) for i in range(14) for j in range(14)))
posblocks=[i for i,z in enumerate(signs) if z==1];negblocks=[i for i,z in enumerate(signs) if z==-1]
ck('seven_positive_negative_block_pairs',len(posblocks)==len(negblocks)==7)
X=matrix(F,168,84)
for i,(a,b) in enumerate(zip(posblocks,negblocks)):
 for j in range(12):X[12*a+j,12*i+j]=1;X[12*b+j,12*i+j]=1
ck('original_exact_maximal_null84_bank',X.rank()==84 and X.transpose()*G*X==0)
cons=AF.stack(Dlin.transpose()*G);C=cons.right_kernel().basis_matrix().transpose();Xi=X*(cons*X).right_kernel().basis_matrix().transpose();pairbank=Xi.transpose()*G*C
ck('constrained_null_bank_enough_pairs',pairbank.rank()>=14)
ids=list(pairbank.transpose().pivots())[:14];UU=Xi[:,ids];VV0=C*(UU.transpose()*G*C).solve_right(identity_matrix(F,14));VV=VV0-UU*(VV0.transpose()*G*VV0)/2
ck('exact_fourteen_hyperbolic_pairs',UU.transpose()*G*UU==0 and VV.transpose()*G*VV==0 and UU.transpose()*G*VV==identity_matrix(F,14))
ck('repair_vectors_preserve_linear_constraints',cons*UU==0 and cons*VV==0)
DF=Dlin+UU-VV*(Dlin.transpose()*G*Dlin)/2
ck('full_section_all_original_K_q_targets',L*DF==identity_matrix(F,14))
ck('full_section_all_T_R_first_layer_constraints',extra*DF==0)
ck('full_section_common_total_nullity',DF.transpose()*G*DF==0)
TFULL=list(vector(P,allT)*matrix(P,DF));RFULL=list(vector(P,allR)*matrix(P,DF))
ck('all14_full_T_R_pairings_in_I',all(I.reduce(z)==0 for z in TFULL+RFULL))
ctrl('unrepaired_full_linear_section_not_null',Dlin.transpose()*G*Dlin!=0)
# One same-section fixture through tenth scalar boundary; K targets at orders
# >=6 deliberately need not belong to J. They are algebraic fixtures, not
# claimed actual Euler-derived K targets.
coeffs={};targets={};boundary=[]
for j in range(5,9):
 if j==5:target=S7
 elif j==6:target=-(56*sum(a*b for a,b in zip(TFULL,coeffs[5]))+35*Rnorm)/28
 else:
  nn=j+2;target=-(binomial(nn,3)*sum(a*b for a,b in zip(TFULL,coeffs[j-1]))+binomial(nn,4)*sum(a*b for a,b in zip(RFULL,coeffs[j-2])))/binomial(nn,2)
 ck('boundary_'+str(j+2)+'_source_in_I',I.reduce(target)==0)
 fj=list(target.lift(I));kj=[w[0]*w[(i%4)+3]**(j-1) if j==5 else w[(i%4)+3]**j for i in range(7)]
 coeffs[j]=vector(P,kj+fj);targets[j]=target
 ck('boundary_'+str(j+2)+'_homogeneous_same_section_lift',sum(a*b for a,b in zip(q0,fj))==target and all(not z or all(sum(e)==j for e in z.dict()) for z in coeffs[j]))
 Rj=matrix(P,DF)*coeffs[j]
 ck('boundary_'+str(j+2)+'_original_q_and_K_replay',matrix(P,L)*Rj==coeffs[j] and sum(qpoly[i]*Rj[i] for i in range(168))==target)
 boundary.append({'order':j+2,'jet_order':j,'K_targets':list(map(str,kj)),'q_coefficients':list(map(str,fj)),'source':str(target)})
ck('same_image_cross_Gram_certificate_all_higher_orders',DF.transpose()*G*DF==0)
# All finite orders follow from homogeneous ideal lifting in this SAME fixed
# section; no coefficient growth, convergence, mixed-normal or Euler inference.
# Compact exact data for bounded same-instance follow-through, excluded from git.
from sage.all import save
scratch=ROOT/'_local/k2433';scratch.mkdir(parents=True,exist_ok=True)
save({'G':G,'L':L,'D0':D0,'Q':Q,'Pmat':Pmat,'Tb':Tb,'A':A,'rhs':rhs,'sol':sol,'newsection':newsection,'P':P,'F':F,'rt':rt,'w':w,'allT':allT,'allR':allR,'q0':q0,'qpoly':qpoly,'S7':S7,'f':f,'Rnorm':Rnorm},str(scratch/'exact-data'))
# Original target-dependent linear condition without forcing all T directions:
# retains degree5 syzygies; future section choice must be coupled with nullity.
# Recursively pin literal source/report references and all declared evidence hashes.
# This reads dependencies; it does not replay unrelated scientific jobs.
import re
pins={};pending=['tests/channel-swings/k2431_quintic_vanishing_ideal_probe.py','lab/process/k2431-quintic-vanishing-ideal.json']
while pending:
 z=pending.pop()
 if z in pins:continue
 body=(ROOT/z).read_bytes();pins[z]=hashlib.sha256(body).hexdigest()
 if z.endswith('.py'):
  pending.extend(v for v in re.findall(r"['\"]((?:tests/channel-swings|lab/process)/[^'\"]+\.(?:py|json))['\"]",body.decode()) if (ROOT/v).is_file())
 elif z.endswith('.json'):
  obj=json.loads(body)
  for path,h in obj.get('dependencies',{}).items():
   assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h,(z,path)
   pending.append(path)
ck('recursive_original_dependency_pins',len(pins)>15)
report={'result_id':'K2433','scope':'Fixed original-section obstruction plus constructive common null section with formal W-only scalar Gram extension; no new complete Euler jet, mixed-normal completion or convergence.','checks':checks,'controls':controls,'dependencies':pins,'forcing':{'identity':'6k_i+15G(N_i,R4W)+15q(U_i)+20G(TW,T_i)=0','J_generators':list(map(str,w[:3])),'I_generators':list(map(str,q0)),'mixed_delta_k':'-(5/2)q(delta_U_i) in I','actual_k':'in J','eta_k':'zero modulo I, hence E'},'fixed_section':{'eighth_remainder':str(rem),'terms':len(rem.dict()),'relaxed_K3_w3pow5':str(co)},'formal_boundary_section':{'constraint_rows':AF.nrows(),'constraint_rank':AF.rank(),'kernel_dimension':C.ncols(),'null_intersection_dimension':Xi.ncols(),'pairing_rank':pairbank.rank(),'D':[[str(z) for z in row] for row in DF],'t_pairings':list(map(str,TFULL)),'r_pairings':list(map(str,RFULL)),'explicit_boundaries':boundary,'scope':'Formal W scalar Gram extension with arbitrary prescribed homogeneous K targets in one common null section; no mixed-normal, Euler or convergence claim'},'automatic_section':{'normal_layer_rows':len(exps),'normal_layer_rank':Tb.rank(),'constraint_rank':rank,'augmented_rank':aug,'linear_consistent':rank==aug,'q_dual_correction_preserves_Tbar':bool(correction_preserves),'null_method':newmethod,'null_solution':None if newsection is None else [[str(z) for z in row] for row in newsection],'dual':None if dual is None else list(map(str,dual)),'dual_rhs':None if dual is None else list(map(str,dual*rhs)),'solution':None if sol is None else [[str(z) for z in row] for row in sol]},'evidence_kinds':{'universal':'written differentiated Gram and ideal-filtration proof','exact':'original tensor vanishing, full syzygy ideal, original common-section matrix identities and homogeneous boundary lifts'}}
frame_extension=frame_eighth_certificate()
ck('original_T7_full_octic_frame_image',True)
report['frame_eighth_extension']=frame_extension
report['scope']='Original-section obstruction, full common null section, formal ambient Gram/sigma extension and Euler through8 by written shared-input composition; no all-order Euler or convergence.'
report['formal_boundary_section']['scope']='Common null W scalar sequence; ambient formal extension follows the written actual-K and normal-ideal division proof.'
path=ROOT/'lab/process/k2433-lower-quartic-compatibility.json'
if '--check' in sys.argv:assert json.loads(path.read_text())==report
else:path.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2433',len(checks),len(controls),'automatic',rank,aug,'PASS',flush=True)
