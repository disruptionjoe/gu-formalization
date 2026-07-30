#!/usr/bin/env python3
"""Joint N2a/N4a handoff: derive a finite useful first slice of N3.

The two child probes are executed as independent contracts.  This integration
probe does not upgrade either result:

* N2a constructs bare native spinor kernels but leaves the total
  P0 x rho(Phi) x Y kernel and full-gauge stabilizer unresolved.
* N4a constructs the Levi--Civita curvature map and a partial grammar
  incidence ledger, but leaves the open-BV Hom rank, EOM factorization, and
  CME unresolved.

The only new result is their intersection: the Lorentz-preserving nonzero
screen representative is trace-type, while the compatible LC physical-R
defect is traceless-Ricci-type.  They cannot be identified as one algebraic
channel.  The code therefore emits six N3 variation/interface discriminators,
plus one campaign-level index/causality carry-through, without changing N1's
packet.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
SEALED_HASH = "1efdffd34e3ad5358fed16c08cda9ecf681df676e817560bf36b436d79658ffb"
FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def run_child(filename: str) -> str:
    result = subprocess.run(
        [sys.executable, str(HERE / filename)],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


Q = Fraction
Matrix4 = tuple[tuple[Q, ...], ...]
ETA4: Matrix4 = (
    (Q(1), Q(0), Q(0), Q(0)),
    (Q(0), Q(1), Q(0), Q(0)),
    (Q(0), Q(0), Q(1), Q(0)),
    (Q(0), Q(0), Q(0), Q(-1)),
)


def metric_trace(tensor: Matrix4) -> Q:
    return sum(ETA4[index][index] * tensor[index][index] for index in range(4))


def scale(value: Q, tensor: Matrix4) -> Matrix4:
    return tuple(tuple(value * entry for entry in row) for row in tensor)


def subtract(left: Matrix4, right: Matrix4) -> Matrix4:
    return tuple(
        tuple(left[row][column] - right[row][column] for column in range(4))
        for row in range(4)
    )


def traceless_part(tensor: Matrix4) -> Matrix4:
    return subtract(tensor, scale(metric_trace(tensor) / 4, ETA4))


def is_zero(tensor: Matrix4) -> bool:
    return all(entry == 0 for row in tensor for entry in row)


@dataclass(frozen=True)
class Emission:
    name: str
    object_out: str
    owners: tuple[str, ...]
    legs: tuple[str, ...]


N3_DISCRIMINATOR_SLICE = (
    Emission(
        "total_kernel_K",
        "P0^dagger K c_rho(v[Phi]) Y_K P0, with sesquilinear reality and 20-slot incidence",
        ("N2b",),
        ("Y", "Q"),
    ),
    Emission(
        "total_kernel_C",
        "P0^T C_(epsilon,tau) c_rho(v[Phi]) Y_C P0, with Grassmann transpose, reality completion, and 20-slot incidence",
        ("N2b",),
        ("Y", "Q"),
    ),
    Emission(
        "fermion_and_vertical_connection_euler",
        "E_Z plus res_s^(V,!)(E_A^V), including the Yukawa current and section-current dual",
        ("N2b", "N4b"),
        ("Y", "Q", "G"),
    ),
    Emission(
        "section_euler_trace_split",
        "E_s = (tr E_s, E_s^0), including variation of s_* and the induced-|II|^2 terms",
        ("N2b", "N4b"),
        ("G", "U"),
    ),
    Emission(
        "ig_parent_connection_euler",
        "(E_PIG,E_U,E_A^IG,E_epsilonIG) plus [nabla_A,Gamma], [nabla_A,P_R], and soldering-equivariance residuals; OmegaIG/F_A/PIG kept distinct",
        ("N4b",),
        ("Q", "G", "U"),
    ),
    Emission(
        "physical_R_noether_defect",
        "Delta_R=P_R H_packet R_r gamma split into LC-Ric0, IG, compatibility, and source-equation pieces",
        ("N4b",),
        ("Q", "U"),
    ),
)

N3_CAMPAIGN_CARRY = (
    Emission(
        "twisted_characteristic_input",
        "principal/subprincipal characteristic packet tensored by nu*e_hat_n, without an index pushforward",
        ("N2b", "N4b", "N5"),
        ("I", "U"),
    ),
)
N3_FIRST_SLICE = N3_DISCRIMINATOR_SLICE + N3_CAMPAIGN_CARRY


print("=" * 96)
print("N2a/N4a INTERSECTION AND MINIMAL N3 FIRST-SLICE CONTRACT")
print("=" * 96)

n2_output = run_child("actual_sym2_c14_orbit_probe.py")
n4_output = run_child("full20_curvature_irrep_open_bv_probe.py")

check(
    "both child probes consume the unchanged N1 packet",
    f"FROZEN HASH: {SEALED_HASH}" in n2_output
    and "frozen N1 construction hash is unchanged" in n4_output,
)
check(
    "N2a is conditional algebra, not a claimed surviving physical interaction",
    "VERDICT: N2a-CONDITIONAL-ALGEBRA-CONSTRUCTED" in n2_output
    and "TOTAL-ODD-KERNEL-AND-NONZERO-GAUGE-STABILIZER-TYPED-UNRESOLVED"
    in n2_output,
)
check(
    "N2a kills the zero representative and leaves all nonzero total kernels undecided",
    "zero                   tr=+0 G=+0 rank(c)=  0" in n2_output
    and "UNRESOLVED: total odd survival without P0, rho(Phi), and Y_C."
    in n2_output,
)
check(
    "only zero and trace preserve the complete fixed-background Lorentz algebra in the screen",
    "fixed zero/trace preserve all six Lorentz generators; space/null do not"
    in n2_output,
)
check(
    "N4a isolates LC physical-R curvature to traceless Ricci",
    "VERDICT: LC-RIEMANN-IRREP-MAP-IS-HALF-TRACELESS-RICCI-ONLY"
    in n4_output,
)
check(
    "N4a preserves W177 nonzero/full-rank while superseding the mixed-convention norm",
    "prior W177 qualitative nonzero/full-rank result survives while its norm is superseded"
    in n4_output,
)
check(
    "N4a does not turn syntactic grammar size into Hom rank, EOM factorization, or CME",
    "RESIDUAL: FULL-SP-IG-COVARIANCE-AND-OPEN-BV-HOM-RANK-DEFERRED"
    in n4_output
    and "NONCLAIM: NO-SOURCE-EOM-FACTORIZATION; NO-CME-TEST" in n4_output,
)

# Exact representation-type firewall.  A scalar multiple of the metric has
# no traceless symmetric component; a traceless-Ricci tensor has no trace.
# This does not say a dynamical trace field cannot source Ric0 through
# derivatives or other fields.  It says there is no direct algebraic
# identification of the two channels.
trace_tensor = scale(Q(-1, 4), ETA4)
ricci_zero_fixture: Matrix4 = (
    (Q(1), Q(0), Q(0), Q(0)),
    (Q(0), Q(-1), Q(0), Q(0)),
    (Q(0), Q(0), Q(0), Q(0)),
    (Q(0), Q(0), Q(0), Q(0)),
)
check(
    "the Lorentz-invariant trace representative has zero traceless projection",
    is_zero(traceless_part(trace_tensor)),
)
check(
    "the N4a Ricci-zero fixture is trace-free and nonzero",
    metric_trace(ricci_zero_fixture) == 0 and not is_zero(ricci_zero_fixture),
)
check(
    "Layer 0 rejects direct trace-orbit = traceless-Ricci-obstruction identification",
    trace_tensor != ricci_zero_fixture
    and is_zero(traceless_part(trace_tensor))
    and traceless_part(ricci_zero_fixture) == ricci_zero_fixture,
)

all_legs = {leg for emission in N3_FIRST_SLICE for leg in emission.legs}
check(
    "the finite N3 first slice carries all five campaign legs",
    all_legs == {"Y", "Q", "G", "I", "U"},
    str(sorted(all_legs)),
)
check(
    "each N3 emission has a downstream discriminator owner",
    all(emission.owners for emission in N3_FIRST_SLICE),
)
check(
    "the N3 slice keeps the omitted Krein and charge-conjugation total kernels distinct",
    N3_DISCRIMINATOR_SLICE[0].name == "total_kernel_K"
    and "P0^dagger K" in N3_DISCRIMINATOR_SLICE[0].object_out
    and "sesquilinear" in N3_DISCRIMINATOR_SLICE[0].object_out
    and N3_DISCRIMINATOR_SLICE[1].name == "total_kernel_C"
    and "P0^T C_" in N3_DISCRIMINATOR_SLICE[1].object_out
    and "Grassmann transpose" in N3_DISCRIMINATOR_SLICE[1].object_out,
)
check(
    "the N3 slice supplies the tracefree section equation required by N4b",
    any(
        emission.name == "section_euler_trace_split"
        and "E_s^0" in emission.object_out
        and "N4b" in emission.owners
        for emission in N3_FIRST_SLICE
    ),
)
check(
    "the N3 slice keeps LC, IG, compatibility, and source-equation pieces separate in Delta_R",
    any(
        emission.name == "physical_R_noether_defect"
        and all(
            token in emission.object_out
            for token in ("LC-Ric0", "IG", "compatibility", "source-equation")
        )
        for emission in N3_DISCRIMINATOR_SLICE
    ),
)
check(
    "the IG parent emission carries the fired Clifford/projector/soldering compatibility residuals",
    any(
        emission.name == "ig_parent_connection_euler"
        and all(
            token in emission.object_out
            for token in (
                "E_epsilonIG",
                "[nabla_A,Gamma]",
                "[nabla_A,P_R]",
                "soldering-equivariance",
            )
        )
        for emission in N3_DISCRIMINATOR_SLICE
    ),
)
check(
    "six discriminator emissions are separated from one index/causality campaign carry",
    len(N3_DISCRIMINATOR_SLICE) == 6
    and len(N3_CAMPAIGN_CARRY) == 1
    and N3_CAMPAIGN_CARRY[0].name == "twisted_characteristic_input"
    and "without an index pushforward" in N3_CAMPAIGN_CARRY[0].object_out,
)

print("\nN3 first-slice emission ledger:")
for emission in N3_FIRST_SLICE:
    print(
        f"  {emission.name}: {emission.object_out}; "
        f"owners={','.join(emission.owners)}; legs={','.join(emission.legs)}"
    )

if FAILURES:
    print(f"\nCONTROLS FAILED: {FAILURES}")
    print("VERDICT: VOID")
    raise SystemExit(1)

print("\nVERDICT: N2A/N4A-JOINT-CONSTRAINT-CONSTRUCTED")
print("VERDICT: TRACE-ORBIT-AND-LC-RICCI0-CHANNELS-SEPARATED")
print("VERDICT: SIX-EMISSION-N3-DISCRIMINATOR-SLICE-FROZEN")
print("VERDICT: ONE-EMISSION-INDEX/CAUSALITY-CAMPAIGN-CARRY-FROZEN")
print("NONCLAIM: NO-N2A-GO; NO-N4B-FACTOR; NO-CME; NO-MASS; NO-INDEX; NO-COUNT")
print("=" * 96)
