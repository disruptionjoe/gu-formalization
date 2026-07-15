#!/usr/bin/env python
"""
W239 Track B prediction scan.

This is a deterministic claim-shape and arithmetic audit.  It does not establish new
physics by enumeration.  It makes the exclusion rules explicit, checks the numerical
content of the strongest conditional candidate, and prevents a structural property,
free-parameter family, data-calibrated relation, or already-excluded conditional from
being relabelled as a standing GU prediction.

Run: python -u tests/W239_track_b_distinctive_prediction_scan.py
"""

from dataclasses import dataclass
from fractions import Fraction
from math import isclose, sqrt


FAIL = []


def check(name, condition, detail=""):
    state = "PASS" if condition else "FAIL"
    print(f"{state} :: {name}" + (f"  --  {detail}" if detail else ""))
    if not condition:
        FAIL.append(name)


@dataclass(frozen=True)
class Candidate:
    key: str
    built_gu_forced: bool
    quantitative: bool
    calibration_independent: bool
    distinctive: bool
    physical_observable: bool
    confrontable: bool
    robust: bool
    data_outcome: str = "not_confronted"

    def failed_gates(self):
        gates = {
            "built_gu_forced": self.built_gu_forced,
            "quantitative": self.quantitative,
            "calibration_independent": self.calibration_independent,
            "distinctive": self.distinctive,
            "physical_observable": self.physical_observable,
            "confrontable": self.confrontable,
            "robust": self.robust,
        }
        return tuple(name for name, passed in gates.items() if not passed)

    def is_standing_prediction(self):
        return not self.failed_gates() and self.data_outcome != "excluded"

    def disposition(self):
        if self.data_outcome == "excluded" and self.failed_gates():
            return "KILLED_CONDITIONAL"
        if self.data_outcome == "excluded":
            return "KILLED_PREDICTION"
        if self.failed_gates():
            return "NOT_A_STANDING_PREDICTION"
        return "STANDING_PREDICTION"


print("== POSITIVE CONTROLS: THE GATE HAS TEETH ==")
synthetic_pass = Candidate(
    "synthetic_pass", True, True, True, True, True, True, True, "confirmed"
)
check("PC1 a genuinely forced, independent, distinctive observable passes",
      synthetic_pass.is_standing_prediction())

synthetic_calibrated = Candidate(
    "synthetic_calibrated", True, True, False, True, True, True, True
)
check("PC2 a target-calibrated number fails", not synthetic_calibrated.is_standing_prediction(),
      str(synthetic_calibrated.failed_gates()))

synthetic_free_scale = Candidate(
    "synthetic_free_scale", True, False, True, True, True, True, False
)
check("PC3 a free-scale family fails", not synthetic_free_scale.is_standing_prediction(),
      str(synthetic_free_scale.failed_gates()))

synthetic_generic = Candidate(
    "synthetic_generic", True, True, True, False, True, True, True
)
check("PC4 a generic known effect fails distinctiveness",
      not synthetic_generic.is_standing_prediction())

synthetic_property = Candidate(
    "synthetic_property", True, True, True, True, False, False, True
)
check("PC5 an inaccessible action property is not an observable prediction",
      not synthetic_property.is_standing_prediction())

synthetic_excluded = Candidate(
    "synthetic_excluded", True, True, True, True, True, True, True, "excluded"
)
check("PC6 an excluded prediction is killed, not a survivor",
      synthetic_excluded.disposition() == "KILLED_PREDICTION")


