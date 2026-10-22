"""Rational primal/dual certificates; floating LP is discovery, never acceptance."""
from fractions import Fraction as F
from pathlib import Path
from collections import deque
import argparse,hashlib,json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix,vstack,hstack,eye
ROOT=Path(__file__).resolve().parents[2];REPORT=ROOT/'lab/process/k1938-certified-finite-duration-scalar-control.json'
L=F(3);C=F(1)
def phi(u):
    if u<0:return -phi(-u)
    return -max(F(0),min(u,F(1),3-u))
def area(u0,u1,z0,z1,d):
    def below(q):
        return (max(F(0),u1+q-z0)**2-max(F(0),u0+q-z0)**2-max(F(0),u1+q-z1)**2+max(F(0),u0+q-z1)**2)/2
    return below(d)-below(F(0))
def grid(T,h,inner=False):
    d=2*C*T;n=int(2*L/h);m=int((2*L+d)/h)
    assert n*h==2*L and m*h==2*L+d and F(1)/h==int(1/h)
    us=[-L+i*h for i in range(n+1)];zs=[-L+i*h for i in range(m+1)]
    b=[h*(phi(us[i])+phi(us[i+1]))/2 for i in range(n)];assert sum(b)==0
    edges=[]
    for i in range(n):
      for j in range(m):
        a=area(us[i],us[i+1],zs[j],zs[j+1],d)
        if a>0 and (not inner or (zs[j]>=us[i+1] and zs[j+1]<=us[i]+d)):edges.append((i,n+j,a))
    return n,m,b,edges

def solve(T,h,inner=False):
    n,m,b,edges=grid(T,h,inner);nv=n+m;ne=len(edges)
    rows=[];cols=[];data=[]
    for k,(i,j,a) in enumerate(edges):rows.extend([i,j]);cols.extend([k,k]);data.extend([1,1])
    eq=coo_matrix((data,(rows,cols)),shape=(nv,ne)).tocsr();caps=np.array([float(e[2]) for e in edges]);zero=coo_matrix((nv,1));eq=hstack([eq,zero]).tocsr()
    ub=vstack([hstack([eye(ne),-caps[:,None]]),hstack([-eye(ne),-caps[:,None]])]).tocsr();obj=np.zeros(ne+1);obj[-1]=1
    rhs=np.array(list(map(float,b))+[0.]*m)
    res=linprog(obj,A_ub=ub,b_ub=np.zeros(2*ne),A_eq=eq,b_eq=rhs,bounds=[(None,None)]*ne+[(0,None)],method='highs')
    assert res.success,res.message
    y=[F(float(z)).limit_denominator(10**6) for z in res.eqlin.marginals]
    den=sum(a*abs(y[i]+y[j]) for i,j,a in edges);num=sum(b[i]*y[i] for i in range(n));lower=num/den
    if not inner:return {'T':str(T),'h':str(h),'dual':list(map(str,y)),'m_lower':str(lower)}
    x=[F(float(z)).limit_denominator(10**7) for z in res.x[:-1]]
    # Repair rounded rational flows exactly on a spanning forest.
    residual=b+[F(0)]*m
    adj=[[] for _ in range(nv)]
    for k,(i,j,a) in enumerate(edges):residual[i]-=x[k];residual[j]-=x[k];adj[i].append((j,k));adj[j].append((i,k))
    seen=set()
    for root in range(nv):
        if root in seen:continue
        seen.add(root);order=[root];parent={}
        for v in order:
            for u,k in adj[v]:
                if u not in seen:seen.add(u);parent[u]=(v,k);order.append(u)
        for u in reversed(order[1:]):
            v,k=parent[u];delta=residual[u];x[k]+=delta;residual[v]-=delta;residual[u]=0
        assert residual[root]==0,'exact flow repair compatibility'
    upper=max(abs(w)/a for w,(_,_,a) in zip(x,edges))
    # Each cell lies in one linear segment: exact residual ||r||=h/2, ||int r||=h^2/8.
    correction=h*h/(4*C*T*T)+h/T
    cert={'T':str(T),'h':str(h),'flows':[str(w) for w in x],'m_inner':str(upper),'correction_M':str(correction),'M_upper':str(2*C*upper+correction),'inner_dual':list(map(str,y)),'m_inner_lower':str(lower)}
    verify_inner(cert)
    return cert

def verify_inner(cert,fault=None):
    T,h=F(cert['T']),F(cert['h']);n,m,b,edges=grid(T,h,True);x=list(map(F,cert['flows']));bound=F(cert['m_inner'])
    if fault=='flow':x[len(x)//2]+=F(1,100)
    totals=[F(0)]*(n+m)
    for w,(i,j,a) in zip(x,edges):
        assert abs(w)<=bound*a,'pointwise pulse capacity';totals[i]+=w;totals[j]+=w
    assert totals==b+[F(0)]*m,'exact two marginals'
    assert F(cert['correction_M'])==h*h/(4*C*T*T)+h/T,'endpoint residual correction'
    assert F(cert['M_upper'])==2*C*bound+F(cert['correction_M']),'physical Jacobian'
    return len(x)+n+m+2

def verify_outer(cert,fault=None):
    T,h=F(cert['T']),F(cert['h']);n,m,b,edges=grid(T,h,False);y=list(map(F,cert['dual']))
    if fault=='capacity':edges=[(i,j,a*2) for i,j,a in edges]
    den=sum(a*abs(y[i]+y[j]) for i,j,a in edges);num=sum(b[i]*y[i] for i in range(n))
    assert den>0 and num/den==F(cert['m_lower']),'continuum dual bound'
    return len(edges)+2

def calculate():
    records=[];count=0
    for T in [F(1,2),F(1),F(3,2),F(3),F(9,2)]:
      for h in ([F(1,2),F(1,4),F(1,8),F(1,16)] if T==F(9,2) else [F(1,2),F(1,4),F(1,8)]):
        if 2*T<=2*h:continue
        outer=solve(T,h);inner=solve(T,h,True);count+=verify_outer(outer)+verify_inner(inner)
        low=2*C*F(outer['m_lower']);upper=F(inner['M_upper']);assert low<=upper
        records.append({'T':str(T),'h':str(h),'M_lower':str(low),'M_upper':str(upper),'outer':outer,'inner':inner})
    return {'claim':'K1938','evidence_kind':'floating LP discovers, rational flows and dual potentials rigorously certify continuum enclosures; analytic convergence proof in note','exact_controls':count,'profile':{'L':'3','a':'1','b':'2','c':'1','plateau_magnitude':'1','gradient_energy':'4'},'records':records,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=calculate()
    if a.write:REPORT.write_text(json.dumps(r,indent=2)+'\n')
    for v in r['records']:print(v['T'],v['h'],v['M_lower'],v['M_upper'],float(F(v['M_upper'])-F(v['M_lower'])))
    print('PASS',r['exact_controls'],'rational controls')
