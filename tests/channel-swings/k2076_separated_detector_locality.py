"""Exact sufficient detector-separation resources; continuum proof in K2076."""
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt,factorial
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2]
def upper(a,terms=80):
    assert isinstance(a,int) and a>=1
    lo=isqrt(a);hi=lo+(lo*lo<a)
    # pi>3 implies 1/sqrt(2*pi)<1/2. Positive Taylor sum < exp(a).
    total=sum((Q(a)**k/factorial(k) for k in range(terms+1)),Q(0))
    return min(Q(1,2),(2*hi+Q(27,8*lo))/(2*total))
def produce():
    refs=['lab/process/k2073-confined-pointer-energy.json','explorations/conditional-build/k2071-confined-pointer-control-2026-10-25.md','explorations/conditional-build/k2062-bounded-local-multiplier-rigidity-2026-10-25.md','explorations/conditional-build/k2065-position-measurement-compatibility-2026-10-25.md']
    rows=[]
    for a in [1,4,8,12,20,32]:
        u=upper(a);rows.append(dict(mass_times_separation=a,cross_norm_upper=str(u),commutator_upper=str(2*u),luders_disturbance_upper=str(3*u),unitary_operator_order_upper=str(2*u),unitary_probability_order_upper=str(min(Q(1),4*u))))
    assert 3*upper(20)<Q(1,20000000)
    assert 3*upper(32)<Q(1,10**12)
    return dict(id='K2076',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs},kernel='(m beta h-i alpha.grad h)/2; h=m*K1(m*r)/(2*pi^2*r)',schur_tail='((a+2)*K0(a)+a*K1(a)+integral_a^infinity K0(z) dz)/pi',elementary_bound='min(1/2,exp(-a)/sqrt(2*pi)*(2*sqrt(a)+27/(8*sqrt(a))))',valid_for='a=m*d>0; resource rows a integer>=1',resources=rows,free_unequal_time_resources=[dict(mass='1',spatial_gap='30',time_gap='10',effective_mass_gap='20',luders_upper=str(3*upper(20))),dict(mass='2',spatial_gap='20',time_gap='4',effective_mass_gap='32',luders_upper=str(3*upper(32)))],physical_dimension=1408,dimension_factor_in_bound=1,operational_scope='separated positive-energy effects and freely evolved Heisenberg effects at d>|t-s|; specified unitary or binary Lueders instruments only; no exact microcausality or GU field completion')
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();d=produce();p=ROOT/'lab/process/k2076-separated-detector-locality.json'
    if args.write:p.write_text(json.dumps(d,indent=2)+'\n')
    else:assert json.loads(p.read_text())==d
    print('PASS six exact rational separation resources and two strict tolerance inequalities')
