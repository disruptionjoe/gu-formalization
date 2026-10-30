"""Exact finite loss channels; general control/renewal proofs are in the note."""
from pathlib import Path
import sympy as s
from fractions import Fraction as Q
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2]
def maps(N,eta,reference=True):
 states=[(n,m-n) for m in range(N+1) for n in range(m+1)];pos={x:i for i,x in enumerate(states)};out=[]
 for lp in range(N+1):
  for lr in range(N+1-lp):
   if not reference and lr:continue
   K=s.zeros(len(states),N+1)
   for n in range(N+1):
    if lp<=n and lr<=N-n:
     c=s.sqrt(s.binomial(n,lp))*(1-eta)**s.Rational(lp,2)*eta**s.Rational(n-lp,2)
     if reference:c*=s.sqrt(s.binomial(N-n,lr))*(1-eta)**s.Rational(lr,2)*eta**s.Rational(N-n-lr,2)
     K[pos[n-lp,N-n-lr],n]=c
   out.append((lp,lr,K))
 E=s.zeros(len(states),N+1)
 for n in range(N+1):E[pos[n,N-n],n]=1
 return states,out,E

def evaluate(fault=None):
 checks={}
 def check(n,v):checks[n]=bool(v)
 eta=s.Rational(4,9)
 for N in [1,2,3,4]:
  states,Ks,E=maps(N,eta,fault!='remove_reference_loss');eye=s.eye(N+1);P=E*E.T;K0=Ks[0][2]
  check('complete_'+str(N),sum((K.T*K for _,_,K in Ks),s.zeros(N+1))==eye)
  check('scalar_no_jump_'+str(N),K0==eta**s.Rational(N,2)*E)
  check('survival_'+str(N),K0.T*K0==eta**N*eye)
  number=s.diag(*[sum(x) for x in states]);avg=sum((K.T*number*K for _,_,K in Ks),s.zeros(N+1))
  check('mean_stock_'+str(N),avg==eta*N*eye)
  flag=s.eye(len(states)) if fault=='accept_loss_sectors' else P
  check('final_flag_'+str(N),sum((K.T*flag*K for _,_,K in Ks),s.zeros(N+1))==eta**N*eye)
  check('orthogonal_loss_'+str(N),all(P*K==s.zeros(*K.shape) for lp,lr,K in Ks if lp+lr))
 H=s.Matrix([[2,1+2*s.I,0],[1-2*s.I,-3,3-s.I],[0,3+s.I,4]])
 n=s.diag(0,1,2);off=H-s.diag(*H.diagonal());U=s.diag(1,s.I,-1)
 check('speed_conjugacy',(s.I*(H*n-n*H)+U*off*U.conjugate().T).applyfunc(s.simplify)==s.zeros(3))
 psi=s.Matrix([1,2*s.I,3])/s.sqrt(14);m=(psi.conjugate().T*n*psi)[0];m2=(psi.conjugate().T*n*n*psi)[0];gamma=s.symbols('gamma',positive=True)
 raw=-s.I*H*psi-gamma*n*psi/2
 den=(raw.conjugate().T*psi+psi.conjugate().T*raw)[0];num=(raw.conjugate().T*n*psi+psi.conjugate().T*n*raw)[0]
 drift=s.simplify(num-m*den);comm=(s.I*psi.conjugate().T*(H*n-n*H)*psi)[0]
 predicted=comm+(gamma if fault=='reverse_conditional_drift' else -gamma)*(m2-m*m)
 check('normalized_drift',s.simplify(drift-predicted)==0);check('positive_variance',m2-m*m>0)
 J,M,N=s.symbols('J M N',positive=True);t=s.symbols('t',real=True)
 exposure=s.integrate(J*t,(t,0,M/J));check('backward_cone',s.simplify(exposure-M*M/(2*J))==0)
 check('protected_exposure',s.simplify(exposure.subs(M,N/2)-N*N/(8*J))==0)
 equal=(1 if fault=='drop_stock_factor' else N)*N/(2*J);check('equal_loss_exposure',s.simplify(equal-N*N/(2*J))==0)
 states,Ks,E=maps(1,eta,False);v=Ks[0][2]*s.ones(2,1)/s.sqrt(2);p=(v.T*v)[0]
 check('filter_survival',p==(1+eta)/2);check('ideal_exposure_is_wrong',p!=s.sqrt(eta))
 check('conditional_mean',s.simplify((v.T*s.diag(*[a[0] for a in states])*v)[0]/p-eta/(1+eta))==0)
 z=s.symbols('z',positive=True);check('conditional_hazard',s.simplify((-gamma*z/2)/((1+z)/2)+gamma*z/(1+z))==0)
 p0=Q(43,45);eps=Q(1,172);success=p0*(1 if fault=='discard_failures_in_confidence' else 1-eps)
 check('all_launch_confidence',success==Q(19,20));check('average_budget',Q(9491,10**15)+Q(5,10**13)==Q(9991,10**15)<Q(1,10**11))
 stock=3*10**27;check('confidence_rate_before_pi',2*eps/Q(stock*stock)==Q(1,86*9*10**54));check('average_rate_before_pi',2*Q(5,10**13)/Q(stock*stock)==Q(1,9*10**66))
 p,ell=s.symbols('p ell',positive=True);total=ell/p;check('renewal_equation',s.simplify(total-ell-(1-p)*total)==0)
 charge=(1 if fault=='omit_charge_two' else 2)*total;check('charge_units',s.simplify(charge-2*ell/p)==0)
 check('record_bits',2**91<stock+2<=2**92)
 # Exact N1 compiler ODE, endpoint, norm and speed barrier.
 theta=s.symbols('theta',real=True);alpha,nu=s.symbols('alpha nu',positive=True)
 vec=s.Matrix([s.cos(theta),s.sin(theta)]);rot=s.Matrix([[0,-J],[J,0]])
 raw=rot*vec-s.diag(0,gamma/2)*vec
 angle=s.simplify(-s.sin(theta)*raw[0]+s.cos(theta)*raw[1])
 expected=J-(gamma/(2 if fault=='double_angle_loss' else 4))*s.sin(2*theta)
 check('angle_speed',s.simplify(angle-expected)==0)
 check('target_barrier',s.simplify(angle.subs(theta,s.pi/4)-(J-gamma/4))==0)
 # Explicit exponential solves the unnormalized two-state ODE, nu^2=J^2-alpha^2.
 tt=s.symbols('tt',real=True)
 v0=s.exp(-alpha*tt)*(s.cos(nu*tt)+alpha*s.sin(nu*tt)/nu)
 v1=s.exp(-alpha*tt)*J*s.sin(nu*tt)/nu
 residual=s.Matrix([s.diff(v0,tt),s.diff(v1,tt)])-s.Matrix([[0,-J],[J,-2*alpha]])*s.Matrix([v0,v1])
 check('compiler_ode_0',s.simplify(residual[0].subs(J*s.Integer(1),J)).subs(nu**2,J**2-alpha**2).simplify()==0)
 check('compiler_ode_1',s.simplify(residual[1])==0)
 check('compiler_initial',v0.subs(tt,0)==1 and v1.subs(tt,0)==0)
 # Choose a=3/5,nu/J=4/5; target sine/cosine values are 2/sqrt5,1/sqrt5.
 aa=s.Rational(3,5);bb=s.Rational(4,5);sinT=2/s.sqrt(5);cosT=1/s.sqrt(5)
 ca=cosT+aa*sinT/bb;cb=sinT/bb
 check('compiler_endpoint',s.simplify(ca-cb)==0)
 factor=ca*ca+cb*cb
 if fault=='omit_survival_denominator':factor=1
 check('compiler_survival_factor',s.simplify(factor-1/(1-aa))==0)
 check('time_angle_identity',s.simplify(sinT/cosT-bb/(1-aa))==0)
 check('threshold_quadratic_zero',s.limit((1-s.sin(2*theta))/(theta-s.pi/4)**2,theta,s.pi/4)==2)
 return checks
