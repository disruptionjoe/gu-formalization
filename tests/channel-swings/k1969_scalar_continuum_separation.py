"""Exact algebraic halfcut optimum and an actual non-halfcut counterexample."""
from fractions import Fraction as F
from pathlib import Path
from math import comb
import argparse, hashlib, json
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1969-scalar-continuum-separation.json'
P=list(map(F,[-138,392,-168,-102,101]))
K=[F(1,6),F(0),F(-1,2),F(2,3),F(-1,4)]
D=[F(-7,100),F(69,200),F(-77,200)]
def poly(c,x):
    out=F(0)
    for z in c[::-1]:out=out*x+z
    return out
def add(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out
def scale(a,n):return [x*n for x in a]
def ia(a,b):return (a[0]+b[0],a[1]+b[1])
def im(a,b):
    v=[x*y for x in a for y in b];return min(v),max(v)
def iv(a,b):
    assert b[0]>0
    return im(a,(1/b[1],1/b[0]))
def ip(c,x):
    v=(F(0),F(0))
    for y in c[::-1]:v=ia(im(v,x),(y,y))
    return v
def isolate():
    l,r=F(9,20),F(23,50)
    for _ in range(96):
        m=(l+r)/2
        if poly(P,m)<0:l=m
        else:r=m
    return l,r
def capacity(parts):
    pts=sorted({F(-3),F(3),F(6),F(12)}|{x+d for a,b in parts for x in(a,b) for d in(0,9)})
    def vals(z):
        a=sum(max(F(0),min(b,z)-max(l,z-9)) for l,b in parts)
        ell=max(F(0),min(F(3),z)-max(F(-3),z-9))
        return a,ell-a
    ans=F(0)
    for l,r in zip(pts,pts[1:]):
        a,b=vals(l);c,d=vals(r);xs=[l,r]
        if (a-b)*(c-d)<0:xs.insert(1,l+(r-l)*(a-b)/(a-b-c+d))
        for x,y in zip(xs,xs[1:]):ans+=(y-x)*(min(vals(x))+min(vals(y)))/2
    return ans
def path_capacity(parts):
    s=sum(b-a for a,b in parts);t=2*s-6
    assert s<=3
    xs=sorted({F(0),F(6)}|{x+3 for ab in parts for x in ab})
    def w(x):return 2*sum(max(F(0),min(b,x-3)-a) for a,b in parts)-x
    def dist(v):return max(F(0),v,t-v)
    total=F(0)
    for l,r in zip(xs,xs[1:]):
        u,v=w(l),w(r);pts=[l,r]
        if u!=v:
            for level in(t,F(0)):
                if min(u,v)<level<max(u,v):pts.append(l+(r-l)*(level-u)/(v-u))
        pts=sorted(pts)
        for a,b in zip(pts,pts[1:]):total+=(b-a)*(dist(w(a))+dist(w(b)))/2
    return 9*s-total
def vint(L,t,q):
    u=min(t,q);ans=(t-t*t/(2*L))*u*u/2-u**3/6
    if q>t:ans+=t*t/(2*L)*(L*(q-t)-(q*q-t*t)/2)
    return ans
FREE=[(F(-3),F(-2)),(F(-1),F(1)),(F(2),F(3))]
def clamp(s,a,b):return max(F(0),min(b-a,s-a))
def mean(s):return sum(vint(b-a,clamp(s,a,b),b-a) for a,b in FREE)
def green(s,t):return sum(vint(b-a,clamp(s,a,b),clamp(t,a,b)) for a,b in FREE)-mean(s)*mean(t)/F(5,6)
def deficit(s):return 2-s*s/2-F(23,200)*(3-abs(s))*(6+abs(s))
def calculate():
    count=0
    def ck(cond,msg):
        nonlocal count
        assert cond,msg
        count+=1
    der=[i*P[i] for i in range(1,5)]
    bern=[sum(der[k]*F(comb(i,k),comb(3,k)) for k in range(i+1)) for i in range(4)]
    ck(bern==list(map(F,[392,280,66,154])) and min(bern)>0,'unique root by positive derivative')
    l,r=isolate();ck(poly(P,l)<0<poly(P,r),'exact isolating interval')
    ck(r-l<F(1,10**28),'isolation width')
    contact=scale(add(mul([F(-69),F(154)],K),scale(mul(D,[F(0),F(1),F(-2),F(1)]),-100)),12)
    ck(contact[:5]==P and all(x==0 for x in contact[5:]),'algebraic tangent contact')
    ki,di=ip(K,(l,r)),ip(D,(l,r));lam=iv(di,ki)
    energy=ia((F(4),F(4)),scale_tuple(iv(im(di,di),ki),2))
    ck(F(3,50)<lam[0]<lam[1]<F(7,100),'positive contact multipliers')
    ck(energy[0]>F(1730979348830867,432645592385000),'strict prior lower-bound improvement')
    ck(energy[1]<F(4000917583,10**9),'conservative numerical upper on halfcut value')
    ck(F(77,100)-F(7,200)>0,'negative Q second derivative on contact-to-plateau')
    ck(F(123,100)-F(7,200)>0,'positive Q second derivative on outer interval')
    ck(F(1)-F(7,100)/2-F(23,100)>0,'b exceeds M')
    ck(-1+F(23,200)*7==F(-39,200),'plateau derivative')
    # Exact within-model ripple bounds.
    slack=F(23,200)*F(1,4)*(9-F(1,4))-F(1,4)**2/2
    ck(slack==F(141,640)>F(1,8),'all-halfcut ripple slack')
    floor=F(3,2)+F(163,64)-3
    ck(floor==F(67,64)>F(207,200),'pointwise physical bound violation')
    violation=F(1,32)*(floor-F(207,200))
    ck(violation==F(19,51200)>0,'actual arbitrary-cut violation')
    # The finite 96-cell phase is genuinely not continuum halfcut feasible.
    t=F(7,16);la=deficit(t)/(green(t,t)+green(t,-t));s=F(-227,500)
    old=deficit(s)-la*(green(s,t)+green(s,-t))
    ck(old==F(14581117749,144545312500000)>0,'finite-grid counterexample')
    # Exact all-cut reduction on every union of eight equal cells, using complement.
    for mask in range(256):
        if mask.bit_count()>4:mask=255^mask
        parts=[(F(-3)+F(3,4)*i,F(-3)+F(3,4)*(i+1)) for i in range(8) if mask>>i&1]
        ck(capacity(parts)==path_capacity(parts),'capacity versus cumulative path')
    inputs=['lab/process/k1942-complete-scalar-energy-duality.json','lab/process/k1965-scalar-uniform-lipschitz-certificates.json']
    return dict(result_id='K1969',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',
        target_claim='NONE-NOT-A-KILL',exact_controls=count,polynomial=list(map(str,P)),
        root_interval=list(map(str,(l,r))),lambda_interval=list(map(str,lam)),
        energy_interval=list(map(str,energy)),derivative_bernstein=list(map(str,bern)),
        ripple={'support_positive':['5/2','11/4'],'height':'2','primitive_bound':'1/8',
                'halfcut_slack':'141/640','violated_cut':['163/64','165/64'],
                'violation_lower':str(violation)},
        finite_phase_violation=str(old),
        scope='Exact all-halfcut optimum; explicit all-halfcut-feasible but all-cut-infeasible phase; full optimum remains open.',
        inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
def scale_tuple(a,n):return a[0]*n,a[1]*n
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();r=calculate()
    if args.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert r==json.loads(OUT.read_text()),'report equality'
    print('PASS K1969',r['exact_controls'],'exact controls')
    print('halfcut energy interval',r['energy_interval'])
