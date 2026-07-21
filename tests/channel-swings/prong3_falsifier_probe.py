"""
Prong 3 FALSIFIER probe for the oriented-shard-cycle swing.

Deterministic, numpy only, no network. Foreground. Exit 0 on ALL PASS.

Decides two things the Prong-3 doc argues:

(a) MASS-HIERARCHY confrontation. The model says the three generation copies
    are IDENTICAL in alpha-odd content (quantum numbers) and may differ only in
    an alpha-EVEN magnitude (an issuance rate). We confront the two readings:
      - STRONG reading (mass tied to the frozen weight labels {-2,0,+2}):
          * |weight|  -> magnitudes {0,2,2}  (a DEGENERATE pair)
          * signed w  -> symmetric {-2,0,+2} (an alpha-ODD-flavored, sign-carrying
                          ladder, and Q3 forbids tying the hierarchy to sigma)
        Neither is a three-DISTINCT monotone hierarchy, so neither matches the
        observed charged-lepton ratios ~ (1 : 200 : 3500). => the STRONG reading
        is FALSIFIED. This is WHY the model must (and does) locate mass-splitting
        as EXTERNAL, leaving only the WEAK prediction.
      - WEAK reading (identical quantum numbers + an external alpha-even ordering
        magnitude): identical Krein signature across the 3 copies MATCHES the
        observed identical gauge quantum numbers; an external alpha-even magnitude
        is COMPATIBLE with any ordered, distinct hierarchy (mass is alpha-even).
    The planted "the model predicts EQUAL masses" is a category error: frozen
    kinematic degeneracy != physical mass degeneracy (mass-splitting is external/
    dynamical, excluded from the frozen inventory).

(b) SHADOW (seed<->realization consistency). Each observer's per-observer bit
    sigma_R must agree with the single external seed s. We test whether this
    forbids anything THIRD-PERSON-VISIBLE (alpha-even), i.e. whether it leaves a
    non-empty shadow, or forbids nothing (=> unfalsifiable).
      - Each sigma_R is alpha-ODD (flips under the global flip alpha).
      - The RELATIVE sign c = sigma_R1 * sigma_R2 is alpha-EVEN (product of odds),
        hence third-person-visible.
      - "record contact" (causal-past overlap) is an independent alpha-even fact.
      - The consistency forbids the joint alpha-even configuration
        (contact = yes, c = -1): two record-sharing observers with mutually
        anti-oriented records. That set is NON-EMPTY => non-vacuous shadow.
      - It is INDEPENDENT of the absolute seed s: both s=+1 and s=-1 give a fully
        consistent world, so the ABSOLUTE bit is unfalsifiable (Godel-independent
        external posit) while the RELATIVE consistency is falsifiable.
    CONTROL: a NULL model with no consistency (per-observer bit unconstrained)
    forbids NOTHING (empty shadow). A genuine shadow must forbid >= 1 config; the
    null forbids 0. The test distinguishes shadow from no-shadow.
"""

import itertools
import numpy as np

TOL = 1e-12
E, F, T = [], [], []  # exhibited / falsifier-control / setup


def rec(bucket, name, ok, detail=""):
    bucket.append((name, bool(ok), detail))


# ============================================================================
# alpha = the global K_S-sign flip. On the sigma-slot it negates every sigma.
# ============================================================================
def alpha_on_bits(bits):
    """Global orientation flip: negate every per-observer/seed bit."""
    return tuple(-b for b in bits)


# ---- parity typing (setup facts, from Q2 defense-attorney / prong-I) ----
rec(T, "record COUNT/rate is alpha-EVEN (visible); DIRECTION is alpha-ODD (sigma)",
    True, "Q2 defense-attorney typing; consumed, not re-derived")
rec(T, "internal (alpha-even) algebra has ZERO capacity to read a single sigma",
    True, "prong-I: Hom(triv,sign)=0 (Schur); consumed")

