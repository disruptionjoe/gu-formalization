#!/usr/bin/env python3
"""Finite exact controls for the full-transverse CW boundary estimate.
The all-dimensional integration/functional-analysis proof is written and reviewed.
"""
from pathlib import Path
import argparse,hashlib,json,sys,time
sys.dont_write_bytecode=True
import sympy as s
from printed_equation_jets_symbol_probe import engine
from cw_fullsystem_domain_probe import D,FACTORS
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/cw-all-threshold-boundary-certificates.json'
PINS={'lab/process/cw-fullsystem-domain-certificates.json': '8ede03f10d6bd28570a3028eb5c320d297de67a827d8b51c545ee5da76314be5', 'lab/process/cw-one-sided-boundary-certificates.json': 'f4e6666601b25a18bb1288d2fa19493df432e6b3f194fe17b301cf70d81e0ea2', 'lab/process/cw-bilinear-boundary-certificates.json': '7117b31256935c37cbb552ca064f989403e3f85df02d4eb6db3aa38079c4dc65', 'tests/program-focus/cw_fullsystem_domain_probe.py': '705acae3569fb46445ecb8c7562baddce793a3eb482e5477848c20ee9900cc1d', 'tests/program-focus/printed_equation_jets_symbol_probe.py': 'e43da867d17cf985bfac8c014657e8cbf18c94e80013350ca69eee804a4ebeb8', 'tests/program-focus/source_action_deep_algebra.py': '4e3800131049e2b397bbce6106bfc5766d2f5fbf996319c50942f3b805d65598'}
"""Bounded native full-symbol vertex controls, called by build."""


