from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json,hashlib,sys
import sympy as s
from k77_exact_bank_api import K77Core,load_bank
ROOT=Path(__file__).resolve().parents[2];bank=load_bank();c=K77Core(bank.signature,bank.channels);eta=c.eta;checks={}
def check(n,v):checks[n]=bool(v)
def form(mu,J):return {1<<mu:c.blade(J)}
def Epair(t,u,v):
 k={1<<t:{0:(Q(1),Q(0))}}
 a=c.pair(v,c.shiab(c.wedge_raw(k,u)));b=c.pair(u,c.shiab(c.wedge_raw(k,v)))
 assert a[1]==b[1]==0
 return (a[0]-b[0])/2
old=json.loads((ROOT/'lab/process/k2297-symmetric-shiab-companion.json').read_text())
for p,h in old['dependencies'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
receivers=[tuple(v) for v in old['nonzero_receivers']];Et=s.Matrix([[s.Rational(v) for v in row] for row in old['nonzero_coefficients']]);selectors=[]
for row,(i,a,b) in enumerate(receivers):
 if i in (a,b):
  sel=[0]*64;sel[row]=1;selectors.append(sel)
for a,b,d in combinations(range(4),3):
 ids=[receivers.index(z) for z in [(a,b,d),(b,a,d),(d,a,b)]]
 sel=[0]*64;sel[ids[0]]=eta[b];sel[ids[1]]=eta[a];selectors.append(sel)
 sel=[0]*64;sel[ids[0]]=eta[d];sel[ids[2]]=-eta[a];selectors.append(sel)
P=s.Matrix(selectors);projected=P*Et
check('full_firstjet_hook_rank',projected.rank()==Et.rank()==20)
check('same_firstjet_kernel',projected.col_join(Et).rank()==20)
check('repeated_rows_alone_insufficient',Et[[i for i,(mu,a,b) in enumerate(receivers) if mu in (a,b)],:].rank()==12)
# All grade5 inputs that can reach the four used horizontal triple labels.
# K132 XOR identity implies J=L xor{t} xor{mu}; popcount5 forces t,mu outside L and distinct.
columns=[];alternating=True;nonzero=0
for triple in combinations(range(4),3):
 a,b,d=triple;vs=[form(a,(b,d)),form(b,(a,d)),form(d,(a,b))]
 for t in range(14):
  if t in triple:continue
  for mu in range(14):
   if mu in triple or mu==t:continue
   J=tuple(sorted((*triple,t,mu)));u=form(mu,J);vals=[Epair(t,u,v) for v in vs]
   alternating &= eta[b]*vals[0]+eta[a]*vals[1]==0 and eta[d]*vals[0]-eta[a]*vals[2]==0
   nonzero+=any(vals);columns.append([list(triple),t,mu,[str(z) for z in vals]])
check('all440_grade5_columns_alternating',len(columns)==440 and alternating and nonzero>0)
check('grade5_repeated_label_impossible',all(len(set(J)^{mu}^{t})!=1 for J in combinations(range(14),5) for mu in range(14) for t in range(4)))
# Sparse K^-1 E coefficient action. XOR label determines every possible output.
def Laxis(t,u):
 out={}
 for fm,element in u.items():
  mu=fm.bit_length()-1
  for J,coeff in element.items():
   assert coeff[1]==0
   inp={fm:{J:(Q(1),Q(0))}};label=J^fm^(1<<t)
   for nu in range(14):
    mask=label^(1<<nu);v={1<<nu:{mask:(Q(1),Q(0))}}
    z=Epair(t,inp,v);gram=c.pair(v,c.hodge(v))[0]
    assert gram in (-1,1)
    if z:out=c.fadd(out,c.fscale(coeff[0]*z/gram,v))
 return out
def curvature(slot):
 # h_ii''=1, derivative in0, full14 curvature and independent selected Shiab.
 f={}
 met=lambda a,b:int((a,b)==slot or (b,a)==slot)
 k=lambda a:int(a==0)
 for i,j in combinations(range(14),2):
  value={}
  for a,b in combinations(range(14),2):
   z=-Q(1,2)*eta[a]*eta[b]*(k(i)*k(a)*met(j,b)-k(i)*k(b)*met(j,a)-k(j)*k(a)*met(i,b)+k(j)*k(b)*met(i,a))
   if z:value=c.eadd(value,c.escale(z,c.blade((a,b))))
  if value:f[(1<<i)|(1<<j)]=value
 return c.shiab(f)
A=curvature((1,1));V=c.hodge(A);expected={1<<i:c.blade(i) for i in range(2,14)}
check('ambient_curvature_all14',V==expected)
LV=Laxis(0,V);LLV=Laxis(0,LV);LLLV=Laxis(0,LLV)
check('first_correction_even_grade2',{m.bit_count() for e in LV.values() for m in e}=={2})
check('second_correction_odd_grades',{m.bit_count() for e in LLV.values() for m in e}<={1,5})
# T=-V*t²/2+LV*t-LLV (kappa=1), K^-1 Ah=V*t²/2.
# Coefficients by t-power; actual differentiation and L application.
T={2:c.fscale(-Q(1,2),V),1:LV,0:c.fscale(-1,LLV)}
res={d:c.fadd(T.get(d,{}),c.fscale(d+1,Laxis(0,T.get(d+1,{}))),c.fscale(Q(1,2),V) if d==2 else {}) for d in range(3)}
check('complete_unsourced_companion',all(not v for v in res.values()))
# All10 horizontal metric source components, via polarizing metric curvature if needed:
J=[-c.pair(V,curvature((i,i)))[0] for i in range(4)]
check('metric_source_with_vertical_trace',J==[0,-12,-11,-11])
# Offdiagonal source zero follows diagonal coefficient V and curvature trace; explicit full h curvature generalization.
source_slots=[(a,b) for a in range(4) for b in range(a,4)]
J10=[-c.pair(V,curvature(slot))[0] for slot in source_slots]
check('all10_metric_source_components',J10==[0,0,0,0,-12,0,0,-11,0,-11])
check('nonzero_source_conserved',J[0]==0 and J[1]!=0)
check('even_correction_necessary',bool(LV))
# Different derivative directions obey actual skew principal coefficient (one representative).
u=form(1,(1,));v=form(1,(0,1));check('Euler_skew',Epair(0,u,v)!=0 and Epair(0,u,v)==-Epair(0,v,u))
assert all(checks.values()),[k for k,vv in checks.items() if not vv]
# Genuine changed operator/input constructions run through baseline residuals.
def residual(poly):
 return {d:c.fadd(poly.get(d,{}),c.fscale(d+1,Laxis(0,poly.get(d+1,{}))),c.fscale(Q(1,2),V) if d==2 else {}) for d in range(3)}
without_even={2:T[2],0:T[0]};wrong_sign={2:T[2],1:c.fscale(-1,T[1]),0:T[0]}
truncated={fm:e for fm,e in V.items() if fm<(1<<4)}
faults={
 'delete_even_correction':['complete_unsourced_companion'] if any(residual(without_even).values()) else [],
 'wrong_neumann_sign':['complete_unsourced_companion'] if any(residual(wrong_sign).values()) else [],
 'drop_vertical_curvature':['metric_source_with_vertical_trace'] if [-c.pair(truncated,curvature((i,i)))[0] for i in range(4)]!=J else [],
 'delete_hook_projection':['full_firstjet_hook_rank'] if Et[[i for i,(mu,a,b) in enumerate(receivers) if mu in (a,b)],:].rank()!=20 else [],
 'wrong_hook_sign':['all440_grade5_columns_alternating'] if any(Q(z[3][0])+Q(z[3][1])!=0 for z in columns if z[0]==[0,1,2]) else []}
assert all(faults.values()),faults
stem='k2298-enlarged-native-companion';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),'lab/process/k2297-symmetric-shiab-companion.json','tests/channel-swings/k77_exact_bank_api.py','tests/fixtures/k77_exact_coefficient_bank_v1.json','lab/process/selected-k132-native-i1b-t0-all-grade-noether-complex.json']
def serial(f):return [[fm,m,str(z[0]),str(z[1])] for fm,e in sorted(f.items()) for m,z in sorted(e.items())]
data=dict(schema_version='1.0',result_id='K2298',checks=len(checks),check_names=list(checks),mutation_failed_checks=faults,evidence_kind='exact sparse Clifford and rational firstjet identities; universal label/analytic proof in note',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},grade5_columns=columns,projector_rows=selectors,polynomial_coefficients={str(d):serial(f) for d,f in T.items()},metric_source=[str(v) for v in J],metric_source_all10=[str(v) for v in J10],claim_ceiling='flat selected T0 germ; odd-only obstruction and full polynomial sourced-metric escape, no physical matter/domain')
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result='K2298',checks=len(checks),faults=len(faults))))
