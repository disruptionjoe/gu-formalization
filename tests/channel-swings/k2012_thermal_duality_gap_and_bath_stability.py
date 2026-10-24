"""Exact endpoint, physical separation and faithful-bath stability consumers."""
from fractions import Fraction as F
from pathlib import Path
from itertools import combinations
import json,argparse,hashlib
from k2010_countable_thermal_attainment import rate,shells
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2012-thermal-duality-gap-and-bath-stability.json'
EA,EB,RA,RB,LAM,A=F(6,5),F(11,5),F(9,20),F(3,10),F(3,20),F(63,100)

def bath(t):return [t**i/sum(t**j for j in range(4)) for i in range(4)]
def tv(a,b):return sum(abs(x-y) for x,y in zip(a,b))/2

def pair_return(p,b):
    x,y=p
    incoming_x=sum(max(y*b[k]-x*b[k+2],0) for k in range(2))
    incoming_y=sum(max(x*b[k+2]-y*b[k],0) for k in range(2))
    return (max(x-incoming_x,0)+max(y-incoming_y,0))/2

def produce():
    assert shells(list(map(F,range(5))),[F(1),F(3)])
    for p,e,r in [([F(9,10),F(1,10)],EA,RA),([F(2,5),F(3,5)],EB,RB)]:
        assert sum(x*y for x,y in zip([F(1),F(3)],p))==e
        assert rate([F(1),F(3)],p,F(1,2))==pair_return(p,bath(F(1,2)))==r
        assert r+LAM*e==A
    chords=[]
    for k in range(1,20):
        w=F(k,20);E=(1-w)*EA+w*EB;line=A-LAM*E
        assert (1-w)*RA+w*RB==line
        for lam in [F(0),F(1,20),LAM,F(1,5),F(1)]:
            bound=min(RA+lam*EA,RB+lam*EB)-lam*E
            assert bound<=line
            if lam!=LAM:assert bound<line
        chords.append(dict(E=str(E),line=str(line)))
    physical=[]
    for delta in [F(1,100),F(1,10),F(1,2)]:
        levels=sorted([F(i) for i in range(5)]+[F(i)+delta for i in range(5)])
        assert min(y-x for x,y in zip(levels,levels[1:]))==delta
        for k in range(1,10):
            w=F(k,10);E=(1-w)*EA+w*EB
            support=[F(1),F(3),1+delta,3+delta];p=[(1-w)*F(9,10),(1-w)*F(1,10),w*F(2,5),w*F(3,5)]
            assert shells(levels,support)
            cost=sum(x*y for x,y in zip(support,p));ret=rate(support,p,F(1,2))
            assert cost==E+w*delta and ret==A-LAM*E
            assert ret+LAM*cost-A==LAM*w*delta>0
            physical.append(dict(delta=str(delta),w=str(w),energy=str(cost),return_value=str(ret),penalty=str(LAM*w*delta)))
    baths=[bath(t) for t in [F(1,10),F(1,3),F(1,2),F(2,3),F(9,10)]]
    baths += [[F(a,8),F(b,8),F(c,8),F(8-a-b-c,8)] for a in range(1,5) for b in range(1,6-a) for c in range(1,7-a-b)]
    checks=0
    for x,y in combinations(baths,2):
        for p in [[F(9,10),F(1,10)],[F(2,5),F(3,5)],[F(1,2)]*2]:
            assert abs(pair_return(p,x)-pair_return(p,y))<=tv(x,y);checks+=1
    # Rational neighborhood of the Gibbs reference; radius belongs to a supplied gap, not a claimed numerical global gap.
    continuity=[]
    for t in [F(49,100),F(1,2),F(51,100)]:
        d=tv(bath(t),bath(F(1,2)));assert d<=12*abs(t-F(1,2))
        continuity.append(dict(t=str(t),bath_TV=str(d),gap_loss_upper=str(2*d)))
    tails=[];coefficients=[]
    for high in [F(10),F(20),F(50)]:
      for q in [F(1,10000),F(1,1000),F(1,100)]:
        p=[(1-q)*F(9,10),(1-q)*F(1,10),q];sites=[F(1),F(3),high]
        E=sum(x*y for x,y in zip(sites,p));assert EA<E<EB
        R=rate(sites,p,F(1,2));gap=R-(A-LAM*E)
        assert q<=100*gap/7 and q<=(E-1)/7
        low=RA;assert low-R<=q/(1-q)
        assert (low-(A-LAM*E))<=gap*(1+100/(8-E))
        tails.append(dict(high=str(high),tail=str(q),energy=str(E),return_value=str(R),gap=str(gap),normalized_low=str(low)))
    for k in range(1,20):
      E=EA+F(k,20);ell=LAM*min(E-EA,EB-E);factor=(8-E)/(108-E)
      assert 0<factor*ell<=ell
      coefficients.append(dict(E=str(E),factor=str(factor),liminf_lower=str(factor*ell),limsup_upper=str(ell)))
    inputs=['explorations/conditional-build/k2010-countable-thermal-attainment-2026-10-24.md','explorations/conditional-build/k1950-global-catalyst-energy-certificates-2026-10-22.md','explorations/conditional-build/k2008-effective-thermal-dimension-approximation-2026-10-24.md','tests/channel-swings/k2010_countable_thermal_attainment.py','explorations/conditional-build/k1998-uniform-small-spacing-transfer-2026-10-23.md']
    return dict(result_id='K2012',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',endpoints={'A':[str(EA),str(RA)],'B':[str(EB),str(RB)],'price':str(LAM),'value':str(A)},chords=chords,physical_separation=physical,temperature_controls=continuity,tail_transfers=tails,linear_order_coefficients=coefficients,counts={'endpoint_protocols':2,'budget_chords':len(chords),'physical_separation_protocols':len(physical),'bath_stability_groups':checks,'tail_transfers':len(tails),'coefficient_controls':len(coefficients)},scope='Exact all-dimension Lagrange dual on the exposed interval with strict positive primal gap by K2010; dimension-uniform faithful-bath stability by trace contractivity. 23-level multiplicative gap reduction and unrestricted Theta(delta) rate by written proof. No hard-budget finite attainment, sharp coefficient or numerical unrestricted gap claimed. Bath endpoints with missing support are excluded.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();r=produce()
    if args.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert r==json.loads(OUT.read_text())
    print('PASS K2012',r['counts'])
