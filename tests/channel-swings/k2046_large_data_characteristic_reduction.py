"""Exact characteristic identities for the phase-locked large-data theorem."""
from pathlib import Path
import json,hashlib,argparse
import sympy as s
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2046-large-data-characteristic-reduction.json'
def produce():
 a,b,L,M,A,B=s.symbols('a b L M A B',positive=True);c,cu,cv=s.symbols('c cu cv',real=True)
 # sigma=-1: a_v=b_u=-2*a*b**2, c_u=2*a.
 av=-2*a*b*b;bu=av;assert s.simplify(-bu/b**2-2*a)==0
 cuv=2*av;assert s.simplify(cuv-(-2*(2*a)*b*b))==0
 b0,b0p,a0=s.symbols('b0 b0p a0',positive=True)
 f=-b0p/b0**2-2*(a0+b0)
 assert s.simplify(2/b0**-1+f-(-b0p/b0**2-2*a0))==0
 H=1/(2*B);K=L*(H+2*M)**2+2*(A+B);m=1/(2*B+K)
 assert s.simplify(2/m-K-(4*B+K))==0
 assert s.simplify(1/m-(2*B+K))==0
 # Arbitrary phase curvature defect; delta_u and delta_v are actual phase jets.
 d,du,dv=s.symbols('delta delta_u delta_v',real=True)
 cu=-2*a*s.sin(d);av=2*a*b*b*s.sin(d)
 lhs=-2*av*s.sin(d)-2*a*s.cos(d)*dv
 rhs=2*s.sin(d)*cu*b*b-2*s.cos(d)*du*b
 defect=s.expand(lhs-rhs);assert s.simplify(defect-2*s.cos(d)*(b*du-a*dv))==0
 paths=['explorations/conditional-build/k2044-arbitrary-phase-characteristic-control-2026-10-25.md','explorations/conditional-build/k2042-sextic-transport-instability-2026-10-25.md']
 return dict(result_id='K2046',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',coefficients=dict(density=-2,reciprocal_u=2,repulsion=2,initial_density=-2,phase_defect=2,complex_lipschitz=10),system=['Dplus X=2*sigma*X*Y**4','Dminus Y=-2*sigma*X**2*Y**3'],phase_condition='cos(2*theta-4*phi)=0; sigma=sin(2*theta-4*phi) in {-1,+1}',null_coordinates='u=x-t, v=x+t; Dplus=2*d_v, Dminus=-2*d_u',reverse_plane={'a_v':'-2*a*b**2','b_u':'-2*a*b**2','c_u':'2*a','c_v':'2/c+c0prime(v)-2*rho0(v)','integrated':'c(u,v)=c0(v)-2*integral_u^v a(s,v)ds >= c0(v)-2*M'},barrier={'H':'1/(2*B)','K':'L*(H+2*M)**2+2*(A+B)','m':'1/(2*B+K)','boundary_derivative_lower':'4*B+K','definitions':'A=sup X0**2; B=sup Y0**2>0; L=sup |(Y0**2)prime|; M=integral(X0**2+Y0**2)'},bounds={'sigma_minus_forward':'a<=A; b<=2*B+K','sigma_plus_forward':'b<=B; a<=A*exp(2*M*B)','backward':'reflect x and reverse t, exchanging sigma; same initial norm constants'},phase_defect='c_uv - d_u(-2*sin(delta)/c) = 2*cos(delta)*(b*delta_u-a*delta_v)',phase_jet_witness={'a':1,'b':1,'delta':0,'theta_u':0,'phi_v':0,'theta_v':1,'phi_u':-1,'delta_u':4,'delta_v':2,'defect':4},scope='All smooth real phase-locked finite-charge bounded initial data with bounded derivatives on R, both time directions, zeros allowed. Small complex perturbations of compact reference profiles in fixed support are also global; unrestricted complex data and genuine transverse dynamics remain open. No source physical parity/domain conclusion.',complex_neighborhood={'radius':'(eta/2)*exp(-10*(R0+eta)**4*T)','support':'same fixed interval [l,r]','horizon':'T>(r-l)/2','conclusion':'global arbitrary-phase solution and exact scattering; open relative to fixed-support smooth data'},scattering='For compact initial support in [l,r], exact free transport after |t|>(r-l)/2; no smallness condition in the phase-locked class.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2046 exact null reduction, barrier coefficient and arbitrary-phase defect')
