"""Independent raw full-matrix elimination and exact phase-certificate replay."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import json,copy,hashlib
import sympy as sp
from k1979_multicoordinate_symmetric_pairing_probe import data,decode
from k1967_paired_raw_coefficient_observation_probe import mul,add,tr
ROOT=Path(__file__).resolve().parents[2]
def full_rank(J,T,O,sign,p=1000033):
    # Direct R, without the producer's J0 inverse, sector map or block elimination.
    l=[{i:(j,v) for (i,j),v in a.items()} for a in O]
    r=[{i:(j,v) for (i,j),v in a.items()} for a in J[:14]];t={i:(j,v) for (i,j),v in T.items()}
    rows=[defaultdict(F) for _ in range(16384)]
    for i in range(128):
        for j in range(128):
            col=128*i+j
            for k in range(14):
                a,u=l[k][i];b,v=r[k][j];rows[128*a+b][col]+=(1 if k<7 else -1)*u*v
            b,v=t[j];rows[128*i+b][col]-=sign*v
    basis={}
    for row in rows:
        q={j:v.numerator*pow(v.denominator,-1,p)%p for j,v in row.items() if v};q={j:v for j,v in q.items() if v}
        while q:
            k=min(q);c=q[k]
            if k not in basis:
                inv=pow(c,-1,p);basis[k]={j:v*inv%p for j,v in q.items()};break
            for j,v in basis[k].items():
                z=(q.get(j,0)-c*v)%p
                if z:q[j]=z
                else:q.pop(j,None)
    return len(basis)
def check(d,expensive=False):
    I,V,J,T,O=data();count=0
    assert sp.isprime(1000033)
    # Independent chart/derivation controls for fractional leading orders.
    t,y=sp.symbols('t y',positive=True)
    for exponent in [sp.Rational(-3,2),sp.Rational(-1,3),sp.Rational(1,2),sp.Rational(7,3)]:
        a=sp.sqrt(1+y*y);q=t**exponent*a
        dx0=sp.diff(q,y)/t
        dx1=sp.diff(q,t)-y*sp.diff(q,y)/t
        assert sp.simplify(dx0-t**(exponent-1)*sp.diff(a,y))==0,'transverse derivative order'
        assert sp.simplify(dx1-t**(exponent-1)*(exponent*a-y*sp.diff(a,y)))==0,'radial derivative order'
        count+=2
    norm=lambda A:max(sum(abs(v) for (i,j),v in A.items() if i==r) for r in range(128))
    for f in d['families']:
        sign=f['sign']
        def R(A):return add(*[((1 if k<7 else -1),mul(mul(tr(O[k]),A),J[k])) for k in range(14)],(-sign,mul(A,T)))
        raw=R(I);cols=[add((1,mul(tr(j),raw)),(-1,mul(tr(raw),j))) for j in J[:14]]
        M=[[F(v) for v in row] for row in f['phase_matrix']];B=[[F(v) for v in row] for row in f['phase_inverse']]
        for i,ij in enumerate(map(tuple,f['phase_slots'])):
            assert M[i]==[c.get(ij,F(0)) for c in cols],'raw phase coefficients';count+=1
        for i in range(14):
            for j in range(14):assert sum(B[i][k]*M[k][j] for k in range(14))==F(i==j),'phase inverse';count+=1
        bn=max(sum(abs(v) for v in row) for row in B);cr=sum(norm(tr(o))*norm(j) for o,j in zip(O,J))+norm(T);c=2*cr*sum(norm(tr(j)) for j in J[:14])
        assert [bn,cr,c]==list(map(F,[f['phase_inverse_row_norm'],f['right_operator_norm_bound'],f['phase_perturbation_bound']])),'norm constants'
        assert bn*c*F(f['one_phase_exclusion_radius'])<=F(1,2),'one-phase neighborhood'
        if expensive:assert full_rank(J,T,O,sign)==16384,'full raw zero-order rank';count+=1
        old=json.loads((ROOT/'lab/process/k1979-multicoordinate-symmetric-pairing.json').read_text())['families'];h=next(x for x in old if x['sign']==sign)
        assert add(*[((1 if k<7 else -1),mul(decode(v),J[k])) for k,v in enumerate(h['identity_first_jets'])])==raw,'genuine multicoordinate positive first jet';count+=3
    for p,h in d['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    return count
if __name__=='__main__':
    d=json.loads((ROOT/'lab/process/k2000-raw-pairing-polynomial-structure.json').read_text());n=check(d,True);caught=[]
    for fault in ['mass_sign','phase_coefficient','inverse','radius']:
        q=copy.deepcopy(d);f=q['families'][0]
        if fault=='mass_sign':f['sign']*=-1
        if fault=='phase_coefficient':f['phase_matrix'][0][0]=str(F(f['phase_matrix'][0][0])+1)
        if fault=='inverse':f['phase_inverse'][0][0]=str(F(f['phase_inverse'][0][0])+1)
        if fault=='radius':f['one_phase_exclusion_radius']=str(4*F(f['one_phase_exclusion_radius']))
        try:check(q)
        except AssertionError as e:caught.append([fault,str(e)])
        else:raise AssertionError('undetected mathematical fault '+fault)
    print('PASS K2000 direct raw rank at second prime,',n,'phase/contrary checks;',caught)
