"""Exact equality-ray audit at the two inherited certificate intersections."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,argparse
from k2059_energy_aware_thermal_tail import bellman,K,C,allowed
from k2075_thermal_equality_rigidity import loss,LH
ROOT=Path(__file__).resolve().parents[2];Z=Q(0);THETA=Q(69,100)
def read(n):return json.loads((ROOT/'lab/process'/n).read_text())
def incoming(s,p):
    if len(s)==1:return p[-1]
    L,H=LH[s[-1]-s[-2]]
    return max(Z,p[-1]-max(Z,H*p[-2]-L*p[-1]))
def assignments():
    ass=read('k2059-energy-aware-thermal-tail.json')['assignments']
    for f in ['k2066-thermal-terminal-response.json','k2070-joint-terminal-thermal-bound.json','k2072-compulsory-ladder-thermal-bound.json','k2074-subdivided-incoming-thermal-bound.json']:
        for ci,v in read(f)['replacements'].items():ass[int(ci)]=v
    return ass

def price188(a,t):
    j=read('k2070-joint-terminal-thermal-bound.json');d=read('k2074-subdivided-incoming-thermal-bound.json');p=read('k2072-compulsory-ladder-thermal-bound.json');g=bellman(a,t,64);values=[];rays=[]
    def add(ds,xs,c,rewards):
        L,H=LH[ds[0]];values.append((sum(x*y for x,y in zip(xs,rewards))-c-THETA*min(Q(1),max(Z,L*xs[0]-H))/2,ds,xs))
    for gap in [2,3]:
        L,H=LH[gap]
        for x in [Z,K[gap],H/L,(1+H)/L]:add((gap,),(x,),loss([Q(1),x],[gap]),[a-t*(11+gap)])
        rays.append(Q(1,2)-a+t*(11+gap))
    for size,geoms in [(2,j['arrangements']),(3,j['triple_arrangements']),(4,{**p['quad_arrangements'],**d['quad_arrangements']})]:
        for key,data in geoms.items():
            ds=tuple(map(int,key.split(',')))
            if ds[0] not in [2,3] or (size==4 and ds not in [(2,2,2,2),(2,2,2,3)]):continue
            ns=[11+sum(ds[:i+1]) for i in range(size)];rewards=[a-t*n for n in ns]
            if size>=3 and ds!=(2,2,2):rewards[-1]=g[ns[-1],ds[-1]]
            for r in data['vertices']:add(ds,tuple(map(Q,r[:-1])),Q(r[-1]),rewards)
            for r in data['rays']:rays.append(Q(r[-1])-sum(x*y for x,y in zip(map(Q,r[:-1]),rewards)))
    beta=max(x[0] for x in values);w=[r for r in values if r[0]==beta];assert len(w)==1 and w[0][1]==(2,2,2,2) and w[0][2]==tuple(Q(1,9)**i for i in range(1,5))
    assert min(rays)>0
    return beta,dict(vertices=len(values),rays=len(rays),second_gap=str(beta-max(v[0] for v in values if v[0]<beta)),minimum_ray_slack=str(min(rays)),gaps=list(w[0][1]),ratios=list(map(str,w[0][2])))

def produce():
    bank=read('k2045-third-thermal-spacing-phase.json')['bank'];ass=assignments();end=read('k2074-subdivided-incoming-thermal-bound.json');a0,s0=map(Q,end['lower_line']);ends=list(map(Q,end['interval']));ties=[]
    for E in ends:
        dif=[Q(v['a'])+E*Q(v['s'])-a0-E*s0 for v in ass];assert min(dif)==0
        ties.append([i for i,v in enumerate(dif) if v==0])
    assert ties==[[187,188],[187,235]]
    rows=[]
    for ci,endpoint,ell in [(188,ends[0],Q(25,2)),(235,ends[1],Q(11))]:
        a,t=Q(ass[ci]['a']),-Q(ass[ci]['s']);g=bellman(a,t,64);h=bellman(a-t*ell,t,64);cell=bank[ci];ss=cell['s'];census=None
        if ci==188:beta,census=price188(a,t)
        def boundary(p):
            A=incoming(ss,p);last=p[-1]
            if ci==188:return max(Z,beta*last+THETA*A/2)
            gg=g[14,3];L,H=LH[3]
            return max(Z,gg*K[3]*last,(gg-Q(1,2))*H*last/L+(Q(1,2)+(gg-Q(1,2))/L)*A)
        sl=[Q(v['value'])-a+t*Q(v['energy'])-boundary(list(map(Q,v['p']))) for v in cell['vertices']];assert min(sl)==0
        zeros=[i for i,x in enumerate(sl) if x==0];assert zeros==([57] if ci==188 else [35]);v=cell['vertices'][zeros[0]];pp=list(map(Q,v['p']));support=list(ss);initial=list(pp)
        if ci==188:
            for _ in range(4):support.append(support[-1]+2);pp.append(pp[-1]/9)
            n,d=19,2;capstart=21
            assert incoming(ss,initial)==0
        else:
            A=incoming(ss,pp);assert A==pp[-1];L,H=LH[3];gg=g[14,3]
            assert gg*K[3]*pp[-1]>max(Z,(gg-Q(1,2))*H*pp[-1]/L+(Q(1,2)+(gg-Q(1,2))/L)*A)
            support.append(14);pp.append(pp[-1]/23);n,d=14,3;capstart=16
        policy=[]
        while True:
            assert g[n,d]>0
            opts=[(a-t*n+K[e]*g.get((n+e,e),Z),e) for e in K if d+e>=4]
            best=max([Z]+[v for v,e in opts]);assert best==g[n,d]
            live=[(val,e) for val,e in opts if g.get((n+e,e),Z)>0]
            choices=[e for val,e in live if val==best]
            policy.append(dict(energy=n,incoming_gap=d,bellman=str(best),cap_slack=str(C[d]-best),next_gaps=choices))
            if not choices:
                assert best==a-t*n and all(g.get((n+e,e),Z)==0 for val,e in opts);break
            assert len(choices)==1
            e=choices[0];n+=e;d=e;support.append(n);pp.append(pp[-1]*K[e])
        assert all(Q(r['cap_slack'])>0 for r in (policy[1:] if ci==188 else policy))
        if ci==188:assert support==list(range(1,44,2))
        else:assert support==[1,3,5,7,10,11,14,15,18,19,22,23,26,27,30,31,34]
        # Only one cap saturation exists in the relevant generic suffix region;
        # the forced state-aware path never visits it.
        caps=[(C[d]-g[n,d],n,d) for n in range(capstart,65) for d in K];assert min(x[0] for x in caps)>=0
        zero_caps=[[n,d] for x,n,d in caps if x==0];assert zero_caps==([] if ci==188 else [[16,2]])
        if ci==188:assert C[2]==g[20,2]
        high=min((Q(v['value'])-a+t*(Q(v['energy'])+ell)-Q(v['p'][-1])*max([Z]+[K[d]*h.get((bc['s'][-1]+d,d),Z) for d in allowed(bc['s'])]),bi,vi) for bi,bc in enumerate(bank) for vi,v in enumerate(bc['vertices']))
        root=min((Q(1,2)-a+t*(n+ell)-K[d]*h.get((n+d,d),Z),n,d) for n in range(12,65) for d in K)
        assert high[0]>0 and root[0]>0 and all(v<=C[d] for (n,d),v in h.items())
        mass=sum(pp);energy=sum(n*p for n,p in zip(support,pp))/mass;assert energy!=endpoint
        # Need only necessary equality consequences, not sufficiency of this ray.
        rows.append(dict(cell=ci,endpoint=str(endpoint),line=[str(a),str(-t)],high_offset=str(ell),low_zero_vertices=zeros,low_population=list(map(str,initial)),minimum_other_low_slack=str(min(x for x in sl if x>0)),tail_price=str(beta) if ci==188 else None,tail_census=census,high_margin=[str(high[0]),*high[1:]],root_margin=[str(root[0]),*root[1:]],forced_support=support,forced_population=list(map(str,pp)),normalized_necessary_energy=str(energy),endpoint_energy_difference=str(endpoint-energy),state_aware_policy=policy,unvisited_saturated_cap=[20,2] if ci==188 else [16,2]))
    refs=['lab/process/'+n for n in ['k2045-third-thermal-spacing-phase.json','k2059-energy-aware-thermal-tail.json','k2066-thermal-terminal-response.json','k2070-joint-terminal-thermal-bound.json','k2072-compulsory-ladder-thermal-bound.json','k2074-subdivided-incoming-thermal-bound.json','k2075-thermal-equality-rigidity.json','k2068-thermal-population-construction.json']]+['tests/channel-swings/k2059_energy_aware_thermal_tail.py']
    return dict(id='K2078',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs},closed_energy_interval=end['interval'],endpoint_ties=ties,endpoint_exclusions=rows,unique_population='K2068 affine N20 occupied population on energies1,3,...,39',minimum_physical_dimension=41,scope='closed inherited certificate interval, spacing1/2<delta<=1, finite/countable catalysts; no channel uniqueness or wider-interval claim',correction='Provisional cell235 path using incoming gap2 at14 rejected; correct incoming gap3 gives alternating1,3 continuation.')
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();d=produce();p=ROOT/'lab/process/k2078-thermal-certificate-endpoints.json'
    if args.write:p.write_text(json.dumps(d,indent=2)+'\n')
    else:assert json.loads(p.read_text())==d
    print('PASS endpoint ties, exact equality paths, strict high/root margins; closed-interval rigidity')
    for r in d['endpoint_exclusions']:print(r['cell'],r['normalized_necessary_energy'],float(Q(r['normalized_necessary_energy'])),r['tail_census'])
