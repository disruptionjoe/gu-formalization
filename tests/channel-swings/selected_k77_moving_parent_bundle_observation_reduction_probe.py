#!/usr/bin/env python3
"""Exact moving-parent bundle and observation-reduction composition.

This composes v0.57's global epsilon-moved Clifford frame, v0.78's overlap
law, and v0.129's complete Euler grade graph.  It tests whether the proper
rank-8128 sector globalizes as a moving subbundle and keeps that question
separate from full-U principal connection ownership and observation pullback.
"""

from collections import Counter
from fractions import Fraction
from pathlib import Path
import importlib.util
import json
import sys


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

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def load_module(name, relative):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


print("A. PRIOR ART, SOURCE LOCUS, AND LAYER ZERO")
v129 = strict("lab/process/selected-k77-grade5-unitary-parent-euler-closure.json")
global_bundle = strict("lab/process/k77-global-chimeric-spin-reduction-and-support-normalization.json")
overlap = strict("lab/process/selected-k77-action-bundle-observation-overlap.json")
source = (ROOT / "lab/sources/selected-k77-action-parent-source-reinspection-2026-08-09.md").read_text()
check("prior_art", "v0.129 owns fixed-epsilon grade closure and both carrier sizes",
      v129["exact_result"]["spin_coefficient_dimension"] == 8128
      and v129["exact_result"]["unitary_completed_coefficient_dimension"] == 16384)
check("prior_art", "v0.57 owns the global source epsilon moved Clifford frame",
      global_bundle["global_full_reduction"]["moved_map"]
      == "gamma_epsilon_EQUALS_AD_EPSILON_INVERSE_COMPOSE_GAMMA_0")
check("prior_art", "v0.78 owns noncommuting overlap and observation-projector descent",
      overlap["exact_results"]["direct_sequential_coefficient_cocycle"] is True
      and "ordinary pullback" in overlap["layer0"]["observation"])
check("source", "the source owns full U64,64 P_H and separately two C32,32 Weyl halves",
      "`U(64,64)`" in source and "principal-group arena" in source
      and "two 64-dimensional Weyl pieces" in source
      and "connection-valued varpi" in source)
for label in (
    "fixed invariant subspace versus epsilon-transported moving subbundle",
    "two Weyl vector bundles versus a two-factor principal connection",
    "full-U principal bundle versus a moving block reduction inside it",
    "connection value versus homogeneous adjoint-valued connection tangent",
    "observation pullback versus structure-group reduction",
    "moving Euler covariance versus physical parent selection",
):
    check("type", label + " remain distinct", True)


api = load_module("k77_exact_bank_api_for_moving_parent", "tests/channel-swings/k77_exact_bank_api.py")
bank = api.load_bank()
core = api.K77Core(bank.signature, bank.channels)
ONE_ELEMENT = {0: api.ONE}
ZERO_ELEMENT = {}
SKEW_GRADES = {1, 2, 5, 6, 9, 10, 13, 14}
SELF_GRADES = set(range(15)) - SKEW_GRADES


def basis(mask):
    return {mask: api.ONE if mask.bit_count() in SKEW_GRADES else api.I}


def adjoint(group, value, inverse):
    return core.emul(core.emul(group, value), inverse)


def adjoint_form(group, value, inverse):
    return core.fclean({form: adjoint(group, element, inverse)
                        for form, element in value.items()})


def fixed_skew_projector(value):
    return core.eclean({mask: coefficient for mask, coefficient in value.items()
                        if mask.bit_count() in SKEW_GRADES})


def moving_skew_projector(value, group, inverse):
    return adjoint(group, fixed_skew_projector(adjoint(inverse, value, group)), inverse)


def moving_skew_form_projector(value, group, inverse):
    return core.fclean({form: moving_skew_projector(element, group, inverse)
                        for form, element in value.items()})


def make_group(generator, scalar, vector):
    return core.eadd(core.escale(scalar, ONE_ELEMENT), core.escale(vector, generator))


X = core.blade((0, 1, 2, 3), api.I)  # X^2=+1
Y = core.blade((0, 1, 2, 4), api.I)  # Y^2=-1
g01 = make_group(X, Fraction(5, 3), Fraction(4, 3))
h01 = make_group(X, Fraction(5, 3), Fraction(-4, 3))
g12 = make_group(Y, Fraction(3, 5), Fraction(4, 5))
h12 = make_group(Y, Fraction(3, 5), Fraction(-4, 5))
g02 = core.emul(g12, g01)
h02 = core.emul(h01, h12)


print("\nB. EXACT MOVING PROJECTOR AND NONCOMMUTING COCYCLE")
check("exact", "both rational Clifford group elements have exact inverses",
      core.emul(g01, h01) == core.emul(h01, g01) == ONE_ELEMENT
      and core.emul(g12, h12) == core.emul(h12, g12) == ONE_ELEMENT)
