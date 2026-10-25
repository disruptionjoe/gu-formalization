"""Exact small-factor checks for a specified independent-dual kinetic bar.

No predecessor code imports or full 1408/1920 matrix assembly. Universal claims
are proved in the associated artifact; finite fixtures are controls only.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
REPORT = 'lab/process/k2056-common-dual-successor.json'
PINS = {
    'explorations/conditional-build/k2038-observed-action-compression-2026-10-24.md': 'fd73ae69845af69c0b33dd7d59760b80071ede188fb4baa2a991eb13f207d8ab',
    'tests/channel-swings/k2038_observed_action_compression_probe.py': 'ba44f4a112539255574f7f165bf9cc29c6084c5c3d3bc5c28ce23816771d25b5',
    'explorations/conditional-build/k2021-common-degree-dual-operator-2026-10-24.md': '06023c99126ddeb43e48a3d5fb83b95bf0bef025f60e341810011653aaad55ac',
}


def add(*terms):
    out = {}
    for a, matrix in terms:
        for ij, value in matrix.items():
            out[ij] = out.get(ij, 0) + a * value
    return {ij: value for ij, value in out.items() if value}


def mul(a, b):
    rows = {}
    for (i, j), value in b.items():
        rows.setdefault(i, []).append((j, value))
    out = {}
    for (i, k), v in a.items():
        for j, w in rows.get(k, []):
            out[i, j] = out.get((i, j), 0) + v * w
    return {ij: v for ij, v in out.items() if v}


def trans(a):
    return {(j, i): v for (i, j), v in a.items()}


def identity(n):
    return {(i, i): F(1) for i in range(n)}


def gamma(k):
    q = 6 - k % 7
    out = {}
    for col in range(128):
        sign = (-1) ** ((col >> (q + 1)).bit_count())
        if k >= 7:
            sign *= 1 if col & (1 << q) else -1
        out[col ^ (1 << q), col] = F(sign)
    return out


def product(xs):
    out = identity(128)
    for x in xs:
        out = mul(out, x)
    return out


# Gaussian rational sparse matrices, represented by (real, imaginary) pairs.
def zmul(a, b):
    out = {}
    for (i, k), (x, y) in a.items():
        for (l, j), (u, v) in b.items():
            if k == l:
                r, s = out.get((i, j), (F(0), F(0)))
                out[i, j] = (r+x*u-y*v, s+x*v+y*u)
    return {ij:z for ij,z in out.items() if z != (0,0)}


def zconj(a):
    return {ij:(x,-y) for ij,(x,y) in a.items()}


def zscale(a, scalar):
    x,y=scalar
    return {ij:(x*u-y*v,x*v+y*u) for ij,(u,v) in a.items()}


def zreal(a):
    return {ij:(v,F(0)) for ij,v in a.items()}


def produce(root):
    for name, digest in PINS.items():
        assert hashlib.sha256((root / name).read_bytes()).hexdigest() == digest
    checks = []

    def check(name, truth):
        assert truth, name
        checks.append(name)

    gs = [gamma(k) for k in range(14)]
    ii = identity(128)
    b = product(gs[7:]); volume = product(gs)
    wb = add((F(3, 2), ii), (F(1, 2), volume))
    g = mul(b, gs[0]); f = add((-1, mul(g, wb)))
    check('G_squared_minus_identity', mul(g, g) == add((-1, ii)))
    check('G_skew', trans(g) == add((-1, g)))
    check('G_commutes_Wbar', mul(g, wb) == mul(wb, g))
    check('F_squared_minus_Wbar_squared', mul(f, f) == add((-1, mul(wb, wb))))
    check('both_ambient_halves_retained', sorted(volume.values()) == [F(-1)] * 64 + [F(1)] * 64 and all(i == j for i, j in volume))
    c = {(i, j): F(10 if i == j == 0 else 4 if i == 0 or j == 0 else int(i != j)) for i in range(11) for j in range(11)}
    c = {ij: v for ij, v in c.items() if v}
    i11 = identity(11)
    p2 = {(0, 0): F(1)}
    p2.update({(i, j): F(1, 10) for i in range(1, 11) for j in range(1, 11)})
    pp = add((1, i11), (-1, p2)); c2 = mul(c, p2)
    numerator = add((19, c2), (140, p2))
    check('copy_projection', mul(p2, p2) == p2)
    check('transverse_copy_minus_identity', mul(c, pp) == add((-1, pp)))
    check('two_copy_minimal_polynomial', mul(c2, c2) == add((19, c2), (70, p2)))
    check('absolute_copy_radical_identity', mul(numerator, numerator) == add((641, mul(c2, c2))))
    check('orthogonal_copy_sectors', not mul(pp, numerator))
    check('radical_positive_root_bracket', 25 ** 2 < 641 < 26 ** 2)
    j = {(0, 1): F(1), (1, 0): F(-1)}; i2 = identity(2)
    half_controls = []
    for w in (F(1), F(2)):
        t = add((w, j)); ti = add((-1 / w, j)); pstar = add((w, i2))
        r = add((-1, mul(ti, pstar)))  # A=iR, so Abar(A)=R^2.
        check('kinetic_sign_half_' + str(w), mul(trans(r), t) == pstar)
        check('anti_square_half_' + str(w), mul(r, r) == add((-1, i2)))
        check('P_I_square_half_' + str(w), mul(ti, ti) == add((-1 / (w*w), i2)))
        check('compatibility_half_' + str(w), mul(mul(pstar, ti), pstar) == add((-1, t)))
        half_controls.append({'Wbar': str(w), 'P_I_bar_square': str(-1 / (w*w)), 'Pstar_bar_square': '-1'})
    pind = {(0, 0): F(1), (1, 1): F(-1)}
    rind = mul(j, pind)
    check('indefinite_kinetic_sign', mul(trans(rind), j) == pind)
    check('indefinite_involution_survives', mul(rind, rind) == i2)
    complex_controls=[]
    for w in (F(1),F(2)):
        p={(0,0):(2*w,F(0)),(0,1):(F(0),w),
           (1,0):(F(0),-w),(1,1):(w,F(0))}
        tz=zreal(add((w,j))); tiz=zreal(add((-1/w,j)))
        az=zscale(zmul(tiz,zconj(p)),(F(0),F(-1)))
        check('complex_P_Hermitian_'+str(w), trans(zconj(p))==p)
        check('complex_P_positive_minors_'+str(w), 2*w>0 and w*w>0)
        check('complex_kinetic_transpose_'+str(w), zmul(trans(az),tz)==zscale(p,(F(0),F(1))))
        check('complex_bar_square_'+str(w), zmul(az,zconj(az))==zreal(add((-1,i2))))
        check('complex_compatibility_'+str(w), zmul(zmul(zconj(p),tiz),p)==zscale(tz,(F(-1),F(0))))
        complex_controls.append({'Wbar':str(w),'P_over_Wbar':[['2','i'],['-i','1']], 'leading_minor':str(2*w),'determinant':str(w*w),'bar_square':'-I'})
    return {
        'result_id': 'K2056', 'status': 'active_research',
        'classification': 'INTERNAL_STRUCTURAL_ONLY', 'target_claim': 'NONE-NOT-A-KILL',
        'assumptions': ['T real invertible skew', 'P Hermitian positive definite, not necessarily real', 'same-coordinate antilinear b=A conjugation', 'A^T T=i P'],
        'identities': {'A': '-i T^-1 conjugate(P)', 'bar_square': 'T^-1 conjugate(P) T^-1 P', 'minus_one_criterion': 'conjugate(P) T^-1 P=-T', 'negative_similarity': 'P^(1/2) (A conjugate(A)) P^(-1/2)=-M M^dagger; M=P^(1/2) T^-1 conjugate(P^(1/2))', 'positive_control': 'Pstar=sqrt(-T^2)', 'actual_positive_control': '|Ccopy| tensor Wbar', 'actual_Astar': '-i sign(Ccopy) tensor B gamma0', 'two_plane_square': '-det(P)/w^2 I for T=wJ'},
        'copy_data': {'transverse_eigenvalue': -1, 'transverse_multiplicity': 9, 'other_polynomial': [1, -19, -70], 'discriminant': 641, 'absolute_numerator': [19, 140]},
        'half_controls': half_controls, 'complex_controls':complex_controls, 'checks': checks,
        'scope': 'Specified graph kinetic identification only; distinct inverse dual maps and indefinite P remain allowed. No source bar, physical quotient, statistics, quantum positivity, global domain or GU verdict.',
        'universal_proof': 'Written complex-skew Hermitian similarity argument, not finite fixtures.',
        'inputs': PINS,
    }


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', type=Path, default=ROOT)
    ap.add_argument('--output', type=Path)
    ap.add_argument('--write', action='store_true')
    args = ap.parse_args()
    out = args.output or args.root / REPORT
    result = produce(args.root)
    if args.write:
        out.write_text(json.dumps(result, indent=2) + '\n')
    else:
        assert result == json.loads(out.read_text())
    print('PASS K2056:', len(result['checks']), 'exact small-factor controls; three separate provenance pins')
