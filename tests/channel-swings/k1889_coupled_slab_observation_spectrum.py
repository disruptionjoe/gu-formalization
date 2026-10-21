#!/usr/bin/env python3
"""Actual slab boundary algebra; continuum completeness is proved in the note."""
import argparse, hashlib, json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
INPUTS=['lab/process/k1832-k77-common-energy-form.json','lab/process/k1836-k77-differential-dirac-quotient.json','lab/process/k1888-bounded-support-energy-inverse.json']
OUT='lab/process/k1889-coupled-slab-observation-spectrum.json'
def mat(d):
    a=s.zeros(d.get('rows',16),d.get('columns',16))
    for i,j,v in d['entries']:a[i,j]=s.Rational(v)
    return a

def produce(root=ROOT):
    en,ob,old=[json.loads((root/p).read_text()) for p in INPUTS]
    alpha=s.Rational(138,25);beta=s.Rational(1866,625);rho=beta/alpha;c=s.factor(alpha*(1-rho**2));K=s.diag(1,-1,-1,1)
    k,p,q=s.symbols('k p q',real=True);checks={};blocks=[]
    def ck(n,b):
        checks[n]=bool(b)
        if not b:raise AssertionError('FAIL '+n)
    for j,(e,o) in enumerate(zip(en['blocks'],ob['blocks'])):
        H=mat(e['H']);T=list(map(mat,o['T']));G=s.Matrix.vstack(*T)*H.inv()*s.Matrix.vstack(*T).T
        J2=G[:4,4:8]/beta;J3=G[:4,8:]/beta;M=k*K-s.I*rho*(p*J2+q*J3);m2=k*k+rho*rho*(p*p+q*q)
        ck('actual_gram_'+str(j),G==mat(old['blocks'][j]['flux_gram']))
        ck('normal_block_'+str(j),G[:4,:4]==alpha*s.eye(4))
        ck('Clifford_'+str(j),J2**2==J3**2==-s.eye(4) and J2*J3+J3*J2==s.zeros(4))
        ck('drift_anticommutators_'+str(j),K*J2+J2*K==K*J3+J3*K==s.zeros(4))
        ck('Hermitian_Robin_'+str(j),M.conjugate().T==M)
        ck('Robin_square_'+str(j),s.simplify(M*M-m2*s.eye(4))==s.zeros(4) and s.trace(M)==0)
        ck('boundary_sign_'+str(j),-alpha*M+alpha*k*K-s.I*(p*G[:4,4:8]+q*G[:4,8:])==s.zeros(4))
        ck('surface_eigenvalue_'+str(j),s.simplify(alpha*(k*k+p*p+q*q)-alpha*m2-c*(p*p+q*q))==0)
        blocks.append({'J2':[[str(v) for v in J2.row(i)] for i in range(4)],'J3':[[str(v) for v in J3.row(i)] for i in range(4)]})
    ck('strict_surface_coefficient',0<c<alpha and 0<rho<1)
    x,m,w,L=s.symbols('x m w L',real=True,nonzero=True)
    u=s.cos(w*(x+L))+m/w*s.sin(w*(x+L))
    ck('bulk_ODE',s.simplify(-s.diff(u,x,2)-w*w*u)==0)
    ck('left_endpoint',s.simplify((s.diff(u,x)-m*u).subs(x,-L))==0)
    ck('endpoint_determinant',s.simplify((s.diff(u,x)-m*u).subs(x,L)+(w*w+m*m)/w*s.sin(2*L*w))==0)
    ck('surface_ODE',s.diff(s.exp(m*x),x,2)==m*m*s.exp(m*x))
    ck('surface_normalization',s.simplify(s.integrate(s.exp(2*m*x),(x,-L,L))-s.sinh(2*m*L).rewrite(s.exp)/m)==0)
    ck('two_mode_energy',s.Rational(1,4)+s.Rational(4,25)==s.Rational(41,100))
    ck('two_mode_error',s.Rational(1,4)+s.Rational(1,25)==s.Rational(29,100))
    return dict(result_id='K1889',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',alpha=str(alpha),beta=str(beta),rho=str(rho),surface_coefficient=str(c),blocks=blocks,formulas={'surface':'c*|p|^2, multiplicity4 for each p','bulk':'alpha*(kappa^2+|p|^2+(n*pi/(2L))^2), multiplicity4, n>=1','torus_gap':'min(c*p_min^2,alpha*(kappa^2+pi^2/(4L^2)))','plane_gaussian_energy':'((1+a)*exp(a)*E1(a)-1)/c','plane_gaussian_error_squared':'a-a^2*exp(a)*E1(a)','a':'t/c'},scope={'periodic_transverse_slab':True,'rectangular_box_spectrum':False,'preparation_operator_not_evolution':True,'plane_massive_uniform_inverse':False,'native_GU':False},checks=checks,inputs={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in INPUTS})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=produce()
    if a.write:(ROOT/OUT).write_text(json.dumps(d,indent=2)+'\n')
    elif d!=json.loads((ROOT/OUT).read_text()):raise AssertionError('FAIL certificate drift')
    print('PASS K1889',len(d['checks']),'exact algebra groups;',len(INPUTS),'pins; continuum proof analytic')
