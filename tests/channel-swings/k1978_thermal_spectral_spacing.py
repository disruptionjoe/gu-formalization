"""Exact spectral compression with closed spacing, and physical upper families."""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json
from k1950_global_catalyst_energy_certificates_probe import shell_return
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1978-thermal-spectral-spacing.json'
def compress(energies,delta):
    e=sorted(map(F,energies));d=len(e);assert e[0]==0 and all(b-a>=delta for a,b in zip(e,e[1:]))
    parent=list(range(d))
    def root(i):
        while parent[i]!=i:i=parent[i]
        return i
    for i in range(d):
        for j in range(i):
            if e[i]-e[j] in (1,2,3):parent[root(i)]=root(j)
    groups={}
    for i in range(d):groups.setdefault(root(i),[]).append(i)
    groups=list(groups.values());m=len(groups);label={i:c for c,g in enumerate(groups) for i in g}
    offsets=[min(e[i] for i in g) for g in groups];n=[e[i]-offsets[label[i]] for i in range(d)]
    assert all(x.denominator==1 for x in n)
    edges=[(label[i-1],label[i],delta+n[i-1]-n[i]) for i in range(1,d)]
    x=[F(0)]*m
    for _ in range(m):
        old=x[:]
        for a,b,w in edges:x[b]=max(x[b],x[a]+w)
        if x==old:break
    assert all(x[b]>=x[a]+w for a,b,w in edges)
    new=[x[label[i]]+n[i] for i in range(d)]
    bound=(d-1)*(delta+3*(d-1))+3*(d-1)
    assert new[0]==0 and all(b-a>=delta for a,b in zip(new,new[1:]))
    assert all(a<=b for a,b in zip(new,e)) and max(new)<=bound
    # Each original energy shell still lies in one new shell, so old blocks survive.
    shells={}
    for i,v in enumerate(e):
        for b in range(4):shells.setdefault(v+b,[]).append((i,b))
    assert all(len({new[i]+b for i,b in members})==1 for members in shells.values())
    return dict(original=list(map(str,e)),compressed=list(map(str,new)),delta=str(delta),bound=str(bound),components=m)
def physical(E,delta):
    assert 0<delta<=F(1,2) and F(6,5)<E<F(11,5)
    w=(E-F(6,5))/(1+delta);s=[F(1),F(3),1+delta,3+delta];p=[(1-w)*F(9,10),(1-w)/10,2*w/5,3*w/5]
    energies=sorted([F(i)+h for h in [F(0),delta] for i in range(5)])
    assert min(b-a for a,b in zip(energies,energies[1:]))==delta
    assert sum(p)==1 and sum(a*b for a,b in zip(s,p))==E
    for z in {a+b for a in s for b in range(4)}:
        assert sum(z-a in range(4) for a in energies)>=2*sum(z-a in range(4) for a in s)
    R=shell_return(F(1,2),s,p);gap=R-(F(63,100)-F(3,20)*E)
    assert gap==F(3,20)*(E-F(6,5))*delta/(1+delta)>0
    return dict(energy=str(E),spacing=str(delta),return_error=str(R),gap=str(gap))
def calculate():
    cases=[]
    for delta in [F(1,10),F(1,2),F(1)]:
        for shift in [F(10),F(100),F(1000),F(23,2)]:
            for spare in [False,True]:
                e=list(map(F,range(5)))+[shift+i for i in range(5)]
                if spare:e+=[shift+100]
                cases.append(compress(e,delta))
    uppers=[physical(F(6,5)+F(i,10),delta) for i in range(1,10) for delta in [F(1,2),F(1,10),F(1,100)]]
    # At spacing>1, a populated level's bath-index1 shell forces the lower gap2;
    # bath-index2 forces upper gap2. At spacing>2 the first is impossible.
    required={b:[q for q in range(-3,4) if abs(q)>1 and b-q in range(4)] for b in [1,2]}
    assert required=={1:[-2],2:[2]}
    spectrum=[F(0),F(2),F(4)];support=[F(2)]
    assert all(sum(z-a in range(4) for a in spectrum)>=2 for z in range(2,6))
    r=shell_return(F(1,2),support,[F(1)]);assert r==F(1,2)
    return dict(result_id='K1978',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',compression_controls=cases,upper_families=uppers,spacing_threshold='2',threshold_witness=dict(dimension=3,energies=['0','2','4'],mean_energy='2',return_error=str(r)),scope='Fixed positive spacing and finite dimension: nonempty mean-energy-budget feasible set has an attained return optimum and strict interior exposed-chord gap, uniform on compact interior energy intervals. Exact channel impossible for spacing>2; spacing2 feasible with three levels at energy2.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['explorations/conditional-build/k1975-thermal-sharp-dimension-threshold-2026-10-23.md','lab/process/k1950-global-catalyst-energy-certificates.json','lab/process/k1968-joint-thermal-finite-dimension-program.json']})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=calculate()
    if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert r==json.loads(OUT.read_text())
    print('PASS K1978',len(r['compression_controls']),'compression and',len(r['upper_families']),'physical families; sharp spacing2 witness')
