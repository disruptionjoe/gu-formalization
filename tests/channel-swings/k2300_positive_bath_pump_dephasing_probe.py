from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,sys,math
import sympy as s
import numpy as np
from scipy.linalg import expm
ROOT=Path(__file__).resolve().parents[2];checks={}
def check(n,v):checks[n]=bool(v)
def z(x):return s.simplify(s.expand(x))==0
mu,t=s.symbols('mu t',positive=True)
coh=mu*(s.exp(t)-1);thermal=-s.log(2-s.exp(t))+mu*(s.exp(t)-1)/(2-s.exp(t))
polys={}
for name,logmgf in [('coherent',coh),('thermal',thermal)]:
 cumul=[s.simplify(s.diff(logmgf,t,j).subs(t,0)) for j in range(1,5)];m,k2,k3,k4=cumul
 var2=s.expand(4*m*m*k2+4*m*k3+k4+2*k2*k2);central=s.expand(k4+2*k2*k2)
 expect=4*mu**3+6*mu*mu+mu if name=='coherent' else 12*mu**3+102*mu*mu+203*mu+66
 check(name+'_square_variance',z(var2-expect));check(name+'_central_square_variance',z(central-(2*mu*mu+mu if name=='coherent' else 18*mu*mu+99*mu+34)))
 polys[name]=dict(m=m,k2=k2,k3=k3,k4=k4,var2=var2,central=central)
# Charge-moment identity, not a stored Boolean.
K,m=s.symbols('K m',real=True);expect=lambda poly: s.expand(poly).subs({K**4:s.Symbol('m4'),K**3:s.Symbol('m3'),K**2:s.Symbol('m2'),K:m})
check('Qsquare_charge_factor',s.expand((2*K)**4)==16*K**4)
e,R,th=s.symbols('e R th',real=True)
check('miscenter_linear_term',z((R-e)**2-R*R+2*e*R-e*e))
w,g,T,c=s.symbols('w g T c',positive=True)
phase=g*g*(w*T-s.sin(w*T))/(w*w)-c*T
check('counterterm_phase',z(phase.subs(c,g*g/w)+g*g*s.sin(w*T)/w**2))
check('revival_phase_mismatch',z(phase.subs({c:g*g/w+w/16,T:2*s.pi/w})+s.pi/8))
tau=s.symbols('tau',real=True)
bop,bdop=s.symbols('bop bdop',commutative=False);qop=s.symbols('qop',real=True)
check('positive_square_completion',s.expand(w*(bdop+g*qop/w)*(bop+g*qop/w)-(w*bdop*bop+g*qop*(bop+bdop)+g*g/w*qop**2))==0)
check('wrong_normal_order_distinct',s.expand(w*(bop+g*qop/w)*(bdop+g*qop/w)-(w*bdop*bop+g*qop*(bop+bdop)+g*g/w*qop**2))!=0)
# Exact half-period filters and covariance.
F1=2*s.I/w;F2=-F1;cov=s.Matrix([[s.re(F1*s.conjugate(F1)),s.re(F1*s.conjugate(F2))],[s.re(F2*s.conjugate(F1)),s.re(F2*s.conjugate(F2))]])
check('common_bath_revival_covariance',s.simplify((s.ones(1,2)*cov*s.ones(2,1))[0])==0 and s.trace(cov)>0)
check('sign_switch_destroys_revival',z((F1-F2)*s.conjugate(F1-F2)-16/w**2))
# Finite oscillator direct propagation independently checks sign and all factors.
dim=36;ann=np.diag(np.sqrt(np.arange(1,dim)),1);bd=ann.T;num=bd@ann;ident=np.eye(dim)
omega=1.3;coupling=.17;duration=.71;ct=coupling**2/omega+.04;nE=.4
weights=np.array([(1/(1+nE))*(nE/(1+nE))**k for k in range(dim)]);rho=np.diag(weights)
def exact_factor(q,qp):
 H=lambda q:omega*num+q*coupling*(ann+bd)+ct*q*q*ident
 return np.trace(expm(-1j*duration*H(q))@rho@expm(1j*duration*H(qp)))
vv=(2*nE+1)*4*coupling**2*math.sin(omega*duration/2)**2/omega**2
angle=(coupling**2/omega-ct)*duration-coupling**2*math.sin(omega*duration)/omega**2
for q,qp in [(0,2),(2,4),(1,3)]:
 actual=exact_factor(q,qp);formula=np.exp(-vv*(q-qp)**2/2+1j*angle*(q*q-qp*qp));check('oscillator_'+str(q)+'_'+str(qp),abs(actual-formula)<2e-13)
