#!/usr/bin/env python3
r"""
W48 / Path 2 -- Branch A: the Cutkosky / unitarity-cut test of keep-and-grade at one loop.

GU-INDEPENDENT. Concrete example: the Stelle massive-spin-2 graviton. This file encodes the
sign/residue bookkeeping of the ghost cut and turns the branch's one-loop optical-theorem finding
into deterministic assertions. It does NOT change any claim status.

CONSTRUCTIONS USED (fork discipline, GEOMETER-VS-PHYSICS-OBJECTS.md):
  * "the ghost"      = the WRONG-SIGN-RESIDUE pole in the partial-fraction split of the fourth-order
                       (induced |II|^2 / Stelle) spin-2 propagator. We KEEP it (keep-and-grade side),
                       we do not remove it. This is the standard-physics construction of the ghost;
                       GU's Krein [P,S]=0 grading is the intended physical-subspace selector, tested
                       here at the level of the cut, which is grading-agnostic.
  * "unitarity/cut"  = Cutkosky rules + largest-time equation in the INDEFINITE (Krein) metric.
                       We distinguish two notions that the loop separates:
                         (K) Krein pseudo-unitarity   S^dag eta S = eta   (automatic, all orders)
                         (P) physical-subspace positivity  2 Im M = sum_phys |M|^2 >= 0  (the prize)

PROPAGATOR SPLIT (with the overall-sign convention made explicit -- fork discipline):
    (1/m2^2) [ 1/p^2  -  1/(p^2 - m2^2) ]  ==  - 1/(p^2 (p^2 - m2^2))
  i.e. the brief's split form equals MINUS the bare product form. The overall sign is a CONVENTION
  (it is fixed by the overall sign of the induced |II|^2 action / which term you call the physical
  graviton); it carries no physics. The physics is entirely the RELATIVE minus between the two
  poles: the 1/p^2 term is the healthy massless graviton (residue +1) and the -1/(p^2 - m2^2) term
  is the ghost (residue -1). Cutting the ghost line carries a NEGATIVE spectral weight, so it
  contributes NEGATIVELY to a discontinuity. We keep the ghost (keep-and-grade), not remove it.

WHAT THE ONE-LOOP CUT SHOWS (the branch's honest finding, asserted below):
  1. Kallen-Lehmann spectral density of the split propagator has a NEGATIVE delta at s=m2^2
     -> KL positivity is violated -> indefinite (Krein) metric. Feature per the fork table, but it
     is exactly what makes the cut leak.
  2. A one-loop bubble has cuts weighted by the product of the two cut lines' spectral weights:
       graviton+graviton  (+1)(+1) = +1   (opens at s>0)         positive
       graviton+ghost      (+1)(-1) = -1   (opens at s>m2^2)      NEGATIVE  <- the leak
       ghost+ghost         (-1)(-1) = +1   (opens at s>4 m2^2)    positive
  3. If the ghost is treated as a STABLE asymptotic state graded only by the Krein form, the
     graviton+ghost cut injects a piece of Im M with NO positive-norm-state origin: the optical
     theorem 2 Im M = sum_phys |M|^2 (RHS >= 0) cannot hold. Negative probability leaks. FAILS.
  4. In Stelle gravity the massive spin-2 sits ABOVE threshold (it decays to two massless gravitons,
     threshold at s=0), so it is UNSTABLE: not an asymptotic state. Removing it from the physical
     sum AND deforming its cut away with a complex-conjugate-pole / CLOP / fakeon prescription makes
     2 Im M = sum_phys |M|^2 hold ON THE PHYSICAL SUBSPACE AT ONE LOOP. That prescription is the
     LOAD-BEARING ASSUMPTION -- Krein grading alone does not do it -- and it costs micro-causality.

  Reduction sanity check (persona 4): the Pais-Uhlenbeck / PT quantum mechanics optical theorem
  (Bender-Mannheim) is 0+1 dimensional: NO continuum threshold, so the ghost cut never opens and
  positivity is automatic. The loop is exactly where the continuum cut appears and infects Im M.
  That is why tree/QM positivity does NOT imply loop positivity.

Reproducible: python tests/W48_path2_A_cutkosky.py   (exit 0 on the asserted conclusion)
No canon/verdict/claim-status file touched. Exploration-grade.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

TOL = 1e-12
results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


# --------------------------------------------------------------------------------------------------
# 1. Propagator split + residue signs (the ghost = wrong-sign residue term)
# --------------------------------------------------------------------------------------------------

def full_prop(x: float, m2sq: float) -> float:
    """Fourth-order spin-2 denominator 1/(x (x - m2^2)), x = p^2 (Euclidean sample, x != 0, m2^2)."""
    return 1.0 / (x * (x - m2sq))


def split_prop(x: float, m2sq: float) -> float:
    """(1/m2^2)[ 1/x - 1/(x - m2^2) ]  -- the brief's partial-fraction convention."""
    return (1.0 / m2sq) * (1.0 / x - 1.0 / (x - m2sq))


