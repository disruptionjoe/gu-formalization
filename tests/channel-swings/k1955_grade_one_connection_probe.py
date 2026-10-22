"""Independent signed-bit raw assembly for the grade-one leakage certificate."""
import hashlib
import json
from copy import deepcopy, copy
from pathlib import Path
from sage.all import QQ, matrix, identity_matrix, zero_matrix, block_matrix, diagonal_matrix, prod
from k1951_coordinated_zero_southeast_principal_probe import gamma, mat

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'lab/process/k1955-grade-one-connection.json'


def assemble(value):
    g = gamma(); eye = identity_matrix(QQ, 128, sparse=True)
    z = zero_matrix(QQ, 128, 128, sparse=True)
    vol = prod(g); W = (3 * eye - vol) / 2; Wi = (3 * eye + vol) / 4
    eta = [1] * 7 + [-1] * 7
    def D(k):
        return block_matrix([[eta[r] * g[r] * g[k] * g[c] * W if r != k and c not in (r, k) else z
                              for c in range(14)] + [eye if r == k else z] for r in range(14)] +
                            [[-eta[c] * eye if c == k else z for c in range(14)] + [z]], sparse=True)
    parts = [[z] * 15 for _ in range(15)]
    parts[0][14] = -eye; parts[14][0] = eye
    for r in range(1, 14):
        for c in range(1, 14):
            parts[r][c] = Wi * eta[r] * g[r] * g[0] * g[c] * (QQ(1) / 12 - (1 if r == c else 0))
    inv = block_matrix(parts, sparse=True); d0 = D(0)
    assert d0 * inv == identity_matrix(QQ, 1920), 'independent time inverse'
    rows = json.loads((ROOT / 'lab/process/k1951-coordinated-zero-southeast-principal.json').read_text())['blocks']
    J = matrix(QQ, 1920, 128, sparse=True)
    for b, row in enumerate(rows):
        js = mat(row['basis']) * mat(row['section'])
        for (i, j), v in js.dict().items():
            J[row['coordinates'][i], 4 * b + j] = v
    piv = J.transpose().pivots(); L = matrix(QQ, 128, 1920, sparse=True)
    small_inv = J.matrix_from_rows(piv).inverse()
    for j, p in enumerate(piv):
        L.set_column(p, small_inv.column(j))
    assert L * J == identity_matrix(QQ, 128), 'actual core coordinates'
    ds = {k: D(k) for k in [0, 7, 8, 9]}
    As = {k: inv * d for k, d in ds.items()}
    for n, k in enumerate([7, 8, 9]):
        C = block_matrix([[mat(rows[i]['quotient_generators'][n]) if i == j else zero_matrix(QQ, 4, 4)
                           for j in range(32)] for i in range(32)], sparse=True)
        assert ds[k] * J == d0 * J * C, 'independent actual principal restriction'
    for row in rows:
        h = mat(row['quotient_energy']); cs = list(map(mat, row['quotient_generators']))
        assert h.is_positive_definite() and all(h * c == c.transpose() * h for c in cs), 'stored positive principal energy'
    T = diagonal_matrix(QQ, [1] * 14 + [-1], sparse=True).tensor_product(vol)
    tj = mat(value['induced_total_chirality'])
    assert T * J == J * tj and tj * tj == identity_matrix(QQ, 128), 'actual core chirality'
    assert all(T * d == -d * T for d in ds.values()), 'raw odd principal coefficients'
    assert all(T * a == a * T for a in As.values()), 'even evolution coefficients'
    def column(k, a, fault=None):
        generator = g[(a + 1) % 14] if fault == 'wrong_grade_one_generator' else g[a]
        if fault == 'missing_connection':
            generator = 0 * generator
        slots = diagonal_matrix(QQ, [1] * 14 + [0], sparse=True) if fault == 'missing_auxiliary_connection' else identity_matrix(QQ, 15, sparse=True)
        action = slots.tensor_product(generator) * J
        if fault == 'wrong_covector':
            k = 7 if k == 0 else 0
        V = As[k] * action; residual = V - J * (L * V)
        return [residual[i // 128, i % 128] for i in value['selected_rows']]
    cols = [column(k, a) for k, a in value['labels']]
    Jc = matrix(QQ, 1920, 640, sparse=True); Lc = matrix(QQ, 640, 1920, sparse=True)
    for b, row in enumerate(rows):
        basis = mat(row['basis']); ix = basis.transpose().pivots()
        small = basis.matrix_from_rows(ix).inverse()
        for (i, j), v in basis.dict().items():
            Jc[row['coordinates'][i], 20 * b + j] = v
        for j, i in enumerate(ix):
            for k in range(20):
                if small[k, j]:
                    Lc[20 * b + k, row['coordinates'][i]] = small[k, j]
    assert Lc * Jc == identity_matrix(QQ, 640), 'independent cyclic coordinates'
    def cyclic_column(k, a, fault=False):
        slots = identity_matrix(QQ, 15, sparse=True)
        if fault:
            k = 7 if k == 0 else 0
        V = As[k] * slots.tensor_product(g[a]) * Jc
        residual = V - Jc * (Lc * V)
        return [residual[i // 640, i % 640] for i in value['cyclic_parent']['selected_rows']]
    Bc = matrix(QQ, [cyclic_column(k, a) for k, a in value['labels']]).transpose()
    return matrix(QQ, cols).transpose(), column, Bc, cyclic_column


def audit(value, B):
    assert value['result_id'] == 'K1955', 'report identity'
    for p, h in value['inputs'].items():
        assert hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h, 'input pin'
    assert value['labels'] == [[k, a] for k in [0, 7, 8, 9] for a in range(14)], 'complete grade-one basis'
    inv = mat(value['inverse'])
    assert inv * B == identity_matrix(QQ, 56), 'independent full leakage rank certificate'
    assert value['rank'] == 56, 'rank reporting'
    assert QQ(value['inverse_infinity_norm']) == max(sum(abs(z) for z in row) for row in inv.rows()), 'exact residual bound'
    seed = matrix(QQ, 56, 1, {(value['labels'].index([k, k]), 0): (1 if k == 0 else -1) for k in [0, 7, 8, 9]})
    assert B * seed == mat(value['trace_seed_selected_residual']) != 0, 'actual trace seed residual'
    i, z = value['trace_seed_witness']
    assert (B * seed)[i, 0] == QQ(z) != 0, 'nonzero trace seed witness'
    return 8


def audit_auxiliary(value, fault=None):
    rows = json.loads((ROOT / 'lab/process/k1951-coordinated-zero-southeast-principal.json').read_text())['blocks']
    certificates = value['auxiliary_support']['blocks']; assert len(certificates) == len(rows) == 32
    for n, (row, cert) in enumerate(zip(rows, certificates)):
        J = mat(row['basis']); R = mat(row['radical']); S = mat(row['section'])
        F = J.matrix_from_rows([i for i, c in enumerate(row['coordinates']) if c >= 1792])
        if fault == 'auxiliary_projection' and n == 0:
            F = copy(F); F[0, 0] += 1
        E = J.solve_right(mat(row['seed'])); B = list(map(mat, row['generators']))
        U = block_matrix([[E] + [b * E for b in B]])
        if fault == 'observed_principal_image' and n == 0:
            U = copy(U); U[0, 4] += 1
        assert F * R * mat(cert['radical_auxiliary_right_inverse']) == identity_matrix(QQ, 4), 'independent radical auxiliary surjectivity'
        assert F * S * mat(cert['core_auxiliary_inverse']) == identity_matrix(QQ, 4), 'independent core auxiliary bijection'
        assert mat(cert['observed_range_core_inverse']) * block_matrix([[U, S]]) == identity_matrix(QQ, 20), 'independent auxiliary range core decomposition'
    return 96


if __name__ == '__main__':
    value = json.loads(OUT.read_text()); B, col, Bc, cyclic_col = assemble(value)
    print('PASS K1955 independent raw baseline', audit(value, B), flush=True)
    vc = value['cyclic_parent']; ic = mat(vc['inverse'])
    assert ic * Bc == identity_matrix(QQ, 56), 'independent cyclic leakage inverse'
    assert vc['rank'] == 56 and QQ(vc['inverse_infinity_norm']) == max(sum(abs(z) for z in r) for r in ic.rows()), 'cyclic rank and residual constant'
    print('PASS independent quotient-parent obstruction and bound', flush=True)
    print('PASS independent auxiliary-support identities', audit_auxiliary(value), flush=True)
    caught = []
    for fault in ['missing_connection', 'wrong_grade_one_generator', 'wrong_covector', 'missing_auxiliary_connection']:
        bad = copy(B); changed = False
        for j, (k, a) in enumerate(value['labels']):
            v = col(k, a, fault)
            if v != list(B.column(j)):
                bad.set_column(j, v); changed = True; break
        assert changed, 'fault must alter mathematical input'
        try:
            audit(value, bad)
        except AssertionError as e:
            assert str(e) == 'independent full leakage rank certificate', str(e)
            caught.append(fault)
        else:
            raise AssertionError('undetected mathematical fault')
    print('PASS mathematical faults', caught, flush=True)
    for j, (k, a) in enumerate(value['labels']):
        changed = cyclic_col(k, a, True)
        if changed != list(Bc.column(j)):
            bad = copy(Bc); bad.set_column(j, changed)
            assert ic * bad != identity_matrix(QQ, 56), 'cyclic fault must break the actual inverse certificate'
            break
    else:
        raise AssertionError('cyclic mathematical fault changed no input')
    print('PASS cyclic-parent mathematical fault: wrong observed covector', flush=True)
    for fault in ['identity', 'pin']:
        bad = deepcopy(value)
        if fault == 'identity':
            bad['result_id'] = 'WRONG'
        else:
            bad['inputs'][next(iter(bad['inputs']))] = '0' * 64
        try:
            audit(bad, B)
        except AssertionError as e:
            assert str(e) == ('report identity' if fault == 'identity' else 'input pin')
        else:
            raise AssertionError('undetected reporting fault')
    print('PASS two separate reporting faults')
    for fault in ['auxiliary_projection', 'observed_principal_image']:
        try:
            audit_auxiliary(value, fault)
        except AssertionError as e:
            assert str(e) in ['independent radical auxiliary surjectivity', 'independent core auxiliary bijection', 'independent auxiliary range core decomposition'], str(e)
        else:
            raise AssertionError('undetected auxiliary-support mathematical fault')
    print('PASS auxiliary-support mathematical faults: projection and principal image')
