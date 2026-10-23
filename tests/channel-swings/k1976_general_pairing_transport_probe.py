"""Independent raw reconstruction and four-dimensional transport verification."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
from itertools import permutations
from math import factorial,ceil
from copy import deepcopy
from k1967_paired_raw_coefficient_observation_probe import build,gamrow,mul,add,tr
ROOT=Path(__file__).resolve().parents[2]
def decode(v):return {(i,j):F(x) for i,j,x in v}
def check(fault=None):
    r=json.loads((ROOT/'lab/process/k1976-general-pairing-transport.json').read_text())
    J,C,raw,dj,selected=build();I={(i,i):F(1) for i in range(128)}
    V=I
    gam=[]
    for k in range(14):
        g={}
        for i in range(128):j,z=gamrow(k,i);g[i,j]=F(z)
        gam.append(g);V=mul(V,g)
    ref=json.loads((ROOT/'lab/process/k1967-paired-raw-coefficient-observation.json').read_text())['scalar']['repair'][0]
    M={(i,j):F(x) for i,j,x in ref['M']['entries']};T=add((-1,mul(J[0],M)))
    a,b,c,d=map(F,ref['parameters']);O=[]
    for k in range(14):
        u,w=(a,c) if k in [0,7,8,9] else (b,d)
        O.append(mul(gam[k],add(((1 if k<7 else -1)*u,I),((1 if k<7 else -1)*w,V))))
    if fault=='coefficient':O[0]=add((2,O[0]))
    count=0
    for fam in r['families']:
        sign=fam['sign'];jets=list(map(decode,fam['jets']));B=F(fam['operator_norm_bound'])
        assert jets[0]==I and F(fam['invertibility_radius'])*2*B==1
        for q,qp in zip(jets,jets[1:]):
            lhs=mul(qp,J[0]);rhs={}
            for k in range(14):
                weight=1 if k<7 else -1
                if fault=='signature' and k==7:weight=1
                adj=O[k] if fault=='transpose' else tr(O[k])
                rhs=add((1,rhs),(weight,mul(mul(adj,q),J[k])))
            rhs=add((1,rhs),(-sign if fault!='mass_sign' else sign,mul(q,T)))
            assert lhs==rhs;count+=1
        assert add((1,jets[1]),(-1,tr(jets[1])))==decode(fam['first_jet_asymmetry'])
        assert fam['first_jet_asymmetry'] and fam['volume_commutator']
        S=decode(fam['permutation']);basis=[I,V,S,mul(V,S)]
        assert mul(S,S)==I and not add((1,mul(S,V)),(1,mul(V,S)))
        for Q,col in zip(basis,fam['reduced_columns']):
            dQ=add(*[(F(c),b) for c,b in zip(col,basis)])
            rhs=add(*[((1 if k<7 else -1),mul(mul(tr(O[k]),Q),J[k])) for k in range(14)],(-sign,mul(Q,T)))
            assert mul(dQ,J[0])==rhs;count+=1
        # The algebra is a repeated real 2x2 representation; determinant formula.
        for a,b,c,d in [(F(1),F(0),F(0),F(0)),(F(2),F(1,3),F(1,4),F(1,5)),(F(0),F(0),F(1),F(0))]:
            Q=add(*zip((a,b,c,d),basis));Qbar=add(*zip((a,-b,-c,-d),basis))
            assert mul(Q,Qbar)==add((a*a-b*b-c*c+d*d,I));count+=1
        # Full-space transfer: the Frobenius-adjoint also preserves the algebra.
        inverse={(j,i):1/v for (i,j),v in J[0].items()}
        assert mul(J[0],inverse)==I
        for j,Q in enumerate(basis):
            rhs=add(*[((1 if k<7 else -1),mul(mul(O[k],Q),tr(mul(J[k],inverse)))) for k in range(14)],(-sign,mul(Q,tr(mul(T,inverse)))))
            col=fam['frobenius_adjoint_columns'][j]
            assert rhs==add(*[(F(c),b) for c,b in zip(col,basis)])
            assert col==[fam['reduced_columns'][k][j] for k in range(4)];count+=1
        # Independent Leibniz determinant for symmetry observability.
        A=list(zip(*[[F(x) for x in c] for c in fam['reduced_columns']]))
        def mv(row):return [sum(row[i]*A[i][j] for i in range(4)) for j in range(4)]
        obs=[];row=[F(0),F(0),F(0),F(1)]
        for _ in range(4):obs.append(row);row=mv(row)
        D=F(0)
        for p in permutations(range(4)):
            term=F((-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4)))
            for i in range(4):term*=obs[i][p[i]]
            D+=term
        assert D==F(fam['reduction_consumers']['symmetry_observability_determinant'])!=0
        # Separately sum a longer series and bound its exact rational tail.
        v=[F(1),F(0),F(0),F(0)];term=v[:]
        for k in range(1,49):
            term=[sum(A[i][j]*term[j] for j in range(4))/k for i in range(4)]
            v=[a+b for a,b in zip(v,term)]
        B=max(sum(abs(x) for x in row) for row in A);err=F(3)**ceil(B)*B**49/factorial(49)
        mid=v[0]**2-v[1]**2-v[2]**2+v[3]**2
        rad=sum(2*abs(x)*err+err**2 for x in v)
        lo,hi=map(F,fam['reduction_consumers']['determinant_at_one_interval'])
        assert lo<mid-rad<=mid+rad<hi;count+=2
        # A constant scalar rescaling cannot remove first-order asymmetry.
        assert add((1,jets[1]),(-1,tr(jets[1])))
    for path,h in r['inputs'].items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h
    return count
if __name__=='__main__':
    n=check();rejected=[]
    for fault in ['coefficient','signature','transpose','mass_sign']:
        try:check(fault)
        except AssertionError:rejected.append(fault)
        else:raise AssertionError('undetected mathematical fault '+fault)
    print('PASS K1976 independent',n,'raw/reduced/determinant obligations;',len(rejected),'mathematical faults rejected')
