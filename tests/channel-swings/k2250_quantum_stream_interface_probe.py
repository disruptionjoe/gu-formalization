#!/usr/bin/env python3
"""Exact spin injection, fermionic transfer blocks and thermal replacement controls."""
import sympy as s
from fractions import Fraction as F
FAULTS=['wrong_double_sector','refresh_spent_bath','ordinary_swap','omit_Q','omit_output_order','bath_gradient']
def tau(p):return s.diag(1-p,p)
def trbath(A,ds):
    db=A.rows//ds
    return s.Matrix(ds,ds,lambda i,j:sum(A[i*db+b,j*db+b] for b in range(db)))
def trsys(A,ds):
    db=A.rows//ds
    return s.Matrix(db,db,lambda i,j:sum(A[a*db+i,a*db+j] for a in range(ds)))
def gamma(U):
    n=U.rows;states=[[j for j in range(n) if k&(1<<(n-1-j))] for k in range(2**n)]
    return s.Matrix(2**n,2**n,lambda i,j:0 if len(states[i])!=len(states[j]) else (1 if not states[i] else U.extract(states[i],states[j]).det()))
def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    p=s.Rational(1,5);c=s.Rational(3,5);t=s.Rational(4,5);plus=s.ones(2)/2
    U=s.Matrix([[1,0,0,0],[0,c,-s.I*t,0],[0,-s.I*t,c,0],[0,0,0,-1 if fault=='wrong_double_sector' else 1]])
    first=U*s.kronecker_product(plus,tau(p))*U.conjugate().T
    bath=trsys(first,2)
    ck('bath_population',bath[1,1]==s.Rational(49,125))
    ck('bath_coherence',bath[1,0]==-s.I*s.Rational(6,25))
    if fault=='refresh_spent_bath':bath=tau(p)
    second=trbath(U*s.kronecker_product(plus,bath)*U.conjugate().T,2)
    ck('coherent_second_population',second[1,1]==s.Rational(1973,6250))
    diagonal=s.Rational(2693,6250)
    ck('coherent_cross_term',second[1,1]-diagonal==-s.Rational(72,625))
    for q1,q2 in [(0,1),(p,p),(s.Rational(1,2),s.Rational(1,2))]:
        x=U*s.kronecker_product(tau(q1),tau(p))*U.conjugate().T
        y=trbath(U*s.kronecker_product(tau(q2),trsys(x,2))*U.conjugate().T,2)
        expected=c*c*q2+t*t*(c*c*p+t*t*q1)
        ck('diagonal_retained_'+str((q1,q2)),y[1,1]==expected)
    P=s.Matrix([[0,1],[1,0]]);G=gamma(P)
    swap=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
    if fault=='ordinary_swap':G=swap
    ck('fermion_swap_double_phase',G[3,3]==-1)
    ck('fermion_swap_CZ_relation',G*s.diag(1,1,1,-1)==swap)
    # Rational unitary step on endpoint plus two bath modes.
    R01=s.Matrix([[c,-t,0],[t,c,0],[0,0,1]])
    R12=s.Matrix([[1,0,0],[0,c,-t],[0,t,c]])
    V=R01*R12;ck('one_particle_unitary',V.T*V==s.eye(3))
    Q=s.diag(0,1,1) if fault!='omit_Q' else s.eye(3)
    ff=[(V*(Q*V)**j)[0,0] for j in range(3)]
    ck('renewal_first',ff[0]==V[0,0])
    ck('renewal_second',ff[1]==(V*V)[0,0]-V[0,0]**2)
    W=s.eye(4);idx=[0,2,3]
    for i in range(3):
        for j in range(3):W[idx[i],idx[j]]=V[i,j]
    PP=s.eye(4);PP.row_swap(0,1)
    circuit=(PP if fault!='omit_output_order' else s.eye(4))*W*PP*W
    D=circuit[:2,:2];expected=s.Matrix([[ff[0],0],[ff[1],ff[0]]])
    ck('two_output_triangular_transfer',D==expected)
    ck('full_circuit_unitary',circuit.T*circuit==s.eye(4))
    ck('transfer_Frobenius_weight',(D.T*D).trace()==2*ff[0]**2+ff[1]**2)
    # Full fermionic transfer on four modes: exact replacement on every input matrix unit.
    S=s.zeros(4)
    for j in range(2):S[j,j+2]=S[j+2,j]=1
    GS=gamma(S);bt=s.kronecker_product(tau(p),tau(s.Rational(2,5) if fault=='bath_gradient' else p))
    wanted=s.kronecker_product(tau(p),tau(p))
    ck('full_transfer_unitary',GS.T*GS==s.eye(16))
    for i in range(4):
        for j in range(4):
            X=s.zeros(4);X[i,j]=1
            Y=trbath(GS*s.kronecker_product(X,bt)*GS.T,4)
            ck('full_transfer_matrix_unit_'+str((i,j)),Y==(wanted if i==j else s.zeros(4)))
    # Rational resource inequalities bound the analytic consumer; no sampled Bessel proof.
    ck('factorial_base',F(3)*F(3,10)**10<F(1,10000))
    ck('joint_main_bound',F(22,7)*F(10,7)*10/10000<F(45,10000))
    ck('sqrt_two_upper_bound',F(10,7)**2>2)
    ck('sqrt_ten_upper_bound',F(19,6)**2>10)
    ck('finite_tail_coefficient',2*F(22,7)*10*F(19,6)<200)
    ck('reservoir_energy',3*2000000*F(1,5)==1200000)
    return out

RESULT='K2250'
REPORT='lab/process/k2250-quantum-stream-interface.json'
DEPS=['explorations/conditional-build/k2250-quantum-stream-interface-2026-10-29.md', 'explorations/conditional-build/k2249-finite-density-chain-reset-2026-10-29.md']
EVIDENCE="Finite exact algebra/arithmetic controls and actual input faults; universal results are written proofs, not established by finite controls. Hash checks are reporting integrity."

def main():
    import argparse,hashlib,json
    from pathlib import Path
    args=argparse.ArgumentParser();args.add_argument('--write',action='store_true');a=args.parse_args()
    root=Path(__file__).resolve().parents[2]
    checks=controls();assert all(checks.values()),[k for k,v in checks.items() if not v]
    faults={}
    for fault in FAULTS:
        bad=[k for k,v in controls(fault).items() if not v]
        assert bad,('undetected mathematical input fault',fault)
        faults[fault]=bad
    report=dict(result_id=RESULT,checks=checks,fault_failures=faults,evidence_kinds=EVIDENCE,
        dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in DEPS},
        probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    p=root/REPORT
    if a.write:p.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(p.read_text())==report,'certificate drift'
    print(json.dumps(dict(result=RESULT,controls=len(checks),faults=len(faults))))
if __name__=='__main__':main()
