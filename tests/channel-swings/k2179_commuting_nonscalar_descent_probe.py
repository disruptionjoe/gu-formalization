#!/usr/bin/env python3
"""Exact commuting nonscalar descent, faithful multiplicity and original-row controls."""
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as F
import sympy as S
from k2177_exceptional_spectrum_descent_probe import tang,rev
from k2173_general_mixed_port_constraints_probe import grade,scalar
from k2171_mixed_port_euler_filter_probe import G,I,ETA,W,N,OM,mm,add,scale,blade,port,inv,bar,comm,neg,kernel,C,RR,K,filt
from pathlib import Path
import argparse,json,hashlib
ROOT=Path(__file__).resolve().parents[2]

def trace_certificate():
    out={}
    X=[[F(-2,5),F(6,5)],[F(0),F(0)]];Y=[[F(0),F(0)],[F(-17,9),F(3)]]
    for k,Z,den in [(2,[[F(-169,384),F(243,384)],[F(7,384),F(99,384)]],30720),(-6,[[F(-1,2),F(81,70)],[F(-1,2),F(-3,14)]],960)]:
        rows=[];dets=[]
        for m in range(33):
            for n in range(33-m):
                mat=[[F(i==j)-(m*X[i][j]+n*Y[i][j]+(32-m-n)*Z[i][j])/32 for j in range(2)] for i in range(2)]
                d=mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
                num=32*m*n+329*m-2935*n+32480 if k==2 else m*n-30*m-132*n+2304
                assert d==F(num,den) and d!=0
                rows.append([m,n,num]);dets.append(abs(d))
        out[str(k)]=dict(count=len(rows),minimum_absolute_determinant=str(min(dets)),zero_pairs=[],integer_numerator_rows=rows)
    return out

def fixtures():
    ix=lambda a:blade([N[i-1] for i in a]);vol=blade(N)
    return [('grade4',add(ix([1,2,3,4,5,6,7]),scale(ix([1,2,3,4,5,8,9]),F(2,3))),ix([1,2,3]),4),
            ('grade8',mm(vol,add(ix([1,2,3]),scale(ix([1,4,5]),F(2,3)))),ix([1,2,4]),8),
            ('mixed',mm(vol,ix([1,2,3])),add(ix([1,2,4]),scale(ix([5,6,7]),F(1,3)),scale(ix([5,8,9]),F(1,5))),None)]

