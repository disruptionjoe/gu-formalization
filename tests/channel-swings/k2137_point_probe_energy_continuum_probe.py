"""Symbolic resource controls; numerical integrals are sanity evidence only."""
from pathlib import Path
import argparse,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def compute(fault=None):
 R=s.Rational;I=s.I
 t,a,w=s.symbols('t a w',positive=True,real=True)
 actual=s.integrate(t/a*s.exp(I*w*t),(t,0,a))+s.integrate((2*a-t)/a*s.exp(I*w*t),(t,a,2*a))
 expected=-(s.exp(I*w*a)-1)**2/(a*w**2)
 if fault=='pulse_normalization':expected*=2
 checks={'triangular_Fourier_transform':s.simplify(actual-expected)==0,
 'triangle_area':s.integrate(t/a,(t,0,a))+s.integrate((2*a-t)/a,(t,a,2*a))==a,
 'triangle_phase_bound':s.integrate((t/a)**2,(t,0,a))+s.integrate(((2*a-t)/a)**2,(t,a,2*a))+a*2==8*a/3}
 k,L,lam=s.symbols('k L lam',positive=True);m=s.symbols('m',positive=True)
 fbound=lam**2/(4*s.pi*k**3)
 checks['rectangle_displacement_tail']=s.integrate(2*4*fbound,(k,L,s.oo))==lam**2/(s.pi*L**2)
 checks['rectangle_energy_tail']=s.integrate(2*4*k*fbound,(k,L,s.oo))==2*lam**2/(s.pi*L)
 power=5 if fault!='wrong_triangle_UV_power' else 3
 tri=4*lam**2/(s.pi*a*a*k**power)
 checks['triangle_norm_tail']=s.integrate(2*tri,(k,L,s.oo))==2*lam**2/(s.pi*a*a*L**4)
 checks['triangle_energy_tail']=s.integrate(2*k*tri,(k,L,s.oo))==8*lam**2/(3*s.pi*a*a*L**3)
 checks['triangle_second_tail']=s.integrate(2*k*k*tri,(k,L,s.oo))==4*lam**2/(s.pi*a*a*L**2)
 x=s.symbols('x',real=True);poly=x*x/2-x**4/24
 checks['rectangle_lower_polynomial']=poly.subs(x,1)==R(11,24) and s.diff(poly,x)==x-x**3/6 and 1-R(2,6)>0
 checks['triangle_sinc_lower']=1-R(2,16)/6==R(47,48)
 # Point form integral and triangle global M2 bound from exact antiderivatives.
 anti=s.atan(k/m)/m;checks['point_form_antiderivative']=s.simplify(s.diff(anti,k)-1/(k*k+m*m))==0
 checks['point_energy_shift']=s.simplify(lam**2/(4*s.pi)*(s.pi/m)-lam**2/(4*m))==0
 anti3=k/(m*m*s.sqrt(k*k+m*m))
 checks['triangle_global_second_moment']=s.simplify(s.diff(anti3,k)-(k*k+m*m)**(-R(3,2)))==0 and s.simplify(4*lam**2/(s.pi*a*a)*(2/m**2)-8*lam**2/(s.pi*a*a*m*m))==0
 # Finite NUMBER GENERATOR action only; not a truncated approximation to a Weyl operator.
 creation=s.zeros(4)
 for j in range(3):creation[j+1,j]=s.sqrt(j+1)
 Q=creation-creation.T;V=s.eye(4)[:,:2];gram=(Q*V).T*(Q*V)
 if fault=='wrong_code_generator_constant':bound=2
 else:bound=3
 checks['code_generator_bound']=gram==s.diag(1,3) and bound>=max(gram.eigenvals())
 # Independent two-mode coherent Poisson energy moment generating function.
 b,r1,r2,w1,w2=s.symbols('b r1 r2 w1 w2',positive=True)
 generating=s.exp(r1*(s.exp(b*w1)-1)+r2*(s.exp(b*w2)-1))
 if fault=='drop_energy_variance':generating=s.exp(b*(r1*w1+r2*w2))
 mean=r1*w1+r2*w2;second=s.diff(generating,b,2).subs(b,0)
 checks['coherent_second_moment']=s.expand(second-mean**2)==r1*w1**2+r2*w2**2
 return {k:bool(v) for k,v in checks.items()}
def report():
 c=compute();assert all(c.values()),c;faults={}
 for f in ['pulse_normalization','wrong_triangle_UV_power','wrong_code_generator_constant','drop_energy_variance']:
  bad=[k for k,v in compute(f).items() if not v];assert bad,f;faults[f]=bad
 return {'schema_version':'1.0','status':'conditional_symbolic_resource_controls','exact_checks':c,'fault_failures':faults,'evidence_kind':'Exact Fourier integration, tail majorant antiderivatives, polynomial bounds and low-number generator action. Universal bounds/domain/causality are written proofs, not samples.','probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
def main():
 a=argparse.ArgumentParser();a.add_argument('--write',action='store_true');args=a.parse_args();d=report();p=ROOT/'lab/process/k2137-point-probe-energy-continuum.json'
 if args.write:p.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(p.read_text())==d,'stored evidence differs'
 print('PASS',len(d['exact_checks']),'symbolic controls;',len(d['fault_failures']),'equation/input faults')
if __name__=='__main__':main()
