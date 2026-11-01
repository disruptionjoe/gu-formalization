"""Complete A-projection replay and exact repeated-hook algebraic lifting."""
from pathlib import Path
p=Path(__file__).resolve().parent/'k2414_inherited_polar_fiber_probe.py';src=p.read_text()
exec(compile(src[:src.index('# One raw three-W dual')],str(p),'exec'),globals())
inherited_checks=dict(checks);checks={};controls={}
exec(compile(s08[s08.index('bas3={}'):s08.index('three=all_threeW')],str(p08),'exec'),globals())
projection=all_threeW(SA)
ck('complete_A_projection_fails66_of168',len(projection['failed_targets'])==66 and projection['residual_entries']==384)
# Derive an original-column annihilator for its first failure.
wt,op=projection['failed_targets'][0];target=defaultdict(F)
for ep in EP:
 slots=[7+x for x in wt]+list(ep)
 for pos in combinations(range(5),2):
  aa=[slots[i] for i in pos];bb=[slots[i] for i in range(5) if i not in pos]
  for pa,pb,fac in ([(0,0,1),(1,1,2)] if op==0 else [(0,1,1),(1,0,1)]):
   for key,v in pol(eval_L(pa,aa),evfield(SA[pb],[vec[a] for a in bb])).items():target[ep,key]-=fac*v
res=quotient3(clean(target));obs=min(res);du={obs:F(1)}
for pv in sorted(bas3,reverse=True):
 v=-sum(c*du.get(k,F(0)) for k,c in bas3[pv].items() if k!=pv)
 if v:du[pv]=v
ck('projection_dual_original6272_columns',all(sum(v*raw_Ucol(r,h).get(key,F(0)) for key,v in du.items())==0 for r in range(7) for h in hs))
value=sum(v*target.get(key,F(0)) for key,v in du.items());ck('projection_dual_nonzero_original_target',value==res[obs] and bool(value))
repeat=[i for i,h in enumerate(tk) if all(len(set(k))<3 for k in h)];distinct=[i for i in range(len(tk)) if i not in repeat]
ck('complete_polar_split161_123',len(repeat)==161 and len(distinct)==123 and all(all(len(set(k))==3 for k in tk[i]) for i in distinct))
# All repeated B effects are Gram-only on the actual W-pair lower jet.
ww=[eval_L(ip,[7+a,7+b]) for ip in range(2) for a,b in w2]
ck('actual_L_WW_repeated',all(all(len(set(k))<3 for k in h) for h in ww))
ck('all_repeated_B_sigma_zero',all(not any(key for key in pol(l,tk[hi])) for l in ww for hi in repeat))
# Construct seven actual full-hook repeated Gram-dual directions. They are NOT
# polar and are quartic unknowns, not new cubic freedoms.
M=sp.Matrix([[sp.Rational(ns['gram'](k,h)) for h in hs[:168]] for k in KE]);_,piv=M.rref();ck('full_repeated_Gram_rank7',len(piv)==7)
inv=M[:,list(piv)].inv();Jr=[add(*[(F(inv[j,r]),hs[piv[j]]) for j in range(7)]) for r in range(7)]
ck('original_Gram_duals',all(pol(KE[a],Jr[b])==({():F(1)} if a==b else {}) for a in range(7) for b in range(7)))
# Original A,N decomposition was replayed by inherited lower tensors. Its
# repeated support supplies the universal sigma(N,Delta)=0 identity.
ck('all_actual_N_repeated',all(all(len(set(k))<3 for k in h) for part in N for h in part.values()))
ck('all_repeated_polar_members',all(not pol(K[a],tk[i]) for i in repeat for a in range(n)))
# Homogeneous polynomials use ordinary coefficients, explicitly distinct from
# symmetric derivative entries. Product evaluation counts each polynomial once.
def pad(target,mon,coef,h):
 if coef:target[mon]=add((1,target.get(mon,{})),(coef,h))
def ppair(A,B):
 out={}
 for ma,ha in A.items():
  for mb,hb in B.items():pad(out,tuple(sorted(ma+mb)),1,pol(ha,hb))
 return {k:v for k,v in out.items() if v}
def pairpoly(A,B):
 out=[{},{}]
 for pa,pb,op,fac in [(0,0,0,1),(1,1,0,2),(0,1,1,1),(1,0,1,1)]:
  for mon,h in ppair(A[pa],B[pb]).items():pad(out[op],mon,fac,h)
 return [{k:v for k,v in p.items() if v} for p in out]
def combine(A,B,fac=1):return [{m:add((1,A[ip].get(m,{})),(fac,B[ip].get(m,{}))) for m in set(A[ip])|set(B[ip]) if add((1,A[ip].get(m,{})),(fac,B[ip].get(m,{})))} for ip in range(2)]
# A mixed A/B/C witness across both field parts exercises multiplicities and
# sqrt2 products; every monomial has at least one transverse coordinate.
delta=[{(0,7,8):tk[repeat[0]],(0,0,7):tk[repeat[15]]},{(1,1,2):tk[repeat[80]],(2,8,8):tk[repeat[-1]]}]
kap=[{(r,):KE[r] for r in range(7)},{}]
ell=[{(a,b):{k:v*(1 if a==b else 2) for k,v in eval_L(ip,[a,b]).items()} for a,b in receivers} for ip in range(2)]
adaptA=[[add(*[(v,A[ip][a]) for a,v in vec[r].items()]) for r in range(n)] for ip in range(2)]
us=[{},{}]
for pa,pb,op,fac in [(0,0,0,1),(1,1,0,2),(0,1,1,1),(1,0,1,1)]:
 for r in range(n):
  for mon,h in delta[pb].items():
   rot=add(*[(v,rho(h,a,b)) for (a,b),v in adaptA[pa][r].items()]);pad(us[op],tuple(sorted((r,)+mon)),4*fac,rot)
