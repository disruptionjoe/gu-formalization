"""Direct bath-label physical replay and exact coefficient certificates."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def direct(s,p):
    b=[Q(8,15),Q(4,15),Q(2,15),Q(1,15)]
    return sum(max(Q(0),v-sum(max(w*b[k] for y,w in zip(s,p) for k in range(4) if y+k==x+j)/2 for j in range(4))) for x,v in zip(s,p))
def physical(row,fault=None):
    a,s,p=[list(map(Q,row[k])) for k in ['spectrum','support','populations']];d,E=Q(row['delta']),Q(row['energy'])
    if fault=='free_offset':s=[x-x%1 for x in s]
    if fault=='missing_completion':a.remove(Q(0))
    assert len(a)==10 and len(set(a))==10 and min(a)==0 and min(y-x for x,y in zip(a,a[1:]))>=d
    assert set(s)<=set(a) and sum(p)==1 and min(p)>=0 and sum(x*v for x,v in zip(s,p))==E
    for T in {x+b for x in s for b in range(4)}:assert sum(x+b==T for x in a for b in range(4))>=2*sum(x+b==T for x in s for b in range(4))
    R=direct(s,p)
    if fault=='return_factor':R*=2
    assert R==Q(row['return_value'])
    r=E-Q(6,5);expected=min(Q(9,20)-Q(3,20)*r/(1+d),Q(3,10)+Q(3,20)*(1-r)/(1-d))
    assert R==expected and Q(row['gap'])==R-(Q(63,100)-Q(3,20)*E)
    return E,d,R
def complete_interval_replay(census,D=Q(4,15)):
    from k2015_finite_thermal_ray_separation_probe import bath_planes
    from itertools import combinations
    rays=sorted({(Q(v['energy']),Q(v['return'])) for c in census['cells'] for v in c['vertices']})
    A,B,M,lam=Q(6,5),Q(11,5),Q(17,10),Q(3,20);counts={'single':0,'separated':0,'same_cone':0}
    def value(d,E):return min(Q(9,20)-lam*(E-A)/(1+d),Q(3,10)+lam*(B-E)/(1-d))
    for e,R in rays:
      for shift in (0,1):
        events={Q(0),D}
        for a,b in [(e-A,shift),(e-B,shift),(e-M,Q(shift)-Q(1,2))]:
            if b and 0<=-a/b<=D:events.add(-a/b)
        for d in events:
            E=e+shift*d
            if A<=E<=B:assert R>=value(d,E);counts['single']+=1
    def chord(e,R,b,f,S,k,kind):
        # Exact geometric endpoints of the feasible interval, derived from
        # crossings of moving ray energies with the branch meeting energy.
        if min(e,e+b*D)>M+D/2 or max(f,f+k*D)<M:return
        events={Q(0),D}
        for a,z in [(e-M,Q(b)-Q(1,2)),(f-M,Q(k)-Q(1,2))]:
            if z and 0<=-a/z<=D:events.add(-a/z)
        for d in events:
            x,y,mid=e+b*d,f+k*d,M+d/2
            if x<=mid<=y:
                if x<y:assert (R*(y-mid)+S*(mid-x))/(y-x)>=Q(3,8)
                else:assert min(R,S)>=Q(3,8)
                counts[kind]+=1
    for e,R in rays:
      for f,S in rays:
        if e<=M+D/2 and f+D>=M:chord(e,R,0,f,S,1,'separated')
        if f<=M+D/2 and e+D>=M:chord(f,S,1,e,R,0,'separated')
    for cell in census['cells']:
        _,_,Drows=bath_planes(cell['support'],cell['orientation'],True);vs=cell['vertices']
        signs=[[sum(x*Q(y) for x,y in zip(row,v['p'])) for row in Drows] for v in vs]
        for i,j in combinations(range(len(vs)),2):
            if any(x*y<0 for x,y in zip(signs[i],signs[j])):continue
            e,R=Q(vs[i]['energy']),Q(vs[i]['return']);f,S=Q(vs[j]['energy']),Q(vs[j]['return'])
            if e>f:e,f,R,S=f,e,S,R
            if e<=M+D/2 and f>=M:chord(e,R,0,f,S,0,'same_cone')
    return counts

if __name__=='__main__':
    bank=json.loads((ROOT/'lab/process/k2016-explicit-unrestricted-thermal-window.json').read_text());D=Q(bank['window']['spacing_max']);ca=Q(81,12940);cb=Q(9,7540);lam=Q(3,20)
    # Affine numerator nonnegativity at both endpoints certifies the ENTIRE interval.
    for d in [Q(0),Q(3,380)]:assert ca+(ca-lam)*d>=0 and cb-(cb+lam)*d>=0
    assert cb-(cb+lam)*Q(3,380)==0 and ca+(ca-lam)*Q(3,380)>0
    assert D==Q(1,15)<Q(22,95)
    census=json.loads((ROOT/'lab/process/k2015-finite-thermal-ray-separation.json').read_text())['census'];interval_counts=complete_interval_replay(census)
    assert (7-3*Q(15,8)-20*D)/(20*(1+D))==Q(1,512)>0
    assert Q(35491,20199)>Q(26,15)
    for row in bank['optimal_physical_witnesses']:
        E,d,R=physical(row);q=Q(row['tail_mass_prebound']);ep=Q(row['retained_budget_lower']);r=E-Q(6,5)
        assert ep==(E-9*q)/(1-q)>Q(6,5)
        slope=lam/(1+d) if E<Q(15,8) else lam/(1-d)
        assert q<5*r/39 and Q(row['kappa'])==slope*(9-E)-1
        if E>=Q(15,8):assert ep>Q(17,10)+d/2
        assert Q(row['faithful_bath_TV_radius'])==Q(row['gap'])/2 and Q(row['gibbs_t_radius'])==Q(row['gap'])/12
    for row in bank['near_optimizer_consumers']:
        E,d,eps,k=Q(row['energy']),Q(row['delta']),Q(row['epsilon']),Q(row['tail_mass_bound'])
        kap=(lam/(1+d) if E<Q(15,8) else lam/(1-d))*(9-E)-1
        assert eps==kap*k/(1-k)
        assert Q(row['retained_budget_lower'])>Q(6,5)
    # Independent shell exhaustion on the canonical two-site preparation.
    badsizes=0
    for n in range(2,5):
        for a in combinations(range(7),n):
            if not {1,3}<=set(a):continue
            valid=all(sum(x+b==T for x in a for b in range(4))>=2*sum(x+b==T for x in [1,3] for b in range(4)) for T in range(1,7))
            assert not valid;badsizes+=1
    # Equality types have opposite edge winner at gap two, so cannot share a cone.
    assert 3*Q(9,10)-12*Q(1,10)>0>3*Q(2,5)-12*Q(3,5)
    # Reject an attempted sharpness proof: the minimum directional-margin ray
    # and B do not lie in the same return cone; their convex interpolation is not linear.
    c=[Q(69,77),Q(23,231),Q(1,231)];b=[Q(2,5),Q(3,5),Q(0)];mix=[(x+y)/2 for x,y in zip(c,b)]
    assert direct([1,3,6],mix)>(direct([1,3,6],c)+direct([1,3,6],b))/2
    faults=[]
    for f in ['free_offset','missing_completion','return_factor']:
        try:physical(bank['optimal_physical_witnesses'][0],f)
        except AssertionError:faults.append(f)
        else:raise AssertionError('undetected '+f)
    for f,pred in [('extended_directional_window',lambda:cb-(cb+lam)*Q(1,100)>=0),('inflated_tail_slope',lambda:Q(1,10)<=Q(1,512))]:
        try:assert pred()
        except AssertionError:faults.append(f)
        else:raise AssertionError('undetected '+f)
    for row in bank['larger_spacing_counterexamples']:
        a=row['spectrum'];ss=row['support'];p=list(map(Q,row['populations']));E=Q(row['energy']);d=Q(row['delta'])
        assert sum(x*v for x,v in zip(ss,p))==E and direct(ss,p)==Q(row['return_value'])
        assert all(sum(x+b==T for x in a for b in range(4))>=2*sum(x+b==T for x in ss for b in range(4)) for T in range(1,9))
        expected=min(Q(9,20)-lam*(E-Q(6,5))/(1+d),Q(3,10)+lam*(Q(11,5)-E)/(1-d))
        assert Q(row['return_value'])<=expected and (Q(row['return_value'])<expected)==row['strict']
    print('PASS independent entire-interval event replay',interval_counts)
    for p,h in bank['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    print('PASS K2016 separate',len(bank['optimal_physical_witnesses']),'physical optima;',len(bank['near_optimizer_consumers']),'tail consumers;',badsizes,'small completion exclusions;',len(faults),'faults;',len(bank['inputs']),'hashes')
