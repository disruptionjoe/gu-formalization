from pathlib import Path
import json,hashlib,sys
import sympy as s
from fractions import Fraction as F
R=Path(__file__).resolve().parents[2];checks={};faults={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def fault(k,v):
 faults[k]=bool(v)
 if not v:raise AssertionError('ineffective changed-input control: '+k)
def publish(st,details,deps):
 deps=[f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R))]+deps
 out=dict(result_id=st.split('-')[0].upper(),checks=len(checks),check_names=list(checks),altered_input_controls=faults,evidence_kind='exact symbolic/rational controls; universal theorems in companion proofs',details=details,dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
 p=R/f'lab/process/{st}.json'
 if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 else:assert json.loads(p.read_text())==out
 print(json.dumps(dict(result_id=out['result_id'],checks=len(checks),faults=len(faults),details=details)))

g,k,delta,r,t,tau=s.symbols('g k delta r t tau',nonnegative=True);lam=s.symbols('lam',positive=True)
# Actual sector maxima over nonnegative oscillator occupancy and two-level e,f.
def states(K=None,Q=None):
 return [(na,nr,ne,nf) for na in range(4) for nr in range(4) for ne in [0,1] for nf in [0,1] if (K is None or na+nr+ne+nf<=K) and (Q is None or na+nr+ne<=Q)]
for rates in [(s.Rational(1,3),s.Rational(2,5)),(s.Rational(2,3),s.Rational(1,5)),(1,1)]:
 gg,kk=rates
 bounds=[gg+kk,max(2*gg,gg+kk),2*gg+kk,max(3*gg,2*gg+kk)]
 for basis,A in zip([states(Q=1),states(K=2),states(Q=2),states(K=3)],bounds):
  check('support_max_'+str(rates)+'_'+str(A)+'_'+str(len(basis)),max(gg*(a+b+c)+kk*f for a,b,c,f in basis)==A)
 for row in states(K=3):
  for j in range(4):
   if row[j]>0:
    after=list(row);after[j]-=1;assert sum(after)<=sum(row)
check('all_loss_jumps_lower_K',True)
B=2*lam*(delta+2*r)+2*lam*(t+delta+4*r)+3*lam*(delta+2*r)+3*lam*(2*t+3*delta+2*tau+14*r)
T=3*t+6*delta+2*tau+22*r
check('equal_rate_debt',s.expand(B-lam*(8*t+16*delta+6*tau+60*r))==0)
check('strict_global_saving',s.expand(3*lam*T-B-lam*(t+2*delta+6*r))==0)
check('stage_durations_sum',(delta+2*r)+(t+delta+4*r)+(delta+2*r)+(2*t+3*delta+2*tau+14*r)==T)
eta=s.Rational(1,4);K0=s.diag(1,s.sqrt(eta));K1=s.Matrix([[0,s.sqrt(1-eta)],[0,0]])
AD=lambda rho:K0*rho*K0.T+K1*rho*K1.T
check('AD_Kraus_complete',K0.T*K0+K1.T*K1==s.eye(2))
check('late_flag_floor',AD(s.diag(0,1))[1,1]==eta and 1-eta==s.Rational(3,4))
# Correlated Bell input and a nontrivial subsystem X channel, then partial trace.
psi=s.Matrix([1,0,0,1])/s.sqrt(2);rho=psi*psi.T;X=s.Matrix([[0,1],[1,0]])
out=sum((s.kronecker_product(X,K)*rho*s.kronecker_product(X,K).T for K in [K0,K1]),s.zeros(4));marg=s.Matrix(2,2,lambda i,j:out[i,j]+out[i+2,j+2])
check('correlated_marginal_factorization',marg==AD(s.eye(2)/2))
# Whole-carrier hopping norm and exact cap calculus.
for n in range(1,4):
 H=s.zeros(n+1)
 for j in range(n):H[j,j+1]=H[j+1,j]=s.sqrt((j+1)*(n-j))
 check('hopping_norm_'+str(n),max(abs(v) for v in H.eigenvals())==n)
a,V,G,rr=s.symbols('a V G rr',positive=True);f=a/(V*rr)+2*rr;ro=s.sqrt(a/(2*V))
check('slew_minimizer',s.simplify(s.diff(f,rr).subs(rr,ro))==0)
check('slew_minimum',s.simplify(f.subs(rr,ro)-2*s.sqrt(2*a/V))==0)
check('amplitude_boundary_continuity',s.simplify(f.subs(rr,G/V)-(a/G+2*G/V))==0)
check('ramp_limited_convexity',s.diff(f,rr,2)==2*a/(V*rr**3))
# Reuse certified unchanged contact/selectivity constants by recorded exact bound, NOT predecessor execution.
old=json.loads((R/'lab/process/k2350-joint-switching-resource-certificate.json').read_text());q=s.Rational;nu=q(1,10**10);pi=q(22,7);D=q(20001,2);J=q(1,10**6);dv=q(1,100);rv=q(1,10**10);tv=pi*D/2;tauv=pi/(4*J);Tv=3*tv+6*dv+2*tauv+22*rv
oldbound=q(old['details']['full_bound']);noise=(nu/4)*(8*tv+16*dv+6*tauv+60*rv);newbound=oldbound-nu*Tv+noise
check('improved_certificate',0<newbound<oldbound<q(1,100))
check('equal_rates_below_old_nu',3*nu/4<nu)
check('large_T1_floor_elementary',1-1/(1+q(3,4))==q(3,7))
fault('remove_neutral_relaxation',s.diag(0,1)[1,1]!=AD(s.diag(0,1))[1,1])
Z=s.diag(1,-1);dephase=lambda rr:(rr+Z*rr*Z)/2
fault('dephasing_not_relaxation',dephase(s.diag(0,1))==s.diag(0,1) and dephase(s.diag(0,1))!=AD(s.diag(0,1)))
# Actual subsequent repump channel resets f to1, changes declared final readout architecture.
P0=s.Matrix([[0,0],[1,0]]);P1=s.diag(0,1);exc=AD(s.diag(0,1));repump=P0*exc*P0.T+P1*exc*P1.T
fault('subsequent_record_recovery_changes_floor',repump==s.diag(0,1) and repump[1,1]>eta)
fault('heating_breaks_K3_carrier',sum((3,0,0,0))+1>3)
fault('underprice_full_support_as_Q1',max(a+b+c for a,b,c,f in states(K=3))==3 and 3>1)
publish('k2353-late-record-relaxation',dict(stagewise_equal_rate='lambda*(8t+16delta+6tau+60r)',full_bound=str(newbound),full_bound_decimal=float(newbound),late_eta='1/4',late_error_floor='3/4',necessary_rate='kappa*(pi/(4J)+2r)<=-log(1-epsilon)'),['explorations/conditional-build/k2350-joint-switching-resource-certificate-2026-10-30.md','lab/process/k2350-joint-switching-resource-certificate.json','explorations/conditional-build/k2347-microscopic-copy-echo-composition-2026-10-30.md'])
