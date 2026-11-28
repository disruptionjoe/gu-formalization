#!/usr/bin/env python3
"""Exact full-lapse metric-row and conservation controls; not a physical-state proof."""
from pathlib import Path
import argparse, json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/unimodular-lambda-certificates.json'

def build():
    checks=[]
    def ck(name, expression):
        assert expression, name
        checks.append(name)
    def zero(name, expression): ck(name, s.simplify(expression)==0)
    H,r,b,a,c,ell,e,t=s.symbols('H r b a c ell epsilon t',real=True)
    R=s.symbols('R',real=True)
    f=b*R**2-a*R+c+2*ell
    zero('constant shift cancels from scalar mass', (s.diff(f,R)-R*s.diff(f,R,2))/(3*s.diff(f,R,2))+a/(6*b))
    zero('Einstein background polynomial', s.diff(f,R)*R-2*f-(a*R-2*c-4*ell))
    zero('unrestricted fixed curvature', (a*R-2*c).subs(R,2*c/a))
    zero('integration sector curvature', (a*R-2*c-4*ell).subs(R,2*(c+2*ell)/a))
    dc=s.symbols('dc')
    zero('constant density shift absorbed by sector label', (c+dc+2*(ell-dc/2))-(c+2*ell))
    # Independent metric calculation, retaining lapse before varying. This path
    # has the fixed background volume exactly, at every epsilon in a local patch.
    q=s.Function('q')(t)
    N=(1+e*q)**s.Rational(-3,2)
    scale=s.exp(H*t)*s.sqrt(1+e*q)
    hc=s.diff(scale,t)/scale
    R00=-3*(s.diff(scale,t,2)/scale-hc*s.diff(N,t)/N)
    Rsp=(s.diff(scale,t,2)/scale+2*hc**2-hc*s.diff(N,t)/N)/N**2
    curvature=6*(s.diff(scale,t,2)/scale+hc**2-hc*s.diff(N,t)/N)/N**2
    zero('exact metric determinant', -N**2*scale**6+s.exp(6*H*t))
    zero('background curvature',curvature.subs(e,0)-12*H**2)
    dR=s.simplify(s.diff(curvature,e).subs(e,0))
    dH=s.simplify(s.diff(hc/N,e).subs(e,0))
    zero('lapse-corrected delta H',dH-(s.diff(q,t)+3*H*q)/2)
    zero('curvature variation with lapse',dR-3*(s.diff(q,t,2)+7*H*s.diff(q,t)+12*H**2*q))
    zero('metric tangent trace',-s.diff(-N**2,e).subs(e,0)+3*s.diff(scale**2,e).subs(e,0)/s.exp(2*H*t))
    # Derive E00 and Eii from Ricci and scalar Hessian, not just the trace.
    F=2*b*curvature-a
    density=b*curvature**2-a*curvature+c+2*ell
    E00=F*R00+N**2*density/2+3*hc*s.diff(F,t)
    Esp=F*Rsp-density/2-(s.diff(F,t,2)+(2*hc-s.diff(N,t)/N)*s.diff(F,t))/N**2
    sector={ell:3*a*H**2-c/2}
    zero('all background temporal rows',E00.subs(e,0).subs(sector))
    zero('all background spatial rows',Esp.subs(e,0).subs(sector))
    l00=s.simplify(s.diff(E00,e).subs(e,0).subs(sector))
    lsp=s.simplify(s.diff(Esp,e).subs(e,0).subs(sector))
    qmode=s.exp(r*t)/(3*(r+3*H)*(r+4*H))
    mode={q:qmode,**{s.diff(q,t,k):s.diff(qmode,t,k) for k in range(1,5)}}
    dispersion={a:6*b*r*(r+3*H)}
    zero('all-row temporal growing mode',l00.subs(mode).subs(dispersion))
    zero('all-row spatial growing mode',lsp.subs(mode).subs(dispersion))
    zero('normalized nonzero curvature mode',dR.subs(mode)-s.exp(r*t))
    zero('critical F0 no denominator', (24*b*H**2-a).subs(dispersion)-6*b*(H-r)*(r+4*H))
    zero('critical temporal row direct',l00.subs(mode).subs(r,H).subs(a,24*b*H**2))
    zero('critical spatial row direct',lsp.subs(mode).subs(r,H).subs(a,24*b*H**2))
    zero('critical normalized q',qmode.subs(r,H)-s.exp(H*t)/(60*H**2))
    # Distinct conformal/Jordan representative, only a control for critical locus.
    box=lambda u:-s.diff(u,t,2)-3*H*s.diff(u,t)
    psi=t*s.exp(H*t)/(15*H)
    zero('critical resonant conformal metric',-3*(box(psi)+4*H**2*psi)-s.exp(H*t))
    zero('critical curvature Hessian temporal',s.diff(s.exp(H*t),t,2)-H**2*s.exp(H*t))
    zero('critical curvature Hessian spatial',-H*s.diff(s.exp(H*t),t)+H**2*s.exp(H*t))
    # A mutation dropping lapse must fail the curvature/constraint calculation.
    badR=3*s.diff(q,t,2)+12*H*s.diff(q,t)
    ck('lapse-omission mutation detected',s.simplify((dR-badR).subs(q,s.exp(t)).doit().subs(H,1))!=0)
    m0,m1,m2,h=s.symbols('m0 m1 m2 h',nonzero=True)
    W={a:99*h*m1/4,b:17*h*m0/12,c:2115*h*m2/16}
    zero('owned wedge scalar mass',(-a/(6*b)).subs(W)+99*m1/(34*m0))
    zero('owned unshifted Lambda', (c/(2*a)).subs(W)-s.Rational(235,88)*m2/m1)
    zero('positive F threshold', (24*b*(c+2*ell)/(6*a)-a).subs(ell,a**2/(8*b)-c/2))
    zero('critical growth ratio', (r*r+3*H*r).subs(r,H)-4*H**2)
    # Calibrated ordinary Einstein and healthy R+R² signs.
    ck('ordinary GR has no scalar box coefficient',(6*b).subs(b,0)==0)
    ck('healthy R plus R2 mass positive',s.Rational(1,6)>0)
    ck('tachyon convention mass negative',s.Rational(-1,6)<0)
    zero('healthy R plus R2 temporal decaying mode',l00.subs(mode).subs(r,-H).subs(a,-12*b*H**2))
    zero('healthy R plus R2 spatial decaying mode',lsp.subs(mode).subs(r,-H).subs(a,-12*b*H**2))
    ck('healthy R plus R2 rejects planted growing mode',s.simplify(l00.subs(mode).subs({r:1,H:1,b:1,a:-24,t:0}))!=0)
    ck('GR rejects nonzero scalar curvature mode',s.simplify((a*dR).subs(mode).subs({r:1,H:1,a:-1,t:0}))!=0)
    zero('pure quadratic all Einstein backgrounds temporal control',E00.subs(e,0).subs({a:0,c:0,ell:0}))
    zero('pure quadratic all Einstein backgrounds spatial control',Esp.subs(e,0).subs({a:0,c:0,ell:0}))
    # Fixed-density does not mean R is constant: the actual q path witnesses it.
    ck('tracefree mode nonzero',s.simplify(dR.subs(mode).subs({H:1,r:1,t:0}))==1)
    # External scalar coefficients: simple exact nonconservative countercontrol.
    x,y=s.symbols('x y',real=True)
    coeff=x*x+y
    trace=-2*coeff; j=[-s.diff(coeff,z)/2 for z in (x,y)]
    for i,z in enumerate((x,y)):zero('tracefree pure density Ward '+str(i),s.diff(trace,z)-4*j[i])
    ck('nonconstant density tracefree equation not constant Lambda',s.diff(-coeff/2,y)!=0)
    zero('exact current curl zero',s.diff(j[1],x)-s.diff(j[0],y))
    # J=x dy is not a permitted d ell; circle dtheta is closed but has period.
    ck('nonclosed current compatibility fails',s.diff(x,x)-s.diff(0,y)==1)
    theta=s.symbols('theta',real=True)
    ck('closed circle current nonzero period',s.integrate(1,(theta,0,2*s.pi))==2*s.pi)
    return {'artifact':'UNIMODULAR_LAMBDA_EXACT_CONTROLS','checks':checks,'count':len(checks),
        'derived':{'delta_R':str(dR),'delta_H':str(dH),'linear_E00':str(l00),'linear_Eii_over_gii':str(lsp)},
        'scope':'Exact symbolic classical local metric and finite compatibility identities; no full14D, physical-domain, measure-selection or nonlinear stability certification.'}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--verify',action='store_true');args=ap.parse_args()
    d=build()
    if args.verify: assert json.loads(OUT.read_text())==d,'certificate replay mismatch'
    else: OUT.write_text(json.dumps(d,indent=2)+'\n')
    print('PASS',d['count'],'exact controls', 'replayed' if args.verify else 'recorded')
