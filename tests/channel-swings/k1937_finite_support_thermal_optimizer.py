"""Finite occupied-support optimizer; exact path arithmetic and complex shell witnesses."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import argparse,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/k1937-finite-support-thermal-optimizer.json'
def coeff(t,d):
    L=sum(t**b for b in range(4-d))/sum(t**b for b in range(4))
    return L,t**d*L

def profile(t,gaps,root,fault=None):
    n=len(gaps)+1
    assert 0<t<1 and all(d in (1,2,3) for d in gaps)
    assert all(a+b>=4 for a,b in zip(gaps,gaps[1:])),'triple occupancy'
    x=[F(0)]*n;x[root]=F(1);D=F(0)
    for i in range(root-1,-1,-1):
        L,H=coeff(t,gaps[i]);x[i]=L*x[i+1]/(1+H if fault!='denominator' else 1-H);D+=H*x[i]
    for i in range(root+1,n):
        L,H=coeff(t,gaps[i-1]);x[i]=H*x[i-1]/(1+L);D+=L*x[i]
    assert D<=F(1,2),'all-input leakage bound'
    Z=sum(x);return [a/Z for a in x],F(1,2)/Z,D/Z

def optimize(t,N):
    """State stores best arm reward and outward ordered gaps for each first gap."""
    arms=[]
    for side in (0,1):
        table=[{}]
        for n in range(1,N):
            row={}
            for d in (1,2,3):
                L,H=coeff(t,d);v=L/(1+H) if side==0 else H/(1+L)
                tail=(F(0),()) if n==1 else max((table[n-1][e] for e in (1,2,3) if d+e>=4),key=lambda z:z[0])
                row[d]=(v*(1+tail[0]),(d,)+tail[1])
            table.append(row)
        arms.append(table)
    best=None
    for a in range(N):
        b=N-1-a
        ls=[(F(0),())] if a==0 else list(arms[0][a].values())
        rs=[(F(0),())] if b==0 else list(arms[1][b].values())
        for vl,dl in ls:
            for vr,dr in rs:
                if dl and dr and dl[0]+dr[0]<4:continue
                reward=1+vl+vr
                if best is None or reward>best[0]:best=(reward,tuple(reversed(dl))+dr,a)
    reward,gaps,root=best;weights,R,D=profile(t,gaps,root)
    assert R==1/(2*reward),'DP reward and physical weights'
    return gaps,root,weights,R,D

def shell_unitary(E,S,root,j,fault=None):
    vs=[s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([1,1])/s.sqrt(2),s.Matrix([1,s.I])/s.sqrt(2)]
    v=s.Matrix([[1,1],[1,-1]])*vs[j]/s.sqrt(2)
    if fault=='phase' and j==3:v=s.conjugate(v)
    occ=[b for b in range(4) if E-b in S];U=s.eye(4)
    if len(occ)==1:
        b=occ[0];other=next(a for a in range(4) if a!=b);pairs=[(b,(b,other),other)]
    else:
        assert len(occ)==2
        heavy=min(occ,key=lambda b:abs(S.index(E-b)-root));light=next(b for b in occ if b!=heavy)
        outside=[b for b in range(4) if b not in occ];U=s.zeros(4)
        pairs=[(heavy,(heavy,light),outside[0]),(light,tuple(outside),outside[1])]
    for col,rows,other in pairs:
        U[rows[0],col]=v[0];U[rows[1],col]=v[1]
        U[rows[0],other]=-s.conjugate(v[1]);U[rows[1],other]=s.conjugate(v[0])
    return U,vs

def witness(t,gaps,root,fault=None):
    weights,R,D=profile(t,gaps,root,fault);S=[3]
    for d in gaps:S.append(S[-1]+d)
    dim=S[-1]+4;outs=[[s.S(0)]*dim for _ in range(4)];Z=sum(t**b for b in range(4));count=0
    for E in range(S[0],S[-1]+4):
        occ=[b for b in range(4) if E-b in S]
        if not occ:continue
        us=[shell_unitary(E,S,root,j,fault)[0] for j in range(4)];vs=shell_unitary(E,S,root,0)[1]
        for j,U in enumerate(us):
            assert s.simplify(U.H*U)==s.eye(4),'full shell unitarity';count+=1
            for b in occ:
                wt=s.Rational(weights[S.index(E-b)]*t**b/Z)
                for a in range(4):outs[j][E-a]+=wt*s.simplify(abs(U[a,b])**2)
                for k,V in enumerate(us):
                    assert s.simplify((V[:,b].H*U[:,b])[0]-(vs[k].H*vs[j])[0])==0,'complex channel Gram';count+=1
    returns=[]
    for j,c in enumerate([F(1,2),F(1,2),F(1),F(1,2)]):
        out=[s.simplify(x) for x in outs[j]]
        assert sum(out)==1,'output normalization'
        returns.append(sum(abs(x-(s.Rational(weights[S.index(a)]) if a in S else 0)) for a,x in enumerate(out))/2)
        assert returns[-1]==(1-c)*weights[root]+(2*c-1)*D,'physical all-input transport';count+=2
    assert max(returns)==R,'attaining worst-case return';return count+1

def calculate(fault=None):
    count=0;examples=[]
    for t in [F(1,4),F(1,2),F(3,4),F(9,10)]:
        previous=F(1)
        for N in range(1,21):
            ds,r,w,R,D=optimize(t,N)
            assert R<previous and R>t*t/(1+t*t)**2,'finite-size ordering';previous=R
            assert sum(w)==1 and D<=w[r]/2,'normalization/leakage';count+=2
            if N<=8:examples.append({'t':str(t),'N':N,'gaps':list(ds),'root':r,'return':str(R),'weights':list(map(str,w))})
    # Deliberately include every possible local pair, left/right and mixed roots.
    for gaps,root in [((1,3,1),1),((3,1,3),2),((2,2,2),1),((1,3,2,2),3),((2,3,1,3),1)]:
        count+=witness(F(3,4),gaps,root,fault)
    needs=[]
    for target in [F(1,4),F(1,5),F(17,100),F(161,1000)]:
        N=1
        while optimize(F(1,2),N)[3]>target:N+=1
        needs.append({'t':'1/2','return_budget':str(target),'minimum_occupied_levels':N})
    return {'claim':'K1937','evidence_kind':'exact rational DP and full complex shell matrices; universal analytic proof in note','exact_controls':count,'examples':examples,'support_budget_consumers':needs,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();result=calculate()
    if a.write:REPORT.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',result['exact_controls'],'exact controls',result['support_budget_consumers'])
