#!/usr/bin/env python3
"""Exact printed quadratic resonance and completion controls.

No dense inversion or physical-state selection. Root integrates and executes;
contributors supplied independently scrutinized sparse algebra sketches.
"""
from pathlib import Path
import argparse,hashlib,json,sys,time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tests/program-focus'))
from printed_equation_jets_symbol_probe import engine
CERT=ROOT/'lab/process/printed-state-completion-certificates.json'
from fractions import Fraction as F
from math import prod
import sympy as sp
from source_action_deep_algebra import add, scale


FACTORS = [1, 12, 22, 30, 36, 40, 42] + list(range(-1, -13, -1))


def response_checks(e):
    checks = []
    kap, time_sign = F(12), F(-1)

    def ck(name, value):
        assert value, name
        checks.append(name)

    ck('orthonormal-frozen-K95', e.dim == 14 and tuple(e.d) == tuple(map(F, [-1, 1, 1, 1] + [1]*6 + [-1]*4)))

    def rec(field):
        return [[leg, c, str(z)] for (leg, c), z in sorted(field.items()) if z]

    def symbol(zeta, field):
        return e.Phi(e.wedge({(1 << i, 0): z for i, z in zeta.items() if z}, field))

    def ell(field):
        # This full mass-shifted cokernel row at n=3 is authenticated by
        # root's exhaustive26 XOR-capable-column check, not coker(P) alone.
        return sp.expand(field.get((1, 2), 0) - field.get((2, 1), 0)
                         - sp.I*field.get((1, 1026), 0)
                         + sp.I*field.get((2, 1025), 0))

    def trace_mode(xi, label):
        zeta = {i: sp.I*z for i, z in xi.items()}
        q = sum(z*z/e.d[i] for i, z in zeta.items())
        gamma = {(0, 1 << i): z/e.d[i] for i, z in zeta.items()}
        longitudinal = {(1 << i, 1 << j): z*w/e.d[j]/q
                        for i, z in zeta.items() for j, w in zeta.items()}
        O = add(e.phi1, scale(-1, longitudinal))
        V = e.wedge(gamma, O)
        mode = add(scale(kap, O), scale(2, V))
        ck(label+':trace-shell', q == -3)
        ck(label+':full-massive-mode', not add(scale(kap, mode), symbol(zeta, mode)))
        ck(label+':primary-minus-grades', all(c.bit_count() in (1, 2) for leg, c in mode))
        return mode

    def family(n):
        n = F(n)
        omega = (5*n-11)/(5-n)
        spatial = (n*n-5*n+14)/(5-n)
        ck(f'n={n}:rational-input-shell', spatial*spatial-omega*omega-n*n == 3)
        up = trace_mode({0: omega, 1: spatial, 10: n}, f'n={n}:plus')
        um = trace_mode({0: -omega, 1: -spatial, 10: n}, f'n={n}:minus')
        force = e.Phi(add(e.wedge(up, um), e.wedge(um, up)))
        ck(f'n={n}:actual-polarized-force', force == e.Phi(e.wedge(up, um, 'comm')))
        return {'n': n, 'omega': omega, 'p': spatial, 'q': 4*n*n,
                'zeta': {10: 2*sp.I*n}, 'force': force}

    def forcing_split(data):
        q, force, zeta = data['q'], data['force'], data['zeta']
        P = lambda field: symbol(zeta, field)
        powers = [force]
        for _ in range(5):
            powers.append(P(powers[-1]))
        # Force-specific, small Krylov identity, NOT a full-carrier identity.
        ck(f'n={data["n"]}:force-small-polynomial', not add(powers[5], scale(44*q, powers[3]), scale(-192*q*q, powers[1])))
        hook = scale(F(1)/(208*q*q), add(powers[4], scale(48*q, powers[2])))
        trace = scale(F(1)/(2496*q*q), add(powers[4], scale(-4*q, powers[2])))
        zero = add(force, scale(-1, hook), scale(-1, trace))
        phook, ptrace = P(hook), P(trace)
        ck(f'n={data["n"]}:hook-square', P(phook) == scale(4*q, hook))
        ck(f'n={data["n"]}:trace-square', P(ptrace) == scale(-48*q, trace))
        ck(f'n={data["n"]}:zero-sector-is-kernel', not P(zero))
        minus = scale(F(1, 2), add(hook, scale(-F(1)/(4*data['n']), phook)))
        plus = add(hook, scale(-1, minus))
        ck(f'n={data["n"]}:negative-hook-eigenvalue', P(minus) == scale(-4*data['n'], minus))
        ck(f'n={data["n"]}:positive-hook-eigenvalue', P(plus) == scale(4*data['n'], plus))
        return {'P': P, 'hook': hook, 'trace': trace, 'zero': zero,
                'phook': phook, 'ptrace': ptrace, 'minus': minus, 'plus': plus}

    resonant, generic = family(3), family(4)
    ck('family-hits-old-resonance', (resonant['omega'], resonant['p']) == (2, 4))
    ck('family-hits-new-generic-point', (generic['omega'], generic['p']) == (9, 10))
    rs, gs = forcing_split(resonant), forcing_split(generic)
    ck('old-force-receiver-reproduced', resonant['force'].get((1, 1)) == -22080)
    ck('mass-shifted-cokernel-force', ell(resonant['force']) == 104448)
    ck('resonant-obstruction-nonzero', bool(rs['minus']) and ell(rs['minus']) == 104448)
    residue = scale(F(1, 4), rs['minus'])
    ck('pole-residue-coordinate', residue.get((1, 2)) == 6528)
    ck('pole-residue-cokernel-row', ell(residue) == 26112)

    # A genuine nonzero compatible forcing at resonance: cancel just the
    # obstructing projection. This is calibration, not a selected source law.
    good_force = add(resonant['force'], scale(-1, rs['minus']))
    q = resonant['q']
    good_response = add(scale(-F(1)/kap, rs['zero']), scale(-F(1)/(2*kap), rs['plus']),
                        scale(-F(1)/(kap*kap+48*q), add(scale(kap, rs['trace']), scale(-1, rs['ptrace']))))
    ck('compatible-resonant-force-is-nonzero', bool(good_force))
    ck('compatible-resonant-force-has-zero-row', ell(good_force) == 0)
    ck('compatible-resonant-force-solved', not add(scale(kap, good_response), rs['P'](good_response), good_force))

    q = generic['q']
    ck('generic-three-denominators-nonzero', kap != 0 and kap*kap-4*q != 0 and kap*kap+48*q != 0)
    response = add(scale(-F(1)/kap, gs['zero']),
                   scale(-F(1)/(kap*kap-4*q), add(scale(kap, gs['hook']), scale(-1, gs['phook']))),
                   scale(-F(1)/(kap*kap+48*q), add(scale(kap, gs['trace']), scale(-1, gs['ptrace']))))
    ck('generic-actual-system-particular', not add(scale(kap, response), gs['P'](response), generic['force']))
    ck('generic-full-scalarizer-nonresonant', all(kap*kap-4*a*q != 0 for a in FACTORS))

    # Universal scalarizer coefficients m(z,q)=sum c_j z^(40-2j)q^j.
    coeff = [F(1)]
    for a in FACTORS:
        nxt = [F(0)]*(len(coeff)+1)
        for j, c in enumerate(coeff):
            nxt[j] += c
            nxt[j+1] -= 4*a*c
        coeff = nxt

    # Time polynomials use coefficients (t^0,t^1,t^2), never derivatives.
    def poly_add(*values):
        return [add(*(v[k] for v in values)) for k in range(3)]

    def poly_scale(scalar, value):
        return [scale(scalar, field) for field in value]

    def poly_dd(value):
        return [scale(2, value[2]), {}, {}]

    def box(value, q):
        return poly_add(poly_scale(q, value), poly_scale(time_sign, poly_dd(value)))

    def full_P(value, zeta):
        return [add(symbol(zeta, value[k]),
                    scale(k+1, symbol({0: F(1)}, value[k+1])) if k < 2 else {})
                for k in range(3)]

    def scalarizer(value, q):
        out = value
        for a in FACTORS:
            out = poly_add(poly_scale(kap*kap, out), poly_scale(-4*a, box(out, q)))
        return poly_scale(kap*kap, out)

    def B_apply(value, q, zeta):
        out = [{}, {}, {}]
        power = value
        for exponent in range(40):
            alpha = beta = F(0)
            for j, c in enumerate(coeff):
                r = 40-2*j
                if exponent < r:
                    factor = -c*(-kap)**(r-1-exponent)
                    alpha += factor*q**j
                    if j:
                        beta += factor*j*q**(j-1)
            # Box^j=q^j+j q^(j-1) s_time partial_t^2 on degree<=2.
            out = poly_add(out, poly_scale(alpha, power),
                           poly_scale(time_sign*beta, poly_dd(power)))
            if exponent != 39:
                power = full_P(power, zeta)
        return out

    q, force, zeta = resonant['q'], resonant['force'], resonant['zeta']
    ck('resonant-scalar-root-simple', kap*kap == 4*q and all(kap*kap-4*a*q != 0 for a in FACTORS if a != 1))
    dprime = kap*kap*(-4)*prod(kap*kap-4*a*q for a in FACTORS if a != 1)
    ck('scalar-root-derivative-nonzero', dprime != 0)
    auxiliary = [{}, {}, scale(F(1)/(2*time_sign*dprime), force)]
    ck('scalar-forced-polynomial', scalarizer(auxiliary, q) == [force, {}, {}])
    secular = B_apply(auxiliary, q, zeta)
    direct = poly_add(poly_scale(kap, secular), full_P(secular, zeta))
    ck('actual-system-secular-particular', direct == [force, {}, {}])
    ck('secular-quadratic-coefficient-nonzero', bool(secular[2]))
    ck('secular-leading-is-three-projections', secular[2] == scale(3, rs['minus']))
    ck('secular-leading-receiver', secular[2].get((1, 2)) == 78336)
    # The actual second-order nonlinear equation uses minus this particular.

    # Exact row ell P_tau. The owned compact symbol formula exhausts these
    # inputs: for longitudinal output0 the Clifford XOR shift is b; for
    # transverse output1 it is 1 XOR 0 XOR b. Both receiver pairs therefore
    # give two13-column candidate sets below (their union has26 columns).
    candidates = {(1 << b, target ^ (1 << b))
                  for b in range(1, 14) for target in (2, 1026)}
    ck('ell-Ptau-XOR-candidate-count', len(candidates) == 26)
    tau_row = {}
    for leg, blade in sorted(candidates):
        value = ell(symbol({0: F(1)}, {(leg, blade): F(1)}))
        if value:
            tau_row[(leg, blade)] = value
    ck('ell-Ptau-is-nonzero', bool(tau_row))
    functional = [ell(symbol({0: F(1)}, field)) for field in secular]
    ck('forced-ODE-functional-slope', functional[1] == 104448 and functional[2] == 0)
    for degree, field in enumerate(secular):
        ck('secular-L0-left-row:'+str(degree), ell(add(scale(kap, field), symbol(zeta, field))) == 0)

    return {
        'status': 'PASS', 'checks': len(checks), 'check_names': checks,
        'resonant': {'n': 3, 'q': str(resonant['q']), 'force': rec(force),
                     'cokernel_row_force': str(ell(force)), 'obstructing_projection': rec(rs['minus']),
                     'response_pole_residue': rec(residue)},
        'generic': {'n': 4, 'omega': '9', 'p': '10', 'q': str(generic['q']),
                    'force': rec(generic['force']), 'particular_for_negative_force': rec(response)},
        'compatible_resonance_control': {'force': rec(good_force), 'particular_for_negative_force': rec(good_response)},
        'secular_particular_for_positive_force': {'time_degree': 2, 'coefficients': [rec(v) for v in secular],
                                                  'dprime': str(dprime), 'leading_receiver': str(secular[2].get((1, 2)))},
        'forced_modal_ODE': {'ell_Ptau_row': rec(tau_row),
                            'ell_Ptau_secular_coefficients': [str(v) for v in functional],
                            'slope_for_negative_force': '-104448',
                            'consequence': 'Any all-time solution of Ptau Wprime+L0 W=-F has ell(Ptau W)=constant-104448*t and cannot be uniformly bounded in a fixed finite-dimensional norm.'},
        'analytic_family': {'omega': '(5*n-11)/(5-n)', 'p': '(n*n-5*n+14)/(5-n)',
                            'negative_hook_response': 'G(n)/(4*(n-3))', 'theta0_gamma1_residue': '6528'},
        'scope': [
            'Only the actual trace-pair input polarizations and their quadratic mixed Fourier coefficient are tested; no all19-channel stable-band assertion.',
            'The resonant obstruction is coker(kappa+P(i6eta)), not coker(P). It forbids frequency-locked algebraic quadratic slaving for this pair.',
            'The generic particular is one second-order coefficient, not a complete nonlinear state manifold or all-interaction closure.',
            'The explicit degree2-time response is a permitted frozen particular with no chosen physical boundary/initial prescription; it prevents an inference of insolubility or necessarily exponential forcing.',
            'The unbounded all-time modal functional concerns this second-order forced coefficient; it does not rule out local solutions, nonlinear resummation, extra resonant state variables, or physical boundedness of the full theory.',
            'No actual curved response, physical instability, source-required state rule or full-GU verdict follows.',
        ],
    }

