#!/usr/bin/env python3
r"""
W112 / PROTECTION SWEEP: the HORN-Q-ROBUST CORE of the two newest mathematical results (W107, W106).

THE QUESTION.  HORN K (f_2^2* = 0, the genuinely non-removable kept ghost) is truncation-conditional
(W95: FRONTIER, firmable-leaning, NOT a theorem).  The content story built on W107 (grading-blindness /
the grading-relative invariant) and W106 (per-state/sup separation) must therefore not silently assume
HORN K.  This test re-runs the W107 transversality computation and the W106 dichotomy computation as
CLASS STATEMENTS -- theorems about the class of Krein doublet towers, with the coupling/gap profile as
an explicit PARAMETER -- and verifies each clause on BOTH a horn-K-like profile (kept ghost, non-UV-soft
coupling: the wall fires) and a horn-Q-like profile (ghost removable / UV-soft entry: no wall).

THE HORN-INDEPENDENT RESTATEMENTS ENCODED (each checked on both horn-like profiles):

  H1 (per-mode identity, profile-free):  for EVERY r < 1,
        ||Delta_{phi o AdJ, phi}|| = (1+r)/(1-r) = cond(eta(r))   EXACTLY,
     and eta(-r) = (1-r^2) eta(r)^{-1}, F(phi, phi o J) = 1-r^2 exactly.  This is a statement about
     the Krein doublet fiber; no coupling profile, hence no horn, enters.

  H2 (grading-blindness, class-level):  the grading r -> -r preserves the Araki-Woods eigenvalue list
     ((1-r)/2, (1+r)/2) of EVERY mode of EVERY profile -- so every classical (algebra, state) invariant
     of the tower is grading-invariant, for the whole class at once.  Horn-independent.

  H3 (transversality, class-level):  "the wall is transverse to the classical ratio-set/type invariant"
     is a statement about the CLASS of towers: all four cells of (wall) x (0 in r_inf) are inhabited by
     explicit profiles {PHYS, SOFT, MARG, DERIV}.  Which cell PHYSICS lands in is the horn's only role;
     the four-cell table exists either way.

  H4 (the repaired identity as a biconditional over the class):
        wall(profile)  <=>  sup_k ||Delta_{phi o AdJ, phi}||_k = inf
     holds for EVERY profile -- verified TRUE=TRUE on the horn-K-like profile and FALSE=FALSE on the
     horn-Q-like profile.  A biconditional that holds on both sides of the horn is horn-independent.

  H5 (W106 dichotomy, class-level):  for any tower in the class, the strip form is the quadratic form
     of the multiplication operator by cost_strip(k) = (1-r_k)^{-1/2}:
       * horn-K-like (1-r_k ~ c k^{-(p+1)}): the operator is UNBOUNDED; finiteness holds exactly on
         tail exponents alpha > alpha*(p) = (p+3)/4; the unit-ball sup diverges (sqrt(2)/octave at p=0);
         Schwartz-decay states are inside for every polynomial p.
       * horn-Q-like (UV-soft): the operator is BOUNDED; every L^2 state is finite; the sup is finite.
     In BOTH cases the statement "per-state finiteness exactly on the form domain; sup = the operator
     norm" holds -- the dichotomy is the Reed-Simon form dichotomy, horn-independent; the horn only
     decides whether the operator is unbounded (i.e., whether the physical tower is in the wall
     subclass).

  H6 (coherence, class-level):  two regions differing by a scalar modular weight bounded below have
     tail classes that agree on overlaps -- on the horn-K-like profile both restrict to the SAME
     singular class (same 2P limit, same null line); on the horn-Q-like profile both restrict to the
     same INVERTIBLE class.  Coherent in both; the horn only picks which shared class.

  H7 (the honest converse):  the horn does NOT create or destroy the mathematics -- a non-UV-soft kept-
     ghost tower has the wall EVEN IF one imagines it under HORN Q, and a UV-soft tower has no wall
     even under HORN K.  The horn's entire role is whether GU's PHYSICAL tower is forced into the wall
     subclass (HORN K: kept ghost, non-UV-soft derivative coupling => in;  HORN Q: ghost removable =>
     the Krein tower is not forced at all).  Encoded: the wall predicate depends only on the profile
     argument, never on a horn flag.

Deterministic, numpy-only, self-validating; exit 0 on success.  No canon / RESEARCH-STATUS / CANON /
claim-status / verdict / posture file is touched.  Exploration-grade.  NOT committed by this run.
"""
from __future__ import annotations

