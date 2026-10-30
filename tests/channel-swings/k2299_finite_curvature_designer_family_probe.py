from pathlib import Path
import sympy as s
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2];checks={}
def check(n,v):checks[n]=bool(v)
def z(a):return s.simplify(s.expand(a))==0
x=s.symbols('x',positive=True);M,N,L,alpha,A=s.symbols('M N L alpha A',positive=True)
E=M*x**3+N*x**4+L;p=x*x*s.sqrt(E);q0=x*s.diff(E,x)/s.sqrt(E)
g=s.Function('g')(x);u=s.Function('u')(x);I=s.Function('I')(x)
Lf=lambda f:x*x*E*s.diff(f,x,2)+x*(2*E+x*s.diff(E,x)/2)*s.diff(f,x)-x*s.diff(E,x)*f
check('self_adjoint_equation',z((s.diff(p*s.diff(u,x),x)-q0*u)*s.sqrt(E)-Lf(u)))
gpp=s.solve(Lf(g),s.diff(g,x,2))[0];Ip=-1/(p*g*g);Ipp=s.diff(Ip,x)
res=Lf(g*I).subs({s.diff(I,x,2):Ipp,s.diff(I,x):Ip}).subs(s.diff(g,x,2),gpp)
check('reduction_of_order',z(res));check('Wronskian',z((g*s.diff(g*I,x)-(g*I)*s.diff(g,x)).subs(s.diff(I,x),Ip)+1/p))
R=12*E-3*x*s.diff(E,x);q=3*alpha*(M*x**3+N*x**4);P=alpha*N*x**4;F=s.Function('F')(x)
f=R*F-6*E*F+2*q+6*E*x*s.diff(F,x)
full=Lf(F)+q+P
check('reconstruction_integrability',z(s.diff(f,x)-F*s.diff(R,x)-6*full/x))
check('curvature_monotonic',z(s.diff(R,x)-9*M*x*x));check('source_conservation',z(s.diff(q,x)-3*(q+P)/x));check('constant_particular',z(Lf(alpha)+q+P))
r=(-5-s.sqrt(73))/4;rp=(-5+s.sqrt(73))/4
check('dust_indicial',z(2*r*r+5*r-6));check('dust_decreasing',r<0 and rp>0)
Fd=alpha-A*x**r;Rd=3*M*x**3;fd=alpha*Rd+A*M*(3-6*r)*x**(r+3)
check('dust_action_derivative',z(s.diff(fd,x)-Fd*s.diff(Rd,x)));check('dust_equation',z((Lf(Fd)+q+P).subs({N:0,L:0})))
frr=s.diff(Fd,x)/s.diff(Rd,x)
check('dust_mass_numerator',z(Fd-Rd*frr-(alpha-A*(1-r/3)*x**r)))
check('mass_countercontrol',bool((Fd-Rd*frr).subs({x:1,alpha:1,A:s.Rational(3,4)})<0))
check('healthy_mass_control',bool((Fd-Rd*frr).subs({x:1,alpha:1,A:s.Rational(1,4)})>0))
check('endpoint_failure',Fd.subs({x:1,A:alpha})==0)
check('negative_amplitude_wrong_sign',bool(frr.subs({x:1,M:1,A:-1})<0))
# Universal s derivative identity using independent jet variables.
v,w,n=s.symbols('v w n',positive=True)
vv=s.Function('v')(x);ww=s.symbols('ww');n_expr=x*s.diff(E,x)/E
vpp=s.solve(Lf(vv),s.diff(vv,x,2))[0]
check('log_coordinate_w_equation',z((-x*s.diff(vv,x)-x*x*vpp).subs(s.diff(vv,x),-ww/x)+(1+n_expr/2)*ww+n_expr*vv))
check('general_mass_identity',z(R*(-A*s.diff(vv,x)/(9*M*x*x))-A*(s.Rational(1,3)+4*L/(3*M*x**3))*(-x*s.diff(vv,x))))
check('w_monotone',s.ask(s.Q.negative(-(1+n/2)*w-n*v)))
check('limit_integral_majorant',z(s.integrate(x**s.Rational(-7,2),(x,x,s.oo))-s.Rational(2,5)*x**s.Rational(-5,2)))
# Run clean baseline before any changed algebra/reference.
assert all(checks.values()),[k for k,vv in checks.items() if not vv]
faults={
 'wrong_sturm_sign':['self_adjoint_equation'] if not z((s.diff(p*s.diff(u,x),x)+q0*u)*s.sqrt(E)-Lf(u)) else [],
 'wrong_reconstruction_derivative_sign':['reconstruction_integrability'] if not z(s.diff(f-12*E*x*s.diff(F,x),x)-F*s.diff(R,x)-6*full/x) else [],
 'wrong_action_coefficient':['dust_action_derivative'] if not z(s.diff(alpha*Rd+A*M*(3+6*r)*x**(r+3),x)-Fd*s.diff(Rd,x)) else [],
}
assert all(faults.values()),faults
stem='k2299-finite-curvature-designer-family';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),'lab/process/k2295-quadratic-expansion-reconstruction.json']
data=dict(schema_version='1.0',result_id='K2299',checks=len(checks),check_names=list(checks),mutation_failed_checks=faults,evidence_kind='exact symbolic identities and algebraic sign controls; continuum proof in note; hashes provenance',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},dust_exponents=[str(r),str(rp)],claim_ceiling='supplied metric homogeneous family; algebraic mass is not rolling physical mass')
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result='K2299',checks=len(checks),faults=len(faults))))
