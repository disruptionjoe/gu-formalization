"""Actual original scalar direction and mixed-degree estimates; no rank extrapolation."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
from itertools import combinations,combinations_with_replacement
from math import factorial,prod,comb
import ast,json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2]
# Load the original tensor construction and pure polynomial functions only.
p37=ROOT/'tests/channel-swings/k2437_augmented_compatibility_adjoint_probe.py'
t37=p37.read_text();prefix=t37[:t37.index('for deg in range(8):')]
exec(compile(prefix,str(p37),'exec'),globals())
original_checks=dict(checks);checks={};controls={}
for node in ast.parse(t37).body:
 if isinstance(node,ast.FunctionDef) and node.name in {'coeff','jp','ja'}:exec(compile(ast.Module(body=[node],type_ignores=[]),str(p37),'exec'),globals())
ck('original_witness_constraints_replayed',all(original_checks.values()))
# Fixed shear y1=u,y2=v+u/8519. Pull polynomial to u,v ordinary coordinates.
def shear(P,sign=1):
 out=[]
 c=field(sign)/8519
 for mon,val in P.items():
  n2=mon.count(2);rest=list(mon)
  for _ in range(n2):rest.remove(2)
  for j in range(n2+1):out.append((val*comb(n2,j)*c**j,{tuple(sorted(rest+[1]*j+[2]*(n2-j))):field(1)}))
 return pa(*out)
def adapted_integrate(P):
 return {tuple(sorted(mon+(1,))):v/(a*(mon.count(1)+1)) for mon,v in P.items()}
def l1(P):return sum(abs(v) for v in P.values())
for k in [0,1,2,3,5,9,17]:
 for passive in [(),(7,),(7,8,8),(7,)*11]:
  pp={tuple(sorted((2,)*k+passive)):field(1)}
  ps=shear(pp);sadapt=adapted_integrate(ps);back=shear(sadapt,-1)
  ck(f'shear_inverse_{k}_{passive}',shear(ps,-1)==pp)
  ck(f'actual_direction_inverse_{k}_{passive}',directional(back)==pp)
  ck(f'adapted_primitive_bound_{k}_{passive}',l1(sadapt)<=l1(ps)/a)
  ck(f'passive_unchanged_{k}_{passive}',all(tuple(x for x in mon if x>=7)==passive for mon in back))
ctrl('original_coordinate_1_over_a_not_uniform',l1(primitive({(2,)*17:field(1)}))>1/a)
# Actual ordinary forcing and scalar correction: start with an original hook field,
# rather than assert R_k is constructed numerically at every degree.
vhook=rep[0];P={(0,1,2):field(2),(1,2,2):field(-3)};g={(0,2):field(7),(2,2):field(-2)}
jV=jp(P,coeff(vhook));coh=coeff(h)
for d in [3,5,8,17]:
 repair=primitive(pa((field(d)/4,g),(-1,jV)))
 ck('augmented_diagonal_exact_'+str(d),pa((field(4)/d,jV),(field(4)/d,jp(repair,coh)))==g)
 ck('ordinary_correction_zero_'+str(d),all(not symbol(h,al) for al in alphas))
 ctrl('wrong_total_degree_normalization_'+str(d),pa((field(4)/d,jV),(field(4)/d,jp(primitive(pa((1,g),(-1,jV))),coh)))!=g if d!=4 else True)
# Original ambient mixed fixture, no predecessor report regeneration.
ftrans=primitive({(2,2):field(1)});fmixed={tuple(sorted(mon+(7,8))):v for mon,v in ftrans.items()}
Eout={}
for r in range(n):
 for ij,v in symbol(h,covs[r]).items():Eout[ij]=pa((1,Eout.get(ij,{})),(ff(v),der(fmixed,r)))
Eout={ij:v for ij,v in Eout.items() if v}
ctrl('actual_transverse_kernel_not_ambient',bool(Eout))
ck('actual_EW_raises_degree',all(sum(x<7 for x in mon)>=3 for pp in Eout.values() for mon in pp))
ambient_a=[jlinear(h,covs[r]) for r in range(n)];ambient_b={}
for r in range(n):
 for ss in range(n):
  for t in range(7):
   v=-sum(F(eta[i]*eta[j],2)*av*bv*fp(KE[t],h,i,j) for i,av in covs[r].items() for j,bv in covs[ss].items())
   if v:ambient_b[r,ss,t]=ff(v)
jmixed=jp(fmixed,(ambient_a,ambient_b));leading={mon:v for mon,v in jmixed.items() if sum(x<7 for x in mon)==2}
ck('actual_scalar_leading_block',leading=={(2,2,7,8):field(1)})
ck('actual_scalar_higher_blocks',all(sum(x<7 for x in mon)>=2 for mon in jmixed))
# The degree-shift count is structural for every original mixed coefficient:
# a W derivative replaces an E derivative, raising receiver E degree by one;
# y_E d_W d_W raises by two. This table is a formula check, not tensor evidence.
for de,dw,ymul in [(1,0,0),(0,1,0),(2,0,1),(1,1,1),(0,2,1)]:
 ck(f'degree_shift_{de}_{dw}_{ymul}',1-de+ymul==dw)
import sympy as sp
for d in [2,3,4,7]:
 NN=sp.zeros(d)
 for i in range(d-1):NN[i+1,i]=1
 DD=sp.diag(*[2**i for i in range(d)]);L0=sp.diag(*[sp.Rational(1,2**i) for i in range(d)]);RR=sum(((-DD*NN)**j*DD for j in range(d)),sp.zeros(d))
 ck('finite_triangular_inverse_'+str(d),(L0+NN)*RR==sp.eye(d) and (DD*NN)**d==sp.zeros(d))
 ctrl('geometric_diagonals_not_geometric_product_'+str(d),abs(RR[d-1,0])==2**(d*(d-1)//2) and max(sum(abs(NN[i,j]) for i in range(d)) for j in range(d))==1)
 B=3;C=2;raw=d*C**d*sum((B*d**3*C**d)**j for j in range(d));bound=d*d*max(1,B)**(d-1)*d**(3*(d-1))*C**(d*d)
 ck('mixed_bound_sum_'+str(d),raw<=bound)
# Coefficient norms compare summed passive polynomials without a coefficient-count factor.
P0={(0,2,7):field(2),(1,2,8,8):field(-3),(0,0,9):root2}
ck('passive_coefficient_sum_identity',l1(P0)==sum(l1({tuple(x for x in mon if x<7):v}) for mon,v in P0.items()))
deps=['tests/channel-swings/k2425_frame_euler_module_probe.py','tests/channel-swings/k2437_augmented_compatibility_adjoint_probe.py','lab/process/k2437-augmented-compatibility-adjoint.json','lab/process/k2443-hook-quantitative-symbol.json','explorations/conditional-build/k2446-augmented-diagonal-estimate-2026-11-01.md',str(Path(__file__).relative_to(ROOT))]
for pp in deps:
 if pp.endswith('.json'):
  rr=json.loads((ROOT/pp).read_text());ck('inherited_pins_'+Path(pp).stem,all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==v for p,v in rr['dependencies'].items()))
evidence={'original_direction':{'a':str(a),'b':str(b),'second_order_nonzero':len(bc)},'universal':'written diagonal composition, compatible mixed finite inverse and quadratic-exponential upper bound; restricted entire forcing consumer','finite_exact':'original tensor witness, fixed shear, passive monomials, scalar4/d, actual ambient mixed fixture','comparison_only':'triangular matrices with quadratic-exponential products do not prove hook lower bounds','ceilings':'no geometric mixed inverse, nonlinear convergence or native GU solution'}
report={'result_id':'K2446','checks':checks,'controls':controls,'evidence':evidence,'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2446-augmented-diagonal-estimate.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2446',len(checks),'checks',len(controls),'controls PASS')
