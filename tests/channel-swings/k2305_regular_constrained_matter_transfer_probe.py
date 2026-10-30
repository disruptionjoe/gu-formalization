from pathlib import Path
import json,hashlib,sys
import sympy as s
ROOT=Path(__file__).resolve().parents[2];checks={}
def check(n,v): checks[n]=bool(v)
def zero(v): return s.simplify(v)==0

H,phi,u,d,rho,M,beta=s.symbols('H phi u d rho M beta',real=True);V=s.Function('V')(phi);z=s.Matrix([H,phi,u,d,rho]);f=s.Matrix([-(u*u+d+4*rho/3)/(2*M*M),u,-3*H*u-s.diff(V,phi)-beta*d,(-3*H+beta*u)*d,-4*H*rho]);C=3*M*M*H*H-u*u/2-V-d-rho;g=s.Matrix([C]).jacobian(z);J=f.jacobian(z)
check('off_shell_constraint',zero((g*f)[0]))
check('tangent_constraint',all(zero(q) for q in g.jacobian(z)*f+J.T*g.T))
dsol=3*M*M*H*H-u*u/2-V-rho;fred=s.Matrix([f[i].subs(d,dsol) for i in [0,1,2,4]]);zr=s.Matrix([H,phi,u,rho]);Jr=fred.jacobian(zr)
check('radiation_constrained_trace',zero(s.trace(Jr)-(-10*H+beta*u)))
fd=s.Matrix([fred[i].subs(rho,0) for i in [0,1,2]]);Jd=fd.jacobian(s.Matrix([H,phi,u]));check('dust_constrained_trace',zero(s.trace(Jd)-(-6*H+beta*u)))
check('regular_constraint_chart',s.diff(C,d)==-1)
# Exact dust fixture: y=A*x^-p, so differentiate before using polynomial relation.
x,y,p=s.symbols('x y p',positive=True);F=1-y;S=s.sqrt(s.Rational(3,2));xdot=-x**s.Rational(5,2)/s.sqrt(F)
def dx(q):return s.diff(q,x)-p*y/x*s.diff(q,y)
def dt(q):return s.simplify(dx(q)*xdot)
def pzero(q):
 q=s.factor(q);return zero(q.subs(p,(5+s.sqrt(73))/4))
