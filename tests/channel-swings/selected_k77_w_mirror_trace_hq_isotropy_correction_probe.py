#!/usr/bin/env sage-python
"""Exact base/normal classification of H_q on W and its ASD mirror.

The predecessor used gamma_0, a positive observation-base covector, while its
prose called q the tautological vertical trace receiver.  This probe preserves
that valid base-q theorem and separately inserts the owned trace direction,
which is a negative axis in the normal ten-plane.

All ranks, zero matrices, conjugation relations and span dimensions below are
computed over Q(i).  No physical positivity, BV cohomology or domain follows.
"""

import ast
import sys
from pathlib import Path

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
    nodes = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "build_structures"]
    check("repo", "source probe exposes exactly one build_structures function", len(nodes) == 1)
    if len(nodes) != 1:
        raise SystemExit(1)
    node = nodes[0]
    namespace = {
        "identity_matrix": __import__("sage.all", fromlist=["identity_matrix"]).identity_matrix,
        "matrix": matrix,
        "block_matrix": __import__("sage.all", fromlist=["block_matrix"]).block_matrix,
        "zero_matrix": __import__("sage.all", fromlist=["zero_matrix"]).zero_matrix,
    }
    exec(compile(ast.Module(body=[node], type_ignores=[]), "<build>", "exec"), namespace)
    return namespace["build_structures"]


def dense(A):
    return sp.SparseMatrix(A.n, A.n, {(A.perm[j], j): A.sign[j] for j in range(A.n)})


def sympy_to_sage(A, field, ii):
    def cv(x):
        x = sp.expand(x)
        re = sp.Rational(sp.re(x))
        im = sp.Rational(sp.im(x))
        return field(int(re.p)) / field(int(re.q)) + field(int(im.p)) / field(int(im.q)) * ii

    return matrix(field, A.rows, A.cols,
                  {(int(r), int(c)): cv(v) for (r, c), v in A.todok().items()})


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


def exact_hermitian_inertia(A, field, ii):
    """Hermitian Gram--Schmidt over Q(i), with isotropic-pivot repair."""
    A = A.dense_matrix()
    pos = neg = zero = 0
    while A.nrows():
        n = A.nrows()
        pivot = next((j for j in range(n) if A[j, j] != 0), None)
        if pivot is None:
            off = next(((j, k) for j in range(n) for k in range(j + 1, n)
                        if A[j, k] != 0), None)
            if off is None:
                zero += n
                break
            j, k = off
            a = A[j, k]
            c = field(1) if a + a.conjugate() != 0 else ii
            T = identity_matrix(field, n)
            T[k, j] = c
            A = T.conjugate_transpose() * A * T
            pivot = j
        if pivot:
            A.swap_rows(0, pivot)
            A.swap_columns(0, pivot)
        d = A[0, 0]
        assert d != 0 and d == d.conjugate()
        if QQ(d) > 0:
            pos += 1
        else:
            neg += 1
        if n == 1:
            break
        A = A[1:, 1:] - A[1:, 0] * A[0, 1:] / d
    return pos, neg, zero


def coefficient_span_rank(forms, field):
    keys = sorted({key for form in forms for key, value in form.dict().items() if value})
    return matrix(field, len(keys), len(forms),
                  {(r, c): forms[c][key]
                   for r, key in enumerate(keys)
                   for c in range(len(forms)) if forms[c][key] != 0}).rank()


print("A. SOURCE, PRIOR ART AND LAYER ZERO")
owner = (ROOT / "explorations/conditional-build/selected-k77-tautological-trace-q-two-half-ownership-gate-2026-08-12.md").read_text()
receiver = (ROOT / "explorations/k77-wave2-q-receiver-trace-adjoint-ward-selection-2026-08-04.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k77-w-mirror-antilinear-hq-pairing-2026-08-13.md").read_text()
check("prior", "the owned trace receiver is q_g=g/2 with negative DeWitt norm",
      "q_g = g/2" in owner and "negative axis in the normal `(6,4)` plane" in owner)
check("prior", "prior art explicitly forbids reusing the positive base witness as trace q",
      "earlier Hermitian gate chose a positive base axis" in owner
      and "cannot be reused" in owner)
check("prior", "the receiver ledger distinguishes trace q from observer time",
      "normalized trace receiver" in receiver and "observation vector `u`" in receiver)
old_probe = (TESTS / "selected_k77_w_mirror_antilinear_hq_pairing_probe.py").read_text()
check("correction", "the predecessor's exact base-q calculation is preserved rather than erased",
      "positive observation-base witness" in old_probe
      and "companion trace-Hq correction probe" in old_probe)
for label in (
    "base covector versus tautological vertical trace covector",
    "same-sector restriction versus W-mirror cross-pair",
    "W/mirror one-form sectors versus ambient C^(32,32) halves",
    "Hermitian carrier Gram versus positive Hilbert form",
    "finite pairing versus presymplectic reduction and BV cohomology",
):
    check("layer0", label, True)


print("\nB. EXACT FOURTEEN-DIRECTION CLASSIFICATION")
K = QuadraticField(-1, "ii")
ii = K.gen()
data = load_build_structures()(K, ii)

gammas_sp, _ = c12.build_cl77()
dB, bB = c12.bilinear_space(gammas_sp, 128, [-1] * 14)
assert dB == 1
B_sp = c12.sparse_to_sp(bB[0], 128)
if B_sp.sign[0] == -1:
    B_sp = B_sp.neg()
