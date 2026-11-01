"""Original frame-Euler extension: new minors and full polarized compatibility."""
from pathlib import Path
import json,sys,hashlib,ast
ROOT=Path(__file__).resolve().parents[2]
_k25path=ROOT/'tests/channel-swings/k2425_frame_euler_module_probe.py';_k25text=_k25path.read_text()
exec(compile(_k25text[:_k25text.index('ss=[[symbol')],str(_k25path),'exec'),globals())
inherited_checks=dict(checks);checks={};controls={}
prior=json.loads((ROOT/'lab/process/k2425-frame-euler-module.json').read_text())
prior27=json.loads((ROOT/'lab/process/k2427-frame-boundary-quotient.json').read_text())
ck('prior25_dependencies_current',all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in prior['dependencies'].items()))
ck('prior27_dependencies_current',all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in prior27['dependencies'].items()))
ss=[[symbol(h,a) for a in alphas] for h in rep];ls=[(name,{(r,t):symbol(hh,alphas[r]) for t,hh in h.items() for r in range(7)}) for name,h in linear]
prime=1000003
ck('rational_rank_prime',sp.isprime(prime))
def mod(v):v=F(v);assert v.denominator%prime;return v.numerator*pow(v.denominator,-1,prime)%prime
ss=[[[ (receivers.index(ij),mod(v)) for ij,v in c.items()] for c in row] for row in ss]
ls=[(name,{key:[(receivers.index(ij),mod(v)) for ij,v in c.items()] for key,c in block.items()}) for name,block in ls]
results=[]
for degree in [6]:
 start=time.time();mons=list(combinations_with_replacement(range(7),degree));mi={m:i for i,m in enumerate(mons)};basis={};pivot_ids=[];digestcols=hashlib.sha256();count=0
 def coladd(out,mon,vals,factor):
  off=105*mi[mon]
  for ij,v in vals:
   key=off+ij;z=(out.get(key,0)+factor*v)%prime
   if z:out[key]=z
   elif key in out:del out[key]
 def accept(name,col):
  global count
  count+=1;digestcols.update(repr((name,sorted(col.items()))).encode())
  while col:
   pivot=min(col);v=col[pivot]
   if pivot not in basis:
    iv=pow(v,-1,prime);basis[pivot]={j:x*iv%prime for j,x in col.items()};pivot_ids.append([name,pivot]);return
   for j,x in basis[pivot].items():
    z=(col.get(j,0)-v*x)%prime
    if z:col[j]=z
    elif j in col:del col[j]
 for mon in combinations_with_replacement(range(7),degree+1):
  counts=Counter(mon)
  for hi,cols in enumerate(ss):
   out={}
   for r,mul in counts.items():
    rest=list(mon);rest.remove(r);coladd(out,tuple(rest),cols[r],mul)
   accept(['constant',list(mon),hi],out)
 for mon in mons:
  counts=Counter(mon)
  for name,block in ls:
   out={}
   for (r,t),vals in block.items():
    mul=counts[r]+(r==t)
    if mul:
     rest=list(mon)+[t];rest.remove(r);coladd(out,tuple(sorted(rest)),vals,mul)
   accept([list(name),list(mon)],out)
 expected=104*comb(degree+6,6)-(comb(degree+4,6) if degree>=2 else 0)
 print('T',degree,'rank',len(basis),'expected',expected,'columns',count,'seconds',round(time.time()-start,2),flush=True)
 results.append({'degree':degree,'rows':105*len(mons),'columns':count,'rank_mod_prime':len(basis),'universal_upper':expected,'column_sha256':digestcols.hexdigest(),'pivot_original_columns_and_rows':pivot_ids})
 # A failed candidate rank is scientific evidence, not a fabricated success.
 if len(basis)!=expected:break

ck('ordinary_T6_original_minor',len(results)==1 and results[0]['rank_mod_prime']==95886==results[0]['universal_upper'])
oldmaps=prior['transverse_ranks']
full_septic_rank=sum(comb(12-k,6)*x['rank_mod_prime'] for k,x in enumerate(oldmaps+results))
ck('literal_frame_septic_Euler_full_image',full_septic_rank==2819348)
qpath=ROOT/'tests/channel-swings/k2405_fifth_euler_compatibility_probe.py';qsrc=qpath.read_text();qn={'__file__':str(qpath),'__name__':'lowerS'}
exec(compile(qsrc[:qsrc.index('# Pair-field covariant derivative')],str(qpath),'exec'),qn)
for node in ast.parse(qsrc).body:
 if isinstance(node,ast.FunctionDef) and node.name=='fp':exec(compile(ast.Module(body=[node],type_ignores=[]),str(qpath),'exec'),qn)
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
for degree in [5]:
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


ck('augmented_T5_original_minor',len(augfull)==1 and augfull[0]['rank']==48426==augfull[0]['upper'])
oldaug=prior['sixth_Euler_boundary_discriminator']['augmented_maps']+prior27['new_augmented_map']
fullrank=sum(comb(11-k,6)*x['rank'] for k,x in enumerate(oldaug+augfull))
ck('shared_sixth_Euler_eighth_compatibility_image',fullrank==899080==890512+8568)

