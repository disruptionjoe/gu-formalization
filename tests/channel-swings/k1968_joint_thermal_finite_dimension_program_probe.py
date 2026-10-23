"""Independent shell census and exact LP duals against the vertex producer."""
from fractions import Fraction as Q
from itertools import combinations,product
from pathlib import Path
import json
import numpy as np
from scipy.optimize import linprog
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/k1968-joint-thermal-finite-dimension-program.json'

def census(d):
    # Enumerate coordinate subsets rather than the producer's gap words.
    keep={};count=0
    for n in range(3,d+1):
        for tail in combinations(range(1,3*(n-1)+1),n-1):
            A=(0,)+tail
            if any(b-a>3 for a,b in zip(A,A[1:])):continue
            count+=1
            multiplicities={e:sum(a<=e<=a+3 for a in A) for e in range(A[-1]+4)}
            for k in range(1,(n-1)//2+1):
                for S in combinations(A[1:],k):
                    if all(2*sum(s<=e<=s+3 for s in S)<=multiplicities[e] for e in multiplicities):
                        keep[S]=min(keep.get(S,n),n)
    # Independently select the nondominated energy-offset/dimension pairs.
    answer={}
    for S,n in keep.items():
        g=tuple(S[i]-S[i-1] for i in range(1,len(S)))
        if not any(tuple(T[i]-T[i-1] for i in range(1,len(T)))==g and k<=n and T[0]<=S[0] and (k<n or T[0]<S[0]) for T,k in keep.items()):answer[S]=n
    return answer,count,len(keep)

def cells(S,E,signs,fault=None,tags=None):
    n=len(S);incoming=[[Q(0)]*n for _ in S];A=[];b=[]
    edges=[(i,j,S[j]-S[i]) for i in range(n) for j in range(i+1,n) if S[j]-S[i] in (1,2,3) and (tags is None or tags[i]==tags[j])]
    bath=[Q(8,15),Q(4,15),Q(2,15),Q(1,15)]
    if fault=='bath':bath=[Q(1,4)]*4
    for (i,j,g),sg in zip(edges,signs):
        low=sum(bath[:4-g]);high=sum(bath[g:]);v=[Q(0)]*n;v[i]=high;v[j]=-low
        A.append([-sg*x for x in v]+[Q(0)]*n);b.append(Q(0))
        idx=j if sg>0 else i;incoming[idx]=[x+sg*y for x,y in zip(incoming[idx],v)]
    for i in range(n):
        A.append([Q(i==j)-incoming[i][j] for j in range(n)]+[-Q(i==j) for j in range(n)]);b.append(Q(0))
    energies=list(map(Q,S))
    if fault=='energy':energies=[x+1 for x in energies]
    A.append(energies+[Q(0)]*n);b.append(E)
    c=[Q(0)]*n+[Q(1,2)]*n;eq=[Q(1)]*n+[Q(0)]*n
    return A,b,c,eq

def dot(x,y):return sum(a*b for a,b in zip(x,y))
def rational(v):return Q(float(v)).limit_denominator(10**8)
def solve(S,E,signs,fault=None,tags=None):
    A,b,c,eq=cells(S,E,signs,fault,tags);m=len(b);n=len(c)
    ans=linprog(list(map(float,c)),A_ub=np.array(A,float),b_ub=np.array(b,float),A_eq=[list(map(float,eq))],b_eq=[1],bounds=(0,None),method='highs-ds',options={'threads':1})
    if ans.success:
        x=list(map(rational,ans.x));y=list(map(rational,ans.ineqlin.marginals));v=rational(ans.eqlin.marginals[0])
        assert all(z>=0 for z in x) and dot(eq,x)==1
        assert all(dot(row,x)<=rhs for row,rhs in zip(A,b))
        assert all(z<=0 for z in y)
        assert all(sum(A[i][j]*y[i] for i in range(m))+eq[j]*v<=c[j] for j in range(n))
        assert dot(c,x)==dot(b,y)+v
        return dot(c,x),x[:len(S)],n+m+4
    # Certify infeasible orientations, rather than trusting HiGHS status.
    AA=[[float(A[i][j]) for i in range(m)]+[float(eq[j])] for j in range(n)]+[[-float(z) for z in b]+[-1.]]
    bb=[0.]*n+[-1.]
    cert=linprog([0.]*(m+1),A_ub=AA,b_ub=bb,bounds=[(None,0)]*m+[(None,None)],method='highs-ds',options={'threads':1})
    assert cert.success
    y=list(map(rational,cert.x[:-1]));v=rational(cert.x[-1])
    assert all(z<=0 for z in y)
    assert all(sum(A[i][j]*y[i] for i in range(m))+eq[j]*v<=0 for j in range(n))
    assert dot(b,y)+v>0
    return None,None,n+2

def optimum(S,E,fault=None,tags=None):
    ne=sum(S[j]-S[i] in (1,2,3) and (tags is None or tags[i]==tags[j]) for i in range(len(S)) for j in range(i+1,len(S)))
    good=[];checks=0
    for signs in product((-1,1),repeat=ne):
        r,p,n=solve(S,E,signs,fault,tags);checks+=n
        if r is not None:good.append((r,p))
    return (min(good,key=lambda x:x[0]) if good else (None,None)),checks

def run():
    doc=json.loads(REPORT.read_text());d=doc['limit'];assert d in (7,8)
    observed,count,raw=census(d)
    assert count==doc['shape_count'] and raw==doc['raw_valid_supports']
    assert observed=={tuple(z['S']):len(z['A']) for z in doc['pareto_blocks']}
    checks=3;physical=0
    from k1943_arbitrary_preparation_catalyst_energy import shell_witness
    # Two occupied components need >=3+3 dimensions. At d<=7 neither component
    # can hold two occupied sites (that component alone needs >=5), so mixtures
    # have return1/2 through d7. At d8, the sole nontrivial split3+5 is
    # verified separately by its actual tagged orientation programs.
    for fr in doc['frontiers']:
        dim=fr['d'];pieces=fr['pieces'];points={Q(1),Q(3,2),Q(2),Q(3),Q(4)}
        for z in pieces:
            lo=Q(z['lo']);points.add(lo)
            if z['hi'] is not None:points.add((lo+Q(z['hi']))/2)
        for E in sorted(points):
            values=[]
            for S,n in observed.items():
                if n>dim:continue
                (r,p),nc=optimum(S,E);checks+=nc
                if r is not None:values.append((r,S,p))
            r,S,p=min(values,key=lambda z:z[0])
            if dim==8:
                # Only nontrivial multi-tag split is dimensions3+5. Rebuild
                # its orientation programs with an explicit forbidden cross-tag
                # edge; do not convexify different pair preparations.
                (mixed,mp),nc=optimum((1,1,3),E,tags=(0,1,1));checks+=nc
                r=min(r,mixed)
            z=next(z for z in pieces if E>=Q(z['lo']) and (z['hi'] is None or E<=Q(z['hi'])))
            assert r==Q(z['slope'])*E+Q(z['intercept']),'complete exact primal/dual comparison'
            checks+=1
        # Physical matrix-unit check at an interior non-breakpoint budget.
        E=Q(3,2);vals=[]
        for S,n in observed.items():
            if n<=dim:
                (r,p),nc=optimum(S,E);checks+=nc
                if r is not None:vals.append((r,S,p))
        r,S,p=min(vals,key=lambda z:z[0]);A=next(z['A'] for z in doc['pareto_blocks'] if tuple(z['S'])==S)
        positive=[(s,w) for s,w in zip(S,p) if w];actual,nc=shell_witness(Q(1,2),[s for s,w in positive],[w for s,w in positive],A)
        assert actual==r;physical+=nc+1
    faults=[]
    baseline,_=optimum((1,3),Q(2));assert baseline[0]==Q(7,20)
    for fault in ('bath','energy'):
        changed,_=optimum((1,3),Q(2),fault);assert changed[0]!=baseline[0];faults.append(fault)
    assert not all(sum(a<=e<=a+3 for a in (0,1,2,3))>=2*sum(s<=e<=s+3 for s in (1,3)) for e in range(7));faults.append('removed_physical_padding')
    # The tempting convex-envelope relaxation is strictly too optimistic at d5.
    z=next(fr for fr in doc['frontiers'] if fr['d']==5);E=Q(3,2);row=next(r for r in z['pieces'] if Q(r['lo'])<=E and (r['hi'] is None or E<=Q(r['hi'])))
    actual=Q(row['slope'])*E+Q(row['intercept']);assert actual==Q(9,20)>Q(5,12);faults.append('unbudgeted_dimension_convexification')
    # Deleting tag separation creates a single occupied site instead of two
    # distinct sectors; a rational shift keeps the declared dimension unchanged.
    tags=[(0,1,2),(Q(1,100),Q(101,100),Q(201,100))];flat=[x for a in tags for x in a]
    assert len(set(flat))==6 and len(set((0,1,2)*2))==3;faults.append('collapsed_fractional_tags')
    if d==8:
        E=Q(3,2);singles=[]
        for S,n in observed.items():
            (r,p),nc=optimum(S,E);checks+=nc
            if r is not None:singles.append(r)
        assert min(singles)>Q(5,12),'no single-component attainment of joint infimum'
        # An initially attempted GLOBAL secant bound is false at the low-root
        # vertex (E=6/5,R=9/20). It cannot replace the tagged orientation LP.
        assert Q(9,20)<Q(2,3)-Q(6,5)/6
        (mixed,mp),nc=optimum((1,1,3),E,tags=(0,1,1));checks+=nc
        assert mixed==Q(5,12)
        # A concrete eight-level separated witness reaches the exact budget.
        for eps in (Q(1,100),Q(1,1000)):
            w=(E-1)/(Q(6,5)+eps);S=[Q(1),1+eps,3+eps];p=[1-w,w*Q(2,5),w*Q(3,5)]
            A=[Q(0),Q(1),Q(2)]+[Q(i)+eps for i in range(5)]
            assert len(set(A))==8 and sum(a*b for a,b in zip(S,p))==E
            actual,nc=shell_witness(Q(1,2),S,p,sorted(A));physical+=nc+2
            assert actual==Q(1,2)-w/5>Q(5,12)
    print('PASS K1968 independent',checks,'exact LP/shell/census obligations;',physical,'physical;',len(faults),'mathematical faults',faults)
if __name__=='__main__':run()
