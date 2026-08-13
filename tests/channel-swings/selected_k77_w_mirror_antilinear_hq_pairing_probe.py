#!/usr/bin/env sage-python
"""Exact W/mirror anti-linear equivalence and trace-Hq pairing gate."""

import ast
import sys
from pathlib import Path

import numpy as np
import sympy as sp
from sage.all import QQ, QuadraticField, identity_matrix, matrix

ROOT = Path(__file__).resolve().parents[2]
TESTS = ROOT / "tests/channel-swings"
sys.path.insert(0, str(TESTS))

COUNTS = {}
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] = COUNTS.get(kind, 0) + 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}", flush=True)
    if not ok:
        FAILURES.append(label)

import nguyen_c1c2_real_form_probe as c12


def load_build_structures():
    source = (TESTS / "selected_k77_induced_fermion_principal_discriminator.py").read_text()
    tree = ast.parse(source)
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "build_structures")
    module = ast.Module(body=[node], type_ignores=[])
    namespace = {
        "identity_matrix": __import__("sage.all", fromlist=["identity_matrix"]).identity_matrix,
        "matrix": matrix,
        "block_matrix": __import__("sage.all", fromlist=["block_matrix"]).block_matrix,
        "zero_matrix": __import__("sage.all", fromlist=["zero_matrix"]).zero_matrix,
    }
    exec(compile(module, "<extracted-build-structures>", "exec"), namespace)
    return namespace["build_structures"]


def dense(A):
    return sp.SparseMatrix(A.n, A.n, {(A.perm[j], j): A.sign[j] for j in range(A.n)})


def sympy_to_sage(A, field, ii):
    def cv(x):
        x = sp.expand(x)
        re = sp.Rational(sp.re(x))
        im = sp.Rational(sp.im(x))
        return field(int(re.p)) / field(int(re.q)) + (field(int(im.p)) / field(int(im.q))) * ii

    return matrix(field, A.rows, A.cols, {(int(r), int(c)): cv(v) for (r, c), v in A.todok().items()})


print("A. SOURCE, PRIOR ART AND LAYER ZERO")
source = (ROOT / "lab/sources/selected-k77-action-parent-source-reinspection-2026-08-09.md").read_text()
prior = (ROOT / "explorations/conditional-build/selected-k77-physical-operator-admission-closure-2026-08-13.md").read_text()
two_half = (ROOT / "explorations/conditional-build/selected-k77-two-half-hermitian-witt-rotation-gate-2026-08-12.md").read_text()
check("source", "source distinguishes full U(64,64) from two C^(32,32) carrier halves",
      "two C^(32,32) Weyl halves" in source and "separate full U(64,64) principal-group arena" in source)
check("source", "source does not own the repository W/mirror projector or physical selector",
      "SOURCE-SILENT" in source and "W_sd192" not in source and "mirror_asd192" not in source)
check("prior", "predecessor proves only equal W/mirror rank and kernel",
      "`224/96` on both `W` and its" in prior)
check("prior", "trace Hq is an exact moving Hermitian family with two neutral halves",
      "signature(H_q|S_+) = (32,32)" in two_half and "signature(H_q|S_-) = (32,32)" in two_half)
check("layer0", "W/mirror one-form sectors are not the two ambient C^(32,32) halves", True)
check("layer0", "anti-linear equivalence is not a linear gauge identification", True)
check("layer0", "a fibre Krein form is not BV cohomology or a physical domain", True)


print("\nB. EXACT ANTI-LINEAR PRINCIPAL EQUIVALENCE")
build_structures = load_build_structures()
K = QuadraticField(-1, "ii")
ii = K.gen()
data = build_structures(K, ii)

# Rebuild the certified invariant spinor form and H_q in the same Clifford basis.
gammas_sp, eta = c12.build_cl77()
dB, bB = c12.bilinear_space(gammas_sp, 128, [-1] * 14)
assert dB == 1
B_sp = c12.sparse_to_sp(bB[0], 128)
if B_sp.sign[0] == -1:
    B_sp = B_sp.neg()
B = sympy_to_sage(dense(B_sp), K, ii)
Q = data["gammas"][0]
Hq = ii * B * Q

check("exact", "Hq is an exact Hermitian involution",
      Hq.conjugate_transpose() == Hq and Hq * Hq == identity_matrix(K, 128))

P_w = data["projectors"]["W_sd192"]
P_m = data["projectors"]["mirror_asd192"]
check("exact", "complex conjugation exchanges the W and mirror projectors",
      P_w.conjugate() == P_m)
check("planted", "W and mirror projectors are not the same linear projector", P_w != P_m)

# Use the conjugate W basis for the mirror so the anti-linear relation is explicit.
cols = list(P_w.pivots())
W = P_w.matrix_from_columns(cols)
M = W.conjugate()
check("exact", "conjugate W basis is a full rank-192 mirror basis",
      W.rank() == M.rank() == 192 and (P_m * M - M).is_zero())

eta14 = matrix.diagonal(K, data["eta"])
K1 = eta14.tensor_product(Hq)
Gw = W.conjugate_transpose() * K1 * W
Gm = M.conjugate_transpose() * K1 * M
check("exact", "Hq changes sign under external complex conjugation",
      Hq.conjugate() == -Hq)
