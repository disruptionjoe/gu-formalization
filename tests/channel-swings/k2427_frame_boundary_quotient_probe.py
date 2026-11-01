"""Shared frame boundary quotient and original seventh-Euler compatibility."""
from pathlib import Path
import json,sys,hashlib,ast
ROOT=Path(__file__).resolve().parents[2]
_k25path=ROOT/'tests/channel-swings/k2425_frame_euler_module_probe.py';_k25text=_k25path.read_text()
# Reconstruct original tensors and generators; do not rerun unchanged large ranks.
exec(compile(_k25text[:_k25text.index('ss=[[symbol')],str(_k25path),'exec'),globals())
qpath=ROOT/'tests/channel-swings/k2405_fifth_euler_compatibility_probe.py';qsrc=qpath.read_text();qn={'__file__':str(qpath),'__name__':'lowerS'}
exec(compile(qsrc[:qsrc.index('# Pair-field covariant derivative')],str(qpath),'exec'),qn)
for node in ast.parse(qsrc).body:
 if isinstance(node,ast.FunctionDef) and node.name=='fp':exec(compile(ast.Module(body=[node],type_ignores=[]),str(qpath),'exec'),qn)
# Exact proper-ideal and original-generator lift reconstruction, no prior rank replay.
exec(compile(_k25text[_k25text.index('from sage.all import QuadraticField,PolynomialRing,matrix'):_k25text.index("report={'result_id':'K2425'")],str(_k25path),'exec'),globals())
inherited_checks=dict(checks);inherited_controls=dict(controls);checks={};controls={}
from sage.all import vector
prior=json.loads((ROOT/'lab/process/k2425-frame-euler-module.json').read_text())
ck('inherited_dependency_hashes_current',all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in prior['dependencies'].items()))
# Exact original constant kernel, retaining all 154 freedoms.
ker=Q.left_kernel().basis_matrix();ck('constant_kernel154',ker.nrows()==154 and ker*Q==0)
tpol=[sum((ff(gram(h,hh))*(rt if ip else 1)*mono(t) for ip,part in enumerate(T3) for t,hh in part.items()),P(0)) for h in rep]
tker=[ideal.reduce(sum((c*t for c,t in zip(row,tpol)),P(0))) for row in ker.rows()]
mons3=list(combinations_with_replacement(range(7),3));tm=matrix(field,[[t.monomial_coefficient(mono(m)) for m in mons3] for t in tker]);tpiv=tm.transpose().pivots();ck('constant_kernel_cubic_image11',len(tpiv)==11)
coeffs=[]
for j,t in enumerate(next_coeffs):
 row=vector(field,[t.monomial_coefficient(mono(m)) for m in mons3]);co=tm.transpose().solve_right(row);ck('particular_class_cancel_'+str(j),tm.transpose()*co==row);coeffs.append(co)
# State the ideal directly and independently compare both containments.
ell=w[3]-field(20736)/1445*rt*w[4];simple=[w[i]*w[j] for i in range(3) for j in range(i,3)]+[w[0]*ell]
ck('quadratic_ideal_exact_presentation',all(ideal.reduce(x)==0 for x in simple) and all(P.ideal(simple).reduce(x)==0 for x in qpolys))
std8=[]
for t in combinations_with_replacement(range(7),8):
 exp=tuple(t.count(i) for i in range(7))
 if not any(all(a>=b for a,b in zip(exp,lm)) for lm in lms):std8.append(exp)
ck('eighth_quotient441',len(std8)==441==comb(11,3)+2*comb(10,3)+comb(9,2))
def pairfield(Pa,Pb):
 out=P(0)
 for ma,ha in Pa.items():
  for mb,hb in Pb.items():
   val=sum(ff(F(eta[k[0]]*eta[k[1]]*eta[k[2]],2))*v*hb.get(k,0) for k,v in ha.items())
   if val:out+=val*mono(ma+mb)
 return out