from itertools import permutations
# Independent original polarized replay on both field components and repeated slots.
fixturesJ={(0,0,1,2,3,6):rep[31],(4,5,5,7,8,10):rho(KE[3],0,5),(1,1,3,6,9,11):rep[70]}
factorsJ={m:(root2 if j==2 else field(1)) for j,m in enumerate(fixturesJ)}
derivJ={m:add((F(1,len(set(permutations(m)))),h)) for m,h in fixturesJ.items()}
def getJ(ids):
 t=tuple(sorted(ids));return derivJ.get(t,{}),factorsJ.get(t,field(1))
polyJ=defaultdict(lambda:field(0));omittedJ=defaultdict(lambda:field(0))
for m,h in fixturesJ.items():
 counts=Counter(m);fac=factorsJ[m]
 for i,mul in counts.items():
  rest=list(m);rest.remove(i);polyJ[tuple(rest)]+=fac*field(2)/3*mul*jlinear(h,{i:F(1)})
 for i,ci in counts.items():
  for j,cj in counts.items():
   mult=ci*(cj-(i==j))
   if not mult:continue
   rest=list(m);rest.remove(i);rest.remove(j)
   for t,kt in enumerate(K):
    v=-fac*ff(F(eta[i]*eta[j]*mult,3)*fp(kt,h,i,j));polyJ[tuple(sorted(rest+[t]))]+=v;omittedJ[tuple(sorted(rest+[t]))]+=v
rawJ={}
for ids in combinations_with_replacement(range(n),5):
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
ck('all8568_original_J5_polarized_receivers',len(rawJ)==8568 and all(rawJ.get(t,0)==polyJ.get(t,0) for t in set(rawJ)|set(polyJ)))
ck('J5_both_field_components_exercised',any(list(v)[1] for v in rawJ.values()) and any(list(v)[0] for v in rawJ.values()))
ctrl('J5_external_K_Leibniz_terms_required',any(omittedJ.values()))
ctrl('quartic_normalization_fails_on_sextic',any(rawJ.values()) and any(rawJ.get(t,0)!=field(3)/2*polyJ.get(t,0) for t in rawJ))
fixture_digest=hashlib.sha256(repr(sorted((t,str(v)) for t,v in rawJ.items() if v)).encode()).hexdigest()