def controls(fault=None):
    out={};ck=lambda n,v:out.__setitem__(n,bool(v))
    a,c,V,T,m,n=S.symbols('a c V T m n');X=S.Matrix([[S.Rational(-2,5),S.Rational(6,5)],[0,0]]);Y=S.Matrix([[0,0],[S.Rational(-17,9),3]])
    for k in [2,-6]:
        kk=-k if fault=='grade_weight' else k
        eq=[10*V+(16+3*kk)*T+4*a-12*c,(142+7*kk)*V+36*T+(69 if fault=='linear_coefficient' else 68)*a-108*c]
        sol=S.solve(eq,(V,T));Z=S.Matrix([[S.diff(sol[v],q) for q in [a,c]] for v in [V,T]])
        size=31 if fault=='trace_dimension' else 32
        det=S.factor((S.eye(2)-(m*X+n*Y+(size-m-n)*Z)/size).det())
        expected=(32*m*n+329*m-2935*n+32480)/30720 if k==2 else (m*n-30*m-132*n+2304)/960
        ck(f'trace_determinant_{k}',S.cancel(det-expected)==0)
        ck(f'nilpotent_branch_{k}',all(sol[q].subs({a:0,c:0})==0 for q in [V,T]))
    num=32*m*n+329*m-2935*n+32480
    ck('mod32_coefficient',all(int(num.subs({m:i,n:j})-9*(i+j))%32==0 for i in range(33) for j in range(33-i)))
    ck('edge_quadratic',S.expand(num.subs(n,32-m))==-32*(m*m-134*m+1920))
    ck('nonsquare_discriminant',134**2-4*1920==4*2569 and 50**2<2569<51**2)
    ck('divisor_factor',S.expand((132-m)*(30-n)-1656)==m*n-30*m-132*n+2304)
    ck('divisor_gap',1656==23*72 and not any(1656%d==0 for d in range(100,133)))
    # Real weights solve the relaxation, but are not valid 32-dimensional multiplicities.
    ck('continuous_weight_countercontrol',F(6,11)*F(46,3)+F(5,11)*(-3)==7 and F(5,11)*F(33,5)==3 and F(32*6,11).denominator!=1)
    for label,v,u,hom in fixtures():
        t=mm(OM,u);h=mm(v,t);U=K(h);vs=mm(v,v);tsq=mm(t,t);av=scalar(vs);cv=scalar(tsq)
        ck(label+'_commuting',not comm(v,t))
        ck(label+'_nonscalar_square',bool(add(vs,scale(I,-av))) or bool(add(tsq,scale(I,-cv))))
        ck(label+'_homogeneous_applicability',({d for d in [4,8] if grade(h,d)}=={hom}) if hom else bool(grade(h,4)) and bool(grade(h,8)))
        FF=add(scale(vs,10),scale(tsq,16),scale(I,4*av-12*cv));GG=add(scale(vs,142),scale(tsq,36),scale(I,68*av-108*cv))
        q0=add(mm(FF,v),scale(mm(U,t),3));q4=add(mm(GG,t),scale(mm(U,v),7))
        rr,pp,fl,aa,bb,ww=filt(v,u);ss=add(scale(v,7),scale(t,9));pol=add(mm(aa,ss),neg(mm(bb,pp)))
        ck(label+'_pencil_invertible',mm(pp,inv(pp))==I)
        ck(label+'_ordered_polynomial_tangent0',tang(pol,0)==scale(q0,-504))
        ck(label+'_ordered_polynomial_tangent4',tang(pol,4)==scale(q4,72))
        ru=neg(rev(U)) if fault=='reversion_sign' else rev(U)
        rq0=add(mm(rev(v),rev(FF)),scale(mm(rev(t),ru),3))
        rq4=add(mm(rev(t),rev(GG)),scale(mm(rev(v),ru),7))
        ck(label+'_centrality_t_residual',add(q0,rq0)==scale(comm(U,t),3))
        ck(label+'_centrality_v_residual',add(q4,rq4)==scale(comm(U,v),7))
        square=add(scale(mm(vs,vs),35),scale(mm(vs,tsq),-156 if fault=='square_coefficient' else -157),scale(mm(tsq,tsq),-54),scale(vs,14*av-42*cv),scale(tsq,-102*av+162*cv))
        ck(label+'_square_filter_transfer',add(scale(mm(q0,v),7),scale(mm(q4,t),-3))==scale(square,2))
        if hom:
            ck(label+'_K_h_weight',U==scale(h,2 if hom==4 else -6))
        else:
            ck('mixed_centrality_not_automatic',bool(comm(U,t)) and not comm(U,v))
        # Original equations are independently constructed, not substituted polynomial assertions.
        adapters={j:scale(mm(inv(pp),port(rr)[j]),-ETA[j]) for j in N};z=add(v,t)
        qs={j:RR(adapters,*C(port(z),*kernel(adapters,j)))[1] for j in N}
        contraction=add(*(scale(mm(qs[j],G[j]),ETA[j] if fault=='row_contraction' else 1) for j in N))
        ck(label+'_original10_Euler',scale(mm(bar(pp),contraction),6)==fl)
        ck(label+'_original10_rejects',bool(q0) or bool(q4))
        ck(label+'_original_rows_nonzero',any(qs.values()))
    # Released polynomial consequence with commuting abstract variables, before any spectral sampling.
    vv,tt,uu,ff,gg=S.symbols('v t U F G');r0=ff*vv+3*uu*tt;r4=gg*tt+7*uu*vv
    ck('eliminate_v',S.expand(gg*r0-3*uu*r4)==S.expand((ff*gg-21*uu**2)*vv))
    ck('eliminate_t',S.expand(ff*r4-7*uu*r0)==S.expand((ff*gg-21*uu**2)*tt))
    return out

FAULTS=['grade_weight','linear_coefficient','trace_dimension','reversion_sign','square_coefficient','row_contraction']
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    cs=controls();assert all(cs.values()),[n for n,v in cs.items() if not v]
    faults={}
    for f in FAULTS:
        bad=[n for n,v in controls(f).items() if not v];assert bad,('undetected',f);faults[f]=bad
    deps=['explorations/conditional-build/k2179-commuting-nonscalar-descent-2026-10-28.md','tests/channel-swings/k2177_exceptional_spectrum_descent_probe.py','tests/channel-swings/k2171_mixed_port_euler_filter_probe.py','tests/channel-swings/k2169_invertible_pencil_full_descent_probe.py','explorations/conditional-build/k2177-exceptional-spectrum-descent-2026-10-28.md']
    report=dict(result_id='K2179',status='conditional_exact_controls',checks=cs,fault_failures=faults,certificate=trace_certificate(),dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Independent reconstruction of real-grade, reversion, trace and arithmetic proof; exhaustive1122 multiplicity controls and actual original ten-row fixtures. No proof-assistant or physical quotient claim.')
    dst=ROOT/'lab/process/k2179-commuting-nonscalar-descent.json'
    if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dst.read_text())==report
    print(json.dumps(dict(result='K2179',checks=len(cs),census_rows=1122,faults=faults)))
if __name__=='__main__':main()
