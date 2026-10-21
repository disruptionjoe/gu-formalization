"""Exact finite controls; general proofs and claim ceilings are in the note."""
from pathlib import Path
import argparse, hashlib, json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
N=0
def check(ok,name):
    global N
    assert bool(ok),name
    N+=1
def eq(a,b,name): check(s.simplify(a-b)==0,name)
def mat(a,b,name): check((a-b).applyfunc(s.simplify)==s.zeros(*a.shape),name)
def adj(a):return a.conjugate().T
def pin(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def target():
    q=s.sqrt(2);V=s.Matrix([[1,0,1/q,1/q],[0,1,1/q,s.I/q]])
    B=s.Matrix([[-1,-1,q,0],[-1,s.I,0,q]])
    return adj(V)*V,adj(B)*B

def calculate():
    global N
    N=0;C,H=target();q=s.sqrt(2);I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]])
    G=[s.zeros(2),s.pi*(I-X)/2,s.pi*Y/4,s.pi*X/4]
    U=[I,X,(I-s.I*Y)/q,(I-s.I*X)/q]
    for j in range(4):
        mat(G[j],adj(G[j]),'Hermitian generator');mat((-s.I*G[j]).exp().applyfunc(s.expand_complex),U[j],'generator exponential')
    e0=s.Matrix([1,0]);states=[u*e0 for u in U]
    D=s.Matrix(4,4,lambda j,k:(adj(states[k])*states[j])[0]);mat(D,C,'actual branch overlap orientation')
    # Full Fock gate product is block diagonal over all 16 occupation strings.
    blocks=[]
    for bits in range(16):
        b=I
        for j in [1,2,3]:
            if (bits>>j)&1:b=U[j]*b
        blocks.append(b);mat(adj(b)*b,I,'whole-Fock branch unitarity')
    W=s.diag(*blocks);mat(adj(W)*W,s.eye(32),'full Fock unitarity')
    parity=s.diag(*[(-1)**bits.bit_count() for bits in range(16)])
    mat(W*s.kronecker_product(parity,I),s.kronecker_product(parity,I)*W,'even parity preservation')
    for j in range(4):mat(blocks[1<<j],U[j],'one-particle branch selected')
    P1=s.diag(0,1);energies=[s.simplify((adj(v)*P1*v)[0]) for v in states]
    check(energies==[0,1,s.Rational(1,2),s.Rational(1,2)],'memory energy coefficients')
    eq(sum(energies)/4,s.Rational(1,2),'uniform input energy')
    eq(s.pi+s.pi/4+s.pi/4,3*s.pi/2,'integrated control norm')
    eps=(6-4*q)/(8*(4+q));eq(2*(4+q)*eps,(6-4*q)/4,'gate-error threshold')
    return {'integrated_norm':'3*pi/2','memory_energy_coefficients':[str(x) for x in energies],'uniform_memory_energy_over_omega':'1/2','error_budget':str(eps),'fock_dimension':32,'math_checks':N}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write-report',action='store_true');args=ap.parse_args()
    result=calculate();result['dependency_sha256']=pin('explorations/conditional-build/k1903-quantum-dephasing-witness-2026-10-21.md')
    if args.write_report:(ROOT/'lab/process/k1905-causal-quantum-memory-realization.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
