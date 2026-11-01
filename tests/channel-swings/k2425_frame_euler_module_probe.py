"""Original transverse frame-Euler module ranks; modular lower certificates."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
from itertools import combinations,combinations_with_replacement
from math import comb
import json,hashlib,sys,time
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'tests/channel-swings/k2421_mixed_sixth_structural_reduction_probe.py';src=p.read_text()
exec(compile(src[:src.index('# Reuse only ordinary-polynomial')],str(p),'exec'),globals())
inherited_checks=dict(checks);checks={};controls={}
rep=[h for h in tk if all(len(set(k))<3 for k in h)]
ck('repeated_polar_basis161',len(rep)==161)
def symbol(h,a):return clean({ij:sum(eta[m]*v*(h.get((ij[0],m,ij[1]),0)+h.get((ij[1],m,ij[0]),0)) for m,v in a.items()) for ij in receivers})
# Every linear generator preserves G(K,Z); rotations preserve sigma as well.
linear=[]
for a,b in combinations(range(7),2):linear.append((('koszul',a,b),{b:Jr[a],a:add((-1,Jr[b]))}))
for a,b in combinations(range(n),2):linear.append((('rotation',a,b),{r:add((4,rho(h,a,b))) for r,h in enumerate(KE)}))
ck('all112_linear_generators_pointwise_Gram_zero',all(all(sum(gram(KE[t[pos]],h.get(t[1-pos],{})) for pos in range(2))==0 for t in combinations_with_replacement(range(7),2)) for name,h in linear))
ss=[[symbol(h,a) for a in alphas] for h in rep];ls=[(name,{(r,t):symbol(hh,alphas[r]) for t,hh in h.items() for r in range(7)}) for name,h in linear]
prime=1000003
ck('rational_rank_prime',sp.isprime(prime))
def mod(v):v=F(v);assert v.denominator%prime;return v.numerator*pow(v.denominator,-1,prime)%prime
ss=[[[ (receivers.index(ij),mod(v)) for ij,v in c.items()] for c in row] for row in ss]
ls=[(name,{key:[(receivers.index(ij),mod(v)) for ij,v in c.items()] for key,c in block.items()}) for name,block in ls]
results=[]
for degree in range(6):
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
ck('all_four_transverse_images_maximal',len(results)==6 and all(x['rank_mod_prime']==x['universal_upper'] for x in results[:4]))
rank=sum(comb(9-k,6)*x['rank_mod_prime'] for k,x in enumerate(results[:4]))
ck('triangular_full_image_rank',rank==58226)
ck('fifth_Euler_frame_image247415',sum(comb(10-k,6)*x['rank_mod_prime'] for k,x in enumerate(results[:5]))==247415)
ck('sixth_Euler_polar_image890512',sum(comb(11-k,6)*x['rank_mod_prime'] for k,x in enumerate(results))==890512)
ctrl('boundary_rank_alone_not_certificate',results[0]['rank_mod_prime']<rank)
# Independent ambient polynomial replay of the algebraically admissible lifts.
import ast
p17=ROOT/'tests/channel-swings/k2417_coupled_three_w_compatibility_probe.py';s17=p17.read_text()
for node in ast.parse(s17).body:
 if isinstance(node,ast.FunctionDef) and node.name in ['pad','ppair','pairpoly','combine','ambient']:
  exec(compile(ast.Module(body=[node],type_ignores=[]),str(p17),'exec'),globals())
def rotate(h,a):return add(*[(v,rho(h,u,w)) for (u,w),v in a.items()])
def op(rot,P):
 out=[{},{}]
 for pa,pb,ip,c in [(0,0,0,1),(1,1,0,2),(0,1,1,1),(1,0,1,1)]:
  for m,a in rot[pa].items():
   for t,h in P[pb].items():pad(out[ip],tuple(sorted(m+t)),c,rotate(h,a))
 return out
kap=[{(r,):KE[r] for r in range(7)},{}]
adA=[{(r,):add(*[(v,A[ip][a]) for a,v in vec[r].items()]) for r in range(n)} for ip in range(2)]
def evalL(ip,a,b):return add(*[(v*w,L[ip][tuple(sorted((i,j)))]) for i,v in vec[a].items() for j,w in vec[b].items()])
ell=[{(a,b):add((1 if a==b else 2,evalL(ip,a,b))) for a,b in receivers} for ip in range(2)]
nn=combine(ell,op(adA,kap),-2)
cubic=[{(0,7,7):{(2,4):F(1)},(1,2,8):{(0,5):F(2,3)}},{(3,8,8):{(1,6):F(-3,5)}}]
zz=combine([{},{}],op(cubic,kap),4)
vv=combine(combine([{},{}],op(cubic,nn),10),op(adA,op(cubic,kap)),20)
def six(z,v):return combine([{m:add((6,h)) for m,h in part.items()} for part in pairpoly(kap,v)],pairpoly(ell,z),15)
ck('rotation_original_fifth_identity',not any(pairpoly(kap,zz)))
ck('rotation_original_sixth_identity',not any(six(zz,vv)))
wrong=combine([{},{}],op(cubic,ell),10)
ck('simpler_rotation_sixth_lift_also_valid',not any(six(zz,wrong)))
ctrl('simplified_lift_is_not_literal_frame_jet',any(combine(vv,wrong,-1)))
ctrl('wrong_rotation_sixth_factor_detected',any(six(zz,combine([{},{}],op(cubic,ell),9))))
syz=[{(0,0,1,7):Jr[2],(0,0,2,7):add((-1,Jr[1]))},{}]
ck('mixed_repeated_Koszul_fifth_identity',not any(pairpoly(kap,syz)))
sv=combine([{},{}],op(adA,syz),5);raw=six(syz,sv)
ck('Koszul_sixth_sigma_cancels',all(all(k==() for k in h) for part in raw for h in part.values()))
for ip,part in enumerate(raw):
 for m,h in part.items():
  r=next(x for x in m if x<7);rest=list(m);rest.remove(r);pad(sv[ip],tuple(rest),-h[()]/6,Jr[r])
ck('Koszul_shared_Gram_repair',not any(six(syz,sv)))
ka=[{(a,):h for a,h in enumerate(K) if h},{}];la=[{mon:add((1 if mon[0]==mon[1] else 2,h)) for mon,h in part.items()} for part in L]
for label,z,v in [('rotation',zz,vv),('Koszul',syz,sv)]:
 za=[ambient(part) for part in z];va=[ambient(part) for part in v]
 residual=combine([{m:add((6,h)) for m,h in part.items()} for part in pairpoly(ka,va)],pairpoly(la,za),15)
 ck(label+'_ambient_sixth_replay',not any(residual))
 def euler(P,coframe,wrong=False):
  out=[{},{}]
  for ip,part in enumerate(P):
   for m,h in part.items():
    for r in set(m):
     rest=list(m);rest.remove(r);pad(out[ip],tuple(rest),1 if wrong else m.count(r),symbol(h,coframe[r]))
  return out
 adapted=euler(z,covs);aout=[ambient(part) for part in adapted]
 original=euler(za,[{i:F(1)} for i in range(n)])
 ck(label+'_all_ambient_Euler_entries',not any(combine(original,aout,-1)))
 ctrl(label+'_wrong_derivative_multiplicity_detected',any(combine(euler(z,covs,True),adapted,-1)))

# Outcome-released sixth-Euler compatibility boundary discriminator.
# Derive the U-linear part before setting H=0; lower jets remain fixed.
qpath=ROOT/'tests/channel-swings/k2405_fifth_euler_compatibility_probe.py';qsrc=qpath.read_text();qn={'__file__':str(qpath),'__name__':'curvature_only'}
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
augcols=[]
for r in range(7):
 for hi,h in enumerate(rep):
  col={receivers.index(k):ff(v) for k,v in symbol(h,alphas[r]).items()};jv=jy(h,r)
  if jv:col[105]=jv
  augcols.append((['constant',r,hi],col))
for name,hpoly in linear:
 col={};jv=field(0)
 for r,h in hpoly.items():
  for k,v in symbol(h,alphas[r]).items():col[receivers.index(k)]=col.get(receivers.index(k),field(0))+ff(v)
  jv+=jy(h,r)
 if jv:col[105]=jv
 augcols.append((list(name),{k:v for k,v in col.items() if v}))
ab={};ap=[]
for name,col0 in augcols:
 col=dict(col0)
 while col:
  p=min(col);v=col[p]
  if p not in ab:ab[p]={k:x/v for k,x in col.items()};ap.append([name,p]);break
  for k,x in ab[p].items():
   z=col.get(k,field(0))-v*x
   if z:col[k]=z
   elif k in col:del col[k]
aug={'columns':len(augcols),'exact_Qsqrt2_rank':len(ab),'universal_surjectivity_target':105,'pivot_original_columns':ap}
if len(ab)==104:
 du={105:field(1)}
 for p in sorted(ab,reverse=True):
  v=-sum(x*du.get(k,field(0)) for k,x in ab[p].items() if k!=p)
  if v:du[p]=v
 ck('augmented_boundary_original_dual_all1239',all(sum(v*col.get(k,field(0)) for k,v in du.items())==0 for name,col in augcols))
 aug['dual']=[[k,str(v)] for k,v in sorted(du.items())];aug['scope']='Additional scalar is determined by Euler on the transverse linear boundary; this excludes universal independent control, not the actual affine compatibility target.'
else:
 ck('augmented_boundary_surjective',len(ab)==105)
 aug['scope']='Transverse linear boundary controls its scalar compatibility independently; higher mixed blocks remain to be tested.'
print('augmented sixth-Euler boundary exact rank',len(ab),flush=True)

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
for degree in range(4):
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
 expected=results[degree]['universal_upper']+len(mons)
 print('augmented T',degree,'rank',len(bas),'upper',expected,flush=True)
 augfull.append({'degree':degree,'columns':cnt,'rank':len(bas),'upper':expected,'column_sha256':cols_hash.hexdigest(),'pivots':pivs})
 if len(bas)!=expected:break
ck('all_four_augmented_images_maximal',len(augfull)==4 and all(x['rank']==x['upper'] for x in augfull))
ck('shared_fourthEuler_and_560_sixthCompatibility_image',sum(comb(9-k,6)*x['rank'] for k,x in enumerate(augfull))==58786)
aug['augmented_maps']=augfull;aug['prime']=prime2;aug['sqrt2_mod_prime']=sqrt2mod;aug['scope']='All560 sixth-Euler compatibility values can be independently prescribed while retaining fourthEuler and fifth/sixth algebraic/W4. This augmented map alone does not prove seventh algebraic; the separate exact boundary lift and later Euler maps below supply that shared completion.'

# Independent original symmetric-tensor replay of the complete J3 linear operator.
# Deliberately not restricted to the correction family, to expose all Leibniz terms.
from itertools import permutations
fixturesJ={(0,0,1,2):rep[31],(4,5,5,7):rho(KE[3],0,5)}
derivJ={m:add((F(1,len(set(permutations(m)))),h)) for m,h in fixturesJ.items()}
def getJ(ids):return derivJ.get(tuple(sorted(ids)),{})
polyJ=defaultdict(lambda:field(0));omittedJ=defaultdict(lambda:field(0))
for m,h in fixturesJ.items():
 counts=Counter(m)
 for i,mul in counts.items():
  rest=list(m);rest.remove(i);polyJ[tuple(rest)]+=mul*jlinear(h,{i:F(1)})
 for i,ci in counts.items():
  for j,cj in counts.items():
   mult=ci*(cj-(i==j))
   if not mult:continue
   rest=list(m);rest.remove(i);rest.remove(j)
   for t,kt in enumerate(K):
    v=-ff(F(eta[i]*eta[j]*mult,2)*fp(kt,h,i,j));polyJ[tuple(sorted(rest+[t]))]+=v;omittedJ[tuple(sorted(rest+[t]))]+=v
rawJ={}
for a,b,c in combinations_with_replacement(range(n),3):
 val=field(0)
 for (p,i,j,k),v in Rc.items():
  hv=getJ((a,b,c,i)).get((p,k,j),0)
  if hv:val-=ff(eta[p]*eta[i]*eta[j]*eta[k]*hv)*(ff(v[0])+root2*ff(v[1]))
 for i in range(n):
  h=getJ((a,b,c,i))
  if h:
   for j in range(n):val-=ff(4*eta[i]*eta[j]*fp(h,K[j],i,j))
  for j in range(n):
   for pre,kt in [((a,b),K[c]),((a,c),K[b]),((b,c),K[a])]:
    h=getJ((*pre,i,j))
    if h:val-=ff(2*eta[i]*eta[j]*fp(h,kt,i,j))
 rawJ[a,b,c]=len(set(permutations((a,b,c))))*val
ck('all560_J3_original_polarized_receivers',all(rawJ.get(t,0)==polyJ.get(t,0) for t in set(rawJ)|set(polyJ)))
ctrl('omitting_external_K_Leibniz_terms_fails',any(omittedJ.values()))
# A genuinely mixed ambient fixture must exercise the new term.
ck('J3_fixture_nonzero',any(rawJ.values()))
aug['original_polarized_J3_fixture_targets']=560
aug['J3_fixture_sha256']=hashlib.sha256(repr(sorted((t,str(v)) for t,v in rawJ.items() if v)).encode()).hexdigest()

from sage.all import QuadraticField,PolynomialRing,matrix
field=QuadraticField(2,'rt2');rt=field.gen();P=PolynomialRing(field,7,'w',order='degrevlex');w=P.gens()
def ff(v):v=F(v);return field(v.numerator)/v.denominator
def mono(t):
 v=P(1)
 for i in t:v*=w[i]
 return v
from itertools import product,permutations
def ev(T,t):
 out={}
 for choices in product(*[list(W[i].items()) for i in t]):
  ids=tuple(sorted(i for i,v in choices));c=F(1)
  for i,v in choices:c*=v
  out=add((1,out),(c,T[ids]))
 return out
qm=list(combinations_with_replacement(range(7),2));lws=[[ev(L[ip],t) for t in qm] for ip in range(2)]
qrows=[[ff(gram(lws[0][j],h))+rt*ff(gram(lws[1][j],h)) for j in range(28)] for h in rep]
Q=matrix(field,qrows);print('exact q rank',Q.rank(),flush=True);piv=Q.transpose().pivots()
qpolys=[sum((1 if a==b else 2)*Q[i,j]*w[a]*w[b] for j,(a,b) in enumerate(qm)) for i in piv]

ideal=P.ideal(qpolys);gb=ideal.groebner_basis();
S=qn['S']
r23=json.loads((ROOT/'lab/process/k2423-corotating-mixed-sixth.json').read_text());r4=[{tuple(m):{tuple(k):F(v) for k,v in h} for m,h in part} for part in r23['changed_W4_repair']['inner_repeated_W4']]
T3=[{} for _ in range(2)]
for ip in range(2):
 for t in combinations_with_replacement(range(7),3):
  h=ev(S[ip],t);h=add((len(set(permutations(t))),h));T3[ip][t]=h
# Subtract3 A_W N_WW on ordinary diagonal coefficients, with field multiplication.
for pa,pb,ip,c in [(0,0,0,1),(1,1,0,2),(0,1,1,1),(1,0,1,1)]:
 for a in range(7):
  aw=add(*[(v,A[pa][i]) for i,v in W[a].items()])
  for j,t in enumerate(qm):
   h=lws[pb][j];rh=add(*[(v,rho(h,u,vv)) for (u,vv),v in aw.items()]);m=tuple(sorted((a,)+t));T3[ip][m]=add((1,T3[ip].get(m,{})),(-3*c*(1 if t[0]==t[1] else 2),rh))
assert all(all(len(set(k))<3 for k in h) for part in T3 for h in part.values())
target=P(0)
for pa,pb,ip,c in [(0,0,0,1),(1,1,0,2),(0,1,1,1),(1,0,1,1)]:
 for t,h in T3[pa].items():
  for u,j in r4[pb].items():
   v=gram(h,j)
   if v:target+=ff(-F(5,3)*c*len(set(permutations(u)))*v)*(rt if ip else 1)*mono(t+u)
rem=ideal.reduce(target)
print('target terms',len(target.dict()),'remainder terms',len(rem.dict()),flush=True)

# Leading monomial count independently gives exact degree7 quotient dimension.
lms=[tuple(g.lm().exponents()[0]) for g in gb];std=[]
for t in combinations_with_replacement(range(7),7):
 exp=tuple(t.count(i) for i in range(7))
 if not any(all(a>=b for a,b in zip(exp,lm)) for lm in lms):std.append(exp)
print('degree7 standard monomials',len(std),flush=True)

ck('allW_seventh_qspan_exact7',Q.rank()==7)
ck('allW_seventh_quotient316',len(std)==316)
ck('actual_allW_seventh_target_in_ideal',rem==0 and len(target.dict())==830)
# Exact constructive lift, tracked back to seven ORIGINAL repeated-hook generators.
qmatrix=matrix(field,[[q.monomial_coefficient(mono(t)) for t in qm] for q in qpolys])
gbmatrix=matrix(field,[[g.monomial_coefficient(mono(t)) for t in qm] for g in gb])
change=qmatrix.transpose().solve_right(gbmatrix.transpose()).transpose()
ck('groebner_generators_original_qspan',change*qmatrix==gbmatrix)
lifts=[P(0) for q in qpolys];work=target
while work:
 for j,g in enumerate(gb):
  if all(a>=b for a,b in zip(work.lm().exponents()[0],g.lm().exponents()[0])):
   exp=tuple(a-b for a,b in zip(work.lm().exponents()[0],g.lm().exponents()[0]));term=P({exp:work.lc()/g.lc()});work-=term*g
   for i in range(len(qpolys)):lifts[i]+=term*change[j,i]
   break
 else:raise AssertionError('nonzero exact ideal remainder')
ck('constructive_allW_seventh_original_q_lift',sum(q*h for q,h in zip(qpolys,lifts))==target)
ck('seventh_lift_homogeneous_degree5',all(all(sum(exp)==5 for exp in h.dict()) for h in lifts))
# Independently reconstruct all1716 original scalar coefficients from hook pairings.
h5={}
for qi,lift in zip(piv,lifts):
 for exp,value in lift.dict().items():
  mon=tuple(i for i,e in enumerate(exp) for _ in range(e));hh=h5.setdefault(mon,{})
  for k,v in rep[qi].items():hh[k]=hh.get(k,field(0))+value*ff(v)
original7=P(0)
for t,hh in h5.items():
 for j,(a,b) in enumerate(qm):
  value=sum((ff(lws[0][j].get(k,0))+rt*ff(lws[1][j].get(k,0)))*ff(F(eta[k[0]]*eta[k[1]]*eta[k[2]],2))*v for k,v in hh.items())
  original7+=(1 if a==b else 2)*value*mono(t+(a,b))
ck('all1716_seventh_original_Gram_receivers',original7==target)
ctrl('seventh_ideal_is_not_surjective',ideal.reduce(w[6]**7)!=0)
ctrl('wrong_seventh_binomial_ratio_detected',original7!=target*field(4)/5)
seventh={'q_rank':int(Q.rank()),'q_original_basis':list(map(int,piv)),'q_generators':list(map(str,qpolys)),'groebner':list(map(str,gb)),'standard_monomials_degree7':len(std),'ideal_rank_degree7':1716-len(std),'target':str(target),'target_terms':len(target.dict()),'remainder':str(rem),'constructive_original_q_lift':list(map(str,lifts)),'original_scalar_receivers':1716,'scope':'Exact fixed-boundary seventh Gram target membership; no all-target surjectivity. Literal frame quintic followed by polar sextic gives one finite shared completion if the recorded Euler image ranks pass.'}

# Identify whether the next boundary can discard the sixth-Gram particular.
r20=json.loads((ROOT/'lab/process/k2420-coupled-nuisance-image.json').read_text())
Jorth=[{tuple(k):F(v) for k,v in h} for h in r20['actual_affine_target']['all_W_sixth_followthrough']['orthogonal_duals']]
ck('seventh_lift_original_Jorth_contract',all(gram(k,h)==(1 if i==j else 0) for i,k in enumerate(KE) for j,h in enumerate(Jorth)) and all(gram(k,h)==0 for part in lws for k in part for h in Jorth))
next_coeffs=[]
for h in Jorth:
 poly=sum((ff(gram(h,hh))*(rt if ip else 1)*mono(t) for ip,part in enumerate(T3) for t,hh in part.items()),P(0))
 next_coeffs.append(ideal.reduce(poly))
seventh['next_boundary_Jorth_T_remainders']=list(map(str,next_coeffs))
seventh['next_boundary_nonzero_Jorth_T_remainders']=sum(bool(x) for x in next_coeffs)
print('next boundary Jorth/T quotient couplings',sum(bool(x) for x in next_coeffs),flush=True)
report={'result_id':'K2425','checks':checks,'controls':controls,'inherited_checks':inherited_checks,'prime':prime,'transverse_ranks':results,'full_quartic_Euler_image_rank':rank,'sixth_Euler_boundary_discriminator':aug,'seventh_algebraic_completion':seventh,'scope':'Original rational modular minors plus universal upper bounds and exact fixed-boundary seventh-Gram ideal lift prove a common finite jet through sixth Euler and seventh algebraic compatibility. No all-order, smooth or native GU solution.'}
report['dependencies']={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT/'tests/channel-swings/k2421_mixed_sixth_structural_reduction_probe.py',ROOT/'tests/channel-swings/k2417_coupled_three_w_compatibility_probe.py',ROOT/'tests/channel-swings/k2405_fifth_euler_compatibility_probe.py',ROOT/'lab/process/k2423-corotating-mixed-sixth.json',ROOT/'lab/process/k2420-coupled-nuisance-image.json',ROOT/'tests/channel-swings/k2393_coupled_polar_dual_probe.py',ROOT/'tests/channel-swings/k2387_coupled_hook_jet_blocks_probe.py',ROOT/'tests/channel-swings/k2390_full_hook_jet_probe.py']}
report=json.loads(json.dumps(report));out=ROOT/'lab/process/k2425-frame-euler-module.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:assert json.loads(out.read_text())==report
print(json.dumps({'checks':len(checks),'controls':len(controls),'rank':rank}))
