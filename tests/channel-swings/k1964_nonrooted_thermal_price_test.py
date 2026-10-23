"""All-spectrum small-price certificate, exact constants and physical witnesses."""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json
from k1960_thermal_frontier_convexification import family,Q
from k1939_physical_catalyst_resource_frontier import shell_witness
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1964-nonrooted-thermal-price-test.json'
C=F(1,419904);W=F(25,8);c=F(163,440);DISP=36

def calculate():
    eps0=c/(4*W);B0=W/c+F(1,2);checks=0
    assert eps0<F(1,2) and B0*eps0<1,'small deficit regime'
    assert 2*W*B0<64,'logarithmic constant'
    assert F(DISP)/(2*W)+2<8,'exponential constant'
    assert C==1/(F(64)*3**8) and C<eps0/(2*W),'large-deficit continuation'
    checks+=4
    rows=[]
    for n in range(41):
        S,p,E,R,Z=family(n,n);delta=R-F(4,25)
        assert E<=2*n+F(41,32),'physical mean bound'
        assert delta<=F(17,50)*Q**n,'physical return bound'
        assert delta>0 and R>F(4,25);checks+=3
        if n<5:rows.append(dict(n=n,energy=str(E),return_cost=str(R)))
    # The global E-envelope upper constant follows from q-floor arithmetic.
    assert F(17,50)/Q**2<1 and F(17,50)<Q,'Cplus=1 covers all E>=1';checks+=1
    physical=[];pc=0
    for n in [1,2,3]:
        S,p,E,R,Z=family(n,n);actual,k=shell_witness(F(1,2),S,p,list(range(S[-1]+4)))
        assert actual==R;pc+=k+1
        physical.append(dict(support=S,weights=list(map(str,p)),energy=str(E),return_cost=str(R)))
    return dict(result_id='K1964',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_controls=checks,physical_shell_controls=pc,constants=dict(Cminus=str(C),Cplus='1',floor='4/25',a='log(3/2)/2',eps0=str(eps0),B0=str(B0)),physical=physical,examples=rows,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1958-sharp-thermal-energy-rate.json','lab/process/k1960-thermal-frontier-convexification.json','lab/process/k1962-finite-tail-thermal-improvement.json']},scope='All finite spectra global priced logarithmic law and localization of price-near-optimal physical protocols; no sharp O(lambda) constant or rooted completeness.')
def scout():
    # Search only; floating objectives never certify global or finite optimality.
    import warnings
    from itertools import product
    import numpy as np
    from scipy.optimize import linprog
    from k1943_arbitrary_preparation_catalyst_energy import canonical_paths,cell,rate
    from k1962_finite_tail_thermal_improvement import optimize
    warnings.filterwarnings('ignore',message='Unrecognized options detected')
    prices=[F(1,10),F(1,25),F(1,50),F(1,100)]
    bests={str(l):optimize(l)[0] for l in prices};count=0
    for S in canonical_paths(13):
     for orient in product((-1,1),repeat=len(S)-1):
      A,b,c,eq=cell(F(1,2),S,F(100),orient);A=A[:-1];b=b[:-1]
      for lam in prices:
       obj=[lam*e for e in S]+[F(1,2)]*len(S)
       ans=linprog(np.array(obj,float),A_ub=np.array(A,float),b_ub=np.array(b,float),A_eq=[np.array(eq,float)],b_eq=[1.],bounds=(0,None),method='highs-ds',options={'threads':1})
       count+=1
       assert ans.success
       if ans.fun<float(bests[str(lam)][0])-1e-10:
        p=[F(float(x)).limit_denominator(10**9) for x in ans.x[:len(S)]];R=rate(F(1,2),S,p)[0];E=sum(e*x for e,x in zip(S,p));val=R+lam*E
        assert sum(p)==1 and abs(float(val)-ans.fun)<1e-8
        bests[str(lam)]=(val,S,p,E,R)
        print('NEW',lam,S,list(map(str,p)),E,R,val,flush=True)
    print('COMPLETE',count,{k:str(v) for k,v in bests.items()},flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');p.add_argument('--scout',action='store_true');a=p.parse_args()
    if a.scout:
        scout();raise SystemExit(0)
    r=calculate()
    if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert r==json.loads(OUT.read_text()),'report equality'
    print('PASS K1964',r['exact_controls'],'exact',r['physical_shell_controls'],'physical',flush=True)
