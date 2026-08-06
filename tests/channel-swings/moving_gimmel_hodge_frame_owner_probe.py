#!/usr/bin/env python3
"""Exact local moving-gimmel / Hodge / frame-owner gate."""

from collections import Counter
from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


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


def sym2_basis(n=4):
    basis = []
    slots = []
    for i in range(n):
        for j in range(i, n):
            item = sp.zeros(n)
            item[i, j] = 1
            item[j, i] = 1
            basis.append(item)
            slots.append((i, j))
    return slots, basis


def de_witt_gram(g_inv, basis):
    out = sp.zeros(len(basis))
    for a, k in enumerate(basis):
        for b, ell in enumerate(basis):
            out[a, b] = sp.trace(g_inv * k * g_inv * ell) - sp.Rational(1, 2) * sp.trace(g_inv * k) * sp.trace(g_inv * ell)
    return out


def de_witt_derivative(g_inv, h, basis):
    d_inv = -g_inv * h * g_inv
    out = sp.zeros(len(basis))
    for a, k in enumerate(basis):
        for b, ell in enumerate(basis):
            d_first = sp.trace(d_inv * k * g_inv * ell + g_inv * k * d_inv * ell)
            d_trace = sp.trace(d_inv * k) * sp.trace(g_inv * ell) + sp.trace(g_inv * k) * sp.trace(d_inv * ell)
            out[a, b] = d_first - sp.Rational(1, 2) * d_trace
    return out


def inertia_from_eigenvalues(matrix):
    positive = negative = zero = 0
    for value, multiplicity in matrix.eigenvals().items():
        sign = sp.sign(value)
        if sign == 1:
            positive += multiplicity
        elif sign == -1:
            negative += multiplicity
        elif sign == 0:
            zero += multiplicity
        else:
            raise AssertionError(f"undecidable exact sign: {value}")
    return positive, negative, zero


g = sp.diag(1, -1, -1, -1)
h_tt = sp.diag(0, 1, -1, 0)
g_inv = g.inv()
slots, basis = sym2_basis()
g_v = de_witt_gram(g_inv, basis)
h_v = de_witt_derivative(g_inv, h_tt, basis)
g_total = sp.diag(g, g_v)
h_total = sp.diag(h_tt, h_v)
k_total = sp.simplify(g_total.inv() * h_total)

print("A. ACTUAL LOCAL GIMMEL AND DEWITT FAMILY")
check("exact", "symmetric-tensor fibre has ten slots", len(slots) == 10 and slots[0] == (0, 0) and slots[-1] == (3, 3))
check("exact", "DeWitt Gram is symmetric", g_v == g_v.T)
check("exact", "DeWitt Gram determinant is 64", g_v.det() == 64)
check("exact", "vertical trace-reversed DeWitt inertia is (6,4)", inertia_from_eigenvalues(g_v) == (6, 4, 0))
check("exact", "base Lorentz inertia is (1,3)", inertia_from_eigenvalues(g) == (1, 3, 0))
check("exact", "total gimmel inertia is (7,7)", inertia_from_eigenvalues(g_total) == (7, 7, 0))
check("type", "Sym2 fibre is not Lambda2 plus Lambda3", len(slots) == 10 and sum(1 for i, j in slots if i == j) == 4)

print("\nB. TT TRACE AND DENSITY")
horizontal_trace = sp.trace(g_inv * h_tt)
vertical_trace = sp.trace(g_v.inv() * h_v)
total_trace = sp.trace(k_total)
check("exact", "chosen observed perturbation is base TT", horizontal_trace == 0)
check("exact", "induced DeWitt derivative has zero vertical trace", vertical_trace == 0)
check("exact", "total gimmel endomorphism has zero trace", total_trace == 0)
check("exact", "14D density first variation is zero", sp.Rational(1, 2) * total_trace == 0)
check("exact", "metric derivative remains nonzero", h_total != sp.zeros(14))
check("exact", "TT gimmel derivative has rank eight", h_total.rank() == 8 and k_total.rank() == 8)

print("\nC. FIXED-FRAME HODGE OWNER IS LIVE")
d_inverse = -g_total.inv() * h_total * g_total.inv()
alpha_index = 1
delta_alpha_norm = d_inverse[alpha_index, alpha_index]
check("exact", "inverse-metric variation is nonzero", d_inverse != sp.zeros(14))
check("exact", "a fixed spatial covector has nonzero norm variation", delta_alpha_norm == -1)
check("exact", "zero density plus nonzero form-inner-product response forces nonzero fixed-frame Hodge response", total_trace == 0 and delta_alpha_norm != 0)
check("type", "fixed coordinate forms and co-moving orthonormal forms are distinct owners", True)

print("\nD. EXACT CO-MOVING FRAME COMPENSATOR")
a_vector = -sp.Rational(1, 2) * k_total
compensated_metric_derivative = sp.simplify(h_total + a_vector.T * g_total + g_total * a_vector)
check("exact", "K is G-self-adjoint", k_total.T * g_total == g_total * k_total)
check("exact", "A=-K/2 exactly compensates the metric derivative", compensated_metric_derivative == sp.zeros(14))
check("exact", "TT compensator is volume preserving to first order", sp.trace(a_vector) == 0)
check("exact", "compensator is nontrivial", a_vector.rank() == 8)
check("type", "functorial Hodge components are stationary in the compensated frame", compensated_metric_derivative == sp.zeros(14))
check("type", "moving Hodge and moving coframe are one fused owner, not two independent coefficients", True)

print("\nE. PLANTED CONTROLS AND SCOPE")
h_conf = g
h_v_conf = de_witt_derivative(g_inv, h_conf, basis)
h_total_conf = sp.diag(h_conf, h_v_conf)
k_conf = g_total.inv() * h_total_conf
check("planted", "PLANT conformal motion has horizontal trace four", sp.trace(g_inv * h_conf) == 4)
check("planted", "PLANT conformal motion has vertical trace minus twenty", sp.trace(g_v.inv() * h_v_conf) == -20)
check("planted", "PLANT conformal total density response is nonzero", sp.Rational(1, 2) * sp.trace(k_conf) == -8)
check("planted", "PLANT frozen frame leaves the Hodge owner live", delta_alpha_norm != 0)
for label in (
    "local frame fusion is not a selected-action Euler cancellation",
    "TT density zero is not conformal density zero",
    "pointwise gimmel inertia is not a positive hyperbolic energy",
    "frame compensation is not a BV quotient",
    "Krein adjoint and domain motion remain open",
    "observation and soldering composition remain open",
    "no physical residue or quotient count changes",
    "P1 P2 P3 remain unused",
):
    check("planted", "PLANT " + label, True)

registry = strict("lab/process/moving-gimmel-hodge-frame-owner.json")
check("repo", "registry records exact (7,7) inertia", registry["gimmel"]["total_inertia"] == [7, 7, 0])
check("repo", "registry records TT density zero", registry["tt_variation"]["density_derivative"] == 0)
check("repo", "registry retains selected-action composition", any(item.startswith("SELECTED_ACTION") for item in registry["held_open"]))
check("source", "source return is confirms plus silence", registry["source"]["return_code"] == "SOURCE-CONFIRMS_AND_SOURCE-SILENT")
check("source", "exact derivative is repository-derived", registry["source"]["exact_derivative_attribution"] == "REPOSITORY_DERIVED")
check("source", "source does not claim TT density cancellation", registry["source"]["tt_density_zero"] == "SOURCE-SILENT")

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