def residue_massless() -> float:
    """Residue of the 1/p^2 term at p^2 = 0 (healthy graviton)."""
    return +1.0


def residue_ghost() -> float:
    """Residue of the -1/(p^2 - m2^2) term at p^2 = m2^2 (ghost: WRONG sign)."""
    return -1.0


# --------------------------------------------------------------------------------------------------
# 2. Cut arithmetic: spectral weights and two-particle-phase-space discontinuities
# --------------------------------------------------------------------------------------------------

def kallen(s: float, a2: float, b2: float) -> float:
    """Kallen triangle lambda(s, a^2, b^2)."""
    return s * s + a2 * a2 + b2 * b2 - 2.0 * (s * a2 + s * b2 + a2 * b2)


def two_body_phase(s: float, ma: float, mb: float) -> float:
    """4D two-body phase-space factor sqrt(lambda)/s /(16 pi), 0 below threshold."""
    thr = (ma + mb) ** 2
    if s <= thr:
        return 0.0
    lam = kallen(s, ma * ma, mb * mb)
    if lam <= 0.0:
        return 0.0
    return math.sqrt(lam) / s / (16.0 * math.pi)


@dataclass(frozen=True)
class CutChannel:
    """One two-particle cut of a one-loop bubble."""

    name: str
    ma: float
    mb: float
    weight: float  # product of the two cut lines' spectral weights (+1 healthy, -1 ghost line)

    def disc(self, s: float) -> float:
        """Signed contribution of this cut to 2 Im Pi(s) (unit couplings)."""
        return self.weight * two_body_phase(s, self.ma, self.mb)

    def is_physical(self) -> bool:
        """A cut is a physical (positive-norm asymptotic) channel iff no cut line is a ghost."""
        return self.weight > 0.0 and self.ma >= 0.0 and self.mb >= 0.0 and self.weight == 1.0


# Model: light matter/graviton = massless positive-norm line (weight +1); ghost line weight -1.
def build_channels(m2: float) -> dict[str, CutChannel]:
    return {
        "gg": CutChannel("graviton+graviton", 0.0, 0.0, +1.0),   # (+1)(+1)
        "gG": CutChannel("graviton+ghost", 0.0, m2, -1.0),        # (+1)(-1)  <- the leak
        "GG": CutChannel("ghost+ghost", m2, m2, +1.0),            # (-1)(-1)
    }


def signed_imM(channels: dict[str, CutChannel], s: float, mode: str) -> float:
    """2 Im M from Cutkosky (the discontinuity actually present in the analytic amplitude).

    mode = 'stable_ghost'  : ghost is an asymptotic state graded only by the Krein form; every cut
                             including graviton+ghost is present in Im M.
    mode = 'prescription'  : ghost is unstable (above the massless-graviton threshold); its cut is
                             deformed away by the complex-pole / CLOP / fakeon prescription.
    """
    total = 0.0
    for key, ch in channels.items():
        if mode == "prescription" and "ghost" in ch.name:
            continue  # contour prescription removes any cut touching the ghost line
        total += ch.disc(s)
    return total


def physical_positive_imM(channels: dict[str, CutChannel], s: float) -> float:
    """RHS of the optical theorem: sum over POSITIVE-NORM physical asymptotic states only (>= 0)."""
    return sum(ch.disc(s) for ch in channels.values() if ch.is_physical() and "ghost" not in ch.name)


def optical_theorem_residual(channels: dict[str, CutChannel], s: float, mode: str) -> float:
    """LHS - RHS. Zero == optical theorem holds on the physical subspace at this order."""
    return signed_imM(channels, s, mode) - physical_positive_imM(channels, s)


# --------------------------------------------------------------------------------------------------
# Run
# --------------------------------------------------------------------------------------------------

log("=" * 92)
log("W48 / PATH 2 -- BRANCH A: CUTKOSKY UNITARITY-CUT TEST OF KEEP-AND-GRADE (one loop)")
log("=" * 92)

m2 = 1.0
m2sq = m2 * m2

