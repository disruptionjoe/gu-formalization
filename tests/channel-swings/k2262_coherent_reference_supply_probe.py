#!/usr/bin/env python3
"""Exact finite SWAP/history, phase-stock, resource and fidelity controls."""
import sympy as s
from fractions import Fraction as F
FAULTS=['omit_swap','unequal_charge_spectra','dephase_donor','correlated_stock','wrong_orbit_power','coherent_record_sum','missing_stock_cell']
def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    I=s.eye(2);plus=s.Matrix([1,1])/s.sqrt(2);beta=plus*plus.H
    W=s.zeros(4)
    for b in range(2):
        for d in range(2):W[2*d+b,2*b+d]=1
    N=s.diag(0,1,1,2) if fault!='unequal_charge_spectra' else s.diag(0,2,1,3)
    ck('swap_unitary',W.H*W==s.eye(4));ck('swap_hermitian',W.H==W);ck('number_conserved',W*N==N*W)
    ck('positive_generator',set((s.eye(4)-W).eigenvals()).issubset({0,2}))
    Pplus=(s.eye(4)+W)/2;Pminus=(s.eye(4)-W)/2
    ck('swap_propagator',Pplus+s.exp(-s.I*s.pi)*Pminus==W)
    # State order B,F,D; B starts maximally entangled with retained history F.
    psi=s.kronecker_product(s.Matrix([1,0,0,1])/s.sqrt(2),plus);rho=psi*psi.H
    if fault=='dephase_donor':rho=s.kronecker_product(s.Matrix([1,0,0,1])*s.Matrix([[1,0,0,1]])/2,I/2)
    U=s.zeros(8)
    for b in range(2):
        for f in range(2):
            for d in range(2):U[4*d+2*f+b,4*b+2*f+d]=1
    if fault=='omit_swap':U=s.eye(8)
    actual=U*rho*U.H
    target=s.zeros(8)
    for b in range(2):
        for bb in range(2):
            for f in range(2):
                for ff in range(2):target[4*b+2*f+f,4*bb+2*ff+ff]=beta[b,bb]/2
    ck('full_history_transfer',actual==target)
    # Fresh mixed stock control: joint independence matters, even with correct marginals.
    clean=s.kronecker_product(s.Matrix([[1,0],[0,0]]),I/2,I/2)
    corr=s.zeros(8);corr[0,0]=corr[3,3]=s.Rational(1,2)
    inp=corr if fault=='correlated_stock' else clean
    outstate=U*inp*U.H
    def bf(state):return s.Matrix(4,4,lambda a,b:sum(state[2*a+d,2*b+d] for d in range(2)))
    ck('fresh_mixed_stock_decouples',bf(outstate)==s.eye(4)/4)
    ck('correlated_countercontrol',bf(U*corr*U.H)!=s.eye(4)/4)
    # Rational unit-circle rotation and exact independent sine-stock overlaps.
    t=(3-4*s.I)/5
    for L in [2,3]:
        probs=[s.simplify(2*s.sin((j+1)*s.pi/(L+1))**2/(L+1)) for j in range(L)]
        ck('sine_normalized_'+str(L),sum(probs)==1)
        mean=sum(j*p for j,p in enumerate(probs));var=s.simplify(sum(p*(j-mean)**2 for j,p in enumerate(probs)))
        ck('sine_mean_'+str(L),mean==s.Rational(L-1,2));ck('sine_variance_'+str(L),var==(s.Rational(1,4) if L==2 else s.Rational(1,2)))
        g=s.simplify(sum(p*t**j for j,p in enumerate(probs)));g2=s.simplify(g*s.conjugate(g))
        for M in [1,2,5,10]:
            power=2*M if fault=='wrong_orbit_power' else M
            d2=1-g2**power
            # Direct tensor probability expansion gives the squared orbit overlap independently.
            polynomial=s.Poly(sum(p*s.Symbol('z')**j for j,p in enumerate(probs))**M,s.Symbol('z'))
            overlap=s.simplify(polynomial.as_expr().subs(s.Symbol('z'),t))
            ck(f'stock_orbit_{L}_{M}',s.simplify(d2-(1-overlap*s.conjugate(overlap)))==0)
            ck(f'bernoulli_orbit_{L}_{M}',s.simplify(1-g2**M)<=M*(1-g2))
            offset=s.simplify(t**17*overlap);ck(f'offset_invariance_{L}_{M}',s.simplify(offset*s.conjugate(offset)-overlap*s.conjugate(overlap))==0)
    p=s.Rational(9,25);r=s.Rational(16,25);a=s.simplify(p*p/(1-r*t*t));b=s.simplify(1-2*p+a)
    fidelity=abs(a+b) if fault=='coherent_record_sum' else abs(a)+abs(b)
    ck('recorded_fidelity',s.simplify(fidelity-(abs(a)+abs(b)))==0)
    # An exact angle with simple root fidelity and two-level-stock overlap.
    half=s.simplify(abs(p*p/(1+r))+abs(1-2*p+p*p/(1+r)))
    stock=s.simplify(abs((1-s.I)/2)**2)
    ck('halfturn_recorded_fidelity',half==s.Rational(449,1025))
    ck('halfturn_stock_overlap',stock==s.Rational(1,2))
    bound=s.simplify(stock*(1-half)**2/8)
    ck('joint_restoration_bound',bound==s.Rational(20736,1050625))
    for M in [1,2,5,100]:
        x=F(100,81*M);drop=F(9,25)*x/(2*(1+x));ck('linear_stock_drop_'+str(M),drop>=F(18,181*M))
    x=F(360,181);ck('linear_stock_consumer',1+x+x*x/2>4)
    Q=15999999;R=5183999998;L=99999999999999;K=10
    ck('input_tail_square',F(4,Q+1)==F(1,2000)**2)
    ck('output_tail_square',F(324,R+2)==F(1,4000)**2)
    third=F((Q+R)*22,7*(L+1));ck('phase_bound',third<F(164,1000000))
    ck('complete_consumer',K*(F(1,2000)+F(1,4000)+third)+F(2,10000)<F(934,100000))
    capacity=R+L-1+Q;occupied=R+L-1;mean=F(2*R+L-1,2)
    ck('capacity',capacity==100005199999995);ck('occupied',occupied==100005183999996);ck('mean',mean==50005183999997)
    cells=K-1 if fault=='missing_stock_cell' else K
    ck('whole_stock_mean',cells*mean==500051839999970)
    ck('empty_margins_not_charge',capacity>occupied and occupied>mean)
    tvar=s.symbols('u',real=True);g=s.sin(tvar)**2
    ck('pulse_area',s.integrate(g,(tvar,0,s.pi))==s.pi/2)
    ck('pulse_endpoint',g.subs(tvar,0)==g.subs(tvar,s.pi)==0)
    ck('pulse_slew_endpoint',s.diff(g,tvar).subs(tvar,0)==s.diff(g,tvar).subs(tvar,s.pi)==0)
    return out

RESULT='K2262'
REPORT='lab/process/k2262-coherent-reference-supply.json'
DEPS=['explorations/conditional-build/k2262-coherent-reference-supply-2026-10-29.md', 'explorations/conditional-build/k2253-full-instrument-reference-reuse-2026-10-29.md', 'explorations/conditional-build/k2260-coherent-replenishment-bound-2026-10-29.md']
EVIDENCE='Finite exact algebra, rational resource and changed-input controls. Universal continuum/channel theorems are written proofs; hashes establish report provenance only.'

def main():
    import argparse,hashlib,json
    from pathlib import Path
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args()
    root=Path(__file__).resolve().parents[2];checks=controls()
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    faults={}
    for f in FAULTS:
        bad=[k for k,v in controls(f).items() if not v];assert bad,('undetected input fault',f);faults[f]=bad
    report=dict(result_id=RESULT,checks=checks,fault_failures=faults,evidence_kinds=EVIDENCE,dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in DEPS},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    p=root/REPORT
    if a.write:p.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(p.read_text())==report,'report drift'
    print(json.dumps(dict(result=RESULT,controls=len(checks),faults=len(faults))))
if __name__=='__main__':main()
