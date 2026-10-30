from pathlib import Path
import json,hashlib,sys,math
import sympy as s
ROOT=Path(__file__).resolve().parents[2];checks={}
def check(n,v): checks[n]=bool(v)
def zero(v): return s.simplify(v)==0
x,A,alpha,v,w,n=s.symbols('x A alpha v w n',positive=True)
vs=-w;ws=-(1+n/2)*w-n*v;Js=vs+ws/2
check('J_derivative',zero(Js+(s.Rational(3,2)+n/4)*w+n*v/2))
F=alpha-A*v;dotF=-A*w
check('conformal_factor',zero(1+dotF/(2*F)-(alpha-A*(v+w/2))/F))
p=(5+s.sqrt(73))/4
check('dust_exponent',zero(2*p*p-5*p-6));check('dust_exact_interval',bool(p>3) and bool(p<4))
amp=s.Rational(2,5);check('crossing_amplitude',bool(amp*(1+p/2)>1));check('positive_mass_allx',bool(1-amp*(1+p/3)>0))
zstar=1/(amp*(1+p/2));check('crossing_F',zero(1-amp*zstar-p/(p+2)))
check('unique_crossing_domain',bool(zstar>0) and bool(zstar<1))
# Exact dust derivative of HE through conformal map compared with healthy-dust Raychaudhuri.
# Normalize alpha=M=Fref=C=1 and use z=x^-p as an independent monomial.
z=s.symbols('z',positive=True);F=1-amp*z;dF=amp*p*z/x;H=x**s.Rational(3,2);HE=H*(1-x*dF/(2*F))/s.sqrt(F)
dx=lambda f:s.diff(f,x)-p*z*s.diff(f,z)/x
lhs=-H*x*dx(HE)/s.sqrt(F)
phidot=-s.sqrt(s.Rational(3,2))*H*x*dF/F**s.Rational(3,2);rho=3*x**3/F**2
check('dust_Raychaudhuri',zero(lhs+(phidot**2+rho)/2))
c,eps,X,Xb,O=s.symbols('c eps X Xb O',positive=True)
P=c*X**2+eps*(X-Xb)**2;added=eps*(X-Xb)**2
check('same_background_value',added.subs(X,Xb)==0);check('same_background_Xderivative',s.diff(added,X).subs(X,Xb)==0);check('same_background_chiderivative',s.diff(added,Xb).subs(X,Xb)==0)
K=(s.diff(P,X)+2*X*s.diff(P,X,2)).subs(X,Xb);G=s.diff(P,X).subs(X,Xb)
check('matter_kinetic',zero(K-(6*c+4*eps)*Xb));check('matter_gradient',zero(G-2*c*Xb));check('healthy_radiation_speed',zero((G/K).subs(eps,0)-s.Rational(1,3)))
check('unhealthy_same_background',K.subs(eps,-2*c)==-2*c*Xb and zero((G/K).subs(eps,-2*c)+1))
check('radiation_conformal_cancellation',zero(O**-2*c*(O*X)**2-c*X**2))
check('radiation_stress',zero(2*X*s.diff(c*X**2,X)-c*X**2-3*c*X**2))
assert all(checks.values()),checks
faults={'wrong_conformal_sign':['conformal_factor'] if not zero(1-dotF/(2*(alpha-A*v))-(alpha-A*(v+w/2))/(alpha-A*v)) else [],'wrong_flow_damping':['J_derivative'] if not zero((-w+(-(2+n/2)*w-n*v)/2)-Js) else [],'omit_matter_Hessian':['matter_kinetic'] if not zero(G-K) else [],'wrong_measure_power':['radiation_conformal_cancellation'] if not zero(O**-1*c*(O*X)**2-c*X**2) else []}
result='K2302';note='explorations/conditional-build/k2302-designer-frame-turnaround-2026-10-30.md';report='k2302-designer-frame-turnaround.json';extra_deps=['explorations/conditional-build/k2299-finite-curvature-designer-family-2026-10-30.md','explorations/conditional-build/k2291-rolling-scalar-applicability-2026-10-30.md'];evidence='Exact symbolic conformal/flow/matter identities; universal monotonicity proof in note';details={'p':str(p),'amplitude':'2/5','crossing_F_over_alpha':str(p/(p+2)),'kinetic':str(K),'gradient':str(G)}

assert all(checks.values()),[k for k,v in checks.items() if not v]
assert all(faults.values()),faults
deps=[str(Path(__file__).relative_to(ROOT)),note]+extra_deps
data=dict(schema_version='1.0',result_id=result,checks=len(checks),check_names=list(checks),mutation_failed_checks=faults,evidence_kind=evidence,dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details=details)
out=ROOT/'lab/process'/report
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result=result,checks=len(checks),faults=len(faults))))
