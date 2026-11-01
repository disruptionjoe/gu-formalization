"""Original hook rotation coercivity, symbol rank variation and analytic controls."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
from itertools import combinations,combinations_with_replacement
from math import factorial,prod
import json,hashlib,sys,ast
import sympy as sp
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'tests/channel-swings/k2435_fischer_frame_annihilator_probe.py';src=p.read_text()
# Reconstruct original161/112 generators and universal identities only, before generic rank.
exec(compile(src[:src.index('# Exact symbol rank')],str(p),'exec'),globals())
inherited=dict(checks);checks={};controls={}
def ck(name,v):
 checks[name]=bool(v)
 if not v:raise AssertionError(name)
def ctrl(name,v):
 controls[name]=bool(v)
 if not v:raise AssertionError(name)
ck('original_basis_and_covectors',len(rep)==161 and len(linear)==112 and alphas==[{0:F(1)},{2:F(9012),4:F(8519)},{5:F(1)},{6:F(1)},{7:F(1)},{8:F(1)},{9:F(1)}])
A0=sp.Matrix([[sp.Rational(symbol(h,alphas[0]).get(ij,0)) for h in rep] for ij in receivers]);rank0=A0.rank()
ck('all78_offdiagonal_rows_zero',all(not any(A0[receivers.index((i,j)),:]) for i,j in combinations(range(1,14),2)))
ck('two_independent_remaining_covectors',all(A0[receivers.index((0,0)),j]==0 and sum(eta[i]*A0[receivers.index((i,i)),j] for i in range(14))==0 for j in range(161)))
ck('original_special_rank_exact25',rank0==25)
avec=add(*[(r+1,a) for r,a in enumerate(alphas)]);Ag=sp.Matrix([[sp.Rational(symbol(h,avec).get(ij,0)) for h in rep] for ij in receivers]);rg=Ag.rank();ck('original_generic_rank88',rg==88);ctrl('constant_rank_elliptic_shortcut_false',rank0<rg)
prior=json.loads((ROOT/'lab/process/k2435-fischer-frame-annihilator.json').read_text());table=prior['rotation_elimination_table'];ops={}
for name,part in linear:
 if name[0]!='rotation':continue
 ops[tuple(name[1:])]={}
 for tt,h in part.items():
  for rr in range(7):
   vals=symbol(h,alphas[rr])
   for j,ij in enumerate(dark):
    if vals.get(ij,0):ops[tuple(name[1:])][rr,tt,j]=vals[ij]
us=[1,3,10,11,12,13];rs=[0,2,3,4,5,6];active=[0,5,6,7,8,9]
for row in table:
 u,ss,aa,partner=row['u'],row['s'],row['active_axis'],row['partner'];A=F(row['A']);B=F(row['B']) if row['B'] else None
 expected={}
 for v,rv in zip(us,rs):
  if v==u:continue
  j=dark.index(tuple(sorted((u,v))));val=A+(B if rv==ss and B is not None else 0)
  if val:expected[ss,rv,j]=val
 ck(f'original_row_{u}_{ss}',ops.get(tuple(sorted((aa,u))),{})==expected)
selected=[(3,0),(3,3),(3,4),(3,5),(3,6),(1,2),(10,2),(1,3),(1,4),(1,5),(1,6),(10,4),(10,5),(10,6),(11,5),(11,6),(12,6)]
inv={};records=[]
for u,ss in selected:
 row=next(z for z in table if z['u']==u and z['s']==ss);B=F(row['B']);lam=F(row['lambda']);v=-lam
 candidates={0,max(0,v.numerator//v.denominator),max(0,v.numerator//v.denominator+1)}
 gap=min(abs(B*(n+lam)) for n in candidates);inv[u,ss]=1/gap
 ck(f'nonresonant_min_{u}_{ss}',gap>0)
 records.append(dict(row,inverse_bound=str(1/gap),nearest_candidates=sorted(candidates)))
ck('exact_selected_inverse_bounds',[inv[3,j] for j in [0,3,4,5,6]]==[F(70,53),F(70),F(70,11),F(70,11),F(70,11)])
ck('remaining_inverse_bounds',inv[1,3]==35 and inv[1,4]==F(35,6) and inv[10,4]==F(70,11) and inv[11,5]==F(7,3))
k=sp.symbols('k',nonnegative=True)
bd1=(6790+3220*k)/71;bd10=95+46*k
expressions=[(3430+1610*k,35*(1+sp.Rational(71,70)*bd1)),(580+273*k,sp.Rational(35,6)*(1+sp.Rational(36,35)*bd1)),(620+297*k,sp.Rational(70,11)*(1+sp.Rational(71,70)*bd10)),(8000*(k+1),7737+3320*k)]
for j,(upper,expr) in enumerate(expressions):
 pp=sp.Poly(sp.expand(upper-expr),k);ck(f'uniform_affine_bound_{j}',all(a>=0 for a in pp.all_coeffs()))
ck('aggregate_bound',sp.expand(700+(3430+1610*k)+3*(580+273*k)+3*(620+297*k)+7)==7737+3320*k)
# Inhomogeneous actual Q in constant-symbol kernel, all original rotation rows evaluated.
cs={ij:{(0,0,2):F(j+1,7),(1,3,4):F((-1)**j,5)} for j,ij in enumerate(dark)}
QQ={ij:v for ij,v in cs.items()};norm=lambda P:sum(abs(v) for v in P.values())
ck('actual_nonzero_constant_kernel',bool(QQ) and all(not adj(h,QQ) for h in rep))
res={tuple(name[1:]):ladj(part,QQ) for name,part in linear if name[0]=='rotation'};MM=max(norm(P) for P in res.values())
ck('actual_polynomial_coercive_bound',MM>0 and sum(norm(P) for P in cs.values())<=(7737+3320*3)*MM)
for row in table:
 u,ss,partner=row['u'],row['s'],row['partner'];delta=pa(*[(1,der(cs[tuple(sorted((u,v)))],rv)) for v,rv in zip(us,rs) if v!=u]);want=pa((F(row['A']),mul({(ss,):F(1)},delta)))
 if row['B'] is not None:
  cc=cs[tuple(sorted((u,partner)))];want=pa((1,want),(F(row['B']),mul({(ss,):F(1)},der(cc,ss))),(F(row['A'])+F(row['B']),cc))
 ck(f'inhomogeneous_formula_{u}_{ss}',want==res[tuple(sorted((row['active_axis'],u)))])
ctrl('dropping_zero_order_changes_actual_residual',any(ladj(part,QQ)!=pa(*[(1,adj(h,{ij:der(v,r) for ij,v in QQ.items()})) for r,h in part.items()]) for name,part in linear if name[0]=='rotation'))
# Geometric off-kernel splitting: original88-coordinate minor and exact monomial gauge.
from math import lcm
free=[ij for ij in receivers if ij not in dark and ij not in [(1,1),(0,5)]]
ck('offkernel_gauge_dimension',len(free)==88)
restricted=Ag.extract([receivers.index(ij) for ij in free],list(range(161)))
pivots=restricted.rref()[1]
ck('original_offkernel_minor_nonzero',len(pivots)==88)
coeffs=[[[symbol(rep[j],alphas[r]).get(ij,F(0)) for r in range(7)] for ij in free] for j in pivots]
A=max(F(1),max(sum(abs(v) for v in entry) for row in coeffs for entry in row));D=lcm(*(v.denominator for row in coeffs for entry in row for v in entry))
ck('minor_coefficient_bounds',A>=1 and D>=1 and all((v*D).denominator==1 for row in coeffs for entry in row for v in entry))
beta={ij:next(iter(bb[ij].values())) for ij in [(0,5),(0,6),(5,6)]}
ck('actual_three_monomial_gauge_entries',bb[0,5]=={(0,2):beta[0,5]} and bb[0,6]=={(0,3):beta[0,6]} and bb[5,6]=={(2,3):beta[5,6]} and all(abs(v)==2 for v in beta.values()))
def without(P,r):return {m:v for m,v in P.items() if r not in m}
def mdivide(P,mon):
 out={}
 for m,v in P.items():
  rem=list(m)
  for r in mon:
   assert r in rem,(m,mon)
   rem.remove(r)
  out[tuple(rem)]=v
 return out
# Include monomials divisible by y0*y2, missing either factor, and missing both.
Qraw={ij:{(0,2,4):F(j+1,13),(0,0,3):F(j%5-2,7),(2,3,6):F(j%7-3,11),(1,4,6):F(j%3+1,17)} for j,ij in enumerate(receivers)}
qt={ij:pa((1,Qraw[ij]),(1,mul(Qraw[1,1],tau.get(ij,{})))) for ij in receivers if ij not in dark};qt={ij:P for ij,P in qt.items() if P}
b0=bb[0,5];q0=qt[0,5];tt={ij:pa((1,mul(b0,qt.get(ij,{}))),(-1,mul(bb.get(ij,{}),q0))) for ij in receivers};tt={ij:P for ij,P in tt.items() if P}
ck('gauge_exact88_support',all(ij in free for ij in tt))
g={m:v/beta[0,5] for m,v in mdivide({m:v for m,v in q0.items() if 0 in m and 2 in m},(0,2)).items()};r=pa((1,q0),(-1,mul(b0,g)))
rA=pa((-1/beta[5,6],mdivide(without(mdivide(tt[5,6],(2,)),0),(3,))))
rB=pa((-1/beta[0,6],mdivide(without(mdivide(tt[0,6],(0,)),2),(3,))))
rr=pa((1,rA),(1,rB),(-1,without(rB,0)))
ck('actual_remainder_recovered',r==rr)
ck('remainder_norm_bound',norm(r)<=sum(norm(P) for P in tt.values())/2)
qp={ij:pa((1/beta[0,5],mdivide(pa((1,tt.get(ij,{})),(1,mul(bb.get(ij,{}),r))),(0,2)))) for ij in receivers};qp={ij:P for ij,P in qp.items() if P}
ck('actual_quotient_representative',all(qp.get(ij,{})==pa((1,qt.get(ij,{})),(-1,mul(bb.get(ij,{}),g))) for ij in receivers))
ck('actual_offkernel_residual_preserved',all(adj(h,qp)==adj(h,Qraw) for h in rep))
bnorm=sum(norm(P) for P in bb.values())
ck('actual_offkernel_norm_bound',sum(norm(P) for P in qp.values())<=(F(1,2)+bnorm/4)*sum(norm(P) for P in tt.values()))
# Fixed degree88 monomials have strictly decreasing weight under lex reductions.
W=89**6
ck('lex_degree88_weight_gaps',all(89**j>88*sum(89**i for i in range(j)) for j in range(7)))
# A small exact division instance checks branching coefficients, not the universal proof.
vx,vy=sp.symbols('vx vy');Ptest=2*vx**2-vx*vy+3*vy**2;Ttest=vx**4-2*vx*vy**3+vy**4
quot,rem=sp.div(sp.Poly(Ptest*Ttest,vx,vy),sp.Poly(Ptest,vx,vy));ck('lex_exact_division_fixture',quot.as_expr()==Ttest and rem.is_zero)
G=sum(abs(v) for name,part in linear if name[0]=='rotation' for h in part.values() for aa in alphas for v in symbol(h,aa).values())
offkernel={'minor_size':88,'selected_hook_indices':list(pivots),'entry_l1_bound_A':str(A),'common_denominator_D':D,'b_l1':str(bnorm),'rotation_l1_bound_G':str(G),'lex_weight_W':W,'t_bound':'2*88!*A^87*D^88*(1+88!*(A*D)^88)^[W*(k+90)+1] * ||H Q||_1','representative_bound':'(1/2+||b||_1/4)*||t||_1','scope':'original full ordinary-adjoint quotient, geometric in degree; mixed and nonlinear estimates separate'}
# Exact comparison equations: finite witnesses accompany the universal recurrence proof.
x,y=sp.symbols('x y');rec=[]
for degree in [0,1,2,5,10,20]:
 f=sum(sp.Rational(factorial(degree),factorial(degree-j))*x**j*y**(degree-j) for j in range(degree+1));g=sum(sp.Rational(factorial(degree),factorial(degree-j)*factorial(j+1))*x**j*y**(degree-j) for j in range(degree+1))
 ck(f'triangular_bad_recurrence_{degree}',sp.expand(f-x*sp.diff(f,y)-y**degree)==0)
 ck(f'denominator_good_recurrence_{degree}',sp.expand(x*sp.diff(g,x)+g-x*sp.diff(g,y)-y**degree)==0)
 ck(f'geometric_good_bound_{degree}',all(sp.Rational(factorial(degree),factorial(degree-j)*factorial(j+1))<=2**degree for j in range(degree+1)))
 rec.append({'degree':degree,'bad_x_power':str(factorial(degree)),'good_x_power':str(sp.Rational(1,degree+1))})
ctrl('identity_diagonals_do_not_bound_inverse_geometrically',factorial(20)>2**20)
deps=dict(prior['dependencies'])
for path in ['tests/channel-swings/k2435_fischer_frame_annihilator_probe.py','lab/process/k2435-fischer-frame-annihilator.json',str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2443-hook-quantitative-symbol-2026-11-01.md']:deps[path]=hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
for path,digest in deps.items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
report={'result_id':'K2443','checks':checks,'controls':controls,'actual_symbol_ranks':{'y_e0':rank0,'y_1_through_7':rg},'selected_rows':records,'uniform_bound':'7737+3320k <=8000(k+1)','offkernel':offkernel,'example':{'degree':3,'quotient_l1':str(sum(norm(P) for P in cs.values())),'max_rotation_residual_l1':str(MM)},'comparison_recurrences':rec,'evidence_kinds':{'exact':'original161 repeated hooks and112 generators; all36 row identities; actual special and generic matrices; exact inverse gaps; inhomogeneous original polynomial','universal':'written coefficient-l1 elimination, fixed-polynomial division and ordinary adjoint quotient estimate, rank restriction and factorial/geometric comparison proofs; no mixed or nonlinear analytic inverse'},'dependencies':deps}
out=ROOT/'lab/process/k2443-hook-quantitative-symbol.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2443',len(checks),'checks',len(controls),'controls PASS; ranks',rank0,rg,flush=True)
