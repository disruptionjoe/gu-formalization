"""Exact harmonic and adjoint controls; continuum domain proofs are in note."""
from pathlib import Path
import sympy as s
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2]
def evaluate(fault=None):
 c={}
 def ck(n,x):c[n]=bool(x)
 r,z,u,x=s.symbols('r z u x',positive=True);mu=s.symbols('mu',real=True)
 th,ee=s.symbols('th ee',real=True);aa=s.sin(th)*s.cos(th)
 jac=s.sin(th+ee*aa)/s.sin(th)*(1+ee*s.diff(aa,th))
 div=s.diff(aa,th)+s.cos(th)/s.sin(th)*aa
 ck('angular_map_jacobian',s.trigsimp(s.diff(jac,ee).subs(ee,0)-div)==0)
 contrast=s.diff(1/jac,ee).subs(ee,0) if fault!='reverse_count_sign' else s.diff(jac,ee).subs(ee,0)
 ck('angular_count_sign',s.trigsimp(contrast+div)==0)
 K=(r-z)/(r*z) if fault!='wrong_kernel' else (r-z)/(r*r)
 ck('lens_kernel',s.simplify(K-(1/z-1/r))==0)
 F=30*(r-1)**2*(2-r)**2;G=60*(r-1)**3*(2-r)**2
 M=s.integrate(F,(r,1,2));L=s.integrate(F/r,(r,1,2));f=s.integrate(F*K,(r,1,2))
 ck('source_normalized',M==1);ck('foreground_moment',s.simplify(f-(M/z-L))==0)
 P=s.legendre(2,mu);lap=s.diff((1-mu**2)*s.diff(P,mu),mu)
 ck('quadrupole_eigen',s.expand(lap+(5 if fault=='laplace5' else 6)*P)==0)
 ck('monopole_zero',s.diff(s.Integer(1),mu)==0)
 ck('observer_dipole_projection',s.integrate(mu*P,(mu,-1,1))==0)
 ck('log_remainder_L2',s.integrate(s.log(x)**2/x**2,(x,1,s.oo))==2)
 ck('cross_growth_sublinear',s.limit(s.sqrt(x)/x,x,s.oo)==0)
 ck('angular_mean_zero',s.integrate(P,(mu,-1,1))==0)
 ck('normalized_Y20',s.integrate(2*s.pi*5/(4*s.pi)*P**2,(mu,-1,1))==1)
 j1=s.sin(u)/u**2-s.cos(u)/u
 j2=(3/u**3-1/u)*s.sin(u)-3*s.cos(u)/u**2
 primitive=j1/u if fault!='wrong_primitive' else j1/u**2
 ck('bessel_primitive',s.simplify(s.diff(primitive,u)+j2/u)==0)
 ck('bessel_origin',s.limit(j1/u,u,0)==s.Rational(1,3))
 ck('bessel_second_order',s.limit(j2/u**2,u,0)==s.Rational(1,15))
 angular=(-3*s.diff(2*s.sin(u)/u,u,2)-2*s.sin(u)/u)/2
 ck('plane_wave_l2',s.simplify(angular+2*j2)==0)
 coefficient=(-24*s.pi)*(s.Rational(1,4) if fault=='wrong_integral' else s.Rational(1,3))
 ck('tail_coefficient',coefficient==-8*s.pi)
 ck('variance_slope',s.expand(coefficient**2)==64*s.pi**2)
 ck('positive_counterwindow',s.minimum(1+P/2,mu,s.Interval(-1,1))>0)
 comp=(F-G)/2 if fault!='same_sign_repair' else (F+G)/2
 ck('repair_angular_moment',s.integrate(comp,(r,1,2))==0)
 ck('repair_nontrivial',s.expand(comp)!=0)
 ck('repair_normalized',s.integrate((F+G)/2,(r,1,2))==1)
 ck('repair_radial_information',s.integrate(comp/r,(r,1,2))!=0)
 ck('taper_trace',all(s.diff(F,r,j).subs(r,v)==0 for j in [0,1] for v in [1,2]))
 # Exact scalar Fourier power laws, not sampled continuum certification.
 ck('white_tail_diverges',s.integrate(1,(x,1,s.oo)) is s.oo)
 ck('borderline_log',s.integrate(1/x,(x,1,s.oo)) is s.oo)
 ck('colored_tail_finite',s.integrate(x**-2,(x,1,s.oo))==1)
 eps=s.symbols('eps',positive=True)
 ck('foreground_weight_cost',s.integrate(z**-2,(z,eps,1))==1/eps-1)
 Phi,b,chi=s.symbols('Phi b chi');W=(Phi+b*chi)+(Phi-b*chi if fault!='wrong_weyl' else Phi+b*chi)
 ck('weyl_cancellation',s.expand(W-2*Phi)==0)
 # Tangential divergence formula and volume Jacobian cancellation.
 pp=s.Function('p')(z);ff=s.Function('f')(mu);angular_div=s.diff((1-mu**2)*s.diff(ff,mu),mu)
 ck('tangent_divergence',s.simplify((pp/z)/z*angular_div-pp*angular_div/z**2)==0)
 ck('vector_L2_radial_measure',s.simplify(z**2*(pp/z)**2-pp**2)==0)
 D=s.Matrix([[1,2],[3,1]]);B=s.Matrix([[2,-1],[-1,2]]);Q=s.diag(2,3)
 cov=(D+B)*Q*(D+B).T
 actual=D*Q*D.T+B*Q*B.T if fault=='independent_seed' else cov
 ck('shared_covariance',actual==s.Matrix([[21,21],[21,35]]))
 ck('shared_positive',cov.det()>0)
 return c
base=evaluate();assert all(base.values()),[k for k,v in base.items() if not v]
faults={}
for f in ['reverse_count_sign','wrong_kernel','laplace5','wrong_primitive','wrong_integral','same_sign_repair','wrong_weyl','independent_seed']:
 b=[k for k,v in evaluate(f).items() if not v];assert b,'undetected '+f;faults[f]=b
stem='k2323-born-lensing-observer-domain';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT))]+[f'explorations/conditional-build/{v}-2026-10-30.md' for v in ['k2321-radial-count-operator','k2311-uniform-constrained-dust-evolution','k2319-lightcone-density-readout']]
out=dict(schema_version='1.0',result_id='K2323',checks=len(base),check_names=list(base),mutation_failed_checks=faults,evidence_kind='exact symbolic harmonic, adjoint, moment and finite covariance controls; universal continuum conclusions use written proofs',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details={'tail':'-8pi*p(0)*M2*Y20/k','scope':'specified Born angular map and white-UV seed; not full relativistic counts','repairs':['foreground cutoff','angularly constant integrated moment','explicit colored quadrupole P~k^-alpha, alpha>1']})
p=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print(json.dumps({'result':'K2323','exact':len(base),'faults':faults}))
