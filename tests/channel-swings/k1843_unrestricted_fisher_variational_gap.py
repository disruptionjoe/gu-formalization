#!/usr/bin/env python3
"""Symbolic controls for the written unrestricted Fisher theorem."""
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]

def produce():
    checks={}
    def ck(name,value):
        checks[name]=bool(value);assert value,name
    p,p1,p2,h,h1,h2,e=s.symbols('p p1 p2 h h1 h2 e',real=True)
    # Euler derivative of p1²/p uses total derivative in independent jets.
    L=p1*p1/p
    dLdp=s.diff(L,p);dLdp1=s.diff(L,p1)
    total=s.diff(dLdp1,p)*p1+s.diff(dLdp1,p1)*p2
    ck('Euler_jet',s.simplify(dLdp-total-(-2*p2/p+p1*p1/p**2))==0)
    Le=(p1+e*h1)**2/(p+e*h)
    ck('second_variation',s.simplify(s.diff(Le,e,2)-2*(h1*p-h*p1)**2/(p+e*h)**3)==0)
    u,u1,u2=s.symbols('u u1 u2',nonzero=True)
    ck('sqrt_p_Euler',s.simplify((-2*p2/p+p1*p1/p**2).subs({p:u*u,p1:2*u*u1,p2:2*u1*u1+2*u*u2})+4*u2/u)==0)
    x,M,v=s.symbols('x M v',positive=True)
    gauss=s.exp(-(x-M)**2/(2*v))
    R=-2*s.diff(gauss,x,2)/gauss+(s.diff(gauss,x)/gauss)**2
    ck('tail_polynomial',s.simplify(R-(2/v-(x-M)**2/v**2))==0)
    ck('tail_linear_obstruction',s.expand(R).coeff(x,1)==2*M/v**2)
    a,r=s.symbols('a r',real=True);v0=1-a*a
    ck('feasible_variance',a*a+v0==1)
    ck('feasible_fourth',s.expand(a**4+6*a*a*v0+3*v0*v0)==3-2*a**4)
    m=s.symbols('m');ou=s.expand(r**4*m+6*r*r*(1-r*r)+3*(1-r*r)**2)
    ck('OU_fourth',s.expand(ou-(3+r**4*(m-3)))==0)
    bump=(1-x*x)**8;hh=s.diff(bump,x,6)
    for j in (0,2,4):ck('moment_'+str(j),s.integrate(x**j*hh,(x,-1,1))==0)
    for j in range(6):ck('boundary_'+str(j),s.diff(bump,x,j).subs(x,1)==0 and s.diff(bump,x,j).subs(x,-1)==0)
    ck('nonzero_descent_control',s.integrate(x**6*hh,(x,-1,1))==s.factorial(6)*s.integrate(bump,(x,-1,1)))
    b,kap,I,lam=s.symbols('b kap I lam');energy=lam**2*I+a/lam**2+b*kap/lam**4
    ck('virial',s.diff(energy,lam).subs(lam,1)==2*I-2*a-4*b*kap)
    ck('ground_energy',s.expand((I+a+b*kap).subs(I,a+2*b*kap))==2*a+3*b*kap)
    pp,qq,dp,dq=s.symbols('pp qq dp dq',positive=True)
    gap=(dp*dp/pp+dq*dq/qq)/2-(dp+dq)**2/(2*(pp+qq))
    ck('strict_convexity_defect',s.factor(gap)==(dp*qq-dq*pp)**2/(2*pp*qq*(pp+qq)))
    return {'artifact':'K1843','scope':'even_densities_second_moment_1_fourth_k_between_1_and_3','mathematical_checks':checks,
        'analytic_proof':'explorations/k1843-unrestricted-fisher-variational-gap-2026-10-20.md',
        'existence_proof':'relaxed fourth moment, compactness, strict OU improvement enforces saturation',
        'unique_positive_quartic_ground_state':True,'strict_budget_improvement':'all positive relative Fisher budgets; uses K1825 attainment','finite_common_variance_mixtures_stationary':False,
        'effective_gap':False,'unrestricted_endpoint_expansion':False,'GU_physics_credit':False,'canon_promotion':False}
if __name__=='__main__':
    out=produce();(ROOT/'lab/process/k1843-unrestricted-fisher-variational-gap.json').write_text(json.dumps(out,indent=2)+'\n');print('K1843 exact groups:',len(out['mathematical_checks']))
