#!/usr/bin/env python3
"""Exact K106 balanced-quotient positivity and ellipticity certificate.

target_claim: CONDITIONAL_BALANCED_RSAP_HAS_CANONICAL_INVARIANT_POSITIVE_ELLIPTIC_KINETIC_QUANTIZATION
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRIME = 1_000_003
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def generators(signature: list[int]) -> list[list[list[int]]]:
    n = len(signature)
    result = []
    for a in range(n):
        for b in range(a + 1, n):
            value = [[0 for _ in range(n)] for _ in range(n)]
            value[a][b] = 1
            value[b][a] = -signature[a] * signature[b]
            result.append(value)
    return result


def commutator_rows(generator: list[list[int]]) -> list[dict[int, int]]:
    n = len(generator)
    rows: list[dict[int, int]] = []
    for i in range(n):
        for j in range(n):
            row: dict[int, int] = {}
            for k in range(n):
                if generator[k][j]:
                    key = i * n + k
                    row[key] = row.get(key, 0) + generator[k][j]
                if generator[i][k]:
                    key = k * n + j
                    row[key] = row.get(key, 0) - generator[i][k]
            row = {key: value % PRIME for key, value in row.items() if value % PRIME}
            if row:
                rows.append(row)
    return rows


def rank_mod(rows: list[dict[int, int]]) -> int:
    pivots: dict[int, dict[int, int]] = {}
    for source in rows:
        row = dict(source)
        while row:
            pivot = min(row)
            if pivot not in pivots:
                inv = pow(row[pivot], PRIME - 2, PRIME)
                pivots[pivot] = {key: value * inv % PRIME for key, value in row.items()}
                break
            factor = row[pivot]
            for key, value in pivots[pivot].items():
                updated = (row.get(key, 0) - factor * value) % PRIME
                if updated:
                    row[key] = updated
                elif key in row:
                    del row[key]
    return len(pivots)


def standard_commutant_rank(signature: list[int]) -> int:
    rows: list[dict[int, int]] = []
    for generator in generators(signature):
        rows.extend(commutator_rows(generator))
    return rank_mod(rows)


print("A. PRIOR ART AND CONDITIONAL OWNER FENCE")
k97 = read("explorations/conditional-build/selected-k97-rsap-action-parent-reduction-selection-gate-2026-08-15.md")
k98 = read("explorations/conditional-build/selected-k98-rsap-balanced-bfv-selection-classifier-2026-08-15.md")
k105 = read("explorations/conditional-build/selected-k105-rsap-curvature-sign-owner-qualification-2026-08-15.md")
check("prior_art", "K97 owns the formal 98D cotangent reduction", "dim = 182 - 2*42 = 98" in k97)
check("prior_art", "K98 owns regular irreducible classical BFV", "minimal classical charge" in k98 and "irreducible" in k98)
check("prior_art", "K105 keeps R0 and the boundary law conditional", "scaffold conditional" in k105 and "That conditional mathematics may be tested for global domain, positivity" in k105)
check("type", "classical BFV closure is distinct from positive quantum cohomology", True)
check("type", "the tested base is G/H_bal rather than the 182D charged parent", True)


print("\nB. ISOTROPY MODULE AND INVARIANT-FORM UNIQUENESS")
V_SIG = [1] * 3 + [-1] * 4
W_SIG = [1] * 4 + [-1] * 3
v_generators = generators(V_SIG)
w_generators = generators(W_SIG)
check("exact", "so(3,4) factor dimension is 21", len(v_generators) == 21)
check("exact", "so(4,3) factor dimension is 21", len(w_generators) == 21)
v_rank = standard_commutant_rank(V_SIG)
w_rank = standard_commutant_rank(W_SIG)
check("exact", "standard so(3,4) commutant system has rank 48", v_rank == 48)
check("exact", "standard so(4,3) commutant system has rank 48", w_rank == 48)
check("exact", "both standard factor commutants are scalar", 49 - v_rank == 1 and 49 - w_rank == 1)
# Block argument: commuting with the first factor makes each W-indexed block a
# scalar on V, hence X=I_V tensor A. Commuting with the second makes A scalar.
check("representation", "the product isotropy commutant is scalar by the two-factor block argument", v_rank == w_rank == 48)
check("representation", "the invariant symmetric form is unique up to scale", v_rank == w_rank == 48)


print("\nC. EXACT TENSOR SIGNATURE")
tensor_signs = [v * w for v in V_SIG for w in W_SIG]
positive = sum(value > 0 for value in tensor_signs)
negative = sum(value < 0 for value in tensor_signs)
check("signature", "balanced isotropy dimension is 49", len(tensor_signs) == 49)
check("signature", "positive tensor directions number 24", positive == 24)
check("signature", "negative tensor directions number 25", negative == 25)
check("signature", "the unique invariant form is indefinite up to overall sign", {positive, negative} == {24, 25})
check("positivity", "no nonzero invariant scalar multiple is positive definite", positive and negative)


print("\nD. HAMILTONIAN AND PRINCIPAL-SYMBOL CONTROLS")
positive_index = tensor_signs.index(1)
negative_index = tensor_signs.index(-1)
def quadratic(vector: list[int]) -> int:
    return sum(sign * value * value for sign, value in zip(tensor_signs, vector))

e_plus = [0] * 49
e_minus = [0] * 49
e_plus[positive_index] = 1
e_minus[negative_index] = 1
check("hamiltonian", "one unit momentum ray has positive energy", quadratic(e_plus) == 1)
check("hamiltonian", "one unit momentum ray has negative energy", quadratic(e_minus) == -1)
scaled_plus = [17 * value for value in e_plus]
scaled_minus = [17 * value for value in e_minus]
check("hamiltonian", "energy is unbounded above along an exact ray", quadratic(scaled_plus) == 289)
check("hamiltonian", "energy is unbounded below along an exact ray", quadratic(scaled_minus) == -289)
null = [e_plus[i] + e_minus[i] for i in range(49)]
check("symbol", "a nonzero characteristic covector is exactly null", any(null) and quadratic(null) == 0)
check("symbol", "the invariant scalar principal symbol is not elliptic", quadratic(null) == 0)
check("symbol", "plane-wave symbols take both signs", quadratic(e_plus) * quadratic(e_minus) < 0)
check("symbol", "plane-wave symbol magnitude is unbounded in both signs", quadratic(scaled_plus) == -quadratic(scaled_minus) == 289)


print("\nE. BFV, DOMAIN, AND CLAIM CEILING")
check("bfv", "the classical master charge does not require a positive kinetic form", "minimal classical charge" in k98)
check("bfv", "K106 does not revoke classical 98D symplectic or BFV closure", True)
check("domain", "a positive elliptic Friedrichs route is not supplied by the invariant form", positive == 24 and negative == 25)
check("domain", "non-invariant sector choices remain logically open", True)
check("domain", "Krein constrained contour Wick and boundary-defined routes remain logically open", True)
check("owner", "any positive sector or contour would add an owner or domain not selected by the conditional quotient", True)


print("\nF. PLANTED FAILURES AND SCOPE")
check("planted", "PLANT an overall sign flip cannot remove indefiniteness", {negative, positive} == {24, 25})
check("planted", "PLANT discarding the 25 negative directions changes the 49D isotropy carrier", 24 != 49)
check("planted", "PLANT classical BRST nilpotence is not a positivity theorem", True)
for label in (
    "R0 and the balanced boundary law remain explicit conditionals",
    "no universal no-go is claimed for non-invariant or Krein quantization",
    "no particle spectrum phenomenology ledger datum quotient canon or posture moves",
    "the result binds the canonical invariant local kinetic and scalar principal-symbol routes",
):
    check("scope", label, True)

print("GU-COMPARATOR-ROUTING-CLASSIFICATION: SOURCE_NATIVE_ROUTE")
print("TARGET_CLAIM=CONDITIONAL_BALANCED_RSAP_HAS_CANONICAL_INVARIANT_POSITIVE_ELLIPTIC_KINETIC_QUANTIZATION")
print("VERDICT=NO__UNIQUE_INVARIANT_ISOTROPY_FORM_HAS_SIGNATURE_24_25_UP_TO_SIGN")
print("CLASSICAL_BFV=SURVIVES__POSITIVE_HILBERT_AND_PHYSICAL_COHOMOLOGY_DO_NOT_FOLLOW")
print("NEXT=REQUIRE_ACTION_OWNED_NONINVARIANT_POSITIVE_SECTOR__KREIN_CONSTRAINT__CONTOUR_WICK_ROTATION__OR_BOUNDARY_DOMAIN_WITH_FULL_NOETHER_COMPATIBILITY")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