import numpy as np

np.random.seed(0)

results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


SX = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
SY = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
SZ = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def eta(r: float) -> np.ndarray:
    return I2 + r * SY


def opnorm(A: np.ndarray) -> float:
    return float(np.linalg.norm(A, 2))


def dag(X: np.ndarray) -> np.ndarray:
    return X.conj().T


def mpow(A: np.ndarray, p: complex) -> np.ndarray:
    w, V = np.linalg.eigh(A)
    return V @ np.diag(np.exp(p * np.log(w))) @ dag(V)


# --- the tower CLASS: r_k = g_k / (g_k + Dw(k)/2), Dw ~ m2^2/2k (W98 mode data); the coupling/gap
# --- profile is the PARAMETER.  No horn flag exists anywhere in the wall computation (that IS H7).
M1, M2, G = 0.0, 0.30, 0.10


def dsplit(k: float) -> float:
    return abs(np.sqrt(k * k + M1 * M1) - np.sqrt(k * k + M2 * M2))


def r_of(g_k: float, k: float) -> float:
    return float(min(g_k / (g_k + 0.5 * dsplit(k)), 1.0 - 1e-15))


def cond_of(r: float) -> float:
    return (1.0 + r) / (1.0 - r)


def mu_of(r: float) -> float:
    return (1.0 - r) / 2.0


PROFILES = {
    # horn-K-like entry points into the class (kept ghost, non-UV-soft):
    "PHYS":  lambda k: G,                   # W98 physical p=0
    "DERIV": lambda k: G * k,               # derivative vertex p=1 (the arguably-physical HORN-K case)
    # horn-Q-like entry points (ghost removable / UV-soft; condition X):
    "SOFT":  lambda k: G / (k * k + 1.0),
    # mathematics-only profiles that inhabit the remaining transversality cells:
    "MARG":  lambda k: G / k,               # Powers plateau: 0 in r_inf, NO wall
}
HORN_K_LIKE, HORN_Q_LIKE = "PHYS", "SOFT"


def wall_of(name: str) -> bool:
    """The wall predicate: a function of the PROFILE ONLY (no horn flag) -- that is the point (H7)."""
    sups = []
    for a, b in ((1e3, 2e3), (8e3, 1.6e4), (6.4e4, 1.28e5)):
        ks = np.linspace(a, b, 400)
        sups.append(max(cond_of(r_of(PROFILES[name](float(k)), float(k))) for k in ks))
    return sups[2] > 3.0 * sups[1] and sups[2] > 1e3


log("=" * 100)
log("W112: the HORN-Q-ROBUST CORE -- W107/W106 re-run as CLASS statements, profile as parameter,")
log("      each clause checked on a horn-K-like AND a horn-Q-like profile.")
log("=" * 100)

# ====================================================================================================
# H1 -- per-mode identity: profile-free, hence horn-free.
# ====================================================================================================
log("\n[H1] Per-mode identity ||Delta_{phi o J, phi}|| = cond(eta(r)) EXACTLY -- no profile enters")
h1 = True
for r in np.concatenate([np.linspace(0.05, 0.95, 10), [0.99, 0.999, 0.99999]]):
    rho, sig = eta(r) / 2.0, (SZ @ eta(r) @ SZ) / 2.0
    h1 &= opnorm(sig - (1 - r * r) / 4.0 * np.linalg.inv(rho)) < 1e-11          # eta(-r)=(1-r^2)eta^{-1}
    h1 &= abs(opnorm(np.kron(sig, np.linalg.inv(rho).T)) - cond_of(r)) < 1e-9 * cond_of(r)
    sr = np.linalg.cholesky(rho)
    F = float(np.sum(np.sqrt(np.maximum(np.linalg.eigvalsh(dag(sr) @ sig @ sr), 0.0)))) ** 2
    h1 &= abs(F - (1 - r * r)) < 1e-9
