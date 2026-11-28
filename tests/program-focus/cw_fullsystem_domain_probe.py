#!/usr/bin/env python3
"""Exact reuse checker for common-domain nonlinear closure.

This authenticates accepted exact native artifacts, adds finite domain and
descriptor controls, and reuses the pinned native engine for one new sparse
boosted-force check. It does not rerun the old full symbol census or probe.
The written Schwartz-packet implication is separately reviewed mathematics.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse
import hashlib
import json

CERT = 'lab/process/printed-state-completion-certificates.json'
PRODUCER = 'tests/program-focus/printed_state_completion_probe.py'
CERT_SHA = 'ec0aafeace76b0d47f9ec9a7b142be29b6c7349e2c3397283029d14fe3e88977'
PRODUCER_SHA = '2be9b235defb0b52f2940f479ffc328d69b8e0477a941b509d18af19d61f8a88'
FACTORS = [1, 12, 22, 30, 36, 40, 42] + list(range(-1, -13, -1))


def support_check(repo):
    def sha(path):
        return hashlib.sha256((repo / path).read_bytes()).hexdigest()

    assert sha(CERT) == CERT_SHA
    assert sha(PRODUCER) == PRODUCER_SHA
    cert = json.loads((repo / CERT).read_text())
    assert cert['status'] == 'PASS'
    assert cert['probe_sha256'] == PRODUCER_SHA
    assert all(sha(path) == digest for path, digest in cert['dependencies'].items())
    native = cert['native_response_checks']
    assert native['status'] == 'PASS'
    generic = native['generic']
    assert (generic['n'], generic['omega'], generic['p'], generic['q']) == (4, '9', '10', '64')
    for name in ['n=4:plus:full-massive-mode', 'n=4:minus:full-massive-mode',
                 'n=4:actual-polarized-force', 'generic-actual-system-particular',
                 'generic-full-scalarizer-nonresonant']:
        assert name in native['check_names']

    # These are new exact arithmetic controls, not a new native-Q replay.
    kappa, omega, positive, normal = map(F, (12, 9, 10, 4))
    spatial_square = positive**2 - normal**2
    assert -omega**2 + spatial_square == 3
    assert spatial_square == 84 and spatial_square > kappa**2 / 4
    shell_squares = {a: spatial_square + kappa**2 / (4*a) for a in FACTORS}
    assert all(value > 0 for value in shell_squares.values())
    assert min(shell_squares.values()) == 48
    assert shell_squares[-12] == omega**2 == 81

    # Full frequencies are (time, ordinary spatial, negative normal).
    plus, minus = (9, 10, 4), (-9, -10, 4)
    negative = lambda vector: tuple(-x for x in vector)
    inputs = [plus, minus, negative(plus), negative(minus)]
    total = tuple(x+y for x, y in zip(plus, minus))
    assert total == (0, 0, 8)
    sum_spatial_square = F(total[1]**2-total[2]**2)
    assert sum_spatial_square == -64 < kappa**2 / 4
    contributing = [(i, j) for i, x in enumerate(inputs) for j, y in enumerate(inputs)
                    if tuple(a+b for a, b in zip(x, y)) == total]
    assert contributing == [(0, 1), (1, 0)]
    spatial_contributing = [(i, j) for i, x in enumerate(inputs) for j, y in enumerate(inputs)
                            if tuple(a+b for a, b in zip(x[1:], y[1:])) == total[1:]]
    assert spatial_contributing == [(0, 1), (1, 0)]

    force = {(a, b): value for a, b, value in generic['force']}
    assert force[(1, 1)] == '-749632'
    assert F(force[(1, 1)]) != 0
    q_sum = -sum_spatial_square
    assert q_sum == 64
    assert all(kappa**2 - 4*a*q_sum != 0 for a in FACTORS)
    assert generic['particular_for_negative_force']
    assert F(-749632, 12**2) == -F(46852, 9)
    return {
        'status': 'PASS',
        'kind': 'owned-native-reuse-and-new-support-arithmetic',
        'certificate_sha256': CERT_SHA,
        'producer_sha256': PRODUCER_SHA,
        'input_spatial_square': str(spatial_square),
        'common_domain_margin': str(spatial_square-kappa**2/4),
        'minimum_temporal_square_all19': str(min(shell_squares.values())),
        'sum_spatial_square': str(sum_spatial_square),
        'native_cross_receiver': force[(1, 1)],
        'full_massive_sum_nonresonant': True,
        'owned_bounded_particular_retained': True,
        'limits': [
            'Does not rerun the owned native vertex or response producer.',
            'The strict nonlinear full-field cutoff fails; enlarged off-support dynamics are separate.',
            'Schwartz packet transfer is the accompanying written argument, not a finite-code theorem.',
            'No source-selected state, norm, action, physical instability, or GU verdict follows.',
        ],
    }



import sys,time
sys.dont_write_bytecode=True
import sympy as sp
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/'lab/process/cw-fullsystem-domain-certificates.json'

import sympy as s

I = s.I
D = [-1, 1, 1, 1] + [1] * 6 + [-1] * 4
HORIZONTAL = 15


def clean(a):
    return {k: s.expand(v) for k, v in a.items() if s.expand(v) != 0}


def add(*xs):
    out = {}
    for x in xs:
        for k, v in x.items():
            out[k] = out.get(k, 0) + v
    return clean(out)


def scale(c, x):
    return clean({k: c*v for k, v in x.items()})


def conjugate(x):
    return clean({k: s.conjugate(v) for k, v in x.items()})


def cliff_product_mask(a, b):
    inversions = sum((b & ((1 << i)-1)).bit_count()
                     for i in range(14) if a & (1 << i))
    coefficient = (-1)**inversions
    for i in range(14):
        if a & b & (1 << i):
            coefficient *= D[i]
    return a ^ b, coefficient


def cp(a, b):
    out = {}
    for x, vx in a.items():
        for y, vy in b.items():
            blade, c = cliff_product_mask(x, y)
            out[blade] = out.get(blade, 0) + c*vx*vy
    return clean(out)


def bracket(a, b, anti=False):
    return add(cp(a, b), scale(1 if anti else -1, cp(b, a)))


def rows(field):
    out = {}
    for (leg, blade), coefficient in field.items():
        out.setdefault(leg.bit_length()-1, {})[blade] = coefficient
    return out


def compact_symbol(xi, field):
    """P_xi from the owned full compact commutator/nested-anticommutator formula."""
    Y = rows(field)
    gamma = [{1 << j: s.Integer(1)} for j in range(14)]
    result = {}
    for k, xk in xi.items():
        if not xk:
            continue
        inner = add(*(scale(D[k]*D[b], bracket(cp(gamma[k], gamma[b]),
                              Y.get(b, {}), anti=True))
                      for b in range(14) if b != k))
        longitudinal = add(*(scale(D[b], bracket(gamma[b], Y.get(b, {})))
                             for b in range(14) if b != k))
        for a in range(14):
            lead = longitudinal if a == k else scale(-D[k], bracket(gamma[k], Y.get(a, {})))
            value = add(lead, scale(-s.Rational(1, 2), bracket(gamma[a], inner, anti=True)))
            for blade, coefficient in value.items():
                key = (1 << a, blade)
                result[key] = result.get(key, 0) + xk*coefficient
    return clean(result)


def theta_amplitude(field):
    # Ad_U flips precisely horizontal real gammas; J conjugates coefficients.
    # R acts on every exterior leg too. This formula also works on higher forms.
    return clean({(leg, blade): (-1)**(((leg ^ blade) & HORIZONTAL).bit_count())
                  *s.conjugate(v) for (leg, blade), v in field.items()})


def frequency_after_theta(xi):
    # Theta[T](x) includes x -> R x and coefficient conjugation.
    return {j: (v if j < 4 else -v) for j, v in xi.items() if v}


def trace_mode(xi, kappa=12):
    zeta = {j: I*s.Rational(v) for j, v in xi.items()}
    q = sum(v*v/D[j] for j, v in zeta.items())
    assert q != 0
    O = {(1 << j, 1 << j): s.Integer(1) for j in range(14)}
    O = add(O, {(1 << a, 1 << b): -va*vb/(D[b]*q)
                for a, va in zeta.items() for b, vb in zeta.items()})
    gamma = {1 << j: v/D[j] for j, v in zeta.items()}
    derivative_part = {}
    for a, row in rows(O).items():
        for blade, value in cp(gamma, row).items():
            derivative_part[(1 << a, blade)] = value
    return add(scale(kappa, O), scale(2, derivative_part))


def ell(field, opposite=False):
    phase = I if opposite else -I
    return s.expand(field.get((1, 2), 0)-field.get((2, 1), 0)
                    +phase*field.get((1, 1026), 0)-phase*field.get((2, 1025), 0))


def theta_controls(repo):
    checks = []
    def ck(name, condition):
        assert condition, name
        checks.append(name)
    path = repo/'lab/process/printed-state-completion-certificates.json'
    data = json.loads(path.read_text())
    ck('source-certificate-hash', hashlib.sha256(path.read_bytes()).hexdigest() ==
       'ec0aafeace76b0d47f9ec9a7b142be29b6c7349e2c3397283029d14fe3e88977')
    force = {(int(a), int(b)): s.sympify(v, locals={'I': I})
             for a, b, v in data['native_response_checks']['resonant']['force']}
    # Generic complex amplitudes catch the distinction between conjugation
    # and a complex-linear reflection, and transport the receiver coefficients.
    generic = {(1, 2): 2+3*I, (2, 1): 5-I,
               (1, 1026): 7+2*I, (2, 1025): -3+4*I,
               (16, 31): 1-2*I, (8, 16383): 4+I}
    ck('theta-amplitude-involution', theta_amplitude(theta_amplitude(generic)) == generic)
    ck('theta-is-antilinear', theta_amplitude(scale(I, generic)) == scale(-I, theta_amplitude(generic)))
    ck('receiver-opposite-frequency-transport',
       s.expand(ell(theta_amplitude(generic), opposite=True)-s.conjugate(ell(generic))) == 0)
    ck('receiver-is-not-naively-fixed',
       s.expand(ell(theta_amplitude(generic))-s.conjugate(ell(generic))) != 0)
    for label, xi in [('mixed', {0: 2, 2: -3, 7: 5}), ('normal', {10: 6})]:
        zeta = {j: I*v for j, v in xi.items()}
        transformed_zeta = {j: I*v for j, v in frequency_after_theta(xi).items()}
        ck('compact-symbol-theta:'+label,
           theta_amplitude(compact_symbol(zeta, generic)) ==
           compact_symbol(transformed_zeta, theta_amplitude(generic)))
    xp = {0: 2, 1: 4, 10: 3}
    xm = {0: -2, 1: -4, 10: 3}
    up, um = trace_mode(xp), trace_mode(xm)
    for label, xi, mode in [('plus', xp, up), ('minus', xm, um)]:
        ck('exact-linear-mode:'+label,
           not add(scale(12, mode), compact_symbol({j: I*v for j, v in xi.items()}, mode)))
        ck('mode-theta-covariance:'+label,
           theta_amplitude(mode) == trace_mode(frequency_after_theta(xi)))
        ck('mode-has-only-vector-bivector:'+label,
           all(blade.bit_count() in (1, 2) for leg, blade in mode))
    ck('real-pair-support-exchange', frequency_after_theta(xp) == {j: -v for j, v in xm.items()})
    ck('plus-maps-to-conjugate-minus', theta_amplitude(up) == conjugate(um))
    ck('minus-maps-to-conjugate-plus', theta_amplitude(um) == conjugate(up))
    # An arbitrary COMMON complex coefficient in the two positive-frequency
    # modes, together with their conjugates, yields a Theta-invariant real field.
    amplitude = 2+3*I
    ck('common-amplitude-real-pair-is-theta-fixed',
       theta_amplitude(scale(amplitude, up)) == conjugate(scale(amplitude, um)) and
       theta_amplitude(scale(amplitude, um)) == conjugate(scale(amplitude, up)))
    ck('force-is-same-owned-mixed-coefficient', force.get((1, 1)) == -22080)
    ck('force-has-horizontal-reflection-even-tensor-parity',
       all(((leg ^ blade) & HORIZONTAL).bit_count() % 2 == 0 for leg, blade in force))
    ck('force-theta-is-opposite-frequency-amplitude', theta_amplitude(force) == conjugate(force))
    ck('nonzero-owned-plus-receiver', ell(force) == 104448)
    ck('nonzero-transported-minus-receiver', ell(theta_amplitude(force), opposite=True) == 104448)
    # Realification with common amplitude preserves rather than cancels force.
    ck('real-force-pair-is-theta-fixed',
       theta_amplitude(scale(amplitude**2, force)) == conjugate(scale(amplitude**2, force)))
    # The owned nonresonant control has the same symmetry, so Theta does
    # not distinguish resonance from a bounded stationary forced response.
    gx = {0: 9, 1: 10, 10: 4}
    gy = {0: -9, 1: -10, 10: 4}
    gu, gv = trace_mode(gx), trace_mode(gy)
    for label, xi, mode in [('plus', gx, gu), ('minus', gy, gv)]:
        ck('generic-pair-linear-mode:'+label,
           not add(scale(12, mode), compact_symbol({j: I*v for j, v in xi.items()}, mode)))
    ck('generic-pair-theta-exchange', theta_amplitude(gu) == conjugate(gv)
       and theta_amplitude(gv) == conjugate(gu))
    generic_force = {(int(a), int(b)): s.sympify(v, locals={'I': I})
                     for a, b, v in data['native_response_checks']['generic']['force']}
    ck('generic-force-theta-covariance', theta_amplitude(generic_force) == conjugate(generic_force))
    return {'checks': checks, 'check_count': len(checks),
            'input_certificate': str(path.relative_to(repo)),
            'input_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'scope': 'Frozen primary-minus K95 printed P,Q; Theta amplitude and real-pair controls. Q covariance is the accompanying tensor proof, and the force is inherited exact data. No closed domain, positive metric, Hamiltonian or quantum conclusion.'}




def boost_field(field, sign=1):
    c=s.Rational(5,3);h=sign*s.Rational(4,3)
    gam=[{1<<i:s.Integer(1)}for i in range(14)]
    gam[0]={1:c,2:-h};gam[1]={1:-h,2:c}
    out={}
    for (leg,blade),v in field.items():
        assert leg.bit_count()==1
        forms={leg:s.Integer(1)}
        if leg==1:forms={1:c,2:h}
        if leg==2:forms={1:h,2:c}
        b={0:s.Integer(1)}
        for i in range(14):
            if blade&(1<<i):b=cp(b,gam[i])
        for le,lc in forms.items():
            for cl,cc in b.items():out[(le,cl)]=out.get((le,cl),0)+v*lc*cc
    return clean(out)

def boost_controls(repo):
    sys.path.insert(0,str(repo/'tests/program-focus'))
    from printed_equation_jets_symbol_probe import engine
    e=engine(D);checks=[]
    def ck(n,v):assert v,n;checks.append(n)
    old=json.loads((repo/CERT).read_text())['native_response_checks']['resonant']
    force={(a,b):s.sympify(v)for a,b,v in old['force']}
    phi1={(1<<i,1<<i):s.Integer(1)for i in range(14)}
    ck('boost preserves canonical tensor',boost_field(phi1)==phi1)
    ck('boost inverse on native force',boost_field(boost_field(force),-1)==force)
    oldx={0:2,1:4,10:3};oldy={0:-2,1:-4,10:3}
    xp={0:s.Rational(26,3),1:s.Rational(28,3),10:3};xm={0:-s.Rational(26,3),1:-s.Rational(28,3),10:3}
    vp,vm=trace_mode(xp),trace_mode(xm)
    ck('boost actual polarizations',boost_field(trace_mode(oldx))==vp and boost_field(trace_mode(oldy))==vm)
    ck('boost actual full linear modes',not add(scale(12,vp),compact_symbol({i:I*v for i,v in xp.items()},vp)) and not add(scale(12,vm),compact_symbol({i:I*v for i,v in xm.items()},vm)))
    actual=e.Phi(add(e.wedge(vp,vm),e.wedge(vm,vp)))
    ck('new native quadratic force equals covariant old force',actual==boost_field(force))
    ck('boosted massive receiver nonzero',ell(boost_field(actual,-1))==104448)
    for key in [(1,2),(2,1025),(16,31)]:
        f={key:s.Integer(1)}
        ck('normal output L0 commutes boost '+str(key),boost_field(add(scale(12,f),compact_symbol({10:6*I},f)))==add(scale(12,boost_field(f)),compact_symbol({10:6*I},boost_field(f))))
    r2=s.Rational(28,3)**2-9
    ck('boosted pair inside common domain',r2==s.Rational(703,9) and r2>36)
    ck('boosted trace frequency',r2-3==s.Rational(26,3)**2)
    ck('boosted output same resonant normal sum',{i:xp.get(i,0)+xm.get(i,0)for i in xp}=={0:0,1:0,10:6})
    return {'check_names':checks,'check_count':len(checks),'omega':'26/3','horizontal_p':'28/3','normal_n':3,'spatial_square':'703/9','common_domain_margin':'379/9','transported_receiver':'104448','force':[[a,b,str(v)]for (a,b),v in sorted(actual.items())],'scope':'Actual newly checked boosted quadratic pair; general Lorentz covariance remains written tensor proof. Regular slaving exclusion retains its character/regularity premises, not all Sobolev maps.'}

def build():
    checks=[]
    def ck(name,value):
        assert value,name
        checks.append(name)
    reuse=support_check(ROOT);ck('native generic support fixture authenticated',reuse['status']=='PASS')
    z,q,lam,t=sp.symbols('z q lam t',real=True);kap=sp.Integer(12)
    d=kap**2*sp.prod(kap**2-4*a*q for a in FACTORS)
    m=z*z*sp.prod(z*z-4*a*q for a in FACTORS)
    dp=sp.diff(d,q)
    roots=[]
    for a in FACTORS:
        qa=kap**2/(4*a);beta=-sp.diff(m,z).subs({z:-kap,q:qa});beta2=2*kap**3*sp.prod(kap**2-4*b*qa for b in FACTORS if b!=a)
        ck('beta nonzero '+str(a),beta==beta2 and beta!=0)
        ck('scalar shell simple '+str(a),dp.subs(q,qa)!=0)
        roots.append(sp.Rational(84)+kap**2/(4*a))
    ck('38 simple imaginary temporal roots in stable region',len(set(roots))==19 and min(roots)==48)
    ck('spatial C invertible on example stable patch',d.subs(q,-84)!=0)
    # Exact descriptor with two dynamical modes and one algebraic constraint.
    w=sp.Integer(3);A=sp.diag(2,3,0);G=sp.Matrix([[0,1,0],[-w*w,0,0],[0,0,0]]);C=-A*G;C[2,2]=1;L=lam*A+C
    resolvent=L.inv()*A
    R=[]
    for lb in [sp.I*w,-sp.I*w]:
        rb=resolvent.applyfunc(lambda x:sp.simplify(sp.limit((lam-lb)*x,lam,lb)))
        R.append(rb);ck('temporal residue idempotent '+str(lb),rb*rb==rb);ck('actual kernel residue '+str(lb),(lb*A+C)*rb==sp.zeros(3))
    ck('temporal residue direct compatible decomposition',R[0]*R[1]==sp.zeros(3) and sum(R,sp.zeros(3))==sp.diag(1,1,0))
    ck('compatible initial state sufficient',C.det()!=0 and (C.inv()*A)*R[0]==(-1/(sp.I*w))*R[0])
    H=sp.diag(w*w,1,0);ck('positive oscillator conserved norm',G.T*H+H*G==sp.zeros(3) and w*w>0)
    ck('algebraic state excluded',L*sp.Matrix([0,0,1])==sp.Matrix([0,0,1]))
    # Threshold and growing comparator: sign is diagnostic, not a GU import.
    N=sp.Matrix([[0,1],[0,0]]);v0=sp.Matrix([1,0]);v1=sp.Matrix([0,1]);h=t*v0+v1
    ck('threshold Jordan chain',N*v0==sp.zeros(2,1) and N*v1==v0 and sp.diff(h,t)==N*h)
    forced=sp.Matrix([t*t/2,t]);ck('forced threshold degree2',sp.diff(forced,t)==N*forced+sp.Matrix([0,1]))
    a,b,c=sp.symbols('a b c',real=True);K=sp.Matrix([[a,b],[b,c]])
    ck('threshold positive conserved metric obstruction',(N.T*K+K*N)==sp.Matrix([[0,a],[a,2*b]]))
    growth=sp.Matrix([[0,1],[4,0]]);ck('forbidden exponential branch',set(growth.eigenvals())=={-2,2})
    # q fixed analytic curve and multiplicity at both relevant thresholds.
    for r2,aa in [(sp.Integer(36),-1),(-sp.Integer(36),1)]:
        scale=sp.sqrt(1-lam*lam/r2);curveq=-lam*lam-r2*scale*scale
        ck('fixed q curve '+str(aa),sp.simplify(curveq+r2)==0 and sp.diff(scale,lam).subs(lam,0)==0)
        ck('threshold q matches '+str(aa),-r2==kap*kap/(4*aa))
        g0=4*aa*kap*kap*sp.prod(kap*kap+4*b*r2 for b in FACTORS if b!=aa)
        ck('threshold temporal double root '+str(aa),g0!=0)
    other=[sp.Rational(36)-sp.Rational(36,a)for a in FACTORS if a!=1]
    ck('old resonant slice other36 exponential roots',len(set(other))==18 and min(other)>0)
    # Equal-frequency PU comparison: two nonzero double roots, different spectrum.
    u=t*sp.exp(sp.I*w*t);D=lambda x:sp.diff(x,t,2)+w*w*x
    ck('PU Jordan-type polynomial factor',sp.simplify(D(D(u)))==0 and sp.simplify(D(u))!=0)
    old=json.loads((ROOT/CERT).read_text())['native_response_checks'];sec=old['secular_particular_for_positive_force'];fo=old['forced_modal_ODE']
    ck('owned degree2 leading receiver',sec['time_degree']==2 and sec['leading_receiver']=='78336')
    ck('owned negative forcing slope',fo['slope_for_negative_force']=='-104448')
    coeff=[{(a,b):sp.sympify(v)for a,b,v in x}for x in sec['coefficients']]
    fm={(a,b):sp.sympify(v)for a,b,v in old['resonant']['obstructing_projection']}
    ck('leading coefficient exactly three resonant projection',coeff[2]=={k:3*v for k,v in fm.items()})
    ck('linear receiver is not polynomial degree',fo['ell_Ptau_secular_coefficients']==['0','104448','0'])
    theta=theta_controls(ROOT);checks.extend('theta:'+n for n in theta['checks'])
    boost=boost_controls(ROOT);checks.extend('boost:'+n for n in boost['check_names'])
    deps={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in [CERT,PRODUCER,'explorations/conditional-build/printed-equation-jets-and-symbol-2026-11-27.md','explorations/conditional-build/printed-differential-solvability-2026-11-27.md','lab/active-research/joe-directed/external-results/pt-mannheim-applicability-2026-11-26.md']}
    return {'schema':'gu-cw-fullsystem-v1','status':'PASS','probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies':deps,'check_names':checks,'check_count':len(checks),'reused_native_support':reuse,'theta_controls':theta,'boosted_resonance':boost,'linear_domain':{'factors':FACTORS,'common_stable_region':'r^2 > kappa^2/4','temporal_roots':38,'norm':'auxiliary modal L2; ordinary compatible L2 equivalence only on compact separated patches'},'secular':{'actual_negative_force_time_degree':2,'leading_receiver':'-78336','forced_functional_slope':'-104448','old_sum_other_real_roots':36,'homogeneous_threshold_chain_length':2},'scope':'Small exact controls and pinned native reuse; full descriptor, wave-packet and slice arguments remain reviewed written mathematics. No physical norm, timescale or GU verdict.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group(required=True);g.add_argument('--write',action='store_true');g.add_argument('--verify',action='store_true');a=p.parse_args();t0=time.monotonic();data=build()
    if a.write:OUTPUT.write_text(json.dumps(data,indent=2)+'\n')
    else:assert json.loads(OUTPUT.read_text())==data,'certificate mismatch'
    print(json.dumps({'status':'PASS','checks':data['check_count'],'seconds':time.monotonic()-t0}))
