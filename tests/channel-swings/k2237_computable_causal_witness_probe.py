#!/usr/bin/env python3
"""K2237 finite rational algebra controls; no continuum certification."""
from fractions import Fraction as F
from math import comb, factorial

def weights(n,N,x):
    return sum((F(comb(n+1,j+1),factorial(j))*N**(n-j)*x**j
                /(1+N)**(n+j+2) for j in range(n+1)),F(0))

def recurrence(count,N,x,fault):
    r,d=N/(N+1),x/(N+1)**(1 if fault=='weight_denominator' else 2)
    prev,cur=F(0),F(1);out=[]
    for n in range(count):
        out.append(cur/(N+1)**2)
        nxt=(2*r+d/F(n+1))*cur+(1 if fault=='recurrence_sign' else -1)*r*r*prev
        prev,cur=cur,nxt
    return out

def clip(x,R):return min(R,max(-R,x))
def half_tv(p,q):return sum(abs(a-b) for a,b in zip(p,q))/2
def bob(p):return (p[0]+p[2],p[1]+p[3])
def mix(p,q,t):return tuple((1-t)*a+t*b for a,b in zip(p,q))

FAULTS=('weight_denominator','recurrence_sign','squeeze_inverse','complement_omitted',
        'parity_swapped','clip_tail_reduction','norm_effect_confusion','different_mixture_reference')

def run(fault=None):
    checks={}
    checks['weight_polynomial_vs_independent_ODE_recurrence']=all(
        weights(n,N,x)==v
        for N in (F(0),F(1,100),F(1,3),F(2))
        for x in (F(1,100),F(1,2),F(3))
        for n,v in enumerate(recurrence(12,N,x,fault)))
    checks['coherent_limit']=all(weights(n,F(0),F(1,3))==F(1,3)**n/factorial(n) for n in range(12))
    checks['thermal_zero_displacement']=all(weights(n,F(1,3),F(0))==F(n+1)*F(1,3)**n/F(4,3)**(n+2) for n in range(12))
    # Actual zero-link adjoint: e1(0)=0,e1(1)=1/2, so sigma0=s0/sqrt(2).
    s0=F(3,2) if fault=='squeeze_inverse' else F(2,3)
    checks['actual_zero_link_squared']=s0*s0/2<F(1,4)
    p0=F(99,100)/F(101,100)**2
    checks['tail_lower_bound_arithmetic']=F(9,10)*p0-F(2,5)>F(47,100)
    # Direct displacement of field+complement for identity channel.
    checks['identity_does_not_signal']=F(3,7)+(-F(3,7) if fault!='complement_omitted' else 0)==0
    # q^2 preserves parity: two diagonal blocks of sum s_r^2 e_r.
    e_even,e_odd=(F(4,5),F(1,5)) if fault=='parity_swapped' else (F(1,5),F(4,5))
    qcoeff=lambda e:4*e+F(1,4)*(1-e)
    pcoeff=lambda e:F(1,4)*e+4*(1-e)
    checks['blindspot_q2_adjoints']=(qcoeff(e_even),qcoeff(e_odd))==(F(1),F(13,4))
    checks['blindspot_p2_adjoints']=(pcoeff(e_even),pcoeff(e_odd))==(F(13,4),F(1))
    checks['blindspot_first_moments']=F(2,5)*(2+F(1,2))==1
    # Pointwise clipping inequality on an independent rational grid.
    tail_factor=F(1,8) if fault=='clip_tail_reduction' else F(1)
    checks['signed_clip_pointwise']=all(abs(x-clip(x,R))<=tail_factor*x*x/R
        for R in (F(1,3),F(1),F(3)) for x in (F(-7),F(-2),F(-1,4),F(0),F(1,2),F(2),F(7)))
    # Exact diagonal density matrices distinguish norm-one and effect constants.
    rho,sig=(F(1),F(0)),(F(0),F(1))
    distance=half_tv(rho,sig)
    factor=1 if fault=='norm_effect_confusion' else 2
    checks['norm_one_vs_effect']=abs(sum((a-b)*x for a,b,x in zip(rho,sig,(-1,1))))<=factor*distance
    checks['effect_expectation_contract']=abs(rho[0]-sig[0])<=distance
    # Actual causal identity-on-Bob inputs, then shared-reference mixing.
    vacuum=(F(1),F(0),F(0),F(0));alice=(F(0),F(0),F(1),F(0))
    wrong=(F(0),F(1),F(0),F(0))
    checks['common_reference_mixing_causality']=bob(mix(vacuum,vacuum,F(1,4)))==bob(mix(wrong if fault=='different_mixture_reference' else vacuum,alice,F(1,4)))
    # Exact consumer arithmetic, not independent continuum proof.
    checks['N_and_nu_numeric_majorants']=F(17,16)<F(51,50)**4 and F(17,16)<4
    M=4*(F(49,25)*F(103,100)+F(1,100))+4
    checks['primary_rational_consumer']=M==F(7572,625) and (2*F(1,100)*F(47,100)**2)/(16*M)==F(2209,96921600)
    checks['energy_consumer']=F(1,25)*F(17,16)/2==F(17,800)
    vq,x=F(51,100),F(1,100)
    M4=8*(16*(6*vq*vq+12*vq*x+4*x*x)+6+12*x+4*x*x)
    checks['second_moment_rational_consumer']=M4==F(160378,625) and (F(9,4)*x)**2/(8*M4)==F(81,328454144)
    return checks

def main():
    import argparse, hashlib, json
    from pathlib import Path
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
    root=Path(__file__).resolve().parents[2]
    checks=run();assert all(checks.values()),[k for k,v in checks.items() if not v]
    faults={}
    for fault in FAULTS:
        failed=[k for k,v in run(fault).items() if not v]
        assert failed,('undetected mathematical mutation',fault)
        faults[fault]=failed
    deps=['explorations/conditional-build/k2237-computable-causal-witness-2026-10-29.md','explorations/conditional-build/k2225-positive-drift-detector-control-2026-10-28.md','explorations/conditional-build/k2228-continuum-energy-form-detector-control-2026-10-28.md','explorations/conditional-build/k2234-causal-detector-error-bound-2026-10-29.md']
    report=dict(result_id='K2237',checks=checks,fault_failures=faults,dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Finite exact weight recurrence, parity adjoints, displacement/clipping/state controls and rational consumer arithmetic; universal continuum/domain/reference and tail proofs are separate written arguments.')
    dest=root/'lab/process/k2237-computable-causal-witness.json'
    if args.write:dest.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dest.read_text())==report,'certificate drift'
    print(json.dumps(dict(result='K2237',controls=len(checks),faults=len(faults))))
if __name__=='__main__': main()
