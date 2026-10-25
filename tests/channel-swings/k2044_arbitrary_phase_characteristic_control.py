"""Exact identities supporting the written characteristic continuation theorem."""
from pathlib import Path
import json,hashlib,argparse
import sympy as s
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2044-arbitrary-phase-characteristic-control.json'
def produce():
 x,y,u,v=s.symbols('x y u v',real=True);z=x+s.I*y;w=u+s.I*v
 V=s.expand(s.re(z*z*s.conjugate(w)**4));g=[s.diff(V,q) for q in [x,y,u,v]]
 force=[-g[1],g[0],-g[3]/2,g[2]/2]
 expected=[s.re(2*s.I*s.conjugate(z)*w**4),s.im(2*s.I*s.conjugate(z)*w**4),s.re(2*s.I*z*z*s.conjugate(w)**3),s.im(2*s.I*z*z*s.conjugate(w)**3)]
 assert all(s.expand(a-b)==0 for a,b in zip(force,expected))
 da=s.expand(2*x*force[0]+2*y*force[1]);db=s.expand(2*u*force[2]+2*v*force[3]);assert s.expand(da+db)==0
 a=x*x+y*y;b=u*u+v*v;P=s.expand(s.re(z*z*s.conjugate(w)**4));assert s.expand(16*a*a*b**4-da**2-16*P**2)==0
 # Exact algebraic slack for reciprocal bound at maximal allowed charge flux M/2.
 M,B=s.symbols('M B',positive=True);bstar=B/(1-2*M*B)
 assert s.simplify(1/bstar-(1/B-4*M/2))==0
 lam=s.symbols('lambda',positive=True);assert s.simplify((lam**s.Rational(1,2)*B)*(lam**s.Rational(-1,2)*M)-B*M)==0
 path='explorations/conditional-build/k2042-sextic-transport-instability-2026-10-25.md'
 return dict(result_id='K2044',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',potential=str(V),force=list(map(lambda f:str(s.expand(f)),force)),density_source=str(da),opposite_source=str(db),identity='source_a^2+16*Re(z^2*conj(w)^4)^2=16*a^2*b^4',flux_bound='integral opposite density along either characteristic <= M/2',condition='2*M*B < 1; B=||w0||_infinity^2; M=integral(|z0|^2+|w0|^2)',bounds={'w_squared':'B/(1-2*M*B)','z_squared':'A*exp(2*M*B/(1-2*M*B))','A':'||z0||_infinity^2'},directional_conditions={'forward':'sup_y 2*|w0(y)|^2*M_left(y)<1','backward':'sup_y 2*|w0(y)|^2*M_right(y)<1','bound':'B/(1-eta) in each admitted direction'},scaling={'amplitude_exponent':'1/4','mass_exponent':'-1/2','squared_sup_exponent':'1/2'},compact_support='Each component support translates at its own speed. If both initial supports lie in [l,r], interaction vanishes for |t|>(r-l)/2; outgoing and incoming profiles then translate exactly.',scope='Smooth bounded finite-charge data on R (equivalently R x T2 per transverse volume), arbitrary phases, stated smallness; no arbitrary large-data or transverse PDE result. Sufficient condition, not sharp threshold.',inputs={path:hashlib.sha256((ROOT/path).read_bytes()).hexdigest()})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2044 exact polynomial/current/reciprocal/scaling identities')
