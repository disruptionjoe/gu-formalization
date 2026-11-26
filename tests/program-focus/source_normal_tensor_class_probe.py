#!/usr/bin/env python3
"""Exact finite controls for the normal-tensor classification.

Correction 2026-11-26: this legacy fixture tests the PLUS/reversion comparator,
not printed source eq3.27. See source_adjoint_spinless_probe.py for both pairings.

The written proof supplies Lie generation, complete reducibility and the
real-form argument. These finite checks neither construct a physical VEV nor
certify a source action. Matrices are binary-exact Clifford fixtures, not
floating-point rank tests. Run serially.
"""
import argparse
from collections import Counter
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib
import json
import os
import sys
for key in ('OPENBLAS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','OMP_NUM_THREADS'):
    os.environ.setdefault(key,'1')
import numpy as np


def character_counts():
    # SU3 fundamental weights, SU2 highest-weight normalization, integer6Y.
    v=[(1,0,0,-2),(-1,1,0,-2),(0,-1,0,-2),(0,0,1,3),(0,0,-1,3)]
    weights=v+[tuple(-z for z in x) for x in v]
    positive_roots=[(2,-1,0,0),(-1,2,0,0),(1,1,0,0),(0,0,2,0)]
    shifts=[]
    for bits in product((0,1),repeat=4):
        shifts.append(((-1)**sum(bits),tuple(sum(b*r[j] for b,r in zip(bits,positive_roots)) for j in range(4))))
    targets=[(1,0,0,-2),(0,1,0,2),(0,0,1,3),(0,0,1,-3)]
    rows=[]
    for k in range(11):
        char=Counter(tuple(sum(weights[i][j] for i in subset) for j in range(4)) for subset in combinations(range(10),k))
        def multiplicity(lam):
            return sum(sign*char[tuple(lam[j]+s[j] for j in range(4))] for sign,s in shifts)
        rows.append(dict(degree=k,dimension=sum(char.values()),invariants=multiplicity((0,0,0,0)),normal_multiplicity=sum(multiplicity(t) for t in targets)))
    return rows