def fieldpoly(parts,mult=False):
 out={}
 for ip,part in enumerate(parts):
  for m,h in part.items():
   hh=out.setdefault(m,{})
   for k,v in h.items():hh[k]=hh.get(k,0)+ff(v)*(rt if ip else 1)*(len(set(permutations(m))) if mult else 1)
 return out
TF=fieldpoly(T3);RF=fieldpoly(r4,True)
bound=56*pairfield(TF,h5)+35*pairfield(RF,RF);br=ideal.reduce(bound)
ctrl('fixed_eighth_source_not_already_in_quadratic_ideal',br!=0)
# Use raw cubic polynomials for original-column lifts, not their quotient representatives.
rawt=[sum((c*t for c,t in zip(ker.row(i),tpol)),P(0)) for i in tpiv]
gens=qpolys+rawt;ext=P.ideal(gens);ck('constant_kernel_removes_actual_eighth_obstruction',ext.reduce(bound)==0)
lift=list(bound.lift(ext));ck('original_generators_eighth_identity',sum((a*b for a,b in zip(gens,lift)),P(0))==bound)
ck('eighth_homogeneous_lift_degrees',all(not p or all(sum(e)==(6 if i<7 else 5) for e in p.dict()) for i,p in enumerate(lift)))
# Exact hook reconstruction of q-kernel correction and R6 boundary.
cor5={};cor6={}
def hookpolyadd(out,poly,h,factor):
 for exp,val in poly.dict().items():
  m=tuple(i for i,e in enumerate(exp) for _ in range(e));hh=out.setdefault(m,{})
  for k,v in h.items():hh[k]=hh.get(k,field(0))+factor*val*v
for i,pol in enumerate(lift[:7]):hookpolyadd(cor6,pol,{k:ff(v) for k,v in rep[piv[i]].items()},-field(1)/28)
for i,pol in zip(tpiv,lift[7:]):
 hh={}
 for c,h in zip(ker.row(i),rep):
  for k,v in h.items():hh[k]=hh.get(k,field(0))+c*ff(v)
 hookpolyadd(cor5,pol,hh,-field(1)/56)
NF={}
for j,t in enumerate(qm):
 h={}
 for ip in range(2):
  for k,v in lws[ip][j].items():h[k]=h.get(k,field(0))+ff(v)*(rt if ip else 1)*(1 if t[0]==t[1] else 2)
 NF[t]=h
ck('original_hook_correction_preserves_seventh',pairfield(NF,cor5)==0)
ck('all3003_original_eighth_boundary_coefficients',bound+56*pairfield(TF,cor5)+28*pairfield(NF,cor6)==0)
ctrl('wrong_eighth_binomial_factor_fails',bound+55*pairfield(TF,cor5)+28*pairfield(NF,cor6)!=0)
boundary={'q_kernel_dimension':154,'cubic_quotient_image_rank':11,'constant_kernel_pivots':list(map(int,tpiv)),'Jorth_cancellation_kernel_coefficients':[[str(c) for c in row] for row in coeffs],'quadratic_generators':list(map(str,qpolys)),'cubic_generators':list(map(str,rawt)),'quotient_dimension_degree8':441,'fixed_source':str(bound),'fixed_source_terms':len(bound.dict()),'quadratic_ideal_remainder':str(br),'eighth_original_generator_lift':list(map(str,lift)),'boundary_receivers':3003}
# Outcome-released ninth-boundary discriminator on the original full repeated space.
repeated_all=hs[:168]
r4pair=[]
for hh in repeated_all:
 pol=sum((sum(ff(F(eta[k[0]]*eta[k[1]]*eta[k[2]],2))*v*ff(hh.get(k,0)) for k,v in h.items())*mono(m) for m,h in RF.items()),P(0))
 r4pair.append(ext.reduce(pol))
