"""Independent physical-shell replay and affine support tests; no producer import."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,copy
from k2039_thermal_component_undercut_probe import physical
ROOT=Path(__file__).resolve().parents[2]

def verify(r):
    for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'provenance'
    ea,ra=map(F,r['endpoint_A']);eb,rb=map(F,r['endpoint_B']);a,c=map(F,r['line']);D=eb-ea;delta=F(r['certified_spacing'])
    bank=json.loads((ROOT/'lab/process/k2037-thermal-seven-level-boundary.json').read_text())['banks']['9'];ct=0;bounds={'A':[],'B':[]}
    for cell in bank:
        ss=list(map(F,cell['s']));zero=set()
        for v in cell['vertices']:
            pp=list(map(F,v['p']));rr,_=physical(ss,pp,list(map(F,range(13))),F(1));ee=sum(x*y for x,y in zip(ss,pp));ct+=1
            assert rr==F(v['value']) and ee==F(v['energy'])
            gap=rr+c*ee-a
            if not gap:zero.add((ee,rr));continue
            ca=(ra-rb)/(D+delta);cb=(ra-rb)/(D-delta)
            assert rr+ca*ee>=ra+ca*ea,'A support line'
            assert rr+cb*ee>=rb+cb*eb,'B support line'
            for label,den in [('A',c*(ee-ea)-gap),('B',c*(eb-ee)+gap)]:
                if den>0:bounds[label].append((D*gap/den,ee,rr))
        assert len(zero)<=1
    for label in bounds:assert list(map(str,min(bounds[label])))==r[label+'_certificate_limit']
    assert ct==r['bank_records']==3137
    pa=list(map(F,[F(486,1306),F(729,1306),F(81,1306),F(9,1306),F(1,1306)]));pb=[F(x,181) for x in (36,54,81,9,1)]
    ss=list(map(F,[1,3,5,7,9]));checks=0
    assert physical(ss,pa,list(map(F,range(11))),F(1))[0]==ra,'endpoint A return'
    assert physical(ss,pb,list(map(F,range(11))),F(1))[0]==rb,'endpoint B return'
    for d in [delta/3,delta/2,delta]:
        for x in [F(0),D/5,D/2,(D+d)/2,3*D/4,D]:
            left=c*d*x/(D+d);right=c*d*(D-x)/(D-d);shift_b=left<=right
            mass_b=x/(D+d) if shift_b else (x-d)/(D-d)
            assert 0<=mass_b<=1
            support=[y+(0 if shift_b else d) for y in ss]+[y+(d if shift_b else 0) for y in ss]
            pop=[(1-mass_b)*y for y in pa]+[mass_b*y for y in pb]
            spec=sorted([F(y) for y in range(11)]+[F(y)+d for y in range(11)])
            value,_=physical(support,pop,spec,d)
            assert value==a-c*(ea+x)+min(left,right)
            assert sum(z*p for z,p in zip(support,pop))==ea+x
            checks+=1
        assert c*d*((D+d)/2)/(D+d)==c*d/2
    # Exact finite-delta remainder identities and the moving maximum.
    for d in [delta/2,delta]:
        for x in [D/4,D/2,3*D/4]:
            left=c*d*x/(D+d);right=c*d*(D-x)/(D-d)
            if x<=D/2:
                assert left-c*x*d/D == -c*x*d*d/(D*(D+d))
            else:
                assert right-c*(D-x)*d/D == c*(D-x)*d*d/(D*(D-d))
        for theta in [F(-1),F(0),F(1,4),F(1,2),F(1)]:
            x=D/2+theta*d
            actual=min(c*d*x/(D+d),c*d*(D-x)/(D-d))-c*min(x,D-x)*d/D
            if theta<=0: expected=-c*x*d*d/(D*(D+d))
            elif theta<=F(1,2): expected=c*d*d*(2*D*theta-D/2+theta*d)/(D*(D+d))
            else:expected=c*(D-x)*d*d/(D*(D-d))
            assert actual==expected,'boundary layer exact remainder'
    # Each endpoint forces all11 completion levels: remove each level and test real capacities.
    necessary=0
    for pop in (pa,pb):
        physical(ss,pop,list(map(F,range(11))),F(1))
        for missing in range(11):
            try:physical(ss,pop,[F(y) for y in range(11) if y!=missing],F(1))
            except AssertionError:necessary+=1
            else:raise AssertionError('unneeded completion level')
    assert necessary==22
    w=r['successor_witness'];d,e,t=map(F,[w['delta'],w['energy'],w['shifted_mass']]);pold=[F(x,145) for x in (54,81,9,1)]
    support=[F(y)+d for y in [1,3,5,7]]+ss;pop=[t*y for y in pold]+[(1-t)*y for y in pb]
    spec=sorted([F(y)+d for y in range(9)]+[F(y) for y in range(11)])
    val,_=physical(support,pop,spec,d)
    assert val==F(w['return_value']) and sum(x*y for x,y in zip(support,pop))==e
    assert len(spec)==20 and F(w['old_return'])-val==F(w['improvement'])>0
    return ct,checks,necessary
if __name__=='__main__':
    r=json.loads((ROOT/'lab/process/k2041-exact-small-spacing-frontier.json').read_text());print('PASS baseline',verify(r))
    # Data mutations: support-line range, endpoint return, physical successor population and return.
    for label,mut in [('range-overreach',lambda x:x.__setitem__('certified_spacing',str(2*F(x['certified_spacing'])))),('endpoint-return',lambda x:x['endpoint_A'].__setitem__(1,'1/4')),('successor-mass',lambda x:x['successor_witness'].__setitem__('shifted_mass','1/2')),('successor-return',lambda x:x['successor_witness'].__setitem__('return_value','0'))]:
        b=copy.deepcopy(r);mut(b)
        try:verify(b)
        except AssertionError as e:print('DETECTED',label,str(e))
        else:raise AssertionError('MISSED '+label)
    print('PASS four actual coefficient/range/physical-data faults')
