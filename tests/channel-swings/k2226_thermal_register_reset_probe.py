#!/usr/bin/env python3
"""Exact finite thermal reset controls and rational resource certificates."""
from fractions import Fraction as F
from math import comb
from itertools import product
import json, argparse, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def spectrum_optimum(n,p,w):
    bath=[p**sum(x)*(1-p)**(n-sum(x)) for x in product((0,1),repeat=n)]
    vals=sorted([r*v for r in (1-w,w) for v in bath])
    return sum(vals[:2**n],F(0))

def pair_formula(n,p,w):
    return sum((comb(n,k)*min((1-w)*(1-p)**(n-k)*p**k,
                             w*(1-p)**k*p**(n-k)) for k in range(n+1)),F(0))

def tails(n,p):
    tail=sum((comb(n,k)*p**k*(1-p)**(n-k) for k in range(n//2+1,n+1)),F(0))
    point=comb(n,n//2)*(p*(1-p))**(n//2) if n%2==0 else F(0)
    return tail,point

def parity_formula(n,p,w):
    tail,point=tails(n,p)
    return tail+w*point

def uniform_formula(n,p):
    tail,point=tails(n,p)
    return tail+point/2

def explicit_uniform_channel(n,p):
    # Sort original bath words into designated-qubit sectors, then SWAP.
    d=2**n
    weights=[p**b.bit_count()*(1-p)**(n-b.bit_count()) for b in range(d)]
    order=sorted(range(d),key=lambda b:(-weights[b],b))
    compressed={b:y for y,b in enumerate(order)}
    def image(i,b):
        y=compressed[b]
        return y//(d//2),i*(d//2)+y%(d//2)
    images=[image(i,b) for i in (0,1) for b in range(d)]
    assert len(set(images))==2*d
    eps=uniform_formula(n,p)
    for i,j in product((0,1),repeat=2):
        out=[[F(0),F(0)],[F(0),F(0)]]
        for b,v in enumerate(weights):
            ri,bi=image(i,b); rj,bj=image(j,b)
            if bi==bj: out[ri][rj]+=v
        target=[[1-eps,F(0)],[F(0),eps]] if i==j else [[F(0),F(0)],[F(0),F(0)]]
        assert out==target

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    source=json.loads((ROOT/'lab/process/k2223-stable-detector-resource-realization.json').read_text())
    wa,wb=map(F,source['switch_certificate']['click_probability'])
    assert F(3045489,10**7)<wa<=wb<F(3046040,10**7)
    checks=1
    for n,p,w in product(range(1,8),(F(1,5),F(1,4),F(2,5),F(1,2)),(F(1,10),F(3,10),F(1,2))):
        assert spectrum_optimum(n,p,w)==pair_formula(n,p,w); checks+=1
    for n in range(1,8):
        for w in (F(3045489,10**7),F(3046040,10**7)):
            assert parity_formula(n,F(1,4),w)==spectrum_optimum(n,F(1,4),w); checks+=1
        assert spectrum_optimum(n,F(1,4),F(1,2))==uniform_formula(n,F(1,4)); checks+=1
        assert pair_formula(n,F(1,2),F(3,10))==F(3,10); checks+=1
        assert pair_formula(n,F(0),F(3,10))==0; checks+=1
    for n in range(1,6):
        explicit_uniform_channel(n,F(1,4)); checks+=1
    # Real equation faults: omit even tie mass; use wrong marginal as uniform;
    # drop shell multiplicity; change a joint-spectrum eigenvalue product.
    n=2;p=F(1,4);w=F(3,10)
    reference=spectrum_optimum(n,p,w)
    faults={
        'omit_even_boundary': tails(n,p)[0]!=reference,
        'marginal_is_uniform': parity_formula(n,p,w)!=uniform_formula(n,p),
        'omit_shell_multiplicity':sum((min((1-w)*(1-p)**(n-k)*p**k,w*(1-p)**k*p**(n-k)) for k in range(n+1)),F(0))!=reference,
        'wrong_joint_product':sum((comb(n,k)*min((1-w)*(1-p)**(n-k)*p**k,(1-w)*(1-p)**k*p**(n-k)) for k in range(n+1)),F(0))!=reference,
    }
    assert all(faults.values())
    lo=parity_formula(100,p,F(3045489,10**7));hi=parity_formula(100,p,F(3046040,10**7))
    e100=uniform_formula(100,p);e101=uniform_formula(101,p)
    assert F(35038,10**12)<lo<=hi<F(35042,10**12)
    assert F(43848,10**12)<e100<F(43849,10**12)
    assert F(32580,10**12)<e101<F(32581,10**12)
    assert 1000*e101<F(32581,10**9)
    # Squared Bhattacharyya upper bound is rational at p=1/4.
    for n in range(1,102):
        eps=uniform_formula(n,p)
        assert 4*eps*eps <= (4*p*(1-p))**n
    deps=['explorations/conditional-build/k2226-thermal-register-reset-2026-10-28.md','lab/process/k2223-stable-detector-resource-realization.json','explorations/conditional-build/k2223-stable-detector-resource-realization-2026-10-28.md']
    out=dict(result='K2226',exact_checks=checks+105,equation_faults_detected=faults,
        N100_fixed_bounds=[str(lo),str(hi)],N100_uniform=str(e100),N101_uniform=str(e101),
        probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps})
    if args.write:(ROOT/'lab/process/k2226-thermal-register-reset.json').write_text(json.dumps(out,indent=2)+'\n')
    else:assert json.loads((ROOT/'lab/process/k2226-thermal-register-reset.json').read_text())==out, 'stale certificate; regenerate after final changes'
    print(json.dumps(dict(passed=checks+105,faults_rejected=len(faults))))

if __name__=='__main__': main()
