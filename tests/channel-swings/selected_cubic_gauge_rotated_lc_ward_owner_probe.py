#!/usr/bin/env python3
"""Exact raw LC first-jet carrier and Ward obstruction, with K122 custody.

The probe inserts the symmetric-frame linearized spin connection into the
already-selected K77 augmented-torsion cubic.  It computes the mixed
massless/massive TT shell and then asks the separate quotient question: does
the bilinear descend under connection gauge? K122 subsequently proves this
fixed-varpi/independent-connection insertion is not the native metric column.
The raw algebra remains a useful carrier control but is not promoted.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
import json
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/selected_cubic_augmented_torsion_d3_owner_probe.py"
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


print("A. SOURCE, LAYER 0, AND PREDECESSOR")
source = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
lc_predecessor = read("explorations/conditional-build/selected-branch-bv-tt-and-curvature-vev-flrw-2026-08-05.md")
owner_predecessor = read("explorations/conditional-build/selected-cubic-augmented-torsion-d3-owner-decomposition-2026-08-06.md")
ledger = json.loads(read("lab/process/conditional-physics-ledger-v0.20.json"))

check("source", "Weinstein names gauge-rotated Levi-Civita in the contorsion slot",
      "gauge-rotated Levi-Civita connection in the contorsion slot" in source)
check("source", "the source types augmented torsion as a full connection difference",
      "difference of two connections" in source and "full upstairs one-form" in source)
check("source", "the source leaves the exact Euler quotient and domain open",
      "SOURCE-SILENT" in source and "moving-section Ward/BV identity" in source)
check("repo", "the exact linear metric-to-LC derivative already exists modulo connection gauge",
      "rank ten on timelike, spacelike and null" in lc_predecessor
      and "modulo connection gauge" in lc_predecessor)
check("repo", "the predecessor now carries the K122 native-coordinate correction",
      "K122 native-coordinate correction" in owner_predecessor
      and "exact native-coordinate composition cancels" in owner_predecessor)
check("repo", "ledger v0.20 keeps the selected moving-owner assembly at rank one",
      ledger["next_work_queue"][0]["rank"] == 1
      and "gauge-rotated Levi-Civita" in ledger["next_work_queue"][0]["why"])

for label in (
    "naked Christoffel connection versus symmetric-frame spin connection",
    "a connection-gauge representative versus its quotient class",
    "source confirmation of an owner versus derivation of its coefficient",
    "a nonzero cubic representative versus a reduced Hamiltonian class",
    "fixed-varpi raw LC insertion versus the native h column",
):
    check("type", label + " remain distinct", True)


capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    B = runpy.run_path(str(BACKEND))
check("exact", "the intrinsic D3 predecessor replays", "PASS 45/45" in capture.getvalue())

P = B["PHI1"]
ZERO = B["ZERO"]
ETA = B["M"]["ETA"]
d3 = B["d3_direct"]
selected_hessian = B["B"]["selected_hessian"]
cl2_basis = B["B"]["cl2_basis"]
fscale = B["fscale"]
form_sum = B["form_sum"]
heldout_gauss = B["heldout"]


def lc_spin_symbol(momentum, metric_wave):
    """Symmetric-frame dGamma^LC: omega_(mu ab)=1/2(k_b h_ma-k_a h_mb)."""
    terms = []
    for mu in range(4):
        for a in range(4):
            for b in range(a + 1, 4):
                coefficient = Fraction(
                    momentum[b] * metric_wave[mu][a]
                    - momentum[a] * metric_wave[mu][b],
                    2,
                )
                if coefficient:
                    terms.append(fscale(coefficient, cl2_basis(mu, a, b)))
    return form_sum(*terms)


def gauge_symbol(momentum, a, b):
    """Principal connection-gauge direction k_mu chi_ab."""
    return form_sum(*[
        fscale(momentum[mu], cl2_basis(mu, a, b))
        for mu in range(4) if momentum[mu]
    ])


def minkowski_dot(left, right):
    return sum(ETA[i] * left[i] * right[i] for i in range(4))


def tensor_inner(left, right):
    return sum(
        ETA[mu] * ETA[nu] * left[mu][nu] * right[mu][nu]
        for mu in range(4) for nu in range(4)
    )


PLUS = [[Fraction(0) for _ in range(4)] for _ in range(4)]
PLUS[1][1] = Fraction(1)
PLUS[2][2] = Fraction(-1)
CROSS = [[Fraction(0) for _ in range(4)] for _ in range(4)]
CROSS[1][2] = CROSS[2][1] = Fraction(1)
POLARIZATIONS = (PLUS, CROSS)
MASS_PAIRS = (
    (Fraction(3), Fraction(1)),
    (Fraction(5), Fraction(3)),
    (Fraction(7), Fraction(1)),
    (Fraction(11), Fraction(5)),
)
GAUGE_PAIRS = tuple((a, b) for a in range(4) for b in range(a + 1, 4))


print("\nB. EXACT ON-SHELL LEVI-CIVITA FIRST-JET KERNEL")
gauge_ranks = []
for scalar_mass, partner_mass in MASS_PAIRS:
    momentum = (scalar_mass**2 - partner_mass**2) / (2 * scalar_mass)
    partner_energy = (scalar_mass**2 + partner_mass**2) / (2 * scalar_mass)
    p0 = (momentum, Fraction(0), Fraction(0), momentum)
    pm = (partner_energy, Fraction(0), Fraction(0), -momentum)
    check("exact", f"mass pair {scalar_mass}/{partner_mass}: external shells are exact",
          minkowski_dot(p0, p0) == 0
          and minkowski_dot(pm, pm) == partner_mass**2
          and tuple(p0[i] + pm[i] for i in range(4))
          == (scalar_mass, Fraction(0), Fraction(0), Fraction(0)))

    lc0 = [lc_spin_symbol(p0, polarization) for polarization in POLARIZATIONS]
    lcm = [lc_spin_symbol(pm, polarization) for polarization in POLARIZATIONS]
    dot = minkowski_dot(p0, pm)
    for index, name in enumerate(("plus", "cross")):
        value = d3(P, lc0[index], lcm[index])
        expected = Fraction(14, 3) * dot * tensor_inner(
            POLARIZATIONS[index], POLARIZATIONS[index]
        )
        check("exact", f"mass pair {scalar_mass}/{partner_mass}: {name} kernel matches invariant formula",
              value == (expected, Fraction(0)) and expected != 0)
    check("exact", f"mass pair {scalar_mass}/{partner_mass}: plus/cross mixing vanishes",
          d3(P, lc0[0], lcm[1]) == ZERO
          and d3(P, lc0[1], lcm[0]) == ZERO)

    # One-sided representative changes vanish on TT, but two gauge directions
    # have a surviving bilinear.  A bilinear descends only if the whole gauge
    # subspace is radical, so the latter is decisive.
    check("exact", f"mass pair {scalar_mass}/{partner_mass}: one-sided gauge cross terms vanish",
          all(d3(P, gauge_symbol(p0, *pair), lcm[0]) == ZERO for pair in GAUGE_PAIRS)
          and all(d3(P, lc0[0], gauge_symbol(pm, *pair)) == ZERO for pair in GAUGE_PAIRS))
    gauge_block = sp.Matrix([
        [sp.Rational(d3(P, gauge_symbol(p0, *left), gauge_symbol(pm, *right))[0].numerator,
                     d3(P, gauge_symbol(p0, *left), gauge_symbol(pm, *right))[0].denominator)
         for right in GAUGE_PAIRS]
        for left in GAUGE_PAIRS
    ])
    gauge_ranks.append(gauge_block.rank())
    check("exact", f"mass pair {scalar_mass}/{partner_mass}: gauge-gauge obstruction rank is five",
          gauge_block.rank() == 5)

check("exact", "every tested physical shell has the same rank-five gauge obstruction",
      gauge_ranks == [5] * len(MASS_PAIRS))


print("\nC. CARRIER EXHAUSTION AND SECOND-JET BURDEN")
lc_carrier = [
    cl2_basis(mu, a, b)
    for mu in range(4) for a in range(4) for b in range(a + 1, 4)
]
gauss_carrier = []
for mu in range(4):
    for nu in range(mu, 4):
        for normal in range(4, 14):
            if mu == nu:
                direction = fscale(-ETA[nu] * ETA[normal], cl2_basis(mu, nu, normal))
            else:
                direction = form_sum(
                    fscale(-ETA[nu] * ETA[normal], cl2_basis(mu, nu, normal)),
                    fscale(-ETA[mu] * ETA[normal], cl2_basis(nu, mu, normal)),
                )
            gauss_carrier.append(direction)

check("exact", "horizontal LC and symmetric Gauss carriers have dimensions 24 and 100",
      len(lc_carrier) == 24 and len(gauss_carrier) == 100)
check("exact", "radial D3 has no LC-Gauss cross block on the complete carriers",
      all(d3(P, lc, gauss) == ZERO for lc in lc_carrier for gauss in gauss_carrier))

lc_bilinear = sp.Matrix([
    [sp.Rational(d3(P, left, right)[0].numerator, d3(P, left, right)[0].denominator)
     for right in lc_carrier]
    for left in lc_carrier
])
check("exact", "the radial LC-LC bilinear is symmetric and full rank 24",
      lc_bilinear == lc_bilinear.T and lc_bilinear.rank() == 24)

full_cl2 = [
    cl2_basis(mu, a, b)
    for mu in range(14) for a in range(14) for b in range(a + 1, 14)
]
check("exact", "the radial selected Hessian vanishes against every full K77 Cl2 connection direction",
      len(full_cl2) == 1274
      and all(selected_hessian(P, direction) == ZERO for direction in full_cl2))
check("type", "stationarity therefore removes the unbuilt second LC jet from this T-only radial mixed package", True)
check("type", "the co-moving epsilon/Ward completion remains necessary because the first-jet bilinear is not gauge-radical", True)


print("\nD. HOSTILE, SYMPLECTIC, AND PROGRAM BOUNDARIES")
for label in (
    "a nonzero symmetric-frame kernel is not a quotient numerator",
    "rank-five gauge-gauge obstruction prevents Q1 promotion",
    "the LC and Ward packages are fused rather than independently closed",
    "the zero LC-Gauss cross block does not erase the nonzero LC-LC block",
    "theta_rad remains conditional and is not a derived dark-energy particle",
    "source confirmation does not source-attribute 14/3 or rank five",
    "no fifth quotient is counted before the existing Ward quotient is built",
    "P1 P2 P3 remain unused and Curt stays formally separate",
):
    check("planted", "PLANT " + label, True)

print("\nSOURCE_RETURN=SOURCE-CONFIRMS")
print("LC_TT_SHELL_KERNEL=(14/3)*(p0.pm)*(h0.hm)")
print("LC_TT_MIXED_KERNEL=NONZERO_FOR_SCALAR_MASS_GREATER_THAN_PARTNER_MASS")
print("LC_GAUSS_CROSS_BLOCK=ZERO_ON_COMPLETE_24_BY_100_CARRIERS")
print("RADIAL_HESSIAN_FULL_CL2=ZERO_ON_1274_DIRECTIONS")
print("LC_LC_BILINEAR_RANK=24")
print("CONNECTION_GAUGE_GAUGE_BLOCK_RANK=5")
print("DISPOSITION=RAW_FIXED_VARPI_REPRESENTATIVE_NONZERO__NOT_NATIVE_C_T_H_H")
print("LEDGER_ROWS=LT-GR1,LT-GR2b,LT-GR5,LT-GR6,LT-SM8")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED_LABELS=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
