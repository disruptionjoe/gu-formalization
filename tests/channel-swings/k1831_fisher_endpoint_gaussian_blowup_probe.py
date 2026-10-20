#!/usr/bin/env python3
"""Separate exact score-test and limiting-regime controls, no producer import."""
import json,copy,math
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def moment(n,atoms,variance):
    return sum(w*sum(F(math.comb(n,k))*a**(n-k)*variance**(k//2)*math.prod(range(1,k,2)) for k in range(0,n+1,2)) for w,a in atoms)
def main():
    n=0
    for l in [F(1,4),F(1,2),F(3,4)]:
        for b in [F(1,8),F(1,2),F(1),F(2),F(8)]:
            p=l/(l+b*b);atoms=[(p,-b),(1-p,l/b)];m=[moment(j,atoms,1-l) for j in range(7)]
            assert m[1]==0 and m[2]==1
            k=b*b/l+l/(b*b)-2
            assert m[3]**2==l**3*k and m[4]-3==l*l*(k-2)
            # Cauchy tests: integration-by-parts against u²-1 and u³-3u.
            assert m[4]-1>0 and m[6]-6*m[4]+9>0
            gap=m[3]**2/(m[4]-1) if k>=1 else (m[4]-3)**2/(m[6]-6*m[4]+9)
            assert gap>=l**4/231;n+=1
    # Symmetric counterexample defeats using the skewness test alone.
    atoms=[(F(1,2),F(-1,2)),(F(1,2),F(1,2))]
    assert moment(3,atoms,F(3,4))==0 and moment(4,atoms,F(3,4))-3==F(-1,8)
    # Exact rare-atom controls: weak Gaussian limit loses latent variance, not total Fisher cost.
    for N in [4,16,64]:
        l=F(1,2);b=F(N);p=l/(l+b*b)
        assert p<F(1,N*N) and p*b*b+(1-p)*(l/b)**2==l
        assert 1/(1-l)>1+l**4/231
    # Coordinate counterexample: c=o(delta) does not fix the z scale or select c=0.
    for j in [10,100,1000]:
        d=F(1,j*j);c=d*d
        for z in [d,F(1,2),F(1)]:
            p=c/(c+z*z);assert p*(1-z)**2+(1-p)*(1+c/z)**2==1+c
    # Independent posterior-variance identity with arbitrary positive likelihoods.
    posterior_cases=0
    for weights in [[F(1,3)]*3,[F(1,10),F(9,20),F(9,20)]]:
        for likes in [[F(1),F(2),F(3)],[F(7),F(1,2),F(1,9)]]:
            atoms=[F(-1),F(0),F(1)];rho=sum(w*l for w,l in zip(weights,likes));post=[w*l/rho for w,l in zip(weights,likes)]
            mean=sum(p*a for p,a in zip(post,atoms));var=sum(p*(a-mean)**2 for p,a in zip(post,atoms))
            pair=sum(post[i]*post[j]*(atoms[i]-atoms[j])**2 for i in range(3) for j in range(i+1,3))
            assert var==pair;posterior_cases+=1
    assert posterior_cases==4
    d=json.loads((ROOT/'lab/process/k1831-fisher-endpoint-gaussian-blowup.json').read_text())
    def valid(x):
        r=x['results'];return r['ratio_optimal_iff']=='c/(2-q) -> 0' and r['noise_ratio_limit']=='v/(2-q) -> 1/4' and not r['sharp_subleading_constant_known'] and not r['optimal_displacement_scale_known'] and not r['physical_or_canon_promotion'] and all(x['checks'].values())
    assert valid(d);mut=0
    for k,v in [('ratio_optimal_iff','c=0'),('noise_ratio_limit','v/(2-q) -> 1'),('sharp_subleading_constant_known',True),('optimal_displacement_scale_known',True),('physical_or_canon_promotion',True)]:
        m=copy.deepcopy(d);m['results'][k]=v;assert not valid(m);mut+=1
    m=copy.deepcopy(d);m['checks'][next(iter(m['checks']))]=False;assert not valid(m);mut+=1
    print('PASS 15 independent exact profile controls; symmetric/rare/shape counterexamples; 4 posterior-variance identities; 6 reporting mutations')
if __name__=='__main__':main()
