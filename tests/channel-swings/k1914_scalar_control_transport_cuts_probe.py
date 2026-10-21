"""Independent rational network feasibility and exact strip geometry controls."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
N=0
def ck(v,label):
    global N
    assert bool(v),label
    N+=1

def independent(demand=(1,2,-2,-1), flux=3):
    # On this tree, every zero-column flow is (a,-a,b,-b,c,-c).
    a=demand[0];b=demand[0]+demand[1];c=sum(demand[:3])
    edge=[a,-a,b,-b,c,-c]
    ck(sum(demand)==0,'global zero area')
    ck(max(map(abs,edge))==flux,'unique tree primal optimum')
    ck(sum(demand[:2])==3,'bottleneck numerator')
    edges=[(0,0),(1,0),(1,1),(2,1),(2,2),(3,2)]
    best=F(0)
    for mask in range(16):
        A={i for i in range(4) if mask>>i&1};num=abs(sum(demand[i] for i in A))
        # Minimize B one column at a time, independent of producer's all-cut loop.
        cut=0
        for j in range(3):
            left=sum(i in A for i,k in edges if k==j);right=sum(i not in A for i,k in edges if k==j)
            cut+=min(left,right)
        if cut:best=max(best,F(num,cut))
        else:ck(num==0,'zero cut balance')
    ck(best==3,'eliminated-column dual optimum')
    # Rational trapezoid areas for actual continuous half-cut and saturating pulse.
    for L,d in [(F(1),F(2)),(F(1),F(3)),(F(2),F(5))]:
        cap=L*L/2+L*(d-2*L)+L*L/2
        rowarea=L*(d-L)
        ck(cap==rowarea,'long-cut exact area and primal equality')
    for d in [F(1,3),F(1),F(3,2)]:
        ck(2*(d/2)*(d/2)/2==d*d/4,'short cut two triangles')
    # Local finite row constraints all pass at m=1 although the cut fails.
    ck(all(abs(v)<=deg for v,deg in zip(demand,[1,2,2,1])),'planted false local feasibility')
    ck(abs(sum(demand[:2]))>1,'global obstruction rejects local-only test')

def caught(fn,label):
    try:fn()
    except AssertionError as exc:ck(bool(str(exc)),label+' real failure');return
    raise AssertionError('missed '+label)
if __name__=='__main__':
    independent()
    caught(lambda:independent(demand=(1,2,-2,0)),'nonzero phase integral')
    caught(lambda:independent(flux=1),'undersized edge capacity')
    r=json.loads((ROOT/'lab/process/k1914-scalar-control-transport-cuts.json').read_text())
    def report(x):
        ck(x['finite_optimum']==3,'report optimum');ck(x['smooth_exact_endpoint']=='strict amplitude slack; fixed compact smooth phase','regularity scope')
        for p,d in x['dependency_sha256'].items():ck(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==d,'dependency bytes')
    report(r)
    caught(lambda:report(dict(r,smooth_exact_endpoint='proved')),'report overclaim')
    bad=json.loads(json.dumps(r));bad['dependency_sha256'][next(iter(bad['dependency_sha256']))]='0'*64;caught(lambda:report(bad),'pin corruption')
    print(json.dumps({'independent_math_baseline':'pass','mathematical_input_faults':2,'report_faults':1,'pin_faults':1,'assertions_including_repeated_baselines':N,'continuum_scope':'analytic separation and coarea proof only'}))
