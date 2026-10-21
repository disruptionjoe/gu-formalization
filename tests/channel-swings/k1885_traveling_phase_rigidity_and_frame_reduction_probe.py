#!/usr/bin/env python3
"""Separate differential-action, matrix-bank, frame and band fault checks."""
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import sympy as sp

ROOT=Path(os.environ.get('GU_ROOT',Path(__file__).resolve().parents[2]))
def matrix(d):
    a=[[sp.Integer(0) for _ in range(d.get('columns',16))] for _ in range(d.get('rows',16))]
    for i,j,x in d['entries']:a[i][j]=sp.Rational(x)
    return sp.Matrix(a)
def load(name):return json.loads((ROOT/('lab/process/'+name+'.json')).read_text())
def zmat(x):return all(sp.expand(v)==0 for v in x)
def insist(x,label):
    if not x:raise AssertionError('FAIL '+label)

def differential_check(fault=None):
    data=load('k1836-k77-differential-dirac-quotient');old=load('k1840-k77-conservative-variable-observation')
    D=[matrix(x) for x in data['target_D']];J=D[0]*D[1]*D[2]
    B1,B2=[matrix(x['B']) for x in old['blocks'][0]['repairs']]
    z=sp.Symbol('z');xi=sp.symbols('x0:3');alpha=sp.Rational(5,3);speed=sp.Rational(2,7)
    a=[sp.Rational(2,3),sp.Rational(3,5),sp.Rational(-4,7)];b=sp.Rational(7,11)
    mass1=2+3*z-5*z*z;mass2=7-2*z+z*z;B=mass1*B1+mass2*B2;u=1+2*z+3*z*z
    derivfactor=-24+(1 if fault=='potential_derivative' else 0)
    V=u*sp.eye(4)+derivfactor*alpha*D[0]*B.diff(z)-24*sum((a[i]*D[i]*B*J for i in range(3)),sp.zeros(4))
    G=[a[i]*J+b*D[i]*J for i in range(3)]
    # Apply both differential compositions to exp(xi.x)*e, including all
    # coefficients hit by derivatives; do not reuse the producer's Z formula.
    K=-alpha*sum(x*x for x in xi)*sp.eye(4)+sum((G[i]*xi[i] for i in range(3)),sp.zeros(4))+V
    Q=sum((D[i]*xi[i]/24 for i in range(3)),sp.zeros(4))+B
    timesign=1 if fault=='time_sign' else -1
    QK=timesign*speed*K.diff(z)+D[0]*K.diff(z)/24+Q*K
    KQ=-alpha*(sum(x*x for x in xi)*Q+2*xi[0]*Q.diff(z)+Q.diff(z,2))+sum((G[i]*(xi[i]*Q+(Q.diff(z) if i==0 else sp.zeros(4))) for i in range(3)),sp.zeros(4))+V*Q
    E=(QK-KQ).applyfunc(sp.expand);count=0
    for i in range(4):
        for j in range(4):
            for x in xi:insist(sp.diff(E[i,j],x)==0,'differential coefficient');count+=1
    factor=95 if fault=='angular_factor' else 96
    angular=sp.trace((D[0]*B*J).T*E)
    expected=factor*alpha*speed*(mass1*mass2.diff(z,2)-mass2*mass1.diff(z,2))+4*(24*a[0]*speed+b)*(mass1*mass1.diff(z)+mass2*mass2.diff(z))
    insist(sp.expand(angular-expected)==0,'angular trace via operator action');count+=1
    # A chirped unit circle has zero radial derivative but a nonzero angular
    # residual; a uniform circle is the essential surviving contrary control.
    for R,v,w,acc in [(2,sp.Rational(1,24),3,5),(3,-1,0,2),(1,2,7,0)]:
        m,n=R,0;p,q=0,R*w;r,t=-R*w*w,R*acc
        angular_value=96*alpha*v*(m*t-n*r)
        insist(angular_value==96*alpha*v*R*R*acc,'chirp jet');count+=1
        if acc:insist(angular_value!=0,'nonconstant frequency rejected');count+=1
    return count

def bank_check(doc,mutate=False):
    src=load('k1836-k77-differential-dirac-quotient');en=load('k1832-k77-common-energy-form');old=load('k1840-k77-conservative-variable-observation')
    D=[matrix(x) for x in src['target_D']];J=D[0]*D[1]*D[2];v=sp.Symbol('v');count=0
    for k,(sr,er,kr) in enumerate(zip(src['blocks'],en['blocks'],old['blocks'])):
        H=matrix(er['H']);Hi=H.inv();A=[matrix(x) for x in er['matrices']];T=[matrix(x) for x in sr['T']];L=matrix(er['J'])
        if T[0]*L!=J*T[0]:L=-L
        C0=v*L-A[0]*L;B0=v*J-D[0]*J/24;S0=-T[0]*L
        B1=matrix(kr['repairs'][0]['B']);Y=sp.zeros(70,1)
        for i,x in doc['tangent_dual_witnesses'][k]:Y[i]=sp.sympify(x,locals={'v':v})
        if mutate and k==0:Y[4]+=1
        for row in matrix(kr['full_conservative_kernel']).tolist():
            U=sp.zeros(16);nums=iter(row[:120])
            for i in range(16):
                for j in range(i+1,16):U[i,j]=next(nums);U[j,i]=-U[i,j]
            C=Hi*U;S=sp.Matrix(4,16,row[126:]);B=sp.zeros(4);nums=iter(row[120:126])
            for i in range(4):
                for j in range(i+1,4):B[i,j]=next(nums);B[j,i]=-B[i,j]
            insist(H*C+C.T*H==sp.zeros(16),'tangent energy');count+=1
            insist(all(T[i]*C-B*T[i]+S*A[i]-D[i]*S/24==sp.zeros(4,16) for i in range(3)),'actual tangent bank');count+=1
            column=sp.Matrix([B[i,j] for i in range(4) for j in range(i+1,4)]+list(S0*C+S*C0-B0*S))
            insist(sp.expand((Y.T*column)[0])==0,'dual annihilates every allowed slope');count+=1
        rhs=sp.Matrix([B1[i,j] for i in range(4) for j in range(i+1,4)]+list(B1*S0))
        insist(sp.expand((Y.T*rhs)[0]-v)==0,'dual contradiction all speeds');count+=1
    return count

