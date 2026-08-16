#!/usr/bin/env python3
"""Exact K128 T=0 coupled-Hessian, derivative-order, and Schur gate."""

from pathlib import Path
import json
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHECKS = []


def check(kind, label, condition):
    ok = bool(condition)
    CHECKS.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


# Universal local action germ for I1B in native independent coordinates:
# x is a metric direction and y is a distortion/radial direction.  F(0)=0 is
# the K127 Ricci-flat translation stationarity condition.
x, y = sp.symbols("x y")
A, B, C0, C1, Q = sp.symbols("A B C0 C1 Q")
F = A*x + B*x**2/2
C = C0 + C1*x
I = y*F + C*y**2/2 + Q*y**3/3

origin = {x: 0, y: 0}
gradient = sp.Matrix([sp.diff(I, x), sp.diff(I, y)]).subs(origin)
H = sp.hessian(I, (x, y)).subs(origin)

check("stationarity", "Ricci-flat translation row makes the T0 germ stationary", gradient == sp.zeros(2, 1))
check("graph", "I1B vanishes identically on the T0 metric graph", sp.expand(I.subs(y, 0)) == 0)
check("graph", "every pure metric derivative on the T0 graph vanishes", all(sp.diff(I, x, n).subs(y, 0) == 0 for n in range(1, 7)))
check("hessian", "pure metric Hessian block is zero", H[0, 0] == 0)
check("hessian", "mixed metric-distortion Hessian owns DF", H[0, 1] == A and H[1, 0] == A)
check("hessian", "distortion Hessian owns the quadratic T packet", H[1, 1] == C0)
check("hessian", "complete scalar Hessian has the coupled block form", H == sp.Matrix([[0, A], [A, C0]]))
check("order", "K127 radial-metric-metric response is third derivative B", sp.diff(I, y, x, x).subs(origin) == B)
check("order", "K127 radial response is not the pure metric Hessian", sp.diff(I, y, x, x).subs(origin) != H[0, 0])
check("order", "moving distortion Hessian is a separate x-y-y cubic", sp.diff(I, x, y, y).subs(origin) == C1)
check("order", "pure radial cubic is independently Q-owned", sp.diff(I, y, 3).subs(origin) == 2*Q)

# Invertible Schur reduction is conditional on an owned C^{-1}.
check("schur", "coupled Hessian determinant does not require a pure hh block", sp.factor(H.det()) == -A**2)
check("schur", "formal elimination yields minus A squared over C", sp.simplify(0 - A*(1/C0)*A) == -A**2/C0)
check("schur", "formal reduction is undefined when C has a kernel", sp.simplify((-A**2/C0).subs(C0, 0)).has(sp.zoo))

a1, a2, c1 = sp.symbols("a1 a2 c1", nonzero=True)
Avec = sp.diag(a1, a2)
Csing = sp.diag(c1, 0)
h1, h2, t1, t2 = sp.symbols("h1 h2 t1 t2")
hvec = sp.Matrix([h1, h2])
tvec = sp.Matrix([t1, t2])
distortion_equation = Csing*tvec + Avec*hvec
check("kernel", "singular C equation fixes t1 only after h1 is supplied", sp.solve(distortion_equation[0], t1)[0] == -a1*h1/c1)
check("kernel", "kernel row becomes a metric constraint", distortion_equation[1] == a2*h2)
check("kernel", "kernel multiplier t2 is not eliminated", not distortion_equation.has(t2))
check("kernel", "constraint closure requires h2 zero rather than a fitted inverse", sp.solve(distortion_equation[1], h2)[0] == 0)

# Different invertible regularizations of the same singular block give
# different effective metric operators; the limit diverges in the kernel row.
eps = sp.symbols("eps", nonzero=True)
Creg = sp.diag(c1, eps)
Schur = sp.simplify(-Avec.T*Creg.inv()*Avec)
check("control", "regularized Schur complement retains inverse choice", Schur == sp.diag(-a1**2/c1, -a2**2/eps))
check("control", "kernel-direction coefficient is not intrinsic at eps zero", Schur[1, 1].has(eps))

# Coordinate retyping: a linear change y'=y+s x can create an apparent xx
# entry, while congruence preserves the coupled quadratic form.
s = sp.symbols("s")
P = sp.Matrix([[1, 0], [-s, 1]])  # (x,y) = P (x,y')
Hprime = sp.expand(P.T*H*P)
check("coordinate", "coordinate mixing can create an apparent hh entry", Hprime[0, 0] == C0*s**2 - 2*A*s)
check("coordinate", "congruence preserves determinant up to det(P)^2", sp.factor(Hprime.det()) == -A**2)
check("coordinate", "native graph coordinate keeps the genuine hh block zero", H[0, 0] == 0)

# Repository custody and propagation.
k122 = (ROOT / "explorations/conditional-build/selected-k122-native-i1b-cubic-and-preboundary-owner-decomposition-2026-08-15.md").read_text()
k127 = (ROOT / "explorations/conditional-build/selected-k127-native-i1b-ricci-flat-weyl-tt-closure-gate-2026-08-16.md").read_text()
artifact = (ROOT / "explorations/conditional-build/selected-k128-native-i1b-t0-coupled-hessian-and-schur-domain-gate-2026-08-16.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-16-selected-k128-native-i1b-t0-coupled-hessian-and-schur-domain-gate-review.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k128-native-i1b-t0-coupled-hessian-and-schur-domain-gate.json").read_text())
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()

check("source", "K122 owns native h and t columns separately", "Hbar=(H,DB_LC[H])" in k122 and "Vbar=(0,V)" in k122)
check("predecessor", "K127 explicitly denies pure TT Hessian identification", "not the pure TT Hessian" in k127)
check("artifact", "routing notice is present", "GU-COMPARATOR-ROUTING — scope before inference" in artifact)
check("artifact", "classification is explicit", "Classification: `SOURCE_NATIVE_ROUTE`." in artifact)
check("artifact", "target claim is internal and exact", "target_claim: K127_NEXT_GATE" in artifact)
check("artifact", "scope sentence binds the T0 native I1B germ", "Scope: this result binds" in artifact)
check("review", "hostile review separates third derivative from Hessian", "third derivative" in review and "quadratic Hessian" in review)
check("review", "hostile review forbids a fitted inverse", "fitted inverse" in review)
check("registry", "registry records zero pure metric block", registry["t0_coupled_hessian"]["hh_block"] == 0)
check("registry", "registry records mixed block owner", registry["t0_coupled_hessian"]["ht_block"] == "D_g_SHIAB_F_B")
check("registry", "registry keeps Schur reduction conditional", registry["schur_reduction"]["selected"] is False)
check("registry", "registry keeps domain open", registry["global_domain_selected"] is False)
check("repo", "current state advances through K128", "K128 now proves" in current)
check("repo", "roadmap advances to K129", "K129" in roadmap[:7000])
check("repo", "context records the conditional Schur operator", "schur" in context[:12000].lower() and "domain" in context[:12000].lower())
check("predecessor", "K127 carries the K128 successor classification", "## K128 successor classification" in k127)

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
raise SystemExit(1 if failures else 0)
