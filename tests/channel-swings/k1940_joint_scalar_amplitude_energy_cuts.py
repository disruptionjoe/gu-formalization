"""Exact affine-rectangle pulse witnesses and Dirichlet cut-energy lower bounds."""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix,hstack,vstack,eye
ROOT=Path(__file__).resolve().parents[2];REPORT=ROOT/'lab/process/k1940-joint-scalar-amplitude-energy-cuts.json'
ELL=F(7,8)
def phi(u):
    if u<0:return -phi(-u)
    return -max(F(0),min(u,F(1),(2+ELL-u)/ELL))

def geometry(h):
    T=F(9,2);d=2*T;n=int(6/h);m=int(15/h)
    us=[-3+i*h for i in range(n+1)];zs=[-3+j*h for j in range(m+1)]
    rhs=[h*phi(us[i+side])/2 for i in range(n) for side in (0,1)]+[F(0)]*m
    edges=[]
    for i in range(n):
        for j in range(m):
            if zs[j]>=us[i+1] and zs[j+1]<=us[i]+d:
                for side in (0,1):edges.append((2*i+side,2*n+j))
    return n,m,us,zs,rhs,edges

def discover(h=F(1,8)):
    n,m,us,zs,rhs,edges=geometry(h);nv=2*n+m;ne=len(edges)
    rows=[];cols=[]
    for k,(i,j) in enumerate(edges):rows.extend([i,j]);cols.extend([k,k])
    eq=coo_matrix(([1]*(2*ne),(rows,cols)),shape=(nv,ne)).tocsr();eq=hstack([eq,coo_matrix((nv,1))]).tocsr()
    cap=np.full((ne,1),float(h*h/2));ub=vstack([hstack([eye(ne),-cap]),hstack([-eye(ne),-cap])]).tocsr();obj=np.zeros(ne+1);obj[-1]=1
    ans=linprog(obj,A_ub=ub,b_ub=np.zeros(2*ne),A_eq=eq,b_eq=np.array(list(map(float,rhs))),bounds=[(None,None)]*ne+[(0,None)],method='highs-ds',options={'threads':1});assert ans.success,ans.message
    x=[F(float(v)).limit_denominator(10**7) for v in ans.x[:-1]];res=rhs.copy();adj=[[] for _ in range(nv)]
    for k,(i,j) in enumerate(edges):res[i]-=x[k];res[j]-=x[k];adj[i].append((j,k));adj[j].append((i,k))
    seen=set()
    for root in range(nv):
        if root in seen:continue
        seen.add(root);order=[root];parent={}
        for v in order:
            for u,k in adj[v]:
                if u not in seen:seen.add(u);parent[u]=(v,k);order.append(u)
        for u in reversed(order[1:]):
            v,k=parent[u];dx=res[u];x[k]+=dx;res[v]-=dx;res[u]=0
        assert res[root]==0,'exact flow balance'
    M=4*max(map(abs,x))/(h*h)
    return dict(h=str(h),T='9/2',flows=list(map(str,x)),M_upper=str(M),energy=str(2+2/ELL),outer_ramp=str(ELL))

def verify(cert,fault=None):
    h=F(cert['h']);n,m,us,zs,rhs,edges=geometry(h);x=list(map(F,cert['flows']));M=F(cert['M_upper'])
    if fault=='flow':x[len(x)//3]+=F(1,100)
    if fault=='jacobian':M/=2
    totals=[F(0)]*len(rhs)
    for a,(i,j) in zip(x,edges):
        assert 4*abs(a)<=M*h*h,'physical peak capacity';totals[i]+=a;totals[j]+=a
    assert totals==rhs,'exact affine endpoints and column marginal'
    energy=sum((phi(us[i+1])-phi(us[i]))**2/h for i in range(n))
    assert energy==F(cert['energy'])==2+2/ELL,'actual phase energy'
    assert M<F(23,100),'strict useful amplitude budget'
    return len(edges)+len(rhs)+2

def lower(M=F(23,100),s=F(-9,20),fault=None):
    r=1+s;I=F(1,12)+r*r/2-r**3/6;J=F(1,12)+r**3/3-r**4/8;H=F(5,6)
    K=J-I*I/H;capacity=(3+s)*(6-s);defect=2-s*s/2-M*capacity/2
    if fault=='projection':K=J
    assert K==J-I*I/H,'zero-area Riesz projection'
    assert K>0 and defect>0,'nontrivial cut deficit'
    return dict(s=str(s),M=str(M),capacity=str(capacity),defect=str(defect),riesz_norm_squared=str(K),energy_lower=str(4+defect**2/K),relaxed_multiplier=str(defect/K))

def calculate(discovery=False):
    cert=discover() if discovery else json.loads(REPORT.read_text())['affine_pulse']
    count=verify(cert);lo=lower();assert F(lo['energy_lower'])>4
    return dict(claim='K1940',evidence_kind='rational continuum primal pulse and cut/Dirichlet certificates; analytic convex existence in note',exact_controls=count+2,affine_pulse=cert,cut_energy_lower=lo,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=calculate(a.write)
    if a.write:REPORT.write_text(json.dumps(r,indent=2)+'\n')
    print('PASS',r['exact_controls'],'exact controls; M_upper=',r['affine_pulse']['M_upper']);print(r['cut_energy_lower'])
