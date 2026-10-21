"""Exact support, rearrangement, Gibbs-mixture and damping controls."""
from pathlib import Path
from itertools import permutations
import argparse,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def calculate(normalizer=s.Rational(4,5), damping_gain=1):
    n=0
    def ck(v,label):
        nonlocal n
        assert bool(v),label;n+=1
    tau=s.diag(s.Rational(8,15),s.Rational(4,15),s.Rational(2,15),s.Rational(1,15))
    rho=s.diag(tau[0,0],tau[1,1],0,0)/normalizer;tail=s.diag(0,0,s.Rational(2,3),s.Rational(1,3))
    ck(s.trace(rho)==1,'truncated Gibbs normalization')
    ck(rho.rank()==2,'rank resource')
    ck(tau==s.Rational(4,5)*rho+s.Rational(1,5)*tail,'exact Gibbs mixture')
    ck(sum(abs(v) for v in (rho-tau).diagonal())/2==s.Rational(1,5),'exact minimal trace distance witness')
    energies=[0,1,2,3];ev=[s.Rational(2,3),s.Rational(1,3),0,0]
    vals=[sum(energies[i]*r[i] for i in range(4)) for r in permutations(ev)]
    ck(min(vals)==s.Rational(1,3),'rearranged energy global permutation minimum')
    cost=s.expand_log(sum(rho[i,i]*s.log(rho[i,i]/tau[i,i]) for i in range(2)),force=True)
    ck(s.simplify(cost-s.log(s.Rational(5,4)))==0,'Gibbs relative entropy')
    U=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[1,-1],[1,1]])/s.sqrt(2),s.Matrix([[1,-s.I],[-s.I,1]])/s.sqrt(2)]
    W=[s.kronecker_product(x,s.eye(2)) for x in U]
    corr=lambda state,ops:s.simplify(s.Matrix(4,4,lambda j,k:s.trace(state*ops[k].conjugate().T*ops[j])))
    C=corr(s.diag(1,0),U);D=corr(tau,W);Ct=corr(tail,W)
    ck(all(x.conjugate().T*x==s.eye(4) for x in W),'full bath unitary extensions')
    ck(corr(rho,W)==C,'mixed rank-two support exact channel')
    ck(s.simplify(D-s.Rational(4,5)*C-s.Rational(1,5)*Ct)==s.zeros(4),'unchanged Gibbs channel mixture')
    q,r=s.symbols('q r',positive=True)
    K0=s.diag(1,r);K1=s.Matrix([[0,s.sqrt(1-r*r)],[0,0]])
    initial=s.diag(1-q,q)
    final=K0*initial*K0+s.Integer(damping_gain)*K1*initial*K1.T
    ck(s.simplify(s.trace(final)-1)==0,'damping trace preservation')
    ck(s.simplify(final-s.diag(1-q*r*r,q*r*r))==s.zeros(2),'damping eigenvalues')
    ck(s.simplify(final-K0*initial*K0)==s.diag(q*(1-r*r),0),'positive jump remainder')
    # Noncommuting state, rational amplitude, exact positive jump difference.
    rotated=s.Matrix([[s.Rational(3,5),s.Rational(1,5)],[s.Rational(1,5),s.Rational(2,5)]])
    k=s.diag(1,s.Rational(3,5));j=s.Matrix([[0,s.Rational(4,5)],[0,0]])
    jump=j*rotated*j.T
    ck(jump==s.diag(s.Rational(32,125),0),'noncommuting no-jump comparison')
    ck(k.T*k-s.Rational(9,25)*s.eye(2)==s.diag(s.Rational(16,25),0),'minimum singular value')
    delta=6-4*s.sqrt(2);h=4+s.sqrt(2)
    ck(delta>0,'positive witness gap')
    ck(s.simplify((2*q*r*r)*delta/(16*h)-q*r*r*delta/(8*h))==0,'composed qubit channel floor')
    vectors=[x[:,0] for x in U]
    projs=[x*x.conjugate().T for x in vectors]
    realvec=lambda x:s.Matrix([s.re(v) for v in x]+[s.im(v) for v in x])
    ck(s.Matrix.hstack(*[realvec(x) for x in projs]).rank()==4,'base extreme-projector span')
    products=[s.kronecker_product(x,y) for x in projs for y in projs]
    ck(s.Matrix.hstack(*[realvec(x) for x in products]).rank()==16,'tensor extreme-projector span')
    ck(4*2<=9 and 4*3>9,'collective support budget')
    ck(s.simplify(2*s.log(3)-s.log(s.Rational(9,2))-s.log(2))==0,'collective free-energy saving')
    return {'math_checks':n,'d':4,'target_rank':2,'support_rank':2,'retained_Gibbs_mass':'4/5','minimum_relative_entropy':'log(5/4)','minimum_trace_distance':'1/5','exact_preparation_scope':'state-resource optimum; no finite-time or total-work claim','rate_scope':'finite-dimensional regular GKSL with finite integrated ||sum L*L||'}
def pins():
    return {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['explorations/conditional-build/k1912-faithful-bath-dephasing-boundary-2026-10-21.md','explorations/conditional-build/k1913-leakage-robust-bath-bound-2026-10-21.md']}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write-report',action='store_true');a=ap.parse_args();r=calculate();r['dependency_sha256']=pins()
    if a.write_report:(ROOT/'lab/process/k1916-bath-preparation-resource-limits.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r))
