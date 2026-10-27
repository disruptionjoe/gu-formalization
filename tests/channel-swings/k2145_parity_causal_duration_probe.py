from pathlib import Path
import json,argparse,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]

ID='K2145';OUT='k2145-parity-causal-duration.json'
DEPS=['explorations/conditional-build/k2143-local-canonical-parity-2026-10-27.md']
EVIDENCE='Exact finite symplectic reflection, Weyl-phase, energy-exponent, Givens and complete-record matrix controls. Causal duration/channel norms and continuum energy follow the independently reviewed written argument, not matrix extrapolation.'
FAULTS=['reflection-factor','signal-half','energy-factor','gate-inverse','record-cross']
def compute(fault=None):
 f=s.Matrix([s.Rational(3,5),s.Rational(4,5),0]);h=s.Matrix([1,0,0]);g=s.Matrix([0,1,0]);factor=1 if fault=='reflection-factor' else 2;R=s.eye(3)-factor*f*f.T
 a=(f.T*h)[0];b=(f.T*g)[0];rg=R*g
 ck={'unit_normalization':(f.T*f)[0]==1,'canonical_reflection':R*R==s.eye(3),'disjoint_source_receiver':(h.T*g)[0]==0,'exact_transmitted_phase':(h.T*rg)[0]==-2*a*b}
 theta=s.symbols('theta',real=True);signal=(s.exp(-2*s.I*theta)-1)/(1 if fault=='signal-half' else 2)
 ck['weyl_signal_modulus']=s.simplify(s.expand_complex(signal*s.conjugate(signal))-s.sin(theta)**2)==0
 E,Q,c,aa,bb=s.symbols('E Q c a b',positive=True);lam=s.sqrt((1 if fault=='energy-factor' else 2)*E/Q);t=s.pi/(2*lam*aa*bb)
 ck['finite_energy_budget']=s.simplify(lam**2*Q/2-E)==0
 ck['error_exponent_32']=s.simplify(t*t*c/4-s.pi**2*c*Q/(32*E*aa**2*bb**2))==0
 # Explicit adjacent rotations whose first row is a normalized real mode vector.
 G12=s.Matrix([[s.Rational(3,5),s.Rational(4,5),0],[-s.Rational(4,5),s.Rational(3,5),0],[0,0,1]])
 G23=s.Matrix([[1,0,0],[0,s.Rational(5,13),s.Rational(12,13)],[0,-s.Rational(12,13),s.Rational(5,13)]])
 O=G12*G23;f3=O[0,:].T;D=s.diag(-1,1,1)
 assembled=(O if fault=='gate-inverse' else O.T)*D*O
 ck['adjacent_givens_exact_mode']=O*O.T==s.eye(3) and f3==s.Matrix([s.Rational(3,5),s.Rational(4,13),s.Rational(48,65)])
 ck['gather_parity_undo']=assembled==s.eye(3)-2*f3*f3.T
 # Exact instrument with reference, not only the unread channel.
 V=s.Matrix([[0,1],[1,0]]);I=s.eye(2);P=(I+V)/2;M=(I-V)/2
 if fault=='record-cross':M=(I+V)/2
 psi=s.Matrix([1,0,0,1])/s.sqrt(2);rho=psi*psi.T
 branch=lambda K:s.kronecker_product(K,I)*rho*s.kronecker_product(K.T,I)
 plus,minus=branch(P),branch(M)
 ck['record_completeness']=P.T*P+M.T*M==I and P*M==s.zeros(2)
 ck['full_record_reference_trace']=s.trace(plus)+s.trace(minus)==1 and plus!=minus and s.trace(plus)==s.Rational(1,2)
 ck['unread_reference_channel']=plus+minus==(rho+s.kronecker_product(V,I)*rho*s.kronecker_product(V,I))/2
 return {k:bool(v) for k,v in ck.items()}

def main():
 ck=compute();assert all(ck.values()),ck
 failures={}
 for f in FAULTS:
  failures[f]=[k for k,v in compute(f).items() if not v]
  assert failures[f],('FAULT UNDETECTED',f)
 report={'result_id':ID,'status':'conditional_exact_controls','exact_checks':ck,'fault_failures':failures,'universal_evidence':EVIDENCE,'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependency_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in DEPS}}
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();out=ROOT/'lab/process'/OUT
 if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(out.read_text())==report,'stored evidence differs'
 print(json.dumps({'result':ID,'checks':len(ck),'faults':len(failures),'failures':failures,'pass':True}))
if __name__=='__main__':main()
