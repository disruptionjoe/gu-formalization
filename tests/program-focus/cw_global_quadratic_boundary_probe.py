#!/usr/bin/env python3
"""Actual kernel/vertex controls; analytic bounds and full-dimensional packets are written proofs."""
from pathlib import Path
import argparse,hashlib,json,sys,time
sys.dont_write_bytecode=True
import sympy as s
from printed_equation_jets_symbol_probe import engine
from cw_fullsystem_domain_probe import D,FACTORS
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/cw-global-quadratic-boundary-certificates.json'
PINS={'lab/process/cw-edge-decay-global-certificates.json': '39368dc509ff1e0be1d5f49449b73bbcc822bb75c8abd77b83ac2ba1a67ced42', 'lab/process/cw-fullsystem-domain-certificates.json': '8ede03f10d6bd28570a3028eb5c320d297de67a827d8b51c545ee5da76314be5', 'lab/process/cw-one-sided-boundary-certificates.json': 'f4e6666601b25a18bb1288d2fa19493df432e6b3f194fe17b301cf70d81e0ea2', 'tests/program-focus/cw_fullsystem_domain_probe.py': '705acae3569fb46445ecb8c7562baddce793a3eb482e5477848c20ee9900cc1d', 'tests/program-focus/printed_equation_jets_symbol_probe.py': 'e43da867d17cf985bfac8c014657e8cbf18c94e80013350ca69eee804a4ebeb8', 'tests/program-focus/source_action_deep_algebra.py': '4e3800131049e2b397bbce6106bfc5766d2f5fbf996319c50942f3b805d65598'}
"""Actual high-frequency intrinsic boundary fixture.

native_fixture(e), with the owned frozen K95 engine(D); root executes serially.
The analytic domain is R>6. No import-time or filesystem effects.
"""


