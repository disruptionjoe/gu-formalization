"""Grade-one connection realization on the actual fixed SE0 stable carrier."""
import argparse
import hashlib
import json
from pathlib import Path
from sage.all import QQ, matrix, identity_matrix, zero_matrix, block_matrix, diagonal_matrix, prod
from k1953_spin_connection_stable_mass import setup
from k1951_coordinated_zero_southeast_principal import left
from k1836_k77_differential_dirac_quotient import enc, mat

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'lab/process/k1955-grade-one-connection.json'
INPUT = 'lab/process/k1951-coordinated-zero-southeast-principal.json'


def assemble():
    g, As, J, L, Cs, H = setup()
    labels = [[k, a] for k in [0, 7, 8, 9] for a in range(14)]
    evol = dict(zip([0, 7, 8, 9], [identity_matrix(QQ, 1920, sparse=True)] + As))
    columns, outputs = [], []
    for k, a in labels:
        V = evol[k] * identity_matrix(QQ, 15, sparse=True).tensor_product(g[a]) * J
        M = L * V
        columns.append({i * 128 + j: z for (i, j), z in (V - J * M).dict().items()})
        outputs.append(M)
    keys = sorted(set().union(*(set(c) for c in columns)))
    indices = {v: i for i, v in enumerate(keys)}
    T = matrix(QQ, len(keys), 56, {(indices[i], j): z for j, c in enumerate(columns) for i, z in c.items()}, sparse=True)
    omega = prod(g)
    total = diagonal_matrix(QQ, [1] * 14 + [-1], sparse=True).tensor_product(omega)
    tj = L * total * J
    assert total * total == identity_matrix(QQ, 1920), 'raw chirality involution'
    assert all(total * a == a * total for a in As), 'fixed evolutions preserve total chirality'
    assert total * J == J * tj and tj * tj == identity_matrix(QQ, 128), 'positive core preserves chirality'
    assert all(tj * c == c * tj for c in Cs), 'induced principal chirality'
    # Algebraic parity is independent of the pivot projection L used for residuals.
    assert all(total * identity_matrix(QQ, 15, sparse=True).tensor_product(a) ==
               -identity_matrix(QQ, 15, sparse=True).tensor_product(a) * total for a in g), 'grade-one parity'
    return T, keys, labels, outputs, enc(tj), g, As


def cyclic_certificate(g, As, prior=None):
    rows = json.loads((ROOT / INPUT).read_text())['blocks']
    J = matrix(QQ, 1920, 640, sparse=True); L = matrix(QQ, 640, 1920, sparse=True)
    for b, row in enumerate(rows):
        j = mat(row['basis']); ll = left(j)
        for (i, k), v in j.dict().items():
            J[row['coordinates'][i], 20 * b + k] = v
        for (k, i), v in ll.dict().items():
            L[20 * b + k, row['coordinates'][i]] = v
    assert L * J == identity_matrix(QQ, 640), 'actual cyclic coordinates'
    cols = []
    for A in [identity_matrix(QQ, 1920, sparse=True)] + As:
        for a in g:
            V = A * identity_matrix(QQ, 15, sparse=True).tensor_product(a) * J
            cols.append({i * 640 + j: v for (i, j), v in (V - J * (L * V)).dict().items()})
    keys = sorted(set().union(*(set(c) for c in cols))); indices = {v: i for i, v in enumerate(keys)}
    T = matrix(QQ, len(keys), 56, {(indices[i], j): v for j, c in enumerate(cols) for i, v in c.items()}, sparse=True)
    if prior:
        piv = [keys.index(i) for i in prior['selected_rows']]; inv = mat(prior['inverse'])
    else:
        piv = list(T.transpose().pivots()); assert len(piv) == 56, 'cyclic preservation rank'
        inv = T.matrix_from_rows(piv).inverse()
    assert inv * T.matrix_from_rows(piv) == identity_matrix(QQ, 56), 'cyclic leakage inverse'
    return dict(rank=56, equation_count=len(keys), selected_rows=[keys[i] for i in piv], inverse=enc(inv),
                inverse_infinity_norm=str(max(sum(abs(v) for v in row) for row in inv.rows())))


