"""Zero-loss terminal erasure, unrestricted frontier, physical witnesses and stability."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib,argparse
from k2017_sharp_unrestricted_thermal_transition import sharp,encode
from k2019_posttransition_thermal_frontier import curve,kink,A,B,C,RC
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k2020-posttransition-tail-and-resources.json'
D2=Q(36,91);D3=Q(2,5)
def shells(a,s):
    return all(sum(x+b==e for x in a for b in range(4))>=2*sum(x+b==e for x in s for b in range(4)) for e in {x+b for x in s for b in range(4)})
def physical(d,E):
    pa=[Q(9,10),Q(1,10),Q(0)];pc=[Q(81,91),Q(9,91),Q(1,91)]
    X=kink(d)
    if E<=C:
        w=(E-A)/(C-A);s=list(map(Q,[1,3,5]));p=[(1-w)*x+w*y for x,y in zip(pa,pc)];a=list(map(Q,range(7)));kind='AC-seven'
    elif E<=X:
        if d<=D2:top=B;rp=[Q(2,5),Q(3,5)];dim=5;kind='CB-twelve'
        else:top=Q(19,8);rp=[Q(3,8),Q(9,16),Q(1,16)];dim=7;kind='CD-fourteen'
        w=(E-C)/(top+d-C);pairs=sorted([(Q(x),(1-w)*y) for x,y in zip([1,3,5],pc)]+[(Q(x)+d,w*y) for x,y in zip([1,3,5],rp)])
        s=[x for x,y in pairs];p=[y for x,y in pairs];a=sorted(list(map(Q,range(7)))+[Q(i)+d for i in range(dim)])
    elif d<D3:
        w=(E-A-d)/(B-A-d);pairs=sorted([(Q(x)+d,(1-w)*y) for x,y in zip([1,3],[Q(9,10),Q(1,10)])]+[(Q(x),w*y) for x,y in zip([1,3],[Q(2,5),Q(3,5)])]);s=[x for x,y in pairs];p=[y for x,y in pairs];a=sorted(list(map(Q,range(5)))+[Q(i)+d for i in range(5)]);kind='AB-ten'
    else:
        s=list(map(Q,[1,3]));p=[(3-E)/2,(E-1)/2];a=list(map(Q,range(5)));kind='J-five'
    assert min(p)>=0 and sum(p)==1 and sum(x*y for x,y in zip(s,p))==E
    assert shells(a,[x for x,y in zip(s,p) if y]) and min(y-x for x,y in zip(a,a[1:]))>=d
    R=sharp(s,p,Q(1,2));assert R==curve(d,E)
    kap=(9-E)/10-R;assert kap>=Q(33,100)
    return dict(delta=d,energy=E,kind=kind,spectrum=a,support=s,populations=p,return_value=R,dimension=len(a),kappa=kap,bath_TV_gap_radius=(R-(Q(63,100)-Q(3,20)*E))/2)
def local_pair(u,p,c,L,H):
    a=H*p
    return max(p-c-max(L*u-a,0),0)+max(u-max(a-L*u,0),0)
def produce():
    prior=json.loads((ROOT/'lab/process/k2017-sharp-unrestricted-thermal-transition.json').read_text())
    erased=[]
    for row in prior['physical_deletions']:
        s=list(map(Q,row['support']));p=list(map(Q,row['populations']));t=Q(row['t']);N=row['cutoff']
        low=[v if x<=N else Q(0) for x,v in zip(s,p)]
        assert sharp(s,low,t)<=sharp(s,p,t)
        erased.append(row)
    terminal=[]
    for t in [Q(1,4),Q(1,2),Q(3,4)]:
      for gap in (1,2,3):
       L=sum(t**j for j in range(4-gap))/sum(t**j for j in range(4));H=t**gap*L
       for p in [Q(1,10),Q(1),Q(3)]:
        for c in [Q(0),p/2,2*p]:
         knots=sorted(set([Q(0),H*p/(1+L),H*p/L,max(Q(0),(p-c+H*p)/L),Q(10)]));us=sorted(set(knots+[(x+y)/2 for x,y in zip(knots,knots[1:])]))
         values=[local_pair(u,p,c,L,H) for u in us];assert all(y>=x for x,y in zip(values,values[1:]))
         terminal.append(dict(t=t,gap=gap,p=p,incoming=c,u=us,twice_local_return=values))
    # A real positive tail gives zero unnormalized loss, so coefficient0 is sharp.
    assert sharp([Q(1),Q(3)],[Q(9,10),Q(1,10)],Q(1,2))==sharp([Q(1)],[Q(9,10)],Q(1,2))==Q(9,20)
    deltas=[Q(4,15),(Q(4,15)+D2)/2,D2,(D2+D3)/2,D3,(D3+Q(1,2))/2,Q(1,2)]
    witnesses=[];consumers=[]
    for d in deltas:
        X=kink(d);assert C<X<B and X>Q(17,10)
        for E in [A+Q(1,10**6),(A+C)/2,C,(C+X)/2,X,(X+B)/2,B-Q(1,10**6)]:
            w=physical(d,E);witnesses.append(w);R=w['return_value'];kap=w['kappa']
            for q in [Q(0),(E-A)/(9-A),(E-1)/8]:
                x=(E-9*q)/(1-q);low=(1-q)*curve(d,x)
                assert low>=R+kap*q
                consumers.append(dict(delta=d,energy=E,tail_mass=q,retained_budget=x,lower_return=low,kappa=kap))
    # Analytic slope floor; cross-multiplication handles the full parameter strips.
    slopes=[Q(9,76),Q(66,455)/(Q(436,455)+D2),Q(477,2912)/(Q(825,728)+Q(1,2)),Q(3,20)/(1-Q(4,15)),Q(1,4)]
    assert min(slopes)>=Q(1,10) and Q(1,10)*(9-A)-Q(9,20)==Q(33,100)
    # Transition equations and a concrete wrong old continuation.
    assert Q(66,455)/(Q(436,455)+D2)==Q(477,2912)/(Q(825,728)+D2)==Q(3,28)
    assert Q(3,20)/(1-D3)==Q(1,4)
    d=Q(9,20);E=(kink(d)+B)/2;w=physical(d,E)
    oldright=Q(3,10)+Q(3,20)/(1-d)*(B-E);assert w['return_value']<oldright
    inputs=['lab/process/k2019-posttransition-thermal-frontier.json','lab/process/k2017-sharp-unrestricted-thermal-transition.json','explorations/conditional-build/k2008-effective-thermal-dimension-approximation-2026-10-24.md','explorations/conditional-build/k2012-thermal-duality-gap-and-bath-stability-2026-10-24.md']
    return encode(dict(result_id='K2020',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',zero_loss_deletions=erased,terminal_breakpoint_controls=terminal,globally_optimal_witnesses=witnesses,secant_consumers=consumers,uniform_constants=dict(slope='1/10',kappa='33/100',tail_mass_per_epsilon='100/33',tail_energy_per_epsilon='300/11',budget_slack_per_epsilon='10'),dimension_upper_bounds={'AC':7,'CB':12,'CD':14,'GA':10,'J':5},scope='Unrestricted finite/countable optimum for4/15<=delta<=1/2 and6/5<E<11/5. Resource sizes are sufficient, not globally minimal. No GU identification, arbitrary-bath optimum or novelty.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs}))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();z=produce()
    if a.write:OUT.write_text(json.dumps(z,indent=2)+'\n')
    else:assert z==json.loads(OUT.read_text()),'certificate drift'
    print('PASS K2020',len(z['zero_loss_deletions']),'physical deletions',len(z['terminal_breakpoint_controls']),'terminal programs',len(z['globally_optimal_witnesses']),'physical optima',len(z['secant_consumers']),'secants')
