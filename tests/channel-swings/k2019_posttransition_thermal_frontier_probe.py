"""Separate rational interpolation / exact-extremum verifier of all frontier obligations.
No producer polynomial arithmetic, Bernstein implementation or cone coefficients are used.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json,hashlib
from k2015_finite_thermal_ray_separation_probe import bath_planes
ROOT=Path(__file__).resolve().parents[2]
A=Q(6,5);B=Q(11,5);C=Q(113,91);RC=Q(81,182)
REGIMES=[(Q(4,15),Q(36,91),B,Q(3,10),Q(3,20),-1),(Q(36,91),Q(2,5),Q(19,8),Q(9,32),Q(3,20),-1),(Q(2,5),Q(1,2),Q(19,8),Q(9,32),Q(1,4),0)]
def poly(fn):
    y0,y1,y2=[fn(Q(i)) for i in (0,1,2)];c=(y2-2*y1+y0)/2
    return (y0,y1-y0-c,c)
def val(p,x):return p[0]+x*(p[1]+x*p[2])
def extrema(p,l,h):
    vs=[val(p,l),val(p,h)]
    if p[2]:
        z=-p[1]/(2*p[2])
        if l<z<h:vs.append(val(p,z))
    return min(vs),max(vs)
def certify(p,cs,l,h):
    todo=[(l,h,0)];parts=0
    while todo:
        lo,hi,n=todo.pop()
        if any(extrema(c,lo,hi)[1]<0 for c in cs):continue
        if extrema(p,lo,hi)[0]>=0:parts+=1;continue
        d=(lo+hi)/2
        assert not(all(val(c,d)>=0 for c in cs) and val(p,d)<0),'feasible negative polynomial'
        assert n<64,'unresolved polynomial domain'
        todo.extend([(lo,d,n+1),(d,hi,n+1)])
    return parts

def replay(c,reg):
    lo,hi,top,rv,rr,k=reg;u=RC-rv;v=top-C;counts={};parts=0
    def targets(d):
        ul=v+d;ur=1+k*d;den=rr*ul-u*ur
        x=(Q(3,10)-RC)*ul*ur+rr*B*ul-u*C*ur
        y=rr*RC*ul-u*Q(3,10)*ur+rr*u*(C-B)
        return den,x,y
    for fn in [lambda d:targets(d)[0],lambda d:targets(d)[1]-Q(17,10)*targets(d)[0],lambda d:B*targets(d)[0]-targets(d)[1]]:
        assert extrema(poly(fn),lo,hi)[0]>0
    def check(kind,fn,conditions):
        nonlocal parts
        counts[kind]=counts.get(kind,0)+1;parts+=certify(poly(fn),[poly(f) for f in conditions],lo,hi)
    rs=sorted({(Q(v['energy']),Q(v['return'])) for cell in c['cells'] for v in cell['vertices']})
    for e,R in rs:
      for b in (0,1):
        common=[lambda d:e+b*d-A,lambda d:B-e-b*d]
        check('single_AC',lambda d:R-Q(9,20)+Q(9,76)*(e+b*d-A),common+[lambda d:C-e-b*d])
        check('single_CB',lambda d:(R-RC)*(v+d)+u*(e+b*d-C),common+[lambda d:e+b*d-C,lambda d:targets(d)[1]-(e+b*d)*targets(d)[0]])
        check('single_GA',lambda d:(R-Q(3,10))*(1+k*d)-rr*(B-e-b*d),common+[lambda d:(e+b*d)*targets(d)[0]-targets(d)[1]])
    def pair(e,R,b,f,S,j,kind):
        def gap(d):
            den,x,y=targets(d)
            return R*((f+j*d)*den-x)+S*(x-(e+b*d)*den)-(f-e+(j-b)*d)*y
        check(kind,gap,[lambda d:targets(d)[1]-(e+b*d)*targets(d)[0],lambda d:(f+j*d)*targets(d)[0]-targets(d)[1]])
    for e,R in rs:
      for f,S in rs:
        if e<=B and f+hi>=Q(17,10):pair(e,R,0,f,S,1,'sep')
        if f<=B and e+hi>=Q(17,10):pair(f,S,1,e,R,0,'sep')
    for cell in c['cells']:
        _,_,df=bath_planes(tuple(cell['support']),tuple(cell['orientation']),True);vs=cell['vertices']
        signs=[[sum(a*Q(b) for a,b in zip(row,v['p'])) for row in df] for v in vs]
        for i,j in combinations(range(len(vs)),2):
            if any(x*y<0 for x,y in zip(signs[i],signs[j])):continue
            e,R=Q(vs[i]['energy']),Q(vs[i]['return']);f,S=Q(vs[j]['energy']),Q(vs[j]['return'])
            if e>f:e,f,R,S=f,e,S,R
            if e<=B and f>=Q(17,10):pair(e,R,0,f,S,0,'same')
    return counts,parts

if __name__=='__main__':
    r=json.loads((ROOT/'lab/process/k2019-posttransition-thermal-frontier.json').read_text());c=json.loads((ROOT/'lab/process/k2015-finite-thermal-ray-separation.json').read_text())['census']
    assert len(r['certificates'])==len(REGIMES)==3
    total=0
    for reg,bank in zip(REGIMES,r['certificates']):
        assert bank['interval']==list(map(str,reg[:2]));counts,parts=replay(c,reg);assert counts==bank['obligation_counts'];total+=parts
        print('PASS separate interval',bank['interval'],counts,'accepted partitions',parts,flush=True)
    # Green baseline, then actual polynomial/constrained-domain faults.
    assert certify((Q(0),Q(0),Q(1)),[],Q(-1),Q(1))
    faults=0
    for p,cs,lo,hi in [((Q(-1,100),Q(0),Q(1)),[],Q(-1),Q(1)),((Q(-1),Q(0),Q(0)),[(Q(1),Q(0),Q(0))],Q(0),Q(1)),((Q(0),Q(1),Q(-2)),[],Q(0),Q(1))]:
        try:certify(p,cs,lo,hi)
        except AssertionError:faults+=1
        else:raise AssertionError('accepted corrupted sign certificate')
    for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    print('PASS K2019 separate complete coverage',total,'partitions;',faults,'actual sign faults;',len(r['inputs']),'provenance hashes')
