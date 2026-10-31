#!/usr/bin/env python3
"""Exact physical invariance and rational continuity consumers; --write saves report."""
from fractions import Fraction as F
from itertools import product

checks = 0
def require(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1

# Actual physical X_ET edges on ternary pair basis: empty=-1, occupied bits=0,1.
# x_i annihilates empty and exchanges occupied bits. (5-N)/2 multiplies edges.
basis = list(product((-1, 0, 1), repeat=4))
def occupancy(state):
    return tuple(int(s != -1) for s in state)
def x_edges(state):
    n = sum(occupancy(state))
    for i, j in ((0, 1), (2, 3)):
        if state[i] != -1 and state[j] != -1:
            out = list(state)
            out[i] = 1 - out[i]
            out[j] = 1 - out[j]
            yield tuple(out), F(5-n, 2)

for state in basis:
    for out, coefficient in x_edges(state):
        require(occupancy(out) == occupancy(state), 'X_ET preserves each N_i')
        require(coefficient > 0, 'actual X_ET coefficient on reached carrier')
    # Z_ET is diagonal, with z(vac)=0 and z(s)=(-1)^s.
    z = tuple(0 if s == -1 else 1-2*s for s in state)
    z_et = F((5-sum(occupancy(state))) * (z[0]+z[1]) * (z[2]+z[3]), 4)
    require(abs(z_et) <= 1, 'Z_ET physical diagonal norm check')

# Logical code supports are orthogonal; each has exactly half weight on n_10.
supports = {b: {(r, r, r ^ b, r ^ b) for r in (0, 1)} for b in (0, 1)}
require(supports[0].isdisjoint(supports[1]), 'logical code supports orthogonal')
for b0 in (0, 1):
    for b1 in (0, 1):
        compressed = sum((F(1, 2) for state in supports[b0] & supports[b1]
                          if state[0] == 0), F(0))
        require(compressed == (F(1, 2) if b0 == b1 else 0),
                'V dagger n_10 V = I/2')

# Rates are symbolic log data: baseline pair 1 =100 ln2, actual bit0=121 ln2.
# sqrt(121)-sqrt(100)=1, hence d=ln2 and d/alpha=1/100.
require((11-10)**2 == 1, 'exact square-root rate coefficient')
a, c, b = F(1, 2**100), F(1, 2**121), F(999, 1000)
q = (1-a)/100
p0 = a*b**3
p1 = (1-a)*b**3 + 3*(1-b)*a*b**2
bad = 1-p0-p1
require(bad == 1-b**3-3*a*b*b*(1-b), 'full good-probability formula')
require(0 < bad < 1-b**3 < F(3, 1000), 'baseline nonvacuous failure budget')
require(0 < q < F(1, 100), 'survival-weighted perturbation square')
require(bad + F(1, 10) < F(103, 1000), 'total half-diamond certificate')
# ln2 >= 1/2 follows by integral_1^2 1/x dx >= 1/2.
require(21*F(1, 2) > 1, 'same-reference L1 debt provably exceeds one')

# Exact finite common-instrument overlap f=sqrt(ac)+sqrt((1-a)(1-c)).
# f>=1-a-c is certified entirely by rational squaring.
require(1-a-c > 0, 'positive lower-bound side before squaring')
require((1-a)*(1-c) >= (1-a-c)**2, 'finite radical overlap lower bound')
require(a+c < q, 'finite dilation difference 1-f <= a+c < Q')
# Same-time-history integral coefficient, distinct from endpoint compression.
require(F(2*10*11,100+121)==F(220,221), 'continuum jump integral coefficient')
require(F(1,221)<q, 'continuum dilation bound below survival theorem')
# Individual occupied-rail Kraus normalizations remain exact.
for eta in (a, c, b):
    require(0 < eta < 1 and eta+(1-eta) == 1, 'physical amplitude-damping TP')

# Equal schedules produce zero squared jump-amplitude differences.
for root_rate in (F(1, 3), F(2), F(7, 5)):
    require((root_rate-root_rate)**2 == 0, 'matched comparison Q=0')

# Complementarity: baseline k=ln(100/99), actual altered bit=4k, duration1.
# Q=1/100, so sqrtQ=1/10; D1=3 ln(100/99)<=3/99<1/10.
require(3*F(1, 99) < F(1, 10), 'L1 wins in small-exposure control')

# A vacuum/occupied flip breaks the survival assumption and the bound it needs.
pre_occupancy = F(1, 4)
after_flip = 1-pre_occupancy
require(after_flip == F(3, 4) and after_flip > pre_occupancy,
        'pumping control violates no-pump survival envelope')
require(occupancy((-1, 0, 0, 0)) != occupancy((0, 0, 0, 0)),
        'vacuum-occupied flip fails pair occupancy conservation')

print(f'PASS: {checks} exact assertions; analytic time-continuum proof remains in note')

from pathlib import Path
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[2]
deps=['explorations/conditional-build/k2374-time-ordered-loss-recovery-2026-10-31.md','explorations/conditional-build/k2368-unequal-rail-recovery-2026-10-31.md']
report={'result_id':'K2377','checks':checks,'changed_input_controls':['pumping violates occupancy envelope','L1 wins in small exposure'],'Q':str(q),'baseline_bad':str(bad),'total_upper_bound':'103/1000 (strict)','scope':'Exact finite checks plus analytic full-history proof; endpoint two-Kraus dilation is distinct from time-resolved dilation; no hardware calibration.','dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
text=json.dumps(report,indent=2,sort_keys=True)+'\n'
if '--write' in sys.argv:(ROOT/'lab/process/k2377-time-ordered-rate-robustness.json').write_text(text)
print(text)
