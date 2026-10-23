"""Exact support-count optimizer and finite physical attainments at bath t=1/2."""
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json
from k1956_finite_energy_thermal_gap import rates
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1966-sharp-thermal-support-size.json'
q,p,W=F(2,3),F(1,9),F(25,8)
def weight(n,m): return W-2*q**n-p**m/8
def optimal(N):
    z,n=max((weight(n,N-1-n),n) for n in range(N))
    return n,N-1-n,z

def bellman(limit):
    # Exact finite arm maxima indexed by FIRST gap, not an infinite bound.
    L=[{d:F(0) for d in (1,2,3)}];R=[L[0].copy()]
    for k in range(1,limit+1):
        L.append({d: rates(d)[0]/(1+rates(d)[1])*(1+max([F(0)] if k==1 else [L[k-1][e] for e in (1,2,3) if d+e>=4])) for d in (1,2,3)})
        R.append({d: rates(d)[1]/(1+rates(d)[0])*(1+max([F(0)] if k==1 else [R[k-1][e] for e in (1,2,3) if d+e>=4])) for d in (1,2,3)})
    return L,R

def calculate(physical=False):
    L,R=bellman(40);checks=0;rows=[]
    assert F(1,2)*(1+2)==F(3,2)
    assert F(7,29)*(1+F(3,55))==F(14,55)
    assert F(1,23)*(1+F(14,55))==F(3,55)<p
    assert weight(5,1)>1+F(3,2)+F(14,55)
    checks+=4
    for N in range(1,41):
        candidates=[F(1)]
        for n in range(N):
            m=N-1-n
            if n==0 and m: candidates+=list(1+x for x in R[m].values())
            elif m==0 and n:candidates+=list(1+x for x in L[n].values())
            elif n and m:candidates += [1+L[n][a]+R[m][b] for a in (1,2,3) for b in (1,2,3) if a+b>=4]
        actual=max(candidates);n,m,z=optimal(N)
        assert actual==z,'all admissible gap words and rooted positions'
        energy=1+2*n+2*(sum(k*p**k for k in range(1,m+1))-sum(k*q**k for k in range(1,n+1)))/z
        rows.append(dict(N=N,n=n,m=m,reward=str(z),bellman_reward=str(actual),return_cost=str(1/(2*z)),excess=str(1/(2*z)-F(4,25)),canonical_mean_energy=str(energy)))
        checks+=1
    # Integer minimizer certificate: strictly increasing forward differences.
    for N in range(7,81):
        n,m,z=optimal(N)
        D=[2*q**k+p**(N-1-k)/8 for k in range(N)]
        slopes=[b-a for a,b in zip(D,D[1:])]
        assert all(a<b for a,b in zip(slopes,slopes[1:])), 'strict discrete convexity'
        assert (n==0 or slopes[n-1]<0) and (n==N-1 or slopes[n]>0)
        assert all(v!=0 for v in slopes), 'prime-factor no-tie identity'
        assert all(z>=weight(k,N-1-k) for k in range(N))
        checks+=4
    physical_checks=0;witness=[]
    if physical:
        from k1943_arbitrary_preparation_catalyst_energy import shell_witness
        for N in (1,2,6,7,9,12):
            n,m,z=optimal(N);support=list(range(1,2*N,2));raw=[q**(n-i) if i<=n else p**(i-n) for i in range(N)];probs=[v/z for v in raw]
            assert sum(probs)==1
            result,nc=shell_witness(F(1,2),support,probs,list(range(2*N+1)))
            assert result==1/(2*z)
            physical_checks+=nc+2;witness.append(dict(N=N,n=n,m=m,physical_dimension=2*N+1,return_cost=str(result)))
    return dict(result_id='K1966',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_controls=checks,physical_controls=physical_checks,rows=rows,physical_witnesses=witness,inputs={x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in ['lab/process/k1935-arbitrary-support-thermal-return.json','lab/process/k1943-arbitrary-preparation-catalyst-energy.json']},scope='Exact occupied support N>=1 and physical dimension d>=3 at fixed t=1/2; not mean-energy optimum or density-matrix rank.')
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');ap.add_argument('--physical',action='store_true');a=ap.parse_args();r=calculate(a.physical)
    if a.write:
        assert a.physical;OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:
        old=json.loads(OUT.read_text())
        for k in ['rows','inputs','exact_controls']:assert r[k]==old[k]
    print('PASS K1966',r['exact_controls'],'exact;',r['physical_controls'],'physical')
