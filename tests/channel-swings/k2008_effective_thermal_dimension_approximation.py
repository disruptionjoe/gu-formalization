"""Exact controls for energy-preserving fixed-spacing finite approximations.

Universal statements are proved in the note. No arbitrary-d census is claimed.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'lab/process/k2008-effective-thermal-dimension-approximation.json'


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def rate(s, p, t):
    inc = [F(0)]*len(s)
    Z = sum(t**b for b in range(4))
    for i, j in combinations(range(len(s)), 2):
        if s[i] > s[j]:
            i, j = j, i
        g = s[j]-s[i]
        if g in (1, 2, 3):
            g = int(g)
            low = sum(t**b for b in range(4-g))/Z
            flow = low*(p[j]-t**g*p[i])
            inc[i] += max(flow, 0)
            inc[j] += max(-flow, 0)
    return sum(max(x-y, 0) for x, y in zip(p, inc))/2


def shells(a, s):
    return all(2*sum(e-x in range(4) for x in s)
               <= sum(e-x in range(4) for x in a)
               for e in {x+b for x in s for b in range(4)})


def min_gap(a):
    a = sorted(a)
    return min(y-x for x, y in zip(a, a[1:]))


def components(a):
    remaining = set(a)
    out = []
    while remaining:
        todo = [min(remaining)]
        block = set(todo)
        remaining.difference_update(block)
        while todo:
            x = todo.pop()
            new = {y for y in remaining if abs(y-x) in (1, 2, 3)}
            block.update(new)
            todo.extend(new)
            remaining.difference_update(new)
        out.append(sorted(block))
    return out


def two_weight_vertex(e, r, budget):
    choices = []
    for i in range(len(e)):
        if e[i] <= budget:
            w = [F(0)]*len(e)
            w[i] = F(1)
            choices.append(w)
    for i, j in combinations(range(len(e)), 2):
        if e[i] == e[j]:
            continue
        wi = (budget-e[j])/(e[i]-e[j])
        if 0 <= wi <= 1:
            w = [F(0)]*len(e)
            w[i], w[j] = wi, 1-wi
            choices.append(w)
    assert choices
    return min(choices, key=lambda w: (dot(w, r), dot(w, e), tuple(w)))


def compress_after_cut(a, s, p, t, N):
    old_e, old_r = dot(s, p), rate(s, p, t)
    assert N > old_e >= 1 and shells(a, s)
    gap = min_gap(a)
    q = sum((v for x, v in zip(s, p) if x > N), F(0))
    low_s = [x for x in s if x <= N]
    low_p = [v for x, v in zip(s, p) if x <= N]
    low_r = rate(low_s, low_p, t)
    kept_a = [x for x in a if x <= N+3]
    normalized = [v/(1-q) for v in low_p]
    assert q <= (old_e-1)/(N-1) < 1
    assert low_r <= old_r+q/2
    assert dot(low_s, normalized) <= old_e
    assert low_r/(1-q) <= old_r+(old_e-1)/(N-old_e)
    assert shells(kept_a, low_s)
    blocks = []
    for block in components(kept_a):
        pairs = [(x, v) for x, v in zip(low_s, normalized) if x in block]
        mass = sum(v for x, v in pairs)
        if mass:
            support = [x for x, v in pairs]
            pops = [v/mass for x, v in pairs]
            blocks.append((block, support, pops, mass))
    energies = [dot(s0, p0) for _, s0, p0, _ in blocks]
    returns = [rate(s0, p0, t) for _, s0, p0, _ in blocks]
    original_weights = [w for _, _, _, w in blocks]
    weights = two_weight_vertex(energies, returns, dot(energies, original_weights))
    assert dot(weights, returns) <= dot(original_weights, returns)
    assert dot(weights, energies) <= dot(original_weights, energies)
    selected_a, selected_s, selected_p = [], [], []
    for (block, support, pops, _), weight in zip(blocks, weights):
        if weight:
            selected_a.extend(block)
            selected_s.extend(support)
            selected_p.extend(weight*v for v in pops)
    offset = min(selected_a)
    selected_a = sorted(x-offset for x in selected_a)
    selected_s = [x-offset for x in selected_s]
    assert len(selected_a) <= 2*N+7
    assert min_gap(selected_a) >= gap and min(selected_a) == 0
    assert shells(selected_a, selected_s) and sum(selected_p) == 1
    assert dot(selected_s, selected_p) <= old_e
    new_r = rate(selected_s, selected_p, t)
    assert new_r <= old_r+(old_e-1)/(N-old_e)
    return dict(N=N, t=t, budget=old_e, tail_mass=q, before_return=old_r,
                after_return=new_r, error_bound=(old_e-1)/(N-old_e),
                original_spectrum=a, original_support=s, original_populations=p,
                final_spectrum=selected_a, final_support=selected_s,
                final_populations=selected_p, original_spacing=gap,
                original_dimension=len(a), final_dimension=len(selected_a),
                populated_components_before=len(blocks),
                populated_components_after=sum(bool(w) for w in weights))


def geometric_return(r, t):
    L = 1/(1+t*t)
    if r >= t*t:
        return (1-L*(r-t*t))/2
    return (1-r+max(r-L*(t*t-r), 0))/2


def produce():
    cases = []
    for seed in range(1, 25):
        count = 2+seed % 5
        N = 6+seed % 4
        a, s, p = [], [], []
        for j in range(count):
            offset = F(j, count+1)
            a.extend(offset+k for k in range(2*N+5))
            support = [offset+1, offset+3, offset+2*N+1]
            pops = [F(40+j), F(2+seed % 5), F(1, seed+10)]
            s.extend(support)
            p.extend(pops)
        total = sum(p)
        p = [v/total for v in p]
        for t in (F(1,7), F(1,2), F(6,7)):
            cases.append(compress_after_cut(sorted(a), s, p, t, N))
    # Same-coset disconnected components; discarded old ground component;
    # a retained supported level exactly at the cutoff; no tail at all.
    special = [
        (list(map(F, list(range(7))+list(range(12,19)))),
         list(map(F, [1,3,13,15])), [F(8,10),F(1,10),F(1,20),F(1,20)], 5),
        (sorted(list(map(F, range(13)))+[F(1,4)+j for j in range(7)]),
         [F(9),F(5,4),F(13,4)], [F(1,100),F(90,100),F(9,100)], 5),
        (list(map(F, range(7))), [F(1),F(3)], [F(3,4),F(1,4)], 3),
        (list(map(F, range(7))), [F(1),F(3)], [F(3,4),F(1,4)], 5),
    ]
    for a, s, p, N in special:
        for t in (F(1,3),F(1,2),F(3,4)):
            cases.append(compress_after_cut(a,s,p,t,N))
    infinite = []
    for r in (F(1,4),F(1,2),F(2,3)):
        E = (1+r)/(1-r)
        for t in (F(1,3),F(1,2),F(3,4)):
            for extra in (3,7):
                N = int(E)+extra
                m = (N+1)//2
                s = [F(2*k+1) for k in range(m)]
                low = [(1-r)*r**k for k in range(m)]
                q = r**m
                exact = geometric_return(r,t)
                low_r = rate(s,low,t)
                p = [v/(1-q) for v in low]
                a = list(map(F,range(N+4)))
                assert sum(low) == 1-q and shells(a,s)
                assert dot(s,p) <= E and low_r <= exact+q/2
                assert rate(s,p,t) <= exact+(E-1)/(N-E)
                infinite.append(dict(r=r,t=t,E=E,N=N,tail_mass=q,
                    exact_infinite_return=exact,finite_return=rate(s,p,t),
                    finite_mean=dot(s,p),finite_dimension=len(a),
                    bound=(E-1)/(N-E)))
    resources=[]
    for E in (F(101,100),F(3,2),F(2),F(7)):
        for epsilon in (F(1,10),F(1,100),F(1,1000)):
            z=E+2*(E-1)/epsilon
            N=-(-z.numerator//z.denominator)
            delta=min(F(1,2),epsilon)
            assert N>E and delta/2+(E-1)/(N-E)<=epsilon
            resources.append(dict(E=E,epsilon=epsilon,N=N,d=2*N+7,delta=delta,
                                  total_error_bound=delta/2+(E-1)/(N-E)))
    inputs = [
        'explorations/conditional-build/k1933-covariant-catalyst-dephasing-reduction-2026-10-22.md',
        'explorations/conditional-build/k1943-arbitrary-preparation-catalyst-energy-2026-10-22.md',
        'explorations/conditional-build/k1950-global-catalyst-energy-certificates-2026-10-22.md',
        'explorations/conditional-build/k1972-thermal-two-component-reduction-2026-10-22.md',
        'explorations/conditional-build/k2006-uniform-two-component-spacing-2026-10-24.md',
    ]
    return dict(result_id='K2008',status='active_research',
        classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',
        physical_cases=cases,infinite_geometric_controls=infinite,
        effective_joint_resources=resources,
        scope='For any feasible positive spacing and 0<t<1, integer N>E>1: '
              '0<=F_(2N+7)-F_infty<=(E-1)/(N-E). Finite-mean countable '
              'nondegenerate catalysts with minimum spacing have the same infimum. '
              'For 0<delta<=1/2 the explicit joint upper error to R_star is '
              'delta/2+(E-1)/(N-E). Written proofs carry universal statements; '
              'finite rational controls do not enumerate all protocols. No '
              'unrestricted attainment, sharp complexity, GU or novelty claim.',
        inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})


def encode(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,list): return [encode(y) for y in x]
    if isinstance(x,dict): return {k:encode(v) for k,v in x.items()}
    return x


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args()
    value=encode(produce())
    if args.write: OUT.write_text(json.dumps(value,indent=2)+'\n')
    else: assert value==json.loads(OUT.read_text())
    print('PASS K2008',len(value['physical_cases']),'physical cases;',
          len(value['infinite_geometric_controls']),'exact infinite-family controls;',
          len(value['effective_joint_resources']),'effective resource choices')
