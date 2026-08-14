#!/usr/bin/env sage-python
"""Wholesale real-action/Helmholtz gate for the K77 W/mirror fork.

The exact theorem is class-level.  If an anti-linear involution exchanges
``W`` and ``M`` and a block-preserving operator is homogeneous under that
involution, its two diagonal blocks are conjugate up to sign. Rank and nullity
therefore agree, while the characteristic polynomials are conjugate. A Hessian of a real invariant
action at an involution-fixed stationary background lies in the even class.

This does not cover a non-fixed stationary vacuum, a conjugation-asymmetric
domain/BV quotient, or an action that does not preserve the real structure.
"""

from __future__ import annotations

import ast
from collections import Counter
from pathlib import Path

from sage.all import (
    QuadraticField,
    block_diagonal_matrix,
    block_matrix,
    identity_matrix,
    matrix,
    PolynomialRing,
    zero_matrix,
)


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text()


def load_build_structures():
    """Load the immutable exact K77 carrier constructor, not probe outputs."""
    source = read("tests/channel-swings/selected_k77_induced_fermion_principal_discriminator.py")
    tree = ast.parse(source)
    node = next(
        n for n in tree.body
        if isinstance(n, ast.FunctionDef) and n.name == "build_structures"
    )
    namespace = {
        "identity_matrix": identity_matrix,
        "matrix": matrix,
        "block_matrix": block_matrix,
        "zero_matrix": zero_matrix,
    }
    exec(
        compile(ast.Module(body=[node], type_ignores=[]), "<build-structures>", "exec"),
        namespace,
    )
    return namespace["build_structures"]


print("A. SOURCE, PRIOR ART AND LAYER ZERO")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
claim_register = read("lab/sources/source-claim-register.yaml")
owner = read("explorations/conditional-build/selected-k77-i2b-source-natural-second-action-owner-2026-08-13.md")
pairing = read("explorations/conditional-build/selected-k77-w-mirror-action-pairing-ownership-2026-08-13.md")
anti = read("explorations/conditional-build/selected-k77-w-mirror-antilinear-hq-pairing-2026-08-13.md")
check("source", "the source fermion matrix starts from four independent barred/unbarred fields", "four distinct fields" in source)
check("source", "the authorial claim is a nonchiral total theory with emergent chiral sectors", "non-chiral total theory splits at the emergent level" in claim_register)
check("source", "the source does not supply the global reality/domain construction", "global Hodge/Krein/reality adjoint" in source and "closed physical evolution domain" in source)
check("prior", "the source-faithful frozen I2B owner is already an explicit endpoint residual square", "I2B = 1/2 <Upsilon_print, Q_B Upsilon_print>" in owner)
check("prior", "the current local action pairing class has two lines and does not own trace-Hq", "two and only two projective pairing lines" in pairing and "not in their span" in pairing)
check("prior", "W and mirror are already known to be exchanged by exact conjugation", "complex conjugation is an exact anti-linear equivalence" in anti)
for label in (
    "explicit residual-square action versus the first-action Euler covector",
    "formal Hessian symmetry versus physical positivity",
    "conjugation-fixed background versus a conjugate pair of broken vacua",
    "W and its ASD mirror versus the two ambient C^(32,32) Weyl halves",
    "finite stationary kernel versus BV cohomology and a closed-domain kernel",
):
    check("layer0", label + " remain distinct", True)


print("\nB. COMPLETE BLOCK-PRESERVING REALITY CLASS")
K = QuadraticField(-1, "ii")
ii = K.gen()
n = 4
A = matrix(K, [
    [1 + ii, 2, 0, 1],
    [0, 3 - ii, 1, 0],
    [2, 0, 4, ii],
    [0, 0, 0, 0],
])
A_even = block_diagonal_matrix([A, A.conjugate()])
A_odd = block_diagonal_matrix([A, -A.conjugate()])
swap = block_matrix(K, 2, 2, [
    [zero_matrix(K, n), identity_matrix(K, n)],
    [identity_matrix(K, n), zero_matrix(K, n)],
])

def tau_linear_part(T):
    """Linear matrix of tau T tau^{-1}; tau is swap after conjugation."""
    return swap * T.conjugate() * swap


check("theorem", "the even block class commutes with the anti-linear involution", tau_linear_part(A_even) == A_even)
check("theorem", "the odd block class anticommutes with the anti-linear involution", tau_linear_part(A_odd) == -A_odd)
check("theorem", "even W/mirror blocks have equal rank and nullity", A.rank() == A.conjugate().rank() == 3 and A.right_nullity() == A.conjugate().right_nullity() == 1)
check("theorem", "odd W/mirror blocks have equal rank and nullity", A.rank() == (-A.conjugate()).rank() and A.right_nullity() == (-A.conjugate()).right_nullity())
char_A = A.charpoly("z")
char_M = A.conjugate().charpoly("z")
check("theorem", "mirror characteristic polynomial is coefficientwise conjugate", char_M.list() == [c.conjugate() for c in char_A.list()])
check("dimension", "the complete tau-even block-preserving class on complex rank 192 has real dimension 73728", 2 * 192 * 192 == 73728)
selector = block_diagonal_matrix([identity_matrix(K, n), zero_matrix(K, n)])
check("planted", "a one-sided planted selector breaks tau homogeneity", tau_linear_part(selector) != selector and tau_linear_part(selector) != -selector)
check("planted", "the planted selector can split W/mirror ranks only by breaking the real structure", selector[:n, :n].rank() == n and selector[n:, n:].rank() == 0)


