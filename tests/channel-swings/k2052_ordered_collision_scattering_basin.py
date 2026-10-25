"""Exact real-coordinate identities for the written ordered-overlap theorem."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse
import sympy as s
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2052-ordered-collision-scattering-basin.json'
def produce():
 x,y,p,q=s.symbols('x y p q',real=True);z=x+s.I*y;w=p+s.I*q;a=x*x+y*y;b=p*p+q*q
 records=[]
 for m in [2,3,4]:
  gamma=s.Rational(3,2);zv=s.expand(s.I*s.conjugate(z)*w**(2*m));wu=s.expand(-s.I*gamma*z*z*s.conjugate(w)**(2*m-1))
  av=s.expand(2*s.re(s.conjugate(z)*zv));bu=s.expand(2*s.re(s.conjugate(w)*wu));P=s.expand(s.re(z*z*s.conjugate(w)**(2*m)))
  assert s.expand(bu-gamma*av)==0
  assert s.expand(av*av+4*P*P-4*a*a*b**(2*m))==0
  assert s.expand(s.re(zv)**2+s.im(zv)**2-a*b**(2*m))==0
  assert s.expand(s.re(wu)**2+s.im(wu)**2-gamma**2*a*a*b**(2*m-1))==0
  records.append(dict(m=m,gamma=str(gamma),a_v=str(av),b_u=str(bu)))
 # Differential coefficients, not numerical evolution.
 aa,bb,g=s.symbols('a b gamma',positive=True)
 for m in range(2,9):
  assert s.simplify(s.diff(bb**(1-m),bb)*(2*g*aa*bb**m)+2*g*(m-1)*aa)==0
 for N in [2,3,4]:
  k=F(N);eta=(1-k**(-3))/2
  assert 1-eta>k**(-3)
 inputs=['explorations/conditional-build/k2044-arbitrary-phase-characteristic-control-2026-10-25.md','explorations/conditional-build/k2046-large-data-characteristic-reduction-2026-10-25.md','explorations/conditional-build/k2050-local-conservation-classification-2026-10-25.md']
 return dict(result_id='K2052',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',identity_records=records,coefficients=dict(density_bound=2,reciprocal_factor=2,envelope_exponent=2,null_time_separation=2,w_scattering_gamma_power=2,full_line_tail_factor=2),criterion='2 gamma (m-1) sup_v b0(v)^(m-1) integral_-infinity^v A_k < 1-k^(1-m)',envelope='A_k(u)=a0(u) exp(2 k^m integral_u^infinity b0^m)',m_range='integers m>=2',topology='L2 intersect Linfinity within smooth finite-charge data with bounded derivatives',conclusions=['global future smooth solution','strong L2 outgoing scattering with explicit integral tail bounds','open two-sided scattering neighborhood of every compact reference surviving its finite collision interval','noncompact arbitrary-phase perturbations allowed'],scope='Sufficient ordered criterion only; no unrestricted large complex data, m=1, transverse evolution, source physical quotient or novelty claim.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=produce()
 if args.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2052 symbolic actual-force identities for three powers; seven reciprocal identities; written continuum proof required')
