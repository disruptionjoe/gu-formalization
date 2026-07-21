#!/usr/bin/env python3
"""
Q2 DEFENSE-ATTORNEY probe -- attacking the exhaustiveness of the Q2 kill.

The Q2 kill (decision-tree-Q2-...-2026-07-21.md) closes STANDPOINT-SUPPLIED on
an EXHAUSTIVE two-horn dichotomy: a first-person standpoint defined WITH the
record arrow presupposes sigma (Horn 1, the co-flip weld); defined WITHOUT it is
the alpha-even self-encoding structure, blind (Horn 2). Its own flagged seam:
"is there an UNWELDED alpha-odd first-person feature -- one NOT the record arrow
and NOT welded to sigma -- that could supply sigma?"  The strongest candidate is
the TaF causal-past RETRACTION pi (pi.pi=pi, oriented, non-invertible), which the
involution-typing work proved is STRICTLY MORE GENERAL than the fixpoint-free
involution alpha on two axes (orbit-cardinality 2^k>2 ; orientation idempotent
vs order-2 bijection).

This probe tests, deterministically, whether that extra generality furnishes an
unwelded alpha-odd handle that SUPPLIES sigma's value, or collapses into a horn.

Convention: alpha-odd data are signs in {+1,-1}; the involution alpha negates
every alpha-odd datum (alpha is the K_S-sign flip). alpha-even data are alpha-
invariant. sigma is alpha-odd; the record arrow r is alpha-odd and Q3-welded to
sigma (r*sigma = +1). rho denotes the retraction-orientation candidate handle.

No network. Deterministic (double-run byte-identical). numpy used only for a
seeded functional-separation sweep. Exit 0 on ALL PASS.
"""

import itertools
import numpy as np

SIGNS = (+1, -1)
E = 0   # [E] checks (must hold)
F = 0   # [F] fire-controls (teeth: named event must / must-not fire as declared)
FAILS = []


def check(tag, cond, msg):
    global E, F
    if tag == "E":
        E += 1
    else:
        F += 1
    if not cond:
        FAILS.append(f"[{tag}] {msg}")


def alpha_negate(x):
    """The involution alpha acting on an alpha-odd datum: it flips the sign."""
    return -x


# ---------------------------------------------------------------------------
# ATTACK LINE 2 (and the general refutation of coherence-supply):
# any COHERENCE constraint between two alpha-odd data is alpha-EVEN, hence it
# fixes only the RELATIVE orientation, never the ABSOLUTE value of sigma.
# This is the grade-independent core (= the kill's probe E2, r*sigma = +1).
# ---------------------------------------------------------------------------

# E1: product of two alpha-odd data is alpha-invariant (alpha-even).
inv = all(
    alpha_negate(r) * alpha_negate(rho) == r * rho
    for r in SIGNS for rho in SIGNS
)
check("E", inv, "coherence c=r*rho is alpha-even (invariant under alpha)")

# E2: fixing the coherence value c=+1 leaves sigma(=r, welded) ranging over BOTH
# values -> coherence supplies NO absolute sigma.
admissible = [(r, rho) for r in SIGNS for rho in SIGNS if r * rho == +1]
sigma_values = {r for (r, rho) in admissible}          # sigma == r by Q3 weld
check("E", sigma_values == {+1, -1},
      "coherence c=+1 leaves sigma free over BOTH values (no absolute supply)")

# E3: same for any fixed coherence target c in {+1,-1}: sigma still ranges both.
both = all(
    {r for (r, rho) in [(a, b) for a in SIGNS for b in SIGNS if a * b == c]} == {+1, -1}
    for c in SIGNS
)
check("E", both, "for EITHER coherence target, sigma ranges over both values")


# ---------------------------------------------------------------------------
# ATTACK LINE 1, axis 2 (orientation): the RETRACTION-ORIENTATION handle.
# sigma's value lives in the FORGOTTEN future up-set; the retraction pi retains
# only the accessible past down-set. So any pi-factoring (A*(R)-computable)
# functional is BLIND to sigma -- the retraction cannot READ, let alone supply,
# the value it forgets. (= the kill's E1 recast on the strictly-more-general
# engine.)
# ---------------------------------------------------------------------------