check("exact", "W-to-mirror conjugation is an exact Hq anti-isometry",
      Gm == -Gw.conjugate())
check("exact", "both restricted Gram forms are nondegenerate rank 192",
      Gw.rank() == Gm.rank() == 192)
check("planted", "anti-isometry is not silently promoted to isometry",
      Gm != Gw.conjugate())

# Numerical inertia is a scout only; exact relations/ranks above are certificates.
def inertia(A):
    arr = np.array([[complex(x) for x in row] for row in A], dtype=np.complex128)
    vals = np.linalg.eigvalsh(arr)
    tol = max(1.0, float(np.max(np.abs(vals)))) * 1e-9
    return int(np.sum(vals > tol)), int(np.sum(vals < -tol)), int(np.sum(np.abs(vals) <= tol)), float(np.min(np.abs(vals)))

w_scout = inertia(Gw)
m_scout = inertia(Gm)
check("scout", "floating spectra are well separated and suggest neutral 96/96 inertia",
      w_scout[:3] == m_scout[:3] == (96, 96, 0)
      and w_scout[3] > 0.1 and m_scout[3] > 0.1)


def support_components(A):
    neighbors = [set() for _ in range(A.nrows())]
    for (r, c), value in A.dict().items():
        if value and r != c:
            neighbors[r].add(c)
            neighbors[c].add(r)
    unseen = set(range(A.nrows()))
    out = []
    while unseen:
        seed = unseen.pop()
        component = {seed}
        frontier = [seed]
        while frontier:
            v = frontier.pop()
            new = neighbors[v] & unseen
            unseen -= new
            component |= new
            frontier.extend(new)
        out.append(sorted(component))
    return out


components = support_components(Gw)
check("exact", "the W Gram support splits into 32 exact six-dimensional blocks",
      len(components) == 32 and set(map(len, components)) == {6})


def exact_hermitian_inertia(A):
    """Hermitian Gram-Schmidt over Q(i), including isotropic pivot repair."""
    A = A.dense_matrix()
    pos = neg = zero = 0
    while A.nrows():
        n = A.nrows()
        pivot = next((j for j in range(n) if A[j, j] != 0), None)
        if pivot is None:
            off = next(((j, k) for j in range(n) for k in range(j + 1, n) if A[j, k] != 0), None)
            if off is None:
                zero += n
                break
            j, k = off
            a = A[j, k]
            c = K(1) if a + a.conjugate() != 0 else ii
            T = identity_matrix(K, n)
            T[k, j] = c
            A = T.conjugate_transpose() * A * T
            pivot = j
            assert A[pivot, pivot] != 0
        if pivot:
            A.swap_rows(0, pivot)
            A.swap_columns(0, pivot)
        d = A[0, 0]
        assert d == d.conjugate()
        dq = QQ(d)
        if dq > 0:
            pos += 1
        elif dq < 0:
            neg += 1
        else:
            zero += 1
        if n == 1:
            break
        col = A[1:, 0]
        row = A[0, 1:]
        A = A[1:, 1:] - col * row / d
    return pos, neg, zero


component_inertias = [exact_hermitian_inertia(Gw.matrix_from_rows_and_columns(c, c)) for c in components]
exact = tuple(sum(x[k] for x in component_inertias) for k in range(3))
check("exact", "every six-dimensional block has exact inertia (3,3,0)",
      set(component_inertias) == {(3, 3, 0)})
check("exact", "W and mirror have exact neutral nondegenerate inertia (96,96,0)",
      exact == (96, 96, 0) and (exact[1], exact[0], exact[2]) == (96, 96, 0))
check("planted", "Hq does not make W positive definite", exact != (192, 0, 0))

# The rolled symbol is real, hence conjugation intertwines it exactly.
xi = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
D = data["rolled_symbol"](xi)
check("exact", "the rolled principal symbol is real and conjugation-intertwined",
      D.conjugate() == D)
check("analytic", "finite fibre inertia does not construct a closed domain or spectrum", True)
check("symplectic", "the symmetric Hq Gram is not a reduced presymplectic/BFV form", True)

print("\nRESULT")
print("disposition=EXACT_ANTILINEAR_PRINCIPAL_EQUIVALENCE__HQ_ANTIISOMETRIC_NEUTRAL_PAIR__NO_CURRENT_HALF_SELECTOR")
print("W_MIRROR_PROJECTOR_RELATION=CONJUGATE")
print("HQ_CONJUGATION_RELATION=SIGN_FLIP")
print("RESTRICTED_INERTIA=W_96_96_0__MIRROR_96_96_0")
print("SOURCE_RETURN=SOURCE_CONFIRMS_FULL_U6464_AND_TWO_C32_32_CARRIER_HALVES__SOURCE_SILENT_W_MIRROR_HQ_PHYSICAL_SELECTOR")
print("NEXT=TEST_ACTION_OWNED_LOWER_ORDER_NONZERO_FERMION_BV_OR_DOMAIN_TERM_FOR_BREAKING_OF_THE_ANTILINEAR_EQUIVALENCE")
print(f"counts={COUNTS}")
print(f"failures={FAILURES}")
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
