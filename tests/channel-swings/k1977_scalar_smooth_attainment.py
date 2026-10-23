"""Exact regularity obstruction and curvature/energy tradeoff."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,argparse
from k1969_scalar_continuum_separation import isolate,ip,iv,K,D,P,poly
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1977-scalar-smooth-attainment.json'
def calculate():
    interval=isolate();lam=iv(ip(D,interval),ip(K,interval));assert F(3,50)<lam[0]<lam[1]<F(7,100)
    rows=[]
    # Monotone conservative lower bound: numerator lower, denominator upper.
    a=1+lam[0]/2
    for L in map(F,[2,3,4,8,16,32,64,128,256,1024]):
        h=a/(L+lam[1]);gap=2*a**3/(3*(L+lam[1]))
        integral=2*(a*a*h-a*(L+lam[1])*h*h+(L+lam[1])**2*h**3/3)
        assert 0<h<1 and integral==gap>0
        rows.append(dict(phase_curvature=str(L),radius=str(h),energy_gap_lower=str(gap)))
    return dict(result_id='K1977',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',root_interval=list(map(str,interval)),lambda_interval=list(map(str,lam)),outer_derivative_jump_lower=str(a),controls=rows,scope='No C1 pulse attains the exact measurable optimum. For feasible phases with derivative Lipschitz constant L, L>=2 and energy gap >=2(1+lambda/2)^3/[3(L+lambda)]. No equality of smooth infimum asserted.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['explorations/conditional-build/k1969-scalar-continuum-separation-2026-10-22.md','explorations/conditional-build/k1974-scalar-excursion-separation-2026-10-23.md']})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=calculate()
    if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert r==json.loads(OUT.read_text())
    print('PASS K1977',len(r['controls']),'exact curvature certificates')
