#!/usr/bin/env python3
"""Commuting Clifford trace descent and exact finite affine spectral filters."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,json,hashlib
import sympy as S
import k2181_mixed_square_pencil_descent_probe as previous
k=previous.k;ROOT=Path(__file__).resolve().parents[2]

def controls(fault=None):
    cs={};ck=lambda n,v:cs.__setitem__(n,bool(v))
    V,T,a,c,z,r,M,m,kk=S.symbols('V T a c z r M m k')
    FF=10*V+16*T+4*a-12*c;GG=142*V+36*T+68*a-108*c
    expr=S.Poly(S.expand((FF*GG-28*FF*V-252*V*T)/4),V,T)
    traced=0
    for (i,j),coef in expr.terms():
        traced+=coef*({(0,0):1,(1,0):a,(0,1):c}.get((i,j),V**i*T**j))
    target=285*V**2+(482 if fault=='trace_cross' else 483)*V*T+144*T**2+352*a*a-616*a*c-216*c*c
    ck('trace_expansion',S.expand(traced-target)==0)
    A=35-157*z-54*z*z;L=285+483*z+144*z*z
    C0=49*a*a-301*a*c+108*c*c;C1=637*a*a-133*a*c-72*c*c
    D=84*a-199*c+z*(-259*a+54*c)
    affine=S.expand(target.subs({V:a+S.Symbol('X'),T:c+z*S.Symbol('X')}));affine=S.Poly(affine,S.Symbol('X'))
    ck('affine_trace',S.expand(affine.coeff_monomial(S.Symbol('X')**2)*M+affine.coeff_monomial(1)-L*M-C1)==0)
    E=S.expand(A*C1-L*C0)
    explicit=-2*((20727*z*z+61838*z-4165)*a*a-(25263*z*z+83132*z+40565)*a*c+(5832*z*z+20430*z+16650)*c*c)
    ck('elimination_expansion',S.expand(E-explicit)==0)
    c0=C0.subs({a:1,c:r});c1=C1.subs({a:1,c:r});dd=D.subs({a:1,c:r});ee=E.subs({a:1,c:r})
    ck('Jordan_resultant',S.resultant(c0,c1,r)==(-1443826943 if fault=='resultant_data' else -1443826944))
    ck('AL_resultant',S.resultant(A,L,z)==203212800)
    ck('a_zero_polynomial',S.expand(E.subs(a,0)/(-36*c*c))==324*z*z+1135*z+925)
    az=S.resultant(324*z*z+1135*z+925,(1024-4*kk)*108*A+kk*(-199+54*z)**2,z)
    ck('a_zero_resultant',S.expand(az)==2916*(15239903841*kk*kk+33615525529600*kk+7671026339020800))
    polys={};size=31 if fault=='trace_dimension' else 32
    lead=2268426384*(21990393*kk*kk+20902856704*kk-5674993975296)
    disc=20902856704**2+4*21990393*5674993975296
    ck('leading_discriminant',disc==936110809545523068928 and 30595927989**2<disc<30595927990**2)
    quartic=2006694*z**4+22562181*z**3+69814211*z*z+58023859*z-14806945
    for mult in [2,4,6,8,10,12,14,16]:
        f=(size-2*mult)**2*A*c0+mult*(size-mult)*dd**2
        res=S.Poly(S.resultant(ee,f,r),z);poly=res.sqf_part().monic()
        ck('leading_'+str(mult),res.LC()==lead.subs(kk,mult*(32-mult)))
        ck('degree_'+str(mult),poly.degree()==(4 if mult==16 else 8))
        if mult==16:ck('balanced_quartic',poly==S.Poly(quartic,z).monic())
        polys[str(mult)]=[str(q) for q in poly.all_coeffs()]
    ck('finite_slope_count',7*8+4==60)
    # Independent Sturm counts certify the real quartic relaxation.
    intervals=[(S.Rational(-3150,467),S.Rational(-20647,3061)),(S.Rational(-2499,925),S.Rational(-7832,2899)),(S.Rational(-2487,1244),S.Rational(-2485,1243)),(S.Rational(319,1575),S.Rational(303,1496))]
    for i,(lo,hi) in enumerate(intervals):ck('quartic_root_'+str(i),lo<hi and S.Poly(quartic,z).count_roots(lo,hi)==1)
    ck('quartic_simple',S.degree(S.gcd(quartic,S.diff(quartic,z)),z)==0)
    ck('balanced_denominator',84-259*S.Rational(199,54)!=0)
    # Exact parity model: an odd invertible swap pairs volume sectors inside X eigenspaces.
    J=S.diag(S.I,S.I,-S.I,-S.I);P=S.Matrix([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]]);X=S.diag(2,3,2,3)
    ck('volume_pairing_model',P*J+J*P==S.zeros(4) and P*X==X*P and P.det()!=0)
    # Actual central affine ansatz, with real normal signatures ++++------.
    b,cc,d,e=S.symbols('b c d e',real=True)
    ix=lambda ns:k.blade([k.N[i-1] for i in ns])
    clean=lambda x:{q:S.expand(v) for q,v in x.items() if S.expand(v)!=0}
    # Lift the existing rational Clifford blade multiplication to polynomial coefficients.
    def pscale(x,c):return clean({q:c*v for q,v in x.items()})
    def padd(*xs):
        out={}
        for x in xs:
            for q,v in x.items():out[q]=out.get(q,0)+v
        return clean(out)
    def pmul(x,y):
        out={}
        for q,v in x.items():
            for t,w in y.items():
                for mask,sign in k.mm({q:1},{t:1}).items():out[mask]=out.get(mask,0)+sign*v*w
        return clean(out)
    def pK(x):return padd(*(pscale(pmul(pmul(k.G[j],x),k.G[j]),k.ETA[j]) for j in k.N))
    v=pmul(k.blade(k.N),pmul(ix([1]),padd(pscale(ix([2,3]),b),pscale(ix([4,5]),cc))))
    u=pmul(ix([6]),padd(pscale(ix([2,3]),d),pscale(ix([4,5]),e)));t=pmul(k.OM,u)
    va=cc**2-b**2;ca=e**2-d**2;vs=pmul(v,v);ts=pmul(t,t);U=pK(pmul(v,t))
    ck('ansatz_real_signatures',[k.ETA[i] for i in k.N]==[1,1,1,1,-1,-1,-1,-1,-1,-1])
    ck('ansatz_commuting',not clean(padd(pmul(v,t),pscale(pmul(t,v),-1))))
    ck('ansatz_Bsquare',pmul(ix([2,3,4,5]),ix([2,3,4,5]))==pscale(k.I,-1))
    ck('ansatz_V',clean(vs)==clean(padd(pscale(k.I,va),pscale(ix([2,3,4,5]),2*b*cc))))
    ck('ansatz_T',clean(ts)==clean(padd(pscale(k.I,ca),pscale(ix([2,3,4,5]),2*d*e))))
    ff=padd(pscale(vs,10),pscale(ts,16),pscale(k.I,4*va-12*ca))
    gg=padd(pscale(vs,142),pscale(ts,36),pscale(k.I,68*va-108*ca))
    q0=padd(pmul(ff,v),pscale(pmul(U,t),3));q4=padd(pmul(gg,t),pscale(pmul(U,v),7))
    f1=7*b**3-17*b*cc**2-7*b*d**2-5*b*e**2-(9 if fault=='ansatz_cross' else 10)*cc*d*e
    f2=17*b*b*cc+10*b*d*e-7*cc**3+5*cc*d*d+7*cc*e*e
    ck('ansatz_original_q0',clean(q0)==clean(padd(pscale(ix([4,5,6,7,8,9,10]),-2*f1),pscale(ix([2,3,6,7,8,9,10]),2*f2))))
    g1=21*b*b*d-32*b*cc*e-28*cc*cc*d-9*d**3;g2=28*b*b*e+32*b*cc*d-21*cc*cc*e+9*e**3
    ck('ansatz_original_q4',clean(q4)==clean(padd(pscale(pmul(k.OM,ix([2,3,6])),-8*g1),pscale(pmul(k.OM,ix([4,5,6])),-8*g2))))
    ck('ansatz_elimination',S.expand(cc*f1+b*f2-(2*b*cc*(ca-12*va)-10*va*d*e))==0)
    hh=45*z*z-101*z-384;jj=S.expand(ee.subs(r,12+5*z))
    ck('ansatz_D',S.expand(dd.subs(r,12+5*z))==6*hh)
    ck('ansatz_J',jj==-2*(145800*z**4+1084275*z**3+3009569*z*z+3801349*z+1906655))
    ck('ansatz_resultant',S.resultant(hh,jj,z)==199816992133516800)
    ck('ansatz_remainder',S.rem(jj,hh,z)==-(325040858*z+652393142)/5)
    ck('ansatz_boundary_b0',S.expand(f1.subs(b,0))==-10*cc*d*e)
    ck('ansatz_boundary_c0',S.expand(f2.subs(cc,0))==10*b*d*e)
    ck('ansatz_zero_v_q4',g1.subs({b:0,cc:0})==-9*d**3 and g2.subs({b:0,cc:0})==9*e**3)
    rows={}
    for label,v,u,slope,offset in previous.fixtures():
        t=k.mm(k.OM,u);vs=k.mm(v,v);ts=k.mm(t,t);av=k.scalar(vs);cv=k.scalar(ts);h=k.mm(v,t);U=k.K(h)
        if fault=='grade_weight':U=k.add(k.scale(k.grade(h,4),3),k.scale(k.grade(h,8),-6))
        identity=k.scalar(k.add(k.mm(U,U),k.scale(k.mm(U,h),4),k.scale(k.mm(h,h),-12)))
        ck(label+'_grade_trace_identity',identity==0)
        residual=285*k.scalar(k.mm(vs,vs))+483*k.scalar(k.mm(vs,ts))+144*k.scalar(k.mm(ts,ts))+352*av*av-616*av*cv-216*cv*cv
        ck(label+'_moment_rejects',residual==(-10704 if label=='proportional' else -35268))
        ck(label+'_commutes',not k.comm(v,t))
        rr,pp,fl,aa,bb,ww=k.filt(v,u)
        adapters={j:k.scale(k.mm(k.inv(pp),k.port(rr)[j]),-k.ETA[j]) for j in k.N}
        qs={j:k.RR(adapters,*k.C(k.port(k.add(v,t)),*k.kernel(adapters,j)))[1] for j in k.N}
        contraction=k.add(*(k.scale(k.mm(qs[j],k.G[j]),k.ETA[j] if fault=='row_contraction' else 1) for j in k.N))
        ck(label+'_original10_transfer',k.scale(k.mm(k.bar(pp),contraction),6)==fl)
        ck(label+'_original10_rejection',sum(bool(q) for q in qs.values())==9)
        rows[label]=dict(moment_residual=str(residual),nonzero_original_rows=sum(bool(q) for q in qs.values()))
    return cs,polys,rows
FAULTS=['trace_cross','resultant_data','trace_dimension','grade_weight','row_contraction','ansatz_cross']
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    cs,polys,rows=controls();assert all(cs.values()),[n for n,v in cs.items() if not v]
    faults={}
    for f in FAULTS:
        bad=[n for n,v in controls(f)[0].items() if not v];assert bad,('undetected',f);faults[f]=bad
    deps=['explorations/conditional-build/k2183-commuting-trace-descent-2026-10-28.md','explorations/conditional-build/k2181-mixed-square-pencil-descent-2026-10-28.md','explorations/conditional-build/k2179-commuting-nonscalar-descent-2026-10-28.md','tests/channel-swings/k2181_mixed_square_pencil_descent_probe.py','tests/channel-swings/k2179_commuting_nonscalar_descent_probe.py','tests/channel-swings/k2169_invertible_pencil_full_descent_probe.py']
    report=dict(result_id='K2183',status='conditional_exact_controls',checks=cs,fault_failures=faults,monic_squarefree_slope_polynomials=polys,fixtures=rows,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written trace, Jordan, zero-scalar and parity proofs plus finite algebraic projection; exact controls and original-row fixtures supplement independent review. No affine existence, all-port exclusion, physical quotient or proof-assistant claim.')
    dst=ROOT/'lab/process/k2183-commuting-trace-descent.json'
    if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dst.read_text())==report
    print(json.dumps(dict(result='K2183',checks=len(cs),faults=len(faults),fixtures=rows)))
if __name__=='__main__':main()
