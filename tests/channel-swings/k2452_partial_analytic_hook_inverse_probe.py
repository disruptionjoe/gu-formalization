"""Exact original hook analytic subfamilies; no finite-rank extrapolation."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
from itertools import combinations,combinations_with_replacement
from math import factorial,prod,comb
import ast,json,hashlib,sys
SOURCE_FILE=Path(__file__).resolve()
ROOT=Path(sys.argv[sys.argv.index('--root')+1]).resolve() if '--root' in sys.argv else SOURCE_FILE.parents[2]
p37=ROOT/'tests/channel-swings/k2437_augmented_compatibility_adjoint_probe.py';t37=p37.read_text()
# The inherited prefix reconstructs original K/h and exact coefficients only;
# it stops before the predecessor's polynomial fixtures or output writes.
exec(compile(t37[t37.index('source25path='):t37.index('for deg in range(8):')],str(p37),'exec'),globals())
inherited=dict(checks);checks={};controls={}
for node in ast.parse(t37).body:
 if isinstance(node,ast.FunctionDef) and node.name in {'jp','ja'}:
  exec(compile(ast.Module(body=[node],type_ignores=[]),str(p37),'exec'),globals())
ck('inherited_original_witness',all(inherited.values()))
allowed=tuple(range(7))+(7,9,10,12)
ck('eleven_selected_coordinates',len(set(allowed))==11)
c=F(9012,8519)
# Exact symbols on the entire ambient coordinate basis prove the displayed
# linear symbol formula universally, not only on selected covectors.
for r in range(14):
 xi={r:F(1)};v=-xi.get(2,0)+c*xi.get(4,0)
 want={(11,11):2*v,(13,13):-2*v,(2,11):xi.get(11,0),(4,11):c*xi.get(11,0),(2,13):-xi.get(13,0),(4,13):-c*xi.get(13,0)}
 ck('ambient_symbol_formula_'+str(r),symbol(h,xi)=={k:v for k,v in want.items() if v})
rank_witness=[symbol(h,{r:F(1)}) for r in (2,11,13)]
ck('ambient_symbol_rank_exactly_three',all(rank_witness[i].get(key,0)!=0 and all(not rank_witness[j].get(key,0) for j in range(3) if j!=i) for i,key in enumerate(((11,11),(2,11),(2,13)))))
for r in allowed:
 xi=covs[r]
 ck('selected_covector_in_S_'+str(r),xi.get(11,0)==xi.get(13,0)==0 and -xi.get(2,0)+c*xi.get(4,0)==0)
 for slot in range(3):
  out=defaultdict(F)
  for ix,v in h.items():out[ix[:slot]+ix[slot+1:]]+=eta[ix[slot]]*xi.get(ix[slot],0)*v
  ck('slot_contraction_'+str(r)+'_'+str(slot),not any(out.values()))
 ck('full_ordinary_symbol_zero_'+str(r),not symbol(h,xi))
# These three independent constraints give dim S=11; inspect the actual
# omitted passive symbols rather than assuming all W parameters are passive.
for r in (8,11,13):ctrl('forbidden_passive_symbol_'+str(r),bool(symbol(h,covs[r])))
aa=[jlinear(h,covs[r]) for r in range(14)];bb={}
for r in range(14):
 for s in range(14):
  for t in range(7):
   v=-sum(F(eta[i]*eta[j],2)*av*bv*fp(KE[t],h,i,j) for i,av in covs[r].items() for j,bv in covs[s].items())
   if v:bb[r,s,t]=ff(v)
ck('all_original_second_order_terms_zero_on_S',not any(v for (r,s,t),v in bb.items() if r in allowed and s in allowed))
ck('nonzero_transverse_integration_direction',aa[1]==field(2253)/2)
ck('inherited_second_direction',aa[2]==field(2253)/17038)
ck('complete_first_order_bank',all(not v for r,v in enumerate(aa) if r not in (1,2)))
ck('explicit_scalar_radius_factor',1+abs(aa[2]/aa[1])==field(8520)/8519)
ck('explicit_hook_norm',sum(abs(v) for v in h.values())==4*(1+c))
a0=aa[1]
def integrate(P):return {tuple(sorted(m+(1,))):v/(m.count(1)+1) for m,v in P.items()}
def lateral(P):return pa(*[(aa[r],der(P,r)) for r in allowed if r!=1 and aa[r]])
def primitive_full(P):
 term=pa((1/a0,integrate(P)));out=dict(term)
 # Each derivative-integration step decreases non-y1 degree by one;
 # integration commutes with all those derivatives.
 for _ in range(max((len(m) for m in P),default=0)+1):
  term=pa((-1/a0,integrate(lateral(term))))
  if not term:break
  out=pa((1,out),(1,term))
 ck('primitive_series_terminates_'+str(len(checks)),not term)
 return out
def ordinary(P):
 out={}
 for r in range(14):
  for ij,v in symbol(h,covs[r]).items():out[ij]=pa((1,out.get(ij,{})),(ff(v),der(P,r)))
 return {k:v for k,v in out.items() if v}
fixtures=[{(2,7,9):field(2),(1,10,12):root2},{(7,)*5:field(1)},{(2,9,10,12):field(-3),(1,1,7,12):root2}]
normalization_control=False
for i,P in enumerate(fixtures):
 d=1+len(next(iter(P)));V=primitive_full(P);scaled=pa((field(d)/4,V))
 ck('original_scalar_primitive_'+str(i),jp(V,(aa,bb))==P)
 ck('full_ordinary_zero_'+str(i),not ordinary(V))
 ck('boundary_ideal_'+str(i),all(1 in m for m in V))
 ck('dependence_stays_in_S_'+str(i),all(set(m)<=set(allowed) for m in V))
 ck('actual_degree_normalization_'+str(i),pa((field(4)/d,jp(scaled,(aa,bb))))==P)
 normalization_control|=pa((field(4)/d,jp(V,(aa,bb))))!=P
ctrl('dropping_degree_normalization_detected',normalization_control)
# A full mixed ordinary response rejects extending the chosen scalar ring to
# all passive variables. This uses original h/covs, not an abstract matrix.
ctrl('full_W_extension_fails',bool(ordinary({(1,8):field(1)})))
# Original scalar EW/WW terms strictly lower passive degree: each b term
# multiplies one E coordinate and has precisely the shown W derivatives.
ck('mixed_scalar_passive_filtration',all(((r>=7)+(s>=7)) in (1,2) for (r,s,t) in bb if r>=7 or s>=7))
ck('all_multiplier_coordinates_transverse',all(t<7 for r,s,t in bb))
# The fixed-m geometric majorization is elementary, checked at endpoints and
# mixed (m,d) fixtures. It is not the all-degree proof (given in the note).
for m,d in [(0,4),(1,4),(3,7),(8,12)]:
 B=F(3,2);C=F(2);lhs=d*C**d*sum((B*d**3*C**d)**j for j in range(min(m,d-1)+1))
 mid=(m+1)*max(1,B)**m*d**(3*m+1)*C**((m+1)*d)
 Cm=2**(3*m+1)*(m+1)*max(1,B)**m*C**(m+1)
 ck('fixed_m_geometric_majorization_'+str(m)+'_'+str(d),lhs<=mid<=Cm**d)
note='explorations/conditional-build/k2452-partial-analytic-hook-inverse-2026-11-01.md'
probe='tests/channel-swings/k2452_partial_analytic_hook_inverse_probe.py'
deps=[note,probe,'explorations/conditional-build/k2446-augmented-diagonal-estimate-2026-11-01.md','explorations/conditional-build/k2449-full-mixed-boundary-adjoint-2026-11-01.md','tests/channel-swings/k2437_augmented_compatibility_adjoint_probe.py','tests/channel-swings/k2425_frame_euler_module_probe.py','lab/process/k2437-augmented-compatibility-adjoint.json']
report={'result_id':'K2452','checks':checks,'controls':controls,'allowed_adapted_coordinates':list(allowed),'original_first_order_coefficients':[str(v) for v in aa],'ambient_second_order_nonzero':len(bb),'selected_second_order_nonzero':sum(r in allowed and s in allowed for r,s,t in bb),'evidence_kinds':{'universal':'written original mixed passive-degree filtration, geometric fixed-m bound, exact eleven-dimensional contraction argument and analytic primitive','finite_exact':'original symbol coefficients, all slot contractions, full scalar coefficient bank and nonzero mixed controls','ceiling':'no unrestricted mixed quotient bound, nonlinear closure or source-native identification'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2452-partial-analytic-hook-inverse.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
elif '--output' in sys.argv:Path(sys.argv[sys.argv.index('--output')+1]).write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2452',len(checks),'checks',len(controls),'controls PASS')
print('ambient a:',[str(v) for v in aa])