nonzero9=[i for i,x in enumerate(r4pair) if x]
print('ninth R4/full-repeated quotient couplings',len(nonzero9),flush=True)
# All Jorth T couplings are removable by the same constant kernel, but R4 is new.
ck('ninth_Jorth_T_classes_in_extended_ideal',all(ext.reduce(x)==0 for x in next_coeffs))
ninth={'full_repeated_dimension':168,'nonzero_R4_pairing_classes':nonzero9,'R4_pairing_remainders':list(map(str,r4pair)),'scope':'Exact next-boundary dependence diagnostic only. No ninth-algebraic/seventh-Euler conjunction follows.'}

# Executed successor: a sufficient coupled-boundary kernel closes all ninth sources.
# Use the EXACT constant kernel of (q,t), not only t modulo I.
qall=[sum((1 if a==b else 2)*Q[i,j]*w[a]*w[b] for j,(a,b) in enumerate(qm)) for i in range(len(rep))]
QT=matrix(field,[[*Q.row(i),*[t.monomial_coefficient(mono(m)) for m in mons3]] for i,t in enumerate(tpol)])
Cqt=QT.left_kernel().basis_matrix()
ck('coupled_constant_kernel130',Cqt.nrows()==130 and Cqt*QT==0 and QT.rank()==31)
tq=[sum((c*t for c,t in zip(h,tpol)),P(0)) for h in ker.rows()]
# Original-hook pairings, collected by hook coordinate to avoid repeated products.
rb={};tb={}
for bank,parts in [(rb,RF),(tb,TF)]:
 for m,h in parts.items():
  for k,v in h.items():bank[k]=bank.get(k,P(0))+ff(F(eta[k[0]]*eta[k[1]]*eta[k[2]],2))*v*mono(m)
def bankpair(bank,h):return sum((ff(v)*bank.get(k,P(0)) for k,v in h.items()),P(0))
rpol=[bankpair(rb,h) for h in rep]
rqt=[sum((c*r for c,r in zip(h,rpol)),P(0)) for h in Cqt.rows()]
ngens=qpolys+tq+rqt;NI=P.ideal(ngens);ngb=NI.groebner_basis()
ck('old_ninth_ideal_contained_in_coupled_ideal',all(NI.reduce(g)==0 for g in gens))
# Every generator has a concrete correction: R7 pivot/36, R6 Cq/84, R5 Cqt/126.
ck('R6_kernel_preserves_seventh_and_eighth',ker*Q==0)
ck('R5_joint_kernel_preserves_seventh_and_eighth',Cqt*QT==0)
alltargets=[bankpair(tb,h) for h in repeated_all]+[bankpair(rb,h) for h in repeated_all]
ck('all336_original_T_R4_pairings_in_coupled_ideal',len(alltargets)==336 and all(NI.reduce(x)==0 for x in alltargets))
# Track homogeneous lifts through the original q/t/r generators, never just remainders.
ngb_lift=[list(g.lift(NI)) for g in ngb]
ck('ninth_Groebner_original_generator_identities',all(sum((a*b for a,b in zip(h,ngens)),P(0))==g for h,g in zip(ngb_lift,ngb)))
def original_lift(target):
 result=[P(0)]*len(ngens);work=target
 while work:
  for g,h in zip(ngb,ngb_lift):
   if all(a>=b for a,b in zip(work.lm().exponents()[0],g.lm().exponents()[0])):
    exp=tuple(a-b for a,b in zip(work.lm().exponents()[0],g.lm().exponents()[0]));factor=P({exp:work.lc()/g.lc()});work-=factor*g
    result=[x+factor*y for x,y in zip(result,h)];break
  else:raise AssertionError('unremoved ninth source')
 return result
