"""Exact odd-tail recurrence and a finite separated-component counterexample."""
from pathlib import Path
from fractions import Fraction as Q
import argparse, hashlib, json
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k2039-thermal-component-undercut.json'
E0,R0=Q(1575,653),Q(729,2612)
EB,RB=Q(675,181),Q(81,362)
EI,RI=Q(415,172),Q(12,43)
LA,LC=Q(1053,2768),Q(2907,69200)
PA=[Q(x,1306) for x in (486,729,81,9,1)]
PB=[Q(x,181) for x in (36,54,81,9,1)]
def edge_return(s,p):
    inc=[Q(0)]*len(s)
    for i in range(len(s)-1):
        if s[i+1]-s[i]!=2:raise ValueError('odd chain required')
        flow=(3*p[i]-12*p[i+1])/15
        inc[i]+=max(-flow,0);inc[i+1]+=max(flow,0)
    return sum(max(x-y,0) for x,y in zip(p,inc))/2

def family(m):
    q=Q(1,9)**(m+1)
    Z=(43-27*q)/16;H=(415-27*(8*m+21)*q)/64
    w=[Q(1)]+[Q(3,2*9**j) for j in range(m+1)]
    s=list(range(1,2*len(w),2));p=[x/Z for x in w]
    assert sum(w)==Z and sum(x*y for x,y in zip(s,w))==H
    assert edge_return(s,p)==Q(3,4)/Z
    C=48/(344*m+445+27*q)
    return s,p,H/Z,Q(3,4)/Z,C

