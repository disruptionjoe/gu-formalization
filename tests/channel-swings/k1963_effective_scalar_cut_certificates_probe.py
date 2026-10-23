"""Independent ODE reconstruction and finite transfer counter-controls."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
x=s.symbols('x',real=True)

def audit(fault=None):
    cuts=[s.Rational(-1,2),s.Rational(1,2)];lam=s.Rational(2,35)
    if fault=='multiplier':lam*=2
    free=[(-3,-2),(-1,1),(2,3)];segs=[];means=[]
    def raw(a,b,t,left,right):
        z=x-a;L=s.Rational(b-a);v=max(s.S(0),min(L,t-a))
        return s.expand((v-v*v/(2*L))*z-z*z/2) if right<=t else s.expand(v*v/(2*L)*(L-z))
    for t in cuts:
        mean=0
        for a,b in free:
            ks=sorted({s.Rational(a),s.Rational(b)}|{t} if a<t<b else {s.Rational(a),s.Rational(b)})
            for l,r in zip(ks,ks[1:]):mean+=s.integrate(raw(a,b,t,l,r),(x,l,r))
        means.append(mean)
    energy=0;tot=0;ints=[0,0];checks=0
    allsegs=[(-3,-2,x+3),(-2,-1,s.S(1)),(-1,1,-x),(1,2,s.S(-1)),(2,3,x-3)]
    for a,b,base in allsegs:
        ks=sorted({s.Rational(a),s.Rational(b)}|{t for t in cuts if a<t<b})
        for l,r in zip(ks,ks[1:]):
            phi=base
            if (a,b) in free:
                h=(x-a)*(b-x)/2
                for t,m in zip(cuts,means):phi-=lam*(raw(a,b,t,l,r)-m*h/s.Rational(5,6))
            phi=s.expand(phi)
            tot+=s.integrate(phi,(x,l,r));energy+=s.integrate(s.diff(phi,x)**2,(x,l,r))
            for i,t in enumerate(cuts):
                if l<t:ints[i]+=s.integrate(phi,(x,l,min(r,t)))
            segs.append((l,r,phi))
    assert tot==0,'zero area'
    assert energy==s.Rational(5601,1400),'ODE energy'
    for t,val in zip(cuts,ints):assert val==s.Rational(23,200)*(3-abs(t))*(6+abs(t)),'active cut contact'
    checks+=4
    # Independent integration of phase-averaging loss and transport cost on single cells.
    for k in range(1,20):
        w=s.Rational(k,20);h=s.Rational(1,2);mass=h*w
        # Filled left subinterval versus uniform density w: cumulative difference is nonnegative.
        W1=s.integrate((1-w)*x,(x,0,h*w))+s.integrate(w*(h-x),(x,h*w,h))
        assert W1==h*h*w*(1-w)/2 and W1<=h*mass,'same-cell coupling cost'
        first=s.integrate(x,(x,0,h*w))-w*s.integrate(x,(x,0,h))
        allowance=0 if fault=='averaging' else h*mass
        assert abs(first)<=allowance,'phase averaging allowance'
        transport=0 if fault=='transport' else 2*h*mass
        assert 2*W1<=transport,'window convolution transport';checks+=3
    M=F(23,100);M0=F(22451259,97656250);U0=F(78227902689379,19531250000000);J=F(5601,1400);eps=F(51,50)
    theta=eps/(M-M0+eps)
    if fault=='mixing':theta/=2
    assert (1-theta)*(M+eps)+theta*M0<=M,'physical budget after repair'
    U=(1-theta)*J+theta*U0
    assert J<U<U0 and F(283,200)**2>=J/2,'strict upper improvement';checks+=2
    return checks,str(U),str(U0-U)
def quadrature(fault=None):
    from k1942_complete_scalar_energy_duality import union_capacity
    step=F(2) if fault=='coarsening' else F(1)
    zs=sorted({F(-3)+j*step for j in range(int(15/step)+1)}|{F(12)})
    for mask in range(64):
        ab=[(F(-3+i),F(-2+i)) for i in range(6) if mask>>i&1]
        vals=[]
        for z in zs:
            mass=sum(max(F(0),min(b,z)-max(a,z-9)) for a,b in ab)
            ell=max(F(0),min(F(3),z)-max(F(-3),z-9))
            vals.append(min(mass,ell-mass))
        graph=sum((r-l)*(a+b)/2 for l,r,a,b in zip(zs,zs[1:],vals,vals[1:]))
        assert graph==union_capacity(ab),'universal aligned-grid quadrature'
    return 64

if __name__=='__main__':
    n,U,gap=audit();n+=quadrature();caught=[]
    for f in ['multiplier','averaging','transport','mixing']:
        try:audit(f)
        except AssertionError:caught.append(f)
        else:raise AssertionError('missed mathematical input fault '+f)
    try:quadrature('coarsening')
    except AssertionError:caught.append('coarsening')
    else:raise AssertionError('missed quadrature coarsening fault')
    r=json.loads((ROOT/'lab/process/k1963-effective-scalar-cut-certificates.json').read_text())
    for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    assert r['grid']['energy']=='5601/1400'
    print('PASS K1963 independent',n,'controls;',len(caught),'mathematical faults; repaired U',U,'improvement',gap)
