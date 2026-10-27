from pathlib import Path
import json,argparse,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
OUT='k2143-local-canonical-parity.json'
DEPS=['explorations/conditional-build/k2139-finite-weyl-record-obstruction-2026-10-27.md','explorations/conditional-build/k2140-point-sites-blind-sectors-2026-10-27.md']
EVIDENCE='Exact two-frequency symplectic/Bogoliubov/energy controls and finite recorded-channel identities. Continuum local CCR implementability, strict vacuum response and finite-energy transfer use independently reviewed written proofs.'
FAULTS=['reflection_normalization','beta_sum','omit_energy_cross','wrong_readout','global_mode_substitution']
def compute(fault=None):
 I=s.I;f=s.Matrix([s.Rational(3,5),s.Rational(4,5)]);W=s.diag(1,4);Wh=s.diag(1,2);Wi=s.diag(1,s.Rational(1,2));P=f*f.T
 R=s.eye(2)-(1 if fault=='reflection_normalization' else 2)*P
 if fault=='global_mode_substitution':R=-s.eye(2)
 alpha=(Wh*R*Wi+Wi*R*Wh)/2
 beta=(Wh*R*Wi+(1 if fault=='beta_sum' else -1)*Wi*R*Wh)/2
 A=(f.T*W*f)[0];B=(f.T*W.inv()*f)[0];C=(f.T*W*W*f)[0]
 u=Wh*f;v=Wi*f;betaf=v*u.T-u*v.T
 energy=s.trace(W*beta*beta.T)
 expected=B*C+(A if fault=='omit_energy_cross' else -A)
 cov=s.diag(B/2,A/2);sv=1/s.sqrt(A*B);odd=(1-sv)/2
 # Exact finite instrument: first tensor factor is a reference, second the tested mode.
 # V=I_reference tensor Z; the test state is entangled. Universal identity is proved in the note.
 V=s.diag(1,-1,1,-1);eye=s.eye(4);Kp=(eye+V)/2;Km=(eye-V)/2
 if fault=='wrong_readout':Kp=eye/s.sqrt(2);Km=V/s.sqrt(2)
 ket=s.Matrix([1,I,2,-I])/s.sqrt(7);rho=ket*ket.conjugate().T
 out=Kp*rho*Kp.conjugate().T+Km*rho*Km.conjugate().T
 H=s.diag(0,3);vac=s.Matrix([1,0]);VV=s.Matrix([[s.Rational(3,5),s.Rational(4,5)],[s.Rational(4,5),-s.Rational(3,5)]]);EV=(vac.T*VV*H*VV*vac)[0];pp=(s.eye(2)+VV)/2;pm=(s.eye(2)-VV)/2
 branch=[(vac.T*K*H*K*vac)[0] for K in [pp,pm]]
 f0=s.Matrix([1,0]);R0=s.eye(2)-2*f0*f0.T
 beta0=(Wh*R0*Wi-Wi*R0*Wh)/2
 A0=(f0.T*W*f0)[0];B0=(f0.T*W.inv()*f0)[0]
 checks={
 'canonical_reflection':R*R==s.eye(2) and R.T==R and R*f==-f,
 'native_single_mode_reflection':R==s.eye(2)-2*P,
 'bogoliubov_CCR':alpha*alpha.T-beta*beta.T==s.eye(2) and alpha*beta.T==beta*alpha.T,
 'rank_two_pair_creation':beta==betaf and beta.rank()==2,
 'exact_free_energy':energy==expected,
 'particle_number':s.trace(beta*beta.T)==2*(A*B-1),
 'vacuum_covariance':s.simplify(1/(2*s.sqrt(cov.det()))-sv)==0,
 'strict_vacuum_baseline':A*B>1 and odd>0,
 'spectral_mode_countercontrol':beta0==s.zeros(2) and A0*B0==1 and s.trace(W*beta0*beta0.T)==0,
 'recorded_projectors':Kp*Kp==Kp and Km*Km==Km and Kp*Km==s.zeros(4),
 'unread_channel':s.simplify(out-(rho+V*rho*V)/2)==s.zeros(4),
 'branch_energy_without_cross_terms':branch==[EV/4,EV/4],
 'intraregional_commutator':R[0,1]==-2*f[0]*f[1] and R[0,1]!=0,
 'ordinary_free_dynamics_not_commuting':W*R!=R*W,
 'bounded_unread_signal':s.simplify(s.exp(I*s.pi*s.Rational(25,24)*R[0,1])-1)==-2 and s.Matrix([1,0]).dot(s.Matrix([0,1]))==0,
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
