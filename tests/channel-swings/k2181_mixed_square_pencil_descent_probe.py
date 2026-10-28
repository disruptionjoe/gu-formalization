#!/usr/bin/env python3
"""Proportional and affine square-pencil identities and actual Clifford consumers."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,json,hashlib
import sympy as S
import k2179_commuting_nonscalar_descent_probe as k
ROOT=Path(__file__).resolve().parents[2]

def fixtures():
    ix=lambda a:k.blade([k.N[i-1] for i in a])
    return [
      ('proportional',k.mm(k.blade(k.N),k.add(ix([1,2,3]),k.scale(ix([1,4,5]),2))),k.add(ix([2,3,6]),k.scale(ix([4,5,6]),2)),1,0),
      ('affine',k.mm(k.blade(k.N),k.add(ix([1,2,3]),ix([1,4,5]))),k.add(k.scale(ix([2,3,6]),2),k.scale(ix([4,5,6]),3)),6,5)]

def controls(fault=None):
    cs={};ck=lambda name,value:cs.__setitem__(name,bool(value))
    z,a,c,X,V,T,r=S.symbols('z a c X V T r')
    Q=35*V**2-(156 if fault=='square_cross' else 157)*V*T-54*T**2+(14*a-42*c)*V+(-102*a+162*c)*T
    A=35-157*z-54*z*z;B=14-144*z+162*z*z
    D=84*a-199*c+z*(-259*a+54*c);C0=49*a*a-301*a*c+108*c*c
    ck('proportional_factor',S.expand(Q.subs({T:z*V,c:z*a})-V*(A*V+B*a))==0)
    ck('affine_factor',S.expand(Q.subs({V:a+X,T:c+z*X})-(A*X*X+D*X+C0))==0)
    ck('AB_bezout_step',S.expand(B+3*A)==119-615*z)
    ck('AB_exceptional_point',A.subs(z,S.Rational(119,615))==S.Rational(983136,378225))
    ck('AB_resultant',S.resultant(A,B,z)==-53089344)
    R=S.resultant(D.subs({a:1,c:r}),C0.subs({a:1,c:r}),r)
    ck('affine_resultant_polynomial',S.expand(R)==49*(64854*z*z+227077*z-47531))
    ck('affine_exceptional_resultant',S.resultant(A,R,z)==-2212378216925184)
    ck('affine_a_zero',C0.subs(a,0)==108*c*c)
    ck('affine_remainder',S.rem(R,A,z)==1176*(1605*z-229))
    ck('affine_exceptional_point',A.subs(z,S.Rational(229,1605))==S.Rational(29624496,2576025))
    # Derive trace filter from two actual eigenvalues satisfying trace zero.
    q,AA=S.symbols('q AA',nonzero=True);size=31 if fault=='trace_dimension' else 32
    for m in range(33):
        x1=(32-m)*q;x2=-m*q;DD=-AA*(x1+x2);CC=AA*x1*x2
        expr=(size-2*m)**2*AA*CC+m*(size-m)*DD**2
        ck('multiplicity_'+str(m),S.expand(expr)==0)
    J=S.Matrix([[0,1],[0,0]])
    ck('nilpotent_not_zero',J!=S.zeros(2) and J**2==S.zeros(2))
    rows={}
    for name,v,u,slope,offset in fixtures():
        t=k.mm(k.OM,u);vs=k.mm(v,v);ts=k.mm(t,t);av=k.scalar(vs);cv=k.scalar(ts);h=k.mm(v,t);U=k.K(h)
        ck(name+'_commuting',not k.comm(v,t))
        ck(name+'_mixed',bool(k.grade(h,4)) and bool(k.grade(h,8)))
        ck(name+'_central',not k.comm(U,v) and not k.comm(U,t))
        ck(name+'_affine_relation',ts==k.add(k.scale(vs,slope),k.scale(k.I,offset)))
        ck(name+'_nonscalar',bool(k.add(vs,k.scale(k.I,-av))))
        ck(name+'_not_proportional' if name=='affine' else name+'_proportional',offset!=0 if name=='affine' else ts==vs)
        rr,pp,fl,aa,bb,ww=k.filt(v,u)
        ck(name+'_pencil',k.mm(pp,k.inv(pp))==k.I)
        FF=k.add(k.scale(vs,10),k.scale(ts,16),k.scale(k.I,4*av-12*cv));GG=k.add(k.scale(vs,142),k.scale(ts,36),k.scale(k.I,68*av-108*cv))
        q0=k.add(k.mm(FF,v),k.scale(k.mm(U,t),3));q4=k.add(k.mm(GG,t),k.scale(k.mm(U,v),7))
        square=k.add(k.scale(k.mm(vs,vs),35),k.scale(k.mm(vs,ts),-157),k.scale(k.mm(ts,ts),-54),k.scale(vs,14*av-42*cv),k.scale(ts,-102*av+162*cv))
        ck(name+'_square_nonzero',bool(square))
        ck(name+'_square_transfer',k.add(k.scale(k.mm(q0,v),7),k.scale(k.mm(q4,t),-3))==k.scale(square,2))
        ss=k.add(k.scale(v,7),k.scale(t,9));poly=k.add(k.mm(aa,ss),k.neg(k.mm(bb,pp)))
        ck(name+'_Euler_tangent0',k.tang(poly,0)==k.scale(q0,-504))
        ck(name+'_Euler_tangent4',k.tang(poly,4)==k.scale(q4,72))
        adapters={j:k.scale(k.mm(k.inv(pp),k.port(rr)[j]),-k.ETA[j]) for j in k.N}
        qs={j:k.RR(adapters,*k.C(k.port(k.add(v,t)),*k.kernel(adapters,j)))[1] for j in k.N}
        contraction=k.add(*(k.scale(k.mm(qs[j],k.G[j]),k.ETA[j] if fault=='row_contraction' else 1) for j in k.N))
        ck(name+'_original10_transfer',k.scale(k.mm(k.bar(pp),contraction),6)==fl)
        ck(name+'_original10_rejection',any(qs.values()))
        rows[name]=dict(nonzero_original_rows=sum(bool(x) for x in qs.values()),a=str(av),c=str(cv),slope=slope,offset=offset)
    # Cancellation in the exceptional case is an actual commutative identity.
    vv,hh,zz=S.symbols('V h z',nonzero=True);uu=-(10+(15 if fault=='exceptional_coefficient' else 16)*zz)*hh/(3*zz)
    ck('exceptional_U_transfer',S.expand(((10+16*zz)*vv**2+3*uu*hh).subs(hh**2,zz*vv**2))==0)
    return cs,rows

FAULTS=['square_cross','trace_dimension','row_contraction','exceptional_coefficient']
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    cs,rows=controls();assert all(cs.values()),[n for n,v in cs.items() if not v]
    faults={}
    for f in FAULTS:
        bad=[n for n,v in controls(f)[0].items() if not v];assert bad,('undetected',f);faults[f]=bad
    deps=['explorations/conditional-build/k2181-mixed-square-pencil-descent-2026-10-28.md','explorations/conditional-build/k2177-exceptional-spectrum-descent-2026-10-28.md','explorations/conditional-build/k2179-commuting-nonscalar-descent-2026-10-28.md','tests/channel-swings/k2179_commuting_nonscalar_descent_probe.py','tests/channel-swings/k2171_mixed_port_euler_filter_probe.py','tests/channel-swings/k2169_invertible_pencil_full_descent_probe.py']
    report=dict(result_id='K2181',status='conditional_exact_controls',checks=cs,fault_failures=faults,fixtures=rows,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written proportional and exceptional-affine proofs; exact polynomial controls and real Clifford original ten-row fixtures supplement independent internal reconstruction, not a proof assistant or physical quotient claim.')
    dst=ROOT/'lab/process/k2181-mixed-square-pencil-descent.json'
    if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dst.read_text())==report
    print(json.dumps(dict(result='K2181',checks=len(cs),faults=len(faults),fixtures=rows)))
if __name__=='__main__':main()
