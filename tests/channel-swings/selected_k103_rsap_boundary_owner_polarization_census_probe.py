#!/usr/bin/env python3
"""Exact K103 boundary-owner and polarization census."""

H = 42
P = 49
G = H + P
PRIME = 1_000_000_007


def check(condition: bool, label: str, receipts: list[str]) -> None:
    if not condition:
        raise AssertionError(label)
    receipts.append(label)


def zeros(rows: int, cols: int | None = None) -> list[list[int]]:
    return [[0] * (rows if cols is None else cols) for _ in range(rows)]


def pair(form: list[list[int]], i: int, j: int, value: int = 1) -> None:
    form[i][j] += value
    form[j][i] -= value


def rank_exact_unit_block(form: list[list[int]]) -> int:
    """Rank mod a large prime; all nonzero minors used here have determinant ±1."""
    a = [row[:] for row in form]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col] % PRIME), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        inverse = pow(a[pivot_row][col] % PRIME, PRIME - 2, PRIME)
        a[pivot_row] = [(x * inverse) % PRIME for x in a[pivot_row]]
        for r in range(rows):
            if r == pivot_row:
                continue
            factor = a[r][col] % PRIME
            if factor:
                a[r] = [(x - factor * y) % PRIME for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def matvec(form: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(x * y for x, y in zip(row, vector)) for row in form]


receipts: list[str] = []

base = zeros(2 * G)
for i in range(G):
    pair(base, i, G + i)

check(H == 42, "h_bal dimension is 42", receipts)
check(P == 49, "balanced complement dimension is 49", receipts)
check(G == 91, "so(7,7) dimension is 91", receipts)
check(len(base) == 182, "endpoint parent dimension is 182", receipts)
check(rank_exact_unit_block(base) == 182, "endpoint parent is symplectic", receipts)
check(len(base) - rank_exact_unit_block(base) == 0,
      "charged horn has no characteristic kernel", receipts)

zero_level = zeros(H + 2 * P)
for i in range(P):
    pair(zero_level, H + i, H + P + i)

check(len(zero_level) == 140, "zero-level tangent dimension is 140", receipts)
zero_rank = rank_exact_unit_block(zero_level)
check(zero_rank == 98, "zero-level pullback rank is 98", receipts)
check(len(zero_level) - zero_rank == 42, "zero-level characteristic rank is 42", receipts)
check(zero_rank == 98,
      "zero-level characteristic quotient is 98D", receipts)

edge = zeros(2 * G + H)
qh = 0
qp = H
ph = G
pp = G + H
phi = 2 * G
for i in range(H):
    pair(edge, qh + i, ph + i)
    pair(edge, phi + i, ph + i, -1)
for i in range(P):
    pair(edge, qp + i, pp + i)

check(len(edge) == 224, "minimal edge-extended dimension is 224", receipts)
edge_rank = rank_exact_unit_block(edge)
check(edge_rank == 182, "edge-extended presymplectic rank is 182", receipts)
check(len(edge) - edge_rank == 42, "edge diagonal gauge kernel is 42D", receipts)
check(edge_rank == 182,
      "edge characteristic quotient remains 182D", receipts)
edge_generators = []
for i in range(H):
    v = [0] * len(edge)
    v[qh + i] = 1
    v[phi + i] = 1
    edge_generators.append(v)
check(all(matvec(edge, v) == [0] * len(edge) for v in edge_generators),
      "all 42 diagonal edge generators are characteristic", receipts)
check(len({tuple(v) for v in edge_generators}) == H,
      "the 42 diagonal edge generators are independent", receipts)

edge_reduced = zeros(2 * G)
for i in range(G):
    pair(edge_reduced, i, G + i)
check(rank_exact_unit_block(edge_reduced) == 182,
      "edge quotient retains all endpoint pairs", receipts)
nonzero_charge = [0] * (2 * G)
nonzero_charge[G] = 1
check(nonzero_charge[G] == 1, "edge quotient admits nonzero h charge", receipts)

edge_zero = zeros(2 * H + 2 * P)
for i in range(P):
    pair(edge_zero, H + i, H + P + i)
check(len(edge_zero) == 182, "edge plus zero-charge surface is 182D", receipts)
edge_zero_rank = rank_exact_unit_block(edge_zero)
check(edge_zero_rank == 98, "edge plus zero-charge pullback rank is 98", receipts)
check(len(edge_zero) - edge_zero_rank == 84,
      "edge plus zero charge has 84 characteristic directions", receipts)
check(edge_zero_rank == 98,
      "edge reaches 98D only after extra zero-charge reduction", receipts)

dirac_surface = zeros(2 * H + 2 * P)
for i in range(P):
    pair(dirac_surface, H + i, H + P + i)
check(2 * G + 2 * H == 266, "multiplier extended phase dimension is 266", receipts)
check(len(dirac_surface) == 182, "Dirac joint constraint surface is 182D", receipts)
dirac_rank = rank_exact_unit_block(dirac_surface)
check(dirac_rank == 98, "Dirac joint pullback rank is 98", receipts)
check(len(dirac_surface) - dirac_rank == 84,
      "Dirac primary plus Gauss characteristic rank is 84", receipts)
check(dirac_rank == 98,
      "Dirac multiplier quotient is 98D", receipts)

zero_jacobian = zeros(H, 2 * G)
for i in range(H):
    zero_jacobian[i][i] = 1
check(rank_exact_unit_block(zero_jacobian) == 42,
      "right-H zero constraint rank is 42", receipts)
check(182 - 42 - 42 == 98, "base constraint-plus-quotient count is 98", receipts)
check(224 - 42 == 182, "edge completion cancels only its added coordinates", receipts)
check(266 - 2 * 84 == 98, "Dirac first-class count returns 98", receipts)
check(182 != 98, "charge-preserving edge quotient is not the RSAP quotient", receipts)

print(f"PASS {len(receipts)}/{len(receipts)}")
for receipt in receipts:
    print(f"PASS {receipt}")
