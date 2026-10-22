"""Finite exact controls for the analytic energy-shell preparation theorem."""
from pathlib import Path
import sympy as s
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2]
def calculate(middle_energy=1,retained_denominator=2):
 labels=[]
 def ck(v,n): assert bool(v),n;labels.append(n)
 def zero(M,n):ck(M.applyfunc(s.simplify)==s.zeros(*M.shape),n)
 r=s.sqrt(2)/2;V=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[r,-r],[r,r]]),s.Matrix([[r,-s.I*r],[-s.I*r,r]])]
 vectors=[v[:,0] for v in V];C=s.Matrix(4,4,lambda i,j:(vectors[j].H*vectors[i])[0]);ck(C.rank()==2,'target rank')
 projs=[v*v.H for v in vectors];ck(s.Matrix.hstack(*[p.reshape(4,1) for p in projs]).rank()==4,'extreme projector span')
 HB=s.diag(0,1,middle_energy,2);U=[s.diag(1,v,1) for v in V];rho=s.diag(0,1,0,0);tau=s.diag(s.Rational(9,16),s.Rational(3,16),s.Rational(3,16),s.Rational(1,16))
 for j,u in enumerate(U):
  zero(u.H*u-s.eye(4),'unitary '+str(j));zero(HB*u-u*HB,'shell conservation '+str(j))
 D=s.Matrix(4,4,lambda i,j:s.trace(rho*U[j].H*U[i]));zero(D-C,'exact excited-shell endpoint')
 Q=s.diag(0,1,0,0);p=s.trace(Q*tau);ck(p==s.Rational(3,16),'Gibbs retained mass');ck(sum(abs(x) for x in (rho-tau).diagonal())/2==1-p,'optimal trace distance')
 # Coherent bath across two two-dimensional shells; no stationarity assumption.
 H2=s.diag(0,0,3,3);W=[s.diag(v,v) for v in V];psi=s.Matrix([s.Rational(3,5),0,s.Rational(4,5),0]);rc=psi*psi.H;rd=s.diag(s.Rational(9,25),0,s.Rational(16,25),0)
 ck(rc*H2!=H2*rc,'genuine energy coherence')
 for state in [rc,rd]:zero(s.Matrix(4,4,lambda i,j:s.trace(state*W[j].H*W[i]))-C,'coherent or pinched exact endpoint')
 # Exact Lucas-product identity over rational Gibbs probabilities.
 for m in range(1,25):
  for q in [s.Rational(1,4),s.Rational(1,2),s.Rational(2,3)]:
   direct=sum((int(s.binomial(m,j))//2)*q**j*(1-q)**(m-j) for j in range(m+1))
   rem=s.prod((1-q)**(2**b)+q**(2**b) for b in range(m.bit_length()) if (m>>b)&1)
   ck(direct==(1-rem)/retained_denominator,f'Lucas mass m{m} q{q}')
   ck(0<=direct<=s.Rational(1,2),'universal resource mass ceiling')
 # Tensor extremality, not inferred just from rank.
 tens=[s.kronecker_product(a,b) for a in vectors for b in vectors]
 ck(s.Matrix.hstack(*[(v*v.H).reshape(16,1) for v in tens]).rank()==16,'two-copy projector span')
 dep=['explorations/conditional-build/k1912-faithful-bath-dephasing-boundary-2026-10-21.md','explorations/conditional-build/k1916-bath-preparation-resource-limits-2026-10-21.md','explorations/conditional-build/k1922-energy-conserving-thermal-channel-floor-2026-10-22.md']
 return dict(result_id='K1923',evidence_kind='analytic theorem and exact finite matrix/combinatorial controls',mathematical_controls=labels,example_mass='3/16',example_distance='13/16',minimum_relative_entropy='-log(sum_e floor(d_e/k)*exp(-beta*E_e)/Z)',scope='exact extreme Schur target, finite product bath, strict additive conservation',dependencies={x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in dep})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=calculate();path=ROOT/'lab/process/k1923-energy-shell-preparation-cost.json'
 if args.write:path.write_text(json.dumps(r,indent=2)+'\n')
 else:assert json.loads(path.read_text())==r,'report consistency'
 print('PASS K1923 exact controls',len(r['mathematical_controls']))
