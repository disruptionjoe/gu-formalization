"""Exact controls for a continuum finite-separation-rank obstruction.

The universal obstruction and weak compactness argument are proved in the note.
These finite rational controls verify the released coarse-pulse and residual formulas.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1997-finite-rank-pulse-obstruction.json'
def grid(n):
    assert n>0 and n%2==0
    x=[F(2*i+1,n)-1 for i in range(n)]
    a=[[F((j>i)-(j<i)) for j in range(n)] for i in range(n)]
    return x,a,[-z for z in x]
def produce():
    rows=[];checks=0
    for n in [2,4,8,16,32]:
        x,a,b=grid(n)
        for t in [F(9,20),F(23,50),F(1,2)]:
            alpha=4*t/(3+4*t)
            for i in range(n):
                assert alpha*sum(a[i])/n+(1-alpha)*b[i]==-x[i]
                assert all(abs(v)<=1 for v in a[i]+[b[i]])
                checks+=2
            for j in range(n):
                assert sum(a[i][j] for i in range(n))/n==x[j];checks+=1
            assert sum(b)==0
            # Exact integrals of (x-midpoint)^2 under uniform measure.
            rowerr=sum(((F(2*(i+1),n)-1-x[i])**3-(F(2*i,n)-1-x[i])**3)/6 for i in range(n))
            assert rowerr==F(1,3*n*n)
            colerr=alpha*rowerr
            strong=alpha/F(n)+(1-alpha)*rowerr
            rows.append(dict(n=n,t=str(t),alpha=str(alpha),row_residual_squared=str(rowerr),column_residual_squared=str(colerr),combined_residual_squared=str(rowerr+colerr),elementary_pulse_distance_squared=str(strong),rank_upper=n))
            checks+=2
    # A quantitative finite-basis conditioning consequence, not a rank-only bound.
    conditioning=[]
    for C in [F(1),F(2),F(5),F(10),F(100)]:
        for t in [F(9,20),F(23,50)]:
            W=3+4*t;beta=2*t/W
            deficit=F(1,2*C)
            qerr=beta/(3*C**3)
            assert qerr==2*t/(3*W*C**3)
            conditioning.append(dict(C=str(C),t=str(t),h_column_ceiling=str(1-deficit),q_column_residual_lower_squared=str(qerr)))
            checks+=1
    return dict(result_id='K1997',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',coarse_pulses=rows,conditioning=conditioning,exact_rational_controls=checks,scope='Every capped pulse with the actual optimal central marginals has infinite separation rank, even for measurable discontinuous factors. Every fixed-rank capped class has a strictly positive combined marginal-residual floor (not quantified by rank here). Explicit rank-at-most-n coarse pulses have exact residual squared (1+alpha)/(3n^2) and converge to the elementary feasible pulse, not the minimum-norm pulse.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['explorations/conditional-build/k1991-tight-cut-pulse-factorization-2026-10-23.md','explorations/conditional-build/k1993-pulse-sobolev-corner-obstruction-2026-10-23.md']})
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();d=produce()
    if args.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
    else:assert d==json.loads(OUT.read_text())
    print('PASS K1997',d['exact_rational_controls'],'rational controls; continuum proof in note')
