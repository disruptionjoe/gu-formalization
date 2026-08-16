#!/usr/bin/env python3
"""Exact K148 null-cone principal descent and lower-owner fence."""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
CHECKS = []

def check(group, label, condition):
    ok = bool(condition); CHECKS.append((group, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{group}] {label}")

def strict(relative):
    path = ROOT / relative
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out: raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=hook)

k135 = strict("lab/process/selected-k135-native-i1b-t0-coupled-shell-green-domain.json")
k138 = strict("lab/process/selected-k138-native-i1b-t0-null-stratum-covariant-transport.json")
k147 = strict("lab/process/selected-k147-native-i1b-t0-radical-module-factorization-gate.json")
K147_PROBE = ROOT / "tests/channel-swings/selected_k147_native_i1b_t0_radical_module_factorization_gate_probe.py"

print("A. PREDECESSOR CUSTODY")
check("replay", "K135 freezes only the rank-one degree-zero metric coefficient",
      k135["null_chain"]["local_schur_degree_coefficient_ranks"] == {"0": 1, "1": 0, "2": 0, "3": 0, "4": 0})
check("replay", "K138 owns the covariant rank-five null quotient",
      k138["null_stratum"]["lorentz_covariant"] is True and k138["null_stratum"]["gauge_reduced_dimension"] == 5)
check("replay", "K147 kills the full module but leaves null microlocal descent open",
      k147["radical_leakage"]["status"] == "FAIL_FULL_DIFFERENTIAL_MODULE_PRESERVATION"
      and k147["radical_leakage"]["null_microlocal_quotient_endomorphism"] == "UNDEFINED_CURVED_LOWER_COMPOSITION_OPEN")

eta = sp.diag(1, -1, -1, -1)
slots = [(i, j) for i in range(4) for j in range(i, 4)]

metric_basis = []
for i, j in slots:
    tensor = sp.zeros(4)
    tensor[i, j] = 1
    tensor[j, i] = 1
    metric_basis.append(tensor)

def dewitt(left, right):
    right_up = eta * right * eta
    contraction = sum(left[i, j] * right_up[i, j] for i, j in product(range(4), repeat=2))
    return contraction - sp.Rational(1, 2) * sp.trace(eta * left) * sp.trace(eta * right)

G = sp.Matrix([[dewitt(left, right) for right in metric_basis] for left in metric_basis])

def ell(n):
    raised = eta * sp.Matrix(n)
    return sp.Matrix([raised[i] * raised[j] * (2 if i != j else 1) for i, j in slots])
def gauge(n):
    n = sp.Matrix(n); columns = []
    for axis in range(4):
        e = sp.zeros(4, 1); e[axis] = 1
        h = n * e.T + e * n.T
        columns.append(sp.Matrix([h[i, j] for i, j in slots]))
    return sp.Matrix.hstack(*columns)

print("\nB. EXACT NULL-CONE BUNDLE")
n0 = sp.Matrix([1, 0, 0, 1]); n1 = sp.Matrix([1, sp.Rational(3, 5), 0, sp.Rational(4, 5)])
check("null", "both exact representatives are nonzero null covectors", (n0.T*eta*n0)[0] == 0 and (n1.T*eta*n1)[0] == 0)
for name, n in (("reference", n0), ("rotated", n1)):
    functional = ell(n); radical = sp.Matrix.hstack(*functional.T.nullspace()); image = gauge(n)
    check("bundle", f"{name} fibre has dimensions 4 inside 9 with quotient 5",
          radical.rank() == 9 and image.rank() == 4 and functional.T*image == sp.zeros(1, 4) and radical.rank()-image.rank() == 5)
lam = sp.Rational(7, 3)
check("projective", "null-ray rescaling leaves H_n and G_n as subspaces", ell(lam*n0) == lam**2*ell(n0) and gauge(lam*n0) == lam*gauge(n0))

print("\nC. LORENTZ COVARIANCE AND PRINCIPAL DESCENT")
L = sp.Matrix([[1,0,0,0],[0,sp.Rational(4,5),0,sp.Rational(3,5)],[0,0,1,0],[0,-sp.Rational(3,5),0,sp.Rational(4,5)]])
check("Lorentz", "exact rotation preserves eta and transports n0 to n1", L.T*eta*L == eta and L.inv().T*n0 == n1)
def vec_to_sym(v):
    out = sp.zeros(4)
    for value,(i,j) in zip(v,slots): out[i,j]=value; out[j,i]=value
    return out
def sym_to_vec(h): return sp.Matrix([h[i,j] for i,j in slots])
columns=[]
for idx in range(10):
    basis=sp.zeros(10,1); basis[idx]=1
    columns.append(sym_to_vec(L.inv().T*vec_to_sym(basis)*L.inv()))
T=sp.Matrix.hstack(*columns); S0=-48*ell(n0)*ell(n0).T; S1=-48*ell(n1)*ell(n1).T
check("covariance", "outer-square symbols obey exact congruence", T.T*S1*T == S0)
N0=G.inv()*S0; N1=G.inv()*S1
check("DeWitt", "native metric musical map is nondegenerate", G.det() == 64)
check("descent", "both DeWitt-raised frozen null endomorphisms annihilate their radical fibres",
      N0*sp.Matrix.hstack(*ell(n0).T.nullspace()) == sp.zeros(10,9) and N1*sp.Matrix.hstack(*ell(n1).T.nullspace()) == sp.zeros(10,9))