check("H1  the grading-relative modular identity is a statement about the Krein doublet FIBER "
      "(every r < 1): ||Delta_rel|| = cond exactly, eta(-r) = (1-r^2)eta(r)^{-1}, F = 1-r^2.  "
      "No coupling profile appears, hence no horn dependence is even expressible.", h1)

# ====================================================================================================
# H2 -- grading-blindness at the CLASS level: r -> -r preserves the eigenvalue list of every mode of
#       every profile (so every classical (algebra, state) invariant is grading-invariant class-wide).
# ====================================================================================================
log("\n[H2] Grading-blindness: r -> -r preserves every Araki-Woods eigenvalue list, EVERY profile")
h2 = True
for nm in PROFILES:
    for k in (1.0, 1e2, 1e4, 1e6):
        r = r_of(PROFILES[nm](float(k)), float(k))
        ev_p = np.sort(np.linalg.eigvalsh(eta(r) / 2.0))
        ev_m = np.sort(np.linalg.eigvalsh((SZ @ eta(r) @ SZ) / 2.0))
        h2 &= bool(np.allclose(ev_p, ev_m, atol=1e-14))
check("H2  the grading twist preserves the per-mode eigenvalue list ((1-r)/2, (1+r)/2) for every mode "
      "of every profile: the ITPFI/Connes data of the twisted tower equals that of the untwisted one "
      "CLASS-WIDE.  Grading-blindness of the classical classification is horn-independent.", h2)

# ====================================================================================================
# H3 -- transversality as a CLASS statement: all four (wall) x (0 in r_inf) cells inhabited by explicit
#       profiles.  The horn picks physics' cell; the table exists either way.
# ====================================================================================================
log("\n[H3] Transversality: the four-cell table is a property of the CLASS, not of the horn")
wall = {nm: wall_of(nm) for nm in PROFILES}
# 0 in r_inf from the same Araki-Woods criteria W107 T3 established (re-derived summarily here):
#   PHYS: lam ~ c/k slowly varying, non-summable  => III_1        => 0 in r_inf
#   DERIV: mu_k summable                           => type I_inf   => 0 not in r_inf
#   SOFT: sum(1/2-mu)^2 < inf                      => II_1         => 0 not in r_inf
#   MARG: lam -> const                             => Powers III   => 0 in r_inf
lam = lambda nm, k: (1 - r_of(PROFILES[nm](k), k)) / (1 + r_of(PROFILES[nm](k), k))
klam_spread = max(k * lam("PHYS", k) for k in (1e3, 1e5)) / min(k * lam("PHYS", k) for k in (1e3, 1e5))
deriv_tail = sum(mu_of(r_of(PROFILES["DERIV"](float(k)), float(k))) for k in np.linspace(1e4, 1e6, 20000)) * (1e6 - 1e4) / 20000
soft_tail = sum((0.5 - mu_of(r_of(PROFILES["SOFT"](float(k)), float(k)))) ** 2 for k in np.linspace(1e4, 1e6, 20000)) * (1e6 - 1e4) / 20000
marg_plateau = abs(lam("MARG", 1e4) - lam("MARG", 1e6)) < 5e-3
criteria_ok = klam_spread < 1.02 and deriv_tail < 1e-3 and soft_tail < 1e-3 and marg_plateau
zero_in_rinf = {"PHYS": True, "SOFT": False, "MARG": True, "DERIV": False}
cells = {(wall[nm], zero_in_rinf[nm]) for nm in PROFILES}
h3 = criteria_ok and cells == {(True, True), (True, False), (False, True), (False, False)} \
    and wall == {"PHYS": True, "DERIV": True, "SOFT": False, "MARG": False}
check("H3  all four (wall) x (0 in r_inf) cells are inhabited by explicit profiles "
      "{PHYS, DERIV, SOFT, MARG} -- the transversality of the wall to the classical invariant is a "
      "theorem about the tower CLASS.  The horn only selects which profile is GU's physical one; "
      "the table (and hence the finer-invariant necessity) exists under either horn.",
      h3, f"wall map={wall}, criteria ok={criteria_ok}")