ninthlifts=[original_lift(x) for x in alltargets]
ck('all336_original_ninth_lift_identities',all(sum((a*b for a,b in zip(h,ngens)),P(0))==g for h,g in zip(ninthlifts,alltargets)))
gendeg=[2]*7+[3]*len(tq)+[4]*len(rqt)
ck('all336_ninth_lifts_homogeneous',all(all(not a or all(sum(e)==(3 if i<168 else 4)-d for e in a.dict()) for a,d in zip(h,gendeg)) for i,h in enumerate(ninthlifts)))
ctrl('q_kernel_alone_does_not_preserve_eighth',any(tq))
ctrl('coupled_ninth_ideal_still_not_surjective',NI.reduce(w[6]**9)!=0)
nlm=[tuple(g.lm().exponents()[0]) for g in ngb]
ndim=sum(not any(all(a>=b for a,b in zip(tuple(z.count(i) for i in range(7)),e)) for e in nlm) for z in combinations_with_replacement(range(7),9))
ck('coupled_ninth_quotient283',ndim==283)
ninth['universal_boundary']={'constant_qt_rank':31,'constant_qt_kernel_dimension':130,'kernel_vectors':[[str(x) for x in h] for h in Cqt.rows()],'tq_generators':list(map(str,tq)),'rqt_generators':list(map(str,rqt)),'groebner_basis':list(map(str,ngb)),'original_targets':list(map(str,alltargets)),'original_generator_lifts':[{str(j):str(x) for j,x in enumerate(h) if x} for h in ninthlifts],'quotient_degree9_dimension':283,'scope':'All ninth boundary sources 84t(R6W)+126r(R5W) from arbitrary repeated R5W/R6W are removable while preserving seventh/eighth boundaries. No frame-preserving septic Euler replacement, eighth Euler, all-order or smooth theorem.'}
print('all336 ninth source generators lifted; proper quotient283; universal boundary PASS',flush=True)

print('eighth original boundary lift PASS',flush=True)
Rc=qn['Rc'];fp=qn['fp']
from sage.all import QuadraticField
field=QuadraticField(2,'rt2');root2=field.gen()
def ff(v):v=F(v);return field(v.numerator)/v.denominator
def jlinear(h,a):
 value=field(0)
 for (p,i,j,k),v in Rc.items():
  factor=-F(eta[p]*eta[i]*eta[j]*eta[k],4)*a.get(i,0)*h.get((p,k,j),0)
  if factor:value+=ff(factor)*(ff(v[0])+root2*ff(v[1]))
 for i,av in a.items():
  for j in range(n):value-=ff(eta[i]*eta[j]*av*fp(h,K[j],i,j))
 return value
jcache={}
def jy(h,r):
 key=(tuple(sorted(h.items())),r)
 if key not in jcache:jcache[key]=jlinear(h,alphas[r])
 return jcache[key]
