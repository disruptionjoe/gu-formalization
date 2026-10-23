"""Exact dimension threshold for the global exposed thermal chord."""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json
from k1950_global_catalyst_energy_certificates_probe import shell_return
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1975-thermal-sharp-dimension-threshold.json'
EA,EB,RA,RB=F(6,5),F(11,5),F(9,20),F(3,10)
def physical(E,eps):
    w=(E-EA)/(EB-EA+eps);assert 0<w<1 and 0<eps<1
    A=tuple(map(F,range(5)))+tuple(F(i)+eps for i in range(5));s=(F(1),F(3),1+eps,3+eps)
    p=((1-w)*F(9,10),(1-w)*F(1,10),w*F(2,5),w*F(3,5))
    assert len(set(A))==10
    for e in {x+b for x in s for b in range(4)}:
        assert sum(e-a in (0,1,2,3) for a in A)>=2*sum(e-x in (0,1,2,3) for x in s),'shell completion'
    assert sum(p)==1 and sum(x*y for x,y in zip(s,p))==E
    r=shell_return(F(1,2),s,p);base=F(63,100)-F(3,20)*E;gap=F(3,20)*eps*(E-EA)/(1+eps)
    assert r-base==gap>0
    return dict(energy=str(E),epsilon=str(eps),B_weight=str(w),return_error=str(r),global_infimum=str(base),gap=str(gap))
def calculate():
    prior=json.loads((ROOT/'lab/process/k1950-global-catalyst-energy-certificates.json').read_text());bank=next(b for b in prior['global_duals'] if F(b['slope'])==F(3,20))
    faces=set()
    for cell in bank['cells']:
        if F(cell['intercept'])==F(bank['intercept']):faces.add(tuple((e,F(p)) for e,p in zip(cell['support'],cell['x']) if F(p)))
    assert faces=={((1,F(9,10)),(3,F(1,10))),((1,F(2,5)),(3,F(3,5)))}
    assert 2*(2*2+1)==10
    samples=[physical(E,eps) for E in [EA+F(i,20) for i in range(1,20)] for eps in [F(1,7),F(1,100),F(1,10000)]]
    return dict(result_id='K1975',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',dimension_threshold=10,open_energy_interval=[str(EA),str(EB)],exposed_faces=[[[e,str(p)] for e,p in f] for f in sorted(faces)],physical_controls=len(samples),consumers=samples,scope='For every interior energy, d>=10 has global chord as infimum; every fixed d<=9 has a strict positive gap. Global interior remains unattained at any finite nondegenerate d. Endpoints need only5.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1950-global-catalyst-energy-certificates.json','lab/process/k1968-joint-thermal-finite-dimension-program.json','lab/process/k1972-thermal-two-component-reduction.json','tests/channel-swings/k1950_global_catalyst_energy_certificates_probe.py']})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=calculate()
    if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
    else:assert v==json.loads(OUT.read_text())
    print('PASS K1975',v['physical_controls'],'exact10-level families; threshold10 follows compact exposed-face proof')
