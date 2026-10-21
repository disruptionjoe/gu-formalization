#!/usr/bin/env python3
"""Actual target Clifford checks and exact UV/one-dimensional integration coefficients."""
import argparse,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2];OUT='lab/process/k1896-local-phase-vacuum-boundary.json'
INPUTS=['lab/process/k1836-k77-differential-dirac-quotient.json','lab/process/k1840-k77-conservative-variable-observation.json','lab/process/k1892-causal-observation-algebra.json']
def mat(d):
    a=s.zeros(d['rows'],d['columns'])
    for i,j,v in d['entries']:a[i,j]=s.Rational(v)
    return a
def zero(m):return all(s.simplify(x)==0 for x in m)
def produce():
    ob,rep,_=[json.loads((ROOT/p).read_text()) for p in INPUTS]
    D=list(map(mat,ob['target_D']));M=-s.I*mat(rep['blocks'][0]['repairs'][0]['B']);G=D+[M];checks={}
    def ck(n,b):
        checks[n]=bool(b)
        if not b:raise AssertionError('FAIL '+n)
    for i,A in enumerate(G):
        ck('Hermitian_'+str(i),A==A.H);ck('trace_zero_'+str(i),s.trace(A)==0)
        for j,B in enumerate(G):ck(f'Clifford_{i}{j}',A*B+B*A==(2*s.eye(4) if i==j else s.zeros(4)))
    products=[]
    for mask in range(16):
        A=s.eye(4)
        for j in range(4):
            if (mask>>j)&1:A=A*G[j]
        products.append(A.reshape(16,1))
    ck('complex_Clifford_full_matrix_algebra',s.Matrix.hstack(*products).rank()==16)
    eps0,dt,rate,delta=s.symbols('epsilon dt g delta',real=True)
    ck('binary_smooth_pulse_noise_curvature',s.diff(s.cos(eps0*rate*delta*dt),dt,2).subs(dt,0)==-eps0**2*rate**2*delta**2)
    p=s.symbols('p1:4',real=True);q=s.symbols('q1:4',real=True);mu=s.symbols('mu',real=True);ep,eq=s.symbols('Ep Eq',positive=True)
    Hp=sum((p[i]*D[i] for i in range(3)),s.zeros(4))+mu*M
    Hq=sum((q[i]*D[i] for i in range(3)),s.zeros(4))+mu*M
    overlap=s.trace((s.eye(4)+Hp/ep)*(s.eye(4)-Hq/eq)/4)
    ck('actual_overlap',s.simplify(overlap-(1-(sum(p[i]*q[i] for i in range(3))+mu**2)/(ep*eq)))==0)
    # Rotate q to radial direction: a=n.k and b=|k|^2. UV expansion by epsilon=1/r.
    eps,a,b=s.symbols('eps a b',real=True)
    cos=(1+a*eps+mu**2*eps**2)/s.sqrt((1+mu**2*eps**2)*(1+2*a*eps+(b+mu**2)*eps**2))
    uv=s.expand(s.series(1-cos,eps,0,3).removeO()).coeff(eps,2)
    ck('mass_independent_UV_coefficient',s.simplify(uv-(b-a*a)/2)==0)
    z,k,L,c=s.symbols('z k Lambda c',positive=True)
    angular=s.integrate((1-z*z)/2,(z,-1,1))*2*s.pi
    ck('sphere_overlap_integral',angular==4*s.pi/3)
    coeff=s.simplify(angular/(2*s.pi)**3)
    ck('three_dimensional_number_coefficient',coeff==1/(6*s.pi**2))
    # Energy-weighted diagnostic, not the density-matrix energy of an unspecified cutoff.
    ck('three_dimensional_energy_weight_coefficient',s.integrate(2*c*z,(z,0,L))*coeff==c*L*L/(6*s.pi**2))
    # One massless spatial dimension, target spin rank4: two states in each velocity.
    ck('one_dimensional_crossing_length',s.integrate(2,(z,0,k))==2*k)
    ck('one_dimensional_number_coefficient',s.Rational(2)/(2*s.pi)==1/s.pi)
    ck('one_dimensional_energy_coefficient',s.integrate(2*c*k,(z,0,k))/(2*s.pi)==c*k*k/s.pi)
    # Explicit smooth phase u=(x-i a)/(x+i a), a>0; |vhat(k)|^2=8*pi*a^2 exp(-2 a k), k>0.
    aa=s.symbols('a0',positive=True)
    density=8*s.pi*aa**2*s.exp(-2*aa*k)
    ck('rational_phase_pair_number',s.integrate(k*density,(k,0,s.oo))/s.pi==2)
    ck('rational_phase_energy',s.integrate(c*k*k*density,(k,0,s.oo))/s.pi==2*c/aa)
    x=s.symbols('x',real=True);u=(x-s.I*aa)/(x+s.I*aa)
    ck('rational_phase_unitary',s.simplify(u*s.conjugate(u)-1)==0)
    ck('rational_phase_gradient',s.simplify(s.diff(u,x)*s.conjugate(s.diff(u,x))-4*aa**2/(x*x+aa*aa)**2)==0)
    ck('rational_phase_gradient_integral',s.integrate(4*aa**2/(x*x+aa*aa)**2,(x,-s.oo,s.oo))==2*s.pi/aa)
    return dict(result_id='K1896',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',
        overlap='1-(p.q+mu^2)/(sqrt(p^2+mu^2)*sqrt(q^2+mu^2))',
        number_asymptotic='Lambda/(6*pi^2)*integral |grad u|^2',
        energy_weighted_diagnostic='c*Lambda^2/(6*pi^2)*integral |grad u|^2',
        one_dimension=dict(number='(1/pi)*integral |k|*|vhat(k)|^2',energy='(c/pi)*integral k^2*|vhat(k)|^2',rational_phase_number=2,rational_phase_energy='2*c/a'),
        temporal_Born=dict(kernel='-i*(2*pi)^(-3/2)*theta_hat(p-q)*g_tilde(c*(Ep+Eq))*Pplus(p)*Pminus(q)',smooth_compact_switch_finite_all_energy_moments=True,all_orders_implementation_proved=False),
        smooth_pulse_repair=dict(mass_condition='R>0',potential='epsilon*g(t)*theta(x)*I',imported_theorem='Deckert-Merkl 1505.06039v2 Theorem1.5 and Corollary1.4',all_order_sea_implementability=True,finite_binary_mixture_causal_and_normal=True,finite_energy_all_orders=False,Markov_semigroup=False),
        scope=dict(constant_mass_rank4_target=True,nonconstant_smooth_compact_phase_not_sea_implementable_in_3D=True,algebraic_CAR_invalid=False,native_GU=False),
        checks=checks,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=produce()
    if a.write:(ROOT/OUT).write_text(json.dumps(d,indent=2)+'\n')
    else:assert d==json.loads((ROOT/OUT).read_text()),'FAIL report drift'
    print('PASS K1896',len(d['checks']),'exact coefficient/Clifford groups;',len(INPUTS),'pins; continuum estimates in note')
