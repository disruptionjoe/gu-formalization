#!/usr/bin/env python3
"""K2244 exact finite compression/support and resource controls, not a Fock proof."""
import sympy as s
from fractions import Fraction as F
FAULTS=['skip_polar','bad_extension','wrong_phase','coupled_support','tail_cutoff','resource_cutoff','pulse_area']
def controls(fault=None):
    checks={}
    def ck(k,v):checks[k]=bool(v)
    # Actual 3D unitary leaks from low input e0 to omitted e2.
    U=s.Matrix([[s.Rational(3,5),0,-s.Rational(4,5)],[0,1,0],[s.Rational(4,5),0,s.Rational(3,5)]])
    PL=s.diag(1,0,0);PR=s.diag(1,1,0)
    A=PR*U*PL
    V=A if fault=='skip_polar' else PL
    ck('unitary_target',U.T*U==s.eye(3))
    ck('compression_really_leaks',(U*PL-A).T*(U*PL-A)==s.diag(s.Rational(16,25),0,0))
    ck('polar_isometry',V.T*V==PL)
    W=s.diag(1,1,1) if fault!='bad_extension' else PR*U*PR
    ck('extended_unitary',W.T*W==s.eye(3))
    ck('extension_matches_polar',W*PL==V)
    ck('compression_not_unitary',(PR*U*PR).T*(PR*U*PR)!=PR)
    ck('polar_error_bound',((V-U*PL).T*(V-U*PL))[0,0]<=1)
    # Exact onsite diagonal interaction-picture phase restoration.
    D=s.diag(1,s.I,-1);K=s.Matrix([[1,1,0],[1,1,0],[0,0,0]])
    H=D*K*D.conjugate().T
    ck('onsite_modulation_hermitian',H==H.conjugate().T)
    ck('onsite_modulation_positive',sorted(H.eigenvals())==[0,2])
    ck('interaction_picture_generator',D.conjugate().T*H*D==K)
    correction=D.conjugate().T if fault!='wrong_phase' else D
    ck('laboratory_picture_cancellation',D*correction==s.eye(3))
    # One-excitation restriction of three sites, onsite vacuum projector.
    hopping=s.Matrix([[0,1,0],[1,0,1],[0,1,0]])
    local=s.diag(0,1,1)
    drift=s.diag(1,2,3) if fault!='coupled_support' else hopping
    ck('onsite_drift_preserves_site_projector',drift*local-local*drift==s.zeros(3))
    comm=hopping*local-local*hopping
    ck('coupled_drift_spreads',comm[0,1]!=0)
    nested=hopping*comm-comm*hopping
    ck('coupled_drift_reaches_third',nested[0,2]!=0)
    # Actual finite spectral approximation omits the last admitted level under fault.
    target=s.diag(1,s.I,-1)
    cutoff=2 if fault!='tail_cutoff' else 1
    actual=s.diag(*[target[j,j] if j<=cutoff else 1 for j in range(3)])
    ck('spectral_gate_agrees_on_fixed_admitted_sector',actual==target)
    # Rare high occupation supplies a positive Markov witness (not fault credit).
    L=4;level=L+1;prob=F(1,level+1);G=F(1)+prob*level
    ck('tail_control_positive',prob>0)
    ck('tail_markov',prob<=G/F(L+1))
    Rplus=9*10**15 if fault!='resource_cutoff' else 9*10**9
    dsq=F(9*10**9,Rplus)
    ck('consumer_delta_squared',dsq<=F(1,10**6))
    ck('consumer_tail_squared',F(4*5832,10**9)<F(1,200**2))
    ck('consumer_complete_error',14*(F(1,1000)+F(1,10**6)+F(1,200))==F(42007,500000)<F(1,10))
    z=s.symbols('z',real=True)
    pulse=(2 if fault!='pulse_area' else 1)*s.sin(s.pi*z)**2
    ck('smooth_pulse_area',s.integrate(pulse,(z,0,1))==1)
    ck('smooth_pulse_endpoints',pulse.subs(z,0)==pulse.subs(z,1)==0)
    deriv=s.diff(pulse,z)
    ck('smooth_pulse_endpoint_derivatives',deriv.subs(z,0)==deriv.subs(z,1)==0)
    piup=F(22,7);tau=F(64);rmax=F(1)
    ck('slew_consumer_upper_bounds',4*piup/tau<1 and 4*piup*piup/(tau*tau)+8*piup*rmax/tau<1)
    return checks

RESULT='K2244'
REPORT='lab/process/k2244-onsite-drift-local-control.json'
DEPS=['explorations/conditional-build/k2244-onsite-drift-local-control-2026-10-29.md', 'explorations/conditional-build/k2241-local-mode-detector-network-2026-10-29.md', 'explorations/conditional-build/k2225-positive-drift-detector-control-2026-10-28.md']
EVIDENCE='Exact finite polar-compression and support countercontrols plus rational bounds; universal Fock energy/reference/unitary completion theorem in note.'

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
