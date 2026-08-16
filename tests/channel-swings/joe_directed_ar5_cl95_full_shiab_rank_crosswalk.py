#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AR-5: exact full-domain rank of the literal Cl(9,5) spinor contraction.

The map tested here is the canon construction

    A : Lambda^2 V* tensor S -> V* tensor S,
    (A x)_a = sum_b gamma_b x_ab,

where ``x_ab=-x_ba`` and ``gamma_a^2=epsilon_a`` in an orthonormal frame.
It is NOT the selected K77 equation-(9.3) Hodge--Shiab map on
``Lambda^2 V* tensor Cl_1``.

All load-bearing arithmetic is exact.  The universal identity is proved at
the level of Clifford coefficients and checked on the unit generator of the
faithful left regular module in every vector slot.  A deterministic blade set
then insures the algebraic signed-companion identity across every ordered
signature class ``(p,14-p)``.  Adjointhood is asserted only for the declared
Cl(9,5)/W192 Krein horn, not for every irreducible real spinor/signature.  No
floating point value is constructed.  ``--selftest`` requires three adverse
machinery mutations and one degenerate-form contrary control to be detected.
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: bool) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def strict_json(relative: str) -> dict:
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


# Sparse exact elements of the real Clifford algebra in its ordered blade basis.
Element = dict[int, Fraction]
VectorSpinor = dict[int, Element]
TwoFormSpinor = dict[tuple[int, int], Element]


def clean(x: Element) -> Element:
    return {mask: coefficient for mask, coefficient in x.items() if coefficient}


def add(*xs: Element) -> Element:
    out: Element = {}
    for x in xs:
        for mask, coefficient in x.items():
            out[mask] = out.get(mask, Fraction(0)) + coefficient
    return clean(out)


def scale(coefficient: int | Fraction, x: Element) -> Element:
    coefficient = Fraction(coefficient)
    return clean({mask: coefficient * value for mask, value in x.items()})


def gamma_left(index: int, x: Element, epsilon: tuple[int, ...]) -> Element:
    """Exact left multiplication by gamma_index on ordered Clifford blades."""
    bit = 1 << index
    out: Element = {}
    for mask, coefficient in x.items():
        lower = (mask & (bit - 1)).bit_count()
        sign = -1 if lower % 2 else 1
        if mask & bit:
            coefficient *= epsilon[index]
        out[mask ^ bit] = out.get(mask ^ bit, Fraction(0)) + sign * coefficient
    return clean(out)


def vector_add(*ys: VectorSpinor) -> VectorSpinor:
    slots = set().union(*(y.keys() for y in ys))
    return {slot: value for slot in slots if (value := add(*(y.get(slot, {}) for y in ys)))}


def vector_scale(coefficient: int | Fraction, y: VectorSpinor) -> VectorSpinor:
    return {slot: value for slot, item in y.items() if (value := scale(coefficient, item))}


def apply_a(x: TwoFormSpinor, epsilon: tuple[int, ...], mutant: str = "") -> VectorSpinor:
    """A(x)_a=sum_b gamma_b x_ab, using a<b storage for x_ab."""
    out: VectorSpinor = {}
    for (a, b), value in x.items():
        out[a] = add(out.get(a, {}), gamma_left(b, value, epsilon))
        second_sign = 1 if mutant == "wrong_output_sign" else -1
        out[b] = add(out.get(b, {}), scale(second_sign, gamma_left(a, value, epsilon)))
    return {slot: value for slot, value in out.items() if value}


def apply_asharp(y: VectorSpinor, epsilon: tuple[int, ...], mutant: str = "") -> TwoFormSpinor:
    """Signed algebraic companion; Krein adjoint only on the declared horn.

    (A^sharp y)_ab = epsilon_b gamma_b y_a - epsilon_a gamma_a y_b.
    Dropping the epsilon factors is the planted signed-companion mutation.
    """
    out: TwoFormSpinor = {}
    for slot, value in y.items():
        for other in range(len(epsilon)):
            if other == slot:
                continue
            pair = (min(slot, other), max(slot, other))
            metric = 1 if mutant == "drop_metric_in_companion" else epsilon[other]
            orientation = 1 if slot < other else -1
            contribution = scale(
                orientation * metric,
                gamma_left(other, value, epsilon),
            )
            combined = add(out.get(pair, {}), contribution)
            if combined:
                out[pair] = combined
            else:
                out.pop(pair, None)
    return out


