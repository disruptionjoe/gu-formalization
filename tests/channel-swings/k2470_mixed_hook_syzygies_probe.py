from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, permutations
import json
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'tests/channel-swings/k2464_cancelling_hook_inverse_probe.py';s=p.read_text();exec(compile(s[:s.index('fixtures=')],str(p),'exec'),globals())
inherited=dict(checks);checks={};controls={};ck('inherited_original_inputs',all(inherited.values()))
# Extract w_i directly from K_r[i,i,r]; away from partner exceptions,
# its differences are independent of r, which is all determinants need.
pairs=[(0,1),(4,2),(5,3),(6,10),(7,11),(8,12),(9,13)]
# Symbolic coefficient computation: differential symbols use same sparse polynomial ring.
u={4:{(5,5):field(eta[5]),(6,6):field(-eta[6])},5:{(6,6):field(eta[6]),(4,4):field(-eta[4])},6:{(4,4):field(eta[4]),(5,5):field(-eta[5])}}
v={7:{(8,8):field(eta[8]),(9,9):field(-eta[9])},8:{(9,9):field(eta[9]),(7,7):field(-eta[7])},9:{(7,7):field(eta[7]),(8,8):field(-eta[8])}}
def pm(P,Q):return pa(*[(a*b,{tuple(sorted(m+n)):field(1)}) for m,a in P.items() for n,b in Q.items()])
V={}
for i in u:
 for j in v:
  pp=pm(u[i],v[j]);V[i,j]=pa((eta[i],mulvar(pp,j)));V[j,i]=pa((-eta[j],mulvar(pp,i)))
O={};J1={};J2=[{} for _ in K];G=[{} for _ in K];trace={}
for (i,j),P0 in V.items():
 H={(i,i,j):F(1),(i,j,i):F(-1)}
 trace[j]=pa((1,trace.get(j,{})),(eta[i],P0))
 for a in range(14):
  for ij,z in symbol(H,{a:F(1)}).items():O[ij]=pa((1,O.get(ij,{})),(ff(z),mulvar(P0,a)))
  J1=pa((1,J1),(jlinear(H,{a:F(1)}),mulvar(P0,a)))
 for ell,kk in enumerate(K):
  G[ell]=pa((1,G[ell]),(ff(gram(H,kk)),P0))
  for a in range(14):
   for b in range(14):
    z=-F(eta[a]*eta[b],2)*fp(kk,H,a,b)
    if z:J2[ell]=pa((1,J2[ell]),(ff(z),mulvar(mulvar(P0,a),b)))

ck('six_original_positive_signs',all(eta[i]==1 for i in range(4,10)))
ck('all_trace_coefficients_zero',not any(trace.values()))
ck('complete_ordinary_polynomial_zero',not any(O.values()))
ck('all14_original_Gram_coefficients_zero',not any(G))
ck('all14_original_second_scalar_polynomials_zero',not any(J2))
ck('complete_first_scalar_has30_terms',len(J1)==30)
ck('repeated_sigma_zero',all(not any(key for key in pol({(i,i,j):F(1),(i,j,i):F(-1)},kk)) for i,j in V for kk in K))
alpha=(4,5,5,5,9,9);ck('leading_coefficient',J1[alpha]==field(1)/8)
rest=pa((1,J1),(-field(1)/8,{alpha:field(1)}))
ck('strict_weight_on_every_remaining_term',all(m.count(5)+m.count(9)<=4 for m in rest))
ck('exact_error_coefficient_norm35',sum(abs(8*z) for z in rest.values())==35)
ck('full_field_norm144',2*sum(abs(z) for pp in V.values() for z in pp.values())==144)
ck('max_normal_derivative_two',max(m.count(5) for pp in V.values() for m in pp)==2)
def apply(D,P):
 terms=[]
 for inds,z in D.items():
  pp=P
  for i in inds:pp=der(pp,i)
  if pp:terms.append((z,pp))
 return pa(*terms)
def right0(P):
 for i in alpha:P=integ(P,i)
 return pa((8,P))
def inverse(P):
 n=max(map(len,P),default=0);total={};q=P;steps=0
 while q:
  total=pa((1,total),(1,q));q=pa((-1,apply(rest,right0(q))));steps+=1
  assert steps<=n+1
 return right0(total),steps
