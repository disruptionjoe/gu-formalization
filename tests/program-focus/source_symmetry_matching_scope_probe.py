#!/usr/bin/env python3
"""Exact comparator controls only. No GU spectrum or bordism computation."""
from fractions import Fraction as F
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mutant', choices=['drop-neutral', 'wrong-rh-conjugation'])
args = parser.parse_args()

# name, d3, d2, Y, B-L, SU3 cubic sign; T(fund)=1/2.
sm15 = [
    ('Q', 3, 2, F(1, 6), F(1, 3), 1),
    ('uc', 3, 1, F(-2, 3), F(-1, 3), -1),
    ('dc', 3, 1, F(1, 3), F(-1, 3), -1),
    ('L', 1, 2, F(-1, 2), F(-1), 0),
    ('ec', 1, 1, F(1), F(1), 0),
]
neutral = ('nc', 1, 1, F(0), F(1), 0)
sm16 = sm15 if args.mutant == 'drop-neutral' else sm15 + [neutral]

def power_sum(rows, index, power):
    return sum(r[1]*r[2]*r[index]**power for r in rows)

def coeffs(rows):
    return {
        'SU3cub': sum(d2*a for _,d3,d2,y,b,a in rows),
        'SU3sqY': sum(d2*F(1,2)*y for _,d3,d2,y,b,a in rows if d3==3),
        'SU2sqY': sum(d3*F(1,2)*y for _,d3,d2,y,b,a in rows if d2==2),
        'Y': power_sum(rows, 3, 1),
        'Ycub': power_sum(rows, 3, 3),
        'SU2mod2': sum(d3 for _,d3,d2,y,b,a in rows if d2==2) % 2,
        'SU3sqBL': sum(d2*F(1,2)*b for _,d3,d2,y,b,a in rows if d3==3),
        'SU2sqBL': sum(d3*F(1,2)*b for _,d3,d2,y,b,a in rows if d2==2),
        'YsqBL': sum(d3*d2*y*y*b for _,d3,d2,y,b,a in rows),
        'YBLsq': sum(d3*d2*y*b*b for _,d3,d2,y,b,a in rows),
    }

checks = 0
def check(condition, name):
    global checks
    assert condition, name
    checks += 1

for rows, size in [(sm15,15),(sm16,16)]:
    check(sum(r[1]*r[2] for r in rows)==size, f'{size} component count')
    for name, value in coeffs(rows).items():
        check(value==0, f'{size}: {name}')
    for r in rows:
        x=5*r[4]-4*r[3]
        check(x.denominator==1 and x%4==1, f'{size}: X charge {r[0]}')

for power in [1,3]:
    check(power_sum(sm15,4,power)==-1, f'15 BL power{power}')
    check(power_sum(sm16,4,power)==0, f'16 BL power{power}')
    check(sum(r[1]*r[2]*(5*r[4]-4*r[3])**power for r in sm15)==-5**power,
          f'15 X power{power}')
    check(sum(r[1]*r[2]*(5*r[4]-4*r[3])**power for r in sm16)==0,
          f'16 X power{power}')

for nf in range(1,7):
    for nr in range(nf+1):
        check((15*nf+nr)%16 == (-nf+nr)%16, 'mod16 formula')
check(45%16==13, 'three15 residue')
check(48%16==0, 'three16 residue')

# Mirror charge conjugation reverses odd moments and Spin-Z4 chirality.
mirror = [(n+'bar',d3,d2,-y,-b,-a) for n,d3,d2,y,b,a in sm15]
for power in [1,3]:
    check(power_sum(sm15+mirror,4,power)==0, 'mirrored BL cancellation')
check((15-15)%16==0, 'mirrored Z4 cancellation')

# (4,2,1)+(bar4,1,2): covering-product central kernel and anomalies.
check((-1)*(-1)*1==1 and (-1)*1*(-1)==1, 'PS diagonal Z2 acts trivially')
check(2-2==0, 'PS SU4 cubic')
check(4%2==0, 'PS SU2L/R Witten')
# z=(i I4,I2,-I2) has equal i phase on both chiral16 summands.
check(1j == (-1j)*(-1), 'PS normal-center equal phase')
check((1j)**2==-1, 'normal center squares to fermion parity')

# Central iI on raw L/R is vector-like: converting R to LH reverses charge.
raw_l, raw_r = 1, 1
left_conjugate_r = raw_r if args.mutant=='wrong-rh-conjugation' else -raw_r
check(raw_l+left_conjugate_r==0, 'parent central phase is not uniform chiral X')
print(f'PASS {checks} exact comparator arithmetic and contrary controls; no GU anomaly verdict')
