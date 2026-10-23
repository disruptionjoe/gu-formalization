"""Exact chiral-weighted adjoint obstruction on the inherited raw core."""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json
import k1967_paired_raw_coefficient_observation_probe as base
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1970-weighted-adjoint-mass-completion.json'

def calculate():
    J,C,_,_,_=base.build();old=json.loads(base.REPORT.read_text());rep=old['scalar']['repair'][0]
    a,b,c,d=map(F,rep['parameters']);M=base.decode(rep['M']);T=base.add((-1,base.mul(J[0],M)))
    I={(i,i):F(1) for i in range(128)};B={};Om={(i,i):F(base.omega(i)) for i in range(128)}
    gam=[]
    for k in range(14):gam.append({(i,base.gamrow(k,i)[0]):F(base.gamrow(k,i)[1]) for i in range(128)})
    for i in range(128):j,s=base.chain(tuple(range(7)),i);B[i,j]=F(s)
    assert base.mul(base.tr(B),B)==I
    assert base.add((1,base.mul(B,Om)),(1,base.mul(Om,B)))=={}
    for g in gam:assert base.mul(base.mul(base.tr(B),base.tr(g)),B)==g
    result=[];checks=16
    for name,Q in [('coordinate',I),('spin_invariant',B)]:
        lower={}
        for k in range(14):
            u,w=(a,c) if k in [0,7,8,9] else (b,d)
            O=base.mul(gam[k],{(i,i):F(1 if k<7 else -1)*(u+w*base.omega(i)) for i in range(128)})
            bar=base.mul(base.mul(base.tr(Q),base.tr(O)),Q)
            lower=base.add((1,lower),(-1 if k<7 else 1,base.mul(bar,J[k])))
        assert set(lower)==set(T) and len(T)==128
        ratios={e:{lower[key]/v for key,v in T.items() if base.omega(key[0])==e} for e in [1,-1]}
        assert all(len(v)==1 for v in ratios.values())
        rp,rm=(next(iter(ratios[e])) for e in [1,-1]);product=rp*rm
        assert product!=1 and product>0
        for q in [F(1),F(-1),F(2),F(-3,2),rp,1/rm]:
            for sign in [-1,1]:
                defect={key:(sign*(1/q if base.omega(key[0])==1 else q)*lower[key]-T[key]) for key in T}
                defect={k:v for k,v in defect.items() if v}
                assert len(defect) in [64,128]
                checks+=1
        # Independently free chirality multipliers CAN hit the target, but
        # their product violates the involutive-adjoint condition.
        sp,sm=1/rp,1/rm
        assert sp*sm!=1
        assert all((sp if base.omega(i)==1 else sm)*lower[i,j]==v for (i,j),v in T.items())
        result.append(dict(family=name,positive_ratio=str(rp),negative_ratio=str(rm),product=str(product),obstruction=str(product-1),free_positive_multiplier=str(sp),free_negative_multiplier=str(sm),required_rescaling_squared=str(1/product),minimum_residual_rank=64))
        checks+=5
    return dict(result_id='K1970',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',families=result,exact_controls=checks,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1951-coordinated-zero-southeast-principal.json','lab/process/k1967-paired-raw-coefficient-observation.json','tests/channel-swings/k1967_paired_raw_coefficient_observation_probe.py']},scope='All nonzero complex chiral weights in two declared constant bilinear-adjoint classes and both overall signs. Fixed core and conservative scalar line only; no source-star identification.')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=calculate()
    if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
    else:assert v==json.loads(OUT.read_text())
    print('PASS K1970',v['exact_controls'],v['families'])