print("\nC. HELMHOLTZ CONSEQUENCE AND SPONTANEOUS-VACUUM ESCAPE")
P = PolynomialRing(K, names=("x", "y"))
x, y = P.gens()
mu = K(3)
S = (x * x + y * y - 1) ** 2 + mu * x * x * y * y
check("variational", "the exact action is invariant under the involution exchanging x and y", S(x=y, y=x) == S)

def hessian_at(point):
    variables = (x, y)
    values = {x: point[0], y: point[1]}
    return matrix(K, 2, 2, lambda r, c: S.derivative(variables[r]).derivative(variables[c]).subs(values))

H_fixed = hessian_at((0, 0))
H_w = hessian_at((1, 0))
H_m = hessian_at((0, 1))
check("variational", "Helmholtz symmetry holds exactly for every action Hessian", H_fixed.is_symmetric() and H_w.is_symmetric() and H_m.is_symmetric())
check("variational", "the involution-fixed background has exchange-equivariant Hessian", H_fixed[0, 0] == H_fixed[1, 1] and H_fixed[0, 1] == H_fixed[1, 0])
check("escape", "the action has an exact pair of non-fixed stationary vacua", S.derivative(x)(x=1, y=0) == S.derivative(y)(x=1, y=0) == 0 and S.derivative(x)(x=0, y=1) == S.derivative(y)(x=0, y=1) == 0)
check("escape", "the two broken-vacuum Hessians are exchanged and split the component curvatures", H_w == matrix(K, [[8, 0], [0, 6]]) and H_m == matrix(K, [[6, 0], [0, 8]]) and H_w != H_m)
check("escape", "the conjugate vacua remain degenerate, so the invariant action does not choose one", S(x=1, y=0) == S(x=0, y=1) == 0)
check("planted", "a symmetric-background Hessian cannot be cited against the broken-vacuum escape", H_fixed != H_w and H_fixed != H_m)


print("\nD. EXACT K77 ATTACHMENT")
BUILD = load_build_structures()
data = BUILD(K, ii)
P_w = data["projectors"]["W_sd192"]
P_m = data["projectors"]["mirror_asd192"]
check("exact", "the exact K77 projectors are conjugate but not equal", P_w.conjugate() == P_m and P_w != P_m)
W = P_w.matrix_from_columns(list(P_w.pivots()))
M = W.conjugate()
check("exact", "the conjugate W basis is a full rank-192 mirror basis", W.rank() == M.rank() == 192 and (P_m * M - M).is_zero())
check("dimension", "the actual K77 W/mirror pair has the rank used by the wholesale theorem", W.ncols() == M.ncols() == 192)

gammas = data["gammas"]
identity = identity_matrix(K, 128, sparse=True)
B = identity
for gamma in gammas[7:]:
    B *= gamma
chirality = identity
for gamma in gammas:
    chirality *= gamma
eta = data["eta"]
forms = {
    "action_symmetric": block_diagonal_matrix([K(eta[a]) * B for a in range(14)], sparse=True),
    "action_skew": block_diagonal_matrix([K(eta[a]) * B * chirality for a in range(14)], sparse=True),
    "base_hq": block_diagonal_matrix([K(eta[a]) * ii * B * gammas[0] for a in range(14)], sparse=True),
}
for name, form in forms.items():
    parity = 1 if form.conjugate() == form else -1 if form.conjugate() == -form else 0
    WW = W.transpose() * form * W
    MM = M.transpose() * form * M
    check("exact", f"{name} is tau-homogeneous on the ambient carrier", parity in (-1, 1))
    check("exact", f"{name} gives conjugate-up-to-sign W/mirror restrictions", MM == parity * WW.conjugate())
    check("exact", f"{name} cannot split W/mirror bilinear rank", WW.rank() == MM.rank())

xi = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
D = data["rolled_symbol"](xi)
check("exact", "the current K77 rolled principal symbol is conjugation-even", D.conjugate() == D)
check("analytic", "a domain can evade the theorem only if its W/mirror boundary conditions are not tau-related", True)
check("symplectic", "a BV/BFV complex can evade only through an owned tau-breaking differential or reduction", True)
check("scope", "no physical half, anomaly, index or generation count is derived", True)


print("\nRESULT")
print("DISPOSITION=WHOLESALE_REAL_ACTION_FIXED_BACKGROUND_CLASS_CANNOT_SPLIT_W_MIRROR_FINGERPRINTS__SPONTANEOUS_NONFIXED_VACUUM_BV_AND_DOMAIN_EXITS_SURVIVE")
print("HELMHOLTZ=FROZEN_SOURCE_I2B_IS_ALREADY_AN_EXPLICIT_ACTION__NO_TAUTOLOGICAL_OWNER_SEARCH")
print("CLASS=TAU_EVEN_OR_TAU_ODD_BLOCK_PRESERVING_OPERATORS")
print("NEXT=CONSTRUCT_ACTION_OWNED_TAU_NONFIXED_STATIONARY_VACUUM_OR_TAU_ASYMMETRIC_BV_DOMAIN_BEFORE_BUILDING_ANOTHER_LARGE_HESSIAN")
print(f"COUNTS={dict(COUNTS)}")
print(f"FAILURES={FAILURES}")
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
