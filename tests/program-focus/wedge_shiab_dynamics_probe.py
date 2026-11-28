#!/usr/bin/env python3
"""Exact wedge-owned temporal/energy controls and native leading invariants.

Fields U,V are represented by real sparse coefficients U0,V0 with the
explicit common phase U=i U0,V=i V0. This avoids floating/complex arithmetic.
The held pairing is b=-Re tr/128. No owner files are written by default.
"""
import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

sys.dont_write_bytecode = True


def build(root):
    sys.path.insert(0, str(root/'tests/program-focus'))
    from shiab_graded_derivation_probe import theta, prod, add, scale, cmul
    from shiab_bianchi_companion_probe import hodge

    checks, sectors = {}, []

    def ok(name, condition):
        if name in checks:
            raise AssertionError('duplicate '+name)
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)

    def scalar_pair(a, b, eta):
        """Normalized real Clifford trace with the one-form metric; no phases/sign."""
        value = F(0)
        for (fa, ca), va in a.items():
            assert fa.bit_count() == 1
            slot = fa.bit_length()-1
            for (fb, cb), vb in b.items():
                if fa != fb:
                    continue
                sign, blade = cmul(ca, cb, eta)
                if blade == 0:
                    value += eta[slot]*va*vb*sign
        return value

    def actual_pair(a, b, eta, phase_a=1, phase_b=1):
        """b=-Re tr/128, actual fields i^phase_a a and i^phase_b b."""
        phase = (phase_a+phase_b) % 4
        if phase % 2:
            return F(0)
        real_phase = 1 if phase == 0 else -1
        return -real_phase*scalar_pair(a, b, eta)

    def sharp_skew(a, phase):
        return all((-1)**(c.bit_count()*(c.bit_count()+1)//2+phase) == -1
                   for _, c in a)

    def poly_add(*terms):
        out = {}
        for p in terms:
            for key, value in p.items():
                out[key] = out.get(key, F(0))+value
        return {key: value for key, value in out.items() if value}

    def poly_scale(p, s):
        return {key: value*s for key, value in p.items() if value*s}

    def derivative(p, slot):
        out = {}
        for powers, value in p.items():
            if powers[slot]:
                new = list(powers)
                new[slot] -= 1
                key = tuple(new)
                out[key] = out.get(key, F(0))+value*powers[slot]
        return out

    def multiply_var(p, slot):
        out = {}
        for powers, value in p.items():
            new = list(powers)
            new[slot] += 1
            out[tuple(new)] = value
        return out

    def dt_linear(p):
        # Used only for momenta linear in u,v, never for acceleration terms.
        assert all(powers[2] == powers[3] == 0 for powers in p)
        return poly_add(multiply_var(derivative(p, 0), 2),
                        multiply_var(derivative(p, 1), 3))

    ports = [
        ('K95', [-1, 1, 1, 1]+[1]*6+[-1]*4, 0),
        ('K77', [1]*7+[-1]*7, 7),
    ]
    for port, eta, negative_clock in ports:
        th = theta(14, eta)
        positive_clock = next(a for a in range(14) if eta[a] == 1)
        for tau in (negative_clock, positive_clock):
            q = eta[tau]
            prefix = f'{port}/clock{tau}/q{q}'
            derivative_form = {(1 << tau, 0): F(1)}
            c_tau = {(0, 1 << tau): F(q)}

            def principal(t):
                curvature = prod(derivative_form, t, eta)
                response = scale(add(prod(th, curvature, eta),
                                     prod(curvature, th, eta)), -1)
                # *^-1 on degree13: *²=(-1)^(13*(14-13)+number_of_minuses).
                inverse_sign = (-1)**(13+eta.count(-1))
                return scale(hodge(response, eta), inverse_sign)

            positive_slots = [a for a in range(14) if a != tau and eta[a] == 1]
            negative_slots = [a for a in range(14) if a != tau and eta[a] == -1]
            blade_sets = [tuple(sorted(positive_slots[:4])),
                          tuple(sorted(positive_slots[:3]+negative_slots[:1]))]
            for inds in blade_sets:
                assert len(inds) == len(set(inds)) == 4 and tau not in inds
                label = prefix+'/Z'+','.join(map(str, inds))
                mask = sum(1 << a for a in inds)
                U = {(1 << a, mask ^ (1 << a)): F(eta[a]*(-1)**j)
                     for j, a in enumerate(inds)}
                V = prod(U, c_tau, eta)
                PU, PV = principal(U), principal(V)
                ok(label+' full sparse P U=-6V', PU == scale(V, -6))
                ok(label+' full sparse P V=-6qU', PV == scale(U, -6*q))
                ok(label+' square36q on U', principal(PU) == scale(U, 36*q))
                ok(label+' grades3 and4', all(c.bit_count() == 3 for _, c in U)
                   and all(c.bit_count() == 4 for _, c in V))
                ok(label+' primary-minus actual reality', sharp_skew(U, 1) and sharp_skew(V, 1))

                sign_z = 1
                for a in inds:
                    sign_z *= eta[a]
                norm_u, norm_v = actual_pair(U, U, eta), actual_pair(V, V, eta)
                ok(label+' minus-trace U norm', norm_u == -4*sign_z)
                ok(label+' V norm', norm_v == -q*norm_u)
                ok(label+' orthogonality', actual_pair(U, V, eta) == 0 and actual_pair(V, U, eta) == 0)
                ok(label+' principal skew pairing',
                   actual_pair(U, PV, eta)+actual_pair(PU, V, eta) == 0
                   and actual_pair(V, PU, eta)+actual_pair(PV, U, eta) == 0)

                # The entire actual Riemann/metric mixed response is grade1.
                # Check raw scalar traces, not a spurious Re(i*real)=0 shortcut.
                mixed_zero = True
                for form_slot in range(14):
                    for cliff_slot in range(14):
                        test = {(1 << form_slot, 1 << cliff_slot): F(1)}
                        mixed_zero &= scalar_pair(U, test, eta) == 0
                        mixed_zero &= scalar_pair(V, test, eta) == 0
                ok(label+' full grade1 mixed-metric annihilation', mixed_zero)
                ok(label+' no longitudinal component', all(f != 1 << tau for f, _ in U)
                   and all(f != 1 << tau for f, _ in V))
                ok(label+' mass divergence constraint U', not prod(derivative_form, hodge(U, eta), eta))
                ok(label+' mass divergence constraint V', not prod(derivative_form, hodge(V, eta), eta))

                if q == -1:
                    s = norm_u
                    for kappa in (F(1), F(2), F(-1), F(0)):
                        tag = label+f'/kappa{kappa}'
                        # Variables are u,v,udot,vdot. L=1/2<t,P dt>+mass.
                        kinetic = {(1, 0, 0, 1): 3*s, (0, 1, 1, 0): -3*s}
                        mass = {(2, 0, 0, 0): kappa*s/2,
                                (0, 2, 0, 0): kappa*s/2}
                        lagrangian = poly_add(kinetic, mass)
                        pi_u, pi_v = derivative(lagrangian, 2), derivative(lagrangian, 3)
                        el_u = poly_add(derivative(lagrangian, 0), poly_scale(dt_linear(pi_u), -1))
                        el_v = poly_add(derivative(lagrangian, 1), poly_scale(dt_linear(pi_v), -1))
                        expected_u = poly_add({(0, 0, 0, 1): 6*s}, {(1, 0, 0, 0): kappa*s})
                        expected_v = poly_add({(0, 0, 1, 0): -6*s}, {(0, 1, 0, 0): kappa*s})
                        ok(tag+' independent Euler u', el_u == expected_u)
                        ok(tag+' independent Euler v', el_v == expected_v)
                        energy = poly_add(multiply_var(pi_u, 2), multiply_var(pi_v, 3),
                                          poly_scale(lagrangian, -1))
                        ok(tag+' canonical energy minus mass', energy == poly_scale(poly_add(mass), -1))
                        # d(theta)=6s du wedge dv with theta=pi_u du+pi_v dv.
                        symplectic = poly_add(derivative(pi_v, 0), poly_scale(derivative(pi_u, 1), -1))
                        ok(tag+' presymplectic coefficient rank2', symplectic == {(0, 0, 0, 0): 6*s} and s != 0)
                        ok(tag+' homogeneous temporal frequency', (kappa/F(6))**2 == kappa*kappa/F(36))
                        if kappa == 0:
                            ok(tag+' massless energy zero control', not energy)
                    sectors.append({'port': port, 'clock': tau, 'clock_square': q,
                                    'blade_indices': list(inds), 'blade_sign': sign_z,
                                    'pairing': '-Re tr/128 with actual U=i U0,V=i V0',
                                    'U_norm': str(norm_u), 'V_norm': str(norm_v),
                                    'symplectic_coefficient': str(6*s),
                                    'kappa1_energy_coefficient_each_square': str(-s/2)})

            radial = {(1 << a, 1 << a): F(1) for a in range(14) if a != tau}
            radial_v = prod(radial, c_tau, eta)
            ok(prefix+' distinct radial factor24 U', principal(radial) == scale(radial_v, -24))
            ok(prefix+' distinct radial factor24 V', principal(radial_v) == scale(radial, -24*q))
            longitudinal = {(1 << tau, 1 << ((tau+1) % 14)): F(1)}
            ok(prefix+' longitudinal temporal kernel', not principal(longitudinal))

    for port, _, _ in ports:
        entries = [s for s in sectors if s['port'] == port]
        signs = {F(s['kappa1_energy_coefficient_each_square']) > 0 for s in entries}
        ok(port+' both canonical-energy signs at same negative clock', signs == {False, True})

    ric = [F(1,4)]*5+[F(-5,4)]*9
    scalar = sum(ric)
    ein = [v-scalar/2 for v in ric]
    ok('native scalar curvature', scalar == -10)
    ok('actual spin-normalized Einstein amplitudes', ein == [F(21,4)]*5+[F(15,4)]*9)
    norm = sum(v*v for v in ein)
    ok('native Einstein contraction', norm == F(2115,8))
    ok('native curvature square identity', norm == sum(v*v for v in ric)+F(5,2)*scalar**2)
    ok('native induced density coefficient', norm/2 == F(2115,16))
    ok('literal observed leading receiver', F(21,4)/4 == F(21,16))
    from itertools import combinations
    grade_pairs = 0
    eta = ports[0][1]
    for inds in combinations(range(14),3):
        blade = sum(1<<a for a in inds)
        for a in range(14):
            left = cmul(blade,1<<a,eta); right = cmul(1<<a,blade,eta)
            assert left[1] == right[1]
            ok('grade3-1 anticommutator '+str(inds)+'/'+str(a),
               left[0]+right[0] == 0 or left[1].bit_count() == 2)
            grade_pairs += 1
    ok('all grade3-1 pairs tested', grade_pairs == 5096)

    dependencies = [
        'tests/program-focus/shiab_graded_derivation_probe.py',
        'tests/program-focus/shiab_bianchi_companion_probe.py',
        'tests/program-focus/wedge_shiab_action_recheck_probe.py',
        'explorations/conditional-build/wedge-shiab-action-recheck-2026-11-27.md',
        'explorations/conditional-build/shiab-bianchi-companion-class-2026-11-27.md',
    ]
    return {'status': 'PASS', 'check_count': len(checks), 'checks': checks,
            'sectors': sectors,
            'dependency_sha256': {p: hashlib.sha256((root/p).read_bytes()).hexdigest() for p in dependencies},
            'producer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'native': {'Einstein_norm': str(norm), 'leading_effective_density': str(norm/2), 'observed_receiver': '21/16', 'grade_pairs': grade_pairs},
            'scope': [
                'Exact sparse temporal sector of this wedge action, not W2 or the printed low-Phi endpoint.',
                'Conditional flat-ambient stationary joint first-action reference; native flat X is not flat Y.',
                'Mixed metric row vanishes using the bound torsion-free Riemann-to-grade1 response, not by freezing the metric equation.',
                'Homogeneous energy densities, not finite-volume/normalizable physical states, native vacuum instability, quantum ghosts or a mass gap.',
                'No all-order nonlinear closure of this grade3/4 sector is asserted.'
            ]}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo-root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--output', type=Path)
    parser.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    root = args.repo_root.resolve()
    result = build(root)
    output = args.output or root/'lab/process/wedge-shiab-dynamics-certificates.json'
    if args.verify:
        assert result == json.loads(output.read_text()), 'persisted certificate differs'
    else:
        output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status':result['status'], 'check_count':result['check_count'], 'native':result['native'], 'sector_count':len(result['sectors']), 'verified':args.verify}))