raw=combine(pairpoly(kap,us),pairpoly(ell,delta),2)
ck('full_polynomial_sigma_lift',all(all(key==() for key in h) for part in raw for h in part.values()))
ck('remaining_Gram_in_transverse_ideal',all(any(a<7 for a in mon) for part in raw for mon in part))
u=[dict(part) for part in us]
for ip,part in enumerate(raw):
 for mon,h in part.items():
  r=next(a for a in mon if a<7);rest=list(mon);rest.remove(r);pad(u[ip],tuple(rest),-h[()],Jr[r])
ck('shared_quartic_all_polynomial_coefficients',not any(combine(pairpoly(kap,u),pairpoly(ell,delta),2)))
# Expand through the independently inverted coframe and check original ambient
# K,L. This tests factors on original coordinates, not the transformed map alone.
def ambient(poly):
 out={}
 for mon,h in poly.items():
  coeff={():F(1)}
  for i in mon:
   nxt=defaultdict(F)
   for old,v in coeff.items():
    for j,w in covs[i].items():nxt[tuple(sorted(old+(j,)))]+=v*w
   coeff=clean(nxt)
  for mm,v in coeff.items():pad(out,mm,v,h)
 return {m:h for m,h in out.items() if h}
da=[ambient(part) for part in delta];ua=[ambient(part) for part in u];uka=[{(a,):h for a,h in enumerate(K) if h},{}];ula=[{mon:{k:v*(1 if mon[0]==mon[1] else 2) for k,v in h.items()} for mon,h in part.items()} for part in L]
ck('original_ambient_full_fifth_identity',not any(combine(pairpoly(uka,ua),pairpoly(ula,da),2)))
wrong=[{mon:{k:v/2 for k,v in h.items()} for mon,h in part.items()} for part in us]
ctrl('factor_two_sigma_primitive_fails',any(any(key for key in h) for part in combine(pairpoly(kap,wrong),pairpoly(ell,delta),2) for h in part.values()))
# This algebraic freedom is not an Euler/J solution. Reconstruct derivative
# entries from homogeneous coefficients and inspect the native Euler operator.
def deriv(poly):
 out={}
 for mon,h in poly.items():
  mult=len(set(permutations(mon)));out[mon]={k:v/mult for k,v in h.items()}
 return out
dder=[deriv(p) for p in da]
nonzero=0
for part in dder:
 for a,b in receivers:
  for i,j in receivers:
   nonzero+=sum(eta[z]*(part.get(tuple(sorted((a,b,z))),{}).get((i,z,j),0)+part.get(tuple(sorted((a,b,z))),{}).get((j,z,i),0)) for z in range(n))!=0
ctrl('algebraic_lift_does_not_imply_Euler',nonzero>0)
# A fixed-A repeated-only repair cannot alter the projection's sigma dual.
ck('projection_dual_sigma_only',all(key for ep,key in du))
ck('projection_B_repeated_only_excluded',all(not any(key for key in pol(l,tk[hi])) for l in ww for hi in repeat) and bool(value))
report={'result_id':'K2417','checks':checks,'controls':controls,'inherited_checks':len(inherited_checks),'A_projection':projection,'A_projection_original_dual':{'W':wt,'field':op,'target':str(value),'terms':[[list(ep),list(key),str(v)] for (ep,key),v in sorted(du.items())]},'polar_split':{'repeated':161,'distinct':123,'full_ABC_field_coordinates':476*284,'algebraically_active_before_Euler_J':476*123},'primitive_fixture':{'adapted_delta_terms':sum(len(v) for v in delta),'ambient_delta_terms':sum(len(v) for v in da),'ambient_quartic_terms':sum(len(v) for v in ua),'Euler_nonzero_entries':nonzero,'delta_sha256':digest(da),'quartic_sha256':digest(ua)},'scope':'Repeated W3-fixed polar corrections admit a shared algebraic quartic lift; retain them through combined Euler/J elimination. A-only and fixed-A repeated-only repairs fail; full coupled family remains unresolved.'}
deps+=['tests/channel-swings/k2414_inherited_polar_fiber_probe.py','tests/channel-swings/k2408_joint_cubic_compatibility_probe.py','lab/process/k2408-joint-cubic-compatibility.json','lab/process/k2381-rotated-null-hook-prolongation.json']
report['dependencies']={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dict.fromkeys(deps)}
out=ROOT/'lab/process/k2417-coupled-three-w-compatibility.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
elif '--verify-only' not in sys.argv:assert json.loads(out.read_text())==report
print(json.dumps({'checks':len(checks),'controls':len(controls),'report':str(out)}),flush=True)
