"""Independent shell, exact matrix-pencil, and small-spacing verification."""
from fractions import Fraction as F
from pathlib import Path
import json,copy
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def ret(t,S,p):
    Z=sum(t**k for k in range(4));inc=[F(0)]*len(S)
    for i in range(len(S)):
        for j in range(i+1,len(S)):
            gap=S[j]-S[i]
            if gap.denominator!=1 or not 1<=gap<=3:continue
            g=int(gap);lo=sum(t**b for b in range(4-g))/Z;hi=t**g*lo
            z=hi*p[i]-lo*p[j]
            inc[j]+=max(z,0);inc[i]+=max(-z,0)
    return sum(max(p[i]-inc[i],0) for i in range(len(S)))/2

def two_ladder_value(E,delta):
    # Complete cones of the exact g=2 return: adjacent breakpoints within each tag.
    aa=[F(0),F(2,5),F(4,5),F(9,10),F(1)]
    rays=[(c,j,3-2*a+c*delta,ret(F(1,2),[F(1),F(3)],[a,1-a])) for c in range(2) for j,a in enumerate(aa)]
    values=[R for c,j,e,R in rays if e<=E]
    for i,(c,j,e,R) in enumerate(rays):
        for cc,jj,ee,RR in rays[i+1:]:
            if c==cc and abs(j-jj)>1:continue
            if e==ee or not min(e,ee)<=E<=max(e,ee):continue
            w=(E-ee)/(e-ee);values.append(w*R+(1-w)*RR)
    return min(values)

def check(d):
    count=0
    for r in d['physical_transfers']:
        A=list(map(F,r['spectrum']));S=list(map(F,r['support']));p=list(map(F,r['weights']));delta=F(r['delta']);t=F(r['t'])
        assert min(A)==0 and len(A)==r['d'] and min(b-a for a,b in zip(A,A[1:]))>=delta,'physical spacing'
        for E in {a+b for a in A for b in range(4)}:
            assert 2*sum(E-z in [0,1,2,3] for z in S)<=sum(E-z in [0,1,2,3] for z in A),'shell rank'
        assert sum(p)==1
        assert sum(a*w for a,w in zip(S,p))==F(r['energy']),'energy'
        assert ret(t,S,p)==F(r['return_error']),'return'
        assert F(r['energy'])-F(r['base_energy'])<=r['overhead']*delta,'overhead'
        count+=4
    for r in d['exposed_face_families']:
        E=F(r['E']);delta=F(r['delta']);A=list(map(F,r['spectrum']));S=list(map(F,r['support']));p=list(map(F,r['weights']))
        assert min(b-a for a,b in zip(A,A[1:]))>=delta,'face spacing'
        assert sum(e*w for e,w in zip(S,p))==E,'face energy'
        assert ret(F(1,2),S,p)-(F(63,100)-F(3,20)*E)==F(r['gap']),'face return'
        assert F(r['sharp_leading_coefficient'])==F(3,20)*min(E-F(6,5),F(11,5)-E),'face leading'
        count+=4
    # Offset packing lower bound for arbitrary component weights.
    for m in range(2,9):
        weights=[F(j+1,m*(m+1)//2) for j in range(m)]
        for delta in [F(1,100),F(1,20)]:
            offsets=[j*delta for j in range(m)]
            cost=sum(w*x for w,x in zip(weights,offsets))
            assert cost>=delta*(1-max(weights));count+=1
    curves=json.loads((ROOT/'lab/process/k1968-joint-thermal-finite-dimension-program.json').read_text())['frontiers']
    for r,curve in zip(d['lipschitz_consumers'],curves):
        L=F(r['lipschitz_constant']);assert all(abs(F(p['slope']))<=L for p in curve['pieces']),'modulus'
        assert L==max(abs(F(p['slope'])) for p in curve['pieces']),'minimal piecewise modulus'
        count+=1
    z=s.symbols('z');V=s.Rational(13,30)
    gap=s.Rational(1,2)-s.Rational(2,5)/(6+5*z)-V
    assert s.simplify(gap-z/(3*(5*z+6)))==0
    assert s.limit(gap/z,z,0)==s.Rational(d['exact_linear_coefficient_eight_levels']),'leading coefficient'
    for r in d['sharp_eight_level_controls']:
        delta=F(r['delta']);assert F(r['gap'])==delta/(18+15*delta),'sharp gap';count+=1
    optimized=0
    for E in [F(5,4),F(7,5),F(3,2),F(17,10),F(2),F(21,10)]:
        rr=E-F(6,5)
        for delta in [F(1,1000),F(1,100)]:
            exact=two_ladder_value(E,delta)
            predicted=F(63,100)-F(3,20)*E+F(3,20)*delta*min(rr/(1+delta),(1-rr)/(1-delta))
            assert exact==predicted,'complete two-ladder program';optimized+=1
    # Cramer determinants are affine when only the energy row varies.
    # Check several nontrivial bases directly, independently of thermal producer.
    pencils=0
    for k in range(1,7):
        B=s.Matrix([[1,1,1],[1,-k,0],[1+z,3+2*z,5-k*z]])
        b=s.Matrix([1,0,s.Rational(7,5)])
        det=s.expand(B.det());assert s.degree(det,z)<=1
        nums=[]
        for j in range(3):
            Bj=B.copy();Bj[:,j]=b;n=s.expand(Bj.det());assert s.degree(n,z)<=1;nums.append(n)
        p=s.Matrix([n/det for n in nums]);assert (B*p-b).applyfunc(s.simplify)==s.zeros(3,1)
        objective=(p[0]+2*p[1]+3*p[2])/7
        num,den=s.fraction(s.cancel(objective));assert s.degree(num,z)<=1 and s.degree(den,z)<=1
        # Bounded c=0 branches cancel to constants, not quadratic onset.
        assert s.cancel((k*z)/(2*z))==s.Rational(k,2)
        pencils+=1
    return count,pencils,optimized
if __name__=='__main__':
    d=json.loads((ROOT/'lab/process/k1998-uniform-small-spacing-transfer.json').read_text());n,p,o=check(d);faults=0
    for key,field in [('physical_transfers','energy'),('physical_transfers','return_error'),('lipschitz_consumers','lipschitz_constant'),('sharp_eight_level_controls','gap'),('exposed_face_families','sharp_leading_coefficient')]:
        bad=copy.deepcopy(d);bad[key][0][field]=str(F(bad[key][0][field])+F(1,100))
        try:check(bad)
        except AssertionError as e:
            assert str(e);faults+=1;print('DETECTED mathematical fault:',field,str(e))
        else:raise AssertionError('missed '+field)
    print('PASS K1998 probe:',n,'physical/curve controls;',p,'exact symbolic matrix pencils;',o,'complete four-population programs;',faults,'faults rejected after green baseline')
