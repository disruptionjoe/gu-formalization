#!/usr/bin/env python3
"""Exact K123 native I1B h-containing cubic identifiability gate."""

from pathlib import Path
import json
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHECKS = []


def check(kind, label, condition):
    ok = bool(condition)
    CHECKS.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


print("A. EXACT RANK-TWO NATIVE COEFFICIENT DEFICIT")
t, h, v = sp.symbols("t h v")
a, b, norm = sp.symbols("a b N")
q_tt, q_th, q_tv, q_hh, q_hv, q_vv = sp.symbols(
    "q_tt q_th q_tv q_hh q_hv q_vv"
)
quadratic = (
    q_tt*t**2 + 2*q_th*t*h + 2*q_tv*t*v
    + q_hh*h**2 + 2*q_hv*h*v + q_vv*v**2
) / 2
known = quadratic + sp.Rational(8736, 6)*t**3 - sp.Rational(56, 6)*norm*t*v**2
missing = a*t*h**2/2 + b*t*h*v
completed = known + missing
origin = {t: 0, h: 0, v: 0}
variables = (t, h, v)

check("identifiability", "planted moving germ preserves stationarity",
      all(sp.diff(missing, x).subs(origin) == 0 for x in variables))
check("identifiability", "planted moving germ preserves the complete quadratic germ",
      all(sp.diff(missing, x, y).subs(origin) == 0 for x in variables for y in variables))
check("identifiability", "planted moving germ vanishes on the fixed-metric slice",
      sp.expand(missing.subs(h, 0)) == 0)
check("identifiability", "radial cubic remains 8736",
      sp.diff(completed, t, 3).subs(origin) == 8736)
check("identifiability", "radial-TT cubic remains minus 56 over 3 times the norm",
      sp.diff(completed, t, v, v).subs(origin) == -sp.Rational(56, 3)*norm)
check("identifiability", "missing first native target shifts by a",
      sp.diff(completed-known, t, h, h).subs(origin) == a)
check("identifiability", "missing second native target shifts by b",
      sp.diff(completed-known, t, h, v).subs(origin) == b)
target_map = sp.Matrix([
    sp.diff(missing, t, h, h).subs(origin),
    sp.diff(missing, t, h, v).subs(origin),
]).jacobian((a, b))
check("identifiability", "missing-jet to native-target map has rank two",
      target_map == sp.eye(2) and target_map.rank() == 2)
completion_1 = completed.subs({a: 1, b: 2})
completion_2 = completed.subs({a: 3, b: 5})
check("identifiability", "two completions agree on every fixed-metric cubic control",
      sp.expand((completion_1-completion_2).subs(h, 0)) == 0)
check("identifiability", "two admitted completions disagree on C_t_h_h",
      sp.diff(completion_1-completion_2, t, h, h).subs(origin) == -2)
check("identifiability", "two admitted completions disagree on C_t_h_v",
      sp.diff(completion_1-completion_2, t, h, v).subs(origin) == -3)


print("\nB. PRIMITIVE SOURCE-COORDINATE REDISTRIBUTION")
s, c, d, b2 = sp.symbols("s c d b2")
Crgg, Crgw, Crww, Hrw = sp.symbols("C_rgg C_rgw C_rww H_rw")
A_native = Crgg + 2*s*Crgw + s**2*Crww + b2*Hrw
B_native = Crgw + s*Crww
C_native = Crww

s_linear = s + c
Crgw_linear = Crgw - c*Crww
Crgg_linear = Crgg - 2*c*Crgw + c**2*Crww
A_linear = sp.expand(Crgg_linear + 2*s_linear*Crgw_linear + s_linear**2*Crww + b2*Hrw)
B_linear = sp.expand(Crgw_linear + s_linear*Crww)
check("coordinate", "linear connection reparametrization preserves native C_t_h_h",
      sp.expand(A_linear-A_native) == 0)
check("coordinate", "linear connection reparametrization preserves native C_t_h_v",
      sp.expand(B_linear-B_native) == 0)
check("coordinate", "linear connection reparametrization preserves native C_t_v_v",
      C_native == Crww)
check("coordinate", "linear reparametrization moves the primitive radial-metric-connection slot",
      sp.expand(Crgw_linear-Crgw) == -c*Crww)
check("coordinate", "linear reparametrization moves the primitive radial-metric-metric slot",
      sp.expand(Crgg_linear-Crgg) == -2*c*Crgw+c**2*Crww)

b2_nonlinear = b2 + d
Crgg_nonlinear = Crgg - d*Hrw
A_nonlinear = sp.expand(Crgg_nonlinear + 2*s*Crgw + s**2*Crww + b2_nonlinear*Hrw)
check("coordinate", "nonlinear connection reparametrization preserves native C_t_h_h",
      sp.expand(A_nonlinear-A_native) == 0)
check("coordinate", "nonlinear reparametrization trades primitive D3 against Hessian-times-D2F",
      Crgg_nonlinear != Crgg and b2_nonlinear != b2)
native_target_vector = sp.Matrix([A_native, B_native])
check("coordinate", "the h-containing native target has exactly two components",
      native_target_vector.shape == (2, 1))
