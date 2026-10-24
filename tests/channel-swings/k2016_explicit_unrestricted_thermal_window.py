"""Explicit global thermal window from the complete cutoff-nine cone census."""
from fractions import Fraction as Q
from pathlib import Path
import argparse,json,hashlib
from k2014_unrestricted_ten_level_onset import witness,G,B
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2016-explicit-unrestricted-thermal-window.json'
L=Q(3,20);A=Q(6,5);Z=Q(11,5);C=Q(11,50);D=Q(1,15)
def encode(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x

def produce():
    census=json.loads((ROOT/'lab/process/k2015-finite-thermal-ray-separation.json').read_text())['census'];ca=Q(census['directional_slopes']['without_B']);cb=Q(census['directional_slopes']['without_A'])
    assert ca/(L-ca)==Q(27,620) and cb/(L+cb)==Q(3,380)
    assert Q(census['compatible_interval_certificate']['delta_max'])>=D
    controls=0
    for cell in census['cells']:
        for v in cell['vertices']:
            e,R,z=map(Q,[v['energy'],v['return'],v['surplus']]);p=list(map(Q,v['p']));ss=cell['support'];actual=[(s,x) for s,x in zip(ss,p) if x]
            isA=actual==[(1,Q(9,10)),(3,Q(1,10))];isB=actual==[(1,Q(2,5)),(3,Q(3,5))]
            if not isB:assert z>=ca*(e-A);controls+=1
            if not isA:assert z>=cb*(Z-e);controls+=1
    rows=[];near=[];slopes=0
    budgets=[A+Q(k,20) for k in range(1,20)]+[A+Q(1,10**6),Z-Q(1,10**6)]
    for E in budgets:
      r=E-A
      for d in [Q(1,1000),Q(1,200),D]:
        g=G(d,E)-B(E)
        row=witness(d,E,'B' if r<=(1+d)/2 else 'A');assert row['return_value']==G(d,E)
        qbar=g/C;Ep=(E-9*qbar)/(1-qbar);m=L/(1+d) if E<Q(15,8) else L/(1-d);kappa=m*(9-E)-1;assert A<Ep<=E<Z and kappa>0
        if E>=Q(15,8):assert Ep>Q(17,10)+d/2
        assert qbar<=Q(15,22)*d*r/(1+d)
        assert d<=D<Q(22,95) and kappa>=Q(1,512)
        assert G(d,Ep)>=G(d,E)+m*(E-Ep)
        row.update(certified_global_optimum=True,tail_mass_prebound=qbar,retained_budget_lower=Ep,kappa=kappa,faithful_bath_TV_radius=g/2,gibbs_t_radius=g/12)
        rows.append(row)
        epsmax=min(C*r/(2*(9-A))-g,Q(1,10000));assert epsmax>0
        for eps in [epsmax/100,epsmax/2,epsmax]:
            qb=(g+eps)/C;ep=(E-9*qb)/(1-qb);bound=eps/(kappa+eps)
            assert qb<=r/(2*(9-A)) and ep>A and bound>0
            if E>=Q(15,8):assert ep>Q(17,10)+d/2
            # Exact equivalence epsilon >= kappa*q/(1-q) iff q<=bound.
            for q in [Q(0),bound/2,bound, min(Q(9,10),(1+bound)/2)]:
                assert (eps>=kappa*q/(1-q))==(q<=bound);slopes+=1
            near.append(dict(delta=d,energy=E,epsilon=eps,epsilon_max=epsmax,tail_mass_bound=bound,preliminary_mass_bound=qb,retained_budget_lower=ep))
    counter=[]
    for delta in [Q(4,15),Q(3,10),Q(1,2)]:
        e=Q(113,91);rv=Q(81,182);candidate=G(delta,e);assert rv<=candidate
        if delta>Q(4,15):assert rv<candidate
        counter.append(dict(delta=delta,energy=e,spectrum=list(range(7)),support=[1,3,5],populations=[Q(81,91),Q(9,91),Q(1,91)],return_value=rv,ten_level_formula=candidate,strict=delta>Q(4,15)))
    inputs=['lab/process/k2015-finite-thermal-ray-separation.json','explorations/conditional-build/k2013-energy-sensitive-thermal-cutoff-2026-10-24.md','explorations/conditional-build/k2012-thermal-duality-gap-and-bath-stability-2026-10-24.md','tests/channel-swings/k2014_unrestricted_ten_level_onset.py']
    return encode(dict(result_id='K2016',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',window=dict(spacing_max=D,energy_lower=A,energy_upper=Z,endpoint_included=True,energy_endpoints_excluded=True,sharp_threshold_claim=False),directional_certificates=dict(without_B_slope=ca,without_A_slope=cb,without_B_spacing=ca/(L-ca),without_A_spacing=cb/(L+cb)),optimal_physical_witnesses=rows,near_optimizer_consumers=near,larger_spacing_counterexamples=counter,counts=dict(ray_inequalities=controls,optimal_witnesses=len(rows),near_optimizer_consumers=len(near),tail_equivalence_controls=slopes),scope='Exact unrestricted finite-or-countable optimum on a single uniform explicit positive-spacing interval. The sufficient endpoint1/15 is not claimed sharp. Exact channel, four-state bath, nondegenerate spectrum and marginal return only; no GU physics.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs}))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce()
    if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert r==json.loads(OUT.read_text()),'certificate drift'
    print('PASS K2016',r['counts'])
