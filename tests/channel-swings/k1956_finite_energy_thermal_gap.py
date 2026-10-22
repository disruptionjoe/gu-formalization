"""Exact controls for the analytic finite-energy thermal-gap theorem.

Universal claims are proved in the companion note; finite checks do not replace them.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'lab/process/k1956-finite-energy-thermal-gap.json'
CONSTANTS = dict(q='2/3', p='1/9', W='25/8', c='163/440', C='652/34375',
                 lower_exponent='25/16', upper_C='17/50', upper_energy_offset='41/32')


def solve(a, b):
    m = [list(row) + [z] for row, z in zip(a, b)]
    for j in range(len(m)):
        k = next(k for k in range(j, len(m)) if m[k][j])
        m[j], m[k] = m[k], m[j]
        z = m[j][j]
        m[j] = [x / z for x in m[j]]
        for k in range(len(m)):
            if k != j:
                z = m[k][j]
                m[k] = [x - z * y for x, y in zip(m[k], m[j])]
    return [row[-1] for row in m]


def rates(d):
    t = F(1, 2)
    z = sum(t**j for j in range(4))
    return sum(t**j for j in range(4-d))/z, sum(t**j for j in range(d, 4))/z


def matrix_d(gaps, bits):
    n = len(gaps)+1
    a = [[F(i == j) for j in range(n)] for i in range(n)]
    for i, (d, bit) in enumerate(zip(gaps, bits)):
        lo, hi = rates(d)
        if bit == 1:  # low site wins: incoming high = H*p_low-L*p_high
            a[i+1][i] -= hi
            a[i+1][i+1] += lo
        else:
            a[i][i+1] -= lo
            a[i][i] += hi
    return a


def root_family(n):
    q, p = F(2, 3), F(1, 9)
    raw = [q**(n-i) if i <= n else p**(i-n) for i in range(2*n+1)]
    z = sum(raw)
    weights = [x/z for x in raw]
    support = list(range(1, 4*n+2, 2))
    energy = sum(e*x for e, x in zip(support, weights))
    return support, weights, energy, 1/(2*z), z


def calculate(physical=False):
    q, p, W, c, C = [F(CONSTANTS[k]) for k in ['q', 'p', 'W', 'c', 'C']]
    assert C == c/(2*W*W)
    assert F(CONSTANTS['lower_exponent']) == W/2
    assert W == 1+q/(1-q)+p/(1-p)
    qs = [lo/(1+hi) for lo, hi in map(rates, [1, 2, 3])]
    ps = [hi/(1+lo) for lo, hi in map(rates, [1, 2, 3])]
    y1 = ps[0]*(1+ps[2])/(1-ps[0]*ps[2])
    y3 = ps[2]*(1+ps[0])/(1-ps[0]*ps[2])
    assert max(qs) == q and y1 == F(14,55) and y3 == F(3,55)
    assert F(17,8)-F(3,2)-y1 == c and y3 < F(1,8)
    count = 5
    for length in range(5):
        for gaps in product([1,2,3], repeat=length):
            if any(a+b < 4 for a,b in zip(gaps,gaps[1:])):
                continue
            e = [max(1,3-gaps[0]) if gaps else 1]
            for d in gaps:
                e.append(e[-1]+d)
            for bits in product([-1,1], repeat=length):
                a = matrix_d(gaps,bits)
                reward = solve(list(map(list,zip(*a))), [F(1)]*len(e))
                for en,w in zip(e,reward):
                    assert w > 0 and W-w > 0 and (W-w)**2 >= c*c*q**en
                    count += 1
            # Actual weights choose their own orientation; this is required for u<=p.
            for weights in [[F(1,len(e))]*len(e), [F(2**i,2**len(e)-1) for i in range(len(e))]]:
                bits=[1 if rates(d)[1]*weights[i] >= rates(d)[0]*weights[i+1] else -1 for i,d in enumerate(gaps)]
                a=matrix_d(gaps,bits)
                u=[max(F(0),sum(x*y for x,y in zip(row,weights))) for row in a]
                assert all(x<=y for x,y in zip(u,weights))
                assert sum(en*x for en,x in zip(e,u)) <= sum(en*x for en,x in zip(e,weights))
                assert sum(u)>=1/W
                count += 3
    families=[]
    for n in range(16):
        s,w,E,R,z=root_family(n)
        assert z==W-2*q**n-F(1,8)*p**n
        assert E<=2*n+F(41,32)
        moments=lambda r: sum(k*r**k for k in range(1,n+1))
        assert E==1+2*n+2*(moments(p)-moments(q))/z
        assert 0<R-F(4,25)<=F(17,50)*q**n
        # Incoming imbalances independently evaluate the sharp preparation formula.
        inc=[F(0)]*len(s)
        for i in range(len(s)-1):
            lo,hi=rates(2);v=hi*w[i]-lo*w[i+1]
            inc[i]+=max(F(0),-v);inc[i+1]+=max(F(0),v)
        assert sum(max(F(0),x-y) for x,y in zip(w,inc))/2==R
        families.append(dict(n=n,energy=str(E),return_cost=str(R),normalization=str(z)))
        count+=5
    assert 1+2*(p/(1-p)**2-q/(1-q)**2)/W == F(-11,4)
    assert 1/W**2 == F(64,625)
    count+=2
    physical_controls=0
    if physical:
        from k1943_arbitrary_preparation_catalyst_energy import shell_witness
        for n in [0,1,2,3]:
            s,w,E,R,z=root_family(n)
            actual,nc=shell_witness(F(1,2),s,w,list(range(s[-1]+4)))
            assert actual==R
            physical_controls+=nc+1
    inputs={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in [
        'lab/process/k1934-nonuniform-four-level-catalyst-optimization.json',
        'lab/process/k1935-arbitrary-support-thermal-return.json',
        'lab/process/k1943-arbitrary-preparation-catalyst-energy.json']}
    return dict(result_id='K1956',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',
                target_claim='NONE-NOT-A-KILL',constants=CONSTANTS,inputs=inputs,
                exact_controls=count,physical_controls=physical_controls,families=families,
                scope='Fixed t=1/2 exact extreme channel, arbitrary finite nondegenerate catalyst spectra and bounded mean energy. Universal gap proof analytic; logarithmic resource order, not sharp constants or native GU.')


if __name__ == '__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');ap.add_argument('--physical',action='store_true');args=ap.parse_args()
    result=calculate(args.physical)
    if args.write:
        assert args.physical, 'report requires physical consumers'
        OUT.write_text(json.dumps(result,indent=2)+'\n')
    else:
        saved=json.loads(OUT.read_text())
        for k in ['result_id','constants','inputs','families','exact_controls']:
            assert result[k]==saved[k], k
    print('PASS K1956:',result['exact_controls'],'exact controls;',result['physical_controls'],'physical shell controls; universal proof is analytic')
