"""Full metric coefficient audit; no source ownership or PDE stability claim."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from functools import lru_cache
import ast,json,hashlib,sys
import sympy as sp
from k77_exact_bank_api import K77Core,load_bank,gadd,gmul,gscale
ROOT=Path(__file__).resolve().parents[2];bank=load_bank();c=K77Core(bank.signature,bank.channels);eta=c.eta;checks={}
def check(n,v):
 checks[n]=bool(v)
 if not v:raise AssertionError('[FAIL] '+n)
source='tests/channel-swings/k2298_enlarged_native_companion_probe.py'
tree=ast.parse((ROOT/source).read_text());exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in {'form','Epair','Laxis'}],type_ignores=[]),source,'exec'))
@lru_cache(None)
def unitL(fm,J):return Laxis(0,{fm:{J:(Q(1),Q(0))}})
def L(f):
 out={}
 for fm,e in f.items():
  for J,z in e.items():out=c.fadd(out,c.fscale(z[0],unitL(fm,J)))
 return out
src2='tests/channel-swings/k2307_spatial_coupled_native_mode_probe.py'
tree=ast.parse((ROOT/src2).read_text());exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in {'curvature','metslot'}],type_ignores=[]),src2,'exec'))
def neg(z):return (-z[0],-z[1])
def es(z,e):return {m:gmul(z,v) for m,v in e.items() if gmul(z,v)!=(0,0)}
q=[(Q(int(i==0)),Q(0)) for i in range(14)]
def field(M,even=False):
 out={}
 for (i,j),z in M.items():out=c.fadd(out,c.fscale(z,form(i,(0,j) if even else (j,))))
 return out
def trace(M):return sum(M.get((i,i),0) for i in range(1,14))
def linear(M,a,b):
 out={ij:a*z for ij,z in M.items()};tr=trace(M)
 for i in range(1,14):out[i,i]=out.get((i,i),0)+b*tr
 return {ij:z for ij,z in out.items() if z}
def metric(M):
 h=[[(Q(0),Q(0)) for j in range(14)] for i in range(14)]
 for (i,j),z in M.items():h[i][j]=(Q(eta[j]*z),Q(0))
 return h
basis=[]
for i in range(1,14):basis.append((str(i),{(i,i):Q(1)},Q(1)))
for i,j in combinations(range(1,14),2):basis.append((f'{i}_{j}',{(i,j):Q(1),(j,i):Q(eta[i]*eta[j])},Q(2*eta[i]*eta[j])))
for name,M,g in basis:
 W=field(M);U=field(M,True);BM=linear(M,-2,1)
 check('odd_closure_'+name,L(W)==field(BM,True))
 check('even_closure_'+name,L(U)==field(BM))
 check('curvature_'+name,c.hodge(curvature(q,metric(M)))==field(linear(M,1,-1)))
 check('Gram_'+name,c.pair(W,c.hodge(W))==(g,0) and c.pair(U,c.hodge(U))==(-g,0))
# Distinct matrix slots have disjoint form/Clifford coordinates, including odd/even.
supports=[{(fm,J) for fm,e in field(M,ev).items() for J in e} for _,M,_ in basis for ev in [False,True]]
check('Gram_cross_zero',all(not (a&b) for i,a in enumerate(supports) for b in supports[i+1:]))
for i in range(14):check('longitudinal_'+str(i),not curvature(q,metslot(0,i)))
# Universal trace/traceless coupled blocks; actual basis checks above identify R and B.
k,z=sp.symbols('k z',nonzero=True);h,o,e=sp.symbols('h o e')
blocks={}
for label,r,b in [('trace',-12,11),('tracefree',1,-2)]:
 mat=sp.Matrix([[0,z*z*r,0],[z*z*r,k,z*b],[0,z*b,k]])
 det=sp.factor(mat.det());check('det_'+label,det==-k*z**4*r*r)
 for pole in [4,121]:check('resonance_'+label+'_'+str(pole),det.subs(z*z,k*k/pole)!=0)
 blocks[label]={'R':r,'B':b,'det':str(det)}
j,fo,fe=sp.symbols('j fo fe')
for label,rr,bb in [('trace',-12,11),('tracefree',1,-2)]:
 oo=j/(z*z*rr);ee=(fe-z*bb*oo)/k;hh=(fo-k*oo-z*bb*ee)/(z*z*rr)
 mat=sp.Matrix([[0,z*z*rr,0],[z*z*rr,k,z*bb],[0,z*bb,k]])
 check('forced_response_'+label,sp.simplify(mat*sp.Matrix([hh,oo,ee])-sp.Matrix([j,fo,fe]))==sp.zeros(3,1))
# The R inverse M=Y-tr(Y)I/12 proves surjectivity for arbitrary dimension13 matrices.
for name,M,g in basis:check('R_inverse_'+name,linear(linear(M,1,-1),1,-Q(1,12))==M)
# Actual corrupted signed basis/curvature/coefficient inputs through the same evaluators.
i,j=1,4;good={(i,j):Q(1),(j,i):Q(eta[i]*eta[j])};bad={(i,j):Q(1),(j,i):Q(1)}
mutants={
 'wrong_mixed_signature':c.hodge(curvature(q,metric(good)))!=field(linear(bad,1,-1)),
 'delete_trace_coupling':c.hodge(curvature(q,metric({(1,1):Q(1)})))!=field({(1,1):Q(1)}),
 'omit_even_partner':L(field({(1,1):Q(1)}))!={},
 'flip_L_sign':L(field(good))!=c.fscale(-1,field(linear(good,-2,1),True)),
 'zero_kappa':sp.Matrix([[0,z*z,0],[z*z,0,-2*z],[0,-2*z,0]]).det()==0,
 'zero_covector':not curvature([(Q(0),Q(0))]*14,metric({(1,1):Q(1)}))}
check('all_faults_detected',all(mutants.values()))
hypothesis_controls={k:mutants.pop(k) for k in ['zero_kappa','zero_covector']}
failure_names=dict(wrong_mixed_signature='curvature_1_4',delete_trace_coupling='curvature_1',omit_even_partner='odd_closure_1',flip_L_sign='odd_closure_1_4')
stem='k2313-full-metric-variation-boundary';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),source,src2,'tests/channel-swings/k77_exact_bank_api.py','tests/fixtures/k77_exact_coefficient_bank_v1.json']
data=dict(schema_version='1.0',result_id='K2313',checks=len(checks),check_names=list(checks),mutation_failed_checks={n:[failure_names[n]] for n,v in mutants.items() if v},hypothesis_degeneracy_controls=hypothesis_controls,evidence_kind='exact native full91 signed-basis identities and coupled determinant; universal reducing-complement/covariance argument in note',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details={'transverse_metric_dimension':91,'longitudinal_dimension':14,'reducing_distortion_dimension':182,'blocks':blocks})
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result='K2313',checks=len(checks),faults=len(mutants))))
