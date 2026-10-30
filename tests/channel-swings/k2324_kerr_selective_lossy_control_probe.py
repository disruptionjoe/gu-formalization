"""Exact selector identities and labeled finite numerical contraction controls."""
from pathlib import Path
import sympy as s
import mpmath as mp
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2];mp.mp.dps=65

def exact(fault=None):
 c={}
 def ck(n,x):c[n]=bool(x)
 n,k,chi=s.symbols('n k chi',real=True)
 E=lambda j:chi*j*(j-1)/2
 freq=chi*(k if fault=='wrong_carrier' else k-1)
 ck('detuning',s.expand(E(n)-E(n-1)-freq-chi*(n-k))==0)
 NN=4;num=s.diag(*range(NN+1));F=s.zeros(NN+1)
 for j in range(1,NN+1):F[j,j-1]=j+s.I;F[j-1,j]=j-s.I
 D=s.diag(*[s.I**j for j in range(NN+1)])
 comm=num*F-F*num if fault!='anticommutator' else num*F+F*num
 ck('dissipative_similarity',(s.I*comm-D*F*D.conjugate().T).applyfunc(s.simplify)==s.zeros(NN+1))
 checks=[]
 for N in range(2,8):
  for kk in range(1,N+1):
   for j in range(1,N+1):
    if j!=kk:checks.append(s.Rational(j*(N-j+1),kk*(N-kk+1)*(j-kk)**2)<=2)
 ck('coupling_ratio_controls',all(checks))
 A=s.zeros(5)
 for j in range(1,5):A[j,j-1]=A[j-1,j]=s.sqrt(j*(5-j))
 lam=s.symbols('lam');ck('beam_splitter_spectrum',s.expand(A.charpoly(lam).as_expr()-lam*(lam**2-4)*(lam**2-16))==0)
 V=A.copy();V[2,1]=V[1,2]=0
 ck('deleted_edge_blocks',V[:2,2:]==s.zeros(2,3) and V[2:,:2]==s.zeros(3,2))
 b1=s.sqrt(1*(1-1+1));ck('N1_no_unwanted',b1==1 and len([j for j in range(1,2) if j!=1])==0)
 x,L=s.symbols('x L',positive=True)
 f=1/s.sqrt(x*(L-x));log_second=s.diff(s.log(f),x,2)
 ck('convex_log',s.simplify(log_second-(1/(2*x*x)+1/(2*(L-x)**2)))==0)
 # Exact finite sum-of-squares identity is an independent coupling check.
 for N in [2,4,7]:ck('reciprocal_square_sum_'+str(N),sum(s.Rational(1,j*(N-j+1)) for j in range(1,N+1))==2*s.harmonic(N)/(N+1))
 a=s.Rational(1,2);q=(s.pi/2+s.asin(a))/s.sqrt(1-a*a)
 ck('fixed_a_resource_constant',s.simplify(q-4*s.pi/(3*s.sqrt(3)))==0)
 phi=(1+s.sqrt(5))/2
 ck('N3_passive_obstruction',s.simplify(phi**2-3)!=0)
 ck('N3_sine_ratio',s.simplify(s.sin(2*s.pi/5)/s.sin(s.pi/5)-phi)==0)
 N,J,qq,gg=s.symbols('N J q gamma',positive=True)
 per=4*s.sqrt(2)*J/chi*(N+qq/J*(2*J*N+J*N*s.pi+gg*N/2))
 bound=4*s.sqrt(2)*J*N/chi*(1+qq*(2+(gg/(4*J) if fault=='wrong_loss_factor' else gg/(2*J))+s.pi))
 ck('sequence_constant',s.simplify(per-bound)==0)
 T,t0=s.symbols('T t0',real=True)
 ck('terminal_phase_gap',s.expand(E(k)*T-E(k-1)*T-chi*(k-1)*T)==0)
 local_phase=-freq*t0 if fault!='wrong_start_phase' else freq*t0
 ck('global_clock_recovery',s.simplify(local_phase+freq*t0)==0)
 # Exact CPTP amplitude damping plus shell test, including a failed shell.
 rho=s.diag(0,s.Rational(9,10),s.Rational(1,10));P=s.diag(1,1,0)
 K0=s.diag(1,s.sqrt(s.Rational(4,5)),1);K1=s.zeros(3);K1[2,1]=s.sqrt(s.Rational(1,5))
 channel=lambda X:K0*X*K0.T+K1*X*K1.T
 ck('readout_channel_TP',K0.T*K0+K1.T*K1==s.eye(3))
 final=s.trace(channel(P*rho*P)) if fault=='early_flag' else s.trace(P*channel(rho)*P)
 ck('readout_final_flag',final==s.Rational(18,25))
 return c

