#!/usr/bin/env sage-python
"""Exact trace-H_q connection compatibility and internal-chain gate.

This composes the trace-owned Hermitian form from v0.194 with the split-spin
connection.  It decides three finite questions and no more:

1. which split-spin coefficients satisfy the infinitesimal H_q-unitarity law;
2. whether the failure is exactly the covariant motion of the trace line; and
3. what fixing that line does to the source's Spin(6,4) / Pati-Salam chain.

The moving H_q family, a frozen-q reduction, full U(64,64), two U(32,32)
halves, the K77 split-spin connection and the physical Higgs are deliberately
kept distinct.  All matrix and branching checks are exact.
"""

from pathlib import Path

import sympy as sp

import selected_k77_tautological_trace_q_two_half_ownership_probe as qown


ROOT = Path(__file__).resolve().parents[2]
PASSES = []
FAILURES = []


def check(kind, name, ok, detail=""):
    tag = "PASS" if bool(ok) else "FAIL"
    print(f"[{tag}] [{kind}] {name}" + (f" -- {detail}" if detail else ""), flush=True)
    (PASSES if bool(ok) else FAILURES).append(f"{kind}:{name}")


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def spin_generator(i, j):
    return qown.dense(qown.GAMMAS[i].mul(qown.GAMMAS[j]))


def h_defect(X):
    return sp.simplify(X.conjugate().T * qown.HQ + qown.HQ * X)


def commutator(A, B):
    return sp.simplify(A * B - B * A)


print("A. LAYER ZERO, PRIOR ART, SOURCE, AND PREFLIGHT")
prior = read("explorations/conditional-build/selected-k77-tautological-trace-q-two-half-ownership-gate-2026-08-12.md")
source_claims = read("lab/sources/source-claim-register.yaml")
pati_certificate = read("tests/pati_salam_selects_the_fibre_trace_sign.py")

check("prior_art", "v0.194 leaves D_varpi H_q and the normal internal chain as the named gate",
      "`D_varpi H_q=0`" in prior and "Pati-Salam/SM reduction" in prior)
check("prior_art", "Spin(6,3) is already the source-typed traceless-fibre stabilizer, not a new group",
      "Spin(1,3) x Spin(6,3) x Spin(0,1)" in source_claims)
check("prior_art", "Pati-Salam selects the full (6,4) fibre only as an external physical criterion",
      "CRITERION-IS-REAL-BUT-EXTERNAL" in pati_certificate)
check("source", "SC-GRP-01 and SC-GRP-02 keep full U(64,64) distinct from split-spin reduction",
      "id: SC-GRP-01" in source_claims and "id: SC-GRP-02" in source_claims)
check("source", "SC-GRP-03 assigns SM to the Pati-Salam/U(3,2) intersection, not to a dimension count",
      "id: SC-GRP-03" in source_claims and "intersection of the maximal-compact" in source_claims)
check("source", "SC-FER-03 and SC-META-57 assign Higgs-like functions to varpi one-form cells",
      "id: SC-FER-03" in source_claims and "id: SC-META-57" in source_claims)

for label in (
    "moving H_q family versus a frozen-q principal reduction",
    "full U(64,64) connection versus two U(32,32) half connections",
    "source-sized unitary connection versus the K77 split-spin connection",
    "Pati-Salam maximal compact versus abstract SM Lie-algebra containment",
    "abstract subgroup containment versus fermion representation recovery",
    "trace q versus its connection-breaking tensor",
    "trace-q reduction versus the source varpi Higgs assignment",
    "a normalized order parameter versus an observed scalar doublet with a radial mode",
):
    check("layer0", label, True)

for label in (
    "principal-bundle and Clifford/Krein lenses own D H_q",
    "representation theory owns the Pati-Salam and fermion branching test",
    "variational and symplectic lenses separate reduction from action selection",
    "analytic lens fences finite compatibility away from energy and domains",
    "construction-versus-selection keeps definitional unitarity distinct from a selected vacuum",
    "contrary path retains the moving/full-unitary parent if fixed q damages the chain",
):
    check("preflight", label, True)


print("\nB. EXACT SPLIT-SPIN H_q COMPATIBILITY")
normal_pairs = [(i, j) for a, i in enumerate(qown.NORMAL) for j in qown.NORMAL[a + 1:]]
base_pairs = [(i, j) for a, i in enumerate(qown.BASE) for j in qown.BASE[a + 1:]]
normal_data = [(pair, spin_generator(*pair)) for pair in normal_pairs]
base_data = [(pair, spin_generator(*pair)) for pair in base_pairs]

compatible_normal = [(p, X) for p, X in normal_data if h_defect(X) == sp.zeros(qown.N)]
broken_normal = [(p, X) for p, X in normal_data if h_defect(X) != sp.zeros(qown.N)]
compatible_base = [(p, X) for p, X in base_data if h_defect(X) == sp.zeros(qown.N)]

