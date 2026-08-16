#!/usr/bin/env python3
"""Exact K117 TT symbol-order custody and moving-Hessian gate."""

from pathlib import Path
import json
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHECKS = []


def check(kind, label, condition):
    ok = bool(condition)
    CHECKS.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


a, b, d, t, z = sp.symbols("a b d t z", nonzero=True, real=True)
u = sp.symbols("u", real=True)
Ehh = sp.Matrix([[1, 0], [0, 0]])
K0 = sp.Matrix([[a, 1], [1, 0]])
M0 = sp.Matrix([[0, 0], [0, b]])
J0 = z * K0 + M0

owner = (ROOT / "explorations/conditional-build/selected-cubic-reduced-numerator-completion-fork-2026-08-05.md").read_text()
first = (ROOT / "explorations/conditional-build/first-interaction-krein-and-global-zero-mode-horn-2026-08-05.md").read_text()
k116 = (ROOT / "explorations/conditional-build/selected-k116-rsap-tt-frame-consistency-correction-and-transport-gate-2026-08-15.md").read_text()
check("source", "owner states fixed-symbol hh response", "delta J_{hh}(z)=d z" in owner and "fixed TT symbol" in owner)
check("source", "predecessor states Einstein coefficient replacement", "a -> a+beta theta" in first)
check("source", "owner keeps full moving third derivative open", "CONSTRUCT_FULL_MOVING_D3_I_SELECTED" in owner)

dJ_hh = d * z * Ehh
dJ_mass = u * Ehh
check("order", "inherited response is principal-order z dependent", dJ_hh.diff(z) == d * Ehh)
check("order", "inherited response vanishes at zero symbol", dJ_hh.subs(z, 0) == sp.zeros(2))
check("planted", "K116 mass insertion does not vanish at zero symbol", dJ_mass.subs(z, 0) != sp.zeros(2))
check("planted", "background-independent u cannot identify the two polynomials", sp.Poly(dJ_hh[0, 0] - dJ_mass[0, 0], z).degree() == 1)

r = a + d * t
K = sp.Matrix([[r, 1], [1, 0]])
Jhh = z * K + M0
L = sp.simplify(K.inv() * M0)
C = sp.Matrix([[1, 2 / r], [0, -1]])
majorant = sp.simplify(K * C)
check("exact", "hh-only pencil changes K not M", sp.simplify(Jhh.diff(t) - dJ_hh) == sp.zeros(2))
check("exact", "normalized lower-order dynamics", sp.simplify(L - sp.Matrix([[0, b], [0, -r * b]])) == sp.zeros(2))
check("exact", "spectral involution squares to one", sp.simplify(C * C - sp.eye(2)) == sp.zeros(2))
check("exact", "spectral involution commutes with dynamics", sp.simplify(C * L - L * C) == sp.zeros(2))
check("exact", "spectral involution is K self-adjoint", sp.simplify(C.T * K - K * C) == sp.zeros(2))
check("exact", "majorant formula", majorant == sp.Matrix([[r, 1], [1, 2 / r]]))
check("exact", "majorant determinant one", sp.simplify(majorant.det()) == 1)
check("exact", "characteristic discriminant is one-wall square", sp.factor(sp.trace(L) ** 2 - 4 * L.det()) == b**2 * r**2)
check("exact", "hh-only eigenvalues are zero and minus rb", sp.simplify(L.det()) == 0 and sp.simplify(sp.trace(L) + r * b) == 0)
check("control", "free point recovers the original P", sp.simplify(C.subs(t, 0) - sp.Matrix([[1, 2 / a], [0, -1]])) == sp.zeros(2))

dr = sp.symbols("dr", nonzero=True, real=True)
dK = K.diff(t) * (dr / d)
dC = C.diff(t) * (dr / d)
Jdiag = sp.diag(1, -1)
Astar = Jdiag * dr / (2 * r)
check("connection", "Astar is K compatible", sp.simplify(dK - (Astar.T * K + K * Astar)) == sp.zeros(2))
check("connection", "Astar parallelizes C", sp.simplify(dC + Astar * C - C * Astar) == sp.zeros(2))

p, q, s, w = sp.symbols("p q s w")
Ag = sp.Matrix([[p, q], [s, w]])
eqs = list(dK - (Ag.T * K + K * Ag)) + list(dC + Ag * C - C * Ag)
solution = sp.solve(eqs, (p, q, s, w), dict=True)
check("connection", "simultaneous compatibility fixes all four entries uniquely", solution == [{p: dr/(2*r), q: 0, s: 0, w: -dr/(2*r)}])