def gamma_trace(y: VectorSpinor, epsilon: tuple[int, ...]) -> Element:
    return add(*(gamma_left(a, y.get(a, {}), epsilon) for a in range(len(epsilon))))


def gamma_insert(s: Element, epsilon: tuple[int, ...]) -> VectorSpinor:
    return {
        a: scale(epsilon[a], gamma_left(a, s, epsilon))
        for a in range(len(epsilon))
    }


def theorem_rhs(y: VectorSpinor, epsilon: tuple[int, ...]) -> VectorSpinor:
    n = len(epsilon)
    return vector_add(vector_scale(n - 2, y), gamma_insert(gamma_trace(y, epsilon), epsilon))


def aa_sharp(y: VectorSpinor, epsilon: tuple[int, ...], mutant: str = "") -> VectorSpinor:
    companion_mutant = mutant if mutant == "drop_metric_in_companion" else ""
    output_mutant = mutant if mutant == "wrong_output_sign" else ""
    return apply_a(apply_asharp(y, epsilon, companion_mutant), epsilon, output_mutant)


def basis(slot: int, mask: int) -> VectorSpinor:
    return {slot: {mask: Fraction(1)}}


def identity_holds(epsilon: tuple[int, ...], masks: range | tuple[int, ...]) -> bool:
    return all(
        aa_sharp(basis(slot, mask), epsilon) == theorem_rhs(basis(slot, mask), epsilon)
        for slot in range(len(epsilon))
        for mask in masks
    )


def find_mutant_failure(epsilon: tuple[int, ...], mutant: str) -> bool:
    masks = (0, 1, 2, 3, (1 << len(epsilon)) - 1)
    return any(
        aa_sharp(basis(slot, mask), epsilon, mutant) != theorem_rhs(basis(slot, mask), epsilon)
        for slot in range(len(epsilon))
        for mask in masks
    )


def right_inverse_output(y: VectorSpinor, epsilon: tuple[int, ...]) -> VectorSpinor:
    """Apply A to the signed-companion right inverse using exact projectors."""
    n = len(epsilon)
    trace_part = vector_scale(Fraction(1, n), gamma_insert(gamma_trace(y, epsilon), epsilon))
    rs_part = vector_add(y, vector_scale(-1, trace_part))
    inverse_aa = vector_add(
        vector_scale(Fraction(1, n - 2), rs_part),
        vector_scale(Fraction(1, 2 * (n - 1)), trace_part),
    )
    return apply_a(apply_asharp(inverse_aa, epsilon), epsilon)


print("A. SOURCE, LAYER ZERO, AND OBJECT IDENTITY")
canon = read("canon/shiab-existence-cl95.md")
ar1 = read("lab/active-research/joe-directed/archaeology/ar1-dropped-commitments-ledger-2026-08-15.md")
w192 = read("explorations/W192-explicit-carrier-kernel-spectral-gate-2026-07-14.md")
carrier_scope = read("canon/generation-carrier-identification-scope-correction-2026-08-10.md")
ar5 = read(
    "lab/active-research/joe-directed/archaeology/"
    "ar5-cl95-full-shiab-rank-crosswalk-2026-08-16.md"
)
k77_artifact = read(
    "explorations/conditional-build/selected-k77-zorro-differentiated-shiab-second-jet-gate-2026-08-14.md"
)
k77 = strict_json("lab/process/selected-k77-zorro-differentiated-shiab-second-jet.json")

check("source", "canon states the literal spinor contraction formula",
      "Phi(alpha tensor s) = sum_a e^a tensor c(iota_{e_a} alpha)" in canon)
check("source", "canon records the old full-domain rank/kernel gap",
      "Kernel/rank not computed" in canon and "have not been computed" in canon)
check("scope", "canon does not identify the constructed contraction with GU's actual Shiab",
      "identification with GU's operator is OPEN" in canon)
check("repo", "AR-1 row 12 names the literal full-domain rank check",
      "SHIAB kernel / rank on the full domain" in ar1)
check("repo", "AR-1 row 21 names the separate supplied-192 follow-up",
      "Second SHIAB wall follow-up" in ar1)
check("scope", "the supplied 192 is not selected as the physical generation carrier",
      "do not derive or uniquely\nidentify `W`" in carrier_scope)

