#!/usr/bin/env python3
"""W187: lightweight exact audit of auxiliary elimination versus propagating poles.

This does not implement the GU reduction.  It checks the construction-independent
quadratic algebra used to state what a future GU reduction must establish.

Run:
    python -u tests/W187_law_shadow_reduction_audit.py

Dependencies: stdlib + sympy (already used by the targeted W161/W167/W176 tests).
Exit status is nonzero if any check fails.
"""

from __future__ import annotations

import sympy as sp


FAILURES: list[str] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    ok = bool(condition)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {name}" + (f" | {detail}" if detail else ""), flush=True)
    if not ok:
        FAILURES.append(name)


def degree(expr: sp.Expr, variable: sp.Symbol) -> int:
    return int(sp.Poly(sp.together(expr), variable).degree())


print("=" * 88)
print("W187 -- law/shadow Schur-complement and pole-classification audit")
print("=" * 88)

# ---------------------------------------------------------------------------
# 1. General stationary elimination and determinant identity.
# ---------------------------------------------------------------------------
h, t = sp.symbols("h t", real=True)
A, B, C = sp.symbols("A B C", real=True, nonzero=True)

lagrangian = sp.Rational(1, 2) * A * h**2 + B * h * t + sp.Rational(1, 2) * C * t**2
t_star = sp.solve(sp.diff(lagrangian, t), t)[0]
effective = sp.factor(lagrangian.subs(t, t_star))
expected_effective = sp.Rational(1, 2) * (A - B**2 / C) * h**2

check(
    "SC1 stationary eliminated field is t* = -C^{-1} B h",
    sp.simplify(t_star + B * h / C) == 0,
    f"t*={t_star}",
)
check(
    "SC2 substitution gives K_eff = A - B C^{-1} B",
    sp.simplify(effective - expected_effective) == 0,
    f"S_eff={effective}",
)

block_hessian = sp.Matrix([[A, B], [B, C]])
schur = A - B**2 / C
check(
    "SC3 det(full Hessian) = det(C) det(K_eff)",
    sp.simplify(block_hessian.det() - C * schur) == 0,
    f"det={block_hessian.det()}",
)

# ---------------------------------------------------------------------------
# 2. Positive control: nonderivative auxiliary coupling only shifts one pole.
#    Minkowski spectral variable s=p^2.  Positive mass has root s=m^2 >= 0.
# ---------------------------------------------------------------------------
s = sp.symbols("s", real=True)
A_pos = s - 1
B_pos = sp.Integer(1)
C_pos = sp.Integer(4)
K_pos = sp.factor(A_pos - B_pos**2 / C_pos)
det_pos = sp.factor(sp.Matrix([[A_pos, B_pos], [B_pos, C_pos]]).det())
root_pos = sp.solve(sp.Eq(K_pos, 0), s)
residue_pos = sp.simplify(1 / sp.diff(K_pos, s).subs(s, root_pos[0]))

check(
    "PC1 nonderivative elimination does not raise inverse-propagator degree",
    degree(K_pos, s) == degree(A_pos, s) == 1,
    f"K_eff={K_pos}",
)
check(
    "PC2 full determinant and Schur complement have the same single pole",
    sp.simplify(det_pos - C_pos * K_pos) == 0 and root_pos == [sp.Rational(5, 4)],
    f"root={root_pos}",
)
check(
    "PC3 shifted pole is positive-mass and positive-residue in Hilbert control",
    root_pos[0] >= 0 and residue_pos > 0,
    f"m^2={root_pos[0]}, residue={residue_pos}",
)

# ---------------------------------------------------------------------------
# 3. Negative control: t is algebraic in itself, but B(s)=s is derivative.
#    Exact elimination raises the degree and the new zero is a full-Hessian zero.
# ---------------------------------------------------------------------------
A_der = s - 1
B_der = s
C_der = sp.Integer(9)
K_der = sp.factor(A_der - B_der**2 / C_der)
det_der = sp.factor(sp.Matrix([[A_der, B_der], [B_der, C_der]]).det())
roots_der = sorted(sp.solve(sp.Eq(K_der, 0), s), key=lambda x: float(sp.N(x)))
expected_roots = [
    (sp.Integer(9) - 3 * sp.sqrt(5)) / 2,
    (sp.Integer(9) + 3 * sp.sqrt(5)) / 2,
]
residues_der = [sp.simplify(1 / sp.diff(K_der, s).subs(s, root)) for root in roots_der]

