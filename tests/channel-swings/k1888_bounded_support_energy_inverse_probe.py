#!/usr/bin/env python3
"""Independent row, domain-countercontrol, primitive and budget checks for K1888."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import sympy as s

INPUTS = ['lab/process/k1832-k77-common-energy-form.json',
          'lab/process/k1836-k77-differential-dirac-quotient.json',
          'lab/process/k1840-k77-conservative-variable-observation.json',
          'lab/process/k1883-compact-support-observation-range.json',
          'lab/process/k1886-support-bounded-observation-approximation.json']
OUT = 'lab/process/k1888-bounded-support-energy-inverse.json'
COUNTS = {'mathematical': 0, 'report_or_pin': 0}


def check(condition, name, category='mathematical'):
    if not condition:
        raise AssertionError('FAIL '+name)
    COUNTS[category] += 1


def read_matrix(data):
    rows = data.get('rows', 16)
    cols = data.get('columns', 16)
    values = {(i,j): s.Rational(x) for i,j,x in data['entries']}
    return s.Matrix(rows, cols, lambda i,j: values.get((i,j), s.S.Zero))


def zero(M):
    return all(s.simplify(v) == 0 for v in M)


def check_gram(G):
    I = s.eye(12)
    check(G == G.T, 'Gram symmetry')
    check((625*G-1584*I)*(625*G-7182*I) == s.zeros(12), 'Gram polynomial')
    P = (625*G-1584*I)/5598
    check(P*P == P and s.trace(P) == 4, 'Gram spectral multiplicities')
    return P


def baseline(root, certificate):
    en, ob, vr, _, _ = [json.loads((root/p).read_text()) for p in INPUTS]
    gamma, upper, alpha = s.Rational(1584,625), s.Rational(7182,625), s.Rational(138,25)
    original_grams = []
    for j,(er,tr,mr,stored) in enumerate(zip(en['blocks'],ob['blocks'],vr['blocks'],certificate['blocks'])):
        H = read_matrix(er['H'])
        Hi = H.inv()
        T = [read_matrix(v) for v in tr['T']]
        rows = [T[i][a,:] for i in range(3) for a in range(4)]
        # Independently accumulate row pairings, rather than read producer Gram.
        G = s.Matrix(12,12,lambda a,b: sum(rows[a][i]*Hi[i,k]*rows[b][k] for i in range(16) for k in range(16)))
        original_grams.append(G)
        P = check_gram(G)
        check(G == read_matrix(stored['flux_gram']), 'serialized Gram matches row pairings')
        Z = s.Matrix.vstack(*T)
        N = read_matrix(stored['flux_right_inverse'])
        check(Z*N == s.eye(12), 'flux reconstruction')
        check(N.T*H*N == G.inv(), 'source metric flux energy')
        check(H*N == Z.T*G.inv(), 'weighted adjoint normalization')
        for v in [s.ones(12,1), s.Matrix(range(12)), s.Matrix([(-1)**i*(i+1) for i in range(12)])]:
            check((v.T*G*v)[0] >= gamma*(v.T*v)[0], 'positive Gram lower control')
            check((v.T*G*v)[0] <= upper*(v.T*v)[0], 'positive Gram upper control')
            flux = Z*(N*v)
            check(flux == v, 'actual flux sample')
            check(((N*v).T*H*(N*v))[0] == (v.T*G.inv()*v)[0], 'actual energy sample')
        for i in range(3):
            check(T[i]*Hi*T[i].T == alpha*s.eye(4), 'single directional energy alpha')
        check(G[:4,4:8]*s.eye(4)[:,0] == s.Matrix([0,0,s.Rational(1866,625),0]), 'actual scalar-Neumann boundary failure')
        S = read_matrix(mr['repairs'][0]['S'])
        K = s.diag(1,-1,-1,1)
        check(S == 24*K*T[0], 'signed drift factorization')
        # Exhibit a gamma eigenvector so replacing gamma by alpha is falsified.
        v = (s.eye(12)-P)[:,0]
        check(v != s.zeros(12,1) and G*v == gamma*v, 'lower eigendirection exists')
        check((v.T*(G-alpha*s.eye(12))*v)[0] < 0, 'alpha lower bound false')
    # Elementary interval spectra. These check the ODE and endpoints, not completeness.
    x=s.symbols('x',real=True)
    for length in (s.Rational(1),s.Rational(3,2),s.Rational(4)):
        for drift in (s.Rational(0),s.Rational(1,3),s.Rational(-2)):
            ground=s.exp(drift*x)
            check(s.diff(ground,x)-drift*ground == 0, 'drift ground mode')
            for n in (1,2):
                freq=n*s.pi/length
                u=s.cos(freq*x)+drift/freq*s.sin(freq*x)
                check(s.simplify(-s.diff(u,x,2)+drift**2*u-(drift**2+freq**2)*u)==0,'interval ODE')
                check(s.simplify((s.diff(u,x)-drift*u).subs(x,0))==0,'interval left boundary')
                check(s.simplify((s.diff(u,x)-drift*u).subs(x,length))==0,'interval right boundary')
    # Independent compact polynomial primitive on (0,1)^3. Extension by zero
    # has enough finite regularity for these norm/derivative controls, not C-infinity.
    x,y,z=s.symbols('x y z',real=True)
    rho=lambda v:30*v**2*(1-v)**2
    drho=lambda v:s.diff(rho(v),v)
    for v in (x,y,z):
        check(s.integrate(rho(v),(v,0,1))==1,'unit bump integral')
        check(rho(v).subs(v,0)==rho(v).subs(v,1)==0,'bump endpoint')
    # Nonseparable sum triggers both marginal subtraction terms.
    h=drho(x)*rho(y)*rho(z)+rho(x)*drho(y)*rho(z)+rho(x)*rho(y)*drho(z)
    H1=s.integrate(h,(x,0,1));H2=s.integrate(H1,(y,0,1))
    F1=s.integrate(h-rho(x)*H1,x);F1-=F1.subs(x,0)
    F2=rho(x)*s.integrate(H1-rho(y)*H2,y);F2-=F2.subs(y,0)
    F3=rho(x)*rho(y)*s.integrate(H2,z);F3-=F3.subs(z,0)
    check(s.expand(s.diff(F1,x)+s.diff(F2,y)+s.diff(F3,z)-h)==0,'tensor primitive exact divergence')
    for Fi,coordinate in ((F1,x),(F2,y),(F3,z)):
        check(s.expand(Fi.subs(coordinate,0))==0 and s.expand(Fi.subs(coordinate,1))==0,'primitive both endpoint traces')
    for drift in (s.Rational(0),s.Rational(1,2),s.Rational(-3)):
        f1,f2,f3=[s.exp(-drift*x)*Fi for Fi in (F1,F2,F3)]
        check(s.simplify(s.diff(f1,x)+drift*f1+s.diff(f2,y)+s.diff(f3,z)-s.exp(-drift*x)*h)==0,'weighted primitive divergence')
    # Exact finite spectral consumers test the completion-of-squares identity.
    # Use squared rational singular values so all source vectors remain rational.
    for singular in ((1,2,3),(s.Rational(1,2),1,4),(2,3,5)):
        A=s.diag(*singular);lam=[v*v for v in singular]
        for target in (s.Matrix([1,2,-1]),s.Matrix([0,3,1])):
            E=sum(target[i]**2/lam[i] for i in range(3))
            for penalty in (s.Rational(1,3),s.Rational(1),s.Rational(5)):
                psi=s.Matrix([singular[i]*target[i]/(lam[i]+penalty) for i in range(3)])
                budget=(psi.T*psi)[0]
                error=((A*psi-target).T*(A*psi-target))[0]
                formula=sum(penalty**2*target[i]**2/(lam[i]+penalty)**2 for i in range(3))
                dual=sum(penalty*target[i]**2/(lam[i]+penalty) for i in range(3))-penalty*budget
                check(error==formula==dual,'spectral error and dual identity')
                check(0<budget<E,'finite positive budget below exact lift')
                for trial in (s.zeros(3,1),s.ones(3,1),s.Matrix([-2,1,3])):
                    lhs=((A*trial-target).T*(A*trial-target))[0]+penalty*(trial.T*trial)[0]
                    opt=error+penalty*budget
                    rest=((trial-psi).T*(A.T*A+penalty*s.eye(3))*(trial-psi))[0]
                    check(lhs-opt==rest and rest>=0,'completed square global optimum')
                larger=penalty+1
                check(sum(lam[i]*target[i]**2/(lam[i]+larger)**2 for i in range(3))<budget,'budget strict monotonicity')
            exact=A.inv()*target
            check((exact.T*exact)[0]==E,'exact energy endpoint')
    report_checks(root,certificate)
    return original_grams


def report_checks(root,data):
    expected={'gamma':'1584/625','Gamma':'7182/625','alpha':'138/25',
              'gamma_multiplicity':8,'Gamma_multiplicity':4,'kappa_over_R':24,
              'gram_cross_coefficient':'1866/625'}
    check(data['coefficients']==expected,'reported coefficients','report_or_pin')
    scope={'coupled_conormal_domain_required':True,'auxiliary_scalar_gap_is_actual_gap':False,
           'compact_error_floor_requires_energy_blowup':False,'smooth_compatible_exact_compact_lift_energy_inf':True,
           'arbitrary_L2_has_exact_smooth_compact_lift':False,'compact_infimum_always_attained':False,
           'budget_zero_and_pure_charge_endpoints_explicit':True,'instantaneous_repaired_frame_transfer':True,
           'fixed_box_dynamical_intertwining':False,'native_GU':False,'general_spectral_budget_calculus_new':False}
    check(data['scope']==scope,'reported scope','report_or_pin')
    check(data['result_id']=='K1888' and data['classification']=='INTERNAL_STRUCTURAL_ONLY','reported identity','report_or_pin')
    check(data['checks'] and all(v is True for v in data['checks'].values()),'producer reports green baseline','report_or_pin')
    for path in INPUTS:
        check(data['inputs'].get(path)==hashlib.sha256((root/path).read_bytes()).hexdigest(),'input pin '+path,'report_or_pin')


def expect_failure(name,job):
    try:
        job()
    except AssertionError as error:
        if not str(error).startswith('FAIL '):
            raise
        print('CAUGHT',name,':',error)
        return
    raise AssertionError('FAIL planted fault escaped: '+name)


def mutations(root,data,grams):
    G=grams[0]
    faulty=G.copy();faulty[0,0]+=1
    expect_failure('actual Gram coefficient corruption',lambda:check_gram(faulty))
    crossless=G.copy();crossless[:4,4:8]=s.zeros(4);crossless[4:8,:4]=s.zeros(4)
    expect_failure('actual omitted cross-boundary Gram',lambda:check_gram(crossless))
    P=(625*G-1584*s.eye(12))/5598;v=(s.eye(12)-P)[:,0]
    expect_failure('actual alpha used as lower bound',lambda:check((v.T*(G-s.Rational(138,25)*s.eye(12))*v)[0]>=0,'false alpha lower bound'))
    expect_failure('actual scalar Neumann substituted for conormal',lambda:check(G[:4,4:8]*s.eye(4)[:,0]==s.zeros(4,1),'false scalar boundary flux'))
    a,z,t=s.Rational(2),s.Rational(3),s.Rational(5)
    correct=(a*(a*z/(a*a+t))-z)**2
    expect_failure('actual missing squared penalty in error',lambda:check(correct==t*z*z/(a*a+t)**2,'false error coefficient'))
    N=read_matrix(data['blocks'][0]['flux_right_inverse'])
    expect_failure('actual source metric dropped in flux inverse',lambda:check(N.T*N==G.inv(),'false Euclidean source energy'))
    for key,value in [('gamma','138/25'),('kappa_over_R',1)]:
        altered=copy.deepcopy(data);altered['coefficients'][key]=value
        expect_failure('serialized coefficient '+key,lambda d=altered:report_checks(root,d))
    for key in ('native_GU','auxiliary_scalar_gap_is_actual_gap','compact_error_floor_requires_energy_blowup','fixed_box_dynamical_intertwining'):
        altered=copy.deepcopy(data);altered['scope'][key]=not altered['scope'][key]
        expect_failure('reported scope '+key,lambda d=altered:report_checks(root,d))
    altered=copy.deepcopy(data);altered['inputs'][INPUTS[0]]='0'*64
    expect_failure('reported input pin',lambda:report_checks(root,altered))
    print('PASS planted faults: 6 actual mathematical controls; 2 serialized coefficients; 5 report/pin faults')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2])
    parser.add_argument('--certificate',type=Path)
    parser.add_argument('--selftest',action='store_true')
    args=parser.parse_args()
    data=json.loads((args.certificate or args.root/OUT).read_text())
    grams=baseline(args.root,data)
    print('PASS K1888 clean baseline',dict(COUNTS),'continuum proof remains analytic')
    if args.selftest:
        mutations(args.root,data,grams)


if __name__=='__main__':
    main()