def auxiliary_scope(root):
    from fractions import Fraction as Q
    from types import SimpleNamespace
    root = Path(root).resolve()
    sys.path.insert(0, str(root / 'tests/program-focus'))
    import source_action_deep_geometry as g
    import source_action_weak_response_probe as w
    from source_action_deep_algebra import add, scale
    from source_action_paired_response_probe import C, I, build_api

    w.configure(root)
    E = w._fast_exact_class()(g)

    def iso(i, j, x):
        H = g.zero()
        H[i][j] = Q(1)
        H[j][i] = -g.eta[i] * g.eta[j]
        act = [g.h_action(H, a) for a in range(14)]
        sp = {}
        for a in range(14):
            for b in range(a + 1, 14):
                z = act[b].get(a, Q(0)) / (2 * g.d[b])
                if z:
                    sp[(1 << a) | (1 << b)] = z
        out = {}
        for (e, c), v in x.items():
            ai = e.bit_length() - 1
            for b in range(14):
                z = -act[b].get(ai, Q(0))
                if z:
                    out[1 << b, c] = out.get((1 << b, c), 0) + v * z
            for cc, z in E.cliff_product(sp, {c: Q(1)}, 'comm').items():
                out[e, cc] = out.get((e, cc), 0) + v * z
        return {k: v for k, v in out.items() if v}

    poly = {0: C(1)}
    for a, b in [(0, 1), (10, 12), (9, 11), (5, 8)]:
        poly = E.cliff_product(poly, {1 << a: C(1), 1 << b: I})
    bs = []
    for mask in range(64):
        zs = [a for j, a in enumerate([2, 3, 4, 6, 7, 13]) if mask >> j & 1]
        if (4 + len(zs)) % 4 not in (0, 3):
            continue
        c = poly
        for a in zs:
            c = E.cliff_product(c, {1 << a: C(1)})
        v = {(1 << a, k): f * x for a, f in [(5, C(1)), (8, I)]
             for k, x in c.items()}
        bs.append(scale(1 / v[min(v)], v))
    assert len(bs) == 36
    h = SimpleNamespace(bs=bs, I=I, rot=iso)
    q = build_api(root, {'C': C, 'E': E, 'h': h})

    def part(s, j, js):
        out = s
        for k in js:
            if k != j:
                out = scale(Q(1, j * (j + 1) - k * (k + 1)),
                            add(q['cas'](out), scale(-k * (k + 1), out)))
        return out

    def witness(v):
        k = min(v) if v else None
        return [list(k), C(v[k]).ser()] if k else None

    report = {'basis_revision': '736d965e076a82608cc8f2d1ca2016612de4142c',
              'scope': 'Exact geometric leakage; no cokernel obstruction, inverse, physical or source verdict.',
              'boost_range': [], 'normal_source': []}
    Vs = [q['K'](3, bs[j]) for j in (5, 12)]
    halfturn_sign = [1, -1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1]
    def halfturn(v):
        out = {}
        for (e, c), z in v.items():
            sign = 1
            for a, s in enumerate(halfturn_sign):
                if e >> a & 1:
                    sign *= s
                if c >> a & 1:
                    sign *= s
            out[e, c] = sign * z
        return out
    report['real_structure_halfturn'] = []
    for V in Vs:
        assert not q['P'](V)
        assert q['cas'](V) == scale(56, V)
        cv = {k: C(z).conj() for k, z in V.items()}
        hv = halfturn(V)
        sign = next(s for s in (1, -1) if hv == scale(s, cv))
        report['real_structure_halfturn'].append(sign)
    report['highest7_range_hermitian_gram'] = [
        [C(E.pair({k: C(z).conj() for k, z in U.items()}, V)).ser() for V in Vs]
        for U in Vs]
    for j, V in zip((5, 12), Vs):
        for a in (0, 1, 2):
            W = iso(a, 3, V)
            W = add(W, scale(-1, q['P'](W)))
            W6 = part(W, 6, [6, 7])
            assert q['cas'](W6) == scale(42, W6)
            report['boost_range'].append({
                'source': j, 'boost': str(a) + '3', 'range_terms': len(W),
                'spin6_terms': len(W6), 'witness': witness(W6)})
            if a != 0:
                continue
            assert not add(iso(0, 2, W6), scale(I, iso(1, 2, W6)))
            for b in (5, 8):
                L = q['P'](q['K'](b, W6))
                L4 = part(L, 4, [4, 5, 6, 7])
                assert q['cas'](L4) == scale(20, L4)
                report['normal_source'].append({
                    'source': j, 'boost': '03', 'normal_source_axis': b,
                    'source_terms': len(L), 'spin4_terms': len(L4),
                    'witness': witness(L4)})
    return report


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--output');args=ap.parse_args()
    root=Path(args.repo).resolve();sys.path.insert(0,str(root/'tests/channel-swings'))
    from actual_sym2_c14_orbit_probe import native_gammas
    checks=[]
    def check(name,condition):
        checks.append({'name':name,'passed':bool(condition)})
        if not condition: raise AssertionError(name)
    rows=character_counts()
    check('exterior dimensions reconstruct full Clifford algebra',all(r['dimension']==comb(10,r['degree']) for r in rows) and sum(r['dimension'] for r in rows)==1024)
    odd=[rows[k]['normal_multiplicity'] for k in (1,3,5,7,9)]
    inv=[rows[k]['invariants'] for k in (0,2,4,6,8,10)]
    check('full SM odd normal multiplicities',[4,8,10,8,4]==odd)
    check('full SM even invariant multiplicities',[1,2,3,3,2,1]==inv)
    check('even normal intertwiners exist but are parity excluded',[rows[k]['normal_multiplicity'] for k in range(0,11,2)]==[0,0,4,4,0,0])
    check('middle odd invariant is outside even target',[rows[k]['invariants'] for k in range(1,10,2)]==[0,0,2,0,0])
    check('dual-degree character symmetry',all(rows[k]['invariants']==rows[10-k]['invariants'] and rows[k]['normal_multiplicity']==rows[10-k]['normal_multiplicity'] for k in range(11)))
    residual=[odd[j]-inv[j]-inv[j+1] for j in range(5)]
    check('gamma-traceless multiplicities',[1,3,4,3,1]==residual)
    check('sharp and C real dimensions',2*sum(odd)==68 and 2*(odd[1]+odd[3])==32)
    check('sharp real image and kernel dimensions',2*sum(inv[j]+inv[j+1] for j in range(5))==44 and 2*sum(residual)==24)
    check('C image and kernel dimensions',2*sum(inv[j]+inv[j+1] for j in (1,3))==20 and 2*(residual[1]+residual[3])==12)
    # Integer hypercharge and exterior parity reject epsilon-only apparent extras.
    charge_cases=[]
    for p,q,pp,qq in product(range(4),range(3),range(4),range(3)):
        for delta in (-2,2,3,-3):
            if -2*(pp-p)+3*(qq-q)==delta and (pp+qq-p-q)%2:
                charge_cases.append((delta,pp-p,qq-q))
    check('hypercharge and oddness force nearest occupation steps',set(charge_cases)=={(-2,1,0),(2,-1,0),(3,0,1),(-3,0,-1)})
    g,eta=native_gammas();eye=np.eye(128,dtype=complex);zero=np.zeros_like(eye);eq=np.array_equal
    def mul(xs):
        z=eye.copy()
        for x in xs:z=z@x
        return z
    H=[9,0,1,2];N=[3,4,5,6,7,8,10,11,12,13]
    K=mul(g[:9]);C=mul([x for x in g if eq(x.conjugate(),-x)])
    h=mul([g[a] for a in H]);n=mul([g[a] for a in N]);om=h@n
    basis=[eye,h,n,om]
    check('actual signature split',sum(eta[a]>0 for a in H)==3 and sum(eta[a]>0 for a in N)==6)
    check('native vectors sharp selfadjoint',all(eq(x.conjugate().T@K,K@x) for x in g))
    check('native quaternionic anti-linear law',eq(C@C.conjugate(),-eye) and all(eq(C@x.conjugate(),x@C) for x in g))
    check('volume squares and commuting factors',eq(h@h,-eye) and eq(n@n,-eye) and eq(om@om,eye) and eq(h@n,n@h))
    check('four volume coefficients independent',all(np.trace(x.conjugate().T@y)==(128 if i==j else 0) for i,x in enumerate(basis) for j,y in enumerate(basis)))
    chi_h=1j*h;chi_n=1j*n
    check('sharp flips horizontal chirality only',eq(chi_h.conjugate().T@K,-K@chi_h) and eq(chi_n.conjugate().T@K,K@chi_n))
    check('C flips both chirality labels and preserves ambient',eq(C@chi_h.conjugate(),-chi_h@C) and eq(C@chi_n.conjugate(),-chi_n@C) and eq(C@om.conjugate(),om@C))
    tensors=[[g[a]@A for a in N] for A in basis]
    check('four real tensors are sharp selfadjoint',all(eq(x.conjugate().T@K,K@x) for alpha in tensors for x in alpha))
    check('four real tensors C-even',all(eq(C@x.conjugate(),x@C) for alpha in tensors for x in alpha))
    check('imaginary four tensors sharp skew and C-odd',all(eq((1j*x).conjugate().T@K,-K@(1j*x)) and eq(C@(1j*x).conjugate(),-(1j*x)@C) for alpha in tensors for x in alpha))
    check('four tensors ambient odd',all(eq(om@x,-x@om) for alpha in tensors for x in alpha))
    for index,(alpha,A) in enumerate(zip(tensors,basis)):
        check(f'normal contraction coefficient {index}',eq(sum((eta[a]*g[a]@x for a,x in zip(N,alpha)),zero.copy()),10*A))
    # Check complete normal vector covariance, including indefinite generators.
    covariance=[]
    for alpha in tensors:
        for i,a in enumerate(N):
            for j,b in enumerate(N):
                if j<=i:continue
                J=g[a]@g[b]/2
                for k,c in enumerate(N):
                    rhs=(eta[b]*alpha[i] if c==b else zero)-(eta[a]*alpha[j] if c==a else zero)
                    covariance.append(eq(J@alpha[k]-alpha[k]@J,rhs))
    check('all normal bivector equivariance equations',all(covariance))
    check('horizontal scalar covariance',all(eq((g[a]@g[b])@x,x@(g[a]@g[b])) for ia,a in enumerate(H) for b in H[ia+1:] for alpha in tensors for x in alpha))
    projectors={(s,t):(eye-s*1j*h)@(eye-t*1j*n)/4 for s,t in product((-1,1),repeat=2)}
    check('joint volume projectors rank32 and complete',eq(sum(projectors.values(),zero.copy()),eye) and all(eq(P@P,P) and np.trace(P)==32 for P in projectors.values()))
    rank_counts=Counter()
    for a,b,c,d in product((-1,0,1),repeat=4):
        A=1j*(a*eye+b*h+c*n+d*om)
        nonzero=0
        for (s,t),P in projectors.items():
            lam=1j*(a+1j*b*s+1j*c*t-d*s*t)
            check(f'joint eigenvalue {a,b,c,d,s,t}',eq(A@P,lam*P))
            nonzero+=int(lam!=0)
        rank=32*nonzero;rank_counts[rank]+=1
        check(f'opposite blocks paired {a,b,c,d}',rank in (0,64,128))
    # A real degree-three SM-compatible tensor survives in the block-only class:
    # theta = (color Kahler 2-form)^2. Geometric weak acts on disjoint N4.
    pairs=[(3,4),(5,6),(7,8)]
    theta=sum((2*mul([g[a],g[b],g[c],g[d]]) for (a,b),(c,d) in combinations(pairs,2)),zero.copy())
    alpha=[(g[a]@theta-theta@g[a])/2 for a in N] # Clifford interior for degree4
    check('nonzero real degree3 block control',any(not eq(x,zero) for x in alpha))
    check('block control is sharp skew and C-even',all(eq(x.conjugate().T@K,-K@x) and eq(C@x.conjugate(),x@C) for x in alpha))
    check('degree3 contraction is four theta',eq(sum((eta[a]*g[a]@x for a,x in zip(N,alpha)),zero.copy()),4*theta))
    check('block control not full normal invariant',not eq((g[3]@g[10])@theta,theta@(g[3]@g[10])))
    evidence={'basis_revision':'736d965e076a82608cc8f2d1ca2016612de4142c','checks':checks,'character_rows':rows,'odd_multiplicities':odd,'even_invariants':inv,'clifford_covariance_equations':len(covariance),'fixture_rank_counts':dict(rank_counts),'dimensions':{'block_complex':[68,24,44],'block_sharp_real':[68,44,24],'block_sharp_C_real':[32,20,12],'endogenous_weak_sharp_real':[4,4,0],'endogenous_weak_sharp_C_real':[0,0,0]},'scope':'fixed pointwise tensor isotropy; not a moving reduction/VEV, W2 pairing, physical spectrum or GU verdict','input_sha256':{p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in ['tests/channel-swings/actual_sym2_c14_orbit_probe.py','explorations/conditional-build/weak-endogenous-grading-2026-11-24.md','explorations/conditional-build/source-reality-mixing-class-2026-11-24.md']}}
    evidence['auxiliary_scope']=auxiliary_scope(root)
    if args.output:Path(args.output).write_text(json.dumps(evidence,indent=2)+'\n')
    print(f'PASS {len(checks)} exact controls; {len(covariance)} vector equations; class68R/32R ->4R/0R')

if __name__=='__main__':main()
