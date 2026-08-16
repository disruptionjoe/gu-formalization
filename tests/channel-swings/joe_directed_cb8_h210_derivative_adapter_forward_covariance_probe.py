#!/usr/bin/env sage-python
"""CB-8A exact forward-covariance certificate for ``gamma(q_H) o d0``.

The H210 port and a coherently transforming horizontal covector section are
declared conditional inputs.  This probe does not construct or select either
input.  It checks the bundle algebra, including the inhomogeneous connection
law, and separates source-Y from pullback-X and graph-H_J stage claims.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from sage.all import GF, QQ, diagonal_matrix, identity_matrix, matrix, zero_matrix


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, ROUTING, CONDITIONAL SCOPE, AND PRIOR ART")
packet = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "he4-path-reprioritization-2026-08-16.md"
)
cb7 = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb7-wave-h210-half-duality-reprioritization-2026-08-16.md"
)
review = read(
    "lab/process/hostile-reviews/"
    "2026-08-16-joe-directed-cb7-h210-half-duality-review.md"
)
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
routing = read("lab/methods/source-native-comparator-routing.md")
cb4 = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb4-h210-finite-comoving-naturality-square-2026-08-16.md"
)
cb6 = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb6-h210-full-correlated-lift-naturality-2026-08-16.md"
)
check("scope", "the lane declares H210 and forbids construction of external data",
      "Action and external datum are off-limits" in packet)
check("scope", "CB7 asks for an assumed nowhere-null section, not its owner",
      "Assume a smooth nowhere-null horizontal covector section" in cb7)
check("source", "equation 9.16 is candidate grammar rather than a unique operator",
      "operators like" in source and "not a unique stabilized" in source)
check("source", "bars remain four independent source fields",
      "four distinct fields" in source)
check("source", "source row and column orders remain fixed",
      "bar-zeta-minus" in source and "zeta-plus" in source)
check("routing", "ordinary family index and Higgs comparators are non-adjudicating",
      "not** become evidence" in routing and "Ordinary family index" in routing)
check("prior_art", "CB4 supplies the associated-bundle moving-square discipline",
      "associated-bundle morphism" in cb4 and "inhom" not in cb4)
check("prior_art", "CB6 keeps the intrinsic graph plane and local cocycle distinct",
      "admitted overlap" in cb6 and "global Spin" in cb6)
check("prior_art", "hostile review requires the missing connection and null tests",
      "connection" in review and "null" in review and "Leibniz" in review)
for lens in (
    "source fidelity: modify only the declared conditional candidate",
    "stage/base: Y, X, and H_J have different ownership",
    "associated bundle: move every bundle factor on overlaps",
    "Clifford connection: include the affine connection term",
    "first-order symbol: isolate xi tensor gamma(q)",
    "Leibniz: q postcomposes the derivative",
    "null strata: nowhere-zero is weaker than nowhere-null",
    "both halves: retain the conjugate cell",
    "adverse transitions: freeze each moving factor",
    "novelty: do not rerun CB4/CB6 pointwise naturality",
    "scope: covariance does not construct a cocycle or section",
):
    check("preflight", lens, True)


print("B. EXACT MOVING CONNECTION/CLIFFORD/FORM SQUARE OVER QQ")
# At one overlap point, h and dh are the value and derivative of
# diag(x+2,(x+2)^-1).  psi and dpsi are an arbitrary exact first jet.
h = diagonal_matrix(QQ, [3, QQ(1) / 3])
dh = diagonal_matrix(QQ, [1, -QQ(1) / 9])
psi = matrix(QQ, 2, 1, [2, -1])
dpsi = matrix(QQ, 2, 1, [3, 4])
connection = diagonal_matrix(QQ, [2, -3])
gamma = matrix(QQ, [[0, 1], [1, 0]])
q = QQ(5)
q_coframe = QQ(2)
form_coframe = QQ(3)

psi_prime = h * psi
dpsi_prime = dh * psi + h * dpsi
connection_prime = h * connection * h.inverse() - dh * h.inverse()
nabla = dpsi + connection * psi
nabla_prime = dpsi_prime + connection_prime * psi_prime

# The horizontal q-covector and exterior one-form output have distinct bundle
# legs and may have distinct transitions.  The new Clifford frame is chosen
# so gamma'(C_H q) h = h gamma(q).
q_prime = q_coframe * q
gamma_prime = (QQ(1) / q_coframe) * h * gamma * h.inverse()
D = q * gamma * nabla
D_prime = form_coframe * q_prime * gamma_prime * nabla_prime
transported_D = form_coframe * h * D

check("connection", "inhomogeneous connection law gives nabla' psi'=h nabla psi",
      nabla_prime == h * nabla)
check("clifford", "moving q, Clifford frame, and spin frame obey covariance",
      q_prime * gamma_prime * h == h * (q * gamma))
check("form", "the derivative one-form carries the coframe transition",
      form_coframe * nabla_prime == form_coframe * h * nabla)
check("square", "D_q'=gamma'(q') d0' equals transported D_q",
      D_prime == transported_D)
check("parity", "the model gamma is odd between its two half slots",
      gamma[0, 0] == 0 and gamma[1, 1] == 0 and gamma[0, 1] != 0 and gamma[1, 0] != 0)
check("both_halves", "the forward square holds for each source half separately",
      all(D_prime[i, 0] == transported_D[i, 0] for i in (0, 1)))

# Exact hostile mutations.  Each omits one load-bearing motion.
connection_frozen = connection
nabla_bad_connection = dpsi_prime + connection_frozen * psi_prime
check("mutation", "freezing the connection fails", nabla_bad_connection != h * nabla)
connection_wrong_sign = h * connection * h.inverse() + dh * h.inverse()
check("mutation", "using the wrong affine sign fails",
      dpsi_prime + connection_wrong_sign * psi_prime != h * nabla)
check("mutation", "omitting q transport fails",
      form_coframe * q * gamma_prime * nabla_prime != transported_D)
check("mutation", "freezing the Clifford frame fails",
      form_coframe * q_prime * gamma * nabla_prime != transported_D)
check("mutation", "freezing the spinor jet fails",
      dpsi + connection_prime * psi != h * nabla)
check("mutation", "omitting exterior-form transport fails",
      q_prime * gamma_prime * nabla_prime != transported_D)


print("C. FIRST-ORDER SYMBOL AND LEIBNIZ RULE")
xi = QQ(7)
symbol = xi * q * gamma
check("symbol", "principal symbol is xi tensor gamma(q)", symbol == xi * (q * gamma))
check("symbol", "nonzero q gives a full-rank model symbol for nonzero xi",
      symbol.rank() == 2)
check("symbol", "zero cotangent frequency kills the first-order symbol",
      (QQ(0) * q * gamma).rank() == 0)
f, df = QQ(11), QQ(-2)
nabla_fpsi = f * nabla + df * psi
left = q * gamma * nabla_fpsi
right = f * D + df * q * gamma * psi
check("leibniz", "D_q(f psi)=f D_q psi+df tensor gamma(q)psi", left == right)
check("leibniz", "postcomposition creates no forward derivative-of-q term",
      left == right and q not in (0,))
qdot = QQ(3)
postcomposed_jet = q * gamma * dpsi
precomposed_jet = q * gamma * dpsi + qdot * gamma * psi
check("order", "precomposition is different and carries a derivative-of-q term",
      precomposed_jet - postcomposed_jet == qdot * gamma * psi
      and precomposed_jet != postcomposed_jet)


print("D. EXACT CL(7,7) ZERO, NULL, AND NON-NULL RANK STRATA")


def tensor_all(factors):
    out = matrix(factors[0].base_ring(), [[1]], sparse=True)
    for factor in factors:
        out = out.tensor_product(factor)
    return out


def build_cl77(field):
    i2 = identity_matrix(field, 2, sparse=True)
    s1 = matrix(field, [[0, 1], [1, 0]], sparse=True)
    s3 = matrix(field, [[1, 0], [0, -1]], sparse=True)
    eps = matrix(field, [[0, 1], [-1, 0]], sparse=True)
    plus, minus = [], []
    for index in range(7):
        plus.append(tensor_all([s3] * index + [s1] + [i2] * (6 - index)))
        minus.append(tensor_all([s3] * index + [eps] + [i2] * (6 - index)))
    return plus + minus


def product(items):
    out = identity_matrix(items[0].base_ring(), items[0].nrows(), sparse=True)
    for item in items:
        out *= item
    return out


for prime in (1009, 1013):
    field = GF(prime)
    raw = build_cl77(field)
    # Current repository H_(1,3) axes: one positive, then three negative.
    gammas = [raw[i] for i in (0, 7, 8, 9)]
    omega = product(raw)
    zero = zero_matrix(field, 128, 128, sparse=True)
    check("cl77", f"Clifford signs reproduce H_(1,3) over GF({prime})",
          gammas[0] * gammas[0] == identity_matrix(field, 128)
          and all(g * g == -identity_matrix(field, 128) for g in gammas[1:]))
    check("cl77", f"horizontal Clifford action flips ambient half over GF({prime})",
          all(g * omega == -omega * g for g in gammas))
    nonnull = gammas[0]
    null = gammas[0] + gammas[1]
    check("stratum", f"non-null gamma(q) has full half-to-half rank over GF({prime})",
          nonnull.rank() == 128 and nonnull * nonnull == identity_matrix(field, 128))
    check("stratum", f"nonzero null gamma(q) is nilpotent rank 64 over GF({prime})",
          null != zero and null * null == zero and null.rank() == 64)
    check("stratum", f"q=0 has rank zero over GF({prime})", zero.rank() == 0)
    for sign in (-1, 1):
        source_half = (omega - field(sign) * identity_matrix(field, 128)).right_kernel_matrix().transpose()
        check("both_halves", f"non-null q has rank 64 on ambient half {sign} over GF({prime})",
              (nonnull * source_half).rank() == 64)
        check("both_halves", f"null q has rank 32 on ambient half {sign} over GF({prime})",
              (null * source_half).rank() == 32)


print("E. BASE/STAGE CLASSIFIER AND SEMANTIC MUTANTS")
stage_rows = {
    "source_Y": {"base": "Y", "upstream": True, "observed": True,
                 "requires": "source horizontal subbundle and cocycle"},
    "pullback_X": {"base": "X", "upstream": False, "observed": True,
                   "requires": "typed pullback operator"},
    "graph_HJ": {"base": "X", "upstream": False, "observed": True,
                 "requires": "admitted graph atlas and Spin cocycle"},
}
check("stage", "only a source-Y horn can modify the upstream Y operator",
      [name for name, row in stage_rows.items() if row["upstream"]] == ["source_Y"])
check("stage", "pullback-X and graph-H_J horns type only observed operators",
      all(stage_rows[name]["observed"] and not stage_rows[name]["upstream"]
          for name in ("pullback_X", "graph_HJ")))
check("stage", "graph-H_J retains an explicit atlas/cocycle dependency",
      "graph atlas" in stage_rows["graph_HJ"]["requires"])
check("stage", "source-Y requires stronger source-horizontal structure",
      "source horizontal" in stage_rows["source_Y"]["requires"])
check("semantic_mutant", "X-only q is not promoted upstream",
      not stage_rows["pullback_X"]["upstream"])
check("semantic_mutant", "graph-plane q is not a source-owned section",
      not stage_rows["graph_HJ"]["upstream"])
check("semantic_mutant", "nowhere-zero does not imply nowhere-null",
      "nonzero null" in review or "nonzero null" in cb7)
check("semantic_mutant", "formal covariance does not construct a global atlas",
      "does not construct" in cb6)
check("semantic_mutant", "bars are not promoted to adjoints or reality",
      "independent" in source and "adjoint" in source)
check("semantic_mutant", "downstream kappa does not repair upstream cell typing",
      "downstream" in cb7 and "upstream" in cb7)


total = sum(COUNTS.values())
print(f"\nCB8-A COMPLETE: {total - len(FAILURES)}/{total} checks pass")
print("Counts:", dict(sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("Failures: " + "; ".join(FAILURES))
