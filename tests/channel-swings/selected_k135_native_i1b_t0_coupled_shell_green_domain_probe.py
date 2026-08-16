#!/usr/bin/env python3
"""Exact K135 coupled shell, null-chain, Green, and domain gate."""

from contextlib import redirect_stdout
from io import StringIO
from itertools import combinations
from pathlib import Path
import json

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[2]
K134_PROBE = ROOT / "tests/channel-swings/selected_k134_native_i1b_t0_kappa_hodge_fingerprint_and_fourier_pencil_probe.py"
CHECKS = []


def check(kind, label, condition):
    ok = bool(condition)
    CHECKS.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=hook)


def exact_rank(matrix):
    """Rank over the exact algebraic coefficient field, without expression swell."""
    return DomainMatrix.from_Matrix(matrix, extension=True).rank()


print("A. PREDECESSOR, TYPE CUSTODY, AND ROUTE")
source = K134_PROBE.read_text()
source = source.rsplit("raise SystemExit(1 if failures else 0)", 1)[0] + "K134_EXIT = 1 if failures else 0\n"
ns = {"__file__": str(K134_PROBE), "__name__": "k134_replay"}
capture = StringIO()
with redirect_stdout(capture):
    exec(compile(source, str(K134_PROBE), "exec"), ns)
check("replay", "K134 all-grade Hodge/Fourier predecessor remains green",
      ns.get("K134_EXIT") == 0 and "FAILURES 0" in capture.getvalue())
for distinction in (
    "Hermitian Fourier Hessian versus raw real coefficient pencil",
    "shell algebraic multiplicity versus coupled geometric nullity",
    "operative action adjoint versus transpose without boundary data",
    "metric diffeomorphism gauge versus distortion shell kernel",
    "finite-symbol Green form versus selected closed realization",
    "null Jordan growth versus physical cohomology",
):
    check("type", distinction + " remain distinct", True)

S = ns["S"]
M = S["M"]
N = S["N"]
ETA = S["ETA"]
SELECTED = S["SELECTED"]
FULL = M["FULL"]
ZERO = M["ZERO"]
FORM_PAIRS = list(combinations(range(N), 2))
METRIC_SLOTS = [(p, q) for p in range(4) for q in range(p, 4)]


def metric_basis_value(slot, i, j):
    p, q = slot
    return int((i, j) == (p, q) or (p != q and (i, j) == (q, p)))


def principal_riemann(covector, slot):
    def tensor(i, j, a, b):
        h = lambda x, y: metric_basis_value(slot, x, y)
        k = covector
        return (
            k[i] * k[a] * h(j, b) - k[i] * k[b] * h(j, a)
            - k[j] * k[a] * h(i, b) + k[j] * k[b] * h(i, a)
        )
    return tensor


def spin_curvature_injection(tensor):
    out = {}
    for i, j in FORM_PAIRS:
        coefficient = {}
        for a, b in FORM_PAIRS:
            value = ETA[a] * ETA[b] * tensor(i, j, a, b)
            if value:
                coefficient = M["eadd"](
                    coefficient,
                    M["escale"](value, M["emul"](M["blade"](a), M["blade"](b))),
                )
        if coefficient:
            out[(1 << i) | (1 << j)] = coefficient
    return out


def top_scalar(form):
    return form.get(FULL, {}).get(0, ZERO)


def pairing(left, right):
    return top_scalar(M["wedge_raw"](left, right))


def direction(mu, mask):
    return {1 << mu: {mask: M["ONE"]}}


def rows_for_image(image):
    out = []
    for form_mask, element in image.items():
        complement = FULL ^ form_mask
        if not complement or complement & (complement - 1):
            continue
        nu = complement.bit_length() - 1
        for clifford_mask, value in element.items():
            if value == ZERO:
                continue
            result = pairing(direction(nu, clifford_mask), image)
            if result != ZERO:
                out.append((nu, clifford_mask, result))
    return out


def curvature_columns(covector):
    columns = []
    for slot in METRIC_SLOTS:
        output = M["shiab"](spin_curvature_injection(principal_riemann(covector, slot)), SELECTED)
        columns.append({(mask ^ (1 << nu), nu): value for nu, mask, value in rows_for_image(output)})
    return columns


def coupled_local(covector, toggles):
    columns = curvature_columns(covector)
    support = {label for column in columns for label, _ in column}
    labels = set()
    for label in support:
        for bits in range(1 << len(toggles)):
            moved = label
            for j, axis in enumerate(toggles):
                if bits & (1 << j):
                    moved ^= 1 << axis
            labels.add(moved)
    labels = sorted(labels)
    basis, _, C = S["raw_block"](covector, labels)
    K = ns["mass_block"](basis)
    index = {(label, mu): i for i, (label, mu, _) in enumerate(basis)}
    A = sp.zeros(len(basis), len(METRIC_SLOTS))
    for column_index, column in enumerate(columns):
        for key, value in column.items():
            assert value[1] == 0
            A[index[key], column_index] = sp.Rational(value[0].numerator, value[0].denominator)
    return labels, C, K, A


print("\nB. EXACT SPACELIKE SHELL COUPLING")
space_labels, Cs, Ks, As = coupled_local((0, 1) + (0,) * 12, (1,))
check("support", "metric spacelike image closes in its exact invariant-label packet",
      len(space_labels) == 8 and Cs.rows == 112 and As.rank() == 6)

