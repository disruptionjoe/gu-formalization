"""Exact finite-union controls for an effective continuum-cut transfer theorem."""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json
from k1942_complete_scalar_energy_duality import union_capacity,green,active_solve
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1963-effective-scalar-cut-certificates.json'

def phi0_integral(a,b):
    knots=sorted({a,b}|{x for x in map(F,[-3,-2,-1,1,2,3]) if a<x<b})
    def phi(x):
        if x<0:return -phi(-x)
        return -min(x,F(1),3-x)
    return sum((r-l)*(phi(l)+phi(r))/2 for l,r in zip(knots,knots[1:]))

def intervals(mask,h):
    return [(-3+i*h,-3+(i+1)*h) for i in range(int(6/h)) if mask>>i&1]

def weighted_capacity(parts):
    """Parts are (left,right,density), with disjoint intervals and 0<=density<=1."""
    knots=sorted({F(-3),F(3),F(6),F(12)}|{x+d for l,r,w in parts for x in (l,r) for d in (0,9)})
    def val(z):
        a=sum(w*max(F(0),min(r,z)-max(l,z-9)) for l,r,w in parts)
        ell=max(F(0),min(F(3),z)-max(F(-3),z-9))
        return a,ell-a
    total=F(0)
    for l,r in zip(knots,knots[1:]):
        a,b=val(l);c,d=val(r);pts=[l,r]
        if (a-b)*(c-d)<0:pts.insert(1,l+(r-l)*(a-b)/(a-b-c+d))
        for x,y in zip(pts,pts[1:]):total+=(y-x)*(min(val(x))+min(val(y)))/2
    return total

def graph_certificate(h,phase_integrals,fault=None):
    """Integer max-flow/min-cut certificate for every grid-union inequality."""
    import math
    from collections import deque
    M=F(23,100);N=int(6/h);zs=[-3+j*h for j in range(int(15/h)+1)]
    arcs=[];source=N+len(zs);sink=source+1;nv=sink+1
    for i,b in enumerate(phase_integrals):
        if b>0:arcs.append((source,i,b))
        if b<0:arcs.append((i,sink,-b))
    for j,z in enumerate(zs):
        weight=h/2 if j in (0,len(zs)-1) else h
        if fault=='quadrature':weight*=F(3,4)
        for i in range(N):
            length=max(F(0),min(-3+(i+1)*h,z)-max(-3+i*h,z-9))
            cap=M*weight*length/2
            if cap:arcs.extend([(i,N+j,cap),(N+j,i,cap)])
    den=math.lcm(*(c.denominator for _,_,c in arcs));edges=[];adj=[[] for _ in range(nv)]
    for u,v,c in arcs:
        k=len(edges);cap=int(c*den);edges.extend([[v,cap,cap],[u,0,0]]);adj[u].append(k);adj[v].append(k+1)
    flow=0
    while True:
        level=[-1]*nv;level[source]=0;q=deque([source])
        while q:
            u=q.popleft()
            for k in adj[u]:
                v,cap,_=edges[k]
                if cap and level[v]<0:level[v]=level[u]+1;q.append(v)
        if level[sink]<0:break
        it=[0]*nv
        def send(u,f):
            if u==sink:return f
            while it[u]<len(adj[u]):
                k=adj[u][it[u]];v,cap,_=edges[k]
                if cap and level[v]==level[u]+1:
                    z=send(v,min(f,cap))
                    if z:edges[k][1]-=z;edges[k^1][1]+=z;return z
                it[u]+=1
            return 0
        while True:
            f=send(source,sum(int(c*den) for u,v,c in arcs if u==source))
            if not f:break
            flow+=f
    reached={source};q=deque([source])
    while q:
        u=q.popleft()
        for k in adj[u]:
            v,cap,_=edges[k]
            if cap and v not in reached:reached.add(v);q.append(v)
    assert sink not in reached
    balance=[0]*nv;cutcap=0
    for a,(u,v,c) in enumerate(arcs):
        sent=edges[2*a][2]-edges[2*a][1];cap=int(c*den)
        assert 0<=sent<=cap,'exact primal capacity'
        balance[u]-=sent;balance[v]+=sent
        if u in reached and v not in reached:cutcap+=cap
    assert all(b==0 for i,b in enumerate(balance) if i not in [source,sink]),'flow conservation'
    assert balance[sink]==flow==-balance[source]==cutcap,'exact flow/cut equality'
    value=F(flow,den)-sum(max(F(0),b) for b in phase_integrals)
    chosen=[i for i in range(N) if i in reached]
    actual=M*union_capacity([(-3+i*h,-3+(i+1)*h) for i in chosen])/2-sum(phase_integrals[i] for i in chosen)
    assert value==actual,'graph agrees with analytic continuum capacity'
    return dict(h=str(h),nodes=nv,directed_arcs=len(arcs),minimum_deficit=str(value),chosen_cells=chosen)

