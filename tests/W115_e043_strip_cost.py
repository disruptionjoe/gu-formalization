#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
W115: TI's E043 SAX-vs-entropy discriminator, run ON GU's strip-cost functional.

CROSS-REPO STRESS TEST (one-way rule: this stress-tests TI's mu-bridge hypothesis;
it never supports it). READ side: temporal-issuance E043 (TI-C021 Subadditivity
Axiom SAX + the Disjoint-Independent Discriminator), E045 (D-FORK), E140
(cost-of-finality route). COMPUTE side: the GU W98/W109 interacting Krein mode
tower and its strip-cost functional (per-mode norm of the -i/2 Connes-cocycle
continuation = sqrt(cond(eta(r_k))), W105/W106/W109; Petermann dictionary W113).

TI's SAX as recorded in E043 Section 6 (quoted):
  (SAX-0) mu(empty) = 0
  (SAX-1) monotone: A subset B => mu(A) <= mu(B)
  (SAX-2) strict size-subadditivity: disjoint A,B with |A|,|B|>0 =>
          mu(A u B) < mu(A) + mu(B)
  (SAX-3) size-determined: mu(A) = g(|A|), g strictly concave, g(0)=0
          (canonical g(s) = c s^alpha, 0<alpha<1)
Entropy side (P_corr, E043 Section 2): H(A,B) <= H(A)+H(B), equality iff A,B
independent; deficit = I(A;B). E043's direction-1 discriminator: on disjoint
INDEPENDENT A,B the entropy deficit is exactly 0 while a genuine mu_alpha
deficit is strictly > 0.

TYPINGS OF THE STRIP COST TESTED (domain = subsets S of the mode tower):
  T-A  per-state strip form:  mu_f(S) = sum_{k in S} |f(k)|^2 * cost_strip(k),
       cost_strip(k) = (1-r_k)^{-1/2} = per-mode norm of the -i/2 cocycle leg
       (the KMS/crossing bottleneck, W106 nesting table). The honest
       "cost of finalizing a selection over the mode-subset S".
  T-B  Araki/entropy leg:     L_f(S) = sum_{k in S} |f(k)|^2 * log cond(eta(r_k)).
  T-C  uniformity/sup typing: N(S) = sup_{k in S} cost_strip(k)  (the norm of
       Delta^{-1/2} restricted to S -- the W98 break object itself).
  T-D  trajectory typing (steelman for the adversary "you chose the domain"):
       initial segments S_K = {k <= K}, size = K, g(K) = N(S_K).

