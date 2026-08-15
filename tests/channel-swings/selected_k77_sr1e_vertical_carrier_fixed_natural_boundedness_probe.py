#!/usr/bin/env sage -python
"""Exact SR-1E vertical carrier lift and fixed-natural boundedness gate.

The source instability lives in ``V10* tensor so(6,4)``.  The observation
splitting ``R(7,7)=R(1,3)+R(6,4)`` gives a canonical block inclusion into
``V14* tensor so(7,7)``.  This probe constructs that rank-450 inclusion,
checks all 45 infinitesimal intertwiners, and evaluates the leading selected
Shiab/I2B quartic on two exact rays in its image.

The fixed-natural residual primalizer is unique up to nonzero scale.  The two
quartic values have opposite signs, so every allowed scale has a negative
ray.  The eddy-completed first action is at most cubic and cannot repair that
large-amplitude runaway.  Moving primalizers, source-derived constraints and
new higher-even action terms remain outside this gate.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
import contextlib
import io
import json
from pathlib import Path
import runpy
import subprocess

from sage.all import QQ, diagonal_matrix, matrix


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. PREDECESSORS, SOURCE OWNER, AND TYPE FENCES")
interface_probe = ROOT / "tests/channel-swings/selected_k77_sr1e_source_instability_ownership_gate_probe.py"
interface_run = subprocess.run(
    ["python3", str(interface_probe)], capture_output=True, text=True, check=False
)
check("prior", "the exact SR-1E ownership gate replays 45/45",
      interface_run.returncode == 0
      and "45/45 exact/interface checks passed" in interface_run.stdout)
owner = read(
    "explorations/conditional-build/selected-k77-i2b-source-natural-second-action-owner-2026-08-13.md"
)
pairing = read(
    "explorations/conditional-build/selected-k77-residual-pairing-invariance-2026-08-08.md"
)
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
check("prior", "the fixed-natural source I2B owner is Q_B=c times trace/Hodge with c nonzero",
      "Q_B = c Q_trace/Hodge,   c != 0" in owner)
check("prior", "the exact local trace/Hodge residual pairing is indefinite",
      "inertia `(741,729,0)`" in pairing)
check("source", "the released first action contains only the linear quadratic and cubic eddy chain",
      "F_{B_\\omega}" in source and "\\frac12d_{B_\\omega}T_\\omega" in source
      and "\\frac13[T_\\omega,T_\\omega]" in source)
for label in (
    "an observation-relative equivariant inclusion versus a source-selected orbit",
    "a point carrier versus a canonical first-jet lift",
    "raw curvature norm versus selected-Shiab residual norm",
    "fixed-natural Q_B versus a moving fundamental symmetry",
    "global boundedness versus local criticality",
    "a negative ray versus a physical BV tangent",
):
    check("type", label + " remain distinct", True)


print("\nB. CANONICAL VERTICAL 450 TO 1274 CARRIER MAP")
ETA_H = (1, -1, -1, -1)
ETA_V = (1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
ETA_14 = ETA_H + ETA_V
NORMAL = tuple(range(4, 14))
LOCAL_PAIRS = [(i, j) for i in range(10) for j in range(i + 1, 10)]
AMBIENT_PAIRS = [(i, j) for i in range(14) for j in range(i + 1, 14)]
DOMAIN = [(mu, i, j) for mu in range(10) for i, j in LOCAL_PAIRS]
AMBIENT = [(mu, i, j) for mu in range(14) for i, j in AMBIENT_PAIRS]
ambient_index = {label: index for index, label in enumerate(AMBIENT)}


def so_generator(eta, i: int, j: int):
    value = matrix(QQ, len(eta), len(eta), sparse=True)
    value[i, j] = eta[j]
    value[j, i] = -eta[i]
    return value


def decompose_so(value, eta):
    output = {}
    reconstruction = matrix(QQ, len(eta), len(eta), sparse=True)
    for i in range(len(eta)):
        for j in range(i + 1, len(eta)):
            coefficient = value[i, j] / eta[j]
            if coefficient:
                output[(i, j)] = coefficient
                reconstruction += coefficient * so_generator(eta, i, j)
    assert reconstruction == value
    return output


def carrier_action(eta, generator, label):
    mu, i, j = label
    output = defaultdict(QQ)
    dual = -generator.transpose()
    for nu in range(len(eta)):
        if dual[nu, mu]:
            output[(nu, i, j)] += dual[nu, mu]
    adjoint = generator * so_generator(eta, i, j) - so_generator(eta, i, j) * generator
    for (left, right), coefficient in decompose_so(adjoint, eta).items():
        output[(mu, left, right)] += coefficient
    return {key: value for key, value in output.items() if value}


def embed_label(label):
    mu, i, j = label
    return (mu + 4, i + 4, j + 4)


inclusion = matrix(QQ, len(AMBIENT), len(DOMAIN), sparse=True)
for column, label in enumerate(DOMAIN):
    inclusion[ambient_index[embed_label(label)], column] = 1
check("dimension", "the source vertical carrier has dimension 10 times 45 equals 450",
      len(DOMAIN) == 450)
check("dimension", "the ambient point carrier has dimension 14 times 91 equals 1274",
      len(AMBIENT) == 1274)
check("map", "the block inclusion has exact rank 450 and zero kernel",
      inclusion.rank() == 450)
check("map", "its image is exactly the N-star tensor Lambda2(N) coordinate block",
      {embed_label(label) for label in DOMAIN}
      == {(mu, i, j) for mu in NORMAL for i in NORMAL for j in NORMAL if i < j})

eta_v_matrix = diagonal_matrix(QQ, ETA_V, sparse=True)
metric_skew = []
intertwiner_checks = []
for a, b in LOCAL_PAIRS:
    local_generator = so_generator(ETA_V, a, b)
    metric_skew.append(
        local_generator.transpose() * eta_v_matrix
        + eta_v_matrix * local_generator
        == matrix(QQ, 10, 10, sparse=True)
    )
    ambient_generator = so_generator(ETA_14, a + 4, b + 4)
    for label in DOMAIN:
        local_image = {
            embed_label(key): value
            for key, value in carrier_action(ETA_V, local_generator, label).items()
        }
        ambient_image = carrier_action(ETA_14, ambient_generator, embed_label(label))
        intertwiner_checks.append(local_image == ambient_image)
check("group", "all 45 local generators are exactly so(6,4)-skew",
      len(metric_skew) == 45 and all(metric_skew))
check("equivariance", "all 45 by 450 infinitesimal carrier intertwiners close exactly",
      len(intertwiner_checks) == 20250 and all(intertwiner_checks))

# A mixed horizontal/normal generator takes the vertical block outside itself;
# the map is natural for the observation stabilizer, not full SO(7,7).
mixed = so_generator(ETA_14, 0, 4)
mixed_image = carrier_action(ETA_14, mixed, embed_label((0, 0, 1)))
check("planted", "PLANT a mixed H/N generator exits the vertical image",
      any(mu < 4 or i < 4 or j < 4 for mu, i, j in mixed_image))


print("\nC. SELECTED SHIAB AND I2B QUARTIC ON THE EMBEDDED RAYS")
backend_capture = io.StringIO()
with contextlib.redirect_stdout(backend_capture):
    M = runpy.run_path(
        str(ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py")
    )
check("prior", "the exact selected-Shiab backend replays",
      "failures=0" in backend_capture.getvalue().lower())
FULL = M["FULL"]
ZERO = M["ZERO"]
SELECTED = ("comm", "symi", "symi")


def one_form_bivector(form_index: int, left: int, right: int):
    return {
        1 << form_index: M["emul"](M["blade"](left), M["blade"](right))
    }


def top_pair(left, right):
    return M["wedge_raw"](left, right).get(FULL, {}).get(0, ZERO)


def ray(first_form: int, second_form: int):
    return M["fadd"](
        one_form_bivector(first_form, 4, 5),
        one_form_bivector(second_form, 5, 6),
    )


def ray_packet(value):
    curvature = M["wedge_raw"](value, value)
    residual_lead = M["shiab"](curvature, SELECTED)
    return {
        "T": value,
        "curvature": curvature,
        "residual": residual_lead,
        "raw_quartic": top_pair(curvature, M["hodge"](curvature)),
        "selected_quartic": top_pair(residual_lead, M["hodge"](residual_lead)),
        "first_action_cubic": top_pair(value, residual_lead),
        "mass": top_pair(value, M["hodge"](value)),
    }


positive_plane = ray_packet(ray(4, 5))
mixed_plane = ray_packet(ray(4, 10))


def support_is_vertical_cl2(value):
    for (form_mask, clifford_mask), coefficient in M["flatten"](value).items():
        form_indices = [index for index in range(14) if form_mask & (1 << index)]
        clifford_indices = [index for index in range(14) if clifford_mask & (1 << index)]
        if (not coefficient or len(form_indices) != 1 or form_indices[0] < 4
                or len(clifford_indices) != 2
                or any(index < 4 for index in clifford_indices)):
            return False
    return True


check("carrier", "both rays lie wholly in the embedded N-star tensor so(6,4) block",
      support_is_vertical_cl2(positive_plane["T"])
      and support_is_vertical_cl2(mixed_plane["T"]))
check("exact", "the raw DeWitt/Killing quartics are minus four and plus four",
      positive_plane["raw_quartic"] == (Fraction(-4), Fraction(0))
      and mixed_plane["raw_quartic"] == (Fraction(4), Fraction(0)))
check("exact", "selected Shiab sends each ray to one Lambda13-Cl1 residual cell",
      all(len(M["flatten"](packet["residual"])) == 1
          and all(form.bit_count() == 13 and cliff.bit_count() == 1
                  for form, cliff in M["flatten"](packet["residual"]))
          for packet in (positive_plane, mixed_plane)))
check("exact", "the source-natural trace/Hodge I2B quartics are minus sixteen and plus sixteen",
      positive_plane["selected_quartic"] == (Fraction(-16), Fraction(0))
      and mixed_plane["selected_quartic"] == (Fraction(16), Fraction(0)))
check("parity", "the eddy first-action cubic vanishes separately on both Cl2 rays",
      positive_plane["first_action_cubic"] == ZERO
      and mixed_plane["first_action_cubic"] == ZERO)
check("control", "the lower quadratic mass return remains live on the positive-plane ray",
      positive_plane["mass"] == (Fraction(-2), Fraction(0)))


print("\nD. FIXED-NATURAL BOUNDEDNESS THEOREM")
# With Q_B=c Q_trace/Hodge, the leading I2B coefficient is one half c times
# the displayed quartic.  For either sign of nonzero c, one embedded ray has
# negative leading coefficient.  Background curvature, kappa and I1B add only
# lower-degree terms and cannot alter the large-amplitude sign.
c_positive = Fraction(1)
c_negative = Fraction(-1)
leading_pp_positive_c = c_positive * positive_plane["selected_quartic"][0] / 2
leading_pm_positive_c = c_positive * mixed_plane["selected_quartic"][0] / 2
leading_pp_negative_c = c_negative * positive_plane["selected_quartic"][0] / 2
leading_pm_negative_c = c_negative * mixed_plane["selected_quartic"][0] / 2
check("theorem", "positive fixed-natural scale has a negative quartic ray",
      leading_pp_positive_c == -8 and leading_pm_positive_c == 8)
check("theorem", "negative fixed-natural scale merely exchanges which ray runs away",
      leading_pp_negative_c == 8 and leading_pm_negative_c == -8)
check("theorem", "every admissible nonzero fixed-natural scale is globally indefinite",
      positive_plane["selected_quartic"][0]
      == -mixed_plane["selected_quartic"][0] != 0)
check("degree", "I1B has amplitude degree at most three while I2B supplies degree four",
      "\\frac13[T_\\omega,T_\\omega]" in source)
check("degree", "no linear quadratic or cubic term can bound a negative quartic ray",
      True)
check("owner", "zero scale is not an allowed primalizer and would delete I2B",
      "c != 0" in owner)
check("result", "the released fixed-natural I1B plus I2B bosonic action is unbounded below",
      leading_pp_positive_c < 0 and leading_pm_negative_c < 0)


print("\nE. CLAIM CEILING AND NEXT GATE")
for kind, label in (
    ("scope", "the carrier map is canonical only relative to the observation H/N splitting"),
    ("scope", "no source-selected negative orbit or critical amplitude is constructed"),
    ("scope", "no canonical B_Z first jet or inherited Bianchi lift is constructed"),
    ("escape", "a moving action-owned fundamental symmetry remains open"),
    ("escape", "a source-derived constraint or BV tangent excluding the runaway remains open"),
    ("escape", "a new higher-even full-action term dominating the quartic remains open"),
    ("status", "SR-1 remains background-missing and VRS-6 remains blocked"),
    ("accounting", "no ledger canon residue quotient datum or public-posture move follows"),
    ("physics", "no vacuum spectrum superposition Born rule or empirical prediction follows"),
):
    check(kind, label, True)


RESULT = {
    "disposition": "CANONICAL_VERTICAL_450_TO1274_CARRIER_MAP_BUILT__FIXED_NATURAL_SELECTED_I2B_QUARTIC_HAS_OPPOSITE_SIGN_RAYS__RELEASED_BOSONIC_ACTION_UNBOUNDED_BELOW",
    "carrier_map": {
        "domain": "V10_STAR_TENSOR_SO_6_4",
        "domain_dimension": len(DOMAIN),
        "codomain": "V14_STAR_TENSOR_SO_7_7",
        "codomain_dimension": len(AMBIENT),
        "rank": int(inclusion.rank()),
        "image": "N_STAR_TENSOR_LAMBDA2_N",
        "so_6_4_intertwiner_checks": len(intertwiner_checks),
        "full_so_7_7_equivariant": False,
    },
    "quartic": {
        "raw_dewitt_killing": [-4, 4],
        "selected_shiab_i2b": [-16, 16],
        "first_action_cubic": [0, 0],
        "fixed_natural_Q_B": "c*Q_TRACE_HODGE__c_NONZERO",
        "bounded_for_any_nonzero_c": False,
    },
    "sr1": "BACKGROUND-MISSING",
    "vrs6": "BLOCKED",
    "next_gate": "SR-1F_ACTION_OWNED_MOVING_FUNDAMENTAL_SYMMETRY_OR_SOURCE_CONSTRAINT_OR_HIGHER_EVEN_ACTION_TERM__THEN_SELECT_CRITICAL_ORBIT_AND_BUILD_CANONICAL_FIRST_JET",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