def calculate():
    h=F(1,2);M=F(23,100);cuts=[-h,h]
    _,_,lam,J=active_solve(cuts,M);lam=list(map(F,lam));J=F(J)
    checks=0;worst=F(0)
    for mask in range(1<<12):
        ab=intervals(mask,h);C=union_capacity(ab)
        integral=sum(phi0_integral(a,b)-sum(x*(green(b,s)-green(a,s)) for x,s in zip(lam,cuts)) for a,b in ab)
        assert abs(integral)<=M*C/2,'ALL grid unions, not halfcuts only';checks+=1
        worst=max(worst,abs(integral)-M*C/2)
    graph=[]
    for hh in [F(1),F(1,2),F(1,4),F(1,16)]:
        ss=F(7,16) if hh==F(1,16) else F(1,2)
        _,_,ll,jj=active_solve([-ss,ss],M);ll=list(map(F,ll))
        vals=[phi0_integral(-3+i*hh,-3+(i+1)*hh)-sum(v*(green(-3+(i+1)*hh,t)-green(-3+i*hh,t)) for v,t in zip(ll,[-ss,ss])) for i in range(int(6/hh))]
        g=graph_certificate(hh,vals);g['phase_energy']=str(jj);g['active_halfcut']=str(ss);graph.append(g)
        assert F(g['minimum_deficit'])==0,'candidate passes ALL unions via exact mincut';checks+=1
    bad=graph_certificate(F(1,2),[phi0_integral(-3+i*h,-3+(i+1)*h) for i in range(12)])
    assert F(bad['minimum_deficit'])<0,'baseline phase genuinely violates a cut';checks+=1
    # Fractional-cell arrangements: exact sliding-window capacity and layer cake.
    controls=[]
    for k in range(1,16):
        parts=[];averages=[]
        for i in range(6):
            l=F(-3+i);w=F((k*(i+1))%7,7)
            if w:parts.append((l,l+w,F(1)))
            averages.append((l,l+1,w))
        C=weighted_capacity(parts);Ca=weighted_capacity(averages);mass=sum((r-l)*w for l,r,w in parts);small=min(mass,6-mass)
        assert abs(C-Ca)<=2*small,'transport capacity bound'
        levels=sorted({F(0),F(1)}|{w for _,_,w in averages});cake=F(0)
        for x,y in zip(levels,levels[1:]):cake+=(y-x)*union_capacity([(l,r) for l,r,w in averages if w>(x+y)/2])
        assert cake<=Ca,'capacity concavity direction'
        assert C>=3*small,'central rectangle lower capacity';checks+=3
        controls.append(dict(k=k,capacity=str(C),averaged_capacity=str(Ca),layer_cake=str(cake),mass=str(mass)))
    # An actual within-cell capacity change prevents setting the transport error to zero.
    assert any(c['capacity']!=c['averaged_capacity'] for c in controls)
    cert=json.loads((ROOT/'lab/process/k1944-optimized-scalar-pulse-certificate.json').read_text())
    # Read exact predecessor fields without repeating its large unchanged flow replay.
    return dict(result_id='K1963',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_controls=checks+1,graph_certificates=graph,baseline_violated_cut=bad,grid=dict(h=str(h),M=str(M),cuts=list(map(str,cuts)),multipliers=list(map(str,lam)),energy=str(J),union_count=4096),fractional_controls=controls,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1942-complete-scalar-energy-duality.json','lab/process/k1944-optimized-scalar-pulse-certificate.json']},scope='Finite ALL-grid-union certificate plus proved amplitude inflation and strict-slack energy convergence; no exact optimum or practical complexity claim.')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=calculate()
    if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert r==json.loads(OUT.read_text()),'report equality'
    print('PASS K1963',r['exact_controls'],r['grid'],flush=True)
