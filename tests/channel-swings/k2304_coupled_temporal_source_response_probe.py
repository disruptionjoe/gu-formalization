from pathlib import Path
import json,hashlib,sys
import sympy as s
ROOT=Path(__file__).resolve().parents[2];checks={}
def check(n,v): checks[n]=bool(v)
def zero(v): return s.simplify(v)==0

import ast
from fractions import Fraction as Q
from itertools import combinations
from k77_exact_bank_api import K77Core,load_bank
bank=load_bank();c=K77Core(bank.signature,bank.channels);eta=c.eta
source='tests/channel-swings/k2298_enlarged_native_companion_probe.py'
tree=ast.parse((ROOT/source).read_text());names={'form','Epair','Laxis','curvature'}
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names],type_ignores=[]),source,'exec'))
def sumforms(vs):
 out={}
 for v in vs:out=c.fadd(out,v)
 return out
odd=[form(i,(i,)) for i in [1,2,3]]+[sumforms(form(i,(i,)) for i in range(4,14))]+[c.fadd(form(i,(j,)),form(j,(i,))) for i,j in combinations([1,2,3],2)]
even=[form(i,(0,i)) for i in [1,2,3]]+[sumforms(form(i,(0,i)) for i in range(4,14))]+[c.fadd(form(i,(0,j)),form(j,(0,i))) for i,j in combinations([1,2,3],2)]
basis=odd+even
B4=s.Matrix([[-1,1,1,10],[1,-1,1,10],[1,1,-1,10],[1,1,1,8]])
B=s.diag(B4,-2*s.eye(3));G7=s.diag(1,1,1,10,2,2,2);G=s.diag(G7,-G7);L=s.zeros(14);L[:7,7:]=B;L[7:,:7]=B
R=s.Matrix([[0,1,1,0,0,0],[1,0,1,0,0,0],[1,1,0,0,0,0],[1,1,1,0,0,0],[0,0,0,-1,0,0],[0,0,0,0,-1,0],[0,0,0,0,0,-1]])
def formcol(v):return sumforms(c.fscale(Q(v[i]),basis[i]) for i in range(14))
for j,b in enumerate(basis):check('native_L_column_'+str(j),Laxis(0,b)==formcol(L[:,j]))
actualG=s.Matrix([[s.Rational(c.pair(u,c.hodge(v))[0]) for v in basis] for u in basis])
check('native_all_grams',actualG==G);check('nondegenerate_reducing',G.det()!=0 and L.T*G+G*L==s.zeros(14))
slots=[(1,1),(2,2),(3,3),(1,2),(1,3),(2,3)]
# Check actual A image as forms, not only projection pairings.
for j,slot in enumerate(slots):check('native_A_image_'+str(j),c.hodge(curvature(slot))==formcol(R[:,j].col_join(s.zeros(7,1))))
pairs=s.Matrix([[s.Rational(c.pair(v,curvature(slot))[0]) for v in basis] for slot in slots])
check('native_Astar_six_rows',pairs==(R.T*G7).row_join(s.zeros(6,7)))
check('native_four_temporal_rows',all(not curvature(slot) for slot in [(0,0),(0,1),(0,2),(0,3)]))
k,z=s.symbols('k z',nonzero=True,real=True);Delta=(k*k-121*z*z)*(k*k-4*z*z);N=17*k*k-113*z*z
inv=(k*k*s.eye(7)-z*z*B*B).inv();Sm=-k*z**4*R.T*G7*inv*R
mf=-k*z**4/(k*k-4*z*z);ms=-2*k*z**4*N/Delta
expected=s.diag(mf*s.eye(3)+(ms-mf)*s.ones(3)/3,2*mf*s.eye(3))
check('native_full_schur',all(zero(a) for a in Sm-expected))
check('restricted_previous_response',zero(Sm[0,0]+12*k*z**4*(k*k-13*z*z)/Delta) and zero(Sm[1,0]+k*z**4*(11*k*k-35*z*z)/Delta))
W=s.diag(1,1,1,2,2,2);Jmap=expected.inv()*W
Tmap=(-k*z*z*inv*R*Jmap).col_join(z**3*B*inv*R*Jmap)
check('all_six_joint_companion_rows',all(zero(a) for a in (k*s.eye(14)+z*L)*Tmap+z*z*R.col_join(s.zeros(7,6))*Jmap))
check('all_six_joint_metric_rows',all(zero(a) for a in z*z*pairs*Tmap-W))
check('old_companion_poles_cancel',all(s.denom(s.cancel(a)).subs(z,k/11)!=0 and s.denom(s.cancel(a)).subs(z,k/2)!=0 for a in list(Jmap)+list(Tmap)))
alpha=s.symbols('alpha',real=True);pvec=s.Matrix([1,1,1,0,0,0,0]);ivec=s.Matrix([1,1,1,1,0,0,0]);h=s.Matrix([1,1,1,0,0,0]);to=17*k*(6*pvec-ivec)/270;te=17*alpha*(12*pvec-7*ivec)/270
res=(k*s.eye(14)+alpha*L)*to.col_join(te)+alpha**2*R.col_join(s.zeros(7,6))*h
check('full_homogeneous_companion',all(zero(s.expand(a).subs(alpha**2,17*k*k/113)) for a in res))
check('full_homogeneous_metric',pairs*to.col_join(te)==s.zeros(6,1))
check('homogeneous_not_companion_root',s.factor(Delta.subs(z*z,17*k*k/113))!=0)
check('zero_order_four',s.limit(mf/z**4,z,0)==-1/k and s.limit(ms/z**4,z,0)==-34/k)
# Compact forcing columns: two tracefree diagonals, three offdiagonals; scalar N D4.
Tf=s.Matrix([[1,1,0,0,0],[-1,0,0,0,0],[0,-1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]])
comp=(Jmap.col_join(Tmap))*Tf*z**4
check('tracefree_compact_repair',all(s.Poly(s.cancel(a),z) is not None for a in comp))
compS=(Jmap.col_join(Tmap))*h*N*z**4
check('scalar_compact_repair',all(s.Poly(s.cancel(a),z) is not None for a in compS))
# Square-integrable closed Schur domain: both multipliers order2 at infinity.
w=s.symbols('w',positive=True);check('schur_order_two',s.limit(mf.subs(z,s.I*w)/w**2,w,s.oo)==-k/4 and s.limit(ms.subs(z,s.I*w)/w**2,w,s.oo)==-113*k/242)
t=s.symbols('t',real=True);hp=h*(t*t+t**3);top=-R*hp.diff(t,2)/k;tep=B*R*hp.diff(t,3)/k**2;tp=top.col_join(tep)
check('polynomial_tempered_homogeneous',all(zero(a) for a in k*tp+L*tp.diff(t)+R.col_join(s.zeros(7,6))*hp.diff(t,2)) and pairs*tp.diff(t,2)==s.zeros(6,1))
check('scalar_curvature_not_gauge',bool(sumforms(curvature(slot) for slot in [(1,1),(2,2),(3,3)])))
assert all(checks.values()),[a for a,b in checks.items() if not b]
bad=L.copy();bad[3,7]=9
faults={
 'wrong_normal_multiplicity':['native_L_column_7'] if formcol(bad[:,7])!=Laxis(0,basis[7]) else [],
 'omit_even_companion':['full_homogeneous_companion'] if any(not zero(s.expand(a).subs(alpha**2,17*k*k/113)) for a in (k*s.eye(14)+alpha*L)*to.col_join(s.zeros(7,1))+alpha**2*R.col_join(s.zeros(7,6))*h) else [],
 'omit_offdiagonal_factor_two':['all_six_joint_metric_rows'] if pairs*Tmap*z*z!=s.eye(6) else [],
 'replace_scalar113':['native_full_schur'] if not zero(ms+2*k*z**4*(17*k*k-112*z*z)/Delta) else [],
 'retain_restricted_pole':['full_homogeneous_companion'] if any(not zero(s.expand(a).subs(alpha**2,k*k/13)) for a in res) else [],
 'drop_normal_metric_source':['full_homogeneous_metric'] if (R[:3,:].T*G7[:3,:3]*to[:3,:])!=s.zeros(6,1) else []}
result='K2304';note='explorations/conditional-build/k2304-coupled-temporal-source-response-2026-10-30.md';report='k2304-coupled-temporal-source-response.json';extra_deps=[source,'tests/channel-swings/k77_exact_bank_api.py','tests/fixtures/k77_exact_coefficient_bank_v1.json'];evidence='Exact native Clifford and rational matrix identities; continuum Fourier/domain and moment proofs in note';details={'B':B.tolist(),'R':R.tolist(),'scalar_response':str(ms),'tracefree_response':str(mf)}
details={k:str(v) for k,v in details.items()}

assert all(checks.values()),[k for k,v in checks.items() if not v]
assert all(faults.values()),faults
deps=[str(Path(__file__).relative_to(ROOT)),note]+extra_deps
data=dict(schema_version='1.0',result_id=result,checks=len(checks),check_names=list(checks),mutation_failed_checks=faults,evidence_kind=evidence,dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details=details)
out=ROOT/'lab/process'/report
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result=result,checks=len(checks),faults=len(faults))))
