#!/usr/bin/env python3
"""Exact finite controls for the written full-Fock pulse/resource proof."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from itertools import permutations
import argparse,hashlib,json
import sympy as s
from fractions import Fraction as F
import k2210_detector_stationary_certificate_probe as arithmetic
ROOT=Path(__file__).resolve().parents[2]

def rotation(a,b,fault=None):
    return s.Matrix([[a,-b],[b,a if fault!='record_norm' else 2*a]])
def pulse_matrix(x,fault=None):
    quarter=s.Matrix([[0,1/x],[-x,0]]);unit=s.Matrix([[0,1],[-1,0]])
    return quarter*unit**3 if fault=='pulse_order' else unit**3*quarter

def reset_minimum(w,tau,fault=None):
    eigen=[p*t for p in [w,1-w] for t in tau]
    if fault=='reset_product':eigen=[p+t for p in [w,1-w] for t in tau]
    return sum(sorted(eigen)[:len(tau)])

def tail_mass(n,fault=None):
    return F(0) if fault=="tail_omitted" else F(4)**-n

def controls(fault=None):
    c={}
    def ck(k,v):c[k]=bool(v)
    a=s.Rational(3,5);b=s.Rational(4,5);u=rotation(a,b,fault)
    ck('record_unitary',u.T*u==s.eye(2));ck('positive_root_Kraus',u[:,0]==s.Matrix([a,b]))
    ck('Kraus_complete',sum(v*v for v in u[:,0])==1)
    Y=s.Matrix([[0,-s.I],[s.I,0]])
    shift=0 if fault=='hamiltonian_shift' else s.pi/2
    H=shift*s.eye(2)+s.pi*Y/3
    ck('measurement_positive',min(H.eigenvals())>=0)
    ck('measurement_upper',max(H.eigenvals())<=s.pi)
    x=s.symbols('x',positive=True);P=pulse_matrix(x,fault)
    ck('exact_squeeze',P==s.diag(x,1/x))
    J=s.Matrix([[0,1],[-1,0]])
    ck('symplectic',s.simplify(P*J*P.T)==J)
    # Real cos/sin controls of the full positive-oscillator flow.
    for q in [s.Rational(2,3),s.Rational(7,5),s.Integer(1)]:
        K=max(q,1/q);R=s.Matrix([[a,b/q],[-q*b,a]])
        D=K*K*s.eye(2)-R.T*R
        ck('G_bound_'+str(q),D[0,0]>=0 and D[1,1]>=0 and D.det()>=0)
        ck('positive_oscillator_'+str(q),q>0 and 1/q>0)
        ck('plateau_energy_bound_'+str(q),K>=q and K>=1/q)
    B,C,E=s.symbols('B C E',real=True)
    switches=[s.pi/2,B-s.pi/2,C-B,E-C]
    ck('signed_switch_work',s.simplify(sum(switches)-E)==0)
    # Canonical two-qubit SWAP, including a correlated field-record state.
    swap=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
    anti=(s.eye(4)-swap)/2
    ck('swap_unitary',swap.T*swap==s.eye(4));ck('swap_positive_generator',anti*anti==anti and anti.T==anti)
    # |F=0,R=0,B=0> amplitude3/5 plus |F=1,R=1,B=0> amplitude4/5.
    v=s.zeros(8,1);v[0]=a;v[6]=b
    out=s.kronecker_product(s.eye(2),swap)*v
    ck('reset_record_pure',all(out[i]==0 for i in [2,3,6,7]))
    ck('correlations_transferred',out[0]==a and out[5]==b)
    w=s.Rational(1,3);tau=[s.Rational(3,4),s.Rational(1,4)]
    exact=[w*t for t in tau]+[(1-w)*t for t in tau]
    direct=min(sum(p[:2]) for p in permutations(exact))
    ck('sharp_reset_vs_all_permutations',reset_minimum(w,tau,fault)==direct)
    ck('sharp_reset_quarter',reset_minimum(w,tau,fault)==s.Rational(1,4))
    ck('full_rank_positive_bound',direct>=len(tau)*min(w,1-w)*min(tau)>0)
    ck('pure_bit_escape',reset_minimum(w,[s.Integer(1),s.Integer(0)],fault)==0)
    ck('full_rank_input',all(v>0 for v in exact) and len(exact)==4)
    ck('geometric_tail_mass',tail_mass(7,fault)==F(3,4)*F(4)**-7/(1-F(1,4)))
    z=(1+s.I/5)**4/(1+s.I/239)
    ck('Machin_identity',s.simplify(s.im(z)-s.re(z))==0 and s.re(s.expand_complex(z))>0)
    return c

def switch_certificate():
    # The true K2219 optimizer belongs to these certified all-tail boxes.
    IV=arithmetic.IV
    old=json.loads((ROOT/'lab/process/k2219-detector-global-capture.json').read_text())['certificate']
    bank=old['basin']
    boxes=[IV(F(a),F(b)) for a,b in bank['coordinate_boxes']]
    squeezes=[IV(F(a),F(b)) for a,b in bank['squeeze_boxes']]
    w=sum((F(3,4)*F(4)**-n*boxes[n] for n in range(len(boxes))),IV(0))
    # All unseen e are capped and admitted above3/20; full geometric tail.
    tail=tail_mass(len(boxes));w=w+IV(F(3,20)*tail,tail)
    assert F(1,4)<w.a and w.b<F(3,4)
    R1=(1+5*w)/6;R0=F(5,6)-R1
    B=sum((rr*(q+1/q)/2 for rr,q in zip([R1,R0],squeezes)),IV(0))
    C=sum((rr*(q*q+1/(q*q))/2 for rr,q in zip([R1,R0],squeezes)),IV(0))
    # Machin identity and alternating arctan series give rational pi bounds.
    def atan(q,n):
        total=sum(((-1)**k*q**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
        rem=q**(2*n+1)/F(2*n+1)
        return IV(total,total+rem) if n%2==0 else IV(total-rem,total)
    pi=16*atan(F(1,5),60)-4*atan(F(1,239),20)
    assert pi.a>F(314159,100000) and pi.b<F(314160,100000)
    E=IV(F(old['global_energy_lower']),F(old['global_energy_upper']))
    terms=[pi/2,B-pi/2,C-B,E-C]
    assert terms[0].a>0 and terms[1].b<0 and terms[2].a>0 and terms[3].b<0
    absolute=pi+2*C-2*B-E
    pair=lambda x:[str(x.a),str(x.b)]
    return dict(actual_optimizer_reset_error_for_bath_threequarters_onequarter='1/4',click_probability=pair(w),B=pair(B),C=pair(C),net_work=pair(E),switch_work_intervals=[pair(x) for x in terms],absolute_mean_work=pair(absolute),pi=pair(pi),tail_method='seven coordinate boxes plus complete geometric cap tail; no truncation')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args()
    c=controls();assert all(c.values()),[k for k,v in c.items() if not v]
    faults={f:[k for k,v in controls(f).items() if not v] for f in ['record_norm','pulse_order','hamiltonian_shift','reset_product','tail_omitted']};assert all(faults.values())
    deps=['explorations/conditional-build/k2160-outcome-conditioned-squeezing-2026-10-27.md','explorations/conditional-build/k2219-detector-global-capture-2026-10-28.md','explorations/conditional-build/k1916-bath-preparation-resource-limits-2026-10-21.md','explorations/conditional-build/k2223-stable-detector-resource-realization-2026-10-28.md','lab/process/k2219-detector-global-capture.json','tests/channel-swings/k2210_detector_stationary_certificate_probe.py']
    report=dict(result_id='K2223',status='conditional_semibounded_switched_realization_and_reset_resources',checks=c,switch_certificate=switch_certificate(),fault_failures=faults,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Written functional-calculus, metaplectic domain, telescoping-work and eigenvalue-variational proof. Exact symbolic pulse and rational reset/permutation controls, not a truncated-CCR or physical apparatus proof.')
    p=ROOT/'lab/process/k2223-stable-detector-resource-realization.json'
    if a.write:p.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(p.read_text())==report
    print(json.dumps(dict(result='K2223',controls=len(c),faults=faults)))
if __name__=='__main__':main()
