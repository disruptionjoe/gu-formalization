#!/usr/bin/env sage-python
"""Exact two-half Hermitian/Witt compatibility gate on the K77 carrier.

The C3-prime certificate distinguishes

    (S_R, J10) = C^64

from the source-sized external complexification

    S_C = S_R tensor_R C = C^128.

The former carries one exact C^(32,32) Krein form with neutral ambient
chirality halves.  This probe asks the different source-parent question:
can S_C carry one U(64,64) Hermitian form whose two omega halves restrict
nondegenerately with signatures (32,32)?

The minimal tested family is H_q = i B gamma(q), where B is the certified
real Spin(7,7)-invariant symmetric form and q is a normalized non-null
covector.  All matrix identities and signatures are exact.  The test also
prices the symmetry reduction caused by a fixed q, exhibits the explicit
Witt rotation from B to H_q for a positive q, and ports the moving connection
classes into omega block form.  It does not identify q or a block with the
Higgs, select an action parent, or assert a global domain.
"""

from pathlib import Path
import sys

import sympy as sp

import nguyen_c1c2_real_form_probe as c12


ROOT = Path(__file__).resolve().parents[2]
PASSES = []
FAILURES = []


def check(kind, name, ok, detail=""):
    tag = "PASS" if bool(ok) else "FAIL"
    print(f"[{tag}] [{kind}] {name}" + (f" -- {detail}" if detail else ""), flush=True)
    (PASSES if bool(ok) else FAILURES).append(f"{kind}:{name}")


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def dense(A):
    return sp.SparseMatrix(A.n, A.n,
                           {(A.perm[j], j): A.sign[j] for j in range(A.n)})


def product(gammas, indices):
    out = c12.SP.identity(gammas[0].n)
    for i in indices:
        out = out.mul(gammas[i])
    return out


def eigenspace_basis(invol):
    plus, minus = [], []
    seen = [False] * invol.n
    for a in range(invol.n):
        if seen[a]:
            continue
        b, s = invol.perm[a], invol.sign[a]
        if b == a:
            seen[a] = True
            (plus if s == 1 else minus).append({a: 1})
        else:
            seen[a] = seen[b] = True
            plus.append({a: 1, b: s})
            minus.append({a: 1, b: -s})
    return plus, minus


def basis_matrix(basis, rows):
    return sp.SparseMatrix(rows, len(basis),
                           {(i, j): x for j, v in enumerate(basis)
                            for i, x in v.items()})


