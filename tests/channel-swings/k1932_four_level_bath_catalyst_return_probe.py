"""Separate rational transport reconstruction, plus producer input-fault controls."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,hashlib
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
p=HERE/'k1932_four_level_bath_catalyst_return.py'
spec=importlib.util.spec_from_file_location('producer',p);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)

def independently_transport(l,N,t,c,refined=False):
    # Reconstruct joint bath/catalyst populations directly, without shell matrices.
    m=4*l;d=2*N+2*m-3;S=[m-1+2*i for i in range(N)];Z=sum(t**b for b in range(m));out=[F(0)]*d
    for n in S:
        for b in range(m):
            e=b%2;a=b//2;w=t**b/(Z*N)
            if a<l:dest=[n-2*a,n-2*a-2]
            else:
                a-=l;dest=[n+2*l-2*a+2*e-1,n+2*l-2*a+2*e-3]
            if refined and sum(n+b-bb in S for bb in range(m))==1:
                dest=[n,n+b-(b^1)]
            out[dest[0]]+=c*w;out[dest[1]]+=(1-c)*w
    return sum(abs(x-(F(1,N) if a in S else 0)) for a,x in enumerate(out))/2

def main():
    n=0
    for l in (1,2,3,4):
        for N in (l,2*l,7*l):
            for t in (F(1,2),F(2,3)):
                for c in (F(1,2),F(1)):
                    r=independently_transport(l,N,t,c);u=t*t;Z=sum(t**b for b in range(4*l))
                    # Finite geometric sum evaluated separately by integer indices.
                    L=sum((2*a+2-2*c)*t**(2*a) for a in range(l))*(1+t)/(2*Z)
                    assert r==u**l/(1+u**l)+L/N;n+=1
    assert independently_transport(1,2,F(1,2),F(1,2))==F(2,5);n+=1
    # The claimed growing-bath return is not free: initial mean energy is exact.
    for l,N in ((1,2),(2,4),(3,21)):
        m=4*l;assert sum(F(m-1+2*i,N) for i in range(N))==m+N-2;n+=1
    for N in range(1,9):
        for t in (F(1,2),F(2,3),F(3,4)):
            pH=t*t/(1+t*t)
            for c in (F(1,2),F(1)):
                assert independently_transport(1,N,t,c,True)==pH*(1-F(1,N))+(1-c)/N;n+=1
    baseline=mod.report();stored=json.loads((ROOT/'lab/process/k1932-four-level-bath-catalyst-return.json').read_text())
    assert baseline==stored;n+=1
    assert stored['script_sha256']==hashlib.sha256(p.read_bytes()).hexdigest();n+=1
    caught=[]
    for fault in ('phase','pair','bath','normalization'):
        try:mod.calculate(fault)
        except AssertionError:caught.append(fault)
        else:raise AssertionError('undetected actual input fault '+fault)
    altered=dict(stored);altered['examples']=[]
    assert altered!=baseline;n+=1
    altered=dict(stored);altered['script_sha256']='0'*64
    assert altered!=baseline;n+=1
    print(json.dumps({'independent_exact_controls':n,'mathematical_input_faults_rejected':caught,'report_faults_rejected':1,'pin_faults_rejected':1,'baseline':'green','universal_scope':'analytic, not inferred from finite controls'}))
if __name__=='__main__':main()