# --- 1. partial-fraction identity holds numerically at sample momenta ------------------------------
# Honest sign bookkeeping: (1/m2^2)[1/x - 1/(x-m2^2)] = -1/(x(x-m2^2)). The split equals MINUS the
# bare product form -- an overall-convention sign with no physics; the ghost content is the RELATIVE
# minus between the two poles, which is convention-independent.
sample_pts = [0.3, 0.7, 1.9, 4.2, 10.0, -2.5]
id_ok = all(abs(split_prop(x, m2sq) - (-full_prop(x, m2sq))) < TOL for x in sample_pts)
check(
    "A1  partial-fraction split (1/m2^2)[1/p^2 - 1/(p^2-m2^2)] = -1/(p^2(p^2-m2^2)) is exact; the "
    "overall sign is convention, the RELATIVE minus between the poles (the ghost) is the physics",
    id_ok,
    f"max|split - (-full)| < {TOL:g} over {len(sample_pts)} sample p^2",
)

# --- 2. residue signs: massless +1, ghost -1 ------------------------------------------------------
check(
    "A2  the ghost is the wrong-sign-residue pole: res(massless)=+1, res(ghost)=-1 "
    "(kept, not removed -- keep-and-grade side)",
    abs(residue_massless() - 1.0) < TOL and abs(residue_ghost() + 1.0) < TOL,
    f"res_massless={residue_massless():+.0f}, res_ghost={residue_ghost():+.0f}",
)

# --- 3. Kallen-Lehmann spectral weight of the ghost pole is NEGATIVE -> Krein/indefinite ----------
rho_massless = residue_massless() / m2sq   # weight of delta(s)      in rho(s)
rho_ghost = residue_ghost() / m2sq         # weight of delta(s-m2^2) in rho(s)
check(
    "A3  Kallen-Lehmann density rho(s) = (1/m2^2)[delta(s) - delta(s-m2^2)] has NEGATIVE weight at "
    "the massive pole -> KL positivity violated -> indefinite (Krein) metric (this is what leaks)",
    rho_massless > 0.0 and rho_ghost < 0.0,
    f"rho weights: massless={rho_massless:+.3f}, ghost={rho_ghost:+.3f}",
)

channels = build_channels(m2)

# --- 4. cut weights: graviton+ghost is the negative cut -------------------------------------------
check(
    "A4  two-particle cut weights: gg=+1, graviton+ghost=-1, ghost+ghost=+1 (one minus per ghost "
    "line); the graviton+ghost cut carries a NEGATIVE discontinuity",
    channels["gg"].weight == 1.0 and channels["gG"].weight == -1.0 and channels["GG"].weight == 1.0,
    "weights: gg=+1, gG=-1, GG=+1",
)

# --- 5. at s in (m2^2, 4 m2^2): gg and graviton+ghost open; graviton+ghost disc is < 0 -------------
s_mid = 2.5 * m2sq
disc_gg = channels["gg"].disc(s_mid)
disc_gG = channels["gG"].disc(s_mid)
disc_GG = channels["GG"].disc(s_mid)
check(
    "A5  at s = 2.5 m2^2: graviton+graviton cut > 0, graviton+ghost cut < 0, ghost+ghost cut still "
    "CLOSED (below its 4 m2^2 threshold) -- the negative cut is unavoidably in the amplitude here",
    disc_gg > 0.0 and disc_gG < 0.0 and disc_GG == 0.0,
    f"disc: gg={disc_gg:+.5f}, gG={disc_gG:+.5f}, GG={disc_GG:+.5f}",
)

# --- 6. STABLE-GHOST / Krein-grade-only: optical theorem VIOLATED on the physical subspace ---------
res_stable = optical_theorem_residual(channels, s_mid, mode="stable_ghost")
check(
    "A6  Q-cut FAIL branch: with the ghost a stable Krein-graded asymptotic state, 2 Im M carries "
    "the graviton+ghost piece that no positive-norm state can produce -> optical-theorem residual "
    "!= 0 -> negative probability leaks (case c)",
    abs(res_stable - disc_gG) < TOL and res_stable < 0.0,
    f"residual (LHS-RHS) = {res_stable:+.5f}  (= the negative graviton+ghost cut)",
)

# --- 7. PRESCRIPTION (unstable ghost + complex-pole/CLOP/fakeon): restored at ONE loop -------------
res_presc = optical_theorem_residual(channels, s_mid, mode="prescription")
check(
    "A7  Q-cut CONDITIONAL-PASS branch: the massive spin-2 is above threshold (decays to 2 massless "
    "gravitons) so it is UNSTABLE; removing it from physical states AND deforming its cut away "
    "(complex-conjugate pole / CLOP / fakeon) gives residual = 0 on the physical subspace AT ONE "
    "LOOP. That prescription -- NOT the Krein grading alone -- is the load-bearing assumption",
    abs(res_presc) < TOL,
    f"residual (LHS-RHS) = {res_presc:+.5f} with prescription (ghost cut removed)",
)

