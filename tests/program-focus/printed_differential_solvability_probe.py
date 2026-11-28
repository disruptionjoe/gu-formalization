#!/usr/bin/env python3
"""Exact printed-P scalarizer and lifted modes; no variable-PDE solver."""
from pathlib import Path
from fractions import Fraction as Q
import argparse,hashlib,json,sys,time
sys.dont_write_bytecode=True
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tests/program-focus'))
from printed_equation_jets_symbol_probe import engine
from source_action_deep_algebra import add,scale
CERT=ROOT/'lab/process/printed-differential-solvability-certificates.json'
A=[1,12,22,30,36,40,42]+list(range(-1,-13,-1))

def build():
 checks=[];modes=[]
 def ck(name,value):
  assert value,name
  checks.append(name)
 z,k,q=s.symbols('z k q');poly=s.Poly(s.prod(z-4*a for a in A),z)
 coeff=poly.all_coeffs();ck('nineteen-distinct-factors',len(A)==len(set(A))==19)
 ck('nonzero-highest-box-coefficient',coeff[-1]!=0)
 # m(z,q)=sum c_j z^(40-2j)q^j. Quotients need no noncommuting reordering.
 for j,c in enumerate(coeff):
  n=40-2*j;b=sum(-(-k)**l*z**(n-1-l)for l in range(n))
  ck(f'quotient-telescope:{n}',s.expand((k+z)*b-((-k)**n-z**n))==0)
 ck('max-orders',(max(40-2*j for j in range(20)),max(39-2*j for j in range(20)))==(40,39))
 # Exact covariant trace seam, using actual nested-star Phi in two odd-index ports.
 for name,eta,j in [('K95',[-1,1,1,1]+[1]*6+[-1]*4,10),('K77',[1,-1,-1,-1]+[1]*6+[-1]*4,4)]:
  e=engine(eta);sign=eta[0];kap=Q(12)
  for r in [Q(4),Q(8),Q(16)]:
   lo=(r-3/r)/2;hi=(r+3/r)/2
   lam,freq=(hi,lo)if sign<0 else(lo,hi)
   cov={0:lam,j:s.I*freq};qq=sum(eta[a]*v*v for a,v in cov.items())
   gamma={1<<a:eta[a]*v for a,v in cov.items()}
   one={(1<<a,0):v for a,v in cov.items()}
   longitudinal={(1<<a,c):v*w/qq for a,v in cov.items()for c,w in gamma.items()}
   O=add(e.phi1,scale(-1,longitudinal));V=e.wedge({(0,c):v for c,v in gamma.items()},O)
   P=lambda T:e.Phi(e.wedge(one,T))
   ck(f'{name}:{r}:nonnull-mass-shell',qq==-3 and kap*kap+48*qq==0)
   ck(f'{name}:{r}:trace-forward',P(O)==scale(-2,V))
   ck(f'{name}:{r}:trace-back',P(V)==scale(24*qq,O))
   vv=add(scale(kap,O),scale(2,V))
   ck(f'{name}:{r}:actual-endpoint-mode',not add(scale(kap,vv),P(vv)))
   ck(f'{name}:{r}:nonzero-mode',bool(vv))
   ck(f'{name}:{r}:only-sharp-skew-grades',all(c.bit_count()in[1,2]for leg,c in vv))
   ck(f'{name}:{r}:growing-rate',lam>0 and freq>0 and lam/freq>Q(1,2))
   ck(f'{name}:{r}:dispersion',lam*lam==freq*freq-sign*kap*kap/48)
   modes.append({'port':name,'lambda':str(lam),'normal_frequency':str(freq),'q':str(qq),'components':len(vv)})
  # Real primary-minus sharp on Clifford grades1/2, with odd negative index.
  ck(name+':sharp-grades-1-2',all((-1)**(p*(p+1)//2)==-1 for p in[1,2])and sum(x<0 for x in eta)%2==1)
 # Two-channel symbolic closure, independently of its native realization.
 M=s.Matrix([[0,24*q],[-2,0]]);v=s.Matrix([k,2])
 ck('two-channel-mass-shell-residual',(k*s.eye(2)+M)*v==s.Matrix([k*k+48*q,0]))
 ck('two-channel-square',M*M==-48*q*s.eye(2))
 # One-time Dirac is a known positive-norm control, not another printed mode.
 n,m=s.symbols('n m',real=True);alpha=s.Matrix([[0,1],[1,0]]);beta=s.diag(1,-1)
 D=-s.I*(n*alpha+m*beta)
 ck('ordinary-Dirac-positive-norm-control',D.conjugate().T+D==s.zeros(2))
 ck('ordinary-Dirac-dispersion-control',s.simplify(D*D+(n*n+m*m)*s.eye(2))==s.zeros(2))
 # Opposite signs give Q(lambda dt+i n dx)=-lambda^2-n^2.
 lam=s.symbols('lam',real=True);one_time_Q=-lam**2+(s.I*n)**2
 ck('one-time-mass-shell-sign',s.solve(k*k+48*one_time_Q,lam**2)==[k*k/48-n*n])
 # Variable coefficients are not licensed by pointwise nilpotency alone.
 x=s.symbols('x');H=s.Matrix([[1,0],[x,1]]);N=H*s.Matrix([[0,1],[0,0]])*H.inv()
 ck('moving-nilpotent-pointwise',N*N==s.zeros(2))
 ck('moving-nilpotent-derivative-defect',N*N.diff(x)!=s.zeros(2))
 Dv=lambda v:s.simplify(N*v.diff(x));f=s.Matrix([x*x,x**3]);kap=s.Rational(3,2)
 ck('moving-operator-idempotent',Dv(Dv(f))==Dv(f))
 naive=f/kap-Dv(f)/kap**2;correct=f/kap-Dv(f)/(kap*(kap+1))
 ck('moving-frozen-truncation-fails',s.simplify(kap*naive+Dv(naive)-f)!=s.zeros(2,1))
 ck('moving-modified-finite-inverse-survives',s.simplify(kap*correct+Dv(correct)-f)==s.zeros(2,1))
 inp=['tests/program-focus/source_action_deep_algebra.py','tests/program-focus/printed_equation_jets_symbol_probe.py','explorations/conditional-build/printed-equation-jets-and-symbol-2026-11-27.md','explorations/conditional-build/ricci-flat-ambient-source-jets-2026-11-27.md']
 return {'status':'PASS','checks':len(checks),'check_names':checks,'scalar_factors':A,'homogeneous_coefficients':[str(c)for c in coeff],'native_modes':modes,'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in inp},'sympy_version':s.__version__,'scope':'Exact algebra, native mixed-covector modes and controls. Universal symbol identity, fundamental solutions, curved analytic CK and Sobolev-growth argument are written proofs. No nonlinear endpoint, physical quotient or variable-coefficient instability certified.'}

if __name__=='__main__':
 p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group(required=True);g.add_argument('--write-certificate',action='store_true');g.add_argument('--verify',action='store_true');a=p.parse_args();t=time.monotonic();d=build()
 if a.write_certificate:CERT.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(CERT.read_text())==d,'certificate differs'
 print(json.dumps({'status':'PASS','checks':d['checks'],'modes':d['native_modes'],'seconds':time.monotonic()-t}))
