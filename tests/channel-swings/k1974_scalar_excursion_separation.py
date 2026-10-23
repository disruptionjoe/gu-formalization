"""All measurable cuts reduce to a left-side interval for the fixed phase.

The analytic relaxed-control/subgradient proof carries the continuum claim;
finite exact grid subsets test the actual capacity and rearrangement data.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json
import k1969_scalar_continuum_separation as old
import k1963_effective_scalar_cut_certificates as prior
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1974-scalar-excursion-separation.json';M=F(23,100)
def positive_area(a,b,h):
    if min(a,b)>=0:return h*(a+b)/2
    if max(a,b)<=0:return F(0)
    return h*max(a,b)**2/(2*abs(b-a))
def capacity(bits,h):
    s=h*sum(bits);W=F(0);area=F(0)
    for b in bits:
        V=W+h*(2*b-1);area+=positive_area(W,V,h);W=V
    area+=max(F(0),2*s-3)**2/2
    return 9*s-area

def calculate(n=12):
    h=F(3,n);l,r=old.isolate();t=(l+r)/2;lam=old.poly(old.D,t)/old.poly(old.K,t)
    values=[prior.phi0_integral(-3+i*h,-3+(i+1)*h)-lam*sum(old.green(-3+(i+1)*h,z)-old.green(-3+i*h,z) for z in [-t,t]) for i in range(n)]
    best={0:F(0)};witness={0:[]}
    for size in range(1,n+1):
        candidates=[]
        for start in range(n-size+1):
            bs=[int(start<=i<start+size) for i in range(n)];D=sum(v*b for v,b in zip(values,bs))-M*capacity(bs,h)/2;candidates.append((D,start))
        best[size],start=max(candidates);witness[size]=[str(-3+start*h),str(-3+(start+size)*h)]
    for mask in range(1<<n):
        bits=[(mask>>i)&1 for i in range(n)];D=sum(v*b for v,b in zip(values,bits))-M*capacity(bits,h)/2
        assert D<=best[sum(bits)],'same-mass interval dominates every left grid cut'
    assert 1-F(7,100)/2>M
    assert -1+F(7,100)/2<0
    # Full cut reduction: remove paired points, then fold all surviving pairs left.
    nfull=10;hf=F(6,nfull)
    vf=[prior.phi0_integral(-3+i*hf,-3+(i+1)*hf)-lam*sum(old.green(-3+(i+1)*hf,z)-old.green(-3+i*hf,z) for z in [-t,t]) for i in range(nfull)]
    def cap(bs):return old.capacity([(-3+i*hf,-3+(i+1)*hf) for i,b in enumerate(bs) if b])
    def demand(bs):return sum(v*b for v,b in zip(vf,bs))
    for mask in range(1<<nfull):
        A=[(mask>>i)&1 for i in range(nfull)]
        B=[a*(1-A[-1-i]) for i,a in enumerate(A)]
        C=[max(B[i],B[-1-i]) if i<nfull//2 else 0 for i in range(nfull)]
        assert demand(A)==demand(B)<=demand(C),'antisymmetry and positive-side folding'
        assert cap(C)<=cap(B)<=cap(A),'submodular removal and convex excursion folding'
    return dict(result_id='K1974' ,status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',grid_count=n,exact_grid_controls=1<<n,full_grid_controls=1<<nfull,energy_formula='4+2D(t)^2/K(t)',energy_interval=json.loads((ROOT/'lab/process/k1969-scalar-continuum-separation.json').read_text())['energy_interval'],surrogate_t=str(t),surrogate_lambda=str(lam),interval_witnesses=witness,scope='All measurable cuts pass for exact K1969 phase by submodular removal, convex reflection folding and unimodal interval domination. Full measurable-pulse minimum equals the unique halfcut phase energy; pulse existence, not explicit smooth pulse bytes. Rational grids are controls only.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1969-scalar-continuum-separation.json','lab/process/k1971-scalar-all-cut-optimizer.json','tests/channel-swings/k1969_scalar_continuum_separation.py','tests/channel-swings/k1963_effective_scalar_cut_certificates.py']})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=calculate();v['interval_witnesses']={str(k):x for k,x in v['interval_witnesses'].items()}
    if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
    else:assert v==json.loads(OUT.read_text())
    print('PASS K1974',v['exact_grid_controls'],'exact grid-subset comparisons; continuum via subgradient proof')
