"""Exact marginal-preserving central pulse cycle with rigorous norm intervals."""
from fractions import Fraction as F
from pathlib import Path
import json,argparse,hashlib
from k1969_scalar_continuum_separation import isolate,ia,im,iv
from k1991_tight_cut_pulse_factorization import norm_interval,f,pulse,neg,point,M
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1995-central-marginal-cycle-improvement.json'
A=F(1,4);B=F(1,2);H=F(1,2);WIDTH=F(1,4)
def epsilon(x,t):return 1-f(x+H,t)
def modified(x,y,t,kappa=F(1)):
    if x<0:return -modified(-x,None if y is None else -y,t,kappa)
    q=pulse(x,y,t)
    if y is None:return q
    if A<x<B:
        e=kappa*epsilon(x,t)
        if 0<y<WIDTH:q+=e
        if B<y<B+WIDTH:q-=e
    if A+H<x<B+H:
        e=kappa*epsilon(x-H,t)
        if 0<y<WIDTH:q-=e
        if B<y<B+WIDTH:q+=e
    return q

def fI(x,t):return iv(im(ia(point(3),im(point(4),t)),x),ia(point(3),im(im(point(4),t),x)))
def gain_interval(t,N=2048):
    # Direct interval integration of the rational positive gain. Interval widths
    # converge to zero; no derivative or numerical-quadrature error is omitted.
    total=point(0);dx=(B-A)/N
    for i in range(N):
        x=(A+i*dx,A+(i+1)*dx);e=ia(point(1),neg(fI(ia(x,point(H)),t)));one=ia(point(1),fI(x,t))
        v=ia(im(point(2),im(e,one)),neg(im(point(4),im(e,e))))
        term=im(point(dx),v);D=10**30
        term=(F((term[0]*D).__floor__(),D),F((term[1]*D).__ceil__(),D))
        total=ia(total,term)
    return im(im(point(4*M*M*WIDTH),im(t,t)),total)

def produce():
    t=isolate();gain=gain_interval(t);_,central,upper=norm_interval(t);newupper=upper[1]-gain[0]
    lower=F(json.loads((ROOT/'lab/process/k1989-capped-pulse-dual-certificates.json').read_text())['certificate']['squared_norm_lower_bound'])
    controls=0
    for tt in [F(9,20),F(23,50)]:
        for i in range(1,101):
            x=A+(B-A)*F(i,101);e=epsilon(x,tt);f1=f(x,tt);f2=f(x+H,tt)
            q=[-f1,1,-f2,-f2];dq=[e,-e,-e,e]
            assert 0<e< F(1,5) and e<(1+f1)/4
            assert sum(dq[:2])==sum(dq[2:])==dq[0]+dq[2]==dq[1]+dq[3]==0
            assert all(abs(a+b)<=1 for a,b in zip(q,dq))
            reduction=sum(a*a-(a+b)**2 for a,b in zip(q,dq))
            assert reduction==2*e*(1+f1)-4*e*e>0
            for y in [F(1,8),F(5,8),F(-1,8),F(7,8),None]:
                for xx in [x,x+H]:assert abs(modified(xx,y,tt))<=1;controls+=1
            controls+=4
    assert gain[0]>0 and newupper<upper[1] and lower<newupper
    return dict(result_id='K1995',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',root_interval=list(map(str,t)),gain_interval=list(map(str,gain)),central_norm_squared_interval=[str(central[0]-gain[1]),str(central[1]-gain[0])],whole_pulse_norm_squared_upper_bound=str(newupper),inherited_squared_norm_lower_bound=str(lower),strong_distance_squared_upper_bound=str(newupper-lower),prior_central_nonoptimality_gap_lower_bound=str(gain[0]),interval_cells=2048,exact_rational_controls=controls,scope='Explicit cap-respecting four-rectangle circulation and reflected partner preserve exact central row/column marginals; pointwise optimal amplitude inside this fixed cycle family strictly improves K1991 and proves it is not regional minimum-norm. Whole-pulse bound retains inherited wing existence; no explicit wings, global/regional optimality, phase-energy improvement, smoothness or GU claim.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['tests/channel-swings/k1991_tight_cut_pulse_factorization.py','lab/process/k1989-capped-pulse-dual-certificates.json','tests/channel-swings/k1969_scalar_continuum_separation.py']})
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();d=produce()
    if a.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
    else:assert d==json.loads(OUT.read_text())
    print('PASS K1995',d['exact_rational_controls'],'rational controls; gain',*[float(F(x)) for x in d['gain_interval']],'upper',float(F(d['whole_pulse_norm_squared_upper_bound'])),'distance',float(F(d['strong_distance_squared_upper_bound']))**.5)