check(
    "NC1 derivative coupling raises K_eff degree from one to two",
    degree(A_der, s) == 1 and degree(K_der, s) == 2,
    f"K_eff={K_der}",
)
check(
    "NC2 both effective poles are zeros of the full mixed Hessian",
    sp.simplify(det_der - C_der * K_der) == 0
    and all(sp.simplify(det_der.subs(s, root)) == 0 for root in roots_der),
    f"det={det_der}",
)
check(
    "NC3 exact roots match (9 +/- 3 sqrt(5))/2",
    all(sp.simplify(got - want) == 0 for got, want in zip(roots_der, expected_roots)),
    f"roots={roots_der}",
)
check(
    "NC4 roots have opposite residues: one healthy, one ghost-like in Hilbert control",
    residues_der[0] > 0 and residues_der[1] < 0,
    f"residues={residues_der}",
)

# The same local polynomial can be only a self-energy expansion on a restricted EFT domain.
cutoff_squared = sp.Integer(4)
parent_roots_in_domain = [r for r in sp.solve(sp.Eq(A_der, 0), s) if 0 <= r < cutoff_squared]
effective_roots_in_domain = [r for r in roots_der if 0 <= r < cutoff_squared]
effective_roots_outside = [r for r in roots_der if r >= cutoff_squared]
check(
    "EFT1 below cutoff s<4 there is no additional in-domain pole versus the parent",
    len(parent_roots_in_domain) == len(effective_roots_in_domain) == 1,
    f"parent={parent_roots_in_domain}, effective={effective_roots_in_domain}",
)
check(
    "EFT2 the extra resummed pole lies outside the declared EFT domain",
    len(effective_roots_outside) == 1 and effective_roots_outside[0] > cutoff_squared,
    f"outside={effective_roots_outside}",
)

# ---------------------------------------------------------------------------
# 4. Tachyon and ghost are distinct diagnoses.
# ---------------------------------------------------------------------------
K_tachyon = s + 2
tachyon_root = sp.solve(sp.Eq(K_tachyon, 0), s)[0]
tachyon_residue = sp.simplify(1 / sp.diff(K_tachyon, s).subs(s, tachyon_root))
check(
    "CLASS1 tachyon control has m^2<0 but positive residue",
    tachyon_root < 0 and tachyon_residue > 0,
    f"m^2={tachyon_root}, residue={tachyon_residue}",
)
check(
    "CLASS2 negative-residue derivative-control pole is not tachyonic",
    roots_der[1] > 0 and residues_der[1] < 0,
    f"m^2={roots_der[1]}, residue={residues_der[1]}",
)

# ---------------------------------------------------------------------------
# 5. If C has an on-domain zero, it cannot be globally called auxiliary there.
# ---------------------------------------------------------------------------
C_dynamic = s - 3
B_dynamic = sp.Integer(1)
A_dynamic = s - 1
K_dynamic = sp.together(A_dynamic - B_dynamic**2 / C_dynamic)
check(
    "GATE1 eliminated block with C(3)=0 makes Schur complement singular",
    C_dynamic.subs(s, 3) == 0 and sp.denom(K_dynamic).subs(s, 3) == 0,
    f"K_eff={K_dynamic}",
)
check(
    "GATE2 auxiliary interpretation is valid only away from zeros of C",
    sp.simplify(
        sp.Matrix([[A_dynamic, B_dynamic], [B_dynamic, C_dynamic]]).det()
        - C_dynamic * K_dynamic
    )
    == 0,
    "determinant identity is rational and elimination excludes C=0",
)

print("-" * 88)
total = 16
passed = total - len(FAILURES)
print(f"W187: {passed}/{total} checks passed")
if FAILURES:
    print("Failures: " + "; ".join(FAILURES))
    raise SystemExit(1)

print("VERDICT: the Schur complement decides the quadratic shadow. Algebraic elimination alone")
print("does not prove absence of extra full-system poles; a local higher-derivative coefficient")
print("alone does not prove an in-domain particle. Gauge reduction, domain, sheet, and operative")
print("metric remain mandatory. This script does not implement the GU reduction.")
raise SystemExit(0)
