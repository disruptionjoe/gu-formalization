#!/usr/bin/env python3
"""K2397 exact finite fixtures. Universal statements use the note's proofs."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb
import argparse
import hashlib
import json
from pathlib import Path

@lru_cache(None)
def pmf(n, p):
    return tuple(F(comb(n,k))*p**k*(1-p)**(n-k) for k in range(n+1))

@lru_cache(None)
def tails(n,p):
    probs=pmf(n,p)
    lo=[]
    total=F(0)
    for x in probs:
        total+=x
        lo.append(total)
    return tuple(lo), tuple(1-lo[k]+probs[k] for k in range(n+1))

def interval(n,k,epsilon,grid):
    lower=max([F(0)]+[g for g in grid if tails(n,g)[1][k]<=epsilon])
    upper=min([F(1)]+[g for g in grid if tails(n,g)[0][k]<=epsilon])
    return lower,upper

def endpoint_mean(values,env,r):
    n1=sum(env); n0=len(env)-n1
    s1=sum((v for v,c in zip(values,env) if c),F(0))
    s0=sum((v for v,c in zip(values,env) if not c),F(0))
    if not n1:return s0/n0
    if not n0:return s1/n1
    if r is None:return s1/n1  # +infinity
    return (r*s1+s0)/(r*n1+n0)

def normalizer(values,env,low,high):
    return max(endpoint_mean(values,env,low),endpoint_mean(values,env,high))

def run(root):
    checks={}
    grid=tuple(F(j,12) for j in range(13))
    epsilon=F(1,400)
    coverage_checks=0
    for n in (1,2,6,20,100):
        bounds=[interval(n,k,epsilon,grid) for k in range(n+1)]
        assert all(lo<=hi for lo,hi in bounds)
        # These finite checks complement the all-real-p proof.
        for p in (F(j,48) for j in range(49)):
            lower_error=sum((v for v,(lo,hi) in zip(pmf(n,p),bounds) if p<lo),F(0))
            upper_error=sum((v for v,(lo,hi) in zip(pmf(n,p),bounds) if p>hi),F(0))
            assert lower_error<=epsilon and upper_error<=epsilon
            coverage_checks+=1
    checks['rational_true_parameter_coverage_cases']=coverage_checks
    bounds=interval(100,50,epsilon,grid)
    assert bounds==(F(1,3),F(2,3))
    assert tails(100,F(1,3))[1][50]<=epsilon
    assert tails(100,F(5,12))[1][50]>epsilon
    assert tails(100,F(2,3))[0][50]<=epsilon
    assert tails(100,F(7,12))[0][50]>epsilon
    lo_p,hi_p=bounds;lo_q,hi_q=bounds
    rlo=lo_q*(1-hi_p)/(hi_p*(1-lo_q))
    rhi=hi_q*(1-lo_p)/(lo_p*(1-hi_q))
    assert (rlo,rhi)==(F(1,4),F(4))
    checks['training_fixture']={'n_each':100,'count_each':50,'interval':[str(x) for x in bounds],'odds_interval':[str(rlo),str(rhi)],'delta':'1/100'}
    normalizer_cases=0
    # Actual shared-label conditional distributions, including same-env pools.
    for n in (2,3,4):
        for env in product((0,1),repeat=n):
            for values in product((F(0),F(1),F(2)),repeat=n):
                c=normalizer(values,env,rlo,rhi)
                for r in (rlo,F(1,2),F(1),F(2),rhi):
                    assert endpoint_mean(values,env,r)<=c
                assert c in (endpoint_mean(values,env,rlo),endpoint_mean(values,env,rhi))
                normalizer_cases+=1
    checks['shared_environment_normalizer_cases']=normalizer_cases
    assert normalizer((F(1),F(0),F(0)),(1,1,0),rlo,rhi)==F(4,9)
    assert normalizer((F(0),F(0),F(1)),(1,1,0),rlo,rhi)==F(2,3)
    assert normalizer((F(1),F(0),F(0)),(1,1,0),F(0),None)==F(1,2)
    assert normalizer((F(1),F(0),F(0)),(1,1,1),F(0),None)==F(1,3)
    assert interval(100,0,epsilon,grid)[0]==0
    assert interval(100,100,epsilon,grid)[1]==1
    checks['unbounded_odds_and_same_environment_controls']=4
    alpha,delta=F(1,20),F(1,100)
    eta=(alpha-delta)/(1-delta)
    threshold=1/eta
    assert eta==F(4,99) and threshold==F(99,4)
    assert delta+(1-delta)*eta==alpha
    assert delta+(1-delta)*alpha>alpha
    assert (1-delta)*1+delta*(1/delta)==2-delta>1
    checks['total_error_budget']={'alpha':str(alpha),'delta':str(delta),'conditional_eta':str(eta),'threshold':str(threshold)}
    # Evaluate the SAME symmetric bonus rule for ALL possible science labels.
    def factors(scores,env):
        maxima=[i for i,v in enumerate(scores) if v==max(scores)]
        b=tuple(F(int(len(maxima)==1 and i==maxima[0])) for i in range(len(scores)))
        c=normalizer(b,env,rlo,rhi)
        return tuple(F(1,4)+F(3,4)*(v/c if c else 0) for v in b)
    assert factors((4,1,1),(1,1,0))==(F(31,16),F(1,4),F(1,4))
    assert factors((1,1,4),(1,1,0))==(F(1,4),F(1,4),F(11,8))
    assert factors((4,4,1),(1,1,0))==(F(1,4),)*3
    for scores in ((4,1,1),(1,1,4),(4,4,1)):
        for r in (rlo,F(1),rhi):
            assert endpoint_mean(factors(scores,(1,1,0)),(1,1,0),r)<=1
    high,low=F(31,16),F(1,4)
    cells=tuple(map(F,(-1,)))+(F(-3,4),F(-1,2),F(0),F(1,2),F(3,4),F(1))
    ev=[]
    for theta in cells:
        e=F(1)
        for x,y in ((1,1),(1,-1))+((0,4),)*6:
            e*=factors(((F(y)-theta*F(x))**2,F(1,4),F(1,4)),(1,1,0))[0]
        ev.append(e)
    cert=low*high**7
    separate=low**2*high**6
    assert min(ev)==cert>threshold
    assert low*high**6<threshold and separate<threshold
    checks['continuous_graph_fixture']={'cells_and_endpoints':len(cells),'shared_minimum':str(cert),'separate_minima_product':str(separate),'exposures':48,'environment_training_observations':200}
    # Model-compatible independent training plug-in failure.
    assert pmf(2,F(1,2))[1]*pmf(2,F(3,4))[1]==F(3,16)>0
    actual_mass=F(3,7)
    assert actual_mass/F(1,3)==F(9,7)>1
    assert F(4,9)/F(2,5)==F(10,9)>1
    # Distinguished-label fitting gives 3 on every realized label.
    assert all(1/normalizer(tuple(F(int(i==j)) for i in range(3)),(1,1,1),rlo,rhi)==3 for j in range(3))
    # Drift beyond learned r=4 loses normalization at r=9.
    assert endpoint_mean((F(9,4),F(0),F(0)),(1,1,0),F(9))==F(81,76)>1
    checks['finite_counterexample_assumption_controls']=6 # plug-in, odds, label, drift, omitted delta, unconditional e-process
    support={(0,0),(1,-3),(-1,3),(1,-5),(-1,5),(0,1),(0,-1)}
    assert all((-x,-y) in support for x,y in support)
    for err,z in (((1,-3),(1,1)),((1,-5),(1,-1)),((0,0),(0,4))):
        assert err in support and (err[0],4+err[1])==z
    assert tuple(F(a-b,2) for a,b in zip((0,1),(0,0)))==(0,F(1,2))
    checks['synthetic_finite_symmetric_support']=True
    deps=['lab/process/k2394-robust-pool-sequential-evidence.json','lab/process/k2391-shifted-sequential-calibration.json']
    return {'result':'K2397','status':'pass','evidence_kind':'Exact binomial, shared-environment normalizer and continuous-graph fixtures; universal coverage and anytime claims are proved in the note, not inferred from finite counts','checks':checks,'dependencies':{p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in deps}}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2])
    parser.add_argument('--report',type=Path)
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args()
    report=run(args.repo)
    output=json.dumps(report,indent=2,sort_keys=True)+'\n'
    if args.report:args.report.write_text(output)
    elif args.write:(args.repo/'lab/process/k2397-finite-training-shift-confidence.json').write_text(output)
    print(output,end='')