def schedule(N,g):
 target=mp.matrix([mp.sqrt(mp.mpf(2)/(N+2))*mp.sin((j+1)*mp.pi/(N+2)) for j in range(N+1)])
 v=target.copy();nu=mp.sqrt(1-g*g/16);pulses=[]
 for k in range(N,0,-1):
  t=mp.atan2(nu*v[k],v[k-1]-g*v[k]/4)/nu
  B=mp.zeros(N+1);B[k-1,k]=1;B[k,k-1]=-1
  v=mp.expm((B+mp.diag([g*j/2 for j in range(N+1)]))*t)*v
  assert abs(v[k])/mp.norm(v)<mp.mpf('1e-50');v[k]=0;pulses.append((k,t))
 return target,list(reversed(pulses)),1/v[0]

def numeric(fault=None):
 c={};details=[]
 for N,g,chi in [(1,mp.mpf('.1'),mp.mpf('17')),(2,mp.mpf('.2'),mp.mpf('1000')),(3,mp.mpf('.3'),mp.mpf('1200'))]:
  target,pulses,A=schedule(N,g);T=sum(t for _,t in pulses);num=mp.diag(list(range(N+1)));H0=mp.diag([chi*j*(j-1)/2 for j in range(N+1)])
  creation=mp.zeros(N+1)
  for j in range(1,N+1):creation[j,j-1]=mp.sqrt(j*(N-j+1))
  ideal=mp.zeros(N+1,1);ideal[0]=1;actual=ideal.copy();t0=mp.mpf(0);errsum=mp.mpf(0)
  for k,t in pulses:
   freq=chi*(k-1);bk=mp.sqrt(k*(N-k+1));phase=mp.exp(1j*freq*T) if fault!='omit_terminal_phase' else 1
   u=1j*phase/bk;Hk=mp.zeros(N+1);Hk[k,k-1]=u*bk;Hk[k-1,k]=mp.conj(u*bk)
   ideal=mp.expm((-1j*Hk-g*num/2)*t)*ideal
   # Exact rotating-frame solution for actual GLOBAL-time laboratory drive.
   rot1=mp.diag([mp.exp(-1j*freq*j*(t0+t)) for j in range(N+1)])
   rot0=mp.diag([mp.exp(1j*freq*j*t0) for j in range(N+1)])
   Hconst=H0-freq*num+u*creation+mp.conj(u)*creation.T
   Ka=rot1*mp.expm((-1j*Hconst-g*num/2)*t)*rot0
   actual=Ka*actual;t0+=t
   fbound=0 if N==1 else 4*mp.sqrt(2)/abs(chi)
   errsum+=fbound*(1+t*(2+N/bk+g/2))
  ideal_lab=mp.diag([mp.exp(-1j*H0[j,j]*T) for j in range(N+1)])*ideal
  err=mp.norm(actual-A*target);norm=mp.norm(actual);p=A*A
  c['ideal_lab_endpoint_N'+str(N)]=mp.norm(ideal_lab-A*target)<mp.mpf('1e-48')
  c['actual_error_bound_N'+str(N)]=err<=errsum+mp.mpf('1e-48')
  c['survival_lower_N'+str(N)]=norm>=max(0,A-errsum)-mp.mpf('1e-48')
  overlap=abs(sum(mp.conj(target[j])*actual[j]/norm for j in range(N+1)))
  distance=mp.sqrt(max(mp.mpf(0),1-overlap*overlap))
  c['conditional_distance_N'+str(N)]=distance<=errsum/A+mp.mpf('1e-30')
  q=(mp.pi/2+mp.asin(g/4))/mp.sqrt(1-g*g/16);coarse=4*mp.sqrt(2)*(1+q*(2+g/2+mp.pi))*N/abs(chi)
  c['whole_sequence_bound_N'+str(N)]=errsum<=coarse+mp.mpf('1e-48')
  details.append({'N':N,'gamma':str(g),'chi':str(chi),'raw_error':mp.nstr(err,18),'proved_bound':mp.nstr(errsum,18),'ideal_survival':mp.nstr(p,18)})
 return c,details
base=exact();assert all(base.values()),[k for k,v in base.items() if not v]
nb,details=numeric();assert all(nb.values()),[k for k,v in nb.items() if not v]
faults={}
for f in ['wrong_carrier','anticommutator','wrong_loss_factor','wrong_start_phase','early_flag']:
 bad=[k for k,v in exact(f).items() if not v];assert bad,'undetected '+f;faults[f]=bad
mut,_=numeric('omit_terminal_phase');bad=[k for k,v in mut.items() if not v];assert bad;faults['omit_terminal_phase']=bad
stem='k2324-kerr-selective-lossy-control';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT))]+[f'explorations/conditional-build/{v}-2026-10-30.md' for v in ['k2322-protected-reference-compiler','k2312-relational-finite-calibration']]
data=dict(schema_version='1.0',result_id='K2324',exact_checks=len(base),numeric_checks=len(nb),check_names=list(base)+list(nb),mutation_failed_checks=faults,evidence_kind='symbolic finite identities and 65-digit finite matrix exponential controls; universal bounds use written proof, not interval or proof-assistant certification',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},numerical_controls=details,scope='supplied finite-shell Kerr/beam-splitter Markov model; no hardware or native GU claim')
p=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:p.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==data
print(json.dumps({'result':'K2324','exact':len(base),'numerical':len(nb),'faults':faults,'controls':details}))
