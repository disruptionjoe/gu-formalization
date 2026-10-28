#!/usr/bin/env python3
"""Exact algebraic certificates; representation transfer is proved in the note."""
import sys
sys.dont_write_bytecode=True
import sympy as S
import argparse,json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def controls(fault=None):
    x,a,c,d,p,D,t,r,s=S.symbols('x a c d p D t r s')
    q=S.symbols('q', nonzero=True)
    checks={}
    def ck(n,v):
        checks[n]=bool(v)

    V=(-35*a+81*c)/70-S.Rational(55 if fault=='Euler_coefficient' else 54,35)*q*x-q/(5*x)
    T=-a/2-S.Rational(3,14)*c+S.Rational(30,7)*q*x-q/x
    Q=108*q*x**4+(35*a-81*c)*x**3+(315 if fault=='quartic_coefficient' else 314)*q*x*x-(35*a+15*c)*x-70*q
    ck('quartic_from_T_equals_VX2',S.cancel(70*x*(T-V*x*x)-Q)==0)
    ck('first_Euler_rational',S.cancel(10*V-2*T+4*a-12*c+24*q*x)==0)
    ck('second_Euler_rational',S.cancel(100*V+36*T+68*a-108*c+56*q/x)==0)
    ck('VT_X_inverse_independence',S.det(S.Matrix([[-S.Rational(54,35),-S.Rational(1,5)],[S.Rational(30,7),-1]]))==S.Rational(12,5))
    mx=-7*(a-c)/(12*q);mi=-3*(7*a-3*c)/(7*q)
    ck('trace_V_equals_a',S.cancel((-35*a+81*c)/70-S.Rational(54,35)*q*mx-q*mi/5-a)==0)
    ck('trace_T_equals_c',S.cancel(-a/2-S.Rational(3,14)*c+S.Rational(30,7)*q*mx-q*mi-c)==0)
    A=(35*a-81*c)/108; C=-(35*a+15*c)/108; B=S.Rational(157,54); E=-S.Rational(35,54)
    ck('shifted_Vieta_X',S.cancel((-A+d)/4-mx.subs(q,1)-(217*a-171*c+108*d)/432)==0)
    ck('shifted_Vieta_inverse',S.cancel((-C/E-d/p)/4-mi.subs(q,1)-(161*a-75*c-14*d/p)/56)==0)
    ck('full_characteristic_trace_contradiction', S.det(S.Matrix([[217,-171],[161,-75]]))==11256)
    # a=c=0 implies m2=-B/2 and h=(-54/35)X²-1/5.
    ck('full_characteristic_h_trace',-S.Rational(54,35)*(-B/2)-S.Rational(1,5)==S.Rational(143,70))
    sol=S.solve([217*a-171*c+108*d,161*a-75*c-14*d/p],[a,c])
    af=S.factor(A.subs(sol)/d); cf=S.factor(C.subs(sol)/d)
    ck('A_coefficient',S.cancel(af+(1116*p+161)/(1206*p))==0)
    ck('C_coefficient',S.cancel(cf+5*(324*p+77)/(3618*p))==0)
    # P4 remainder by x²-zx+p. D=d² and t=d*z.
    f0=p*p-p*(D+4*p)-af*p*t-B*p+E
    f1=t*(D+2*p+B)+af*D*(D+3*p)+cf*D
    fh=-(-3348*D*p-483*D+3618*p*t-9782*p)/(9380*p)
    z=S.symbols('z')
    m1=-S.Rational(7,12)*(a-c)
    m2=(A*A-2*B+d*z)/4
    htrace=(-35*a+81*c)/70*m1-S.Rational(54,35)*m2-S.Rational(11 if fault=='h_trace_target' else 6,5)
    ck('htrace_substitution',S.cancel(S.expand(htrace.subs(sol)).subs({d*d:D,d*z:t})-fh)==0)
    rem=S.rem(x**4+A*x**3+B*x*x+C*x+E,x*x-z*x+p,x)
    ck('constant_remainder',S.cancel(S.expand(rem.coeff(x,0).subs(sol)).subs({z*z:D+4*p,d*z:t})-f0)==0)
    ck('linear_remainder',S.cancel(rem.coeff(x,1)-(z**3-2*p*z+A*(z*z-p)+B*z+C))==0)
    n0=S.factor(-3618*f0); nh=S.factor(-9380*p*fh)
    M,b=S.linear_eq_to_matrix([n0,nh],[D,t])
    ck('exceptional_determinant',S.expand(M.det()-9*(90*p-161)*(2322*p+161))==0)
    for pv in [S.Rational(161,90),-S.Rational(161,2322)]:
     ck('exception_inconsistent_'+str(pv),M.subs(p,pv).rank()==1 and M.row_join(b).subs(p,pv).rank()==2)
    solDt=S.solve([n0,nh],[D,t]);den=3*(90*p-161)*(2322*p+161)
    ck('D_solution',S.cancel(solDt[D]-(-13089924*p**3-1769202*p*p-1253168*p)/den)==0)
    ck('t_solution',S.cancel(solDt[t]-(-12113064*p**3-1689606*p*p-4310579*p-377545)/den)==0)
    f=(654105457 if fault=='elimination_coefficient' else 654105456)*p**4-3130538868*p**3-644992956*p*p-832929405*p-52073525
    g=586116*p**4-3091284*p**3-758643*p*p-736330*p-82075
    ck('linear_remainder_numerator',S.cancel(f1.subs(solDt)-f/(54*den))==0)
    ck('d_z_identity_numerator',S.cancel((t*t-D*(D+4*p)).subs(solDt)-67*g/(3*den))==0)
    u,v,h=S.gcdex(f,g,p)
    ck('Bezout_one',h==1 and S.expand(u*f+v*g)==1)
    return checks,dict(bezout_u=str(S.factor(u)),bezout_v=str(S.factor(v)),resultant=str(S.resultant(f,g,p)))

