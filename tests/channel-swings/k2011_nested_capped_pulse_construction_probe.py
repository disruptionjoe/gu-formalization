"""Independent polygon geometry, polynomial quadrature and mathematical fault checks."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib
from k1983_certified_continuum_pulse_evaluation import TL,TR,LL,LR,DG
ROOT=Path(__file__).resolve().parents[2];REPORT=ROOT/'lab/process/k2011-nested-capped-pulse-construction.json';M=Q(23,100);T=(TL+TR)/2;L=(LL+LR)/2

def polygon_area(a,b,c,d):
    p=[(a,c),(b,c),(b,d),(a,d)]
    for f in (lambda x,y:y-x,lambda x,y:x+9-y):
        nxt=[]
        for X,Y in zip(p,p[1:]+p[:1]):
            fx,fy=f(*X),f(*Y)
            if fx>=0:nxt.append(X)
            if (fx<0<fy) or (fy<0<fx):
                t=fx/(fx-fy);nxt.append((X[0]+t*(Y[0]-X[0]),X[1]+t*(Y[1]-X[1])))
        p=nxt
        if not p:return Q(0)
    return abs(sum(x*v-y*u for (x,y),(u,v) in zip(p,p[1:]+p[:1])))/2

def phase(x):
    if x<0:return -phase(-x)
    if x<=T:return (-1+L*(1-T)**2/2)*x
    if x<=1:return -L*T*T/2+(-1+L*(1+T*T)/2)*x-L*x*x/2
    if x<=2:return Q(-1)
    return -3-3*L+(1+5*L/2)*x-L*x*x/2

def integrate(fun,a,b,order=4):
    cuts=sorted({a,b}|{x for x in [-T,T,Q(-2),Q(-1),Q(0),Q(1),Q(2)] if a<x<b});out=Q(0)
    for l,h in zip(cuts,cuts[1:]):
        if order==2:out+=(h-l)*(fun(l)+4*fun((l+h)/2)+fun(h))/6
        else:out+=(h-l)*sum(w*fun(l+(h-l)*Q(k,4)) for k,w in enumerate([7,32,12,32,7]))/90
    return out

def certify(c,mut=None):
    n=c['rows'];a=list(map(Q,c['row_potentials']));b=list(map(Q,c['column_potentials']));h=Q(6,n)
    us=[-3+i*h for i in range(n+1)];zs=[-3+j*h for j in range(len(b)+1)]
    areas=[[polygon_area(x,y,z,w) for z,w in zip(zs,zs[1:])] for x,y in zip(us,us[1:])]
    if mut=='geometry':areas[0][0]=h*h
    assert sum(map(sum,areas))==54,'actual strip geometry'
    v=[[max(-M,min(M,x+y)) for y in b] for x in a]
    if mut=='cap':v[0][0]=M+Q(1,100)
    assert all(abs(x)<=M for row in v for x in row),'actual cap'
    gs=[2*integrate(phase,x,y,2) for x,y in zip(us,us[1:])]
    linear=2*sum(x*y for x,y in zip(a,gs));penalty=Q(0)
    for i,row in enumerate(areas):
        for j,area in enumerate(row):
            z=a[i]+b[j];penalty+=area*(z*z if abs(z)<=M else 2*M*abs(z)-M*M)
    if mut=='normalization':linear/=2
    lower=linear-penalty-18*DG*h*sum(map(abs,a))
    assert lower==Q(c['norm_lower']),'continuum Fenchel normalization'
    row2=Q(0);col2=Q(0)
    for i,(l,r) in enumerate(zip(us,us[1:])):
        def er(x):return sum(v[i][j]*max(Q(0),min(w,x+9)-max(z,x)) for j,(z,w) in enumerate(zip(zs,zs[1:])))-2*phase(x)
        row2+=integrate(lambda x:er(x)**2,l,r)
    for j,(l,r) in enumerate(zip(zs,zs[1:])):
        def ec(x):return sum(v[i][j]*max(Q(0),min(y,x)-max(z,x-9)) for i,(z,y) in enumerate(zip(us,us[1:])))
        col2+=(r-l)*(ec(l)**2+4*ec((l+r)/2)**2+ec(r)**2)/6
    if mut=='false_zero':row2=Q(0)
    assert row2==Q(c['row_surrogate_L2_squared']) and row2>0,'full row residual'
    assert col2==Q(c['column_L2_squared']) and col2>0,'full column residual'
    rr=Q(c['row_continuum_L1_upper'])-54*DG;cc=Q(c['column_continuum_L1_upper'])
    assert rr*rr>=6*row2 and cc*cc>=15*col2
    assert lower>Q('2.3494')
    return n*len(b)

def main():
    r=json.loads(REPORT.read_text());cells=sum(certify(c) for c in r['certificates']);faults=0
    for mutation in ['geometry','cap','normalization','false_zero']:
        try:certify(r['certificates'][0],mutation)
        except AssertionError:faults+=1
        else:raise AssertionError('undetected mathematical fault '+mutation)
    assert Q(r['certificates'][-1]['norm_lower'])>Q('2.3897489868')
    for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    print('PASS K2011 polygon cells',cells,'full continuum residual integrations',3,'mathematical faults',faults,'provenance hashes',len(r['inputs']))
if __name__=='__main__':main()