# Outcome-released tenth-boundary test, using original hooks rather than ideal names.
exec(compile(_k25text[_k25text.index('from sage.all import QuadraticField,PolynomialRing,matrix'):_k25text.index('target=P(0)',_k25text.index('from sage.all import QuadraticField,PolynomialRing,matrix'))],str(_k25path),'exec'),globals())
z=add((1,rep[133]),(-1,rep[136]))
ck('tenth_counterdirection_exact_norm_minus2',gram(z,z)==-2)
ck('tenth_direction_original_q_zero',all(gram(z,h)==0 for part in lws for h in part))
ck('tenth_direction_original_t_zero',all(gram(z,h)==0 for part in T3 for h in part.values()))
ck('tenth_direction_original_r_zero',all(gram(z,h)==0 for part in r4 for h in part.values()))
# Z is w0=w1=w2=0. Check tensors, not only ideal membership of their pairings.
ck('N_vanishes_on_Z',all(not h or any(i<3 for i in mon) for part in lws for mon,h in zip(qm,part)))
ck('T_vanishes_on_Z',all(not h or any(i<3 for i in mon) for part in T3 for mon,h in part.items()))
ck('R4_vanishes_on_Z',all(not h or any(i<3 for i in mon) for part in r4 for mon,h in part.items()))
# The lambda^2 coefficient is nonzero independently of the unselected R5 base.
tenth_quadratic=126*ff(gram(z,z))*w[6]**10
ck('tenth_coefficient_minus252',tenth_quadratic==-252*w[6]**10)
ctrl('ninth_boundary_does_not_force_tenth',tenth_quadratic!=0)
ck('tenth_binomial_factors', [comb(10,j) if j<5 else comb(10,5)//2 for j in [1,2,3,4,5]]==[10,45,120,210,126])
# Independent Gram nondegeneracy on original full repeated space.
repeated_basis=hs[:168];Grep=matrix(field,[[ff(gram(a,b)) for b in repeated_basis] for a in repeated_basis])
ck('full_repeated_Gram_rank168',Grep.rank()==168)
tenth={'common_zero_locus':'w0=w1=w2=0','counterdirection':[[list(k),str(v)] for k,v in sorted(z.items())],'norm':'-2','original_q_t_r_annihilation':True,'lambda_squared_boundary_coefficient':str(tenth_quadratic),'full_repeated_Gram_rank':168,'scope':'A free quintic boundary direction preserves orders seven through nine and exposes a nonzero tenth quadratic coefficient. At least one of any three distinct lambda values fails the necessary tenth condition; no exclusion of the whole selectable quintic fiber.'}

# Same-assumption repair: discriminate the tempting small family, then the full
# rational K-polar constant kernel. These are original contractions, not quotient tests.
from sage.all import QQ
banks=[g for part in lws for g in part]+[g for part in T3 for g in part.values()]+[g for part in r4 for g in part.values()]
simple=[]
for j in [7,0,4,5,6,9]:
 h={(8,8,j):1,(8,j,8):-1,(12,12,j):1,(12,j,12):-1}
 simple.append({'label':j,'norm':str(gram(h,h)),'raw_joint_kernel':all(gram(h,g)==0 for g in banks)})
ctrl('simple_positive_contrasts_do_not_preserve_raw_boundaries',all(x['norm']=='2' and not x['raw_joint_kernel'] for x in simple))
# QQ conversion is an exact rational-carrier assertion; no field extension is hidden.
Mrepair=matrix(QQ,[[QQ(str(gram(h,g))) for h in repeated_basis] for g in banks+list(KE)+[z]])
Krepair=Mrepair.right_kernel().basis_matrix();Grepair=matrix(QQ,[[QQ(str(gram(a,b))) for b in repeated_basis] for a in repeated_basis]);Hrepair=Krepair*Grepair*Krepair.transpose()
ck('rational_polar_joint_kernel_and_z_orthogonality',Mrepair.nrows()==652 and Mrepair.rank()+Krepair.nrows()==168 and not Mrepair*Krepair.transpose())
ck('rational_restricted_Gram_rank_at_least5',Hrepair.rank()>=5)
positive=None
for i in range(Krepair.nrows()):
 for j in range(i,Krepair.nrows()):
  for sign in [1,-1]:
   v=Krepair[i] if i==j else Krepair[i]+sign*Krepair[j];norm=v*Grepair*v
   if norm>0:positive=(i,j,sign,v,norm);break
  if positive:break
 if positive:break
ck('rational_kernel_contains_positive_vector',positive is not None)
pi,pj,ps,pv,pnorm=positive
ph=add(*[(F(str(c)),h) for c,h in zip(pv,repeated_basis) if c])
ck('positive_witness_original_contractions',gram(ph,ph)==F(str(pnorm)) and gram(ph,z)==0 and all(gram(ph,g)==0 for g in banks+list(KE)))
positive_square=bool(field(2/pnorm).is_square())
n0={(5,5,0):1,(5,0,5):-1,(6,6,0):1,(6,0,6):-1,(8,8,0):-2,(8,0,8):2,(5,5,1):1,(5,1,5):-1,(6,6,1):1,(6,1,6):-1,(8,8,1):-2,(8,1,8):2}
ck('explicit_nonzero_rational_null_deformation',bool(n0) and gram(n0,n0)==0 and gram(n0,z)==0 and all(gram(n0,g)==0 for g in banks+list(KE)))
ctrl('null_alternative_does_not_cancel_negative_z',gram(add((1,z),(1,n0)),add((1,z),(1,n0)))==-2)
tenth['repair']={'simple_candidates':simple,'rational_matrix_shape':[Mrepair.nrows(),Mrepair.ncols()],'constraint_rank':Mrepair.rank(),'kernel_dimension':Krepair.nrows(),'restricted_Gram_rank':Hrepair.rank(),'kernel_basis_sha256':hashlib.sha256(repr(Krepair).encode()).hexdigest(),'positive_basis_indices_and_sign':[pi,pj,ps],'positive_norm':str(pnorm),'positive_rescaling_square_in_Qsqrt2':positive_square,'explicit_null_hook':[[list(k),str(v)] for k,v in sorted(n0.items())],'meyer_consequence':'A nonsingular rational complement of rank at least5 has a positive direction. Meyer applied to Q(v)-2t^2 proves existence of a rational p perpendicular to z with norm2; the note handles t=0. This is existence, not an extracted norm2 witness or affine quintic solution.'}

report={'result_id':'K2429','checks':checks,'controls':controls,'inherited_checks':inherited_checks,'new_ordinary_map':results,'new_augmented_map':augfull,'full_septic_frame_rank':full_septic_rank,'full_sextic_augmented_rank':fullrank,'original_J5_receivers':8568,'original_J5_fixture_sha256':fixture_digest,'tenth_boundary':tenth,'scope':'Conditional finite jet; common eighth Euler/ninth algebraic requires the written same-coefficient assembly. No all-order or smooth field.'}
deps=['tests/channel-swings/k2425_frame_euler_module_probe.py','tests/channel-swings/k2427_frame_boundary_quotient_probe.py','lab/process/k2425-frame-euler-module.json','lab/process/k2427-frame-boundary-quotient.json','tests/channel-swings/k2405_fifth_euler_compatibility_probe.py']
report['dependencies']={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps};report=json.loads(json.dumps(report));out=ROOT/'lab/process/k2429-shared-eighth-euler-extension.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:assert json.loads(out.read_text())==report
print(json.dumps({'checks':len(checks),'controls':len(controls),'ordinary_rank':full_septic_rank,'augmented_rank':fullrank}))
