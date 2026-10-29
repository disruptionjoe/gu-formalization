#!/usr/bin/env python3
"""Exact walk moments, reference channel and finite reservoir resource controls."""
from fractions import Fraction as F
from math import factorial,comb
import sympy as s
FAULTS=['endpoint_weight','periodic_boundary','bulk_endpoint','drop_coherence','phase_conjugation','nonvacuum_bath','reservoir_length']
def walks(size,power,fault=None,start=0):
    v=[0]*size;v[start]=1
    for _ in range(power):
        w=[0]*size
        for n,a in enumerate(v):
            if n:w[n-1]+=a*(2 if fault=='endpoint_weight' and n==1 else 1)
            if n+1<size:w[n+1]+=a*(2 if fault=='endpoint_weight' and n==0 else 1)
        if fault=='periodic_boundary':w[0]+=v[-1];w[-1]+=v[0]
        v=w
    return v

def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    for k in range(7):
        moment=walks(15,2*k,fault)[0]
        if fault=='bulk_endpoint':moment=walks(31,2*k,start=15)[15]
        ck('endpoint_Catalan_'+str(k),moment==comb(2*k,k)//(k+1))
    for n in range(5):
        for m in range(4):
            degree=n+2*m
            actual=F(walks(15,degree,fault)[n],factorial(degree))
            expected=F(n+1,factorial(m)*factorial(n+m+1))
            ck('all_site_Bessel_series_'+str((n,m)),actual==expected)
    # Finite boundary difference occurs first at the walk that reaches site M and returns.
    M=4
    ck('finite_initial_moments_equal',all(walks(M,k)[0]==walks(15,k)[0] for k in range(2*M)))
    ck('finite_first_boundary_return',walks(15,2*M)[0]-walks(M,2*M)[0]==1)
    # Exact complex amplitude checks full channel, including off-diagonal reference blocks.
    a=3*s.I/5;b=s.Rational(4,5)
    K0=s.diag(1,a);K1=s.Matrix([[0,b],[0,0]])
    if fault=='phase_conjugation':K0=K0.conjugate()
    ks=[K0,K1]
    if fault=='drop_coherence':ks=[P*k for P in [s.diag(1,0),s.diag(0,1)] for k in ks]
    ck('channel_trace_preserving',K0.conjugate().T*K0+K1.conjugate().T*K1==s.eye(2))
    for i in range(2):
        for j in range(2):
            unit=s.zeros(2);unit[i,j]=1
            replacement=s.diag(s.trace(unit),0)
            got=sum((k*unit*k.conjugate().T for k in ks),s.zeros(2))-replacement
            rr=s.Rational(9,25)
            expected=s.Matrix([[-rr*unit[1,1],s.conjugate(a)*unit[0,1]],[a*unit[1,0],rr*unit[1,1]]])
            ck('complete_matrix_unit_difference_'+str((i,j)),got==expected)
    e=s.Matrix([[0,1],[0,0]])
    got=sum((k*e*k.conjugate().T for k in ks),s.zeros(2))
    ck('off_diagonal_channel',got==s.conjugate(a)*e)
    bell=s.Matrix([1,0,0,1]);rho=bell*bell.T/2
    channel=sum((s.kronecker_product(k,s.eye(2))*rho*s.kronecker_product(k.conjugate().T,s.eye(2)) for k in ks),s.zeros(4))
    ck('reference_coherence',channel[0,3]==s.conjugate(a)/2)
    ck('reference_marginal',s.Matrix([[channel[0,0]+channel[2,2],channel[0,1]+channel[2,3]],[channel[1,0]+channel[3,2],channel[1,1]+channel[3,3]]])==s.eye(2)/2)
    # Actual SWAP target excitation after swapping with independently supplied bath.
    bath=s.diag(1,0) if fault!='nonvacuum_bath' else s.diag(0,1)
    swap=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
    joint=swap*s.kronecker_product(s.diag(1,0),bath)*swap.T
    ck('vacuum_reset_control',joint[2,2]+joint[3,3]==0)
    ck('one_input_error',F(1,200)+F(1,200**2)==F(201,40000))
    prefix=sum(k*k for k in range(1,11));ck('prefix_exact_sum',prefix==385)
    ck('prefix_resource',F(prefix,10000**2)<F(1,250000))
    n=4000 if fault!='reservoir_length' else 400
    ck('finite_chain_resource_integer',400*3**400*400**n*10**1000<factorial(n))
    ck('horizon_distance_condition',n>=400)
    ck('positive_one_particle',min(s.Matrix([[2,1],[1,2]]).eigenvals())==1)
    return out

RESULT='K2246'
REPORT='lab/process/k2246-autonomous-vacuum-reservoir.json'
DEPS=['explorations/conditional-build/k2246-autonomous-vacuum-reservoir-2026-10-29.md', 'explorations/conditional-build/k2235-microscopic-thermal-renewal-2026-10-29.md', 'explorations/conditional-build/k2238-finite-clock-thermal-circuit-2026-10-29.md']
EVIDENCE='Finite exact arithmetic and algebra controls; universal domain/channel/locality claims are written independently reviewed proofs, not consequences of counts.'

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
