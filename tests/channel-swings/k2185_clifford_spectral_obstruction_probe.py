#!/usr/bin/env python3
"""Exact affine grade-square exclusions and exterior-support controls."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,json,hashlib,itertools,math
import sympy as S
import k2181_mixed_square_pencil_descent_probe as previous
k=previous.k;ROOT=Path(__file__).resolve().parents[2]

def wedge(x,y):
    out={}
    for a,v in x.items():
        for b,w in y.items():
            if a&b:continue
            sign=(-1)**sum((b&((1<<i)-1)).bit_count() for i in range(10) if a>>i&1)
            out[a|b]=out.get(a|b,0)+sign*v*w
    return {a:v for a,v in out.items() if v}
def blade(*ns):return {sum(1<<i for i in ns):1}
def add(*xs):
    out={}
    for x in xs:
        for a,v in x.items():out[a]=out.get(a,0)+v
    return {a:v for a,v in out.items() if v}
def scale(x,c):return {a:c*v for a,v in x.items() if c*v}
def wedge_ranks():
    cols=[sum(1<<i for i in c) for c in itertools.combinations(range(10),3)]
    rows=[sum(1<<i for i in c) for c in itertools.combinations(range(10),5)]
    ri={b:i for i,b in enumerate(rows)};out={}
    for rank in [2,4,6,8,10]:
        b=add(*(blade(i,i+1) for i in range(0,rank,2)))
        data={}
        for j,a in enumerate(cols):
            for t,v in wedge(b,{a:1}).items():data[ri[t],j]=v
        # Small integer exterior matrices; exact fraction-free DomainMatrix rank.
        out[rank]=S.polys.matrices.DomainMatrix.from_Matrix(S.SparseMatrix(252,120,data)).rank()
    return out

def controls(fault=None,ranks=None):
    cs={};ck=lambda n,v:cs.__setitem__(n,bool(v))
    V,T,a,c,z,r,X,U,h=S.symbols('V T a c z r X U h')
    F=10*V+16*T+4*a-12*c;G=142*V+36*T+68*a-108*c
    A=35-157*z-54*z*z;L=285+483*z+144*z*z
    C0=49-301*r+108*r*r;C1=637-133*r-72*r*r
    D=84-199*r+z*(-259+54*r);E=S.expand(A*C1-L*C0)
    hs=[S.expand(F*G-(83 if fault=='H4_coefficient' else 84)*F*V+756*V*T),S.expand(F*G+28*F*V+(85 if fault=='H8_coefficient' else 84)*V*T)]
    js=[];res=[]
    for index,pol in enumerate(hs):
        pp=S.Poly(S.expand(pol.subs({a:1,c:r,V:1+X,T:r+z*X})),X)
        jj=S.expand(A*pp.coeff_monomial(X)-D*pp.coeff_monomial(X**2));js.append(jj)
        res.append(S.resultant(E,jj,r))
    exact4=8*((2916*z**3+18504*z*z+37260*z+15600)*r-3465*z**3-18151*z*z-29015*z+2975)
    exact8=8*((2916*z**3+12456*z*z+61956*z+42480)*r-11025*z**3-22015*z*z-52367*z+2975)
    ck('scalar_h4_coefficient',S.expand(js[0]-exact4)==0);ck('scalar_h8_coefficient',S.expand(js[1]-exact8)==0)
    rr4=37632*(z-5)*(9*z+25)*(54*z*z+69*z-85)*(62937*z**4+447264*z**3+1025270*z*z+586000*z-325375)
    rr8=-338688*(3*z+13)*(11*z+5)*(54*z*z+69*z-85)*(15471*z**4-182466*z**3-994996*z*z-1096718*z+153365)
    ck('h4_resultant',S.expand(res[0]-rr4)==0);ck('h8_resultant',S.expand(res[1]-rr8)==0)
    polynomials={}
    for m in [2,4,6,8,10,12,14,16]:
        size=30 if fault=='dimension' else 32
        rm=S.Poly(S.resultant(E,(size-2*m)**2*A*C0+m*(size-m)*D*D,r),z)
        # Reconstruct inherited full32 spectral polynomial independently of size fault.
        reference=S.Poly(S.resultant(E,(32-2*m)**2*A*C0+m*(32-m)*D*D,r),z)
        ck('full32_spectrum_'+str(m),rm==reference)
        for label,rr in zip(['h4','h8'],res):
            aa,bb,gg=S.gcdex(S.Poly(rr,z),rm)
            ck(label+'_bezout_'+str(m),gg==1 and aa*S.Poly(rr,z)+bb*rm==1)
        polynomials[str(m)]=[str(v) for v in rm.sqf_part().monic().all_coeffs()]
    # Grade identities are algebraic identities in independent commuting h4,h8.
    b,d=S.symbols('h4 h8');uu=(3 if fault=='grade_weight' else 2)*b-6*d;hh=b+d
    ck('grade4_square_identity',S.expand(21*(uu+6*hh)**2-1344*b*b)==0)
    ck('grade8_square_identity',S.expand(21*(2*hh-uu)**2-1344*d*d)==0)
    ranks=wedge_ranks() if ranks is None else ranks
    for rank,wanted in [(2,56),(4,86),(6,106),(8,120),(10,120)]:ck('wedge_rank_'+str(rank),ranks[rank]==wanted)
    ck('rank4_support_dimension',math.comb(4,3)+(math.comb(4,2)-1)*6==34)
    ck('rank6_support_dimension',math.comb(6,3)-math.comb(6,5)==14)
    # Wedge support does NOT force the residual complement bivector simple.
    B=add(blade(0,1),blade(2,3));aa=add(blade(0,1),scale(blade(2,3),-1));cc=add(blade(0,3),blade(1,2))
    ww=add(wedge(aa,blade(4)),wedge(cc,blade(6)));uu=add(wedge(aa,blade(5)),wedge(cc,blade(7)))
    prod=wedge(ww,uu);dd=add(scale(blade(4,5),-2),scale(blade(6,7),2))
    ck('rank4_support_example',not wedge(B,ww) and not wedge(B,uu))
    ck('rank4_top_product',prod==wedge(blade(0,1,2,3),dd))
    ck('residual_not_simple',bool(wedge(dd,dd)))
    fixtures={}
    for label,v,u,slope,offset in previous.fixtures():
        t=k.mm(k.OM,u);hh=k.mm(v,t);uu=k.K(hh);vs=k.mm(v,v);ts=k.mm(t,t);av=k.scalar(vs);cv=k.scalar(ts)
        ff=k.add(k.scale(vs,10),k.scale(ts,16),k.scale(k.I,4*av-12*cv));gg=k.add(k.scale(vs,142),k.scale(ts,36),k.scale(k.I,68*av-108*cv))
        h4=k.grade(hh,4);h8=k.grade(hh,8)
        ck(label+'_mixed_grades',bool(h4) and bool(h8))
        ck(label+'_both_grade_squares_scalar',set(k.mm(h4,h4))<= {0} and set(k.mm(h8,h8))<= {0})
        ck(label+'_central_U',not k.comm(uu,v) and not k.comm(uu,t))
        w=k.scale(k.mm(k.blade(k.N),v),-1);wu=k.mm(w,u)
        ck(label+'_trivector_dual',set(mask.bit_count() for mask in w)=={3})
        ck(label+'_anticommutes',not k.add(wu,k.mm(u,w)))
        bv=k.grade(wu,2)
        ck(label+'_bivector_anticommutators',not k.add(k.mm(bv,w),k.mm(w,bv)) and not k.add(k.mm(bv,u),k.mm(u,bv)))
        rr,pp,fl,_,_,_=k.filt(v,u);ad={j:k.scale(k.mm(k.inv(pp),k.port(rr)[j]),-k.ETA[j]) for j in k.N}
        qs={j:k.RR(ad,*k.C(k.port(k.add(v,t)),*k.kernel(ad,j)))[1] for j in k.N}
        contraction=k.add(*(k.scale(k.mm(qs[j],k.G[j]),k.ETA[j] if fault=='row_contraction' else 1) for j in k.N))
        ck(label+'_original_transfer',k.scale(k.mm(k.bar(pp),contraction),6)==fl)
        ck(label+'_original_rejected',sum(bool(q) for q in qs.values())==9)
        fixtures[label]={'nonzero_original_rows':sum(bool(q) for q in qs.values()),'B_blades':len(bv)}
    return cs,polynomials,fixtures
FAULTS=['H4_coefficient','H8_coefficient','dimension','grade_weight','row_contraction']
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    ranks=wedge_ranks();cs,polys,fixtures=controls(ranks=ranks);assert all(cs.values()),[n for n,v in cs.items() if not v]
    faults={}
    for fault in FAULTS:
        bad=[n for n,v in controls(fault,ranks)[0].items() if not v];assert bad,('undetected',fault);faults[fault]=bad
    deps=['explorations/conditional-build/k2185-clifford-spectral-obstruction-2026-10-28.md','explorations/conditional-build/k2183-commuting-trace-descent-2026-10-28.md','explorations/conditional-build/k2179-commuting-nonscalar-descent-2026-10-28.md','tests/channel-swings/k2181_mixed_square_pencil_descent_probe.py','tests/channel-swings/k2169_invertible_pencil_full_descent_probe.py']
    report=dict(result_id='K2185',status='conditional_exact_controls',checks=cs,fault_failures=faults,wedge_map_ranks=ranks,spectral_polynomials=polys,fixtures=fixtures,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written Clifford centrality and exterior-support proofs, sixteen exact polynomial Bezout certificates; finite rank and original-row controls. No rank-four existence, general exclusion or physical quotient claim.')
    # JSON normalizes integer dictionary keys.
    report=json.loads(json.dumps(report));dst=ROOT/'lab/process/k2185-clifford-spectral-obstruction.json'
    if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dst.read_text())==report
    print(json.dumps(dict(result='K2185',checks=len(cs),faults=len(faults),wedge_ranks=ranks)))
if __name__=='__main__':main()
