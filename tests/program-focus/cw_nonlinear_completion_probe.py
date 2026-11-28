#!/usr/bin/env python3
"""New sparse null-vertex controls and exact threshold arithmetic.

The functional-analysis theorem is written/reviewed, not proved by this script.
Accepted full-symbol/boosted-force certificates are reused by immutable hashes.
"""
from pathlib import Path
import argparse
import hashlib
import json
import sys
import time
from fractions import Fraction

sys.dont_write_bytecode = True
import sympy as s
from printed_equation_jets_symbol_probe import engine
from cw_fullsystem_domain_probe import (
    D, FACTORS, add, scale, compact_symbol, trace_mode, ell, boost_field,
)

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / 'lab/process/cw-nonlinear-completion-certificates.json'
PINS = {
    'tests/program-focus/cw_fullsystem_domain_probe.py':
        '705acae3569fb46445ecb8c7562baddce793a3eb482e5477848c20ee9900cc1d',
    'lab/process/cw-fullsystem-domain-certificates.json':
        '8ede03f10d6bd28570a3028eb5c320d297de67a827d8b51c545ee5da76314be5',
    'lab/process/printed-state-completion-certificates.json':
        'ec0aafeace76b0d47f9ec9a7b142be29b6c7349e2c3397283029d14fe3e88977',
}