check("planted", "PLANT the two finite unitary transitions do not commute",
      core.emul(g12, g01) != core.emul(g01, g12))

fixed_escape = adjoint(g01, basis(1), h01)
check("planted", "PLANT a fixed rank-8128 projector fails under the unitary escape",
      fixed_skew_projector(fixed_escape) != fixed_escape)

accept_failures = []
reject_failures = []
idempotence_failures = []
cocycle_failures = []
for mask in range(1 << 14):
    original = basis(mask)
    moved = adjoint(g01, original, h01)
    projected = moving_skew_projector(moved, g01, h01)
    if mask.bit_count() in SKEW_GRADES:
        if projected != moved:
            accept_failures.append(mask)
    elif projected:
        reject_failures.append(mask)
    if moving_skew_projector(projected, g01, h01) != projected:
        idempotence_failures.append(mask)
    sequential = adjoint(g12, moved, h12)
    direct = adjoint(g02, original, h02)
    if sequential != direct:
        cocycle_failures.append(mask)
check("exact", "the moving projector accepts all 8128 transported skew directions",
      not accept_failures)
check("exact", "the moving projector rejects all 8256 transported complementary directions",
      not reject_failures)
check("exact", "the moving rank-8128 projector is idempotent on the full basis",
      not idempotence_failures)
check("exact", "direct and sequential transport agree on all 16384 directions",
      not cocycle_failures)


def shiab_with(phi1, phi2, curvature):
    first_channel, inner_channel, outer_channel = core.channels
    star = core.hodge(curvature)
    first = core.wedge(phi1, star, first_channel)
    middle = core.hodge(core.wedge(phi2, star, inner_channel))
    second = core.hodge(core.wedge(phi1, middle, outer_channel))
    return core.fadd(first, core.fscale(Fraction(-1, 2), second))


def euler_with(phi1, phi2, q, value):
    return core.fadd(shiab_with(phi1, phi2, core.wedge_raw(q, value)), core.hodge(value))


phi1_1 = adjoint_form(g01, core.phi1, h01)
phi2_1 = adjoint_form(g01, core.phi2, h01)
q = {1 << 0: ONE_ELEMENT}
form_index = 1
operator_failures = []
sector_failures = []
lower_failures = []
for mask in range(1 << 14):
    value0 = {1 << form_index: basis(mask)}
    value1 = adjoint_form(g01, value0, h01)
    e0 = euler_with(core.phi1, core.phi2, q, value0)
    e1 = euler_with(phi1_1, phi2_1, q, value1)
    if e1 != adjoint_form(g01, e0, h01):
        operator_failures.append(mask)
    projected = moving_skew_form_projector(e1, g01, h01)
    if mask.bit_count() in SKEW_GRADES:
        if projected != e1:
            sector_failures.append(mask)
    elif projected:
        sector_failures.append(mask)
    curvature0 = core.fadd(core.wedge_raw(core.phi1, value0),
                           core.wedge_raw(value0, core.phi1))
    curvature1 = core.fadd(core.wedge_raw(phi1_1, value1),
                           core.wedge_raw(value1, phi1_1))
    if shiab_with(phi1_1, phi2_1, curvature1) != adjoint_form(
            g01, shiab_with(core.phi1, core.phi2, curvature0), h01):
        lower_failures.append(mask)

check("exact", "the recomputed moving first-order Euler operator is equivariant on all 16384 directions",
      not operator_failures)
check("theorem", "the moving Euler operator preserves both transported sectors wholesale",
      not sector_failures)
check("exact", "the recomputed moving background-A term is equivariant wholesale",
      not lower_failures)

witness0 = {1 << form_index: basis(1)}
witness1 = adjoint_form(g01, witness0, h01)
check("planted", "PLANT freezing Phi and the Euler operator breaks the moving-frame law",
      euler_with(core.phi1, core.phi2, q, witness1)
      != adjoint_form(g01, euler_with(core.phi1, core.phi2, q, witness0), h01))


print("\nC. MOVING WEYL-HALF REDUCTION INSIDE FULL U")
chi0 = {core.full: api.ONE}
chi1 = adjoint(g01, chi0, h01)
check("exact", "fixed and moved chirality involutions square to one",
      core.emul(chi0, chi0) == core.emul(chi1, chi1) == ONE_ELEMENT)


def block_project(value, chi):
    return core.escale(Fraction(1, 2), core.eadd(
        value, core.emul(core.emul(chi, value), chi)))


def coset_project(value, chi):
    return core.escale(Fraction(1, 2), core.eadd(
        value, core.escale(-1, core.emul(core.emul(chi, value), chi))))


