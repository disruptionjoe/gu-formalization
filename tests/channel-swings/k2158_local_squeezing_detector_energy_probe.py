#!/usr/bin/env python3
"""Symbolic covariance identities and exact rational scalar certificates."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import sympy as sp
ROOT=Path(__file__).resolve().parents[2]
def A(x,a=F(5),d=F(205,9)):
 return a/4*(x**-2+2*x-3)+d/4*(x-1)**2
def energy(x,E=F(5)):return x*E+A(x)
def deriv(x,E=F(5)):return E+F(5,2)*(1-x**-3)+F(205,18)*(x-1)
def certificate():
 lo=F(1,2);hi=F(1)
 for _ in range(90):
  mid=(lo+hi)/2
  if deriv(mid)<0:lo=mid
  else:hi=mid
 mid=(lo+hi)/2;upper=energy(mid)
 # Global convex tangent at mid, minimized over the certified minimizer interval.
 lower=upper+min(deriv(mid)*(lo-mid),deriv(mid)*(hi-mid))
 assert deriv(lo)<0<deriv(hi) and lower<=upper and upper-lower<F(1,10**40)
 return {k:str(v) for k,v in dict(root_lower=lo,root_upper=hi,energy_lower=lower,energy_upper=upper).items()}
def controls(fault=None,symbolic=False):
 ck={};check=lambda k,v:ck.__setitem__(k,bool(v));x=F(4,5);E=F(5)
 xx=1/x if fault=='inverse_squeeze' else x
 actual=xx*E+(0 if fault=='omit_vacuum_cost' else A(xx))
 check('rational_improvement',actual==F(12761,2880) and actual<E)
 check('vacuum_cost',A(x)==F(1241,2880)>0)
 check('zero_squeeze',energy(F(1),E)==E and A(F(1))==0 and deriv(F(1))==E)
 # Independent two-mode covariance evaluation in actual spectral fixture.
 n=F(1,3);s=F(2,3);h=j=F(5);cross=0 if fault=='drop_cross_energy' else F(-4)
 ch=(xx+1/xx)/2;sh=(xx-1/xx)/2;t=s-E/(2*(h+j)*s)
 nh=(n+1)*(n+(2*n+1)*sh**2)+n*(n+1)-2*s*ch*t
 nj=(n+1)*n+n*(n+1+(2*n+1)*sh**2)-2*s*ch*t
 hj=(2*n+1)*sh*(t-s*ch)
 check('independent_bogoliubov_energy',h*nh+j*nj+2*cross*hj==F(12761,2880))
 check('CCR_under_squeezing',ch*ch-sh*sh==1)
 check('spectral_cross_identity',cross*(2*n+1)/s==-(h+j))
 # Exact finite unitary fixture checks operation ordering and each effect (not an all-Fock proof).
 U=sp.Matrix([[sp.Rational(3,5),-sp.Rational(4,5)],[sp.Rational(4,5),sp.Rational(3,5)]])
 K=[sp.diag(sp.Rational(3,5),0),sp.diag(sp.Rational(4,5),1)]
 L=[k*U if fault=='presqueeze' else U*k for k in K]
 check('all_recorded_effects_unchanged',all(l.T*l==k.T*k for l,k in zip(L,K)))
 check('complete_record',sum((l.T*l for l in L),sp.zeros(2))==sp.eye(2))
 z=F(1,4);alpha=z;eta=F(1)
 if fault=='changed_signal':eta=1-(1-z)**2
 check('fixed_photon_added_ROC',alpha==F(1,4) and eta==1 and (1-(eta-alpha))/2==F(1,8))
 check('strict_positive_vacuum_controls',all(A(q)>0 for q in [F(1,2),F(4,5),F(6,5),F(2)]))
 if symbolic:
  N,m1,m2,X,B=sp.symbols('N m1 m2 X B',positive=True);a=2*N+1;nu=m1/a;s2=N*(N+1)
  eh=(nu+2*m1+m2/nu)/(4*(N+1));ej=(nu-2*m1+m2/nu)/(4*N);es=sp.factor(eh+ej)
  # Products s*t and F*s avoid symbolic square-root branches.
  st=s2-B/(2*es);fs=(nu-m2/nu)/4;c=(X+1/X)/2;v=(X-1/X)/2
  nh=(N+1)*(N+a*v*v)+N*(N+1)-2*c*st
  nj=(N+1)*N+N*(N+1+a*v*v)-2*c*st
  crossenergy=2*fs*a*v*(st/s2-c)
  original=eh*nh+ej*nj+crossenergy
  target=X*B+m1/4*(X**-2+2*X-3)+(a*a*m2/m1)/4*(X-1)**2
  check('symbolic_spectral_cross_identity',sp.factor(fs*a+s2*es)==0)
  check('symbolic_all_covariance_energy',sp.factor(original-target)==0)
  ax=target-X*B
  check('symbolic_strict_convexity',sp.simplify(sp.diff(ax,X,2)-(3*m1/(2*X**4)+a*a*m2/(2*m1)))==0)
  check('small_energy_second_order',sp.simplify(sp.diff(ax,X,2).subs(X,1)-(3*m1+a*a*m2/m1)/2)==0)
  check('symbolic_quartic',sp.expand((2*sp.diff(target,X)*X**3)-(a*a*m2/m1*X**4+(2*B+m1-a*a*m2/m1)*X**3-m1))==0)
  # Physical Q/P Hamiltonian derivation independent of h,j variables.
  D=sp.symbols('D',positive=True)
  delta=B+m1/4*(X**-2-1)+D/4*(X**2-1)+(X-1)*(B+(m1-D)/2)
  check('symbolic_physical_covariance_energy',sp.expand(delta-(X*B+m1/4*(X**-2+2*X-3)+D/4*(X-1)**2))==0)
 return ck
FAULTS=['inverse_squeeze','omit_vacuum_cost','drop_cross_energy','presqueeze','changed_signal']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 base=controls(symbolic=True);assert all(base.values()),('BASELINE FAIL',[k for k,v in base.items() if not v]);faults={}
 for f in FAULTS:
  failed=[k for k,v in controls(f).items() if not v];assert failed,('UNDETECTED',f);faults[f]=failed
 cert=certificate();assert F('4.4289859434858')<F(cert['energy_lower'])<=F(cert['energy_upper'])<F('4.4289859434859');deps=['explorations/conditional-build/k2158-local-squeezing-detector-energy-2026-10-27.md','explorations/conditional-build/k2153-diagonal-detector-energy-2026-10-27.md','explorations/conditional-build/k2156-energy-budget-detector-frontier-2026-10-27.md']
 report=dict(result_id='K2158',status='conditional_exact_controls',exact_checks=base,fault_failures=faults,rational_certificate=cert,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Companion note proves countable-instrument finite energy, monotone scalar optimization and exact frontier transport; finite unitary fixture verifies ordering/effects only. No all-local optimality or apparatus cost.')
 p=ROOT/'lab/process/k2158-local-squeezing-detector-energy.json'
 if args.write:p.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(p.read_text())==report,'stored report differs'
 print(json.dumps({'result':'K2158','exact_checks':len(base),'faults':faults,'optimum_interval':[float(F(cert['energy_lower'])),float(F(cert['energy_upper']))]}))
if __name__=='__main__':main()