# --- 8. Krein pseudo-unitarity vs physical positivity: the two must be kept distinct ---------------
# Pseudo-unitarity S^dag eta S = eta is an algebraic identity (largest-time equation still holds in
# the indefinite metric). Model it as: the SIGNED cut sum equals the full Krein discontinuity always.
krein_identity_holds = True  # LTE/Cutkosky as an algebraic identity, independent of positivity
positivity_holds_stable = abs(res_stable) < TOL
positivity_holds_presc = abs(res_presc) < TOL
check(
    "A8  the loop SEPARATES the two notions: Krein pseudo-unitarity (S^dag eta S = eta) holds as an "
    "algebraic identity in BOTH modes, but physical-subspace POSITIVITY fails for the stable ghost "
    "and needs the prescription -- so 'unitary in the Krein metric' does not imply 'positive on the "
    "physical subspace'",
    krein_identity_holds and (not positivity_holds_stable) and positivity_holds_presc,
    f"pseudo-unitary={krein_identity_holds}, positive(stable)={positivity_holds_stable}, "
    f"positive(prescription)={positivity_holds_presc}",
)

# --- 9. Pais-Uhlenbeck / PT-QM reduction: NO continuum cut, so QM positivity is silent on loops ----
# 0+1 dim: two-body phase space has no continuum; encode as: the cut factor vanishes identically
# because there is no phase-space volume (all "thresholds" are isolated points, measure zero).
def qm_continuum_cut() -> float:
    return 0.0  # no continuum threshold in 0+1 QM -> the ghost cut never opens
check(
    "A9  cross-check: the Bender-Mannheim / Pais-Uhlenbeck QM optical theorem lives in 0+1 dim with "
    "NO continuum cut (qm_continuum_cut == 0), so tree/QM positivity says NOTHING about the loop "
    "cut -- exactly the gap this branch probes",
    qm_continuum_cut() == 0.0,
    "0+1-dim ghost cut identically closed",
)

# --- 10. adversary's process: light matter scattering through the s-channel ghost self-energy ------
# The graviton+ghost cut is present at ANY s > m2^2 in the s-channel bubble of chi chi -> chi chi;
# there is no kinematic window that removes it without a prescription. Confirm it stays negative
# across the whole window (m2^2, 4 m2^2).
window = [1.1, 1.6, 2.5, 3.4, 3.9]
adversary_all_negative = all(channels["gG"].disc(t * m2sq) < 0.0 for t in window)
check(
    "A10 adversary: across the entire window m2^2 < s < 4 m2^2 the graviton+ghost cut is negative "
    "-- no kinematic region evades it; only a contour prescription (extra input) can remove it",
    adversary_all_negative,
    f"graviton+ghost cut < 0 at s/m2^2 in {window}",
)

log("\n" + "=" * 92)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

# --------------------------------------------------------------------------------------------------
# Hard assertions -- the branch's asserted one-loop conclusion
# --------------------------------------------------------------------------------------------------
assert id_ok
assert abs(residue_ghost() + 1.0) < TOL
assert rho_ghost < 0.0
assert channels["gG"].weight == -1.0
assert disc_gG < 0.0 and disc_gg > 0.0 and disc_GG == 0.0
assert res_stable < 0.0, "stable-ghost optical-theorem leak must be negative (Q-cut FAIL branch)"
assert abs(res_presc) < TOL, "prescription must restore the optical theorem on the physical subspace"
assert (not positivity_holds_stable) and positivity_holds_presc
assert qm_continuum_cut() == 0.0
assert adversary_all_negative
assert npass == ntot, "some Branch A cut checks failed"

log("")
log("BRANCH A VERDICT (one loop, cut construction):")
log("  Q-cut : the ghost cut is PRESENT and NEGATIVE for a stable Krein-graded ghost -> optical")
log("          theorem fails on the physical subspace (case c, leak). It DECOUPLES at one loop ONLY")
log("          under a complex-pole / CLOP / fakeon prescription (ghost above threshold, unstable).")
log("          Grade: one-loop indication, load-bearing on the prescription. NOT a proof.")
log("  Q-pos : Krein pseudo-unitarity S^dag eta S = eta survives trivially; the POSITIVE physical")
log("          inner product surviving renormalization is prescription-dependent and NOT settled")
log("          here. Grade: plausibility only from the cut vantage.")
log("  Q-caus: the prescription that saves Q-cut (Lee-Wick complex poles / fakeon average-")
log("          continuation) VIOLATES micro-causality at the ghost scale -- unitarity bought with")
log("          causality. Grade: one-loop indication (NEGATIVE / traded).")
log("  ONE-KILLING-OBSTRUCTION: the CLOP ambiguity / wrong-sign width -- if no UNIQUE contour")
log("  prescription reproduces the same physical S-matrix beyond one loop, there is no construction-")
log("  independent physical subspace and the ghost cut re-leaks. This file settles nothing above one")
log("  loop and changes no claim status.")
raise SystemExit(0)
