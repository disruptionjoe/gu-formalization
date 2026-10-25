"""Exact equality contacts of the inherited thermal certificate; no new optimization."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,argparse
from k2059_energy_aware_thermal_tail import bellman,K,C,allowed
ROOT=Path(__file__).resolve().parents[2]
Z=Q(0)
LH={1:(Q(14,15),Q(7,15)),2:(Q(4,5),Q(1,5)),3:(Q(8,15),Q(1,15))}
def read(name):return json.loads((ROOT/'lab/process'/name).read_text())
def loss(pop,ds):
    return (sum(max(Z,x-(max(Z,LH[ds[i-1]][1]*pop[i-1]-LH[ds[i-1]][0]*x) if i else 0)-(max(Z,LH[ds[i]][0]*pop[i+1]-LH[ds[i]][1]*x) if i<len(ds) else 0)) for i,x in enumerate(pop))-pop[0])/2

def census():
    J=read('k2070-joint-terminal-thermal-bound.json');bank=read('k2045-third-thermal-spacing-phase.json')['bank'];end=read('k2074-subdivided-incoming-thermal-bound.json');upper=read('k2068-thermal-population-construction.json')
    v=J['replacements']['187'];a,t=Q(v['a']),-Q(v['s']);assert [str(a),str(-t)]==end['lower_line'] and not Q(v.get('mixture') or 0)
    g=bellman(a,t,64);h=bellman(a-t*Q(25,2),t,64);vals=[];rays=[]
    for d in allowed(bank[187]['s']):
        n=11+d;L,H=LH[d]
        for x in [Z,K[d],H/L,(1+H)/L]:vals.append(((a-t*n)*x-loss([Q(1),x],[d]),(d,),(x,)))
        rays.append((Q(1,2)-(a-t*n),(d,),(Q(1),)))
    for keyname,size in [('arrangements',2),('triple_arrangements',3)]:
        for key,data in J[keyname].items():
            ds=tuple(map(int,key.split(',')))
            if ds[0] not in allowed(bank[187]['s']):continue
            ns=[11+sum(ds[:i+1]) for i in range(size)];qs=[a-t*n for n in ns]
            if size==3:qs[-1]=g[ns[-1],ds[-1]]
            for r in data['vertices']:vals.append((sum(q*x for q,x in zip(qs,map(Q,r[:-1])))-Q(r[-1]),ds,tuple(map(Q,r[:-1]))))
            for r in data['rays']:rays.append((Q(r[-1])-sum(q*x for q,x in zip(qs,map(Q,r[:-1]))),ds,tuple(map(Q,r[:-1]))))
    beta=max(r[0] for r in vals);maxima=[v for v in vals if v[0]==beta];assert len(maxima)==1 and maxima[0][1:]==((2,2,2),(Q(3,2),Q(9,4),Q(27,8)))
    second=max(x[0] for x in vals if x[0]<beta);raymin=min(r[0] for r in rays);assert raymin>0
    slacks=[Q(v['value'])-a+t*Q(v['energy'])-beta*Q(v['p'][-1]) for v in bank[187]['vertices']];assert min(slacks)==0
    zeros=[i for i,x in enumerate(slacks) if not x];assert zeros==[33,35]
    high=min((Q(v['value'])-a+t*(Q(v['energy'])+Q(25,2))-max([Z]+[K[d]*h.get((cell['s'][-1]+d,d),Z) for d in allowed(cell['s'])])*Q(v['p'][-1]),ci,vi) for ci,cell in enumerate(bank) for vi,v in enumerate(cell['vertices']))
    root=min((Q(1,2)-a+t*(n+Q(25,2))-K[d]*h.get((n+d,d),Z),n,d) for n in range(12,65) for d in K)
    cap=min((C[d]-g[n,d],n,d) for n in range(19,65) for d in K);assert min(high[0],root[0],cap[0])>0
    assert all(v<=C[d] for (n,d),v in h.items()),'high suffix caps'
    policy=[]
    for n in range(17,40,2):
        opts=[(Z,'erase')]+[(a-t*n+K[e]*g.get((n+e,e),Z),e) for e in K if 2+e>=4]
        best=max(x[0] for x in opts);choices=[x[1] for x in opts if x[0]==best]
        assert best==g[n,2]>0
        if n<39:assert choices==[2] and best>a-t*n
        else:assert best==a-t*n and all(g.get((n+e,e),Z)==0 for e in K if e+2>=4)
        policy.append(dict(energy=n,value=str(best),next_gaps=choices))
    assert 40<a/t<41 and all(v==0 for (n,d),v in g.items() if n>=41)
    extended=[]
    for vi in zeros:
        pp=list(map(Q,bank[187]['vertices'][vi]['p']));b=pp[-1];assert pp[-1]>=pp[-2]/4
        pp += [b*Q(3,2),b*Q(9,4),b*Q(27,8)];b=pp[-1];pp += [b*Q(1,9)**i for i in range(1,12)]
        mass=sum(pp);energy=sum(Q(2*i+1)*x for i,x in enumerate(pp));extended.append((pp,mass,energy))
    (p0,m0,e0),(p1,m1,e1)=extended;det=m0*e1-m1*e0;assert det
    # Solve normalization and energy as affine identities, never decimals.
    pop=[[str((x*e1-y*e0)/det),str((-x*m1+y*m0)/det)] for x,y in zip(p0,p1)]
    assert pop==upper['population_affine']
    ends=sorted([e0/m0,e1/m1]);left,right=map(Q,end['interval']);assert ends[0]<left<right<ends[1]
    return dict(id='K2075',line=[str(a),str(-t)],open_energy_interval=end['interval'],spacing='1/2 < delta <= 1',tail_vertices=len(vals),tail_rays=len(rays),tail_price=str(beta),second_price=str(second),tail_vertex_gap=str(beta-second),minimum_recession_slack=str(raymin),retained_zero_vertices=zeros,minimum_other_low_slack=str(min(x for x in slacks if x>0)),high_retained_margin=[str(high[0]),*high[1:]],erased_root_margin=[str(root[0]),*root[1:]],deep_cap_margin=[str(cap[0]),*cap[1:]],bellman_policy=policy,zero_reward_from=41,extended_cone_energy_interval=list(map(str,ends)),population_affine=pop,occupied_support=list(range(1,40,2)),minimum_physical_dimension=41,scope='unique occupied population measure and minimum physical dimension; not unique channel or complete empty-level spectrum')

def produce():
    refs=['lab/process/k2074-subdivided-incoming-thermal-bound.json','lab/process/k2070-joint-terminal-thermal-bound.json','lab/process/k2045-third-thermal-spacing-phase.json','lab/process/k2068-thermal-population-construction.json','tests/channel-swings/k2059_energy_aware_thermal_tail.py','explorations/conditional-build/k2054-quantitative-terminal-erasure-2026-10-25.md','explorations/conditional-build/k2072-compulsory-ladder-thermal-bound-2026-10-25.md']
    d=census();d['inputs']={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs};return d
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();d=produce();out=ROOT/'lab/process/k2075-thermal-equality-rigidity.json'
    if args.write:out.write_text(json.dumps(d,indent=2)+'\n')
    else:assert json.loads(out.read_text())==d
    print('PASS equality census, strict high/root/cap margins, exact affine reconstruction; dimension41')
