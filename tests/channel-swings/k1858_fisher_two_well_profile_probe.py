#!/usr/bin/env python3
"""Independent rational controls and clean-baseline fault detection for K1858."""
from fractions import Fraction as F
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent
SCRIPT=HERE/'k1858_fisher_two_well_profile.py'

def call(*args):
    return subprocess.run([sys.executable,str(SCRIPT),*args],text=True,capture_output=True)

def main():
    base=call()
    assert base.returncode==0 and base.stdout.startswith('PASS K1858:'), 'producer clean baseline failed: '+base.stdout+base.stderr
    controls=0
    # Independent physical-to-local scaling, with rational square-root parameter.
    for n in [7,13,31,97]:
        h=F(1,n); delta=h*h
        for y in [F(1,5),F(2,3),F(9,10),F(11,10),F(5,3),F(21,2)]:
            local=2*(y-1)/h
            assert local**2*(y+1)**2 == 4*(y*y-1)**2/delta
            assert local**2 <= 4*(y*y-1)**2/delta
            controls+=2
    # Cramer--Rao equality coefficients, and scalar quartic barrier polynomial.
    assert F(1,2)**2==F(1,4)*1
    controls+=1
    for n in range(17):
        x=F(n,32)
        polynomial=4*x**4-8*x*x+4
        assert polynomial==4*(1-x*x)**2 and polynomial>=F(9,4)
        controls+=1
    for eta in [F(1,7),F(2,9),F(3,8)]:
        lower=(4-4/(1+eta))/eta
        upper=(4/(1-eta)-4)/eta
        assert lower==4/(1+eta)<4<upper==4/(1-eta)
        controls+=1
    for B in [F(17),F(99),F(1001)]:
        d=4/(B+2)
        assert 4/d-1==B+1
        assert (d-4/B+8/(B*B))==16/(B*B*(B+2))
        controls+=2
    # Solve moments from scratch; do not import producer or its parameter map.
    for t in [F(1,101),F(1,257),F(1,997)]:
        mass=t**19; variance=t**-8; target=1+t*t
        core_variance=(1-mass*variance)/(1-mass)
        core_fourth=(target-3*mass*variance**2)/((1-mass)*core_variance**2)
        assert 1<core_fourth<3
        assert (1-mass)*core_variance+mass*variance==1
        assert (1-mass)*core_variance**2*core_fourth+3*mass*variance**2==target
        assert mass*15*variance**3==15/t**5
        assert mass*(3*variance**2-16)/(t**4)==3/t-16*t**15
        controls+=5
    faults=['local_scale','weight','energy','mean_correction','virial','eigen_energy','jump','budget_shift','gaussian_fourth','gaussian_sixth']
    for fault in faults:
        got=call('--fault',fault)
        assert got.returncode==1 and got.stdout.startswith('ASSERTION:') and 'Traceback' not in got.stderr, 'input fault was not assertion-detected: '+fault+' '+got.stdout+got.stderr
        print('[DETECTED mathematical-input fault]', fault, got.stdout.strip())
    reporting=['balanced_signs_without_extra_assumption','unconditional_zero_extension_H1','uniform_high_moment_transfer','next_coefficient','gu_physics']
    for fault in reporting:
        got=call('--report-fault',fault)
        assert got.returncode==1 and got.stdout.startswith('ASSERTION: scope reporting:') and 'Traceback' not in got.stderr, 'reporting fault was not assertion-detected: '+fault
        print('[DETECTED reporting fault]', fault, got.stdout.strip())
    print(f'PASS K1858 independent probe: {controls} rational controls; {len(faults)} mathematical-input faults; {len(reporting)} reporting faults; clean baseline first')

if __name__=='__main__':
    main()
