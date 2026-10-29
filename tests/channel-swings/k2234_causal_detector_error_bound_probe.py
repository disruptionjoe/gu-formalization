#!/usr/bin/env python3
"""Exact finite proof controls; continuum classification uses the written proof."""
from fractions import Fraction as F
import argparse
import json


def matmul(A, B):
    return [[sum((x*y for x, y in zip(row, col)), F(0))
             for col in zip(*B)] for row in A]


def transpose(A):
    return list(map(list, zip(*A)))


def sigma(a, b):
    return a[0]*b[1]-a[1]*b[0]


def weyl_mul(A, B, omit_cocycle=False):
    # W(a)W(b)=exp(i phase) W(a+b); all phases here rational.
    a, pa = A
    b, pb = B
    return ((a[0]+b[0], a[1]+b[1]),
            pa+pb-(F(0) if omit_cocycle else sigma(a,b)/2))


def run(fault=None):
    checks=[]
    def check(name, got, expected):
        checks.append({'name':name, 'pass':got == expected})
    a,b=F(3,5),F(4,5)
    O=[[a,b],[-b,a]]
    check('real_mode_normalized',a*a+b*b,F(1))
    check('mode_change_orthogonal',matmul(O,transpose(O)),[[F(1),F(0)],[F(0),F(1)]])
    # rho_fc for A-site photon, obtained by transforming the site vector.
    psi=matmul(O,[[F(1)],[F(0)]])
    rho=matmul(psi,transpose(psi))
    check('input_offdiagonal',rho[0][1],F(-12,25))
    fixtures=[('projective',[F(1),F(0)],[F(0),F(1)],F(0),F(288,625)),
              ('soft',[F(3,5),F(4,5)],[F(4,5),F(3,5)],F(24,25),F(288,15625)),
              ('constant',[F(3,5),F(4,5)],[F(3,5),F(4,5)],F(1),F(0))]
    for name,d0,d1,gamma_expected,p_expected in fixtures:
        check(name+'_effect0_complete',sum(x*x for x in d0),F(1))
        check(name+'_effect1_complete',sum(x*x for x in d1),F(1))
        gamma=sum(x*y for x,y in zip(d0,d1))
        check(name+'_overlap',gamma,gamma_expected)
        out=[[F(0),F(0)],[F(0),F(0)]]
        for r in range(2):
            K=[[d1[r],F(0)],[F(0),d0[r]]]
            if fault == 'erase_complement_identity':
                K[1][1]=F(0)
            block=matmul(matmul(K,rho),K)
            for i in range(2):
                for j in range(2):
                    out[i][j]+=block[i][j]
        if fault == 'erase_detector_dephasing':
            out[0][1]=out[1][0]=rho[0][1]
        check(name+'_trace',out[0][0]+out[1][1],F(1))
        check(name+'_coherence',out[0][1],gamma*rho[0][1])
        out_site=matmul(matmul(transpose(O),out),O)
        check(name+'_bob_probability',out_site[1][1],p_expected)
        check(name+'_independent_closed_formula',out_site[1][1],2*a*a*b*b*(1-gamma_expected))
    # Effect-distance versus norm-one observable constants are kept distinct.
    pB=F(288,625)
    check('effect_half_trace_bound',pB/2,F(144,625))
    # Physical equal-frequency omega0=3 fixture; vacuum mixture energy exact.
    omega0,E=F(3),F(1,10)
    mix=min(F(1),E/omega0)
    if fault == 'ignore_input_mixing_budget':
        mix=F(1)
    check('low_energy_mixture_weight',mix,F(1,30))
    check('low_energy_input',mix*omega0,E)
    check('low_energy_effect_bound',mix*pB/2,F(24,3125))
    # Generic continuum bounded-observable bound at declared d and E_*.
    d,E_star=F(3,7),F(9)
    for energy in (F(1,10),F(9),F(20)):
        weight=min(F(1),energy/E_star)
        bound=weight*d/4
        check('generic_witness_budget_'+str(energy),weight*E_star<=energy,True)
        check('generic_witness_positive_'+str(energy),bound>0,True)
        check('generic_witness_saturation_'+str(energy),bound<=d/4,True)
    # Weyl cocycle and complete-positivity block conjugation exact phase test.
    zs=[(F(0),F(0)),(F(1),F(2)),(F(-2,3),F(4,5))]
    for i,zi in enumerate(zs):
        for j,zj in enumerate(zs):
            negzi=(-zi[0],-zi[1])
            negzj=(-zj[0],-zj[1])
            inner=weyl_mul((negzi,F(0)),(zj,F(0)),
                           omit_cocycle=(fault=='drop_cp_weyl_cocycle'))
            total=weyl_mul(weyl_mul((zi,F(0)),inner),(negzj,F(0)))
            check('cp_block_phase_'+str(i)+'_'+str(j),total,((F(0),F(0)),F(0)))
    za,zb=(F(2,3),F(5,7)),(F(-3,5),F(7,11))
    negative_a=(-za[0],-za[1])
    conj=weyl_mul(weyl_mul((negative_a,F(0)),(zb,F(0))),(za,F(0)))
    check('conjugation_eigenphase',conj,(zb,sigma(za,zb)))
    complement_phase=-sigma(za,zb)
    if fault=='reverse_complement_phase':
        complement_phase=-complement_phase
    check('spatial_weyls_commute',conj[1]+complement_phase,F(0))
    # Squeezing connects occupations by even steps; number effects are diagonal.
    step=1 if fault=='replace_squeeze_by_odd_generator' else 2
    for n in range(6):
        check('squeeze_parity_'+str(n),(-1)**(n+step),(-1)**n)
    return checks


FAULTS=['erase_complement_identity','erase_detector_dephasing',
        'ignore_input_mixing_budget','drop_cp_weyl_cocycle',
        'reverse_complement_phase','replace_squeeze_by_odd_generator']


def main():
    import hashlib
    from pathlib import Path
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--controls-only',action='store_true')
    args=parser.parse_args()
    baseline=run()
    failures=[c['name'] for c in baseline if not c['pass']]
    if failures:
        raise AssertionError('FAIL baseline: '+repr(failures))
    caught={}
    for fault in FAULTS:
        # Exceptions propagate; only explicit failed checks count as detection.
        caught[fault]=[c['name'] for c in run(fault) if not c['pass']]
        if not caught[fault]:
            raise AssertionError('FAIL mutation escaped: '+fault)
    if not args.controls_only:
        root=Path(__file__).resolve().parents[2]
        deps=['explorations/conditional-build/k2234-causal-detector-error-bound-2026-10-29.md',
              'explorations/conditional-build/k2228-continuum-energy-form-detector-control-2026-10-28.md',
              'explorations/conditional-build/k2231-spatial-local-control-boundary-2026-10-29.md',
              'explorations/conditional-build/k2145-parity-causal-duration-2026-10-27.md']
        target=root/'lab/process/k2234-causal-detector-error-bound.json'
        report=dict(result='K2234',controls=baseline,faults=caught,
            evidence_kind='finite exact density-matrix/Weyl phase controls; continuum proof is written in the note',
            probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in deps})
        if args.write:
            target.write_text(json.dumps(report,indent=2)+'\n')
        elif json.loads(target.read_text())!=report:
            raise AssertionError('FAIL stale certificate')
    print(json.dumps(dict(result='K2234',controls=len(baseline),
                         faults={k:len(v) for k,v in caught.items()})))

if __name__=='__main__':
    main()
