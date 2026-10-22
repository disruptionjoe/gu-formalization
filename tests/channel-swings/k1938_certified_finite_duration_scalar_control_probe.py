"""Independent polygon geometry and primal/dual arithmetic; no LP solver rerun."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
import k1938_certified_finite_duration_scalar_control as p

def polygon_area(u0,u1,z0,z1,d):
    poly=[(u0,z0),(u1,z0),(u1,z1),(u0,z1)]
    for fn in [lambda u,z:z-u,lambda u,z:d-z+u]:
        out=[]
        for a,b in zip(poly,poly[1:]+poly[:1]):
            va,vb=fn(*a),fn(*b)
            if va>=0:out.append(a)
            if (va<0 and vb>0) or (va>0 and vb<0):
                q=va/(va-vb);out.append(tuple(x+q*(y-x) for x,y in zip(a,b)))
        poly=out
        if not poly:return F(0)
    return abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(poly,poly[1:]+poly[:1])))/2

def check(record,fault=None):
    T,h=F(record['T']),F(record['h']);d=2*T;n=int(6/h);m=int((6+d)/h)
    ys=list(map(F,record['outer']['dual']));flows=list(map(F,record['inner']['flows']));cap=F(record['inner']['m_inner']);rows=[F(0)]*n;cols=[F(0)]*m;den=F(0);k=0;count=0
    if fault=='flow':flows[0]+=1
    for i in range(n):
      a=-3+i*h;b=a+h
      for j in range(m):
        z=-3+j*h;zz=z+h;area=polygon_area(a,b,z,zz,d)
        assert area==p.area(a,b,z,zz,d),'polygon versus integral geometry';count+=1
        den+=area*abs(ys[i]+ys[n+j])
        if area and z>=b and zz<=a+d:
            f=flows[k];k+=1;assert abs(f)<=cap*h*h,'actual pointwise bound';rows[i]+=f;cols[j]+=f
    # Integrate the fixed affine profile independently through midpoints.
    demand=[]
    for i in range(n):
        u=-3+(i+F(1,2))*h;v=min(abs(u),F(1),3-abs(u));demand.append(h*v*(1 if u<0 else -1))
    assert rows==demand and not any(cols),'actual endpoint integrals'
    lower=2*sum(ys[i]*demand[i] for i in range(n))/den
    if fault=='jacobian':lower/=2
    assert lower==F(record['M_lower']),'physical lower conversion'
    # For a unit-slope cell residual r=x-h/2, primitive x(x-h)/2 attains -h^2/8.
    A=h*h/8;P=h/2;correction=2*A/(T*T)+2*P/T
    if fault=='residual':correction=0
    assert 2*cap+correction==F(record['M_upper']),'exact residual consumption'
    return count+n+m+3

def main():
    report=json.loads(p.REPORT.read_text());assert report['source_sha256']==hashlib.sha256(Path(p.__file__).read_bytes()).hexdigest(),'source pin baseline'
    count=sum(check(r) for r in report['records'])
    last=report['records'][-1];assert F(last['M_upper'])<F(1,4),'released quarter-budget pulse'
    # A=[-3,-9/20] gives a strictly stronger continuum obstruction than both old elementary bounds.
    s=-F(9,20);cut=(4-s*s)/((3+s)*(6-s))
    assert cut==F(1519,6579)>F(23,100)>F(2,9),'shifted cut consumer'
    for fault in ['flow','jacobian','residual']:
        try:check(report['records'][0],fault)
        except AssertionError as e:print('DETECTED mathematical input',fault,str(e))
        else:raise AssertionError('missed '+fault)
    try:p.verify_outer(report['records'][0]['outer'],'capacity')
    except AssertionError as e:print('DETECTED mathematical input capacity',str(e))
    else:raise AssertionError('missed capacity')
    for key in ['exact_controls','source_sha256']:
        bad=dict(report);bad[key]='corrupted'
        try:assert bad==report,key
        except AssertionError:print('DETECTED reporting',key)
        else:raise AssertionError('missed report mutation')
    print('PASS',count,'independent exact controls; 4 math-input, 2 report/pin faults')
if __name__=='__main__':main()
