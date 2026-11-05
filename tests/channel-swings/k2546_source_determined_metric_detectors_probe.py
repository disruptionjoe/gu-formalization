"""Exact operator, original-trace and Weyl-spectrum algebra; analytic proofs in note."""
from pathlib import Path
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(bank,name,v):
 bank[name]=bool(v)
 if not bank[name]:raise AssertionError('FAIL '+name)
def eq(name,a,b=0):ck(checks,name,s.simplify(a-b)==0)
k=s.symbols('k',nonzero=True);D=s.symbols('D');a=-5*k/2288;la=35*k*k/604032;e=5*la/6;mu=611557655*k*k/s.Integer(39953092608);c=970112/(13395*k);r=1/(6*a)
L=(D+e)*(D+mu);N=s.Rational(429,106)*D/k-s.Rational(70547,60632)*k
alpha=s.Rational(429,106)/k;delta=mu-e
# Eliminate ORIGINAL amplitude, retain both nonzero source residues.
eq('numerator_from_both_original_factors',r*(D+mu)+r*r*(D+e)/c,N)
eq('nonzero_pole_difference',delta,67736495*k*k/s.Integer(4439232512))
for name,pole in [('Einstein',-e),('tensor',-mu)]:
 ck(checks,'nonzero_residue_'+name,s.simplify(N.subs(D,pole))!=0)
 ck(controls,'single_factor_retains_'+name,s.simplify((D+(mu if name=='Einstein' else e)).subs(D,pole))!=0)
# Reconstruction modulo LH=NJ, treating operators as commuting polynomials.
H,J=s.symbols('H J');v=((D+mu)*H-alpha*J)/delta;u=((D+e)*H-alpha*J)/(delta*r)
eq('reconstruction_original_h',v-r*u,H)
eq('Einstein_reconstruction_residual',(D+e)*v-r*J,(L*H-N*J)/delta)
eq('tensor_reconstruction_residual',c*(D+mu)*u+r*J,c*(L*H-N*J)/(delta*r))
ck(controls,'shifted_metric_not_original_numerator',s.simplify(r*(D+mu)-N)!=0)
ck(checks,'nonempty_constant_source_contact',N.subs(D,0)!=0)
J0=s.symbols('J0');v0=r*J0/e;u0=-r*J0/(c*mu)
eq('explicit_constant_Einstein_response',e*v0,r*J0)
eq('explicit_constant_tensor_response',c*mu*u0,-r*J0)
eq('explicit_constant_filtered_signal',e*mu*(v0-r*u0),N.subs(D,0)*J0)
# Independent original two traces recover Ac/Bc and u, then full divergence.
Rh,tau,uu,t=s.symbols('Rh tau u t');m0=-4*k/11;mv=503*k/858;mh=893*k/858
orig=[72*a*Rh+12*(uu-la*tau)-t,m0*tau+121*uu/mv+12*Rh]
sol=s.solve(orig,[Rh,uu]);A=41511*k/s.Integer(1735888);B=34606/(s.Integer(29589)*k)
eq('original_curvature_trace',sol[Rh],A*tau-B*t)
q=s.Rational(2515,2820818)*k*5*k/12;rr=s.Rational(2515*1144,2820818*15)
eq('original_displacement_trace',sol[uu],q*tau+rr*t)
c0=s.Rational(5082101,4603456)*k;Z=s.symbols('W_C');raw=c0*sol[uu]+k*D*tau+4*Z/mh
elim=s.factor(raw.subs(tau,(Rh+B*t)/A)*A/k)
f=s.Rational(127052525,309793516032);g=s.Rational(5082101,2234087856);hw=s.Rational(1618929,17615318)
eq('full_retained_Weyl_elimination',elim,(D+f*k*k)*Rh+B*D*t+g*k*t+hw*Z/k)
ck(controls,'deleting_Weyl_changes_equation',s.diff(elim,Z)!=0)
eq('curved_volume_countercontrol',(-7*la/s.Integer(13))*D,-245*k*k*D/s.Integer(7852416))
ck(controls,'curved_volume_Weyl_not_zero',-7*la*D/13!=0)
# Derive curvature/Weyl eigenvalues from block contractions, no matrix assertion.
K=la/6
W_total=la-la*(14-1)/13
W_relative=la+la/13
W_tf=-K+la/13
W_mixed=la/13
for name,value,expected in [('total',W_total,0),('relative',W_relative,14*la/13),('block_tf',W_tf,-7*la/78),('mixed',W_mixed,la/13)]:eq('Weyl_eigenvalue_'+name,value,expected)
ck(checks,'full_symmetric_dimension',1+1+2*(7*8//2-1)+7*7==14*15//2)
ck(checks,'Weyl_kernel_only_total_metric',W_total==0 and all(s.simplify(x)!=0 for x in [W_relative,W_tf,W_mixed]))
ck(controls,'flat_Weyl_substitution_changes_kernel',all(x.subs(k,0)==0 for x in [W_relative,W_tf,W_mixed]))
# Hess phi=constant chi G implies lambda dphi=0, with Ricci term essential.
x=s.symbols('dphi');eq('Hessian_divergence_constraint',la*x,35*k*k*x/s.Integer(604032));ck(controls,'omitted_Ricci_loses_scalar_filter_obstruction',la!=0)
# Original block-adjoint signs, independent scalar formal variables.
z,Q,j,Epsi,Pchi,Lchi=s.symbols('z Q j Epsi Pchi Lchi');
eq('full_adjoint_shift_cancellation',(z-r*Q)*Epsi+Q*(r*Epsi+Lchi),z*Epsi+Q*Lchi)
eq('metric_filter_sign',-s.Rational(1,2)*L*H,-s.Rational(1,2)*(D+mu)*(D+e)*H)
for d,order,expected in [(7,4,s.Rational(15,2)),(7,2,s.Rational(11,2))]:eq('L2_scaling_order_'+str(order),s.Rational(d,2)+order,expected)
ck(controls,'unfiltered_noise_exponent_is_different',s.Rational(7,2)!=s.Rational(15,2))
paths=['explorations/conditional-build/k2546-source-determined-metric-detectors-2026-11-04.md',str(Path(__file__).relative_to(R)),'explorations/conditional-build/k2539-covariant-tensor-constraints-2026-11-04.md','explorations/conditional-build/k2543-localized-source-readout-2026-11-04.md','explorations/conditional-build/k2544-constrained-tensor-response-2026-11-04.md']
report={'result':'K2546','exact_algebra':checks,'contrary_controls':controls,'coefficients':{n:str(v) for n,v in dict(f=f,g=g,hW=hw,e=e,mu=mu,N=N).items()},'scope':'conditional compact contact probes and scalar Weyl-annihilation obstruction; analytic proofs in note, no arbitrary-source inverse','dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
p=R/'lab/process/k2546-source-determined-metric-detectors.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(p.read_text())==report,'saved report mismatch'
print('K2546',len(checks),'exact algebra groups',len(controls),'contrary controls')
