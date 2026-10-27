"""Exact Gaussian-integral and full-record controls, no truncated-Fock certification."""
from pathlib import Path
import json,hashlib,argparse
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
DEPS=['lab/process/k2143-local-canonical-parity.json','lab/process/k2146-fixed-support-parity-ultraviolet.json','explorations/conditional-build/k2133-recorded-instrument-vacuum-disturbance-2026-10-27.md']
FAULTS=['gaussian_factor','missing_v_overlap','wrong_s_weight','global_parity','moving_square','record_only']
def eq(A,B):return all(s.simplify(v)==0 for v in A-B) if isinstance(A,s.MatrixBase) else s.simplify(A-B)==0
def compute(fault=None):
 W=s.diag(1,9,4);f=s.Matrix([1,1,0])/s.sqrt(2);R=s.eye(3)-2*f*f.T;M=W+R*W*R
 a1=(f.T*W*f)[0];am=(f.T*W.inv()*f)[0];u=W**s.Rational(1,2)*f/s.sqrt(a1);v=W**s.Rational(-1,2)*f/s.sqrt(am);ss=1/s.sqrt(a1*am)
 sg=s.sqrt(2**3*W.det()/M.det());B=u*u.T+(0 if fault=='missing_v_overlap' else 1)*v*v.T
 integral=(1 if fault=='gaussian_factor' else 2)*sg*W**s.Rational(1,2)*M.inv()*R*W**s.Rational(1,2)
 formula=ss*s.eye(3)-B if fault=='wrong_s_weight' else ss*(s.eye(3)-B)
 if fault=='global_parity':formula=-s.eye(3)
 ck={'vacuum_gaussian_integral':eq(sg,ss) and ss==s.Rational(3,5),'independent_one_particle_integral':eq(integral,formula),'known_matrix_control':eq(integral,s.Matrix([[0,-s.Rational(9,25),0],[-s.Rational(9,25),0,0],[0,0,s.Rational(3,5)]])),'overlap_gram':eq((u.T*v)[0],ss)}
 hp=(u+v)/s.sqrt(2*(1+ss));hm=(u-v)/s.sqrt(2*(1-ss));odd=lambda h:s.simplify((1-(s.conjugate(h).T*formula*h)[0])/2)
 ck['moving_optimal_record']=eq(odd(hp),(1+(ss if fault=='moving_square' else ss**2))/2) and eq(odd(hp),s.Rational(17,25))
 ck['antisymmetric_signal']=eq(odd(hm),s.Rational(8,25));ck['spectator_signal']=eq(odd(s.Matrix([0,0,1])),s.Rational(1,5));ck['complex_signal']=eq(odd(s.Matrix([1,s.I,0])/s.sqrt(2)),s.Rational(1,2))
 a2=(f.T*W**2*f)[0];eng=(a2/a1+1/am+2*ss*a1)/(2*(1+ss))
 ck['moving_signal_energy']=eq((hp.T*W*hp)[0],eng)
 # Equal-frequency control is ordinary occupied-mode parity with a dark vacuum.
 W0=4*s.eye(3);M0=W0+R*W0*R;G0=2*W0**s.Rational(1,2)*M0.inv()*R*W0**s.Rational(1,2)
 ck['equal_frequency_mode']=eq(G0,R) and eq((f.T*G0*f)[0],-1)
 # Explicit entangled system/reference state; output includes both record blocks.
 psi=s.Matrix([s.sqrt(3)/2,0,0,s.Rational(1,2)]);rho=psi*psi.T;Pp=s.diag(1,1,0,0);Pm=s.eye(4)-Pp
 diff=s.diag(Pp*rho*Pp-rho,Pm*rho*Pm);norm=sum(abs(ev)*mult for ev,mult in diff.eigenvals().items())/2
 q=s.Rational(1,4);F=q if fault=='record_only' else (s.sqrt(4*q-3*q*q)+q)/2
 ck['reference_full_record_distance']=eq(norm,F) and eq(norm,(1+s.sqrt(13))/8)
 # Second nonbalanced profile checks formula independent of symmetric special case.
 f2=s.Matrix([s.Rational(3,5),s.Rational(4,5),0]);R2=s.eye(3)-2*f2*f2.T;M2=W+R2*W*R2;a=(f2.T*W*f2)[0];c=(f2.T*W.inv()*f2)[0];sg2=s.sqrt(8*W.det()/M2.det());u2=W**s.Rational(1,2)*f2/s.sqrt(a);v2=W**s.Rational(-1,2)*f2/s.sqrt(c)
 ck['nonbalanced_independent_integral']=eq(2*sg2*W**s.Rational(1,2)*M2.inv()*R2*W**s.Rational(1,2),sg2*(s.eye(3)-u2*u2.T-v2*v2.T))
 return {k:bool(v) for k,v in ck.items()}
def main():
 ck=compute();assert all(ck.values()),ck
 faults={f:[k for k,v in compute(f).items() if not v] for f in FAULTS};assert all(faults.values()),faults
 out={'result_id':'K2148','status':'conditional_exact_controls','exact_checks':ck,'fault_failures':faults,'dependency_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in DEPS},'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'universal_evidence':'Written characteristic-function, Fourier weak-convergence and fixed-code proof independently internally reviewed; finite exact Gaussian and record controls are not a continuum certificate.'}
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();p=ROOT/'lab/process/k2148-fixed-signal-parity-response.json'
 if args.write:p.write_text(json.dumps(out,indent=2)+'\n')
 else:assert json.loads(p.read_text())==out
 print(json.dumps({'result':'K2148','checks':len(ck),'faults':faults,'pass':True}))
if __name__=='__main__':main()
