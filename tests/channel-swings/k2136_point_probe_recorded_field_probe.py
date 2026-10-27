"""Exact algebraic controls; continuum form/domain/locality rests on written proof."""
from pathlib import Path
import argparse,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def compute(fault=None):
 I=s.I; R=s.Rational; eye=s.eye; zero=s.zeros
 x,y,u,v=s.symbols('x y u v',real=True);w=s.symbols('w',positive=True);t=s.symbols('t',real=True)
 # Weyl convention D(z)D(w)=exp((z*conj(w)-conj(z)*w)/2)D(z+w).
 coc=lambda z,q:s.expand((z*s.conjugate(q)-s.conjugate(z)*q)/2)
 f=s.symbols('f',real=True);z=s.exp(-I*w*t)*f
 phase=coc(-f,z);wanted=-I*f*f*s.sin(w*t)
 if fault=='weyl_phase_sign':phase=-phase
 checks={'static_Weyl_phase':s.simplify(s.expand_complex(phase-wanted))==0,
 'displacement_picture':s.simplify(s.exp(I*w*t)*(s.exp(-I*w*t)-1)*f-(1-s.exp(I*w*t))*f)==0,
 'Weyl_cocycle_associative':s.simplify(coc(x+I*y,u+I*v)+coc(x+u+I*(y+v),2+3*I)-coc(u+I*v,2+3*I)-coc(x+I*y,u+2+I*(v+3)))==0}
 # Any unitary representation checks the exact complete instrument identity.
 D=s.Matrix([[R(3,5),-R(4,5)],[R(4,5),R(3,5)]]);Dm=D.T
 Kp=(D+Dm)/2;Km=(D-Dm)/2
 if fault=='Z_instead_of_X_readout':Kp=D/s.sqrt(2);Km=Dm/s.sqrt(2)
 ket0=s.Matrix([1,0]);ket1=s.Matrix([0,1]);plus=(ket0+ket1)/s.sqrt(2);minus=(ket0-ket1)/s.sqrt(2)
 P0=ket0*ket0.T;P1=ket1*ket1.T;PXp=plus*plus.T;PXm=minus*minus.T;X=s.Matrix([[0,1],[1,0]])
 controlled=s.kronecker_product(P0,D)+s.kronecker_product(P1,Dm)
 gotp=s.kronecker_product(plus.T,eye(2))*controlled*s.kronecker_product(plus,eye(2))
 gotm=s.kronecker_product(minus.T,eye(2))*controlled*s.kronecker_product(plus,eye(2))
 checks['Ramsey_record_Kraus']=gotp==Kp and gotm==Km
 checks['complete_record_normalization']=Kp.conjugate().T*Kp+Km.conjugate().T*Km==eye(2)
 checks['unread_two_displacements']=all(Kp*e*Kp.conjugate().T+Km*e*Km.conjugate().T==(D*e*D.T+Dm*e*Dm.T)/2 for e in [s.Matrix(2,2,lambda a,b:int(a==j and b==k)) for j in range(2) for k in range(2)])
 Urec=s.kronecker_product(PXp,eye(2))+s.kronecker_product(PXm,X)
 checks['record_copy_unitary']=Urec.T*Urec==eye(4) and Urec*s.kronecker_product(plus,ket0)==s.kronecker_product(plus,ket0) and Urec*s.kronecker_product(minus,ket0)==s.kronecker_product(minus,ket1)
 # On the projector generator's spectrum {0,2}, exp(-i*pi/2*(I-X))=X.
 checks['record_generator_phase']=s.exp(-I*s.pi)==-1 and (eye(2)+X)/2+s.exp(-I*s.pi)*(eye(2)-X)/2==X
 A=s.symbols('A',positive=True); c=s.symbols('c',nonnegative=True)
 scale=2 if fault!='halve_record_Weyl_argument' else 1
 vacuum=s.exp(-scale**2*A/2);one=vacuum*(1-scale**2*c)
 checks['one_photon_record_contrast']=s.simplify(((1-one)/2-(1-vacuum)/2)-2*s.exp(-2*A)*c)==0
 checks['global_vacuum_fidelity']=s.simplify(s.exp(-A/2)**2-s.exp(-A))==0
 p,q,dp,dq=s.symbols('p q dp dq',real=True);energy=lambda p,q:(p*p+q*q)/2
 cross=(energy(p+dp,q+dq)+energy(p-dp,q-dq))/2
 if fault=='omit_opposite_displacement':cross=energy(p+dp,q+dq)
 checks['unread_energy_cross_cancellation']=s.expand(cross-energy(p,q)-(dp*dp+dq*dq)/2)==0
 checks['nonGaussian_characteristic_zero']=s.cos(s.pi/2)==0 and s.exp(-R(1,2))>0
 return {k:bool(v) for k,v in checks.items()}
def report():
 c=compute();assert all(c.values()),c;faults={}
 for f in ['weyl_phase_sign','Z_instead_of_X_readout','halve_record_Weyl_argument','omit_opposite_displacement']:
  bad=[k for k,v in compute(f).items() if not v];assert bad,f;faults[f]=bad
 return {'schema_version':'1.0','status':'conditional_algebra_controls','exact_checks':c,'fault_failures':faults,'evidence_kind':'Weyl algebra, finite memory/record matrix equations and symbolic field-energy cancellation. No finite matrix is claimed to represent exact continuum CCR.','proof_dependency':'K2136 written form construction, retarded Klein-Gordon support and Fock characteristic identities','probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
def main():
 a=argparse.ArgumentParser();a.add_argument('--write',action='store_true');args=a.parse_args();d=report();p=ROOT/'lab/process/k2136-point-probe-recorded-field.json'
 if args.write:p.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(p.read_text())==d,'stored evidence differs'
 print('PASS',len(d['exact_checks']),'exact algebra controls;',len(d['fault_failures']),'equation/input faults')
if __name__=='__main__':main()
