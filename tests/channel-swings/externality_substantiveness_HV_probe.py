#!/usr/bin/env python3
"""
HOSTILE-VERIFY probe for the Prong III externality capstone.

Claim under test: "the observer forces sigma's externality but cannot SUPPLY
its value" is a genuine THEOREM = `no_invariant_valuation` for the fixpoint-free
K_S flip.

This probe isolates EXACTLY what `no_invariant_valuation` proves and what it does
NOT, by separating the TWO group actions that the prose conflates:

  * CODOMAIN action  -- InvariantValuation (Lean): alpha acts on the LABEL object
    B = {+K_S,-K_S}. `no_invariant_valuation` = "no map v:A->B has alpha-FIXED
    output". Trivial given fixpoint-freeness; GU-free.

  * DOMAIN action    -- alpha-EVEN reader (Schur / prong I): alpha acts on STATES
    A. "internal reader is alpha-even" => identical channel rows => cannot resolve
    the alpha-odd sigma. This is the SUBSTANTIVE physics content -- and it is a
    DIFFERENT statement, NOT what `no_invariant_valuation` proves.

The probe shows a genuine physical sigma-READER exists that the codomain theorem
does NOT forbid (it is alpha-equivariant, not alpha-invariant), and that the
reader is blocked ONLY by the separate alpha-even ("internal") premise = the
named BRIDGE LEMMA. Fully deterministic (exhaustive enumeration, no RNG, no
network). Foreground. Exit 0 on all-pass.
"""

# ----- objects ---------------------------------------------------------------
# Label object B = {+1,-1} standing for {+K_S,-K_S}. flip = the K_S-sign flip.
B = (+1, -1)
def flip(b):            # alpha on the CODOMAIN (fixpoint-free involution on B)
    return -b

# Domain A = one alpha-orbit of states {p_plus, p_minus}. The state-level action
# swaps them (this is the physical K_S flip acting on states).
A = ("p_plus", "p_minus")
def act(a):             # alpha on the DOMAIN (swaps the two orbit points)
    return "p_minus" if a == "p_plus" else "p_plus"

# The TRUE orientation reader sigma: reads which orbit point is actual.
sigma = {"p_plus": +1, "p_minus": -1}

def all_maps():
    """All 4 maps v:A->B."""
    out = []
    for vp in B:
        for vm in B:
            out.append({"p_plus": vp, "p_minus": vm})
    return out

def is_invariant_valuation(v):           # Lean InvariantValuation (CODOMAIN)
    return all(flip(v[a]) == v[a] for a in A)

def is_alpha_even_reader(v):             # DOMAIN-even (internal, per the bridge)
    return all(v[act(a)] == v[a] for a in A)

def is_equivariant(v):                   # intertwines the two actions (a READER)
    return all(v[act(a)] == flip(v[a]) for a in A)

def reads_sigma(v):                      # distinguishes the two sigma values
    return v["p_plus"] != v["p_minus"]

results = []
def check(tag, name, cond):
    results.append((tag, name, bool(cond)))

# ----- E1: no_invariant_valuation is TRUE (codomain) -- and it is trivial ------
inv = [v for v in all_maps() if is_invariant_valuation(v)]
check("E", "no_invariant_valuation: ZERO alpha-invariant valuations exist",
      len(inv) == 0)

# ----- E2: the theorem MISSES the physical reader ----------------------------
# sigma itself is a perfect reader, is alpha-EQUIVARIANT, and is NOT an invariant
# valuation. So "no invariant valuation" does NOT imply "no reader".
check("E", "sigma READS the bit (distinguishes +K_S from -K_S)",
      reads_sigma(sigma))
check("E", "sigma is alpha-EQUIVARIANT (a genuine reader), NOT invariant-valuation",
      is_equivariant(sigma) and not is_invariant_valuation(sigma))
readers_missed = [v for v in all_maps()
                  if reads_sigma(v) and not is_invariant_valuation(v)]
check("E", "codomain theorem is SILENT about equivariant readers (>=1 missed)",
      len(readers_missed) >= 1)

# ----- E3: what ACTUALLY blocks the reader is the alpha-EVEN (domain) premise --
# The bridge premise: internal reader = alpha-even. Enumerate alpha-even maps and
# count how many read sigma. Answer 0 (identical rows / Schur) -- a DIFFERENT
# computation from no_invariant_valuation.
even_maps = [v for v in all_maps() if is_alpha_even_reader(v)]
even_readers = [v for v in even_maps if reads_sigma(v)]
check("E", "under the alpha-EVEN bridge: ZERO internal readers of sigma (Schur)",
      len(even_readers) == 0 and len(even_maps) == 2)

# ----- F1 (teeth): dissolve the BRIDGE -> a reader REAPPEARS ------------------
# Drop the alpha-even restriction (allow general/external maps): sigma reads it.
# Proves the block in E3 is contingent on the bridge premise, NOT on
# no_invariant_valuation. So the SUBSTANCE lives in the bridge, not the Lean line.
general_readers = [v for v in all_maps() if reads_sigma(v)]
check("F", "dissolve alpha-even bridge => reader reappears (block is bridge-borne)",
      len(general_readers) >= 1 and sigma in general_readers)

# ----- F2 (teeth): dissolve FIXPOINT-FREENESS -> invariant valuations reappear -
# With alpha = identity on B, every map is an invariant valuation (4 of them).
# Confirms no_invariant_valuation's ENTIRE content is fixpoint-freeness -- GU-free,
# would hold for ANY fixpoint-free Z/2 (a coin flip), matching prong III's control.
def is_invariant_valuation_idflip(v):
    return all(v[a] == v[a] for a in A)   # alpha=id => trivially all
inv_id = [v for v in all_maps() if is_invariant_valuation_idflip(v)]
check("F", "dissolve fixpoint-freeness (alpha=id) => 4 invariant valuations reappear",
      len(inv_id) == 4)

# ----- report ----------------------------------------------------------------
E = [r for r in results if r[0] == "E"]
F = [r for r in results if r[0] == "F"]
Epass = all(r[2] for r in E)
Ffire = all(r[2] for r in F)
for tag, name, ok in results:
    print(f"  [{tag}] {'PASS' if ok else 'FAIL'}  {name}")
allok = Epass and Ffire
print()
print(f"HEADLINE: {len(E)} [E] + {len(F)} [F] = {len(results)} :: "
      f"no_invariant_valuation is CODOMAIN-trivial; physical reader-blindness "
      f"needs the alpha-EVEN bridge (a DIFFERENT statement) :: "
      f"{'ALL PASS -> BRIDGE-GAP CONFIRMED' if allok else 'ANOMALY'}")
import sys
sys.exit(0 if allok else 1)
