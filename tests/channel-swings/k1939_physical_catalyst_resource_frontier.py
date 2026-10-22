"""Exact physical shell completion and two-support energy/return certificates."""
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json
import sympy as sy
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/k1939-physical-catalyst-resource-frontier.json'
def coeff(t,d):
    L=sum(t**b for b in range(4-d))/sum(t**b for b in range(4));return L,t**d*L

def rate(t,d,x):
    L,H=coeff(t,d);heavy=max(H*x,L*(1-x))
    return max(F(0),((1+H)*x-heavy)/2)+max(F(0),((1+L)*(1-x)-heavy)/2)

def optimum(t,E):
    if E<1:return None
    best=(F(1,2),None,F(1),F(1))
    for d in (1,2,3):
        a=max(1,3-d)
        if E<a:continue
        L,H=coeff(t,d);lo=max(F(0),1-(E-a)/d)
        knots=[lo,F(1),L/(1+L+H),(1+L)/(1+L+H),L/(L+H)]
        for x in knots:
            if lo<=x<=1:
                val=(rate(t,d,x),d,x,F(a)+d*(1-x))
                if val[0]<best[0]:best=val
    return best

def shell_witness(t,S,weights,A,fault=None):
    """Build every actual shell, including incomplete edges and unused inputs."""
    vs=[sy.Matrix([1,0]),sy.Matrix([0,1]),sy.Matrix([1,1])/sy.sqrt(2),sy.Matrix([1,sy.I])/sy.sqrt(2)]
    W=sy.Matrix([[1,1],[1,-1]])/sy.sqrt(2);Z=sum(t**b for b in range(4))
    outs=[[sy.S(0) for _ in A] for _ in vs];checks=0
    shells=sorted({a+b for a in A for b in range(4)})
    for E in shells:
        bs=[b for b in range(4) if E-b in A];occ=[b for b in bs if E-b in S];n=len(bs)
        assert 2*len(occ)<=n,'physical shell rank doubling';checks+=1
        if not occ:continue
        order=sorted(occ,key=lambda b:weights[S.index(E-b)]*t**b,reverse=True)
        outside=[b for b in bs if b not in occ]
        if len(occ)==1:spec=[(occ[0],[occ[0],outside[0]],outside[0])]
        else:spec=[(order[0],order,outside[0]),(order[1],outside,outside[1])]
        us=[]
        for j,v in enumerate(vs):
            q=W*v
            if fault=='phase' and j==3:q=sy.conjugate(q)
            U=sy.eye(n) if len(occ)==1 else sy.zeros(n)
            for col,pair,comp in spec:
                i,k=map(bs.index,pair);col=bs.index(col);comp=bs.index(comp)
                U[i,col]=q[0];U[k,col]=q[1];U[i,comp]=-sy.conjugate(q[1]);U[k,comp]=sy.conjugate(q[0])
            assert sy.simplify(U.H*U)==sy.eye(n),'full physical unitarity';checks+=1;us.append(U)
        for j,U in enumerate(us):
            for b in occ:
                col=bs.index(b);wt=sy.Rational(weights[S.index(E-b)]*t**b/Z)
                for r,bb in enumerate(bs):outs[j][A.index(E-bb)]+=wt*sy.simplify(abs(U[r,col])**2)
                for k,V in enumerate(us):
                    assert sy.simplify((V[:,col].H*U[:,col])[0]-(vs[k].H*vs[j])[0])==0,'full complex Gram';checks+=1
    returns=[]
    for row in outs:
        row=list(map(sy.simplify,row));assert sum(row)==1,'probability'
        returns.append(sum(abs(v-(sy.Rational(weights[S.index(a)]) if a in S else 0)) for a,v in zip(A,row))/2)
    return max(returns),checks+4

def calculate(fault=None):
    nchecks=0;examples=[]
    # Minimal physical dimension, with actual incomplete edge shells.
    for N in range(1,5):
        A=list(range(2*N+1));S=list(range(1,2*N,2));w=[F(1,N)]*N
        if fault=='empty_level':A=A[1:]
        _,k=shell_witness(F(1,2),S,w,A);nchecks+=k
        slack=[sum(a+b==E for a in A for b in range(4))-2*sum(a+b==E for a in S for b in range(4)) for E in range(max(A)+4)]
        assert min(slack)>=0 and sum(slack)==4,'exact dimension slack';nchecks+=1
    # Independent all-input complex constructions at nonoptimal weights.
    for d in (1,2,3):
        a=max(1,3-d);A=list(range(a+d+4));S=[a,a+d]
        for x in [F(1,5),F(1,2),F(4,5)]:
            r,k=shell_witness(F(3,4),S,[x,1-x],A,fault);nchecks+=k
            expected=rate(F(3,4),d,x)
            if fault=='return_factor':expected*=2
            assert r==expected,'all-input return formula';nchecks+=1
    for t in [F(1,4),F(1,2),F(3,4)]:
        last=F(1)
        for E in [F(1),F(21,20),F(11,10),F(5,4),F(3,2),F(2),F(5,2),F(3),F(4)]:
            r,d,x,energy=optimum(t,E);assert r<=last and energy<=E,'budget and monotonicity';last=r;nchecks+=1
            examples.append(dict(t=str(t),E=str(E),return_cost=str(r),gap=d,lower_weight=str(x),mean_energy=str(energy)))
    return dict(claim='K1939',evidence_kind='exact rational resource optimization and full complex shell matrices; universal proofs in note',exact_controls=nchecks,dimension='D_min=2N+1',examples=examples,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=calculate()
    if a.write:REPORT.write_text(json.dumps(r,indent=2)+'\n')
    print('PASS',r['exact_controls'],'exact controls');print([x for x in r['examples'] if x['t']=='1/2'])
