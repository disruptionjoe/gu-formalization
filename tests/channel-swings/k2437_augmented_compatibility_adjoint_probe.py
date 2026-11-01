"""Original Euler-null compatibility direction and exact all-degree primitive.
Universal image/formal-jet conclusions use the written induction, not finite ranks.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
from itertools import combinations,combinations_with_replacement
from math import factorial,prod,comb
import ast,json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2]
source25path=ROOT/'tests/channel-swings/k2425_frame_euler_module_probe.py';source25text=source25path.read_text()
exec(compile(source25text[:source25text.index('ss=[[symbol')],str(source25path),'exec'),globals())
inherited=dict(checks);checks={};controls={}
start=source25text.index('qpath=');end=source25text.index('augcols=[]',start)
exec(compile(source25text[start:end],str(source25path),'exec'),globals())
h=add((1,rep[32]),(F(9012,8519),rep[55]))
ck('witness_original_repeated_hook',bool(h) and all(len(set(ix))<3 for ix in h))
ck('all_original_Gram_polar_constraints',all(gram(k,h)==0 for k in K))
ck('all_seven_transverse_Euler_symbols_zero',all(not symbol(h,a) for a in alphas))
ac=[jy(h,r) for r in range(7)]
expected=[field(0),ff(F(2253,2)),ff(F(2253,17038)),field(0),field(0),field(0),field(0)]
ck('original_curvature_and_quadratic_first_order_coefficients',ac==expected)
bc={}
for r in range(7):
 for s0 in range(7):
  for t in range(7):
   v=-sum(F(eta[i]*eta[j],2)*av*bv*fp(KE[t],h,i,j) for i,av in alphas[r].items() for j,bv in alphas[s0].items())
   if v:bc[r,s0,t]=ff(v)
ck('all343_original_second_order_coefficients_vanish',not bc)
# Sparse ordinary polynomials, exact coefficients in Q(sqrt2).
def pa(*terms):
 out=defaultdict(lambda:field(0))
 for c,P in terms:
  for m,v in P.items():out[m]+=c*v
 return {m:v for m,v in out.items() if v}
def der(P,r):
 out={}
 for m,v in P.items():
  if r in m:
   t=list(m);t.remove(r);out[tuple(t)]=v*m.count(r)
 return out
def mulvar(P,r):return {tuple(sorted(m+(r,))):v for m,v in P.items()}
def fisher(P,Q):return sum(v*Q.get(m,0)*prod(factorial(a) for a in Counter(m).values()) for m,v in P.items())
a,b=expected[1:3]
def primitive(P):
 terms=[]
 for m,v in P.items():
  counts=Counter(m);u=counts[1];v2=counts[2]
  for j in range(v2+1):
   t=list(m)
   for _ in range(j):t.remove(2)
   t += [1]*(j+1)
   c=v*(-b)**j/a**(j+1)*field(factorial(v2))/factorial(v2-j)*field(factorial(u))/factorial(u+j+1)
   terms.append((c,{tuple(sorted(t)):field(1)}))
 return pa(*terms)
def directional(P):return pa((a,der(P,1)),(b,der(P,2)))
for deg in range(8):
 mons=list(combinations_with_replacement(range(7),deg))
 # All monomials at low degrees; representative mixed ones at higher degree.
 selected=mons if deg<=3 else [mons[0],mons[-1],tuple([2]*deg),tuple(sorted(i%7 for i in range(deg)))]
 ck('primitive_original_direction_degree_'+str(deg),all(directional(primitive({m:field(1)}))=={m:field(1)} for m in selected))
 ck('primitive_vanishes_on_W_degree_'+str(deg),all(all(1 in t for t in primitive({m:field(1)})) for m in selected))
# Quantitative successor: the scalar primitive alone has only geometric growth.
c=b/a
for k in [0,1,2,4,8,16,32,64]:
 pp=primitive({(2,)*k:field(1)})
 norm=sum(abs(v) for v in pp.values())
 exact=((1+c)**(k+1)-1)/(a*c*(k+1))
 ck('scalar_primitive_coefficient_bound_'+str(k),norm==exact and norm<=(1+c)**k/a)
ctrl('scalar_inverse_exceeds_naive_1_over_a_bound',sum(abs(v) for v in primitive({(2,)*64:field(1)}).values())>1/a)
P={(0,1,2,2):field(2)+root2,(1,1,3,4):field(-3)}
sol=primitive(P)
ctrl('omit_second_direction_fails',pa((a,der(sol,1)))!=P)
ctrl('wrong_curvature_scale_fails',pa((field(2),directional(sol)))!=P)
# Independent coefficient-level primal/dual test of augmented scalar operators.
def coeff(hh):
 aa=[jy(hh,r) for r in range(7)];bb={}
 for r in range(7):
  for s0 in range(7):
   for t in range(7):
    z=-sum(F(eta[i]*eta[j],2)*av*bv*fp(KE[t],hh,i,j) for i,av in alphas[r].items() for j,bv in alphas[s0].items())
    if z:bb[r,s0,t]=ff(z)
 return aa,bb
def jp(P,co):
 aa,bb=co
 return pa(*[(v,der(P,r)) for r,v in enumerate(aa) if v],*[(v,mulvar(der(der(P,r),s0),t)) for (r,s0,t),v in bb.items()])
def ja(P,co,wrong=False):
 aa,bb=co
 return pa(*[(v,mulvar(P,r)) for r,v in enumerate(aa) if v],*[(v,der(mulvar(mulvar(P,r),s0),t) if wrong else mulvar(mulvar(der(P,t),r),s0)) for (r,s0,t),v in bb.items()])
fixtures=[rep[0],rep[32],rep[55],h,linear[-1][1][0]]
f={(0,1,1,2):field(3),(2,2,3,4):root2};q={(0,1,2):field(2),(1,2,2):field(-1),(2,3,4):field(5)}
wrong_detected=False
for i,hh in enumerate(fixtures):
 co=coeff(hh);ck('original_scalar_Fischer_pairing_'+str(i),fisher(jp(f,co),q)==fisher(f,ja(q,co)))
 wrong_detected |= ja(q,co)!=ja(q,co,True)
ctrl('reversed_second_order_adjoint_detected',wrong_detected)
# Multiplying a constant hook by y_t takes an outer derivative in the adjoint.
co=coeff(rep[32]);t=1;ffix={(0,1,2):field(2),(2,3,4):field(3)}
ck('linear_generator_outer_derivative',fisher(jp(mulvar(ffix,t),co),q)==fisher(ffix,der(ja(q,co),t)))
ctrl('omitted_outer_derivative_detected',der(ja(q,co),t)!=ja(der(q,t),co))
# Explicit mixed E/W fixture: transverse kernel is not a full ambient kernel.
ftrans=primitive({(2,2):field(1)})
fmixed={tuple(sorted(m+(7,8))):v for m,v in ftrans.items()}
Eout={}
for r in range(n):
 for ij,v in symbol(h,covs[r]).items():Eout[ij]=pa((1,Eout.get(ij,{})),(ff(v),der(fmixed,r)))
Eout={ij:v for ij,v in Eout.items() if v}
ctrl('transverse_kernel_not_ambient_kernel',bool(Eout))
ck('mixed_Euler_only_higher_E_degree',all(sum(x<7 for x in m)>=3 for pp in Eout.values() for m in pp))
ambient_a=[jlinear(h,covs[r]) for r in range(n)];ambient_b={}
for r in range(n):
 for s0 in range(n):
  for t in range(7):
   v=-sum(F(eta[i]*eta[j],2)*av*bv*fp(KE[t],h,i,j) for i,av in covs[r].items() for j,bv in covs[s0].items())
   if v:ambient_b[r,s0,t]=ff(v)
jmixed=jp(fmixed,(ambient_a,ambient_b))
leading={m:v for m,v in jmixed.items() if sum(x<7 for x in m)==2}
ck('mixed_scalar_leading_block_original_replay',leading=={(2,2,7,8):field(1)})
ck('mixed_scalar_other_blocks_strictly_higher',all(sum(x<7 for x in m)>=2 for m in jmixed))
# Binomial conversion of the top d-jet in d-1 derivatives of curved compatibility.
for d in range(4,15):
 ck('diagonal_normalization_'+str(d),F(1,d)==F(factorial(d-1),factorial(d)) and F(4,d)==4*F(factorial(d-1),factorial(d)) and F(2,d)==2*F(factorial(d-1),factorial(d)))
# The same triangular filtration uses all-degree ordinary ranks, not finite extrapolation.
for d in range(4,12):
 rk=lambda k:104*comb(k+6,6)-(comb(k+4,6) if k>=2 else 0)
 aug=sum(comb(d+5-k,6)*(rk(k)+comb(k+6,6)) for k in range(d))
 ck('ambient_augmented_dimension_'+str(d),aug==105*comb(d+12,13)-comb(d+10,13))
# Keep inherited report hashes and a direct same-section premise, rather than recertifying all old ranks.
deps=['tests/channel-swings/k2425_frame_euler_module_probe.py','tests/channel-swings/k2435_fischer_frame_annihilator_probe.py','lab/process/k2435-fischer-frame-annihilator.json','lab/process/k2433-lower-quartic-compatibility.json','explorations/conditional-build/k2433-lower-quartic-compatibility-2026-11-01.md','explorations/conditional-build/k2429-shared-eighth-euler-extension-2026-11-01.md']
for dep in deps:
 if dep.endswith('.json'):
  j=json.loads((ROOT/dep).read_text());ck('dependency_pins_'+Path(dep).stem,all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==v for p,v in j.get('dependencies',{}).items()))
report={'result_id':'K2437','scope':'Conditional original hook model; all-degree augmented image and shared formal Gram/sigma/Euler construction, subject to written induction; no convergence or source-native GU identification.','checks':checks,'controls':controls,'witness':{'rep_coefficients':[[32,'1'],[55,'9012/8519']],'original_hook':[[list(k),str(v)] for k,v in sorted(h.items())],'first_order':[str(v) for v in ac],'second_order_nonzero':len(bc),'operator':'(2253/2) partial_y1 + (2253/17038) partial_y2'},'primitive':'finite sum_j (-b)^j/a^(j+1) I_y1^(j+1) partial_y2^j target','analytic_scalar_bound':'||S p||_(r1,r2) <= r1/a ||p||_(r1,r2+r1/8519); degree-k coefficient l1 bound (1+1/8519)^k/a; full recursion inverse not bounded','evidence_kinds':{'exact':'original symbol, Gram, curvature, all343 second coefficients, polynomial primitives, Fischer pairings','universal':'written directional-antiderivative, triangular image and same-jet induction','reporting':'dependency pins and dimension/binomial fixtures'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2437-augmented-compatibility-adjoint.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2437',len(checks),'checks',len(controls),'controls PASS',flush=True)
print(json.dumps(report['witness'],indent=2))
