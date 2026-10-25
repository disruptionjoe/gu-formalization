"""Independent raw-bath/state-aware checks of endpoint equality certificates."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,copy
ROOT=Path(__file__).resolve().parents[2];Z=F(0);BATH=list(map(F,['8/15','4/15','2/15','1/15']))
K={1:F(7,29),2:F(1,9),3:F(1,23)};C={1:F(29,135),2:F(9,50),3:F(23,90)}
def read(n):return json.loads((ROOT/'lab/process'/n).read_text())
def raw(s,p):return sum(max(Z,x-sum(max([Z]+[q*BATH[e+b-y] for y,q in zip(s,p) if 0<=e+b-y<4]) for b in range(4))/2) for e,x in zip(s,p))
def bell(a,t):
    cache={}
    def val(n,d):
        if a-t*n<=0:return Z
        if (n,d) not in cache:cache[n,d]=max([Z]+[a-t*n+K[e]*val(n+e,e) for e in K if d+e>=4])
        return cache[n,d]
    return val

def check(data,fault=None):
    data=copy.deepcopy(data);bank=read('k2045-third-thermal-spacing-phase.json')['bank'];joint=read('k2070-joint-terminal-thermal-bound.json');prev=read('k2072-compulsory-ladder-thermal-bound.json');new=read('k2074-subdivided-incoming-thermal-bound.json');count=0
    ass=read('k2059-energy-aware-thermal-tail.json')['assignments']
    for n in ['k2066-thermal-terminal-response.json','k2070-joint-terminal-thermal-bound.json','k2072-compulsory-ladder-thermal-bound.json','k2074-subdivided-incoming-thermal-bound.json']:
        for i,c in read(n)['replacements'].items():ass[int(i)]=c
    line=list(map(F,new['lower_line']))
    for E,tie in zip(map(F,data['closed_energy_interval']),data['endpoint_ties']):
        values=[F(c['a'])+F(c['s'])*E-line[0]-line[1]*E for c in ass]
        assert min(values)==0 and [i for i,x in enumerate(values) if x==0]==tie;count+=len(values)
    for row in data['endpoint_exclusions']:
        ci=row['cell'];a,t=F(row['line'][0]),-F(row['line'][1]);g=bell(a,t)
        p=list(map(F,row['forced_population']));s=row['forced_support'];initial=list(map(F,row['low_population']));ss=bank[ci]['s'];last=initial[-1]
        assert raw(ss,initial)==F(bank[ci]['vertices'][row['low_zero_vertices'][0]]['value']);count+=1
        if ci==188:
            prices=[];rays=[]
            # Independently reconstruct ALL serialized loss values from the bath, not stored cost.
            for size,geoms in [(2,joint['arrangements']),(3,joint['triple_arrangements']),(4,{**prev['quad_arrangements'],**new['quad_arrangements']})]:
                for key,geom in geoms.items():
                    ds=tuple(map(int,key.split(',')))
                    if ds[0] not in [2,3] or (size==4 and ds not in [(2,2,2,2),(2,2,2,3)]):continue
                    ns=[11]
                    for d in ds:ns.append(ns[-1]+d)
                    ws=[a-t*n for n in ns[1:]]
                    if size>=3 and ds!=(2,2,2):ws[-1]=g(ns[-1],ds[-1])
                    if fault=='omit_shorter_prefix' and ds==(2,2,2):ws[-1]=g(ns[-1],ds[-1])
                    L=sum(BATH[:4-ds[0]]);H=sum(BATH[ds[0]:])
                    for rr in geom['vertices']:
                        pp=list(map(F,rr[:-1]));cost=raw(ns,[F(1),*pp])-F(1,2);assert cost==F(rr[-1])
                        price=sum(x*y for x,y in zip(pp,ws))-cost-F(69,200)*min(F(1),max(Z,L*pp[0]-H));prices.append((price,ds,pp));count+=1
                    for rr in geom['rays']:
                        pp=list(map(F,rr[:-1]));cost=raw(ns,[Z,*pp]);assert cost==F(rr[-1]);rays.append(cost-sum(x*y for x,y in zip(pp,ws)));count+=1
            beta=F(row['tail_price']);assert max(x[0] for x in prices)==beta and min(rays)>0
            winner=[(ds,p) for value,ds,p in prices if value==beta];assert winner==[((2,2,2,2),[F(1,9)**i for i in range(1,5)])]
            assert p[6:10]==[last*F(1,9)**i for i in range(1,5)]
        else:
            if fault=='wrong_incoming_state':row['state_aware_policy'][0]['incoming_gap']=2
            assert p[6]==last/23 and s[6]==14
        if fault=='wrong_tail_ratio':p[-1]*=F(9,8)
        if fault=='missing_last_atom':s=s[:-1];p=p[:-1]
        for rec in row['state_aware_policy']:
            n,d=rec['energy'],rec['incoming_gap'];opts=[(a-t*n+K[e]*g(n+e,e),e) for e in K if d+e>=4]
            best=max([Z]+[v for v,e in opts]);choices=[e for v,e in opts if v==best and g(n+e,e)>0]
            assert best==F(rec['bellman']) and choices==rec['next_gaps'];count+=1
            if choices:
                idx=s.index(n);e=choices[0];assert s[idx+1]==n+e and p[idx+1]==K[e]*p[idx]
            else:assert n==s[-1] and best==a-t*n
        sat=row['unvisited_saturated_cap'];assert g(*sat)==C[sat[1]]
        if fault=='visit_saturated_cap':assert tuple(sat) in [(r['energy'],r['incoming_gap']) for r in row['state_aware_policy']]
        else:assert tuple(sat) not in [(r['energy'],r['incoming_gap']) for r in row['state_aware_policy']]
        energy=sum(x*y for x,y in zip(s,p))/sum(p);assert energy==F(row['normalized_necessary_energy'])
        if fault=='false_endpoint_attainment':assert energy==F(row['endpoint'])
        else:assert energy!=F(row['endpoint']) and F(row['endpoint'])-energy==F(row['endpoint_energy_difference'])
        # Every alleged equality ray may be only necessary. Never promote it to feasible endpoint.
        ell=F(row['high_offset']);hh=bell(a-t*ell,t);hs=[]
        for cell in bank:
            ss=cell['s'];prev_gap=ss[-1]-ss[-2] if len(ss)>1 else 4
            ds=[d for d in K if ss[-1]+d>=12 and prev_gap+d>=4]
            for v in cell['vertices']:
                pp=list(map(F,v['p']));r=raw(ss,pp);assert r==F(v['value'])
                slack=r-a+t*(sum(x*y for x,y in zip(ss,pp))+ell)-pp[-1]*max([Z]+[K[d]*hh(ss[-1]+d,d) for d in ds]);hs.append(slack);count+=1
        assert min(hs)==F(row['high_margin'][0])>0
        assert min(F(1,2)-a+t*(n+ell)-K[d]*hh(n+d,d) for n in range(12,65) for d in K)==F(row['root_margin'][0])>0
    # The retained N20 witness realizes the same objective at BOTH exact endpoints.
    upper=read('k2068-thermal-population-construction.json');s=list(range(1,40,2));mandatory=set()
    for E in map(F,data['closed_energy_interval']):
        p=[F(x)+E*F(y) for x,y in upper['population_affine']]
        assert min(p)>0 and sum(p)==1 and sum(x*y for x,y in zip(s,p))==E
        assert raw(s,p)==line[0]+line[1]*E;count+=4
    for x,y in zip(s,s[1:]):
        for shell in set(range(x,x+4))&set(range(y,y+4)):mandatory.update(shell-b for b in range(4))
    if fault=='dimension40':assert len(mandatory)==40
    else:assert mandatory==set(range(41)) and data['minimum_physical_dimension']==41
    return count
if __name__=='__main__':
    d=read('k2078-thermal-certificate-endpoints.json')
    for p,h in d['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    n=check(d);caught=[]
    for fault in ['omit_shorter_prefix','wrong_incoming_state','wrong_tail_ratio','missing_last_atom','visit_saturated_cap','false_endpoint_attainment','dimension40']:
        try:check(d,fault)
        except (AssertionError,ValueError,IndexError):caught.append(fault)
        else:raise AssertionError('undetected '+fault)
    print('PASS',n,'independent raw-bath/policy/endpoint controls;',len(caught),'actual faults',caught)