base=evaluate();assert all(base.values()),[n for n,v in base.items() if not v]
faults={}
for f in ['remove_reference_loss','accept_loss_sectors','reverse_conditional_drift','drop_stock_factor','discard_failures_in_confidence','omit_charge_two','double_angle_loss','omit_survival_denominator']:
 result=evaluate(f);faults[f]=[n for n,v in result.items() if not v];assert faults[f],'undetected '+f
stem='k2320-lossy-selective-calibration';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT))]+[f'explorations/conditional-build/{x}-2026-10-30.md' for x in ['k2312-relational-finite-calibration','k2315-calibration-control-cost','k2318-loss-limited-calibration']]
data=dict(schema_version='1.0',result_id='K2320',checks=len(base),check_names=list(base),mutation_failed_checks=faults,evidence_kind='exact finite Kraus, conditional drift, exposure and rational resource controls; arbitrary-N/time-dependent proofs in note',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details={'equal_loss_preparation_exposure':'N**2/(2*J)','protected_exact_conditional_endpoint_exposure':'N**2/(8*J)','confidence_sufficient_loss':'1/172','average_sufficient_loss':'5/10**13','renewal_photons':'N*(1-exp(-gamma*T))*exp(gamma*N*T)'})
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps({'result':'K2320','checks':len(base),'faults':len(faults)}))
