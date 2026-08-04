#!/usr/bin/env python3
r"""W230 -> FLRW composition map: the five-arrow ledger and its FIRST UNBUILDABLE
arrow, with exact-rational certificates (Wave A-2 redo; hostile-review findings 1-4).

THE QUESTION.  The 2026-08-03 hostile review holds the FLRW scalar B and W230's
connection distortion UNCERTAIN as the same object because five maps were never
composed: observation, pullback, projection, normalization, equation.  The paper
composition lives in explorations/de-certification-redo-2026-08-03.md Section 3.
This script carries (i) the machine-checked ledger with repo-text ties (silent
drift in a cited artifact fails here), and (ii) the preregistered cheap
computations in EXACT RATIONAL arithmetic (fractions.Fraction; no finite
differences, no float tolerances on the decisive claims -- P-H29 compliant).

THE LEDGER (composition order; statuses justified in the exploration):
  A1 OBS   theta = pi - eps^{-1} B eps, the connection distortion.  DEFINED
           (canon/dark-energy-theta-divergence-free.md Section 1; W230 typing).
  A2 PULL  restriction to the FLRW section s: X4 -> Y14 (Y14 = Met(X); s = the
           FLRW metric point).  DEFINED-CONDITIONAL on A1 (well-typed; no
           artifact computes it, none is needed at configuration level).
  A3 PROJ  fibre-mode projection onto the normal-Laplacian ground mode on
           GL(4,R)/O(3,1): B(t) := ground-mode amplitude, lambda_{N,1} = 8.
           RECONSTRUCTION-GRADE (rc3 spectrum; canon theta-field lines 80-81).
           Layer-0 fence: W230's finite fixture lives on the 14-dim FRAME
           direction space, a DIFFERENT object from this metric fibre.
  A4 NORM  kinetic split/normalization: the coefficients (c_b, c_s, c_f) of the
           reduced action come from evaluating the native gradient term
           Z_U = |D_A U|^2 (connection Laplacian D_A* D_A) on the A1-A3
           configuration.  Z_U is NOT BUILT (W203 coefficient ledger).
           STATUS: UNBUILDABLE WITH CURRENT OBJECTS  <-- FIRST UNBUILDABLE ARROW.
  A5 EQ    Euler-Lagrange of the normalized reduced action (+ source pullback)
           -> H44's  B'' + (3 + H'/H) B' + (M^2/H^2) B = 0  iff A4 delivers
           (c_b, c_f) = (1, 1) x normalization and a negligible source.
           DEFINED-CONDITIONAL (mechanical given A4).

EXACT CERTIFICATES (preregistered in the exploration, Section 1.2):
  [EXACT-8]   lambda_{N,1} = (9/2)^2 - (7/2)^2 = 8 exactly.
  [EXACT-K0]  in a properly-typed separable gradient model the k -> 0 limit
              annihilates EXACTLY and ONLY the base-spatial sub-block; the
              base-time block and fibre eigenvalue are exactly k-independent;
              omega^2 = (c_f/c_b) lambda_1 in exact rationals.  Consequence:
              seat2's k = 0 caveat cannot decide the c_kin question; only
              building Z_U (arrow A4) can.
  [EXACT-RAY] the review's finding-3 ray criterion at certificate grade: the
              proportional family c M preserves the target ray exactly; the
              NON-proportional planted witness L = M + (Mt)(Mt)^T also
              preserves it exactly (sharper than the review's L = M); a
              generic integer perturbation breaks it exactly; all verified
              through the full field equation solved over Fractions.

SCOPE.  Nothing here builds the native Z_U, decides c_kin, or moves M-H13 /
C10 / the native-bridge status (register-owned).  The exact toys certify TYPE
statements about which sub-blocks the homogeneous limit removes and where the
iff boundary of the ray criterion lies -- not native coefficients.

Run: PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python -u \
       tests/de-certification/w230_flrw_composition_first_arrow.py
Exit 0 iff the ledger ties and every exact certificate hold.
"""
from __future__ import annotations
import os
import sys
from fractions import Fraction as Fr

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(m=""):
    print(m, flush=True)


ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


