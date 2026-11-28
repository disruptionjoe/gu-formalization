#!/usr/bin/env python3
"""Exact finite controls and pinned actual-operator replay.
Written orbit/coarea/history proofs are not formalized by this probe.
"""
from pathlib import Path
import argparse, hashlib, json, sys, time
sys.dont_write_bytecode=True
import sympy as s
from cw_fullsystem_domain_probe import D,FACTORS,add,scale,compact_symbol,trace_mode,conjugate,ell,boost_field
from printed_equation_jets_symbol_probe import engine
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/cw-symmetry-domain-certificates.json'
PINS={'lab/process/cw-fullsystem-domain-certificates.json': '8ede03f10d6bd28570a3028eb5c320d297de67a827d8b51c545ee5da76314be5', 'lab/process/cw-one-sided-boundary-certificates.json': 'f4e6666601b25a18bb1288d2fa19493df432e6b3f194fe17b301cf70d81e0ea2', 'lab/process/cw-bilinear-boundary-certificates.json': '7117b31256935c37cbb552ca064f989403e3f85df02d4eb6db3aa38079c4dc65', 'tests/program-focus/cw_fullsystem_domain_probe.py': '705acae3569fb46445ecb8c7562baddce793a3eb482e5477848c20ee9900cc1d', 'tests/program-focus/printed_equation_jets_symbol_probe.py': 'e43da867d17cf985bfac8c014657e8cbf18c94e80013350ca69eee804a4ebeb8', 'tests/program-focus/source_action_deep_algebra.py': '4e3800131049e2b397bbce6106bfc5766d2f5fbf996319c50942f3b805d65598'}
"""Sparse Lorentz-core controls called by build with the owned K95 engine.
The neighborhood, orbit and L2 spectral proofs remain written mathematics.
"""


def core_controls(e):
    import sympy as s
    from cw_fullsystem_domain_probe import (
        D, FACTORS, add, scale, compact_symbol, trace_mode, conjugate,
    )

    checks = []

    def ck(name, condition):
        assert condition, name
        checks.append(name)

    def record(field):
        return [[a, b, str(v)] for (a, b), v in sorted(field.items())]

    kap = s.Integer(12)
    xi = {0: s.Rational(83, 13), 4: s.Rational(86, 13)}
    zeta = {a: s.I*v for a, v in xi.items()}
    q = s.expand(sum(v*v / D[a] for a, v in zeta.items()))
    normal_square = xi[4]**2
    ck('held frozen frame time and normal signs', D[0] == -1 and D[4] == 1)
    ck('actual trace shell', q == -3)
    ck('Lorentz core strict normal margin', normal_square - 36 == s.Rational(1312, 169))
    ck('all nineteen observed mass squares positive',
       all(normal_square + kap**2/(4*a) > 0 for a in FACTORS))

    longitudinal = {
        (1 << a, 1 << b): va*vb/(D[b]*q)
        for a, va in zeta.items() for b, vb in zeta.items()
    }
    O = add(e.phi1, scale(-1, longitudinal))
    gamma = {(0, 1 << b): vb/D[b] for b, vb in zeta.items()}
    V = e.wedge(gamma, O)
    plus = trace_mode(xi)
    minus = trace_mode({a: -v for a, v in xi.items()})
    ck('plus trace polarization', plus == add(scale(kap, O), scale(2, V)))
    ck('minus trace polarization', minus == add(scale(kap, O), scale(-2, V)))
    ck('opposed modes are conjugates', minus == conjugate(plus))

    def native_symbol(z, field):
        covector = {(1 << a, 0): v for a, v in z.items()}
        return e.Phi(e.wedge(covector, field))

    for label, z, field in [
        ('plus', zeta, plus),
        ('minus', {a: -v for a, v in zeta.items()}, minus),
    ]:
        ck(label + ' compact/native symbol binding',
           compact_symbol(z, field) == native_symbol(z, field))
        ck(label + ' actual massive kernel',
           not add(scale(kap, field), native_symbol(z, field)))

    real_part = {key: s.re(v) for key, v in plus.items() if s.re(v) != 0}
    imag_part = {key: s.im(v) for key, v in plus.items() if s.im(v) != 0}
    ck('real quadrature primary-minus skew', e.real_skew(real_part))
    ck('imaginary quadrature primary-minus skew', e.real_skew(imag_part))
    ck('both real quadratures nonzero', bool(real_part) and bool(imag_part))

    OO = e.wedge(O, O)
    ck('actual trace V wedge identity', e.wedge(V, V) == scale(-q, OO))
    ck('pinned Phi trace identity at new core fixture',
       e.Phi(OO) == add(scale(264, O), scale(312, longitudinal)))
    cross_wedge = add(e.wedge(plus, minus), e.wedge(minus, plus))
    ck('opposed cross wedge coefficient', cross_wedge == scale(264, OO))
    force = e.Phi(cross_wedge)
    ck('actual opposed force',
       force == add(scale(69696, O), scale(82368, longitudinal)))
    ck('horizontal receiver nonzero', force.get((2, 2), 0) == 69696)
    ck('actual force real skew', e.real_skew(force) and force == conjugate(force))
    response = add(scale(-5808, O), scale(-6864, longitudinal))
    ck('zero-output massive operator invertible', not native_symbol({}, response))
    ck('regular static quadratic response', not add(scale(kap, response), force))
    ck('zero normal output outside strict core', not (s.Integer(0) > kap**2/4))

    # Boundary exception: a=-1 admits a nonzero null horizontal orbit, but
    # another shell's rest point defeats branch-complete support at N=36.
    boundary_N = kap**2/4
    ck('minus-one massless boundary', boundary_N + kap**2/(4*(-1)) == 0)
    ck('positive shell rest point hits excluded CW equality',
       boundary_N + kap**2/4 > 0 and not (boundary_N > kap**2/4))
    eps = s.symbols('eps', positive=True)
    ck('normal margin gives minimal squared mass',
       s.expand((boundary_N + eps) + kap**2/(4*(-1))) == eps)

    # Correlated observed normal action: an explicit Sym2 covector changes
    # under the base boost but its held DeWitt norm is invariant. This small
    # geometry control does not replace full form/Clifford covariance.
    g = s.diag(-1, 1, 1, 1)
    B = s.Matrix([[s.Rational(5, 3), s.Rational(4, 3), 0, 0],
                  [s.Rational(4, 3), s.Rational(5, 3), 0, 0],
                  [0, 0, 1, 0], [0, 0, 0, 1]])
    Q = s.diag(0, 1, -1, 0)
    Qprime = B.inv().T * Q * B.inv()

    def dewitt_norm(T):
        E = g.inv()*T
        return s.expand(s.trace(E*E) - s.Rational(1, 2)*s.trace(E)**2)

    ck('observed rational boost Lorentz', B.T*g*B == g)
    ck('normal action is not inert', Qprime != Q)
    ck('correlated Sym2 action preserves normal norm',
       dewitt_norm(Qprime) == dewitt_norm(Q) == 2)

    return {
        'status': 'PASS',
        'check_names': checks,
        'check_count': len(checks),
        'fixture': {'kappa': 12, 'omega': '83/13', 'normal': '86/13',
                    'normal_square': str(normal_square), 'input_factor': -12},
        'opposed_force': record(force),
        'static_response': record(response),
        'receiver': {'form_mask': 2, 'clifford_mask': 2, 'value': '69696'},
        'scope': [
            'Actual selected frozen K95 printed symbol and polarized Q only.',
            'Strict Lorentz-core support nonclosure; regular static response survives.',
            'No physical massless eigenstate, gauge quotient, quantum gap or curved transfer.',
        ],
    }


