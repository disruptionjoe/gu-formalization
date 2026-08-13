"""M-H9 Tier 1: does the base FS flip propagate to C_perp?

PREREGISTERED BEFORE RUNNING.
Tier 0 established that the base commuting real structure flips character between
the horns: J.conj(J) = +I at (3,1), -I at (1,3), with the (6,4) fibre unchanged.
Tier 1 asks whether that flip survives into the object that actually carries the
delta_e sign, C_perp = K . J_obs on the 128-dim spinor module.

  EXPECTED : C_perp conj(C_perp) has OPPOSITE character at the two bases.
  FALSIFIED IF : the character is the SAME at both. Then the base flip does not
                 reach C_perp, and the endpoint-flip mechanism fails exactly
                 where it would have to work.

Also checks the repo's standing claim that the DeWitt fibre is (6,4) on BOTH
bases -- the premise that lets (9,5) and (7,7) differ only in the base.

SCOPE. This computes the involution CHARACTER of C_perp. It does NOT re-derive
the DeWitt loop transport: DEWITT_FRAME, mixed_rotation's timelike_leg and the
diagonal/off-diagonal bases are all built for a mostly-plus base with the
distinguished leg at index 3, and re-deriving them is a separate step. So this
establishes the sign that would propagate, CONDITIONAL on the 2026-07-30
all-ten-equal result transferring to the other base -- which is proven at (3,1)
and is NOT established here.
"""
import importlib.util, sys
import numpy as np

spec = importlib.util.spec_from_file_location(
    "f20", "tests/channel-swings/full20_dewitt_loop_transport_probe.py")
m = importlib.util.module_from_spec(spec); sys.modules["f20"] = m
spec.loader.exec_module(m)


def inertia(gram, tol=1e-9):
    ev = np.linalg.eigvalsh(gram)
    return int((ev > tol).sum()), int((ev < -tol).sum()), int((abs(ev) <= tol).sum())


def cperp_character(base_pos, base_neg):
    g4, e4 = m.signed_gammas(base_pos, base_neg)
    g10, e10 = m.signed_gammas(6, 4)
    om4 = m.normalized_chirality(g4)
    I32 = np.eye(32, dtype=complex)
    g14 = [np.kron(g, I32) for g in g4] + [np.kron(om4, g) for g in g10]
    e14 = np.concatenate((e4, e10))
    obs = np.kron(m.commuting_real_structure(g4), m.commuting_real_structure(g10))
    krein = m.matrix_product([g for g, s in zip(g14, e14) if s > 0])
    cperp = krein @ obs
    prod = cperp @ cperp.conj()
    for s in (+1.0, -1.0):
        if m.max_abs(prod - s * np.eye(128, dtype=complex)) < 1e-9:
            return int(s), float(m.max_abs(prod - s * np.eye(128, dtype=complex)))
    return None, float(m.max_abs(prod))


print("=" * 78)
print("M-H9 Tier 1 -- does the base FS flip reach C_perp?")
print("=" * 78)

print("\n[1] DeWitt fibre signature, the premise that the horns differ only in the base")
for lbl, met in (("(3,1) base", [1., 1., 1., -1.]), ("(1,3) base", [1., -1., -1., -1.])):
    p, n, z = inertia(m.dewitt_metric(np.diag(met)))
    print(f"    {lbl}: dewitt_metric inertia = ({p},{n})  zero {z}   -> {'(6,4) CONFIRMED' if (p,n)==(6,4) else 'NOT (6,4)'}")

print("\n[2] C_perp involution character on the 128-dim spinor module")
res = {}
for lbl, (p, q) in (("(3,1) base of the (9,5) horn", (3, 1)),
                    ("(1,3) base of the (7,7) horn", (1, 3))):
    s, r = cperp_character(p, q)
    res[(p, q)] = s
    shown = f"{s:+d} I" if s is not None else "NOT +/- I"
    print(f"    {lbl}: C_perp conj(C_perp) = {shown}   (residual {r:.2e})")

a, b = res[(3, 1)], res[(1, 3)]
print("\n[3] Verdict")
if a is None or b is None:
    print("    INCONCLUSIVE: C_perp is not an involution on at least one base.")
elif a != b:
    print("    OPPOSITE -> the base FS flip DOES reach C_perp.")
    print("    Endpoint-flip mechanism survives at the level that carries delta_e.")
else:
    print("    SAME -> the base flip does NOT reach C_perp.")
    print("    PREREGISTERED FALSIFICATION: the mechanism fails where it must work.")

# ---------------------------------------------------------------------------
# Assertions. The preregistered expectation was OPPOSITE characters; the result
# is SAME, so the assertions below pin the FALSIFICATION, not the hypothesis.
# ---------------------------------------------------------------------------
assert inertia(m.dewitt_metric(np.diag([1., 1., 1., -1.])))[:2] == (6, 4)
assert inertia(m.dewitt_metric(np.diag([1., -1., -1., -1.])))[:2] == (6, 4)
assert a == +1 and b == +1, f"C_perp character changed: {a} vs {b}"
assert a == b, "if this ever fails, the mechanism is revived -- re-open M-H9"
print("\nVERDICT: CPERP-CHARACTER-DOES-NOT-FLIP__MH9-ENDPOINT-MECHANISM-FALSIFIED")
print("SCOPE: frame-independent -- C_perp is built from gammas only, so the")
print("  hardcoded DEWITT_FRAME and timelike_leg never enter and the artefact")
print("  risk flagged for a frame re-derivation does not apply here. What is")
print("  NOT established: the DeWitt loop transport itself under (1,3), and")
print("  therefore whether the 2026-07-30 all-ten-equal result transfers.")