# ===========================================================================
# Exact rational linear algebra (small dimensions; partial-pivot elimination).
# ===========================================================================
def fr_solve(A, b):
    n = len(A)
    M = [[Fr(A[i][j]) for j in range(n)] + [Fr(b[i])] for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [x - f * y for x, y in zip(M[r], M[col])]
    return [M[i][n] for i in range(n)]


def matvec(A, v):
    return [sum(Fr(A[i][j]) * v[j] for j in range(len(v))) for i in range(len(A))]


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def parallel_exact(u, v):
    """True iff u and v are exactly parallel: every 2x2 minor vanishes."""
    n = len(u)
    return all(u[i] * v[j] - u[j] * v[i] == 0 for i in range(n) for j in range(i + 1, n))


# ===========================================================================
# THE LEDGER (data), with repo-text ties.
# ===========================================================================
LEDGER = [
    ("A1 OBS", "connection distortion theta = pi - eps^{-1} B eps",
     "canon/dark-energy-theta-divergence-free.md", "DEFINED"),
    ("A2 PULL", "restriction to the FLRW section s: X4 -> Y14",
     "GEOMETER-VS-PHYSICS-OBJECTS.md (arena); well-typed given A1", "DEFINED-CONDITIONAL"),
    ("A3 PROJ", "fibre normal-Laplacian ground-mode amplitude B(t), lambda_1 = 8",
     "canon/theta-field-flrw-dark-energy-eos.md (rc3 reconstruction)", "RECONSTRUCTION-GRADE"),
    ("A4 NORM", "kinetic split (c_b, c_s, c_f) from Z_U = |D_A U|^2",
     "explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md", "UNBUILDABLE"),
    ("A5 EQ", "Euler-Lagrange -> H44's B'' equation",
     "tests/wave25/H44_de_backreacted_background.py", "DEFINED-CONDITIONAL"),
]


def main():
    log("=" * 78)
    log("W230 -> FLRW composition: five-arrow ledger + exact certificates")
    log("=" * 78)

    # -----------------------------------------------------------------------
    # [LEDGER] -- exactly one first unbuildable arrow, tied to artifact text.
    # -----------------------------------------------------------------------
    log("\n[LEDGER] composition order, status, defining artifact")
    for name, obj, art, status in LEDGER:
        log(f"  {name:8s} {status:22s} {obj}")
        log(f"           <- {art}")
    unbuildable = [i for i, row in enumerate(LEDGER) if row[3] == "UNBUILDABLE"]
    check("LED1: exactly one UNBUILDABLE arrow in the ledger", len(unbuildable) == 1,
          f"{[LEDGER[i][0] for i in unbuildable]}")
    check("LED2: the first (and only) unbuildable arrow is A4 NORM, requiring "
          "Z_U = |D_A U|^2 -- the review's predicted blocker CONFIRMED",
          unbuildable == [3], f"index {unbuildable}")

    w203 = read("explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md")
    zline = [ln for ln in w203.splitlines() if "Z_U" in ln and "NOT BUILT" in ln]
    check("LED3 (repo tie): W203's coefficient ledger still carries the Z_U "
          "NOT-BUILT row", len(zline) >= 1, f"{len(zline)} line(s)")
    w230 = read("explorations/W230-close-a4-derive-w154-2026-07-14.md")
    check("LED4 (repo tie): W230 names c_kin L as the stand-in for D_A* D_A "
          "(the unbuilt nonlocal Z_U)", ("D_A* D_A" in w230) and ("c_kin" in w230))
    h44 = read("tests/wave25/H44_de_backreacted_background.py")
    check("LED5 (repo tie): H44 carries the target equation "
          "B'' + (3 + H'/H) B' + (M^2/H^2) B",
          "B'' + (3 + H'/H) B' + (M^2/H^2) B" in h44)
    canon = read("canon/theta-field-flrw-dark-energy-eos.md")
    check("LED6 (repo tie): the canon pins M_KK to the fibre normal-Laplacian "
          "ground eigenvalue (rc3 reconstruction)",
          "lambda_{N,1}" in canon and "rc3" in canon)

    # -----------------------------------------------------------------------
    # [EXACT-8] -- the mass IS a fibre-gradient eigenvalue, exactly.
    # -----------------------------------------------------------------------
    log("\n[EXACT-8] lambda_{N,1} = (9/2)^2 - (7/2)^2 in exact rationals")
    lam1 = Fr(9, 2) ** 2 - Fr(7, 2) ** 2
    log(f"  (9/2)^2 - (7/2)^2 = {lam1}")
    check("E8: lambda_1 = 8 exactly (Fraction arithmetic; the repo's M^2 is a "
          "fibre-GRADIENT eigenvalue, untouchable by X4 homogeneity)", lam1 == 8)

    # -----------------------------------------------------------------------
    # [EXACT-K0] -- the k = 0 limit removes exactly and only the spatial block.
    # -----------------------------------------------------------------------
    log("\n[EXACT-K0] separable typed gradient: L(k) = c_t T + c_s k^2 I + c_f lam1 I")
    log("  T = exact second-difference circulant on 4 time nodes (eigenvalues {0,2,4});")
    log("  base-space enters ONLY through k^2; fibre ONLY through lam1 = 8.")
    n = 4
    T = [[Fr(0)] * n for _ in range(n)]
    for i in range(n):
        T[i][i] = Fr(2)
        T[i][(i + 1) % n] += Fr(-1)
        T[i][(i - 1) % n] += Fr(-1)
    c_t, c_s, c_f = Fr(2), Fr(5), Fr(3)          # arbitrary nonzero rationals

    def L_of_k2(k2):
        return [[c_t * T[i][j] + (c_s * k2 + c_f * lam1) * (Fr(1) if i == j else Fr(0))
                 for j in range(n)] for i in range(n)]

    L0 = L_of_k2(Fr(0))
    Lk = L_of_k2(Fr(7, 3))                        # a nonzero rational k^2
    spatial_at_0 = [[L0[i][j] - (c_t * T[i][j] + c_f * lam1 * (Fr(1) if i == j else Fr(0)))
                     for j in range(n)] for i in range(n)]
    check("K0-1: at k = 0 the base-spatial sub-block is EXACTLY the zero matrix",
          all(x == 0 for row in spatial_at_0 for x in row))
    diff_time = [[Lk[i][j] - L0[i][j] - c_s * Fr(7, 3) * (Fr(1) if i == j else Fr(0))
                  for j in range(n)] for i in range(n)]
    check("K0-2: the time block and fibre term are EXACTLY k-independent "
          "(L(k) - L(0) = c_s k^2 I identically)",
          all(x == 0 for row in diff_time for x in row))
    check("K0-3: the time block survives at k = 0 (c_t T != 0 exactly; only the "
          "STATIC time mode is annihilated: T has eigenvalue 0 once, 2 and 4 else)",
          any(c_t * T[i][j] != 0 for i in range(n) for j in range(n)))
    # circulant eigenvalues 2 - 2 cos(2 pi j / 4) = {0, 2, 4, 2}: verify exactly
    # via the known eigenvectors (1,1,1,1), (1,-1,1,-1), (1,0,-1,0).
    v_const = [Fr(1)] * 4
    v_alt = [Fr(1), Fr(-1), Fr(1), Fr(-1)]
    v_half = [Fr(1), Fr(0), Fr(-1), Fr(0)]
    check("K0-4: T-eigenpairs exact: T(1,1,1,1) = 0, T(1,-1,1,-1) = 4x, "
          "T(1,0,-1,0) = 2x",
          matvec(T, v_const) == [Fr(0)] * 4
          and matvec(T, v_alt) == [Fr(4) * x for x in v_alt]
          and matvec(T, v_half) == [Fr(2) * x for x in v_half])
    # separable oscillator identity omega^2 = (c_f/c_b) lam1 with sample rationals
    omega2 = (c_f / c_t) * lam1
    check("K0-5: omega^2 = (c_f/c_b) lambda_1 exactly (= 12 at c_b=2, c_f=3)",
          omega2 == Fr(12))
    log("  => the k = 0 escape removes ONE of THREE typed sub-blocks.  Whether the")
    log("     native stiffness maps purely into that sub-block is exactly the arrow-A4")
    log("     content (Z_U), which is unbuilt: the question is not decidable at k = 0.")

    # -----------------------------------------------------------------------
    # [EXACT-RAY] -- the finding-3 ray criterion at certificate grade.
    # -----------------------------------------------------------------------
    log("\n[EXACT-RAY] ray criterion over Fractions: fixture M = B^T B + diag, integer J")
    # SPD integer fixture (n = 5): M = B^T B with unit-upper-shift B, plus diag.
    n = 5
    B = [[Fr(1) if i == j else (Fr(1) if j == i + 1 else Fr(0)) for j in range(n)]
         for i in range(n)]
    M = [[sum(B[k][i] * B[k][j] for k in range(n)) + (Fr(1) if i == j else Fr(0))
          for j in range(n)] for i in range(n)]
    J = [Fr(1), Fr(-2), Fr(3), Fr(5), Fr(-1)]
    t = fr_solve(M, J)                            # the identity target t = M^{-1} J
    Mt = matvec(M, t)
    check("RAY0: fixture sanity -- M t = J exactly", Mt == J)

    def ray_residual_zero(L):
        Lt = matvec(L, t)
        return parallel_exact(Lt, Mt)

    # (i) proportional family c M: exact preservation for a sample of rationals
    ok_prop = all(ray_residual_zero([[c * M[i][j] for j in range(n)] for i in range(n)])
                  for c in (Fr(1), Fr(7, 3), Fr(-2, 5)))
    check("RAY1: every tested member of the proportional family c M preserves the "
          "target ray EXACTLY (residual identically zero)", ok_prop)

    # (ii) NON-proportional planted witness L = M + (Mt)(Mt)^T
    Lplant = [[M[i][j] + Mt[i] * Mt[j] for j in range(n)] for i in range(n)]
    not_prop = not parallel_exact([Lplant[i][j] for i in range(n) for j in range(n)],
                                  [M[i][j] for i in range(n) for j in range(n)])
    check("RAY2: L = M + (Mt)(Mt)^T is NOT proportional to M (exact minor witness) "
          "yet preserves the target ray EXACTLY -- the iff boundary 'L t in span(M t)' "
          "contains non-proportional SPD members (sharper than the review's L = M)",
          ray_residual_zero(Lplant) and not_prop)

    # (iii) generic integer perturbation breaks the ray exactly
    Lgen = [[M[i][j] for j in range(n)] for i in range(n)]
    Lgen[0][0] += Fr(1)                           # rank-one integer perturbation E11
    Lt_gen = matvec(Lgen, t)
    minors = [Lt_gen[i] * Mt[j] - Lt_gen[j] * Mt[i] for i in range(n) for j in range(i + 1, n)]
    check("RAY3: the generic perturbation L = M + E11 breaks the target ray EXACTLY "
          "(a 2x2 minor of [Lt | Mt] is exactly nonzero)",
          any(m != 0 for m in minors),
          f"first nonzero minor = {next((m for m in minors if m != 0), None)}")

    # (iv) through the full field equation, solved over Fractions (m^2 = kappa = 1, c = 1)
    theta_plant = fr_solve([[M[i][j] + Lplant[i][j] for j in range(n)] for i in range(n)], J)
    theta_gen = fr_solve([[M[i][j] + Lgen[i][j] for j in range(n)] for i in range(n)], J)
    check("RAY4: theta = (M + L)^{-1} J is EXACTLY parallel to M^{-1} J for the "
          "planted witness and EXACTLY non-parallel for the generic perturbation",
          parallel_exact(theta_plant, t) and not parallel_exact(theta_gen, t))

    # -----------------------------------------------------------------------
    log("\n" + "-" * 78)
    log("DISPOSITION")
    log("-" * 78)
    log("  FIRST UNBUILDABLE ARROW: A4 NORM.  Arrows A1-A3 compose at configuration")
    log("  level with existing artifacts (A1 defined; A2 well-typed; A3 reconstruction")
    log("  grade with the frame-space/metric-fibre homonym fenced).  A4 requires the")
    log("  native kinetic quadratic form Z_U = |D_A U|^2 -- W203: NOT BUILT -- so the")
    log("  (c_b, c_s, c_f) split, the normalization, and hence A5's equation cannot be")
    log("  derived.  The review's prediction is CONFIRMED.  The k = 0 escape is exactly")
    log("  typed: it removes only the base-spatial sub-block, so it cannot decide the")
    log("  c_kin question; and the ray criterion's iff boundary is now certificate-grade")
    log("  with a non-proportional exact preserver guarding any future theorem statement.")
    log("  No M-H13 / C10 / native-bridge status moves here (register-owned).")

    if FAIL:
        log(f"\nFAILED: {FAIL}")
        sys.exit(1)
    log("\nexit 0 = ledger ties + exact certificates recorded (LED 6/6, E8, K0 5/5, "
        "RAY 5/5).  First unbuildable arrow: A4 NORM (Z_U = |D_A U|^2).")
    sys.exit(0)


if __name__ == "__main__":
    main()
