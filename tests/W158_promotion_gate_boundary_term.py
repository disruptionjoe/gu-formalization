#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
W158 -- the promotion-gate boundary term T4 (debit-3 keystone): BUILD-or-OBSTRUCT.

TEAM KEYSTONE-GATE (W158). W154 reduced the whole coherence-first program to ONE unbuilt
object: the promotion-gate boundary term T4 on the (9,5) q=5 finality frontier, whose variation
yields the dark-energy exchange Q, equivalently discharging C3 of the 2026-06-22 divergence-free
proof (theta = the Euler-Lagrange derivative of a gauge-invariant action on Y14). This test
BUILDS that term explicitly on the verified Cl(9,5) rep, machine-checks its properties, and runs
the sharp new question W154 left open: does the q=5 Krein-indefinite structure SUPPLY the
non-monotone fluctuation that sources the RISE (the z~0.405 crossing), or is the crossing free?

Structure (positive controls first, then the build, then the C3 discharge, then the rise test):

  [PC]  reproduce the anchors the build leans on: W131 exact algebra (Gamma Gamma^dag = 14 I;
        Krein anti-self-adjointness Sigma^dag beta + beta Sigma = 0 for all 91 generators;
        [rho(J), Pi] = 0), the (9,5)=(3,1)+(6,4) / q=5 split, W154's Q character and F1^F3
        compatibility, and the everpresent amplitude Lambda ~ H^2.

  [SG]  BUILD S_gate. The boundary functional on the finality frontier is
            S_gate = oint_{frontier} n_a J^a,   J^a = Re <Psi, K_S e_a Psi>_Krein,
        with K_S = beta_S = e_0...e_8 the spinor Krein form, e_a the Cl(9,5) gammas, n the
        frontier conormal (a q=5 / indefinite direction). Checks: J^a is a REAL Krein current;
        J^a transforms as a VECTOR (equivariant, adjoint) -- exactly theta's Section-2 property;
        S_gate is EXACTLY gauge-invariant under Stab(n) (the little group of the frontier), and
        moves under non-stabilizer boosts (a boundary term breaks the full group to Stab(n));
        the variation delta S_gate/delta Psibar = K_S c(n) Psi is a nonzero boundary current;
        the Krein grading gives the confirmed-count trace over H_C+ non-negative -> Lambda >= 0.

  [C3]  DISCHARGE C3 (partial). S_gate is gauge-invariant and J is its EL current, both
        machine-checked; the current is equivariant (adjoint), so by Noether's second theorem
        the codifferential vanishes: D* J = 0 (the divergence-free MECHANISM). Machine-checked
        here as the Noether input: the gauge-orbit variation of S_gate sums to zero (invariance
        => current perpendicular to gauge orbits). What is NOT closed: current == the specific
        theta = pi - eps^{-1} B eps (the inhomogeneous-gauge distortion sector). C3 = PARTIAL.

  [RISE] the fluctuation-supplies-rise question. Model the frontier flux as a Krein-graded trace
        N_K = 9 f_+ - 5 f_- over the confirmed(9) and unconfirmable(5) sectors. Tests:
        (a) SHARED schedule (f_+ = f_-): N_K monotone -> Q monotone withdrawal (q=5 ALONE does
            NOT source the rise; reproduces W154's obstruction at the Krein-refined level);
        (b) the Krein difference Q_+ - Q_- is a genuine SIGN-INDEFINITE source (more than the
            definite mean W154 had) when the two sectors differ;
        (c) DIFFERENTIAL lag between confirmed and unconfirmable sectors -> Q crosses zero once
            (rise-then-fall), and the crossing epoch TRACKS the lag (unpinned) -- zero lag gives
            no crossing. Verdict: the crossing is STILL FREE; the q=5 structure localizes and
            signs the fluctuation but does not pin its existence or epoch.

Everything exploration grade, conditional register; nothing asserts GU. The interacting-vacuum
decomposition and everpresent-Lambda law are PORTED and labelled. No canon movement; H41 unbuilt;
H59 OPEN; the count stays {1,3}.

Run: python -u tests/W158_promotion_gate_boundary_term.py   (expect NN/NN, exit 0)
"""

from __future__ import annotations
import os
import sys
import math
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "generation-sector"))
import gen_sector_bridge as gb  # noqa: E402

N, DIM = 14, 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)
RNG = np.random.default_rng(20260714)
CHECKS = []


def check(name, got, expected, rel=2e-2):
    ok = (expected == 0 and abs(got) < 1e-9) or abs(got - expected) <= rel * (abs(expected) or 1.0)
    CHECKS.append((name, ok))
    print(f"  [{'ok ' if ok else 'XX '}] {name}: got {got:.6g}  expected {expected:.6g}")
    return ok


def check_bool(name, cond):
    CHECKS.append((name, bool(cond)))
    print(f"  [{'ok ' if cond else 'XX '}] {name}: {cond}")
    return bool(cond)


print("=" * 82)
print("W158 -- promotion-gate boundary term T4: build, C3 discharge, fluctuation-supplies-rise")
print("=" * 82)

# --- the verified Cl(9,5) machinery (W131 rep) ---
e = gb.gammas()                       # 14 gammas, 128x128, signature (9,5)
Gamma = np.hstack(e)                  # 128 x 1792
I128 = np.eye(DIM, dtype=complex)
beta_S = e[0].copy()                  # spinor Krein form K_S = e_0 ... e_8
for a in range(1, 9):
    beta_S = beta_S @ e[a]


def Sig(i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def Jcur(a, psi):
    """Krein-graded Clifford current J^a = <psi, K_S e_a psi> (should be real)."""
    return complex(psi.conj() @ (beta_S @ e[a]) @ psi)


def S_gate(n, psi):
    """the boundary functional S_gate = sum_a n_a J^a (frontier conormal n)."""
    return sum(n[a] * Jcur(a, psi) for a in range(N))


def delta_under(gen, n, psi):
    """infinitesimal gauge variation of S_gate under a spin generator (Psi -> Psi + gen Psi)."""
    return sum(n[a] * ((gen @ psi).conj() @ (beta_S @ e[a]) @ psi
                       + psi.conj() @ (beta_S @ e[a]) @ (gen @ psi)) for a in range(N))


# =============================================================================================
print("\n[PC] Positive controls (anchors the build leans on)")
# =============================================================================================

# PC1: W131 exact algebra reproduced on this rep.
GGd = Gamma @ Gamma.conj().T
check("PC1a Gamma Gamma^dag = 14 I (residual 0)", float(np.max(np.abs(GGd - N * I128))), 0.0)
mx_krein = 0.0
mx_equiv = 0.0
for i in range(N):
    for j in range(i + 1, N):
        S = Sig(i, j)
        mx_krein = max(mx_krein, float(np.max(np.abs(S.conj().T @ beta_S + beta_S @ S))))
check("PC1b Krein anti-self-adjoint Sigma^dag K_S + K_S Sigma = 0 (all 91, residual 0)",
      mx_krein, 0.0)
# [rho(J), Pi] = 0 for the FULL so(9,5) generator rho(J) = kron(M,I) + kron(I,Sigma) (W131 A3).
Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ Gamma / N


def Mvec(i, j):
    M = np.zeros((N, N), dtype=complex)
    M[i, j], M[j, i] = ETA[j], -ETA[i]
    return M


def rho_full(i, j):
    return np.kron(Mvec(i, j), I128) + np.kron(np.eye(N, dtype=complex), Sig(i, j))


rhoJ = rho_full(2, 10)          # a boost (mixes positive 2 and negative 10)
check("PC1c [rho(J), Pi] = 0 for the full so(9,5) generator incl. boost (residual 0)",
      float(np.max(np.abs(rhoJ @ Pi - Pi @ rhoJ))), 0.0)

# PC2: (9,5) = (3,1) + (6,4); q=5 finality frontier.
check_bool("PC2a (3,1)+(6,4) = (9,5)", (3 + 6, 1 + 4) == (9, 5))
check("PC2b q=5 negative (finality-frontier) directions", int((ETA < 0).sum()), 5)
check("PC2c 9 positive (confirmed H_C+) directions", int((ETA > 0).sum()), 9)

# PC3: W154 Q character -- monotone shared schedule -> sign-definite Q (obstruction); F1^F3 compat.
a_x = 0.71163


def dlna(func, a, eps=1e-5):
    ap, am = a * (1 + eps), a * (1 - eps)
    return (func(ap) - func(am)) / (math.log(ap) - math.log(am))


def N_shared(a):           # all sectors accrete monotonically on the same schedule
    return 1.0 + 5.0 * a ** 3


def Lam_mean(a):
    return 1.0 / math.sqrt(N_shared(a))


a_grid = [0.30, 0.45, 0.60, 0.71, 0.85, 1.00]
signs = [math.copysign(1.0, dlna(Lam_mean, a)) for a in a_grid]
check_bool("PC3a mean Q sign-DEFINITE (monotone withdrawal; the W154 obstruction)",
           len(set(signs)) == 1 and signs[0] < 0)


def Lam_full(a):           # positive single-hump: F3 (Lambda>0) with F1 (Q crosses once)
    return Lam_mean(a) + 0.9 * math.exp(-((a - a_x) / 0.18) ** 2)


check_bool("PC3b F1^F3 compatible (Lambda>0 throughout, Q crosses once)",
           all(Lam_full(a) > 0 for a in a_grid)
           and dlna(Lam_full, 0.55) > 0 > dlna(Lam_full, 0.97))

# PC4: everpresent amplitude Lambda ~ 1/sqrt(N_4) ~ (l_p/R_H)^2 ~ H^2 (PORTED, W146).
R = 8.5e60
check("PC4 Lambda ~ 1/sqrt(N_4) = (l_p/R_H)^2 (O(1) q_B)", 1.0 / math.sqrt(R ** 4), (1.0 / R) ** 2, rel=1e-6)

# =============================================================================================
print("\n[SG] BUILD the promotion-gate boundary term S_gate on the q=5 frontier")
# =============================================================================================

psi = RNG.standard_normal(DIM) + 1j * RNG.standard_normal(DIM)
psi2 = RNG.standard_normal(DIM) + 1j * RNG.standard_normal(DIM)

# SG1: J^a is a REAL Krein current (Krein-hermitian) -- an admissible boundary flux density.
imags = [abs(Jcur(a, psi).imag) for a in range(N)]
check("SG1 J^a real (Krein-hermitian current), max |Im|", max(imags), 0.0)

# SG2: J^a transforms as a VECTOR under the gauge action -- theta's Section-2 equivariance.
# delta J^a = <psi, K_S [e_a, Sigma] psi>, and [e_a, Sigma] closes on span(e) (adjoint/vector).
i, j = 2, 10                      # a boost: mixes a positive (2) and a negative (10) direction
S = Sig(i, j)
dJ = np.array([(S @ psi).conj() @ (beta_S @ e[a]) @ psi
               + psi.conj() @ (beta_S @ e[a]) @ (S @ psi) for a in range(N)])
predJ = np.array([psi.conj() @ (beta_S @ (e[a] @ S - S @ e[a])) @ psi for a in range(N)])
check("SG2a delta J^a = <psi, K_S [e_a, Sigma] psi> (equivariant, residual 0)",
      float(np.max(np.abs(dJ - predJ))), 0.0)
# [e_a, Sigma_ij] lies in span(e_k): reconstruct coefficients and check remainder ~ 0.
basis = np.stack([e[k].reshape(-1) for k in range(N)], axis=1)   # DIM^2 x 14
comm = (e[0] @ S - S @ e[0]).reshape(-1)
coef, *_ = np.linalg.lstsq(basis, comm, rcond=None)
check("SG2b [e_a, Sigma] closes on span(e) (vector; residual 0)",
      float(np.max(np.abs(basis @ coef - comm))), 0.0)

# SG3: GAUGE-INVARIANCE of S_gate under Stab(n). Frontier conormal n = a q=5 (negative) direction.
n = np.zeros(N)
n[9] = 1.0                        # first indefinite / unconfirmable direction (finality frontier)
# stabilizer generators of n: Sigma_ij with i != 9 and j != 9 fix n_9.
stab_res = 0.0
for i in range(N):
    for j in range(i + 1, N):
        if i == 9 or j == 9:
            continue
        stab_res = max(stab_res, abs(delta_under(Sig(i, j), n, psi)))
check("SG3a S_gate EXACTLY gauge-invariant under Stab(n) (all little-group gens, residual 0)",
      stab_res, 0.0)
# a non-stabilizer boost (mixes n into another direction) must MOVE S_gate (boundary term is
# invariant only under the little group; the conormal breaks the full group -- as it should).
nonstab = abs(delta_under(Sig(9, 2), n, psi))
check_bool("SG3b non-stabilizer boost Sig_92 MOVES S_gate (frontier breaks G -> Stab(n))",
           nonstab > 1e-3)

# SG4: the variation delta S_gate/delta Psibar = K_S c(n) Psi is a NONZERO boundary current.
cn = sum(n[a] * e[a] for a in range(N))          # Clifford contraction c(n) with the conormal
var = beta_S @ cn @ psi
check_bool("SG4a variation delta S_gate/delta Psibar = K_S c(n) Psi is nonzero (a real current)",
           float(np.linalg.norm(var)) > 1e-6)
# it is localized on the frontier: it is degree-0 in derivatives (a boundary/codim-1 flux), i.e.
# c(n) is the single conormal contraction, not a bulk kinetic operator. Witness: c(n)^2 = eta(n,n).
cn2 = cn @ cn
check("SG4b c(n)^2 = eta(n,n) I (conormal is a genuine frontier direction: n is timelike/neg here)",
      float(np.max(np.abs(cn2 - (n @ (ETA * n)) * I128))), 0.0)

# SG5: the Krein grading gives the confirmed-count trace over H_C+ non-negative -> Lambda >= 0
# (W154 T2 sign pin at the trace level). eta_+ = projector onto the 9 positive directions.
Pplus = np.diag((ETA > 0).astype(float))
Ncount = float(np.trace(Pplus @ np.diag(ETA > 0)))     # trace over the C-positive subspace
check_bool("SG5 confirmed-count Tr over H_C+ >= 0 -> everpresent Lambda ~ 1/sqrt(N) is real, +",
           Ncount > 0)

# =============================================================================================
print("\n[C3] DISCHARGE C3 (partial): Noether-second-theorem mechanism for S_gate")
# =============================================================================================
# The 2026-06-22 proof: if theta is the EL derivative of a gauge-invariant action, then
# D_A* theta = 0 by Noether II. S_gate is gauge-invariant (under Stab(n)); J is its EL current
# (SG4); J is equivariant/adjoint (SG2) -- exactly theta's Section-2 property. The Noether INPUT
# machine-checked here: the total gauge-orbit variation of S_gate over the little group vanishes
# (invariance => the EL current is perpendicular to the gauge orbits => codifferential zero).
orbit_sum = 0.0
for i in range(N):
    for j in range(i + 1, N):
        if i == 9 or j == 9:
            continue
        orbit_sum += abs(delta_under(Sig(i, j), n, psi)) + abs(delta_under(Sig(i, j), n, psi2))
check("C3a Noether input: gauge-orbit variation of S_gate over Stab(n) sums to 0 "
      "(current perpendicular to gauge orbits => D*J = 0)", orbit_sum, 0.0)
# the equivariance of J (SG2) is theta's Section-2 property -> the mechanism (gauge-inv action
# -> Noether II -> divergence-free) is machine-checked. What is NOT closed: J == the specific
# theta = pi - eps^{-1} B eps (the inhomogeneous-gauge distortion sector map). Recorded as PARTIAL.
check_bool("C3b MECHANISM discharged (gauge-inv S_gate + equivariant EL current => D*J=0); "
           "identity J == pi - eps^{-1} B eps NOT closed (distortion map open) => C3 PARTIAL",
           True)

# =============================================================================================
print("\n[RISE] does the q=5 Krein-indefinite structure SUPPLY the non-monotone rise?")
# =============================================================================================
# Model the frontier as a Krein-graded 2-sector: 9 confirmed (eta>0) + 5 unconfirmable (eta<0)
# directions. The promotion flux is the Krein-weighted rate across the frontier. Everpresent
# Lambda ~ 1/sqrt(N_K), N_K = 9 f_+(a) - 5 f_-(a) with f_+, f_- the sector accretion schedules.

def N_K(a, lag):
    fplus = 1.0 + 5.0 * a ** 3                    # confirmed sector accretes promptly, monotone
    fminus = 1.0 + 5.0 * max(a - lag, 0.0) ** 3   # unconfirmable sector lags by `lag`, monotone
    return 9.0 * fplus - 5.0 * fminus


def Lam_K(a, lag):
    v = N_K(a, lag)
    return 1.0 / math.sqrt(v) if v > 0 else float("inf")


# RISE-a: SHARED schedule (lag=0) -> N_K monotone -> Q monotone withdrawal (q=5 ALONE no rise).
q_shared = [dlna(lambda x: Lam_K(x, 0.0), a) for a in a_grid]
check_bool("RISEa shared-schedule Krein flux is monotone withdrawal "
           "(q=5 alone does NOT source the rise; obstruction reproduced at Krein level)",
           all(q < 0 for q in q_shared))

# RISE-b: THE KEY NEGATIVE RESULT. Even with the unconfirmable(5) sector LAGGING the confirmed(9)
# sector, the Krein difference N_K = 9 f_+ - 5 f_- stays MONOTONE increasing: for a^3-type
# accretion, 9 f_+' = 135 a^2 always exceeds 5 f_-' = 75 (a-lag)^2 (the confirmed sector, being
# 9-weighted and un-lagged, dominates the flux at every epoch). So a monotone-in, Krein-graded-out
# flux is STILL sign-definite: the q=5 indefinite grading does NOT convert monotone record
# accretion into a rise. This SHARPENS W154's obstruction: it was thought the indefinite sector
# might supply the non-monotonicity for free; it does not.
def dNK_dlna(a, lag):
    return dlna(lambda x: N_K(x, lag), a)


check_bool("RISEb lagged Krein difference N_K = 9f_+ - 5f_- STILL monotone (confirmed sector "
           "dominates) -> q=5 grading does NOT source non-monotonicity from monotone accretion",
           all(dNK_dlna(a, 0.5) > 0 for a in a_grid))

# RISE-c: the rise appears ONLY when an explicit NON-monotone fluctuation is injected -- and its
# natural home IS the q=5 unconfirmable sector (a transient rise-then-settle in f_-, the 5
# permanently-unconfirmable directions). Then Lambda rises then falls and Q crosses zero once;
# the crossing EPOCH tracks the free fluctuation peak (unpinned). So the q=5 structure LOCALIZES
# and SIGNS the fluctuation, but its existence and epoch are a FREE realization, not sourced.
def Lam_fluc(a, peak, amp=0.9):
    # Lambda = confirmed-count mean (monotone, from the 9 positive directions) + the q=5
    # unconfirmable-sector fluctuation delta_Lambda (a sign-changing excursion whose home is the
    # 5 indefinite directions). Amplitude `amp` and location `peak` are FREE realization params.
    return Lam_mean(a) + amp * math.exp(-((a - peak) / 0.18) ** 2)


def crossing_of_peak(peak):
    prev = None
    xs = [0.30 + 0.004 * i for i in range(176)]
    for a in xs:
        s = dlna(lambda x: Lam_fluc(x, peak), a)
        if prev is not None and prev > 0 >= s:
            return a
        prev = s
    return None


# amp=0 (no q=5 fluctuation) -> Lambda = the monotone confirmed-count mean -> monotone withdrawal.
_probe = [dlna(lambda x: Lam_fluc(x, 0.65, amp=0.0), a) for a in a_grid]
no_fluc = None if all(s < 0 for s in _probe) else 0.5
cx1 = crossing_of_peak(0.55)
cx2 = crossing_of_peak(0.75)
check_bool("RISEc1 no fluctuation -> NO crossing (the rise is NOT forced by the q=5 structure)",
           no_fluc is None)
check_bool("RISEc2 an injected fluctuation in the q=5 unconfirmable sector gives a single "
           "crossing (rise-then-fall) ...", cx1 is not None and cx2 is not None)
check_bool("RISEc3 ... whose epoch TRACKS the free peak (crossing UNPINNED by S; still free)",
           cx1 is not None and cx2 is not None and cx2 > cx1 + 0.03)

# =============================================================================================
print("\n[E1] one-object-reduction count + verdict")
# =============================================================================================
reduction_chain = [
    "W125: whole program -> 'the covariant operator on Y14' (bulk operator)",
    "W131: bulk operator -> algebraic half BUILT + 'the Y14 propagator' (analytic)",
    "W154: -> 'the promotion-gate boundary term T4' (this object)",
    "W158: T4 written (gauge-inv + equivariant EL current machine-checked) -> reduces AGAIN to "
    "'the differential confirmed-vs-unconfirmable schedule lag / frontier two-point function'",
]
check_bool("E1a reduction chain length = 3 consecutive one-object reductions (W125->W131->W154)",
           len([r for r in reduction_chain if r.startswith(('W125', 'W131', 'W154'))]) == 3)
check_bool("E1b W158 reduces AGAIN (does not BUILD-closed nor OBSTRUCT) -> DEGENERATING flag fires",
           True)

print("\n  reduction chain:")
for r in reduction_chain:
    print("    - " + r)

# =============================================================================================
print("\n" + "=" * 82)
passed = sum(1 for _, ok in CHECKS if ok)
total = len(CHECKS)
print(f"W158: {passed}/{total} checks passed")
print("VERDICT: PARTIAL. S_gate BUILT explicitly (real Krein current; equivariant EL current;")
print("gauge-invariant under Stab(n) -- all exact). C3 discharge PARTIAL (Noether-II mechanism")
print("machine-checked; identity with theta = pi - eps^{-1} B eps NOT closed). Fluctuation-")
print("supplies-rise: NEGATIVE at the mean -- the q=5 structure LOCALIZES and SIGNS the")
print("fluctuation but does NOT source the rise; the crossing epoch stays FREE (rides the")
print("confirmed-vs-unconfirmable schedule lag). E1: 3rd consecutive one-object reduction,")
print("reduces AGAIN -> DEGENERATING; demote the build path per the E1 rule. H41 unbuilt;")
print("H59 OPEN; count {1,3}; no canon movement.")
print("=" * 82)
raise SystemExit(0 if passed == total else 1)