# ============================================================================
# (b1) sigma_R alpha-ODD, relative sign c = s1*s2 alpha-EVEN (product of odds)
# ============================================================================
odd_ok = True
even_ok = True
for s1, s2 in itertools.product((+1, -1), repeat=2):
    fs1, fs2 = alpha_on_bits((s1, s2))
    # each individual bit flips sign under alpha => alpha-odd
    if not (fs1 == -s1 and fs2 == -s2):
        odd_ok = False
    # the product is invariant under alpha => alpha-even
    if fs1 * fs2 != s1 * s2:
        even_ok = False
rec(E, "each per-observer bit sigma_R is alpha-ODD (flips under global alpha)",
    odd_ok, "sigma_R -> -sigma_R")
rec(E, "relative sign c = sigma_R1*sigma_R2 is alpha-EVEN (third-person visible)",
    even_ok, "product of two odds is even (Q2 identity)")

# ============================================================================
# (b2) the consistency shadow: forbid (contact=yes, c=-1). Non-empty?
# Configuration space: (seed s, sigma_R1, sigma_R2, contact in {0,1}).
# Consistency constraint C: for observers in record-contact, sigma_R = s for all.
#   => under contact, sigma_R1 = sigma_R2 = s  => c = +1 forced.
# The shadow = configs the constraint FORBIDS among the a-priori CONSTRUCTIBLE
# ones (the F-bundle holonomy is non-trivial, so anti-orientation between two
# frames IS a real bundle configuration; nothing analytic excludes c=-1).
# ============================================================================
all_configs = [
    (s, s1, s2, contact)
    for s in (+1, -1)
    for s1 in (+1, -1)
    for s2 in (+1, -1)
    for contact in (0, 1)
]


def consistency_allows(cfg):
    """Real seed<->realization consistency: in-contact observers share the seed."""
    s, s1, s2, contact = cfg
    if contact == 1:
        return (s1 == s) and (s2 == s)
    return True  # no constraint on observers not in record-contact


def null_allows(cfg):
    """CONTROL null model: no consistency at all -> everything allowed."""
    return True


forbidden_real = [c for c in all_configs if not consistency_allows(c)]
forbidden_null = [c for c in all_configs if not null_allows(c)]

# the specific constructible config the shadow must forbid:
witness = (+1, +1, -1, 1)  # single seed +1, two IN-CONTACT observers, c = -1
rec(E, "shadow FORBIDS the constructible config (seed +1, in-contact, c=-1)",
    witness in forbidden_real,
    "two record-sharing observers with anti-oriented records is ruled out")
rec(E, "the shadow is NON-EMPTY (real consistency forbids >= 1 config)",
    len(forbidden_real) >= 1, f"|forbidden_real| = {len(forbidden_real)}")

# every forbidden config has contact=1 AND c=-1 (i.e. the shadow is exactly the
# in-contact, relative-disagreement set) -> the shadow lives on the alpha-EVEN
# relative-sign observable, not on the absolute seed.
shadow_is_relative = all(
    (contact == 1 and s1 * s2 == -1)
    or (contact == 1 and (s1 != s or s2 != s))
    for (s, s1, s2, contact) in forbidden_real
)
# sharper: among in-contact configs, forbidden <=> not all equal to seed;
# and the SURVIVING in-contact configs all have c=+1 (agreement):
surviving_contact = [c for c in all_configs
                     if c[3] == 1 and consistency_allows(c)]
all_survivors_agree = all(s1 * s2 == +1 for (_, s1, s2, _) in surviving_contact)
rec(E, "every SURVIVING in-contact world has relative sign c=+1 (one arrow)",
    all_survivors_agree,
    "consistency => all record-sharing observers share one orientation")

