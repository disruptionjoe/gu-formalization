"""Effective continuum finite-rank obstruction by nested corner compressions."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1999-effective-rank-residual-bound.json'
def certificate(r):
    n=r+2;alpha=F(1,3);k=F(1,16*n);rho=alpha*k*k
    a=[F(1,4)*rho**i for i in range(n)];b=[k*x for x in a]
    lower=alpha**2*k**2*a[-1]**3/(64*n*n)
    assert lower==1/(F(9437184)*n**4*(768*n*n)**(3*(n-1)))
    controls=0
    for i in range(n):
        assert 0<a[i]<2*a[i]<=1 and 0<b[i]<2*b[i]<=F(1,2)
        if i:assert 2*a[i]<a[i-1] and 2*b[i]<b[i-1]
        for j in range(n):
            base=F(3,2)*b[j]/a[i] if j>=i else F(3,2)*a[i]/(alpha*b[j])
            assert base<=F(3,32*n);controls+=1
            # Squared Cauchy error constants avoid any irrational arithmetic.
            row_error2=lower/(4*alpha**2*b[j]**2*a[i])
            column_error2=lower/(4*a[i]**2*alpha*b[j])
            assert row_error2<=F(1,256*n*n) and column_error2<=F(1,256*n*n)
            controls+=2
    entry_bound=F(5,32*n)
    assert 2*n*entry_bound==F(5,16)<1
    return dict(rank=r,compression_size=n,ratio=str(rho),smallest_row_band=str(a[-1]),smallest_column_band=str(b[-1]),squared_residual_lower_bound=str(lower),entry_error_bound=str(entry_bound),singular_value_lower_bound='11/32',unrestricted_rank_approximation_error_squared=str(F(169,256)*alpha*k*a[-1]**2),exact_inequality_controls=controls)
def produce():
    certs=[certificate(r) for r in [0,1,2,4,8,16,32]]
    # Strong approximation and existing growing-rank comparison.
    consumers=[]
    for r in [1,2,4,8,16,32]:
        c=certificate(r);low=F(c['squared_residual_lower_bound'])
        upper=F(2,3*r*r)
        assert low<upper
        consumers.append(dict(rank=r,squared_distance_lower_bound=str(low/2),existing_even_rank_residual_upper_bound=str(upper) if r%2==0 else None))
    precision=[]
    for digits in [10,50,100,250]:
        excluded=-1
        for r in range(100):
            if F(1,10**(2*digits))<=F(certificate(r)['squared_residual_lower_bound']):excluded=r
            else:break
        precision.append(dict(residual_at_most='1e-'+str(digits),required_rank_at_least=excluded+1))
    return dict(precision_consumers=precision,result_id='K1999',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',alpha_lower_bound='1/3',formula='J(q)>1/[9437184*(r+2)^4*(768*(r+2)^2)^(3*(r+1))] for capped rank(q)<=r',certificates=certs,consumers=consumers,scope='Actual central marginals and amplitude cap; explicit nonsharp rank-only bound. Continuum proof uses Cauchy-Schwarz and a full-rank averaged triangular matrix, not finite sampling. No exact full pulse, sharp rate, minimum-norm formula or GU physics.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['explorations/conditional-build/k1997-finite-rank-pulse-obstruction-2026-10-23.md','explorations/conditional-build/k1991-tight-cut-pulse-factorization-2026-10-23.md']})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=produce()
    if a.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
    else:assert d==json.loads(OUT.read_text())
    print('PASS K1999',sum(c['exact_inequality_controls'] for c in d['certificates']),'rational interval/error inequalities')
