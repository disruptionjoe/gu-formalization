"""Exact matrix controls for the analytic support and thermal-bound theorems."""
from pathlib import Path
import argparse
import hashlib
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
N=0

def check(ok,label):
    global N
    assert bool(ok),label
    N+=1

def eq(a,b,label):
    check(s.simplify(s.expand_complex(a-b))==0,label)

def mat(a,b,label):
    check((a-b).applyfunc(s.expand_complex).applyfunc(s.simplify)==s.zeros(*a.shape),label)

def calculate(phase=-1, thermal_sign=1):
    global N
    N=0
    a=1/s.sqrt(2);I=s.I
    U=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[a,-a],[a,a]]),s.Matrix([[a,phase*I*a],[phase*I*a,a]])]
    for u in U:mat(u.conjugate().T*u,s.eye(2),'unitary bath operation')
    C=s.Matrix(4,4,lambda j,k:(U[k].conjugate().T*U[j])[0,0])
    Cp=s.Matrix(4,4,lambda j,k:(U[k].conjugate().T*U[j])[1,1])
    eq(C[2,3],(1+I)/2,'target orientation')
    B=s.Matrix([[-1,-1,s.sqrt(2),0],[-1,I,0,s.sqrt(2)]]);H=B.conjugate().T*B
    eq(s.trace(H*C),0,'target witness zero');eq(s.trace(H*Cp),4,'excited-column witness')
    proj=[U[j][:,0]*U[j][:,0].conjugate().T for j in range(4)]
    coeff=s.Matrix([[s.trace(P),P[0,0]-P[1,1],P[0,1]+P[1,0],I*(P[0,1]-P[1,0])] for P in proj])
    check(coeff.det()!=0,'projectors span Hermitian two: extremality')
    q=s.symbols('q',real=True);rho=s.diag(1-q,thermal_sign*q)
    D=s.Matrix(4,4,lambda j,k:s.trace(rho*U[k].conjugate().T*U[j]))
    mat(D,(1-q)*C+q*Cp,'thermal convex channel identity')
    for j in range(4):eq(D[j,j],1,'population trace normalization')
    R=[sum((B[l,j]*U[j] for j in range(4)),s.zeros(2)) for l in range(2)]
    residual=sum((r.conjugate().T*r for r in R),s.zeros(2))
    eq(s.trace(H*D),s.trace(rho*residual),'nontracial witness identity')
    eq(s.trace(H*D),4*q,'thermal witness')
    eq(sum(abs(H[j,k]) for j in range(4) for k in range(4) if j!=k),10*s.sqrt(2),'offdiagonal error coefficient')
    check(set(H.eigenvals())=={0,4-s.sqrt(2),4+s.sqrt(2)},'witness norm')
    z=s.Matrix([1,1,1,(1-I)/s.sqrt(2)])
    eq((z.conjugate().T*H*z)[0],6-4*s.sqrt(2),'sharp tracial saturation')
    check(max(abs(v) for v in Cp-C)==s.sqrt(2),'thermal max entry error')
    # Mixed nonfaithful spectator: support rank two, dimension four, same channel.
    spectator=s.diag(s.Rational(1,3),s.Rational(2,3));rho4=s.kronecker_product(s.diag(1,0),spectator)
    V=[s.kronecker_product(u,s.eye(2)) for u in U]
    C4=s.Matrix(4,4,lambda j,k:s.trace(rho4*V[k].conjugate().T*V[j]))
    mat(C4,C,'support-saturating mixed bath');check(rho4.rank()==2,'mixed bath support rank')
    check(4==2*rho4.rank(),'exact support dimension saturation')
    margin=s.Rational(1,176000)-s.Rational(1,110)*(s.Rational(1,3300)+s.Rational(1,6400))
    check(margin>0,'finite thermal circuit margin')
    return {'target_rank':2,'support_dimension_condition':'d>=rank(C)*rank(rho)',
            'faithful_finite_exact_realization':False,'tracial_witness_minimum':'6-4*sqrt(2)',
            'thermal_entry_error_floor':'d*lambda_min(rho)*(6-4*sqrt(2))/(10*sqrt(2))',
            'bandwidth_floor':'exp(-beta*Delta)*(6-4*sqrt(2))/(10*sqrt(2))',
            'thermal_repair_witness':'4*q','thermal_nonclassical_sufficient':'q<(6-4*sqrt(2))/4',
            'process_diamond_error':'2*t*q','thirty_cell_trace_distance_margin':str(margin),'math_checks':N}

def pins():
    return {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in [
        'explorations/conditional-build/k1903-quantum-dephasing-witness-2026-10-21.md',
        'explorations/conditional-build/k1909-poisson-phase-classification-2026-10-21.md']}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--write-report',action='store_true');args=parser.parse_args()
    report=calculate();report['dependency_sha256']=pins()
    if args.write_report:(ROOT/'lab/process/k1912-faithful-bath-dephasing-boundary.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))