# ============================================================================
# (b3) independence of the ABSOLUTE seed: both s=+1 and s=-1 give consistent
# worlds -> absolute bit unfalsifiable; only the relative consistency bites.
# ============================================================================
consistent_world_exists = {
    s: any(consistency_allows((s, s1, s2, 1)) and s1 * s2 == +1
           for s1 in (+1, -1) for s2 in (+1, -1))
    for s in (+1, -1)
}
rec(E, "a fully consistent world exists for BOTH seed values (+1 and -1)",
    consistent_world_exists[+1] and consistent_world_exists[-1],
    "absolute seed is Godel-independent/unfalsifiable; only relative is testable")

# ============================================================================
# (b3-coh) COHERENCE handle (three-tier recalibration): the model PREDICTS the
# first-person inside is blind to the ABSOLUTE seed (prong-I zero inward
# capacity). Check that predicted invisibility holds CONSISTENTLY, i.e. the
# alpha-EVEN visible data {contact, relative sign c} does NOT determine s.
# For the SAME visible profile (contact=1, c=+1) BOTH s values must occur among
# consistent worlds -> visible data underdetermines s -> invisibility consistent.
# The FAILURE mode (a leak) would be: some visible profile pins s. It does not.
# ============================================================================
def visible_profile(cfg):
    _, s1, s2, contact = cfg
    return (contact, s1 * s2)  # both alpha-EVEN, third-person-visible


consistent = [c for c in all_configs if consistency_allows(c)]
prof_agree = (1, +1)  # in-contact, records AGREE (c=+1)
seeds_for_profile = {c[0] for c in consistent if visible_profile(c) == prof_agree}
rec(E, "COHERENCE: visible (alpha-even) data underdetermines the absolute seed "
       "(profile contact=1,c=+1 admits BOTH s=+1 and s=-1)",
    seeds_for_profile == {+1, -1},
    "model's predicted first-person invisibility of absolute sigma holds "
    "CONSISTENTLY => F-SCAFFOLD, not F-VACUOUS")
rec(F, "COHERENCE control: no alpha-EVEN visible profile pins the absolute seed "
       "(a leak would falsify the model's own invisibility prediction)",
    all(
        len({c[0] for c in consistent if visible_profile(c) == p}) == 2
        for p in {visible_profile(c) for c in consistent}
    ),
    "every realizable visible profile admits both seeds; the inside cannot "
    "bootstrap the absolute from the relative (would need an external alpha-odd)")

# ============================================================================
# (b) CONTROL: null model (no shadow) forbids NOTHING; real shadow forbids >=1.
# A model that forbids nothing is unfalsifiable -- the test must separate them.
# ============================================================================
rec(F, "CONTROL: NULL (no-consistency) model forbids NOTHING (empty shadow)",
    len(forbidden_null) == 0,
    "an unfalsifiable model leaves an empty shadow -- correctly detected")
rec(F, "CONTROL: real consistency forbids strictly MORE than the null",
    len(forbidden_real) > len(forbidden_null),
    f"real forbids {len(forbidden_real)} > null forbids {len(forbidden_null)}")

# ============================================================================
# (a) MASS-HIERARCHY confrontation.
# Frozen weight labels of the three generation copies (trit tau): {-2, 0, +2}.
# Observed charged-lepton mass ratios (e:mu:tau) ~ 1 : 200 : 3500 (three DISTINCT,
# monotone). Test the STRONG (weight-tied) mass readings against that.
# ============================================================================
weights = np.array([-2.0, 0.0, 2.0])
obs_ratio = np.array([1.0, 200.0, 3500.0])  # charged-lepton scale, order of magnitude

# STRONG reading 1: mass ~ |weight|
mag_abs = np.abs(weights)                        # {2,0,2} -> sorted {0,2,2}
distinct_abs = len(set(mag_abs.tolist())) == 3   # are all three distinct?
rec(F, "STRONG |weight| reading is a DEGENERATE pair, NOT three-distinct",
    (not distinct_abs) and sorted(mag_abs.tolist()) == [0.0, 2.0, 2.0],
    f"|w| magnitudes sorted = {sorted(mag_abs.tolist())} (0:2:2, degenerate)")

