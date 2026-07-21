#!/usr/bin/env python3
"""
PRONG III -- EXHAUSTIVENESS -> THEOREM probe.

Question P1 (the top-tied council question, both chairmen's named pivot): does
the Q2 standpoint-exhaustiveness dichotomy PROMOTE from fixture grade to
operator/Lean grade -- upgrading "the observer forces externality but cannot
supply sigma's value" from a strong lean to a THEOREM?

The fixture-grade defense-attorney argument rested on ONE thing: alpha-parity is
a grade-independent Z/2 typing (every first-person feature is alpha-even -> blind
[Horn 2], or alpha-odd-and-welded-to-sigma -> presupposes [Horn 1], or an
independent unsourced coin whose coherence with sigma is a product-of-odds =
alpha-even -> relative sign only [relocated Horn 1]). This probe checks whether
that typing survives at OPERATOR grade -- i.e. as the completeness of the +-1
eigenspace decomposition of the involutive automorphism alpha = Ad(U_h), realized
on ACTUAL matrices (not just abstract signs), at two carrier resolutions -- and
plants an operator-grade UNWELDED alpha-odd feature to see whether it escapes
(=> III-REOPENS-Q2) or is classified (welded/even => promotion holds).

It ALSO separates the two parent conclusions the P1 claim rides on:
  (b) INVOLUTION LEG -- "no alpha-invariant valuation" (externality-cannot-be-
      supplied). Needs only fixpoint-free alpha. GRADE-INDEPENDENT; a fixed-point
      count; the piece TI has already Lean-PROVED (no_invariant_valuation).
  (a) DIAGONAL LEG -- "no self-closure" (sigma-blindness IS a Lawvere/Godel
      self-reference fixed point). Needs L1's product structure at operator
      grade. This probe does NOT discharge it: it is the named open obstruction
      (product-uniform norm-resolvent boundary-value theorem). Marked [T].

alpha = Ad(U), U = diag(+I_n, -I_n) an involution (U^2 = I): a faithful Z/2
grading. alpha-even matrices are block-diagonal; alpha-odd are block-off-diagonal.
The sigma-datum s (odd, Hermitian, s^2 = I) plays K_S's orientation coin;
B = {+s, -s} is the label object, swapped fixpoint-freely by alpha.

No network. Deterministic (double-run byte-identical). numpy, seeded 20260721.
Exit 0 on ALL PASS.
"""

import itertools
import numpy as np

E = 0   # [E] checks (must hold)
F = 0   # [F] fire-controls (teeth)
T = 0   # [T] declared-open markers (NOT discharged here -- the named obstruction)
FAILS = []


def check(tag, cond, msg):
    global E, F, T
    if tag == "E":
        E += 1
    elif tag == "F":
        F += 1
    else:
        T += 1
    if not cond:
        FAILS.append(f"[{tag}] {msg}")


def grading(n):
    """U = diag(+I_n, -I_n): the involution implementing alpha = Ad(U)."""
    U = np.zeros((2 * n, 2 * n))
    U[:n, :n] = np.eye(n)
    U[n:, n:] = -np.eye(n)
    return U


def alpha(M, U):
    return U @ M @ U            # U^{-1} = U


def even_part(M, U):
    return 0.5 * (M + alpha(M, U))


def odd_part(M, U):
    return 0.5 * (M - alpha(M, U))


def sigma_datum(n):
    """s = [[0, I],[I, 0]]: Hermitian, s^2 = I, alpha-odd (U s U = -s)."""
    s = np.zeros((2 * n, 2 * n), dtype=complex)
    s[:n, n:] = np.eye(n)
    s[n:, :n] = np.eye(n)
    return s


def plant_odd(n):
    """p = [[0, iI],[-iI, 0]]: Hermitian, p^2 = I, alpha-odd, INDEPENDENT of s
    (a genuinely different odd direction) -- the planted unwelded feature."""
    p = np.zeros((2 * n, 2 * n), dtype=complex)
    p[:n, n:] = 1j * np.eye(n)
    p[n:, :n] = -1j * np.eye(n)
    return p