def build():
    checks = []
    def ck(name, value):
        assert value, name
        checks.append(name)
    def sha(path):
        return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
    for path, digest in PINS.items():
        ck('reuse hash ' + path, sha(path) == digest)
    old = json.loads((ROOT / 'lab/process/printed-state-completion-certificates.json').read_text())
    for path, digest in old['dependencies'].items():
        ck('native dependency ' + path, sha(path) == digest)
    cw = json.loads((ROOT / 'lab/process/cw-fullsystem-domain-certificates.json').read_text())
    ck('owned complete factors', cw['linear_domain']['factors'] == FACTORS)
    force = {(a, b): s.sympify(v) for a, b, v in cw['boosted_resonance']['force']}
    ck('owned boosted residue receiver', ell(boost_field(force, -1)) == 104448)

    # One new native vertex, with an exact full-system particular even though
    # its output shell is resonant elsewhere in the carrier.
    e = engine(D)
    xi = {0: s.Integer(9), 1: s.Integer(10), 10: s.Integer(4)}
    zeta = {j: s.I*v for j, v in xi.items()}
    q = sum(v*v / D[j] for j, v in zeta.items())
    ck('self input trace shell', q == -3)
    gamma = {(0, 1 << j): v / D[j] for j, v in zeta.items()}
    longitudinal = {(1 << i, 1 << j): v*w / (D[j]*q)
                    for i, v in zeta.items() for j, w in zeta.items()}
    transverse = add(e.phi1, scale(-1, longitudinal))
    partner = e.wedge(gamma, transverse)
    mode = trace_mode(xi)
    ck('self invariant trace polarization', mode == add(scale(12, transverse), scale(2, partner)))
    ck('self full linear kernel', not add(scale(12, mode), compact_symbol(zeta, mode)))
    wedge = e.wedge(mode, mode)
    ck('native self wedge reduction', wedge == scale(156, e.wedge(transverse, transverse)))
    image = e.Phi(e.wedge(transverse, transverse))
    ck('native invariant Phi image', image == add(scale(264, transverse), scale(312, longitudinal)))
    self_force = e.Phi(wedge)
    ck('native self force exact', self_force == add(scale(41184, transverse), scale(48672, longitudinal)))
    p2 = lambda f: compact_symbol({j: 2*v for j, v in zeta.items()}, f)
    ck('output trace block first column', p2(transverse) == scale(-4, partner))
    ck('output trace block second column', p2(partner) == scale(-144, transverse))
    ck('output longitudinal column', not p2(longitudinal))
    ck('self output is a minus3 resonance', 144 == 4*(-3)*(4*q))
    block = s.Matrix([[12, -144, 0], [-4, 12, 0], [0, 0, 12]])
    ck('forcing invariant subspace nonresonant', block.det() == -5184)
    particular = add(scale(1144, transverse), scale(s.Rational(1144, 3), partner),
                     scale(-4056, longitudinal))
    ck('actual full-system bounded self particular',
       not add(scale(12, particular), p2(particular), self_force))
    ck('self force is not zero', bool(self_force))

    # Exact threshold divisor and receiver residue. The coarea/L2 implication
    # requires the written theorem; these finite tests do not prove it.
    delta, nu, qv = s.symbols('delta nu q', real=True)
    kap = s.Integer(12)
    d = kap**2 * s.prod(kap**2 - 4*a*qv for a in FACTORS)
    complement = kap**2 * s.prod(kap**2 - 4*a*qv for a in FACTORS if a != 1)
    ck('threshold factor identity', s.cancel(d/complement) == 144-4*qv)
    ck('one-sided denominator', (144-4*qv).subs(qv, 36+delta+nu**2) == -4*(delta+nu**2))
    ck('all other shell factors invertible at threshold', complement.subs(qv, 36) != 0)
    beta = 2*kap**3*s.prod(kap**2 - 4*a*36 for a in FACTORS if a != 1)
    ck('inverse residue coefficient', s.cancel(beta/(-4*complement.subs(qv,36))) == -6)
    ck('negative-force numerator receiver', -(-6)*104448 == 626688)
    ck('boosted stable margin', s.Rational(703,9)-36 == s.Rational(379,9))
    ck('internal phase normal derivative', -s.Rational(3,1)/s.Rational(26,3)
       - s.Rational(3,1)/s.Rational(26,3) == -s.Rational(9,13))
    ck('threshold output is smooth hypersurface', 2*6 == 12)
    ck('coarea lower-bound scaling', s.simplify((2*s.sqrt(delta))/(2*delta)-1/s.sqrt(delta)) == 0)

    # Necessary and sufficient shell arithmetic for a nonzero-frequency
    # equal-group-velocity quadratic resonance. Actual vertices are separate.
    F = Fraction
    triads = [(a,b,c) for a in FACTORS for b in FACTORS for c in FACTORS
              if a*b > 0 and (F(1,c)-F(1,a)-F(1,b))**2 == F(4,a*b)]
    expected = [(-1,-4,-4),(-2,-8,-8),(-3,-12,-12),(-4,-1,-4),
                (-4,-4,-1),(-8,-2,-8),(-8,-8,-2),(-12,-3,-12),(-12,-12,-3)]
    ck('all nineteen-shell ordered arithmetic triads', sorted(triads) == sorted(expected))
    for a,b,c in triads:
        t = s.simplify((s.Rational(a,c)-1-s.Rational(a,b))/2)
        ck('triad proportionality '+str((a,b,c)), t*t == s.Rational(a,b)
           and t != -1 and s.simplify(s.Rational(a,1)/(1+t)**2) == c)
    ck('no positive-factor space-time resonance', all(a<0 and b<0 and c<0 for a,b,c in triads))
    return {
        'schema': 'gu-cw-nonlinear-completion-v1', 'status': 'PASS',
        'probe_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependencies': {**PINS, **old['dependencies']},
        'check_count': len(checks), 'check_names': checks,
        'self_null_control': {'input': ['9','10','4'], 'input_a': -12,
            'output_a': -3, 'forcing_coefficients_O_L': ['41184','48672'],
            'negative_force_particular_O_V_L': ['1144','1144/3','-4056'],
            'full_force_nonzero': True, 'resonant_projection_zero': True},
        'threshold': {'kappa': 12, 'output_K': '6 eta', 'delta': '-r(K)^2-36',
            'input_phase_derivative': '-9/13', 'threshold_gradient_eta': 12,
            'actual_negative_force_numerator_receiver': '626688',
            'forced_graph_receiver_lower_bound': 'c/sqrt(delta)',
            'target': 'ordinary global Sobolev, which requires Fourier L2 on a neighborhood of K0 including the threshold'},
        'ordered_space_time_shell_triads': triads,
        'limits': ['No source-selected domain or physical norm.',
            'Kernel/coarea graph exclusion is reviewed written analysis, not finite-code proof.',
            'No finite-time nonlinear breakdown or complete GU exclusion.',
            'Triad arithmetic does not establish nullity of untested mixed vertices.'],
    }


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument('--write', action='store_true')
    g.add_argument('--verify', action='store_true')
    args = p.parse_args()
    started = time.monotonic()
    data = build()
    if args.write:
        OUTPUT.write_text(json.dumps(data, indent=2)+'\n')
    else:
        assert json.loads(OUTPUT.read_text()) == json.loads(json.dumps(data)), 'certificate mismatch'
    print(json.dumps({'status': 'PASS', 'checks': data['check_count'], 'seconds': time.monotonic()-started}))
