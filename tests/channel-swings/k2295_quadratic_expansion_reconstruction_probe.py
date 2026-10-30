from pathlib import Path
import json,hashlib,sys
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
checks={}
def check(n,v):checks[n]=bool(v)
def zero(v):return s.cancel(s.expand(v))==0
x=s.symbols('x',positive=True);a,b,rho,M,N,L,d,r=s.symbols('a b rho M N L d r',real=True)
E=M*x**3+N*x**4+L;R=12*E-3*x*s.diff(E,x);F=a+b*R;f=a*R+b*R**2/2-rho
qreq=s.expand(3*F*E-(F*R-f)/2-3*E*x*s.diff(F,x))
expected=3*a*M*x**3+3*N*(a+12*b*L)*x**4-s.Rational(81,4)*b*M*M*x**6-18*b*M*N*x**7+3*a*L-rho/2
check('full00_polynomial',zero(qreq-expected));check('curvature_radiation_cancellation',zero(R-3*M*x**3-12*L))
p=s.Poly(qreq-d*x**3-r*x**4,x)
check('sixth_coefficient_obstruction',p.nth(6)==-s.Rational(81,4)*b*M**2)
check('seventh_coefficient',p.nth(7)==-18*b*M*N)
check('exact_coefficient_support',set(k[0] for k,v in p.terms())=={0,3,4,6,7})
check('radiation_countercontrol',zero((qreq-r*x**4).subs({M:0,r:3*N*(a+12*b*L),rho:6*a*L})))
check('einstein_countercontrol',zero((qreq-d*x**3-r*x**4).subs({b:0,d:3*a*M,r:3*a*N,rho:6*a*L})))
for n,w in [(3,0),(4,s.Rational(1,3)),(6,1),(7,s.Rational(4,3))]:check('fluid_power_'+str(n),n==3*(1+w))
# Arbitrary functions, not just the polynomial special case.
e=s.Function('E')(x);ff=s.Function('F')(x);fun=s.Function('f')(x);q=s.Function('q')(x);P=s.Function('P')(x)
rr=12*e-3*x*s.diff(e,x)
def equations(drift=1,pressure=1,trace_pressure=3):
 LF=x*x*e*s.diff(ff,x,2)+x*(2*e+x*s.diff(e,x)/2)*s.diff(ff,x)-x*s.diff(e,x)*ff+q+pressure*P
 C=3*ff*e-(ff*rr-fun)/2-q-drift*3*e*x*s.diff(ff,x)
 Box=-e*x*x*s.diff(ff,x,2)+x*(2*e-x*s.diff(e,x)/2)*s.diff(ff,x)
 S=ff*(3*e-x*s.diff(e,x)/2)-fun/2-e*x*x*s.diff(ff,x,2)+x*(e-x*s.diff(e,x)/2)*s.diff(ff,x)-P
 T=ff*rr-2*fun+3*Box+q-trace_pressure*P
 frec=rr*ff-6*e*ff+2*q+6*e*x*s.diff(ff,x)
 return dict(spatial=zero(S+LF+C),trace=zero(T+4*C+3*LF),integrability=zero(s.diff(frec,x)-ff*s.diff(rr,x)-6*LF/x-2*(s.diff(q,x)-3*(q+P)/x)),reconstruction00=zero(C.subs(fun,frec)))
for n,v in equations().items():check(n,v)
u=s.Function('u')(x);eps=s.symbols('eps',positive=True);Fd=a+eps*u;qd=3*a*(M*x**3+N*x**4);Pd=a*N*x**4
Lu=x*x*E*s.diff(u,x,2)+x*(2*E+x*s.diff(E,x)/2)*s.diff(u,x)-x*s.diff(E,x)*u
Lfd=x*x*E*s.diff(Fd,x,2)+x*(2*E+x*s.diff(E,x)/2)*s.diff(Fd,x)-x*s.diff(E,x)*Fd+qd+Pd
check('designer_homogeneous_reduction',zero(Lfd-eps*Lu));check('matter_conservation',zero(s.diff(qd,x)-3*(qd+Pd)/x));check('curvature_invertibility',zero(s.diff(R,x)-9*M*x*x))
check('positive_quadrant_boundary',zero(s.solve(Lu,s.diff(u,x,2))[0].subs(s.diff(u,x),0)-s.diff(E,x)*u/(x*E)))
nn=s.symbols('n',real=True);y=s.symbols('y',positive=True);tau=s.symbols('tau',nonnegative=True)
check('logtime_ODE',zero(x*x*s.diff(u,x,2)+x*(2+nn/2)*s.diff(u,x)-nn*u-(x*x*s.diff(u,x,2)+x*s.diff(u,x)+(1+nn/2)*x*s.diff(u,x)-nn*u)))
check('n_lower_identity',zero(2*x*s.diff(E,x)-3*E-3*(M*x**3-L)-5*N*x**4))
check('n_upper_identity',zero(4*E-x*s.diff(E,x)-M*x**3-4*L))
z=(1-s.exp(-3*tau))/2
check('comparison_solution',zero(s.diff(z,tau)+3*z-s.Rational(3,2)))
bound=tau/2-(1-s.exp(-3*tau))/6
check('integrated_log_lower',zero(s.diff(bound,tau)-z))
faults={}
for name,kw in [('wrong00_derivative_sign',dict(drift=-1)),('omit_pressure',dict(pressure=0)),('wrong_trace_pressure',dict(trace_pressure=-3))]:faults[name]=[k for k,v in equations(**kw).items() if not v]
for name,expr in [('omit_stiff',expected+s.Rational(81,4)*b*M*M*x**6),('omit_mixed_radiation',expected+18*b*M*N*x**7),('vacuum_source_transplant',s.Integer(0))]:faults[name]=['full00_polynomial'] if not zero(qreq-expr) else []
# Incorrectly asserting positive curvature alone suffices must fail the actual00.
check('positiveF_does_not_rescue00',qreq.subs({a:1,b:1,M:1,N:0,L:1,rho:6,x:1})!=3)
assert all(checks.values()),checks
assert all(faults.values()),faults
stem='k2295-quadratic-expansion-reconstruction'
deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),'lab/process/k2292-conserved-matter-cosmology.json','lab/process/k2265-shared-cosmology-consistency.json']
data=dict(schema_version='1.0',result_id='K2295',checks=len(checks),check_names=list(checks),mutation_failed_checks=faults,evidence_kind='exact symbolic identities; analytic positivity and ODE existence proof in companion; hashes are provenance',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},claim_ceiling='exact supplied metric backgrounds only; no approximate-fit exclusion or GU verdict')
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result='K2295',checks=len(checks),faults=len(faults))))