def auxiliary_certificate():
    rows = json.loads((ROOT / INPUT).read_text())['blocks']; certificates = []
    for row in rows:
        J = mat(row['basis']); R = mat(row['radical']); S = mat(row['section'])
        B = list(map(mat, row['generators']))
        F = J.matrix_from_rows([i for i, c in enumerate(row['coordinates']) if c >= 1792])
        E = left(J) * mat(row['seed'])
        right = left((F * R).transpose()).transpose(); core_inv = (F * S).inverse()
        U = block_matrix([[E] + [b * E for b in B]])
        decomposition_inv = block_matrix([[U, S]]).inverse()
        assert F * R * right == identity_matrix(QQ, 4), 'radical surjects onto auxiliary input'
        assert F * S * core_inv == identity_matrix(QQ, 4), 'core auxiliary coordinate is invertible'
        assert decomposition_inv * block_matrix([[U, S]]) == identity_matrix(QQ, 20), 'observed auxiliary range complements stable core'
        certificates.append(dict(radical_auxiliary_right_inverse=enc(right), core_auxiliary_inverse=enc(core_inv),
                                 observed_range_core_inverse=enc(decomposition_inv)))
    return dict(blocks=certificates, global_radical_auxiliary_rank=128, global_core_auxiliary_rank=128,
                global_observed_auxiliary_range_dimension=512, global_stable_core_dimension=128,
                arbitrary_observed_endomorphism_parameter_count=4 * 128 * 128)


def produce():
    T, keys, labels, outputs, tj, g, As = assemble()
    old = json.loads(OUT.read_text()) if OUT.exists() else None
    if old:
        rows = [keys.index(i) for i in old['selected_rows']]
        inv = mat(old['inverse'])
    else:
        rows = list(T.transpose().pivots())
        assert len(rows) == 56, ('grade-one kernel requires further classification', len(rows))
        inv = T.matrix_from_rows(rows).inverse()
    B = T.matrix_from_rows(rows)
    assert inv * B == identity_matrix(QQ, 56), 'exact full leakage rank'
    norm = max(sum(abs(z) for z in r) for r in inv.rows())
    # A source-motivated observed trace seed is a strict subset of this class.
    seed = matrix(QQ, 56, 1, {(labels.index([k, k]), 0): (1 if k == 0 else -1) for k in [0, 7, 8, 9]})
    residual = B * seed
    assert residual != 0, 'observed grade-one trace seed fails invariance'
    witness = next((i, str(residual[i, 0])) for i in range(56) if residual[i, 0])
    return dict(result_id='K1955', status='active_research', classification='INTERNAL_STRUCTURAL_ONLY',
                target_claim='NONE-NOT-A-KILL', labels=labels, rank=56,
                selected_rows=[keys[i] for i in rows], inverse=enc(inv), inverse_infinity_norm=str(norm),
                cyclic_parent=cyclic_certificate(g, As, old.get('cyclic_parent') if old else None),
                auxiliary_support=auxiliary_certificate(),
                induced_total_chirality=tj, trace_seed_selected_residual=enc(residual), trace_seed_witness=list(witness),
                inputs={p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in [INPUT, 'lab/process/k1953-spin-connection-stable-mass.json']},
                scope='Conditional fixed observed SE0 system: all56 real grade-one common spinor connection coefficients fail stable128 invariance unless zero. No source-selected full20 placement, barred map, density, action or physical quotient.')


if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--write', action='store_true'); args = p.parse_args()
    value = produce()
    if args.write:
        OUT.write_text(json.dumps(value, indent=2) + '\n')
    else:
        assert value == json.loads(OUT.read_text()), 'report drift'
    print('PASS K1955 exact leakage rank', value['rank'], 'inverse bound', value['inverse_infinity_norm'], 'and total-chirality identities')