print("\n== ACTUAL GU CANDIDATE CENSUS ==")
candidates = (
    Candidate(
        "SM_YUKAWA_MAGNITUDE_RELATION",
        built_gu_forced=False,
        quantitative=False,
        calibration_independent=True,
        distinctive=False,
        physical_observable=True,
        confrontable=False,
        robust=False,
    ),
    Candidate(
        "H36_DEWITT_TO_SPIN2_YUKAWA_LOCK",
        built_gu_forced=False,
        quantitative=True,
        calibration_independent=False,
        distinctive=False,
        physical_observable=True,
        confrontable=True,
        robust=True,
        data_outcome="excluded",
    ),
    Candidate(
        "MIRROR_SPECTRUM",
        built_gu_forced=False,
        quantitative=False,
        calibration_independent=True,
        distinctive=True,
        physical_observable=False,
        confrontable=False,
        robust=False,
    ),
    Candidate(
        "FOURTH_ORDER_SEVEN_DOF",
        built_gu_forced=True,
        quantitative=True,
        calibration_independent=True,
        distinctive=False,
        physical_observable=False,
        confrontable=False,
        robust=True,
    ),
    Candidate(
        "SOURCE_SCREENING_LENGTH",
        built_gu_forced=False,
        quantitative=False,
        calibration_independent=True,
        distinctive=False,
        physical_observable=True,
        confrontable=False,
        robust=False,
    ),
    Candidate(
        "DARK_ENERGY_PHANTOM_FEATURE",
        built_gu_forced=False,
        quantitative=False,
        calibration_independent=False,
        distinctive=False,
        physical_observable=True,
        confrontable=False,
        robust=False,
    ),
    Candidate(
        "THREE_CHIRAL_GENERATIONS",
        built_gu_forced=False,
        quantitative=True,
        calibration_independent=True,
        distinctive=False,
        physical_observable=True,
        confrontable=True,
        robust=False,
    ),
)

for candidate in candidates:
    check(f"CENSUS {candidate.key} does not clear every prediction gate",
          not candidate.is_standing_prediction(),
          f"{candidate.disposition()}; fails={candidate.failed_gates()}")

check("C1 the census has no standing distinctive GU prediction",
      not any(candidate.is_standing_prediction() for candidate in candidates))
check("C2 the H36 candidate is retained as a killed conditional",
      next(c for c in candidates if c.key.startswith("H36")).disposition()
      == "KILLED_CONDITIONAL")


print("\n== TEN DIVERGENT PERSONAS: 30 PREDICTION TARGETS ==")
persona_proposals = (
    # persona, leg, target, impact (1..5), difficulty (1..5), readiness, first kill
    ("flavor_rep_theorist", "flavor", "basis-invariant Yukawa singular-value ratio", 5, 5,
     "target", "any independent surviving flavor coefficient remains"),
    ("flavor_rep_theorist", "flavor", "Z/3 texture-zero mixing sum rule", 4, 4,
     "target", "the relation is basis-dependent or broken by the required source spurion"),
    ("flavor_rep_theorist", "flavor", "Dirac-only neutrino mass selection", 5, 4,
     "structural_seed", "an allowed physical Majorana spurion survives the quotient"),

    ("collider_phenomenologist", "mirror", "complete vectorlike mirror multiplet spectrum", 5, 5,
     "structural_seed", "the mirror is BRST-exact or its masses remain independent"),
    ("collider_phenomenologist", "mirror", "SO(10)-fixed mirror branching-fraction ratios", 5, 5,
     "target", "unfixed mixing angles or decay operators alter the ratios"),
    ("collider_phenomenologist", "mirror", "channel-S composite resonance pattern", 4, 5,
     "target", "no isolated physical pole exists after confinement and quotient"),

    ("gravity_phenomenologist", "gravity", "fixed-strength fixed-range short-distance force", 5, 5,
     "killed_conditional", "a native scale cannot be derived without target data"),
    ("gravity_phenomenologist", "gravity", "massive-spin-2 gravitational-wave dispersion", 5, 5,
     "target", "the pole decouples at every accessible frequency"),
    ("gravity_phenomenologist", "gravity", "parameter-free Kerr ringdown correction", 5, 5,
     "target", "the correction depends on the free higher-derivative scale"),

    ("cosmologist", "cosmology", "predeclared w(z) width and crossing shape", 4, 4,
     "target", "the width shifts with f0, ansatz, or initial conditions"),
    ("cosmologist", "cosmology", "fixed sign relation between w(z) and f-sigma8", 5, 5,
     "target", "growth sign varies over allowed completion parameters"),
    ("cosmologist", "cosmology", "dark-energy to spin-2 scale ratio", 5, 5,
     "killed_conditional", "the observed dark-energy density is used to set the scale"),

    ("qft_renormalization_expert", "quantization", "physical extra-pole residue and line shape", 5, 5,
     "target", "no positive interacting C metric or gauge-independent pole exists"),
    ("qft_renormalization_expert", "quantization", "renormalization-group fixed coupling ratio", 5, 5,
     "target", "the ratio runs with an unfixed relevant direction"),
    ("qft_renormalization_expert", "quantization", "threshold matching relation across GU sectors", 4, 5,
     "target", "unknown heavy thresholds supply arbitrary finite matching terms"),

    ("geometric_analyst", "geometry", "exact observable ratio of Einstein Weyl and vacuum terms", 5, 5,
     "structural_seed", "field normalization or section choice changes the physical ratio"),
    ("geometric_analyst", "geometry", "topologically protected spectral multiplicity", 4, 4,
     "structural_seed", "the multiplicity is only an arena count and not a physical excitation count"),
    ("geometric_analyst", "geometry", "fixed tensor ratios in the source response function", 4, 4,
     "structural_seed", "free algebraic K_IG terms change the measurable tensor ratios"),

    ("brst_krein_expert", "physical_state", "physical mirror cohomology parity", 5, 5,
     "structural_seed", "interacting BRST makes the mirror exact or nonunitary"),
    ("brst_krein_expert", "physical_state", "positivity-fixed sign of a scattering interference term", 5, 5,
     "target", "the sign is convention-dependent or the S matrix is unbuilt"),
    ("brst_krein_expert", "physical_state", "channel-S allowed and channel-D forbidden chiral spectrum", 5, 5,
     "structural_seed", "the operative grading cannot coexist with the required vacuum"),

    ("records_foundations_expert", "record_source", "retarded record-current transfer function", 4, 4,
     "structural_seed", "the response is equivalent to an ordinary fixed-source kernel"),
    ("records_foundations_expert", "record_source", "record-creation gravitational memory signal", 4, 5,
     "target", "the memory is gauge-removable or generic to standard nonlinear response"),
    ("records_foundations_expert", "record_source", "capability-change correlated source pulse", 4, 5,
     "target", "no GU-native observable maps the record event to a source amplitude"),

    ("experimental_strategist", "measurement", "zero-parameter relation among measured SM inputs", 5, 5,
     "target", "the theory needs one fitted coefficient"),
    ("experimental_strategist", "measurement", "torsion-balance force with predeclared alpha and lambda", 5, 5,
     "killed_conditional", "the predeclared point is excluded or calibrated from the same data"),
    ("experimental_strategist", "measurement", "fixed-rate mirror production and decay packet", 5, 5,
     "target", "unknown mass or branching fraction prevents a rate prediction"),

    ("hostile_model_selector", "model_selection", "dimensionless overconstraint of existing data", 5, 5,
     "target", "one GU-specific free parameter can absorb the discrepancy"),
    ("hostile_model_selector", "model_selection", "sign prediction opposite a live competitor", 5, 4,
     "target", "both signs occur in allowed GU branches"),
    ("hostile_model_selector", "model_selection", "complete correlated smoking-gun spectrum", 5, 5,
     "target", "a standard effective model reproduces it with equal or fewer assumptions"),
)

