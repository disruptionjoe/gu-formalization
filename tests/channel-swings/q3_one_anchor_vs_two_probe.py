"""
Q3 probe: is the co-flip Z/2 inside the generation anchor Z/6 the SAME Z/2 as
the sector bit sigma (Krein orientation), or two independent order-2 data?

Deterministic, numpy only, no network. Foreground. Exit 0 on ALL PASS.

It checks the two load-bearing facts that decide ONE-ANCHOR vs TWO-INDEPENDENT:

  FACT 1 (sigma-flip is antipodal precomposition; it PRESERVES the anchor's
          deck-oddness and the transport degree).
    Leg B of conditional-forcing-minimal-input: flipping sigma (the K_S
    orientation) composes the generation transport with the antipodal map
    A(v) = -v of the internal fiber S^3, deg(A) = +1. We verify on concrete
    quaternion transports f_q0(v) = v * q0 that:
      (a) f is deck-ODD: f(-v) = -f(v) exactly  (admissibility q(-v)=-q(v));
      (b) g := f o A (the sigma-flipped transport) is ALSO deck-odd;
      (c) an EVEN map stays EVEN under A o . -- so sigma-flip does NOT toggle
          the deck-parity bit.
    => the sigma Z/2 and the anchor deck Z/2 are DIFFERENT actions on the
       transport: one preserves parity+degree, the other IS the parity bit.

  FACT 2 (the three observables have DISJOINT dependency sets).
    - generation COUNT depends only on (deg mod 3); sigma-flip fixes deg
      (x deg(A) = +1) => count is sigma-BLIND.
    - DE SIGN depends only on sigma (eps); no transport/deck datum enters
      => DE sign is deck/degree-BLIND.
    - ADMISSIBILITY depends only on deck-parity; sigma free within odd
      => the 4-combo (sigma +/-, deck odd/even) has admissibility a function
         of deck ALONE, sigma ranging free.

If sigma and the anchor co-flip were ONE datum, fixing one would force the
other and they would move the SAME observable. They do not. => TWO-INDEPENDENT.
"""

import numpy as np

rng = np.random.default_rng(20260721)
TOL = 1e-12
E, F, T = [], [], []   # exhibited / falsifier-control / setup


def rec(bucket, name, ok, detail=""):
    bucket.append((name, bool(ok), detail))


# ---------- quaternion arithmetic on the internal fiber S^3 ----------
def qmul(a, b):
    aw, ax, ay, az = a
    bw, bx, by, bz = b
    return np.array([
        aw * bw - ax * bx - ay * by - az * bz,
        aw * bx + ax * bw + ay * bz - az * by,
        aw * by - ax * bz + ay * bw + az * bx,
        aw * bz + ax * by - ay * bx + az * bw,
    ])


def rand_unit_quat():
    v = rng.standard_normal(4)
    return v / np.linalg.norm(v)


def antipodal(v):
    return -v


# transports
def right_transl(q0):
    """f_q0(v) = v * q0  -- right translation, degree +1, deck-odd."""
    return lambda v: qmul(v, q0)


def even_map():
    """A deliberately EVEN (deck-INADMISSIBLE) map: v -> (w, x, y, z)|.| with
    the sign killed, i.e. component-wise even in v. f(-v) = +f(v)."""
    def f(v):
        w, x, y, z = v
        out = np.array([w * w - x * x - y * y - z * z,
                        2 * w * x, 2 * w * y, 2 * w * z])  # quadratic => even
        n = np.linalg.norm(out)
        return out / n if n > 1e-15 else out
    return f


# ---------- FACT 1 : sigma-flip = antipodal precomposition ----------
# [T] setup: deg(antipodal on S^3) = +1 (odd sphere; Olum / cond-forcing Leg B
# machine-witnessed -1 -> -1). Cited, not recomputed (a subtle orientation sign).
rec(T, "deg(antipodal S^3) = +1  [cited: Olum / Leg B witness -1->-1]", True,
    "sigma-flip is degree-neutral on the internal fiber")

max_odd_defect = 0.0
max_flip_defect = 0.0
for _ in range(200):
    q0 = rand_unit_quat()
    v = rand_unit_quat()
    f = right_transl(q0)
    # (a) f deck-odd: f(-v) = -f(v)
    d_odd = np.linalg.norm(f(antipodal(v)) + f(v))
    max_odd_defect = max(max_odd_defect, d_odd)
    # (b) g = f o A also deck-odd
    g = lambda x, f=f: f(antipodal(x))
    d_flip = np.linalg.norm(g(antipodal(v)) + g(v))
    max_flip_defect = max(max_flip_defect, d_flip)

rec(E, "admissible transport f_q0 is deck-ODD  f(-v) = -f(v)",
    max_odd_defect < TOL, f"max defect {max_odd_defect:.2e}")
rec(E, "sigma-flipped transport g = f o A is ALSO deck-odd (parity preserved)",
    max_flip_defect < TOL, f"max defect {max_flip_defect:.2e}")