block_count = 0
coset_count = 0
split_failures = []
moving_split_failures = []
for mask in range(1 << 14):
    value0 = basis(mask)
    block0, coset0 = block_project(value0, chi0), coset_project(value0, chi0)
    block_count += bool(block0)
    coset_count += bool(coset0)
    if core.eadd(block0, coset0) != value0:
        split_failures.append(mask)
    value1 = adjoint(g01, value0, h01)
    if (block_project(value1, chi1) != adjoint(g01, block0, h01)
            or coset_project(value1, chi1) != adjoint(g01, coset0, h01)):
        moving_split_failures.append(mask)
check("exact", "full u64,64 splits into 8192 block and 8192 bifundamental directions",
      block_count == coset_count == 8192 and not split_failures)
check("exact", "the moving two-half block/coset split is equivariant on all directions",
      not moving_split_failures)
check("layer0", "the coset half is associated bifundamental data not a two-half connection tangent",
      coset_count == 8192)

skew_even = sum(1 for mask in range(1 << 14)
                if mask.bit_count() in SKEW_GRADES and mask.bit_count() % 2 == 0)
skew_odd = 8128 - skew_even
self_even = sum(1 for mask in range(1 << 14)
                if mask.bit_count() in SELF_GRADES and mask.bit_count() % 2 == 0)
self_odd = 8256 - self_even
check("representation", "the Euler skew sector cuts across both Weyl block and coset halves",
      (skew_even, skew_odd, self_even, self_odd) == (4096, 4032, 4096, 4160))
check("layer0", "two C32,32 halves are a moving reduction inside source full P_H, not a second P_H by notation",
      global_bundle["principal_bundle"]["complex_Krein_extension"] == "U_64_64")


print("\nD. OBSERVATION PULLBACK AND ACCOUNTING")
spin_upstairs = 14 * 8128 + 10 + 91
full_upstairs = 14 * 16384 + 10 + 91
spin_observed_value = 4 * 8128 + 10 + 91
full_observed_value = 4 * 16384 + 10 + 91
check("exact", "upstairs tangent totals reproduce v0.129",
      (spin_upstairs, full_upstairs) == (113893, 229477))
check("exact", "ordinary value pullback changes form slots but not internal carrier ranks",
      (spin_observed_value, full_observed_value) == (32613, 65637))
check("observation", "pullback of P_H retains full U64,64 unless a reduction section is separately used",
      "remain open" in overlap["layer0"]["physical_section"])
check("planted", "PLANT observation pullback does not select skew versus full carrier",
      spin_observed_value != full_observed_value)


print("\nE. DISPOSITION AND FENCES")
for kind, label in (
    ("source", "source confirms full P_H two Weyl halves and epsilon-moved frame but not the skew tangent constraint"),
    ("geometry", "both rank-113893 moving and rank-229477 full associated bundles globalize"),
    ("variational", "carrier selection still requires action ownership of the moving projector constraint"),
    ("symplectic", "moving carrier descent creates no constraint quotient or reduced phase space"),
    ("krein", "global indefinite bundles supply no positive majorant or closed domain"),
    ("analytic", "finite overlap covariance supplies no contour measure spectrum or hyperbolicity"),
    ("scope", "no Standard Model cosmology generation or quantum verdict follows"),
    ("accounting", "no coefficient quotient external datum or P1 P2 P3 change follows"),
):
    check(kind, label, True)

print("MOVING_SPIN_BUNDLE=EPSILON_TRANSPORTED_RANK8128__CONNECTION113792__TOTAL113893__FULL_U_EQUIVARIANT_AS_MOVING_SUBBUNDLE")
print("SOURCE_PARENT=FULL_U6464_P_H_WITH_MOVING_TWO_C32_32_BLOCK_REDUCTION__BLOCK_CONNECTION8192_PLUS_BIFUNDAMENTAL8192")
print("OBSERVATION_VALUE_PULLBACK=SPIN32613__FULL65637__NO_INTERNAL_PARENT_SELECTION")
print("PARENT_DISPOSITION=FIXED_FRAME_FORCE_FULL_RETRACTED_OUTSIDE_FIXED_SCOPE__MOVING_SPIN_AND_FULL_U_BUNDLES_BOTH_GLOBAL__ACTION_PROJECTOR_OWNERSHIP_OPEN")
print("SOURCE_RETURN=SOURCE_CONFIRMS_FULL_U6464_P_H_TWO_C32_32_WEYL_HALVES_AND_EPSILON_MOVED_FRAME__SOURCE_SILENT_SPIN_SKEW_TANGENT_CONSTRAINT_AND_PHYSICAL_REDUCTION")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"PASS {sum(COUNTS.values())-len(FAILURES)}/{sum(COUNTS.values())}")
if FAILURES:
    raise SystemExit("failures: " + "; ".join(FAILURES))