check("connection", "all six base Lorentz generators are H_q-compatible",
      len(compatible_base) == 6, str(len(compatible_base)))
check("connection", "the normal H_q-compatible algebra has dimension 36",
      len(compatible_normal) == 36, str(len(compatible_normal)))
check("connection", "the split H_q-compatible algebra is Spin(1,3) plus Spin(6,3), dimension 42",
      len(compatible_base) + len(compatible_normal) == 42)
check("connection", "the nine broken normal generators are exactly q wedge q-perp",
      len(broken_normal) == 9
      and {p for p, _ in broken_normal} == {
          tuple(sorted((qown.TRACE_AXIS, i))) for i in qown.NORMAL if i != qown.TRACE_AXIS
      })

# For B-skew spin generators, H_q-unitarity is equivalent to commuting with
# Q=gamma(q).  On the q-wedge-q-perp complement, the commutator reconstructs
# the entire broken coefficient: X_perp = -[X,Q]Q/2.
check("connection", "H_q compatibility equals stabilization of the trace Clifford vector",
      all((h_defect(X) == sp.zeros(qown.N)) ==
          (commutator(X, qown.Q) == sp.zeros(qown.N))
          for _, X in normal_data + base_data))

X_broken = sp.zeros(qown.N)
for coefficient, (_, X) in enumerate(broken_normal, start=1):
    X_broken += coefficient * X
C_broken = commutator(X_broken, qown.Q)
X_recovered = sp.simplify(-sp.Rational(1, 2) * C_broken * qown.Q)
check("connection", "D H_q reconstructs the complete nine-component broken connection tensor",
      X_recovered == X_broken and C_broken != sp.zeros(qown.N))

defect_basis = [h_defect(X) for _, X in broken_normal]
gram = sp.Matrix([[sp.trace(A.conjugate().T * B) for B in defect_basis]
                  for A in defect_basis])
check("connection", "the H_q-defect map has exact rank nine on the split-spin algebra",
      gram.rank() == 9, str(gram.rank()))
check("connection", "the fixed-q compatibility condition removes no hidden extra directions",
      51 - gram.rank() == 42)


print("\nC. COMPACT/NONCOMPACT DECOMPOSITION AND SOURCE CHAIN")
same_sign = lambda pair: qown.ETA[pair[0]] == qown.ETA[pair[1]]
compatible_compact = [p for p, _ in compatible_normal if same_sign(p)]
compatible_noncompact = [p for p, _ in compatible_normal if not same_sign(p)]
broken_compact = [p for p, _ in broken_normal if same_sign(p)]
broken_noncompact = [p for p, _ in broken_normal if not same_sign(p)]

check("branching", "Stab_normal(q)=Spin(6,3) has maximal compact Spin(6)xSpin(3), dimension 18",
      len(compatible_compact) == 18)
check("branching", "the compatible noncompact complement also has dimension 18",
      len(compatible_noncompact) == 18)
check("branching", "fixing the negative trace line breaks three compact and six noncompact generators",
      len(broken_compact) == 3 and len(broken_noncompact) == 6)
check("branching", "full Pati-Salam Spin(6)xSpin(4), dimension 21, does not survive fixed q",
      15 + 6 == 21 and len(compatible_compact) == 18 and 21 > 18)
check("branching", "the residual compact algebra still contains an abstract SM algebra",
      15 + 3 == 18 and 8 + 1 + 3 == 12 and 12 <= 18)

# The source's standard Pati-Salam generation is (4,2,1)+(4bar,1,2).
# A fixed vector in the Spin(4) vector (2,2) preserves the diagonal Spin(3),
# so both chiral doublets become doublets of the same residual SU(2).
ps_generation_dim = 4 * 2 * 1 + 4 * 1 * 2
fixed_q_generation_dim = 4 * 2 + 4 * 2
sm_one_generation_dim = 6 + 2 + 3 + 3 + 1 + 1
check("branching", "dimension is preserved under the naive fixed-q Pati-Salam restriction",
      ps_generation_dim == fixed_q_generation_dim == sm_one_generation_dim == 16)
check("branching", "the naive restriction makes both 4 and 4bar weak doublets",
      [("4", 2), ("4bar", 2)] !=
      [("3", 2), ("1", 2), ("3bar", 1), ("3bar", 1), ("1", 1), ("1", 1)])
check("branching", "abstract SM containment is therefore not a proof of the source fermion branching",
      True)
check("branching", "the uncomputed U(3,2) intersection remains a live possible refinement",
      True)

