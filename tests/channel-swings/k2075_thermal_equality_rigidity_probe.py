"""Independent rational bath, Bellman, slack and physical support controls."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,random,copy
R=Path(__file__).resolve().parents[2];Z=F(0);BATH=list(map(F,['8/15','4/15','2/15','1/15']))
K={1:F(7,29),2:F(1,9),3:F(1,23)};C={1:F(29,135),2:F(9,50),3:F(23,90)}
def raw(s,p):
    return sum(max(Z,x-sum(max([Z]+[q*BATH[e+b-y] for y,q in zip(s,p) if 0<=e+b-y<4]) for b in range(4))/2) for e,x in zip(s,p))
def rec(a,t):
    cache={}
    def val(n,d):
        if n>=41:return Z
        if (n,d) not in cache:cache[n,d]=max([Z]+[a-t*n+K[e]*val(n+e,e) for e in K if d+e>=4])
        return cache[n,d]
    return val

def check(data,fault=None):
    a,t=F(data['line'][0]),-F(data['line'][1]);g=rec(a,t);count=0
    # Stored geometry is reused, but its loss values are independently reconstructed from bath labels.
    joint=json.loads((R/'lab/process/k2070-joint-terminal-thermal-bound.json').read_text());prices=[];ray_slacks=[]
    for kind in ['arrangements','triple_arrangements']:
        for gaps,geom in joint[kind].items():
            ds=list(map(int,gaps.split(',')))
            if ds[0] not in [2,3]:continue
            s=[11]
            for d in ds:s.append(s[-1]+d)
            q=[a-t*n for n in s[1:]]
            if len(ds)==3:q[-1]=g(s[-1],ds[-1])
            for row in geom['vertices']:
                pp=list(map(F,row[:-1]));cost=raw(s,[F(1),*pp])-F(1,2);assert cost==F(row[-1]);prices.append((sum(x*y for x,y in zip(q,pp))-cost,ds,pp));count+=1
            for row in geom['rays']:
                pp=list(map(F,row[:-1]));cost=raw(s,[Z,*pp]);assert cost==F(row[-1]);ray_slacks.append(cost-sum(x*y for x,y in zip(q,pp)));count+=1
    beta=F(data['tail_price']);assert max(x[0] for x in prices)==beta
    winners=[(ds,p) for v,ds,p in prices if v==beta];assert winners==[([2,2,2],list(map(F,['3/2','9/4','27/8'])))];assert min(ray_slacks)>0
    for n in range(19,65):
        for d in K:assert C[d]-g(n,d)>=F(data['deep_cap_margin'][0]);count+=1
    # Direct rational finite telescopes with varying gaps, deficits and terminal lengths.
    rng=random.Random(2075)
    for length in range(8):
        for _ in range(16):
            s=[17];ds=[];last=2
            for j in range(length):
                d=rng.choice([d for d in K if d+last>=4]);ds.append(d);s.append(s[-1]+d);last=d
            p=[F(rng.randrange(1,20),rng.randrange(1,12)) for _ in s];gs=[g(17,2)]+[g(n,d) for n,d in zip(s[1:],ds)];ws=[a-t*n for n in s]
            losses=[raw(s[:j+1],p[:j+1])-raw(s[:j],p[:j]) for j in range(1,len(s))]
            xs=[max(Z,p[j]-K[d]*p[j-1]) for j,d in enumerate(ds,1)];ys=[max(Z,K[d]*p[j-1]-p[j]) for j,d in enumerate(ds,1)]
            hs=[gs[j]-ws[j]-(K[ds[j]]*gs[j+1] if j<len(ds) else Z) for j in range(len(s))]
            terms=[loss-C[d]*x for loss,d,x in zip(losses,ds,xs)]+[(C[d]-gg)*x for d,gg,x in zip(ds,gs[1:],xs)]+[h*x for h,x in zip(hs,p)]+[gg*y for gg,y in zip(gs[1:],ys)]
            assert min(terms)>=0
            rhs=sum(terms)-(sum(gg*y for gg,y in zip(gs[1:],ys)) if fault=='missing_y_slack' else Z)
            assert sum(losses)+gs[0]*p[0]-sum(w*x for w,x in zip(ws,p))==rhs;count+=2
    upper=json.loads((R/'lab/process/k2068-thermal-population-construction.json').read_text());support=data['occupied_support'];aff=data['population_affine'];assert support==list(range(1,40,2)) and aff==upper['population_affine']
    if fault=='last_atom':support=support[:-1];aff=aff[:-1]
    for energy in map(F,[data['open_energy_interval'][0],'5/2',data['open_energy_interval'][1]]):
        p=[F(x)+energy*F(y) for x,y in aff]
        if fault=='tail_ratio':p[-1]=p[-2]/8
        assert min(p)>0 and sum(p)==1 and sum(x*y for x,y in zip(support,p))==energy
        assert raw(support,p)==a-t*energy
        for j in range(9,len(p)):assert p[j]==p[j-1]/9
        count+=3
    # Dimension necessity from all shared bath shells, not counting occupied support.
    mandatory=set()
    for x,y in zip(support,support[1:]):
        for shell in sorted(set(range(x,x+4))&set(range(y,y+4))):
            occ=[e for e in support if 0<=shell-e<4];assert len(occ)==2
            slots={shell-b for b in range(4)};assert min(slots)>=0;mandatory |= slots
    if fault=='dimension':assert len(mandatory)==40,'false physical dimension'
    else:assert mandatory==set(range(41)) and len(mandatory)==data['minimum_physical_dimension']
    # Actual terminal controls reject wrong zero-loss threshold and inflated sharp constant.
    k=F(1,10) if fault=='threshold' else K[2];u=F(1,9);delta=raw([0,2],[F(1),u])-F(1,2);assert delta>=C[2]*max(Z,u-k)
    c=F(1,4) if fault=='sharp_cost' else C[2];u=F(3,2);delta=raw([0,2],[F(1),u])-F(1,2);assert delta>=c*(u-K[2])
    assert g(41,2)==0 and a-41*t<0
    assert raw([39,41],[F(1),F(1,9)])==raw([39],[F(1)])
    if fault=='extra_tail':assert a-41*t>=0,'negative reward forbids invisible extra atom'
    if fault=='early_stop':assert g(37,2)==a-37*t,'false terminal37'
    return count
if __name__=='__main__':
    d=json.loads((R/'lab/process/k2075-thermal-equality-rigidity.json').read_text())
    for p,h in d['inputs'].items():assert hashlib.sha256((R/p).read_bytes()).hexdigest()==h
    n=check(d);faults=[]
    for f in ['last_atom','tail_ratio','dimension','threshold','sharp_cost','early_stop','missing_y_slack','extra_tail']:
        try:check(d,f)
        except AssertionError:faults.append(f)
        else:raise AssertionError('undetected fault '+f)
    print('PASS',n,'raw-bath/Bellman/slack/affine controls; eight actual mathematical faults',faults)