# Continue the released augmented maps, using a split good prime for Q(sqrt2).
prime2=1000000007;sqrt2mod=pow(2,(prime2+1)//4,prime2)
ck('split_prime_root_two',sqrt2mod*sqrt2mod%prime2==2 and sp.isprime(prime2))
def mod2(v):
 co=list(field(v));return sum((int(x.numerator())*pow(int(x.denominator()),-1,prime2)%prime2)*pow(sqrt2mod,i,prime2) for i,x in enumerate(co))%prime2
allhs={tuple(sorted(h.items())):h for h in rep}
for name,part in linear:
 for h in part.values():allhs[tuple(sorted(h.items()))]=h
jcoeff={}
for hh,h in allhs.items():
 ac=[mod2(jy(h,r)) for r in range(7)];bc={}
 for r in range(7):
  for s0 in range(7):
   for t in range(7):
    v=-sum(F(eta[i]*eta[j],2)*av*bv*fp(KE[t],h,i,j) for i,av in alphas[r].items() for j,bv in alphas[s0].items())
    if v:bc[r,s0,t]=mod2(ff(v))
 jcoeff[hh]=(ac,bc)
print('augmented original scalar coefficient banks',len(jcoeff),flush=True)
ss2=[[[ (receivers.index(ij),mod2(ff(v))) for ij,v in symbol(h,a).items()] for a in alphas] for h in rep]
ls2=[(name,{(r,t):[(receivers.index(ij),mod2(ff(v))) for ij,v in symbol(hh,alphas[r]).items()] for t,hh in h.items() for r in range(7)}) for name,h in linear]
augfull=[]
for degree in [4]:
 mons=list(combinations_with_replacement(range(7),degree));mi={m:i for i,m in enumerate(mons)};bas={};pivs=[];cols_hash=hashlib.sha256();cnt=0
 def eadd(out,m,vals,factor):
  off=106*mi[m]
  for ij,v in vals:
   k=off+ij;z=(out.get(k,0)+factor*v)%prime2
   if z:out[k]=z
   elif k in out:del out[k]
 def jadd(out,m,h):
  counts=Counter(m);ac,bc=jcoeff[tuple(sorted(h.items()))]
  for r,mul in counts.items():
   rest=list(m);rest.remove(r);eadd(out,tuple(rest),[(105,ac[r])],mul)
  for (r,s0,t),val in bc.items():
   mult=counts[r]*(counts[s0]-(r==s0))
   if mult:
    rest=list(m);rest.remove(r);rest.remove(s0);rest.append(t);eadd(out,tuple(sorted(rest)),[(105,val)],mult)
 def accum(name,col):
  global cnt
  cnt+=1;cols_hash.update(repr((name,sorted(col.items()))).encode())
  while col:
   p=min(col);v=col[p]
   if p not in bas:
    iv=pow(v,-1,prime2);bas[p]={k:x*iv%prime2 for k,x in col.items()};pivs.append([name,p]);return
   for k,x in bas[p].items():
    z=(col.get(k,0)-v*x)%prime2
    if z:col[k]=z
    elif k in col:del col[k]
 for m in combinations_with_replacement(range(7),degree+1):
  for hi,h in enumerate(rep):
   out={}
   for r,mul in Counter(m).items():
    rest=list(m);rest.remove(r);eadd(out,tuple(rest),ss2[hi][r],mul)
   jadd(out,m,h);accum(['constant',list(m),hi],out)
 for m in mons:
  counts=Counter(m)
  for (name,part),(same,block) in zip(linear,ls2):
   out={}
   for (r,t),vals in block.items():
    mul=counts[r]+(r==t)
    if mul:
     rest=list(m)+[t];rest.remove(r);eadd(out,tuple(sorted(rest)),vals,mul)
   for t,h in part.items():jadd(out,tuple(sorted(m+(t,))),h)
   accum([list(name),list(m)],out)
 expected=104*comb(degree+6,6)-comb(degree+4,6)+len(mons)
 print('augmented T',degree,'rank',len(bas),'upper',expected,flush=True)
 augfull.append({'degree':degree,'columns':cnt,'rank':len(bas),'upper':expected,'column_sha256':cols_hash.hexdigest(),'pivots':pivs})
 if len(bas)!=expected:break

ck('new_augmented_quintic_boundary_rank22022',len(augfull)==1 and augfull[0]['rank']==22022)
oldaug=prior['sixth_Euler_boundary_discriminator']['augmented_maps']
fullrank=sum(comb(10-k,6)*x['rank'] for k,x in enumerate(oldaug+augfull))
ck('full_shared_fifthEuler_seventhCompatibility_rank249795',fullrank==247415+2380)
ctrl('1716_is_not_seventhEuler_receiver_count',comb(17,4)==2380 and comb(13,7)==1716)

# Independent original polarized replay on both field components and repeated slots.
fixturesJ={(0,0,1,2,3):rep[31],(4,5,5,7,8):rho(KE[3],0,5),(1,1,3,6,9):rep[70]}
factorsJ={m:(root2 if j==2 else field(1)) for j,m in enumerate(fixturesJ)}
derivJ={m:add((F(1,len(set(permutations(m)))),h)) for m,h in fixturesJ.items()}
def getJ(ids):
 t=tuple(sorted(ids));return derivJ.get(t,{}),factorsJ.get(t,field(1))
polyJ=defaultdict(lambda:field(0));omittedJ=defaultdict(lambda:field(0))
for m,h in fixturesJ.items():
 counts=Counter(m);fac=factorsJ[m]
 for i,mul in counts.items():
  rest=list(m);rest.remove(i);polyJ[tuple(rest)]+=fac*field(4)/5*mul*jlinear(h,{i:F(1)})
 for i,ci in counts.items():
  for j,cj in counts.items():
   mult=ci*(cj-(i==j))
   if not mult:continue
   rest=list(m);rest.remove(i);rest.remove(j)
   for t,kt in enumerate(K):
    v=-fac*ff(F(2*eta[i]*eta[j]*mult,5)*fp(kt,h,i,j));polyJ[tuple(sorted(rest+[t]))]+=v;omittedJ[tuple(sorted(rest+[t]))]+=v
rawJ={}
for ids in combinations_with_replacement(range(n),4):
 val=field(0)
 for (p,i,j,k),v in Rc.items():
  hh,fac=getJ((*ids,i));hv=hh.get((p,k,j),0)
  if hv:val-=fac*ff(eta[p]*eta[i]*eta[j]*eta[k]*hv)*(ff(v[0])+root2*ff(v[1]))
 for i in range(n):
  hh,fac=getJ((*ids,i))
  if hh:
   for j in range(n):val-=fac*ff(4*eta[i]*eta[j]*fp(hh,K[j],i,j))
  for j in range(n):
   for pos,t in enumerate(ids):
    pre=ids[:pos]+ids[pos+1:];hh,fac=getJ((*pre,i,j))
    if hh:val-=fac*ff(2*eta[i]*eta[j]*fp(hh,K[t],i,j))
 rawJ[ids]=len(set(permutations(ids)))*val
ck('all2380_original_J4_polarized_receivers',len(rawJ)==2380 and all(rawJ.get(t,0)==polyJ.get(t,0) for t in set(rawJ)|set(polyJ)))
ck('J4_both_field_components_exercised',any(list(v)[1] for v in rawJ.values()) and any(list(v)[0] for v in rawJ.values()))
ctrl('J4_external_K_Leibniz_terms_required',any(omittedJ.values()))
ctrl('quartic_normalization_fails_on_quintic',any(rawJ.values()) and any(rawJ.get(t,0)!=field(5)/4*polyJ.get(t,0) for t in rawJ))
fixture_digest=hashlib.sha256(repr(sorted((t,str(v)) for t,v in rawJ.items() if v)).encode()).hexdigest()

report={'result_id':'K2427','checks':checks,'controls':controls,'inherited_checks':inherited_checks,'inherited_controls':inherited_controls,'boundary':boundary,'ninth_boundary_discriminator':ninth,'new_augmented_map':augfull,'full_augmented_quintic_rank':fullrank,'original_J4_receivers':2380,'original_J4_fixture_sha256':fixture_digest,'scope':'Shared repeated-frame boundary extension and seventh-Euler compatibility; no all-order, convergence, smooth solution or native GU claim.'}
deps=['tests/channel-swings/k2425_frame_euler_module_probe.py','lab/process/k2425-frame-euler-module.json','lab/process/k2423-corotating-mixed-sixth.json','lab/process/k2420-coupled-nuisance-image.json','tests/channel-swings/k2405_fifth_euler_compatibility_probe.py']
report['dependencies']={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps};report=json.loads(json.dumps(report));out=ROOT/'lab/process/k2427-frame-boundary-quotient.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:assert json.loads(out.read_text())==report
print(json.dumps({'checks':len(checks),'controls':len(controls),'rank':fullrank}))