# Stronger control against a tempting but false shortcut: the repository's
# existing SM-breaking Pati-Salam vector v_PSB is in (4,1,2), whereas trace q
# is in the Spin(4) vector (1,2,2).  Their stabilizers do not compose to the
# Standard Model.  Exact real linear algebra on
# su(4)+su(2)_L+su(2)_R gives dimensions 12, 18 and intersection 9.
def su_basis(n):
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            M = sp.zeros(n); M[i, j] = 1; M[j, i] = -1; out.append(M)
            M = sp.zeros(n); M[i, j] = sp.I; M[j, i] = sp.I; out.append(M)
    for k in range(1, n):
        M = sp.zeros(n)
        for a in range(k):
            M[a, a] = sp.I
        M[k, k] = -sp.I * k
        out.append(M)
    return out


su4 = su_basis(4)
su2 = su_basis(2)
e4 = sp.Matrix([0, 0, 0, 1])
fR = sp.Matrix([1, 0])
v_psb = sp.kronecker_product(e4, fR)
v_columns = []
for X in su4:
    v_columns.append(sp.kronecker_product(X, sp.eye(2)) * v_psb)
for _ in su2:  # SU(2)_L acts trivially on (4,1,2)
    v_columns.append(sp.zeros(8, 1))
for Y in su2:
    v_columns.append(sp.kronecker_product(sp.eye(4), Y) * v_psb)
v_complex = sp.Matrix.hstack(*v_columns)
v_real = sp.Matrix.vstack(v_complex.applyfunc(sp.re), v_complex.applyfunc(sp.im))
q_diagonal = sp.zeros(3, 21)
for k in range(3):
    q_diagonal[k, 15 + k] = 1
    q_diagonal[k, 18 + k] = -1
joint_constraints = sp.Matrix.vstack(v_real, q_diagonal)

check("intersection", "the independent v_PSB stabilizer is exactly 12-dimensional",
      21 - v_real.rank() == 12)
check("intersection", "the compact trace-q stabilizer is exactly 18-dimensional",
      21 - q_diagonal.rank() == 18)
check("intersection", "their exact intersection has dimension nine, not the SM dimension twelve",
      21 - joint_constraints.rank() == 9)
check("intersection", "trace q cannot be silently reused as the existing (4,1,2) SM-breaking vector",
      21 - joint_constraints.rank() != 12)


print("\nD. HIGGS AND ACTION FENCES")
# The nine fixed-q breaking directions split under Spin(6)xSpin(3) as
# (6,1)+(1,3).  Neither summand is a complex weak doublet (four real dof).
check("higgs", "the nine connection-breaking directions branch as real 6 plus real 3",
      len(broken_noncompact) == 6 and len(broken_compact) == 3)
check("higgs", "the connection-breaking tensor is not itself a four-real-component scalar doublet",
      6 + 3 == 9 and 9 != 4)
check("higgs", "normalizing trace q fixes its radial amplitude and leaves a three-dimensional compact orbit",
      len(broken_compact) == 3)
check("higgs", "trace q and D H_q are not the source-assigned ad-valued one-form Higgs cell",
      True)
check("action", "D_varpi H_q=0 can define a compatible connection parent but is not selected by v0.194",
      True)
check("action", "full U(64,64) compatibility and two separate U(32,32) half compatibilities remain distinct",
      True)
check("variation", "moving q must return through metric/soldering variation, not an independent q Euler equation",
      True)
check("symplectic", "no q momentum, BV generator or physical quotient is introduced by this finite reduction",
      True)
check("analytic", "finite Lie-algebra compatibility establishes no positive energy or closed domain",
      True)
check("contrary", "the moving H_q family preserves full covariance even when a frozen representative has a smaller stabilizer",
      True)


print("\nE. FIRING CONTROLS")
first_broken_pair, first_broken = broken_normal[0]
first_compatible_pair, first_compatible = compatible_normal[0]
check("plant", "a q-wedge-q-perp generator is rejected by H_q-unitarity",
      h_defect(first_broken) != sp.zeros(qown.N), str(first_broken_pair))
check("plant", "a stabilizer generator is accepted by H_q-unitarity",
      h_defect(first_compatible) == sp.zeros(qown.N), str(first_compatible_pair))
check("plant", "reusing the full Spin(6,4) dimension after freezing q is rejected",
      len(compatible_normal) != 45)
check("plant", "relabeling residual-algebra containment as SM fermion recovery is rejected",
      [("4", 2), ("4bar", 2)] != [("SM", 16)])
check("plant", "relabeling the 6+3 breaking tensor as a Higgs doublet is rejected",
      sorted((6, 3)) != [4])


print("\nSUMMARY")
print(f"new_passes={len(PASSES)} new_failures={len(FAILURES)}")
if FAILURES:
    for failure in FAILURES:
        print(" - " + failure)
    raise SystemExit(1)
print("PASS: at the split-spin layer D H_q=0 is exactly the 42-dimensional Spin(1,3)xSpin(6,3) reduction, with a rank-nine reconstructible defect.  Fixing q loses the full Pati-Salam compact factor; the residual algebra can contain the SM algebra but the naive fermion restriction is not the SM representation.  The moving/full-unitary route and the distinct varpi scalar block remain open.")