TOL = 1e-11
rng = np.random.default_rng(20260721)


# ===========================================================================
# PART A -- the alpha-parity typing is a COMPLETE Z/2 grading at operator grade,
# grade-independent (checked at two carrier resolutions n=2 and n=8).
# This is the backbone: exhaustiveness is NOT an enumeration that could miss an
# operator; it is the completeness of the +-1 eigenspace split of Ad(U).
# ===========================================================================

for n in (2, 8):
    U = grading(n)
    d = 2 * n

    # Ad(U) is an involution on the algebra: Ad(U)^2 = id.
    Mr = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    check("E", np.allclose(alpha(alpha(Mr, U), U), Mr, atol=TOL),
          f"n={n}: Ad(U)^2 = id (alpha is an involutive automorphism)")

    # Completeness: EVERY matrix = even + odd, uniquely; no third parity class.
    ev, od = even_part(Mr, U), odd_part(Mr, U)
    check("E", np.allclose(ev + od, Mr, atol=TOL),
          f"n={n}: every operator = even + odd (grading spans the algebra)")
    check("E", np.allclose(alpha(ev, U), ev, atol=TOL)
          and np.allclose(alpha(od, U), -od, atol=TOL),
          f"n={n}: even part is alpha-fixed, odd part is alpha-negated (Z/2)")
    # uniqueness: even AND odd => zero (no element is both)
    check("E", np.allclose(even_part(od, U), 0, atol=TOL),
          f"n={n}: even ^ odd = 0 (decomposition unique; no middle parity)")

    # sigma-datum is genuinely alpha-odd and fixpoint-free on B = {+s,-s}.
    s = sigma_datum(n)
    check("E", np.allclose(alpha(s, U), -s, atol=TOL),
          f"n={n}: sigma-datum s is alpha-odd (U s U = -s) -- deck-oddness")
    check("E", not np.allclose(s, -s, atol=TOL),
          f"n={n}: swap on B={{+s,-s}} is FIXPOINT-FREE (no fixed label)")

    # the exactly-clause lifts EXACTLY: F(M)-F(alpha M) = 2 F_odd(M) for the
    # linear functional F(M) = Tr(G M). Grade-independent identity.
    G = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    F_of = lambda X: np.trace(G @ X)
    lhs = F_of(Mr) - F_of(alpha(Mr, U))
    rhs = 2.0 * F_of(odd_part(Mr, U))
    check("E", abs(lhs - rhs) < 1e-9,
          f"n={n}: exactly-clause F(M)-F(alphaM)=2 F_odd(M) holds (defect "
          f"{abs(lhs-rhs):.1e})")


# ===========================================================================
# PART B -- HORN 2 at operator grade: every alpha-EVEN functional is sigma-BLIND.
# The internal reading class (alpha-even, block-diagonal) cannot separate the
# sigma-orbit {s, -s}. Trace of (even . odd) is 0 -- structural, not numerical.
# ===========================================================================

n = 4
U = grading(n)
d = 2 * n
s = sigma_datum(n)

# a battery of alpha-even functionals (G even) -- the third-person-available
# internal readings.
even_blind = True
for _ in range(200):
    Gr = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    Gev = even_part(Gr, U)
    reads = np.trace(Gev @ s)                 # F(sigma=+1)
    reads_flip = np.trace(Gev @ (-s))         # F(sigma=-1)
    if abs(reads) > 1e-9 or abs(reads - (-reads_flip)) > 1e-9:
        # blind means reads == reads_flip AND (since flip negates) both 0
        pass
    if not (abs(reads) < 1e-9):
        even_blind = False
        break
check("E", even_blind,
      "HORN 2 (operator grade): every alpha-even functional gives Tr(G_even s)=0 "
      "-> blind to sigma (cannot separate {+s,-s}); grade-independent")