fixtures=[{(2,2,4,7,8,11,12):field(1)},{(0,2,4,5,7,8,9,11,12):field(2)},{(8,)*6:field(1)},{(4,5,6,7,8,9):field(1)}]
records=[]
for z,g in enumerate(fixtures):
 Phi,steps=inverse(g);fieldout={ij:apply(PP,Phi) for ij,PP in V.items()};nn=len(next(iter(g)));dd=nn+1
 ck('full_inverse_'+str(z),apply(J1,Phi)==g)
 ck('boundary_'+str(z),all(all(5 in m for m in PP) for PP in fieldout.values()))
 ck('potential_norm_'+str(z),sum(abs(v) for v in Phi.values())<=16*210**nn*sum(abs(v) for v in g.values()))
 ck('actual_jet_normalization_'+str(z),pa((field(4)/dd,pa((field(dd)/4,apply(J1,Phi)))))==g)
 ctrl('wrong_scalar_scale_'+str(z),pa((2,apply(J1,Phi)))!=g)
 if dd!=4:ctrl('omitted_actual_degree_normalization_'+str(z),pa((field(4)/dd,apply(J1,Phi)))!=g)
 # First actual fixture independently applies full original response, not composed symbol.
 if z==0:
  oo={};jj={}
  for (i,j),PP in fieldout.items():
   HH={(i,i,j):F(1),(i,j,i):F(-1)};oo=merge(oo,ordinary(HH,PP),1);jj=pa((1,jj),(1,scalar(HH,PP)))
  ck('original_full_field_replay_ordinary',not oo);ck('original_full_field_replay_scalar',jj==g)
  expected={tuple(sorted([2,2,4,4,5,5,5,7,8,9,9,11,12])):field(1)/3,tuple(sorted([2,2,4,5,5,5,5,7,8,9,9,11,12])):-field(1)/6}
  ck('explicit_first_missing_potential',Phi==expected)
  ctrl('single_primitive_insufficient',apply(J1,right0(g))!=g)
  ctrl('old_seven_family_PDE_detects_target',bool(der(der(der(der(der(der(der(g,2),2),4),7),8),11),12)))
  explicit=[[list(m),str(v)] for m,v in Phi.items()]
 records.append({'degree':nn,'iterations':steps,'potential_terms':len(Phi),'field_terms':sum(map(len,fieldout.values()))})
# Deliberately omit antisymmetric P partner: ordinary off-diagonal cancellation fails.
(i,j),PP=next(iter(V.items()));HH={(i,i,j):F(1),(i,j,i):F(-1)}
ctrl('omitting_cancelling_components',any(symbol(HH,{a:F(1)}) for a in range(14)))
ctrl('unintegrated_potential_not_boundary',any(any(5 not in m for m in apply(PP,{next(iter(PP)):field(1)})) for PP in V.values()))
deps=['explorations/conditional-build/k2470-mixed-hook-syzygies-2026-11-01.md',str(Path(__file__).relative_to(ROOT)),'tests/channel-swings/k2464_cancelling_hook_inverse_probe.py','lab/process/k2467-mixed-hook-generators.json','lab/process/k2452-partial-analytic-hook-inverse.json']
for dep in deps[-2:]:
 data=json.loads((ROOT/dep).read_text());ck('authenticated_'+Path(dep).stem,all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in data['dependencies'].items()))
report={'result_id':'K2470','checks':checks,'controls':controls,'scalar_symbol':[[list(m),str(v)] for m,v in sorted(J1.items())],'potential_operator':[[list(ij),[[list(m),str(v)] for m,v in sorted(PP.items())]] for ij,PP in sorted(V.items())],'degree7_potential':explicit,'fixtures':records,'analytic_actual_jet_bound':'576*d*(d+5)^5*210^(d-1)','evidence_kinds':{'universal':'differential syzygy, complete finite symbol, weight nilpotence, factorial telescoping and analytic sum','finite':'original tensor coefficients and direct field replay, polynomial fixtures and genuine countercontrols','ceiling':'full scalar correction; unrestricted ordinary estimate and nonlinear convergence open'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2470-mixed-hook-syzygies.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2470',len(checks),'checks',len(controls),'controls PASS',records,flush=True)
