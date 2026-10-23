"""Full symmetric-jet symbol, exact cokernel and constructive first-jet witness."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
from collections import defaultdict,deque
from k1976_general_pairing_transport import setup,enc
from k1970_weighted_adjoint_mass_completion_probe import plus,product,transpose
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1979-multicoordinate-symmetric-pairing.json';N=128

def right(Q,J,T,O,sign):
    A={}
    for k in range(14):A=plus(A,product(product(transpose(O[k]),Q),J[k]),F(1 if k<7 else -1))
    return plus(A,product(Q,T),-sign)

def symbol_graph(J):
    edges=[];adj=[[] for _ in range(N*N)]
    for k in range(14):
        rows={i:(j,v) for (i,j),v in J[k].items()};eta=1 if k<7 else -1
        for i in range(N):
            a,va=rows[i]
            for j in range(i+1):
                b,vb=rows[j]
                edge=[(N*i+b,eta*vb)] if i==j else [(N*i+b,eta*vb),(N*j+a,eta*va)]
                idx=len(edges);edges.append((k,i,j,edge))
                for v,_ in edge:adj[v].append(idx)
    return edges,adj

def solve_graph(J,rhs):
    edges,adj=symbol_graph(J);seen=set();sol=defaultdict(F);cokernel=[];components=[]
    for root in range(N*N):
        if root in seen:continue
        seen.add(root);nodes=[root];parent={};dual={root:F(1)};q=deque([root])
        while q:
            u=q.popleft()
            for ei in adj[u]:
                e=edges[ei][3]
                for v,b in e:
                    if v not in seen:
                        a=next(c for z,c in e if z==u);dual[v]=-dual[u]*a/b
                        parent[v]=(u,ei,b);seen.add(v);nodes.append(v);q.append(v)
        dot=sum(dual[u]*rhs.get(u,F(0)) for u in nodes)
        pivot=None;pd=F(0)
        for u in nodes:
            for ei in adj[u]:
                z=sum(dual[v]*c for v,c in edges[ei][3])
                if z:pivot=ei;pd=z;break
            if pivot is not None:break
        residual={u:rhs.get(u,F(0)) for u in nodes}
        if pivot is None:
            assert dot==0,'first-jet compatibility'
            cokernel.append({(u//N,u%N):dual[u] for u in nodes})
        else:
            sol[pivot]+=dot/pd
            for u,a in edges[pivot][3]:residual[u]-=a*dot/pd
        for v in reversed(nodes[1:]):
            u,ei,b=parent[v];x=residual[v]/b;sol[ei]+=x
            a=next(c for z,c in edges[ei][3] if z==u);residual[u]-=a*x
        assert residual[root]==0
        components.append([len(nodes),pivot is not None])
    H=[{} for _ in range(14)]
    for ei,x in sol.items():
        if x:
            k,i,j,_=edges[ei];H[k][i,j]=H[k].get((i,j),F(0))+x
            if i!=j:H[k][j,i]=H[k].get((j,i),F(0))+x
    return H,cokernel,components

def reduce_rows(rows):
    piv={}
    for row in rows:
        d={i:v for i,v in enumerate(row) if v}
        while d:
            i=min(d)
            if i not in piv:
                a=d[i];piv[i]={j:v/a for j,v in d.items()};break
            a=d[i]
            for j,v in piv[i].items():
                d[j]=d.get(j,F(0))-a*v
                if not d[j]:d.pop(j,None)
    return piv

def produce():
    I,V,J,T,inv,O=setup();out=[]
    S={ij:F(1) for ij in product(right(I,J,T,O,-1),inv)};basis=[I,V,S]
    for sign in [-1,1]:
        R=right(I,J,T,O,sign);H,Z,components=solve_graph(J,{i*N+j:v for (i,j),v in R.items()})
        lhs={}
        for k,h in enumerate(H):
            assert h==transpose(h)
            lhs=plus(lhs,product(h,J[k]),F(1 if k<7 else -1))
        assert lhs==R and len(Z)==2
        for z in Z:
            for j in J[:14]:assert not plus(product(z,transpose(j)),transpose(product(z,transpose(j))))
        # Pointwise restrictions in the earlier four-dimensional reducing algebra.
        cols=[{ij:(1 if k<7 else -1)*v for ij,v in product(b,J[k]).items()} for k in range(14) for b in basis]
        rcols=[right(b,J,T,O,sign) for b in basis]
        keys=set().union(*(set(c) for c in cols+rcols));rows=[[c.get(ij,F(0)) for c in cols]+[-c.get(ij,F(0)) for c in rcols] for ij in keys]
        B=reduce_rows([r[:42] for r in rows]);aug=reduce_rows(rows);assert len(B)==42 and len(aug)==43
        constraint=next(r for i,r in aug.items() if i>=42)
        assert set(constraint)=={42,43}
        ratio=-constraint[43]/constraint[42];assert abs(ratio)<1
        solutions=[]
        for free in [43,44]:
            x=[F(0)]*45;x[free]=F(1)
            for pivot,row in sorted(aug.items(),reverse=True):x[pivot]=-sum(v*x[j] for j,v in row.items() if j!=pivot)
            assert all(sum(a*b for a,b in zip(row,x))==0 for row in rows)
            assert not any(x[3:42]);solutions.append(x)
        assert solutions[0][2] and solutions[1][0]-ratio*solutions[1][1]
        # Constraint derivative forces c=0; its derivative then forces b=a=0.

        # Constant affine use of these jets is NOT a solution: nonzero linear defects.
        defects=[right(h,J,T,O,sign) for h in H];assert any(defects)
        jet_bound=sum(max([sum(abs(v) for (r,c),v in h.items() if r==i) for i in range(N)]) for h in H)
        out.append(dict(positive_affine_cube_radius=str(1/(2*jet_bound)),sign=sign,symbol_rank=N*N-len(Z),symmetric_unknowns=14*N*(N+1)//2,cokernel=[enc(z) for z in Z],components=components,identity_first_jets=[enc(h) for h in H],affine_defect_nonzero_coordinates=[k for k,d in enumerate(defects) if d],reduced_symbol_rank=len(B),reduced_augmented_rank=len(aug),reduced_a_over_b=str(ratio),reduced_jet_solutions=[[str(x) for x in v] for v in solutions]))
    return dict(result_id='K1979',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',families=out,scope='Complete symmetric first-jet symbol and identity-value compatibility; no integrated positive pairing field or source adjoint. The old symmetric three-basis family cannot be definite even with all14 coordinates.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['tests/channel-swings/k1976_general_pairing_transport.py','lab/process/k1967-paired-raw-coefficient-observation.json','tests/channel-swings/k1973_differential_adjoint_density.py']})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=produce()
    if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert r==json.loads(OUT.read_text())
    print('PASS K1979',[(f['sign'],f['symbol_rank'],f['reduced_a_over_b']) for f in r['families']])