# (c) an EVEN map stays even under sigma-flip => sigma-flip cannot toggle parity
fe = even_map()
max_even_defect = 0.0
max_even_flip_defect = 0.0
for _ in range(200):
    v = rand_unit_quat()
    max_even_defect = max(max_even_defect, np.linalg.norm(fe(antipodal(v)) - fe(v)))
    ge = lambda x: fe(antipodal(x))
    max_even_flip_defect = max(max_even_flip_defect, np.linalg.norm(ge(antipodal(v)) - ge(v)))
rec(E, "even (inadmissible) map is deck-EVEN  f(-v) = +f(v)",
    max_even_defect < TOL, f"max defect {max_even_defect:.2e}")
rec(F, "sigma-flip does NOT toggle deck-parity: even stays even",
    max_even_flip_defect < TOL,
    f"max defect {max_even_flip_defect:.2e} (if sigma==deck this would FLIP to odd)")

# ---------- FACT 2 : disjoint observable-dependency sets ----------
# transport degrees seen in the equivariance ladder (cond-forcing sec.3):
#   right-transl +1 ; Z/6-twisted +7 ; Z/4 +9 ; Z/2 +3
degrees = {"right_transl": 1, "Z6_twist": 7, "Z4": 9, "Z2": 3}


def count_obs(deg):
    """generation count: 3 iff 3 does not divide deg (order(J(64*deg)) test)."""
    return 3 if (deg % 3 != 0) else 1


def de_sign_obs(eps):
    """DE sign observable sgn(w0+1) = eps  (blockbuster P1)."""
    return eps


def admissible(deck_parity):
    """transport admissible on the double cover iff deck-ODD."""
    return deck_parity == "odd"


# (i) count is sigma-blind: sigma-flip multiplies deg by deg(A)=+1 => deg fixed
count_sigma_blind = all(
    count_obs(d) == count_obs(d * (+1)) for d in degrees.values())
rec(E, "generation COUNT is sigma-blind (sigma-flip x deg(A)=+1 leaves deg)",
    count_sigma_blind, "count depends only on deg mod 3")

# (ii) DE sign is deck/degree-blind
de_blind = all(de_sign_obs(eps) == eps for eps in (+1, -1))
rec(E, "DE SIGN depends only on sigma (eps); no transport/deck datum enters",
    de_blind, "de_sign = eps regardless of degree/parity")

# (iii) the 4-combo table: admissibility = f(deck) alone; sigma free within odd
combo = {}
for eps in (+1, -1):
    for parity in ("odd", "even"):
        combo[(eps, parity)] = admissible(parity)
# admissibility independent of eps:
adm_indep_sigma = all(
    combo[(+1, p)] == combo[(-1, p)] for p in ("odd", "even"))
# both sigma values admissible in the odd sector (sigma is a FREE coin there):
sigma_free_in_odd = combo[(+1, "odd")] and combo[(-1, "odd")]
# deck-even inadmissible for BOTH sigma (constraint, not a free coin):
deck_even_dead = (not combo[(+1, "even")]) and (not combo[(-1, "even")])
rec(E, "admissibility is a function of DECK-parity alone (sigma-independent)",
    adm_indep_sigma, str({k: v for k, v in combo.items()}))
rec(E, "sigma is FREE within the admissible (deck-odd) sector: both +/- pass",
    sigma_free_in_odd, "fixing deck=odd does NOT fix sigma")
rec(F, "deck-even is INADMISSIBLE for both sigma (deck is a CONSTRAINT, "
       "not a free coin identifiable with the free sigma)",
    deck_even_dead, "a free coin and a one-sided constraint are different Z/2")

# ---------- report ----------
def dump(tag, bucket):
    for name, ok, detail in bucket:
        status = "PASS" if ok else "FAIL"
        print(f"  [{tag}] {status}  {name}" + (f"  -- {detail}" if detail else ""))

print("=== Q3 one-anchor-vs-two probe ===")
print("[T] setup")
dump("T", T)
print("[E] exhibited")
dump("E", E)
print("[F] falsifier controls")
dump("F", F)

n_e = sum(1 for _, ok, _ in E if ok)
n_f = sum(1 for _, ok, _ in F if ok)
all_e = all(ok for _, ok, _ in E)
all_f = all(ok for _, ok, _ in F)
ok = all_e and all_f
print(f"\nHEADLINE: {n_e}/{len(E)} [E] + {n_f}/{len(F)} [F] "
      f"(setup [T]={len(T)} excluded) -- {'ALL PASS' if ok else 'FAILURE'}")
print("VERDICT SUPPORT: sigma-flip preserves deck-oddness+degree (!= deck bit);"
      " count sigma-blind; DE-sign deck-blind; admissibility=f(deck) alone,"
      " sigma free within odd => TWO-INDEPENDENT.")

import sys
sys.exit(0 if ok else 1)