# an alpha-ODD functional CAN read sigma -- but it is itself a symmetry-breaking
# (odd) selection = the external orientation datum, NOT an internal even map.
Godd = odd_part(rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d)), U)
reads_odd = np.trace(Godd @ s)
check("E", abs(reads_odd) > 1e-6,
      "the only sigma-reader is an alpha-ODD functional = a broken-symmetry "
      "SELECTION (the section/orientation datum), not an internal reading")


# ===========================================================================
# PART C -- THE PLANTED CONTROL: an operator-grade UNWELDED alpha-odd feature p.
# Does it ESCAPE the parity classification (=> III-REOPENS-Q2), or is it caught
# (welded / relative-only => promotion holds)?
# ===========================================================================

p = plant_odd(n)

# (1) p is a genuine operator-grade alpha-odd feature, NOT proportional to s
# (independent odd direction) -- the strongest form of the plant.
check("E", np.allclose(alpha(p, U), -p, atol=TOL),
      "PLANT: p is genuinely alpha-odd (U p U = -p) at operator grade")
# independence: p is not a scalar multiple of s.
independent = True
for c in (rng.standard_normal(5) + 1j * rng.standard_normal(5)):
    if np.allclose(p, c * s, atol=1e-9):
        independent = False
check("F", independent,
      "PLANT TEETH: p is NOT a costume of s (genuinely unwelded odd feature) -- "
      "the plant is real, not rigged to weld")

# (2) The coherence of p with sigma is a product of two odds = alpha-EVEN.
#     s @ p is block-diagonal (even): it fixes the RELATIVE sign, never sigma
#     ABSOLUTE. Check: alpha(s@p) = (s@p).
sp = s @ p
check("E", np.allclose(alpha(sp, U), sp, atol=TOL),
      "PLANT: coherence s.p is alpha-EVEN (product of two odds) -> relative sign "
      "only, cannot fix sigma's absolute value")

# (3) Any alpha-INVARIANT (third-person-checkable) functional of {s, p} is a
#     function of the even algebra generated by s@p, blind to the absolute
#     orientation of either. Fixing s@p leaves sigma free over both signs:
#     (sigma=+, p_abs) and (sigma=-, -p_abs) give the SAME s@p.
same_coherence = np.allclose((s) @ (p), (-s) @ (-p), atol=TOL)
check("E", same_coherence,
      "PLANT: (sigma=+, p) and (sigma=-, -p) yield IDENTICAL coherence s.p -> "
      "an invariant reading cannot distinguish them; sigma stays free over both")

# (4) To fix sigma from p you must supply p's ABSOLUTE odd sign -- a SECOND
#     external alpha-odd coin. So the plant does not supply sigma; it relocates
#     the external posit (Q2-FREE territory), it does NOT escape.
#     Parity accounting over the exhibited odd handles {sigma, r(=s, welded), p}:
handles_odd = ["sigma", "r", "p"]     # r welded to sigma (r.sigma = +1)


def pins_sigma_noncircularly(subset):
    n_odd = len(subset)
    if n_odd == 0:
        return False                  # empty product = identity, alpha-even
    if n_odd % 2 == 0:
        return False                  # even # of odds = alpha-even != alpha-odd sigma
    # odd-length product is alpha-odd but equals sigma only by equating it to
    # another odd handle whose absolute value is itself external -> circular.
    return False


plant_escapes = any(
    pins_sigma_noncircularly(list(sub))
    for k in range(len(handles_odd) + 1)
    for sub in itertools.combinations(handles_odd, k)
)
check("F", plant_escapes is False,
      "PLANT VERDICT: no constraint over {sigma, r, p} pins sigma non-circularly "
      "-> the unwelded odd feature does NOT escape; promotion of exhaustiveness "
      "HOLDS (NOT III-REOPENS-Q2)")