def produce():
    assert edge_return([1,3,5,7,9],PA)==R0
    assert edge_return([1,3,5,7,9],PB)==RB
    assert LA-LC*E0==R0 and LA-LC*EB==RB
    assert 10*LC-LA==Q(549,13840)>0
    bank=json.loads((ROOT/'lab/process/k2037-thermal-seven-level-boundary.json').read_text())['banks']['9']
    positive=[];contacts=set();records=0
    for cell in bank:
        local=set()
        for v in cell['vertices']:
            e,r=Q(v['energy']),Q(v['value']);gap=r+LC*e-LA;records+=1
            assert gap>=0 and 0<=e<=9
            contact=tuple((x,y) for x,y in zip(cell['s'],v['p']) if Q(y))
            if gap:positive.append(gap)
            else:local.add(contact);contacts.add(contact)
        assert len(local)<=1,'orientation cell mixes endpoint contacts'
    assert len(contacts)==2 and len(bank)==183 and records==3137
    gamma=min(positive);assert gamma==Q(9,5017000)
    kappa=10*LC-LA;KA=max((9-E0)/gamma,(10-E0)/kappa,1/LC);KB=EB/gamma;K=max(KA,KB);Delta=EB-E0
    assert K==Q(2398126000,653) and Delta>1
    uniform_M=max(LC*LC*K/(2*Delta),LC/(2*(Delta-Q(1,2))))
    rows=[]
    for m in range(13):
        s,p,e,r,c=family(m);ss,pp,ee,rr,_=family(m+1)
        assert r==c*(2*m+5-e) and rr==c*(2*m+5-ee)
        for u in (Q(0),Q(1,3),Q(1,2),Q(1)):
            pm=[(1-u)*x+u*y for x,y in zip(p+[Q(0)],pp)]
            assert edge_return(ss,pm)==(1-u)*r+u*rr
        threshold=None if m<4 else (R0-RB)*(e-E0)/(R0-r)-(EB-E0)
        rows.append(dict(tail=m,support=s,population=list(map(str,p)),energy=str(e),value=str(r),next_slope=str(c),next_intercept=str((2*m+5)*c),mixture_threshold=None if threshold is None else str(threshold)))
    dstar=(R0-RB)/family(3)[4]-(EB-E0)
    dinf=(R0-RB)*(EI-E0)/(R0-RI)-(EB-E0)
    assert dstar==Q(628,1629) and dinf==Q(315,724)
    thresholds=[Q(row['mixture_threshold']) for row in rows if row['mixture_threshold']]
    assert thresholds[0]==dstar and all(a<b<dinf for a,b in zip(thresholds,thresholds[1:]))
    d=Q(1,4);t=(EI-E0)/(EB+d-E0);value=(1-t)*R0+t*RB
    assert t==Q(17195,31862699) and value==Q(17783631,63725398)
    assert RI-value==Q(201,63725398)>0
    s=list(map(Q,[1,3,5,7,9]))+[Q(x)+d for x in [1,3,5,7,9]]
    p=[(1-t)*x for x in PA]+[t*x for x in PB]
    spec=sorted([Q(x) for x in range(11)]+[Q(x)+d for x in range(11)])
    assert sum(p)==1 and sum(x*y for x,y in zip(s,p))==EI
    assert min(b-a for a,b in zip(spec,spec[1:]))==d
    inputs=['lab/process/k2010-countable-thermal-attainment.json','lab/process/k1952-catalyst-path-energy-extension.json','lab/process/k2037-thermal-seven-level-boundary.json','lab/process/k2020-posttransition-tail-and-resources.json']
    return dict(result_id='K2039',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',tail_family=rows,endpoint_A=dict(energy=str(E0),value=str(R0),population=list(map(str,PA))),endpoint_B=dict(energy=str(EB),value=str(RB),population=list(map(str,PB))),polyhedral_stability=dict(bank_orientation_cells=len(bank),bank_vertex_records=records,positive_vertex_gap=str(gamma),contact_count=len(contacts),max_contacts_per_orientation=1,KA=str(KA),KB=str(KB),K=str(K),energy_width=str(Delta),lower_bound='C*delta*min(E-EA,EB-E)/(Delta+C*delta*K)',asymptotic='F_delta(E)=L(E)+C*min(E-EA,EB-E)*delta/Delta+O(delta^2), uniformly on [EA,EB]',uniform_remainder_constant=str(uniform_M),rate_scope='0<delta<=1/2; coefficient sharp, finite-spacing optimum and second-order coefficient unproved'),strict_spacing_gap=dict(spacing='0<delta<=1',energy='1575/653<E<675/181',tail_charge='549/13840',conclusion='F_delta(E)>L(E); positive minimum gap on every closed rectangle delta_min<=delta<=1, a<=E<=b strictly inside the energy interval',proof='K2010 unrestricted attainment and lower semicontinuity + K2037 strict tail/offset charge + K1952 finite equality/nonattainment',rate='explicit linear lower bound and sharp uniform first-order law from polyhedral stability'),zero_spacing_limit=dict(intercept=str(LA),slope=str(LC),interval=[str(E0),str(EB)],error_bound='LC*delta*(E-E0)/(EB+delta-E0) <= LC*delta',status='K1952 chord recovered with two components and an explicit uniform spacing-error bound'),next_connected_line=dict(intercept='8019/22432',slope='729/22432',interval=['1575/653','28361/11755'],status='feasible, unrestricted optimality refuted at sufficiently small spacing'),separated_thresholds=dict(first_segment=str(dstar),countable_limit=str(dinf),meaning='sharp only for this fixed A/B shifted-mixture comparison'),witness=dict(delta=str(d),mixing_weight=str(t),energy=str(EI),support=list(map(str,s)),population=list(map(str,p)),spectrum=list(map(str,spec)),physical_dimension=len(spec),return_value=str(value),odd_tail_limit=str(RI),strict_improvement=str(RI-value)),inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},scope='Sharp uniform first-order spacing law, exact lower bound, and finite counterexample to all-spacing odd-tail optimality. No unrestricted optimum, sharp minimum dimension, GU mechanism or novelty claim.')
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce()
    if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert r==json.loads(OUT.read_text())
    print('PASS K2039',len(r['tail_family']),'exact family controls; finite22-level strict undercut')