Exit 0 iff all checks pass. numpy optional (pure-python fallback); deterministic.
"""
import math
import sys

FAILS = []


def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {name}" + (f" -- {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)


# ---------------------------------------------------------------- W98 mode data
M1 = 0.0        # healthy mass (W109 instance)
M2 = 0.30       # ghost-partner gap (W109 instance)
G0 = 0.10       # marginal interaction strength (W98/W109)


def omega(k, m):
    return math.sqrt(k * k + m * m)


def dsplit(k, m1=M1, m2=M2):
    # Dw(k) = |m1^2 - m2^2| / (w1 + w2) -> 0 as k -> inf (W98)
    return abs(omega(k, m1) - omega(k, m2))


def r_of(k, g=G0, p=0, m1=M1, m2=M2):
    # exceptional-point parameter with vertex growth g_k = g * k^p
    gk = g * (k ** p)
    return gk / (gk + 0.5 * dsplit(k, m1, m2))


def cond_eta(r):
    return (1.0 + r) / (1.0 - r)


def cost_strip(k, g=G0, p=0):
    # per-mode norm of the -i/2 cocycle continuation = sqrt(cond(eta(r_k)))
    # (W109 adversary-(b) computation; = (1-r)^{-1/2} up to bounded factor)
    return math.sqrt(cond_eta(r_of(k, g, p)))


# mode tower (integer momenta; deterministic)
KMAX = 4096
MODES = list(range(1, KMAX + 1))


# ------------------------------------------------------------------- states
def schwartz(k):
    # Schwartz-class packet, inside the sharp class D(|k|^{(p+1)/4}) for all p
    return math.exp(-((math.log(1.0 + k)) ** 2))


def powerlaw(k, alpha=1.0):
    # power tail alpha=1.0 > alpha*(0)=3/4: inside the p=0 sharp class
    return k ** (-alpha)


# ------------------------------------------------------- typed functionals
def mu_A(S, f, g=G0, p=0):
    return sum((f(k) ** 2) * cost_strip(k, g, p) for k in S)


def mu_B(S, f, g=G0, p=0):
    return sum((f(k) ** 2) * math.log(cond_eta(r_of(k, g, p))) for k in S)


def mu_C(S, g=G0, p=0):
    return max(cost_strip(k, g, p) for k in S) if S else 0.0


def mu_synth(S, alpha=0.5, c=1.0):
    # E043's canonical mu_alpha: size-determined g(s) = c s^alpha (control)
    return c * (len(S) ** alpha)


# ------------------------------------------------------- deterministic PRNG
def lcg(seed):
    s = seed
    while True:
        s = (1103515245 * s + 12345) % (2 ** 31)
        yield s


def random_disjoint_pair(rng, n_a=40, n_b=40):
    pool = list(MODES)
    pick = set()
    while len(pick) < n_a + n_b:
        pick.add(pool[next(rng) % len(pool)])
    pick = sorted(pick)
    return pick[:n_a], pick[n_a:n_a + n_b]


# =========================================================== T1: exponent leg
print("== T1: per-mode strip cost exponent (p+1)/2 (analytic leg check) ==")
for p, want in [(0, 0.5), (1, 1.0), (2, 1.5)]:
    r = cost_strip(2048, p=p) / cost_strip(1024, p=p)
    meas = math.log(r, 2)
    check(f"T1 p={p}: measured exponent {meas:.3f} ~ {(p + 1) / 2}",
          abs(meas - want) < 0.05)

# ================================================= T2: T-A/T-B exact additivity
print("== T2: per-state strip form is EXACTLY ADDITIVE on disjoint mode-sets ==")
rng = lcg(20260713)
worst = 0.0
for trial in range(50):
    A, B = random_disjoint_pair(rng)
    for f in (schwartz, powerlaw):
        for fn in (mu_A, mu_B):
            a, b, ab = fn(A, f), fn(B, f), fn(sorted(A + B), f)
            rel = abs(ab - (a + b)) / max(ab, 1e-300)
            worst = max(worst, rel)
check("T2 SAX-2 on T-A/T-B: deficit == 0 (additive, NOT strictly subadditive)",
      worst < 1e-12, f"worst relative deficit {worst:.2e}")

# ============================================= T3: SAX-3 (size-determinedness)
print("== T3: SAX-3 -- is the strip cost a function of |S| alone? ==")
IR = list(range(1, 41))          # 40 IR modes
UV = list(range(KMAX - 39, KMAX + 1))  # 40 UV modes (same cardinality)
vals_A = (mu_A(IR, schwartz), mu_A(UV, schwartz))
vals_C = (mu_C(IR), mu_C(UV))
check("T3 T-A: equal-size subsets give UNEQUAL values (mode-identity-dependent)",
      abs(vals_A[0] - vals_A[1]) / vals_A[0] > 0.5,
      f"IR {vals_A[0]:.4g} vs UV {vals_A[1]:.4g}")
check("T3 T-C: equal-size subsets give UNEQUAL values (mode-identity-dependent)",
      abs(vals_C[0] - vals_C[1]) / vals_C[1] > 0.5,
      f"IR {vals_C[0]:.4g} vs UV {vals_C[1]:.4g}")
check("T3 control: synthetic mu_alpha IS size-determined",
      mu_synth(IR) == mu_synth(UV))

# ============================== T4: T-C sup typing -- subadditive, wrong reason
print("== T4: sup typing -- strictly subadditive but dominance-driven, not size-driven ==")
rng = lcg(777)
strict = True
dominance_exact = True
size_form_fits = True
for trial in range(50):
    A, B = random_disjoint_pair(rng, 30, 50)
    nA, nB, nAB = mu_C(A), mu_C(B), mu_C(sorted(A + B))
    strict &= (nAB < nA + nB)
    # deficit = min(nA, nB) exactly (max identity), NOT a concavity gap in sizes
    dominance_exact &= abs((nA + nB - nAB) - min(nA, nB)) < 1e-12
    # size-driven prediction (E043 P_size, alpha=1/2 canonical): deficit depends
    # on |A|,|B| only; but here two pairs of the SAME sizes give different deficits
if strict and dominance_exact:
    d1 = mu_C(list(range(1, 31))) + mu_C(list(range(31, 81))) - mu_C(list(range(1, 81)))
    d2 = mu_C(list(range(1000, 1030))) + mu_C(list(range(2000, 2050))) - mu_C(list(range(1000, 1030)) + list(range(2000, 2050)))
    size_form_fits = abs(d1 - d2) / max(d1, d2) < 0.01  # would hold if size-determined
check("T4 T-C is strictly subadditive (max(a,b) < a+b)", strict)
check("T4 T-C deficit == min(N(A),N(B)) exactly (DOMINANCE, not concavity-in-size)",
      dominance_exact)
check("T4 T-C deficit NOT a function of (|A|,|B|): same sizes, different deficits",
      not size_form_fits, f"deficits {d1:.4g} vs {d2:.4g} at identical sizes")

# =============================== T5: E043 direction-1 discriminator, replayed
print("== T5: E043's Disjoint-Independent Discriminator with strip cost in the lineup ==")
# The W98 tower modes are statistically independent (per-mode block-diagonal
# metric; product state). Per-mode occupation from the p=0 pair tail c_k ~ G/2k
# defines independent per-mode Bernoulli-like laws; joint entropy over disjoint
# subsets is exactly the sum (I(A;B)=0).
def mode_entropy(k):
    q = min(0.499, (G0 / (2.0 * k)) ** 2)  # excitation prob from pair tail
    if q <= 0.0:
        return 0.0
    return -(q * math.log(q) + (1 - q) * math.log(1 - q))


A = sorted(set(list(range(5, 45)))); B = sorted(set(list(range(100, 140))))
H_A = sum(mode_entropy(k) for k in A)
H_B = sum(mode_entropy(k) for k in B)
H_AB = sum(mode_entropy(k) for k in sorted(A + B))  # independence => additive
ent_deficit = H_A + H_B - H_AB
strip_deficit = mu_A(A, schwartz) + mu_A(B, schwartz) - mu_A(sorted(A + B), schwartz)
mu_deficit = mu_synth(A) + mu_synth(B) - mu_synth(sorted(A + B))
check("T5 entropy deficit on independent disjoint A,B == 0 (E043 Sec 3)",
      abs(ent_deficit) < 1e-12)
check("T5 STRIP-COST deficit on the same A,B == 0 (sides with the additive/entropy column)",
      abs(strip_deficit) / mu_A(sorted(A + B), schwartz) < 1e-12)
check("T5 genuine mu_alpha deficit on the same A,B > 0 (the mu signature the strip cost LACKS)",
      mu_deficit > 0.1, f"mu_alpha deficit {mu_deficit:.4f}")

# ========================= T6: trajectory typing (steelman) + marginal signature
print("== T6: T-D trajectory typing g(K)=N(S_K): SAX-shaped only at p=0 ==")
for p, expect in [(0, "concave"), (1, "additive"), (2, "superadditive")]:
    g1 = mu_C(list(range(1, 513)), p=p)
    g2 = mu_C(list(range(1, 1025)), p=p)
    g4 = mu_C(list(range(1, 2049)), p=p)
    e = math.log(g4 / g2, 2)  # local exponent
    shape = "concave" if e < 0.95 else ("additive" if e < 1.05 else "superadditive")
    check(f"T6 p={p}: trajectory exponent {e:.3f} -> {shape} (expected {expect})",
          shape == expect)
# marginal cost per doubling: increasing at p>=1 -- ANTI-SAX marginal signature
inc0 = (mu_C(list(range(1, 1025))) - mu_C(list(range(1, 513))))
inc1 = (mu_C(list(range(1, 2049))) - mu_C(list(range(1, 1025))))
check("T6 p=0: marginal sup-cost per octave still INCREASES in absolute terms "
      "(concave exponent 1/2 in K, but c*sqrt(K) increments grow)",
      inc1 > inc0, f"{inc0:.3f} -> {inc1:.3f}")
inc0p1 = (mu_C(list(range(1, 1025)), p=1) - mu_C(list(range(1, 513)), p=1))
inc1p1 = (mu_C(list(range(1, 2049)), p=1) - mu_C(list(range(1, 1025)), p=1))
check("T6 p=1 (physical derivative vertex): marginal cost STRICTLY INCREASING "
      "(opposite sign to SAX's diminishing marginal issuance)",
      inc1p1 > inc0p1 * 1.5, f"{inc0p1:.3f} -> {inc1p1:.3f}")

# ======================================= T7: robustness sweep (couplings/states)
print("== T7: verdict stable across couplings, gaps, states ==")
stable = True
rng = lcg(31337)
for g in (0.05, 0.10, 0.20):
    for m2 in (0.20, 0.30, 0.50):
        A, B = random_disjoint_pair(rng)
        for f in (schwartz, lambda k: powerlaw(k, 1.2)):
            def c_strip(k):
                return math.sqrt(cond_eta(r_of(k, g, 0, M1, m2)))
            a = sum((f(k) ** 2) * c_strip(k) for k in A)
            b = sum((f(k) ** 2) * c_strip(k) for k in B)
            ab = sum((f(k) ** 2) * c_strip(k) for k in sorted(A + B))
            stable &= abs(ab - (a + b)) / ab < 1e-12
check("T7 T-A exact additivity at every (G, m2, state) point (18-point sweep)", stable)

# ------------------------------------------------------------------ VERDICT
print()
print("=" * 76)
if not FAILS:
    print("W115 VERDICT: NOT-A-MU-CANDIDATE (E043 discriminator CLASSIFIES the strip cost).")
    print("  - SAX-2 FAILS on the honest per-state typing (T-A/T-B): exactly additive.")
    print("  - SAX-3 FAILS on every typing: mode-identity- and state-dependent,")
    print("    never size-determined.")
    print("  - The sup typing (T-C) is strictly subadditive but DOMINANCE-driven")
    print("    (deficit = min of the sups), not size-concavity: not SAX.")
    print("  - Entropy side: the strip cost sits in the ADDITIVE column of E043's")
    print("    table on independent structures (deficit 0, like entropy there, like")
    print("    action/linear-information always) -- E036's additive family, not P_corr.")
    print("  - Trajectory steelman (T-D): SAX-shaped concavity only at p=0; ADDITIVE")
    print("    at the physical derivative vertex p=1; ANTI-SAX (superadditive) at p>=2;")
    print("    marginal cost INCREASES with UV extension -- opposite to diminishing")
    print("    marginal issuance.")
    print("  D-FORK placement: the strip cost prices FINALIZING existing selections")
    print("  (TI's cost-of-finality route, E140), not issuance of new possibility.")
    print("ALL CHECKS PASS. exit 0")
    sys.exit(0)
else:
    print(f"W115: {len(FAILS)} CHECK(S) FAILED: {FAILS}")
    sys.exit(1)
