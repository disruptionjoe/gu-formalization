#!/usr/bin/env python3
"""Exact controls for K1858; prose owns the continuum proof. Standard library only."""
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / 'lab/process/k1858-fisher-two-well-profile.json'
PARAMS = dict(local_scale=Q(2), weight=Q(1,4), energy=Q(1,4),
              mean_correction=Q(1,8), virial=Q(2), eigen_energy=Q(2),
              jump=Q(2), budget_shift=Q(2), gaussian_fourth=Q(3),
              gaussian_sixth=Q(15))
REPORT_FAULTS = ['balanced_signs_without_extra_assumption',
                 'unconditional_zero_extension_H1', 'uniform_high_moment_transfer',
                 'next_coefficient', 'gu_physics']

def verify(par, report):
    groups = 0
    for h in [Q(1,10), Q(1,20), Q(1,100)]:
        d=h*h; s=h/par['local_scale']
        for y in [Q(0), Q(1,4), Q(1,2), Q(1), Q(3,2), Q(10)]:
            t=(y-1)/s
            assert t*t*(y+1)**2*par['weight']==(y*y-1)**2/d, 'weighted-moment identity'
            assert (y-1)**2 <= (y*y-1)**2, 'tightness inequality'
        assert s*s*Q(4)/d*par['energy']==Q(1,4), 'kinetic scaling'
        e_t2=Q(7,5); e_t=-s*e_t2/2
        assert 1+s*e_t==1-par['mean_correction']*d*e_t2, 'mean correction'
    groups += 3
    for eta in [Q(1,10),Q(1,3),Q(1,2)]:
        d=Q(1,100)
        lower=(4/d-4/((1+eta)*d))/(eta*d)
        upper=(4/((1-eta)*d)-4/d)/(eta*d)
        assert d*d*lower==4/(1+eta) and d*d*upper==4/(1-eta), 'secant limits'
        assert lower<4/d**2<upper, 'subgradient orientation'
    groups += 1
    b=Q(4); a=-par['virial']*b; e=-b
    for x in [Q(0),Q(1,8),Q(1,4),Q(3,8),Q(1,2)]:
        potential=a*x*x+b*x**4-e
        assert potential==4*(x*x-1)**2, 'virial barrier polynomial'
        assert potential>=Q(9,4), 'barrier margin'
    for d in [Q(1,100),Q(1,200)]:
        f=4/d-1; b=4/d**2; k=1+d
        a=f-par['virial']*b*k
        e=par['eigen_energy']*f-b*k
        assert e==f+a+b*k, 'eigenvalue identity'
    groups += 2
    for d in [Q(1,100),Q(1,1000)]:
        A=1-d/8; c=par['jump']*A/d; fisher=Q(17)
        cross=-par['jump']*A
        assert fisher+2*c*cross+c*c*d==fisher-4*A*A/d, 'jump-score square'
        assert 4*A*A/d==4/d-1+d/16, 'constant extraction'
    groups += 1
    x=Q(-1,2)
    assert Q(-1,2)+2*x+2*x*x==report['results']['fisher_constant'], 'trial I constant'
    assert report['results']['relative_fisher_constant']==report['results']['fisher_constant']-1, 'I versus J'
    for B in [Q(1),Q(10),Q(100)]:
        d=4/(B+par['budget_shift'])
        assert 4/d-2==B, 'budget inverse'
        assert (d-4/B)*B*B==-8*B/(B+2), 'budget second order'
    assert report['results']['budget_second_coefficient']==-8, 'budget report'
    groups += 2
    for t in [Q(1,100),Q(1,200),Q(1,1000)]:
        d=t*t; eps=t**19; w=t**-8
        v=(1-t**11)/(1-t**19)
        k=(1+d-par['gaussian_fourth']*t**3)*(1-t**19)/(1-t**11)**2
        assert 1<k<3 and v>0, 'contamination domain'
        assert (1-eps)*v+eps*w==1, 'exact second'
        assert (1-eps)*v*v*k+3*eps*w*w==1+d, 'exact fourth'
        sixth=par['gaussian_sixth']*eps*w**3
        recurrence=Q(1)
        for n in [1,3,5]: recurrence*=n
        assert sixth==recurrence/t**5, 'sixth moment recurrence'
        assert eps*(3*w*w-16)/d**2==3/t-16*t**15, 'profile fourth divergence'
        assert Q(96,100)<(k-1)/d<Q(101,100), 'leading-order feasibility'
    groups += 2
    flags=report['scope_flags']
    for key in REPORT_FAULTS:
        assert flags[key] is False, 'scope reporting: '+key
    assert flags['all_density_profile'] is True and flags['constant_requires_exact_optimizer'] is True, 'scope reporting: optimizer'
    for item in report['dependencies']:
        assert hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest()==item['sha256'], 'dependency bytes'
    groups += 2
    return groups

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--fault',choices=list(PARAMS))
    parser.add_argument('--report-fault',choices=REPORT_FAULTS)
    args=parser.parse_args()
    par=copy.deepcopy(PARAMS); report=json.loads(REPORT.read_text())
    if args.fault: par[args.fault]+=1
    if args.report_fault: report['scope_flags'][args.report_fault]=True
    try:
        groups=verify(par,report)
    except AssertionError as exc:
        print('ASSERTION:',exc)
        return 1
    print(f'PASS K1858: {groups} exact algebra/control groups; continuum proof remains in artifact')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