# ====================================================================================================
# H4 -- the repaired identity as a biconditional over the class: TRUE=TRUE on horn-K-like,
#       FALSE=FALSE on horn-Q-like.
# ====================================================================================================
log("\n[H4] wall <=> sup ||Delta_rel|| = inf: holds on BOTH horn-like profiles (and on all four)")
h4 = True
sup_norms = {}
for nm in PROFILES:
    ks = np.linspace(6.4e4, 1.28e5, 300)
    sup_norm = max(cond_of(r_of(PROFILES[nm](float(k)), float(k))) for k in ks)   # = max ||Delta_rel||_k (H1)
    sup_norms[nm] = sup_norm
    h4 &= (wall[nm] == (sup_norm > 1e4))
h4 &= wall[HORN_K_LIKE] and (sup_norms[HORN_K_LIKE] > 1e4)          # both sides TRUE under horn-K-like
h4 &= (not wall[HORN_Q_LIKE]) and (sup_norms[HORN_Q_LIKE] < 10.0)   # both sides FALSE under horn-Q-like
check("H4  the repaired identity  wall <=> sup_k ||Delta_{phi o J, phi}||_k = inf  holds for every "
      f"profile: TRUE=TRUE on horn-K-like (sup {sup_norms[HORN_K_LIKE]:.1e}) and FALSE=FALSE on "
      f"horn-Q-like (sup {sup_norms[HORN_Q_LIKE]:.2f}).  A biconditional verified on both sides of "
      "the horn carries no horn dependence.", h4)

# ====================================================================================================
# H5 -- the W106 dichotomy as a CLASS statement: the strip form's Reed-Simon dichotomy holds with the
#       profile as parameter -- unbounded case (horn-K-like) and bounded case (horn-Q-like).
# ====================================================================================================
log("\n[H5] Per-state/sup dichotomy: form-domain statement in BOTH the unbounded and bounded case")
# horn-K-like, p = 0 and p = 1: cost_strip(k) = (1-r_k)^{-1/2} ~ k^{(p+1)/2} -- unbounded.
h5 = True
for p, alpha_star in ((0, 0.75), (1, 1.0)):
    g = lambda k: G * k ** p
    cost = lambda k: (1.0 - r_of(g(float(k)), float(k))) ** -0.5
    # measured growth exponent ~ (p+1)/2:
    ex = np.log(cost(1e6) / cost(1e4)) / np.log(1e2)
    h5 &= abs(ex - (p + 1) / 2.0) < 0.03
    # per-state finiteness exactly above alpha*(p) = (p+3)/4; divergence at/below (octave-ratio test):
    for alpha, conv in ((alpha_star + 0.15, True), (alpha_star - 0.10, False)):
        octs = []
        for a in (1e3, 8e3, 6.4e4):
            ks = np.linspace(a, 8 * a, 4000)
            octs.append(sum(cost(k) * k ** (-2 * alpha) for k in ks) * (7 * a / 4000))
        ratio = octs[2] / octs[1]
        h5 &= (ratio < 0.75) if conv else (ratio > 1.15)
    # the unit-ball sup diverges (normalized UV-edge runaway):
    h5 &= cost(1.28e5) / cost(6.4e4) > 1.35 if p == 0 else cost(1.28e5) > cost(6.4e4)
# horn-Q-like: cost_strip is BOUNDED -- every L^2 state finite, sup finite:
cost_q = [(1.0 - r_of(PROFILES["SOFT"](float(k)), float(k))) ** -0.5 for k in np.linspace(1.0, 1e6, 2000)]
h5 &= max(cost_q) < 2.0
check("H5  the dichotomy is the Reed-Simon form dichotomy WITH THE PROFILE AS PARAMETER: horn-K-like "
      "towers give an unbounded multiplication operator ~ k^{(p+1)/2} (measured exponents match "
      "(p+1)/2 to <0.03), finite exactly above alpha*(p) = (p+3)/4 (checked converge/diverge on both "
      "sides at p=0 and p=1) with divergent unit-ball sup; the horn-Q-like tower gives a BOUNDED "
      f"operator (sup cost {max(cost_q):.3f} < 2): every L^2 state finite, sup finite.  In both cases "
      "'finite exactly on the form domain; sup = operator norm' holds -- the theorem is about the "
      "class; the horn only decides whether the physical tower is in the unbounded subclass.", h5)