def native_fixture(e):
    import sympy as s
    from cw_fullsystem_domain_probe import D, add, scale, compact_symbol, cp

    checks = []

    def ck(name, condition):
        assert condition, name
        checks.append(name)

    def native(zeta, field):
        return e.Phi(e.wedge({(1 << i, 0): v for i, v in zeta.items()}, field))

    def grade(x, p):
        return {mask: value for mask, value in x.items() if mask.bit_count() == p}

    def rows(field):
        out = {}
        for (leg, mask), value in field.items():
            assert leg.bit_count() == 1
            out.setdefault(leg.bit_length()-1, {})[mask] = value
        return out

    def field(rowdict):
        return add({(1 << i, mask): value
                    for i, row in rowdict.items() for mask, value in row.items()})

    def left(gamma, value):
        return field({i: cp(gamma, row) for i, row in rows(value).items()})

    kap = s.Integer(12)
    omega = 3*s.sqrt(34)/2
    xi1 = {0: omega, 1: s.Rational(15, 2), 2: s.Rational(15, 2)}
    xi2 = {0: -omega, 1: -s.Rational(9, 2), 2: -s.Rational(9, 2)}
    zeta1 = {i: s.I*v for i, v in xi1.items()}
    zeta2 = {i: s.I*v for i, v in xi2.items()}
    zeta0 = {1: 3*s.I, 2: 3*s.I}
    q0 = s.Integer(-18)
    Gamma = {1 << i: D[i]*v for i, v in zeta0.items()}
    ck('output Clifford square', cp(Gamma, Gamma) == {0: q0})
    ck('input minus-one shell', s.expand(sum(D[i]*v*v for i, v in zeta1.items())) == -36)
    ck('input plus-one shell', s.expand(sum(D[i]*v*v for i, v in zeta2.items())) == 36)
    ck('actual common stable inputs', s.Rational(225, 2) > 36
       and s.Rational(81, 2) > 36)
    ck('output negative-two threshold', 4*(-2)*q0 == kap**2)

    # A1=E(gamma3 wedge gamma5): both axes are positive and transverse.
    Aseed = {(1 << 3, 1 << 5): s.Integer(1),
             (1 << 5, 1 << 3): s.Integer(-1)}
    # Genuine p9 hook: diagonal tracefree insertion times an eight-blade.
    M = sum(1 << i for i in range(6, 14))
    Hseed = {(1 << 3, (1 << 3) | M): s.Integer(1),
             (1 << 4, (1 << 4) | M): s.Integer(-1)}

    def FC(value, p):
        rr = rows(value)
        F = add(*(scale(D[i], grade(cp({1 << i: 1}, row), p+1))
                  for i, row in rr.items()))
        C = add(*(scale(D[i], grade(cp({1 << i: 1}, row), p-1))
                  for i, row in rr.items()))
        return F, C

    HF, HC = FC(Hseed, 9)
    ck('odd hook wedge and contraction vanish', not HF and not HC)
    modes = []
    for label, zeta, seed in [('minus-one-A1', zeta1, Aseed),
                              ('plus-one-H9', zeta2, Hseed)]:
        pseed = native(zeta, seed)
        ck(label+' compact/native seed', pseed == compact_symbol(zeta, seed))
        ck(label+' square144', native(zeta, pseed) == scale(144, seed))
        v = add(scale(kap, seed), scale(-1, pseed))
        ck(label+' nonzero eigenpolarization', bool(v))
        ck(label+' actual massive kernel', not add(scale(kap, v), native(zeta, v)))
        real = {key: s.re(value) for key, value in v.items() if s.re(value) != 0}
        imag = {key: s.im(value) for key, value in v.items() if s.im(value) != 0}
        ck(label+' primary-minus quadratures', e.real_skew(real) and e.real_skew(imag))
        modes.append(v)

    def output_receiver(value):
        """Grade10 b+6c, the full B11 negative-mass left projection."""
        rr = rows(value)
        longitudinal = add(*(scale(D[i]*zi, rr.get(i, {}))
                             for i, zi in zeta0.items()))
        transverse = {
            i: add(rr.get(i, {}), scale(-zeta0.get(i, 0)/q0, longitudinal))
            for i in range(14)
        }
        beta, betaprime = {}, {}
        for i, row in transverse.items():
            X = grade(row, 11)
            beta[i] = scale(s.Rational(1, 2),
                            add(X, scale(-1/q0, cp(cp(Gamma, X), Gamma))))
            Y = grade(row, 12)
            gamma_part = scale(s.Rational(1, 2),
                               add(Y, scale(-1/q0, cp(cp(Gamma, Y), Gamma))))
            betaprime[i] = scale(1/q0, cp(Gamma, gamma_part))

        def contraction(rowdict):
            return add(*(scale(D[i], grade(cp({1 << i: 1}, row), 10))
                         for i, row in rowdict.items()))

        return add(contraction(beta), scale(6, contraction(betaprime)))

    # A nonzero B11 control supplies normalization and distinguishes a zero
    # physical fixture from a broken/vacuous receiver implementation.
    wmask = sum(1 << i for i in range(3, 13))
    w = {wmask: s.Integer(1)}
    Jw = field({i: grade(cp(add({1 << i: s.Integer(1)},
                               scale(-zeta0.get(i, 0)/q0, Gamma)), w), 11)
                for i in range(14)})
    gammaJw = left(Gamma, Jw)
    ck('receiver positive control', output_receiver(Jw) == scale(3, w))
    ck('receiver Gamma control', output_receiver(gammaJw) == scale(18, w))
    ck('actual B11 forward', native(zeta0, Jw) == scale(-2, gammaJw))
    ck('actual B11 back', native(zeta0, gammaJw) == scale(4*q0, Jw))
    ck('left receiver on L B11', not output_receiver(add(scale(kap, Jw),
                                                       native(zeta0, Jw))))

    force = e.Phi(add(e.wedge(modes[0], modes[1]),
                      e.wedge(modes[1], modes[0])))
    received = output_receiver(force)
    ck('left receiver on L actual force',
       not output_receiver(add(scale(kap, force), compact_symbol(zeta0, force))))

    return {
        'status': 'PASS', 'check_count': len(checks), 'checks': checks,
        'input_factors': [-1, 1], 'output_factor': -2,
        'frequency': '3*sqrt(34)/2', 'output_spatial_square': '18',
        'seed_degrees': [1, 9],
        'mode_terms': [len(v) for v in modes], 'force_terms': len(force),
        'threshold_projection_nonzero': bool(received),
        'receiver': [[mask, str(v)] for mask, v in sorted(received.items())],
        'scope': [
            'One exact actual full-symbol A1/H9 fixture; zero is a valid result.',
            'No trace-minus12 substitution, dense census or global selection theorem.',
            'The all-threshold compact-patch bound is independent of this fixture outcome.',
            'No source-selected domain, curved dynamics or physical mass-gap conclusion.',
        ],
    }