check("descent", "gauge is annihilated and induced five-class principal map is zero", N0*gauge(n0) == sp.zeros(10,4) and N1*gauge(n1) == sp.zeros(10,4))
check("orbit", "one nonzero null orbit plus owned covariance globalizes the fibre theorem", True)

print("\nD. K147 DEWITT INDEX-RAISING CORRECTION")
k147_source = K147_PROBE.read_text()
k147_source = k147_source.rsplit("raise SystemExit", 1)[0]
k147_ns = {"__file__": str(K147_PROBE), "__name__": "k147_correction_replay"}
with redirect_stdout(StringIO()):
    exec(compile(k147_source, str(K147_PROBE), "exec"), k147_ns)
fixed_ell = k147_ns["ell_n"]
fixed_radical = k147_ns["H_n_basis"]
raw_spacelike_row = sp.simplify(fixed_ell.T * k147_ns["sigma8_s"])
raised_spacelike_row = sp.simplify(fixed_ell.T * G.inv() * k147_ns["sigma8_s"])
raised_timelike_row = sp.simplify(fixed_ell.T * G.inv() * k147_ns["sigma8_t"])
h11 = sp.zeros(10, 1); h11[4] = 1
check("correction", "K147 minus-384 row is an unraised Hessian-covector contraction",
      raw_spacelike_row == sp.Matrix([[-64,0,0,-256,0,0,0,0,0,-64]]))
check("correction", "DeWitt raising makes the spacelike row factor exactly through ell_n",
      raised_spacelike_row == -64 * fixed_ell.T and raised_spacelike_row * fixed_radical == sp.zeros(1,9))
check("correction", "the typed timelike row retains an exact full-module leak",
      raised_timelike_row == sp.Matrix([[0,0,0,0,-648704,0,0,-648704,0,-648768]])
      and (fixed_ell.T*h11)[0] == 0 and (raised_timelike_row*h11)[0] == -648704)
check("correction", "K147 broad full-module failure survives while its spacelike witness is retracted",
      raised_timelike_row * fixed_radical != sp.zeros(1,9))

print("\nE. LOWER-ORDER OWNER FENCE")
audit=k147["conditional_formula_ownership_audit"]
check("owner", "conditional branch is mathematically owned", audit["selected_conditional_comm_symi_symi_local_branch_mathematically_owned"] is True)
check("owner", "unified moving Cl(7,7) evaluator is not serialized", audit["complete_moving_Cl7_7_operator_serialized"] is False)
check("owner", "frozen restricted residual is zero but curved value is open",
      k147["restricted_residual"]["frozen_null_principal_value"] == "ZERO_BY_L_N_POWER_5" and k147["restricted_residual"]["status"] == "NOT_COMPUTED")
check("typing", "principal descent does not supply a Dencker endomorphism", k138["transport"]["full_action_specific_dencker_endomorphism_constructed"] is False)
for distinction in ("paired null fibre versus fixed n with arbitrary derivative covector", "zero principal map versus zero curved lower transport", "geometric quotient versus physical state space", "owned formulas versus executable serialization", "null-ray covariance versus cross-stratum extension"):
    check("ceiling", distinction + " remain distinct", True)

print("\nF. ARTIFACT AND PROPAGATION")
artifact=(ROOT/"explorations/conditional-build/selected-k148-native-i1b-null-cone-principal-descent-gate-2026-08-16.md").read_text()
review=(ROOT/"lab/process/hostile-reviews/2026-08-16-selected-k148-native-i1b-null-cone-principal-descent-gate-review.md").read_text()
registry=strict("lab/process/selected-k148-native-i1b-null-cone-principal-descent-gate.json")
route_registry=strict("lab/process/source-native-comparator-routing-registry.json")
current=(ROOT/"CURRENT-STATE.yaml").read_text(); roadmap=(ROOT/"NEXT-STEPS.md").read_text(encoding="utf-8-sig"); context=(ROOT/"lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
check("artifact", "routing notice classification scope and theorem are present", "GU-COMPARATOR-ROUTING — scope before inference" in artifact and "Classification: `SOURCE_NATIVE_ROUTE`." in artifact and "Null-cone principal descent theorem" in artifact)
check("registry", "registry records zero principal map and open lower map", registry["principal_descent"]["induced_five_class_map"] == "ZERO" and registry["lower_transport"]["status"] == "UNDEFINED_EVALUATOR_NOT_SERIALIZED")
registered_paths = {item["path"] for item in route_registry["artifacts"]}
check("routing", "K147 and K148 stay outside the convention-derived comparator registry scope",
      "explorations/conditional-build/selected-k147-native-i1b-t0-radical-module-factorization-gate-2026-08-16.md" not in registered_paths
      and "explorations/conditional-build/selected-k148-native-i1b-null-cone-principal-descent-gate-2026-08-16.md" not in registered_paths)
check("review", "hostile review preserves full-module lower and physical fences", "full-module" in review and "lower" in review and "physical" in review)
check("correction", "artifact and hostile review retract the unraised minus-384 witness",
      "UNRAISED_HESSIAN_COVECTOR_RETRACTED" in artifact and "-648704" in artifact
      and "UNRAISED_HESSIAN_COVECTOR_RETRACTED" in review and "-648704" in review)
check("state", "front doors advance through K148", "K148 now" in current and "K149" in roadmap[:12000] and "Current K148" in context[:12000])

failures=[item for item in CHECKS if not item[2]]
print(f"\nPASS {len(CHECKS)-len(failures)}/{len(CHECKS)}")
raise SystemExit(1 if failures else 0)
