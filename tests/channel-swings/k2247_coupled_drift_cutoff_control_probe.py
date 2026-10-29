#!/usr/bin/env python3
"""Actual small Fock controls for positive local cancellation and cutoff leakage."""
import sympy as s
from fractions import Fraction as F
FAULTS=['cancel_sign','omit_edge','undersized_cutoff','negative_shift','drop_record','resource_tail']
def model(A,fault=None):
    # Global cutoff4 is only a finite fixture; each local cancellation uses its own projector.
    states=[(n,m) for n in range(5) for m in range(5-n)];ix={x:i for i,x in enumerate(states)};d=len(states)
    N1=s.diag(*[n for n,m in states]);N2=s.diag(*[m for n,m in states]);edge=s.zeros(d)
    for (n,m),k in ix.items():
        if m and (n+1,m-1) in ix:edge[ix[n+1,m-1],k]=s.sqrt((n+1)*m)
        if n and (n-1,m+1) in ix:edge[ix[n-1,m+1],k]=s.sqrt(n*(m+1))
    H0=2*N1+2*N2+edge
    terms=[(2*N1,N1,2),(2*N2,N2,2),(edge,N1+N2,1)];C=s.zeros(d)
    pieces=[]
    for j,(h,n,c) in enumerate(terms):
        P=s.diag(*[int(bool(n[k,k]<=A)) for k in range(d)])
        scalar=A*c if fault!='negative_shift' else -A*c
        piece=P*(scalar*s.eye(d)+h if fault=='cancel_sign' else scalar*s.eye(d)-h)*P
        if fault=='omit_edge' and j==2:piece=s.zeros(d)
        pieces.append(piece);C+=piece
    return states,ix,H0,C,pieces

def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    A=2
    states,ix,H0,C,pieces=model(A,fault)
    P=s.diag(*[int(n+m<=A) for n,m in states]);d=len(states)
    ck('drift_number_preserving',H0*s.diag(*[n+m for n,m in states])==s.diag(*[n+m for n,m in states])*H0)
    ck('actual_cancellation',(H0+C-5*A*s.eye(d))*P==s.zeros(d))
    for j,piece in enumerate(pieces):
        ck('positive_piece_'+str(j),piece.is_positive_semidefinite is True)
        bound=2*A*[2,2,1][j]
        ck('bounded_piece_'+str(j),(bound*s.eye(d)-piece).is_positive_semidefinite is True)
    ck('drift_positive',H0.is_positive_semidefinite is True)
    # Finite fixture compression of local K=I-X on |0>,|1>.
    # All derivatives through order3 from vacuum stay below artificial total cutoff4.
    cutoff=0 if fault=='undersized_cutoff' else 1
    states,ix,H0,C,_=model(cutoff);d=len(states);K=s.zeros(d)
    for m in range(5):
        a=ix[0,m];K[a,a]=1
        if (1,m) in ix:
            b=ix[1,m];K[b,b]=1;K[a,b]=K[b,a]=-1
    v=s.zeros(d,1);v[ix[0,0]]=1
    ck('positive_local_gate',K.is_positive_semidefinite is True)
    wanted=(5*cutoff*s.eye(d)+K)
    actual=H0+C+K
    ck('path_first_derivative',actual*v==wanted*v)
    ck('path_second_derivative',actual**2*v==wanted**2*v)
    ck('path_third_derivative',actual**3*v==wanted**3*v)
    # Boundary countercontrol at insufficient A=0 is actually nonzero remote hopping.
    _,_,hz,cz,_=model(0)
    ck('undercut_remote_leak',((hz+K)**2*v-K**2*v)[ix[0,1]]==-1)
    # A record retained after controlled feedback must retain distinguishable outcomes.
    # Start record |+> and system |0>, apply record-controlled X then pinch record.
    CX=s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
    psi=CX*s.Matrix([1,0,1,0])/s.sqrt(2)
    rho=psi*psi.T
    P0=s.diag(1,1,0,0);P1=s.diag(0,0,1,1)
    recorded=P0*rho*P0+P1*rho*P1
    if fault=='drop_record':
        system=recorded[:2,:2]+recorded[2:,2:]
        recorded=s.kronecker_product(s.eye(2)/2,system)
    ck('complete_record_control',recorded==s.diag(s.Rational(1,2),0,0,s.Rational(1,2)))
    L0p=10**8 if fault!='resource_tail' else 10**4
    ck('extra_initial_tail',F(4*2,L0p)<F(3,10000)**2)
    ck('local_tail',F(4*5832,10**9)<F(1,200)**2)
    ck('local_polar_delta',F(9*10**9,9*10**15)==F(1,10**6))
    ck('complete_consumer',F(3,10000)+12*(F(1,1000)+F(1,10**6)+F(1,200))==F(9039,125000)<F(1,10))
    # Exact two-mode hopping spectra on A=1,2,3 certify the edge cost fixtures.
    for count in [1,2,3]:
        h=s.zeros(count+1)
        for k in range(count):h[k,k+1]=h[k+1,k]=s.sqrt((k+1)*(count-k))
        ck('edge_spectrum_'+str(count),set(h.eigenvals())==set(range(-count,count+1,2)))
        optimal=count*s.eye(count+1)-h
        ck('sharp_edge_cost_'+str(count),max(optimal.eigenvals())==2*count and optimal.is_positive_semidefinite is True)
        ck('undershift_fails_'+str(count),min(((count-s.Rational(1,2))*s.eye(count+1)-h).eigenvals())<0)
    return out

RESULT='K2247'
REPORT='lab/process/k2247-coupled-drift-cutoff-control.json'
DEPS=['explorations/conditional-build/k2247-coupled-drift-cutoff-control-2026-10-29.md', 'explorations/conditional-build/k2244-onsite-drift-local-control-2026-10-29.md', 'explorations/conditional-build/k2241-local-mode-detector-network-2026-10-29.md']
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