# ====================================================================================================
# H6 -- coherence as a CLASS statement: scalar weights bounded below => tail classes agree on the
#       overlap, on BOTH horn-like profiles (singular-singular vs invertible-invertible).
# ====================================================================================================
log("\n[H6] Tail-class coherence on overlaps: holds on both horn-like profiles")
W1, W2 = 1.0, 0.45
# horn-K-like: both regions -> the same singular class (metric difference compact, same 2P):
met = [opnorm(eta(r_of(G * W1, k)) - eta(r_of(G * W2, k))) for k in (1e2, 1e5)]
both_2P = all(opnorm(eta(r_of(G * w, 1e5)) - eta(1.0)) < 1e-3 for w in (W1, W2))
cohere_K = met[0] > met[1] and met[1] < 1e-4 and both_2P
# horn-Q-like: both regions' tails are invertible (min eigenvalue bounded below) -- same class again:
mins_q = [min(1.0 - r_of(PROFILES["SOFT"](float(k)) * w, float(k)) for k in np.linspace(1e3, 1e5, 200))
          for w in (W1, W2)]
cohere_Q = min(mins_q) > 0.9
h6 = cohere_K and cohere_Q
check("H6  with scalar modular weights bounded below, the per-region tail classes agree on overlaps "
      "under EITHER horn-like profile: horn-K-like -> both regions in the same SINGULAR class "
      f"(metric diff {met[1]:.1e} compact, same 2P); horn-Q-like -> both INVERTIBLE "
      f"(tail min-eig {min(mins_q):.3f}).  Coherence is a class property; the horn picks which shared "
      "class.", h6)

# ====================================================================================================
# H7 -- the honest converse: the wall predicate is a function of the PROFILE ONLY.  Cross-check: a
#       non-UV-soft tower walls regardless of any horn labeling; a UV-soft tower never walls.  (The
#       horn's entire role is upstream: whether GU's physics forces a kept-ghost non-UV-soft tower.)
# ====================================================================================================
log("\n[H7] The wall is profile-functional: no horn flag exists in the mathematics")
h7 = wall_of("PHYS") and wall_of("DERIV") and (not wall_of("SOFT")) and (not wall_of("MARG"))
check("H7  wall(profile) computed identically with no horn input: non-UV-soft profiles wall "
      "(PHYS, DERIV), UV-soft/marginal do not (SOFT, MARG).  HORN K vs HORN Q never enters the "
      "computation -- it only determines (upstream, via W95/W98) whether GU's physical tower is a "
      "kept-ghost non-UV-soft member of the class.  Under HORN Q the theorems stand as mathematics; "
      "the story's PHYSICAL clause ('GU's tower exhibits the wall') is the only horn-conditional "
      "part.", h7)

# ====================================================================================================
# SUMMARY
# ====================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, okk, _ in results if okk)
log(f"CHECKS: {npass}/{len(results)} passed.")
assert all(okk for _, okk, _ in results), "some W112 checks FAILED"

log("")
log("W112 VERDICT (this file encodes the horn-robust core, not a claim-status change):")
log("  * The W107 results (per-mode grading-relative identity; grading-blindness; transversality;")
log("    the repaired biconditional; class coherence) and the W106 dichotomy are CLASS statements")
log("    about Krein doublet towers with the coupling profile as a parameter.  Every clause verified")
log("    on BOTH a horn-K-like and a horn-Q-like profile.  No horn flag exists in any computation.")
log("  * HORN K's only role is upstream membership: whether GU's physical tower is forced into the")
log("    kept-ghost non-UV-soft (wall) subclass.  Under HORN Q the mathematics survives unchanged;")
log("    what narrows is the physical clause, exactly as W109 U9 already recorded.")
log("  * No canon / RESEARCH-STATUS / CANON / verdict / posture change.  Present, do not decide.")
raise SystemExit(0)
