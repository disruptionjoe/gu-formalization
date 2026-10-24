"""Independent symbolic projection and rational moment-integral verification."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import json
import hashlib
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]

# Deliberately separate interval implementation and integration recurrence.
def ii(x): return x if isinstance(x,tuple) else (F(x),F(x))
def outward(lo,hi):
    scale=10**27
    return F((lo*scale).__floor__(),scale),F((hi*scale).__ceil__(),scale)
def add(a,b):
    a,b=ii(a),ii(b); return outward(a[0]+b[0],a[1]+b[1])
def neg(a): a=ii(a); return -a[1],-a[0]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    a,b=ii(a),ii(b); v=[x*y for x in a for y in b]; return outward(min(v),max(v))
def div(a,b):
    b=ii(b); assert b[0]*b[1]>0
    return mul(a,(1/b[1],1/b[0]))
def power(a,n):
    ans=ii(1)
    for _ in range(n): ans=mul(ans,a)
    return ans
def evalpoly(p,x):
    ans=ii(0)
    for c in p[::-1]: ans=add(mul(ans,x),c)
    return ans
def intpoly(p,x):
    ans=ii(0)
    for n,c in enumerate(p): ans=add(ans,div(mul(c,power(x,n+1)),n+1))
    return ans

def log_bounds(a):
    a=ii(a)
    def point(x):
        z=(x-1)/(x+1); az=abs(z)
        assert az<F(3,4)
        total=2*sum(z**(2*j+1)/F(2*j+1) for j in range(60))
        tail=2*az**121/(121*(1-az*az))
        # Signed Taylor remainder enclosure (distinct from producer reciprocity).
        lo,hi=(total,total+tail) if z>=0 else (total-tail,total)
        scale=10**23
        return F((lo*scale).__floor__(),scale),F((hi*scale).__ceil__(),scale)
    return point(a[0])[0],point(a[1])[1]

def independent_norm():
    p=[-138,392,-168,-102,101]
    lo,hi=F(9,20),F(23,50)
    def val(x): return sum(F(c)*x**j for j,c in enumerate(p))
    for _ in range(55):
        m=(lo+hi)/2
        if val(m)<0: lo=m
        else: hi=m
    t=(lo,hi); L=sub(3,t)
    lam=div(evalpoly([F(-7,100),F(69,200),F(-77,200)],t),
            evalpoly([F(1,6),0,F(-1,2),F(2,3),F(-1,4)],t))
    mm=F(23,100)
    phases=[[0,sub(1,div(lam,2)),div(lam,2)],[1,0,0],
        [add(3,mul(lam,sub(3,power(t,2)))),
         add(-1,div(mul(lam,sub(power(t,2),5)),2)),div(lam,2)]]
    rows=[[add(div(mul(2,c),mm),[-9,-1,0][j]) for j,c in enumerate(poly)] for poly in phases]
    rows=[[add(poly[0],mul(2,L)),poly[1],poly[2]] for poly in rows]
    bounds=[ii(0),ii(1),ii(2),L]
    total=ii(0); integrals=[]; moments=[]
    for row,l,h in zip(rows,bounds,bounds[1:]):
        pc=[sub(intpoly(row,l),total),ii(0),div(row[1],2),div(mul(2,row[2]),3)]
        moments.append(pc)
        total=add(total,sub(intpoly(row,h),intpoly(row,l)))
        coeff=[ii(0) for _ in range(7)]
        for i,a in enumerate(pc):
            for j,b in enumerate(pc): coeff[i+j]=add(coeff[i+j],mul(a,b))
        aa=mul(2,L)
        j0=log_bounds(div(sub(aa,l),sub(aa,h)))
        jm=[j0]
        for n in range(1,5):
            jm.append(sub(mul(aa,jm[-1]),div(sub(power(h,n),power(l,n)),n)))
        integral=ii(0)
        for k in range(2,7): integral=add(integral,mul(coeff[k],jm[k-2]))
        if l[0]>0:
            jminus1=div(add(log_bounds(div(h,l)),j0),aa)
            jminus2=add(div(jminus1,aa),div(sub(div(1,l),div(1,h)),aa))
            integral=add(integral,add(mul(coeff[0],jminus2),mul(coeff[1],jminus1)))
        else: assert coeff[0]==coeff[1]==ii(0)
        integrals.append(integral)
    return t,lam,L,integrals,bounds,moments,rows

def u_integral(pc,l,h,L):
    aa=mul(2,L); j0=log_bounds(div(sub(aa,l),sub(aa,h)))
    j1=sub(mul(aa,j0),sub(h,l))
    value=add(mul(pc[2],j0),mul(pc[3],j1))
    if pc[0]!=ii(0):
        jm1=div(add(log_bounds(div(h,l)),j0),aa)
        jm2=add(div(jm1,aa),div(sub(div(1,l),div(1,h)),aa))
        value=add(value,mul(pc[0],jm2))
    return value

def independent_clipped_dual(bounds,moments,L,wing,gamma,subdivisions):
    assert 0<gamma<=2
    tails=[ii(0)]*4
    for j in range(2,-1,-1):
        tails[j]=add(tails[j+1],u_integral(moments[j],bounds[j],bounds[j+1],L))
    nodes=[]
    for j,(left,right) in enumerate(zip(bounds,bounds[1:])):
        width=div(sub(right,left),subdivisions)
        for k in range(subdivisions):
            x=add(left,mul(F(2*k+1,2),width))
            e=add(u_integral(moments[j],x,right,L),tails[j+1])
            d=sub(div(evalpoly(moments[j],x),mul(x,sub(mul(2,L),x))),e)
            nodes.append((width,d,e))
    top=bottom=F(0)
    def primitive_excess(d):
        # Integrate separately below-1 and above+1 in the linear upper column.
        lower=max(F(0),-1-gamma*d)**3-max(F(0),-1-gamma*(d+1))**3
        upper=max(F(0),gamma*(d+1)-1)**3-max(F(0),gamma*d-1)**3
        return (lower+upper)/(3*gamma)
    for i,(width,d,e) in enumerate(nodes):
        dlo,dhi=d[0]-3*width[1],d[1]+3*width[1]
        if dhi < -1/gamma: top+=width[0]*L[0]*primitive_excess(dhi)
        elif dlo > 1/gamma-1: top+=width[0]*L[0]*primitive_excess(dlo)
        for yw,yd,ye in nodes[i+1:]:
            qlo,qhi=d[0]+ye[0]-3*width[1]-yw[1],d[1]+ye[1]+3*width[1]+yw[1]
            distance=max(F(0),gamma*qlo-1,-1-gamma*qhi)
            bottom+=width[0]*yw[0]*distance**2
    return add(mul(2*gamma-gamma*gamma,wing),top+bottom),top,bottom

def independently_restrict_dual(root,L,bounds,rows,reflected=False,fault=None):
    witness=json.loads((root/'lab/process/k1989-capped-pulse-dual-certificates.json').read_text())['certificate']
    M=F(23,50) if fault=='restricted_normalization' else F(23,100)
    step=F(6,witness['grid_rows'])
    ap=[F(v)/M for v in witness['row_potentials']]
    bp=[F(v)/M for v in witness['column_potentials']]
    if reflected:
        ap=[-v for v in reversed(ap)]
        bp=[-v for v in reversed(bp)]
    # Original witness boundaries are rational; only the last cells are clipped.
    nx=next(i for i in range(len(ap)) if i*step>=L[1])
    ny=next(j for j in range(len(bp)) if j*step>=(mul(2,L))[1])
    xx=[ii(i*step) for i in range(nx)]+[L]
    yy=[ii(j*step) for j in range(ny)]+[mul(2,L)]
    lin=pen=ii(0)
    for i,(lo,hi) in enumerate(zip(xx,xx[1:])):
        for pleft,pright,row in zip(bounds,bounds[1:],rows):
            if hi[1]<=pleft[0] or lo[0]>=pright[1]: continue
            l=pleft if pleft[0]>lo[0] else lo
            h=pright if pright[1]<hi[1] else hi
            lin=add(lin,mul(ap[i],sub(intpoly(row,h),intpoly(row,l))))
    for j,(lo,hi) in enumerate(zip(yy,yy[1:])):
        def pos(v): return max(F(0),v[0]),max(F(0),v[1])
        column_mass=div(sub(power(pos(sub(hi,L)),2),power(pos(sub(lo,L)),2)),2)
        lin=add(lin,mul(bp[j],column_mass))
    for i,(xl,xh) in enumerate(zip(xx,xx[1:])):
        for j,(yl,yh) in enumerate(zip(yy,yy[1:])):
            if j<i: continue
            # Integrate the affine column height over x (independent form).
            if i==j:
                area=(mul(sub(xh,xl),sub(yh,yl)) if fault=='restricted_area' else
                      sub(mul(yh,sub(xh,xl)),div(sub(power(xh,2),power(xl,2)),2)))
            else: area=mul(sub(xh,xl),sub(yh,yl))
            p=ap[i]+bp[j]
            conjugate=p*p if -1<=p<=1 else 2*abs(p)-1
            pen=add(pen,mul(area,conjugate))
    return sub(mul(2,lin),pen)

def mathematical_checks(fault=None):
    x,L=sp.symbols('x L',positive=True)
    # Exact compatible affine fixture: integral R=L²/2 and R(L)=-L.
    R=2*L-3*x
    I=x*R-sp.integrate(R,(x,0,x))
    denominator=x*x*(2*L+x if fault=='ode_denominator' else 2*L-x)
    uprime=sp.cancel(I/denominator)
    assert sp.simplify(sp.diff(x*x*(2*L-x)*uprime,x)-x*sp.diff(R,x))==0, 'ODE derivative'
    # F=xu, a=F' certifies prefix-column cancellation for arbitrary u.
    u=sp.Function('u')(x)
    aa=sp.diff(x*u,x)
    assert sp.simplify(aa-u-x*sp.diff(u,x))==0, 'prefix column primitive'
    y=sp.symbols('y',positive=True)
    slope=2 if fault=='column_slope' else 1
    column=L*(slope*y/L-1)
    assert sp.simplify(column-(y-L))==0, 'terminal column'
    assert sp.simplify(I.subs(x,L)+sp.Rational(3,2)*L*L)==0, 'terminal compatibility'
    # Norm identity uses the base column quadratic exactly.
    base=sp.integrate((y/L-1)**2*L,(y,L,2*L))
    multiplier=2 if fault=='norm_multiplier' else 1
    assert sp.simplify(multiplier*base-L*L/3)==0, 'column-only norm'
    s,z=sp.symbols('s z',nonnegative=True)
    C=sp.Rational(9,2)
    capintegrand=(sp.Rational(1,2)-C*s-z)**2
    wedge=sp.integrate(sp.integrate(capintegrand,(z,0,sp.Rational(1,2)-C*s)),(s,0,1/(2*C)))
    target=sp.Rational(1,432) if fault=='cap_wedge' else sp.Rational(1,864)
    assert sp.simplify(wedge-target)==0, 'integrated cap wedge'
    # Moment-integral recurrence is checked by derivative, including singular terms.
    a=sp.symbols('a',positive=True)
    primitives=[-sp.log(a-x)]
    for n in range(1,5): primitives.append(a*primitives[-1]-x**n/n)
    for n,primitive in enumerate(primitives):
        assert sp.simplify(sp.diff(primitive,x)-x**n/(a-x))==0, 'moment antiderivative'
    jminus1=(sp.log(x)-sp.log(a-x))/a
    jminus2=jminus1/a-1/(a*x)
    assert sp.simplify(sp.diff(jminus1,x)-1/(x*(a-x)))==0
    assert sp.simplify(sp.diff(jminus2,x)-1/(x*x*(a-x)))==0
    return 13

def main(root=ROOT,data_path=None):
    data=json.loads((data_path or root/'lab/process/k2007-analytic-wing-projection.json').read_text())
    for path,digest in data['inputs'].items():
        assert hashlib.sha256((root/path).read_bytes()).hexdigest()==digest, 'input provenance '+path
    print('PASS K2007 provenance hashes',len(data['inputs']))
    checks=mathematical_checks()
    t,lam,L,parts,bounds,moments,rows=independent_norm()
    for independent,published in zip(parts,data['rational_integral_piece_intervals']):
        plo,phi=map(F,published)
        assert independent[0]<=plo<phi<=independent[1], 'independent actual integral enclosure'
        checks+=1
    integral=ii(0)
    for v in parts: integral=add(integral,v)
    wing=add(div(power(L,2),3),integral)
    plo,phi=map(F,data['normalized_wing_uncapped_minimum_squared_norm_interval'])
    assert wing[0]<=plo<phi<=wing[1]
    central=json.loads((root/'lab/process/k2003-exact-central-pulse-optimizer.json').read_text())
    nc=tuple(map(F,central['central_minimum_squared_norm_interval']))
    whole=add(mul(F(23,100)**2,add(sub(sub(54,mul(F(7,3),power(L,2))),mul(mul(2,t),add(3,mul(4,t)))),mul(2,integral))),nc)
    plo,phi=map(F,data['factorized_uncapped_whole_squared_norm_lower_interval'])
    assert whole[0]<=plo<phi<=whole[1], 'whole normalized factorization'
    dual,top,bottom=independent_clipped_dual(bounds,moments,L,wing,
        F(data['selected_dual_scale']),data['clipped_dual_cells_per_phase_piece'])
    reflected=data['restricted_k1989_selected_side']=='right_reflected'
    restricted=independently_restrict_dual(root,L,bounds,rows,reflected)
    rlo,rhi=map(F,data['restricted_k1989_normalized_wing_dual_interval'])
    assert restricted[0]<=rlo<rhi<=restricted[1], 'independent inherited-dual restriction'
    if data['selected_dual_method'].startswith('restricted_'): dual=restricted
    whole=add(add(mul(F(23,100)**2,sub(sub(54,mul(3,power(L,2))),mul(mul(2,t),add(3,mul(4,t))))),nc),mul(2*F(23,100)**2,dual))
    common=F(data['certified_whole_norm_lower_decimal'])
    assert whole[0]>common, 'independent whole-domain clipped dual lower threshold'
    assert F(data['whole_capped_squared_norm_lower_interval'][0])>=common
    checks+=3
    print('PASS independent whole clipped dual lower',float(whole[0]),'common threshold',float(common))
    # Endpoint/wedge derivative bound uses only exact rational constants.
    ll=F(127,50); rp=F(29,3)+F(14,207)
    assert (rp+F(3,2)/(1-1/(81*ll*ll)))/ll<F(9,2)
    assert F(3,2)*ll>rp/9 and F(1,9)<F(27,50)
    checks+=3
    mutations=['ode_denominator','column_slope','norm_multiplier','cap_wedge']
    for fault in mutations:
        try: mathematical_checks(fault)
        except AssertionError as exc: print('PASS mathematical mutation rejected:',fault,'via',str(exc))
        else: raise AssertionError('mutation survived: '+fault)
    for fault in ['restricted_normalization','restricted_area']:
        altered=independently_restrict_dual(root,L,bounds,rows,reflected,fault)
        try:
            assert altered[0]<=rlo<rhi<=altered[1], 'actual restricted-dual certificate mismatch'
        except AssertionError as exc:
            print('PASS mathematical mutation rejected:',fault,'via',str(exc))
        else: raise AssertionError('mutation survived: '+fault)
    print('PASS K2007 independent symbolic/rational obligations',checks,'and',len(mutations)+2,'mathematical mutations')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=ROOT);p.add_argument('--data',type=Path)
    args=p.parse_args();main(args.root,args.data)