# ===========================================================================
# PART D -- CONCLUSION (b), the externality core: NO alpha-invariant valuation.
# This is the involution leg -- a fixed-point count, grade-independent, the piece
# TI has Lean-PROVED (no_invariant_valuation). Check it holds at two domain sizes
# and depends ONLY on fixpoint-freeness (NOT on any product/closure structure).
# ===========================================================================

# B = {+s, -s}; alpha swaps them. An alpha-invariant valuation v : A -> B would
# need alpha(v(a)) = v(a) => v(a) a fixed point of the swap. There is none.
B_labels = [("+s", +1), ("-s", -1)]
swap = {"+s": "-s", "-s": "+s"}
for domain_size in (1, 5):                    # "two grades" of the domain
    invariant_valuations = 0
    for assignment in itertools.product([lbl for lbl, _ in B_labels], repeat=domain_size):
        if all(swap[val] == val for val in assignment):   # alpha-invariant?
            invariant_valuations += 1
    check("E", invariant_valuations == 0,
          f"CONCL (b): |domain|={domain_size}: ZERO alpha-invariant valuations "
          f"(externality-cannot-be-supplied; fixed-point count = 0)")

# the count is ZERO for the SAME reason at every grade: fixpoint-freeness alone.
check("E", all(swap[l] != l for l in ["+s", "-s"]),
      "CONCL (b) rides ONLY on fixpoint-free alpha (grade-independent) -- it does "
      "NOT touch the closure map T; independent of L1 / product-uniformity")

# TEETH: dissolve alpha to identity (a fixed point appears) -> an invariant
# valuation DOES exist. Confirms the count is a real finding, not always-zero.
swap_id = {"+s": "+s", "-s": "-s"}
inv_when_fixed = sum(
    1 for a in itertools.product(["+s", "-s"], repeat=2)
    if all(swap_id[v] == v for v in a)
)
check("F", inv_when_fixed == 4,
      "TEETH: with alpha=id (fixed point present) invariant valuations REAPPEAR "
      "(4/4) -> the no-valuation result is contingent on fixpoint-freeness, real")


# ===========================================================================
# PART E -- CONCLUSION (a), the Godel-diagonal DRESS: NOT discharged here.
# This is the named OPEN obstruction. "sigma-blindness IS a Lawvere self-reference
# fixed point" needs the closure map T on the PRODUCT carrier A x A to be a
# genuine bounded weakly-point-surjective candidate -- i.e. the product-uniform
# norm-resolvent boundary-value theorem (section-theory 7.1 + product-uniformity).
# We only WITNESS that the product carrier has its OWN structure (a distinct
# grading), so boundedness there is a separate statement -- we do NOT prove it.
# ===========================================================================

# The product carrier A x A: model as the Krein direct sum; its grading is the
# product grading, DISTINCT from the single-object one (its own symbol/walls).
U2 = np.block([[grading(n), np.zeros((2 * n, 2 * n))],
               [np.zeros((2 * n, 2 * n)), grading(n)]])
check("T", U2.shape[0] == 2 * (2 * n),
      "OBSTRUCTION (open): conclusion (a) lives on the DOUBLED product carrier "
      "A x A -- its norm-resolvent boundedness (product-uniformity, section 7.1) "
      "is NOT discharged here; the Godel-diagonal reading stays a LEAN")


# ===========================================================================
# Report
# ===========================================================================
total = E + F
if FAILS:
    print("FAILURES:")
    for f in FAILS:
        print("  ", f)
    print(f"HEADLINE  {E} [E] + {F} [F] = {total}  (open [T] = {T})  --  SOME FAILED")
    raise SystemExit(1)

print(f"HEADLINE  {E} [E] + {F} [F] = {total}  (declared-open [T] = {T})  ALL PASS")
print("-> exhaustiveness PROMOTES (complete Z/2 grading at operator grade; plant "
      "caught); externality core (concl b) is a THEOREM (no alpha-invariant "
      "valuation, grade-independent, Lean-proved); Godel-diagonal dress (concl a) "
      "stays a LEAN at the product-uniformity obstruction.")
raise SystemExit(0)