primitive_to_native = sp.Matrix([A_native, B_native, C_native]).jacobian((Crgg, Crgw, Crww))
check("coordinate", "the frozen first-jet primitive-to-native map is triangular and invertible",
      primitive_to_native.det() == 1)


print("\nC. PREBOUNDARY EXACT-FIELD-SPACE SHIFT CONTROL")
gamma = sp.symbols("gamma")
boundary_generator = gamma*t*h*v
p_t = sp.diff(boundary_generator, t)
p_h = sp.diff(boundary_generator, h)
p_v = sp.diff(boundary_generator, v)
check("preboundary", "exact boundary generator shifts all three Cartan columns",
      (p_t, p_h, p_v) == (gamma*h*v, gamma*t*v, gamma*t*h))
check("preboundary", "t-h field-space curl of the exact shift vanishes",
      sp.diff(p_h, t)-sp.diff(p_t, h) == 0)
check("preboundary", "t-v field-space curl of the exact shift vanishes",
      sp.diff(p_v, t)-sp.diff(p_t, v) == 0)
check("preboundary", "h-v field-space curl of the exact shift vanishes",
      sp.diff(p_v, h)-sp.diff(p_h, v) == 0)


print("\nD. REPOSITORY CUSTODY AND SERIALIZATION AUDIT")
k122 = (ROOT / "explorations/conditional-build/selected-k122-native-i1b-cubic-and-preboundary-owner-decomposition-2026-08-15.md").read_text()
source_hessian = (ROOT / "explorations/conditional-build/selected-action-source-variable-hessian-and-diffeomorphism-lift-2026-08-06.md").read_text()
second_jets = (ROOT / "explorations/conditional-build/selected-action-second-soldering-observation-jets-2026-08-06.md").read_text()
moving_gimmel = (ROOT / "explorations/conditional-build/moving-gimmel-hodge-frame-owner-2026-08-06.md").read_text()
ward = (ROOT / "explorations/conditional-build/selected-action-ward-completion-identifiability-2026-08-06.md").read_text()
raw_lc = (ROOT / "explorations/conditional-build/selected-cubic-gauge-rotated-lc-ward-owner-2026-08-06.md").read_text()
k77 = (ROOT / "explorations/conditional-build/selected-k77-zorro-first-action-euler-gate-2026-08-14.md").read_text()
artifact = (ROOT / "explorations/conditional-build/selected-k123-native-i1b-h-containing-cubic-identifiability-and-evaluator-gate-2026-08-15.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k123-native-i1b-h-containing-cubic-identifiability-and-evaluator-gate.json").read_text())
current = (ROOT / "CURRENT-STATE.yaml").read_text()
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()

check("repo", "K122 fixes the radial and fixed-metric radial-TT cubics",
      "D3 I1B[t,t,t] = 8736" in k122 and "-56/3" in k122)
check("repo", "K122 freezes the three primitive evaluation packet",
      "these three evaluations" in k122 and "D2I1B[Pbar,Q_hh]" in k122)
check("repo", "source-variable predecessor leaves the full I1B derivative action open",
      "FULL_I1B_DERIVATIVE_CURVATURE_OPEN" in source_hessian)
check("repo", "second-jet predecessor leaves direct selected-action coefficients open",
      "DIRECT_SELECTED_ACTION_COEFFICIENT_EXPANSION_OPEN" in second_jets)
check("repo", "moving-gimmel predecessor leaves selected-action composition open",
      "SELECTED_ACTION_COMPOSITION_OPEN" in moving_gimmel)
check("repo", "Ward predecessor leaves 21 quotient-form directions unselected",
      "21-dimensional affine space" in ward and "same first-layer action `I1B`" in ward)
check("repo", "old exact LC slice has dimension 24",
      "24-dimensional" in raw_lc and "fixed-`varpi` partial-coordinate representative" in raw_lc)
check("repo", "full K77 connection carrier has 1274 directions",
      "1274" in raw_lc and "full-K77" in raw_lc)
check("repo", "printed K77 action architecture is retained",
      "bar F = F_B + (1/2)D_B T + (1/3)T^2" in k77)
check("repo", "raw 14-over-3 import remains explicitly prohibited",
      "not a native `C_t_h_h` coefficient" in raw_lc)
check("artifact", "source-native comparator routing notice is present",
      "GU-COMPARATOR-ROUTING — scope before inference" in artifact)
check("artifact", "artifact states the rank-two evidence deficit",
      "rank two" in artifact and "does **not** say" in artifact)
check("registry", "registry serializes deficit rank two without adding coefficients",
      registry["identifiability"]["deficit_rank"] == 2
      and registry["identifiability"]["physical_free_coefficients_added"] == 0)
check("registry", "registry names the common full-14D evaluator",
      registry["required_operator"]["name"] == "O_K123")
check("repo", "current state advances to the K123 evaluator obstruction",
      "K123" in current and "rank two" in current.lower())
check("repo", "context records K124 principal closure and routes K125",
      "K124" in context[:15000] and "K125" in context[:15000]
      and "C_t_h_h" in context[:15000])

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
raise SystemExit(1 if failures else 0)