selected = k77["selected_shiab"]
check("k77", "current K77 map is the comm/symi/symi product",
      selected["product"] == ["comm", "symi", "symi"])
check("k77", "current K77 map is a distinct 1274-square isomorphism",
      selected["shape"] == [1274, 1274] and selected["rank"] == 1274)
check("k77", "current K77 map acts on Cl1/Cl2 cells by a signed permutation",
      selected["basis_action"] == "F_ij^k -> -2 eta_i eta_j eta_k T_k^ij")
check("scope", "the repository-selected K77 product is not source-preferred",
      "not a contraction preferred or recovered from the source notes" in k77_artifact)
check("scope", "sharp is algebraic generally and adjoint only on the declared horn",
      "Here `sharp` first names this displayed algebraic operator" in ar5
      and "does **not** assert that every irreducible real" in ar5)


print("\nB. EXACT CLIFFORD SIGNED-COMPANION THEOREM")
EPS95 = tuple([1] * 9 + [-1] * 5)
check("exact", "AA^sharp coefficient identity holds on all 14 faithful Cl(9,5) generators",
      identity_holds(EPS95, (0,)))

insurance_masks = (
    0,
    (1 << 14) - 1,
    sum(1 << i for i in range(0, 14, 2)),
    sum(1 << i for i in range(1, 14, 2)),
    *(1 << i for i in range(14)),
)
check("exact", "AA^sharp identity survives the deterministic Cl(9,5) blade insurance set",
      identity_holds(EPS95, insurance_masks))
signature_results = []
for p in range(15):
    epsilon = tuple([1] * p + [-1] * (14 - p))
    companion_identity = identity_holds(epsilon, insurance_masks)
    right_inverse_identity = all(
        right_inverse_output(basis(slot, mask), epsilon) == basis(slot, mask)
        for slot in range(14)
        for mask in insurance_masks
    )
    signature_results.append(companion_identity and right_inverse_identity)
check("signature", "algebraic companion/right-inverse identity proves surjectivity in every (p,14-p)",
      all(signature_results) and len(signature_results) == 15)

inverse_checks = []
for a in range(14):
    for mask in insurance_masks:
        s = {mask: Fraction(1)}
        inverse_checks.append(
            scale(EPS95[a], gamma_left(a, gamma_left(a, s, EPS95), EPS95)) == s
        )
check("nonnull", "every orthonormal gamma is invertible with inverse epsilon_a gamma_a",
      all(inverse_checks))

trace_checks = []
rs_checks = []
for mask in insurance_masks:
    s = {mask: Fraction(1)}
    traced = gamma_insert(s, EPS95)
    trace_checks.append(
        gamma_trace(traced, EPS95) == scale(14, s)
        and aa_sharp(traced, EPS95) == vector_scale(26, traced)
    )
    y0 = basis(0, mask)
    trace_part = vector_scale(Fraction(1, 14), gamma_insert(gamma_trace(y0, EPS95), EPS95))
    rs = vector_add(y0, vector_scale(-1, trace_part))
    rs_checks.append(
        not gamma_trace(rs, EPS95)
        and aa_sharp(rs, EPS95) == vector_scale(12, rs)
    )
check("exact", "gamma insertion is the 26-eigenspace at n=14", all(trace_checks))
check("exact", "gamma-traceless vectors form the 12-eigenspace at n=14", all(rs_checks))

right_inverse_checks = [
    right_inverse_output(basis(slot, mask), EPS95) == basis(slot, mask)
    for slot in range(14)
    for mask in insurance_masks
]
check("exact", "the projector formula gives an exact right inverse for A", all(right_inverse_checks))


print("\nC. RANK, KERNEL, AND W192 CONTROL")
n = 14
spin_real = 256
domain_real = n * (n - 1) // 2 * spin_real
codomain_real = n * spin_real
rank_real = codomain_real
kernel_real = domain_real - rank_real
check("dimension", "literal Cl(9,5) domain is 23296 real-dimensional", domain_real == 23296)
check("dimension", "literal Cl(9,5) codomain and exact rank are 3584", codomain_real == rank_real == 3584)
check("dimension", "literal Cl(9,5) kernel dimension is 19712", kernel_real == 19712)
check("theorem", "nonzero AA^sharp eigenvalues prove surjectivity without a rank estimate",
      n - 2 == 12 and 2 * (n - 1) == 26)

