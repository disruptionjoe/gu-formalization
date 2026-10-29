"""K2240 finite exact controls; universal claims have written proofs.
No large consumer matrix, numerical optimizer, or sine approximation is used.
"""
from fractions import Fraction as F


def mat(rows): return [[F(x) for x in row] for row in rows]
def eye(n): return mat([[int(i == j) for j in range(n)] for i in range(n)])
def adj(a): return [list(row) for row in zip(*a)]  # fixtures are real

def mul(a, b):
    out = [[F(0) for _ in b[0]] for _ in a]
    for i, row in enumerate(a):
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(b[k]):
                    if y: out[i][j] += x*y
    return out

def scale(c, a): return [[c*x for x in row] for row in a]
def add(a, b): return [[x+y for x, y in zip(r, s)] for r, s in zip(a, b)]
def sub(a, b): return add(a, scale(-1, b))
def unit(j, k): return mat([[int(i == j and l == k) for l in range(2)] for i in range(2)])


def lift(U, N, fault=None):
    d = N+1
    V = [[F(0) for _ in range(2*d)] for _ in range(2*d)]
    if fault in ('unshifted_gate', 'cyclic_wrap'):
        for j in range(2):
            for n in range(d):
                for i in range(2):
                    m = n if fault == 'unshifted_gate' else (n+j-i) % d
                    V[i*d+m][j*d+n] = U[i][j]
        return V
    V[0][0] = V[-1][-1] = F(1)
    for k in range(1, N+1):
        shell = (k, d+k-1)
        for i in range(2):
            for j in range(2): V[shell[i]][shell[j]] = U[i][j]
    return V


def packet_isometry(V, support):
    d = len(V)//2
    return [[sum(V[row][j*d+n] for n in support) for j in range(2)]
            for row in range(2*d)]


def reduced(V, support, X, dephase=False):
    d = len(V)//2
    out = mat([[0, 0], [0, 0]])
    groups = [[n] for n in support] if dephase else [support]
    for group in groups:
        J = packet_isometry(V, group)
        for m in range(d):
            K = [J[m], J[d+m]]
            out = add(out, mul(mul(K, X), adj(K)))
    return scale(F(1, len(support)), out)


def gram_channel(U, L, X):
    out = mat([[0, 0], [0, 0]])
    for i in range(2):
        for k in range(2):
            for j in range(2):
                for l in range(2):
                    overlap = max(F(0), 1-F(abs((j-i)-(l-k)), L))
                    out[i][k] += U[i][j]*X[j][l]*U[k][l]*overlap
    return out


def shared_x_overlap(L, b, N, fresh=False):
    """Contract actual finite battery supports for |00><11| after two X gates."""
    support = list(range(b, b+L))
    # X moves B down for system input0 and up for input1.
    def translate(values, shift):
        result = [n+shift for n in values]
        assert min(result) >= 0 and max(result) <= N
        return result
    if fresh:
        a, c = translate(support, -1), translate(support, 1)
        return F(len(set(a) & set(c)), L)**2
    a, c = translate(support, -2), translate(support, 2)
    return F(len(set(a) & set(c)), L)


