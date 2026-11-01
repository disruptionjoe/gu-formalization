"""Original-hook checks for the mixed-sixth structural reduction; exact arithmetic."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations_with_replacement,product
from math import comb
import json,hashlib,sys,ast
import sympy as sp
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'tests/channel-swings/k2393_coupled_polar_dual_probe.py';source=p.read_text()
# Reconstruct the native polar basis, not an inherited rank/report assertion.
exec(compile(source[:source.index('lw=')],str(p),'exec'),globals())
checks={};controls={}
def ck(name,value):
 checks[name]=bool(value)
 if not value:raise AssertionError(name)
def ctrl(name,value):
 controls[name]=bool(value)
 if not value:raise AssertionError(name)
rho=ns['rho'];gram=ns['gram'];tensor=ns['tensor'];receivers=list(combinations_with_replacement(range(n),2))
Es=[{p:F(1)/alphas[r][p]} for r,(p,q) in enumerate(pairs)];vec=Es+W
KE=[add(*[(v,K[i]) for i,v in e.items()]) for e in Es]
frame=sp.Matrix([[sp.Rational(vec[j].get(i,0)) for j in range(n)] for i in range(n)])
covs=[{j:F(v) for j,v in enumerate(row) if v} for row in frame.inv().tolist()]
ck('original_polar_basis_dimension',len(hs)==896 and len(tk)==284 and len(pb)==612)
ck('full_polar_original_columns',all(not pol(h,k) for h in tk for k in K))
xi=add(*[(1,a) for a in alphas]);sbas={}
for h in tk:
 cc=clean({ij:sum(eta[m]*v*(h.get((ij[0],m,ij[1]),0)+h.get((ij[1],m,ij[0]),0)) for m,v in xi.items()) for ij in receivers})
 ck('tracefree_symbol',sum(eta[i]*cc.get((i,i),0) for i in range(n))==0)
 ck('quadratic_symbol_annihilator',sum(eta[i]*eta[j]*xi.get(i,0)*xi.get(j,0)*cc.get(tuple(sorted((i,j))),0) for i in range(n) for j in range(n))==0)
 while cc:
  k=min(cc);v=cc[k]
  if k not in sbas:sbas[k]={j:x/v for j,x in cc.items()};break
  cc=add((1,cc),(-v,sbas[k]))
ck('original_polar_symbol_rank103',len(sbas)==103)
x,y,z=sp.symbols('x y z');ck('quadratic_cokernel_primitive',sp.gcd(sp.gcd(x*y,x*z),y*z)==1)
ranks={r:104*comb(r+13,13)-(comb(r+11,13) if r>=2 else 0) for r in range(7)}
ck('next_Euler_rank',ranks[4]==247415 and ranks[3]==58226 and ranks[2]==10919)
ck('next_tracefree_cokernel105',104*comb(17,13)-ranks[4]==105)
# Decode original lower-jet rotation and repeated remainder.
prior=json.loads((ROOT/'lab/process/k2381-rotated-null-hook-prolongation.json').read_text());A=[defaultdict(dict),defaultdict(dict)];N=[defaultdict(dict),defaultdict(dict)]
for ip,key in enumerate(['rational_solution','sqrt2_solution']):
 for name,c in prior[key]:
  c=F(c)
  if name[0]=='A':
   _,a,u,v=name;A[ip][a]=add((1,A[ip][a]),(c,{(u,v):F(1)}))
  else:
   _,a,b,r,i,last=name;ds=[F(0)]*n;ds[i]=1;ds[last]=-1;N[ip][a,b]=add((1,N[ip][a,b]),(c,tensor(r,ds)))
def rotate(h,a):return add(*[(v,rho(h,u,vv)) for (u,vv),v in a.items()])
ck('all_original_L_decompositions',all(L[ip][a,b]==add((1,N[ip].get((a,b),{})),(1,rotate(K[b],A[ip][a])),(1,rotate(K[a],A[ip][b]))) for ip in range(2) for a,b in receivers))
ck('original_N_repeated',all(len(set(k))<3 for part in N for h in part.values() for k in h))
M=sp.Matrix([[sp.Rational(gram(k,h)) for h in hs[:168]] for k in KE]);_,piv=M.rref();ck('repeated_Gram_dual_rank7',len(piv)==7);iv=M[:,list(piv)].inv();Jr=[add(*[(F(iv[j,r]),hs[piv[j]]) for j in range(7)]) for r in range(7)]
ck('original_Gram_sigma_duals',all(pol(KE[a],Jr[b])==({():F(1)} if a==b else {}) for a in range(7) for b in range(7)))
# Reuse only ordinary-polynomial arithmetic functions, without predecessor execution.
p17=ROOT/'tests/channel-swings/k2417_coupled_three_w_compatibility_probe.py';s17=p17.read_text();tree=ast.parse(s17)
for node in tree.body:
 if isinstance(node,ast.FunctionDef) and node.name in ['pad','ppair','pairpoly','combine','ambient']:
  exec(compile(ast.Module(body=[node],type_ignores=[]),str(p17),'exec'),globals())
rep=[h for h in tk if all(len(set(k))<3 for k in h)];ck('full_repeated_polar161',len(rep)==161)
def evalL(ip,a,b):return add(*[(v*w,L[ip][tuple(sorted((i,j)))]) for i,v in vec[a].items() for j,w in vec[b].items()])
kap=[{(r,):KE[r] for r in range(7)},{}]
ell=[{(a,b):{k:v*(1 if a==b else 2) for k,v in evalL(ip,a,b).items()} for a,b in receivers} for ip in range(2)]
adA=[[add(*[(v,A[ip][a]) for a,v in vec[r].items()]) for r in range(n)] for ip in range(2)]
# Both field parts, repeated derivatives and mixed E/W monomials.
z4=[{(0,7,8,9):rep[0],(1,1,7,7):rep[15]},{(2,2,8,8):rep[80],(0,1,2,9):rep[-1]}]
ck('quartic_preserves_fifth_algebraic',not any(pairpoly(kap,z4)))
ck('quartic_W4_zero',all(any(r<7 for r in mon) for part in z4 for mon in part))
def primitive(factor):
 out=[{},{}]
 for pa,pb,op,fac in [(0,0,0,1),(1,1,0,2),(0,1,1,1),(1,0,1,1)]:
  for r in range(n):
   for mon,h in z4[pb].items():pad(out[op],tuple(sorted((r,)+mon)),factor*fac,rotate(h,adA[pa][r]))
 return out
def residual(v):return combine([{m:add((6,h)) for m,h in part.items()} for part in pairpoly(kap,v)],pairpoly(ell,z4),15)
v0=primitive(5);raw=residual(v0)
ck('factor5_sigma_primitive',all(all(k==() for k in h) for part in raw for h in part.values()))
ck('remaining_Gram_transverse_ideal',all(any(r<7 for r in mon) for part in raw for mon in part))
v5=[dict(part) for part in v0]
for ip,part in enumerate(raw):
 for mon,h in part.items():
  r=next(r for r in mon if r<7);rest=list(mon);rest.remove(r);pad(v5[ip],tuple(rest),-h[()]/6,Jr[r])
ck('all_coefficients_shared_sixth_lift',not any(residual(v5)))
ctrl('factor4_changes_actual_sigma',any(any(k for k in h) for part in residual(primitive(4)) for h in part.values()))
# Independent ambient composition, using original K,L after coframe expansion.
za=[ambient(part) for part in z4];va=[ambient(part) for part in v5]
ka=[{(a,):h for a,h in enumerate(K) if h},{}];la=[{mon:{k:v*(1 if mon[0]==mon[1] else 2) for k,v in h.items()} for mon,h in part.items()} for part in L]
ra=combine([{m:add((6,h)) for m,h in part.items()} for part in pairpoly(ka,va)],pairpoly(la,za),15)
ck('original_ambient_sixth_identity',not any(ra))
# Gram ideal division handles arbitrary mixed monomials, including repeated slots.
gram6=[{(0,0,7,8,9,10):{():F(3,7)},(1,1,1,8,8,8):{():F(-4,9)}},{(2,3,4,5,6,7):{():F(5,11)}}];gv=[{},{}]
for ip,part in enumerate(gram6):
 for mon,h in part.items():
  r=next(a for a in mon if a<7);rest=list(mon);rest.remove(r);pad(gv[ip],tuple(rest),h[()]/6,Jr[r])
ck('arbitrary_mixed_Gram_lift',not any(combine([{m:add((6,h)) for m,h in part.items()} for part in pairpoly(kap,gv)],gram6,-1)))
ctrl('pure_W_Gram_cannot_be_in_image',all(not h for mon,h in kap[0].items() if mon[0]>=7) and all(not add(*[(v,K[i]) for i,v in w.items()]) for w in W))
# Actual lift is algebraic, not an Euler solution by construction.
euler_residuals=[]
for part in za:
 ev=defaultdict(F)
 for mon,h in part.items():
  for r in set(mon):
   rest=list(mon);rest.remove(r)
   for i,j in receivers:
    ev[tuple(rest),i,j]+=mon.count(r)*eta[r]*(h.get((i,r,j),0)+h.get((j,r,i),0))
 euler_residuals.append(clean(ev))
ctrl('algebraic_fixture_not_automatically_Euler',any(euler_residuals))
# Full repeated module splits into161 free polar directions and Koszul syzygies.
from itertools import combinations
for r,s in combinations(range(7),2):
 syz=[{(s,):Jr[r],(r,):add((-1,Jr[s]))},{}]
 ck('all21_original_Koszul_generators',not any(pairpoly(kap,syz)))
# Enumerate the original monomial multiplication map support: quartics with
# positive E degree map onto degree5 monomials with E degree at least2.
domain_mons=[m for m in combinations_with_replacement(range(14),4) if any(r<7 for r in m)]
image_mons={tuple(sorted((r,)+m)) for m in domain_mons for r in range(7)}
expected={m for m in combinations_with_replacement(range(14),5) if sum(r<7 for r in m)>=2}
ck('complete_repeated_Gram_monomial_image',image_mons==expected and len(image_mons)==6636)
ck('zero_W4_repeated_nuisance_dimension',len(domain_mons)*168-len(image_mons)==357924)
ctrl('omitting_linear_Koszul_loses_freedom',357924>len(domain_mons)*161)
def digest(parts):return hashlib.sha256(repr([[(m,sorted((k,str(v)) for k,v in h.items())) for m,h in sorted(p.items())] for p in parts]).encode()).hexdigest()
report={'result_id':'K2421','checks':checks,'controls':controls,'symbol_ranks_by_receiver_degree':ranks,'next_Euler_cokernel':105,'next_Euler_rank':247415,'repeated_zero_W4_nuisance_dimension':357924,'repeated_Koszul_linear_generators':21,'repeated_quartic_primitive':{'factor':5,'adapted_terms':sum(map(len,z4)),'ambient_quartic_terms':sum(map(len,za)),'ambient_quintic_terms':sum(map(len,va)),'quartic_digest':digest(za),'quintic_digest':digest(va)},'scope':'All-degree symbol image equality; fifth-Euler follows conditionally from same-quartic full sixth algebraic and checked curved J. Gram and repeated-quartic reductions are constructive. Mixed sigma feasibility, curved higher orders and smooth stationarity remain open.'}
deps=['tests/channel-swings/k2387_coupled_hook_jet_blocks_probe.py','tests/channel-swings/k2390_full_hook_jet_probe.py','tests/channel-swings/k2393_coupled_polar_dual_probe.py','tests/channel-swings/k2417_coupled_three_w_compatibility_probe.py','lab/process/k2381-rotated-null-hook-prolongation.json','lab/process/k2390-full-hook-jet.json','lab/process/k2420-coupled-nuisance-image.json','explorations/conditional-build/k2405-fifth-euler-compatibility-2026-10-31.md']
report['dependencies']={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps};out=ROOT/'lab/process/k2421-mixed-sixth-structural-reduction.json'
report=json.loads(json.dumps(report))
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==report
print(json.dumps({'checks':len(checks),'controls':len(controls),'status':'pass'}))
