"""Independent rational bath-shell check, component separation, and real faults."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
BATH=[F(8,15),F(4,15),F(2,15),F(1,15)]
def bath_index(z,x):
    d=z-x
    return int(d) if d.denominator==1 and 0<=d<=3 else None

def physical(s,p,spec,delta):
    assert len(s)==len(p) and sum(p)==1 and min(p)>=0,'population'
    assert set(s)<=set(spec),'support completion'
    spec=sorted(spec);assert len(spec)==len(set(spec)) and min(spec)>=0,'spectrum'
    assert all(b-a>=delta for a,b in zip(spec,spec[1:])),'spacing'
    active=[x for x,v in zip(s,p) if v]
    for z in {x+b for x in active for b in range(4)}:
        assert sum(bath_index(z,x) is not None for x in spec)>=2*sum(bath_index(z,x) is not None for x in active),'shell capacity'
    deficits=[]
    for x,v in zip(s,p):
        retained=F(0)
        for b in range(4):
            z=x+b
            retained+=max(q*BATH[k] for y,q in zip(s,p) if (k:=bath_index(z,y)) is not None)
        deficits.append(v-retained/2)
    return sum(max(v,0) for v in deficits),deficits

def replay(r):
    for path,digest in r['inputs'].items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,'input provenance'
    for row in r['tail_family']:
        s=list(map(F,row['support']));p=list(map(F,row['population']));spec=list(map(F,range(int(max(s))+2)))
        rr,dd=physical(s,p,spec,F(1))
        assert rr==F(row['value']) and sum(x*y for x,y in zip(s,p))==F(row['energy'])
        assert dd[1]==p[1]/2 and all(v<=0 for i,v in enumerate(dd) if i!=1)
    a,b=r['endpoint_A'],r['endpoint_B'];e0,r0=F(a['energy']),F(a['value']);eb,rb=F(b['energy']),F(b['value'])
    for end in (a,b):
        rr,_=physical(list(map(F,[1,3,5,7,9])),list(map(F,end['population'])),list(map(F,range(11))),F(1));assert rr==F(end['value'])
    dstar,dinf=map(F,[r['separated_thresholds']['first_segment'],r['separated_thresholds']['countable_limit']])
    slope=F(r['next_connected_line']['slope']);ei,ri=F(415,172),F(12,43)
    lim=r['zero_spacing_limit'];la,lc=F(lim['intercept']),F(lim['slope'])
    assert la-lc*e0==r0 and la-lc*eb==rb
    assert 10*lc-la==F(r['strict_spacing_gap']['tail_charge'])>0
    bank=json.loads((ROOT/'lab/process/k2037-thermal-seven-level-boundary.json').read_text())['banks']['9']
    positives=[];contact_set=set();count=0
    for cell in bank:
        cell_contacts=set();ss=list(map(F,cell['s']))
        for v in cell['vertices']:
            pp=list(map(F,v['p']));value,_=physical(ss,pp,list(map(F,range(13))),F(1))
            energy=sum(x*y for x,y in zip(ss,pp));gap=value+lc*energy-la;count+=1
            assert value==F(v['value']) and energy==F(v['energy']) and gap>=0
            if gap:positives.append(gap)
            else:
                endpoint=tuple((x,y) for x,y in zip(ss,pp) if y);cell_contacts.add(endpoint);contact_set.add(endpoint)
        assert len(cell_contacts)<=1,'orientation stability'
    st=r['polyhedral_stability'];gamma=min(positives);kappa=10*lc-la
    ka=max((9-e0)/gamma,(10-e0)/kappa,1/lc);kb=eb/gamma;K=max(ka,kb);Delta=eb-e0
    assert gamma==F(st['positive_vertex_gap']) and count==st['bank_vertex_records']==3137
    assert len(contact_set)==st['contact_count']==2 and K==F(st['K'])
    M=max(lc*lc*K/(2*Delta),lc/(2*(Delta-F(1,2))))
    assert M==F(st['uniform_remainder_constant'])
    for d in [F(1,1000000),F(1,1000),F(1,4),F(1,2)]:
        for x in [F(0),Delta/4,Delta/2,3*Delta/4,Delta]:
            e=e0+x;dist=min(x,Delta-x);leading=lc*dist*d/Delta
            low=lc*d*dist/(Delta+lc*d*K)
            upper=lc*d*x/(Delta+d) if x<=Delta/2 else lc*d*(Delta-x)/(Delta-d)
            assert low<=upper and leading-M*d*d<=low and upper<=leading+M*d*d
            # Independent physical construction, including the newly swapped endpoint placement.
            shift_b=x<=Delta/2
            t=x/(Delta+d) if shift_b else (x-d)/(Delta-d)
            assert 0<=t<=1
            ss=[F(j)+(0 if shift_b else d) for j in [1,3,5,7,9]]+[F(j)+(d if shift_b else 0) for j in [1,3,5,7,9]]
            pp=[(1-t)*F(y) for y in a['population']]+[t*F(y) for y in b['population']]
            sp=sorted([F(j) for j in range(11)]+[F(j)+d for j in range(11)])
            value,_=physical(ss,pp,sp,d)
            assert sum(xx*yy for xx,yy in zip(ss,pp))==e and value-(la-lc*e)==upper
    assert (r0-rb)/(eb+dstar-e0)==slope
    assert (r0-rb)/(eb+dinf-e0)==(r0-ri)/(ei-e0)
    w=r['witness'];s,p,spec=([F(x) for x in w[k]] for k in ('support','population','spectrum'));d=F(w['delta'])
    assert all(bath_index(x,y) is None for x in s[:5] for y in s[5:]),'distinct resonance components'
    rr,defs=physical(s,p,spec,d);assert rr==F(w['return_value'])
    assert sum(x*y for x,y in zip(s,p))==F(w['energy']) and ri-rr==F(w['strict_improvement'])>0
    assert len(spec)==22 and sum(v>0 for v in defs)==2
    # Whole shifted family: linearity follows because fractional residues are distinct.
    for d in [F(1,8),F(1,4),dstar,dinf,F(1,2)]:
        for t in [F(1,100000),F(1,7),F(1,2)]:
            ss=list(map(F,[1,3,5,7,9]))+[F(x)+d for x in [1,3,5,7,9]]
            pp=[(1-t)*F(x) for x in a['population']]+[t*F(x) for x in b['population']]
            sp=sorted([F(x) for x in range(11)]+[F(x)+d for x in range(11)])
            value,_=physical(ss,pp,sp,d);energy=sum(x*y for x,y in zip(ss,pp))
            assert value==(1-t)*r0+t*rb and energy==(1-t)*e0+t*(eb+d)
            gap=slope*(11-energy)-value
            assert gap==t*slope*(dstar-d)
    for d in [F(1,1000),F(1,4),F(1,2)]:
        for e in [e0,(e0+eb)/2,eb]:
            t=(e-e0)/(eb+d-e0);value=(1-t)*r0+t*rb;excess=value-(la-lc*e)
            assert excess==lc*d*(e-e0)/(eb+d-e0) and 0<=excess<=lc*d
    return dict(family_controls=len(r['tail_family']),physical_dimension=len(spec),witness_return=str(rr),stability_vertices=count,sharp_rate_controls=20)

def faults(r):
    w=r['witness'];s,p,spec=([F(x) for x in w[k]] for k in ('support','population','spectrum'));d=F(w['delta']);caught=[]
    for label,pp,sp,dd in [('normalization',[2*x for x in p],spec,d),('missing completion',p,[x for x in spec if x!=2],d),('spacing',p,spec,F(1,3))]:
        try:physical(s,pp,sp,dd)
        except AssertionError:caught.append(label)
        else:raise AssertionError('missed '+label)
    value,_=physical(s,p,spec,d);assert value!=F(w['return_value'])+F(1,1000000);caught.append('return corruption')
    # Merging both components onto one ladder loses affine return: actual fault, not a metadata edit.
    a,b=r['endpoint_A'],r['endpoint_B'];pm=[(F(x)+F(y))/2 for x,y in zip(a['population'],b['population'])]
    merged,_=physical(list(map(F,[1,3,5,7,9])),pm,list(map(F,range(11))),F(1))
    assert merged>(F(a['value'])+F(b['value']))/2;caught.append('false same-ladder convexification')
    dwrong=F(1,2);ei,ri=F(415,172),F(12,43);e0,r0=F(a['energy']),F(a['value']);eb,rb=F(b['energy']),F(b['value'])
    twrong=(ei-e0)/(eb+dwrong-e0);wrong=(1-twrong)*r0+twrong*rb
    assert wrong-ri==F(141,147779992)>0;caught.append('overextended spacing range')
    # Raising the stability margin fails on the actual previous-phase endpoint.
    ss=list(map(F,[1,3,5,7]));pp=[F(x,145) for x in [54,81,9,1]]
    value,_=physical(ss,pp,list(map(F,range(9))),F(1));energy=sum(x*y for x,y in zip(ss,pp))
    actual=value+F(2907,69200)*energy-F(1053,2768)
    assert actual==F(9,5017000)<2*F(r['polyhedral_stability']['positive_vertex_gap']);caught.append('inflated stability margin')
    return caught
if __name__=='__main__':
    r=json.loads((ROOT/'lab/process/k2039-thermal-component-undercut.json').read_text());print('BASELINE',replay(r));print('PASS faults',faults(r))
