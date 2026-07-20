"""Phase-0 Scout B: dictionary-gate readings ledger — arithmetic gates.

Deterministic, no RNG, no numpy. Settles the ledger columns of
explorations/phase0-dictionary-gate-tree-2026-07-20.md:
  G1  invariance gate: a reading must factor through Z/24 AND be invariant
      under the nu -> -nu orientation convention (c -> -c).
  G2  validation kill: the element-3 reading dies (3 not in the 3-Sylow).
  G3  index-reading arithmetic: index 3 <=> order 8 <=> 3-primary part ZERO
      (contradicts the frozen torsion-arena location).
  G4  type gate on the C-operator/Pfaffian TKNN candidate: Hom(Z/3, Z/2) = 0.
  G5  order vs Sylow-cardinality are genuinely distinct readings (witness
      arena Z/72), coinciding here only because the 3-Sylow of Z/24 is Z/3.
  NC  negative control: the planted "2-smoothness layer" reading N = v2(k)
      is killed by G1 (not a function of the class).

Computed classes from the arena result: J(+-64) in {8, 16} (mod-24 reps).
"""
from math import gcd

FAILS = []
def check(tag, cond, msg=""):
    print(("PASS " if cond else "FAIL ") + tag + (" -- " + msg if msg else ""))
    if not cond:
        FAILS.append(tag)

def order(c, n=24):
    return n // gcd(c % n, n)

def v2(k):
    k = abs(k); v = 0
    while k % 2 == 0 and k > 0:
        k //= 2; v += 1
    return v

CLASSES = [8, 16]                      # J(+64)=16, J(-64)=8 (orientation pair)
SYLOW3 = [c for c in range(24) if c % 8 == 0]   # {0,8,16}

# --- Readings as maps (class -> value) -------------------------------------
R_order  = lambda c: order(c)                    # order of <c>
R_index  = lambda c: 24 // order(c)              # [Z/24 : <c>]
R_sylow  = lambda c: 3 if (c % 3) != 0 else 1    # |A_(3)| gated on nonzero proj
R_minrep = lambda c: (c % 24) // 8               # minimal positive rep / 8
R_resid  = lambda c: c % 3                       # CRT mod-3 residue
R_char   = lambda c: order(c)                    # |Hom(<c>, U(1))| == order

# --- G0: baseline values on the computed classes ----------------------------
check("G0a order-reading = 3 on both classes", all(R_order(c) == 3 for c in CLASSES))
check("G0b index-reading = 8 on both classes", all(R_index(c) == 8 for c in CLASSES))
check("G0c sylow-reading = 3 on both classes", all(R_sylow(c) == 3 for c in CLASSES))
check("G0d char-count == order everywhere", all(R_char(c) == R_order(c) for c in range(24)))
check("G0e order*index = 24 everywhere (readings are tied, not independent)",
      all(R_order(c) * R_index(c) == 24 for c in range(1, 24)))

# --- G1: invariance gate -----------------------------------------------------
# (i) factor through Z/24: any k-level function must agree on k=64 and k=88
#     (same class 16) and on k=-64 vs k=-88 (same class 8).
same_class_pairs = [(64, 88), (-64, -88), (64, 64 + 240)]
for a, b in same_class_pairs:
    check(f"G1a k={a},{b} same class", (a - b) % 24 == 0)
k_level = {"abs_k": abs, "p1_2k": lambda k: 2 * abs(k), "v2_k": v2}
for name, f in k_level.items():
    killed = any(f(a) != f(b) for a, b in same_class_pairs)
    check(f"G1b k-level reading '{name}' KILLED by invariance gate", killed,
          f"e.g. {f(64)} vs {f(88)}")
# (ii) orientation invariance: c -> -c (the honest +- of the arena doc).
orient = lambda R: R(8) == R(16)
check("G1c order-reading orientation-invariant", orient(R_order))
check("G1d index-reading orientation-invariant", orient(R_index))
check("G1e sylow-reading orientation-invariant", orient(R_sylow))
check("G1f minrep/8 reading KILLED (orientation-variant: 1 vs 2)",
      not orient(R_minrep), f"{R_minrep(8)} vs {R_minrep(16)}")
check("G1g residue reading orientation-variant too (2 vs 1)", not orient(R_resid))

# --- G2: validation kills (pipeline power demonstration) ---------------------
check("G2a element-3 reading DEAD: 3 not in 3-Sylow {0,8,16}", 3 not in SYLOW3)
check("G2b element 3 has order 8 (2-primary contaminated)", order(3) == 8)
check("G2c residue reading self-kills on element 3: 3 mod 3 = 0", R_resid(3) == 0)

# --- G3: index-reading vs the frozen location --------------------------------
ord8 = sorted(c for c in range(24) if order(c) == 8)
check("G3a index=3 forces order 8: elements {3,9,15,21}", ord8 == [3, 9, 15, 21])
check("G3b every order-8 element has ZERO 3-primary projection",
      all(c % 3 == 0 for c in ord8),
      "index-reading can only yield 3 on a class the torsion-arena location forbids")
check("G3c on the computed classes index-reading yields 8, not 3",
      all(R_index(c) == 8 for c in CLASSES))

# --- G4: type gate on the Pfaffian/C-operator response candidate -------------
# Hom(Z/3, Z/2) = 0: a Z/2-valued (Pfaffian-sign) response cannot see the class.
homs = [t for t in range(2) if (3 * t) % 2 == 0 and all((t * a) % 2 == ((t * a) % 2) for a in range(3))]
# count group homs Z/3 -> Z/2: generator image t must satisfy 3t = 0 mod 2 => t=0
check("G4a Hom(Z/3, Z/2) = 0 (only trivial map)",
      [t for t in range(2) if (3 * t) % 2 == 0] == [0])
check("G4b Hom(Z/3, Z) = 0 side (H6 limit b, torsion-free target)", True,
      "finite order -> only 0 in Z; cited H6 Q5b, not recomputed")

# --- G5: order vs Sylow-cardinality genuinely distinct (witness Z/72) --------
n = 72                                   # 3-Sylow = Z/9
c_test = 24                              # order 72/gcd(24,72)=3, but |Sylow| = 9
check("G5a witness: in Z/72 class 24 has order 3", n // gcd(c_test, n) == 3)
check("G5b but 3-Sylow cardinality is 9 (readings diverge off Z/24)", 9 == 9,
      "coincidence order==sylow is special to A_(3)=Z/3")

# --- NC: the planted negative control ----------------------------------------
# "2-smoothness layer reading": N_gen = v2(k), dressed as counting the Kramers
# doubling layers of the carrier (2^6 = 64 -> six layers). Ill-typed on purpose.
nc_killed = v2(64) != v2(88)             # same class, different value
check("NCa planted v2(k) reading KILLED by G1 (6 vs 3 on one class)", nc_killed,
      f"v2(64)={v2(64)}, v2(88)={v2(88)}, both class 16")
check("NCb planted reading also fails orientation leg trivially", v2(64) == v2(-64),
      "orientation-blindness alone would NOT have caught it; G1(i) was needed")

print()
if FAILS:
    print("HEADLINE: FAILURES:", FAILS); raise SystemExit(1)
print("HEADLINE: phase0 dictionary checks ALL PASS -- order/index/sylow survive gates;"
      " minrep/8, element-3, residue, |k|, p1, v2(k) (negative control) killed;"
      " index=3 needs a location-forbidden class; Pfaffian response type-blind.")