def h8_controls(fault=None):
    x,a,c,p,d,D,t,y,s,u,z=S.symbols('x a c p d D t y s u z'); checks={};certificates={}
    def ck(n,b):
     checks[n]=bool(b)
    V=(-169*a+243*c)/384-S.Rational(10 if fault=='h8_Euler_coefficient' else 9,32)*x+S.Rational(77,192)/x
    T=(7*a+99*c)/384+S.Rational(39,32)*x-S.Rational(35,192)/x
    Q=108*x**4+(169*a-243*c)*x**3+(315 if fault=='h8_quartic_coefficient' else 314)*x*x+(7*a+99*c)*x-70
    ck('Euler1',S.cancel(10*V+22*T+4*a-12*c-24*x)==0)
    ck('Euler2',S.cancel(156*V+36*T+68*a-108*c-56/x)==0)
    ck('quartic',S.cancel(384*x*(T-V*x*x)-Q)==0)
    mx=(7*a+5*c)/12;mi=(28*a-9*c)/7
    ck('traceV',S.cancel((-169*a+243*c)/384-S.Rational(9,32)*mx+S.Rational(77,192)*mi-a)==0)
    ck('traceT',S.cancel((7*a+99*c)/384+S.Rational(39,32)*mx-S.Rational(35,192)*mi-c)==0)
    A=(169*a-243*c)/108;C=(7*a+99*c)/108;B=S.Rational(157,54);E=-S.Rational(35,54)
    ck('four_roots_trace_x',S.expand(-108*(-A-4*mx))==421*a-63*c)
    ck('four_roots_trace_inverse',S.expand(-70*(-C/E-4*mi))==1113*a-459*c)
    ck('four_roots_nonzero_det',S.det(S.Matrix([[421,-63],[1113,-459]]))!=0)
    ck('four_roots_h_contradiction',-S.Rational(9,32)*(-B/2)+S.Rational(77,192)==S.Rational(311,384))
    # Three distinct roots, characteristic/missing quartic root quotient.
    ac=S.solve([421*a-63*c-108*d,1113*a-459*c+70*d/p],[a,c]);Af=S.factor(A.subs(ac)/d);Cf=S.factor(C.subs(ac)/d)
    f0=p*p-p*(D+4*p)-Af*p*t-B*p+E
    f1=t*(D+2*p+B)+Af*D*(D+3*p)+Cf*D
    m2=(A*A-2*B+d*z)/4
    htrace=((-169*a+243*c)/384*mx-S.Rational(9,32)*m2+S.Rational(77,192)-(2 if fault=='h8_trace_target' else 1))
    fh=S.factor(S.expand(htrace.subs(ac)).subs({d*d:D,d*z:t}))
    ck('three_htrace_formula',S.cancel(fh+(-7614*D*p-2345*D+4860*p*t+13140*p)/(69120*p))==0)
    M,b=S.linear_eq_to_matrix([f0,fh],[D,t]);
    ck('three_only_exceptional_denominators',S.cancel(M.det()+7*(1782*p+335)*(2754*p+2345)/(335923200*p))==0)
    for pv in [-S.Rational(2345,2754),-S.Rational(335,1782)]:
     ck('three_exception_'+str(pv),M.subs(p,pv).rank()==1 and M.row_join(b).subs(p,pv).rank()==2)
    solDt=S.solve([f0,fh],[D,t]);g1=S.factor(f1.subs(solDt));g2=S.factor((t*t-D*(D+4*p)).subs(solDt));num1=S.fraction(g1)[0];num2=S.fraction(g2)[0]
    F=9491536260*p**4+24610284756*p**3+2902896225*p*p-5922516250*p-2710624875
    G=393660*p**4+1460268*p**3+364655*p*p-494550*p-55125
    ck('three_displayed_F',S.expand(num1+2*F)==0)
    ck('three_displayed_G',S.expand(num2+180*G)==0)
    U,W,H=S.gcdex(num1,num2,p);ck('three_Bezout',H==1 and S.expand(U*num1+W*num2)==1)
    certificates['three_roots']={'f':str(num1),'g':str(num2),'bezout_u':str(U),'bezout_v':str(W),'htrace':str(fh),'Dt':str(solDt)}
    # Two roots r=y*s, s, weight n and 4-n. n=3 swaps n=1.
    for n in [1,2]:
     m1=(n*y+4-n)*s/4;mminus=(n/y+4-n)/(4*s);m2=(n*y*y+4-n)*s*s/4
     ac2=S.solve([7*a+5*c-12*m1,28*a-9*c-7*mminus],[a,c])
     conv=lambda f:S.factor(S.expand(S.cancel(f)).subs(s**4,u*u).subs(s*s,u))
     f=conv(Q.subs(ac2).subs(x,s));g=conv(Q.subs(ac2).subs(x,y*s));h=conv(((-169*a+243*c)/384*m1-S.Rational(9,32)*m2+S.Rational(77,192)-1).subs(ac2))
     hn=S.fraction(h)[0];L=S.diff(hn,u);K=hn.subs(u,0)
     ck('two_h_linear_'+str(n),S.diff(hn,u,2)==0)
     bU,bV,bH=S.gcdex(L,K,y);ck('two_exception_Bezout_'+str(n),bH==1 and S.expand(bU*L+bV*K)==1)
     us=S.solve(h,u)[0];fs=S.factor(f.subs(u,us));gs=S.factor(g.subs(u,us));fn=S.fraction(fs)[0];gn=S.fraction(gs)[0]
     if n==1:
      ff=60750*y**5-364763*y**4+2873112*y**3-55938354*y*y-21121534*y-1006683
      gg=315577*y**5+4991594*y**4-7884842*y**3+24019656*y*y+4697513*y-973674
      uu=7*(1273*y*y+22030*y+1273)/(54*y*(-75*y*y+1174*y+949))
     else:
      ff=3258*y**5-431197*y**4-4608372*y**3-8280762*y*y-824414*y-14289
      gg=14289*y**5+824414*y**4+8280762*y**3+4608372*y*y+431197*y-3258
      uu=7*(1273*y*y+15886*y+1273)/(54*y*(181*y*y+1174*y+181))
     ck('two_displayed_F_'+str(n),S.expand(fn+448*ff)==0)
     ck('two_displayed_G_'+str(n),S.expand(gn-448*gg)==0)
     ck('two_displayed_u_'+str(n),S.cancel(us-uu)==0)
     U,W,H=S.gcdex(fn,gn,y);ck('two_root_Bezout_'+str(n),H==1 and S.expand(U*fn+W*gn)==1)
     certificates['two_roots_'+str(n)]={'f':str(fn),'g':str(gn),'bezout_u':str(U),'bezout_v':str(W),'u':str(us),'exception_bezout_u':str(bU),'exception_bezout_v':str(bV)}
    ck('one_root_contradiction',S.det(S.Matrix([[14,-14],[168,-72]]))!=0)
    return checks,certificates

