#!/usr/bin/env python3
"""Exact finite controls for the continuum proofs in K2335; no empirical calibration."""
import argparse,hashlib,json
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parents[2];ST='k2335-angular-response-recovery'
t=s.symbols('t',real=True);P=s.legendre(2,t)
def evaluate(fault=None):
 out=[];details={}
 def ck(n,v):out.append((n,bool(v)))
 w=[1+P/2,1-P/2]
 shapes=[s.Rational(5,8)*(3*t*t-1)**2,s.Rational(15,4)*t*t*(1-t*t),s.Rational(15,16)*(1-t*t)**2]
 H=2*s.atanh(s.sqrt(s.Rational(3,5)))/s.sqrt(15)
 formulas=[[(260-80*s.pi)/9,20*(s.pi-3)/3,5*(4-s.pi)/3],[36-64*H,40*H-20,4-6*H]]
 for i,wi in enumerate(w):
  for l in [0,1,2,3,4,6]:
   f=s.legendre(l,t);extract=wi*f/(1 if fault=='omit_inverse_response' else wi)
   actual=s.integrate(s.expand(s.cancel(P*extract)),(t,-1,1));expected=s.Rational(2,5) if l==2 else 0
   ck(f'window {i} actual l{l} extraction',s.simplify(actual-expected)==0)
  ck(f'window {i} naive monopole leakage nonzero',s.integrate(P*wi,(t,-1,1))!=0)
  # Integrate rational functions exactly. Sympy may use logarithms instead of atanh;
  # derivative and endpoint checks below retain exact symbolic identities.
  vals=[]
  for m,p in enumerate(shapes):
   integ=s.integrate(p/wi**(1 if fault=='noise_weight_not_squared' else 2),t)
   val=integ.subs(t,1)-integ.subs(t,-1);vals.append(val)
   ck(f'window {i} m{m} exact primitive derivative',s.simplify(s.diff(integ,t)-p/wi**2)==0)
   # log identities are normalized using exact atanh definition, not a tolerance.
   target=formulas[i][m]
   diff=s.expand_log(s.expand_complex((val-target).rewrite(s.log)),force=True)
   exact=s.simplify(s.expand_log(diff,force=True))
   ck(f'window {i} m{m} exact endpoint formula',exact==0)
  details[f'window_{i}_gram']=[str(s.N(x,18)) for x in formulas[i]]
 ck('addition theorem polynomial',s.expand(shapes[0]+2*shapes[1]+2*shapes[2]-s.Rational(5,2))==0)
 mean_covariance=4*s.eye(2);mean_vector=s.Matrix([1,0])
 exponent=-1 if fault=='covariance_inverse_not_sqrt' else -s.Rational(1,2)
 whitened=mean_covariance**exponent*mean_vector
 ck('actual D4 mean normalization beta squared',(whitened.T*whitened)[0]==s.Rational(1,4))
 delta=s.Rational(1,128);beta=s.Rational(1,64)
 ck('covariance plus mean exact five-percent margin',5*delta**2/(4*(1-delta))+beta**2/4<(s.Rational(1,20)-s.Rational(1,32))**2)
 # Actual finite response map whose whitened rows are a coisometry.
 T=s.zeros(10,20)
 for j in range(10):T[j,2*j]=s.Rational(3,5);T[j,2*j+1]=s.Rational(4,5)
 ck('relative covariance extraction coisometry',T*T.T==s.eye(10))
 v=s.ones(20,1);F=v*v.T/s.Integer(2560)
 if fault=='raw_correlation_amplitude':F*=10
 E=T*F*T.T
 ck('raw actual covariance relative bound',max(F.eigenvals())<=delta)
 ck('extracted actual covariance relative bound',max(E.eigenvals())<=delta)
 variances={}
 for L in [2,3,4,6]:
  Y=s.Matrix([s.sqrt(s.Rational(2*l+1,2))*s.legendre(l,t) for l in range(L+1)])
  G=Y*Y.T;G=G.applyfunc(lambda z:s.integrate(z,(t,0,1)));inv=G.inv()
  ck(f'hemisphere L{L} Gram positive',all(G[:k,:k].det()>0 for k in range(1,L+2)))
  ck(f'hemisphere L{L} exact unbiased inverse',inv*G==s.eye(L+1))
  variances[str(L)]=str(inv[2,2])
  if L==2:
   tail=s.Integer(0) if fault=='discard_angular_tail' else s.sqrt(s.Rational(7,2))*s.legendre(3,t)
   raw=(Y*tail).applyfunc(lambda z:s.integrate(z,(t,0,1)))
   bias=(inv*raw)[2]
   ck('actual l3 tail creates quadrupole bias',bias!=0)
   details['hemisphere_L2_l3_bias']=str(bias)
 ck('fixed quadrupole noise increases in concrete band sequence',all(s.Rational(variances[str(b)])>s.Rational(variances[str(a)]) for a,b in [(2,3),(3,4),(4,6)]))
 # Hidden L2 sky under actual hemisphere mask, not claimed compact-k prior support.
 ck('hidden hemisphere quadrupole is nonzero',s.integrate(P*P,(t,-1,0))==s.Rational(1,5))
 ck('small calibration error times monopole leaks',s.integrate(P*P,(t,-1,1))==s.Rational(2,5))
 details['hemisphere_quadrupole_variance_factors']=variances
 return out,details

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();checks,details=evaluate();bad=[n for n,v in checks if not v];assert not bad,bad
 faults=[]
 for f in ['omit_inverse_response','noise_weight_not_squared','raw_correlation_amplitude','discard_angular_tail','covariance_inverse_not_sqrt']:
  c,_=evaluate(f);bad=[n for n,v in c if not v];assert bad,f;faults.append({'changed_input':f,'detected_by':bad})
 report={'result':'K2335','status':'pass','exact_controls':checks,'values':details,'changed_input_faults':faults,'scope':'Exact finite harmonic integrals, finite-band matrices and rational margins; continuum recovery, hidden-sky and divergence results rely on written proofs. No empirical or GU certificate.'}
 deps=[f'tests/channel-swings/{ST.replace("-","_")}_probe.py',f'explorations/conditional-build/{ST}-2026-10-30.md','lab/process/k2331-certified-count-window-covariance.json','explorations/conditional-build/k2333-masked-count-discrimination-2026-10-30.md']
 report['dependencies']={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps}
 if a.write:(R/f'lab/process/{ST}.json').write_text(json.dumps(report,indent=2)+'\n')
 print('PASS',len(checks),'exact controls;',len(faults),'genuine changed-input faults');print(json.dumps(details,indent=2))
if __name__=='__main__':main()