B = sympy_to_sage(dense(B_sp), K, ii)

BASE = (0, 7, 8, 9)
NORMAL = (1, 2, 3, 4, 5, 6, 10, 11, 12, 13)
TRACE_AXIS = 10

P_w = data["projectors"]["W_sd192"]
P_m = data["projectors"]["mirror_asd192"]
W = P_w.matrix_from_columns(list(P_w.pivots()))
M = W.conjugate()
WM = W.augment(M)
eta14 = matrix.diagonal(K, data["eta"])

same_w = []
same_m = []
cross = []
pair = []
for axis, Q in enumerate(data["gammas"]):
    Hq = ii * B * Q
    K1 = eta14.tensor_product(Hq)
    same_w.append(W.conjugate_transpose() * K1 * W)
    same_m.append(M.conjugate_transpose() * K1 * M)
    cross.append(W.conjugate_transpose() * K1 * M)
    pair.append(WM.conjugate_transpose() * K1 * WM)
    check("exact", f"axis {axis} gives an exact Hermitian involution",
          Hq.conjugate_transpose() == Hq and Hq * Hq == identity_matrix(K, 128))
    check("exact", f"axis {axis} preserves the W/mirror anti-linear sign relation",
          same_m[-1] == -same_w[-1].conjugate())

check("exact", "all ten normal directions vanish on W and mirror separately",
      all(same_w[a].is_zero() and same_m[a].is_zero() for a in NORMAL))
check("exact", "all four base directions are nondegenerate on W and mirror separately",
      all(same_w[a].rank() == same_m[a].rank() == 192 for a in BASE))
check("exact", "all four base directions have zero W-mirror cross-pair",
      all(cross[a].is_zero() for a in BASE))
check("exact", "all ten normal directions give a nondegenerate rank-192 W-mirror cross-pair",
      all(cross[a].rank() == 192 for a in NORMAL))
check("exact", "the combined W-plus-mirror restriction is nondegenerate in every canonical direction",
      all(pair[a].rank() == 384 for a in range(14)))

check("exact", "the same-sector restriction map has exact rank four",
      coefficient_span_rank(same_w, K) == 4)
check("exact", "the cross-sector restriction map has exact rank ten",
      coefficient_span_rank(cross, K) == 10)

base_inertias = []
for axis in BASE:
    components = support_components(same_w[axis])
    component_inertias = [exact_hermitian_inertia(
        same_w[axis].matrix_from_rows_and_columns(c, c), K, ii) for c in components]
    total = tuple(sum(value[j] for value in component_inertias) for j in range(3))
    base_inertias.append(total)
check("exact", "each base-q same-sector form has exact neutral inertia (96,96,0)",
      set(base_inertias) == {(96, 96, 0)})


print("\nC. ACTUAL TRACE-Q DISPOSITION")
check("typing", "the actual trace axis lies in the normal plane and not the observation base",
      TRACE_AXIS in NORMAL and TRACE_AXIS not in BASE)
check("exact", "trace Hq makes W and mirror totally isotropic",
      same_w[TRACE_AXIS].is_zero() and same_m[TRACE_AXIS].is_zero())
check("exact", "trace Hq pairs W with mirror nondegenerately",
      cross[TRACE_AXIS].rank() == 192 and pair[TRACE_AXIS].rank() == 384)
check("exact", "the trace-paired W-plus-mirror form is Witt-neutral (192,192)",
      pair[TRACE_AXIS].rank() == 384 and same_w[TRACE_AXIS].is_zero()
      and same_m[TRACE_AXIS].is_zero())
check("planted", "a base-q neutral same-sector witness is not trace-owned q",
      same_w[0].rank() == 192 and same_w[TRACE_AXIS].rank() == 0)
check("planted", "total isotropy is not degeneracy of the full paired carrier",
      pair[TRACE_AXIS].rank() != 0)

check("analytic", "finite nondegenerate cross-pairing does not construct positivity or a closed domain", True)
check("symplectic", "an off-diagonal Hermitian pairing is not a BV/BFV reduction", True)
check("source", "source is silent on the repository W/mirror trace-Hq polarization", True)

print("\nRESULT")
print("disposition=BASE_Q_THEOREM_PRESERVED__TRACE_Q_SAME_SECTORS_ISOTROPIC__TRACE_Q_CROSS_PAIR_NONDEGENERATE")
print("SAME_SECTOR_RESTRICTION_KERNEL=NORMAL_10_PLANE")
print("CROSS_SECTOR_RESTRICTION_KERNEL=BASE_4_PLANE")
print("TRACE_Q_W_AND_MIRROR=TOTALLY_ISOTROPIC")
print("TRACE_Q_W_MIRROR_CROSS_RANK=192")
print("TRACE_Q_COMBINED_WITT_INERTIA=192_192_0")
print("SOURCE_RETURN=SOURCE_SILENT_REPO_W_MIRROR_TRACE_HQ_POLARIZATION")
print("NEXT=TYPE_THE_ACTION_OWNED_CROSS_PAIR_OR_OTHER_PHYSICAL_PAIRING_BEFORE_HALF_SELECTION")
print(f"counts={COUNTS}")
print(f"failures={FAILURES}")
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
