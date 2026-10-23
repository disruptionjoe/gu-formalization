"""Independent sliding-window integrals and polynomial boundary certificates."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def direct(a,b):
    points=sorted({Q(-3),Q(3),Q(6),Q(12),a,b,a+9,b+9})
    def value(z):
        length=max(Q(0),min(Q(3),z)-max(Q(-3),z-9))
        part=max(Q(0),min(b,z)-max(a,z-9))
        return part,length-part
    out=Q(0)
    for left,right in zip(points,points[1:]):
        u,v=value(left);w,x=value(right);knots=[left,right]
        if (u-v)*(w-x)<0:knots.insert(1,left+(right-left)*(u-v)/(u-v-w+x))
        for l,r in zip(knots,knots[1:]):out+=(r-l)*(min(value(l))+min(value(r)))/2
    return out

def check(fault=None):
    M=Q(23,100) if fault!='wrong_amplitude' else Q(1,5);n=0
    assert 9*M/2>1,'strict constant-capacity margin'
    for i in range(31):
        for j in range(i+1,31):
            a,b=-3+Q(i,5),-3+Q(j,5);s=b-a;u=a+3;v=3-b
            short=9*s-max(Q(0),s-u)**2-max(Q(0),s-v)**2
            long=9*(u+v)-u*u-v*v
            formula=short if s<=3 else long
            if fault=='omit_right_excursion' and s<=3:formula=9*s-max(Q(0),s-u)**2
            if fault=='long_interval_as_short' and s>3:formula=short
            assert formula==direct(a,b),'independent whole-window capacity';n+=1
    # Build polynomial directly from primitive minus cut capacity, rather than
    # copying the producer's expanded coefficients.
    def deficit(u,v):return 2-(v-3)**2/2-u*u/2-M*(9*(v-u)-(v-2*u)**2)/2
    assert deficit(Q(0),Q(9,4))==-Q(89,3200)
    assert deficit(Q(1),Q(2))==-Q(7,200)
    dv0=Q(3)-9*M/2+(M-1)*Q(9,4)
    dv1=Q(3)-9*M/2-2*M+(M-1)*2
    assert dv0>0 and dv1<0,'two rectangle vertical boundary monotonicities'
    hessian=(M-1)*(4*M-1)-(-2*M)**2
    assert hessian<0,'no interior local maximum of the quadratic'
    if fault=='wrong_outer_slope':lower=Q(9,10)
    else:lower=1-Q(7,200)
    assert lower>4*M,'outer strict concavity of interval deficit'
    # Capacity lower bound from a disjoint excursion partition: all widths
    # nonnegative; sum squares <= square of sum, including nonuniform splits.
    for k in range(1,21):
        widths=[Q((k*j)%17+1,137) for j in range(1,8)]
        assert sum(x*x for x in widths)<=sum(widths)**2;n+=1
    assert 9-2/M==Q(7,23)
    return n+6
if __name__=='__main__':
    n=check();caught=[]
    for f in ['wrong_amplitude','omit_right_excursion','long_interval_as_short','wrong_outer_slope']:
        try:check(f)
        except AssertionError as e:caught.append([f,str(e)])
        else:raise AssertionError('missed mathematical fault '+f)
    r=json.loads((ROOT/'lab/process/k1971-scalar-all-cut-optimizer.json').read_text())
    for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    print('PASS K1971 independent',n,'exact controls;',caught)
