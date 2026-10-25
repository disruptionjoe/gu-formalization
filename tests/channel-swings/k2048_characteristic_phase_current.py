"""Symbolic characteristic current and amplitude identities, no PDE sampling."""
from pathlib import Path
import json,hashlib,argparse
import sympy as s
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2048-characteristic-phase-current.json'
def produce():
 x,y,h,k,f,g,p,q,r,t=s.symbols('x y h k f g p q r t',real=True)
 z=x+s.I*y;zu=h+s.I*k;F=f+s.I*g;Fp=p+s.I*q;G=r+s.I*t
 zv=s.I*s.conjugate(z)*F
 zuv=s.I*s.conjugate(zu)*F+s.conjugate(z)*z**2*Fp*G
 a=s.expand(z*s.conjugate(z));jv=s.im(s.expand(s.conjugate(zv)*zu+s.conjugate(z)*zuv))
 assert s.expand(jv-a*a*s.im(Fp*G))==0
 lam=s.symbols('lambda',real=True)
 matched=s.I*s.conjugate(zu)*F+lam*a*z*Fp*s.conjugate(Fp)
 au=2*s.re(s.conjugate(z)*zu);av=2*s.re(s.conjugate(z)*zv);J=s.im(s.conjugate(z)*zu)
 auv=2*s.re(s.conjugate(zu)*zv+s.conjugate(z)*matched)
 assert s.expand(a*auv-au*av-4*J*s.re(z*z*s.conjugate(F))-2*lam*a**3*Fp*s.conjugate(Fp))==0
 # The actual quartic-in-w coupling uses G=conj(F')/4.
 w=p+s.I*q;F=w**4;Fp=4*w**3;G=s.conjugate(w)**3
 zv=s.I*s.conjugate(z)*F;zuv=s.I*s.conjugate(zu)*F+s.conjugate(z)*z*z*Fp*G
 assert s.expand(s.im(s.conjugate(zv)*zu+s.conjugate(z)*zuv))==0
 au=2*s.re(s.conjugate(z)*zu);av=2*s.re(s.conjugate(z)*zv);J=s.im(s.conjugate(z)*zu)
 auv=2*s.re(s.conjugate(zu)*zv+s.conjugate(z)*zuv);b=s.expand(w*s.conjugate(w));C=z*z*s.conjugate(w)**4
 assert s.expand(a*auv-au*av-4*J*s.re(C)-8*a**3*b**3)==0
 # Polynomial coefficient classification: a_j*b_k = conjugate(a_k*b_j).
 aj,ak,lam=s.symbols('aj ak lam',real=True);assert s.expand(aj*(lam*ak)-ak*(lam*aj))==0
 paths=['explorations/conditional-build/k2046-large-data-characteristic-reduction-2026-10-25.md','explorations/conditional-build/k2044-arbitrary-phase-characteristic-control-2026-10-25.md']
 return dict(result_id='K2048',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',coefficients={'general_defect':1,'amplitude_current':4,'amplitude_positive':8,'initial_interaction':-1,'general_amplitude':2},current='J=Im(conj(z)*z_u); J_v=0',system=['z_v=i*conj(z)*w**4','w_u=-i*z**2*conj(w)**3'],initial_data='J(u)=Im(conj(z0)*z0prime)-Re(z0**2*conj(w0)**4)',amplitude_identity='a*a_uv-a_u*a_v=4*J*Re(z**2*conj(w)**4)+8*a**3*b**3',polynomial_class={'system':'z_v=i*conj(z)*F(w), w_u=-i*z**2*G(conj(w))','defect':'J_v=|z|**4*Im(Fprime(w)*G(conj(w)))','classification':'If F is nonconstant, identity J_v=0 for every local solution iff G(conj(w))=lambda*conj(Fprime(w)), lambda real. Constant F permits any G.','scope':'polynomials with constant complex coefficients; not a norm-preserving classification','amplitude':'a*a_uv-a_u*a_v=4*J*Re(z**2*conj(F))+2*lambda*a**3*abs(Fprime)**2','conditional_gain':'For F(0)=Fprime(0)=0 and a globally smooth compact solution with J=0, d_u log(aout/ain)=2*lambda*integral a*abs(Fprime)**2 dv; sign follows lambda.'},scattering='For every globally smooth compactly supported solution, Im(conj(Zout)*Zoutprime)=Im(conj(Zin)*Zinprime)=J pointwise at fixed right characteristic label.',scope='Exact local complex PDE identities and necessary scattering constraints; no unrestricted global existence, complete integrability, source physical parity or quantum scattering conclusion.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2048 exact general current defect, sextic current and amplitude identity')