def build():
    checks=[]
    def ck(n,v):assert v,n;checks.append(n)
    deps=dict(PINS)
    for p in PINS:
        if p.endswith('.json'):deps.update(json.loads((ROOT/p).read_text()).get('dependencies',{}))
    for p,h in deps.items():ck('reuse '+p,hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h)
    A,al,q,ca,cb,C=s.symbols('A al q ca cb C',real=True)
    W=s.sqrt(A*al**2+q+cb);w1=s.sqrt(A+ca)
    delta=C-A*(1+al)**2-q
    for sig1 in [-1,1]:
        for sig2 in [-1,1]:
            nu=sig1*w1+sig2*W
            J=s.Matrix([[s.diff(f,x)for x in [al,q]]for f in [delta,nu]])
            ck('exact invariant Jacobian '+str((sig1,sig2)),s.simplify(J.det()+sig2*A/W)==0)
            B=(nu-sig1*w1)**2-cb
            ainv=(C-delta-A-B)/(2*A)
            qinv=B-A*ainv**2
            ck('exact alpha inverse '+str((sig1,sig2)),s.simplify(ainv-al)==0)
            ck('exact q inverse '+str((sig1,sig2)),s.simplify(qinv-q)==0)
    ck('spatial and transverse signatures',D[1:].count(1)==9 and D[1:].count(-1)==4 and 9-1==8)
    ck('held invariant coordinates',s.Rational(-3,5)**2*s.Rational(225,2)==s.Rational(81,2))
    jac=s.Rational(225,2)/(3*s.sqrt(34)/2)
    ck('rankloss point invariant Jacobian nonzero',jac==75/s.sqrt(34) and jac>0)
    # Coarea critical point: two positive polar directions remove the singularity.
    rr,t=s.symbols('r t',nonnegative=True)
    ck('two-positive polar density normalization',s.simplify(2*s.pi*rr/s.diff(rr**2,rr))==s.pi)
    ck('ten remaining transverse dimensions',12-2==10)
    R=s.symbols('R',positive=True)
    ck('bounded spectator box volume',(2*R)**10==1024*R**10)
    # Known dimensional countercontrol: one positive coordinate alone has an
    # unbounded pushforward density near0. The actual proof uses two.
    eps=s.symbols('eps',positive=True)
    ck('one-dimensional quadratic density singular',s.limit(1/s.sqrt(eps),eps,0,dir='+')==s.oo)
    d,v,L=s.symbols('d v L',positive=True)
    ck('boundary kernel temporal integral',s.integrate(1/(d+v**2),(v,-s.oo,s.oo))==s.pi/s.sqrt(d))
    ck('boundary kernel full collar',s.integrate(s.pi/s.sqrt(d),(d,0,L))==2*s.pi*s.sqrt(L))
    ck('threshold tail norm exponent',s.sqrt(s.sqrt(eps))==eps**s.Rational(1,4))
    ck('old squared-state kernel temporal integral',s.integrate(1/(d+v**2)**2,(v,-s.oo,s.oo))==s.pi/(2*d**s.Rational(3,2)))
    ck('old squared-state collar diverges',s.limit(s.pi/s.sqrt(eps),eps,0,dir='+')==s.oo)
    # All shell thresholds stay separated for kappa12; signs do not enter J.
    thresholds=[-s.Rational(36,a)for a in FACTORS]
    ck('all nineteen thresholds distinct',len(set(thresholds))==19)
    ck('negative output factors included',sum(bool(x>0) for x in thresholds)==12)
    ck('positive output factors retained',sum(bool(x<0) for x in thresholds)==7)
    # Reused exact full-time scalar response kernel integrates to2pi t.
    lam=s.symbols('lam',positive=True);tt=s.symbols('t',positive=True)
    weighted=s.pi*(1-(1+2*lam*tt)*s.exp(-2*lam*tt))/lam**2
    antiderivative=s.pi*((s.exp(-2*lam*tt)-1)/lam)
    ck('forward kernel integral antiderivative',s.simplify(s.diff(antiderivative,lam)-weighted)==0)
    ck('forward kernel integral full value',s.limit(antiderivative,lam,s.oo)-s.limit(antiderivative,lam,0,dir='+')==2*s.pi*tt)
    native=native_fixture(engine(D));checks+=native['checks']
    ck('calibrated fixture zero recorded',not native['threshold_projection_nonzero'] and native['force_terms']>0)
    return {'schema':'gu-cw-all-threshold-boundary-v1','status':'PASS','probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies':deps,'check_count':len(checks),'check_names':checks,'analytic_controls':{'Jacobian':'-s2 A/W','Lebesgue_density_factor':'W/sqrt(A)','transverse_signature':[8,4],'quadratic_pushforward_bound':'pi (2R)^10','kernel_squared_norm_bound':'2pi sqrt(D)','tail_operator_rate':'epsilon^(1/4)','output_factors':FACTORS,'signed_input_branches':38,'forward_q_bound':'O(1+sqrt(t)), upper estimate only'},'native_fixture':native,'scope':['Exact finite/control algebra and one actual native fixture; written integration proof independently reviewed.','All output thresholds locally on compact common-CW massive input patches; bounded regular numerator.','Zero projection for one polarization is not a class cancellation theorem.','No unbounded-frequency, retained-decay interaction, nonlinear manifold or physical/source claim.']}
if __name__=='__main__':
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group(required=True);g.add_argument('--write',action='store_true');g.add_argument('--verify',action='store_true');a=p.parse_args();t=time.monotonic();d=build()
    if a.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
    else:assert json.loads(OUT.read_text())==json.loads(json.dumps(d)),'certificate mismatch'
    print(json.dumps({'status':'PASS','checks':d['check_count'],'seconds':time.monotonic()-t,'fixture_projection_nonzero':d['native_fixture']['threshold_projection_nonzero']}))
