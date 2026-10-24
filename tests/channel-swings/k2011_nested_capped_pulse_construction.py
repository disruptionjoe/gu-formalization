"""Finite exact-cell pulse hierarchy; floating search proposes rational dual witnesses."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
from k1989_capped_pulse_dual_certificates import geometry,clip,star
from k1983_certified_continuum_pulse_evaluation import DG,M,TL,TR,PIECES
from math import isqrt
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2011-nested-capped-pulse-construction.json'

def search(n):
    import numpy as np
    from scipy.optimize import minimize
    _,_,A,G=geometry(n);a=np.array(A,dtype=float);g=np.array(G,dtype=float);m=float(M);nz=a.shape[1]
    def fg(x):
        z=x[:n,None]+x[None,n:];v=np.clip(z,-m,m)
        penalty=np.where(abs(z)<=m,z*z/2,m*abs(z)-m*m/2)
        return float((a*penalty).sum()-x[:n]@g),np.r_[(a*v).sum(axis=1)-g,(a*v).sum(axis=0)]
    r=minimize(fg,np.zeros(n+nz),jac=True,method='L-BFGS-B',options={'maxiter':6000,'ftol':1e-15,'gtol':2e-11,'maxcor':20})
    # Optimizer success is diagnostic only. Every rational witness is certified below.
    q=[F(round(float(v)*10**9),10**9) for v in r.x[:n]];b=[F(round(float(v)*10**9),10**9) for v in r.x[n:]]
    return q,b,dict(success=bool(r.success),iterations=int(r.nit),gradient_max=float(abs(r.jac).max()))

def sqrt_up(x):
    scale=10**12;k=isqrt((x.numerator*scale*scale)//x.denominator)
    while F(k,scale)**2<x:k+=1
    return F(k,scale)

def continuum_squared(u,z,v):
    # Uniform grids used here align both strip edges; marginal functions are affine inside each bin.
    pieces=list(PIECES)+[(-b,-a,[-c[k]*(-1)**k for k in range(len(c))]) for a,b,c in PIECES]
    er=F(0);ec=F(0)
    for i,(a,b) in enumerate(zip(u,u[1:])):
        def row(x):return sum(v[i][j]*max(F(0),min(d,x+9)-max(c,x)) for j,(c,d) in enumerate(zip(z,z[1:])))
        fa,fb=row(a),row(b);slope=(fb-fa)/(b-a);offset=fa-slope*a
        for l,h,c in pieces:
            lo,hi=max(a,l),min(b,h)
            if lo>=hi:continue
            poly=[offset,slope,F(0)]
            for k,val in enumerate(c):poly[k]-=2*val
            sq=[F(0)]*5
            for j,x in enumerate(poly):
                for k,y in enumerate(poly):sq[j+k]+=x*y
            er+=sum(x*(hi**(k+1)-lo**(k+1))/F(k+1) for k,x in enumerate(sq))
    for j,(a,b) in enumerate(zip(z,z[1:])):
        def col(x):return sum(v[i][j]*max(F(0),min(h,x)-max(l,x-9)) for i,(l,h) in enumerate(zip(u,u[1:])))
        fa,fb=col(a),col(b);ec+=(b-a)*(fa*fa+fa*fb+fb*fb)/3
    assert er>=0 and ec>=0
    return er,ec

def certify(q,b):
    n=len(q);u,z,A,G=geometry(n);assert len(b)==len(z)-1
    v=[[clip(x+y) for y in b] for x in q]
    norm=sum(A[i][j]*v[i][j]**2 for i in range(n) for j in range(len(b)))
    dual=2*sum(x*g for x,g in zip(q,G))-2*sum(A[i][j]*star(q[i]+b[j]) for i in range(n) for j in range(len(b)))
    forcing_error=18*DG*sum(abs(q[i])*(u[i+1]-u[i]) for i in range(n))
    lower=dual-forcing_error
    rb=sum(abs(sum(A[i][j]*v[i][j] for j in range(len(b)))-G[i]) for i in range(n))+54*DG
    cb=sum(abs(sum(A[i][j]*v[i][j] for i in range(n))) for j in range(len(b)))
    h=F(6,n);mesh_r=rb+2*h*(2*M+F(21,10));mesh_c=cb+10*M*h
    er,ec=continuum_squared(u,z,v);eta_r=min(mesh_r,sqrt_up(6*er)+54*DG);eta_c=min(mesh_c,sqrt_up(15*ec))
    assert all(abs(x)<=M for row in v for x in row)
    assert lower<=norm+2*max(map(abs,q))*rb+2*max(map(abs,b))*cb
    # General strong-Fenchel distance: exact optimizer need not be approximated by a feasible finite array.
    U=F('2.739952052817663');distance2=U-lower;assert distance2>0
    return dict(rows=n,columns=len(b),row_potentials=list(map(str,q)),column_potentials=list(map(str,b)),dual_surrogate=str(dual),forcing_error=str(forcing_error),norm_lower=str(lower),candidate_norm=str(norm),row_bin_L1=str(rb),column_bin_L1=str(cb),row_continuum_L1_upper=str(eta_r),column_continuum_L1_upper=str(eta_c),distance_to_optimizer_squared_upper=str(distance2),mesh=str(h),row_surrogate_L2_squared=str(er),column_L2_squared=str(ec),mesh_row_bound=str(mesh_r),mesh_column_bound=str(mesh_c))

def produce(witnesses):
    cs=[certify(q,b) for q,b in witnesses]
    inputs=['tests/channel-swings/k1989_capped_pulse_dual_certificates.py','tests/channel-swings/k1983_certified_continuum_pulse_evaluation.py','explorations/conditional-build/k1980-constructive-minimum-norm-pulse-2026-10-23.md','explorations/conditional-build/k2007-analytic-wing-projection-2026-10-24.md']
    return dict(result_id='K2011',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',certificates=cs,root_interval=list(map(str,[TL,TR])),scope='New finite-moment exact-cell QP hierarchy converges strongly by written proof. Executed arrays are rational clipped dual witnesses, not exact finite-QP minimizers or continuum-feasible pulses. Exact areas, algebraic forcing enclosure and mesh residual bounds certify every numerical claim. No novelty or GU identification.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    if args.write:
        ws=[]
        for n in (24,48,96):
            q,b,d=search(n);ws.append((q,b));print('SCOUT',n,d,flush=True)
        out=produce(ws);OUT.write_text(json.dumps(out,indent=2)+'\n')
    else:
        old=json.loads(OUT.read_text());out=produce([(list(map(F,c['row_potentials'])),list(map(F,c['column_potentials']))) for c in old['certificates']]);assert out==old
    for c in out['certificates']:print('PASS K2011',c['rows'],'norm lower',float(F(c['norm_lower'])),'residuals',float(F(c['row_continuum_L1_upper'])),float(F(c['column_continuum_L1_upper'])))