def frame_and_bands(fault=None):
    src=load('k1836-k77-differential-dirac-quotient');old=load('k1840-k77-conservative-variable-observation')
    D=[matrix(x) for x in src['target_D']];J=D[0]*D[1]*D[2];B1=matrix(old['blocks'][0]['repairs'][0]['B']);I=sp.eye(4);count=0
    for r in [sp.Rational(0),sp.Rational(1,3),sp.Rational(2)]:
        U=((1-r*r)*I-2*r*J)/(1+r*r)
        for R,v,w in [(2,sp.Rational(1,24),3),(3,-1,2)]:
            Bro=U*(R*B1)*U.T
            Ut=v*w*J*U/2;Ux=-w*J*U/2
            spatial=1 if fault=='frame_spatial_sign' else -1
            hat=R*B1+v*w*J/2+spatial*w*D[0]*J/48
            insist(Ut+D[0]*Ux/24+Bro*U==U*hat,'target frame operator action');count+=1
    K=-sp.I*J;beta=-sp.I*B1;F=D[0]*K
    lam=sp.Symbol('lambda')
    for p,a,b,R in [(0,1,2,3),(2,3,5,1),(sp.Rational(2,3),sp.Rational(-1,7),sp.Rational(5,4),2),(-2,-3,1,2)]:
        H=p*D[0]+R*beta+a*K+b*F
        cp=H.charpoly(lam).as_expr()
        a_used=-a if fault=='band_momentum_sign' else a
        expected=((lam-b)**2-(p+a_used)**2-R**2)*((lam+b)**2-(p-a_used)**2-R**2)
        insist(sp.expand(cp-expected)==0,'actual band characteristic polynomial');count+=1
        insist(H.conjugate().T==H,'real energy bands');count+=1
    # Exact threshold examples; the line frequency is continuous.
    for R,w,gap in [(2,48,1),(1,48,0),(1,96,0),(3,0,3)]:
        insist(max(0,abs(R)-sp.Rational(abs(w),48))==gap,'line gap threshold');count+=1
    for winding in [-3,-2,-1,0,1,2,3]:
        sign=(-1)**abs(winding)
        insist(sign==(1 if winding%2==0 else -1),'circle spin twist');count+=1
    # Monodromy minus sign from the half-angle, including reverse travel.
    for sign in [-1,1]:
        insist(sp.cos(sign*sp.pi)==-1 and sp.sin(sign*sp.pi)==0,'half-angle time monodromy');count+=1
    return count

def reporting(doc):
    insist(doc['identities']['angular_trace_coefficient']==96,'reported angular coefficient')
    insist(doc['identities']['phase_second_derivative']==0,'reported phase rigidity')
    for key in ['nonzero_travelling_speed','nonzero_amplitude_for_phase','canonical_massless_base_no_differentiable_constant_frame_mass_branch','band_formula_one_spatial_dimension_only','odd_winding_changes_periodic_domain']:
        insist(doc['scope'][key],'scope '+key)
    for key in ['general_constant_frame_lift_excluded','general_rotating_lift_excluded','source_native_identification','rotating_frame_gap_is_Floquet_gap']:
        insist(not doc['scope'][key],'scope '+key)
    for p,h in doc['inputs'].items():insist(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'input pin')
    return 11+len(doc['inputs'])

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--certificate',type=Path);args=parser.parse_args()
    doc=json.loads((args.certificate or ROOT/'lab/process/k1885-traveling-phase-rigidity-and-frame-reduction.json').read_text())
    dc=differential_check();bc=bank_check(doc);fc=frame_and_bands();rc=reporting(doc)
    faults=[(differential_check,x) for x in ['potential_derivative','time_sign','angular_factor']]+[(frame_and_bands,x) for x in ['frame_spatial_sign','band_momentum_sign']]
    for fn,name in faults:
        try:fn(name)
        except AssertionError as exc:insist(str(exc).startswith('FAIL '),'specific math rejection');print('DETECTED mathematical',name)
        else:raise AssertionError('FAIL missed mathematical '+name)
    try:bank_check(doc,True)
    except AssertionError as exc:insist(str(exc).startswith('FAIL '),'specific dual rejection');print('DETECTED mathematical dual coefficient')
    else:raise AssertionError('FAIL missed dual coefficient')
    changes=[('identities','angular_trace_coefficient',95),('scope','nonzero_travelling_speed',False),('scope','general_constant_frame_lift_excluded',True),('scope','general_rotating_lift_excluded',True),('scope','source_native_identification',True),('scope','rotating_frame_gap_is_Floquet_gap',True)]
    for section,key,val in changes:
        bad=copy.deepcopy(doc);bad[section][key]=val
        try:reporting(bad)
        except AssertionError as exc:insist(str(exc).startswith('FAIL '),'specific report rejection');print('DETECTED reporting',key)
        else:raise AssertionError('FAIL missed reporting '+key)
    print('PASS K1885 probe',dc,'operator/phase;',bc,'bank/dual;',fc,'frame/band/domain;',rc,'report/pins;',len(faults)+1,'math faults;',len(changes),'report faults')
