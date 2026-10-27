"""Exact energy-form constants, asymptotic coefficients and occupation controls."""
from pathlib import Path
import json,hashlib,argparse
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
DEPS=['lab/process/k2146-fixed-support-parity-ultraviolet.json','lab/process/k2148-fixed-signal-parity-response.json']
FAULTS=['omit_creation_constant','wrong_cross_sign','wrong_inverse_moment','wrong_inverse_root','record_only']
def eq(a,b):return s.simplify(a-b)==0
def compute(fault=None):
 W=s.diag(1,9);f=s.Matrix([1,1])/s.sqrt(2);nu=s.Rational(4)
 h=(s.sqrt(nu)*W**s.Rational(-1,2)+W**s.Rational(1,2)/s.sqrt(nu))*f/2
 j=(s.sqrt(nu)*W**s.Rational(-1,2)-W**s.Rational(1,2)/s.sqrt(nu))*f/2
 moment=lambda n:(f.T*W**n*f)[0]
 A=(nu*moment(-2)+2*moment(-1)+1/nu)/4;C=(nu*moment(-2)+(-1 if fault!='wrong_cross_sign' else 1)*2*moment(-1)+1/nu)/4;D=(nu*moment(-1)+moment(1)/nu-2)/4
 if fault=='omit_creation_constant':D=0
 ck={'canonical_CCR':eq((h.T*h-j.T*j)[0],1),'annihilation_energy_constant':eq((h.T*W.inv()*h)[0],A),'creation_energy_constant':eq((j.T*W.inv()*j)[0],C),'creation_vacuum_constant':eq((j.T*j)[0],D),'positive_difference':eq(A-C,moment(-1)) and A>C>=0}
 # Finite Fock test: cutoff3 contains every output from the 0/1 input subspace.
 a=s.zeros(3);a[0,1]=1;a[1,2]=s.sqrt(2);I=s.eye(3);aa=[s.kronecker_product(a,I),s.kronecker_product(I,a)]
 b=sum((h[i]*aa[i]+j[i]*aa[i].T for i in range(2)),s.zeros(9));H=aa[0].T*aa[0]+9*aa[1].T*aa[1]
 vac=s.eye(9)[:,0];single=s.eye(9)[:,3];psi=(vac+single)/s.sqrt(2);E=(psi.T*H*psi)[0];actual=(psi.T*b.T*b*psi)[0]
 bound=(s.sqrt(E*A)+s.sqrt(E*C+D))**2
 ck['actual_fock_energy_bound']=bool(s.simplify(bound-actual)>=0);ck['vacuum_creation_accounting']=eq((vac.T*b.T*b*vac)[0],D)
 # Exact asymptotic integration coefficients in q, using even moment functional.
 t,q,m,mu2=s.symbols('t q m mu2',real=True);series=s.series(1/((1/t+q)**2+m*m),t,0,6).removeO().expand();avg=lambda p:s.expand(p).subs(q**3,0).subs(q,0) # explicit coefficient below
 c4=s.expand(series).coeff(t,4);expected=(2 if fault=='wrong_inverse_moment' else 3)*q*q-m*m
 ck['inverse_moment_coefficient']=eq(c4,expected)
 am1=t+(mu2-m*m/2)*t**3;am2=t*t+(3*mu2-m*m)*t**4;a1=1/t+m*m*t/2
 AA=s.expand((am2/t+2*am1+t)/4);CC=s.expand((am2/t-2*am1+t)/4);DD=s.expand((am1/t+a1*t-2)/4)
 ck['three_resource_coefficients']=eq(AA,t+(5*mu2-2*m*m)*t**3/4) and eq(CC,mu2*t**3/4) and eq(DD,mu2*t*t/4)
 # Invert at an exact nontrivial point A=4,C=1,D=3,E=1 gives q=16.
 # Use rescaled constants so q remains a probability: A=1/4,C=1/16,D=3/16,E=1 =>q=1.
 av,cv,dv,qv=s.Rational(1,4),s.Rational(1,16),s.Rational(3,16),s.Integer(1)
 inv=((qv-dv)/(s.sqrt(av*qv)+(-1 if fault=='wrong_inverse_root' else 1)*s.sqrt(cv*qv+(av-cv)*dv)))**2
 ck['exact_inverse_envelope']=eq(inv,1) and eq((s.sqrt(av*inv)+s.sqrt(cv*inv+dv))**2,qv)
 # Frequency eigenmode: input sqrt(1-q)|0>+sqrt(q)|1>, E=qK, parity q.
 qv=s.Rational(1,4);freq=s.Integer(7);state=s.Matrix([s.sqrt(3)/2,s.Rational(1,2)]);N=s.diag(0,1)
 pv=s.Rational(1,5);ph=s.Rational(17,25);qtarget=s.Rational(1,2);mix=(qtarget-pv)/(ph-pv)
 ck['exact_mixed_record_target']=0<mix<1 and eq(mix*ph+(1-mix)*pv,qtarget) and mix==s.Rational(5,8)
 ck['eigenmode_linear_energy_threshold']=eq((state.T*(freq*N)*state)[0],qv*freq)
 F=qv if fault=='record_only' else (s.sqrt(4*qv-3*qv*qv)+qv)/2
 plus=s.diag(1,0);minus=s.diag(0,1);rho=state*state.T;diff=s.diag(plus*rho*plus-rho,minus*rho*minus)
 actual=sum(abs(v)*n for v,n in diff.eigenvals().items())/2
 ck['full_record_eigenmode_distance']=eq(F,actual)
 return {k:bool(v) for k,v in ck.items()}
def main():
 ck=compute();assert all(ck.values()),ck
 faults={f:[k for k,v in compute(f).items() if not v] for f in FAULTS};assert all(faults.values()),faults
 out={'result_id':'K2149','status':'conditional_exact_controls','exact_checks':ck,'fault_failures':faults,'dependency_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in DEPS},'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'universal_evidence':'Energy-form/CCR proof and controlled Fourier asymptotics separately internally reviewed; finite oscillator calculations and symbolic coefficients are controls, not continuum proof or optimality certificate.'}
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();p=ROOT/'lab/process/k2149-energy-bounded-parity-limit.json'
 if args.write:p.write_text(json.dumps(out,indent=2)+'\n')
 else:assert json.loads(p.read_text())==out
 print(json.dumps({'result':'K2149','checks':len(ck),'faults':faults,'pass':True}))
if __name__=='__main__':main()
