"""Sharp arbitrary-weight return and exact orientation-cell energy certificates."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse, hashlib, json
import numpy as np
from scipy.optimize import linprog
from k1939_physical_catalyst_resource_frontier import coeff, shell_witness, optimum as two_optimum
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/k1943-arbitrary-preparation-catalyst-energy.json'

def rate(t,S,p,fault=None):
    incoming=[F(0)]*len(S);B=F(0);total=F(0)
    for i,j in [(i,j) for i in range(len(S)) for j in range(i+1,len(S))]:
        d=S[j]-S[i]
        if d not in (1,2,3):continue
        L,H=coeff(t,int(d));x=H*p[i];y=L*p[j]
        incoming[i]+=max(F(0),y-x);incoming[j]+=max(F(0),x-y)
        B+=min(x,y);total+=x+y
    r=sum(max(F(0),a-b) for a,b in zip(p,incoming))/2
    if fault=='normalization':r*=2
    return r,B,total

def cell(t,S,E,orientation):
    """min c.x with A.x<=b and 1.p=1, p,z>=0."""
    n=len(S);incoming=[[F(0)]*n for _ in S];A=[];b=[]
    for i,sign in enumerate(orientation):
        L,H=coeff(t,S[i+1]-S[i]);v=[F(0)]*n;v[i]=H;v[i+1]=-L
        # sign=1: left shell weight >= right; right receives positive difference.
        A.append([-sign*a for a in v]+[F(0)]*n);b.append(F(0))
        recipient=i+1 if sign==1 else i
        incoming[recipient]=[x+sign*y for x,y in zip(incoming[recipient],v)]
    for i in range(n):
        row=[F(int(i==j))-incoming[i][j] for j in range(n)]+[F(-int(i==j)) for j in range(n)]
        A.append(row);b.append(F(0))
    A.append(list(map(F,S))+[F(0)]*n);b.append(E)
    c=[F(0)]*n+[F(1,2)]*n;eq=[F(1)]*n+[F(0)]*n
    return A,b,c,eq

def solve_cell(t,S,E,orient):
    A,b,c,eq=cell(t,S,E,orient)
    ans=linprog(list(map(float,c)),A_ub=np.array(A,float),b_ub=np.array(b,float),A_eq=[list(map(float,eq))],b_eq=[1],bounds=(0,None),method='highs-ds',options={'threads':1})
    if not ans.success:raise AssertionError('unexpected infeasible orientation cell')
    cv=lambda xs:[F(float(v)).limit_denominator(10**8) for v in xs]
    cert=dict(orientation=list(orient),x=list(map(str,cv(ans.x))),dual_ineq=list(map(str,cv(ans.ineqlin.marginals))),dual_eq=str(cv(ans.eqlin.marginals)[0]))
    verify_cell(t,S,E,cert)
    return cert

def verify_cell(t,S,E,cert,fault=None):
    A,b,c,eq=cell(t,S,E,cert['orientation']);x=list(map(F,cert['x']));y=list(map(F,cert['dual_ineq']));v=F(cert['dual_eq'])
    if fault=='energy':x[0]+=F(1,100)
    if fault=='dual':v+=F(1,100)
    assert len(x)==len(c) and len(y)==len(b),'certificate dimensions'
    dot=lambda a,b:sum(u*v for u,v in zip(a,b))
    assert all(a>=0 for a in x) and dot(eq,x)==1,'normalized nonnegative preparation and deficits'
    assert all(dot(row,x)<=rhs for row,rhs in zip(A,b)),'orientation/deficit/energy primal feasibility'
    assert all(a<=0 for a in y),'dual inequality signs'
    assert all(sum(A[i][j]*y[i] for i in range(len(b)))+v*eq[j]<=c[j] for j in range(len(c))),'dual coefficient domination'
    primal=dot(c,x);dual=dot(b,y)+v
    assert primal==dual,'exact strong-duality certificate'
    assert primal==rate(t,S,x[:len(S)])[0],'actual support-deficit rate'
    return primal,len(A)+len(c)+6

def canonical_paths(K):
    yield [1]
    def visit(ds):
        a=max(1,3-ds[0]);S=[a]
        for d in ds:S.append(S[-1]+d)
        if S[-1]>K:return
        yield S
        for d in (1,2,3):
            if ds[-1]+d>=4:yield from visit(ds+[d])
    for d in (1,2,3):yield from visit([d])

def mixture_matrix(t,K,E):
    blocks=[];nv=0
    for S in canonical_paths(K):
        for orientation in product((-1,1),repeat=len(S)-1):
            A,b,c,eq=cell(t,S,E,orientation)
            blocks.append(dict(support=S,orientation=list(orientation),offset=nv,A=A[:-1],b=b[:-1],c=c,eq=eq));nv+=len(c)
    A=[];b=[];c=[F(0)]*nv;eq=c.copy();energy=c.copy()
    for block in blocks:
        off=block['offset'];k=len(block['c']);S=block['support']
        c[off:off+k]=block['c'];eq[off:off+k]=block['eq'];energy[off:off+len(S)]=map(F,S)
        for row,rhs in zip(block['A'],block['b']):A.append([F(0)]*off+row+[F(0)]*(nv-off-k));b.append(rhs)
    A.append(energy);b.append(E)
    return A,b,c,eq,blocks

def mixture_solve(t,K,E):
    A,b,c,eq,blocks=mixture_matrix(t,K,E)
    ans=linprog(np.array(c,float),A_ub=np.array(A,float),b_ub=np.array(b,float),A_eq=[np.array(eq,float)],b_eq=[1.],bounds=(0,None),method='highs-ds',options={'threads':1})
    assert ans.success,ans.message
    cv=lambda xs:list(map(str,[F(float(v)).limit_denominator(10**8) for v in xs]))
    cert=dict(t=str(t),K=K,E=str(E),x=cv(ans.x),y=cv(ans.ineqlin.marginals),v=cv(ans.eqlin.marginals)[0])
    mixture_verify(cert);return cert

def mixture_verify(cert,fault=None):
    A,b,c,eq,blocks=mixture_matrix(F(cert['t']),cert['K'],F(cert['E']));x=list(map(F,cert['x']));y=list(map(F,cert['y']));v=F(cert['v'])
    if fault=='mix_dual':v+=1
    dot=lambda a,b:sum(i*j for i,j in zip(a,b))
    assert len(x)==len(c) and len(y)==len(b),'mixture dimensions'
    assert all(z>=0 for z in x) and dot(eq,x)==1,'mixture normalization'
    assert all(dot(row,x)<=rhs for row,rhs in zip(A,b)),'mixture primal feasibility'
    assert all(z<=0 for z in y),'mixture dual signs'
    assert all(sum(row[j]*yy for row,yy in zip(A,y))+eq[j]*v<=c[j] for j in range(len(c))),'mixture dual coefficients'
    value=dot(c,x);assert value==dot(b,y)+v,'mixture exact duality'
    active=[]
    for block in blocks:
        off=block['offset'];S=block['support'];w=x[off:off+len(S)];mass=sum(w)
        if mass:active.append(dict(support=S,mass=str(mass),weights=list(map(str,[z/mass for z in w])),energy=str(dot(S,w)/mass),return_cost=str(rate(F(cert['t']),S,[z/mass for z in w])[0])))
    cert['infimum_upper']=str(value);cert['active_components']=active
    cert['global_lower_from_cutoff']=str(max(F(0),value-2*F(cert['E'])/cert['K']))
    return len(c)+len(A)+6

def physicalize_mix(cert,epsilon=F(1,1000)):
    comps=cert['active_components'];E=F(cert['E']);t=F(cert['t'])
    shifted_mean=sum(F(c['mass'])*(F(c['energy'])+(i+1)*epsilon) for i,c in enumerate(comps))
    scale=min(F(1),(E-1)/(shifted_mean-1));S=[];p=[];A={F(0),F(1),F(2)}
    if scale<1:S.append(F(1));p.append(1-scale)
    for i,c in enumerate(comps):
        shift=(i+1)*epsilon;mass=scale*F(c['mass'])
        for e,w in zip(c['support'],map(F,c['weights'])):
            if w:S.append(e+shift);p.append(mass*w)
        A.update(F(e)+shift for e in range(max(c['support'])+4))
    order=sorted(range(len(S)),key=lambda i:S[i]);S=[S[i] for i in order];p=[p[i] for i in order];A=sorted(A)
    actual,k=shell_witness(t,S,p,A)
    expected=scale*F(cert['infimum_upper'])+(1-scale)/2
    assert actual==expected==rate(t,S,p)[0],'physical separated-mixture rate'
    assert sum(e*w for e,w in zip(S,p))<=E,'physical separated-mixture energy'
    return dict(t=str(t),E=str(E),epsilon=str(epsilon),physical=list(map(str,A)),support=list(map(str,S)),weights=list(map(str,p)),mean_energy=str(sum(e*w for e,w in zip(S,p))),return_cost=str(actual)),k+2

def calculate(discover=False,fault=None):
    cases=[];checks=0
    # Every cell is accepted with exact primal/dual or exact Farkas evidence.
    if discover:
        for t,S,E in [(F(1,2),[1,3,5],F(3,2)),(F(1,2),[1,3,5],F(2)),(F(1,2),[1,3,5],F(3)),(F(3,4),[1,3,5],F(3)),(F(1,2),[1,3,5,7],F(4))]:
            certs=[]
            for orientation in product((-1,1),repeat=len(S)-1):
                try:certs.append(solve_cell(t,S,E,orientation))
                except AssertionError as exc:
                    # Infeasible cells are not discarded as proof: store and
                    # solve an exact separating dual below.
                    A,b,c,eq=cell(t,S,E,orientation)
                    # Farkas y<=0, A^T y+v eq<=0, b.y+v>=1.
                    m=len(b);Au=[];bu=[]
                    for j in range(len(c)):Au.append([float(A[i][j]) for i in range(m)]+[float(eq[j])]);bu.append(0.)
                    Au.append([-float(z) for z in b]+[-1.]);bu.append(-1.)
                    ans=linprog([0.]*(m+1),A_ub=Au,b_ub=bu,bounds=[(None,0)]*m+[(None,None)],method='highs-ds',options={'threads':1})
                    assert ans.success,str(exc)
                    vals=[F(float(z)).limit_denominator(10**8) for z in ans.x]
                    certs.append(dict(orientation=list(orientation),infeasible=True,y=list(map(str,vals[:-1])),v=str(vals[-1])))
            cases.append(dict(t=str(t),support=S,energy_budget=str(E),cells=certs))
    else:cases=json.loads(REPORT.read_text())['energy_cases']
    for case in cases:
        t=F(case['t']);S=case['support'];E=F(case['energy_budget']);values=[]
        assert len(case['cells'])==2**(len(S)-1),'all orientation cells'
        assert {tuple(c['orientation']) for c in case['cells']}==set(product((-1,1),repeat=len(S)-1)),'orientation coverage'
        for cert in case['cells']:
            if cert.get('infeasible'):
                A,b,c,eq=cell(t,S,E,cert['orientation']);y=list(map(F,cert['y']));v=F(cert['v'])
                assert all(z<=0 for z in y),'Farkas signs'
                assert all(sum(A[i][j]*y[i] for i in range(len(b)))+v*eq[j]<=0 for j in range(len(c))),'Farkas coefficients'
                assert sum(a*z for a,z in zip(b,y))+v>0,'Farkas strict contradiction';checks+=len(c)+2
            else:
                value,k=verify_cell(t,S,E,cert,fault);values.append((value,cert));checks+=k
        best,cert=min(values,key=lambda x:x[0]);p=list(map(F,cert['x']))[:len(S)]
        actual,k=shell_witness(t,S,p,list(range(max(S)+2)))
        assert actual==best,'attaining full shell witness';checks+=k+1
        case['optimum']=str(best);case['weights']=list(map(str,p));case['two_support_global']=str(two_optimum(t,E)[0])
    # Arbitrary preparations, no optimization assumption, including 3/4 gaps.
    for t,S,p in [(F(1,2),[1,3,5],[F(1,2),F(1,3),F(1,6)]),(F(3,4),[2,3,6],[F(1,10),F(1,5),F(7,10)]),(F(2,3),[1,4,5],[F(1,5),F(3,5),F(1,5)]),(F(1,2),[1,3,7],[F(1,3)]*3)]:
        r,B,total=rate(t,S,p,fault);actual,k=shell_witness(t,S,p,list(range(max(S)+4)))
        assert actual==r,'arbitrary-weight all-input equality';assert B<=r and total<=1,'disjoint bath-label bound';checks+=k+2
    mixtures=[mixture_solve(F(1,2),K,E) for K,E in [(5,F(3,2)),(5,F(2)),(5,F(3)),(7,F(3))]] if discover else json.loads(REPORT.read_text())['convexified_cutoffs']
    for cert in mixtures:checks+=mixture_verify(cert,fault)
    physical=[]
    for cert in [mixtures[0],mixtures[-1]]:
        example,k=physicalize_mix(cert);physical.append(example);checks+=k
    # Actual nondegenerate, fractionally shifted components at E=3/2.
    eps=F(1,100);mass=F(50,121);S=[F(1),1+eps,3+eps];p=[1-mass,mass*F(2,5),mass*F(3,5)]
    A=sorted(set([F(0),F(1),F(2)]+[F(i)+eps for i in range(5)]))
    actual,k=shell_witness(F(1,2),S,p,A);checks+=k
    assert sum(a*b for a,b in zip(S,p))==F(3,2),'actual shifted mean energy'
    assert actual==F(101,242)<F(89,200),'disconnected mixture beats connected example';checks+=2
    return dict(claim='K1943' ,evidence_kind='exact rational LP/Farkas and full complex shell controls; universal proof in note',exact_controls=checks,energy_cases=cases,convexified_cutoffs=mixtures,physical_mixtures=physical,shifted_example=dict(epsilon=str(eps),support=list(map(str,S)),physical=list(map(str,A)),weights=list(map(str,p)),energy='3/2',return_cost=str(actual)),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--write',action='store_true');args=a.parse_args();r=calculate(args.write)
    if args.write:REPORT.write_text(json.dumps(r,indent=2)+'\n')
    print('PASS',r['exact_controls'],'exact controls')
    for row in r['energy_cases']:print(row['t'],row['support'],row['energy_budget'],row['optimum'],row['weights'],row['two_support_global'])
