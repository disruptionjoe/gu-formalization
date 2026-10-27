from pathlib import Path
import json,argparse,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
OUT='k2142-finite-time-real-control.json'
DEPS=['explorations/conditional-build/k2136-point-probe-recorded-field-2026-10-27.md','explorations/conditional-build/k2140-point-sites-blind-sectors-2026-10-27.md']
EVIDENCE='Finite exact angular/real-adjoint/moment/Gaussian-resource controls. Infinite-dimensional real density, factorial ill-conditioning, finite propagation and energy-domain transfer are independently reviewed written proofs, not finite sampling.'
FAULTS=['coincident_sites','imaginary_adjoint','moment_corruption','taylor_factorial','phase_slope','record_probability']
def compute(fault=None):
 I=s.I;th=s.symbols('th',real=True);x=s.symbols('x',real=True);d,E,eh=s.symbols('d E eh',positive=True)
 S=s.Matrix([[1,1],[s.exp(-I*th),s.exp(I*th)]])
 if fault=='coincident_sites':S[1,0]=1;S[1,1]=1
 det=s.simplify(s.expand_complex(S.det()))
 # Genuine real adjoint: complex output, real input and real Hilbert pairing.
 A=s.Matrix([[1+I,2-I],[-I,1+2*I]]);u=s.Matrix([2+3*I,-1+I]);v=s.Matrix([3,-2])
 au=A.conjugate().T*u;adj=au.applyfunc(s.im if fault=='imaginary_adjoint' else s.re)
 left=s.re((u.conjugate().T*A*v)[0]);right=(adj.T*v)[0]
 freq=[1,2,3,4];weights=s.Matrix([-1,3,-3,1]);
 if fault=='moment_corruption':weights[0]=1
 moments=[sum(weights[j]*freq[j]**n for j in range(4)) for n in range(4)]
 NN=s.symbols('NN',integer=True,positive=True);aa=s.symbols('aa',positive=True)
 ratio=s.simplify((s.factorial(NN+1)/aa**(NN+1))/(s.factorial(NN)/aa**NN))
 N=4;poly=sum((I*x)**j/s.factorial(j) for j in range(N));rem=(I*x)**N/(s.factorial(N-1) if fault=='taylor_factorial' else s.factorial(N))
 deriv=s.diff(poly+rem,x,N).subs(x,0)
 # Normalized Gaussian characteristic derivative: Hermite energy n=1,2.
 phi=s.exp(-x*x/2)/s.sqrt(2*s.pi)
 h1=x;h2=(x*x-1)/s.sqrt(2)
 herm=[s.integrate(s.diff(h,x)**2*phi,(x,-s.oo,s.oo)) for h in [h1,h2]]
 slope=s.pi/(d if fault=='phase_slope' else 2*d)
 prob=s.erf(d/s.sqrt(2));energy=eh*slope**2*prob
 c=s.sqrt(2/s.pi);delta=s.pi**2*c*eh/(4*E)
 lower=s.simplify(s.Rational(1,2)-c*delta/2)
 p=s.Rational(3,4);q=p/(1 if fault=='record_probability' else 2)
 # Minimax of identical actual record laws against ideal probabilities0,p.
 error=max(q,abs(p-q));
 checks={
 'two_site_determinant':s.simplify(det-2*I*s.sin(th))==0,
 'separated_site_full_rank':S.subs(th,s.pi/2).rank()==2,
 'coincident_site_countercontrol':s.Matrix([[1,1],[1,1]]).rank()==1,
 'real_adjoint_pairing':left==right,
 'complex_real_distinction':s.im(au[1])!=0 and left!=s.re((u.T*A*v)[0]),
 'annihilated_first_three_moments':moments[:3]==[0,0,0],
 'first_remaining_moment':moments[3]==6,
 'real_taylor_coefficient':deriv==I**N,
 'gaussian_dirichlet_hermite_controls':herm==[1,2],
 'clipped_phase_energy_coefficient':s.simplify(energy-eh*s.pi**2*prob/(4*d*d))==0,
 'resource_substitution':s.simplify(lower-(s.Rational(1,2)-s.pi*eh/(4*E)))==0,
 'identical_record_minimax':error==p/2,
 'factorial_successive_term_ratio':s.simplify(ratio-(NN+1)/aa)==0,
 }
 return {k:bool(v) for k,v in checks.items()}

def main():
 checks=compute();assert all(checks.values()),checks
 failures={}
 for fault in FAULTS:
  bad=[k for k,v in compute(fault).items() if not v]
  assert bad,('FAULT NOT DETECTED',fault)
  failures[fault]=bad
 report={'schema_version':'1.0','status':'conditional_exact_controls','exact_checks':checks,'fault_failures':failures,'universal_evidence':EVIDENCE,'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependency_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in DEPS}}
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();p=ROOT/'lab/process'/OUT
 if a.write:p.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(p.read_text())==report,'stored evidence mismatch'
 print(json.dumps({'checks':len(checks),'faults':len(failures),'fault_failures':failures}))
if __name__=='__main__':main()
