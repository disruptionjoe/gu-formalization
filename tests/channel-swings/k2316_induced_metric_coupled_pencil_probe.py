"""Induced ten-direction coefficient pencil; native sparse verification, no source dynamics claim."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
import sympy as sp
import ast,json,hashlib,sys
from k77_exact_bank_api import K77Core,load_bank,gadd,gmul,gscale
ROOT=Path(__file__).resolve().parents[2];checks={}
def check(n,v):
 checks[n]=bool(v)
 if not v:raise AssertionError('[FAIL] '+n)
def funcs(path,names):
 tree=ast.parse((ROOT/path).read_text());exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names],type_ignores=[]),path,'exec'),globals())
geom='tests/channel-swings/selected_k77_full_normal_owner_bank_probe.py'
# Existing functions use Q=SymPy Rational; retain it while constructing geometric data.
Qsave=Q;Q=sp.Rational
funcs(geom,{'sym2_basis','dewitt','d_dewitt'});slots,bs=sym2_basis();g=sp.diag(1,-1,-1,-1);gv=dewitt(g,bs);Ps=[sp.diag(h,d_dewitt(g,h,bs)) for h in bs];Q=Qsave
G=sp.diag(g,gv);ep=sp.symbols('ep')
for a in [0,1,4,5,9]:
 Q=sp.Rational;direct=dewitt((g+ep*bs[a]).inv(),bs).diff(ep).subs(ep,0);Q=Qsave
 check('metric_derivative_'+str(a),direct==Ps[a][4:,4:])
# Rational congruence from fibre-coordinate DeWitt metric to native diagonal K77.
def vec(entries):return sp.Matrix([entries.get(i,0) for i in range(10)])
di=[0,4,7,9];v=[1,-1,-1,-1];had=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]
dvec=[vec({di[i]:sp.Rational(v[i]*col[i],2) for i in range(4)}) for col in had]
p1,p2,p3=5,6,8;n1,n2,n3=1,2,3
vp=[vec({p1:sp.Rational(1,2),p2:sp.Rational(sign,2)}) for sign in [1,-1]]+[vec({p3:sp.Rational(3,4),n3:sp.Rational(1,4)})]
vn=[vec({n1:sp.Rational(1,2),n2:sp.Rational(sign,2)}) for sign in [1,-1]]+[vec({p3:sp.Rational(1,4),n3:sp.Rational(3,4)})]
S=sp.Matrix.hstack(*(dvec[1:]+vp+[dvec[0]]+vn));check('rational_fibre_congruence',S.T*gv*S==sp.diag(*([1]*6+[-1]*4)))
T=sp.diag(sp.eye(4),S);bank=load_bank();c=K77Core(bank.signature,bank.channels);eta=c.eta;E=sp.diag(*eta);check('native_signature',T.T*G*T==E)
Hs=[T.T*p*T for p in Ps];Et=sp.diag(*eta[1:]);Ms=[h[1:,1:]*Et for h in Hs]
C=sp.Matrix(10,10,lambda i,j:sp.trace(Ms[i]*Ms[j]));t=sp.Matrix([sp.trace(m) for m in Ms]);Ci=C.inv();u=Ci*t;tau=(t.T*u)[0]
check('rank10',C.rank()==10);check('trace_vector',t==sp.Matrix([-5,0,0,0,4,0,0,4,0,4]));check('tau',tau==sp.Rational(643,91));check('kernel_direction',u==sp.Matrix([-59,0,0,0,29,0,0,29,0,29])/91)
M=sum((u[a]*Ms[a] for a in range(10)),sp.zeros(13));I=sp.eye(13)
def R(m):return m-sp.trace(m)*I
def B(m):return sp.trace(m)*I-2*m
k,s=sp.symbols('k s',nonzero=True);alpha=-k*s*s/(k*k-4*s);b=(11*k*k-35*s)/(k*k-121*s)
check('secular_root',sp.simplify(1+b*tau-sp.Rational(36,91)*(199*k*k-931*s)/(k*k-121*s))==0)
s0=sp.Rational(199,931);check('nonresonance',1-4*s0!=0 and 1-121*s0!=0)
o=-s0*((M-sp.trace(M)*I/13)/(1-4*s0)-12*sp.trace(M)*I/(13*(1-121*s0)));ebar=-B(o)
check('matrix_odd_companion',o+s0*B(ebar)+s0*R(M)==sp.zeros(13));check('matrix_even_companion',ebar+B(o)==sp.zeros(13))
for a in range(10):check('matrix_metric_'+str(a),sp.trace(R(Ms[a])*o)==0)
check('nonzero_curvature_matrix',R(M)!=sp.zeros(13));check('simple_kernel',(C+b.subs({k:1,s:s0})*t*t.T).rank()==9)
# Generic exact inverse via rank-one coefficients, rather than expensive symbolic inversion.
x=sp.symbols('x');inv=Ci-x*(u*u.T)/(1+x*tau)
check('source_inverse',sp.simplify((C+x*t*t.T)*inv-sp.eye(10))==sp.zeros(10))
check('root_compatible_source',sp.simplify((C-t*t.T/tau)*u)==sp.zeros(10,1))
check('no_pure_transverse_trace',tau!=13)
# At the two poles: no scalar image and nondegenerate tracefree restriction.
check('tracefree_restriction_nondegenerate',tau!=0 and C.det()!=0)
# Independent native curvature and first-order operator evaluations.
funcs('tests/channel-swings/k2298_enlarged_native_companion_probe.py',{'form','Epair','Laxis'})
funcs('tests/channel-swings/k2307_spatial_coupled_native_mode_probe.py',{'curvature','metslot'})
def neg(z):return (-z[0],-z[1])
def es(z,e):return {m:gmul(z,v) for m,v in e.items() if gmul(z,v)!=(0,0)}
@lru_cache(None)
def unitL(fm,J):return Laxis(0,{fm:{J:(Q(1),Q(0))}})
def L(f):
 out={}
 for fm,e in f.items():
  for J,z in e.items():out=c.fadd(out,c.fscale(z[0],unitL(fm,J)))
 return out
def field(mat,ev=False):
 out={}
 for i in range(13):
  for j in range(13):
   if mat[i,j]:out=c.fadd(out,c.fscale(Q(mat[i,j]),form(i+1,(0,j+1) if ev else (j+1,))))
 return out
def metric(h):return [[(Q(h[i,j]),Q(0)) for j in range(14)] for i in range(14)]
q=[(Q(int(i==0)),Q(0)) for i in range(14)]
for a in range(10):check('native_curvature_'+str(a),c.hodge(curvature(q,metric(Hs[a])))==field(R(Ms[a])))
fo=field(o);fe=field(ebar,True);fM=field(R(M))
check('native_odd_companion',not c.fadd(c.fadd(fo,c.fscale(Q(s0),L(fe))),c.fscale(Q(s0),fM)))
check('native_even_companion',not c.fadd(fe,L(fo)))
for a in range(10):check('native_metric_'+str(a),c.pair(fo,curvature(q,metric(Hs[a])))==(0,0))
check('native_nonzero_curvature',bool(fM))
# Mixed-order quadratic coordinate congruence: formal adjoint reverses q.
qq=sp.symbols('qq');jj=qq*sp.Matrix([[1,2],[0,1]]);ss=sp.eye(4);ss[2:,:2]=-jj;sinv=sp.eye(4);sinv[2:,:2]=jj
hh=sp.diag(2+qq**2,3+qq**2,5,7);hh[:2,2:]=qq*sp.Matrix([[1,0],[2,1]]);hh[2:,:2]=-hh[:2,2:].T
adj=ss.subs(qq,-qq).T;new=adj*hh*ss
check('coordinate_inverse',ss*sinv==sp.eye(4))
check('coordinate_det_one',ss.det()==1)
check('old_formal_adjoint',hh.subs(qq,-qq).T==hh)
check('new_formal_adjoint',sp.simplify(new.subs(qq,-qq).T-new)==sp.zeros(4))
check('mixed_order_determinant',sp.factor(new.det()-hh.det())==0)
ytest=sp.Matrix([1,2,3,4]);oldsource=hh*ss*ytest
check('source_covector_transport',sp.simplify(new*ytest-adj*oldsource)==sp.zeros(4,1))
wrongadj=ss.T
check('odd_J_transpose_matters',sp.simplify(wrongadj*hh*ss-new)!=sp.zeros(4))

# Genuine corruptions evaluated through the same native row or matrix map.
def metricrows(oo):return [sp.trace(R(mm)*oo) for mm in Ms]
def solve_o(mm,ss):return -ss*((mm-sp.trace(mm)*I/13)/(1-4*ss)-12*sp.trace(mm)*I/(13*(1-121*ss)))
Mh=sum((u[a]*sp.diag(Hs[a][1:4,1:4],sp.zeros(10))*Et for a in range(10)),sp.zeros(13))
wrong_raise=Hs[1][1:,1:] # no index raising
faults={
 'omit_fibre_variation':any(v!=0 for v in metricrows(solve_o(Mh,s0))),
 'reuse_horizontal_root':any(v!=0 for v in metricrows(solve_o(M,sp.Rational(17,113)))),
 'wrong_index_raising':c.hodge(curvature(q,metric(Hs[1])))!=field(R(wrong_raise)),
 'omit_even_companion':bool(c.fadd(fo,c.fscale(Q(s0),fM))),
 'remove_trace_coupling':c.hodge(curvature(q,metric(Hs[0])))!=field(Ms[0]),
 'ordinary_transpose_for_odd_J':sp.simplify(wrongadj*hh*ss-new)!=sp.zeros(4),
 'omit_companion_source_shift':sp.simplify(new*ytest-oldsource)!=sp.zeros(4,1),
 'source_inverse_sign':sp.simplify((C+x*t*t.T)*(Ci+x*u*u.T/(1+x*tau))-sp.eye(10))!=sp.zeros(10)}
assert all(faults.values()),'[FAIL] undetected corrupted input'
stem='k2316-induced-metric-coupled-pencil';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),geom,'tests/channel-swings/k2298_enlarged_native_companion_probe.py','tests/channel-swings/k2307_spatial_coupled_native_mode_probe.py','tests/channel-swings/k77_exact_bank_api.py','tests/fixtures/k77_exact_coefficient_bank_v1.json','explorations/conditional-build/k2313-full-metric-variation-boundary-2026-10-30.md']
data=dict(schema_version='1.0',result_id='K2316',checks=len(checks),check_names=list(checks),mutation_failed_checks={n:['actual_coefficient_or_source_equation'] for n in faults},evidence_kind='exact rational geometry/native sparse operator and symbolic source algebra; universal covariance/domain boundaries written in note',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details={'root_s_over_kappa_squared':str(s0),'tau':str(tau),'C':str(C),'kernel':str(u),'fibre_congruence':str(S)})
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result='K2316',checks=len(checks),faults=len(faults))))
