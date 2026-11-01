"""Exact original ordinary all-degree image; no augmented compatibility claim."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
from itertools import combinations,combinations_with_replacement
from math import factorial,prod
import json,hashlib,sys
import sympy as sp
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'tests/channel-swings/k2425_frame_euler_module_probe.py';src=p.read_text()
exec(compile(src[:src.index('ss=[[symbol')],str(p),'exec'),globals())
inherited=dict(checks);checks={};controls={}
# Sparse ordinary polynomials, monomials as sorted repeated variable indices.
def pa(*terms):
 d=defaultdict(F)
 for c,P in terms:
  for m,v in P.items():d[m]+=c*v
 return {m:v for m,v in d.items() if v}
def mul(P,Q):
 d=defaultdict(F)
 for m,v in P.items():
  for t,w in Q.items():d[tuple(sorted(m+t))]+=v*w
 return {m:v for m,v in d.items() if v}
def der(P,r):
 d={}
 for m,v in P.items():
  if r in m:
   t=list(m);t.remove(r);d[tuple(t)]=v*m.count(r)
 return d
def fisher(P,Q):return sum(v*Q.get(m,0)*prod(factorial(a) for a in Counter(m).values()) for m,v in P.items())
def adj(h,Q):
 return pa(*[(v,mul({(r,):F(1)},Q.get(ij,{}))) for r in range(7) for ij,v in symbol(h,alphas[r]).items()])
def ladj(part,Q):return pa(*[(1,der(adj(h,Q),r)) for r,h in part.items()])
def primal(part,f):
 out=defaultdict(dict)
 for t,h in part.items():
  hf=mul({(t,):F(1)},f)
  for r in range(7):
   for ij,v in symbol(h,alphas[r]).items():out[ij]=pa((1,out[ij]),(v,der(hf,r)))
 return dict(out)
def cprimal(h,f):
 out=defaultdict(dict)
 for r in range(7):
  for ij,v in symbol(h,alphas[r]).items():out[ij]=pa((1,out[ij]),(v,der(f,r)))
 return dict(out)
def pairing(P,Q):return sum(fisher(p,Q.get(ij,{})) for ij,p in P.items())
tau={(i,i):{():F(eta[i])} for i in range(n)}
xi=[{(r,):F(a[i]) for r,a in enumerate(alphas) if i in a} for i in range(n)]
bb={ij:pa(((2 if ij[0]!=ij[1] else 1)*eta[ij[0]]*eta[ij[1]],mul(xi[ij[0]],xi[ij[1]]))) for ij in receivers}
bb={ij:v for ij,v in bb.items() if v}
ck('all161_trace_and_double_divergence_constant_operators',all(not adj(h,Q) for h in rep for Q in [tau,bb]))
# For arbitrary polynomial f, linear adjoint of Q*f has constant and derivative-f coefficients.
ck('all112_universal_linear_operators',all(not ladj(part,Q) and all(not adj(part.get(r,{}),Q) for r in range(7)) for _,part in linear for Q in [tau,bb]))
# Nontrivial original primal/dual pairing with repeated monomial factorials.
Q={ij:{(0,0,1):F((z%9)-4,7),(2,3,3):F((z%5)-2,3)} for z,ij in enumerate(receivers)}
f={(0,1,1):F(2,3),(2,2,3):F(-3,5)}
fc={(0,0,1,1):F(2,7),(2,2,3,4):F(3,11)}
ck('all161_original_constant_Fischer_pairings',all(pairing(cprimal(h,fc),Q)==fisher(fc,adj(h,Q)) for h in rep))
ck('all112_original_linear_Fischer_pairings',all(pairing(primal(part,f),Q)==fisher(f,ladj(part,Q)) for _,part in linear))
wrong=[]
for name,part in linear:
 # Deliberately omit derivative of the linear y factor in D*Q.
 z=pa(*[(1,adj(h,{ij:der(v,r) for ij,v in Q.items()})) for r,h in part.items()])
 if z!=ladj(part,Q):wrong.append(list(name))
ctrl('omitted_linear_generator_derivative_detected',bool(wrong))
bbad={ij:pa((F(1,2) if ij[0]!=ij[1] else 1,v)) for ij,v in bb.items()}
ctrl('raw_symmetric_offdiagonal_factor_detected',any(adj(h,bbad) for h in rep))
# Actual inactive receiver support gives a constructive constant-only cokernel.
inactive=[i for i in range(n) if not xi[i]];dark=list(combinations(inactive,2))
ck('original_six_inactive_axes',inactive==[1,3,10,11,12,13])
ck('fifteen_dark_receivers_annihilate_repeated_symbol',len(dark)==15 and all(not symbol(h,a).get(ij,0) for h in rep for a in alphas for ij in dark))
# At degree zero all dark covectors are resolved by rotation equations, not Koszul.
darkrot=sp.Matrix([[sum(symbol(h,alphas[r]).get(ij,0) for r,h in part.items()) for ij in dark] for name,part in linear if name[0]=='rotation'])
ck('rotation_resolves_dark_constant_subspace',darkrot.rank()==15)
ck('Koszul_cannot_resolve_dark_constants',all(not sum(symbol(h,alphas[r]).get(ij,0) for r,h in part.items()) for name,part in linear if name[0]=='koszul' for ij in dark))
# Exact symbol rank at a named generic nonzero transverse covector; no generic degree claim.
avec=add(*[(r+1,a) for r,a in enumerate(alphas)])
M=sp.Matrix([[sp.Rational(symbol(h,avec).get(ij,0)) for h in rep] for ij in receivers])
rr=M.rank();print('repeated symbol rank',rr,flush=True)
ck('constant_only_kernel_strictly_exceeds_universal_two',105-rr>=17)
# Inspect the exact remaining 91-by15 first-order rotation system.
rotops=[]
for name,part in linear:
 if name[0]!='rotation':continue
 co={}
 for t,h in part.items():
  for r in range(7):
   v=symbol(h,alphas[r])
   for ij in dark:
    if v.get(ij,0):co[str((r,t,dark.index(ij)))]=str(v[ij])
 if co:rotops.append({'rotation':list(name),'coefficients':co})
# The operator bank is stored in the final report, without scratch writes.
# Structural successor: solve the remaining rotation subsystem in EVERY degree.
import ast
ops={tuple(d['rotation'][1:]):{ast.literal_eval(k):F(v) for k,v in d['coefficients'].items()} for d in rotops}
us=[1,3,10,11,12,13];rs=[0,2,3,4,5,6];active=[0,5,6,7,8,9];table=[]
for u,ru in zip(us,rs):
 for aa,r,ur in zip(active,rs,us):
  o=ops.get(tuple(sorted((aa,u))),{});keys=[(r,rv,dark.index(tuple(sorted((u,v))))) for v,rv in zip(us,rs) if v!=u]
  assert set(o)<=set(keys)
  rest=[o.get(key,F(0)) for key in keys if key[1]!=r];assert len(set(rest))==1
  A=rest[0];B=None if u==ur else o.get((r,r,dark.index(tuple(sorted((u,ur))))),F(0))-A
  table.append({'u':u,'s':r,'active_axis':aa,'partner':ur,'A':str(A),'B':None if B is None else str(B),'lambda':None if B is None else str((A+B)/B)})
ck('all36_original_rotation_operator_identities',len(table)==36)
ck('anchor_divergence',next(z for z in table if z['u']==3 and z['s']==2)['A']=='-1')
ck('every_other_divergence_propagates',all(F(z['A'])!=0 for z in table if z['s']==2 and z['u']!=3))
ck('all30_Euler_shifts_nonresonant',all(F(z['B'])!=0 and not (F(z['lambda']).denominator==1 and F(z['lambda'])<=0) for z in table if z['B'] is not None))
ck('generic_rank88_with_universal17_kernel',rr==88)
# The primitive quadratic entries remove all rational denominators.
y=sp.symbols('y0:7');qb=[]
for ij in [(0,5),(0,6),(5,6)]:qb.append(sum(sp.Rational(v)*prod(y[r] for r in mon) for mon,v in bb[ij].items()))
ck('quadratic_kernel_primitive_three_entries',sp.gcd(sp.gcd(qb[0],qb[1]),qb[2]).is_number and sp.gcd(sp.gcd(qb[0],qb[1]),qb[2])!=0)
ck('inactive_diagonal_extracts_trace_coefficient',bb.get((1,1),{})=={} and tau[1,1]=={():F(-1)})
# Wrong zero-order simplification changes the original exact shift.
row=next(z for z in table if z['u']==3 and z['s']==0)
ctrl('naive_Euler_plus_one_shift_rejected',row['lambda']=='53/54' and row['lambda']!='1')
# All-degree rank now follows from the proved annihilator, not fitted rank extrapolation.
from math import comb
rk=lambda k:104*comb(k+6,6)-(comb(k+4,6) if k>=2 else 0)
ck('all_degree_formula_reproduces_inherited_T0_through_T7', [rk(k) for k in range(8)]==[104,728,2911,8729,21812,47964,95886,178002])
ck('ambient_filtration_convolution',all(sum(comb(m+5-k,6)*rk(k) for k in range(m))==104*comb(m+12,13)-(comb(m+10,13) if m>=3 else 0) for m in range(1,16)))
# Polynomial Poincare identity on a mixed homogeneous scalar and a nonclosed control.
phi={(0,0,1,2,2):F(3,7),(3,4,5,6,6):F(-5,11)}
qs=[der(phi,r) for r in range(7)]
recovered=pa(*[(F(1,5),mul({(r,):F(1)},qs[r])) for r in range(7)])
ck('homogeneous_potential_recovery',recovered==phi)
ck('potential_is_closed',all(der(qs[a],b)==der(qs[b],a) for a,b in combinations(range(7),2)))
qbad=[dict(q) for q in qs];qbad[0]=pa((1,qbad[0]),(1,{(1,1,1,1):F(1)}))
ctrl('nonclosed_potential_rejected',any(der(qbad[a],b)!=der(qbad[b],a) for a,b in combinations(range(7),2)))
# An exact arbitrary-delay resonance in the same D(linear generator*f) architecture.
N=11;ev={str(k):[k-N-(N+2)*b for b in range(k+1)] for k in range(N+1)}
ck('resonance_preceding_degrees_surjective',all(all(v for v in ev[str(k)]) for k in range(N)))
ck('resonance_degree_N_one_dimensional_failure',ev[str(N)].count(0)==1 and ev[str(N)][0]==0)
ctrl('finite_saturation_does_not_certify_all_degrees',0 in ev[str(N)] and all(ev['7']))
# Recursive dependency pins inherited from the previous complete original-module report.
prior=json.loads((ROOT/'lab/process/k2433-lower-quartic-compatibility.json').read_text())
pins=dict(prior['dependencies']);pins['tests/channel-swings/k2425_frame_euler_module_probe.py']=hashlib.sha256((ROOT/'tests/channel-swings/k2425_frame_euler_module_probe.py').read_bytes()).hexdigest()
for path,digest in pins.items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
report={'result_id':'K2435','scope':'Exact ordinary original frame/Euler image in every homogeneous degree; no augmented compatibility, new shared Euler order or convergence claim.','checks':checks,'controls':controls,'dependencies':pins,'original_generator_counts':{'constant':len(rep),'koszul':21,'rotation':91},'rotation_operator_bank':rotops,'rotation_elimination_table':table,'inactive_axes':inactive,'dark_receivers':[list(x) for x in dark],'dark_rotation_rank':15,'constant_symbol_rank_at_y_1_through_7':rr,'omitted_derivative_detected_generators':wrong,'delay_countermodel':{'N':N,'eigenvalues':ev},'evidence_kinds':{'exact':'original rational generators; full adjoint coefficients; primal/dual factorial pairing; support and rank; contrary constructions','universal':'written Fischer adjoint and homogeneous potential proofs; original nonresonant rotation elimination proves ordinary all-degree completeness'}}
path=ROOT/'lab/process/k2435-fischer-frame-annihilator.json'
if '--check' in sys.argv:assert json.loads(path.read_text())==report
else:path.write_text(json.dumps(report,indent=2)+'\n')
print('K2435',len(checks),'checks',len(controls),'controls PASS',flush=True)