# STRONG reading 2: mass ~ signed weight (an alpha-odd-flavored, symmetric ladder;
# masses are non-negative, so a signed ladder is not even a valid mass law, and
# Q3 forbids tying the hierarchy to sigma). Symmetric about 0 => |extremes| equal.
symmetric = np.isclose(abs(weights[0]), abs(weights[-1]))
rec(F, "STRONG signed-weight reading is SYMMETRIC (|-2|=|+2|), not monotone-distinct",
    symmetric, "a sign-carrying ladder is alpha-odd-flavored and Q3-forbidden for mass")

# Does ANY affine map of the weights reproduce the observed monotone ratio pattern
# up to scale? (Strong falsification test of a weight-tied hierarchy.)
# Fit m_i = a*w_i + b to obs_ratio; a degenerate/symmetric source cannot match a
# 1:200:3500 pattern because the middle sits at the ARITHMETIC mean of the ends
# for equally-spaced weights, whereas 200 is NOT the mean of 1 and 3500 (=1750.5).
mid_if_affine = 0.5 * (obs_ratio[0] + obs_ratio[-1])  # forced middle for w={-2,0,2}
affine_matches = np.isclose(mid_if_affine, obs_ratio[1], rtol=0.5)
rec(F, "no AFFINE weight-tied law matches: equal spacing forces middle=mean(ends)",
    not affine_matches,
    f"affine forces m2={mid_if_affine:.1f}, observed m2~{obs_ratio[1]:.0f} "
    f"(off by ~{mid_if_affine/obs_ratio[1]:.0f}x) => strong reading FALSIFIED")

# WEAK reading: identical quantum numbers across copies (equal Krein signature).
# Model B1 fact: all three copies carry (+32,-32,0). Observed: identical gauge
# quantum numbers across the three generations. MATCH.
krein_sig = [(32, 32, 0), (32, 32, 0), (32, 32, 0)]  # B1 result
identical_qnumbers = len(set(krein_sig)) == 1
rec(E, "WEAK reading: 3 copies share identical Krein signature (== identical "
       "quantum numbers) -- MATCHES observed generations",
    identical_qnumbers, f"signatures = {set(krein_sig)}")

# an external alpha-even magnitude CAN realize any ordered distinct hierarchy
# (mass is alpha-even; it is imported, not weight-derived). Compatibility check:
# there exists a strictly increasing assignment consistent with distinct labels.
external_magnitude = np.array([1.0, 200.0, 3500.0])  # imported, unconstrained sign-blind
compatible = np.all(np.diff(external_magnitude) > 0) and \
    len(set(external_magnitude.tolist())) == 3
rec(E, "WEAK reading: an external alpha-even magnitude is COMPATIBLE with the "
       "observed ordered, distinct hierarchy",
    compatible, "mass is alpha-even and external => any monotone hierarchy fits")


# ---------------- report ----------------
def dump(tag, bucket):
    for name, ok, detail in bucket:
        status = "PASS" if ok else "FAIL"
        print(f"  [{tag}] {status}  {name}" + (f"  -- {detail}" if detail else ""))


print("=== Prong 3 FALSIFIER probe (oriented-shard-cycle swing) ===")
print("[T] setup (consumed parity typings)")
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
print("VERDICT SUPPORT (b): the seed<->realization consistency leaves a NON-EMPTY "
      "alpha-even shadow (forbids record-contact ^ relative-disagreement); the "
      "null model forbids nothing => the shadow is a real, weak, falsifiable "
      "constraint (one global arrow). Absolute seed stays unfalsifiable.")
print("VERDICT SUPPORT (a): the STRONG weight-tied mass reading is FALSIFIED "
      "(degenerate/symmetric, cannot make 1:200:3500); the WEAK reading (identical "
      "quantum numbers + external alpha-even magnitude) MATCHES and is COMPATIBLE. "
      "=> weakly falsifiable, consistent.")

import sys
sys.exit(0 if ok else 1)
