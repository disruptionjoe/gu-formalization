"""Direct sliding-window capacities and separately integrated phase polynomials."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
import k1969_scalar_continuum_separation as base
ROOT=Path(__file__).resolve().parents[2]
def integrate(poly,a,b):return sum(c*(b**(i+1)-a**(i+1))/(i+1) for i,c in enumerate(poly))
def phase_integral(a,b,t,lam):
    # Integral on negative half, change variable u=-x.
    pieces=[(F(0),t,[0,1-lam*(1-t)**2/2]),(t,F(1),[lam*t*t/2,1-lam*(1+t*t)/2,lam/2]),(F(1),F(2),[F(1)]),(F(2),F(3),[3+3*lam,-1-F(5,2)*lam,lam/2])]
    ans=F(0)
    for l,h,p in pieces:
        L=max(l,-b);H=min(h,-a)
        if L<H:ans+=integrate(p,L,H)
    return ans

def check(fault=None):
    n=8;h=F(3,n);t=F(9,20);lam=F(3,50);M=F(23,100);count=0
    if fault=='steep_multiplier':lam=F(2)
    assert 1-lam/2>M,'outer ramp must dominate capacity gradient'
    assert -1+lam/2<0,'central ramp remains decreasing'
    val=[phase_integral(-3+i*h,-3+(i+1)*h,t,lam) for i in range(n)]
    if fault=='disconnected_ripple':val[0]+=10;val[5]+=10
    records=[]
    for mask in range(1<<n):
        bits=[(mask>>i)&1 for i in range(n)];intervals=[(-3+i*h,-3+(i+1)*h) for i,b in enumerate(bits) if b];s=h*sum(bits)
        direct=base.capacity(intervals);w=F(0);area=F(0)
        for b in bits:
            z=w+h*(2*b-1)
            if w>=0 and z>=0:area+=h*(w+z)/2
            elif w*z<0:area+=max(w,z)**2/2 # unit slope
            w=z
        tail=max(F(0),2*s-3)**2/2
        if fault=='omit_tail':tail=0
        width=8 if fault=='wrong_width' else 9
        assert direct==width*s-area-tail,'full sliding windows equal reduced excursion capacity';count+=1
        records.append((bits,sum(v*b for v,b in zip(val,bits))-M*direct/2))
    for bits,d in records:
        size=sum(bits);best=max(dd for bb,dd in records if sum(bb)==size and (not size or max(i for i,b in enumerate(bb) if b)-min(i for i,b in enumerate(bb) if b)+1==size))
        assert d<=best,'interval replacement controls arbitrary disconnected subset';count+=1
    # Independent finite arithmetic behind the universal set transformation.
    for length in range(1,9):
        def f(z):return min(z,length-z)
        for common in range(length+1):
            for a in range(length-common+1):
                for b in range(length-common-a+1):
                    assert f(common+a)+f(common+b)>=f(common)+f(common+a+b),'concave window capacity submodularity';count+=1
    for x in [F(i,8) for i in range(1,25)]:
        for L in [F(i,8) for i in range(int(8*x)+1)]:
            for R in [F(i,8) for i in range(int(8*(x-L))+1)]:
                for mass in [L+R,min(F(3),L+R+3-x)]:
                    bottom=2*mass-6
                    f=lambda w:max(F(0),w,bottom-w)
                    assert f(2*(L+R)-x)+f(-x)>=f(2*L-x)+f(2*R-x),'convex two-prefix polarization';count+=1
    for mask in range(256):
        A=[(mask>>i)&1 for i in range(8)];B=[a*(1-A[-1-i]) for i,a in enumerate(A)]
        if fault=='retain_paired_points':B=A
        assert all(B[i]+B[-1-i]<=1 for i in range(8)),'paired removal produces disjoint reflection'
        C=[max(B[i],B[-1-i]) if i<4 else 0 for i in range(8)]
        if fault=='fold_wrong_side':C=C[::-1]
        cap=lambda bs:base.capacity([(F(-3)+F(3,4)*i,F(-3)+F(3,4)*(i+1)) for i,b in enumerate(bs) if b])
        left=[F(1),F(2),F(3),F(4)];values=left+[-v for v in left[::-1]]
        demand=lambda bs:sum(v*b for v,b in zip(values,bs))
        assert demand(A)==demand(B)<=demand(C),'odd positive-side demand survives and improves'
        assert cap(C)<=cap(B)<=cap(A),'full cut reduction capacity'
        count+=3
    r=json.loads((ROOT/'lab/process/k1974-scalar-excursion-separation.json').read_text())
    for p,hsh in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==hsh
    return count
if __name__=='__main__':
    n=check();caught=[]
    for f in ['steep_multiplier','omit_tail','wrong_width','disconnected_ripple','retain_paired_points','fold_wrong_side']:
        try:check(f)
        except AssertionError as e:caught.append([f,str(e)])
        else:raise AssertionError('missed mathematical fault '+f)
    print('PASS K1974 independent',n,'exact controls; faults',caught)
