#!/usr/bin/env python3
"""Historical K116 frame audit; concrete action target superseded by K117."""

from pathlib import Path
import json
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
checks = []


def check(kind, label, condition):
    ok = bool(condition)
    checks.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


a, b, u, u0 = sp.symbols("a b u u0", nonzero=True, real=True)
Kx = sp.Matrix([[a, 1], [1, 0]])
M0x = sp.Matrix([[0, 0], [0, b]])
M1x = sp.Matrix([[1, 0], [0, 0]])
U = sp.Matrix([[1, 1], [0, -a]])
Kq = sp.simplify(U.T * Kx * U)
M0q = sp.simplify(U.T * M0x * U)
M1q = sp.simplify(U.T * M1x * U)

free_source = (ROOT / "explorations/conditional-build/selected-branch-bv-tt-and-curvature-vev-flrw-2026-08-05.md").read_text()
interaction_source = (ROOT / "explorations/conditional-build/first-interaction-krein-and-global-zero-mode-horn-2026-08-05.md").read_text()
check("source", "free source records raw K and M together", "K=\\begin{pmatrix}\\alpha&1\\\\1&0\\end{pmatrix}" in free_source and "M=\\begin{pmatrix}0&0\\\\0&b\\end{pmatrix}" in free_source)
check("source", "interaction source explicitly moves to P eigenbasis", "In the `P`-eigenbasis" in interaction_source and "`h=q_0+q_m`" in interaction_source)
check("source", "free eigenvector matrix is invertible", U.det() == -a)
check("exact", "mode kinetic congruence", Kq == sp.diag(a, -a))
check("exact", "mode free mass congruence", M0q == sp.diag(0, a**2 * b))
check("exact", "metric interaction becomes vvT in mode frame", M1q == sp.ones(2))
check("planted", "raw interaction is not mode interaction", M1x != M1q)
check("planted", "raw kinetic matrix is not mode kinetic matrix", Kx != Kq)

Mx = M0x + u * M1x
Lx = sp.simplify(Kx.inv() * Mx)
Delta = sp.factor(sp.trace(Lx) ** 2 - 4 * Lx.det())
check("exact", "correct raw dynamics", Lx == sp.Matrix([[0, b], [u, -a * b]]))
check("exact", "correct discriminant", Delta == b * (a**2 * b + 4 * u))

Mq = M0q + u * M1q
Lq = sp.simplify(Kq.inv() * Mq)
check("exact", "raw and mode dynamics are similar", sp.simplify(Lq - U.inv() * Lx * U) == sp.zeros(2))
check("exact", "mode discriminant agrees", sp.factor(sp.trace(Lq) ** 2 - 4 * Lq.det()) == Delta)

mixed_L = sp.simplify(Kx.inv() * (M0x + u * sp.ones(2)))
mixed_delta = sp.factor(sp.trace(mixed_L) ** 2 - 4 * mixed_L.det())
old_delta = (b + u) * (a**2 * b + (a - 2) ** 2 * u)
check("historical", "mixed-frame pencil reproduces historical discriminant", sp.expand(mixed_delta - old_delta) == 0)
check("planted", "historical discriminant differs generically", sp.expand(old_delta - Delta) != 0)
check("planted", "exact rational control distinguishes discriminants", old_delta.subs({a: sp.Rational(3, 2), b: 2, u: 1}) != Delta.subs({a: sp.Rational(3, 2), b: 2, u: 1}))

s = sp.sqrt(Delta)
N = sp.Matrix([[a * b, 2 * b], [2 * u, -a * b]])
C = N / s
check("exact", "C squares to identity", sp.simplify(C * C - sp.eye(2)) == sp.zeros(2))
check("exact", "C commutes with dynamics", sp.simplify(C * Lx - Lx * C) == sp.zeros(2))
check("exact", "C is K self-adjoint", sp.simplify(C.T * Kx - Kx * C) == sp.zeros(2))
majorant_num = sp.simplify(Kx * N)
check("exact", "majorant numerator", majorant_num == sp.Matrix([[a**2 * b + 2 * u, a * b], [a * b, 2 * b]]))
check("exact", "majorant determinant is discriminant", sp.factor(majorant_num.det()) == Delta)

H = sp.Matrix([[1, 0], [-a, -1]])
check("exact", "H is an involution", H * H == sp.eye(2))
check("exact", "H is K skew", H.T * Kx + Kx * H == sp.zeros(2))
check("exact", "mode generator is sigma_x", sp.simplify(U.inv() * H * U) == sp.Matrix([[0, 1], [1, 0]]))

dCdu = C.diff(u)
A = sp.simplify(sp.Rational(1, 2) * C * dCdu)
check("exact", "correct spectral connection", sp.simplify(A - H / (a**2 * b + 4 * u)) == sp.zeros(2))
check("exact", "connection preserves K", sp.simplify(A.T * Kx + Kx * A) == sp.zeros(2))
check("exact", "connection parallelizes C", sp.simplify(dCdu + A * C - C * A) == sp.zeros(2))

