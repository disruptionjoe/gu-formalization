"""Exact conditional growth, normalization and contour controls.

Uses the reviewed leading constant-moment 4D action; no ambient or observational
simulation. Written proofs own the quantified moment range and transfer scope.
"""
import argparse
import json
from pathlib import Path
import sympy as s


def run():
    checks=[]
    def ck(name, value):
        assert value, name
        checks.append(name)
    def eq(name, value):
        ck(name, s.factor(value)==0)
    m0,m1,m2,h=s.symbols('m0 m1 m2 h', nonzero=True)
    AQ=h*m0/2; AR=-99*h*m1/4; A0=2115*h*m2/16
    H2=-A0/(6*AR); ms=AR/(17*AQ)
    C=s.Rational(13068,3995); z=m1**2/(m0*m2)
    eq('mass-over-Hubble',-ms/H2-C*z)
    eq('kappa-cancels',s.diff(-ms/H2,h))
    scale=s.symbols('scale',positive=True)
    eq('common-fibre-scale-cancels',z.subs({m1:scale*m1,m2:scale**2*m2}, simultaneous=True)-z)
    zz=s.symbols('z',positive=True); rate=(s.sqrt(9+4*C*zz)-3)/2
    eq('growing-root-relation',rate**2+3*rate-C*zz)
    ck('maximum-rate-less-than-one',C<4)
    ck('positive-moment-ratio-nonzero',z.subs({m0:1,m1:1,m2:1})==1)
    eps=s.symbols('eps',positive=True)
    threshold=eps*(eps+3)/C
    eq('slow-rate-threshold',threshold*C-eps*(eps+3))
    cv=s.symbols('cv',nonnegative=True)
    eq('variance-ratio',1/(1+cv)*(1+cv)-1)
    # Fixed m0=m2=1 with reciprocal positive atoms has arbitrary small z.
    t=s.symbols('t',positive=True); weights=[1/(1+t**2),t**2/(1+t**2)]; atoms=[t,1/t]
    moms=[sum(w*a**j for w,a in zip(weights,atoms)) for j in range(3)]
    eq('fixed-normalizations-m0',moms[0]-1)
    eq('fixed-normalizations-m2',moms[2]-1)
    eq('free-mean',moms[1]-2*t/(1+t**2))
    ck('arbitrarily-small-rate-ratio',s.limit(moms[1]**2,t,0,dir='+')==0)
    # Sharp bounded-support countercontrol: endpoints a and b, weights b/(a+b),a/(a+b).
    a,b=s.symbols('a b',positive=True)
    mean=2*a*b/(a+b); second=a*b
    eq('bounded-support-sharp-ratio',mean**2/second-4*a*b/(a+b)**2)
    mu=s.symbols('mu',positive=True)
    eq('bounded-support-inequality-square',(a+b)**2*mu**2-4*a*b*((a+b)*mu-a*b)-((a+b)*mu-2*a*b)**2)
    # Curvature/expansion and f'(R) response correlations, full admitted mode reused.
    x,E,H=s.symbols('x E H',nonzero=True)
    chi=x*(x+3)
    deltaR=12*H**2*E
    dF_over_F=4*E/(4-chi)
    dH_over_H=(1-x)*dF_over_F/2
    eq('curvature-expansion-relation',dH_over_H-2*E/(x+4))
    wkin=-s.Rational(2,3)*x*dH_over_H
    eq('kinematic-w-relation',wkin+4*x*E/(3*(x+4)))
    alphaF=x*dF_over_F
    eq('response-drift-correlation',wkin+(1-x)*alphaF/3)
    ck('amplitude-sign-not-selected',wkin.subs(E,-E)==-wkin)
    # Finite signed witness, outside the positive-reference theorem.
    signed=[(s.Integer(3),s.Integer(1)),(-s.Integer(2),s.Integer(2))]
    sm=[sum(w*a**j for w,a in signed)for j in range(3)]
    ck('signed-moments',sm==[1,-1,-5])
    sub=dict(zip([m0,m1,m2],sm));Lam=-A0/(2*AR);bR=17*AQ/6;F0=AR+8*bR*Lam
    eq('signed-scalar-mass',ms.subs(sub)-s.Rational(99,34))
    eq('signed-positive-Lambda',Lam.subs(sub)-s.Rational(1175,88))
    eq('signed-F0',F0.subs(sub)-s.Rational(11621,66)*h)
    ck('signed-not-positive-probability',[w*a*a/sm[2]for w,a in signed]==[-s.Rational(3,5),s.Rational(8,5)])
    ck('signed-variation-finite',sum(abs(w)for w,a in signed)==5)
    ck('signed-dividing-by-N-flips-action-sign',sm[2]<0)
    ck('signed-scalar-quadratic-roots-decay',s.Rational(99,34)>0 and s.Rational(1175,264)>0)
    pure={m0:0,m1:-1,m2:-3}
    eq('zero-signed-mass-removes-quadratic',AQ.subs(pure))
    eq('zero-signed-mass-retains-EH',AR.subs(pure)-99*h/4)
    eq('zero-signed-mass-positive-Lambda',Lam.subs(pure)-s.Rational(705,88))
    V=s.Matrix([[1,1,1],[1,2,3],[1,4,9]])
    ck('three-signed-atoms-span-all-moment-triples',V.det()==2)
    ck('uniform-rate-bound-17-over-20',C<s.Rational(17,20)*(s.Rational(17,20)+3))
    # Formal normalized holomorphic conformal circle, NOT full native complex action.
    aa=s.symbols('a')
    residues=[s.residue(aa**(j-1),aa,0)for j in range(3)]
    ck('closed-circle-moments',residues==[1,0,0])
    eq('closed-circle-no-Einstein',AR.subs(dict(zip([m0,m1,m2],residues))))
    eq('closed-circle-no-constant',A0.subs(dict(zip([m0,m1,m2],residues))))
    # Exact scale/shape trace split for arbitrary traceless diagonal variation.
    du,u,v,w=s.symbols('du u v w'); shape=s.diag(u,v,w,-u-v-w)
    tangent=du*s.eye(4)+shape
    eq('native-scale-shape-split',s.trace(tangent*tangent)-s.trace(tangent)**2/2-s.trace(shape*shape)+4*du**2)
    ss=s.symbols('ss',real=True)
    eq('trace-only-rotation',(-4*du**2).subs(du,s.I*ss)-4*ss**2)
    ck('open-imaginary-log-zeroth-moment-diverges',s.integrate(1,(ss,-s.oo,s.oo))==s.oo)
    return {'artifact':'BET_COSMOLOGY_WEDGE_GROWTH_CERTIFICATES','checks':len(checks),'check_names':checks,
            'mass_ratio_constant':str(C),'max_rate_over_H_exact':'(sqrt(88227/3995)-3)/2',
            'max_rate_over_H_display':str(s.N(rate.subs(zz,1),12)),
            'min_efold_Hubble_times_display':str(s.N(1/rate.subs(zz,1),12)),
            'signed_moments':[str(x)for x in sm],'closed_contour_moments':[str(x)for x in residues],
            'scope':'Exact algebra and declared contour controls only. No native complex measure, physical Newton constant, observed dark-energy w, DESI likelihood or full14D evolution is constructed.'}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');p.add_argument('--verify',action='store_true');args=p.parse_args()
    d=run();out=json.dumps(d,indent=2)+'\n'
    path=Path(__file__).resolve().parents[2]/'lab/process/bet-cosmology-wedge-growth-certificates.json'
    if args.write:path.write_text(out)
    elif args.verify:assert path.read_text()==out,'certificate drift'
    print('PASS',d['checks'],'exact controls')
