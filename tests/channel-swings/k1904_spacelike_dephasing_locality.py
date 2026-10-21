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
    N=0;C,H=target();q=s.sqrt(2);delta=6-4*q
    I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1)
    Rs=[s.eye(4),s.kronecker_product(s.diag(1,s.I),I),s.kronecker_product(I,Z),s.kronecker_product(s.diag(1,-1),s.diag(1,-s.I))]
    psi=s.Matrix([1,0,0,1])/q
    for j in range(4):
        mat(adj(Rs[j])*Rs[j],s.eye(4),'unitary relative branch')
        for k in range(j):mat(Rs[j]*Rs[k],Rs[k]*Rs[j],'cross commutation')
    D=s.Matrix(4,4,lambda j,k:(adj(psi)*adj(Rs[k])*Rs[j]*psi)[0])
    phases=[s.Matrix([R[a,a] for R in Rs]) for a in [0,3]]
    mixture=sum((z*adj(z)/2 for z in phases),s.zeros(4))
    mat(D,mixture,'entangled bath joint spectral measure')
    eq(s.trace(H*C),0,'target witness');check(s.simplify(s.trace(H*D)-delta)>0,'classical control witness')
    # Ordered shared-memory signal, Alice and Bob are logical encoded qubits.
    P0=s.diag(1,0);P1=s.diag(0,1)
    WA=s.kronecker_product(P0,I,I)+s.kronecker_product(P1,I,Z)
    WB=s.kronecker_product(I,P0,I)+s.kronecker_product(I,P1,X)
    plus=s.Matrix([1,1])/q;XB=s.kronecker_product(I,X,I)
    obs=[]
    for a in [s.Matrix([1,0]),s.Matrix([0,1])]:
        state=WB*WA*s.kronecker_product(a,plus,plus)
        obs.append(s.simplify((adj(state)*XB*state)[0]))
    check(obs==[1,-1],'ordered common-memory perfect signal')
    check(WA*WB!=WB*WA,'noncommuting joint operations')
    off=sum(abs(H[j,k]) for j in range(4) for k in range(4) if j!=k)
    eq(off,10*q,'entry error coefficient');eq(2*off,20*q,'commuting-reference distance coefficient')
    return {'classical_delta':str(delta),'commuting_distance_floor':str(s.simplify(delta/(20*q))),'signal_expectations':[int(x) for x in obs],'entangled_control_witness':str(s.simplify(s.trace(H*D))),'math_checks':N}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write-report',action='store_true');args=ap.parse_args()
    result=calculate();result['dependency_sha256']=pin('explorations/conditional-build/k1903-quantum-dephasing-witness-2026-10-21.md')
    if args.write_report:(ROOT/'lab/process/k1904-spacelike-dephasing-locality.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