def spin8_controls():
    checks={};basis=list(range(16))
    def wedge(i,j):
        if i&j:return 0
        return (-1)**sum(1 for a in range(4) for b in range(4) if (i>>a)&1 and (j>>b)&1 and a>b)
    B=S.zeros(16)
    for i in basis:
        j=15^i;k=i.bit_count();B[i,j]=(-1)**(k*(k-1)//2)*wedge(i,j)
    gammas=[]
    for k in range(4):
        c=S.zeros(16);a=S.zeros(16)
        for j in basis:
            sign=(-1)**((j&((1<<k)-1)).bit_count())
            if j&(1<<k):a[j^(1<<k),j]=sign
            else:c[j|(1<<k),j]=sign
        gammas += [c+a,c-a]
    checks['Chevalley_symmetric_nondegenerate']=B==B.T and B.det()!=0
    for i,g in enumerate(gammas):checks[f'Clifford_selfadjoint_{i}']=g.T*B==B*g
    for parity in [0,1]:
        ids=[i for i in basis if i.bit_count()%2==parity];bb=B.extract(ids,ids)
        checks[f'halfspin_symmetric_nondegenerate_{parity}']=bb==bb.T and bb.det()!=0
        for i in range(8):
            for j in range(i+1,8):
                z=(gammas[i]*gammas[j]).extract(ids,ids)
                checks[f'bivector_skew_{parity}_{i}_{j}']=z.T*bb+bb*z==S.zeros(8)
    return checks

def degenerate_fixture_controls():
    # Exact Cl(6,2) dictionary fixture; embedded in complex Cl10 for identity checks.
    metric=[1,1,1,-1,1,-1,1,1]
    def add(*vs):
        out={}
        for v in vs:
            for k,x in v.items():out[k]=out.get(k,0)+x
        return {k:x for k,x in out.items() if x}
    def scale(v,c):return {k:c*x for k,x in v.items() if c*x}
    def mul(a,b):
        out={}
        for i,x in a.items():
            for j,y in b.items():
                sign=(-1)**sum(1 for k in range(8) for l in range(k) if i>>k&1 and j>>l&1)
                for k in range(8):
                    if i&j&(1<<k):sign*=metric[k]
                out[i^j]=out.get(i^j,0)+x*y*sign
        return {k:x for k,x in out.items() if x}
    e=[{1<<k:1} for k in range(8)];n1=add(e[2],e[3]);n2=add(e[4],e[5])
    bs=mul(e[0],e[1]);bn=mul(n1,n2);b=add(bs,bn);dd=scale(mul(bs,bn),2)
    bnr=scale(mul(b,dd),S.Rational(-1,2));bsr=add(b,scale(bnr,-1))
    w=mul(e[0],mul(n1,e[6]));u=mul(e[1],mul(n2,e[7]))
    return {'fixture_B_nonzero':bool(b),'fixture_B2_scalar_plus_D':mul(b,b)==add({0:-1},dd),
            'fixture_D_nonzero_nilpotent':bool(dd) and not mul(dd,dd),
            'fixture_split_recovers_Bs_Bn':bsr==bs and bnr==bn,
            'fixture_Bs_square':mul(bs,bs)=={0:-1},'fixture_Bn_square':not mul(bn,bn),
            'fixture_w_u_grade3':bool(w) and bool(u) and all(k.bit_count()==3 for k in list(w)+list(u)),
            'fixture_w_anticommutes_B':not add(mul(b,w),mul(w,b)),
            'fixture_u_anticommutes_B':not add(mul(b,u),mul(u,b))}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    cs,cert=controls();assert all(cs.values()),[n for n,v in cs.items() if not v]
    hc,hcert=h8_controls();cs.update({'h8_'+k:v for k,v in hc.items()});cs.update(spin8_controls());cs.update(degenerate_fixture_controls());cert['h8']=hcert
    assert all(cs.values()),[n for n,v in cs.items() if not v]
    faults={}
    for f in ['Euler_coefficient','quartic_coefficient','h_trace_target','elimination_coefficient']:
        bad=[n for n,v in controls(f)[0].items() if not v];assert bad,f;faults[f]=bad
    for f in ['h8_Euler_coefficient','h8_quartic_coefficient','h8_trace_target']:
        bad=[n for n,v in h8_controls(f)[0].items() if not v];assert bad,f;faults[f]=bad
    deps=['explorations/conditional-build/k2191-clifford-sector-obstruction-2026-10-28.md','explorations/conditional-build/k2189-nonaffine-clifford-reduction-2026-10-28.md','explorations/conditional-build/k2187-affine-clifford-exclusion-2026-10-28.md','explorations/conditional-build/k2179-commuting-nonscalar-descent-2026-10-28.md']
    report=dict(result_id='K2191',status='conditional_exact_controls',checks=cs,fault_failures=faults,certificate=cert,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written all-commuting rank exhaustion: faithful-four six-plane proof and Pfaffian-even halfspin8 trace proof with exhaustive one-through-four distinct spectra, retaining nilpotent/Jordan cases and exceptional denominators. Exact symbolic certificates and concrete pairing/split controls support but do not replace universal representation transfer. No physical/source/ledger verdict or external certification.')
    dest=ROOT/'lab/process/k2191-clifford-sector-obstruction.json'
    if args.write:dest.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dest.read_text())==report
    print(json.dumps(dict(result='K2191',controls=len(cs),faults=len(faults))))
if __name__=='__main__':main()