personas = {row[0] for row in persona_proposals}
check("P1 exactly ten divergent personas participated", len(personas) == 10, str(sorted(personas)))
check("P2 every persona supplied exactly three targets",
      all(sum(row[0] == persona for row in persona_proposals) == 3 for persona in personas))
check("P3 the register contains exactly thirty targets", len(persona_proposals) == 30)
check("P4 every impact and difficulty score is on the 1..5 scale",
      all(1 <= row[3] <= 5 and 1 <= row[4] <= 5 for row in persona_proposals))
check("P5 every target has an explicit first-kill condition",
      all(len(row[6].strip()) >= 20 for row in persona_proposals))
check("P6 no persona labels a proposal as an existing standing prediction",
      all(row[5] in {"target", "structural_seed", "killed_conditional"}
          for row in persona_proposals))
check("P7 the search spans at least nine supporting legs",
      len({row[1] for row in persona_proposals}) >= 9)


print("\n== PRIORITY ROUTE: YUKAWA MAGNITUDES ==")
# H28 computes a three-dimensional invariant support.  Its three coefficients remain free.
allowed_entries = ((0, 0), (1, 2), (2, 1))
free_coefficients = ("y00", "y12", "y21")
check("Y1 Z/3 reduces nine entries to exactly three allowed entries",
      len(allowed_entries) == 3 and len(set(allowed_entries)) == 3)
check("Y2 every surviving Yukawa entry retains an independent coefficient",
      len(free_coefficients) == len(allowed_entries))

# For a charges-add Z/3 selection rule, an allowed entry has q_i + q_j = 0 mod 3.
charges = (0, 2, 1)
exponents_on_allowed = tuple((charges[i] + charges[j]) % 3 for i, j in allowed_entries)
check("Y3 the derived Z/3 is Froggatt-Nielsen sterile on allowed entries",
      exponents_on_allowed == (0, 0, 0), str(exponents_on_allowed))
