"""Complete wide-spacing shell discriminator and exact threshold witnesses."""
from fractions import Fraction as F
from pathlib import Path
from itertools import combinations
import argparse,hashlib,json
from k1950_global_catalyst_energy_certificates_probe import shell_return
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1981-wide-spacing-thermal-frontier.json'

def shell_rank(spectrum,support):
    return all(sum(z-e in range(4) for e in spectrum)>=2*sum(z-e in range(4) for e in support) for z in {e+b for e in support for b in range(4)})
def produce():
    # Local forced partners obstruct every nonzero resonant occupied separation.
    obstructions=[]
    for q in [1,2,3]:
        levels=sorted({F(-2),F(0),F(2),F(q-2),F(q),F(q+2)})
        gap=min(b-a for a,b in zip(levels,levels[1:]));badgap=gap<=1
        shellbad=not shell_rank(levels,[F(0),F(q)])
        assert badgap or shellbad
        obstructions.append(dict(occupied_gap=q,forced_levels=list(map(str,levels)),minimum_gap=str(gap),spacing_obstructed=badgap,shell_rank_obstructed=shellbad))
    controls=[]
    for t in [F(1,10),F(1,4),F(1,2),F(3,4),F(9,10)]:
        assert shell_return(t,[F(2)],[F(1)])==F(1,2)
        for n in range(1,6):
            support=[F(2+4*i) for i in range(n)];spec=sorted({e+d for e in support for d in [-2,0,2]})
            weights=[F(i+1,n*(n+1)//2) for i in range(n)]
            assert min(b-a for a,b in zip(spec,spec[1:]))==2 and shell_rank(spec,support)
            r=shell_return(t,support,weights);assert r==F(1,2)
            controls.append(dict(t=str(t),support=list(map(str,support)),weights=list(map(str,weights)),return_error=str(r)))
    edge=[]
    for t in [F(1,10),F(1,4),F(1,2),F(3,4),F(9,10)]:
        s=[F(1),F(3)];p=[F(1,2),F(1,2)];assert shell_rank(list(map(F,range(5))),s)
        r=shell_return(t,s,p);assert r==(1+3*t*t)/(4*(1+t*t))<F(1,2)
        edge.append(dict(t=str(t),mean_energy='2',spacing='1',dimension=5,return_error=str(r),right_jump_lower_bound=str(F(1,2)-r)))
    return dict(result_id='K1981',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',obstructions=obstructions,physical_controls=controls,boundary_witnesses=edge,scope='For0<t<1,1<delta<=2,d>=3,E>=2, the exact simulation optimum is1/2; infeasible for E<2 or d<3 or delta>2. At delta1 an explicit d5 energy2 family proves a strict right discontinuity. No small-spacing full frontier.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['explorations/conditional-build/k1978-thermal-spectral-spacing-2026-10-23.md','tests/channel-swings/k1950_global_catalyst_energy_certificates_probe.py','lab/process/k1975-thermal-sharp-dimension-threshold.json']})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=produce()
    if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert r==json.loads(OUT.read_text())
    print('PASS K1981',len(r['physical_controls']),'physical families;',len(r['boundary_witnesses']),'strict threshold controls')