def build():
    e=engine([-1,1,1,1]+[1]*6+[-1]*4)
    data=response_checks(e);checks=[]
    def ck(n,v):
        assert v,n
        checks.append(n)
    def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
    def ell(field):return sp.expand(field.get((1,2),0)-field.get((2,1),0)-sp.I*field.get((1,1026),0)+sp.I*field.get((2,1025),0))
    def P(z,field):return e.Phi(e.wedge({(1<<i,0):v for i,v in z.items()},field))
    # Complete left-kernel authentication, including the scalar mass columns.
    candidates=set()
    for leg,c in [(1,2),(2,1),(1,1026),(2,1025)]:
        candidates.add((leg,c));candidates.add((leg,c^1024))
        for b in range(14):
            if b!=10:candidates.add((1<<b,c^leg^1024^(1<<b)))
    ck('massive_left_row_candidate_count',len(candidates)==26)
    for key in sorted(candidates):
        f={key:F(1)}
        ck('massive_left_null_column:'+str(key),ell(add(scale(12,f),P({10:6*sp.I},f)))==0)
    # Reuse certificate custody and exact pre-existing actual-force bytes.
    oldp='lab/process/printed-nonlinear-transfer-certificates.json';old=json.loads((ROOT/oldp).read_text())
    ck('old_producer_binding',old['probe_sha256']==sha('tests/program-focus/printed_nonlinear_transfer_probe.py'))
    for p,h in old['dependencies'].items():ck('old_dependency:'+p,sha(p)==h)
    ck('actual_force_reused_exactly',old['stable_support']['cross_coefficient']==data['resonant']['force'])
    force={(a,b):sp.sympify(v)for a,b,v in data['resonant']['force']}
    for kap in [F(6),F(-6),F(24)]:
        ss=kap/12
        ck('coupling_scale_receiver:'+str(kap),ell(scale(ss*ss,force))==F(2176,3)*kap*kap)
        for key in [(1,2),(2,1025)]:
            f={key:F(1)}
            ck('coupling_scale_operator:'+str((kap,key)),add(scale(kap,f),P({10:sp.I*kap/2},f))==scale(ss,add(scale(12,f),P({10:6*sp.I},f))))
    # Benign ordinary nonlinear resonance: global polynomial/trigonometric
    # solution exists although the missing z cannot be a stationary graph.
    t,omega,rr,z0,n=sp.symbols('t omega rr z0 n',real=True)
    x=rr*sp.cos(omega*t);y=rr*sp.sin(omega*t);z=z0+rr*rr*t
    ck('benign_oscillator_x',sp.simplify(sp.diff(x,t)+omega*y)==0)
    ck('benign_oscillator_y',sp.simplify(sp.diff(y,t)-omega*x)==0)
    ck('benign_resonant_z',sp.trigsimp(sp.diff(z,t)-x*x-y*y)==0)
    ck('benign_no_stationary_full_orbit_graph',sp.simplify(x*x+y*y)==rr**2)
    om=(5*n-11)/(5-n);pp=(n*n-5*n+14)/(5-n)
    ck('analytic_family_identity',sp.factor(pp**2-om**2-n**2-3)==0)
    ck('pole_divisor',sp.expand(12-4*n+4*(n-3))==0)
    deps={p:sha(p)for p in ['tests/program-focus/source_action_deep_algebra.py','tests/program-focus/printed_equation_jets_symbol_probe.py','tests/program-focus/printed_differential_solvability_probe.py','explorations/conditional-build/printed-equation-jets-and-symbol-2026-11-27.md','explorations/conditional-build/printed-differential-solvability-2026-11-27.md','explorations/conditional-build/printed-nonlinear-transfer-2026-11-27.md',oldp]}
    return {'schema':'gu-printed-state-completion-v1','status':'PASS','probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies':deps,'native_response_checks':data,'extra_check_names':checks,'check_count':data['checks']+len(checks),'left_receiver':{'rows':[[1,2,'1'],[2,1,'-1'],[1,1026,'-I'],[2,1025,'I']],'capable_columns':len(candidates),'actual_force':'104448','all_kappa_force':'2176*kappa^2/3'},'scope':'Frozen K95 actual printed P,Q. Exact finite algebra, full forced response and controls; universal graph/PDE statements remain reviewed written proofs. No source physical domain or curved nonlinear theorem.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group(required=True);g.add_argument('--write-certificate',action='store_true');g.add_argument('--verify',action='store_true');a=p.parse_args();t=time.monotonic();d=build()
    if a.write_certificate:CERT.write_text(json.dumps(d,indent=2)+'\n')
    else:assert json.loads(CERT.read_text())==d,'certificate differs'
    print(json.dumps({'status':'PASS','checks':d['check_count'],'force_receiver':d['left_receiver']['actual_force'],'secular_degree':d['native_response_checks']['secular_particular_for_positive_force']['time_degree'],'seconds':time.monotonic()-t}))
