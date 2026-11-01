"""Original isotropic-section certificate and exact coupled boundary discriminators."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'tests/channel-swings/k2429_shared_eighth_euler_extension_probe.py';s=p.read_text();ns={'__file__':str(p),'__name__':'restricted_kernel'}
exec(compile(s[:s.index('\nss=[[symbol')],str(p),'exec'),ns)
a=s.index('qpath=ROOT/');b=s.index('Rc=qn',a);exec(compile(s[a:b],str(p),'exec'),ns)
t=ns['_k25text'];a=t.index('from sage.all import QuadraticField,PolynomialRing,matrix');b=t.index('target=P(0)',a);exec(compile(t[a:b],str(ns['_k25path']),'exec'),ns)
from sage.all import matrix,QQ,identity_matrix
reps=ns['hs'][:168];ff=ns['ff'];gram=ns['gram'];F=ns['field'];rt=F.gen()
G=matrix(F,[[ff(gram(h,k)) for k in reps] for h in reps]);KE=ns['KE']
Pmat=matrix(F,[[ff(gram(k,h)) for h in reps] for k in KE])
# Pairing covectors of N_W after polynomial change w3=ell+c*w4.
w=ns['w'];P=ns['P'];qm=ns['qm'];lws=ns['lws'];mult=lambda t:1 if t[0]==t[1] else 2
qpoly=[sum(mult(t)*ns['mono'](t)*(ff(gram(lws[0][j],h))+rt*ff(gram(lws[1][j],h))) for j,t in enumerate(qm)) for h in reps]
c=F(20736)/1445*rt; changed=[q.subs({w[3]:w[3]+c*w[4]}) for q in qpoly];mons=[w[0]*w[3]]+[w[i]*w[j] for i in range(3) for j in range(i,3)]
Q=matrix(F,[[q.monomial_coefficient(m) for q in changed] for m in mons])
# full 168 covectors simultaneous K,q and qdual Gram
L=Pmat.stack(Q)
import json
out={'G':[[str(x) for x in row] for row in G], 'Q':[[str(x) for x in row] for row in Q], 'K':[[str(x) for x in row] for row in Pmat]}
from sage.all import vector
# Null linear section for K/q; columns are full repeated-hook coordinates.
D=L.solve_right(identity_matrix(F,14));N=G.inverse()*L.transpose();H=D.transpose()*G*D;D0=D-N*H/2
# K targets zero, choose q-only last seven columns.
Dq=D0[:,7:];reptensor=[]
for col in Dq.columns():
 h={}
 for c,v in zip(col,reps):
  for key,val in v.items():h[key]=h.get(key,F(0))+c*ff(val)
 reptensor.append(h)
def pair(h,k):return sum(F(ns['eta'][a]*ns['eta'][b]*ns['eta'][c])/2*v*k.get((a,b,c),0) for (a,b,c),v in h.items())
TF={};RF={}
for bank,parts,mul in [(TF,ns['T3'],False),(RF,ns['r4'],True)]:
 for ip,part in enumerate(parts):
  for mon,h in part.items():
   z=bank.setdefault(mon,{})
   fac=(rt if ip else 1)*(len(set(ns['permutations'](mon))) if mul else 1)
   for key,v in h.items():z[key]=z.get(key,F(0))+ff(v)*fac
Tpol=[sum(pair(h,k)*ns['mono'](mon) for mon,k in TF.items()) for h in reptensor]
Rpol=[sum(pair(h,k)*ns['mono'](mon) for mon,k in RF.items()) for h in reptensor]
# q forms in original coordinates of this null section.
q0=[sum(m*coeff for m,coeff in zip(mons,col)) for col in (Q*Dq).columns()]
q0=[q.subs({w[3]:w[3]-F(20736)/1445*rt*w[4]}) for q in q0]
# Carry exact original matrices for independent reproduction.
out.update(D0=[[str(x) for x in row] for row in D0],Tpol=list(map(str,Tpol)),Rpol=list(map(str,Rpol)),q0=list(map(str,q0)))
# Original quartic norm, independent of mixed quartic choices which vanish on W.
Rnorm=sum(pair(h,k)*ns['mono'](a+b) for a,h in RF.items() for b,k in RF.items())
out['Rnorm']=str(Rnorm)
# Pairings for all14 null-section columns, needed for mixed K forcing.
tall=[];rall=[]
for col in D0.columns():
 h={}
 for coeff,v in zip(col,reps):
  for key,val in v.items():h[key]=h.get(key,F(0))+coeff*ff(val)
 tall.append(sum(pair(h,k)*ns['mono'](mon) for mon,k in TF.items()))
 rall.append(sum(pair(h,k)*ns['mono'](mon) for mon,k in RF.items()))
out['Tall']=list(map(str,tall));out['Rall']=list(map(str,rall))

import sys,hashlib
from sage.all import vector,sage_eval
checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 print(k,bool(v),flush=True)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 print(k,bool(v),flush=True)
 if not v:raise AssertionError(k)
env={'rt2':rt,**{str(z):z for z in w}}
def pp(z):return P(sage_eval(z,locals=env))
prior=json.loads((ROOT/'lab/process/k2425-frame-euler-module.json').read_text())
prior27=json.loads((ROOT/'lab/process/k2427-frame-boundary-quotient.json').read_text())
ck('inherited_dependency_pins',all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for prior0 in [prior,prior27] for p,h in prior0['dependencies'].items()))
ck('original_repeated_Gram_nondegenerate168',G.rank()==168 and G==G.transpose())
ck('original_K_q_independent14',Pmat.rank()==7 and Q.rank()==7 and L.rank()==14)
ck('original_K_q_dual_span_totally_isotropic',L*G.inverse()*L.transpose()==0)
ck('constant_section_right_inverse',L*D==identity_matrix(F,14))
ck('null_section_same_all14_targets',L*D0==identity_matrix(F,14))
ck('null_section_all_pairwise_Gram_zero',D0.transpose()*G*D0==0)
ctrl('uncorrected_section_not_null',D.transpose()*G*D!=0)
wrong=D-N*H/3
ctrl('wrong_half_factor_not_null',wrong.transpose()*G*wrong!=0)
ck('original_q_support_complete',all(changed[j]==sum(m*Q[i,j] for i,m in enumerate(mons)) for j in range(168)))
ck('all14_original_q_contractions',all(sum(qpoly[j]*D0[j,k] for j in range(168))==(0 if k<7 else q0[k-7]) for k in range(14)))
ck('original_q_polynomials',q0==[w[0]*(w[3]-F(20736)/1445*rt*w[4]),w[0]**2,w[0]*w[1],w[0]*w[2],w[1]**2,w[1]*w[2],w[2]**2])
# Independently reconstruct fixed seventh target and quartic norm from original hooks.
S7=-F(5)/3*sum(pair(h,k)*ns['mono'](a+b) for a,h in TF.items() for b,k in RF.items())
ck('actual_original_seventh_target',S7==pp(prior['seventh_algebraic_completion']['target']))
I=P.ideal(q0);Jq=P.ideal([x*g for x in w[:3] for g in q0]);rem7=Jq.reduce(S7)
ctrl('zero_on_Z_impossible_for_seventh_target',rem7!=0 and len(rem7.dict())==17)
normal2=P({e:v for e,v in S7.dict().items() if sum(e[:3])==2})
normal_res=normal2.subs({w[3]:F(20736)/1445*rt*w[4]})
ck('independent_normal_degree_obstruction',normal_res!=0 and len(normal_res.dict())==17 and all(sum(e[:3])==2 for e in normal_res.dict()))
f=list(S7.lift(I));ck('original_seventh_polynomial_lift',sum(a*b for a,b in zip(f,q0))==S7)
B=matrix(P,Dq)*vector(P,f)
ck('null_seventh_original_q_replay',sum(qpoly[j]*B[j] for j in range(168))==S7)
ck('null_seventh_lift_original_Gram_certificate',Dq.transpose()*G*Dq==0 and B==matrix(P,Dq)*vector(P,f))
ck('null_seventh_lift_all_K_targets_zero',matrix(P,Pmat)*B==0)
ck('null_seventh_lift_homogeneous5',all(not x or all(sum(e)==5 for e in x.dict()) for x in B))
ck('null_seventh_lift_nonzero_on_Z',any(x.subs({w[0]:0,w[1]:0,w[2]:0}) for x in B))
# Arbitrary polynomial mixed K forcing is also allowed by the null section.
forces=vector(P,[w[3]**5,w[4]**5,w[5]**5,w[6]**5,w[3]**3*w[4]**2,w[3]*w[5]**4,w[4]*w[6]**4]+f)
Bmix=matrix(P,D0)*forces
ck('mixed_forcing_preserved_all14_targets',matrix(P,L)*Bmix==forces)
ck('mixed_forcing_still_null',D0.transpose()*G*D0==0 and Bmix==matrix(P,D0)*forces)
# Full polynomial syzygies of q, not merely constant kernel.
sy=I.syzygy_module();ck('all_original_q_syzygy_identities',sy.ncols()==7 and sy*vector(P,q0)==0)
tsyz=[sum(a*b for a,b in zip(row,Tpol)) for row in sy.rows()]
ext=P.ideal(q0+tsyz)
# Independent complete pairwise monomial syzygies in the ell coordinates.
pairwise=[]
for i in range(7):
 for j in range(i+1,7):
  ei=list(mons[i].dict())[0];ej=list(mons[j].dict())[0]
  common=tuple(max(a,b) for a,b in zip(ei,ej))
  row=[P(0)]*7
  row[i]=P({tuple(a-b for a,b in zip(common,ei)):F(1)})
  row[j]=-P({tuple(a-b for a,b in zip(common,ej)):F(1)})
  pairwise.append([z.subs({w[3]:w[3]-F(20736)/1445*rt*w[4]}) for z in row])
ck('independent_21_pairwise_syzygy_identities',len(pairwise)==21 and all(sum(a*b for a,b in zip(row,q0))==0 for row in pairwise))
tpair=[sum(a*b for a,b in zip(row,Tpol)) for row in pairwise]
epair=P.ideal(q0+tpair)
ck('independent_complete_syzygy_image_ideal',all(ext.reduce(z)==0 for z in tpair) and all(epair.reduce(z)==0 for z in tsyz))
B8=56*sum(a*b for a,b in zip(f,Tpol))+35*Rnorm
rfix=ext.reduce(B8)
ctrl('K_zero_null_section_eighth_obstruction',rfix!=0)
# This relaxed positive control lets K targets vary; actual mixed-quartic targets are NOT free.
gens=q0+tsyz+tall[:7];FI=P.ideal(gens);rrfree=FI.reduce(B8)
ck('free_K_relaxed_eighth_target_liftable',rrfree==0)
lift=list(B8.lift(FI));ck('free_K_original_generator_lift',sum(a*b for a,b in zip(gens,lift))==B8)
length=len(q0)+len(tsyz);fv=vector(P,f)
for c,row in zip(lift[7:length],sy.rows()):fv-=c*row/56
fk=vector(P,[-c/56 for c in lift[length:]])
R5=matrix(P,D0)*vector(P,list(fk)+list(fv));R6=matrix(P,Dq)*vector(P,[-c/28 for c in lift[:7]])
ck('relaxed_R5_same_seventh_target',sum(a*b for a,b in zip(q0,fv))==S7)
ck('relaxed_R5_still_pointwise_null',D0.transpose()*G*D0==0 and R5==matrix(P,D0)*vector(P,list(fk)+list(fv)))
ck('relaxed_R5_original_q_replay',sum(qpoly[j]*R5[j] for j in range(168))==S7)
ck('relaxed_R6_original_q_replay',sum(qpoly[j]*R6[j] for j in range(168))==sum(q0[j]*(-lift[j]/28) for j in range(7)))
ck('relaxed_R5_explicit_K_targets',matrix(P,Pmat)*R5==fk)
check8=28*sum(a*b for a,b in zip(q0,[-c/28 for c in lift[:7]]))+56*(sum(a*b for a,b in zip(Tpol,fv))+sum(a*b for a,b in zip(tall[:7],fk)))+35*Rnorm
ck('relaxed_all3003_eighth_coefficients',check8==0)
ck('relaxed_lift_homogeneous',all(not z or all(sum(e)==5 for e in z.dict()) for z in list(fv)+list(fk)) and all(not z or all(sum(e)==6 for e in z.dict()) for z in R6))
# A ninth shortcut using only old q and t(Cq) cannot cover all null-section directions.
b=prior27['boundary'];oldI=P.ideal(list(map(pp,b['quadratic_generators']+b['cubic_generators'])))
rclasses=[oldI.reduce(z) for z in rall]
ctrl('ninth_automatic_transfer_not_proved',any(rclasses))
# Actual relaxed R5,R6 ninth source, with all previous relaxed coefficients fixed.
source9=84*sum(a*b for a,b in zip(Tpol,[-c/28 for c in lift[:7]]))+126*(sum(a*b for a,b in zip(Rpol,fv))+sum(a*b for a,b in zip(rall[:7],fk)))
rem9=oldI.reduce(source9)
# This may succeed or fail; report the exact result, not a presupposed theorem.
ck('ninth_remainder_reproducible',oldI.reduce(source9-rem9)==0)
deps=['lab/process/k2425-frame-euler-module.json','lab/process/k2427-frame-boundary-quotient.json','lab/process/k2423-corotating-mixed-sixth.json','tests/channel-swings/k2429_shared_eighth_euler_extension_probe.py','tests/channel-swings/k2425_frame_euler_module_probe.py']
report={'result_id':'K2431','scope':'Exact conditional null linear lift for original K/q targets; zero-on-Z shortcut excluded; relaxed seventh/eighth boundary fixture only. No new full shared Euler jet or GU claim.','checks':checks,'controls':controls,'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},'null_section':{'original_dimension':168,'constraint_rank':14,'D0':[[str(x) for x in row] for row in D0],'original_G_sha256':hashlib.sha256(repr(G).encode()).hexdigest(),'original_L_sha256':hashlib.sha256(repr(L).encode()).hexdigest(),'q_forms':list(map(str,q0))},'zero_restriction':{'original_target':str(S7),'normal_degree_two_terms':len(normal2.dict()),'nonzero_remainder':str(rem7),'normal_restriction':str(normal_res)},'null_seventh':{'q_lift':list(map(str,f)),'q_t_pairings':list(map(str,Tpol)),'q_r_pairings':list(map(str,Rpol))},'coupled_eighth':{'independent_pairwise_syzygies':[[str(z) for z in row] for row in pairwise],'all_q_syzygies':[[str(z) for z in row] for row in sy.rows()],'fixed_K_zero_remainder':str(rfix),'free_K_original_generator_lift':list(map(str,lift)),'relaxed_K_targets':list(map(str,fk)),'relaxed_q_coefficients':list(map(str,fv)),'relaxed_R6_q_coefficients':list(map(str,[-c/28 for c in lift[:7]])),'scope':'K forcing freely selected, not matched to one admissible lower quartic; not the full finite-jet theorem'},'ninth':{'nonzero_r_direction_classes':[i for i,z in enumerate(rclasses) if z],'relaxed_source_remainder':str(rem9),'simple_repair_succeeds':rem9==0,'scope':'q/t(Cq)-only successor on relaxed boundary; no actual mixed-quartic matching'},'evidence_kinds':{'original_exact':'Gram, K/q tensor covectors, isotropic section identities, direct polynomial contractions','ideal_exact':'original-generator lift identities, full Singular syzygy basis independently compared to complete21 monomial syzygy images, and Groebner normal forms','universal':'linear algebra argument in note; no sampling inference'}}
path=ROOT/'lab/process/k2431-quintic-vanishing-ideal.json'
if '--check' in sys.argv:
 if json.loads(path.read_text())!=report:raise AssertionError('no-write report differs')
else:path.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2431',len(checks),'checks',len(controls),'controls PASS; ninth relaxed remainder terms',len(rem9.dict()),flush=True)
