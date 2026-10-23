"""Exact local unrestricted bilinear transport; no source-star identification."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
from math import factorial,ceil
from k1970_weighted_adjoint_mass_completion_probe import plus,product,transpose,dec
from k1973_differential_adjoint_density import data
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1976-general-pairing-transport.json'
def enc(A):return [[i,j,str(v)] for (i,j),v in sorted(A.items())]
def norm(A):
    return max([sum(abs(v) for (r,c),v in A.items() if r==i) for i in range(128)])
def setup():
    vol,J,T=data();I={(i,i):F(1) for i in range(128)}
    inv={(j,i):1/v for (i,j),v in J[0].items()};assert product(J[0],inv)==I and product(inv,J[0])==I
    a,b,c,d=map(F,json.loads((ROOT/'lab/process/k1967-paired-raw-coefficient-observation.json').read_text())['scalar']['repair'][0]['parameters'])
    O=[]
    for k in range(14):
        axis=k%7;g={}
        for j in range(128):
            bit=1<<(6-axis);sgn=(-1)**((j>>(7-axis)).bit_count())
            if k>=7:sgn*=1 if j&bit else -1
            g[j^bit,j]=F(sgn)
        u,w=(a,c) if k in [0,7,8,9] else (b,d)
        O.append(product(g,{ij:(1 if k<7 else -1)*(u+w*vol[ij]) for ij in I}))
    return I,vol,J,T,inv,O
def mm(A,B):return [[sum((a*b for a,b in zip(row,col)),F(0)) for col in zip(*B)] for row in A]
def det(A):
    A=[r[:] for r in A];d=F(1)
    for j in range(len(A)):
        i=next((i for i in range(j,len(A)) if A[i][j]),None)
        if i is None:return F(0)
        if i!=j:A[i],A[j]=A[j],A[i];d=-d
        v=A[j][j];d*=v;A[j]=[x/v for x in A[j]]
        for i in range(j+1,len(A)):
            v=A[i][j];A[i]=[x-v*y for x,y in zip(A[i],A[j])]
    return d
def reduction_consumers(columns):
    A=[list(row) for row in zip(*[[F(x) for x in c] for c in columns])]
    obs=[];row=[[F(0),F(0),F(0),F(1)]]
    for _ in range(4):obs+=row;row=mm(row,A)
    determinant=det(obs);assert determinant
    v=[[F(1)],[F(0)],[F(0)],[F(0)]];term=v
    for j in range(1,41):
        term=[[x[0]/j] for x in mm(A,term)];v=[[a[0]+b[0]] for a,b in zip(v,term)]
    B=max(sum(abs(x) for x in row) for row in A)
    error=F(3)**ceil(B)*B**41/factorial(41)
    def square(x):
        a,b=x-error,x+error
        return (F(0) if a<=0<=b else min(a*a,b*b),max(a*a,b*b))
    q=[square(x[0]) for x in v]
    lo=q[0][0]-q[1][1]-q[2][1]+q[3][0]
    hi=q[0][1]-q[1][0]-q[2][0]+q[3][1]
    interval=[F(4),F(5)] if lo>0 else [F(-3,2),F(-7,5)]
    assert interval[0]<lo<hi<interval[1]
    return dict(symmetry_observability_determinant=str(determinant),determinant_at_one_interval=list(map(str,interval)),taylor_order=40,remainder_bound=str(error))
def produce():
    I,vol,J,T,inv,O=setup();out=[]
    for sign in [-1,1]:
        def L(Q):
            out={}
            for k in range(14):out=plus(out,product(product(transpose(O[k]),Q),J[k]),F(1 if k<7 else -1))
            return product(plus(out,product(Q,T),-sign),inv)
        jets=[I]
        for _ in range(4):jets.append(L(jets[-1]))
        B=sum(norm(transpose(O[k]))*norm(product(J[k],inv)) for k in range(14))+norm(product(T,inv))
        assert B>0
        for i in range(4):
            q,qp=jets[i:i+2];res=product(qp,J[0])
            for k in range(14):res=plus(res,product(product(transpose(O[k]),q),J[k]),F(-1 if k<7 else 1))
            res=plus(res,product(q,T),sign);assert not res
            assert norm(jets[i+1])<=B*norm(jets[i])
        asym=plus(jets[1],transpose(jets[1]),-1)
        off=plus(product(jets[1],vol),product(vol,jets[1]),-1)
        S={ij:F(1) for ij in jets[1]};VS=product(vol,S)
        assert product(S,S)==I and not plus(product(S,vol),VS)
        basis=[I,vol,S,VS];columns=[]
        for Q in basis:
            Y=L(Q);coeff=[];rem=Y.copy()
            for U,V in [(I,vol),(S,VS)]:
                p=next(ij for ij in U if vol[ij[0],ij[0]]==1)
                m=next(ij for ij in U if vol[ij[0],ij[0]]==-1)
                a=(Y.get(p,F(0))+Y.get(m,F(0)))/2
                b=(Y.get(p,F(0))-Y.get(m,F(0)))/2
                coeff.extend([str(a),str(b)]);rem=plus(plus(rem,U,-a),V,-b)
            assert not rem
            columns.append(coeff)
        adjoint_columns=[]
        for j,Q in enumerate(basis):
            Y={}
            for k in range(14):
                Y=plus(Y,product(product(O[k],Q),transpose(product(J[k],inv))),F(1 if k<7 else -1))
            Y=plus(Y,product(Q,transpose(product(T,inv))),-sign)
            rem=Y.copy();coeff=[]
            for b in basis:
                c=sum((v*Y.get(ij,F(0)) for ij,v in b.items()),F(0))/128
                coeff.append(str(c));rem=plus(rem,b,-c)
            assert not rem and coeff==[columns[k][j] for k in range(4)]
            adjoint_columns.append(coeff)
        out.append(dict(sign=sign,reduced_columns=columns,frobenius_adjoint_columns=adjoint_columns,reduction_consumers=reduction_consumers(columns),permutation=enc(S),operator_norm_bound=str(B),invertibility_radius=str(1/(2*B)),jets=[enc(q) for q in jets],first_jet_asymmetry=enc(asym),volume_commutator=enc(off)))
    return dict(result_id='K1976',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',families=out,scope='Local analytic nonsymmetric nondegenerate bilinear pairing, fixed raw core and principal coefficients. No source adjoint, symmetric positive metric, global domain or physical GU realization.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1967-paired-raw-coefficient-observation.json','lab/process/k1951-coordinated-zero-southeast-principal.json','tests/channel-swings/k1973_differential_adjoint_density.py','tests/channel-swings/k1970_weighted_adjoint_mass_completion_probe.py']})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=produce()
    if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert r==json.loads(OUT.read_text())
    print('PASS K1976',[(v['sign'],v['operator_norm_bound'],len(v['first_jet_asymmetry']),len(v['volume_commutator'])) for v in r['families']])
