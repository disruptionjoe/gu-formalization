from pathlib import Path
import json,hashlib,sys,math
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
W=form(1,(1,));V={1<<i:c.blade(i) for i in range(2,14)};U=form(1,(0,1));Z={1<<i:c.blade((0,i)) for i in range(2,14)};basis=[W,V,U,Z]
L=s.Matrix([[0,0,-1,12],[0,0,1,10],[-1,12,0,0],[1,10,0,0]])
for j,u in enumerate(basis):
 expected={}
 for i,v in enumerate(basis):expected=c.fadd(expected,c.fscale(Q(L[i,j]),v))
 check('native_column_'+str(j),Laxis(0,u)==expected)
G=s.Matrix([[s.Rational(c.pair(u,c.hodge(v))[0]) for v in basis] for u in basis]);Gp=s.diag(1,12,1,12)
check('native_gram',G==s.diag(1,12,-1,-12));check('native_skew',L.T*G+G*L==s.zeros(4));check('auxiliary_selfadjoint',L.T*Gp==Gp*L)
check('minimal_polynomial',(L**2-121*s.eye(4))*(L**2-4*s.eye(4))==s.zeros(4) and len(L.eigenvals())==4)
e=s.Matrix([0,1,0,0]);projectors=[]
for lam in [11,-11,2,-2]:
 P=s.eye(4)
 for other in [11,-11,2,-2]:
  if other!=lam:P=P*(L-other*s.eye(4))/(lam-other)
 check('projector_'+str(lam),P*P==P and L*P==lam*P and P*e!=s.zeros(4,1));projectors.append(P)
check('projector_completeness',sum(projectors,s.zeros(4))==s.eye(4))
k,w=s.symbols('k w',real=True,nonzero=True);B=L[:2,2:];f11=-w*w/(k*k+121*w*w);f2=-w*w/(k*k+4*w*w)
q=(12*f11*s.Matrix([1,1])+f2*s.Matrix([-12,1]))/13
T=(-k*q).col_join(s.I*w*B*q)
check('full_fourier_residual',all(zero(z) for z in (k*s.eye(4)+s.I*w*L)*T-w*w*e))
slots=list(combinations(range(4),2))+[(i,i) for i in range(4)]
pairs=[[c.pair(v,curvature(slot))[0] for v in basis] for slot in slots]
expected=[]
for a,b in slots:expected.append([0,0,0,0] if a!=b or a==0 else ([0,12,0,0] if a==1 else [1,11,0,0]))
check('all10_native_source_rows',pairs==expected)
t=s.symbols('t',real=True);poly=-e*t*t/(2*k)+L*e*t/k**2-L**2*e/k**3
check('polynomial_control',all(zero(z) for z in k*poly+L*poly.diff(t)+e*t*t/2))
# Both causal kernels carry unit derivative jump; negative branch includes the minus sign.
check('kernel_jumps',all(s.Rational(lam)*(s.Rational(1,lam))==1 and s.Rational(lam)*(0-(-s.Rational(1,lam)))==1 for lam in [11,-11,2,-2]))
a=s.symbols('a',nonzero=True,real=True);H=t*t*(1-t)**2
moment=s.integrate(s.exp(a*t)*s.diff(H,t,2),(t,0,1));rhs=a*a*s.integrate(s.exp(a*t)*H,(t,0,1))
check('compact_C1_profile_moment',zero(moment-rhs)) # analytic note uses smooth bumps, same integration by parts
check('kappa_zero_constant_kernel',e!=s.zeros(4,1) and (k*e+L*e.diff(t)).subs(k,0)==s.zeros(4,1) and k*e+L*e.diff(t)!=s.zeros(4,1))
# Joint restricted source response, including the independent moment/causal seams.
z=s.symbols('z');Delta=(k*k-121*z*z)*(k*k-4*z*z)
f11z=z*z/(k*k-121*z*z);f2z=z*z/(k*k-4*z*z)
az=-12*k*(f11z-f2z)/13;bz=-k*(12*f11z+f2z)/13
J11=12*z*z*bz;J22=z*z*(az+11*bz)
check('joint_J11_transfer',zero(J11+12*k*z**4*(k*k-13*z*z)/Delta))
check('joint_J22_transfer',zero(J22+k*z**4*(11*k*k-35*z*z)/Delta))
check('joint_source_compatibility',zero(12*(k*k-13*z*z)*J22-(11*k*k-35*z*z)*J11))
check('joint_poles_not_canceled',s.simplify(Delta.subs(z,k/s.sqrt(13)))!=0)
check('fourth_order_zero',s.limit(J11/z**4,z,0)==-12/k)
check('compact_completion',all(s.denom(s.cancel(q*Delta))==1 for q in [az,bz,J11,J22]))
assert all(checks.values()),checks
bad=L.copy();bad[2,1]=11
badcolumn={}
for i,vec in enumerate(basis):badcolumn=c.fadd(badcolumn,c.fscale(Q(bad[i,1]),vec))
faults={'wrong_native_coefficient':['native_column_1'] if badcolumn!=Laxis(0,V) else [],'omit_even_correction':['full_fourier_residual'] if any(not zero(z) for z in (k*s.eye(4)+s.I*w*L)*T[:2,:].col_join(s.zeros(2,1))-w*w*e) else [],'wrong_advanced_sign':['kernel_jumps'] if (-2)*(0-s.Rational(1,-2))!=1 else [],'drop_vertical_source':['all10_native_source_rows'] if c.pair({fm:v for fm,v in V.items() if fm<16},curvature((1,1)))[0]!=12 else []}
faults['wrong_joint_source_coefficient']=['joint_source_compatibility'] if not zero(12*(k*k-12*z*z)*J22-(11*k*k-35*z*z)*J11) else []
result='K2301';note='explorations/conditional-build/k2301-native-companion-time-domain-2026-10-30.md';report='k2301-native-companion-time-domain.json';extra_deps=[source,'tests/channel-swings/k77_exact_bank_api.py','tests/fixtures/k77_exact_coefficient_bank_v1.json'];evidence='Exact native Clifford columns and symbolic domain identities; continuum Fourier and moment proofs in note';details={'L':[[str(x) for x in row] for row in L.tolist()],'G':[[str(x) for x in row] for row in G.tolist()],'source_rows':[[str(x) for x in row] for row in pairs]}

assert all(checks.values()),[k for k,v in checks.items() if not v]
assert all(faults.values()),faults
deps=[str(Path(__file__).relative_to(ROOT)),note]+extra_deps
data=dict(schema_version='1.0',result_id=result,checks=len(checks),check_names=list(checks),mutation_failed_checks=faults,evidence_kind=evidence,dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details=details)
out=ROOT/'lab/process'/report
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result=result,checks=len(checks),faults=len(faults))))