rp, r0 = sp.symbols("rp r0", positive=True)
K_at_rp = sp.Matrix([[rp, 1], [1, 0]])
C_at_rp = sp.Matrix([[1, 2 / rp], [0, -1]])
T = sp.diag(sp.sqrt(r0 / rp), sp.sqrt(rp / r0))
K_at_r0 = sp.Matrix([[r0, 1], [1, 0]])
C_at_r0 = sp.Matrix([[1, 2 / r0], [0, -1]])
check("transport", "parallel transport determinant one", sp.simplify(T.det()) == 1)
check("transport", "transport carries K(r) to K(r0)", sp.simplify(T.T * K_at_rp * T - K_at_r0) == sp.zeros(2))
check("transport", "transport intertwines C", sp.simplify(T.inv() * C_at_rp * T - C_at_r0) == sp.zeros(2))

B = sp.simplify(K.inv() * dK)
Alit = B / 2
Cdefect = sp.simplify(dC + Alit * C - C * Alit)
mismatch = sp.simplify(B - 2 * Astar)
check("literal", "literal normalized first-order coefficient", B == sp.Matrix([[0, 0], [dr, 0]]))
check("literal", "literal half-coefficient is metric compatible", sp.simplify(dK - (Alit.T * K + K * Alit)) == sp.zeros(2))
check("literal", "literal connection fails C compatibility", Cdefect != sp.zeros(2))
check("literal", "first-order mismatch has nonzero determinant", sp.factor(mismatch.det()) == -dr**2 / r**2)
check("control", "mismatch disappears only on constant background", mismatch.subs(dr, 0) == sp.zeros(2))

scale = 1 + d * t / (2 * a)
S = sp.diag(scale, 1)
Jfr = sp.simplify(S.T * J0 * S)
dJfr0 = sp.simplify(Jfr.diff(t).subs(t, 0))
expected_fr = sp.Matrix([[d * z, d * z / (2 * a)], [d * z / (2 * a), 0]])
check("fork", "field-redefinition tangent has expected full-pencil response", dJfr0 == expected_fr)
check("fork", "two completions share inherited hh entry", dJfr0[0, 0] == dJ_hh[0, 0])
check("fork", "two completions differ in unmeasured hv entry", dJfr0[0, 1] != dJ_hh[0, 1])
Kfr = sp.simplify(S.T * K0 * S)
Mfr = sp.simplify(S.T * M0 * S)
Lfr = sp.simplify(Kfr.inv() * Mfr)
check("fork", "field-redefinition dynamics is similar to free dynamics", sp.simplify(Lfr - S.inv() * (K0.inv() * M0) * S) == sp.zeros(2))
check("fork", "field-redefinition discriminant stays fixed", sp.factor(sp.trace(Lfr)**2 - 4 * Lfr.det()) == a**2 * b**2)
check("fork", "hh-only massive pole moves", sp.simplify(sp.trace(L) + r * b) == 0 and sp.simplify(sp.trace(L).diff(t) + d * b) == 0)
check("planted", "fixed hh entry does not select a unique spectrum", sp.trace(Lfr).diff(t) == 0 and sp.trace(L).diff(t) != 0)

artifact = (ROOT / "explorations/conditional-build/selected-k117-rsap-tt-symbol-order-custody-and-moving-hessian-gate-2026-08-15.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k117-rsap-tt-symbol-order-custody-and-moving-hessian-gate.json").read_text())
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
status = (ROOT / "RESEARCH-STATUS.md").read_text()
check("repo", "artifact states symbol-order correction", "The missing symbol" in artifact and "d z E_hh" in artifact)
check("repo", "registry leaves full selected pencil unselected", registry["completion_fork"]["full_selected_action_pencil"] == "NOT_SELECTED")
check(
    "repo",
    "current question has advanced through K120 to scalar-bridge selection",
    "scalar bridge" in current.lower() and "two-jet" in current.lower(),
)
check("repo", "roadmap preserves K117 beneath current K120", "K120" in roadmap[:3000] and "K117" in roadmap and "symbol" in roadmap.lower())
check("repo", "context blocks K116 action-target reuse", "K116" in context[:5000] and "differential order" in context[:5000])
check("repo", "research status records K117 correction", "K117 TT symbol-order" in status)
check("repo", "K116 carries nearby K117 supersession notice", "K117 SYMBOL-ORDER CORRECTION" in k116)
check("repo", "reverse scaffold routes K118 to full moving owner", registry["reverse_scaffold"]["next_swings"][0] == "K118_FULL_MOVING_D3I_OWNER")

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
raise SystemExit(1 if failures else 0)