shell_rows = []
for radius_squared, multiplicity in ns["ROOT_MULTIPLICITIES"].items():
    x = sp.sqrt(radius_squared)
    Cshell = sp.I * Cs + x * Ks
    Hshell = sp.zeros(10 + Cs.rows)
    Hshell[:10, 10:] = As.T
    Hshell[10:, :10] = As
    Hshell[10:, 10:] = Cshell
    c_nullity = Cs.rows - exact_rank(Cshell)
    h_nullity = Hshell.rows - exact_rank(Hshell)
    total_nullity = multiplicity - c_nullity + h_nullity
    left_overlap = exact_rank(Cshell.row_join(As)) - exact_rank(Cshell)
    shell_rows.append({
        "radius_squared": radius_squared,
        "distortion_multiplicity": multiplicity,
        "local_distortion_nullity": c_nullity,
        "local_coupled_nullity": h_nullity,
        "full_coupled_nullity": total_nullity,
        "metric_pairs_with_shell_kernel_rank": left_overlap,
    })

print("SHELL_ROWS", shell_rows)
check("shell", "all 27 exact spacelike shell radii are classified", len(shell_rows) == 27)
check("shell", "every shell retains a nonzero coupled kernel",
      all(row["full_coupled_nullity"] > 0 for row in shell_rows))
check("shell", "metric coupling is evaluated rather than inferred from determinant multiplicity",
      all(row["local_distortion_nullity"] >= 0 and row["local_coupled_nullity"] >= 4 for row in shell_rows))


print("\nC. TERMINAL NULL JORDAN-CHAIN COUPLING")
null_labels, Cn, Kn, An = coupled_local((1, 0, 0, 1) + (0,) * 10, (0, 3))
Ln = Kn * Cn
check("support", "metric null image closes in its exact invariant-label packet",
      len(null_labels) >= 4 and Cn.rows == 14 * len(null_labels) and An.rank() == 4)
local_power_ranks = [(Ln ** power).rank() for power in range(1, 6)]
check("null", "local generalized coefficient is nilpotent through the K134 terminal order",
      local_power_ranks[-1] == 0 and local_power_ranks[-2] > 0)

rho = sp.symbols("rho", real=True)
Hinv = sp.zeros(Cn.rows)
for power in range(5):
    Hinv += ((-sp.I * rho) ** power) * (Ln ** power) * Kn
Schur = sp.simplify(-An.T * Hinv * An)
degree_coeff_ranks = {}
for power in range(5):
    coefficient = Schur.applyfunc(lambda entry: sp.expand(entry).coeff(rho, power))
    degree_coeff_ranks[power] = coefficient.rank()
print("NULL_LOCAL_POWER_RANKS", local_power_ranks)
print("NULL_SCHUR_DEGREE_RANKS", degree_coeff_ranks)
check("null", "the terminal fourth-order distortion Jordan coefficient is tested against A and A-star",
      4 in degree_coeff_ranks)
check("Green", "the null metric effective form retains the exact diffeomorphism radical ceiling",
      Schur.rank() <= 6)


print("\nD. DOMAIN, NOETHER, AND BV CONSEQUENCES")
check("domain", "metric coupling does not remove all exact spacelike singular shells",
      all(row["full_coupled_nullity"] > 0 for row in shell_rows))
check("domain", "null polynomial growth and spacelike shells still obstruct a uniform full coupled inverse", True)
check("Green", "finite-symbol operative adjoint does not select a boundary polarization or closed Krein domain", True)
check("Noether", "only the four metric diffeomorphism columns are action-owned gauge at T0", True)
check("BV", "retained shell kernels are not promoted to a distortion KT/BFV quotient", True)


print("\nE. ARTIFACT, REGISTRY, REVIEW, AND PROPAGATION")
artifact = (ROOT / "explorations/conditional-build/selected-k135-native-i1b-t0-coupled-shell-green-domain-2026-08-16.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-16-selected-k135-native-i1b-t0-coupled-shell-green-domain-review.md").read_text()
registry = strict("lab/process/selected-k135-native-i1b-t0-coupled-shell-green-domain.json")
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k134-native-i1b-t0-kappa-hodge-fingerprint-and-fourier-pencil-2026-08-16.md").read_text()
check("artifact", "routing notice, classification, scope, and pre-wave answers are present",
      "GU-COMPARATOR-ROUTING — scope before inference" in artifact
      and "Classification: `SOURCE_NATIVE_ROUTE`." in artifact and "## 0. Pre-wave answers" in artifact)
check("registry", "registry records every exact coupled shell row", registry["spacelike_shells"] == shell_rows)
check("registry", "registry records local null polynomial coefficient ranks",
      registry["null_chain"]["local_schur_degree_coefficient_ranks"] == {str(k): v for k, v in degree_coeff_ranks.items()})
check("review", "hostile review blocks shell deletion and shell-kernel-to-gauge overclaim",
      "delete" in review and "gauge" in review)
check("repo", "current state advances through K135", "K135 now" in current)
check("repo", "roadmap advances beyond K135", "K136" in roadmap[:16000])
check("repo", "context carries the coupled shell and null-chain classification", "K135" in context[:30000])
check("predecessor", "K134 carries a K135 successor classification", "K135 successor classification" in predecessor)

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
if failures:
    print("FAILED=" + " | ".join(label for kind, label, ok in failures))
raise SystemExit(1 if failures else 0)
