"""Exact finite controls; the note's polar/Choi proof carries universal scope."""
from pathlib import Path
import argparse, hashlib, json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def calculate(phase=-1, leakage_factor=1):
    nchecks=0
    def check(x,label):
        nonlocal nchecks
        assert bool(x),label
        nchecks+=1
    def eq(a,b,label):check(s.simplify(s.expand_complex(a-b))==0,label)
    a=1/s.sqrt(2); I=s.I
    V=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[a,-a],[a,a]]),s.Matrix([[a,phase*I*a],[phase*I*a,a]])]
    C=s.Matrix(4,4,lambda j,k:(V[k].H*V[j])[0,0]);eq(C[2,3],(1+I)/2,'target orientation')
    B=s.Matrix([[-1,-1,s.sqrt(2),0],[-1,I,0,s.sqrt(2)]]);H=B.H*B
    eq(s.trace(H*C),0,'target zero');h=4+s.sqrt(2);delta=6-4*s.sqrt(2)
    check(set(H.eigenvals())=={0,4-s.sqrt(2),h},'positive witness spectrum')
    co=s.Rational(99,101);si=s.Rational(20,101);q=s.Rational(1,10)
    S=s.eye(4);S[:2,:2]=s.Matrix([[co,-si],[si,co]])
    U=s.kronecker_product(S,s.eye(2))*s.diag(*V)
    check(s.simplify(U.H*U)==s.eye(8),'joint unitary')
    rho=s.diag(1-q,q);A=[U[2*j:2*j+2,2*j:2*j+2] for j in range(4)]
    ell=[s.simplify(1-s.trace(rho*x.H*x)) for x in A]
    check(ell==[leakage_factor*si**2]*2+[0,0],'actual population leakage')
    polar=[s.simplify(s.trace(rho*(A[j]-V[j]).H*(A[j]-V[j]))) for j in range(4)]
    check(all(polar[j]<=ell[j] for j in range(4)),'weighted polar contraction')
    R=[sum((B[l,j]*A[j] for j in range(4)),s.zeros(2)) for l in range(2)]
    WA=s.simplify(sum(s.trace(rho*r.H*r) for r in R))
    DA=s.Matrix(4,4,lambda j,k:s.trace(rho*A[k].H*A[j]))
    eq(WA,s.trace(H*DA),'residual Gram identity')
    # Reconstruct normalized Choi from the actual joint U and mixed rho.
    J=s.zeros(16)
    for b,p in enumerate([1-q,q]):
        for out in range(2):
            K=s.Matrix(4,4,lambda j,k:U[2*j+out,2*k+b])*s.sqrt(p)
            vec=s.Matrix([K[j,k] for j in range(4) for k in range(4)])
            J+=vec*vec.H/4
    Q=s.zeros(16,4)
    for j in range(4):Q[5*j,j]=1
    check(s.simplify(Q.H*J*Q-DA/4)==s.zeros(4),'actual Choi compression')
    eq(s.trace(J),1,'Choi trace');eq(s.trace(Q*H*Q.H*J),WA/4,'positive Choi effect')
    # Noncommuting bath state: positivity polynomial of polar residual bound.
    rho_nc=s.Matrix([[s.Rational(1,2),s.Rational(1,5)],[s.Rational(1,5),s.Rational(1,2)]])
    P=s.diag(s.Rational(1,3),s.Rational(2,3))
    check(P*rho_nc!=rho_nc*P,'noncommuting planted control')
    eq(s.trace(rho_nc*(s.eye(2)-P*P))-s.trace(rho_nc*(s.eye(2)-P)**2),s.Rational(4,9),'noncommuting polar slack')
    floor=s.simplify(2*q*delta/(16*h));check(floor>0,'faithful full-channel floor');check(floor<q,'constructive thermal upper comparison')
    # Positive-effect range bound uses h, not 2h; pure endpoint is not excluded.
    eq((2*s.sqrt(floor))**2,2*q*delta/(4*h),'diamond tradeoff inversion')
    return {'dimension':4,'witness_norm':str(h),'tracial_gap':str(delta),'mean_leakage':str(sum(ell)/4),'choi_witness':str(WA/4),'robust_half_diamond_floor':'d*lambda_min(rho)*(6-4*sqrt(2))/(16*(4+sqrt(2)))','gibbs_floor':'exp(-beta*Delta)*(6-4*sqrt(2))/(16*(4+sqrt(2)))','sharpness':'not claimed','math_checks':nchecks}
def pins():
    names=['explorations/conditional-build/k1912-faithful-bath-dephasing-boundary-2026-10-21.md']
    return {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in names}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write-report',action='store_true');a=ap.parse_args();r=calculate();r['dependency_sha256']=pins()
    if a.write_report:(ROOT/'lab/process/k1913-leakage-robust-bath-bound.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r))
