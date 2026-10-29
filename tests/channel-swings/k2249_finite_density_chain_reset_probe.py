#!/usr/bin/env python3
"""Finite-density exact spin matrix-unit channels and actual reinjection memory."""
import sympy as s
from fractions import Fraction as F
FAULTS=['bath_gradient','bath_coherence','phase_conjugation','bosonic_double_sector','erase_spent_bath','wrong_Gibbs_energy','omit_return_projection','transpose_bath_covariance']
def simp(M):return M.applyfunc(s.simplify)
def tau(p):return s.diag(1-p,p)
def ptr0(M):
    d=M.rows//2
    return s.Matrix(2,2,lambda i,j:sum(M[i*d+b,j*d+b] for b in range(d)))
def ptrbath(M):
    d=M.rows//2
    return s.Matrix(d,d,lambda i,j:M[i,j]+M[d+i,d+j])
def wedge(U):
    n=U.rows;states=[[j for j in range(n) if k&(1<<(n-1-j))] for k in range(2**n)]
    return s.Matrix(2**n,2**n,lambda i,j: 0 if len(states[i])!=len(states[j]) else (1 if not states[i] else U.extract(states[i],states[j]).det()))
def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    co=s.Rational(3,5);si=s.Rational(4,5)
    U=s.Matrix([[(1+co)/2,-s.I*si/s.sqrt(2),(co-1)/2],[-s.I*si/s.sqrt(2),co,-s.I*si/s.sqrt(2)],[(co-1)/2,-s.I*si/s.sqrt(2),(1+co)/2]])
    # Exact three-site open-path propagator at cos(sqrt(2)Jt)=3/5.
    phase=(3+4*s.I)/5;U=phase*U;W=simp(wedge(U))
    if fault=='phase_conjugation':W=W.conjugate()
    if fault=='bosonic_double_sector':W[3,3]=-W[3,3]
    ck('one_particle_unitarity',simp(U*U.conjugate().T)==s.eye(3))
    ck('spin_Fock_unitarity',simp(W*W.conjugate().T)==s.eye(8))
    a=U[0,0];rr=s.simplify(a*s.conjugate(a))
    for p in [s.Rational(1,5),s.Rational(1,2),s.Rational(4,5)]:
        tb=tau(p);tb2=tau(p if fault!='bath_gradient' else 1-p)
        if fault=='bath_coherence':tb=tb+s.Matrix([[0,s.Rational(1,10)],[s.Rational(1,10),0]])
        bath=s.kronecker_product(tb,tb2)
        for i in range(2):
            for j in range(2):
                e=s.zeros(2);e[i,j]=1
                actual=simp(ptr0(W*s.kronecker_product(e,bath)*W.conjugate().T))
                T=s.trace(e);D=p*e[0,0]-(1-p)*e[1,1]
                expected=s.Matrix([[(1-p)*T+rr*D,s.conjugate(a)*e[0,1]],[a*e[1,0],p*T-rr*D]])
                ck('complete_matrix_unit_'+str((p,i,j)),actual==expected)
        equilibrium=s.kronecker_product(tau(p),bath)
        ck('product_stationarity_'+str(p),simp(W*equilibrium*W.conjugate().T)==equilibrium)
    p=s.Rational(1,5);q1=s.Rational(2,3);q2=s.Rational(1,7)
    initial=s.kronecker_product(tau(q1),tau(p),tau(p))
    evolved=simp(W*initial*W.conjugate().T);spent=ptrbath(evolved)
    if fault=='erase_spent_bath':spent=s.kronecker_product(tau(p),tau(p))
    second=simp(ptr0(W*s.kronecker_product(tau(q2),spent)*W.conjugate().T))[1,1]
    kap=s.simplify((U*U)[0,0]-a*a)
    expect=s.simplify(p+rr*(q2-p)+(q1-p)*kap*s.conjugate(kap))
    ck('same_chain_two_input_memory',s.simplify(second-expect)==0)
    ck('memory_is_nonzero',s.simplify(expect-p-rr*(q2-p))!=0)
    # Three insertions checked by full 8x8 spin evolution versus projected covariance.
    C=p*s.eye(3)+(q1-p)*s.diag(1,0,0);joint=initial;Q=s.diag(0,1,1)
    for k,q in enumerate([q1,q2,s.Rational(4,7)]):
        if k:
            joint=s.kronecker_product(tau(q),ptrbath(joint))
            C=p*s.eye(3)+(q-p)*s.diag(1,0,0)+Q*(C-p*s.eye(3))*Q
        joint=simp(W*joint*W.conjugate().T);C=simp(U*C*U.conjugate().T)
        ck('finite_sequence_population_'+str(k),s.simplify(ptr0(joint)[1,1]-C[0,0])==0)
    # Renewal identity from actual projected dynamics, not a success flag.
    QQ=s.eye(3) if fault=='omit_return_projection' else Q
    avec=[s.Integer(1)]+[s.simplify((U**k)[0,0]) for k in range(1,7)]
    fvec=[None]+[s.simplify((U*(QQ*U)**(k-1))[0,0]) for k in range(1,7)]
    for k in range(1,7):
        ck('renewal_convolution_'+str(k),s.simplify(avec[k]-sum(fvec[j]*avec[k-j] for j in range(1,k+1)))==0)
    # Exact spectral disk inequality for representative rational unit phases;
    # universal positive-real proof is in the note, not inferred from samples.
    for zz in [s.Rational(1,2),s.I/3,(3+4*s.I)/10]:
        Az=s.simplify((s.eye(3)-zz*U).inv()[0,0]);Fz=s.simplify(zz*(U*(s.eye(3)-zz*QQ*U).inv())[0,0])
        ck('resolvent_renewal_'+str(zz),s.simplify(Fz-(1-1/Az))==0)
        ck('positive_real_resolvent_'+str(zz),s.re(Az)>s.Rational(1,2))
        ck('inverse_resolvent_cap_'+str(zz),s.simplify(Az*s.conjugate(Az))>=s.Rational(1,4))
    ck('uniform_stream_consumer',8*F(4,5)/200**2==F(1,6250))
    # Correlated even bath: matrix-unit contraction checks the covariance convention.
    p=s.Rational(1,5);eps=s.Rational(1,100);bath=s.Matrix(s.kronecker_product(tau(p),tau(p)))
    bath[2,1]+=s.I*eps;bath[1,2]-=s.I*eps
    low=s.Matrix([[0,1],[0,0]]);Z=s.diag(1,-1)
    bs=[s.kronecker_product(low,s.eye(2)),s.kronecker_product(Z,low)]
    Gamma=s.Matrix(2,2,lambda j,k:s.trace(bath*bs[k].conjugate().T*bs[j]))
    if fault=='transpose_bath_covariance':Gamma=Gamma.T
    vv=s.Matrix([s.conjugate(U[0,1]),s.conjugate(U[0,2])])
    explicit=sum(s.conjugate(U[0,j+1])*U[0,k+1]*s.trace(bath*bs[j].conjugate().T*bs[k]) for j in range(2) for k in range(2))
    got=ptr0(W*s.kronecker_product(tau(q2),bath)*W.conjugate().T)[1,1]
    ck('correlated_bath_covariance_index',s.simplify((vv.conjugate().T*Gamma*vv)[0]-explicit)==0)
    ck('correlated_bath_actual_population',s.simplify(got-rr*q2-explicit)==0)
    ck('correlated_bath_positive',min(bath.eigenvals())>0)
    ck('correlated_bath_differs_from_product',s.simplify(explicit-p*(1-rr))!=0)
    ck('finite_stream_factorial_base',F(3)*F(3,10)**10<F(1,10000))
    ck('finite_stream_population_bound',F(4,5)*F(15001,1000000)**2<F(181,1000000))
    ck('finite_stream_bath_energy',3*4000000*F(1,5)==2400000)
    # True coupled Gibbs has offdiagonal one-excitation weight. Choose exp(-beta omega)=1/8 and exp(beta J)=2.
    ej=s.Integer(2) if fault!='wrong_Gibbs_energy' else s.Integer(1)
    off=-s.Rational(1,8)*(ej-1/ej)/2
    ck('coupled_Gibbs_offdiagonal',off==-s.Rational(3,32))
    # Actual 2-site full exchange sends spent first excitation back on second use.
    exchange=s.Matrix([[1,0,0,0],[0,0,-s.I,0],[0,-s.I,0,0],[0,0,0,1]])
    first=exchange*s.kronecker_product(tau(1),tau(p))*exchange.conjugate().T
    back=ptr0(exchange*s.kronecker_product(tau(0),ptrbath(first))*exchange.conjugate().T)
    ck('full_exchange_recall',back==tau(1))
    ck('thermal_window_error',F(1,200)+F(4,5)*F(1,10000)==F(127,25000))
    ck('thermal_endpoint_error',F(1,400)+F(4,5)*F(1,40000)==F(63,25000))
    ck('same_chain_memory_bound',F(4,5)*(F(1,400)+F(1,40000))**2==F(10201,2000000000))
    ck('bath_mean_energy',3*4000*F(1,5)==2400)
    # Positive local-energy Gibbs f'' is positive for x>0, an exact rational function.
    z=s.symbols('z',positive=True);ff=1/(1+z);second=s.factor(z*s.diff(z*s.diff(ff,z),z))
    ck('Fermi_convexity_coefficient',s.simplify(second-z*(z-1)/(1+z)**3)==0)
    return out

RESULT="K2249"
REPORT="lab/process/k2249-finite-density-chain-reset.json"
DEPS=['explorations/conditional-build/k2249-finite-density-chain-reset-2026-10-29.md', 'explorations/conditional-build/k2246-autonomous-vacuum-reservoir-2026-10-29.md', 'explorations/conditional-build/k2235-microscopic-thermal-renewal-2026-10-29.md']
EVIDENCE="Finite exact controls and actual changed-input faults; universal theorem proofs are written mathematics and independently reviewed, not certified by counts."

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
