"""Exact first-jet density/pairing correction on the fixed raw1920 core."""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json
from k1970_weighted_adjoint_mass_completion_probe import plus,product,dec
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1973-differential-adjoint-density.json'
def data():
    I={(j,j):F(1) for j in range(128)};gam=[]
    for k in range(14):
        axis=k%7;g={}
        for j in range(128):
            bits=[(j>>(6-n))&1 for n in range(7)];v=(-1)**sum(bits[:axis])
            if k>=7:v*=(-1 if bits[axis]==0 else 1)
            g[j^(1<<(6-axis)),j]=F(v)
        gam.append(g)
    vol=I
    for g in gam:vol=product(vol,g)
    J=[{} for _ in range(15)]
    for n,b in enumerate(json.loads((ROOT/'lab/process/k1951-coordinated-zero-southeast-principal.json').read_text())['blocks']):
        for (i,j),v in product(dec(b['basis']),dec(b['section'])).items():
            c=b['coordinates'][i];J[c//128][c%128,4*n+j]=v
    M=dec(json.loads((ROOT/'lab/process/k1967-paired-raw-coefficient-observation.json').read_text())['scalar']['repair'][0]['M'])
    return vol,J,{k:-v for k,v in product(J[0],M).items()}
def calculate():
    vol,J,T=data();cols=[]
    for k in range(14):
        for sign in [1,-1]:cols.append({ij:v for ij,v in J[k].items() if vol[ij[0],ij[0]]==sign})
    support=set().union(*(x.keys() for x in cols));assert not support&set(T)
    # Rank by exact sparse elimination, not a numeric tolerance.
    piv={}
    for col in cols:
        v=col.copy()
        while v:
            i=min(v)
            if i not in piv:
                a=v[i];piv[i]={j:b/a for j,b in v.items()};break
            v=plus(v,piv[i],-v[i])
    assert len(piv)==28
    ratios=json.loads((ROOT/'lab/process/k1970-weighted-adjoint-mass-completion.json').read_text())['families']
    for r in ratios:assert F(r['product'])!=1
    return dict(result_id='K1973',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',gradient_parameters=28,gradient_rank=len(piv),gradient_entry_support=len(support),target_entry_support=len(T),overlap=0,target_entries=[[i,j,str(v)] for (i,j),v in sorted(T.items())],families=ratios,scope='All smooth nonzero chiral-diagonal bilinear weights and positive scalar densities on fixed flat principal/core data; no source star or arbitrary pairing exclusion.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1951-coordinated-zero-southeast-principal.json','lab/process/k1967-paired-raw-coefficient-observation.json','lab/process/k1970-weighted-adjoint-mass-completion.json','tests/channel-swings/k1970_weighted_adjoint_mass_completion_probe.py']})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=calculate()
    if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
    else:assert v==json.loads(OUT.read_text())
    print('PASS K1973 gradient rank',v['gradient_rank'],'target projection overlap',v['overlap'])