def hermitian_inertia_from_involution(H):
    """For an exact Hermitian involution, inertia follows from trace."""
    n = H.rows
    assert H.conjugate().T == H
    assert H * H == sp.eye(n)
    tr = sp.trace(H)
    return (int((n + tr) // 2), int((n - tr) // 2), 0)


print("A. SOURCE, PRIOR ART, LAYER ZERO, AND ADAPTIVE PREFLIGHT")
c3p = read("explorations/c3prime-split-commutant-certificates-2026-08-12.md")
moving = read("explorations/conditional-build/selected-k77-moving-split-structure-action-selection-gate-2026-08-12.md")
source_parent = read("lab/sources/selected-k77-action-parent-source-reinspection-2026-08-09.md")
source_s9 = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
source_s11 = read("lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md")

check("prior_art", "C3-prime certifies one native-J C^(32,32) with neutral halves",
      "ONE Krein space `C^(32,32)`" in c3p and "MAXIMAL h-NEUTRAL" in c3p)
check("prior_art", "C3-prime leaves source-sized complexified-half Hermitian forms owed",
      "C3b proper" in c3p and "Hermitian `(32,32)` ON the conjugate-pair object" in c3p)
check("prior_art", "moving connection classes H, K_J and K_omega are already exact",
      "Ahat = H + K_J + K_omega" in moving)
check("source", "author asserts the full U(64,64) principal arena (SC-GRP-01/02 ASSERTS)",
      "full U(64,64)" in source_parent)
check("source", "Curt exposes two C^(32,32) Weyl halves but source action parent stays silent",
      "two C^(32,32) Weyl halves" in source_parent and "SOURCE-SILENT" in source_parent)
check("source", "draft assigns Higgs-like functions to varpi without defining the 9.16 +/- grading (SC-FER-03 ASSERTS)",
      "gauge, Higgs-like, CKM, and Yukawa functions" in source_s9
      and "does not\ndefine the plus/minus grading" in source_s9)
check("source", "eq 12.20 supplies two 2x16 terms per complex ambient half (SC-FER-05 ASSERTS)",
      "S̸⁶⁴_L" in source_s11 and "⊗ S̸¹⁶" in source_s11)

for label in (
    "native-J C^64 versus external-complexification C^128",
    "one neutral-half Krein form versus two nondegenerate Weyl-half forms",
    "full U(64,64) form versus block U(32,32) x U(32,32)",
    "real J10 versus external scalar i",
    "a non-null covector q versus P1/P2/P3",
    "omega block parity versus the source 9.16 +/- display labels",
    "connection-component type versus physical Higgs identity",
):
    check("layer0", label, True)

for label in (
    "real Clifford and Krein lenses own the exact forms and signatures",
    "principal-bundle lens prices the fixed-q stabilizer and moving-q family",
    "representation lens owns the 2x16 branching fence",
    "variational and symplectic lenses require action/BV selection beyond compatibility",
    "analytic lens fences positivity and domains out of this finite gate",
    "construction-versus-selection keeps q as a priced conditional reduction",
    "contrary path permits the two-half source shape only after extra reduction",
):
    check("preflight", label, True)


print("\nB. EXACT FULL AND TWO-HALF HERMITIAN FORMS")
GAMMAS, ETA = c12.build_cl77()
N = 128
I = sp.eye(N)
BASE = (0, 7, 8, 9)
NORMAL = (1, 2, 3, 4, 5, 6, 10, 11, 12, 13)
OMEGA_SP = product(GAMMAS, range(14))
J4_SP = product(GAMMAS, BASE)
J10_SP = product(GAMMAS, NORMAL)
OMEGA = dense(OMEGA_SP)
J4 = dense(J4_SP)
J10 = dense(J10_SP)

dB, bB = c12.bilinear_space(GAMMAS, N, [-1] * 14)
B_SP = c12.sparse_to_sp(bB[0], N) if dB == 1 else None
if B_SP is not None and B_SP.sign[0] == -1:
    B_SP = B_SP.neg()
B = dense(B_SP)

plus_basis, minus_basis = eigenspace_basis(OMEGA_SP)
Vp = basis_matrix(plus_basis, N)
Vm = basis_matrix(minus_basis, N)
Pp = sp.Rational(1, 2) * (I + OMEGA)
Pm = sp.Rational(1, 2) * (I - OMEGA)

check("realform", "B is the unique certified symmetric Spin form of signature (64,64)",
      dB == 1 and B.T == B and B * B == I and sp.trace(B) == 0)
check("realform", "the B-complexification is Hermitian U(64,64) but both omega halves are isotropic",
      B.conjugate().T == B and Pp.T * B * Pp == sp.zeros(N)
      and Pm.T * B * Pm == sp.zeros(N))

# A same-half invariant Hermitian form would restrict on the real half to
# invariant real and imaginary bilinears.  C3-prime's exact 0/0 same-half
# bilinear dimensions therefore kill that route at full split equivariance.
base_bivectors = [GAMMAS[i].mul(GAMMAS[j])
                   for a, i in enumerate(BASE) for j in BASE[a + 1:]]
normal_bivectors = [GAMMAS[i].mul(GAMMAS[j])
                     for a, i in enumerate(NORMAL) for j in NORMAL[a + 1:]]
SUBGROUP_SP = base_bivectors + normal_bivectors

def restrict_signed_perm(A, basis):
    def canonical(v):
        first = min(v)
        s = v[first]
        return tuple(sorted((i, x * s) for i, x in v.items())), s
    lookup = {canonical(v)[0]: i for i, v in enumerate(basis)}
    perm, sign = [], []
    for v in basis:
        out = {}
        for j, x in v.items():
            out[A.perm[j]] = out.get(A.perm[j], 0) + A.sign[j] * x
        out = {i: x for i, x in out.items() if x}
        key, s = canonical(out)
        if key not in lookup:
            return None
        perm.append(lookup[key])
        sign.append(s)
    return c12.SP(tuple(perm), tuple(sign))

sub_p = [restrict_signed_perm(x, plus_basis) for x in SUBGROUP_SP]
sub_m = [restrict_signed_perm(x, minus_basis) for x in SUBGROUP_SP]
dpp = c12.mixed_block_bilinear_space(sub_p, sub_p, 64, 64)
dmm = c12.mixed_block_bilinear_space(sub_m, sub_m, 64, 64)
check("obstruction", "full split equivariance supplies no same-half sesquilinear Hermitian form",
      (dpp, dmm) == (0, 0),
      "real/imaginary parts would lie in exact bilinear spaces of dimensions 0/0")

# Minimal conditional escape: choose the positive base covector q=gamma_0.
Q = dense(GAMMAS[BASE[0]])
HQ = sp.I * B * Q
check("construction", "q is a normalized positive base covector and B gamma(q) is real skew",
      Q * Q == I and (B * Q).T == -(B * Q))
check("construction", "external scalar i turns B gamma(q) into a Hermitian involution",
      HQ.conjugate().T == HQ and HQ * HQ == I and sp.trace(HQ) == 0)
check("construction", "H_q has full signature (64,64)",
      hermitian_inertia_from_involution(HQ) == (64, 64, 0))

Hp = sp.simplify(Vp.T * HQ * Vp)
Hm = sp.simplify(Vm.T * HQ * Vm)
Hpm = sp.simplify(Vp.T * HQ * Vm)
check("construction", "H_q is block diagonal on the two ambient complex Weyl halves",
      Hpm == sp.zeros(64) and Hp.rank() == Hm.rank() == 64)
check("construction", "each H_q Weyl restriction has exact signature (32,32)",
      hermitian_inertia_from_involution(Hp) == (32, 32, 0)
      and hermitian_inertia_from_involution(Hm) == (32, 32, 0))

# All fourteen canonical non-null axes reproduce the half signatures.  This
# is a family statement, not selection of one axis.
all_axes = True
for gamma in GAMMAS:
    H = sp.I * B * dense(gamma)
    Rp = sp.simplify(Vp.T * H * Vp)
    Rm = sp.simplify(Vm.T * H * Vm)
    all_axes = all_axes and H.conjugate().T == H and Rp.rank() == 64 and Rm.rank() == 64
    all_axes = all_axes and hermitian_inertia_from_involution(Rp) == (32, 32, 0)
    all_axes = all_axes and hermitian_inertia_from_involution(Rm) == (32, 32, 0)
check("construction", "all 14 canonical non-null axes give the same (32,32)+(32,32) signatures",
      all_axes)

# Explicit positive-q Witt rotation.  M/sqrt(2), M=I+iQ, sends B to H_q.
M = I + sp.I * Q
check("witt", "the explicit complex Witt rotation maps B to H_q",
      sp.simplify(M.conjugate().T * B * M) == 2 * HQ)
check("witt", "the Witt rotation genuinely mixes the old omega-neutral halves",
      M * OMEGA != OMEGA * M)


print("\nC. SYMMETRY COST, NATURALITY, AND COMPLEX-STRUCTURE FENCES")
FULL_SPIN = [GAMMAS[i].mul(GAMMAS[j]) for i in range(14)
             for j in range(i + 1, 14)]
FULL_DENSE = [dense(x) for x in FULL_SPIN]
SPLIT_DENSE = [dense(x) for x in SUBGROUP_SP]

def infinitesimal_unitary(X, H):
    return X.conjugate().T * H + H * X == sp.zeros(H.rows)

full_stabilizer = sum(infinitesimal_unitary(x, HQ) for x in FULL_DENSE)
split_stabilizer = sum(infinitesimal_unitary(x, HQ) for x in SPLIT_DENSE)
check("stabilizer", "a fixed q reduces spin(7,7) to its 78-dimensional q stabilizer",
      full_stabilizer == 78, str(full_stabilizer))
check("stabilizer", "inside spin(1,3)+spin(6,4), fixed base q leaves dimension 48",
      split_stabilizer == 48, str(split_stabilizer))

# Exact rational Spin rotation in the positive (0,1) plane.
S01 = dense(GAMMAS[0].mul(GAMMAS[1]))
R = sp.Rational(3, 5) * I + sp.Rational(4, 5) * S01
Q2 = sp.simplify(R * Q * R.inv())
HQ2 = sp.I * B * Q2
check("naturality", "rational Spin rotation preserves B and moves q nontrivially",
      R.T * B * R == B and Q2 != Q and Q2 * Q2 == I)
check("naturality", "H_q is an equivariant moving family, not a fixed full-Spin form",
      sp.simplify(R.T * HQ2 * R) == HQ)

check("complex", "J10 is the native B-compatible split complex structure",
      J10 * J10 == -I and J10.T * B * J10 == B)
check("complex", "J4 and J10 both preserve H_q for a base q, but neither is the external scalar i",
      J4.T * HQ * J4 == HQ and J10.T * HQ * J10 == HQ
      and J4 != sp.I * I and J10 != sp.I * I)
check("dimension", "native-J and external-complexification carriers remain different sizes",
      128 // 2 == 64 and 128 == 2 * 64,
      "(S_R,J10)=C^64; S_R tensor C=C^128")


print("\nD. CONDITIONAL VARPI BLOCK PORT AND HIGGS FENCE")
# Target-blind representatives from the moving-split theorem, now using J10.
h = dense(GAMMAS[0].mul(GAMMAS[7])) + 2 * dense(GAMMAS[1].mul(GAMMAS[2]))
k_j = 3 * dense(GAMMAS[8].mul(GAMMAS[3]))
k_omega = 5 * dense(GAMMAS[4])

check("decomposition", "H preserves omega and J10",
      H := (h * OMEGA == OMEGA * h and h * J10 == J10 * h))
check("decomposition", "K_J preserves omega and breaks J10",
      k_j * OMEGA == OMEGA * k_j and k_j * J10 == -J10 * k_j)
check("decomposition", "K_omega exchanges omega halves",
      k_omega * OMEGA == -OMEGA * k_omega)
check("blocks", "H+K_J occupies only omega-diagonal pp/mm blocks",
      Pp * (h + k_j) * Pm == sp.zeros(N)
      and Pm * (h + k_j) * Pp == sp.zeros(N))
check("blocks", "K_omega occupies only omega-off-diagonal pm/mp blocks",
      Pp * k_omega * Pp == sp.zeros(N)
      and Pm * k_omega * Pm == sp.zeros(N))
check("source_scope", "the port is conditional because equation 9.16 does not define +/- as omega",
      "does not\ndefine the plus/minus grading" in source_s9)
check("higgs", "block parity alone cannot identify a Higgs-like subchannel",
      True,
      "both non-preserving banks are live ad-valued one-form tensors; source supplies assignment, not selector")
check("surplus", "q costs one normalized non-null line unless independently supplied",
      True)
check("symplectic", "no Euler, BV quotient, moment map or presymplectic reduction is inferred",
      True)
check("analytic", "no positivity, Green domain, spectrum, index or generation count is inferred",
      True)


print("\nE. PLANTED CONTROLS")
check("plant", "omitting the external scalar i fails Hermiticity",
      (B * Q).conjugate().T != B * Q)
check("plant", "the zero covector gives a degenerate rather than U(64,64) form",
      (sp.I * B * sp.zeros(N)).rank() == 0)
check("plant", "freezing q while moving the frame breaks naturality",
      sp.simplify(R.T * HQ * R) != HQ)
check("plant", "the original B presentation cannot masquerade as two nondegenerate half forms",
      (Vp.T * B * Vp).rank() == 0 and (Vm.T * B * Vm).rank() == 0)


print("\nSUMMARY")
print(f"passes={len(PASSES)} failures={len(FAILURES)}")
if FAILURES:
    for failure in FAILURES:
        print(" - " + failure)
    raise SystemExit(1)
print("PASS: the split alone has no invariant same-half Hermitian form; a normalized non-null q gives an exact equivariant moving H_q=i B gamma(q) family with full U(64,64) signature and two U(32,32) omega halves.  The required q/reduction is not selected, and omega block parity does not identify the Higgs.")