def run(fault=None):
    count = 0
    def check(ok):
        nonlocal count
        assert ok
        count += 1

    U = mat([[F(3, 5), -F(4, 5)], [F(4, 5), F(3, 5)]])
    X = mat([[0, 1], [1, 0]])
    Z = mat([[1, 0], [0, -1]])
    for gate in (U, X, Z):
        check(mul(adj(gate), gate) == eye(2))
        for L in (2, 4, 6):
            b, N = (0 if fault == 'missing_buffer' else 1), L+1
            support = list(range(b, b+L))
            V = lift(gate, N, fault)
            d = N+1
            check(mul(adj(V), V) == eye(2*d))
            energies = [n+j*(2 if fault == 'unequal_gap' else 1)
                        for j in range(2) for n in range(d)]
            check(all((energies[i]-energies[j])*V[i][j] == 0
                      for i in range(2*d) for j in range(2*d)))
            check(V[0][0] == 1 and V[-1][-1] == 1)
            # Isometry difference is an exact scalar Gram matrix for every input.
            J = packet_isometry(V, support)
            J0 = [[gate[i][j]*int(n in support) for j in range(2)]
                  for i in range(2) for n in range(d)]
            D = sub(J, J0)
            check(mul(adj(D), D) == scale(2*gate[1][0]**2, eye(2)))
            # All matrix units check the complete qubit superoperator, not one state.
            for j in range(2):
                for k in range(2):
                    e = unit(j, k)
                    actual = reduced(V, support, e, fault == 'dephased_packet')
                    check(actual == gram_channel(gate, L, e))
            # Explicit four boundary Kraus blocks and interior U count.
            boundary = [mat([[0, 0], [gate[1][0], 0]]),
                        mat([[gate[0][0], 0], [gate[1][0], gate[1][1]]]),
                        mat([[gate[0][0], gate[0][1]], [0, gate[1][1]]]),
                        mat([[0, gate[0][1]], [0, 0]])]
            completeness = mat([[0, 0], [0, 0]])
            for K in boundary: completeness = add(completeness, mul(adj(K), K))
            check(completeness == scale(2, eye(2)))
            for j in range(2):
                for k in range(2):
                    e = unit(j, k)
                    pred = scale(L-2, mul(mul(gate, e), adj(gate)))
                    for K in boundary: pred = add(pred, mul(mul(K, e), adj(K)))
                    check(scale(F(1, L), pred) == reduced(V, support, e))
            # Exact coherent population / battery mean-energy account on input0.
            out = reduced(V, support, unit(0, 0))
            check(out[1][1] == gate[1][0]**2)
            initial = F(sum(support), L)
            final = sum(F(n, L)*J[i*d+n][0]**2 for i in range(2) for n in range(d))
            check(initial-final == out[1][1])
            check(initial == b+F(L-1, 2))
            variance = sum((F(n)-initial)**2 for n in support)/L
            check(variance == F(L*L-1, 12))
            # Dephased battery has identical energy populations but no output coherence.
            diagonal = reduced(V, support, unit(0, 0), True)
            check(diagonal[0][1] == diagonal[1][0] == 0)

    # Same-qubit gate lift is a representation even at the finite edges.
    N = 7
    VU, VZ = lift(U, N), lift(Z, N)
    actual_product = mul(VU, VZ) if fault == 'wrong_order' else mul(VZ, VU)
    check(actual_product == lift(mul(Z, U), N))
    check(mul(VU, VZ) != mul(VZ, VU))
    check(mul(lift(adj(U), N), VU) == eye(2*(N+1)))
    # Reuse countercontrol changes physical resource, not an acceptance predicate.
    L, b, N = 6, 2, 9
    shared = shared_x_overlap(L, b, N, fault == 'fresh_reuse')
    check(shared == 1-F(4, L))
    fresh = shared_x_overlap(L, b, N, True)
    check(fresh-shared == F(4, L*L))
    check(F(1, 2)*(fresh-shared) == F(2, L*L))
    # Shift overlaps are finite intersections; no cyclic/infinite-ladder convention.
    for L in range(2, 9):
        for j in range(-2, 3):
            for k in range(-2, 3):
                a, c = set(range(3+j, 3+j+L)), set(range(3+k, 3+k+L))
                check(F(len(a & c), L) == max(F(0), 1-F(abs(j-k), L)))
    # L=3 sine eigenvector (1,sqrt2,1): exact Q(sqrt2) arithmetic.
    def qadd(a, b): return (a[0]+b[0], a[1]+b[1])
    def qmul(a, b): return (a[0]*b[0]+2*a[1]*b[1], a[0]*b[1]+a[1]*b[0])
    zero, one, rt2 = (F(0), F(0)), (F(1), F(0)), (F(0), F(1))
    w = [one, rt2, one]
    check(qadd(qadd(qmul(w[0], w[0]), qmul(w[1], w[1])), qmul(w[2], w[2])) == (F(4), F(0)))
    for j in range(3):
        left = qadd(w[j-1] if j else zero, w[j+1] if j < 2 else zero)
        check(left == qmul(rt2, w[j]))
    check(qadd(qmul(w[0], w[1]), qmul(w[1], w[2])) == (F(0), F(2)))
    # Exact rational path Rayleigh factorization for L=2, w=(1,1), cos(theta)=1/2.
    for a, c in ((F(2), F(3)), (F(-1), F(4)), (F(1, 3), F(-2, 5))):
        check((a-c)**2 == a*a+c*c-2*a*c)
    # Consumer uses analytic pi<22/7 and sin(x)<=x, not approximate trig values.
    check(F(44, 7*630) == F(22, 2205))
    check(F(22, 2205) < F(1, 100))
    check(F(22, 2205)+F(4, 10**12) < F(1, 100))
    check(F(4, 10**12)+F(1, 100) == F(2500000001, 250000000000))
    check(629+2*2 == 633)
    check(2+F(629-1, 2) == 316)
    check(F((629-1)**2, 4) == 98596)
    check(2*2**2/F(80000) == F(1, 10000))  # squared flat joint error
    return count


if __name__ == '__main__':
    import argparse, hashlib, json
    from pathlib import Path
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    count = run()
    faults = ('unshifted_gate', 'cyclic_wrap', 'unequal_gap', 'dephased_packet',
              'missing_buffer', 'wrong_order', 'fresh_reuse')
    detected = []
    for fault in faults:
        try: run(fault)
        except AssertionError: detected.append(fault)
        else: raise AssertionError('undetected '+fault)
    deps = ['explorations/conditional-build/k2240-finite-battery-gate-2026-10-29.md',
            'explorations/conditional-build/k2238-finite-clock-thermal-circuit-2026-10-29.md',
            'explorations/conditional-build/k2235-microscopic-thermal-renewal-2026-10-29.md',
            'explorations/conditional-build/k2229-finite-step-thermal-reset-work-2026-10-28.md']
    report = dict(result_id='K2240', exact_controls=count, detected_faults=detected,
                  dependency_sha256={p: hashlib.sha256((root/p).read_bytes()).hexdigest() for p in deps},
                  probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  evidence_kinds='Finite rational shell/energy/isometry/channel/reuse controls, algebraic sine fixture and resource arithmetic; arbitrary-reference, all-L sine optimality and exact-unitary impossibility are separate written proofs.')
    dest = root/'lab/process/k2240-finite-battery-gate.json'
    if args.write: dest.write_text(json.dumps(report, indent=2)+'\n')
    else: assert json.loads(dest.read_text()) == report, 'certificate drift'
    print(json.dumps(dict(result='K2240', controls=count, faults=len(detected))))
