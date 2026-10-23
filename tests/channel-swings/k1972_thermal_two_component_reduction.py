"""Connected-cell vertices plus dimension-charged two-component chords."""
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
import argparse,hashlib,json
import k1968_joint_thermal_finite_dimension_program as old
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1972-thermal-two-component-reduction.json'
def calculate():
    prior=json.loads(old.OUT.read_text());bs=[(tuple(b['S']),tuple(b['A'])) for b in prior['pareto_blocks']]
    single=[];vertices=set();cell_count=0
    for j,(S,A) in enumerate(bs):
        seg={};sites,edges,_,_=old.equations((j,),bs,())
        for orient in product((-1,1),repeat=len(edges)):
            sites,edges,rows,deficit=old.equations((j,),bs,orient)
            for signs in product((-1,1),repeat=len(S)):
                ps=old.cell_vertices(sites,rows,deficit,signs);cell_count+=1
                pts=sorted({(old.dot(S,p),old.rate(sites,p)) for p in ps})
                vertices.update((len(A),e,r) for e,r in pts)
                for e,r in pts:seg[(e,None,F(0),r)]=None
                for (e,r),(f,s) in combinations(pts,2):
                    if e!=f:
                        m=(s-r)/(f-e);seg[e,f,m,r-m*e]=None
        single.append((len(A),seg))
    fronts=[];checks=0
    for d in range(3,9):
        seg={key:None for cost,ss in single if cost<=d for key in ss}
        connected=old.envelope(seg)
        chords=0
        for (k,e,r),(l,f,s) in combinations(sorted(vertices),2):
            if k+l>d or e==f:continue
            if e>f:e,f,r,s=f,e,s,r
            m=(s-r)/(f-e);seg[e,f,m,r-m*e]=None;chords+=1
        pieces=old.envelope(seg)
        assert old.encode(pieces)==prior['frontiers'][d-3]['pieces'],'whole prior frontier recovered'
        fronts.append(dict(d=d,pieces=pieces,connected=connected,chord_count=chords));checks+=1
    # G8 is strictly above F8 in the open disconnected-benefit interval.
    c8=fronts[-1]['connected'];f8=fronts[-1]['pieces'];lo,hi=F(121,91),F(11,5)
    knots=sorted({lo,hi}|{p['lo'] for p in c8 if lo<p['lo']<hi}|{p['lo'] for p in f8 if lo<p['lo']<hi})
    gaps=[]
    for l,h in zip(knots,knots[1:]):
        for E in [(l+h)/2,l,h]:
            gap=old.evaluate(c8,E)-old.evaluate(f8,E)
            assert gap>=0
            if lo<E<hi:assert gap>0
            checks+=1
        gaps.append(dict(lo=l,hi=h,midpoint_gap=old.evaluate(c8,(l+h)/2)-old.evaluate(f8,(l+h)/2)))
    return dict(result_id='K1972',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',connected_cell_count=cell_count,connected_vertex_count=len(vertices),exact_controls=checks,frontiers=fronts,unattained_interval=dict(lo=lo,hi=hi,formula='2/3-E/6',connected_gaps=gaps),inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1968-joint-thermal-finite-dimension-program.json','tests/channel-swings/k1968_joint_thermal_finite_dimension_program.py']},scope='All-d at-most-two populated-component theorem; finite controls and full nonattainment interval only for d8,t=1/2. Coherent physical protocols dominated via pinching; no GU credit.')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=old.encode(calculate())
    if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
    else:assert v==json.loads(OUT.read_text())
    print('PASS K1972',v['connected_cell_count'],v['connected_vertex_count'],v['exact_controls'],v['unattained_interval'])
