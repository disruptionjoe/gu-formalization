from pathlib import Path
import json,argparse,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]

ID='K2146';OUT='k2146-fixed-support-parity-ultraviolet.json'
DEPS=['explorations/conditional-build/k2143-local-canonical-parity-2026-10-27.md']
EVIDENCE='Exact symbolic two-lobe moment coefficients, finite spectral countercontrols and complete branch-energy accounting. Compact Fourier tails and fixed-envelope asymptotic claims have written proof; no finite sample certifies continuum support or causality.'
FAULTS=['inverse-moment','vacuum-half','energy-cross','branch-normalization','lobe-odd-moment']
def compute(fault=None):
 u,q,m,mu=s.symbols('u q m mu',positive=True)
 # u=1/K, central lobe; only coefficient extraction is finite symbolic evidence.
 root=s.sqrt((1+q*u)**2+m*m*u*u)
 series1=s.series(root,u,0,5).removeO();seriesm=s.series(1/root,u,0,5).removeO()
 def even_mean(poly):
  p=s.Poly(s.expand(poly),q);return s.expand(sum(coef*(0 if power[0]%2 else (1 if power[0]==0 else mu if power[0]==2 else s.Symbol('mu4'))) for power,coef in p.terms()))
 mean1=even_mean(series1);meanm=even_mean(seriesm)
 if fault=='lobe-odd-moment':mean1+=u
 ck={'real_envelope_odd_cancellation':s.expand(mean1).coeff(u,1)==0,'a1_coefficient':s.expand(mean1).coeff(u,2)==m*m/2,'inverse_moment_coefficient':s.expand(meanm).coeff(u,2)==mu-m*m/2}
 am=u+(mu-m*m/2)*u**3;a1=1/u+m*m*u/2;a2=1/u**2+mu+m*m
 if fault=='inverse-moment':am=u+(mu+m*m/2)*u**3
 A=s.expand(am*a1);ev=s.expand(am*a2-(2 if fault=='energy-cross' else 1)*a1)
 ck['A_leading_excess']=A.coeff(u,2)==mu
 ck['energy_cancellation']=ev.coeff(u,-1)==0 and ev.coeff(u,1)==2*mu
 ss=s.series((1+mu*u*u)**(-s.Rational(1,2)),u,0,5).removeO();pp=(1-ss)/(1 if fault=='vacuum-half' else 2)
 ck['probability_quarter']=s.expand(pp).coeff(u,2)==mu/4
 ck['rare_particle_count']=s.series((1+ss)/ss**2,u,0,3).removeO().expand()==2+3*mu*u*u/2
 K,d=s.symbols('K d',positive=True);am=(1/(K-d)+1/(K+d))/2;a1=K;a2=K*K+d*d;A=s.factor(am*a1)
 ck['exact_two_frequency_A']=s.factor(A-K*K/(K*K-d*d))==0
 ev=s.factor(am*a2-a1);ck['exact_two_frequency_energy']=s.factor(ev-2*K*d*d/(K*K-d*d))==0
 kval,dval=5,3;sv=s.sqrt(1-s.Rational(dval**2,kval**2));pv=(1-sv)/2;ee=ev.subs({K:kval,d:dval});em=ee/((2 if fault=='branch-normalization' else 4)*pv);ep=ee/(2*(1+sv));nn=(1+sv)/sv**2
 ck['rational_finite_branch_values']=(pv,ee,ee/2,em,ep,nn)==(s.Rational(1,10),s.Rational(45,8),s.Rational(45,16),s.Rational(225,16),s.Rational(25,16),s.Rational(45,16))
 ck['weighted_branch_energy']=s.simplify(pv*em+(1-pv)*ep-ee/2)==0
 ck['monochromatic_zero_probability']=A.subs(d,0)==1 and ev.subs(d,0)==0
 # Actual exact finite family gives the same consumed scaling limits.
 ss=s.sqrt(1-d*d*u*u);pp=(1-ss)/2;em=(1/u)*(1+ss)/ss**2;unread=d*d*u/(1-d*d*u*u)
 ck['noise_conditional_energy_limit']=s.limit(pp*em*em,u,0)==d*d
 ck['mean_conditional_energy_limit']=s.limit(unread*em,u,0)==2*d*d
 return {k:bool(v) for k,v in ck.items()}

def main():
 ck=compute();assert all(ck.values()),ck
 failures={}
 for f in FAULTS:
  failures[f]=[k for k,v in compute(f).items() if not v]
  assert failures[f],('FAULT UNDETECTED',f)
 report={'result_id':ID,'status':'conditional_exact_controls','exact_checks':ck,'fault_failures':failures,'universal_evidence':EVIDENCE,'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependency_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in DEPS}}
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();out=ROOT/'lab/process'/OUT
 if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(out.read_text())==report,'stored evidence differs'
 print(json.dumps({'result':ID,'checks':len(ck),'faults':len(failures),'failures':failures,'pass':True}))
if __name__=='__main__':main()