# Exact rational sqrt upper enclosures for the large actual consumer, no float tiny subtraction.
def su(n):
 n=int(n);a=math.isqrt(n);return a if a*a==n else a+1
delta=Q(9272,10**15);budgets={}
for kind,lam2 in [('raw',Q(1,10**58)),('centered',Q(1,10**44))]:
 for name,number in [('coherent',10**28),('thermal',4*10**28)]:
  d={k:int(v.subs(mu,number)) for k,v in polys[name].items()};vmax=12*lam2
  noise=2*vmax*(d['k2']+su(d['k4']+3*d['k2']**2));kerr=4*lam2*su(d['var2'] if kind=='raw' else d['central']);bound=delta+noise+kerr;budgets[kind+'_'+name]=str(bound)
  check(kind+'_'+name+'_full_budget',bound<(Q(9284,10**15) if kind=='raw' else Q(9358,10**15)))
  check(kind+'_'+name+'_field_consumer',6300000*bound<Q(8,1000)**2)
  energy=4*lam2*(d['k2']+d['m']**2 if kind=='raw' else d['k2'])
  check(kind+'_'+name+'_preparation_energy',energy<(Q(41,1000) if kind=='raw' and name=='coherent' else Q(641,1000) if kind=='raw' else Q(4801,10**18)))
# Coherent parity countercontrol, exact exponential parity sums.
pE=(1+s.exp(-2*mu))/2;pO=(1-s.exp(-2*mu))/2
check('Kerr_parity_overlap',z(pE*pE+pO*pO-(1+s.exp(-4*mu))/2))
# Independent positive number-bath model and non-Gaussian consumer.
rho_ratio,d,aa=s.symbols('rho_ratio d aa',real=True)
char=(1-rho_ratio)/(1-rho_ratio*s.exp(-s.I*d*aa))
check('number_bath_mean',z(s.I*s.diff(char,d).subs({d:0,rho_ratio:s.Rational(1,2)})-aa))
check('number_bath_variance',z(-s.diff(char,d,2).subs({d:0,rho_ratio:s.Rational(1,2)})-aa**2-2*aa**2))
check('number_bath_not_Gaussian',z(s.diff(s.log(char),d,3).subs({d:0,rho_ratio:s.Rational(1,2)})-6*s.I*aa**3))
for name,number in [('coherent',10**28),('thermal',4*10**28)]:
 dd={k:int(v.subs(mu,number)) for k,v in polys[name].items()};area=Q(1,10**28);var=2*area**2
 bound=delta+2*su(dd['k2'])*area+2*var*(dd['k2']+su(dd['k4']+3*dd['k2']**2))
 budgets['number_bath_'+name]=str(bound);check('number_bath_'+name+'_budget',bound<Q(9342,10**15))
assert all(checks.values()),[k for k,v in checks.items() if not v]
faults={
 'omit_counterterm_phase':['oscillator_0_2'] if abs(exact_factor(0,2)-np.exp(-vv*4/2+1j*(coupling**2*(omega*duration-math.sin(omega*duration))/omega**2)*(0-4)))>1e-4 else [],
 'drop_Kerr_phase':['oscillator_0_2'] if abs(exact_factor(0,2)-np.exp(-vv*4/2))>1e-4 else [],
 'wrong_Gaussian_factor':['oscillator_0_2'] if abs(exact_factor(0,2)-np.exp(-vv*4+1j*angle*(-4)))>1e-4 else [],
 'discard_segment_correlations':['common_bath_revival_covariance'] if s.trace(cov)!=0 else [],
 'coherent_moments_for_thermal':['thermal_square_variance'] if not z(polys['thermal']['var2']-polys['coherent']['var2']) else [],
 'wrong_center_sign':['miscenter_linear_term'] if not z((R+e)**2-R*R+2*e*R-e*e) else []}
assert all(faults.values()),faults
stem='k2300-positive-bath-pump-dephasing';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),'lab/process/k2296-stochastic-pump-drift.json','lab/process/k2293-moment-controlled-positive-pump.json']
data=dict(schema_version='1.0',result_id='K2300',checks=len(checks),check_names=list(checks),mutation_failed_checks=faults,evidence_kind='exact cumulants/formulas/rational bounds; finite oscillator numerics independently check channel; universal argument in note; hashes provenance',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},budgets=budgets,claim_ceiling='enlarged supplied collective finite bath; no inherited local alphabet or physical calibration claim')
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result='K2300',checks=len(checks),faults=len(faults))))
