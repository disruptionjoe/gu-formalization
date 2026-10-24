"""Rational error-budget consumers; no sampled residual is a continuum norm."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
from k1989_capped_pulse_dual_certificates import geometry,certify
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2009-robust-tight-cut-pulse-certificates.json';M=F(23,100)

def psi(z,c):return z*z if abs(z)<=c else 2*c*abs(z)-c*c

def finite_cut(w,v,cut,M,eps):
    C=M+eps;K=F(0);cut_integral=F(0);Hcol=F(0);slack=F(0);l1=F(0);eta=F(0)
    for j in range(len(w[0])):
        ell=sum(w[i][j] for i in range(len(w)));m=sum(w[i][j] for i in cut)
        column=sum(w[i][j]*v[i][j] for i in range(len(w)));eta+=abs(column)
        cut_integral+=sum(w[i][j]*v[i][j] for i in cut);K+=min(m,ell-m)
        chosen=cut if 2*m<=ell else set(range(len(w)))-cut;sgn=1 if 2*m<=ell else -1
        if sgn==-1:Hcol+=column
        for i in chosen:
            assert abs(v[i][j])<=C
            slack+=w[i][j]*(C-sgn*v[i][j]);l1+=w[i][j]*abs(v[i][j]-sgn*M)
    rho=cut_integral-M*K
    assert slack==eps*K-rho+Hcol and slack>=0
    bound=2*eps*K+abs(rho)+eta;assert l1<=bound
    return dict(K=K,rho=rho,column_error=eta,slack=slack,Hcol=Hcol,l1=l1,bound=bound)

def produce():
    controls=[];pointwise=0
    for seed in range(12):
      w=[[F((i+2*j+seed)%4+1,7) for j in range(5)] for i in range(4)]
      for eps in (F(0),F(1,100)):
        C=M+eps;v=[[C*F((3*i+j+seed)%9-4,4) for j in range(5)] for i in range(4)]
        for cut in ({0},{0,1},{0,1,2}):
          result=finite_cut(w,v,cut,M,eps)
          controls.append(dict(seed=seed,epsilon=eps,cut=sorted(cut),**result))
    for c in (M,M+F(1,100)):
      for z in (F(-2),-c,-c/2,F(0),c/2,c,F(2)):
        for k in range(-8,9):
          v=c*F(k,8);wc=max(-c,min(c,z))
          assert (v-wc)**2<=v*v-2*z*v+psi(z,c)
          assert 0<=psi(z,c)-psi(z,M)<=2*(c-M)*max(abs(z)-M,0)
          pointwise+=1
    prev=json.loads((ROOT/'lab/process/k1989-capped-pulse-dual-certificates.json').read_text());old=prev['certificate'];a=list(map(F,old['row_potentials']));b=list(map(F,old['column_potentials']))
    assert certify(a,b)==old
    _,_,areas,_=geometry(len(a));A=max(map(abs,a));B=max(map(abs,b));T=sum((areas[i][j]*max(abs(x+y)-M,0) for i,x in enumerate(a) for j,y in enumerate(b)),F(0));D=F(old['squared_norm_lower_bound'])
    tl,tr=map(F,prev['root_interval']);Klo=18-3*tr-tr*tr;Khi=18-3*tl-tl*tl
    budgets=[]
    for eps,er,ec in ((F(0),F(0),F(0)),(F(1,10**6),F(1,10**6),F(1,10**6)),(F(1,10**4),F(1,1000),F(1,1000))):
      penalty=2*A*er+2*B*ec+2*eps*T;Q=4*eps*Khi+2*er+2*ec
      budgets.append(dict(epsilon=eps,row_error=er,column_error=ec,norm_lower=D-penalty,dual_penalty=penalty,forced_L1_upper=Q,forced_L2_squared_upper=(2*M+eps)*Q,regional_row_L1_upper=er+Q,regional_column_L1_upper=ec+Q))
    inputs=['lab/process/k1989-capped-pulse-dual-certificates.json','tests/channel-swings/k1989_capped_pulse_dual_certificates.py','explorations/conditional-build/k1991-tight-cut-pulse-factorization-2026-10-23.md','explorations/conditional-build/k2007-analytic-wing-projection-2026-10-24.md']
    return dict(result_id='K2009',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',cut_controls=controls,pointwise_controls=pointwise,actual_witness=dict(A=A,B=B,T=T,D_low=D,area=sum(map(sum,areas)),K_interval=[Klo,Khi]),actual_error_budgets=budgets,scope='Rigorous continuum error implications when actual L1 marginal and cap bounds are certified; not a feasible pulse, nonlinear repair or new optimized norm bound.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})

def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,list):return [encode(v) for v in x]
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    return x
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();d=encode(produce())
    if args.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
    else:assert d==json.loads(OUT.read_text())
    print('PASS K2009',len(d['cut_controls']),'cut controls;',d['pointwise_controls'],'pointwise controls;',len(d['actual_error_budgets']),'actual error budgets')
    print('Certified conditional lower at 1e-6 errors:',float(F(d['actual_error_budgets'][1]['norm_lower'])))