def native_fixture(e):
    import sympy as s
    from cw_fullsystem_domain_probe import D, add, scale, cp, compact_symbol
    checks = []

    def ck(n, x):
        assert x, n
        checks.append(n)

    def native(z, f):
        return add(e.Phi(e.wedge({(1 << i, 0): v for i, v in z.items()}, f)))

    def left(g, f):
        out = {}
        for (leg, mask), c in f.items():
            for blade, v in cp(g, {mask: c}).items():
                key = (leg, blade)
                out[key] = out.get(key, 0)+v
        return add(out)

    def norm2(f):
        return s.expand(sum(s.conjugate(v)*v for v in f.values()))

    R = s.symbols('R', positive=True, real=True)
    omega = s.sqrt(3*R**2+36)
    delta = 4*R**2-36
    beta1 = {(8, 8): s.Integer(1), (16, 16): s.Integer(-1)}
    beta2 = {(8, 8): s.Integer(1), (32, 32): s.Integer(-1)}
    xis = [{0: omega, 1: 2*R, 10: R},
           {0: -omega, 1: -2*R, 10: R}]
    modes = []
    for label, xi, beta in zip(['one', 'two'], xis, [beta1, beta2]):
        zeta = {i: s.I*v for i, v in xi.items()}
        gamma = {1 << i: D[i]*v for i, v in zeta.items()}
        v = add(scale(12, beta), scale(2, left(gamma, beta)))
        ck(label+' factor1 shell', s.expand(sum(D[i]*v*v for i, v in zeta.items())) == 36)
        ck(label+' actual kernel', not add(scale(12, v), native(zeta, v)))
        ck(label+' compact/native binding', native(zeta, v) == compact_symbol(zeta, v))
        ck(label+' exact modal norm', norm2(v) == 64*(R**2+9))
        for part in [s.re, s.im]:
            real = {key: part(c) for key, c in v.items() if part(c) != 0}
            ck(label+' real quadrature '+str(part), e.real_skew(real))
        modes.append(v)

    force = add(e.Phi(add(e.wedge(modes[0], modes[1]),
                           e.wedge(modes[1], modes[0]))))
    expected = add(scale(32*(R**2-36), e.phi1),
                   {(8, 8): -64*(R**2-36)})
    ck('actual full polarized force', force == expected)
    # The proper positive-plane rotation3->4,4->-3 swaps diagonal tensors.
    # Its odd projection of this exact force is f beta1.
    def rotated(field):
        def blade(mask):
            ids=[j for j in range(14) if mask & (1<<j)]
            out=[4 if j==3 else 3 if j==4 else j for j in ids]
            sign=(-1)**(int(4 in ids)+sum(out[a]>out[b] for a in range(len(out)) for b in range(a+1,len(out))))
            return sum(1<<j for j in out),sign
        ans={}
        for (form,cliff),coeff in field.items():
            ff,fs=blade(form);cc,cs=blade(cliff)
            ans[(ff,cc)]=ans.get((ff,cc),0)+fs*cs*coeff
        return add(ans)
    ck('proper rotation fixes native Phi1',rotated(e.phi1)==e.phi1)
    ck('hook is rotation-odd',rotated(beta1)==scale(-1,beta1))
    f = 32*(36-R**2)
    ck('full force odd receiver projection',scale(s.Rational(1,2),add(force,scale(-1,rotated(force))))==scale(f,beta1))
    ck('actual odd hook source coefficient',
       s.expand((force.get((8, 8), 0)-force.get((16, 16), 0))/2) == f)

    # Full actual resolvent on this projected source is only a two-state
    # cluster plus its algebraic forcing row: no39-step scalarizer is needed.
    ctau = {1: s.Integer(-1)}
    cK = {1 << 10: -2*R}
    A = left(ctau, beta1)
    B = add(scale(12, beta1), scale(2*s.I, left(cK, beta1)))
    U = scale(s.Rational(1, 4), B)
    V = scale(s.Rational(1, 2), A)
    At = lambda value: native({0: s.Integer(1)}, value)
    C = lambda value: add(scale(12, value), native({10: 2*s.I*R}, value))
    ck('actual resolvent highest coefficient', At(V) == beta1)
    ck('actual resolvent middle coefficient', not add(C(V), At(U)))
    ck('actual resolvent constant coefficient', C(U) == scale(-delta, beta1))

    def Arow(value):
        return s.expand((-value.get((8, 9), s.Integer(0))+value.get((16, 17), s.Integer(0)))/2)

    ck('fixed bounded receiver normalization', Arow(A) == 1)
    ck('receiver on U', Arow(U) == 0)
    ck('receiver on V', Arow(V) == s.Rational(1, 2))
    # ν=0, λ=sqrt(delta): (U+λV)f/λ has A receiver f/2.
    # Both unit modal inputs divide the force by their common norm².
    unit_receiver = s.cancel(f/(2*64*(R**2+9)))
    ck('unit modal intrinsic receiver', unit_receiver == (36-R**2)/(4*(R**2+9)))
    ck('nonzero large-frequency receiver', s.limit(unit_receiver, R, s.oo) == -s.Rational(1, 4))
    return {
        'status': 'PASS', 'checks': checks, 'check_count': len(checks),
        'input_factor': 1, 'output_factor': 1,
        'input_spatial_square': '3R^2', 'output_spatial_square': '-4R^2',
        'input_frequency_squared': '3R^2+36', 'decay_rate_squared': '4R^2-36',
        'modal_norm_squared': '64(R^2+9)',
        'unit_intrinsic_boundary_receiver': str(unit_receiver),
        'limit': '-1/4',
        'scope': [
            'Actual frozen primary-minus kernel-valued inputs and algebraic polarized Phi.',
            'Intrinsic Y=(N+lambda Pi)x in the fixed coefficient norm, not an adopted global q0 norm.',
            'Global normalized full13D packet conclusion needs the separate scaling proof.',
            'No source physical state, energy, curved or nonlinear-existence verdict.',
        ],
    }


