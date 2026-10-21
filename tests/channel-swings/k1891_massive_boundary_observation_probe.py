#!/usr/bin/env python3
"""Independent trace-jet, scalar ODE and actual-boundary fault controls."""
import copy,json,hashlib
import sympy as s
from k1891_massive_boundary_observation import ROOT,INPUTS,OUT,mat

def verify(report, fault=None):
    count=0
    def ck(name,b):
        nonlocal count
        if not b:raise AssertionError('FAIL '+name)
        count+=1
    en,ob,rep=[json.loads((ROOT/p).read_text()) for p in INPUTS];D=list(map(mat,ob['target_D']));alpha=s.Rational(report['alpha']);p,q,R=s.symbols('p q R',real=True)
    for j,(e,o,r,br) in enumerate(zip(en['blocks'],ob['blocks'],rep['blocks'],report['blocks'])):
        H=mat(e['H']);A=list(map(mat,e['matrices']));T=list(map(mat,o['T']));C,B,S=[mat(r['repairs'][0][k]) for k in ['C','B','S']];L=mat(br['boundary']);K=mat(br['mass_K']);P=mat(br['target_plus']);M=mat(br['target_minus']);F=H*A[0]
        if fault=='boundary' and j==0:L=L.copy();L[0,0]+=1
        ck('positive_energy',H==H.T and all(H[:n,:n].det()>0 for n in range(1,17)))
        ck('maximal_selforthogonal',L.rank()==8 and L.T*F*L==s.zeros(8))
        # Arbitrary value and time-derivative traces in L; independent normal jets.
        i=s.I;Z=i*(p*A[1]+q*A[2])+R*C
        jet1=A[0].inv()*L;jet0=-A[0].inv()*Z*L
        y1=T[0]*jet1;y0=T[0]*jet0+(i*(p*T[1]+q*T[2])+R*S)*L
        ck('all_boundary_value_jets',all(s.expand(x)==0 for x in P*y0))
        ck('all_boundary_time_jets',P*y1==s.zeros(4,8))
        ck('target_trace',M*D[0]*M==s.zeros(4) and M.rank()==2)
        ann=s.Matrix.hstack(*L.T.nullspace()).T
        sign=-1 if fault=='Robin' else 1
        adj=H.inv()*(-T[0].T*(24*R*sign*M)+(-i*(p*T[1].T+q*T[2].T)+R*S.T)*M)
        ck('adjoint_boundary_values',all(s.expand(x)==0 for x in ann*adj))
        ck('adjoint_boundary_derivatives',ann*H.inv()*T[0].T*P==s.zeros(8,4))
        ck('source_target_energy_scale',T[0]*H.inv()*T[0].T==alpha*s.eye(4))
        ck('radial_source_invisible',(T[0]*mat(br['fast_boundary']))==s.zeros(4,6))
    x,k,kap=s.symbols('x k kap',real=True, nonzero=True)
    u=s.sin(k*x);v=s.cos(k*x)+kap*s.sin(k*x)/k
    masscoef=0 if fault=='mass_gap' else 1
    lam=k*k+masscoef*kap*kap
    for f in [u,v]:ck('bulk_ODE',s.simplify(-s.diff(f,x,2)+kap*kap*f-lam*f)==0)
    ck('Robin_endpoint0',s.simplify(s.diff(v,x).subs(x,0)-kap*v.subs(x,0))==0)
    ck('Robin_endpoint_pi',s.simplify((s.diff(v,x)-kap*v).subs(x,s.pi/k))==0)
    g=s.exp(kap*x);ck('surface_ODE',s.diff(g,x,2)==kap*kap*g)
    ck('surface_boundary',s.diff(g,x)==kap*g)
    g=s.exp(x*x/2);ck('variable_profile_ground',s.simplify(-s.diff(g,x,2)+(x*x+1)*g)==0)
    # Dirichlet/Robin partner via factorization, independently symbolic test polynomial.
    f=x**4+2*x*x+1;Kx=x*x+1
    d=lambda h:s.diff(h,x)+Kx*h
    ds=lambda h:-s.diff(h,x)+Kx*h
    ck('variable_partner_DstarD',s.expand(ds(d(f))-(-s.diff(f,x,2)+(Kx*Kx-s.diff(Kx,x))*f))==0)
    ck('variable_partner_DDstar',s.expand(d(ds(f))-(-s.diff(f,x,2)+(Kx*Kx+s.diff(Kx,x))*f))==0)
    for path,h in report['inputs'].items():ck('input_pin',hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h)
    ck('surface_multiplicity',report['spectrum']['missing_p0_modes']==2)
    return count
if __name__=='__main__':
    report=json.loads((ROOT/OUT).read_text());n=verify(report);caught=[]
    for name in ['boundary','Robin','mass_gap']:
        try:verify(report,name)
        except AssertionError as e:
            assert str(e).startswith('FAIL ');caught.append(str(e))
        else:raise AssertionError('FAIL undetected '+name)
    for key,value in [('alpha','1')]:
        bad=copy.deepcopy(report);bad[key]=value
        try:verify(bad)
        except AssertionError as e:assert str(e).startswith('FAIL ');caught.append(str(e))
        else:raise AssertionError('FAIL undetected serialized coefficient')
    print('PASS K1891 probe',n,'trace/ODE/pin controls;',len(caught),'faults:',caught)
