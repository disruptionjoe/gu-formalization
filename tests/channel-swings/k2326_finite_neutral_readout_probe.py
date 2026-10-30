"""Exact block/instrument controls and finite numerical replay, not all-N certification."""
from pathlib import Path
import sympy as s
import mpmath as mp
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2];mp.mp.dps=60

def exact(fault=None):
 c={}
 def ck(n,x):c[n]=bool(x)
 t,d,nu=s.symbols('t d nu',positive=True);g=s.sqrt(d*d+nu*nu)
 a=s.exp(-d*t)*(s.cos(nu*t)-d/nu*s.sin(nu*t));b=s.exp(-d*t)*g/nu*s.sin(nu*t)
 source_loss=2*d if fault!='half_loss' else d
 ck('source_ODE',s.simplify(s.diff(a,t)+source_loss*a+g*b)==0)
 ck('destination_ODE',s.simplify(s.diff(b,t)-g*a)==0)
 ck('initial_source',a.subs(t,0)==1);ck('initial_destination',b.subs(t,0)==0)
 # Endpoint trigonometric data independently derived from atan2(nu,d).
 ct=d/g;st=nu/g
 ck('endpoint_angle',s.simplify(ct*ct+st*st-1)==0)
 ck('source_endpoint_zero',s.simplify(ct-d/nu*st)==0)
 ck('destination_endpoint_attenuation',s.simplify(g/nu*st)==1)
 delta=s.symbols('delta',real=True);late=s.expand_trig(s.cos(nu*delta)*ct-s.sin(nu*delta)*st-d/nu*(st*s.cos(nu*delta)+ct*s.sin(nu*delta)))
 ck('late_switch_residual',s.simplify(late+g/nu*s.sin(nu*delta))==0)
 ck('residual_first_order',s.simplify(s.diff(late,delta).subs(delta,0)+g)==0)
 r0,r1,r2,z=s.symbols('r0 r1 r2 z',positive=True);aa=[s.Rational(1,2),s.sqrt(2)/2,s.Rational(1,2)];rr=[1,r1,r2]
 pre=[aa[j]/rr[j] for j in range(3)] if fault!='missing_pretilt' else aa
 ck('pretilt_transfer',all(s.simplify(rr[j]*pre[j]-aa[j])==0 for j in range(3)))
 ck('sine_normalized',sum(x*x for x in aa)==1)
 gam,T=s.symbols('gamma T',positive=True)
 for n in [1,2]:ck('query_pretilt_'+str(n),s.simplify(s.exp(gam*n*T/2)*s.exp(-gam*n*T/(2 if fault!='query_loss_factor' else 1)))-1==0)
 En,tt=s.symbols('En tt',real=True)
 raising=s.exp(s.I*En*tt) if fault!='wrong_Kerr_phase' else s.exp(-s.I*En*tt)
 ck('Kerr_interaction_frame',s.simplify(s.exp(-s.I*En*tt)*raising)==1)
 phase_comp=s.exp(s.I*En*tt) if fault!='omit_storage_phase' else s.Integer(1)
 ck('known_storage_phase',s.simplify(phase_comp*s.exp(-s.I*En*tt))==1)
 # Two disjoint readout blocks; true direct-sum norm, not N-fold norm.
 H=s.diag(s.Matrix([[0,-s.I],[s.I,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.zeros(2))
 ck('orthogonal_block_norm',H*H==s.diag(1,1,1,1,0,0))
 Q=s.diag(2,2,2,2,1,1);ck('charge_conserved',H*Q==Q*H)
 L=s.zeros(6);L[4,0]=1;L[5,2]=s.sqrt(2)
 target=s.Matrix([0,1,0,1,0,0]);ck('parked_loss_dark',L*target==s.zeros(6,1))
 ck('lower_shell_inactive',H*s.eye(6)[:,4]==s.zeros(6,1))
 # Ordinary premature finite flag: jump half way leaves accepting amplitude.
 X=s.Matrix([[0,1],[1,0]]);rot=(s.eye(2)-s.I*X)/s.sqrt(2)
 lateprob=s.expand_complex(abs(rot[1,0])**2)
 ck('late_flag_counterexample',s.simplify(lateprob-s.Rational(1,2))==0)
 # Actual CPTP loss between two halves of a finite shell-controlled flag.
 # System basis is pilot-occupied N, parked N, lower shell.
 U=s.diag(rot,rot,s.eye(2));K1=s.zeros(3);K1[2,0]=1;K0=s.diag(0,1,1)
 ck('flag_loss_TP',K0.T*K0+K1.T*K1==s.eye(3))
 state=s.kronecker_product(s.eye(3)[:,0 if fault=='early_flag_as_safe' else 1],s.Matrix([1,0]))
 lost=U*s.kronecker_product(K1,s.eye(2))*U*state
 false_accept=s.expand_complex(abs(lost[5])**2)
 ck('safe_flag_requires_dark',s.simplify(false_accept)==0)
 M=4;F=s.Matrix([[s.I**(j*n)/2 for n in range(M)] for j in range(M)])
 ck('Fourier_unitary',F.conjugate().T*F==s.eye(M));ck('Fourier_fourth_power',F**4==s.eye(M))
 for val in [1,-1,s.I,-s.I]:
  P=sum((val**(-l)*F**l for l in range(4)),s.zeros(M))/4
  ck('spectral_projector_'+str(val),(P*P-P).applyfunc(s.simplify)==s.zeros(M) and (F*P-val*P).applyfunc(s.simplify)==s.zeros(M))
 S=s.zeros(4)
 for i in range(2):
  for j in range(2):S[2*j+i,2*i+j]=1
 ck('swap_involution',S*S==s.eye(4))
 U=(-s.I*s.pi*(s.eye(4)-S)/2).exp()
 ck('finite_swap_pulse',U==S)
 v=s.kronecker_product(s.Matrix([s.Rational(3,5),s.Rational(4,5)]),s.Matrix([1,0]))
 ck('reset_exports_state',S*v==s.kronecker_product(s.Matrix([1,0]),s.Matrix([s.Rational(3,5),s.Rational(4,5)])))
 # Exact alias support test for all n,m in three finite shells.
 for N in [1,2,5]:
  MM=N+(1 if fault=='too_few_outcomes' else 2)
  aliases=[(n,m,j) for n in range(N+1) for m in range(N+1) for j in [-1,1] if n-m+j!=0 and (n-m+j)%MM==0]
  ck('no_loss_alias_N'+str(N),not aliases)
 phi=s.symbols('phi',real=True)
 # N1 M2 control directly sums actual probabilities and circular loss.
 risk=s.cos(phi)**2*4*s.sin(phi)**2+s.sin(phi)**2*4*s.cos(phi)**2
 ck('alias_actual_risk',s.trigsimp(s.expand_trig(risk-(1-s.cos(4*phi))))==0)
 A,Z,eta=s.symbols('A Z eta',positive=True)
 ck('normalized_error_scale',s.simplify(eta/(A/Z)-eta*Z/A)==0)
 ck('survival_composition',s.expand((A/Z-eta)**2-(A/Z)**2*(1-eta*Z/A)**2)==0)
 return c

def numeric(fault=None):
 c={};details=[]
 for N,gamma,G in [(1,mp.mpf('.2'),mp.mpf('1')),(3,mp.mpf('.3'),mp.mpf('1')),(4,mp.mpf('.99'),mp.mpf('1'))]:
  rr=[mp.mpf(1)];taus=[];res=[]
  for n in range(1,N+1):
   d=gamma*n/4;nu=mp.sqrt(G*G-d*d);tau=mp.atan2(nu,d)/nu
   if fault=='uncorrected_pi_pulse':tau=mp.pi/(2*G)
   K=mp.expm(mp.matrix([[-2*d,-G],[G,0]])*tau)
   rr.append(mp.exp(-d*tau));taus.append(tau);res.append(abs(K[0,0])+abs(K[1,0]-rr[-1]))
  c['matrix_endpoint_N'+str(N)]=max(res)<mp.mpf('1e-48')
  c['duration_bound_N'+str(N)]=max(taus)<=mp.pi/(2*G)+mp.mpf('1e-48')
  cs=[mp.sqrt(mp.mpf(2)/(N+2))*mp.sin(mp.pi*(n+1)/(N+2)) for n in range(N+1)]
  Tq=mp.mpf('.7');Z=mp.sqrt(sum(cs[n]**2*mp.exp(gamma*n*Tq)/rr[n]**2 for n in range(N+1)))
  phi=mp.mpf('.31');out=[cs[n]*mp.exp(gamma*n*Tq/2)/(rr[n]*Z)*mp.exp(-gamma*n*Tq/2)*rr[n]*mp.exp(-2j*n*phi) for n in range(N+1)]
  c['full_pretilt_N'+str(N)]=max(abs(out[n]-cs[n]*mp.exp(-2j*n*phi)/Z) for n in range(N+1))<mp.mpf('1e-48')
  c['survival_bound_N'+str(N)]=1/Z**2>=mp.exp(-gamma*N*(Tq+mp.pi/(4*G)))-mp.mpf('1e-48')
  M=N+2;probs=[abs(sum(cs[n]*mp.exp(-2j*n*(phi-mp.pi*j/M)) for n in range(N+1)))**2/M for j in range(M)]
  risk=sum(probs[j]*4*mp.sin(phi-mp.pi*j/M)**2 for j in range(M))
  c['Fourier_risk_N'+str(N)]=abs(risk-2*(1-mp.cos(mp.pi/(N+2))))<mp.mpf('1e-48')
  c['Fourier_normalized_N'+str(N)]=abs(sum(probs)-1)<mp.mpf('1e-48')
  details.append(dict(N=N,gamma=str(gamma),G=str(G),Tq=str(Tq),survival=mp.nstr(1/Z**2,18),max_endpoint_residual=mp.nstr(max(res),6)))
 return c,details
base=exact();assert all(base.values()),[k for k,v in base.items() if not v]
nb,details=numeric();assert all(nb.values()),[k for k,v in nb.items() if not v]
faults={}
for f in ['half_loss','missing_pretilt','query_loss_factor','early_flag_as_safe','too_few_outcomes','wrong_Kerr_phase','omit_storage_phase']:
 bad=[k for k,v in exact(f).items() if not v];assert bad,'undetected '+f;faults[f]=bad
mut,_=numeric('uncorrected_pi_pulse');bad=[k for k,v in mut.items() if not v];assert bad;faults['uncorrected_pi_pulse']=bad
stem='k2326-finite-neutral-readout';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT))]+[f'explorations/conditional-build/{v}-2026-10-30.md' for v in ['k2324-kerr-selective-lossy-control','k2322-protected-reference-compiler','k2312-relational-finite-calibration']]
out=dict(schema_version='1.0',result_id='K2326',exact_checks=len(base),numeric_checks=len(nb),check_names=list(base)+list(nb),mutation_failed_checks=faults,evidence_kind='exact symbolic finite block/instrument controls and 60-digit matrix exponentials; universal bounds rely on written proof, not interval or proof-assistant certificates',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},numerical_controls=details,scope='supplied selective rank-block readout and finite neutral reservoir; no microscopic Kerr readout or native GU acceptance')
p=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print(json.dumps({'result':'K2326','exact':len(base),'numerical':len(nb),'faults':faults}))