L0 = sp.simplify(Kx.inv() * M0x)
L1 = sp.simplify(Kx.inv() * M1x)
comm = sp.simplify(L0 * L1 - L1 * L0)
check("exact", "correct free-interaction commutator", comm == b * H)
check("exact", "commutator determinant", sp.factor(comm.det()) == -b**2)
check("control", "alpha one commutator remains rank two", comm.subs(a, 1).rank() == 2)
check("control", "alpha one connection is nonzero", A.subs(a, 1) != sp.zeros(2))

t = sp.symbols("t", real=True)
T = sp.cosh(t) * sp.eye(2) - sp.sinh(t) * H
check("exact", "closed exponential uses H squared identity", sp.simplify(T * (sp.cosh(t) * sp.eye(2) + sp.sinh(t) * H)) == sp.eye(2))
check("exact", "transport determinant one", sp.simplify(T.det()) == 1)
check("exact", "transport preserves K", sp.simplify(T.T * Kx * T - Kx) == sp.zeros(2))

artifact = (ROOT / "explorations/conditional-build/selected-k116-rsap-tt-frame-consistency-correction-and-transport-gate-2026-08-15.md").read_text()
registry_path = ROOT / "lab/process/selected-k116-rsap-tt-frame-consistency-correction-and-transport-gate.json"
registry = json.loads(registry_path.read_text())
check("repo", "artifact names raw and mode frames", "raw x frame" in artifact and "mode q frame" in artifact)
check("repo", "artifact records correction", "K110--K115" in artifact and "superseded" in artifact.lower())
check("repo", "registry records historical mismatch", registry["frame_custody"]["historical_error"] == "RAW_K_AND_M0_COMBINED_WITH_MODE_M1")
check("repo", "registry next gate uses corrected target", "CORRECTED_H_dpsi" in registry["next_gate"])
check("repo", "twenty-lens vote is complete", sum(registry["twenty_lens_vote"][k] for k in ("FRAME", "SALVAGE", "ACTION", "PARK")) == 20 == registry["twenty_lens_vote"]["total"])
check("repo", "reverse scaffold starts from corrected superposition hypothesis", "CORRECTED_H_dpsi" in registry["reverse_scaffold"]["superposition_hypothesis"] and registry["reverse_scaffold"]["next_swings"][0].startswith("K117_"))

current_state = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text()
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
research_status = (ROOT / "RESEARCH-STATUS.md").read_text()
check(
    "repo",
    "current question has advanced through K118 to action-layer and two-jet selection",
    "action layer" in current_state.lower() and "two-jet" in current_state.lower(),
)
check("repo", "roadmap preserves K116 as superseded predecessor", "K116 CORRECTS THE TT TRANSPORT TARGET" in roadmap and "K117" in roadmap[:3000])
check("repo", "agent context blocks historical owner census", "Do not run an owner census against" in context)
check("repo", "research status records downgrade", "K116 TT frame-consistency correction" in research_status and "superseded in full" in research_status)
check("repo", "K116 artifact records K117 symbol-order correction", "K117 SYMBOL-ORDER CORRECTION" in artifact)

for rel in [
    "explorations/conditional-build/first-perturbative-background-c-operator-2026-08-05.md",
    "explorations/conditional-build/selected-k110-rsap-tt-c-green-domain-composition-gate-2026-08-15.md",
    "explorations/conditional-build/selected-k111-rsap-tt-spectral-transport-connection-owner-gate-2026-08-15.md",
    "explorations/conditional-build/selected-k112-rsap-spectral-connection-variational-owner-port-2026-08-15.md",
    "explorations/conditional-build/selected-k113-rsap-tt-spectral-transport-normal-form-and-boundary-support-gate-2026-08-15.md",
    "explorations/conditional-build/selected-k114-rsap-tt-alpha-normalization-invariant-owner-gate-2026-08-15.md",
    "explorations/conditional-build/selected-k115-rsap-tt-moving-jacobian-classification-and-gap-wall-gate-2026-08-15.md",
]:
    text = (ROOT / rel).read_text()
    check("repo", f"supersession notice: {Path(rel).name}", "K116 FRAME-CONSISTENCY CORRECTION" in text)

for rel in [
    "tests/channel-swings/first_perturbative_background_c_operator_probe.py",
    "tests/channel-swings/selected_k110_rsap_tt_c_green_domain_composition_gate_probe.py",
    "tests/channel-swings/selected_k111_rsap_tt_spectral_transport_connection_owner_gate_probe.py",
    "tests/channel-swings/selected_k112_rsap_spectral_connection_variational_owner_port_probe.py",
    "tests/channel-swings/selected_k113_rsap_tt_spectral_transport_normal_form_and_boundary_support_gate_probe.py",
    "tests/channel-swings/selected_k114_rsap_tt_alpha_normalization_invariant_owner_gate_probe.py",
    "tests/channel-swings/selected_k115_rsap_tt_moving_jacobian_classification_and_gap_wall_gate_probe.py",
]:
    text = (ROOT / rel).read_text()
    check("repo", f"historical probe label: {Path(rel).name}", "superseded" in text[:500].lower())

failures = [item for item in checks if not item[2]]
print(f"\nTOTAL {len(checks)}  FAILURES {len(failures)}")
raise SystemExit(1 if failures else 0)