def rotation(field, inverse=False):
    mapping={1:(4,1),4:(1,-1)} if not inverse else {1:(4,-1),4:(1,1)}
    def mask(m):
        seq=[];sgn=1
        for i in range(14):
            if m&(1<<i):
                j,v=mapping.get(i,(i,1));seq.append(j);sgn*=v
        sgn*=(-1)**sum(seq[i]>seq[j]for i in range(len(seq))for j in range(i+1,len(seq)))
        return sum(1<<i for i in seq),sgn
    out={}
    for (a,b),v in field.items():
        aa,sa=mask(a);bb,sb=mask(b);out[aa,bb]=out.get((aa,bb),0)+sa*sb*v
    return {k:s.expand(v)for k,v in out.items()if s.expand(v)!=0}

def build():
    checks=[]
    def ck(n,v):
        assert v,n
        checks.append(n)
    deps=dict(PINS)
    for p in PINS:
        if p.endswith('.json'):deps.update(json.loads((ROOT/p).read_text()).get('dependencies',{}))
    for p,h in deps.items():ck('reuse '+p,hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h)
    e=engine(D);core=core_controls(e);checks+=core['check_names']
    old=json.loads((ROOT/'lab/process/cw-fullsystem-domain-certificates.json').read_text())
    Fold={(a,b):s.sympify(v)for a,b,v in old['boosted_resonance']['force']}
    xiP={0:s.Rational(26,3),4:s.Rational(28,3),10:s.Integer(3)}
    xiM={0:-s.Rational(26,3),4:-s.Rational(28,3),10:s.Integer(3)}
    vp,vm=trace_mode(xiP),trace_mode(xiM)
    ck('rotated trace input covariance',vp==rotation(trace_mode({0:s.Rational(26,3),1:s.Rational(28,3),10:s.Integer(3)})))
    ck('rotated opposite trace covariance',vm==rotation(trace_mode({0:-s.Rational(26,3),1:-s.Rational(28,3),10:s.Integer(3)})))
    for name,xi,v in [('plus',xiP,vp),('minus',xiM,vm)]:
        z={a:s.I*x for a,x in xi.items()};native=e.Phi(e.wedge({(1<<a,0):x for a,x in z.items()},v))
        ck('rotated '+name+' actual kernel',not add(scale(12,v),native))
        ck('rotated '+name+' compact native adapter',native==compact_symbol(z,v))
        for label,func in [('real',s.re),('imaginary',s.im)]:
            ck('rotated '+name+' '+label+' primary-minus',e.real_skew({k:func(x)for k,x in v.items()if func(x)!=0}))
    N=s.Rational(28,3)**2-9
    ck('resonant pair inside Lorentz core',N==s.Rational(703,9) and N>36)
    ck('rotated pair sum',all(xiP.get(i,0)+xiM.get(i,0)==(6 if i==10 else 0)for i in range(14)))
    F=e.Phi(add(e.wedge(vp,vm),e.wedge(vm,vp)))
    ck('actual rotated quadratic covariance',F==rotation(Fold))
    receiver=lambda f:ell(boost_field(rotation(f,True),-1))
    ck('actual rotated nonzero receiver',receiver(F)==104448)
    ck('rotation invertible',rotation(rotation(F,True))==F)
    P0=lambda f:compact_symbol({10:6*s.I},f)
    At=lambda f:compact_symbol({0:s.Integer(1)},f)
    ck('rotation commutes output symbol',P0(F)==rotation(P0(Fold)))
    ck('rotation commutes time symbol',At(F)==rotation(At(Fold)))
    # Reuse scalarizer proof, compute only the actual rotated forcing jet.
    coeff=[s.Integer(1)]
    for a in FACTORS:
        nxt=[s.Integer(0)]*(len(coeff)+1)
        for j,c in enumerate(coeff):nxt[j]+=c;nxt[j+1]-=4*a*c
        coeff=nxt
    X,Y=F,{};BU,BV={},{}
    for n in range(40):
        alpha=sum(-c*(-12)**(39-2*j-n)*36**j for j,c in enumerate(coeff)if n<40-2*j)
        BU=add(BU,scale(alpha,X));BV=add(BV,scale(alpha,Y))
        if n<39:X,Y=P0(X),add(P0(Y),At(X))
    R=s.prod(s.Integer(144)-144*a for a in FACTORS if a!=1);den=4*144*R
    UF,VF=scale(1/den,BU),scale(1/den,BV)
    ck('actual rotated U force kernel',not add(scale(12,UF),P0(UF)))
    ck('actual rotated V force chain',not add(scale(12,VF),P0(VF),At(UF)))
    ck('actual rotated threshold forcing',receiver(UF)/6==104448)
    ck('actual rotated derivative forcing center zero',receiver(VF)==0)
    ck('actual rotated phase submersion',-6/s.Rational(26,3)==-s.Rational(9,13))
    # Scalar controls distinguish temporal prescriptions and mean cancellation.
    lam,t,eps=s.symbols('lam t eps',positive=True)
    G=-s.exp(-lam*t)/(2*lam)
    ck('Green away from origin',s.simplify(s.diff(G,t,2)-lam**2*G)==0)
    ck('Green derivative jump one',2*s.diff(G,t).subs(t,0)==1)
    pulse=1/(lam*(1+lam));zero=-1/((1+lam)*(2+lam))
    ck('nonzero mean pulse residue',s.limit(lam*pulse,lam,0,dir='+')==1)
    ck('zero mean cancellation control',s.simplify((1/(1+lam)-2/(2+lam))/lam-zero)==0)
    ck('zero mean bounded threshold',s.limit(zero,lam,0,dir='+')==-s.Rational(1,2))
    ck('nonzero mean transverse log divergence',s.limit(-s.log(eps),eps,0,dir='+')==s.oo)
    ck('free future decay reflects to growth',s.exp(-lam*t).subs(t,-t)==s.exp(lam*t))
    ck('decay is forward bounded',s.limit(s.exp(-lam*t),t,s.oo)==0)
    ck('reflected decay is not forward tempered',s.limit(s.exp(lam*t)/t**10,t,s.oo)==s.oo)
    row=lambda f:[[a,b,str(v)]for(a,b),v in sorted(f.items())]
    return {'schema':'gu-cw-symmetry-domain-v1','status':'PASS','probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies':deps,'check_count':len(checks),'check_names':checks,'lorentz_core':core,'rotated_resonance':{'input_normal_square':str(N),'force':row(F),'UF':row(UF),'VF':row(VF),'ell_rot_F':'104448','g1_center':'104448','phase_derivative':'-9/13','scope':'Computational ambient rotation, not observed Lorentz action mixing horizontal and normal.'},'limits':['Finite controls and actual sparse algebra only; no automated orbit, coarea or PDE theorem.','C2 tempered-history and ordinary Fourier-local L2 premises required.','No source-selected state/current, physical gap, quantum positivity, curved or K77 transfer.']}
if __name__=='__main__':
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group(required=True);g.add_argument('--write',action='store_true');g.add_argument('--verify',action='store_true');a=p.parse_args();t=time.monotonic();d=build()
    if a.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
    else:assert json.loads(OUT.read_text())==json.loads(json.dumps(d)),'certificate mismatch'
    print(json.dumps({'status':'PASS','checks':d['check_count'],'seconds':time.monotonic()-t}))
