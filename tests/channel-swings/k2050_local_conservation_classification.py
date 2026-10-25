"""Symbolic local-density census and derivative-current identity."""
from pathlib import Path
import sympy as s
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2050-local-conservation-classification.json'
z,Z,w,W=s.symbols('z Z w W');vars=(z,Z,w,W)
def census(degree,F,lam):
 fb=F.subs(w,W);fp=s.diff(F,w);fbp=s.diff(fb,W)
 mons=[a**i*b**j for a,b in [(z,Z),(w,W)] for i in range(degree+1) for j in range(degree+1-i)]
 cols=[]
 for ix,m in enumerate(mons):
  expr=Z*F*s.diff(m,z)-z*fb*s.diff(m,Z) if ix<len(mons)//2 else lam*(z*z*fbp*s.diff(m,w)-Z*Z*fp*s.diff(m,W))
  cols.append(s.Poly(s.expand(expr),*vars).as_dict())
 rows=sorted(set().union(*(set(c) for c in cols)));A=s.Matrix([[c.get(row,0) for c in cols] for row in rows]);return len(mons),len(mons)-A.rank()
def produce():
 cases=[]
 for degree in [2,4,6]:
  n,dim=census(degree,w**4,s.Rational(1,4));assert dim==3;cases.append(dict(degree=degree,F='w**4',lambda_value='1/4',unknowns=n,nullity=dim))
 for F,lam,label,expected in [((w-2)**3,s.Rational(2,3),'(w-2)**3',3),(w**4+w**2,s.Rational(1,4),'w**4+w**2',2),(w**2+1,s.Rational(1,2),'w**2+1',2),(w,s.Rational(-2),'w',3)]:
  n,dim=census(4,F,lam);assert dim==expected;cases.append(dict(degree=4,F=label,lambda_value=str(lam),unknowns=n,nullity=dim))
 # Formal conjugate variables; free w_v, conjugate(w_v) are independent.
 v,V=s.symbols('v V');I=s.I
 wu=-I*z*z*W**3;Wu=I*Z*Z*w**3;zv=I*Z*w**4;Zv=-I*z*W**4
 wuv=s.expand(-I*(2*z*zv*W**3+3*z*z*W**2*V));Wuv=s.expand(I*(2*Z*Zv*w**3+3*Z*Z*w**2*v))
 Ku=s.expand((Wu*v+W*wuv-wu*V-w*Wuv)/(2*I))
 Pv=s.expand((2*z*zv*W**4+4*z*z*W**3*V+2*Z*Zv*w**4+4*Z*Z*w**3*v)/2)
 assert s.expand(Ku+Pv/2)==0
 # Arbitrary-degree pure powers obey weighted charge balance and exact bad-sign orbit.
 for n in range(1,9):
  lam=s.Rational(2,7);b=1/(lam*n);expr=Z*w**n*Z-z*W**n*z+lam*(z*z*n*W**(n-1)*b*W-Z*Z*n*w**(n-1)*b*w);assert s.expand(expr)==0
 a,b,gamma,m=s.symbols('a b gamma m',positive=True)
 bu=-2*gamma*a*b**m;av=-2*a*b**m
 assert s.simplify((1-m)*b**(-m)*bu-2*gamma*(m-1)*a)==0
 assert s.expand(2*gamma*(m-1)*av-2*(m-1)*bu)==0
 rr=s.symbols('rr',positive=True);phase=(1+s.I)/s.sqrt(2)
 for n in range(1,9):
  zz=phase*rr;ww=rr;lam=-s.Rational(1,n)
  assert s.simplify(2*s.I*s.conjugate(zz)*ww**n-phase*2*rr**(n+1))==0
  assert s.simplify(2*s.I*lam*n*zz**2*s.conjugate(ww)**(n-1)-2*rr**(n+1))==0
 x=s.symbols('x',real=True);phi=(1-x*x)**3;mass=s.integrate(2*phi**2,(x,-1,1));assert mass>0
 refs=['explorations/conditional-build/k2048-characteristic-phase-current-2026-10-25.md','explorations/conditional-build/k2046-large-data-characteristic-reduction-2026-10-25.md']
 return dict(result_id='K2050',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',census=cases,coefficients={'weighted_density_numerator':1,'derivative_current_potential':'1/2','blowup_rate':2,'blowup_denominator_factor':2,'concentration_width_power':2,'reciprocal_factor':2,'repulsion_factor':2},theorem='For nonconstant complex polynomial F and real nonzero lambda, an autonomous real C2 field-only conservation law is nonconstant iff F=A*(w-w0)**n. Modulo constants its density is |z|**2+|w-w0|**2/(lambda*n), and flux is the difference. Positive definite iff lambda>0.',positive_even_power_theorem='F=w**(2*m),lambda>0: all bounded smooth finite weighted-charge phase-plane data with bounded derivatives are globally complete both ways, including zeros; fixed-support complex neighborhoods also scatter.',actual_sextic='F=w**4,lambda=1/4: only mass and its flux modulo constants.',derivative_law='K_u+(Re(z**2*conj(w)**4))_v/2=0, K=Im(conj(w)*w_v)',bad_sign_control='F=w**n,lambda=-1/n: z=exp(i*pi/4)*r,w=r,r=(r0**(-n)-2*n*t)**(-1/n). Changed system, not a blowup of the actual positive coupling.',concentration='z=exp(i*pi/4)*A*phi(A**2*x),w=A*phi(A**2*x): fixed mass, J=0 and derivative integral zero, supremum grows as A. No mass/current-only amplitude bound.',polynomial_C2_control_mass=str(mass),inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs},scope='Written proof covers all C2 field-only laws and all nonconstant polynomials; finite exact censuses are controls, not the universal proof. Original arbitrary-phase large-data existence open.')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2050 symbolic seven density censuses, derivative identity and eight power balances')
