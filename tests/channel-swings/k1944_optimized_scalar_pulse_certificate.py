"""Exact continuum pulse certificate; floating LP discovers, rational checks accept."""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json
from itertools import groupby
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
ROOT=Path(__file__).resolve().parents[2];REPORT=ROOT/'lab/process/k1944-optimized-scalar-pulse-certificate.json'

def geometry(h):
    n=int(6/h);m=int(15/h);us=[-3+i*h for i in range(n+1)];zs=[-3+j*h for j in range(m+1)];edges=[]
    for i in range(n):
        for j in range(m):
            if zs[j]>=us[i+1] and zs[j+1]<=us[i]+9:
                for side in (0,1):edges.append((2*i+side,2*n+j))
    return n,m,us,zs,edges

def discover(h=F(1,32),M=F(2299,10000)):
    n,m,us,zs,edges=geometry(h);ne=len(edges);nv=ne+n+1+n
    rr=[];cc=[];vv=[];rhs=[]
    for k,(a,b) in enumerate(edges):rr.extend([a,b]);cc.extend([k,k]);vv.extend([1.,1.])
    for i in range(n):
        for side in (0,1):rr.append(2*i+side);cc.append(ne+i+side);vv.append(-float(h/2))
    neq=2*n+m
    # Oddness guarantees exact zero area after paired rationalization.
    for i in range(n//2+1):
        rr.extend([neq,neq]);cc.extend([ne+i,ne+n-i]);vv.extend([1.,1.]);neq+=1
    Aeq=coo_matrix((vv,(rr,cc)),shape=(neq,nv)).tocsr()
    ar=[];ac=[];av=[];br=[]
    for i in range(n):
        for a in [F(j,64) for j in range(-128,129)]:
            r=len(br);ar.extend([r]*3);ac.extend([ne+i,ne+i+1,ne+n+1+i]);av.extend([-float(2*a/h),float(2*a/h),-1.]);br.append(float(a*a))
    Aub=coo_matrix((av,(ar,ac)),shape=(len(br),nv)).tocsr()
    bounds=[(-float(M*h*h/4),float(M*h*h/4))]*ne
    for u in us:
        if -2<=u<=-1:bounds.append((1.,1.))
        elif 1<=u<=2:bounds.append((-1.,-1.))
        elif abs(u)==3:bounds.append((0.,0.))
        else:bounds.append((None,None))
    bounds += [(0,None)]*n
    obj=np.zeros(nv);obj[ne+n+1:]=float(h)
    ans=linprog(obj,A_ub=Aub,b_ub=br,A_eq=Aeq,b_eq=np.zeros(neq),bounds=bounds,method='highs-ipm',options={'threads':1,'disp':True})
    assert ans.success,ans.message
    y=[F(0)]*(n+1)
    for i in range(n//2):y[i]=F(round(float(ans.x[ne+i])*10**8),10**8);y[n-i]=-y[i]
    x=[F(round(float(v)*10**12),10**12) for v in ans.x[:ne]]
    rhs=[h*y[i+side]/2 for i in range(n) for side in (0,1)]+[F(0)]*m
    residual=rhs.copy();adj=[[] for _ in rhs]
    for k,(i,j) in enumerate(edges):residual[i]-=x[k];residual[j]-=x[k];adj[i].append((j,k));adj[j].append((i,k))
    seen=set()
    for root in range(len(rhs)):
        if root in seen:continue
        seen.add(root);order=[root];parent={}
        for v in order:
            for u,k in adj[v]:
                if u not in seen:seen.add(u);parent[u]=(v,k);order.append(u)
        for u in reversed(order[1:]):
            v,k=parent[u];dx=residual[u];x[k]+=dx;residual[v]-=dx;residual[u]=0
        assert residual[root]==0,'exact bipartite balance'
    peak=4*max(map(abs,x))/h**2;energy=sum((b-a)**2/h for a,b in zip(y,y[1:]))
    return dict(h=str(h),phase_nodes=list(map(str,y)),flow_runs=[[len(list(group)),str(value)] for value,group in groupby(x)],amplitude=str(peak),energy=str(energy),discovery_amplitude=str(M),discovery_kind='floating LP with tangent energy objective; accepted only after exact verification')

def verify(cert,fault=None):
    h=F(cert['h']);n,m,us,zs,edges=geometry(h);y=list(map(F,cert['phase_nodes']));x=[F(value) for count,value in cert['flow_runs'] for _ in range(count)];M=F(cert['amplitude']);checks=0
    if fault=='flow':x[len(x)//3]+=F(1,100)
    if fault=='trace':y[0]=F(1,100)
    if fault=='capacity':M/=2
    assert len(y)==n+1 and len(x)==len(edges),'dimensions'
    assert y[0]==y[-1]==0,'zero boundary traces';assert all(y[i]==-y[n-i] for i in range(n+1)),'odd phase'
    assert all(y[i]==1 for i,u in enumerate(us) if -2<=u<=-1),'left plateau';assert all(y[i]==-1 for i,u in enumerate(us) if 1<=u<=2),'right plateau';checks+=5
    total=[F(0)]*(2*n+m)
    for f,(a,b) in zip(x,edges):
        assert 4*abs(f)<=M*h*h,'physical peak bound with 2c Jacobian';total[a]+=f;total[b]+=f;checks+=1
    rhs=[h*y[i+side]/2 for i in range(n) for side in (0,1)]+[F(0)]*m
    assert total==rhs,'pointwise affine marginals and zero columns';checks+=len(total)
    energy=sum((b-a)**2/h for a,b in zip(y,y[1:]));assert energy==F(cert['energy']),'exact Dirichlet energy';assert M<F(23,100),'useful amplitude budget';assert energy<F(401,100),'strict energy4.01 decision';checks+=3
    lower=F(1730979348830867,432645592385000)
    assert energy>=lower,'independent prior dual compatibility';checks+=1
    slack=F(23,100)-M
    return checks,dict(energy_lower=str(lower),energy_upper=str(energy),derivative_error_squared=str(energy-lower),uniform_error_squared=str((energy-lower)/2),smooth_amplitude_slack=str(slack),smooth_phase_uniform_sufficient=str(3*slack/4),energy_margin_to_401_100=str(F(401,100)-energy))

def blend_consumer(cert):
    h=F(cert['h']);n=int(6/h);y=list(map(F,cert['phase_nodes']));old=[]
    def previous(u):
        if u<0:return -previous(-u)
        return -max(F(0),min(u,F(1),(F(23,8)-u)/F(7,8)))
    for i in range(n+1):old.append(previous(-3+i*h))
    Eold=sum((b-a)**2/h for a,b in zip(old,old[1:]));assert Eold==F(30,7),'inherited phase energy'
    cross=sum((y[i+1]-y[i])*(old[i+1]-old[i])/h for i in range(n))
    Mold=F(472,2071);Mnew=F(cert['amplitude']);Enew=F(cert['energy']);rows=[]
    for budget in [F(229,1000),F(2295,10000)]:
        theta=(budget-Mold)/(Mnew-Mold);assert 0<theta<1,'blend range'
        energy=(1-theta)**2*Eold+2*theta*(1-theta)*cross+theta**2*Enew
        vals=[(1-theta)*a+theta*b for a,b in zip(old,y)]
        assert energy==sum((b-a)**2/h for a,b in zip(vals,vals[1:])),'actual blended energy'
        assert (1-theta)*Mold+theta*Mnew==budget,'amplitude convexity budget'
        rows.append(dict(amplitude_budget=str(budget),theta=str(theta),energy_upper=str(energy)))
    return dict(previous_certificate='lab/process/k1940-joint-scalar-amplitude-energy-cuts.json',previous_sha256=hashlib.sha256((ROOT/'lab/process/k1940-joint-scalar-amplitude-energy-cuts.json').read_bytes()).hexdigest(),cross_energy=str(cross),budgets=rows)

def calculate(discover_new=False):
    cert=discover() if discover_new else json.loads(REPORT.read_text())['pulse'];checks,gap=verify(cert)
    return dict(claim='K1944',evidence_kind='exact rational continuum pulse, polynomial energy and inherited dual bound; floating discovery is not proof',exact_controls=checks,pulse=cert,consumers=gap,blend=blend_consumer(cert),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();r=calculate(args.write)
    if args.write:REPORT.write_text(json.dumps(r,indent=2)+'\n')
    print('PASS',r['exact_controls'],'exact controls');print(r['consumers']);print('M',r['pulse']['amplitude'])