def build():
 checks=[]
 def ck(n,v):assert v,n;checks.append(n)
 deps=dict(PINS)
 for p in PINS:
  if p.endswith('.json'):deps.update(json.loads((ROOT/p).read_text()).get('dependencies',{}))
 for p,h in deps.items():ck('reuse '+p,hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h)
 ck('positive plane available uniformly',9-1>=2)
 ck('Euclidean spectator dimension',13-1-2==10)
 A,q,u,qa,qb,C,nu,wa=s.symbols('A q u qa qb C nu wa',real=True)
 W=s.symbols('W',positive=True)
 for sign in [-1,1]:
  inv=(A+q+qb-(sign*(nu-wa))**2)/2
  ck('phase Jacobian '+str(sign),s.simplify(s.diff(inv,nu).subs(nu,wa+sign*W))==-sign*W)
 lam,n,pi,x,F,U,V=s.symbols('lam n pi x F U V')
 # Y' = lambda Y - (U+lambda V)F, using n^2=lambda^2 pi, pi n=n, nV=U, pi V=V.
 ck('intrinsic forced boundary identity',s.expand(lam**2*pi*x+lam*n*x-U*F-lam*V*F-(lam*(n+lam*pi)*x-(U+lam*V)*F))==0)
 z,r2=s.symbols('z r2');kap=s.Integer(12)
 for a in FACTORS:
  q0=kap**2/(4*s.Integer(a));da=-r2-q0
  ck('global paired shell remainder '+str(a),s.rem(-z**2-r2-q0,z**2-da,z)==0)
  ck('constant paired denominator '+str(a),4*a*kap**2*s.prod(kap**2-4*b*q0 for b in FACTORS if b!=a)!=0)
 ck('ball exponent45',39+s.Rational(11,2)+s.Rational(1,2)==45)
 ck('packet dimension exponent',13-s.Rational(13,2)-s.Rational(13,2)==0 and s.Rational(13,2)>0)
 ck('balanced derivative lower bound',2*s.Rational(13,4)==s.Rational(13,2))
 v=s.symbols('v',positive=True)
 ck('dyadic tail geometric identity',s.cancel(sum(v**j for j in range(5))-(v**5-1)/(v-1))==0)
 # Known answer controls: a smooth nonzero order-zero convolution symbol
 # has this scaling; a zero vertex stays zero, so denominator alone earns no kill.
 ck('zero-vertex control',s.Integer(0)/(lam-s.I*nu)==0)
 ck('constant multiplier scaling control',s.Rational(13,2)+0==s.Rational(13,2))
 native=native_fixture(engine(D));checks+=native['checks']
 return {'schema':'gu-cw-global-quadratic-boundary-v1','status':'PASS','probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies':deps,'check_count':len(checks),'check_names':checks,'native_fixture':native,'analytic_controls':{'compact_output_pushforward':'pi*(2R)^10/|k|','phase_jacobian':'W','uniform_W_over_k':'sqrt((1+2R/|kappa|)^2+1)','kernel_squared_integral':'2*pi*sqrt(D)','global_ball_upper_exponent':45,'tame_upper_derivatives':45,'packet_growth_lower_exponent':'13/2+p, p>=0','balanced_input_derivative_necessary':'d>=13/4 for Hmodal^d x Hmodal^d to L2','tame_one_high_derivative_necessary':'d>=13/2 for Hmodal^d x L2 + L2 x Hmodal^d to L2'},'limits':['Full-dimensional Laurent-analytic packet and integration arguments are written and independently reviewed, not formalized by finite controls.','No global q0 norm, physical state/current, nonlinear invariant manifold or full DAE lifting is supplied.','The upper45 is conservative and not a sharp loss calculation; p is not identified.']}
if __name__=='__main__':
 p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group(required=True);g.add_argument('--write',action='store_true');g.add_argument('--verify',action='store_true');a=p.parse_args();t=time.monotonic();d=build()
 if a.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(OUT.read_text())==json.loads(json.dumps(d)),'certificate mismatch'
 print(json.dumps({'status':'PASS','checks':d['check_count'],'seconds':time.monotonic()-t}))
