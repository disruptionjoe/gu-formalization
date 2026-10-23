"""Separate raw reconstruction and symbolic integration-by-parts checks."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
def check(fault=None):
    old=json.loads((ROOT/'lab/process/k1951-coordinated-zero-southeast-principal.json').read_text());J=[{} for _ in range(15)]
    for n,b in enumerate(old['blocks']):
        B={(i,j):F(v) for i,j,v in b['basis']['entries']};E={(i,j):F(v) for i,j,v in b['section']['entries']}
        for (i,k),v in B.items():
            for (kk,j),w in E.items():
                if kk==k:
                    rr=b['coordinates'][i];key=(rr%128,4*n+j);J[rr//128][key]=J[rr//128].get(key,0)+v*w
    J=[{k:v for k,v in j.items() if v} for j in J]
    rec=json.loads((ROOT/'lab/process/k1967-paired-raw-coefficient-observation.json').read_text())['scalar']['repair'][0]
    mat={(i,j):F(v) for i,j,v in rec['M']['entries']};T={}
    for (i,k),v in J[0].items():
        for (kk,j),w in mat.items():
            if kk==k:T[i,j]=T.get((i,j),0)-v*w
    T={k:v for k,v in T.items() if v};support=set().union(*(j.keys() for j in J[:14]))
    if fault=='invent_gradient_mass':support.add(next(iter(T)))
    assert not support&set(T),'gradient cannot reach mass-coordinate projection'
    r=json.loads((ROOT/'lab/process/k1973-differential-adjoint-density.json').read_text())
    assert T=={(i,j):F(v) for i,j,v in r['target_entries']},'independent target entries'
    # Volume diagonal from the actual successive tensor action, not report parity.
    volume=[]
    for col in range(128):
        row=col;v=1
        for k in reversed(range(14)):
            bit=1<<(6-k%7);v*=(-1)**((row>>(7-k%7)).bit_count())
            if k>=7:v*=1 if row&bit else -1
            row^=bit
        assert row==col;volume.append(v)
    keys=sorted(support);cols=[{ij:v for ij,v in J[k].items() if volume[ij[0]]==sign} for k in range(14) for sign in [1,-1]]
    A=S.MutableSparseMatrix(len(keys),28,{(i,j):S.Rational(cols[j][key]) for i,key in enumerate(keys) for j in range(28) if key in cols[j]})
    assert A.rank()==28,'independent derivative image rank'
    x=S.symbols('x',real=True);rho=1+x*x;Q=S.diag(2+x*x,3+x**4);O=S.Matrix([[x,1],[-2,x*x]])
    u=S.Matrix([x*(1-x),x*x*(1-x)]);v=S.Matrix([x**2*(1-x),x*(1-x)**2])
    L=rho*Q
    adj=-v.diff(x)+Q.inv()*O.T*Q*v-Q.inv()*Q.diff(x)*v-(rho.diff(x)/rho)*v
    if fault=='omit_density':adj+=(rho.diff(x)/rho)*v
    if fault=='omit_pairing':adj+=Q.inv()*Q.diff(x)*v
    if fault=='wrong_derivative_sign':adj+=2*v.diff(x)
    residual=((u.diff(x)+O*u).T*L*v-u.T*L*adj-(u.T*L*v).diff(x))[0]
    assert S.cancel(residual)==0,'actual variable-density integration by parts'
    # Half-density conjugacy, with its matched weighted domain, is exact.
    f=1+x+x*x;h=1+x*x
    assert S.cancel(h*(f.diff(x)+h.diff(x)*f/h)-(h*f).diff(x))==0,'half-density conjugacy'
    for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    return len(T),A.rank()
if __name__=='__main__':
    n=check();caught=[]
    for f in ['invent_gradient_mass','omit_density','omit_pairing','wrong_derivative_sign']:
        try:check(f)
        except AssertionError as e:caught.append([f,str(e)])
        else:raise AssertionError('missed mathematical fault '+f)
    print('PASS K1973 separate raw/symbolic baseline',n,'math faults',caught)
