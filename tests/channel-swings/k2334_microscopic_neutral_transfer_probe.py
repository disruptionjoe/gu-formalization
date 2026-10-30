#!/usr/bin/env python3
"""Reversible logic exact; full-branch JC/phase/POVM controls at 60 digits."""
import argparse,hashlib,importlib.util,json
from pathlib import Path
import mpmath as m
import sympy as s
R=Path(__file__).resolve().parents[2];ST='k2334-microscopic-neutral-transfer';m.mp.dps=60
prior=Path(__file__).with_name('k2332_exact_jc_selective_control_probe.py');spec=importlib.util.spec_from_file_location('jc_predecessor',prior);jc=importlib.util.module_from_spec(spec);spec.loader.exec_module(jc)
def norm(a):return m.norm(a)
def carry(bits,k):
 d=2**len(bits);c=d-k;a=[0]
 for j,b in enumerate(bits):a.append((b*a[j]) if not (c>>j)&1 else b^a[j]^(b*a[j]))
 return a

def evaluate(fault=None):
 ex=[];nu=[]
 def ck(n,v):ex.append((n,bool(v)))
 def cn(n,v):nu.append((n,bool(v)))
 cases=0
 for q in range(1,5):
  d=2**q
  for k in range(1,d):
   for n in range(d):
    bits=[(n>>j)&1 for j in range(q)];a=carry(bits,k);expected=int(n>=k)
    assert a[-1]==expected
    # Circuit targets XOR into clean carries; reverse same gates, not overwrite.
    for j in range(q-1,-1,-1):
     c=((d-k)>>j)&1;b=bits[j];a[j+1]^=(b*a[j] if not c else b^a[j]^(b*a[j]))
    assert a==[0]*(q+1);cases+=1
 ck('finite exhaustive carry truth and reverse cleanup',cases==310)
 N=2;d=4;q=2;D=m.mpf(2);g=m.mpf('.7');J=m.mpf('0.000001');chi=m.mpf('1.3');conf=dict(jc.BASE)
 labels,ix,H,B,U,Hbare,Bbare,L=jc.matrices(N,D,g,conf);dim=len(labels)
 Pe0=m.diag([int(b=='+') for n,b in labels]);Pe=U.T*Pe0*U
 Lactual=L-Pe if fault=='photon_only' else L
 cn('actual matched contact commutes with JC',norm(Lactual*H-H*Lactual)<m.mpf('1e-45'))
 cn('bare total excitation contact identity',norm(U.T*(m.diag([n-int(b=='+') for n,b in labels])+Pe0)*U-L)<m.mpf('1e-45'))
 cn('lowering commutator',norm(L*B-B*L+B)<m.mpf('1e-45'))
 S=2*m.pi*(1-m.mpf(1)/d);copycoeff=[]
 F=m.matrix(d,d)
 for r in range(d):
  for n in range(d):F[r,n]=m.exp(2j*m.pi*r*n/d)/m.sqrt(d)
 cn('Fourier unitary',norm(F.H*F-m.eye(d))<m.mpf('1e-45'))
 for n in range(N+1):
  reg=m.matrix([m.exp(-1j*n*S/2)*m.exp(2j*m.pi*n*b/d)/m.sqrt(d) for b in range(d)])
  reg=F.H*reg
  if fault!='copy_phase':reg=m.diag([m.exp(1j*S*b/2) for b in range(d)])*reg
  target=m.zeros(d,1);target[n]=1
  cn(f'copy input{n} actual phase and amplitude',norm(reg-target)<m.mpf('1e-45'));copycoeff.append(reg[n])
 # Every saved-label block is simulated with the entire dressed carrier.
 # Neutral Boolean circuit exactness above makes these the coherent block columns.
 errors=[];Tcopy=S/(2*chi)+m.mpf('.37');gap=m.mpf('.173');td=m.pi/(2*chi)
 for n in range(N+1):
  vec=m.zeros(dim,1);vec[ix[n,'-']]=copycoeff[n];vec=m.expm(-1j*H*Tcopy)*vec;t=Tcopy
  for k in range(N,0,-1):
   f=int(n>k) if fault=='strict_threshold' else int(n>=k);z=1-2*f
   vec=m.expm(-1j*H*gap)*vec;t+=gap
   # rightmost A dagger first; actual finite contact propagator.
   vec=m.expm(-1j*(H-chi*z*Lactual)*td)*vec;t+=td
   i,j=ix[k-1,'-'],ix[k,'-'];omega=H[j,j]-H[i,i];b=B[i,j];u=J/b;tau=m.pi/(4*J)
   c=dict(jc.BASE);c['clock']=fault!='reset_clock'
   phase2=m.pi/2 if fault=='second_tone' else m.pi
   vec=jc.actual_pulse(H,B,L,omega,u,phase2,t,tau,c)*vec;t+=tau
   vec=m.expm(-1j*(H+chi*z*Lactual)*td)*vec;t+=td
   vec=jc.actual_pulse(H,B,L,omega,u,m.pi/2,t,tau,c)*vec;t+=tau
   vec=m.expm(-1j*H*gap)*vec;t+=gap
  vec=m.expm(-1j*H*m.mpf('.231'))*vec;t+=m.mpf('.231');target=m.zeros(dim,1);target[0]=1
  err=norm(vec-target);errors.append(err);cn(f'full microscopic transfer column{n}',err<m.mpf('.003'))
  cn(f'upper-branch leakage column{n}',sum(abs(vec[i])**2 for i,(a,b) in enumerate(labels) if b=='+')<m.mpf('.003')**2)
 # Exact ideal echo controls independently of physical sequence.
 X=m.matrix([[0,1j],[-1j,0]]);A=m.diag([1,m.exp(-1j*m.pi/2)])
 Y=m.matrix([[0,-1],[-1,0]])
 cn('conjugate second phase reverses first',norm(A*Y*A.H+X)<m.mpf('1e-45'))
 cn('flag zero cancels two ideal halves',norm(m.expm(-1j*X*m.pi/4)*A*m.expm(-1j*Y*m.pi/4)*A.H-m.eye(2))<m.mpf('1e-45'))
 # Outcome copying then tracing swapped-out register dephases; it does not erase record.
 a=m.matrix([m.sqrt(m.mpf(2)/(N+2))*m.sin((n+1)*m.pi/(N+2)) for n in range(N+1)])
 phi=m.mpf('.19');state=m.matrix([a[n]*m.exp(-2j*n*phi) if n<=N else 0 for n in range(d)]);out=F*state
 risk=sum(abs(out[r])**2*4*m.sin(m.pi*r/d-phi)**2 for r in range(d))
 cn('sine Fourier exact-risk finite control',abs(risk-2*(1-m.cos(m.pi/(N+2))))<m.mpf('1e-45'))
 effects=[]
 for r in range(d):
  eta=m.matrix([m.exp(-2j*m.pi*r*n/d) for n in range(N+1)]);effects.append(eta*eta.H/d)
 cn('actual POVM resolution',norm(sum(effects,m.zeros(N+1))-m.eye(N+1))<m.mpf('1e-45'))
 # Execute actual CNOT copy and SWAP on a nontrivial rational coherent register.
 psi=[s.Rational(1,2),s.I/2,s.Rational(1,2),-s.I/2]
 joint={((r if fault=='omit_reset' else 0),r,(0 if fault=='omit_reset' else r)):psi[r] for r in range(d)}
 reduced=s.zeros(d*d)
 for (b,e,f),amp in joint.items():
  for (bb,ee,ff),other in joint.items():
   if f==ff:reduced[b*d+e,bb*d+ee]+=amp*s.conjugate(other)
 intended=s.zeros(d*d)
 for r in range(d):intended[r,r]=s.Rational(1,4)
 ck('actual copy SWAP trace channel retains diagonal record and resets B',reduced==intended)
 ck('actual trace-preserving channel',s.trace(reduced)==1)
 record=m.diag([abs(out[r])**2 for r in range(d)])
 cn('record survives reset and trace is one',abs(sum(record[r,r] for r in range(d))-1)<m.mpf('1e-45') and sum(record[r,r]>m.mpf('1e-8') for r in range(d))>1)
 Na=3;db=4;aa=[m.sqrt(m.mpf(2)/(Na+2))*m.sin((n+1)*m.pi/(Na+2)) for n in range(Na+1)]
 def alias_risk(dd):
  ff=m.matrix(dd,dd)
  for rr in range(dd):
   for nn in range(dd):ff[rr,nn]=m.exp(2j*m.pi*rr*nn/dd)/m.sqrt(dd)
  bo=ff*m.matrix([aa[nn]*m.exp(-2j*nn*phi) if nn<=Na else 0 for nn in range(dd)])
  return sum(abs(bo[rr])**2*4*m.sin(m.pi*rr/dd-phi)**2 for rr in range(dd))
 br=alias_risk(db)
 cn('actual binary minimal-register alias changes risk',abs(br-2*(1-m.cos(m.pi/(Na+2))))>m.mpf('.001'))
 cn('binary enlarged register removes alias',abs(alias_risk(8)-2*(1-m.cos(m.pi/(Na+2))))<m.mpf('1e-45'))
 # Full budget algebra; includes fixed neutral/contact overhead before roots.
 Ac,lam,Bc,T0,eps=s.symbols('A lambda B T0 epsilon',positive=True);er=eps-lam*T0
 for root in [(er-s.sqrt(er**2-4*Ac*lam*Bc))/(2*Ac),(er+s.sqrt(er**2-4*Ac*lam*Bc))/(2*Ac)]:ck('fixed overhead amplitude polynomial',s.simplify(Ac*root**2-er*root+lam*Bc)==0)
 ck('mismatch population has norm one',Pe0**2==Pe0 and max(Pe0[i,i] for i in range(dim))==1)
 delta=2*g**4/(D*D+4*g*g*N)**m.mpf('1.5');AN=16*N*(N+1)/(delta*m.sqrt(N))*(1+m.pi/4*(3+2*m.sqrt(N)))
 cn('full basis-column error inside universal bound',max(errors)<AN*J)
 ev={'N':N,'d':d,'J':str(J),'all_basis_column_errors':[str(x) for x in errors],'duration_last_column':str(t),'A_prime_N':str(AN),'analytic_control_bound':str(AN*J),'carry_cases':cases,'risk':str(risk),'alias_N':Na,'alias_binary_d':db,'aliased_risk':str(br),'scope':'finite60digit full dressed propagators with nonzero gaps; no interval/hardware certificate, no measured device rates'}
 return ex,nu,ev

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();ex,nu,ev=evaluate()
 for name,ok in ex+nu:print(('PASS ' if ok else 'FAIL ')+name)
 assert all(ok for _,ok in ex+nu),'baseline must pass before faults'
 faults=[]
 for f in ['photon_only','copy_phase','reset_clock','second_tone','strict_threshold','omit_reset']:
  x,y,_=evaluate(f);bad=[n for n,ok in x+y if not ok];assert bad,f;faults.append({'changed_operator_or_input':f,'detected_by':bad});print('PASS fault',f,bad)
 report={'result':'K2334','status':'pass','exact_controls':ex,'finite_60_digit_controls':nu,'evidence':ev,'changed_input_faults':faults,'scope':'universal claims rely on written proofs; finite controls only; copied predecessor functions are hashed dependencies'}
 deps=[f'tests/channel-swings/{ST.replace("-","_")}_probe.py',f'explorations/conditional-build/{ST}-2026-10-30.md',str(prior.relative_to(R)),'explorations/conditional-build/k2332-exact-jc-selective-control-2026-10-30.md'];report['dependencies']={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps}
 if args.write:(R/f'lab/process/{ST}.json').write_text(json.dumps(report,indent=2)+'\n')
 print('PASS',len(ex),'exact;',len(nu),'finite60digit;',len(faults),'genuine faults')
if __name__=='__main__':main()