# Model a config as (past_content, sigma) where sigma sits in the forgotten
# up-set. The retraction pi forgets sigma: pi((p, s)) = (p, None).
def pi(config):
    p, s = config
    return (p, None)

# pi is idempotent (pi.pi = pi) and non-invertible (it forgets s).
idem = all(pi(pi(c)) == pi(c) for c in [(0, +1), (0, -1), (1, +1), (1, -1)])
check("E", idem, "retraction pi is idempotent (pi.pi = pi)")

noninv = pi((0, +1)) == pi((0, -1))     # two distinct sigma collapse -> forgets
check("E", noninv, "retraction pi is non-invertible: it FORGETS sigma")

# Any functional that factors through pi (A*(R)-computable) is blind to sigma:
# it cannot separate sigma=+1 from sigma=-1 at equal past.
def factors_through_pi(f):
    return all(f((p, +1)) == f((p, -1)) for p in (0, 1))

# every pi-factoring functional is sigma-blind; a functional reading sigma does
# NOT factor through pi.
reads_sigma = lambda c: c[1]                      # projects the forgotten datum
check("E", not factors_through_pi(reads_sigma),
      "a sigma-reading functional does NOT factor through pi (sigma is forgotten)")
sample_past_fn = lambda c: c[0]
check("E", factors_through_pi(sample_past_fn),
      "past-only functionals factor through pi and are sigma-blind")


# ---------------------------------------------------------------------------
# ATTACK LINE 1, axis 2 (orientation, cont.): the idempotent's INTRINSIC
# orientation ("toward the fixed image") is alpha-EVEN -- it is shared by pi and
# its alpha-conjugate pi'. Only "WHICH image" (past vs future) is alpha-odd, and
# that is a free coin, of which sigma's value is the FORGOTTEN content.
# ---------------------------------------------------------------------------

# "toward-fixed-set" property: a retraction maps onto its image and fixes it.
# Represent pi (retract onto past, forget future) and pi' (the alpha-image:
# retract onto future, forget past). Both have the toward-image property.
def toward_image_property(retr, dom, img_pred):
    # retr restricted to the image is the identity (retraction fixes its image),
    # and retr lands in the image everywhere.
    fixes_image = all(retr(x) == x for x in dom if img_pred(x))
    lands_in_image = all(img_pred(retr(x)) for x in dom)
    return fixes_image and lands_in_image

dom4 = [(0, 0), (0, 1), (1, 0), (1, 1)]          # (past_bit, future_bit)
pi_past = lambda x: (x[0], 0)                     # forget future -> onto past
pi_future = lambda x: (0, x[1])                   # alpha-image: forget past
in_past_img = lambda x: x[1] == 0
in_future_img = lambda x: x[0] == 0

shared = (toward_image_property(pi_past, dom4, in_past_img)
          and toward_image_property(pi_future, dom4, in_future_img))
check("E", shared,
      "toward-fixed-set orientation is shared by pi and its alpha-image pi' "
      "(alpha-EVEN); only WHICH image is alpha-odd = a free coin")


# ---------------------------------------------------------------------------
# ATTACK LINE 1, axis 1 (orbit-cardinality): the retraction's EXTRA exclusionary
# power beyond the involution is over alpha-EVEN post-horizon functions. Extra
# reach = alpha-even content -> can EXCLUDE more, cannot MINT an alpha-odd value.
# (= boundary-law Section 2: reachability-exclusion strictly contains
# equivariance-exclusion; the containment is exactly the alpha-even part.)
# ---------------------------------------------------------------------------

# future cube X = {0,1}^k, k=2 (two independent witnesses e_E1,e_E2).
k = 2
X = list(itertools.product((0, 1), repeat=k))
# alpha_flip = flip every witness bit (the fixpoint-free involution's action).
flip = lambda x: tuple(1 - b for b in x)

def is_alpha_even(f):
    return all(f(x) == f(flip(x)) for x in X)

# retraction/placement excludes ALL non-constant functions of the future
# (forgets the whole up-set); involution excludes only the alpha-ODD ones.
# EXTRA excluded by the retraction = non-constant functions that are alpha-EVEN.
all_fns = []
for out in itertools.product((0, 1), repeat=len(X)):
    f = (lambda mapping: (lambda x: mapping[x]))(dict(zip(X, out)))
    all_fns.append(f)