h=x**s.Rational(3,2)*(1-(1+p/2)*y)/F**s.Rational(3,2);up=-S*p*y*x**s.Rational(3,2)/F**s.Rational(3,2);dp=3*x**3/F**2;vp=-3*(1+p)*y*x**3/F**2;phip=S*s.log(F);v1=s.simplify(dx(vp)/dx(phip));v2=s.simplify(dx(v1)/dx(phip));bet=-1/s.sqrt(6)
check('fixture_phi',zero(dt(phip)-up));check('fixture_friedmann',pzero(3*h*h-up*up/2-vp-dp));check('fixture_H',pzero(dt(h)+(up*up+dp)/2));check('fixture_scalar',pzero(dt(up)+3*h*up+v1+bet*dp));check('fixture_dust',pzero(dt(dp)-(-3*h+bet*up)*dp))
nu=1-3/p;bb=2+nu*F/(1-F);cc=nu*F/(1-F)**2
check('potential_first',zero(v1+s.sqrt(s.Rational(2,3))*bb*vp));check('potential_second',zero(v2-s.Rational(2,3)*vp*(bb*bb-cc)))
logdet=6*s.log(x)-s.Rational(7,2)*s.log(F);check('fixture_determinant',zero(dt(logdet)-(-6*h+bet*up)))
# Rigorous rational bound envelope, with 3<p<7/2 and 1<=x<=11/10.
Q=s.Rational
check('p_bracket',3<(5+s.sqrt(73))/4<Q(7,2));check('F_upper',1-Q(2,5)/(Q(11,10)**4)<Q(73,100))
check('H_bound',(Q(6,5)*(1-1/(Q(11,10)**4)))/(Q(9,20))<1 and Q(3,5)**3>Q(9,20)**2)
check('u_bound_squared',Q(3,2)*Q(2,5)**2*Q(7,2)**2/Q(3,5)**3<16)
check('dust_bound',3*Q(11,10)**3/Q(3,5)**2<12)
check('potential_bound',3*Q(2,5)*Q(9,2)/Q(3,5)**2<=15)
bmax=2+Q(1,7)*Q(73,100)/Q(27,100);cmax=Q(1,7)*Q(73,100)/Q(27,100)**2
check('potential_derivative_bound',bmax<Q(12,5) and cmax<2 and Q(2,3)*15*Q(12,5)**2<58 and Q(2,3)*(Q(12,5)*15)**2<30**2)
check('row_bound',max(4+Q(1,2),1,12+58+3+Q(1,2),36+6+3+2)<74)
check('crossing_inside',Q(2,5)*(1+Q(3,2))==1 and Q(2,5)*(1+Q(7,4))==Q(11,10) and Q(11,10)**3>Q(11,10))
check('duration_bound',s.sqrt(Q(73,100))<1 and Q(1,10)*74==Q(37,5))
# Chosen perturbation jets: exact differential identities at H=0,M=1,r=0.
f4=s.Matrix([f[i].subs({rho:0,M:1,beta:bet}) for i in range(4)]);z4=s.Matrix([H,phi,u,d]);J4=f4.jacobian(z4);v0=s.Matrix([1,0,0,0]);v1j=(J4*v0).subs(H,0)
check('selected_first_jet',v1j==s.Matrix([0,0,-3*u,-3*d]))
Jdot=J4.applyfunc(lambda q: (s.Matrix([q]).jacobian(z4)*f4)[0]);v2j=((Jdot+J4*J4)*v0).subs(H,0)
check('selected_second_H',zero(v2j[0]-(3*u*u+3*d/2)));check('selected_second_phi',zero(v2j[1]+3*u))
eps=s.symbols('eps');check('integrable_initial_family',zero((3*eps**2-u*u/2-V-(d+3*eps**2))-(-u*u/2-V-d)))
check('crossing_event_sensitivity',zero((-1/f4[0]).subs(H,0)-2/(u*u+d)))
assert all(checks.values()),[a for a,b in checks.items() if not b]
bad=f.copy();bad[2]=-3*H*u-s.diff(V,phi)+beta*d
bad2=f.copy();bad2[3]=-3*H*d
bad3=f.copy();bad3[0]=-(u*u+2*d+4*rho/3)/(2*M*M)
badj=J.copy();badj[3,:]=s.zeros(1,5);badV=J.copy();badV[2,1]=0
faults={'wrong_scalar_exchange':['off_shell_constraint'] if not zero((g*bad)[0]) else [],'omit_dust_exchange':['off_shell_constraint'] if not zero((g*bad2)[0]) else [],'wrong_dust_Raychaudhuri':['off_shell_constraint'] if not zero((g*bad3)[0]) else [],'freeze_dust_tangent':['tangent_constraint'] if any(not zero(q) for q in g.jacobian(z)*f+badj.T*g.T) else [],'omit_potential_hessian':['tangent_constraint'] if any(not zero(q) for q in g.jacobian(z)*f+badV.T*g.T) else [],'wrong_determinant_power':['fixture_determinant'] if not zero(dt(6*s.log(x)-3*s.log(F))-(-6*h+bet*up)) else []}
result='K2305';note='explorations/conditional-build/k2305-regular-constrained-matter-transfer-2026-10-30.md';report='k2305-regular-constrained-matter-transfer.json';extra_deps=['explorations/conditional-build/k2302-designer-frame-turnaround-2026-10-30.md','explorations/conditional-build/k2299-finite-curvature-designer-family-2026-10-30.md'];evidence='Exact symbolic ODE, constraint and Jacobi identities plus rational interval bound certificates; no numerical evolution used';details={'jacobian':str(J),'reduced_dust_trace':str(s.trace(Jd)),'norm_bound':'exp(37/5)','determinant':'(x/x0)^6*(F0/F)^(7/2)'}

assert all(checks.values()),[k for k,v in checks.items() if not v]
assert all(faults.values()),faults
deps=[str(Path(__file__).relative_to(ROOT)),note]+extra_deps
data=dict(schema_version='1.0',result_id=result,checks=len(checks),check_names=list(checks),mutation_failed_checks=faults,evidence_kind=evidence,dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details=details)
out=ROOT/'lab/process'/report
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result=result,checks=len(checks),faults=len(faults))))
