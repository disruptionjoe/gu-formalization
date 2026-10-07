#!/usr/bin/env python3
"""Data-mutation probe for K1371."""
import copy, json
from pathlib import Path

D = json.loads((Path(__file__).resolve().parents[2] / "lab/process/k1371-gauss-source-hminus1-obstruction.json").read_text())

def validate(x):
    c, f, e, q = x["countersequence"], x["fourier_certificate"], x["energy_certificate"], x["decision"]
    errors = []
    if "|u_N|^2-1" not in c["gauss_density"]: errors.append("density")
    if "integral rho_N=0" not in c["neutrality"]: errors.append("neutrality")
    if "(27/64)^2" not in f["hminus1_lower"]: errors.append("lower")
    if "linearly in N" not in f["divergence"]: errors.append("divergence")
    if "<3" not in e["spatial_gradient_bound"]: errors.append("energy")
    if not q["zero_mean_countersequence_constructed"]: errors.append("construction")
    if not q["gauss_density_hminus1_unbounded"]: errors.append("unboundedness")
    if q["k1366_energy_controls_nonlinear_gauss_map"]: errors.append("sufficiency overclaim")
    if q["global_nonlinear_evolution_proved"]: errors.append("evolution overclaim")
    if q["source_action_identified"]: errors.append("source overclaim")
    return errors

assert not validate(D), validate(D)
mutations = [
    ("density", lambda x: x["countersequence"].__setitem__("gauss_density", "constant")),
    ("neutrality", lambda x: x["countersequence"].__setitem__("neutrality", "unknown")),
    ("lower", lambda x: x["fourier_certificate"].__setitem__("hminus1_lower", "none")),
    ("divergence", lambda x: x["fourier_certificate"].__setitem__("divergence", "bounded")),
    ("energy", lambda x: x["energy_certificate"].__setitem__("spatial_gradient_bound", "unknown")),
    ("construction", lambda x: x["decision"].__setitem__("zero_mean_countersequence_constructed", False)),
    ("unboundedness", lambda x: x["decision"].__setitem__("gauss_density_hminus1_unbounded", False)),
    ("sufficiency overclaim", lambda x: x["decision"].__setitem__("k1366_energy_controls_nonlinear_gauss_map", True)),
    ("evolution overclaim", lambda x: x["decision"].__setitem__("global_nonlinear_evolution_proved", True)),
    ("source overclaim", lambda x: x["decision"].__setitem__("source_action_identified", True))
]
for i, (label, mutate) in enumerate(mutations, 1):
    x = copy.deepcopy(D); mutate(x); errors = validate(x); assert errors, label
    print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