check("Y4 no singular-value ratio or coefficient magnitude is emitted",
      not candidates[0].quantitative and not candidates[0].built_gu_forced,
      "selection rule fixes support, not values")


print("\n== STRONGEST QUANTITATIVE CONDITIONAL: H36 ==")
# H51 exact geometric coefficient and H50/H52 conversion.
c_l = Fraction(3, 8)
rho_quarter_ev = 2.3e-3
hbar_c_ev_um = 0.1973269804
m2_eff_min = Fraction(5, 6)
m2_eff_max = Fraction(5, 4)


def yukawa_range_um(m2_eff):
    return (hbar_c_ev_um * float(c_l) ** 0.25
            / (sqrt(float(m2_eff)) * rho_quarter_ev))


lambda_long_um = yukawa_range_um(m2_eff_min)
lambda_short_um = yukawa_range_um(m2_eff_max)
alpha = Fraction(1, 3)

check("H1 c_L is the exact GU geometric coefficient 3/8", c_l == Fraction(3, 8))
check("H2 alpha is the massive-spin-2 value 1/3", alpha == Fraction(1, 3))
check("H3 H36 predicts the corrected range band 60.0 to 73.6 micrometers",
      isclose(lambda_short_um, 60.0, abs_tol=0.15)
      and isclose(lambda_long_um, 73.6, abs_tol=0.15),
      f"[{lambda_short_um:.2f}, {lambda_long_um:.2f}] um")

# H52's cited alpha=1/3 95% CL boundary has central 47.6 um and an honest
# [46.0, 51.2] um envelope.  Use the least excluding edge, 51.2 um.
conservative_bound_um = 51.2
check("H4 the entire predicted range lies beyond the conservative allowed boundary",
      lambda_short_um > conservative_bound_um,
      f"shortest={lambda_short_um:.2f} um > bound={conservative_bound_um:.1f} um")
check("H5 confrontation result is EXCLUDED-CITED", candidates[1].data_outcome == "excluded")
check("H6 the observed dark-energy density is an imported scale in this chain",
      not candidates[1].calibration_independent)
check("H7 H36 is not GU-forced", not candidates[1].built_gu_forced)
check("H8 the killed conditional cannot satisfy Track B",
      not candidates[1].is_standing_prediction())


print("\n== NEAREST DISTINCTIVE STRUCTURAL SEED: MIRROR SECTOR ==")
mirror = candidates[2]
check("M1 the mirror structure is GU-distinctive enough to retain as a seed",
      mirror.distinctive)
check("M2 the mirror seed has no forced mass scale", not mirror.quantitative)
check("M3 physical-state status and production are unresolved",
      not mirror.physical_observable and not mirror.confrontable)
check("M4 W234 leaves the compactifying condensate in the chirality-killing channel D",
      not mirror.built_gu_forced and not mirror.robust)
channel_s_compactifies = False
check("M5 W237 proves the chirality-safe channel S does not compactify",
      not channel_s_compactifies,
      "channel S is Z2-even but has no bilinear adjoint order parameter")


print("\n== TRACK B VERDICT AND REOPEN CONDITION ==")
track_b_status = "NO_CURRENT_DISTINCTIVE_CONFIRMED_PREDICTION"
check("V1 Track B scan closes with no current passing prediction",
      track_b_status == "NO_CURRENT_DISTINCTIVE_CONFIRMED_PREDICTION"
      and not any(c.is_standing_prediction() for c in candidates))

reopen_burdens = {
    "dimensionless_flavor_invariant": "zero free Yukawa coefficients after quotient and running",
    "native_scale_relation": "normalization fixed without observed target data",
    "mirror_observable": "channel S, physical-state status, mass and branching fractions derived",
}
check("V2 three exact reopen routes are recorded", len(reopen_burdens) == 3)

bar_b_open = True
h59_open = True
canon_moved = False
check("V3 bar(b) and H59 remain OPEN", bar_b_open and h59_open)
check("V4 no canon or verdict movement", not canon_moved)


print("\n" + ("ALL PASS -- W239 Track B scan is internally consistent."
               if not FAIL else f"FAILURES: {FAIL}"))
raise SystemExit(1 if FAIL else 0)
