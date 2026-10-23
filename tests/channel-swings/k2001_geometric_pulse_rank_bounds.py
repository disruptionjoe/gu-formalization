"""Geometric-band universal rank barriers; exact elementary pulse spectrum."""
from fractions import Fraction as F
from pathlib import Path
import json,argparse,hashlib
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k2001-geometric-pulse-rank-bounds.json'
RHO=F(1,768); K=F(1,16); ALPHA0=F(1,3)
def certificate(r):
    n=r+2;a=[F(1,4)*RHO**i for i in range(n)];b=[K*v for v in a]
    structural=[[F(3,2)*b[j]/a[i] if j>=i else F(3,2)*a[i]/(ALPHA0*b[j]) for j in range(n)] for i in range(n)]
    S=F(144,767)
    assert all(sum(row)<=S for row in structural)
    assert all(sum(structural[i][j] for i in range(n))<=S for j in range(n))
    # sqrt(rho)<1/27; error terms are bounded by two geometric matrices.
    assert RHO<F(1,729)
    E=F(27,208)
    assert S+E<F(3,8) and F(1,2)-S>F(3,10)
    L=ALPHA0**2*K**2*a[-1]**3/64
    assert L==F(1,9437184)*RHO**(3*(n-1))
    strong=F(9,25)*ALPHA0*K*a[-1]**2
    assert strong==F(3,6400)*RHO**(2*(n-1))
    # Entrywise squared Cauchy factors for the normalized error e=sqrt(L)/2.
    for i in range(n):
        assert 0<2*a[i]<=1 and 0<2*b[i]<=F(1,2)
        if i:assert 2*a[i]<a[i-1]
        for j in range(n):
            rowerr2=L/(4*ALPHA0**2*b[j]**2*a[i])
            colerr2=L/(4*a[i]**2*ALPHA0*b[j])
            assert rowerr2==RHO**(2*(n-1-j)+(n-1-i))/256
            assert colerr2<=RHO**(2*(n-1-i)+(n-1-j))/256
    return dict(rank=r,n=n,residual_squared_lower_bound=str(L),strong_error_squared_lower_bound=str(strong),structural_row_column_bound=str(S),error_row_column_bound=str(E),approximate_compression_sigma_lower_bound='1/8',exact_compression_sigma_lower_bound='3/10',rational_entry_checks=2*n*n)
def produce():
    certs=[certificate(r) for r in [0,1,2,4,8,16,32,64]]
    consumers=[]
    for d in [10,50,100,250]:
        eps2=F(1,10**(2*d));r=-1
        while eps2<=F(1,9437184)*RHO**(3*(r+2)):r+=1
        consumers.append(dict(residual_norm_at_most='1e-'+str(d),required_rank_at_least=r+1))
    return dict(result_id='K2001',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',rho=str(RHO),residual_formula='J(q)>1/(9437184*768^(3*(r+1)))',strong_formula='||q_star-w||^2 >=3/(6400*768^(2*(r+1)))',certificates=certs,precision_consumers=consumers,elementary_pulse_spectrum=dict(gram_kernel='alpha*(1-|x-y|)+(1-alpha)*x*y with dx/2',even='alpha/((n+1/2)*pi)^2, n>=0',odd='alpha/k_n^2, k_n*cot(k_n)=1-alpha; n*pi<k_n<n*pi+pi/2',ordered='odd0,even0,odd1,even1,...',best_rank_squared_error_asymptotic='4*alpha/(pi^2*r)',scope='Unrestricted best rank-r L2 approximation to K1991 elementary q0 only; not every exact pulse and not cap/marginal-preserving spectral truncation'),scope='Actual central rectangle and cap, approximate BOTH marginals. Universal logarithmic necessary rank is nonsharp. No wings, global minimum norm, source or ledger verdict.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['explorations/conditional-build/k1999-effective-rank-residual-bound-2026-10-23.md','explorations/conditional-build/k1997-finite-rank-pulse-obstruction-2026-10-23.md']})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();d=produce()
    if args.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
    else:assert d==json.loads(OUT.read_text())
    print('PASS K2001:',sum(c['rational_entry_checks'] for c in d['certificates']),'exact band/error checks;',d['precision_consumers'])