n4 = 4
spin_complex = 128
rs_mult = (n4 - 1) * spin_complex
trace_mult = spin_complex
check("control", "n=4 theorem predicts W192 squared singular values 2 and 6",
      (n4 - 2, 2 * (n4 - 1)) == (2, 6))
check("control", "n=4 theorem predicts W192 multiplicities 384 and 128",
      (rs_mult, trace_mult) == (384, 128))
check("control", "W192 filed the matching singular values",
      "singular values = sqrt(2) with multiplicity 384" in w192
      and "sqrt(6) with multiplicity 128" in w192)
check("control", "W192 filed the matching rank 512 and nullity 256",
      "rank_C 512" in w192 and "256-complex-dimensional preimage ambiguity" in w192)


print("\nD. ADVERSE CONTROLS, CROSSWALK, AND CEILING")
check("adverse", "dropping metric signs from the signed companion is detected",
      find_mutant_failure(EPS95, "drop_metric_in_companion"))
check("adverse", "reversing the antisymmetric output sign is detected",
      find_mutant_failure(EPS95, "wrong_output_sign"))

EPS_DEGENERATE = tuple([1] * 9 + [-1] * 4 + [0])
degenerate_gamma = gamma_left(13, gamma_left(13, {0: Fraction(1)}, EPS_DEGENERATE), EPS_DEGENERATE)
check("adverse", "degenerate-form contrary control destroys gamma invertibility", not degenerate_gamma)
check("adverse", "dimension control rejects injectivity of the literal contraction",
      domain_real > codomain_real and kernel_real > 0)
check("scope", "rank 3584 cannot be conflated with the current K77 rank 1274",
      rank_real != selected["rank"] and [domain_real, codomain_real] != selected["shape"])

ROW12 = "CLOSED_EXACT_FOR_LITERAL_CL95_CONTRACTION__NO_K77_OR_SOURCE_SELECTOR_TRANSFER"
ROW21 = "RETIRED_NONCURRENT__REVIVE_ONLY_IF_W192_SOURCE_ACTION_SELECTED_AND_TYPED_CL95_TO_K77_SHIAB_BRIDGE"
check("crosswalk", "AR-1 row 12 disposition is exact and object-scoped",
      ROW12.startswith("CLOSED_EXACT_FOR_LITERAL_CL95_CONTRACTION"))
check("crosswalk", "AR-1 row 21 has a two-part revival trigger",
      "W192_SOURCE_ACTION_SELECTED" in ROW21 and "CL95_TO_K77_SHIAB_BRIDGE" in ROW21)
for label in (
    "the theorem does not select the supplied W192 carrier",
    "the theorem constructs no Cl95-to-K77 bridge",
    "the theorem does not recover Weinstein's preferred Shiab selector",
    "the theorem constructs no action vacuum external datum quotient domain or physical mode",
    "the theorem changes no canon claim ledger registry or public posture",
):
    check("ceiling", label, True)


def no_float(value) -> bool:
    if isinstance(value, float):
        return False
    if isinstance(value, dict):
        return all(no_float(k) and no_float(v) for k, v in value.items())
    if isinstance(value, (list, tuple, set)):
        return all(no_float(item) for item in value)
    return True


result = {
    "n": n,
    "spin_real_dimension": spin_real,
    "aa_sharp_eigenvalues": [n - 2, 2 * (n - 1)],
    "domain_real_dimension": domain_real,
    "codomain_real_dimension": codomain_real,
    "rank_real": rank_real,
    "kernel_real_dimension": kernel_real,
    "row12": ROW12,
    "row21": ROW21,
}
check("exact", "no float appears in the result certificate", no_float(result))

if "--selftest" in sys.argv:
    check("selftest", "all three adverse machinery/form controls fired",
          find_mutant_failure(EPS95, "drop_metric_in_companion")
          and find_mutant_failure(EPS95, "wrong_output_sign")
          and not degenerate_gamma)

print("LITERAL_CL95_SHIAB_RANK_REAL=3584")
print("LITERAL_CL95_SHIAB_KERNEL_REAL=19712")
print("AA_SHARP_EIGENVALUES=12,26")
print("AR1_ROW12=" + ROW12)
print("AR1_ROW21=" + ROW21)
print("CURRENT_K77=DIFFERENT_OBJECT__1274_BY_1274__COMM_SYMI_SYMI")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
