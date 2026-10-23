"""Independent polygon areas and exact finite Hilbert/QP verification."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]

def polygon_area(a,b,c,d):
    poly=[(a,c),(b,c),(b,d),(a,d)]
    for f in [lambda x,y:y-x,lambda x,y:9+x-y]:
        out=[]
        for P,Q in zip(poly,poly[1:]+poly[:1]):
            u,v=f(*P),f(*Q)
            if u>=0:out.append(P)
            if (u<0<v) or (v<0<u):
                t=u/(u-v);out.append((P[0]+t*(Q[0]-P[0]),P[1]+t*(Q[1]-P[1])))
        poly=out
    if not poly:return F(0)
    return abs(sum(x*v-y*u for (x,y),(u,v) in zip(poly,poly[1:]+poly[:1])))/2

def check(fault=None):
    r=json.loads((ROOT/'lab/process/k1980-constructive-minimum-norm-pulse.json').read_text());cells=[(i,j,F(w)) for i,j,w in r['cells']];M=F(r['amplitude']);n=len(cells)
    if fault=='cell_area':cells[0]=(cells[0][0],cells[0][1],cells[0][2]+1)
    us=list(map(F,[-3,-1,1,3]));zs=list(map(F,[-3,0,3,6,9,12]));expected=[(i,j,polygon_area(a,b,c,d)) for i,(a,b) in enumerate(zip(us,us[1:])) for j,(c,d) in enumerate(zip(zs,zs[1:])) if polygon_area(a,b,c,d)]
    assert expected==cells,'independent strip polygon geometry'
    W=s.diag(*[w for i,j,w in cells]);P=[]
    for axis in [0,1]:
        mat=s.zeros(n)
        for k,c in enumerate(cells):
            indices=[j for j,d in enumerate(cells) if d[axis]==c[axis]];mass=sum(cells[j][2] for j in indices)
            for j in indices:mat[k,j]=cells[j][2]/mass
        assert mat*mat==mat and W*mat==mat.T*W,'weighted orthogonal projection';P.append(mat)
    g=s.Matrix(list(map(F,r['g'])));wit=s.Matrix(list(map(F,r['witness'])));assert P[0]*wit==g and P[1]*wit==s.zeros(n,1)
    count=3;I=s.eye(n)
    for rec in r['controls']:
        eps=F(rec['epsilon']);q=F(rec['contraction']);assert q==2/(2+eps)
        A=I+(P[0]+P[1])/eps;opt=A.inv()*g/eps
        assert max(map(abs,opt))<=M,'unconstrained fixture optimum is also box optimum'
        assert (opt.T*W*opt)[0]+((P[0]*opt-g).T*W*(P[0]*opt-g)+(P[1]*opt).T*W*(P[1]*opt))[0]/eps<=(wit.T*W*wit)[0]
        v=s.zeros(n,1)
        for _ in range(rec['iterations']):
            raw=((2*I-P[0]+(P[1] if fault=='column_sign' else -P[1]))*v+g)/(eps+(1 if fault=='step_size' else 2))
            v=s.Matrix([max(-M,min(M,x)) for x in raw])
        residual=((P[0]*v-g).T*W*(P[0]*v-g)+(P[1]*v).T*W*(P[1]*v))[0]
        assert residual==F(rec['residual_squared']),'independent exact iterate residual'
        err=((v-opt).T*W*(v-opt))[0];assert err<=q**(2*rec['iterations'])*(opt.T*W*opt)[0],'certified contraction error'
        count+=4
    # Pointwise clipping of a genuinely saturated input; changed amplitude is a mathematical fault.
    cap=M*2 if fault=='amplitude' else M
    clipped=[max(-cap,min(cap,x)) for x in [-3*M,-M,F(0),M,3*M]]
    assert clipped==[-M,-M,0,M,M],'amplitude projection'
    for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    return count+1
if __name__=='__main__':
    n=check();faults=[]
    for fault in ['cell_area','column_sign','step_size','amplitude']:
        try:check(fault)
        except AssertionError as e:faults.append((fault,str(e)))
        else:raise AssertionError('undetected mathematical fault '+fault)
    print('PASS K1980 separate',n,'geometry/projection/QP obligations;',faults)