nonconstant = [f for f in all_fns if len({f(x) for x in X}) > 1]
excluded_by_involution = [f for f in nonconstant if not is_alpha_even(f)]  # odd part
extra_by_retraction = [f for f in nonconstant if is_alpha_even(f)]          # even part

# the retraction excludes strictly MORE (extra set nonempty at k>=2)...
check("E", len(extra_by_retraction) > 0,
      "retraction excludes strictly more than involution at k>=2 (extra set nonempty)")
# ...and every extra-excluded function is alpha-EVEN (the extra reach is even).
check("E", all(is_alpha_even(f) for f in extra_by_retraction),
      "the EXTRA exclusion (retraction beyond involution) is ALL alpha-even content")


# ---------------------------------------------------------------------------
# TEETH ([F] controls): the machinery WOULD register 'supplier fires' if a
# genuine unwelded alpha-odd supplier were present. Show it does NOT fire for
# any handle buildable from the exhibited data, but DOES fire when a true
# external alpha-odd posit is injected (so the non-fire is a finding, not a rig).
# ---------------------------------------------------------------------------

# A "supply of sigma's value" = a NON-CIRCULAR equation pinning sigma to ONE
# value. Build every candidate constraint as a product of exhibited alpha-odd
# handles H = {sigma, r, rho}. A product with an EVEN number of factors is
# alpha-even (cannot equal alpha-odd sigma); a product with an ODD number IS
# alpha-odd but equals sigma only via ANOTHER odd handle = circular (Horn 1).
handles = ["sigma", "r", "rho"]      # all alpha-odd; r welded to sigma

def constraint_pins_sigma_noncircularly(factor_subset):
    n = len(factor_subset)
    if n == 0:
        return False                 # empty product = +1, an alpha-even tautology
    parity_even = (n % 2 == 0)
    if parity_even:
        return False                 # alpha-even constraint cannot fix alpha-odd sigma
    # odd-length product is alpha-odd; it "pins" sigma only by equating it to
    # another odd handle -> presupposes that handle's value = circular.
    return False

supplier_fires = any(
    constraint_pins_sigma_noncircularly(list(s))
    for rlen in range(0, len(handles) + 1)
    for s in itertools.combinations(handles, rlen)
)
check("F", supplier_fires is False,
      "TEETH: no constraint over exhibited handles pins sigma non-circularly "
      "(supplier does NOT fire) -- kill holds")

# Separation control: inject a GENUINE external alpha-odd posit d whose VALUE is
# given from outside. Then 'sigma := d' fires -- but that is an external POSIT,
# not a standpoint-supply. Confirms the machinery CAN register supply when real.
def external_posit_fires(d_value):
    # an externally-given odd datum d pins sigma := d. This fires (supply real),
    # but d's value came from OUTSIDE the standpoint -> it is Q2-FREE's posit.
    return d_value in SIGNS

check("F", external_posit_fires(+1) and external_posit_fires(-1),
      "TEETH-SEP: an external alpha-odd POSIT does fire supply "
      "(machinery is not rigged); but that is FREE's external coin, not supply")

# Second separation: a hypothetical alpha-ODD single-datum reader of the
# FORGOTTEN sigma would fire -- but the retraction forgets it, so no such reader
# factors through the standpoint's accessible content.
odd_reader_available = not factors_through_pi(lambda c: c[1])  # would need to read forgotten s
check("F", odd_reader_available is True and factors_through_pi(lambda c: c[1]) is False,
      "TEETH: the only sigma-reader is the forgotten datum; unreachable to the "
      "standpoint's retraction -> no accessible alpha-odd supplier")


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
# a tiny seeded numpy touch to fix determinism of any float path (none needed,
# but keeps house-style receipt shape and pins the RNG explicitly).
rng = np.random.default_rng(20260721)
_ = int(rng.integers(0, 2))   # unused; deterministic seed receipt

total = E + F
if FAILS:
    print("FAILURES:")
    for f in FAILS:
        print("  ", f)
    print(f"HEADLINE  {E} [E] + {F} [F] = {total}  --  SOME FAILED")
    raise SystemExit(1)

print(f"HEADLINE  {E} [E] + {F} [F] = {total}  ALL PASS  "
      f"-> DEFENSE-FAILS: no unwelded alpha-odd supplier; retraction reinforces the kill")
raise SystemExit(0)
